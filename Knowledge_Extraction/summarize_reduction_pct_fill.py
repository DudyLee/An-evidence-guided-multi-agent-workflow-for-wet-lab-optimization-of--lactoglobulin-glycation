"""Summarize which reduction_pct_reported values were newly computed.

Reads the original JSONL and the computed JSONL produced by
Knowledge_Extraction/compute_reduction_pct_reported.py, then reports:
- how many rows were filled
- distribution of filled rows by unit / metric_name / paper_id
- why remaining nulls are not computable (missing treated/control)
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any


def _is_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and not math.isnan(float(value))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--orig", type=Path, default=Path("data/paper_data/Paper_run_data.jsonl"))
    parser.add_argument("--computed", type=Path, default=Path("data/paper_data/Paper_run_data.computed.jsonl"))
    args = parser.parse_args()

    orig_rows = _load_jsonl(args.orig)
    comp_rows = _load_jsonl(args.computed)
    if len(orig_rows) != len(comp_rows):
        raise SystemExit(f"Row count mismatch: orig={len(orig_rows)} computed={len(comp_rows)}")

    filled: list[dict[str, Any]] = []
    still_null: list[dict[str, Any]] = []

    for o, c in zip(orig_rows, comp_rows, strict=True):
        o_v = o.get("reduction_pct_reported")
        c_v = c.get("reduction_pct_reported")
        if o_v is None and _is_number(c_v):
            filled.append(c)
        if c_v is None:
            still_null.append(c)

    print("ORIG:", args.orig)
    print("COMPUTED:", args.computed)
    print("TOTAL:", len(orig_rows))
    print("FILLED_NEW_NUMERIC:", len(filled))
    print("COMPUTED_STILL_NULL:", len(still_null))
    print()

    by_unit = Counter(r.get("unit") for r in filled)
    by_metric = Counter(r.get("metric_name") for r in filled)
    by_paper = Counter(r.get("paper_id") for r in filled)

    def show(counter: Counter, title: str, n: int = 10) -> None:
        print(title)
        for k, v in counter.most_common(n):
            print(f"  {k}: {v}")
        print()

    show(by_unit, "FILLED_BY_UNIT (top 10)")
    show(by_metric, "FILLED_BY_METRIC (top 10)")
    show(by_paper, "FILLED_BY_PAPER (top 10)")

    # Reasons for still nulls
    reason = Counter()
    for r in still_null:
        tv = r.get("treated_value")
        cv = r.get("control_value")
        comp = r.get("comparator_run_id")
        if not _is_number(tv):
            reason["missing_treated_value"] += 1
        elif _is_number(cv):
            # If control exists but still null, that means reducer chose not to compute (should not happen).
            reason["has_control_value_but_uncomputed"] += 1
        elif comp is None:
            reason["missing_control_value_and_no_comparator"] += 1
        else:
            reason["missing_control_value_and_comparator_lookup_failed"] += 1

    print("STILL_NULL_REASONS")
    for k, v in reason.most_common():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
