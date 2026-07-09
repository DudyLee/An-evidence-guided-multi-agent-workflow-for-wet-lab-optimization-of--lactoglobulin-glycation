## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

### Agenda

Convert the already approved dry-only experimental design for β-LG variant A glycation into a **directly executable wet-lab run-sheet package**. The goal is not to revisit strategy, but to produce a **run-by-run, parameter-complete, operationally clear experiment list** for the wet-lab team, including fixed variables, scanned variables, explicit dry-state conditions, controls, replicates, batching, assay assignments, and execution notes. The round remains restricted to **dry-state observed β-LG IgE-binding reduction**, with explicit attention to interpretability and the time-versus-severity tradeoff.

---

### Team Member Input

#### Principal Investigator
- Framed the meeting as an **execution-clarification exercise**, not a design debate.
- Identified the main risk as **execution ambiguity**, especially unresolved placeholders such as:
  - ratio convention,
  - aw/RH implementation,
  - ultrasound wording.
- Proposed that the final package should likely contain:
  - **24 explicit runs**,
  - block IDs,
  - scientific purpose,
  - matched comparison grouping,
  - assay assignments,
  - and structured naming.
- Asked each team member to focus on execution readiness in their domain.

#### Maillard Reaction Chemistry and Process Scientist
- Strongly agreed that the main remaining issue is **operational under-specification**.
- Recommended the dry-state condition be written using **both**:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark RH-equivalent workflow**
- Required explicit run-sheet wording for:
  - RH setpoint,
  - pre-equilibration duration,
  - acceptance/tolerance window,
  - chamber documentation.
- Stated that the ratio convention **must match the benchmark exactly** and cannot be inferred from chemistry preference.
- Strongly recommended **holding release entirely** if ratio convention is unresolved.
- Required ultrasound to be visible on the run sheet or companion sheet with:
  - SOP ID,
  - instrument/model,
  - frequency,
  - amplitude/power,
  - pulse/continuous,
  - duration,
  - sample volume,
  - vessel type,
  - temperature control,
  - pass/fail acceptance.
- Clarified no-sugar controls should be:
  - β-LG only,
  - same protein loading,
  - same solvent route,
  - same ultrasound,
  - same deposition geometry,
  - same dry workflow,
  - no sugar donor added.
- Explicitly advised **against adding inert filler** unless already in benchmark SOP.
- Highlighted one more process-critical variable that must be fixed:
  - **deposition mass / loaded solids per sample**
  - plus vessel geometry / footprint.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that lower IgE signal is **not automatically meaningful**.
- Required for **all runs**:
  - primary β-LG IgE-binding assay,
  - recovered protein quantification,
  - extractability/solubility assessment,
  - turbidity/insolubility flag,
  - matched assay-input verification,
  - visual severity/handling record.
- Argued for broader preassigned interpretive safeguards than the chemistry-side minimum.
- Recommended **non-IgE β-LG detectability** be preassigned for:
  - all anchors,
  - all no-sugar controls,
  - all **60 C / 4 h sugar-containing runs**,
  - in both blocks.
- Gave a clear answer: **Yes**, all 60 C, 4 h sugar conditions should be preassigned to non-IgE detectability as a hard requirement.
- Recommended preassigned orthogonal confirmation for:
  - all anchors,
  - all no-sugar controls,
  - lactose 60 C / 4 h,
  - glucose 60 C / 4 h,
  - in both blocks.
- Recommended native untreated β-LG be included as a **formal assay control entry** in the assay plan, **not** as a row in the 24-run master list.
- Requested an explicit interpretation guardrail in the final notes:
  - low primary IgE signal alone is not sufficient for advancement.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly supported listing **24 explicit runs**, not “12 conditions × 2”.
- Recommended encoding inferential structure directly in the run sheet.
- Proposed two comparison columns:
  - **primary_comparison_group**
  - **comparison_tags**
- Suggested examples:
  - DONOR55,
  - DONOR60,
  - PROC55,
  - PROC60,
  - TIME60-LAC,
  - TIME60-GLU,
  - ANCHOR-HIST.
- Confirmed reruns should:
  - keep the same **condition_id**,
  - receive a new **run_id**,
  - never replace the original row.
- Recommended native untreated β-LG stay in the **assay/control plan only**, not the master run list.
- Recommended adding **control_status** to the master run list.
- Emphasized that unresolved:
  - ratio convention,
  - RH-equivalent implementation,
  - ultrasound summary,
  are all **true release gates**.

#### Scientific Critic
- Reinforced that the **ratio convention** is the most critical unresolved item and could invalidate donor comparisons if mishandled.
- Identified **RH-equivalent implementation** as the other key under-specified variable needing exact documentation.
- Supported:
  - structured sample labeling,
  - explicit comparison groups,
  - mandatory QC flags such as critical_deviation_flag and interpretation_status.
- Emphasized that execution readiness and analysis readiness must remain aligned.

#### Research Synthesis and Optimization Lead
- Focused on making the run sheet **analysis-ready by design**.
- Strongly recommended separating:
  - **condition identity** from
  - **execution identity**
- Proposed including in the wet-lab-facing sheet:
  - condition_id,
  - run_id,
  - block_id,
  - replicate_id,
  - sample naming label.
- Recommended machine-readable sample labels:
  - `BLGA_[BlockID]_[DonorCode]_[TempC]C_[TimeH]H_[ModeCode]_[CtrlCode]_[RepID]`
- Recommended compact condition IDs:
  - `COND_[DonorCode]_[TempC]C_[TimeH]H_[CtrlCode]`
- Recommended splitting the package into:
  - a concise **wet-lab execution sheet**
  - and a **QC/metadata companion sheet**
- Recommended minimal metadata/QC companion fields covering:
  - identity,
  - design grouping,
  - scientific condition,
  - execution metadata,
  - QC/disposition.
- Agreed that the final sheet should not rely on vague phrases like “same as benchmark”; it should contain **actual locked values or SOP-linked fields**.

---

### Recommendation

My recommendation is to issue a **two-sheet run-sheet package** for this round:

1. a **wet-lab execution sheet** containing the 24 explicit runs and all parameters needed for direct execution,
2. a **QC/metadata companion sheet** containing execution metadata, deviation capture, and downstream-analysis fields.

This is the correct final format because it satisfies both sides of the stage requirement:
- the wet-lab team receives a **clear, non-overloaded execution table**,
- and the project preserves the metadata structure needed for interpretability, evidence synthesis, and later AI-facing use.

However, I am also making a firm governance decision:

## Release-gating decision
The run sheet **must not be released for execution** until the following three benchmark-linked items are confirmed and filled with actual values:
1. **protein:sugar ratio convention**: 1:2 **w/w** or 1:2 **molar**
2. **RH-equivalent implementation** for aw 0.79:
   - RH setpoint,
   - pre-equilibration duration,
   - tolerance/acceptance window
3. **ultrasound execution summary**:
   - SOP ID,
   - instrument/model,
   - frequency,
   - amplitude/power,
   - mode,
   - duration,
   - sample volume,
   - vessel type,
   - temperature control

This recommendation is stricter than simply producing a template with placeholders, but it is the only scientifically responsible option under the agenda rule that **no critical experimental parameter may be left blank**.

Because those benchmark/protocol defaults were **not actually provided in the meeting record**, I cannot honestly claim to generate a fully executable final run sheet with those fields populated. The correct response is therefore:

- provide the **final run-sheet structure and content now**,
- mark the three unresolved benchmark-linked parameters as **release-gating fields requiring immediate SOP lookup**,
- and state clearly that execution should not begin until they are filled.

That is the most rigorous and agenda-compliant recommendation.

---

## Directly Actionable Wet-Lab Run-Sheet Package

# Part A. Round-level execution summary

## Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:
1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the benchmark-linked **60 C, 2 h** region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-structured dataset for restricted dry-domain decision support.

## Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- aw target: **0.79**
- RH-equivalent implementation: **must match benchmark SOP exactly**  
  - **RH setpoint = [RELEASE GATE: fill from SOP]**
  - **Pre-equilibration duration = [RELEASE GATE: fill from SOP]**
  - **Acceptance/tolerance = [RELEASE GATE: fill from SOP]**
- Protein:sugar ratio: **1:2**
  - **Ratio basis = [RELEASE GATE: w/w or molar, fill from benchmark]**
- Pretreatment: **Ultrasound ON**
  - SOP ID = **[RELEASE GATE: fill]**
  - instrument/model = **[RELEASE GATE: fill]**
  - frequency = **[RELEASE GATE: fill]**
  - amplitude/power = **[RELEASE GATE: fill]**
  - mode = **[RELEASE GATE: fill]**
  - duration = **[RELEASE GATE: fill]**
  - sample volume = **[RELEASE GATE: fill]**
  - vessel type = **[RELEASE GATE: fill]**
  - temperature control = **[RELEASE GATE: fill]**
- Sample preparation route: benchmark SOP fixed
- Deposition/sample geometry: benchmark SOP fixed
- Deposition mass / loaded solids per sample: **[RELEASE GATE: fill from SOP]**
- Cooling/stop procedure: benchmark SOP fixed
- Reconstitution/recovery workflow: benchmark SOP fixed
- Primary assay platform: benchmark-matched
- Native untreated β-LG reference: included in assay plan on every assay plate / orthogonal assay batch

## Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (no-sugar process-only control)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

## Deferred variables
- Wet-state mode
- pH / buffer
- aw variation
- ratio variation
- ultrasound variation
- other pretreatments
- 3 h intermediate time
- broader donor expansion

---

# Part B. Master run list

**Important release note:** The table below is structurally complete, but execution is authorized only after the release-gating benchmark values in Part A / Part E are filled.

| run_id | condition_id | group_id | primary_comparison_group | comparison_tags | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| B1-R01 | COND_LAC_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_LAC_55C_4H_DRY_SUG_R1 |
| B1-R02 | COND_GLU_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_GLU_55C_4H_DRY_SUG_R1 |
| B1-R03 | COND_GAL_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_GAL_55C_4H_DRY_SUG_R1 |
| B1-R04 | COND_MAN_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_MAN_55C_4H_DRY_SUG_R1 |
| B1-R05 | COND_LAC_60C_4H_SUG | B1 | DONOR60 | PROC60;TIME60-LAC | 60 C donor ranking; lactose time bridge; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_LAC_60C_4H_DRY_SUG_R1 |
| B1-R06 | COND_GLU_60C_4H_SUG | B1 | DONOR60 | PROC60;TIME60-GLU | 60 C donor ranking; glucose time bridge; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_GLU_60C_4H_DRY_SUG_R1 |
| B1-R07 | COND_GAL_60C_4H_SUG | B1 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability | BLGA_B1_GAL_60C_4H_DRY_SUG_R1 |
| B1-R08 | COND_MAN_60C_4H_SUG | B1 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability | BLGA_B1_MAN_60C_4H_DRY_SUG_R1 |
| B1-R09 | COND_LAC_60C_2H_SUG | B1 | TIME60-LAC | ANCHOR-HIST | Same-round lactose anchor; benchmark continuity | Lactose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_LAC_60C_2H_DRY_SUG_R1 |
| B1-R10 | COND_GLU_60C_2H_SUG | B1 | TIME60-GLU | ANCHOR-HIST | Same-round glucose anchor; benchmark continuity | Glucose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_GLU_60C_2H_DRY_SUG_R1 |
| B1-R11 | COND_NONE_55C_4H_NOSUG | B1 | DONOR55 | PROC55 | 55 C process-only comparator | None | none | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_NONE_55C_4H_DRY_NOSUG_R1 |
| B1-R12 | COND_NONE_60C_4H_NOSUG | B1 | DONOR60 | PROC60 | 60 C process-only comparator | None | none | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_NONE_60C_4H_DRY_NOSUG_R1 |
| B2-R01 | COND_LAC_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_LAC_55C_4H_DRY_SUG_R2 |
| B2-R02 | COND_GLU_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_GLU_55C_4H_DRY_SUG_R2 |
| B2-R03 | COND_GAL_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_GAL_55C_4H_DRY_SUG_R2 |
| B2-R04 | COND_MAN_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_MAN_55C_4H_DRY_SUG_R2 |
| B2-R05 | COND_LAC_60C_4H_SUG | B2 | DONOR60 | PROC60;TIME60-LAC | 60 C donor ranking; lactose time bridge; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_LAC_60C_4H_DRY_SUG_R2 |
| B2-R06 | COND_GLU_60C_4H_SUG | B2 | DONOR60 | PROC60;TIME60-GLU | 60 C donor ranking; glucose time bridge; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_GLU_60C_4H_DRY_SUG_R2 |
| B2-R07 | COND_GAL_60C_4H_SUG | B2 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability | BLGA_B2_GAL_60C_4H_DRY_SUG_R2 |
| B2-R08 | COND_MAN_60C_4H_SUG | B2 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability | BLGA_B2_MAN_60C_4H_DRY_SUG_R2 |
| B2-R09 | COND_LAC_60C_2H_SUG | B2 | TIME60-LAC | ANCHOR-HIST | Same-round lactose anchor; benchmark continuity | Lactose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_LAC_60C_2H_DRY_SUG_R2 |
| B2-R10 | COND_GLU_60C_2H_SUG | B2 | TIME60-GLU | ANCHOR-HIST | Same-round glucose anchor; benchmark continuity | Glucose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_GLU_60C_2H_DRY_SUG_R2 |
| B2-R11 | COND_NONE_55C_4H_NOSUG | B2 | DONOR55 | PROC55 | 55 C process-only comparator | None | none | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_NONE_55C_4H_DRY_NOSUG_R2 |
| B2-R12 | COND_NONE_60C_4H_NOSUG | B2 | DONOR60 | PROC60 | 60 C process-only comparator | None | none | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_NONE_60C_4H_DRY_NOSUG_R2 |

---

# Part C. Batch execution plan

## Batch grouping
- **Block 1 (B1):** full 12-run matrix, independently prepared and processed
- **Block 2 (B2):** full 12-run matrix, independently prepared and processed

## Which runs should be processed together
Within each block, prepare all 12 runs in one coordinated campaign if capacity allows, with balanced handling across:
- sample preparation,
- ultrasound,
- deposition,
- pre-equilibration,
- incubation,
- recovery,
- assay allocation.

Because 55 C and 60 C are distinct incubation temperatures, they may require separate incubator settings or separate temperature-specific sub-batches, but must remain part of the same protected block campaign.

## Protected matched-comparison groupings

### Protected set A: 55 C donor ranking and process-only separation
- LAC 55 C 4 h
- GLU 55 C 4 h
- GAL 55 C 4 h
- MAN 55 C 4 h
- NONE 55 C 4 h

### Protected set B: 60 C donor ranking and process-only separation
- LAC 60 C 4 h
- GLU 60 C 4 h
- GAL 60 C 4 h
- MAN 60 C 4 h
- NONE 60 C 4 h

### Protected set C: 60 C time bridge
- LAC 60 C 2 h
- LAC 60 C 4 h
- GLU 60 C 2 h
- GLU 60 C 4 h

## Processing rules
- Do **not** cluster all runs by donor on the same chamber region or assay plate.
- Randomize chamber position within temperature.
- Distribute anchors and no-sugar controls across assay plates.
- Rotate chamber positions between B1 and B2 if feasible.
- If a run in a protected comparison group fails, interpretability of that comparison group within that block must be flagged as reduced.

---

# Part D. Assay plan

## Assays required for all runs
For all 24 runs:
1. **Primary β-LG IgE-binding assay (benchmark-matched format)**
2. **Recovered protein quantification**
3. **Extractability/solubility assessment**
4. **Turbidity/insolubility flag**
5. **Matched assay-input verification on recovered protein basis**
6. **Visual severity/handling record**

## Preassigned support assays

### Non-IgE β-LG detectability assay
Required for:
- all anchors:
  - B1-R09, B1-R10, B2-R09, B2-R10
- all no-sugar controls:
  - B1-R11, B1-R12, B2-R11, B2-R12
- all 60 C / 4 h sugar runs:
  - B1-R05, B1-R06, B1-R07, B1-R08
  - B2-R05, B2-R06, B2-R07, B2-R08

### Orthogonal confirmation package
Required for:
- all anchors:
  - B1-R09, B1-R10, B2-R09, B2-R10
- all no-sugar controls:
  - B1-R11, B1-R12, B2-R11, B2-R12
- lactose 60 C / 4 h:
  - B1-R05, B2-R05
- glucose 60 C / 4 h:
  - B1-R06, B2-R06

## Conditional support assays after Tier A review
- Orthogonal confirmation and/or detectability for:
  - top new donor branch,
  - one strongest high-caution/high-reduction condition not already preassigned,
  - one competitive low-caution 55 C branch if relevant.
- Free lysine proxy on:
  - anchors,
  - no-sugar controls,
  - top apparent winners,
  - one caution comparator.

## Formal assay control entry
- **Untreated/native β-LG reference**
  - include on every primary assay plate
  - include in every orthogonal assay batch
  - not part of the 24-run process matrix

## Interpretation-support purpose statement
Orthogonal confirmation is used to distinguish apparent IgE-binding reduction consistent with altered β-LG IgE recognition from reduction driven primarily by:
- assay-format sensitivity,
- altered antigen presentation,
- aggregation,
- severe detectability collapse.

---

# Part E. Execution notes

## Parameter definitions
- **Mode:** Dry glycation only
- **aw/RH field wording:**  
  Target aw = 0.79; execute via validated benchmark RH-equivalent workflow with RH setpoint, pre-equilibration duration, and acceptance window filled from SOP before release.
- **Ratio:**  
  1:2 using the exact benchmark basis (**w/w or molar must be confirmed before release**).
- **No-sugar process control:**  
  β-LG only; no donor added; same protein loading, solvent route, ultrasound, deposition geometry, dry-state workflow, and recovery workflow as sugar-containing runs.
- **Pretreatment:**  
  Ultrasound ON with benchmark SOP-linked settings.

## Timing rules
- 4 h applies to:
  - all donor bridge runs,
  - both no-sugar controls.
- 2 h applies only to:
  - lactose 60 C anchor,
  - glucose 60 C anchor.
- Record actual:
  - prep time,
  - equilibration start/stop,
  - incubation start/stop,
  - cooling stop time,
  - recovery time.

## Control rules
- Native untreated β-LG is an assay control, not a process-matrix run.
- No-sugar controls are matched process-only comparators and must be prepared in each block.
- Anchors and no-sugar controls are protected comparators and must be distributed across assay plates.

## Naming rules
- **Condition ID format:**  
  `COND_[DonorCode]_[TempC]C_[TimeH]H_[CtrlCode]`
- **Sample naming label format:**  
  `BLGA_[BlockID]_[DonorCode]_[TempC]C_[TimeH]H_[ModeCode]_[CtrlCode]_[RepID]`
- **Rerun rule:**  
  keep same condition_id, assign new run_id, append rerun suffix to sample label.

## Practical notes for wet-lab implementation
- Do not begin execution until the benchmark-linked release-gating values are filled.
- Include deposition mass / loaded solids per sample and vessel geometry in the companion sheet.
- Record chamber ID and chamber position for every run.
- Use the same β-LG lot across the round if feasible.
- Use the same donor lots/grades across the round if feasible.
- Normalize immunoassay input to recovered protein basis.
- A lower primary IgE-binding signal is **not sufficient** for advancement by itself.
- A condition is considered immunologically interpretable only when:
  - recovery-normalized reduction exceeds matched no-sugar control,
  - β-LG detectability is not severely collapsed,
  - and orthogonal results are not contradictory.

---

### Next Steps

1. **Immediately retrieve the benchmark/protocol defaults** for the three release-gating items:
   - ratio basis: **1:2 w/w or 1:2 molar**
   - RH-equivalent setpoint, pre-equilibration duration, and tolerance for aw 0.79
   - ultrasound execution parameters and SOP ID
2. **Populate those values into Parts A, B, and E**.
3. Add the companion **QC/metadata sheet** with at least:
   - condition_id,
   - run_id,
   - block_id,
   - replicate_id,
   - primary_comparison_group,
   - comparison_tags,
   - control_status,
   - operator,
   - timestamps,
   - chamber ID/position,
   - assay batch/plate IDs,
   - run_disposition,
   - critical_deviation_flag,
   - interpretation_status,
   - trainable_for_modeling.
4. Perform a final **release check**:
   - no blanks in critical fields,
   - all protected comparators present,
   - all preassigned support assays correctly marked.
5. Only then **release the package to the wet-lab team** for execution.

If you want, next I can convert this into a **clean release-ready template** with:
- one execution table,
- one QC/metadata companion table,
- and a short release checklist.
### Agenda

Convert the already approved dry-only experimental design for β-LG variant A glycation into a **directly executable wet-lab run-sheet package**. The goal is not to revisit strategy, but to produce a **run-by-run, parameter-complete, operationally clear experiment list** for the wet-lab team, including fixed variables, scanned variables, explicit dry-state conditions, controls, replicates, batching, assay assignments, and execution notes. The round remains restricted to **dry-state observed β-LG IgE-binding reduction**, with explicit attention to interpretability and the time-versus-severity tradeoff.

---

### Team Member Input

#### Principal Investigator
- Framed the meeting as an **execution-clarification exercise**, not a design debate.
- Identified the main risk as **execution ambiguity**, especially unresolved placeholders such as:
  - ratio convention,
  - aw/RH implementation,
  - ultrasound wording.
- Proposed that the final package should likely contain:
  - **24 explicit runs**,
  - block IDs,
  - scientific purpose,
  - matched comparison grouping,
  - assay assignments,
  - and structured naming.
- Asked each team member to focus on execution readiness in their domain.

#### Maillard Reaction Chemistry and Process Scientist
- Strongly agreed that the main remaining issue is **operational under-specification**.
- Recommended the dry-state condition be written using **both**:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark RH-equivalent workflow**
- Required explicit run-sheet wording for:
  - RH setpoint,
  - pre-equilibration duration,
  - acceptance/tolerance window,
  - chamber documentation.
- Stated that the ratio convention **must match the benchmark exactly** and cannot be inferred from chemistry preference.
- Strongly recommended **holding release entirely** if ratio convention is unresolved.
- Required ultrasound to be visible on the run sheet or companion sheet with:
  - SOP ID,
  - instrument/model,
  - frequency,
  - amplitude/power,
  - pulse/continuous,
  - duration,
  - sample volume,
  - vessel type,
  - temperature control,
  - pass/fail acceptance.
- Clarified no-sugar controls should be:
  - β-LG only,
  - same protein loading,
  - same solvent route,
  - same ultrasound,
  - same deposition geometry,
  - same dry workflow,
  - no sugar donor added.
- Explicitly advised **against adding inert filler** unless already in benchmark SOP.
- Highlighted one more process-critical variable that must be fixed:
  - **deposition mass / loaded solids per sample**
  - plus vessel geometry / footprint.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that lower IgE signal is **not automatically meaningful**.
- Required for **all runs**:
  - primary β-LG IgE-binding assay,
  - recovered protein quantification,
  - extractability/solubility assessment,
  - turbidity/insolubility flag,
  - matched assay-input verification,
  - visual severity/handling record.
- Argued for broader preassigned interpretive safeguards than the chemistry-side minimum.
- Recommended **non-IgE β-LG detectability** be preassigned for:
  - all anchors,
  - all no-sugar controls,
  - all **60 C / 4 h sugar-containing runs**,
  - in both blocks.
