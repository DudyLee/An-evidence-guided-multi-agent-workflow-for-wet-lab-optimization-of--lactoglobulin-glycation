# Evidence-guided multi-agent workflow for beta-lactoglobulin glycation

This repository snapshot contains the data and code selected for reviewer access
after manuscript submission. It was assembled on 2026-07-08 from the active
local manuscript and supplementary-information workspaces.

The package follows the "Data and Code Repository Inventory" in the
Supplementary Information. It is intentionally narrower than the full working
directory: old nanobody-design materials, local caches, copyright-restricted
paper PDFs, LaTeX build outputs and temporary rendering files are not included.

## Repository layout

| Path | Contents | Manuscript connection |
| --- | --- | --- |
| `data/Source_Data.xlsx` | Source Data workbook for quantitative main and supplementary figures. | Fig. 2c,d, Fig. 3a-c, Fig. 4a-c and Supplementary Fig. 1. |
| `data/paper_data/` | Structured literature evidence records, computed reduction fields, wet-lab JSONL packets and the completed 24-run matrix. | Literature evidence layer, run-sheet audit, wet-lab results and repository-deposited data. |
| `data/bepipred_data/` | beta-LG variant A input sequence and BepiPred-3.0 residue-level outputs. | Sequence-prior output for Fig. 2c and Source Data. |
| `data/netglycate_data/` | beta-LG variant A input sequence and NetGlycate lysine-level output. | Sequence-prior output for Fig. 2d and Source Data. |
| `data/agent_prompts_meetings_decisions/` | Curated prompt archive, retained discussion records and locked recommendation record. | Agent prompts, meetings and decision records described in Supplementary Methods 1, 3, 4 and 5. |
| `protein_design/tables/` | Processed wet-lab CSV/JSON exports, cell-level index, run-sheet mappings, audit tables and feedback-locking tables. | Supplementary Tables 3-6 and processed wet-lab data. |
| `protein_design/figures/` | Final plotted figure files plus panel-level CSV/JSON source data. | Reproduction and inspection of Fig. 2c,d, Fig. 3, Fig. 4 and supplementary wet-lab landscape plots. |
| `protein_design/scripts/` | Analysis, data-organization, plotting and Source Data workbook scripts. | Code used to generate processed tables, plots and the Source Data workbook. |
| `Knowledge_Extraction/` | Original web-interface literature extraction prompt, PDF-to-JSONL API reproduction script, deposited-output notes and reduction-fill audit script. | Structured evidence extraction workflow. |
| `src/virtual_lab/` | Virtual Lab meeting framework code, including direct JSONL context builders for literature and wet-lab records. | Human-agent meeting workflow, role-specialized discussions and repository-backed evidence reading. |

## Key data files

- `data/paper_data/Paper_run_data.computed_V2.jsonl`: harmonized structured
  literature evidence with computed reduction-oriented fields.
- `data/paper_data/Paper_run_data.computed_V2.selected_fields_table.csv`:
  compact tabular export of the structured evidence.
- `data/paper_data/condition_envelope_grouped_levels.csv`: grouped axis counts
  and calculation used for the 1,123,584 literature-derived condition envelope.
- `data/paper_data/24_run_condition_result_matrix.xlsx`: completed R01-R24
  condition/result matrix.
- `protein_design/tables/glycation_results_organized/raw_cell_index.csv`:
  cell-level index from the organized wet-lab workbook.
- `protein_design/tables/glycation_results_organized/long_timecourse.csv` and
  `ribose_validation.csv`: donor-time and validation data used in Source Data.
- `data/agent_prompts_meetings_decisions/agent_prompt_decision_archive.zip`:
  compressed version of the retained prompt, meeting and decision archive.

## Code notes

Python package metadata is in `pyproject.toml`. For figure/table scripts, install
the review dependencies:

```bash
python -m pip install -r requirements-review.txt
```

Most figure scripts assume this repository root as their working tree and use
paths such as `data/...` and `protein_design/figures/...`.

The repository-backed literature and wet-lab context builder is provided at
`src/virtual_lab/context_builder.py`. It reads the structured JSONL files under
`data/paper_data/` directly and does not require the excluded vector-store cache.

The Source Data workbook is already included at `data/Source_Data.xlsx`.
The builder script is included at
`protein_design/scripts/source_data_build/build_source_data_workbook.mjs` and
has been adjusted to use package-relative paths. It requires Node.js and the
`@oai/artifact-tool` workbook library used during manuscript preparation.
