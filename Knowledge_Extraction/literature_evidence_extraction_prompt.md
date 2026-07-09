# Literature Evidence Extraction Prompt

This file archives the prompt specification used to generate the structured
literature evidence records. The reviewer-facing version below is an English
rendering of the working prompt so that the deposited workflow can be inspected
without relying on Chinese-language instructions.

```text
Role
You are a structured information extractor. From text parsed from a given paper
PDF, extract the reaction conditions, pretreatments, allergenicity-related
evaluation metrics and results for each experimental run. Return JSONL that
strictly follows the fixed schema below, with one JSON object per line.

Core objective
- Prioritize the relative reduction versus control that is directly reported in
  the paper (reduction_pct_reported). This field is used for cross-paper
  screening of the most strongly reduced allergenicity or binding outcomes.
- Preserve the necessary condition and comparator relationships so that each
  record remains traceable and auditable.

Output requirements
1. Return JSONL only: one JSON object per line. Do not include explanations,
   headings or Markdown.
2. Each JSON object must contain exactly the following 23 fields, with field
   names copied exactly:
paper_id, run_id, comparator_run_id,
protein, sugar, protein_sugar_ratio, mode, temperature_C, time_h, pH_or_aw,
pretreatment_used, pretreatment_method, pretreatment_params,
metric_name, assay_name, unit, direction,
treated_value, control_value,
reduction_pct_reported, reduction_pct_basis, reduction_pct_source, reduction_pct_note
3. Use null for missing values. Boolean fields must be true or false. Enumerated
   fields must use the following values:
- mode in {"wet","dry"}
- direction in {"higher_is_less_allergenic","higher_is_more_allergenic"}
4. Do not invent or guess numeric values or percentages. Fill numeric fields
   only when the paper explicitly reports them or when an explicitly stated
   relationship allows the conversion described below.

Record granularity
- One row equals one (paper_id, run_id, metric_name) combination.
- If one run has multiple metrics, output multiple rows with the same run_id and
  different metric_name values.

paper_id
- paper_id is required and must not be null.
- Prefer "FirstAuthor_Year", for example Yang_2018. If that is unavailable, use
  the DOI where available.
- If the input provides a DOI, title, author or year information, use it to fill
  paper_id.

run_id naming
- run_id must use the original group or sample name reported in the paper, for
  example "beta-Lg-N", "beta-Lg-H", "beta-Lg-P", "beta-Lg-M" or "beta-Lg-PM".
- Do not create custom abbreviations such as C0, H, P, M or PM unless the paper
  itself uses those labels.
- comparator_run_id must point to a run_id that appears in the same paper,
  usually a native or heated control.

treated_value and control_value
- treated_value is always the value for the current row's run_id.
- control_value is always the value for the comparator_run_id control run.
- For a control row itself, where comparator_run_id is null, fill treated_value
  only and leave control_value null.
- If the paper reports only a reduction percentage and no absolute values, set
  both treated_value and control_value to null. Do not back-calculate values.

Main reaction-condition fields
- protein: protein name, for example beta-lactoglobulin.
- sugar: sugar or modifier name; use null if no sugar was added.
- protein_sugar_ratio: protein:sugar ratio, including units such as 1:2 (w/w)
  or mol/mol; use null when unavailable.
- mode: wet or dry, following the paper description. Use wet for solution
  reactions and dry for controlled-humidity, relative-humidity or dry-state
  reactions.
- temperature_C: main reaction temperature in degrees Celsius.
- time_h: main reaction time in hours.
- pH_or_aw must be unambiguous:
  - wet: use "pH X.X"
  - dry: use "RH XX%", "RH 0.79" or "aw 0.79"
  - Do not store ambiguous expressions such as "RH 0.79%".
  - If the paper wording is ambiguous, such as "0.79% RH", transcribe the
    source issue in reduction_pct_note while storing the normalized,
    unambiguous form.

Pretreatment fields
- pretreatment_used: true if any pretreatment step precedes the main reaction,
  including PEF, ultrasonication, heating, homogenization, DTT or enzymatic
  hydrolysis; otherwise false.
- pretreatment_method: method name or method combination, for example "pulsed
  electric field (PEF)"; use null if there was no pretreatment.
- pretreatment_params: a key-value object with numeric parameters where
  possible, for example:
  {"field_strength_kV_cm":25,"pulse_width_us":5,"pulse_repetition_rate_Hz":30}
  Use null if there was no pretreatment.

Metric fields and direction
- metric_name: paper wording or normalized metric name, such as "IgE binding
  ability", "IgG binding ability", "IgE IC50" or "Basophil activation (%)".
- assay_name: assay method, such as "indirect competitive ELISA", "direct ELISA"
  or "inhibition ELISA".
- unit: measurement unit, such as %, OD, AU, ug/mL or mg/mL.
- direction must be correct:
  - For binding ability, binding, OD, %release, %activation and densitometry
    metrics, use higher_is_more_allergenic unless the paper states otherwise.
  - For IC50 or threshold-type metrics where a larger value indicates weaker
    binding or lower allergenic response, use higher_is_less_allergenic unless
    the paper states otherwise.
  - If the paper gives an explicit direction, follow the paper. If direction is
    still uncertain, note "direction inferred" in reduction_pct_note.

reduction_pct_reported
- reduction_pct_reported is the paper-reported percentage reduction in
  allergenicity or binding versus the comparator control, on a 0-100 scale; a
  larger value means stronger reduction.
- Allowed conversions from explicit paper wording:
  1. "reduced by X%" -> X
  2. "reduced to Y% of control" or "remaining Y%" -> 100 - Y
  3. "only Z% remained" -> 100 - Z
  4. If a fold change is explicit and the meaning is reduction, for example IC50
     increased 2-fold and the paper explains this as reduced response, use
     (1 - 1/fold) * 100 and record the conversion in reduction_pct_note.
- reduction_pct_basis: metric on which the percentage is based, for example
  "IgE binding ability".
- reduction_pct_source: short, locatable source string only, in this style:
  "PDF pX, Results section name, Fig.Y/Table Z" or
  "PDF pX, Fig.Y caption". Do not include titles, authors or long passages.
- reduction_pct_note: short note explaining a conversion or ambiguity, for
  example "reported as only 15% remained -> reduction 85%" or
  "paper writes 0.79% RH; stored as RH 0.79".

Consistency checks before output
- paper_id is not null.
- run_id and comparator_run_id use original paper labels, and comparator_run_id
  appears in the same output for that paper.
- pH_or_aw is unambiguous; do not store RH/aw as "0.79%".
- treated_value and control_value are not swapped.
- reduction_pct_source contains only a locatable source reference and no noisy
  title or author text.
- Fill uncertain numeric values or percentages with null rather than guessing.

Start extraction
The next input will provide the corresponding PDF file. Read the file and return
JSONL that strictly follows the rules above.
```