- Gave a clear answer: **Yes**, all 60 C, 4 h sugar conditions should be preassigned to non-IgE detectability as a hard requirement.
- Recommended preassigned orthogonal confirmation for:
  - all anchors,
  - all no-sugar controls,
  - lactose 60 C / 4 h,
  - glucose 60 C / 4 h,
  - in both blocks.
- Recommended native untreated β-LG be included as a **formal assay control entry** in the assay plan, **not** as a row in the 24-run master list.
- Requested an explicit interpretation guardrail in the final notes:
  - low primary IgE signal alone is not sufficient for advancement.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly supported listing **24 explicit runs**, not “12 conditions × 2”.
- Recommended encoding inferential structure directly in the run sheet.
- Proposed two comparison columns:
  - **primary_comparison_group**
  - **comparison_tags**
- Suggested examples:
  - DONOR55,
  - DONOR60,
  - PROC55,
  - PROC60,
  - TIME60-LAC,
  - TIME60-GLU,
  - ANCHOR-HIST.
- Confirmed reruns should:
  - keep the same **condition_id**,
  - receive a new **run_id**,
  - never replace the original row.
- Recommended native untreated β-LG stay in the **assay/control plan only**, not the master run list.
- Recommended adding **control_status** to the master run list.
- Emphasized that unresolved:
  - ratio convention,
  - RH-equivalent implementation,
  - ultrasound summary,
  are all **true release gates**.

#### Scientific Critic
- Reinforced that the **ratio convention** is the most critical unresolved item and could invalidate donor comparisons if mishandled.
- Identified **RH-equivalent implementation** as the other key under-specified variable needing exact documentation.
- Supported:
  - structured sample labeling,
  - explicit comparison groups,
  - mandatory QC flags such as critical_deviation_flag and interpretation_status.
- Emphasized that execution readiness and analysis readiness must remain aligned.

#### Research Synthesis and Optimization Lead
- Focused on making the run sheet **analysis-ready by design**.
- Strongly recommended separating:
  - **condition identity** from
  - **execution identity**
- Proposed including in the wet-lab-facing sheet:
  - condition_id,
  - run_id,
  - block_id,
  - replicate_id,
  - sample naming label.
- Recommended machine-readable sample labels:
  - `BLGA_[BlockID]_[DonorCode]_[TempC]C_[TimeH]H_[ModeCode]_[CtrlCode]_[RepID]`
- Recommended compact condition IDs:
  - `COND_[DonorCode]_[TempC]C_[TimeH]H_[CtrlCode]`
- Recommended splitting the package into:
  - a concise **wet-lab execution sheet**
  - and a **QC/metadata companion sheet**
- Recommended minimal metadata/QC companion fields covering:
  - identity,
  - design grouping,
  - scientific condition,
  - execution metadata,
  - QC/disposition.
- Agreed that the final sheet should not rely on vague phrases like “same as benchmark”; it should contain **actual locked values or SOP-linked fields**.

---

### Recommendation

My recommendation is to issue a **two-sheet run-sheet package** for this round:

1. a **wet-lab execution sheet** containing the 24 explicit runs and all parameters needed for direct execution,
2. a **QC/metadata companion sheet** containing execution metadata, deviation capture, and downstream-analysis fields.

This is the correct final format because it satisfies both sides of the stage requirement:
- the wet-lab team receives a **clear, non-overloaded execution table**,
- and the project preserves the metadata structure needed for interpretability, evidence synthesis, and later AI-facing use.

However, I am also making a firm governance decision:

## Release-gating decision
The run sheet **must not be released for execution** until the following three benchmark-linked items are confirmed and filled with actual values:
1. **protein:sugar ratio convention**: 1:2 **w/w** or 1:2 **molar**
2. **RH-equivalent implementation** for aw 0.79:
   - RH setpoint,
   - pre-equilibration duration,
   - tolerance/acceptance window
3. **ultrasound execution summary**:
   - SOP ID,
   - instrument/model,
   - frequency,
   - amplitude/power,
   - mode,
   - duration,
   - sample volume,
   - vessel type,
   - temperature control

This recommendation is stricter than simply producing a template with placeholders, but it is the only scientifically responsible option under the agenda rule that **no critical experimental parameter may be left blank**.

Because those benchmark/protocol defaults were **not actually provided in the meeting record**, I cannot honestly claim to generate a fully executable final run sheet with those fields populated. The correct response is therefore:

- provide the **final run-sheet structure and content now**,
- mark the three unresolved benchmark-linked parameters as **release-gating fields requiring immediate SOP lookup**,
- and state clearly that execution should not begin until they are filled.

That is the most rigorous and agenda-compliant recommendation.

---

## Directly Actionable Wet-Lab Run-Sheet Package

# Part A. Round-level execution summary

## Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:
1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the benchmark-linked **60 C, 2 h** region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-structured dataset for restricted dry-domain decision support.

## Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- aw target: **0.79**
- RH-equivalent implementation: **must match benchmark SOP exactly**  
  - **RH setpoint = [RELEASE GATE: fill from SOP]**
  - **Pre-equilibration duration = [RELEASE GATE: fill from SOP]**
  - **Acceptance/tolerance = [RELEASE GATE: fill from SOP]**
- Protein:sugar ratio: **1:2**
  - **Ratio basis = [RELEASE GATE: w/w or molar, fill from benchmark]**
- Pretreatment: **Ultrasound ON**
  - SOP ID = **[RELEASE GATE: fill]**
  - instrument/model = **[RELEASE GATE: fill]**
  - frequency = **[RELEASE GATE: fill]**
  - amplitude/power = **[RELEASE GATE: fill]**
  - mode = **[RELEASE GATE: fill]**
  - duration = **[RELEASE GATE: fill]**
  - sample volume = **[RELEASE GATE: fill]**
  - vessel type = **[RELEASE GATE: fill]**
  - temperature control = **[RELEASE GATE: fill]**
- Sample preparation route: benchmark SOP fixed
- Deposition/sample geometry: benchmark SOP fixed
- Deposition mass / loaded solids per sample: **[RELEASE GATE: fill from SOP]**
- Cooling/stop procedure: benchmark SOP fixed
- Reconstitution/recovery workflow: benchmark SOP fixed
- Primary assay platform: benchmark-matched
- Native untreated β-LG reference: included in assay plan on every assay plate / orthogonal assay batch

## Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (no-sugar process-only control)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

## Deferred variables
- Wet-state mode
- pH / buffer
- aw variation
- ratio variation
- ultrasound variation
- other pretreatments
- 3 h intermediate time
- broader donor expansion

---

# Part B. Master run list

**Important release note:** The table below is structurally complete, but execution is authorized only after the release-gating benchmark values in Part A / Part E are filled.

| run_id | condition_id | group_id | primary_comparison_group | comparison_tags | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| B1-R01 | COND_LAC_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_LAC_55C_4H_DRY_SUG_R1 |
| B1-R02 | COND_GLU_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_GLU_55C_4H_DRY_SUG_R1 |
| B1-R03 | COND_GAL_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_GAL_55C_4H_DRY_SUG_R1 |
| B1-R04 | COND_MAN_55C_4H_SUG | B1 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Conditional only | BLGA_B1_MAN_55C_4H_DRY_SUG_R1 |
| B1-R05 | COND_LAC_60C_4H_SUG | B1 | DONOR60 | PROC60;TIME60-LAC | 60 C donor ranking; lactose time bridge; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_LAC_60C_4H_DRY_SUG_R1 |
| B1-R06 | COND_GLU_60C_4H_SUG | B1 | DONOR60 | PROC60;TIME60-GLU | 60 C donor ranking; glucose time bridge; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_GLU_60C_4H_DRY_SUG_R1 |
| B1-R07 | COND_GAL_60C_4H_SUG | B1 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability | BLGA_B1_GAL_60C_4H_DRY_SUG_R1 |
| B1-R08 | COND_MAN_60C_4H_SUG | B1 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability | BLGA_B1_MAN_60C_4H_DRY_SUG_R1 |
| B1-R09 | COND_LAC_60C_2H_SUG | B1 | TIME60-LAC | ANCHOR-HIST | Same-round lactose anchor; benchmark continuity | Lactose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_LAC_60C_2H_DRY_SUG_R1 |
| B1-R10 | COND_GLU_60C_2H_SUG | B1 | TIME60-GLU | ANCHOR-HIST | Same-round glucose anchor; benchmark continuity | Glucose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_GLU_60C_2H_DRY_SUG_R1 |
| B1-R11 | COND_NONE_55C_4H_NOSUG | B1 | DONOR55 | PROC55 | 55 C process-only comparator | None | none | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_NONE_55C_4H_DRY_NOSUG_R1 |
| B1-R12 | COND_NONE_60C_4H_NOSUG | B1 | DONOR60 | PROC60 | 60 C process-only comparator | None | none | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R1 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B1_NONE_60C_4H_DRY_NOSUG_R1 |
| B2-R01 | COND_LAC_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_LAC_55C_4H_DRY_SUG_R2 |
| B2-R02 | COND_GLU_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_GLU_55C_4H_DRY_SUG_R2 |
| B2-R03 | COND_GAL_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_GAL_55C_4H_DRY_SUG_R2 |
| B2-R04 | COND_MAN_55C_4H_SUG | B2 | DONOR55 | PROC55 | 55 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Conditional only | BLGA_B2_MAN_55C_4H_DRY_SUG_R2 |
| B2-R05 | COND_LAC_60C_4H_SUG | B2 | DONOR60 | PROC60;TIME60-LAC | 60 C donor ranking; lactose time bridge; sugar vs process-only comparison | Lactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_LAC_60C_4H_DRY_SUG_R2 |
| B2-R06 | COND_GLU_60C_4H_SUG | B2 | DONOR60 | PROC60;TIME60-GLU | 60 C donor ranking; glucose time bridge; sugar vs process-only comparison | Glucose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_GLU_60C_4H_DRY_SUG_R2 |
| B2-R07 | COND_GAL_60C_4H_SUG | B2 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Galactose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability | BLGA_B2_GAL_60C_4H_DRY_SUG_R2 |
| B2-R08 | COND_MAN_60C_4H_SUG | B2 | DONOR60 | PROC60 | 60 C donor ranking; sugar vs process-only comparison | Mannose | 1:2 [basis release-gated] | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability | BLGA_B2_MAN_60C_4H_DRY_SUG_R2 |
| B2-R09 | COND_LAC_60C_2H_SUG | B2 | TIME60-LAC | ANCHOR-HIST | Same-round lactose anchor; benchmark continuity | Lactose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_LAC_60C_2H_DRY_SUG_R2 |
| B2-R10 | COND_GLU_60C_2H_SUG | B2 | TIME60-GLU | ANCHOR-HIST | Same-round glucose anchor; benchmark continuity | Glucose | 1:2 [basis release-gated] | Dry | 60 | 2 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | sugar_condition | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_GLU_60C_2H_DRY_SUG_R2 |
| B2-R11 | COND_NONE_55C_4H_NOSUG | B2 | DONOR55 | PROC55 | 55 C process-only comparator | None | none | Dry | 55 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_NONE_55C_4H_DRY_NOSUG_R2 |
| B2-R12 | COND_NONE_60C_4H_NOSUG | B2 | DONOR60 | PROC60 | 60 C process-only comparator | None | none | Dry | 60 | 4 | aw 0.79 target; RH=[fill]; pre-eq=[fill] | Ultrasound ON | no_sugar_process_control | R2 | Tier A all-run package | Preassigned: detectability + orthogonal | BLGA_B2_NONE_60C_4H_DRY_NOSUG_R2 |

---

# Part C. Batch execution plan

## Batch grouping
- **Block 1 (B1):** full 12-run matrix, independently prepared and processed
- **Block 2 (B2):** full 12-run matrix, independently prepared and processed

## Which runs should be processed together
Within each block, prepare all 12 runs in one coordinated campaign if capacity allows, with balanced handling across:
- sample preparation,
- ultrasound,
- deposition,
- pre-equilibration,
- incubation,
- recovery,
- assay allocation.

Because 55 C and 60 C are distinct incubation temperatures, they may require separate incubator settings or separate temperature-specific sub-batches, but must remain part of the same protected block campaign.

## Protected matched-comparison groupings

### Protected set A: 55 C donor ranking and process-only separation
- LAC 55 C 4 h
- GLU 55 C 4 h
- GAL 55 C 4 h
- MAN 55 C 4 h
- NONE 55 C 4 h

### Protected set B: 60 C donor ranking and process-only separation
- LAC 60 C 4 h
- GLU 60 C 4 h
- GAL 60 C 4 h
- MAN 60 C 4 h
- NONE 60 C 4 h

### Protected set C: 60 C time bridge
- LAC 60 C 2 h
- LAC 60 C 4 h
- GLU 60 C 2 h
- GLU 60 C 4 h

## Processing rules
- Do **not** cluster all runs by donor on the same chamber region or assay plate.
- Randomize chamber position within temperature.
- Distribute anchors and no-sugar controls across assay plates.
- Rotate chamber positions between B1 and B2 if feasible.
- If a run in a protected comparison group fails, interpretability of that comparison group within that block must be flagged as reduced.

---

# Part D. Assay plan

## Assays required for all runs
For all 24 runs:
1. **Primary β-LG IgE-binding assay (benchmark-matched format)**
2. **Recovered protein quantification**
3. **Extractability/solubility assessment**
4. **Turbidity/insolubility flag**
5. **Matched assay-input verification on recovered protein basis**
6. **Visual severity/handling record**

## Preassigned support assays

### Non-IgE β-LG detectability assay
Required for:
- all anchors:
  - B1-R09, B1-R10, B2-R09, B2-R10
- all no-sugar controls:
  - B1-R11, B1-R12, B2-R11, B2-R12
- all 60 C / 4 h sugar runs:
  - B1-R05, B1-R06, B1-R07, B1-R08
  - B2-R05, B2-R06, B2-R07, B2-R08

### Orthogonal confirmation package
Required for:
- all anchors:
  - B1-R09, B1-R10, B2-R09, B2-R10
- all no-sugar controls:
  - B1-R11, B1-R12, B2-R11, B2-R12
- lactose 60 C / 4 h:
  - B1-R05, B2-R05
- glucose 60 C / 4 h:
  - B1-R06, B2-R06

## Conditional support assays after Tier A review
- Orthogonal confirmation and/or detectability for:
  - top new donor branch,
  - one strongest high-caution/high-reduction condition not already preassigned,
  - one competitive low-caution 55 C branch if relevant.
- Free lysine proxy on:
  - anchors,
  - no-sugar controls,
  - top apparent winners,
  - one caution comparator.

## Formal assay control entry
- **Untreated/native β-LG reference**
  - include on every primary assay plate
  - include in every orthogonal assay batch
  - not part of the 24-run process matrix

## Interpretation-support purpose statement
Orthogonal confirmation is used to distinguish apparent IgE-binding reduction consistent with altered β-LG IgE recognition from reduction driven primarily by:
- assay-format sensitivity,
- altered antigen presentation,
- aggregation,
- severe detectability collapse.

---

# Part E. Execution notes

## Parameter definitions
- **Mode:** Dry glycation only
- **aw/RH field wording:**  
  Target aw = 0.79; execute via validated benchmark RH-equivalent workflow with RH setpoint, pre-equilibration duration, and acceptance window filled from SOP before release.
- **Ratio:**  
  1:2 using the exact benchmark basis (**w/w or molar must be confirmed before release**).
- **No-sugar process control:**  
  β-LG only; no donor added; same protein loading, solvent route, ultrasound, deposition geometry, dry-state workflow, and recovery workflow as sugar-containing runs.
- **Pretreatment:**  
  Ultrasound ON with benchmark SOP-linked settings.

## Timing rules
- 4 h applies to:
  - all donor bridge runs,
  - both no-sugar controls.
- 2 h applies only to:
  - lactose 60 C anchor,
  - glucose 60 C anchor.
- Record actual:
  - prep time,
  - equilibration start/stop,
  - incubation start/stop,
  - cooling stop time,
  - recovery time.

## Control rules
- Native untreated β-LG is an assay control, not a process-matrix run.
- No-sugar controls are matched process-only comparators and must be prepared in each block.
- Anchors and no-sugar controls are protected comparators and must be distributed across assay plates.

## Naming rules
- **Condition ID format:**  
  `COND_[DonorCode]_[TempC]C_[TimeH]H_[CtrlCode]`
- **Sample naming label format:**  
  `BLGA_[BlockID]_[DonorCode]_[TempC]C_[TimeH]H_[ModeCode]_[CtrlCode]_[RepID]`
- **Rerun rule:**  
  keep same condition_id, assign new run_id, append rerun suffix to sample label.

## Practical notes for wet-lab implementation
- Do not begin execution until the benchmark-linked release-gating values are filled.
- Include deposition mass / loaded solids per sample and vessel geometry in the companion sheet.
- Record chamber ID and chamber position for every run.
- Use the same β-LG lot across the round if feasible.
- Use the same donor lots/grades across the round if feasible.
- Normalize immunoassay input to recovered protein basis.
- A lower primary IgE-binding signal is **not sufficient** for advancement by itself.
- A condition is considered immunologically interpretable only when:
  - recovery-normalized reduction exceeds matched no-sugar control,
  - β-LG detectability is not severely collapsed,
  - and orthogonal results are not contradictory.

---

### Next Steps

1. **Immediately retrieve the benchmark/protocol defaults** for the three release-gating items:
   - ratio basis: **1:2 w/w or 1:2 molar**
   - RH-equivalent setpoint, pre-equilibration duration, and tolerance for aw 0.79
   - ultrasound execution parameters and SOP ID
2. **Populate those values into Parts A, B, and E**.
3. Add the companion **QC/metadata sheet** with at least:
   - condition_id,
   - run_id,
   - block_id,
   - replicate_id,
   - primary_comparison_group,
   - comparison_tags,
   - control_status,
   - operator,
   - timestamps,
   - chamber ID/position,
   - assay batch/plate IDs,
   - run_disposition,
   - critical_deviation_flag,
   - interpretation_status,
   - trainable_for_modeling.
4. Perform a final **release check**:
   - no blanks in critical fields,
   - all protected comparators present,
   - all preassigned support assays correctly marked.
5. Only then **release the package to the wet-lab team** for execution.

If you want, next I can convert this into a **clean release-ready template** with:
- one execution table,
- one QC/metadata companion table,
- and a short release checklist.

[end summary 1]

[begin summary 2]

### Agenda

Translate the already approved dry-only β-LG glycation screening design into a **directly executable wet-lab packet**. The goal is not to reopen strategy, but to produce a run-by-run, parameter-complete experiment sheet for the wet-lab team that preserves comparator logic, assay interpretability, and later evidence/model usability. The packet must explicitly specify all fixed and scanned variables, include matched controls and process replicates, define dry-state aw/RH conditions, assign assays, and provide execution/QC rules.

---

### Team Member Input

#### Principal Investigator
- Framed the meeting as **operational translation**, not design revision.
- Reaffirmed the approved design:
  - dry-only
  - β-LG variant A
  - fixed aw backbone
  - fixed 1:2 ratio
  - ultrasound ON
  - 12-condition matrix
  - preferred 2 full independent process blocks
- Identified main execution risks:
  - ambiguous ratio basis
  - ambiguous dry-state control wording
  - insufficient ultrasound definition
  - unclear replicate/block structure
  - unclear assay assignment
  - unclear naming and control handling
- Proposed a final deliverable as a multi-part packet:
  - round summary
  - master run list
  - batch plan
  - assay plan
  - execution/QC notes
- Asked team to focus on process closure, assay assignment, comparator structure, failure modes, and downstream usability.

#### Maillard Reaction Chemistry and Process Scientist
- Strongly agreed the remaining task is **operational closure**.
- Identified critical chemistry/process items that cannot remain implicit:
  1. **Protein:sugar ratio basis must be locked** as either w/w or molar.
  2. **aw 0.79 must be translated into an operational RH-equivalent workflow**.
  3. **Ultrasound must be tied to a fixed SOP and acceptance window**.
  4. **Time-zero and stop rules must be explicit**.
  5. **Sample geometry/loading must be fixed**.
- Recommended the packet use:
  - locked constants in header
  - SOP-linked process wording
  - actuals capture in a companion execution log
- Advised that the run sheet may be drafted now, but **must not be released for execution until ratio basis is locked**.
- Proposed concise execution wording:
  - Dry-state condition: target aw 0.79 using benchmark RH-equivalent workflow per SOP
  - Reaction starts at entry into pre-equilibrated incubation environment and ends at removal for immediate stop/cooling
  - Fixed benchmark deposition and vessel geometry per SOP
- Added a practical warning:
  - browning, caking, and lower recovery are **overprocessing flags**, not success signals.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the packet must pre-wire **interpretability**, not just sample production.
- Stated that lower IgE signal is only useful if distinguished from:
  - poor recovery
  - aggregation
  - altered presentation
  - detectability collapse
  - process-only effects
- Recommended required measurements for **all runs**:
  - primary IgE assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - loading normalization verification
- Recommended **standardized grouped assay columns** in Part B rather than many assay-specific columns.
- Recommended pre-assigned subset assays:
  - runs 9–12 mandatory for non-IgE β-LG detectability
  - runs 9–12 mandatory for orthogonal IgE confirmation
- Conditional subset:
  - top 2 apparent 4 h sugar winners
  - one high-caution/high-reduction case if distinct
  - any advancing condition
- Recommended native untreated β-LG reference be included in **Part D / assay plan**, not as a Part B process run.
- Proposed concise guardrails:
  - primary endpoint is observed IgE-binding reduction, not clinical allergenicity reduction
  - do not interpret lower signal without recovery-normalized loading
  - compare against matched no-sugar controls
  - escalate high-turbidity/low-recovery samples
  - require no major contradiction from detectability or orthogonal data

#### Experimental Design and Evidence Synthesis Scientist
- Emphasized that the packet must preserve **comparison structure** for later synthesis.
- Recommended preferred execution as **2 full independent 12-run process blocks**.
- Strongly recommended fallback confirmation plan be written now but kept separate as a **contingency mini-table**.
- Recommended Part B include essential comparator-link columns:
  - block_id
  - comparison_group
  - matched_control_id
  - paired_temperature_run_id
  - paired_time_anchor_run_id
  - historical_link_flag
- Recommended Part B remain lean but include both:
  - `purpose` for human readability
  - `comparison_group` for analysis readability
- Recommended Part C specify:
  - balancing/randomization principles
  - protected comparator placement
  - not a rigid exact processing order unless already validated
- Warned that comparator links must live in **Part B**, not only Part C.

#### Scientific Critic
- Focused on remaining unsafe-to-release failure points:
  1. unresolved ratio basis
  2. unclear aw/RH operational specification
  3. unclear ultrasound SOP/acceptance
  4. absence of visible critical deviation rules
  5. incomplete comparator structure in Part B
- Supported the proposed sample naming format and requested it remain standardized and free of ambiguous formatting.
- Proposed a short critical deviation box including:
  - wrong donor or ratio basis
  - incorrect temperature
  - missed ultrasound
  - failed RH/aw control
  - major timing deviation
  - recovery failure or sample mix-up
- Recommended a visible QC checklist and a cover-page style summary of key instructions.

#### Research Synthesis and Optimization Lead
- Focused on making the packet useful for both:
  - immediate decision-making
  - downstream restricted-domain model ingestion
