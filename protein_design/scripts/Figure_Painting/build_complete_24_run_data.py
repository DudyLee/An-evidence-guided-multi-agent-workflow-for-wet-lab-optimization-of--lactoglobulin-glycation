from __future__ import annotations

import csv
import os
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[3]
RESULT_ROOT = Path(
    os.environ.get("GLYCATION_RAW_WORKBOOK_DIR", REPO_ROOT / "data" / "raw_wetlab_workbooks")
)
OUTPUT_DIR = REPO_ROOT / "protein_design" / "tables" / "wetlab_runsheet"
SUPPLEMENTAL_ELISA = RESULT_ROOT / "ELISA-2026.6.15.xlsx"

COMMON_MODE = "dry"
COMMON_AW = "0.79"
COMMON_RATIO = "1:2 (w/w)"


BASE_RUNS: list[dict[str, object]] = [
    {
        "run_id": "R01",
        "decision_block": "matched hexose bridge",
        "donor": "lactose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 51.66,
        "error_pct": 0.81,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; lactose 55 C 4 h +US",
        "sample_label": "lactose 55 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R02",
        "decision_block": "matched hexose bridge",
        "donor": "glucose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 59.91,
        "error_pct": 2.62,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; glucose 55 C 4 h +US",
        "sample_label": "glucose 55 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R03",
        "decision_block": "matched hexose bridge",
        "donor": "galactose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 59.59,
        "error_pct": 2.33,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; galactose 55 C 4 h +US",
        "sample_label": "galactose 55 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R04",
        "decision_block": "matched hexose bridge",
        "donor": "mannose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 65.40,
        "error_pct": 1.76,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; mannose 55 C 4 h +US",
        "sample_label": "mannose 55 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R05",
        "decision_block": "matched hexose bridge",
        "donor": "lactose",
        "temperature_C": 60,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 56.59,
        "error_pct": 2.57,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; lactose 60 C 4 h +US",
        "sample_label": "lactose 60 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R06",
        "decision_block": "matched hexose bridge",
        "donor": "glucose",
        "temperature_C": 60,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 60.15,
        "error_pct": 1.52,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; glucose 60 C 4 h +US",
        "sample_label": "glucose 60 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R07",
        "decision_block": "matched hexose bridge",
        "donor": "galactose",
        "temperature_C": 60,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 61.31,
        "error_pct": 2.99,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; galactose 60 C 4 h +US",
        "sample_label": "galactose 60 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R08",
        "decision_block": "matched hexose bridge",
        "donor": "mannose",
        "temperature_C": 60,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 68.15,
        "error_pct": 0.69,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; mannose 60 C 4 h +US",
        "sample_label": "mannose 60 C 4 h +US",
        "figure_panel": "Fig. 3a",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R13",
        "decision_block": "benchmark anchor",
        "donor": "lactose",
        "temperature_C": 60,
        "time_h": 2,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 81.52,
        "error_pct": 2.29,
        "source_workbook": "dry_2h_allergenicity_2026-01-21",
        "source_file": "2026.1.21 尾-Lg-绯栧熀鍖?鑷存晱.xlsx",
        "source_sheet_or_label": "鏁版嵁鏁寸悊; lactose 60 C 2 h +US",
        "sample_label": "lactose 60 C 2 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R14",
        "decision_block": "benchmark anchor",
        "donor": "glucose",
        "temperature_C": 60,
        "time_h": 2,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 70.02,
        "error_pct": 3.31,
        "source_workbook": "dry_2h_allergenicity_2026-01-21",
        "source_file": "2026.1.21 尾-Lg-绯栧熀鍖?鑷存晱.xlsx",
        "source_sheet_or_label": "鏁版嵁鏁寸悊; glucose 60 C 2 h +US",
        "sample_label": "glucose 60 C 2 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R15",
        "decision_block": "practical anchor",
        "donor": "lactose",
        "temperature_C": 55,
        "time_h": 3,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 61.63,
        "error_pct": 1.10,
        "source_workbook": "timecourse_2026-03-19",
        "source_file": "2026.3.19-鍗曠硸浜岀硸-绯栧熀鍖?鏁版嵁鏁寸悊.xlsx",
        "source_sheet_or_label": "Sheet1; lactose 55 C 3 h +US",
        "sample_label": "lactose 55 C 3 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R16",
        "decision_block": "practical anchor",
        "donor": "glucose",
        "temperature_C": 55,
        "time_h": 3,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 70.99,
        "error_pct": 1.99,
        "source_workbook": "timecourse_2026-03-19",
        "source_file": "2026.3.19-鍗曠硸浜岀硸-绯栧熀鍖?鏁版嵁鏁寸悊.xlsx",
        "source_sheet_or_label": "Sheet1; glucose 55 C 3 h +US",
        "sample_label": "glucose 55 C 3 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R17",
        "decision_block": "pentose branch",
        "donor": "arabinose",
        "temperature_C": 55,
        "time_h": 2,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 67.50,
        "error_pct": 2.73,
        "source_workbook": "dry_2h_allergenicity_2026-01-21",
        "source_file": "2026.1.21 尾-Lg-绯栧熀鍖?鑷存晱.xlsx",
        "source_sheet_or_label": "鏁版嵁鏁寸悊; arabinose 55 C 2 h +US",
        "sample_label": "arabinose 55 C 2 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R18",
        "decision_block": "pentose branch",
        "donor": "arabinose",
        "temperature_C": 55,
        "time_h": 3,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 74.98,
        "error_pct": 1.41,
        "source_workbook": "timecourse_2026-03-19",
        "source_file": "2026.3.19-鍗曠硸浜岀硸-绯栧熀鍖?鏁版嵁鏁寸悊.xlsx",
        "source_sheet_or_label": "Sheet1; arabinose 55 C 3 h +US",
        "sample_label": "arabinose 55 C 3 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R20",
        "decision_block": "pentose branch",
        "donor": "ribose",
        "temperature_C": 55,
        "time_h": 3,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "reduction_pct_vs_untreated_N": 79.04,
        "error_pct": 0.36,
        "source_workbook": "timecourse_2026-03-19",
        "source_file": "2026.3.19-鍗曠硸浜岀硸-绯栧熀鍖?鏁版嵁鏁寸悊.xlsx",
        "source_sheet_or_label": "Sheet1; ribose 55 C 3 h +US",
        "sample_label": "ribose 55 C 3 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Source table does not print temperature; user confirmed the condition matches.",
    },
    {
        "run_id": "R23",
        "decision_block": "heated no-sugar control",
        "donor": "none",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "yes",
        "reduction_pct_vs_untreated_N": 25.94,
        "error_pct": 3.13,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; no sugar 55 C 4 h +US",
        "sample_label": "no sugar 55 C 4 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Direct match to the planned 24-run condition.",
    },
    {
        "run_id": "R24",
        "decision_block": "heated no-sugar control",
        "donor": "none",
        "temperature_C": 60,
        "time_h": 4,
        "ultrasound": "+US",
        "no_sugar_control": "yes",
        "reduction_pct_vs_untreated_N": 35.97,
        "error_pct": 1.63,
        "source_workbook": "RPBG_4h_2026-03-20",
        "source_file": "2026.3.20-RPBG-4h-绯栧熀鍖?xlsx",
        "source_sheet_or_label": "鏁版嵁澶勭悊; no sugar 60 C 4 h +US",
        "sample_label": "no sugar 60 C 4 h +US",
        "figure_panel": "Fig. 3b",
        "note": "Direct match to the planned 24-run condition.",
    },
]


