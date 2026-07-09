# Excluded files

This package is a reviewer-facing data/code snapshot, not a full local working
directory clone. The following material was deliberately left out.

## Copyright-restricted literature PDFs

The full-text paper library under `Knowledge_Extraction/papers/` was not copied.
The structured extraction outputs, schema, source locators and harmonized records
are included instead. This avoids redistributing third-party PDFs.

## Vector-store and retrieval caches

`data/paper_data/storage/` was not copied. It contains retrieval/index artifacts
and text chunks derived from source literature. The reviewer-facing structured
evidence files are in `data/paper_data/`.

## Legacy local extraction prototype

`Knowledge_Extraction/schemeA_glycation_extract.py` was excluded from the review
package because it was an older local API prototype with a different schema.
The deposited literature evidence records were generated using the
web-interface prompt archived at
`Knowledge_Extraction/literature_evidence_extraction_prompt.md`.

## Local dependencies and build caches

`node_modules`, `.pnpm`, `__pycache__`, `.pyc` and local dependency caches were
excluded. Dependencies should be installed from package metadata rather than
uploaded as vendored local folders.

## Temporary manuscript build artifacts

LaTeX auxiliary files, PDF render previews, temporary screenshots and working
draft folders were not included. The package keeps manuscript-context excerpts
only where they document the data/code repository scope.

## Unrelated project families

The older SARS-CoV-2 nanobody-design data and code were not copied because this
review package supports the beta-lactoglobulin glycation manuscript only.

## Oversized local inspection artifacts

`glycation_results_organized_2026-06-26.xlsx.inspect.ndjson` was excluded as a
large local inspection dump. The organized workbook, payload JSON, raw cell index
and processed CSV exports are included.