- Recommended a **small structured packet**, matching the agenda.
- Recommended one row per **process run**, not assay well.
- Supported comparator-link columns directly in Part B.
- Recommended only a minimal set of post-run placeholders in Part B:
  - deviation_flag
  - QC_status
  - assayable_status
  - trainability_status
- Recommended controlled vocabulary:
  - deviation_flag: None / Minor / Critical
  - QC_status: Pending / Pass / Fail
  - assayable_status: Pending / Yes / No
  - trainability_status: Pending / Yes / No
- Advised against putting downstream interpretation fields like advancement action or orthogonal support into Part B.
- Noted that `trainability_status` should be assigned by project QC/analysis review, not bench operators.

---

### Recommendation

My recommendation is to issue a **five-part wet-lab packet** for the **preferred 2-block execution plan**, with a **24-row master run list** and a separate **contingency mini-table** for fallback replication. The scientific design remains unchanged.

However, I am making one critical governance decision:

> **The packet may be finalized as a draft now, but it must not be released for bench execution until three hard-stop operational constants are locked from the benchmark SOP:**
> 1. **protein:sugar ratio basis** (`1:2 w/w` or `1:2 molar`)
> 2. **RH-equivalent operational method for aw 0.79**
> 3. **ultrasound SOP identifier with acceptance/pass-fail reference**

This is the correct decision because the team was unanimous that these are not minor clerical details; they are scientifically consequential and directly affect donor ranking, process comparability, and interpretability.

I also recommend the following final structural choices:

- **Part A** will hold locked constants and deferred variables.
- **Part B** will remain a lean but comparator-aware process-run table.
- **Part C** will specify balanced block execution and comparator protection, but not impose a rigid exact within-block order.
- **Part D** will define all-run assays plus pre-assigned and conditional subset assays.
- **Part E** will contain timing rules, naming rules, critical deviations, practical implementation notes, and operator-facing guardrails.

I am also choosing the **grouped assay field approach** in Part B:
- `primary assay(s)`
- `optional assay(s)`

This is preferable to many assay-specific columns because it keeps the run sheet directly usable by wet-lab staff while preserving assay assignment clarity.

