from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


def _is_number(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and not math.isnan(float(v))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def _find_repo_root(start: Path | None = None) -> Path:
    start = (start or Path.cwd()).resolve()
    for p in (start, *start.parents):
        if (p / "pyproject.toml").exists() and (p / "data" / "paper_data").exists():
            return p
    for p in (start, *start.parents):
        if (p / "data" / "paper_data").exists():
            return p
    return start


def _norm_str(v: Any) -> str:
    return "" if v is None else str(v).strip().lower()


def _metric_bucket(r: dict[str, Any]) -> str | None:
    metric = _norm_str(r.get("metric_name"))
    assay = _norm_str(r.get("assay_name"))
    hay = f"{metric} {assay}"

    if "ige" in hay:
        return "IgE"
    if "allergenicity" in hay or "allergenic" in hay:
        return "Allergenicity"
    if "antigenicity" in hay:
        return "Antigenicity"
    if "igg" in hay:
        return "IgG"
    return None


def _is_blg_row(r: dict[str, Any]) -> bool:
    protein = _norm_str(r.get("protein"))
    if not protein:
        return True
    return ("lactoglobulin" in protein) or ("beta-lg" in protein) or ("blg" in protein) or ("β-lg" in protein)


def _time_h_value(r: dict[str, Any]) -> float | None:
    t = r.get("time_h")
    if _is_number(t):
        return float(t)
    return None


def _fmt(v: Any) -> str:
    return "?" if v is None else str(v)


def _metric_priority(bucket: str | None) -> float:
    if bucket in ("IgE", "Allergenicity"):
        return 2.0
    if bucket in ("IgG", "Antigenicity"):
        return 1.5
    return 0.0


def _top_k_max(counter: Counter[str], k: int = 8) -> str:
    pairs = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)[:k]
    return "\n".join([f"- {name}: max_reduction={val:.2f}%" for name, val in pairs])


def _row_line_with_metric(r: dict[str, Any]) -> str:
    bucket = _metric_bucket(r) or _fmt(r.get("metric_name"))
    return " | ".join(
        [
            f"paper={_fmt(r.get('paper_id'))}",
            f"run={_fmt(r.get('run_id'))}",
            f"metric={bucket}: {_fmt(r.get('metric_name'))} ({_fmt(r.get('unit'))})",
            f"reduction={float(r['reduction_pct_reported']):.2f}%",
            f"sugar={_fmt(r.get('sugar'))}",
            f"ratio={_fmt(r.get('protein_sugar_ratio'))}",
            f"mode={_fmt(r.get('mode'))}",
            f"T={_fmt(r.get('temperature_C'))}C",
            f"time={_fmt(r.get('time_h'))}h",
            f"pH/aw={_fmt(r.get('pH_or_aw'))}",
            f"pretreat={_fmt(r.get('pretreatment_method')) if r.get('pretreatment_used') else 'none'}",
            f"treated={_fmt(r.get('treated_value'))}",
            f"control={_fmt(r.get('control_value'))}",
            f"source={_fmt(r.get('reduction_pct_source'))}",
        ]
    )


def _row_line_without_metric(r: dict[str, Any]) -> str:
    pretreat = _fmt(r.get("pretreatment_method")) if r.get("pretreatment_used") else "none"
    return " | ".join(
        [
            f"paper={_fmt(r.get('paper_id'))}",
            f"run={_fmt(r.get('run_id'))}",
            f"reduction={float(r['reduction_pct_reported']):.2f}%",
            f"sugar={_fmt(r.get('sugar'))}",
            f"ratio={_fmt(r.get('protein_sugar_ratio'))}",
            f"mode={_fmt(r.get('mode'))}",
            f"T={_fmt(r.get('temperature_C'))}C",
            f"time={_fmt(r.get('time_h'))}h",
            f"pH/aw={_fmt(r.get('pH_or_aw'))}",
            f"pretreat={pretreat}",
            f"source={_fmt(r.get('reduction_pct_source'))}",
        ]
    )


