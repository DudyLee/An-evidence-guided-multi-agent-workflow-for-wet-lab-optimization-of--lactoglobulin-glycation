"""Extract literature evidence records from PDFs using the archived prompt.

This script reproduces the web-interface extraction workflow with the OpenAI
Responses API. It uploads each user-provided PDF as model input, asks the model
to apply the archived 23-field prompt, validates the JSONL shape, and writes a
combined JSONL output plus per-PDF raw responses for auditing.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED_FIELDS = [
    "paper_id",
    "run_id",
    "comparator_run_id",
    "protein",
    "sugar",
    "protein_sugar_ratio",
    "mode",
    "temperature_C",
    "time_h",
    "pH_or_aw",
    "pretreatment_used",
    "pretreatment_method",
    "pretreatment_params",
    "metric_name",
    "assay_name",
    "unit",
    "direction",
    "treated_value",
    "control_value",
    "reduction_pct_reported",
    "reduction_pct_basis",
    "reduction_pct_source",
    "reduction_pct_note",
]
EXPECTED_FIELD_SET = set(EXPECTED_FIELDS)


def _script_dir() -> Path:
    return Path(__file__).resolve().parent


def default_prompt_path() -> Path:
    return _script_dir() / "literature_evidence_extraction_prompt.md"


def load_prompt(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"```(?:text)?\s*(.*?)\s*```", text, flags=re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def iter_pdfs(pdf_inputs: list[Path], pdf_dir: Path | None) -> list[Path]:
    pdfs: list[Path] = []
    for pdf in pdf_inputs:
        if not pdf.exists():
            raise FileNotFoundError(pdf)
        if pdf.suffix.lower() != ".pdf":
            raise ValueError(f"Not a PDF: {pdf}")
        pdfs.append(pdf)

    if pdf_dir is not None:
        if not pdf_dir.exists():
            raise FileNotFoundError(pdf_dir)
        pdfs.extend(sorted(pdf_dir.glob("*.pdf")))

    # Preserve first occurrence while avoiding duplicate work.
    seen: set[Path] = set()
    unique: list[Path] = []
    for pdf in pdfs:
        resolved = pdf.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def response_text(response: Any) -> str:
    if getattr(response, "output_text", None):
        return str(response.output_text)

    chunks: list[str] = []
    for block in getattr(response, "output", []) or []:
        for content in getattr(block, "content", []) or []:
            text = getattr(content, "text", None)
            if text:
                chunks.append(str(getattr(text, "value", text)))
    return "\n".join(chunks)


def strip_code_fence(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:jsonl|json|text)?\s*", "", stripped, count=1)
        stripped = re.sub(r"\s*```$", "", stripped, count=1)
    return stripped.strip()


def parse_jsonl(text: str, source_name: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cleaned = strip_code_fence(text)
    for line_no, line in enumerate(cleaned.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{source_name}: line {line_no} is not valid JSON: {exc}") from exc
        if not isinstance(row, dict):
            raise ValueError(f"{source_name}: line {line_no} is not a JSON object")
        keys = set(row)
        if keys != EXPECTED_FIELD_SET:
            missing = sorted(EXPECTED_FIELD_SET - keys)
            extra = sorted(keys - EXPECTED_FIELD_SET)
            raise ValueError(
                f"{source_name}: line {line_no} does not match the 23-field schema; "
                f"missing={missing}; extra={extra}"
            )
        rows.append(row)
    return rows


def build_instruction(prompt: str, pdf_path: Path) -> str:
    return (
        f"{prompt}\n\n"
        "[API workflow note]\n"
        "The attached input_file is the PDF to extract. Use the PDF text, tables, "
        "figures and captions where available. Use the filename only as a fallback "
        f"paper_id hint: {pdf_path.stem}. Output JSONL only."
    )


def write_jsonl(path: Path, rows: list[dict[str, Any]], append: bool) -> None:
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        for row in rows:
            ordered = {field: row.get(field) for field in EXPECTED_FIELDS}
            handle.write(json.dumps(ordered, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_log(path: Path, record: dict[str, Any], append: bool = True) -> None:
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def create_response(client: Any, model: str, file_id: str, detail: str, instruction: str, temperature: float | None) -> Any:
    kwargs: dict[str, Any] = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_file", "file_id": file_id, "detail": detail},
                    {"type": "input_text", "text": instruction},
                ],
            }
        ],
    }
    if temperature is not None:
        kwargs["temperature"] = temperature
    return client.responses.create(**kwargs)


def extract_one_pdf(
    client: Any,
    pdf_path: Path,
    prompt: str,
    model: str,
    detail: str,
    temperature: float | None,
    raw_dir: Path,
    keep_uploaded_files: bool,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    uploaded = None
    try:
        with pdf_path.open("rb") as handle:
            uploaded = client.files.create(file=handle, purpose="user_data")

        instruction = build_instruction(prompt, pdf_path)
        response = create_response(
            client=client,
            model=model,
            file_id=uploaded.id,
            detail=detail,
            instruction=instruction,
            temperature=temperature,
        )
        text = response_text(response)
        raw_path = raw_dir / f"{pdf_path.stem}.raw_response.txt"
        raw_path.write_text(text, encoding="utf-8")

        rows = parse_jsonl(text, pdf_path.name)
        log = {
            "pdf": str(pdf_path),
            "file_id": uploaded.id,
            "model": model,
            "detail": detail,
            "raw_response": str(raw_path),
            "row_count": len(rows),
            "response_id": getattr(response, "id", None),
        }
        return rows, log
    finally:
        if uploaded is not None and not keep_uploaded_files:
            try:
                client.files.delete(uploaded.id)
            except Exception as exc:  # noqa: BLE001
                print(f"Warning: could not delete uploaded file {uploaded.id}: {exc}", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", action="append", default=[], type=Path, help="PDF file to extract; may be repeated.")
    parser.add_argument("--pdf-dir", type=Path, help="Directory containing PDF files to extract.")
    parser.add_argument("--prompt", type=Path, default=default_prompt_path(), help="Archived extraction prompt file.")
    parser.add_argument("--output", type=Path, default=Path("data/paper_data/api_extracted_paper_run_data.jsonl"))
    parser.add_argument("--log", type=Path, default=Path("data/paper_data/api_extraction_log.jsonl"))
    parser.add_argument("--raw-dir", type=Path, default=Path("data/paper_data/api_raw_responses"))
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--detail", choices=["low", "high"], default="high")
    parser.add_argument("--temperature", type=float, default=None)
    parser.add_argument("--api-key-env", default="OPENAI_API_KEY")
    parser.add_argument("--base-url", default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--continue-on-error", action="store_true")
    parser.add_argument("--keep-uploaded-files", action="store_true")
    args = parser.parse_args()

    if not os.getenv(args.api_key_env):
        raise SystemExit(f"Missing API key environment variable: {args.api_key_env}")

    pdfs = iter_pdfs(args.pdf, args.pdf_dir)
    if not pdfs:
        raise SystemExit("No PDF files provided. Use --pdf or --pdf-dir.")

    if args.output.exists() and not args.overwrite:
        raise SystemExit(f"Output exists; pass --overwrite to replace: {args.output}")

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit("Missing dependency: install the `openai` Python package.") from exc

    prompt = load_prompt(args.prompt)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.log.parent.mkdir(parents=True, exist_ok=True)
    args.raw_dir.mkdir(parents=True, exist_ok=True)

    if args.overwrite:
        args.output.write_text("", encoding="utf-8")
        args.log.write_text("", encoding="utf-8")

    client_kwargs: dict[str, Any] = {"api_key": os.environ[args.api_key_env]}
    if args.base_url:
        client_kwargs["base_url"] = args.base_url
    client = OpenAI(**client_kwargs)

    total_rows = 0
    append_output = not args.overwrite
    append_log = not args.overwrite

    for pdf_path in pdfs:
        print(f"Extracting {pdf_path.name} ...", file=sys.stderr)
        try:
            rows, log = extract_one_pdf(
                client=client,
                pdf_path=pdf_path,
                prompt=prompt,
                model=args.model,
                detail=args.detail,
                temperature=args.temperature,
                raw_dir=args.raw_dir,
                keep_uploaded_files=args.keep_uploaded_files,
            )
            write_jsonl(args.output, rows, append=append_output)
            write_log(args.log, log, append=append_log)
            append_output = True
            append_log = True
            total_rows += len(rows)
        except Exception as exc:  # noqa: BLE001
            error_log = {"pdf": str(pdf_path), "error": str(exc), "model": args.model}
            write_log(args.log, error_log, append=append_log)
            append_log = True
            if not args.continue_on_error:
                raise
            print(f"ERROR extracting {pdf_path.name}: {exc}", file=sys.stderr)

    print(f"Wrote {total_rows} JSONL rows to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