Finally, I recommend that the native untreated β-LG reference be tracked in **Part D / assay plan**, not as a Part B process run, because it is an assay control rather than a reaction condition.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a dry-only, matched bridge-and-calibration round under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:
1. determine donor ranking at 4 h under matched dry conditions,
2. compare 55 C vs 60 C within donor at 4 h,
3. test whether 4 h is justified relative to the current 60 C, 2 h benchmark region for lactose and glucose,
4. distinguish sugar-associated observed β-LG IgE-binding reduction from process-only effects using matched 4 h no-sugar controls,
5. generate a clean, comparator-aware dataset for restricted dry-domain decision support.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- Dry-state target: **aw 0.79 using benchmark RH-equivalent conditioning workflow per SOP [LOCK SOP ID/version before release]**
- Protein:sugar ratio: **1:2 [LOCK BEFORE RELEASE as w/w or molar per benchmark SOP]**
- Pretreatment: **Ultrasound ON per SOP [LOCK SOP ID/version before release]**
- Ultrasound status: fixed, not scanned
- Sample deposition/loading geometry: **fixed benchmark SOP**
- Vessel type: **fixed benchmark SOP**
- Pre-equilibration workflow: **fixed benchmark SOP**
- Incubation workflow: **fixed benchmark SOP**
- Cooling/stop workflow: **fixed benchmark SOP**
- Reconstitution/recovery workflow: **fixed benchmark SOP**
- Primary IgE assay platform: **same as benchmark**
- IgE source: **same serum pool / defined source across the round**
- Native untreated β-LG reference: included in assay campaign
- Replication plan: **2 independent full process blocks**

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (process-only controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

### Deferred variables
Not optimized in this round; fixed or excluded:
- wet-state conditions
- pH / buffer
- aw variation
- ratio variation
- ultrasound variation
- other pretreatments
- 3 h intermediate time
- donor-specific no-ultrasound panel
- broader donor expansion
- direct clinical allergenicity assessment

---

## Part B. Master run list

**Important release note:**  
This master run list is execution-ready in structure, but **bench execution must not begin until the following are locked in the packet header**:
- ratio basis (`w/w` or `molar`)
- RH-equivalent SOP ID/version for aw 0.79
- ultrasound SOP ID/version

### Controlled wording for assay columns
- **Primary assay(s):** `Primary IgE; Recovery protein quant; Extractability/solubility; Turbidity/insolubility; Loading normalization verification`
- **Optional assay(s):**
  - Runs 9–12: `Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy`
  - Other runs: `Conditional: top 2 apparent 4 h sugar winners; one high-caution/high-reduction case if distinct; any advancing condition`

| run_id | block_id | group_id | comparison_group | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | matched_control_id | paired_temperature_run_id | paired_time_anchor_run_id | historical_link_flag | sample naming label |
|---|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
| R01 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Lactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | Primary IgE; Recovery protein quant; Extractability/solubility; Turbidity/insolubility; Loading normalization verification | Conditional subset only | R11-B1 | R05-B1 | R09-B1 | No | B1_R01_LAC_55C_4H_SUG |
| R02 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Glucose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R06-B1 | R10-B1 | No | B1_R02_GLU_55C_4H_SUG |
| R03 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R07-B1 | NA | No | B1_R03_GAL_55C_4H_SUG |
| R04 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R08-B1 | NA | No | B1_R04_MAN_55C_4H_SUG |
| R05 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with lactose 2 h anchor | Lactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R01-B1 | R09-B1 | No | B1_R05_LAC_60C_4H_SUG |
| R06 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with glucose 2 h anchor | Glucose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R02-B1 | R10-B1 | No | B1_R06_GLU_60C_4H_SUG |
| R07 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R03-B1 | NA | No | B1_R07_GAL_60C_4H_SUG |
| R08 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R04-B1 | NA | No | B1_R08_MAN_60C_4H_SUG |
| R09 | B1 | G-TIME-LAC | time_bridge_lactose | Historical benchmark-linked lactose anchor for 2 h vs 4 h bridge | Lactose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B1 | R05-B1 | NA | Yes | B1_R09_LAC_60C_2H_ANC |
| R10 | B1 | G-TIME-GLU | time_bridge_glucose | Historical benchmark-linked glucose anchor for 2 h vs 4 h bridge | Glucose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B1 | R06-B1 | NA | Yes | B1_R10_GLU_60C_2H_ANC |
| R11 | B1 | G-CTRL55 | process_only_55C | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B1_R11_NOSUG_55C_4H_CTL |
| R12 | B1 | G-CTRL60 | process_only_60C | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B1_R12_NOSUG_60C_4H_CTL |
| R01 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Lactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R05-B2 | R09-B2 | No | B2_R01_LAC_55C_4H_SUG |
| R02 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Glucose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R06-B2 | R10-B2 | No | B2_R02_GLU_55C_4H_SUG |
| R03 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R07-B2 | NA | No | B2_R03_GAL_55C_4H_SUG |
| R04 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R08-B2 | NA | No | B2_R04_MAN_55C_4H_SUG |
| R05 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with lactose 2 h anchor | Lactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R01-B2 | R09-B2 | No | B2_R05_LAC_60C_4H_SUG |
| R06 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with glucose 2 h anchor | Glucose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R02-B2 | R10-B2 | No | B2_R06_GLU_60C_4H_SUG |
| R07 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R03-B2 | NA | No | B2_R07_GAL_60C_4H_SUG |
| R08 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R04-B2 | NA | No | B2_R08_MAN_60C_4H_SUG |
| R09 | B2 | G-TIME-LAC | time_bridge_lactose | Historical benchmark-linked lactose anchor for 2 h vs 4 h bridge | Lactose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B2 | R05-B2 | NA | Yes | B2_R09_LAC_60C_2H_ANC |
| R10 | B2 | G-TIME-GLU | time_bridge_glucose | Historical benchmark-linked glucose anchor for 2 h vs 4 h bridge | Glucose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B2 | R06-B2 | NA | Yes | B2_R10_GLU_60C_2H_ANC |
| R11 | B2 | G-CTRL55 | process_only_55C | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B2_R11_NOSUG_55C_4H_CTL |
| R12 | B2 | G-CTRL60 | process_only_60C | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B2_R12_NOSUG_60C_4H_CTL |

---

## Part C. Batch execution plan

### Batch grouping
- **Preferred execution:** 2 independent full process blocks
  - **Block 1:** all 12 runs B1_R01–B1_R12
  - **Block 2:** all 12 runs B2_R01–B2_R12
- Each block must contain the full 12-condition matrix.

### Which runs should be processed together
- All 12 runs within a block should be prepared and processed under the same coordinated campaign whenever feasible.
- Do **not** split blocks by donor or by temperature into isolated mini-batches.
- If staggered handling is required, use a balanced order that intersperses:
  - 55 C and 60 C runs
  - sugar and no-sugar runs
  - anchors and bridge runs

### Matched-comparison grouping
- **55 C donor ranking group:** R01–R04 vs matched control R11 within each block
- **60 C donor ranking group:** R05–R08 vs matched control R12 within each block
- **Lactose time bridge:** R05 vs R09 within each block
- **Glucose time bridge:** R06 vs R10 within each block
- **Temperature pairs within donor:**
  - lactose: R01 vs R05
  - glucose: R02 vs R06
  - galactose: R03 vs R07
  - mannose: R04 vs R08
- **Protected comparator spine:** R09, R10, R11, R12 in each block

### Randomization / balancing rules
- Randomize chamber position within each block.
- Randomize assay plate placement.
- If multiple plates are required, distribute protected comparators across plates.
- Avoid placing all controls at the start or end only.
- Record chamber/incubator ID and position for every run.

### Contingency plan — use only if full second block cannot be executed

| contingency priority | run selection |
|---|---|
| 1 | R09 lactose 60 C 2 h anchor |
| 2 | R10 glucose 60 C 2 h anchor |
| 3 | R11 no-sugar 55 C 4 h control |
| 4 | R12 no-sugar 60 C 4 h control |
| 5 | top 2 apparent 4 h sugar conditions from block 1 |
| 6 | one additional high-caution/high-reduction condition if distinct |

---

## Part D. Assay plan

### Assays required for all runs
Apply to all 24 process runs:
1. **Primary β-LG IgE-binding assay**
   - same platform as benchmark
   - same IgE source across the round
2. **Recovered protein quantification**
3. **Extractability / solubility assessment**
   - recovered volume
   - reconstitution difficulty
   - visible insoluble residue
4. **Turbidity / insolubility flag**
5. **Loading normalization verification**
   - assay input normalized on recovered-protein basis

### Native untreated β-LG reference
- Include in the assay campaign as assay control.
- If multiple plates are used:
  - include on each plate or
  - use a defined plate-linking/bridging scheme.

### Selected runs for orthogonal confirmation
**Pre-assigned mandatory subset**
- R09 and R10 in both blocks
- R11 and R12 in both blocks

These receive:
- non-IgE β-LG detectability
- orthogonal IgE-binding assay with different antigen-presentation mode
- free lysine proxy preferred

### Conditional orthogonal / interpretation-support subset
After first-pass review, add:
- top 2 apparent 4 h sugar winners
- one high-caution/high-reduction sugar condition if distinct
- any condition proposed for advancement

### Plate protection rules
If multiple assay plates are required:
- distribute R09–R12 across plates or use a defined bridging layout
- include native untreated β-LG reference on each plate or equivalent validated bridge

### Interpretation-support triggers
Escalate for adjudication if any of the following occur:
- unexpectedly strong reduction in no-sugar control
- severe turbidity / particulate carryover
- large reduction with poor recovery
- major drop in non-IgE β-LG detectability
- disagreement between primary and orthogonal IgE assay formats

---

## Part E. Execution notes

### Parameter definitions
- **Protein:** β-LG variant A
- **Mode:** Dry-state glycation only
- **Protein:sugar ratio:** 1:2 **[LOCK BEFORE RELEASE as w/w or molar]**
- **Dry-state condition:** target aw 0.79 using benchmark RH-equivalent conditioning workflow per SOP **[LOCK SOP ID/version before release]**
- **Pretreatment:** Ultrasound ON per benchmark SOP **[LOCK SOP ID/version before release]**
- **Sample loading/geometry:** fixed benchmark deposition and vessel geometry per SOP; use identical loaded mass, vessel type, and sample format across all runs; no deviations without approval

### Timing rules
- **Reaction time starts when the sample is placed into the pre-equilibrated incubation environment at the assigned temperature and ends at physical removal from that environment for immediate stop/cooling per SOP.**
- Record actual equilibration start/stop and incubation start/stop for every run.
- Do not delay cooling/stop after removal.

### Control rules
- R11 is the matched 55 C 4 h no-sugar comparator.
- R12 is the matched 60 C 4 h no-sugar comparator.
- R09 and R10 are same-round time anchors and must be protected comparators.
- No sugar condition may be interpreted without its matched same-temperature no-sugar control.
- Lactose and glucose 4 h conditions at 60 C should be interpreted with their 2 h anchors.

### Naming rules
- Format: `B[block]_R[run]_[donor]_[temp]C_[time]H_[status]`
- Status codes:
  - `SUG` = sugar-containing bridge run
  - `ANC` = same-round anchor
  - `CTL` = no-sugar process-only control
- No spaces or special characters.
- Use standardized donor codes:
  - `LAC`, `GLU`, `GAL`, `MAN`, `NOSUG`

### Assay interpretation guardrails
- Primary endpoint is **observed β-LG IgE-binding reduction**, not clinical allergenicity reduction.
- Do not interpret lower IgE signal without recovery-normalized loading confirmation.
- Compare each sugar condition against its matched same-temperature no-sugar control.
- Escalate high-turbidity, low-recovery, or hard-to-reconstitute samples for caution review.
- Advancement requires no major contradiction from detectability or orthogonal confirmation data.

### Dry-state process warning
- Do **not** treat stronger browning, caking, or lower recovery as evidence of better performance.
- These are overprocessing indicators and must be recorded as caution flags.

### Critical deviation / rerun criteria
Rerun or exclude if any of the following occur:
- wrong donor or wrong ratio basis used
- incorrect temperature assignment
- missed or failed ultrasound application
- failed RH/aw control or wrong conditioning workflow
- major timing deviation (>10 min unless pre-approved tolerance defined in SOP)
- gross loading/geometry deviation
- recovery failure
- sample mix-up or labeling uncertainty

### Minimum actuals/QC capture for each run
Record:
- actual protein mass
- actual sugar mass or no-sugar confirmation
- actual loaded mass
- equilibration start/stop
- incubation start/stop
- chamber/incubator ID
- chamber position
- ultrasound pass/fail
- sample appearance
- browning score
- caking/hard-to-redissolve Y/N
- recovered volume
- turbidity flag
- deviation_flag (`None / Minor / Critical`)
- QC_status (`Pending / Pass / Fail`)
- assayable_status (`Pending / Yes / No`)
- trainability_status (`Pending / Yes / No`) — assigned by project QC/analysis review, not bench operator

### Release blockers before execution
Do **not** release to bench until all three are locked:
1. ratio basis
2. RH-equivalent SOP ID/version for aw 0.79
3. ultrasound SOP ID/version and acceptance rule

---

### Next Steps

1. **Lock the three release blockers immediately**
   - protein:sugar ratio basis
   - aw 0.79 RH-equivalent SOP reference
   - ultrasound SOP reference and pass/fail criteria

2. **Convert the draft packet into the lab’s controlled document format**
   - insert SOP IDs/versions
   - insert benchmark lot fields
   - insert any required document control metadata

3. **Prepare companion worksheets**
   - execution log for actual masses/times/appearance/recovery
   - assay plate map including native untreated β-LG reference
   - QC checklist for protected comparators and deviations

4. **Review the packet once with wet-lab operators before release**
   - confirm no field is ambiguous
   - confirm SOPs are accessible at bench
   - confirm naming convention and sample labels are practical

5. **Release and execute the preferred 2-block plan**
   - only if the three hard-stop items are locked
   - otherwise hold as draft and do not start bench work

6. **After block 1**
   - review comparator integrity
   - determine whether contingency plan is needed
   - pre-select any conditional orthogonal subset based on first-pass results

This concludes the meeting recommendation and provides the directly actionable wet-lab run-sheet packet requested by the agenda.
### Agenda

Translate the already approved dry-only β-LG glycation screening design into a **directly executable wet-lab packet**. The goal is not to reopen strategy, but to produce a run-by-run, parameter-complete experiment sheet for the wet-lab team that preserves comparator logic, assay interpretability, and later evidence/model usability. The packet must explicitly specify all fixed and scanned variables, include matched controls and process replicates, define dry-state aw/RH conditions, assign assays, and provide execution/QC rules.

---

### Team Member Input

#### Principal Investigator
- Framed the meeting as **operational translation**, not design revision.
- Reaffirmed the approved design:
  - dry-only
  - β-LG variant A
  - fixed aw backbone
  - fixed 1:2 ratio
  - ultrasound ON
  - 12-condition matrix
  - preferred 2 full independent process blocks
- Identified main execution risks:
  - ambiguous ratio basis
  - ambiguous dry-state control wording
  - insufficient ultrasound definition
  - unclear replicate/block structure
  - unclear assay assignment
  - unclear naming and control handling
- Proposed a final deliverable as a multi-part packet:
  - round summary
  - master run list
  - batch plan
  - assay plan
  - execution/QC notes
- Asked team to focus on process closure, assay assignment, comparator structure, failure modes, and downstream usability.

#### Maillard Reaction Chemistry and Process Scientist
- Strongly agreed the remaining task is **operational closure**.
- Identified critical chemistry/process items that cannot remain implicit:
  1. **Protein:sugar ratio basis must be locked** as either w/w or molar.
  2. **aw 0.79 must be translated into an operational RH-equivalent workflow**.
  3. **Ultrasound must be tied to a fixed SOP and acceptance window**.
  4. **Time-zero and stop rules must be explicit**.
  5. **Sample geometry/loading must be fixed**.
- Recommended the packet use:
  - locked constants in header
  - SOP-linked process wording
  - actuals capture in a companion execution log
- Advised that the run sheet may be drafted now, but **must not be released for execution until ratio basis is locked**.
- Proposed concise execution wording:
  - Dry-state condition: target aw 0.79 using benchmark RH-equivalent workflow per SOP
  - Reaction starts at entry into pre-equilibrated incubation environment and ends at removal for immediate stop/cooling
  - Fixed benchmark deposition and vessel geometry per SOP
- Added a practical warning:
  - browning, caking, and lower recovery are **overprocessing flags**, not success signals.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the packet must pre-wire **interpretability**, not just sample production.
- Stated that lower IgE signal is only useful if distinguished from:
  - poor recovery
  - aggregation
  - altered presentation
  - detectability collapse
  - process-only effects
- Recommended required measurements for **all runs**:
  - primary IgE assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - loading normalization verification
- Recommended **standardized grouped assay columns** in Part B rather than many assay-specific columns.
- Recommended pre-assigned subset assays:
  - runs 9–12 mandatory for non-IgE β-LG detectability
  - runs 9–12 mandatory for orthogonal IgE confirmation
- Conditional subset:
  - top 2 apparent 4 h sugar winners
  - one high-caution/high-reduction case if distinct
  - any advancing condition
- Recommended native untreated β-LG reference be included in **Part D / assay plan**, not as a Part B process run.
- Proposed concise guardrails:
  - primary endpoint is observed IgE-binding reduction, not clinical allergenicity reduction
  - do not interpret lower signal without recovery-normalized loading
  - compare against matched no-sugar controls
  - escalate high-turbidity/low-recovery samples
  - require no major contradiction from detectability or orthogonal data

#### Experimental Design and Evidence Synthesis Scientist
- Emphasized that the packet must preserve **comparison structure** for later synthesis.
- Recommended preferred execution as **2 full independent 12-run process blocks**.
- Strongly recommended fallback confirmation plan be written now but kept separate as a **contingency mini-table**.
- Recommended Part B include essential comparator-link columns:
  - block_id
  - comparison_group
  - matched_control_id
  - paired_temperature_run_id
  - paired_time_anchor_run_id
  - historical_link_flag
- Recommended Part B remain lean but include both:
  - `purpose` for human readability
  - `comparison_group` for analysis readability
- Recommended Part C specify:
  - balancing/randomization principles
  - protected comparator placement
  - not a rigid exact processing order unless already validated
- Warned that comparator links must live in **Part B**, not only Part C.

#### Scientific Critic
- Focused on remaining unsafe-to-release failure points:
  1. unresolved ratio basis
  2. unclear aw/RH operational specification
  3. unclear ultrasound SOP/acceptance
  4. absence of visible critical deviation rules
  5. incomplete comparator structure in Part B
- Supported the proposed sample naming format and requested it remain standardized and free of ambiguous formatting.
- Proposed a short critical deviation box including:
  - wrong donor or ratio basis
  - incorrect temperature
  - missed ultrasound
  - failed RH/aw control
  - major timing deviation
  - recovery failure or sample mix-up
- Recommended a visible QC checklist and a cover-page style summary of key instructions.

#### Research Synthesis and Optimization Lead
- Focused on making the packet useful for both:
  - immediate decision-making
  - downstream restricted-domain model ingestion
- Recommended a **small structured packet**, matching the agenda.
- Recommended one row per **process run**, not assay well.
- Supported comparator-link columns directly in Part B.
- Recommended only a minimal set of post-run placeholders in Part B:
  - deviation_flag
  - QC_status
  - assayable_status
  - trainability_status
- Recommended controlled vocabulary:
  - deviation_flag: None / Minor / Critical
  - QC_status: Pending / Pass / Fail
  - assayable_status: Pending / Yes / No
  - trainability_status: Pending / Yes / No
- Advised against putting downstream interpretation fields like advancement action or orthogonal support into Part B.
- Noted that `trainability_status` should be assigned by project QC/analysis review, not bench operators.

---

### Recommendation

My recommendation is to issue a **five-part wet-lab packet** for the **preferred 2-block execution plan**, with a **24-row master run list** and a separate **contingency mini-table** for fallback replication. The scientific design remains unchanged.

However, I am making one critical governance decision:

> **The packet may be finalized as a draft now, but it must not be released for bench execution until three hard-stop operational constants are locked from the benchmark SOP:**
> 1. **protein:sugar ratio basis** (`1:2 w/w` or `1:2 molar`)
> 2. **RH-equivalent operational method for aw 0.79**
> 3. **ultrasound SOP identifier with acceptance/pass-fail reference**

This is the correct decision because the team was unanimous that these are not minor clerical details; they are scientifically consequential and directly affect donor ranking, process comparability, and interpretability.

I also recommend the following final structural choices:

- **Part A** will hold locked constants and deferred variables.
- **Part B** will remain a lean but comparator-aware process-run table.
- **Part C** will specify balanced block execution and comparator protection, but not impose a rigid exact within-block order.
- **Part D** will define all-run assays plus pre-assigned and conditional subset assays.
- **Part E** will contain timing rules, naming rules, critical deviations, practical implementation notes, and operator-facing guardrails.

I am also choosing the **grouped assay field approach** in Part B:
- `primary assay(s)`
- `optional assay(s)`

This is preferable to many assay-specific columns because it keeps the run sheet directly usable by wet-lab staff while preserving assay assignment clarity.

Finally, I recommend that the native untreated β-LG reference be tracked in **Part D / assay plan**, not as a Part B process run, because it is an assay control rather than a reaction condition.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a dry-only, matched bridge-and-calibration round under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:
1. determine donor ranking at 4 h under matched dry conditions,
2. compare 55 C vs 60 C within donor at 4 h,
3. test whether 4 h is justified relative to the current 60 C, 2 h benchmark region for lactose and glucose,
4. distinguish sugar-associated observed β-LG IgE-binding reduction from process-only effects using matched 4 h no-sugar controls,
5. generate a clean, comparator-aware dataset for restricted dry-domain decision support.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- Dry-state target: **aw 0.79 using benchmark RH-equivalent conditioning workflow per SOP [LOCK SOP ID/version before release]**
- Protein:sugar ratio: **1:2 [LOCK BEFORE RELEASE as w/w or molar per benchmark SOP]**
- Pretreatment: **Ultrasound ON per SOP [LOCK SOP ID/version before release]**
- Ultrasound status: fixed, not scanned
- Sample deposition/loading geometry: **fixed benchmark SOP**
- Vessel type: **fixed benchmark SOP**
- Pre-equilibration workflow: **fixed benchmark SOP**
- Incubation workflow: **fixed benchmark SOP**
- Cooling/stop workflow: **fixed benchmark SOP**
- Reconstitution/recovery workflow: **fixed benchmark SOP**
- Primary IgE assay platform: **same as benchmark**
- IgE source: **same serum pool / defined source across the round**
- Native untreated β-LG reference: included in assay campaign
- Replication plan: **2 independent full process blocks**

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (process-only controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

### Deferred variables
Not optimized in this round; fixed or excluded:
- wet-state conditions
- pH / buffer
- aw variation
- ratio variation
- ultrasound variation
- other pretreatments
- 3 h intermediate time
- donor-specific no-ultrasound panel
- broader donor expansion
- direct clinical allergenicity assessment

---

## Part B. Master run list

**Important release note:**  
This master run list is execution-ready in structure, but **bench execution must not begin until the following are locked in the packet header**:
- ratio basis (`w/w` or `molar`)
- RH-equivalent SOP ID/version for aw 0.79
- ultrasound SOP ID/version

### Controlled wording for assay columns
- **Primary assay(s):** `Primary IgE; Recovery protein quant; Extractability/solubility; Turbidity/insolubility; Loading normalization verification`
- **Optional assay(s):**
  - Runs 9–12: `Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy`
  - Other runs: `Conditional: top 2 apparent 4 h sugar winners; one high-caution/high-reduction case if distinct; any advancing condition`

| run_id | block_id | group_id | comparison_group | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | matched_control_id | paired_temperature_run_id | paired_time_anchor_run_id | historical_link_flag | sample naming label |
|---|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
| R01 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Lactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | Primary IgE; Recovery protein quant; Extractability/solubility; Turbidity/insolubility; Loading normalization verification | Conditional subset only | R11-B1 | R05-B1 | R09-B1 | No | B1_R01_LAC_55C_4H_SUG |
| R02 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Glucose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R06-B1 | R10-B1 | No | B1_R02_GLU_55C_4H_SUG |
| R03 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R07-B1 | NA | No | B1_R03_GAL_55C_4H_SUG |
| R04 | B1 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R11-B1 | R08-B1 | NA | No | B1_R04_MAN_55C_4H_SUG |
| R05 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with lactose 2 h anchor | Lactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R01-B1 | R09-B1 | No | B1_R05_LAC_60C_4H_SUG |
| R06 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with glucose 2 h anchor | Glucose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R02-B1 | R10-B1 | No | B1_R06_GLU_60C_4H_SUG |
| R07 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R03-B1 | NA | No | B1_R07_GAL_60C_4H_SUG |
| R08 | B1 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Conditional subset only | R12-B1 | R04-B1 | NA | No | B1_R08_MAN_60C_4H_SUG |
| R09 | B1 | G-TIME-LAC | time_bridge_lactose | Historical benchmark-linked lactose anchor for 2 h vs 4 h bridge | Lactose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B1 | R05-B1 | NA | Yes | B1_R09_LAC_60C_2H_ANC |
| R10 | B1 | G-TIME-GLU | time_bridge_glucose | Historical benchmark-linked glucose anchor for 2 h vs 4 h bridge | Glucose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B1 | R06-B1 | NA | Yes | B1_R10_GLU_60C_2H_ANC |
| R11 | B1 | G-CTRL55 | process_only_55C | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B1_R11_NOSUG_55C_4H_CTL |
| R12 | B1 | G-CTRL60 | process_only_60C | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P1 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B1_R12_NOSUG_60C_4H_CTL |
| R01 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Lactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R05-B2 | R09-B2 | No | B2_R01_LAC_55C_4H_SUG |
| R02 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Glucose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R06-B2 | R10-B2 | No | B2_R02_GLU_55C_4H_SUG |
| R03 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R07-B2 | NA | No | B2_R03_GAL_55C_4H_SUG |
| R04 | B2 | G-DONOR55 | donor_ranking_55C | 55 C donor ranking; matched to 55 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R11-B2 | R08-B2 | NA | No | B2_R04_MAN_55C_4H_SUG |
| R05 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with lactose 2 h anchor | Lactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R01-B2 | R09-B2 | No | B2_R05_LAC_60C_4H_SUG |
| R06 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; paired with glucose 2 h anchor | Glucose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R02-B2 | R10-B2 | No | B2_R06_GLU_60C_4H_SUG |
| R07 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R03-B2 | NA | No | B2_R07_GAL_60C_4H_SUG |
| R08 | B2 | G-DONOR60 | donor_ranking_60C | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [LOCK] | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Conditional subset only | R12-B2 | R04-B2 | NA | No | B2_R08_MAN_60C_4H_SUG |
| R09 | B2 | G-TIME-LAC | time_bridge_lactose | Historical benchmark-linked lactose anchor for 2 h vs 4 h bridge | Lactose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B2 | R05-B2 | NA | Yes | B2_R09_LAC_60C_2H_ANC |
| R10 | B2 | G-TIME-GLU | time_bridge_glucose | Historical benchmark-linked glucose anchor for 2 h vs 4 h bridge | Glucose | 1:2 [LOCK] | Dry | 60 | 2 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | Sugar | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | R12-B2 | R06-B2 | NA | Yes | B2_R10_GLU_60C_2H_ANC |
| R11 | B2 | G-CTRL55 | process_only_55C | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B2_R11_NOSUG_55C_4H_CTL |
| R12 | B2 | G-CTRL60 | process_only_60C | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 via benchmark RH-equivalent SOP [LOCK] | Ultrasound ON SOP [LOCK] | No-sugar control | P2 | same as above | Non-IgE β-LG detectability; Orthogonal IgE format; Free lysine proxy | NA | NA | NA | No | B2_R12_NOSUG_60C_4H_CTL |

---

## Part C. Batch execution plan

### Batch grouping
- **Preferred execution:** 2 independent full process blocks
  - **Block 1:** all 12 runs B1_R01–B1_R12
  - **Block 2:** all 12 runs B2_R01–B2_R12
- Each block must contain the full 12-condition matrix.

### Which runs should be processed together
- All 12 runs within a block should be prepared and processed under the same coordinated campaign whenever feasible.
- Do **not** split blocks by donor or by temperature into isolated mini-batches.
- If staggered handling is required, use a balanced order that intersperses:
  - 55 C and 60 C runs
  - sugar and no-sugar runs
  - anchors and bridge runs

### Matched-comparison grouping
- **55 C donor ranking group:** R01–R04 vs matched control R11 within each block
- **60 C donor ranking group:** R05–R08 vs matched control R12 within each block
- **Lactose time bridge:** R05 vs R09 within each block
- **Glucose time bridge:** R06 vs R10 within each block
- **Temperature pairs within donor:**
  - lactose: R01 vs R05
  - glucose: R02 vs R06
  - galactose: R03 vs R07
  - mannose: R04 vs R08
- **Protected comparator spine:** R09, R10, R11, R12 in each block

### Randomization / balancing rules
- Randomize chamber position within each block.
- Randomize assay plate placement.
- If multiple plates are required, distribute protected comparators across plates.
- Avoid placing all controls at the start or end only.
- Record chamber/incubator ID and position for every run.

### Contingency plan — use only if full second block cannot be executed

| contingency priority | run selection |
|---|---|
| 1 | R09 lactose 60 C 2 h anchor |
| 2 | R10 glucose 60 C 2 h anchor |
| 3 | R11 no-sugar 55 C 4 h control |
| 4 | R12 no-sugar 60 C 4 h control |
| 5 | top 2 apparent 4 h sugar conditions from block 1 |
| 6 | one additional high-caution/high-reduction condition if distinct |

---

## Part D. Assay plan

### Assays required for all runs
Apply to all 24 process runs:
1. **Primary β-LG IgE-binding assay**
   - same platform as benchmark
   - same IgE source across the round
2. **Recovered protein quantification**
3. **Extractability / solubility assessment**
   - recovered volume
   - reconstitution difficulty
   - visible insoluble residue
4. **Turbidity / insolubility flag**
5. **Loading normalization verification**
   - assay input normalized on recovered-protein basis

### Native untreated β-LG reference
- Include in the assay campaign as assay control.
- If multiple plates are used:
  - include on each plate or
  - use a defined plate-linking/bridging scheme.

### Selected runs for orthogonal confirmation
**Pre-assigned mandatory subset**
- R09 and R10 in both blocks
- R11 and R12 in both blocks

These receive:
- non-IgE β-LG detectability
- orthogonal IgE-binding assay with different antigen-presentation mode
- free lysine proxy preferred

### Conditional orthogonal / interpretation-support subset
After first-pass review, add:
- top 2 apparent 4 h sugar winners
- one high-caution/high-reduction sugar condition if distinct
- any condition proposed for advancement

### Plate protection rules
If multiple assay plates are required:
- distribute R09–R12 across plates or use a defined bridging layout
- include native untreated β-LG reference on each plate or equivalent validated bridge

### Interpretation-support triggers
Escalate for adjudication if any of the following occur:
- unexpectedly strong reduction in no-sugar control
- severe turbidity / particulate carryover
- large reduction with poor recovery
- major drop in non-IgE β-LG detectability
- disagreement between primary and orthogonal IgE assay formats

---

## Part E. Execution notes

### Parameter definitions
- **Protein:** β-LG variant A
- **Mode:** Dry-state glycation only
- **Protein:sugar ratio:** 1:2 **[LOCK BEFORE RELEASE as w/w or molar]**
- **Dry-state condition:** target aw 0.79 using benchmark RH-equivalent conditioning workflow per SOP **[LOCK SOP ID/version before release]**
- **Pretreatment:** Ultrasound ON per benchmark SOP **[LOCK SOP ID/version before release]**
- **Sample loading/geometry:** fixed benchmark deposition and vessel geometry per SOP; use identical loaded mass, vessel type, and sample format across all runs; no deviations without approval

### Timing rules
- **Reaction time starts when the sample is placed into the pre-equilibrated incubation environment at the assigned temperature and ends at physical removal from that environment for immediate stop/cooling per SOP.**
- Record actual equilibration start/stop and incubation start/stop for every run.
- Do not delay cooling/stop after removal.

### Control rules
- R11 is the matched 55 C 4 h no-sugar comparator.
- R12 is the matched 60 C 4 h no-sugar comparator.
- R09 and R10 are same-round time anchors and must be protected comparators.
- No sugar condition may be interpreted without its matched same-temperature no-sugar control.
- Lactose and glucose 4 h conditions at 60 C should be interpreted with their 2 h anchors.

### Naming rules
- Format: `B[block]_R[run]_[donor]_[temp]C_[time]H_[status]`
- Status codes:
  - `SUG` = sugar-containing bridge run
  - `ANC` = same-round anchor
  - `CTL` = no-sugar process-only control
- No spaces or special characters.
- Use standardized donor codes:
  - `LAC`, `GLU`, `GAL`, `MAN`, `NOSUG`

### Assay interpretation guardrails
- Primary endpoint is **observed β-LG IgE-binding reduction**, not clinical allergenicity reduction.
- Do not interpret lower IgE signal without recovery-normalized loading confirmation.
- Compare each sugar condition against its matched same-temperature no-sugar control.
- Escalate high-turbidity, low-recovery, or hard-to-reconstitute samples for caution review.
- Advancement requires no major contradiction from detectability or orthogonal confirmation data.

### Dry-state process warning
- Do **not** treat stronger browning, caking, or lower recovery as evidence of better performance.
- These are overprocessing indicators and must be recorded as caution flags.

### Critical deviation / rerun criteria
Rerun or exclude if any of the following occur:
- wrong donor or wrong ratio basis used
- incorrect temperature assignment
- missed or failed ultrasound application
- failed RH/aw control or wrong conditioning workflow
- major timing deviation (>10 min unless pre-approved tolerance defined in SOP)
- gross loading/geometry deviation
- recovery failure
- sample mix-up or labeling uncertainty

### Minimum actuals/QC capture for each run
Record:
- actual protein mass
- actual sugar mass or no-sugar confirmation
- actual loaded mass
- equilibration start/stop
- incubation start/stop
- chamber/incubator ID
- chamber position
- ultrasound pass/fail
- sample appearance
- browning score
- caking/hard-to-redissolve Y/N
- recovered volume
- turbidity flag
- deviation_flag (`None / Minor / Critical`)
- QC_status (`Pending / Pass / Fail`)
- assayable_status (`Pending / Yes / No`)
- trainability_status (`Pending / Yes / No`) — assigned by project QC/analysis review, not bench operator

### Release blockers before execution
Do **not** release to bench until all three are locked:
1. ratio basis
2. RH-equivalent SOP ID/version for aw 0.79
3. ultrasound SOP ID/version and acceptance rule

---

### Next Steps

1. **Lock the three release blockers immediately**
   - protein:sugar ratio basis
   - aw 0.79 RH-equivalent SOP reference
   - ultrasound SOP reference and pass/fail criteria

2. **Convert the draft packet into the lab’s controlled document format**
   - insert SOP IDs/versions
   - insert benchmark lot fields
   - insert any required document control metadata

3. **Prepare companion worksheets**
   - execution log for actual masses/times/appearance/recovery
   - assay plate map including native untreated β-LG reference
   - QC checklist for protected comparators and deviations

4. **Review the packet once with wet-lab operators before release**
   - confirm no field is ambiguous
   - confirm SOPs are accessible at bench
   - confirm naming convention and sample labels are practical

5. **Release and execute the preferred 2-block plan**
   - only if the three hard-stop items are locked
   - otherwise hold as draft and do not start bench work

6. **After block 1**
   - review comparator integrity
   - determine whether contingency plan is needed
   - pre-select any conditional orthogonal subset based on first-pass results

This concludes the meeting recommendation and provides the directly actionable wet-lab run-sheet packet requested by the agenda.

[end summary 2]

[begin summary 3]

### Agenda

We needed to convert the already approved **dry-only 12-condition bridge-and-calibration design** for β-LG variant A into a **directly executable wet-lab run sheet**. The purpose was not to redesign the science, but to produce a **parameter-complete, run-by-run, operationally clear experiment list** for the wet-lab team, including fixed conditions, explicit controls, replication, batching, assay assignments, and execution notes. The final output had to be organized as Parts A–E and remain consistent with the project’s restricted claim boundary: **observed β-LG IgE-binding reduction under a controlled dry-state framework**, not direct clinical allergenicity reduction.

---

### Team Member Input

#### Maillard Reaction Chemistry and Process Scientist
- Strongly supported keeping the scientific design unchanged and focusing on execution clarity.
- Recommended that the dry-state condition be specified in **two layers**:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark-matched RH/pre-equilibration equivalent**
- Emphasized that the run sheet must explicitly control **physical state**, including:
  - deposition format
  - vessel/substrate type
  - solids loading
  - drying/pre-equilibration workflow
  - humidity-control sequence
  - time-zero rule
  - stop/cooling rule
  - recovery workflow
- Identified the **1:2 ratio basis** as a true blocker unless benchmark convention is confirmed.
- Recommended **hard-stop placeholder language** if benchmark-dependent fields are still unresolved in draft form.
- Preferred wording for dry implementation:
  - **“Samples pre-equilibrated to target RH, then reacted under benchmark dry-incubation SOP.”**
- Advised that **planned high caution** should apply to **60 C / 4 h monosaccharide runs** only, not lactose 60 C / 4 h.
- Recommended explicit Part E wording for:
  - time zero
  - stop rule
  - physical-state recording
  - recovery consistency

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the wet-lab sheet must generate **interpretable immunoassay inputs**, not just processed samples.
- Recommended the following as **mandatory for all runs**:
  - primary β-LG IgE-binding assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - loading normalization verification
- Recommended **non-IgE β-LG detectability** as:
  - preferred on all runs if feasible
  - mandatory for anchors, no-sugar controls, top apparent 4 h conditions, high-caution hits, and advancing conditions
- Strongly supported automatic inclusion of **both no-sugar controls in both blocks** in the mandatory detectability subset.
- Recommended that **assayability status** be captured as a **post-recovery field**, not a planned run-table column.
- Supported keeping **anchor/control status visible in sample labels**.
- Supported planned high caution for the **60 C / 4 h monosaccharides only**.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly recommended generating an **explicit 24-run master list**, not a 12-run list with repeat instructions.
- Emphasized that the two repeats are **independent process blocks**, not generic replicates.
- Recommended that each block contain **all 12 conditions**.
- Called for **restricted randomization**, not vague randomization:
  - randomize prep order, chamber position, and assay plate position within block
  - do not group entirely by donor, temperature, or control class
  - distribute anchors and no-sugar controls as protected comparators
- Recommended **separate randomized orders for Block 1 and Block 2**, not reusing the same order.
- Recommended explicit comparator mapping in Part C:
  - 55 C sugar runs matched to 55 C no-sugar within block
  - 60 C sugar runs matched to 60 C no-sugar within block
  - lactose 60 C 4 h matched to lactose 60 C 2 h within block
  - glucose 60 C 4 h matched to glucose 60 C 2 h within block
  - cross-block comparison used for replication, not as a substitute for within-block matching
- Recommended defining anchors and no-sugar controls as **protected comparator runs**.

#### Scientific Critic
- Reiterated that the biggest remaining execution blockers were:
  1. unresolved **ratio basis**
  2. unresolved **RH-equivalent implementation**
  3. unresolved **ultrasound operational details**
- Warned against leaving operational terms scientifically precise but practically vague.
- Supported concise contingency handling in the run sheet, with fuller governance elsewhere.
- Recommended final verification before handoff:
  - placeholders resolved
  - SOPs verified
  - calibration/reagent quality/equipment readiness checked
- Supported keeping execution notes concise and action-oriented.

#### Research Synthesis and Optimization Lead
- Strongly supported the requested five-part output structure.
- Recommended making the run sheet both **execution-facing and analysis-ready**.
- Supported explicit **24-run structure** with three identity layers:
  - **condition_id**
  - **run_id**
  - **sample label**
- Proposed a final Part B schema with explicit comparator fields.
- Recommended sample-label syntax:
  - **[Block]-[Donor]-[Temp]-[Time]-[Status]**
- Recommended that **planned high caution** be binary and limited to:
  - glucose 60 C 4 h
  - galactose 60 C 4 h
  - mannose 60 C 4 h
- Recommended keeping Part B free of post-run fields like assayability status or results.

---

### Recommendation

My recommendation is to proceed with a **24-run, two-block, dry-only wet-lab run sheet** built directly from the approved 12-condition design, with all fixed conditions explicitly locked and all comparator relationships preserved. This is the correct and minimal execution-ready structure.

However, I am also making one critical governance decision:

> **The run sheet can be generated now, but it must be marked DRAFT / NOT FOR EXECUTION until three benchmark-dependent fields are resolved:**
> 1. **protein:sugar ratio basis**: w/w vs molar  
> 2. **operational RH-equivalent / salt-equivalent condition** corresponding to aw 0.79  
> 3. **benchmark pre-equilibration duration**

This is the only scientifically honest way to satisfy the “no critical parameter left blank” requirement while also acknowledging that these three fields were not numerically provided in the planning summary.

I am choosing the following final positions:

- **Design**: unchanged 12-condition dry-only matrix
- **Replication**: 2 full independent process blocks, listed explicitly as 24 runs
- **Dry-state wording**:
  - target aw = 0.79
  - samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP
- **Planned high caution**:
  - YES for glucose 60 C 4 h, galactose 60 C 4 h, mannose 60 C 4 h
  - NO for lactose 60 C 4 h, though it will be monitored as anchor-linked extended-time condition
- **Mandatory all-run assay package**: Tier A for all 24 runs
- **Non-IgE β-LG detectability**:
  - preferred on all runs
  - mandatory for anchors, no-sugar controls, top apparent 4 h hits, high-caution/high-reduction runs, and advancing conditions
- **Comparator logic**: explicitly encoded in Part B and Part C
- **Randomization**: restricted and block-specific
- **Naming**: machine-parsable bench labels with anchor/control status visible

This recommendation is justified because it best preserves:
- execution clarity
- comparator integrity
- assay interpretability
- downstream synthesis value
- and the project’s safety/practicality principle around reaction time

Below is the resulting wet-lab run sheet.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw backbone to:
1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the current **60 C, 2 h** benchmark region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-linked dataset for restricted-domain evidence synthesis and future AI-supported decision support.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry**
- Target aw: **0.79**
- Operational humidity implementation: **samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP**
- Protein:sugar ratio: **1:2**
- Ratio basis: **DRAFT placeholder until benchmark confirmed**
  - `1:2 [RATIO BASIS PENDING — must match historical benchmark convention exactly; enter w/w or molar before execution approval]`
- Pretreatment: **Ultrasound ON**
- Ultrasound execution: fixed per benchmark SOP; see Part E
- Sample preparation route: one benchmark SOP
- Deposition/sample geometry: fixed benchmark SOP
- Pre-equilibration workflow: fixed benchmark SOP
- Incubation workflow: fixed benchmark SOP
- Cooling/stop procedure: fixed benchmark SOP
- Recovery/reconstitution workflow: fixed benchmark SOP
- Primary assay format: benchmark-matched β-LG IgE-binding assay
- Same IgE source / serum pool across round
- Same untreated/native β-LG reference across analytical campaign
- Same β-LG lot if feasible
- Same donor lots/grades if feasible

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (no-sugar controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for same-round lactose and glucose anchors at 60 C

### Deferred variables
- Wet-state experiments
- pH/buffer
- aw variation
- RH variation beyond benchmark-matched implementation
- ratio optimization
- ultrasound variation
- no-ultrasound controls
- other pretreatments
- 3 h intermediate time
- broader sugar expansion beyond the 4 selected donors

### Execution approval status
**DRAFT ONLY — NOT FOR LAB EXECUTION until the following benchmark-dependent fields are confirmed and entered:**
1. ratio basis (**w/w or molar**)
2. operational RH/salt-equivalent corresponding to aw 0.79
3. benchmark pre-equilibration duration

---

## Part B. Master run list

| run_id | group_id | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| R01 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-LAC-55C-4H-SUG |
| R02 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-GLU-55C-4H-SUG |
| R03 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-GAL-55C-4H-SUG |
| R04 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-MAN-55C-4H-SUG |
| R05 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; lactose time bridge vs 2 h anchor; matched to 60 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-LAC-60C-4H-SUG |
| R06 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; glucose time bridge vs 2 h anchor; matched to 60 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-GLU-60C-4H-SUG |
| R07 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-GAL-60C-4H-SUG |
| R08 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-MAN-60C-4H-SUG |
| R09 | G-TIME-LAC-60 | Time bridge anchor for lactose; historical benchmark continuity | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-LAC-60C-2H-ANC |
| R10 | G-TIME-GLU-60 | Time bridge anchor for glucose; historical benchmark continuity | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-GLU-60C-2H-ANC |
| R11 | G-CTRL-55-4H | Process-only control for all 55 C 4 h sugar runs | None | none | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-NS-55C-4H-CTRL |
| R12 | G-CTRL-60-4H | Process-only control for all 60 C 4 h sugar runs | None | none | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-NS-60C-4H-CTRL |
| R13 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-LAC-55C-4H-SUG |
| R14 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-GLU-55C-4H-SUG |
| R15 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-GAL-55C-4H-SUG |
| R16 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-MAN-55C-4H-SUG |
| R17 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; lactose time bridge vs 2 h anchor; matched to 60 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-LAC-60C-4H-SUG |
| R18 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; glucose time bridge vs 2 h anchor; matched to 60 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-GLU-60C-4H-SUG |
| R19 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-GAL-60C-4H-SUG |
| R20 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-MAN-60C-4H-SUG |
| R21 | G-TIME-LAC-60 | Time bridge anchor for lactose; historical benchmark continuity | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-LAC-60C-2H-ANC |
| R22 | G-TIME-GLU-60 | Time bridge anchor for glucose; historical benchmark continuity | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-GLU-60C-2H-ANC |
| R23 | G-CTRL-55-4H | Process-only control for all 55 C 4 h sugar runs | None | none | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-NS-55C-4H-CTRL |
| R24 | G-CTRL-60-4H | Process-only control for all 60 C 4 h sugar runs | None | none | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-NS-60C-4H-CTRL |

---

## Part C. Batch execution plan

### Batch grouping
- **Process Block 1**: R01–R12
- **Process Block 2**: R13–R24
- Each process block must contain **all 12 conditions exactly once**
- Blocks should be run as **independent process realizations**, preferably on separate days or separated execution windows

### Which runs should be processed together
Within each block:
- prepare all 12 runs under one coordinated workflow
- pre-equilibrate all samples under the same benchmark RH-equivalent workflow
- execute 55 C and 60 C conditions in the same block using balanced placement
- recover all samples under the same fixed recovery SOP

### Restricted randomization rule
- Each process block must contain all 12 conditions exactly once.
- Within each block, assign sample preparation order, chamber/incubator position, and assay plate position using restricted randomization.
- Do not group runs entirely by donor, temperature, or control class.
- Distribute anchors and no-sugar controls across chamber positions and assay plates as protected comparators.
- If two temperature environments are used simultaneously, randomize position within each temperature environment and record chamber/incubator ID and position for every run.
- Any deviation from planned placement or order must be documented in the deviation log.
- Use **different randomized prep/placement plans** for Block 1 and Block 2.

### Protected comparator runs
The following are protected comparator runs and should not be dropped or deprioritized:
- R09, R10, R11, R12
- R21, R22, R23, R24

If a protected comparator fails, prioritize rerun/disposition review before interpreting dependent comparison sets.

### Matched-comparison grouping
- **55 C sugar vs process-only**
  - R01, R02, R03, R04 matched to R11 within Block 1
  - R13, R14, R15, R16 matched to R23 within Block 2
- **60 C sugar vs process-only**
  - R05, R06, R07, R08 matched to R12 within Block 1
  - R17, R18, R19, R20 matched to R24 within Block 2
- **Lactose time bridge**
  - R05 matched to R09 within Block 1
  - R17 matched to R21 within Block 2
- **Glucose time bridge**
  - R06 matched to R10 within Block 1
  - R18 matched to R22 within Block 2
- **Cross-block comparison**
  - used for replication/confirmation only
  - not a substitute for within-block matched comparison

### Suggested execution order within each block
Use a separately randomized order for each block, but ensure:
- anchors and no-sugar controls are distributed through prep order
- not all 60 C / 4 h monosaccharide runs are clustered adjacently if avoidable
- chamber position is balanced across comparison classes

---

## Part D. Assay plan

### Assays required for all runs
**Tier A required for all 24 runs**
1. **β-LG IgE-binding assay**
   - benchmark-matched format
   - same IgE source / serum pool across round
   - include untreated/native β-LG reference across analytical campaign
2. **Recovered protein quantification**
3. **Extractability/solubility assessment**
   - recovered volume
   - recovered protein concentration
   - ease of reconstitution
   - visible pellet / insoluble residue
4. **Turbidity/insolubility flag**
5. **Loading normalization verification**
   - recovered-protein basis

### Interpretation-support assays
**Non-IgE β-LG detectability**
- Preferred on all runs if feasible
- Mandatory minimum subset:
  - R09, R10, R11, R12
  - R21, R22, R23, R24
  - top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
  - any high-caution/high-reduction condition
  - any condition proposed for advancement

**Chemistry-side caution subset preferred**
- free lysine proxy on:
  - all anchors
  - all no-sugar controls
  - top 2–4 apparent 4 h winners
  - one distinct high-caution comparator if needed

### Selected runs for orthogonal confirmation
Tier B orthogonal confirmation is **selection-rule based**, not pre-fixed by donor winner identity.

Apply after Tier A review to:
- both anchors in both blocks:
  - R09, R10, R21, R22
- both no-sugar controls in both blocks:
  - R11, R12, R23, R24
- top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
- one additional high-caution apparent reducer if not already included
- optionally one unexpectedly strong no-sugar control if observed

### Tier B orthogonal confirmation package
1. Orthogonal β-LG IgE-binding assay with different antigen-presentation mode
2. Gel-based aggregation/profile check
3. Confirmation of comparable recovered antigen handling

---

## Part E. Execution notes

### Parameter definitions
- **Dry-state implementation**: samples are pre-equilibrated to benchmark RH-equivalent corresponding to target aw 0.79 for the benchmark-defined duration, then incubated under the benchmark dry-incubation SOP. Do not substitute continuous RH-controlled thermal incubation unless this matches the benchmark SOP.
- **Protein:sugar ratio**:
  - Sugar runs: `1:2 [RATIO BASIS PENDING — must match historical benchmark convention exactly; enter w/w or molar before execution approval]`
  - No-sugar controls: none
- **Operational RH-equivalent**:
  - `[BENCHMARK RH / SALT-EQUIVALENT PENDING — enter exact benchmark-matched RH setpoint or salt-system equivalent before execution approval]`
- **Pre-equilibration duration**:
  - `[BENCHMARK PRE-EQUILIBRATION DURATION PENDING — enter exact duration before execution approval]`

### Ultrasound fixed conditions
Enter before execution approval:
- instrument/model: `[REQUIRED]`
- operating frequency: `[REQUIRED]`
- amplitude/power setting: `[REQUIRED]`
- pulse vs continuous: `[REQUIRED]`
- sonication duration: `[REQUIRED]`
- sample volume: `[REQUIRED]`
- vessel type: `[REQUIRED]`
- temperature control method: `[REQUIRED]`

**Ultrasound pass/fail acceptance**
- correct instrument/SOP used
- correct programmed setting range used
- correct duration range used
- no documented temperature excursion beyond SOP limit
- no operator-recorded application failure

### Timing rules
- **Time zero definition**: reaction time begins when samples are placed into a pre-equilibrated incubation environment at target temperature per benchmark SOP.
- **Stop rule**: at end of reaction time, remove samples immediately and apply benchmark cooling/stop procedure without delay.
- Use actual insertion and removal times on run sheet.
- Major timing error is a critical deviation.

### Control rules
- 55 C 4 h sugar runs must be interpreted against matched 55 C 4 h no-sugar control from the same block.
- 60 C 4 h sugar runs must be interpreted against matched 60 C 4 h no-sugar control from the same block.
- Lactose 60 C 4 h must be interpreted against lactose 60 C 2 h anchor from the same block.
- Glucose 60 C 4 h must be interpreted against glucose 60 C 2 h anchor from the same block.
- Cross-block replication supports confirmation; it does not replace within-block comparator logic.

### Naming rules
- Sample-label syntax:
  - **[Block]-[Donor]-[Temp]-[Time]-[Status]**
- Donor codes:
  - LAC = lactose
  - GLU = glucose
  - GAL = galactose
  - MAN = mannose
  - NS = no sugar
- Status codes:
  - SUG = sugar run
  - ANC = anchor
  - CTRL = no-sugar control

### Required process metadata capture
For each run record:
- operator
- process block
- prep date/time
- actual equilibration start/stop
- actual incubation start/stop
- chamber/incubator ID
- chamber position
- RH/aw check if available
- loaded protein mass
- loaded sugar mass
- total solids
- deposition volume
- sample mass before/after if feasible
- visible sample state before and after incubation:
  - free-flowing
  - film
  - caked
  - glassy
  - crystalline
  - browned
  - insoluble on recovery
- reconstitution behavior
- pellet yes/no
- turbidity score
- deviations
- disposition

### Required post-recovery capture fields
- recovered volume
- recovered protein concentration
- dilution factor into assay
- normalized loading concentration
- visible pellet
- turbidity
- storage condition if not assayed immediately
- freeze-thaw count
- **assayability status**:
  - Assayable
  - Assayable with caution
  - Not assayable / hold for disposition

### Planned caution rules
**Planned high caution = YES**
- GLU 60 C 4 h
- GAL 60 C 4 h
- MAN 60 C 4 h
  - R06, R07, R08, R18, R19, R20

**Monitor but not planned high caution**
- LAC 60 C 4 h
  - anchor-linked extended-time condition; monitor for presentation/recovery shifts relative to 2 h anchor

### Critical deviations requiring rerun or exclusion
- wrong donor, time, temperature, or ratio basis
- unresolved ratio basis / RH-equivalent / pre-equilibration duration at execution time
- incorrect or missing ultrasound
- failed dry-state control
- major timing error
- grossly inconsistent sample geometry/loading
- sample mix-up or labeling uncertainty
- recovery failure making interpretation impossible

### Concise contingency rules
- **Critical deviation**: stop, flag, notify PI or delegated study lead, hold sample for disposition, do not enter into model-building dataset unless formally rescued.
- **Noncritical deviation**: document, continue if sample remains valid, flag for caution in interpretation.
- **Rerun authority**: PI or delegated study lead after deviation review.

### Pre-execution verification checklist
Before execution approval confirm:
1. ratio basis entered and benchmark-matched
2. RH/salt-equivalent entered and benchmark-matched
3. pre-equilibration duration entered and benchmark-matched
4. ultrasound settings entered
5. SOPs current and verified
6. instrument calibration status current
7. reagent/donor lots recorded
8. assay reagents and IgE source confirmed for round consistency

---

### Next Steps

1. **Resolve the three blocking benchmark-dependent fields immediately**
   - ratio basis: w/w or molar
   - RH/salt-equivalent for aw 0.79
   - pre-equilibration duration

2. **Populate Part E ultrasound fields from the benchmark SOP**
   - instrument/model
   - frequency
   - amplitude/power
   - pulse mode
   - duration
   - sample volume
   - vessel type
   - temperature-control method

3. **Convert this draft into execution-approved version**
   - remove all pending placeholders
   - verify against benchmark record
   - sign off PI/designee approval

4. **Generate block-specific randomized prep and placement maps**
   - one for Block 1
   - one independently randomized for Block 2

5. **Prepare assay plate plan**
   - distribute anchors and no-sugar controls across plates
   - include native untreated β-LG reference throughout analytical campaign

6. **Issue final handoff packet to wet-lab team**
   - execution-approved run sheet
   - associated SOP references
   - deviation log form
   - metadata capture form
   - post-recovery assayability/QC form

This is my final recommendation and the execution-ready draft output for this stage.
### Agenda

We needed to convert the already approved **dry-only 12-condition bridge-and-calibration design** for β-LG variant A into a **directly executable wet-lab run sheet**. The purpose was not to redesign the science, but to produce a **parameter-complete, run-by-run, operationally clear experiment list** for the wet-lab team, including fixed conditions, explicit controls, replication, batching, assay assignments, and execution notes. The final output had to be organized as Parts A–E and remain consistent with the project’s restricted claim boundary: **observed β-LG IgE-binding reduction under a controlled dry-state framework**, not direct clinical allergenicity reduction.

---

### Team Member Input

#### Maillard Reaction Chemistry and Process Scientist
- Strongly supported keeping the scientific design unchanged and focusing on execution clarity.
- Recommended that the dry-state condition be specified in **two layers**:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark-matched RH/pre-equilibration equivalent**
- Emphasized that the run sheet must explicitly control **physical state**, including:
  - deposition format
  - vessel/substrate type
  - solids loading
  - drying/pre-equilibration workflow
  - humidity-control sequence
  - time-zero rule
  - stop/cooling rule
  - recovery workflow
- Identified the **1:2 ratio basis** as a true blocker unless benchmark convention is confirmed.
- Recommended **hard-stop placeholder language** if benchmark-dependent fields are still unresolved in draft form.
- Preferred wording for dry implementation:
  - **“Samples pre-equilibrated to target RH, then reacted under benchmark dry-incubation SOP.”**
- Advised that **planned high caution** should apply to **60 C / 4 h monosaccharide runs** only, not lactose 60 C / 4 h.
- Recommended explicit Part E wording for:
  - time zero
  - stop rule
  - physical-state recording
  - recovery consistency

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the wet-lab sheet must generate **interpretable immunoassay inputs**, not just processed samples.
- Recommended the following as **mandatory for all runs**:
  - primary β-LG IgE-binding assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - loading normalization verification
- Recommended **non-IgE β-LG detectability** as:
  - preferred on all runs if feasible
  - mandatory for anchors, no-sugar controls, top apparent 4 h conditions, high-caution hits, and advancing conditions
- Strongly supported automatic inclusion of **both no-sugar controls in both blocks** in the mandatory detectability subset.
- Recommended that **assayability status** be captured as a **post-recovery field**, not a planned run-table column.
- Supported keeping **anchor/control status visible in sample labels**.
- Supported planned high caution for the **60 C / 4 h monosaccharides only**.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly recommended generating an **explicit 24-run master list**, not a 12-run list with repeat instructions.
- Emphasized that the two repeats are **independent process blocks**, not generic replicates.
- Recommended that each block contain **all 12 conditions**.
- Called for **restricted randomization**, not vague randomization:
  - randomize prep order, chamber position, and assay plate position within block
  - do not group entirely by donor, temperature, or control class
  - distribute anchors and no-sugar controls as protected comparators
- Recommended **separate randomized orders for Block 1 and Block 2**, not reusing the same order.
- Recommended explicit comparator mapping in Part C:
  - 55 C sugar runs matched to 55 C no-sugar within block
  - 60 C sugar runs matched to 60 C no-sugar within block
  - lactose 60 C 4 h matched to lactose 60 C 2 h within block
  - glucose 60 C 4 h matched to glucose 60 C 2 h within block
  - cross-block comparison used for replication, not as a substitute for within-block matching
- Recommended defining anchors and no-sugar controls as **protected comparator runs**.

#### Scientific Critic
- Reiterated that the biggest remaining execution blockers were:
  1. unresolved **ratio basis**
  2. unresolved **RH-equivalent implementation**
  3. unresolved **ultrasound operational details**
- Warned against leaving operational terms scientifically precise but practically vague.
- Supported concise contingency handling in the run sheet, with fuller governance elsewhere.
- Recommended final verification before handoff:
  - placeholders resolved
  - SOPs verified
  - calibration/reagent quality/equipment readiness checked
- Supported keeping execution notes concise and action-oriented.

#### Research Synthesis and Optimization Lead
- Strongly supported the requested five-part output structure.
- Recommended making the run sheet both **execution-facing and analysis-ready**.
- Supported explicit **24-run structure** with three identity layers:
  - **condition_id**
  - **run_id**
  - **sample label**
- Proposed a final Part B schema with explicit comparator fields.
- Recommended sample-label syntax:
  - **[Block]-[Donor]-[Temp]-[Time]-[Status]**
- Recommended that **planned high caution** be binary and limited to:
  - glucose 60 C 4 h
  - galactose 60 C 4 h
  - mannose 60 C 4 h
- Recommended keeping Part B free of post-run fields like assayability status or results.

---

### Recommendation

My recommendation is to proceed with a **24-run, two-block, dry-only wet-lab run sheet** built directly from the approved 12-condition design, with all fixed conditions explicitly locked and all comparator relationships preserved. This is the correct and minimal execution-ready structure.

However, I am also making one critical governance decision:

> **The run sheet can be generated now, but it must be marked DRAFT / NOT FOR EXECUTION until three benchmark-dependent fields are resolved:**
> 1. **protein:sugar ratio basis**: w/w vs molar  
> 2. **operational RH-equivalent / salt-equivalent condition** corresponding to aw 0.79  
> 3. **benchmark pre-equilibration duration**

This is the only scientifically honest way to satisfy the “no critical parameter left blank” requirement while also acknowledging that these three fields were not numerically provided in the planning summary.

I am choosing the following final positions:

- **Design**: unchanged 12-condition dry-only matrix
- **Replication**: 2 full independent process blocks, listed explicitly as 24 runs
- **Dry-state wording**:
  - target aw = 0.79
  - samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP
- **Planned high caution**:
  - YES for glucose 60 C 4 h, galactose 60 C 4 h, mannose 60 C 4 h
  - NO for lactose 60 C 4 h, though it will be monitored as anchor-linked extended-time condition
- **Mandatory all-run assay package**: Tier A for all 24 runs
- **Non-IgE β-LG detectability**:
  - preferred on all runs
  - mandatory for anchors, no-sugar controls, top apparent 4 h hits, high-caution/high-reduction runs, and advancing conditions
- **Comparator logic**: explicitly encoded in Part B and Part C
- **Randomization**: restricted and block-specific
- **Naming**: machine-parsable bench labels with anchor/control status visible

This recommendation is justified because it best preserves:
- execution clarity
- comparator integrity
- assay interpretability
- downstream synthesis value
- and the project’s safety/practicality principle around reaction time

Below is the resulting wet-lab run sheet.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw backbone to:
1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the current **60 C, 2 h** benchmark region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-linked dataset for restricted-domain evidence synthesis and future AI-supported decision support.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry**
- Target aw: **0.79**
- Operational humidity implementation: **samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP**
- Protein:sugar ratio: **1:2**
- Ratio basis: **DRAFT placeholder until benchmark confirmed**
  - `1:2 [RATIO BASIS PENDING — must match historical benchmark convention exactly; enter w/w or molar before execution approval]`
- Pretreatment: **Ultrasound ON**
- Ultrasound execution: fixed per benchmark SOP; see Part E
- Sample preparation route: one benchmark SOP
- Deposition/sample geometry: fixed benchmark SOP
- Pre-equilibration workflow: fixed benchmark SOP
- Incubation workflow: fixed benchmark SOP
- Cooling/stop procedure: fixed benchmark SOP
- Recovery/reconstitution workflow: fixed benchmark SOP
- Primary assay format: benchmark-matched β-LG IgE-binding assay
- Same IgE source / serum pool across round
- Same untreated/native β-LG reference across analytical campaign
- Same β-LG lot if feasible
- Same donor lots/grades if feasible

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (no-sugar controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for same-round lactose and glucose anchors at 60 C

### Deferred variables
- Wet-state experiments
- pH/buffer
- aw variation
- RH variation beyond benchmark-matched implementation
- ratio optimization
- ultrasound variation
- no-ultrasound controls
- other pretreatments
- 3 h intermediate time
- broader sugar expansion beyond the 4 selected donors

### Execution approval status
**DRAFT ONLY — NOT FOR LAB EXECUTION until the following benchmark-dependent fields are confirmed and entered:**
1. ratio basis (**w/w or molar**)
2. operational RH/salt-equivalent corresponding to aw 0.79
3. benchmark pre-equilibration duration

---

## Part B. Master run list

| run_id | group_id | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| R01 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-LAC-55C-4H-SUG |
| R02 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-GLU-55C-4H-SUG |
| R03 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-GAL-55C-4H-SUG |
| R04 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-MAN-55C-4H-SUG |
| R05 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; lactose time bridge vs 2 h anchor; matched to 60 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred | B1-LAC-60C-4H-SUG |
| R06 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; glucose time bridge vs 2 h anchor; matched to 60 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-GLU-60C-4H-SUG |
| R07 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-GAL-60C-4H-SUG |
| R08 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B1 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B1-MAN-60C-4H-SUG |
| R09 | G-TIME-LAC-60 | Time bridge anchor for lactose; historical benchmark continuity | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-LAC-60C-2H-ANC |
| R10 | G-TIME-GLU-60 | Time bridge anchor for glucose; historical benchmark continuity | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-GLU-60C-2H-ANC |
| R11 | G-CTRL-55-4H | Process-only control for all 55 C 4 h sugar runs | None | none | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-NS-55C-4H-CTRL |
| R12 | G-CTRL-60-4H | Process-only control for all 60 C 4 h sugar runs | None | none | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B1 | Tier A required | Non-IgE β-LG detectability mandatory | B1-NS-60C-4H-CTRL |
| R13 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-LAC-55C-4H-SUG |
| R14 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-GLU-55C-4H-SUG |
| R15 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-GAL-55C-4H-SUG |
| R16 | G-DONOR-55-4H | Donor ranking at 4 h; temp comparison; matched to 55 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-MAN-55C-4H-SUG |
| R17 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; lactose time bridge vs 2 h anchor; matched to 60 C no-sugar | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred | B2-LAC-60C-4H-SUG |
| R18 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; glucose time bridge vs 2 h anchor; matched to 60 C no-sugar | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-GLU-60C-4H-SUG |
| R19 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Galactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-GAL-60C-4H-SUG |
| R20 | G-DONOR-60-4H | Donor ranking at 4 h; temp comparison; matched to 60 C no-sugar | Mannose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Sugar run | B2 | Tier A required | Non-IgE β-LG detectability preferred; planned high caution | B2-MAN-60C-4H-SUG |
| R21 | G-TIME-LAC-60 | Time bridge anchor for lactose; historical benchmark continuity | Lactose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-LAC-60C-2H-ANC |
| R22 | G-TIME-GLU-60 | Time bridge anchor for glucose; historical benchmark continuity | Glucose | 1:2 [basis pending benchmark confirmation] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | Anchor sugar run | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-GLU-60C-2H-ANC |
| R23 | G-CTRL-55-4H | Process-only control for all 55 C 4 h sugar runs | None | none | Dry | 55 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-NS-55C-4H-CTRL |
| R24 | G-CTRL-60-4H | Process-only control for all 60 C 4 h sugar runs | None | none | Dry | 60 | 4 | aw 0.79 target; RH-equivalent pending benchmark confirmation | Ultrasound ON | No-sugar control | B2 | Tier A required | Non-IgE β-LG detectability mandatory | B2-NS-60C-4H-CTRL |

---

## Part C. Batch execution plan

### Batch grouping
- **Process Block 1**: R01–R12
- **Process Block 2**: R13–R24
- Each process block must contain **all 12 conditions exactly once**
- Blocks should be run as **independent process realizations**, preferably on separate days or separated execution windows

### Which runs should be processed together
Within each block:
- prepare all 12 runs under one coordinated workflow
- pre-equilibrate all samples under the same benchmark RH-equivalent workflow
- execute 55 C and 60 C conditions in the same block using balanced placement
- recover all samples under the same fixed recovery SOP

### Restricted randomization rule
- Each process block must contain all 12 conditions exactly once.
- Within each block, assign sample preparation order, chamber/incubator position, and assay plate position using restricted randomization.
- Do not group runs entirely by donor, temperature, or control class.
- Distribute anchors and no-sugar controls across chamber positions and assay plates as protected comparators.
- If two temperature environments are used simultaneously, randomize position within each temperature environment and record chamber/incubator ID and position for every run.
- Any deviation from planned placement or order must be documented in the deviation log.
- Use **different randomized prep/placement plans** for Block 1 and Block 2.

### Protected comparator runs
The following are protected comparator runs and should not be dropped or deprioritized:
- R09, R10, R11, R12
- R21, R22, R23, R24

If a protected comparator fails, prioritize rerun/disposition review before interpreting dependent comparison sets.

### Matched-comparison grouping
- **55 C sugar vs process-only**
  - R01, R02, R03, R04 matched to R11 within Block 1
  - R13, R14, R15, R16 matched to R23 within Block 2
- **60 C sugar vs process-only**
  - R05, R06, R07, R08 matched to R12 within Block 1
  - R17, R18, R19, R20 matched to R24 within Block 2
- **Lactose time bridge**
  - R05 matched to R09 within Block 1
  - R17 matched to R21 within Block 2
- **Glucose time bridge**
  - R06 matched to R10 within Block 1
  - R18 matched to R22 within Block 2
- **Cross-block comparison**
  - used for replication/confirmation only
  - not a substitute for within-block matched comparison

### Suggested execution order within each block
Use a separately randomized order for each block, but ensure:
- anchors and no-sugar controls are distributed through prep order
- not all 60 C / 4 h monosaccharide runs are clustered adjacently if avoidable
- chamber position is balanced across comparison classes

---

## Part D. Assay plan

### Assays required for all runs
**Tier A required for all 24 runs**
1. **β-LG IgE-binding assay**
   - benchmark-matched format
   - same IgE source / serum pool across round
   - include untreated/native β-LG reference across analytical campaign
2. **Recovered protein quantification**
3. **Extractability/solubility assessment**
   - recovered volume
   - recovered protein concentration
   - ease of reconstitution
   - visible pellet / insoluble residue
4. **Turbidity/insolubility flag**
5. **Loading normalization verification**
   - recovered-protein basis

### Interpretation-support assays
**Non-IgE β-LG detectability**
- Preferred on all runs if feasible
- Mandatory minimum subset:
  - R09, R10, R11, R12
  - R21, R22, R23, R24
  - top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
  - any high-caution/high-reduction condition
  - any condition proposed for advancement

**Chemistry-side caution subset preferred**
- free lysine proxy on:
  - all anchors
  - all no-sugar controls
  - top 2–4 apparent 4 h winners
  - one distinct high-caution comparator if needed

### Selected runs for orthogonal confirmation
Tier B orthogonal confirmation is **selection-rule based**, not pre-fixed by donor winner identity.

Apply after Tier A review to:
- both anchors in both blocks:
  - R09, R10, R21, R22
- both no-sugar controls in both blocks:
  - R11, R12, R23, R24
- top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
- one additional high-caution apparent reducer if not already included
- optionally one unexpectedly strong no-sugar control if observed

### Tier B orthogonal confirmation package
1. Orthogonal β-LG IgE-binding assay with different antigen-presentation mode
2. Gel-based aggregation/profile check
3. Confirmation of comparable recovered antigen handling

---

## Part E. Execution notes

### Parameter definitions
- **Dry-state implementation**: samples are pre-equilibrated to benchmark RH-equivalent corresponding to target aw 0.79 for the benchmark-defined duration, then incubated under the benchmark dry-incubation SOP. Do not substitute continuous RH-controlled thermal incubation unless this matches the benchmark SOP.
- **Protein:sugar ratio**:
  - Sugar runs: `1:2 [RATIO BASIS PENDING — must match historical benchmark convention exactly; enter w/w or molar before execution approval]`
  - No-sugar controls: none
- **Operational RH-equivalent**:
  - `[BENCHMARK RH / SALT-EQUIVALENT PENDING — enter exact benchmark-matched RH setpoint or salt-system equivalent before execution approval]`
- **Pre-equilibration duration**:
  - `[BENCHMARK PRE-EQUILIBRATION DURATION PENDING — enter exact duration before execution approval]`

### Ultrasound fixed conditions
Enter before execution approval:
- instrument/model: `[REQUIRED]`
- operating frequency: `[REQUIRED]`
- amplitude/power setting: `[REQUIRED]`
- pulse vs continuous: `[REQUIRED]`
- sonication duration: `[REQUIRED]`
- sample volume: `[REQUIRED]`
- vessel type: `[REQUIRED]`
- temperature control method: `[REQUIRED]`

**Ultrasound pass/fail acceptance**
- correct instrument/SOP used
- correct programmed setting range used
- correct duration range used
- no documented temperature excursion beyond SOP limit
- no operator-recorded application failure

### Timing rules
- **Time zero definition**: reaction time begins when samples are placed into a pre-equilibrated incubation environment at target temperature per benchmark SOP.
- **Stop rule**: at end of reaction time, remove samples immediately and apply benchmark cooling/stop procedure without delay.
- Use actual insertion and removal times on run sheet.
- Major timing error is a critical deviation.

### Control rules
- 55 C 4 h sugar runs must be interpreted against matched 55 C 4 h no-sugar control from the same block.
- 60 C 4 h sugar runs must be interpreted against matched 60 C 4 h no-sugar control from the same block.
- Lactose 60 C 4 h must be interpreted against lactose 60 C 2 h anchor from the same block.
- Glucose 60 C 4 h must be interpreted against glucose 60 C 2 h anchor from the same block.
- Cross-block replication supports confirmation; it does not replace within-block comparator logic.

### Naming rules
- Sample-label syntax:
  - **[Block]-[Donor]-[Temp]-[Time]-[Status]**
- Donor codes:
  - LAC = lactose
  - GLU = glucose
  - GAL = galactose
  - MAN = mannose
  - NS = no sugar
- Status codes:
  - SUG = sugar run
  - ANC = anchor
  - CTRL = no-sugar control

### Required process metadata capture
For each run record:
- operator
- process block
- prep date/time
- actual equilibration start/stop
- actual incubation start/stop
- chamber/incubator ID
- chamber position
- RH/aw check if available
- loaded protein mass
- loaded sugar mass
- total solids
- deposition volume
- sample mass before/after if feasible
- visible sample state before and after incubation:
  - free-flowing
  - film
  - caked
  - glassy
  - crystalline
  - browned
  - insoluble on recovery
- reconstitution behavior
- pellet yes/no
- turbidity score
- deviations
- disposition

### Required post-recovery capture fields
- recovered volume
- recovered protein concentration
- dilution factor into assay
- normalized loading concentration
- visible pellet
- turbidity
- storage condition if not assayed immediately
- freeze-thaw count
- **assayability status**:
  - Assayable
  - Assayable with caution
  - Not assayable / hold for disposition

### Planned caution rules
**Planned high caution = YES**
- GLU 60 C 4 h
- GAL 60 C 4 h
- MAN 60 C 4 h
  - R06, R07, R08, R18, R19, R20

**Monitor but not planned high caution**
- LAC 60 C 4 h
  - anchor-linked extended-time condition; monitor for presentation/recovery shifts relative to 2 h anchor

### Critical deviations requiring rerun or exclusion
- wrong donor, time, temperature, or ratio basis
- unresolved ratio basis / RH-equivalent / pre-equilibration duration at execution time
- incorrect or missing ultrasound
- failed dry-state control
- major timing error
- grossly inconsistent sample geometry/loading
- sample mix-up or labeling uncertainty
- recovery failure making interpretation impossible

### Concise contingency rules
- **Critical deviation**: stop, flag, notify PI or delegated study lead, hold sample for disposition, do not enter into model-building dataset unless formally rescued.
- **Noncritical deviation**: document, continue if sample remains valid, flag for caution in interpretation.
- **Rerun authority**: PI or delegated study lead after deviation review.

### Pre-execution verification checklist
Before execution approval confirm:
1. ratio basis entered and benchmark-matched
2. RH/salt-equivalent entered and benchmark-matched
3. pre-equilibration duration entered and benchmark-matched
4. ultrasound settings entered
5. SOPs current and verified
6. instrument calibration status current
7. reagent/donor lots recorded
8. assay reagents and IgE source confirmed for round consistency

---

### Next Steps

1. **Resolve the three blocking benchmark-dependent fields immediately**
   - ratio basis: w/w or molar
   - RH/salt-equivalent for aw 0.79
   - pre-equilibration duration

2. **Populate Part E ultrasound fields from the benchmark SOP**
   - instrument/model
   - frequency
   - amplitude/power
   - pulse mode
   - duration
   - sample volume
   - vessel type
   - temperature-control method

3. **Convert this draft into execution-approved version**
   - remove all pending placeholders
   - verify against benchmark record
   - sign off PI/designee approval

4. **Generate block-specific randomized prep and placement maps**
   - one for Block 1
   - one independently randomized for Block 2

5. **Prepare assay plate plan**
   - distribute anchors and no-sugar controls across plates
   - include native untreated β-LG reference throughout analytical campaign

6. **Issue final handoff packet to wet-lab team**
   - execution-approved run sheet
   - associated SOP references
   - deviation log form
   - metadata capture form
   - post-recovery assayability/QC form

This is my final recommendation and the execution-ready draft output for this stage.

[end summary 3]

Here is the agenda for the meeting:

Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer.

As a reference, here is the agenda from those meetings, which must be addressed here as well:

You are working on a research project to identify glycation conditions that reduce the allergenicity of β-lactoglobulin (β-LG, variant A). The project integrates literature evidence and wet-lab results to infer effective and practical parameter regions across variables such as sugar donor, protein:sugar ratio, reaction mode, temperature, reaction time, pH or aw/RH, and pretreatment. A key project principle is that reaction time is a trade-off variable: longer reactions may further reduce allergenicity, but they also increase AGE formation and other harmful byproducts. Therefore, the overall goal is not simply to maximize reduction at any cost, but to identify condition regions that balance efficacy, safety, and experimental practicality.

You are now entering the wet-lab run-sheet generation stage.

Stage purpose:
Translate the execution planning output into a directly executable wet-lab experiment sheet.
This stage is not for further high-level discussion.
Its purpose is to generate a run-by-run, parameter-complete, operationally clear experiment list that can be handed to the wet-lab team.

Your task:
Using the execution planning summary and the provided lab defaults / protocol defaults, generate a directly executable wet-lab run sheet.

Requirements:
1. Every proposed run must be fully specified.
2. No critical experimental parameter may be left blank.
3. If a variable is not being optimized in this round, it must still be explicitly fixed.
4. If wet-state experiments are included, explicit pH and buffer conditions must be given.
5. If dry-state experiments are included, explicit aw / RH conditions must be given.
6. Each run must be linked to its scientific purpose.
7. Include matched controls and replicates explicitly.
8. Organize the final plan in a way that a wet-lab team can directly execute.

Please produce:

Part A. Round-level execution summary
- objective of this round
- fixed variables
- scanned variables
- deferred variables

Part B. Master run list
For each run, include:
- run_id
- group_id
- purpose
- sugar donor
- protein:sugar ratio
- mode
- temperature_C
- time_h
- pH or aw/RH
- pretreatment
- sugar/no-sugar control status
- replicate_id
- primary assay(s)
- optional assay(s)
- sample naming label

Part C. Batch execution plan
- batch grouping
- which runs should be processed together
- matched-comparison grouping

Part D. Assay plan
- assays required for all runs
- selected runs for orthogonal confirmation
- interpretation-support assays if needed

Part E. Execution notes
- parameter definitions
- timing rules
- control rules
- naming rules
- practical notes for wet-lab implementation

Output format:
Use clear section headings.
In Part B, present the master run list as a structured table.
The output must be directly actionable by a wet-lab team.




Principal Investigator, please provide your response to the agenda.

## Principal Investigator

### Agenda

Merge the prior meeting outputs into a **single, best-version wet-lab run-sheet packet** for the approved **dry-only β-LG variant A glycation screen**, while preserving the original stage purpose: **direct execution readiness**, not further strategy debate. The packet must be run-by-run, parameter-complete, comparator-aware, assay-interpretable, and suitable for later evidence synthesis / AI-facing use.

Because the prior meetings were aligned on the scientific design but differed in emphasis and table structure, I am issuing one consolidated answer that:

- keeps the **approved 12-condition dry-only design**
- uses **2 full independent process blocks** for a **24-run master list**
- preserves **within-block comparator logic**
- includes **explicit assay assignments and execution rules**
- adopts the strongest **QC / interpretability safeguards**
- and makes a clear governance decision on **release readiness**

---

### Team Member Input

#### Principal Investigator
- Repeatedly framed this stage as **operational translation**, not design revision.
- Confirmed the approved backbone:
  - β-LG variant A
  - dry-only
  - fixed aw backbone
  - fixed 1:2 ratio
  - ultrasound ON
  - 12-condition matrix
  - preferred 2 full independent process blocks
- Identified the main execution risks as:
  - unresolved ratio basis
  - unresolved aw/RH implementation
  - unresolved ultrasound details
  - unclear comparator structure
  - unclear assay assignment
  - unclear naming / control handling
- Requested a final packet that is both:
  - **wet-lab executable**
  - **analysis-ready**

#### Maillard Reaction Chemistry and Process Scientist
- Strongly emphasized that the remaining task is **process closure**.
- Required dry-state wording to include both:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark RH-equivalent / pre-equilibration workflow**
- Required explicit control of:
  - ratio basis
  - RH setpoint / equivalent
  - pre-equilibration duration
  - deposition/loading
  - vessel geometry
  - time-zero rule
  - stop/cooling rule
  - recovery workflow
- Clarified no-sugar controls must be:
  - β-LG only
  - same solvent route
  - same ultrasound
  - same loading
  - same geometry
  - same dry workflow
  - no donor added
- Warned that:
  - browning
  - caking
  - poor recovery
  are **overprocessing flags**, not success signals.
- Supported planned high caution for **60 C / 4 h monosaccharides only**.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the packet must generate **interpretable immunoassay inputs**, not just processed samples.
- Required for **all runs**:
  - primary β-LG IgE-binding assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - matched loading normalization verification
- Strongly emphasized:
  - lower IgE signal alone is **not sufficient**
  - compare against matched no-sugar controls
  - normalize on recovered protein basis
  - escalate low-recovery / high-turbidity samples
- Supported:
  - native untreated β-LG as an **assay control**, not a process run
  - non-IgE β-LG detectability as mandatory for anchors and no-sugar controls
  - broader detectability / orthogonal support for high-priority or high-caution conditions
- Supported planned high caution for **60 C / 4 h monosaccharides only**.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly supported an **explicit 24-run master list**, not shorthand replication.
- Emphasized that the two repeats are **independent process blocks**, not generic technical replicates.
- Recommended explicit comparator structure in the run table and batch plan:
  - within-block sugar vs matched no-sugar
  - within-block lactose 4 h vs lactose 2 h anchor
  - within-block glucose 4 h vs glucose 2 h anchor
  - cross-block comparison for replication only
- Recommended:
  - protected comparator runs
  - restricted randomization
  - separate randomized orders for Block 1 and Block 2
- Supported comparator-aware columns and human-readable purpose fields.

#### Scientific Critic
- Reiterated the true release blockers:
  1. ratio basis
  2. RH-equivalent implementation for aw 0.79
  3. ultrasound operational details / SOP acceptance
- Warned against scientifically precise but operationally vague wording.
- Requested visible:
  - critical deviation rules
  - QC checklist logic
  - final pre-release verification
- Supported concise, action-oriented execution notes.

#### Research Synthesis and Optimization Lead
- Strongly supported a packet that is both:
  - execution-facing
  - downstream-analysis ready
- Recommended explicit identity layers:
  - `condition_id`
  - `run_id`
  - `sample naming label`
- Supported one row per **process run**
- Recommended keeping Part B lean but comparator-aware
- Recommended controlled vocabularies for QC in companion capture
- Supported machine-readable sample labels with visible anchor/control status
- Recommended keeping post-run interpretation fields out of the run table itself.

---

### Recommendation

My recommendation is to issue a **five-part wet-lab packet** with a **24-run master run list** built from the approved **12-condition dry-only design**, executed as **2 full independent process blocks**.

However, I am making one firm governance decision:

> **This packet can be finalized as a controlled draft now, but it must not be released for bench execution until all benchmark-dependent operational constants are filled with actual values.**

Across the prior meetings, the team was unanimous that the following are **hard release gates**:

1. **protein:sugar ratio basis**
   - `1:2 w/w` or `1:2 molar`
2. **aw 0.79 operational implementation**
   - RH setpoint or validated salt-equivalent
   - pre-equilibration duration
   - acceptance/tolerance window
3. **ultrasound execution definition**
   - SOP ID/version
   - instrument/model
   - frequency
   - amplitude/power
   - pulse/continuous
   - duration
   - sample volume
   - vessel type
   - temperature control
   - pass/fail acceptance
4. **sample loading / geometry constants**
   - loaded protein mass
   - loaded sugar mass or no-sugar confirmation
   - total loaded solids
   - deposition volume / mass
   - vessel / substrate geometry

This is the only scientifically responsible position under the stage rule that **no critical experimental parameter may be left blank**.

Because the meeting summaries did **not** provide the actual benchmark numeric defaults, I cannot honestly label the packet below as execution-approved. The correct merged answer is therefore:

- provide the **best integrated final packet structure now**
- preserve all comparator and assay logic
- mark the unresolved benchmark-linked constants as **release blockers**
- and state clearly that **bench execution must not begin until those fields are populated from the benchmark SOP**

I am also choosing the following final structural positions:

- **Design**: unchanged 12-condition dry-only matrix
- **Replication**: 2 full independent process blocks, explicitly listed as 24 runs
- **Dry-state wording**:
  - target aw = 0.79
  - samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP
- **Planned high caution**:
  - YES for glucose 60 C 4 h, galactose 60 C 4 h, mannose 60 C 4 h
  - NO for lactose 60 C 4 h
- **All-run assay package**: mandatory Tier A for all 24 runs
- **Native untreated β-LG**: assay control only, not a process-matrix run
- **Comparator logic**: encoded in both Part B and Part C
- **Randomization**: restricted and block-specific
- **Naming**: machine-readable labels with anchor/control status visible

Below is the merged wet-lab packet.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:

1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the benchmark-linked **60 C, 2 h** region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-linked dataset for restricted-domain decision support and later evidence/model synthesis.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- Target aw: **0.79**
- Dry-state implementation: **samples pre-equilibrated to benchmark RH-equivalent corresponding to aw 0.79, then reacted under benchmark dry-incubation SOP**
- Protein:sugar ratio: **1:2**
- Ratio basis: **RELEASE GATE — must be entered as either `w/w` or `molar`**
- Pretreatment: **Ultrasound ON**
- Ultrasound execution: **fixed benchmark SOP; full settings must be entered before release**
- Sample preparation route: **fixed benchmark SOP**
- Deposition/loading geometry: **fixed benchmark SOP**
- Vessel/substrate type: **fixed benchmark SOP**
- Pre-equilibration workflow: **fixed benchmark SOP**
- Incubation workflow: **fixed benchmark SOP**
- Cooling/stop workflow: **fixed benchmark SOP**
- Recovery/reconstitution workflow: **fixed benchmark SOP**
- Primary IgE assay platform: **benchmark-matched**
- Same IgE source / serum pool across round
- Same untreated/native β-LG reference across analytical campaign
- Same β-LG lot across round if feasible
- Same donor lots/grades across round if feasible
- Replication plan: **2 independent full process blocks**

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (process-only controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

### Deferred variables
Not optimized in this round:
- wet-state mode
- pH / buffer
- aw variation
- RH variation beyond benchmark-matched implementation
- ratio variation
- ultrasound variation
- no-ultrasound controls
- other pretreatments
- 3 h intermediate time
- broader donor expansion
- direct clinical allergenicity assessment

### Execution approval status
**DRAFT / NOT FOR EXECUTION** until all release-gated benchmark constants are entered:
1. ratio basis
2. RH-equivalent implementation for aw 0.79
3. pre-equilibration duration and tolerance
4. ultrasound SOP/settings and pass/fail rule
5. deposition/loading/geometry constants

---

## Part B. Master run list

**Controlled wording for assay columns**
- **Primary assay(s):** `Primary β-LG IgE-binding; Recovered protein quantification; Extractability/solubility assessment; Turbidity/insolubility flag; Loading normalization verification`
- **Optional assay(s):**
  - `Non-IgE β-LG detectability preferred`
  - `Non-IgE β-LG detectability mandatory`
  - `Orthogonal confirmation mandatory`
  - `Free lysine proxy preferred`
  - `Planned high caution`

| run_id | condition_id | group_id | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| B1-R01 | COND_LAC_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | Primary β-LG IgE-binding; Recovered protein quantification; Extractability/solubility assessment; Turbidity/insolubility flag; Loading normalization verification | Non-IgE β-LG detectability preferred | B1-LAC-55C-4H-SUG |
| B1-R02 | COND_GLU_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-GLU-55C-4H-SUG |
| B1-R03 | COND_GAL_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs galactose 60 C 4 h | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-GAL-55C-4H-SUG |
| B1-R04 | COND_MAN_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs mannose 60 C 4 h | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-MAN-55C-4H-SUG |
| B1-R05 | COND_LAC_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; lactose time bridge vs lactose 60 C 2 h anchor | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-LAC-60C-4H-SUG |
| B1-R06 | COND_GLU_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; glucose time bridge vs glucose 60 C 2 h anchor | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-GLU-60C-4H-SUG |
| B1-R07 | COND_GAL_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-GAL-60C-4H-SUG |
| B1-R08 | COND_MAN_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-MAN-60C-4H-SUG |
| B1-R09 | COND_LAC_60C_2H_ANC | G-TIME-LAC | Same-round lactose anchor; benchmark continuity; within-block comparator for lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-LAC-60C-2H-ANC |
| B1-R10 | COND_GLU_60C_2H_ANC | G-TIME-GLU | Same-round glucose anchor; benchmark continuity; within-block comparator for glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-GLU-60C-2H-ANC |
| B1-R11 | COND_NONE_55C_4H_CTL | G-CTRL55 | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-NS-55C-4H-CTRL |
| B1-R12 | COND_NONE_60C_4H_CTL | G-CTRL60 | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-NS-60C-4H-CTRL |
| B2-R01 | COND_LAC_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-LAC-55C-4H-SUG |
| B2-R02 | COND_GLU_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-GLU-55C-4H-SUG |
| B2-R03 | COND_GAL_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs galactose 60 C 4 h | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-GAL-55C-4H-SUG |
| B2-R04 | COND_MAN_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs mannose 60 C 4 h | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-MAN-55C-4H-SUG |
| B2-R05 | COND_LAC_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; lactose time bridge vs lactose 60 C 2 h anchor | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-LAC-60C-4H-SUG |
| B2-R06 | COND_GLU_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; glucose time bridge vs glucose 60 C 2 h anchor | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-GLU-60C-4H-SUG |
| B2-R07 | COND_GAL_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-GAL-60C-4H-SUG |
| B2-R08 | COND_MAN_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-MAN-60C-4H-SUG |
| B2-R09 | COND_LAC_60C_2H_ANC | G-TIME-LAC | Same-round lactose anchor; benchmark continuity; within-block comparator for lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-LAC-60C-2H-ANC |
| B2-R10 | COND_GLU_60C_2H_ANC | G-TIME-GLU | Same-round glucose anchor; benchmark continuity; within-block comparator for glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-GLU-60C-2H-ANC |
| B2-R11 | COND_NONE_55C_4H_CTL | G-CTRL55 | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-NS-55C-4H-CTRL |
| B2-R12 | COND_NONE_60C_4H_CTL | G-CTRL60 | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-NS-60C-4H-CTRL |

---

## Part C. Batch execution plan

### Batch grouping
- **Preferred execution:** 2 independent full process blocks
  - **Block 1:** B1-R01 to B1-R12
  - **Block 2:** B2-R01 to B2-R12
- Each block must contain the full **12-condition matrix** exactly once.
- Blocks should be executed as **independent process realizations**, preferably on separate days or separated execution windows.

### Which runs should be processed together
Within each block:
- prepare all 12 runs under one coordinated workflow
- apply the same benchmark sample-preparation route
- apply the same ultrasound SOP
- pre-equilibrate all samples under the same benchmark RH-equivalent workflow
- execute 55 C and 60 C conditions within the same protected block campaign
- recover all samples under the same fixed recovery SOP

Do **not** split a block into donor-isolated mini-batches.

If staggered handling is required:
- intersperse 55 C and 60 C runs
- intersperse sugar and no-sugar runs
- intersperse anchors and bridge runs
- preserve comparator balance

### Matched-comparison grouping

#### 55 C sugar vs process-only
- Block 1:
  - B1-R01, B1-R02, B1-R03, B1-R04 matched to **B1-R11**
- Block 2:
  - B2-R01, B2-R02, B2-R03, B2-R04 matched to **B2-R11**

#### 60 C sugar vs process-only
- Block 1:
  - B1-R05, B1-R06, B1-R07, B1-R08 matched to **B1-R12**
- Block 2:
  - B2-R05, B2-R06, B2-R07, B2-R08 matched to **B2-R12**

#### Lactose time bridge
- Block 1:
  - **B1-R05** matched to **B1-R09**
- Block 2:
  - **B2-R05** matched to **B2-R09**

#### Glucose time bridge
- Block 1:
  - **B1-R06** matched to **B1-R10**
- Block 2:
  - **B2-R06** matched to **B2-R10**

#### Temperature pairs within donor
- lactose:
  - B1-R01 vs B1-R05
  - B2-R01 vs B2-R05
- glucose:
  - B1-R02 vs B1-R06
  - B2-R02 vs B2-R06
- galactose:
  - B1-R03 vs B1-R07
  - B2-R03 vs B2-R07
- mannose:
  - B1-R04 vs B1-R08
  - B2-R04 vs B2-R08

#### Cross-block comparison
- used for **replication / confirmation only**
- not a substitute for within-block matched comparison

### Protected comparator runs
The following are protected comparator runs and must not be dropped or deprioritized:
- Block 1: **B1-R09, B1-R10, B1-R11, B1-R12**
- Block 2: **B2-R09, B2-R10, B2-R11, B2-R12**

If a protected comparator fails, dependent comparison sets in that block must be flagged as reduced in interpretability and reviewed for rerun.

### Restricted randomization / balancing rules
- Use **different randomized prep/placement plans** for Block 1 and Block 2.
- Randomize:
  - sample preparation order
  - chamber/incubator position
  - assay plate placement
- Do **not** group runs entirely by:
  - donor
  - temperature
  - control class
- Distribute anchors and no-sugar controls across chamber positions and assay plates.
- If multiple assay plates are required, distribute protected comparators across plates or use a validated bridging layout.
- Record chamber/incubator ID and position for every run.

### Contingency plan — use only if full second block cannot be executed
Priority order:
1. lactose 60 C 2 h anchor
2. glucose 60 C 2 h anchor
3. no-sugar 55 C 4 h control
4. no-sugar 60 C 4 h control
5. top 2 apparent 4 h sugar conditions from Block 1
6. one additional high-caution/high-reduction condition if distinct

---

## Part D. Assay plan

### Assays required for all runs
Apply to all 24 process runs:

1. **Primary β-LG IgE-binding assay**
   - benchmark-matched format
   - same IgE source / serum pool across round

2. **Recovered protein quantification**

3. **Extractability / solubility assessment**
   - recovered volume
   - recovered protein concentration
   - ease of reconstitution
   - visible insoluble residue / pellet

4. **Turbidity / insolubility flag**

5. **Loading normalization verification**
   - assay input normalized on recovered-protein basis

### Native untreated β-LG reference
- Include as an **assay control**, not a process-matrix run.
- Include on every primary assay plate or use a validated plate-linking scheme.
- Include in every orthogonal assay batch.

### Interpretation-support assays

#### Non-IgE β-LG detectability
- Preferred on all runs if feasible.
- Mandatory minimum subset:
  - B1-R09, B1-R10, B1-R11, B1-R12
  - B2-R09, B2-R10, B2-R11, B2-R12
  - top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
  - any high-caution/high-reduction condition
  - any condition proposed for advancement

#### Free lysine proxy
Preferred on:
- all anchors
- all no-sugar controls
- top 2–4 apparent 4 h winners
- one distinct high-caution comparator if needed

### Selected runs for orthogonal confirmation

#### Mandatory pre-assigned subset
- Anchors in both blocks:
  - B1-R09, B1-R10, B2-R09, B2-R10
- No-sugar controls in both blocks:
  - B1-R11, B1-R12, B2-R11, B2-R12

These receive:
- non-IgE β-LG detectability
- orthogonal β-LG IgE-binding assay with different antigen-presentation mode
- free lysine proxy preferred

#### Conditional orthogonal subset after Tier A review
Add:
- top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
- one additional high-caution apparent reducer if distinct
- any condition proposed for advancement
- optionally one unexpectedly strong no-sugar control if observed

### Tier B orthogonal confirmation package
1. Orthogonal β-LG IgE-binding assay with different antigen-presentation mode
2. Gel-based aggregation / profile check
3. Confirmation of comparable recovered antigen handling

### Interpretation-support triggers
Escalate for adjudication if any of the following occur:
- unexpectedly strong reduction in no-sugar control
- severe turbidity / particulate carryover
- large reduction with poor recovery
- major drop in non-IgE β-LG detectability
- disagreement between primary and orthogonal IgE assay formats

---

## Part E. Execution notes

### Parameter definitions
- **Protein:** β-LG variant A
- **Mode:** Dry-state glycation only
- **Dry-state implementation:** samples are pre-equilibrated to benchmark RH-equivalent corresponding to target aw 0.79 for the benchmark-defined duration, then incubated under the benchmark dry-incubation SOP.
- **Protein:sugar ratio:**
  - sugar runs: `1:2 [RELEASE GATE — enter w/w or molar exactly as benchmark]`
  - no-sugar controls: no donor added
- **Pretreatment:** Ultrasound ON per benchmark SOP
- **Sample loading/geometry:** fixed benchmark deposition and vessel geometry per SOP; identical loaded mass, vessel type, and sample format across all runs

### Release-gated constants to enter before execution
Enter actual values before release:
- ratio basis: `[w/w or molar]`
- RH setpoint or salt-equivalent for aw 0.79: `[REQUIRED]`
- pre-equilibration duration: `[REQUIRED]`
- RH/aw tolerance / acceptance window: `[REQUIRED]`
- ultrasound SOP ID/version: `[REQUIRED]`
- ultrasound instrument/model: `[REQUIRED]`
- ultrasound frequency: `[REQUIRED]`
- ultrasound amplitude/power: `[REQUIRED]`
- ultrasound pulse vs continuous: `[REQUIRED]`
- ultrasound duration: `[REQUIRED]`
- ultrasound sample volume: `[REQUIRED]`
- ultrasound vessel type: `[REQUIRED]`
- ultrasound temperature control method: `[REQUIRED]`
- loaded protein mass per sample: `[REQUIRED]`
- loaded sugar mass per sample or no-sugar confirmation: `[REQUIRED]`
- total loaded solids: `[REQUIRED]`
- deposition volume / mass: `[REQUIRED]`
- vessel / substrate geometry: `[REQUIRED]`

### Ultrasound pass/fail acceptance
- correct SOP and instrument used
- correct programmed setting range used
- correct duration range used
- correct sample volume / vessel type used
- no documented temperature excursion beyond SOP limit
- no operator-recorded application failure

### Timing rules
- **Time zero definition:** reaction time begins when the sample is placed into the pre-equilibrated incubation environment at target temperature per benchmark SOP.
- **Stop rule:** reaction ends at physical removal from that environment for immediate cooling/stop per SOP.
- Record actual:
  - equilibration start/stop
  - incubation start/stop
  - cooling/stop time
  - recovery time
- Major timing deviation is a critical deviation.

### Control rules
- No-sugar controls are matched process-only comparators and must be prepared in each block.
- No-sugar controls must be:
  - β-LG only
  - same protein loading
  - same solvent route
  - same ultrasound
  - same deposition geometry
  - same dry-state workflow
  - same recovery workflow
  - no donor added
- 55 C 4 h sugar runs must be interpreted against matched 55 C 4 h no-sugar control from the same block.
- 60 C 4 h sugar runs must be interpreted against matched 60 C 4 h no-sugar control from the same block.
- Lactose 60 C 4 h must be interpreted against lactose 60 C 2 h anchor from the same block.
- Glucose 60 C 4 h must be interpreted against glucose 60 C 2 h anchor from the same block.
- Cross-block replication supports confirmation; it does not replace within-block comparator logic.
- Native untreated β-LG is an assay control, not a process run.

### Naming rules
- **Condition ID format:** `COND_[DonorCode]_[TempC]C_[TimeH]_[StatusCode]`
- **Sample label format:** `[Block]-[Donor]-[Temp]-[Time]-[Status]`
- Donor codes:
  - `LAC`
  - `GLU`
  - `GAL`
  - `MAN`
  - `NONE` or `NS`
- Status codes:
  - `SUG` = sugar run
  - `ANC` = anchor
  - `CTRL` = no-sugar control
- No spaces or special characters.

### Required process metadata capture
For each run record:
- operator
- process block
- prep date/time
- actual protein mass
- actual sugar mass or no-sugar confirmation
- actual loaded mass / total solids
- deposition volume
- equilibration start/stop
- incubation start/stop
- chamber/incubator ID
- chamber position
- RH/aw check if available
- ultrasound pass/fail
- sample appearance before and after incubation:
  - free-flowing
  - film
  - caked
  - glassy
  - crystalline
  - browned
- reconstitution behavior
- visible pellet yes/no
- recovered volume
- turbidity score
- deviations
- disposition

### Required post-recovery capture fields
- recovered volume
- recovered protein concentration
- dilution factor into assay
- normalized loading concentration
- visible pellet
- turbidity
- storage condition if not assayed immediately
- freeze-thaw count
- assayability status:
  - Assayable
  - Assayable with caution
  - Not assayable / hold for disposition

### Assay interpretation guardrails
- Primary endpoint is **observed β-LG IgE-binding reduction**, not clinical allergenicity reduction.
- Do not interpret lower IgE signal without recovery-normalized loading confirmation.
- Compare each sugar condition against its matched same-temperature no-sugar control.
- Escalate high-turbidity, low-recovery, or hard-to-reconstitute samples for caution review.
- Advancement requires no major contradiction from detectability or orthogonal confirmation data.
- Lower primary IgE signal alone is **not sufficient** for advancement.

### Planned caution rules
**Planned high caution = YES**
- glucose 60 C 4 h
- galactose 60 C 4 h
- mannose 60 C 4 h
  - B1-R06, B1-R07, B1-R08
  - B2-R06, B2-R07, B2-R08

**Monitor but not planned high caution**
- lactose 60 C 4 h
  - B1-R05, B2-R05

### Dry-state process warning
Do **not** treat stronger browning, caking, or lower recovery as evidence of better performance. These are overprocessing indicators and must be recorded as caution flags.

### Critical deviations requiring rerun or exclusion
- wrong donor, time, temperature, or ratio basis
- unresolved ratio basis / RH-equivalent / pre-equilibration duration at execution time
- incorrect or missing ultrasound
- failed RH/aw control or wrong conditioning workflow
- gross loading / geometry deviation
- major timing deviation
- sample mix-up or labeling uncertainty
- recovery failure making interpretation impossible

### Concise contingency rules
- **Critical deviation:** stop, flag, notify PI or delegated study lead, hold sample for disposition.
- **Noncritical deviation:** document, continue if sample remains valid, flag for caution.
- **Rerun authority:** PI or delegated study lead after deviation review.

### Pre-execution verification checklist
Before execution approval confirm:
1. ratio basis entered and benchmark-matched
2. RH/salt-equivalent entered and benchmark-matched
3. pre-equilibration duration entered and benchmark-matched
4. RH/aw tolerance entered
5. ultrasound settings entered
6. loading / geometry constants entered
7. SOPs current and verified
8. instrument calibration status current
9. reagent / donor lots recorded
10. assay reagents and IgE source confirmed for round consistency

---

### Source integration notes

Below I explain what components of this merged answer came from each prior answer and why I included them.

#### Components taken primarily from summary 1
Included:
- the strong **release-gating governance decision**
- the emphasis that the packet should not be released with unresolved:
  - ratio basis
  - RH-equivalent implementation
  - ultrasound details
- the stronger **all-run interpretability safeguards**
- the explicit statement that **low primary IgE signal alone is not sufficient**
- the use of **condition_id** plus **run_id**
- the idea of a **wet-lab packet plus metadata/QC logic**

Why included:
- Summary 1 had the strongest scientific governance and interpretability framing.
- It best protected against false-positive “success” calls driven by poor recovery or detectability collapse.
- It also best supported later evidence synthesis and AI usability.

#### Components taken primarily from summary 2
Included:
- the **five-part packet structure**
- the clearer **comparator-aware batch plan**
- the **contingency mini-plan**
- the concise **critical deviation / rerun criteria**
- the recommendation to keep Part B **lean but comparator-aware**
- the explicit note that native untreated β-LG belongs in **Part D**, not Part B

Why included:
- Summary 2 was the cleanest operational packet format for wet-lab handoff.
- Its Part C and Part E structure were especially practical for execution and governance.
- The contingency plan is useful without cluttering the main design.

#### Components taken primarily from summary 3
Included:
- the final choice that **planned high caution** applies only to:
  - glucose 60 C 4 h
  - galactose 60 C 4 h
  - mannose 60 C 4 h
- the dry-state wording:
  - **samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP**
- the stronger **restricted randomization** language
- the explicit **process metadata capture** and **post-recovery capture** fields
- the visible **sample-label syntax** with anchor/control status

Why included:
- Summary 3 had the best refinement of caution logic and the best practical metadata capture language.
- It also most clearly separated execution-facing fields from post-recovery interpretation fields.
- Its dry-state wording was the most operationally precise while remaining benchmark-linked.

#### Components synthesized across all three
Included:
- the final **24-run, 2-block dry-only design**
- the **within-block comparator logic**
- the **all-run Tier A assay package**
- the use of **anchors and no-sugar controls as protected comparators**
- the insistence that unresolved benchmark constants prevent execution release

Why included:
- These were the most consistent points across all meetings and represent the stable project consensus.

---

### Next Steps

1. **Retrieve and lock all release-gated benchmark constants immediately**
   - ratio basis
   - RH/salt-equivalent for aw 0.79
   - pre-equilibration duration
   - RH/aw tolerance
   - ultrasound SOP/settings
   - loading / geometry constants

2. **Populate those values into Parts A, B, and E**
   - remove all release-gate placeholders
   - verify against benchmark record

3. **Convert this packet into the lab’s controlled document format**
   - SOP IDs / versions
   - lot fields
   - document control metadata
   - approval signatures

4. **Prepare companion worksheets**
   - execution log
   - randomized block-specific prep/placement maps
   - assay plate map including native untreated β-LG reference
   - deviation log
   - post-recovery assayability/QC form

5. **Review once with wet-lab operators before release**
   - confirm no field is ambiguous
   - confirm SOP access at bench
   - confirm labels are practical
   - confirm equipment readiness

6. **Release only after all release blockers are resolved**
   - otherwise hold as draft and do not start bench work

This is my final merged recommendation and the best integrated wet-lab run-sheet packet for this stage.
### Agenda

Merge the prior meeting outputs into a **single, best-version wet-lab run-sheet packet** for the approved **dry-only β-LG variant A glycation screen**, while preserving the original stage purpose: **direct execution readiness**, not further strategy debate. The packet must be run-by-run, parameter-complete, comparator-aware, assay-interpretable, and suitable for later evidence synthesis / AI-facing use.

Because the prior meetings were aligned on the scientific design but differed in emphasis and table structure, I am issuing one consolidated answer that:

- keeps the **approved 12-condition dry-only design**
- uses **2 full independent process blocks** for a **24-run master list**
- preserves **within-block comparator logic**
- includes **explicit assay assignments and execution rules**
- adopts the strongest **QC / interpretability safeguards**
- and makes a clear governance decision on **release readiness**

---

### Team Member Input

#### Principal Investigator
- Repeatedly framed this stage as **operational translation**, not design revision.
- Confirmed the approved backbone:
  - β-LG variant A
  - dry-only
  - fixed aw backbone
  - fixed 1:2 ratio
  - ultrasound ON
  - 12-condition matrix
  - preferred 2 full independent process blocks
- Identified the main execution risks as:
  - unresolved ratio basis
  - unresolved aw/RH implementation
  - unresolved ultrasound details
  - unclear comparator structure
  - unclear assay assignment
  - unclear naming / control handling
- Requested a final packet that is both:
  - **wet-lab executable**
  - **analysis-ready**

#### Maillard Reaction Chemistry and Process Scientist
- Strongly emphasized that the remaining task is **process closure**.
- Required dry-state wording to include both:
  - scientific target: **aw = 0.79**
  - operational implementation: **benchmark RH-equivalent / pre-equilibration workflow**
- Required explicit control of:
  - ratio basis
  - RH setpoint / equivalent
  - pre-equilibration duration
  - deposition/loading
  - vessel geometry
  - time-zero rule
  - stop/cooling rule
  - recovery workflow
- Clarified no-sugar controls must be:
  - β-LG only
  - same solvent route
  - same ultrasound
  - same loading
  - same geometry
  - same dry workflow
  - no donor added
- Warned that:
  - browning
  - caking
  - poor recovery
  are **overprocessing flags**, not success signals.
- Supported planned high caution for **60 C / 4 h monosaccharides only**.

#### Allergenicity and Immunoassay Interpretation Scientist
- Emphasized that the packet must generate **interpretable immunoassay inputs**, not just processed samples.
- Required for **all runs**:
  - primary β-LG IgE-binding assay
  - recovered protein quantification
  - extractability/solubility assessment
  - turbidity/insolubility flag
  - matched loading normalization verification
- Strongly emphasized:
  - lower IgE signal alone is **not sufficient**
  - compare against matched no-sugar controls
  - normalize on recovered protein basis
  - escalate low-recovery / high-turbidity samples
- Supported:
  - native untreated β-LG as an **assay control**, not a process run
  - non-IgE β-LG detectability as mandatory for anchors and no-sugar controls
  - broader detectability / orthogonal support for high-priority or high-caution conditions
- Supported planned high caution for **60 C / 4 h monosaccharides only**.

#### Experimental Design and Evidence Synthesis Scientist
- Strongly supported an **explicit 24-run master list**, not shorthand replication.
- Emphasized that the two repeats are **independent process blocks**, not generic technical replicates.
- Recommended explicit comparator structure in the run table and batch plan:
  - within-block sugar vs matched no-sugar
  - within-block lactose 4 h vs lactose 2 h anchor
  - within-block glucose 4 h vs glucose 2 h anchor
  - cross-block comparison for replication only
- Recommended:
  - protected comparator runs
  - restricted randomization
  - separate randomized orders for Block 1 and Block 2
- Supported comparator-aware columns and human-readable purpose fields.

#### Scientific Critic
- Reiterated the true release blockers:
  1. ratio basis
  2. RH-equivalent implementation for aw 0.79
  3. ultrasound operational details / SOP acceptance
- Warned against scientifically precise but operationally vague wording.
- Requested visible:
  - critical deviation rules
  - QC checklist logic
  - final pre-release verification
- Supported concise, action-oriented execution notes.

#### Research Synthesis and Optimization Lead
- Strongly supported a packet that is both:
  - execution-facing
  - downstream-analysis ready
- Recommended explicit identity layers:
  - `condition_id`
  - `run_id`
  - `sample naming label`
- Supported one row per **process run**
- Recommended keeping Part B lean but comparator-aware
- Recommended controlled vocabularies for QC in companion capture
- Supported machine-readable sample labels with visible anchor/control status
- Recommended keeping post-run interpretation fields out of the run table itself.

---

### Recommendation

My recommendation is to issue a **five-part wet-lab packet** with a **24-run master run list** built from the approved **12-condition dry-only design**, executed as **2 full independent process blocks**.

However, I am making one firm governance decision:

> **This packet can be finalized as a controlled draft now, but it must not be released for bench execution until all benchmark-dependent operational constants are filled with actual values.**

Across the prior meetings, the team was unanimous that the following are **hard release gates**:

1. **protein:sugar ratio basis**
   - `1:2 w/w` or `1:2 molar`
2. **aw 0.79 operational implementation**
   - RH setpoint or validated salt-equivalent
   - pre-equilibration duration
   - acceptance/tolerance window
3. **ultrasound execution definition**
   - SOP ID/version
   - instrument/model
   - frequency
   - amplitude/power
   - pulse/continuous
   - duration
   - sample volume
   - vessel type
   - temperature control
   - pass/fail acceptance
4. **sample loading / geometry constants**
   - loaded protein mass
   - loaded sugar mass or no-sugar confirmation
   - total loaded solids
   - deposition volume / mass
   - vessel / substrate geometry

This is the only scientifically responsible position under the stage rule that **no critical experimental parameter may be left blank**.

Because the meeting summaries did **not** provide the actual benchmark numeric defaults, I cannot honestly label the packet below as execution-approved. The correct merged answer is therefore:

- provide the **best integrated final packet structure now**
- preserve all comparator and assay logic
- mark the unresolved benchmark-linked constants as **release blockers**
- and state clearly that **bench execution must not begin until those fields are populated from the benchmark SOP**

I am also choosing the following final structural positions:

- **Design**: unchanged 12-condition dry-only matrix
- **Replication**: 2 full independent process blocks, explicitly listed as 24 runs
- **Dry-state wording**:
  - target aw = 0.79
  - samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP
- **Planned high caution**:
  - YES for glucose 60 C 4 h, galactose 60 C 4 h, mannose 60 C 4 h
  - NO for lactose 60 C 4 h
- **All-run assay package**: mandatory Tier A for all 24 runs
- **Native untreated β-LG**: assay control only, not a process-matrix run
- **Comparator logic**: encoded in both Part B and Part C
- **Randomization**: restricted and block-specific
- **Naming**: machine-readable labels with anchor/control status visible

Below is the merged wet-lab packet.

---

## Part A. Round-level execution summary

### Objective of this round
Execute a **dry-only, matched bridge-and-calibration round** under a fixed controlled-aw, fixed-ratio, ultrasound-assisted backbone to:

1. determine donor ranking at **4 h** under matched dry conditions,
2. compare **55 C vs 60 C** within donor at 4 h,
3. test whether **4 h** is justified relative to the benchmark-linked **60 C, 2 h** region for lactose and glucose,
4. distinguish **sugar-associated observed β-LG IgE-binding reduction** from **process-only effects** using matched 4 h no-sugar controls,
5. generate a clean, comparator-linked dataset for restricted-domain decision support and later evidence/model synthesis.

### Fixed variables
- Protein: **β-LG variant A**
- Reaction mode: **Dry only**
- Target aw: **0.79**
- Dry-state implementation: **samples pre-equilibrated to benchmark RH-equivalent corresponding to aw 0.79, then reacted under benchmark dry-incubation SOP**
- Protein:sugar ratio: **1:2**
- Ratio basis: **RELEASE GATE — must be entered as either `w/w` or `molar`**
- Pretreatment: **Ultrasound ON**
- Ultrasound execution: **fixed benchmark SOP; full settings must be entered before release**
- Sample preparation route: **fixed benchmark SOP**
- Deposition/loading geometry: **fixed benchmark SOP**
- Vessel/substrate type: **fixed benchmark SOP**
- Pre-equilibration workflow: **fixed benchmark SOP**
- Incubation workflow: **fixed benchmark SOP**
- Cooling/stop workflow: **fixed benchmark SOP**
- Recovery/reconstitution workflow: **fixed benchmark SOP**
- Primary IgE assay platform: **benchmark-matched**
- Same IgE source / serum pool across round
- Same untreated/native β-LG reference across analytical campaign
- Same β-LG lot across round if feasible
- Same donor lots/grades across round if feasible
- Replication plan: **2 independent full process blocks**

### Scanned variables
- Sugar donor:
  - lactose
  - glucose
  - galactose
  - mannose
  - none (process-only controls)
- Temperature:
  - 55 C
  - 60 C
- Time:
  - 4 h for donor bridge panel and no-sugar controls
  - 2 h only for lactose and glucose anchors at 60 C

### Deferred variables
Not optimized in this round:
- wet-state mode
- pH / buffer
- aw variation
- RH variation beyond benchmark-matched implementation
- ratio variation
- ultrasound variation
- no-ultrasound controls
- other pretreatments
- 3 h intermediate time
- broader donor expansion
- direct clinical allergenicity assessment

### Execution approval status
**DRAFT / NOT FOR EXECUTION** until all release-gated benchmark constants are entered:
1. ratio basis
2. RH-equivalent implementation for aw 0.79
3. pre-equilibration duration and tolerance
4. ultrasound SOP/settings and pass/fail rule
5. deposition/loading/geometry constants

---

## Part B. Master run list

**Controlled wording for assay columns**
- **Primary assay(s):** `Primary β-LG IgE-binding; Recovered protein quantification; Extractability/solubility assessment; Turbidity/insolubility flag; Loading normalization verification`
- **Optional assay(s):**
  - `Non-IgE β-LG detectability preferred`
  - `Non-IgE β-LG detectability mandatory`
  - `Orthogonal confirmation mandatory`
  - `Free lysine proxy preferred`
  - `Planned high caution`

| run_id | condition_id | group_id | purpose | sugar donor | protein:sugar ratio | mode | temperature_C | time_h | pH or aw/RH | pretreatment | sugar/no-sugar control status | replicate_id | primary assay(s) | optional assay(s) | sample naming label |
|---|---|---|---|---|---|---|---:|---:|---|---|---|---|---|---|---|
| B1-R01 | COND_LAC_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | Primary β-LG IgE-binding; Recovered protein quantification; Extractability/solubility assessment; Turbidity/insolubility flag; Loading normalization verification | Non-IgE β-LG detectability preferred | B1-LAC-55C-4H-SUG |
| B1-R02 | COND_GLU_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-GLU-55C-4H-SUG |
| B1-R03 | COND_GAL_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs galactose 60 C 4 h | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-GAL-55C-4H-SUG |
| B1-R04 | COND_MAN_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs mannose 60 C 4 h | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-MAN-55C-4H-SUG |
| B1-R05 | COND_LAC_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; lactose time bridge vs lactose 60 C 2 h anchor | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred | B1-LAC-60C-4H-SUG |
| B1-R06 | COND_GLU_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; glucose time bridge vs glucose 60 C 2 h anchor | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-GLU-60C-4H-SUG |
| B1-R07 | COND_GAL_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-GAL-60C-4H-SUG |
| B1-R08 | COND_MAN_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B1 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B1-MAN-60C-4H-SUG |
| B1-R09 | COND_LAC_60C_2H_ANC | G-TIME-LAC | Same-round lactose anchor; benchmark continuity; within-block comparator for lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-LAC-60C-2H-ANC |
| B1-R10 | COND_GLU_60C_2H_ANC | G-TIME-GLU | Same-round glucose anchor; benchmark continuity; within-block comparator for glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-GLU-60C-2H-ANC |
| B1-R11 | COND_NONE_55C_4H_CTL | G-CTRL55 | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-NS-55C-4H-CTRL |
| B1-R12 | COND_NONE_60C_4H_CTL | G-CTRL60 | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B1 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B1-NS-60C-4H-CTRL |
| B2-R01 | COND_LAC_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-LAC-55C-4H-SUG |
| B2-R02 | COND_GLU_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-GLU-55C-4H-SUG |
| B2-R03 | COND_GAL_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs galactose 60 C 4 h | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-GAL-55C-4H-SUG |
| B2-R04 | COND_MAN_55C_4H_SUG | G-DONOR55 | 55 C donor ranking; matched to 55 C no-sugar control; temperature comparison vs mannose 60 C 4 h | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-MAN-55C-4H-SUG |
| B2-R05 | COND_LAC_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; lactose time bridge vs lactose 60 C 2 h anchor | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred | B2-LAC-60C-4H-SUG |
| B2-R06 | COND_GLU_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control; glucose time bridge vs glucose 60 C 2 h anchor | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-GLU-60C-4H-SUG |
| B2-R07 | COND_GAL_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Galactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-GAL-60C-4H-SUG |
| B2-R08 | COND_MAN_60C_4H_SUG | G-DONOR60 | 60 C donor ranking; matched to 60 C no-sugar control | Mannose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Sugar | B2 | same as above | Non-IgE β-LG detectability preferred; Planned high caution | B2-MAN-60C-4H-SUG |
| B2-R09 | COND_LAC_60C_2H_ANC | G-TIME-LAC | Same-round lactose anchor; benchmark continuity; within-block comparator for lactose 60 C 4 h | Lactose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-LAC-60C-2H-ANC |
| B2-R10 | COND_GLU_60C_2H_ANC | G-TIME-GLU | Same-round glucose anchor; benchmark continuity; within-block comparator for glucose 60 C 4 h | Glucose | 1:2 [RELEASE GATE: basis = w/w or molar] | Dry | 60 | 2 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | Anchor sugar run | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-GLU-60C-2H-ANC |
| B2-R11 | COND_NONE_55C_4H_CTL | G-CTRL55 | Process-only comparator for all 55 C 4 h sugar runs | None | None | Dry | 55 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-NS-55C-4H-CTRL |
| B2-R12 | COND_NONE_60C_4H_CTL | G-CTRL60 | Process-only comparator for all 60 C 4 h sugar runs and 60 C anchors | None | None | Dry | 60 | 4 | aw 0.79 target; RH-equivalent [RELEASE GATE]; pre-eq [RELEASE GATE] | Ultrasound ON [RELEASE GATE SOP/settings] | No-sugar control | B2 | same as above | Non-IgE β-LG detectability mandatory; Orthogonal confirmation mandatory; Free lysine proxy preferred | B2-NS-60C-4H-CTRL |

---

## Part C. Batch execution plan

### Batch grouping
- **Preferred execution:** 2 independent full process blocks
  - **Block 1:** B1-R01 to B1-R12
  - **Block 2:** B2-R01 to B2-R12
- Each block must contain the full **12-condition matrix** exactly once.
- Blocks should be executed as **independent process realizations**, preferably on separate days or separated execution windows.

### Which runs should be processed together
Within each block:
- prepare all 12 runs under one coordinated workflow
- apply the same benchmark sample-preparation route
- apply the same ultrasound SOP
- pre-equilibrate all samples under the same benchmark RH-equivalent workflow
- execute 55 C and 60 C conditions within the same protected block campaign
- recover all samples under the same fixed recovery SOP

Do **not** split a block into donor-isolated mini-batches.

If staggered handling is required:
- intersperse 55 C and 60 C runs
- intersperse sugar and no-sugar runs
- intersperse anchors and bridge runs
- preserve comparator balance

### Matched-comparison grouping

#### 55 C sugar vs process-only
- Block 1:
  - B1-R01, B1-R02, B1-R03, B1-R04 matched to **B1-R11**
- Block 2:
  - B2-R01, B2-R02, B2-R03, B2-R04 matched to **B2-R11**

#### 60 C sugar vs process-only
- Block 1:
  - B1-R05, B1-R06, B1-R07, B1-R08 matched to **B1-R12**
- Block 2:
  - B2-R05, B2-R06, B2-R07, B2-R08 matched to **B2-R12**

#### Lactose time bridge
- Block 1:
  - **B1-R05** matched to **B1-R09**
- Block 2:
  - **B2-R05** matched to **B2-R09**

#### Glucose time bridge
- Block 1:
  - **B1-R06** matched to **B1-R10**
- Block 2:
  - **B2-R06** matched to **B2-R10**

#### Temperature pairs within donor
- lactose:
  - B1-R01 vs B1-R05
  - B2-R01 vs B2-R05
- glucose:
  - B1-R02 vs B1-R06
  - B2-R02 vs B2-R06
- galactose:
  - B1-R03 vs B1-R07
  - B2-R03 vs B2-R07
- mannose:
  - B1-R04 vs B1-R08
  - B2-R04 vs B2-R08

#### Cross-block comparison
- used for **replication / confirmation only**
- not a substitute for within-block matched comparison

### Protected comparator runs
The following are protected comparator runs and must not be dropped or deprioritized:
- Block 1: **B1-R09, B1-R10, B1-R11, B1-R12**
- Block 2: **B2-R09, B2-R10, B2-R11, B2-R12**

If a protected comparator fails, dependent comparison sets in that block must be flagged as reduced in interpretability and reviewed for rerun.

### Restricted randomization / balancing rules
- Use **different randomized prep/placement plans** for Block 1 and Block 2.
- Randomize:
  - sample preparation order
  - chamber/incubator position
  - assay plate placement
- Do **not** group runs entirely by:
  - donor
  - temperature
  - control class
- Distribute anchors and no-sugar controls across chamber positions and assay plates.
- If multiple assay plates are required, distribute protected comparators across plates or use a validated bridging layout.
- Record chamber/incubator ID and position for every run.

### Contingency plan — use only if full second block cannot be executed
Priority order:
1. lactose 60 C 2 h anchor
2. glucose 60 C 2 h anchor
3. no-sugar 55 C 4 h control
4. no-sugar 60 C 4 h control
5. top 2 apparent 4 h sugar conditions from Block 1
6. one additional high-caution/high-reduction condition if distinct

---

## Part D. Assay plan

### Assays required for all runs
Apply to all 24 process runs:

1. **Primary β-LG IgE-binding assay**
   - benchmark-matched format
   - same IgE source / serum pool across round

2. **Recovered protein quantification**

3. **Extractability / solubility assessment**
   - recovered volume
   - recovered protein concentration
   - ease of reconstitution
   - visible insoluble residue / pellet

4. **Turbidity / insolubility flag**

5. **Loading normalization verification**
   - assay input normalized on recovered-protein basis

### Native untreated β-LG reference
- Include as an **assay control**, not a process-matrix run.
- Include on every primary assay plate or use a validated plate-linking scheme.
- Include in every orthogonal assay batch.

### Interpretation-support assays

#### Non-IgE β-LG detectability
- Preferred on all runs if feasible.
- Mandatory minimum subset:
  - B1-R09, B1-R10, B1-R11, B1-R12
  - B2-R09, B2-R10, B2-R11, B2-R12
  - top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
  - any high-caution/high-reduction condition
  - any condition proposed for advancement

#### Free lysine proxy
Preferred on:
- all anchors
- all no-sugar controls
- top 2–4 apparent 4 h winners
- one distinct high-caution comparator if needed

### Selected runs for orthogonal confirmation

#### Mandatory pre-assigned subset
- Anchors in both blocks:
  - B1-R09, B1-R10, B2-R09, B2-R10
- No-sugar controls in both blocks:
  - B1-R11, B1-R12, B2-R11, B2-R12

These receive:
- non-IgE β-LG detectability
- orthogonal β-LG IgE-binding assay with different antigen-presentation mode
- free lysine proxy preferred

#### Conditional orthogonal subset after Tier A review
Add:
- top 2 apparent 4 h sugar conditions by recovery-normalized IgE reduction
- one additional high-caution apparent reducer if distinct
- any condition proposed for advancement
- optionally one unexpectedly strong no-sugar control if observed

### Tier B orthogonal confirmation package
1. Orthogonal β-LG IgE-binding assay with different antigen-presentation mode
2. Gel-based aggregation / profile check
3. Confirmation of comparable recovered antigen handling

### Interpretation-support triggers
Escalate for adjudication if any of the following occur:
- unexpectedly strong reduction in no-sugar control
- severe turbidity / particulate carryover
- large reduction with poor recovery
- major drop in non-IgE β-LG detectability
- disagreement between primary and orthogonal IgE assay formats

---

## Part E. Execution notes

### Parameter definitions
- **Protein:** β-LG variant A
- **Mode:** Dry-state glycation only
- **Dry-state implementation:** samples are pre-equilibrated to benchmark RH-equivalent corresponding to target aw 0.79 for the benchmark-defined duration, then incubated under the benchmark dry-incubation SOP.
- **Protein:sugar ratio:**
  - sugar runs: `1:2 [RELEASE GATE — enter w/w or molar exactly as benchmark]`
  - no-sugar controls: no donor added
- **Pretreatment:** Ultrasound ON per benchmark SOP
- **Sample loading/geometry:** fixed benchmark deposition and vessel geometry per SOP; identical loaded mass, vessel type, and sample format across all runs

### Release-gated constants to enter before execution
Enter actual values before release:
- ratio basis: `[w/w or molar]`
- RH setpoint or salt-equivalent for aw 0.79: `[REQUIRED]`
- pre-equilibration duration: `[REQUIRED]`
- RH/aw tolerance / acceptance window: `[REQUIRED]`
- ultrasound SOP ID/version: `[REQUIRED]`
- ultrasound instrument/model: `[REQUIRED]`
- ultrasound frequency: `[REQUIRED]`
- ultrasound amplitude/power: `[REQUIRED]`
- ultrasound pulse vs continuous: `[REQUIRED]`
- ultrasound duration: `[REQUIRED]`
- ultrasound sample volume: `[REQUIRED]`
- ultrasound vessel type: `[REQUIRED]`
- ultrasound temperature control method: `[REQUIRED]`
- loaded protein mass per sample: `[REQUIRED]`
- loaded sugar mass per sample or no-sugar confirmation: `[REQUIRED]`
- total loaded solids: `[REQUIRED]`
- deposition volume / mass: `[REQUIRED]`
- vessel / substrate geometry: `[REQUIRED]`

### Ultrasound pass/fail acceptance
- correct SOP and instrument used
- correct programmed setting range used
- correct duration range used
- correct sample volume / vessel type used
- no documented temperature excursion beyond SOP limit
- no operator-recorded application failure

### Timing rules
- **Time zero definition:** reaction time begins when the sample is placed into the pre-equilibrated incubation environment at target temperature per benchmark SOP.
- **Stop rule:** reaction ends at physical removal from that environment for immediate cooling/stop per SOP.
- Record actual:
  - equilibration start/stop
  - incubation start/stop
  - cooling/stop time
  - recovery time
- Major timing deviation is a critical deviation.

### Control rules
- No-sugar controls are matched process-only comparators and must be prepared in each block.
- No-sugar controls must be:
  - β-LG only
  - same protein loading
  - same solvent route
  - same ultrasound
  - same deposition geometry
  - same dry-state workflow
  - same recovery workflow
  - no donor added
- 55 C 4 h sugar runs must be interpreted against matched 55 C 4 h no-sugar control from the same block.
- 60 C 4 h sugar runs must be interpreted against matched 60 C 4 h no-sugar control from the same block.
- Lactose 60 C 4 h must be interpreted against lactose 60 C 2 h anchor from the same block.
- Glucose 60 C 4 h must be interpreted against glucose 60 C 2 h anchor from the same block.
- Cross-block replication supports confirmation; it does not replace within-block comparator logic.
- Native untreated β-LG is an assay control, not a process run.

### Naming rules
- **Condition ID format:** `COND_[DonorCode]_[TempC]C_[TimeH]_[StatusCode]`
- **Sample label format:** `[Block]-[Donor]-[Temp]-[Time]-[Status]`
- Donor codes:
  - `LAC`
  - `GLU`
  - `GAL`
  - `MAN`
  - `NONE` or `NS`
- Status codes:
  - `SUG` = sugar run
  - `ANC` = anchor
  - `CTRL` = no-sugar control
- No spaces or special characters.

### Required process metadata capture
For each run record:
- operator
- process block
- prep date/time
- actual protein mass
- actual sugar mass or no-sugar confirmation
- actual loaded mass / total solids
- deposition volume
- equilibration start/stop
- incubation start/stop
- chamber/incubator ID
- chamber position
- RH/aw check if available
- ultrasound pass/fail
- sample appearance before and after incubation:
  - free-flowing
  - film
  - caked
  - glassy
  - crystalline
  - browned
- reconstitution behavior
- visible pellet yes/no
- recovered volume
- turbidity score
- deviations
- disposition

### Required post-recovery capture fields
- recovered volume
- recovered protein concentration
- dilution factor into assay
- normalized loading concentration
- visible pellet
- turbidity
- storage condition if not assayed immediately
- freeze-thaw count
- assayability status:
  - Assayable
  - Assayable with caution
  - Not assayable / hold for disposition

### Assay interpretation guardrails
- Primary endpoint is **observed β-LG IgE-binding reduction**, not clinical allergenicity reduction.
- Do not interpret lower IgE signal without recovery-normalized loading confirmation.
- Compare each sugar condition against its matched same-temperature no-sugar control.
- Escalate high-turbidity, low-recovery, or hard-to-reconstitute samples for caution review.
- Advancement requires no major contradiction from detectability or orthogonal confirmation data.
- Lower primary IgE signal alone is **not sufficient** for advancement.

### Planned caution rules
**Planned high caution = YES**
- glucose 60 C 4 h
- galactose 60 C 4 h
- mannose 60 C 4 h
  - B1-R06, B1-R07, B1-R08
  - B2-R06, B2-R07, B2-R08

**Monitor but not planned high caution**
- lactose 60 C 4 h
  - B1-R05, B2-R05

### Dry-state process warning
Do **not** treat stronger browning, caking, or lower recovery as evidence of better performance. These are overprocessing indicators and must be recorded as caution flags.

### Critical deviations requiring rerun or exclusion
- wrong donor, time, temperature, or ratio basis
- unresolved ratio basis / RH-equivalent / pre-equilibration duration at execution time
- incorrect or missing ultrasound
- failed RH/aw control or wrong conditioning workflow
- gross loading / geometry deviation
- major timing deviation
- sample mix-up or labeling uncertainty
- recovery failure making interpretation impossible

### Concise contingency rules
- **Critical deviation:** stop, flag, notify PI or delegated study lead, hold sample for disposition.
- **Noncritical deviation:** document, continue if sample remains valid, flag for caution.
- **Rerun authority:** PI or delegated study lead after deviation review.

### Pre-execution verification checklist
Before execution approval confirm:
1. ratio basis entered and benchmark-matched
2. RH/salt-equivalent entered and benchmark-matched
3. pre-equilibration duration entered and benchmark-matched
4. RH/aw tolerance entered
5. ultrasound settings entered
6. loading / geometry constants entered
7. SOPs current and verified
8. instrument calibration status current
9. reagent / donor lots recorded
10. assay reagents and IgE source confirmed for round consistency

---

### Source integration notes

Below I explain what components of this merged answer came from each prior answer and why I included them.

#### Components taken primarily from summary 1
Included:
- the strong **release-gating governance decision**
- the emphasis that the packet should not be released with unresolved:
  - ratio basis
  - RH-equivalent implementation
  - ultrasound details
- the stronger **all-run interpretability safeguards**
- the explicit statement that **low primary IgE signal alone is not sufficient**
- the use of **condition_id** plus **run_id**
- the idea of a **wet-lab packet plus metadata/QC logic**

Why included:
- Summary 1 had the strongest scientific governance and interpretability framing.
- It best protected against false-positive “success” calls driven by poor recovery or detectability collapse.
- It also best supported later evidence synthesis and AI usability.

#### Components taken primarily from summary 2
Included:
- the **five-part packet structure**
- the clearer **comparator-aware batch plan**
- the **contingency mini-plan**
- the concise **critical deviation / rerun criteria**
- the recommendation to keep Part B **lean but comparator-aware**
- the explicit note that native untreated β-LG belongs in **Part D**, not Part B

Why included:
- Summary 2 was the cleanest operational packet format for wet-lab handoff.
- Its Part C and Part E structure were especially practical for execution and governance.
- The contingency plan is useful without cluttering the main design.

#### Components taken primarily from summary 3
Included:
- the final choice that **planned high caution** applies only to:
  - glucose 60 C 4 h
  - galactose 60 C 4 h
  - mannose 60 C 4 h
- the dry-state wording:
  - **samples pre-equilibrated to benchmark RH-equivalent, then reacted under benchmark dry-incubation SOP**
- the stronger **restricted randomization** language
- the explicit **process metadata capture** and **post-recovery capture** fields
- the visible **sample-label syntax** with anchor/control status

Why included:
- Summary 3 had the best refinement of caution logic and the best practical metadata capture language.
- It also most clearly separated execution-facing fields from post-recovery interpretation fields.
- Its dry-state wording was the most operationally precise while remaining benchmark-linked.

#### Components synthesized across all three
Included:
- the final **24-run, 2-block dry-only design**
- the **within-block comparator logic**
- the **all-run Tier A assay package**
- the use of **anchors and no-sugar controls as protected comparators**
- the insistence that unresolved benchmark constants prevent execution release

Why included:
- These were the most consistent points across all meetings and represent the stable project consensus.

---

### Next Steps

1. **Retrieve and lock all release-gated benchmark constants immediately**
   - ratio basis
   - RH/salt-equivalent for aw 0.79
   - pre-equilibration duration
   - RH/aw tolerance
   - ultrasound SOP/settings
   - loading / geometry constants

2. **Populate those values into Parts A, B, and E**
   - remove all release-gate placeholders
   - verify against benchmark record

3. **Convert this packet into the lab’s controlled document format**
   - SOP IDs / versions
   - lot fields
   - document control metadata
   - approval signatures

4. **Prepare companion worksheets**
   - execution log
   - randomized block-specific prep/placement maps
   - assay plate map including native untreated β-LG reference
   - deviation log
   - post-recovery assayability/QC form

5. **Review once with wet-lab operators before release**
   - confirm no field is ambiguous
   - confirm SOP access at bench
   - confirm labels are practical
   - confirm equipment readiness

6. **Release only after all release blockers are resolved**
   - otherwise hold as draft and do not start bench work

This is my final merged recommendation and the best integrated wet-lab run-sheet packet for this stage.