SUPPLEMENTAL_LABELS: dict[str, dict[str, object]] = {
    "涔崇硸-4h": {
        "run_id": "R09",
        "decision_block": "hexose no-ultrasound sentinel",
        "donor": "lactose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "no US",
        "no_sugar_control": "no",
        "figure_panel": "Fig. 3a",
        "note": "Supplemented from ELISA-2026.6.15.xlsx; user confirmed this label denotes the no-ultrasound 55 C 4 h sentinel.",
    },
    "钁¤悇绯?4h": {
        "run_id": "R10",
        "decision_block": "hexose no-ultrasound sentinel",
        "donor": "glucose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "no US",
        "no_sugar_control": "no",
        "figure_panel": "Fig. 3a",
        "note": "Supplemented from ELISA-2026.6.15.xlsx; user confirmed this label denotes the no-ultrasound 55 C 4 h sentinel.",
    },
    "鍗婁钩绯?4h": {
        "run_id": "R11",
        "decision_block": "hexose no-ultrasound sentinel",
        "donor": "galactose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "no US",
        "no_sugar_control": "no",
        "figure_panel": "Fig. 3a",
        "note": "Supplemented from ELISA-2026.6.15.xlsx; user confirmed this label denotes the no-ultrasound 55 C 4 h sentinel.",
    },
    "鐢橀湶绯?4h": {
        "run_id": "R12",
        "decision_block": "hexose no-ultrasound sentinel",
        "donor": "mannose",
        "temperature_C": 55,
        "time_h": 4,
        "ultrasound": "no US",
        "no_sugar_control": "no",
        "figure_panel": "Fig. 3a",
        "note": "Supplemented from ELISA-2026.6.15.xlsx; user confirmed this label denotes the no-ultrasound 55 C 4 h sentinel.",
    },
    "鏍哥硸-U-2h": {
        "run_id": "R19",
        "decision_block": "pentose branch",
        "donor": "ribose",
        "temperature_C": 55,
        "time_h": 2,
        "ultrasound": "+US",
        "no_sugar_control": "no",
        "figure_panel": "Fig. 3b",
        "note": "Supplemented from ELISA-2026.6.15.xlsx as ribose 55 C 2 h +US.",
    },
    "N-U-2h": {
        "run_id": "R21",
        "decision_block": "heated no-sugar control",
        "donor": "none",
        "temperature_C": 55,
        "time_h": 2,
        "ultrasound": "+US",
        "no_sugar_control": "yes",
        "figure_panel": "Fig. 3b",
        "note": "Supplemented from ELISA-2026.6.15.xlsx as no-sugar 55 C 2 h +US.",
    },
    "N-U-3h": {
        "run_id": "R22",
        "decision_block": "heated no-sugar control",
        "donor": "none",
        "temperature_C": 55,
        "time_h": 3,
        "ultrasound": "+US",
        "no_sugar_control": "yes",
        "figure_panel": "Fig. 3b",
        "note": "Supplemented from ELISA-2026.6.15.xlsx as no-sugar 55 C 3 h +US; the Chinese condition text repeats 2 h, but the sample label and user confirmation specify 3 h.",
    },
}


