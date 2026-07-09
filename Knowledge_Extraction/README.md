# Literature Evidence Extraction

This folder documents the literature evidence extraction workflow used for the
review package.

The structured literature records were produced through a web-interface prompt
workflow, not by running a local API extraction script. The original prompt used
for that workflow is archived here:

- `literature_evidence_extraction_prompt.md`

The local legacy prototype `schemeA_glycation_extract.py` is intentionally not
included in this review package because it used an older extraction schema and
was not the workflow used to generate the deposited literature evidence records.

## API Extraction Script

`extract_literature_with_api.py` is a reproducible API implementation of the
archived web-interface prompt. It uploads user-provided PDFs to the OpenAI Files
API with `purpose="user_data"`, passes the uploaded file into the Responses API
as an `input_file`, and validates that every returned JSONL row contains exactly
the 23 archived fields.

Example:

```bash
python Knowledge_Extraction/extract_literature_with_api.py \
  --pdf-dir Knowledge_Extraction/papers \
  --output data/paper_data/api_extracted_paper_run_data.jsonl \
  --log data/paper_data/api_extraction_log.jsonl \
  --overwrite
```

Set `OPENAI_API_KEY` before running. The full-text PDFs are not included in this
review package; users must provide PDFs they have permission to process.

## Deposited Outputs

The reviewer-facing structured outputs are in `data/paper_data/`:

- `Paper_run_data.jsonl`: original schema-controlled JSONL records.
- `Paper_run_data.computed_V2.jsonl`: harmonized records after reduction-field
  completion where explicit treated/control values supported calculation.
- `Paper_run_data.computed_V2.selected_fields_table.csv`: compact tabular
  export for inspection.
- `reduction_pct_fill_summary.txt`: audit summary for newly filled
  `reduction_pct_reported` values.

The full-text PDFs used as source literature are not redistributed in this
package because they are third-party copyrighted material. The extracted records
preserve source locator fields such as PDF page, figure/table location and note
fields where available.

## Post-processing Utility

`summarize_reduction_pct_fill.py` summarizes which missing
`reduction_pct_reported` values were newly filled by comparing original and
computed JSONL files.

Example:

```bash
python Knowledge_Extraction/summarize_reduction_pct_fill.py \
  --orig data/paper_data/Paper_run_data.jsonl \
  --computed data/paper_data/Paper_run_data.computed_V2.jsonl
```

The script reports counts by unit, metric and paper ID, plus why remaining null
values could not be computed.
