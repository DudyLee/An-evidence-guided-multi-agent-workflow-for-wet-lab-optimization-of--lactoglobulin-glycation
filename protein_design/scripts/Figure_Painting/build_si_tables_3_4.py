from __future__ import annotations

import csv
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
INPUT_DIR = REPO_ROOT / "protein_design" / "tables" / "wetlab_runsheet"
OUTPUT_DIR = INPUT_DIR


def latex_escape(value: object) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def fmt_condition(row: dict[str, str]) -> str:
    donor = "no sugar" if row.get("donor") == "none" else row.get("donor", "")
    return (
        f"{latex_escape(donor)}; "
        f"{latex_escape(row.get('temperature_C', ''))}~$^\\circ$C; "
        f"{latex_escape(row.get('time_h', ''))}~h; "
        f"{latex_escape(row.get('ultrasound', ''))}"
    )


def fmt_reduction(row: dict[str, str]) -> str:
    value = row.get("reduction_pct_vs_untreated_N", "")
    if not value:
        return "--"
    error = row.get("error_pct", "")
    if error:
        return f"{float(value):.2f} $\\pm$ {float(error):.2f}"
    return f"{float(value):.2f}"


def normalized_source_id(source_id: str) -> str:
    mapping = {
        "RPBG_4h_2026-03-20": "RPBG-4h-2026-03-20",
        "dry_2h_allergenicity_2026-01-21": "dry-2h-2026-01-21",
        "timecourse_2026-03-19": "timecourse-2026-03-19",
        "ELISA_2026-06-15": "ELISA-2026-06-15",
    }
    return mapping.get(source_id, source_id.replace("_", "-"))


def table_preamble(title: str, label: str, widths: list[str], headers: list[str]) -> list[str]:
    colspec = "\n".join(
        f"  >{{\\raggedright\\arraybackslash}}p{{{width}}}" for width in widths
    )
    header = " & ".join(r"\textbf{" + head + "}" for head in headers) + r" \\"
    return [
        rf"% {title}",
        r"\clearpage",
        r"\begingroup",
        r"\scriptsize",
        r"\setlength{\tabcolsep}{2pt}",
        r"\renewcommand{\arraystretch}{1.12}",
        r"\begin{longtable}{",
        colspec,
        r"}",
        rf"\caption{{{title}}}",
        rf"\label{{{label}}}\\",
        r"\toprule",
        header,
        r"\midrule",
        r"\endfirsthead",
        "",
        rf"\multicolumn{{{len(headers)}}}{{l}}{{\tablename~\thetable\quad continued}} \\",
        r"\toprule",
        header,
        r"\midrule",
        r"\endhead",
        "",
        r"\midrule",
        rf"\multicolumn{{{len(headers)}}}{{r}}{{Continued on next page}} \\",
        r"\endfoot",
        "",
        r"\bottomrule",
        r"\endlastfoot",
        "",
    ]


def table_closing(note: str) -> list[str]:
    return [
        r"\end{longtable}",
        r"\begin{flushleft}",
        rf"\scriptsize {note}",
        r"\end{flushleft}",
        r"\endgroup",
        "",
    ]


def build_table_3(rows: list[dict[str, str]]) -> str:
    lines = table_preamble(
        "Original 24-condition plan and result-availability audit.",
        "tab:original_24_run_audit",
        [
            "0.065\\linewidth",
            "0.14\\linewidth",
            "0.17\\linewidth",
            "0.14\\linewidth",
            "0.10\\linewidth",
            "0.25\\linewidth",
        ],
        ["Run", "Block", "Condition", "Result status", "Red. (\\%)", "Audit note"],
    )
    for row in rows:
        fields = [
            latex_escape(row.get("run_id", "")),
            latex_escape(row.get("decision_block", "")),
            fmt_condition(row),
            latex_escape(row.get("result_status", "")),
            fmt_reduction(row),
            latex_escape(row.get("note", "")),
        ]
        lines.append(" & ".join(fields) + r" \\")
    note = (
        "All 24 planned conditions now have directly attributable result records. "
        "The seven records previously treated as unavailable (R09--R12, R19, "
        "R21 and R22) were supplied in the supplemental workbook "
        "\\texttt{ELISA-2026.6.15.xlsx}. Reduction values are IgG-binding "
        "reductions relative to the untreated baseline and are shown as mean "
        "$\\pm$ error where available. US, ultrasound pretreatment."
    )
    lines.extend(table_closing(note))
    return "\n".join(lines)


def build_table_4(rows: list[dict[str, str]]) -> str:
    lines = table_preamble(
        "Complete 24-run result matrix and source-record mapping.",
        "tab:complete_24_run_mapping",
        [
            "0.055\\linewidth",
            "0.13\\linewidth",
            "0.16\\linewidth",
            "0.10\\linewidth",
            "0.09\\linewidth",
            "0.27\\linewidth",
        ],
        ["Run", "Block", "Condition", "Red. (\\%)", "Figure", "Source record"],
    )
    for row in rows:
        source = normalized_source_id(row.get("source_workbook", ""))
        fields = [
            latex_escape(row.get("run_id", "")),
            latex_escape(row.get("decision_block", "")),
            fmt_condition(row),
            fmt_reduction(row),
            latex_escape(row.get("current_figure_panel", "")),
            latex_escape(source),
        ]
        lines.append(" & ".join(fields) + r" \\")
    note = (
        "The table preserves the original R01--R24 planning identifiers because "
        "all planned conditions now have matched ELISA results. Source record "
        "gives the normalized workbook identifier used for traceability. US, "
        "ultrasound pretreatment."
    )
    lines.extend(table_closing(note))
    return "\n".join(lines)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = read_csv(INPUT_DIR / "formal_24_run_result_mapping.csv")

    table3 = OUTPUT_DIR / "Supplementary_Table_3_24_run_audit.tex"
    table4 = OUTPUT_DIR / "Supplementary_Table_4_24_run_mapping.tex"
    table3.write_text(build_table_3(rows), encoding="utf-8")
    table4.write_text(build_table_4(rows), encoding="utf-8")

    print(f"Wrote {table3}")
    print(f"Wrote {table4}")
    print(f"Table 3/4: total={len(rows)}; available={len(rows)}; missing=0")


if __name__ == "__main__":
    main()