def read_supplemental_rows() -> list[dict[str, object]]:
    df = pd.read_excel(SUPPLEMENTAL_ELISA, sheet_name="Sheet1", header=None)
    native_row = df[df.iloc[:, 1].eq("N")].iloc[0]
    native_value = float(native_row.iloc[2])
    native_error = float(native_row.iloc[3])

    rows: list[dict[str, object]] = []
    for _, row in df.iloc[2:].iterrows():
        condition_zh = row.iloc[0]
        sample_label = row.iloc[1]
        if pd.isna(sample_label) or sample_label not in SUPPLEMENTAL_LABELS:
            continue
        value = float(row.iloc[2])
        error = float(row.iloc[3])
        reduction = (1 - value / native_value) * 100
        propagated_error = 100 * (
            (error / native_value) ** 2
            + ((value * native_error) / (native_value**2)) ** 2
        ) ** 0.5
        metadata = dict(SUPPLEMENTAL_LABELS[str(sample_label)])
        metadata.update(
            {
                "reduction_pct_vs_untreated_N": reduction,
                "error_pct": propagated_error,
                "source_workbook": "ELISA_2026-06-15",
                "source_file": "ELISA-2026.6.15.xlsx",
                "source_sheet_or_label": f"Sheet1; {sample_label}",
                "sample_label": str(sample_label),
                "source_condition_text": "" if pd.isna(condition_zh) else str(condition_zh),
                "binding_value": value,
                "binding_error": error,
            }
        )
        rows.append(metadata)
    return rows