def _compact_json_for_context(r: dict[str, Any]) -> dict[str, Any]:
    return {
        "paper_id": r.get("paper_id"),
        "run_id": r.get("run_id"),
        "comparator_run_id": r.get("comparator_run_id"),
        "protein": r.get("protein"),
        "sugar": r.get("sugar"),
        "protein_sugar_ratio": r.get("protein_sugar_ratio"),
        "mode": r.get("mode"),
        "temperature_C": r.get("temperature_C"),
        "time_h": r.get("time_h"),
        "pH_or_aw": r.get("pH_or_aw"),
        "pretreatment_used": r.get("pretreatment_used"),
        "pretreatment_method": r.get("pretreatment_method"),
        "pretreatment_params": r.get("pretreatment_params"),
        "reduction_pct_reported": r.get("reduction_pct_reported"),
        "reduction_pct_basis": r.get("reduction_pct_basis"),
        "reduction_pct_source": r.get("reduction_pct_source"),
        "reduction_pct_note": r.get("reduction_pct_note"),
    }


def _build_contexts(*, include_metric: bool, background_prompt: str = "", target_time_h_soft: float = 12.0) -> dict[str, Any]:
    _ = background_prompt  # reserved for compatibility with notebook call sites

    repo_root = _find_repo_root()
    data_dir = repo_root / "data" / "paper_data"

    candidates = [
        data_dir / "Paper_run_data.computed_V2.jsonl",
        data_dir / "Paper_run_data.computed.jsonl",
        data_dir / "Paper_run_data.jsonl",
    ]
    paper_run_data_path = next((p for p in candidates if p.exists()), candidates[-1])
    if not paper_run_data_path.exists():
        raise FileNotFoundError(f"Paper run data not found under: {data_dir}")

    paper_rows = _load_jsonl(paper_run_data_path)

    wetlab_data_path = data_dir / "wetlab_data_3.5.jsonl"
    wetlab_rows = _load_jsonl(wetlab_data_path) if wetlab_data_path.exists() else []

    blg_rows = [r for r in paper_rows if _is_blg_row(r)]
    allergen_rows = [r for r in blg_rows if _metric_bucket(r) in ("IgE", "Allergenicity", "Antigenicity", "IgG")]
    numeric_rows = [r for r in allergen_rows if _is_number(r.get("reduction_pct_reported"))]

    candidate_rows = [
        r
        for r in numeric_rows
        if float(r["reduction_pct_reported"]) > 0 and _metric_bucket(r) in ("IgE", "Allergenicity", "Antigenicity", "IgG")
    ]

    short_time_rows = [r for r in candidate_rows if (_time_h_value(r) is not None and _time_h_value(r) < target_time_h_soft)]
    long_time_rows = [r for r in candidate_rows if (_time_h_value(r) is not None and _time_h_value(r) >= target_time_h_soft)]
    unknown_time_rows = [r for r in candidate_rows if (_time_h_value(r) is None)]

    def _sort_key(r: dict[str, Any]) -> tuple[float, float]:
        bucket = _metric_bucket(r)
        return (_metric_priority(bucket), float(r.get("reduction_pct_reported") or float("-inf")))

    top_candidate_rows = sorted(candidate_rows, key=_sort_key, reverse=True)[:30]
    top_short_time_rows = sorted(short_time_rows, key=_sort_key, reverse=True)[:20]
    top_long_time_rows = sorted(long_time_rows, key=_sort_key, reverse=True)[:10]
    top_unknown_time_rows = sorted(unknown_time_rows, key=_sort_key, reverse=True)[:10]

    by_sugar_max: Counter[str] = Counter()
    by_pretreat_max: Counter[str] = Counter()
    by_mode_max: Counter[str] = Counter()
    by_time_band_max: Counter[str] = Counter()

    for r in candidate_rows:
        red = float(r["reduction_pct_reported"])
        sugar = r.get("sugar") or "(none)"
        pretreat = r.get("pretreatment_method") or ("none" if not r.get("pretreatment_used") else "(unspecified)")
        mode = r.get("mode") or "(unknown mode)"
        time_h = _time_h_value(r)

        if time_h is None:
            time_band = "unknown"
        elif time_h < target_time_h_soft:
            time_band = f"<{target_time_h_soft:.0f}h"
        else:
            time_band = f">={target_time_h_soft:.0f}h"

        by_sugar_max[sugar] = max(by_sugar_max.get(sugar, float("-inf")), red)
        by_pretreat_max[pretreat] = max(by_pretreat_max.get(pretreat, float("-inf")), red)
        by_mode_max[mode] = max(by_mode_max.get(mode, float("-inf")), red)
        by_time_band_max[time_band] = max(by_time_band_max.get(time_band, float("-inf")), red)

    row_formatter = _row_line_with_metric if include_metric else _row_line_without_metric

    top_candidate_lines = [row_formatter(r) for r in top_candidate_rows]
    top_short_time_lines = [row_formatter(r) for r in top_short_time_rows]
    top_long_time_lines = [row_formatter(r) for r in top_long_time_rows]
    top_unknown_time_lines = [row_formatter(r) for r in top_unknown_time_rows]

    if include_metric:
        paper_only_context = "\n".join(
            [
                "You are given a structured extraction dataset from literature (JSONL).",
                f"Path: {paper_run_data_path.as_posix()}",
                f"Records: {len(paper_rows)} total; BLG-related: {len(blg_rows)}; allergenicity-proxy rows: {len(allergen_rows)}; with numeric reductions: {len(numeric_rows)}.",
                "",
                "Optimization goal for this run (literature stage):",
                "- Primary: reduce BLG allergenicity, prioritizing IgE binding (then Antigenicity).",
                f"- Strong-claim constraint: only treat schemes with known time_h <= {target_time_h_soft:.0f}h as compliant evidence.",
                "",
                "Interpretation note: reduction_pct_reported is a % improvement vs control; negative means worse than control.",
                "",
                "Top candidate evidence (IgE/Antigenicity, reduction>0):",
                ("\n".join(top_candidate_lines) if top_candidate_lines else "(none found in dataset)"),
                "",
                f"Subset with time_h < {target_time_h_soft:.0f}h (preferred for compliant evidence):",
                ("\n".join(top_short_time_lines) if top_short_time_lines else "(none)"),
                "",
                f"Subset with time_h >= {target_time_h_soft:.0f}h (possible stronger AGE risk):",
                ("\n".join(top_long_time_lines) if top_long_time_lines else "(none)"),
                "",
                "Subset with missing time_h (needs paper verification):",
                ("\n".join(top_unknown_time_lines) if top_unknown_time_lines else "(none)"),
                "",
                "Best observed max reduction by sugar donor (literature-extracted):",
                (_top_k_max(by_sugar_max, 8) or "(none)"),
                "",
                "Best observed max reduction by pretreatment (literature-extracted):",
                (_top_k_max(by_pretreat_max, 8) or "(none)"),
                "",
                "Best observed max reduction by reaction mode (literature-extracted):",
                (_top_k_max(by_mode_max, 6) or "(none)"),
                "",
                "Best observed max reduction by time band (literature-extracted):",
                (_top_k_max(by_time_band_max, 6) or "(none)"),
            ]
        )

        wetlab_only_context = "\n".join(
            [
                "You are given a HIGH-CONFIDENCE wet-lab dataset that must be read directly and treated separately from literature extraction data.",
                f"Wet-lab path: {wetlab_data_path.as_posix()}",
                f"Wet-lab records: {len(wetlab_rows)}",
                "",
                "Evidence priority note:",
                "- When wet-lab data conflicts with literature-extracted data, prefer wet-lab data and explain the discrepancy.",
                "",
                "HIGH-CONFIDENCE WET-LAB DATA (direct read, separate evidence tier):",
                ("\n".join([json.dumps(r, ensure_ascii=False) for r in wetlab_rows]) if wetlab_rows else "(wetlab file missing or empty)"),
            ]
        )
    else:
        paper_only_context = "\n".join(
            [
                "You are given a structured extraction dataset from literature (JSONL).",
                f"Path: {paper_run_data_path.as_posix()}",
                f"Records: {len(paper_rows)} total; BLG-related: {len(blg_rows)}; allergenicity-proxy rows: {len(allergen_rows)}; with numeric reductions: {len(numeric_rows)}.",
                "",
                "For this stage, discuss ONLY reduction_pct_reported as the outcome of interest.",
                "Do NOT discuss metric_name, assay_name, unit, treated_value, or control_value, even if they exist in the raw dataset.",
                "",
                "Optimization goal for this run (literature stage):",
                "- Primary: identify condition patterns associated with larger reduction_pct_reported.",
                f"- Strong-claim constraint: only treat schemes with known time_h <= {target_time_h_soft:.0f}h as compliant evidence.",
                "",
                "Interpretation note: reduction_pct_reported is a % improvement vs control; negative means worse than control.",
                "",
                "Top candidate evidence (sorted by priority and reduction):",
                ("\n".join(top_candidate_lines) if top_candidate_lines else "(none found in dataset)"),
                "",
                f"Subset with time_h < {target_time_h_soft:.0f}h (preferred for compliant evidence):",
                ("\n".join(top_short_time_lines) if top_short_time_lines else "(none)"),
                "",
                f"Subset with time_h >= {target_time_h_soft:.0f}h (possible stronger AGE risk):",
                ("\n".join(top_long_time_lines) if top_long_time_lines else "(none)"),
                "",
                "Subset with missing time_h (needs paper verification):",
                ("\n".join(top_unknown_time_lines) if top_unknown_time_lines else "(none)"),
                "",
                "Best observed max reduction by sugar donor:",
                (_top_k_max(by_sugar_max, 8) or "(none)"),
                "",
                "Best observed max reduction by pretreatment:",
                (_top_k_max(by_pretreat_max, 8) or "(none)"),
                "",
                "Best observed max reduction by reaction mode:",
                (_top_k_max(by_mode_max, 6) or "(none)"),
                "",
                "Best observed max reduction by time band:",
                (_top_k_max(by_time_band_max, 6) or "(none)"),
                "",
                "Compact literature records for context (metric/assay hidden):",
                "\n".join(json.dumps(_compact_json_for_context(r), ensure_ascii=False) for r in candidate_rows) if candidate_rows else "(none)",
            ]
        )

        wetlab_only_context = "\n".join(
            [
                "You are also given a HIGH-CONFIDENCE wet-lab dataset that must be read directly and treated separately from literature extraction data.",
                f"Wet-lab path: {wetlab_data_path.as_posix()}",
                f"Wet-lab records: {len(wetlab_rows)}",
                "",
                "Evidence priority note:",
                "- When wet-lab data conflicts with literature-extracted data, prefer wet-lab data and explain the discrepancy.",
                "",
                "For the main discussion, still focus on reduction_pct_reported and condition fields only.",
                "Do NOT discuss metric_name, assay_name, unit, treated_value, or control_value unless explicitly requested later.",
                "",
                "HIGH-CONFIDENCE WET-LAB DATA (compact fields only):",
                ("\n".join(json.dumps(_compact_json_for_context(r), ensure_ascii=False) for r in wetlab_rows) if wetlab_rows else "(wetlab file missing or empty)"),
            ]
        )

        paper_plus_wetlab_context = "\n".join(
            [
                paper_only_context,
                "",
                wetlab_only_context,
            ]
        )

        return {
            "REPO_ROOT": repo_root,
            "DATA_DIR": data_dir,
            "paper_run_data_path": paper_run_data_path,
            "paper_rows": paper_rows,
            "wetlab_data_path": wetlab_data_path,
            "wetlab_rows": wetlab_rows,
            "TARGET_TIME_H_SOFT": target_time_h_soft,
            "blg_rows": blg_rows,
            "allergen_rows": allergen_rows,
            "numeric_rows": numeric_rows,
            "candidate_rows": candidate_rows,
            "short_time_rows": short_time_rows,
            "long_time_rows": long_time_rows,
            "unknown_time_rows": unknown_time_rows,
            "top_candidate_rows": top_candidate_rows,
            "top_short_time_rows": top_short_time_rows,
            "top_long_time_rows": top_long_time_rows,
            "top_unknown_time_rows": top_unknown_time_rows,
            "top_candidate_lines": top_candidate_lines,
            "top_short_time_lines": top_short_time_lines,
            "top_long_time_lines": top_long_time_lines,
            "top_unknown_time_lines": top_unknown_time_lines,
            "by_sugar_max": by_sugar_max,
            "by_pretreat_max": by_pretreat_max,
            "by_mode_max": by_mode_max,
            "by_time_band_max": by_time_band_max,
            "paper_only_context": paper_only_context,
            "wetlab_only_context": wetlab_only_context,
            "paper_plus_wetlab_context": paper_plus_wetlab_context,
            "literature_review_contexts_stage1": (paper_only_context,),
            "literature_review_contexts_stage2": (paper_plus_wetlab_context,),
            "literature_review_contexts_wetlab_only": (wetlab_only_context,),
        }

    paper_plus_wetlab_context = "\n".join([paper_only_context, "", wetlab_only_context])

    return {
        "REPO_ROOT": repo_root,
        "DATA_DIR": data_dir,
        "paper_run_data_path": paper_run_data_path,
        "paper_rows": paper_rows,
        "wetlab_data_path": wetlab_data_path,
        "wetlab_rows": wetlab_rows,
        "TARGET_TIME_H_SOFT": target_time_h_soft,
        "blg_rows": blg_rows,
        "allergen_rows": allergen_rows,
        "numeric_rows": numeric_rows,
        "candidate_rows": candidate_rows,
        "short_time_rows": short_time_rows,
        "long_time_rows": long_time_rows,
        "unknown_time_rows": unknown_time_rows,
        "top_candidate_rows": top_candidate_rows,
        "top_short_time_rows": top_short_time_rows,
        "top_long_time_rows": top_long_time_rows,
        "top_unknown_time_rows": top_unknown_time_rows,
        "top_candidate_lines": top_candidate_lines,
        "top_short_time_lines": top_short_time_lines,
        "top_long_time_lines": top_long_time_lines,
        "top_unknown_time_lines": top_unknown_time_lines,
        "by_sugar_max": by_sugar_max,
        "by_pretreat_max": by_pretreat_max,
        "by_mode_max": by_mode_max,
        "by_time_band_max": by_time_band_max,
        "paper_only_context": paper_only_context,
        "wetlab_only_context": wetlab_only_context,
        "paper_plus_wetlab_context": paper_plus_wetlab_context,
        "literature_review_contexts_stage1": (paper_only_context,),
        "literature_review_contexts_stage2": (paper_plus_wetlab_context,),
        "literature_review_contexts_wetlab_only": (wetlab_only_context,),
    }