def complete_rows() -> list[dict[str, object]]:
    rows = [dict(row) for row in BASE_RUNS]
    rows.extend(read_supplemental_rows())
    rows.sort(key=lambda row: int(str(row["run_id"])[1:]))
    for row in rows:
        row["mode"] = COMMON_MODE
        row["aw"] = COMMON_AW
        row["protein_sugar_ratio"] = "none" if row["donor"] == "none" else COMMON_RATIO
        row["result_status"] = "available: direct exact"
    if len(rows) != 24:
        raise RuntimeError(f"Expected 24 runs, found {len(rows)}")
    if len({row["run_id"] for row in rows}) != 24:
        raise RuntimeError("Run identifiers are not unique")
    return rows


def format_number(value: object, digits: int = 2) -> str:
    if value is None or value == "":
        return ""
    return f"{float(value):.{digits}f}"


def normalized_row(row: dict[str, object]) -> dict[str, str]:
    return {
        "run_id": str(row["run_id"]),
        "decision_block": str(row["decision_block"]),
        "donor": str(row["donor"]),
        "temperature_C": str(int(float(row["temperature_C"]))),
        "time_h": str(int(float(row["time_h"]))),
        "ultrasound": str(row["ultrasound"]),
        "mode": str(row["mode"]),
        "aw": str(row["aw"]),
        "protein_sugar_ratio": str(row["protein_sugar_ratio"]),
        "no_sugar_control": str(row["no_sugar_control"]),
        "result_status": str(row["result_status"]),
        "reduction_pct_vs_untreated_N": format_number(row["reduction_pct_vs_untreated_N"]),
        "error_pct": format_number(row["error_pct"]),
        "source_workbook": str(row["source_workbook"]),
        "source_file": str(row["source_file"]),
        "source_sheet_or_label": str(row["source_sheet_or_label"]),
        "sample_label": str(row["sample_label"]),
        "current_figure_panel": str(row["figure_panel"]),
        "note": str(row["note"]),
    }


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def to_markdown(rows: list[dict[str, str]]) -> str:
    columns = [
        "run_id",
        "decision_block",
        "donor",
        "temperature_C",
        "time_h",
        "ultrasound",
        "result_status",
        "reduction_pct_vs_untreated_N",
        "error_pct",
        "source_file",
        "source_sheet_or_label",
        "note",
    ]
    widths = [max(len(col), *(len(row[col]) for row in rows)) for col in columns]
    header = "| " + " | ".join(col.ljust(widths[i]) for i, col in enumerate(columns)) + " |"
    sep = "| " + " | ".join("-" * widths[i] for i in range(len(columns))) + " |"
    body = [
        "| " + " | ".join(row[col].ljust(widths[i]) for i, col in enumerate(columns)) + " |"
        for row in rows
    ]
    return "\n".join([header, sep, *body]) + "\n"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = [normalized_row(row) for row in complete_rows()]

    write_csv(OUTPUT_DIR / "original_24_run_availability_audit.csv", rows)
    write_csv(OUTPUT_DIR / "formal_24_run_result_mapping.csv", rows)
    # Backward-compatible copy for older scripts; contents are now 24-run complete.
    write_csv(OUTPUT_DIR / "formal_17_run_result_mapping.csv", rows)

    md = to_markdown(rows)
    (OUTPUT_DIR / "original_24_run_availability_audit.md").write_text(md, encoding="utf-8")
    (OUTPUT_DIR / "formal_24_run_result_mapping.md").write_text(md, encoding="utf-8")

    print(f"Wrote complete 24-run tables to {OUTPUT_DIR}")
    print("available=24; missing=0; total=24")


if __name__ == "__main__":
    main()