def build_contexts_with_metric(*, background_prompt: str = "", target_time_h_soft: float = 12.0) -> dict[str, Any]:
    return _build_contexts(include_metric=True, background_prompt=background_prompt, target_time_h_soft=target_time_h_soft)


def build_contexts_without_metric(*, background_prompt: str = "", target_time_h_soft: float = 12.0) -> dict[str, Any]:
    return _build_contexts(include_metric=False, background_prompt=background_prompt, target_time_h_soft=target_time_h_soft)


def build_jsonl_context(
    *,
    file_path: str | Path,
    where: dict[str, Any] | None = None,
    max_records: int | None = None,
    title: str | None = None,
) -> str:
    """Build a compact context string from one JSONL file.

    Inputs are intentionally simple:
    - file_path: JSONL file path (absolute or repo-relative)
    - where: optional filter conditions
      - exact match: {"mode": "dry"}
      - membership: {"sugar": ["arabinose", "xylose"]}
      - callable predicate: {"time_h": lambda v: v is not None and v <= 12}
    - max_records: optional cap after filtering

    Output:
    - one context string that can be passed to meeting contexts.
    """
    path = Path(file_path)
    if not path.is_absolute():
        path = _find_repo_root() / path
    if not path.exists():
        raise FileNotFoundError(f"JSONL file not found: {path}")

    where = where or {}

    def _matches(row: dict[str, Any]) -> bool:
        for key, expected in where.items():
            value = row.get(key)
            if callable(expected):
                if not expected(value):
                    return False
            elif isinstance(expected, (list, tuple, set)):
                if value not in expected:
                    return False
            else:
                if value != expected:
                    return False
        return True

    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if not _matches(row):
                continue
            rows.append(row)
            if max_records is not None and len(rows) >= max_records:
                break

    header = title or path.name
    return "\n".join(
        [
            f"CONTEXT: {header}",
            f"path: {path.as_posix()}",
            f"filters: {where if where else '{}'}",
            f"records: {len(rows)}",
            "",
            *[json.dumps(r, ensure_ascii=False) for r in rows],
        ]
    )
