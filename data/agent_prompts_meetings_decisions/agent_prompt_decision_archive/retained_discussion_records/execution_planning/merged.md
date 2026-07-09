## User

This is the beginning of an individual meeting with Principal Investigator to discuss your research project.

Here are summaries of the previous meetings:

[begin summary 1]

### Agenda

We are at the **execution-planning stage** for the β-LG variant A glycation project. The task is to convert the previously agreed project specification into **one directly executable wet-lab round** that can be handed to the lab for run-sheet generation.

The round must:

- center on a **dry-state donor bridge**,
- include the required primary donors:
  - **lactose**
  - **glucose**
  - **galactose**
  - **mannose**
- remain within the main practical window:
  - **55–60 C**
  - **2–4 h**
  - **ultrasound-centered**
- treat **time as a trade-off variable**, not as something to maximize by default,
- include the **minimum controls and validation runs** needed for interpretation,
- and explicitly include a **pentose branch** that tests both **arabinose** and **ribose** to determine whether a pentose should be advanced, and under what conditions.

The required output is a **complete wet-lab plan**, not abstract strategy.

---

### Team Member Input

#### Principal Investigator

I framed the meeting around converting prior strategy into a **single execution-ready round**. I emphasized that the round must protect the **matched dry-state donor bridge**, must not drift into broad side expansions, and must include a real **pentose decision branch** rather than leaving arabinose vs ribose unresolved.

My initial bias was toward:

- a **4 h full donor bridge** at **55 C and 60 C** under dry conditions with ultrasound,
- selected **no-ultrasound controls**,
- and a **minimal earlier-time subset** so the plan itself can test whether **4 h earns its place**.

After round 1, I provisionally locked the following:

- **mode:** dry
- **moisture condition:** **aw 0.79**
- **ratio:** **1:2 protein:sugar (w/w)**
- **temperatures:** **55 C and 60 C only**
- **times:** **4 h main + 3 h subset**
- **pretreatment:** lab-default ultrasound, unchanged
- **donors:** lactose, glucose, galactose, mannose, arabinose, ribose
- **no pH expansion**
- **no wet-mode expansion**
- **no broad donor-ratio sweep**
- **no additional pretreatment families**
- **n = 3 biological replicates per condition**

I also provisionally accepted the **23-condition base matrix** as the smallest coherent one-round plan that still answers all required questions.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry scientist strongly supported a **single common ratio** across all donors, including pentoses:

- **protein:sugar = 1:2 (w/w)**

The key point was that this round is a **matched decision experiment**, not donor-specific optimization. Lowering pentose loading now would reduce interpretability.

Other major chemistry recommendations:

- keep **aw 0.79** fixed for all runs,
- carry forward **existing lab-default ultrasound settings** unchanged,
- if only one earlier timepoint is included, choose **3 h**, not 2 h,
- and do not let pentose numerical strength alone drive advancement.

The chemistry scientist stressed that pentoses, especially **ribose**, can appear strong because they are **overreactive**, not because they are the most practical donors. Therefore pentoses should face a stricter interpretation standard.

In round 2, the chemistry scientist added that the final run sheet should specify donor loading in both:
- **relative form**: 1:2 (w/w)
- and an **absolute example** for handling clarity, such as:
  - **100 mg β-LG + 200 mg donor**

They also recommended adding one low-burden chemistry-facing observation to all runs:

- **visual browning score** on a fixed 0–3 scale

They did **not** support adding **60 C, 3 h ribose** in this round.

A chemistry-specific advancement caution was proposed:

> A donor should not be favored if improved primary reduction mainly coincides with stronger browning, poorer recovery, and more aggregation without an earlier-time or lower-temperature advantage.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology scientist agreed with the fixed dry-state bridge and the 3 h checkpoint, but emphasized that raw reduction values cannot be treated as equivalent to true biologically meaningful allergenicity reduction.

Key interpretation principles raised:

- lower signal can reflect:
  - true epitope disruption,
  - but also masking,
  - reduced extractability,
  - aggregation,
  - altered assay geometry,
  - or coating artifacts.
- therefore the round must answer both:
  1. which conditions reduce the primary immunoassay signal,
  2. which reductions are **interpretable and biologically credible**.

The immunology scientist strongly supported including **both arabinose and ribose** experimentally.

They required backbone-matched **heated no-sugar controls** for interpretation, specifically:
- **55 C, 4 h, ultrasound**
- **60 C, 4 h, ultrasound**
- **55 C, 3 h, ultrasound**
- **55 C, 4 h, no ultrasound**

They proposed a **tiered assay package**:

For **all runs**:
- primary immunoassay
- extractable protein / recovery
- appearance / reconstitution notes

For expanded protection:
- reducing SDS-PAGE for:
  - all pentose runs
  - all no-sugar controls
  - all no-ultrasound donor runs
  - and above-threshold hexose runs

For confirmation:
- orthogonal immunological confirmation for:
  - best hexose
  - best pentose
  - and additional suspicious or near-leading branches if needed

In round 2, they made the recovery rule operational:

- **>=70% of matched heated no-sugar control**: promotion-eligible
- **50–69%**: caution zone
- **<50%**: no-go

They also recommended:
- automatic SDS-PAGE on all pentose runs, all controls, and all no-ultrasound donor runs,
- SDS-PAGE on any hexose run with **>=70% reduction** or within **<10 points** of the leading hexose,
- orthogonal confirmation on:
  - best hexose
  - best pentose
  - and any **>=80%** or close-call suspicious branch

A key interpretability rule they proposed was:

> A condition with strong apparent reduction but poor recovery, dominant aggregation, or failed orthogonal confirmation should be treated as a likely artifact or masking-dominant effect and should not be promoted.

---

#### Experimental Design and Evidence Synthesis Scientist

The design scientist translated the strategy into the smallest one-round structure that still answers all required questions.

They defined five mandatory decision questions for the round:

1. hexose donor ranking under matched dry 4 h conditions,
2. pentose advancement question,
3. 55 C vs 60 C trade-off,
4. 3 h vs 4 h trade-off,
5. ultrasound necessity/enabling/marginality.

They proposed a **23-condition matrix** composed of four run roles:

##### Run role A — primary donor bridge
All 6 donors at:
- **55 C, 4 h, ultrasound**
- **60 C, 4 h, ultrasound**

= **12 runs**

##### Run role B — time-tradeoff subset
At **55 C, 3 h, ultrasound**:
- lactose
- glucose
- arabinose
- ribose

= **4 runs**

##### Run role C — no-ultrasound sentinels
At **55 C, 4 h, no ultrasound**:
- lactose
- glucose
- ribose

= **3 runs**

##### Run role D — shared no-sugar controls
- 55 C, 4 h, ultrasound
- 60 C, 4 h, ultrasound
- 55 C, 3 h, ultrasound
- 55 C, 4 h, no ultrasound

= **4 runs**

Total = **23 conditions**

They also formalized assay assignment:

- **S1 / universal screening package** for all runs
- **S2 / sample-state package** for all pentose, control, no-ultrasound, and triggered hexose runs
- **S3 / orthogonal confirmation** for best hexose, best pentose, and ambiguous lead branches

In round 2, they recommended keeping the no-ultrasound sentinel set as:

- lactose
- glucose
- ribose

and proposed a clean advancement hierarchy:

1. efficacy band,
2. practical preference,
3. interpretability gate,
4. donor-class rule,
5. scope of advancement.

---

#### Scientific Critic

The critic mainly pressured the plan on two fronts:

1. avoid **overdesign**,
2. avoid **underprotection**.

In round 1, the critic argued that testing both temperatures for all pentoses could be excessive and suggested that **60 C pentose runs** would be the first place to cut if capacity were limited. I did **not** adopt that suggestion because the agenda explicitly requires that pentose advancement and condition dependence be answered in this round.

The critic also emphasized that pentose interpretation guardrails must be strong enough to prevent false promotion through aggregation or extraction artifacts.

In round 2, the critic accepted the **23-condition layout** and agreed that the smallest acceptable pentose branch includes:
- arabinose and ribose at **55 C and 60 C, 4 h**
- **55 C, 3 h**
- and **ribose no-ultrasound**

The critic’s strongest useful final contributions were:
- simplify operational logic where possible,
- use clear run-role labeling,
- and keep advancement rules concise enough for wet-lab teams to apply.

They suggested simplifying assay logic into fewer tiers. I have partially incorporated that by retaining the functional distinction among:
- universal screening,
- automatic sample-state assessment,
- targeted orthogonal confirmation,
while keeping the final wording operational and not overly elaborate.

---

### Recommendation

My final recommendation is to execute a **23-condition dry-state matched donor bridge round** with embedded time- and ultrasound-interpretation protection, using a common **1:2 protein:sugar ratio**, fixed **aw 0.79**, and the lab’s current ultrasound settings.

This is the **preferred execution-ready plan** because it is the smallest single round that still answers all of the project’s mandatory questions:

- hexose donor ranking,
- pentose donor decision,
- 55 C vs 60 C trade-off,
- 3 h vs 4 h trade-off,
- and ultrasound classification,

while also satisfying the requirement to include minimum validation needed for interpretation.

I am choosing this plan over smaller alternatives because:

1. a **4 h-only** screen would fail to test whether 4 h is actually worth carrying forward;
2. omitting either **arabinose or ribose** would fail the explicit pentose requirement;
3. dropping **60 C pentose runs** would leave the “if so, under what conditions?” part of the pentose question only partially answered;
4. skipping **no-sugar controls** or sample-state checks would create a serious risk of artifact-driven promotion;
5. broadening beyond this matrix into wet mode, pH, ratio sweeps, or other pretreatments would reduce decision efficiency.

Below is the final plan in the required execution format.

---

## 1. Round objective

Run a **dry-state, ultrasound-centered donor bridge** to identify the most practical glycation condition region for reducing β-LG variant A allergenicity, while explicitly testing:

- matched ranking of **lactose, glucose, galactose, mannose**,
- whether **arabinose or ribose** deserves advancement,
- whether **55 C** can substitute for or outperform **60 C** practically,
- whether **4 h** is meaningfully better than **3 h**,
- and whether ultrasound is **necessary, enabling, or marginal** for key branches.

The round is designed to optimize the **efficient frontier**, not the maximum reduction alone.

---

## 2. Fixed variables

These variables are fixed across the round unless explicitly noted in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)**
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **temperature window:** 55 C or 60 C only
- **time window in this round:** 3 h or 4 h only
- **pretreatment main arm:** ultrasound, using **current lab-default settings unchanged**
- **no-ultrasound condition:** identical processing except ultrasound omitted
- **replication:** **n = 3 biological replicates per condition**
- **reconstitution/extraction SOP:** one standardized lab SOP across all runs
- **primary assay platform:** same assay family used for current `reduction_pct_reported`
- **browning note:** fixed 0–3 visual score for all runs
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

---

## 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 3 h
  - 4 h
- **ultrasound status**
  - yes
  - no

---

## 4. Final experiment matrix

### Assay package definitions
- **P1 = universal screening**
  - primary immunoassay
  - extractable protein recovery
  - appearance/reconstitution notes
  - browning score
- **P2 = sample-state package**
  - all of P1
  - reducing SDS-PAGE
  - soluble/insoluble fraction note if routine
- **P3 = orthogonal confirmation package**
  - orthogonal immunoassay
  - repeat extraction consistency check
  - applied only to advancement-candidate runs after P1/P2 review

> All runs receive P1 or P2 as assigned below.  
> P3 is a planned validation step applied to the top branches defined in the assay plan.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | primary_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R02 | primary_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R03 | primary_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R04 | primary_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R05 | primary_bridge_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R06 | primary_bridge_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R07 | primary_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R08 | primary_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R09 | primary_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R10 | primary_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R11 | primary_bridge_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R12 | primary_bridge_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R13 | time_subset | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R14 | time_subset | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R15 | time_subset_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R16 | time_subset_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R17 | no_ultrasound_sentinel | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R18 | no_ultrasound_sentinel | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R19 | no_ultrasound_sentinel_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R20 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R21 | backbone_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R22 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R23 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | yes | yes | 3 | P2 |

### Validation runs planned within this round
No additional condition branches are added beyond R01–R23.  
Minimum validation is built into the round via:
- backbone controls,
- P2 sample-state package,
- and planned **P3 orthogonal confirmation** for top candidates after primary-screen review.

---

## 5. Pentose branch design

### Pentose runs included
- **R05** arabinose, 55 C, 4 h, +US
- **R06** ribose, 55 C, 4 h, +US
- **R11** arabinose, 60 C, 4 h, +US
- **R12** ribose, 60 C, 4 h, +US
- **R15** arabinose, 55 C, 3 h, +US
- **R16** ribose, 55 C, 3 h, +US
- **R19** ribose, 55 C, 4 h, –US

### Pentose decision question
The pentose branch is designed to answer:

> Does either arabinose or ribose produce a practically credible allergenicity-reduction signal strong enough to justify advancement relative to the best hexose branch, and if so, is that signal achievable under acceptable severity and interpretability conditions?

Sub-questions:
1. **arabinose vs ribose** at matched 4 h conditions
2. whether pentose performance depends on **55 C vs 60 C**
3. whether pentose performance depends on extending from **3 h to 4 h**
4. whether **ribose** depends materially on ultrasound
5. whether any pentose advantage survives:
   - recovery filtering
   - aggregation/state assessment
   - orthogonal immunological confirmation

---

## 6. Experiment-to-question mapping

### Q1. Which hexose donor is strongest under matched dry 4 h conditions?
Use:
- **R01–R04** at 55 C
- **R07–R10** at 60 C

### Q2. Which pentose is stronger, arabinose or ribose?
Use:
- **R05 vs R06**
- **R11 vs R12**
- **R15 vs R16**

### Q3. Does a pentose deserve advancement against the hexose field?
Use:
- best of **R05/R06/R11/R12/R15/R16/R19**
vs
- best of **R01–R04/R07–R10/R13/R14/R17/R18**

with interpretability filters.

### Q4. Is 55 C preferable to 60 C?
Use donor-matched 4 h ultrasound comparisons:
- R01 vs R07
- R02 vs R08
- R03 vs R09
- R04 vs R10
- R05 vs R11
- R06 vs R12

### Q5. Does 4 h earn its place over 3 h?
Use:
- R13 vs R01
- R14 vs R02
- R15 vs R05
- R16 vs R06

### Q6. Is ultrasound necessary, enabling, or marginal?
Use:
- R17 vs R01
- R18 vs R02
- R19 vs R06
with no-sugar anchor:
- **R23 vs R20**

### Q7. Are sugar effects materially stronger than heating/drying alone?
Use donor runs relative to backbone controls:
- 55 C, 4 h, +US donor runs vs **R20**
- 60 C, 4 h, +US donor runs vs **R21**
- 55 C, 3 h, +US donor runs vs **R22**
- 55 C, 4 h, –US donor runs vs **R23**

---

## 7. Assay plan

### Universal screening for all runs
All runs receive **P1 or P2**, which includes:
- primary immunoassay readout for reduction
- extractable protein recovery
- appearance / reconstitution notes
- browning score

### Automatic sample-state package
Runs automatically assigned **P2**:
- all pentose runs:
  - R05, R06, R11, R12, R15, R16, R19
- all no-sugar controls:
  - R20, R21, R22, R23
- all no-ultrasound donor runs:
  - R17, R18, R19

### Triggered P2 on hexose runs
Any hexose run initially assigned P1 should be upgraded to P2 if:
- primary reduction is **>=70%**, or
- it is within **<10 percentage points** of the leading hexose in the relevant comparison set

### Orthogonal confirmation package P3
After initial P1/P2 review, apply P3 to:
1. **best hexose branch**
2. **best pentose branch**
3. any additional branch that is:
   - within **<10 percentage points** of a decision-leading branch, or
   - **>=80% reduction** with recovery in the caution zone or suspicious aggregation behavior

### Minimum interpretation safeguards
A lead branch is not promotable on primary assay alone.  
Promotion requires:
- acceptable recovery,
- no dominant aggregation artifact,
- and orthogonal confirmation where specified.

---

## 8. Go / No-Go criteria

### Efficacy bands
- **Band A:** >=80% reduction
- **Band B:** 70–79% reduction
- **Below Band B:** <70%

### Practical preference rules
- prefer **3 h over 4 h** if 4 h adds **<10 percentage points**
- prefer **55 C over 60 C** if 60 C adds **<10 percentage points**
- prefer **no ultrasound** if +US does not materially improve practical ranking
- do not prefer harsher conditions without clear gain

### Recovery gate
Relative to matched heated no-sugar backbone control:
- **>=70% recovery** = promotion-eligible
- **50–69%** = caution
- **<50%** = no-go

### Sample-state gate
No-go for promotion if:
- reducing SDS-PAGE indicates dominant insolubilization / aggregation artifact,
- or recovery is <50%,
- or orthogonal confirmation fails when required

### Pentose-specific Go / No-Go
#### Pentose Go
Advance a pentose only if it:
- passes all interpretability gates,
- and is either:
  - clearly better than the best hexose under matched practical conditions,
  - or similarly strong at an earlier or milder condition

#### Pentose No-Go
Do not advance a pentose if:
- its apparent strength depends mainly on **60 C, 4 h**,
- or it loses competitiveness at **55 C, 3 h**,
- or it shows stronger browning together with poor recovery / aggregation without practical advantage,
- or orthogonal confirmation does not support the reduction.

### Interpretability rule
A condition with strong apparent reduction but poor recovery, dominant aggregation, or failed orthogonal confirmation should be treated as likely artifact- or masking-dominant and should **not** be promoted.

---

## 9. Advancement logic

### Step 1 — rank by efficacy band
Classify each donor branch into:
- Band A
- Band B
- below Band B

### Step 2 — apply time and temperature trade-off rules
Within matched donor branches:
- prefer **3 h** over **4 h** if the 4 h gain is <10 points
- prefer **55 C** over **60 C** if the 60 C gain is <10 points

### Step 3 — classify ultrasound
For lactose, glucose, ribose:
- **necessary** if removing ultrasound drops the branch below Band B or forces harsher conditions
- **enabling** if removing ultrasound materially worsens performance but does not collapse the branch
- **marginal** if no-ultrasound remains practically competitive

### Step 4 — apply interpretability gate
Disqualify from promotion if:
- recovery <50% of matched no-sugar control,
- dominant aggregation/insolubilization is present,
- or orthogonal confirmation fails when required

### Step 5 — donor-class advancement rule
#### Hexose
Advance if:
- Band A, or Band B with a clear burden advantage,
- and interpretability gates are passed

#### Pentose
Advance only if:
- interpretability gates are passed,
- and pentose is either:
  - clearly superior to the best hexose,
  - or comparably strong at earlier / milder conditions

### Step 6 — decide advancement scope
- **Advance one donor** if it is clearly superior and clean
- **Advance two donors** if top two are within **<10 points** or differ on numerical strength vs practical cleanliness
- **Advance no pentose** if pentose performance depends on harsher chemistry or poor interpretability

---

## 10. Final recommendation to wet lab

Execute the **23-condition matrix R01–R23 exactly as specified** under a fixed dry-state backbone:

- **dry mode**
- **aw 0.79**
- **1:2 protein:sugar**
- **55–60 C**
- **3–4 h**
- **ultrasound-centered using current lab-default settings**

Protect the following as non-negotiable:
1. the full 6-donor **4 h matched bridge**,
2. the **55 C, 3 h** subset for lactose, glucose, arabinose, ribose,
3. the no-ultrasound sentinels for lactose, glucose, ribose,
4. the four backbone-matched no-sugar controls,
5. recovery measurement on all runs,
6. automatic sample-state assessment for all pentose/control/no-ultrasound runs,
7. orthogonal confirmation for the best hexose and best pentose before final advancement.

This plan should be treated as the **preferred and complete next-round wet-lab execution package**.

It gives us the smallest round that can still decisively answer:
- whether lactose/glucose remain the best practical mainline donors,
- whether galactose or mannose overtake them under matched 4 h dry conditions,
- whether arabinose or ribose deserves advancement,
- whether 55 C is sufficient,
- whether 4 h is worth carrying forward,
- and whether ultrasound is necessary or merely enabling.

---

### Next Steps

1. **Generate the wet-lab run sheet** directly from runs **R01–R23**
   - include exact sample labels
   - assign biological replicate IDs
   - link each run to assay package P1/P2 and possible P3 trigger status

2. **Lock SOP references**
   - ultrasound settings = current lab default
   - dry aw handling = current aw 0.79 SOP
   - extraction/reconstitution = one fixed SOP across all runs
   - primary immunoassay platform = same as prior `reduction_pct_reported` workflow

3. **Pre-register the primary comparisons**
   - hexose donor ranking at 55 C and 60 C
   - arabinose vs ribose at 55 C and 60 C
   - 3 h vs 4 h for lactose, glucose, arabinose, ribose
   - +US vs –US for lactose, glucose, ribose

4. **Pre-register advancement thresholds**
   - Band A / Band B definitions
   - <10-point marginal-gain rule
   - recovery gate
   - pentose-specific advancement rule

5. **Prepare post-round analysis template now**
   - rank branches by efficacy
   - apply practical preference rules
   - apply recovery/state filters
   - assign ultrasound classification
   - determine whether to advance one donor, two donors, or no pentose

6. **Round-3 planning trigger**
   - if one donor clearly wins and is clean: move to focused time refinement
   - if two donors remain close: carry both forward
   - if a pentose is strong but interpretation-poor: do not advance to mainline optimization; consider separate side investigation
   - if 4 h does not earn its place: collapse next round to a **3 h-centered refinement program**
### Agenda

We are at the **execution-planning stage** for the β-LG variant A glycation project. The task is to convert the previously agreed project specification into **one directly executable wet-lab round** that can be handed to the lab for run-sheet generation.

The round must:

- center on a **dry-state donor bridge**,
- include the required primary donors:
  - **lactose**
  - **glucose**
  - **galactose**
  - **mannose**
- remain within the main practical window:
  - **55–60 C**
  - **2–4 h**
  - **ultrasound-centered**
- treat **time as a trade-off variable**, not as something to maximize by default,
- include the **minimum controls and validation runs** needed for interpretation,
- and explicitly include a **pentose branch** that tests both **arabinose** and **ribose** to determine whether a pentose should be advanced, and under what conditions.

The required output is a **complete wet-lab plan**, not abstract strategy.

---

### Team Member Input

#### Principal Investigator

I framed the meeting around converting prior strategy into a **single execution-ready round**. I emphasized that the round must protect the **matched dry-state donor bridge**, must not drift into broad side expansions, and must include a real **pentose decision branch** rather than leaving arabinose vs ribose unresolved.

My initial bias was toward:

- a **4 h full donor bridge** at **55 C and 60 C** under dry conditions with ultrasound,
- selected **no-ultrasound controls**,
- and a **minimal earlier-time subset** so the plan itself can test whether **4 h earns its place**.

After round 1, I provisionally locked the following:

- **mode:** dry
- **moisture condition:** **aw 0.79**
- **ratio:** **1:2 protein:sugar (w/w)**
- **temperatures:** **55 C and 60 C only**
- **times:** **4 h main + 3 h subset**
- **pretreatment:** lab-default ultrasound, unchanged
- **donors:** lactose, glucose, galactose, mannose, arabinose, ribose
- **no pH expansion**
- **no wet-mode expansion**
- **no broad donor-ratio sweep**
- **no additional pretreatment families**
- **n = 3 biological replicates per condition**

I also provisionally accepted the **23-condition base matrix** as the smallest coherent one-round plan that still answers all required questions.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry scientist strongly supported a **single common ratio** across all donors, including pentoses:

- **protein:sugar = 1:2 (w/w)**

The key point was that this round is a **matched decision experiment**, not donor-specific optimization. Lowering pentose loading now would reduce interpretability.

Other major chemistry recommendations:

- keep **aw 0.79** fixed for all runs,
- carry forward **existing lab-default ultrasound settings** unchanged,
- if only one earlier timepoint is included, choose **3 h**, not 2 h,
- and do not let pentose numerical strength alone drive advancement.

The chemistry scientist stressed that pentoses, especially **ribose**, can appear strong because they are **overreactive**, not because they are the most practical donors. Therefore pentoses should face a stricter interpretation standard.

In round 2, the chemistry scientist added that the final run sheet should specify donor loading in both:
- **relative form**: 1:2 (w/w)
- and an **absolute example** for handling clarity, such as:
  - **100 mg β-LG + 200 mg donor**

They also recommended adding one low-burden chemistry-facing observation to all runs:

- **visual browning score** on a fixed 0–3 scale

They did **not** support adding **60 C, 3 h ribose** in this round.

A chemistry-specific advancement caution was proposed:

> A donor should not be favored if improved primary reduction mainly coincides with stronger browning, poorer recovery, and more aggregation without an earlier-time or lower-temperature advantage.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology scientist agreed with the fixed dry-state bridge and the 3 h checkpoint, but emphasized that raw reduction values cannot be treated as equivalent to true biologically meaningful allergenicity reduction.

Key interpretation principles raised:

- lower signal can reflect:
  - true epitope disruption,
  - but also masking,
  - reduced extractability,
  - aggregation,
  - altered assay geometry,
  - or coating artifacts.
- therefore the round must answer both:
  1. which conditions reduce the primary immunoassay signal,
  2. which reductions are **interpretable and biologically credible**.

The immunology scientist strongly supported including **both arabinose and ribose** experimentally.

They required backbone-matched **heated no-sugar controls** for interpretation, specifically:
- **55 C, 4 h, ultrasound**
- **60 C, 4 h, ultrasound**
- **55 C, 3 h, ultrasound**
- **55 C, 4 h, no ultrasound**

They proposed a **tiered assay package**:

For **all runs**:
- primary immunoassay
- extractable protein / recovery
- appearance / reconstitution notes

For expanded protection:
- reducing SDS-PAGE for:
  - all pentose runs
  - all no-sugar controls
  - all no-ultrasound donor runs
  - and above-threshold hexose runs

For confirmation:
- orthogonal immunological confirmation for:
  - best hexose
  - best pentose
  - and additional suspicious or near-leading branches if needed

In round 2, they made the recovery rule operational:

- **>=70% of matched heated no-sugar control**: promotion-eligible
- **50–69%**: caution zone
- **<50%**: no-go

They also recommended:
- automatic SDS-PAGE on all pentose runs, all controls, and all no-ultrasound donor runs,
- SDS-PAGE on any hexose run with **>=70% reduction** or within **<10 points** of the leading hexose,
- orthogonal confirmation on:
  - best hexose
  - best pentose
  - and any **>=80%** or close-call suspicious branch

A key interpretability rule they proposed was:

> A condition with strong apparent reduction but poor recovery, dominant aggregation, or failed orthogonal confirmation should be treated as a likely artifact or masking-dominant effect and should not be promoted.

---

#### Experimental Design and Evidence Synthesis Scientist

The design scientist translated the strategy into the smallest one-round structure that still answers all required questions.

They defined five mandatory decision questions for the round:

1. hexose donor ranking under matched dry 4 h conditions,
2. pentose advancement question,
3. 55 C vs 60 C trade-off,
4. 3 h vs 4 h trade-off,
5. ultrasound necessity/enabling/marginality.

They proposed a **23-condition matrix** composed of four run roles:

##### Run role A — primary donor bridge
All 6 donors at:
- **55 C, 4 h, ultrasound**
- **60 C, 4 h, ultrasound**

= **12 runs**

##### Run role B — time-tradeoff subset
At **55 C, 3 h, ultrasound**:
- lactose
- glucose
- arabinose
- ribose

= **4 runs**

##### Run role C — no-ultrasound sentinels
At **55 C, 4 h, no ultrasound**:
- lactose
- glucose
- ribose

= **3 runs**

##### Run role D — shared no-sugar controls
- 55 C, 4 h, ultrasound
- 60 C, 4 h, ultrasound
- 55 C, 3 h, ultrasound
- 55 C, 4 h, no ultrasound

= **4 runs**

Total = **23 conditions**

They also formalized assay assignment:

- **S1 / universal screening package** for all runs
- **S2 / sample-state package** for all pentose, control, no-ultrasound, and triggered hexose runs
- **S3 / orthogonal confirmation** for best hexose, best pentose, and ambiguous lead branches

In round 2, they recommended keeping the no-ultrasound sentinel set as:

- lactose
- glucose
- ribose

and proposed a clean advancement hierarchy:

1. efficacy band,
2. practical preference,
3. interpretability gate,
4. donor-class rule,
5. scope of advancement.

---

#### Scientific Critic

The critic mainly pressured the plan on two fronts:

1. avoid **overdesign**,
2. avoid **underprotection**.

In round 1, the critic argued that testing both temperatures for all pentoses could be excessive and suggested that **60 C pentose runs** would be the first place to cut if capacity were limited. I did **not** adopt that suggestion because the agenda explicitly requires that pentose advancement and condition dependence be answered in this round.

The critic also emphasized that pentose interpretation guardrails must be strong enough to prevent false promotion through aggregation or extraction artifacts.

In round 2, the critic accepted the **23-condition layout** and agreed that the smallest acceptable pentose branch includes:
- arabinose and ribose at **55 C and 60 C, 4 h**
- **55 C, 3 h**
- and **ribose no-ultrasound**

The critic’s strongest useful final contributions were:
- simplify operational logic where possible,
- use clear run-role labeling,
- and keep advancement rules concise enough for wet-lab teams to apply.

They suggested simplifying assay logic into fewer tiers. I have partially incorporated that by retaining the functional distinction among:
- universal screening,
- automatic sample-state assessment,
- targeted orthogonal confirmation,
while keeping the final wording operational and not overly elaborate.

---

### Recommendation

My final recommendation is to execute a **23-condition dry-state matched donor bridge round** with embedded time- and ultrasound-interpretation protection, using a common **1:2 protein:sugar ratio**, fixed **aw 0.79**, and the lab’s current ultrasound settings.

This is the **preferred execution-ready plan** because it is the smallest single round that still answers all of the project’s mandatory questions:

- hexose donor ranking,
- pentose donor decision,
- 55 C vs 60 C trade-off,
- 3 h vs 4 h trade-off,
- and ultrasound classification,

while also satisfying the requirement to include minimum validation needed for interpretation.

I am choosing this plan over smaller alternatives because:

1. a **4 h-only** screen would fail to test whether 4 h is actually worth carrying forward;
2. omitting either **arabinose or ribose** would fail the explicit pentose requirement;
3. dropping **60 C pentose runs** would leave the “if so, under what conditions?” part of the pentose question only partially answered;
4. skipping **no-sugar controls** or sample-state checks would create a serious risk of artifact-driven promotion;
5. broadening beyond this matrix into wet mode, pH, ratio sweeps, or other pretreatments would reduce decision efficiency.

Below is the final plan in the required execution format.

---

## 1. Round objective

Run a **dry-state, ultrasound-centered donor bridge** to identify the most practical glycation condition region for reducing β-LG variant A allergenicity, while explicitly testing:

- matched ranking of **lactose, glucose, galactose, mannose**,
- whether **arabinose or ribose** deserves advancement,
- whether **55 C** can substitute for or outperform **60 C** practically,
- whether **4 h** is meaningfully better than **3 h**,
- and whether ultrasound is **necessary, enabling, or marginal** for key branches.

The round is designed to optimize the **efficient frontier**, not the maximum reduction alone.

---

## 2. Fixed variables

These variables are fixed across the round unless explicitly noted in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)**
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **temperature window:** 55 C or 60 C only
- **time window in this round:** 3 h or 4 h only
- **pretreatment main arm:** ultrasound, using **current lab-default settings unchanged**
- **no-ultrasound condition:** identical processing except ultrasound omitted
- **replication:** **n = 3 biological replicates per condition**
- **reconstitution/extraction SOP:** one standardized lab SOP across all runs
- **primary assay platform:** same assay family used for current `reduction_pct_reported`
- **browning note:** fixed 0–3 visual score for all runs
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

---

## 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 3 h
  - 4 h
- **ultrasound status**
  - yes
  - no

---

## 4. Final experiment matrix

### Assay package definitions
- **P1 = universal screening**
  - primary immunoassay
  - extractable protein recovery
  - appearance/reconstitution notes
  - browning score
- **P2 = sample-state package**
  - all of P1
  - reducing SDS-PAGE
  - soluble/insoluble fraction note if routine
- **P3 = orthogonal confirmation package**
  - orthogonal immunoassay
  - repeat extraction consistency check
  - applied only to advancement-candidate runs after P1/P2 review

> All runs receive P1 or P2 as assigned below.  
> P3 is a planned validation step applied to the top branches defined in the assay plan.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | primary_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R02 | primary_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R03 | primary_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R04 | primary_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R05 | primary_bridge_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R06 | primary_bridge_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R07 | primary_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R08 | primary_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R09 | primary_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R10 | primary_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R11 | primary_bridge_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R12 | primary_bridge_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R13 | time_subset | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R14 | time_subset | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P1 |
| R15 | time_subset_pentose | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R16 | time_subset_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | no | no | 3 | P2 |
| R17 | no_ultrasound_sentinel | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R18 | no_ultrasound_sentinel | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R19 | no_ultrasound_sentinel_pentose | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 3 | P2 |
| R20 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R21 | backbone_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R22 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | ultrasound, lab-default settings | yes | no | 3 | P2 |
| R23 | backbone_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | yes | yes | 3 | P2 |

### Validation runs planned within this round
No additional condition branches are added beyond R01–R23.  
Minimum validation is built into the round via:
- backbone controls,
- P2 sample-state package,
- and planned **P3 orthogonal confirmation** for top candidates after primary-screen review.

---

## 5. Pentose branch design

### Pentose runs included
- **R05** arabinose, 55 C, 4 h, +US
- **R06** ribose, 55 C, 4 h, +US
- **R11** arabinose, 60 C, 4 h, +US
- **R12** ribose, 60 C, 4 h, +US
- **R15** arabinose, 55 C, 3 h, +US
- **R16** ribose, 55 C, 3 h, +US
- **R19** ribose, 55 C, 4 h, –US

### Pentose decision question
The pentose branch is designed to answer:

> Does either arabinose or ribose produce a practically credible allergenicity-reduction signal strong enough to justify advancement relative to the best hexose branch, and if so, is that signal achievable under acceptable severity and interpretability conditions?

Sub-questions:
1. **arabinose vs ribose** at matched 4 h conditions
2. whether pentose performance depends on **55 C vs 60 C**
3. whether pentose performance depends on extending from **3 h to 4 h**
4. whether **ribose** depends materially on ultrasound
5. whether any pentose advantage survives:
   - recovery filtering
   - aggregation/state assessment
   - orthogonal immunological confirmation

---

## 6. Experiment-to-question mapping

### Q1. Which hexose donor is strongest under matched dry 4 h conditions?
Use:
- **R01–R04** at 55 C
- **R07–R10** at 60 C

### Q2. Which pentose is stronger, arabinose or ribose?
Use:
- **R05 vs R06**
- **R11 vs R12**
- **R15 vs R16**

### Q3. Does a pentose deserve advancement against the hexose field?
Use:
- best of **R05/R06/R11/R12/R15/R16/R19**
vs
- best of **R01–R04/R07–R10/R13/R14/R17/R18**

with interpretability filters.

### Q4. Is 55 C preferable to 60 C?
Use donor-matched 4 h ultrasound comparisons:
- R01 vs R07
- R02 vs R08
- R03 vs R09
- R04 vs R10
- R05 vs R11
- R06 vs R12

### Q5. Does 4 h earn its place over 3 h?
Use:
- R13 vs R01
- R14 vs R02
- R15 vs R05
- R16 vs R06

### Q6. Is ultrasound necessary, enabling, or marginal?
Use:
- R17 vs R01
- R18 vs R02
- R19 vs R06
with no-sugar anchor:
- **R23 vs R20**

### Q7. Are sugar effects materially stronger than heating/drying alone?
Use donor runs relative to backbone controls:
- 55 C, 4 h, +US donor runs vs **R20**
- 60 C, 4 h, +US donor runs vs **R21**
- 55 C, 3 h, +US donor runs vs **R22**
- 55 C, 4 h, –US donor runs vs **R23**

---

## 7. Assay plan

### Universal screening for all runs
All runs receive **P1 or P2**, which includes:
- primary immunoassay readout for reduction
- extractable protein recovery
- appearance / reconstitution notes
- browning score

### Automatic sample-state package
Runs automatically assigned **P2**:
- all pentose runs:
  - R05, R06, R11, R12, R15, R16, R19
- all no-sugar controls:
  - R20, R21, R22, R23
- all no-ultrasound donor runs:
  - R17, R18, R19

### Triggered P2 on hexose runs
Any hexose run initially assigned P1 should be upgraded to P2 if:
- primary reduction is **>=70%**, or
- it is within **<10 percentage points** of the leading hexose in the relevant comparison set

### Orthogonal confirmation package P3
After initial P1/P2 review, apply P3 to:
1. **best hexose branch**
2. **best pentose branch**
3. any additional branch that is:
   - within **<10 percentage points** of a decision-leading branch, or
   - **>=80% reduction** with recovery in the caution zone or suspicious aggregation behavior

### Minimum interpretation safeguards
A lead branch is not promotable on primary assay alone.  
Promotion requires:
- acceptable recovery,
- no dominant aggregation artifact,
- and orthogonal confirmation where specified.

---

## 8. Go / No-Go criteria

### Efficacy bands
- **Band A:** >=80% reduction
- **Band B:** 70–79% reduction
- **Below Band B:** <70%

### Practical preference rules
- prefer **3 h over 4 h** if 4 h adds **<10 percentage points**
- prefer **55 C over 60 C** if 60 C adds **<10 percentage points**
- prefer **no ultrasound** if +US does not materially improve practical ranking
- do not prefer harsher conditions without clear gain

### Recovery gate
Relative to matched heated no-sugar backbone control:
- **>=70% recovery** = promotion-eligible
- **50–69%** = caution
- **<50%** = no-go

### Sample-state gate
No-go for promotion if:
- reducing SDS-PAGE indicates dominant insolubilization / aggregation artifact,
- or recovery is <50%,
- or orthogonal confirmation fails when required

### Pentose-specific Go / No-Go
#### Pentose Go
Advance a pentose only if it:
- passes all interpretability gates,
- and is either:
  - clearly better than the best hexose under matched practical conditions,
  - or similarly strong at an earlier or milder condition

#### Pentose No-Go
Do not advance a pentose if:
- its apparent strength depends mainly on **60 C, 4 h**,
- or it loses competitiveness at **55 C, 3 h**,
- or it shows stronger browning together with poor recovery / aggregation without practical advantage,
- or orthogonal confirmation does not support the reduction.

### Interpretability rule
A condition with strong apparent reduction but poor recovery, dominant aggregation, or failed orthogonal confirmation should be treated as likely artifact- or masking-dominant and should **not** be promoted.

---

## 9. Advancement logic

### Step 1 — rank by efficacy band
Classify each donor branch into:
- Band A
- Band B
- below Band B

### Step 2 — apply time and temperature trade-off rules
Within matched donor branches:
- prefer **3 h** over **4 h** if the 4 h gain is <10 points
- prefer **55 C** over **60 C** if the 60 C gain is <10 points

### Step 3 — classify ultrasound
For lactose, glucose, ribose:
- **necessary** if removing ultrasound drops the branch below Band B or forces harsher conditions
- **enabling** if removing ultrasound materially worsens performance but does not collapse the branch
- **marginal** if no-ultrasound remains practically competitive

### Step 4 — apply interpretability gate
Disqualify from promotion if:
- recovery <50% of matched no-sugar control,
- dominant aggregation/insolubilization is present,
- or orthogonal confirmation fails when required

### Step 5 — donor-class advancement rule
#### Hexose
Advance if:
- Band A, or Band B with a clear burden advantage,
- and interpretability gates are passed

#### Pentose
Advance only if:
- interpretability gates are passed,
- and pentose is either:
  - clearly superior to the best hexose,
  - or comparably strong at earlier / milder conditions

### Step 6 — decide advancement scope
- **Advance one donor** if it is clearly superior and clean
- **Advance two donors** if top two are within **<10 points** or differ on numerical strength vs practical cleanliness
- **Advance no pentose** if pentose performance depends on harsher chemistry or poor interpretability

---

## 10. Final recommendation to wet lab

Execute the **23-condition matrix R01–R23 exactly as specified** under a fixed dry-state backbone:

- **dry mode**
- **aw 0.79**
- **1:2 protein:sugar**
- **55–60 C**
- **3–4 h**
- **ultrasound-centered using current lab-default settings**

Protect the following as non-negotiable:
1. the full 6-donor **4 h matched bridge**,
2. the **55 C, 3 h** subset for lactose, glucose, arabinose, ribose,
3. the no-ultrasound sentinels for lactose, glucose, ribose,
4. the four backbone-matched no-sugar controls,
5. recovery measurement on all runs,
6. automatic sample-state assessment for all pentose/control/no-ultrasound runs,
7. orthogonal confirmation for the best hexose and best pentose before final advancement.

This plan should be treated as the **preferred and complete next-round wet-lab execution package**.

It gives us the smallest round that can still decisively answer:
- whether lactose/glucose remain the best practical mainline donors,
- whether galactose or mannose overtake them under matched 4 h dry conditions,
- whether arabinose or ribose deserves advancement,
- whether 55 C is sufficient,
- whether 4 h is worth carrying forward,
- and whether ultrasound is necessary or merely enabling.

---

### Next Steps

1. **Generate the wet-lab run sheet** directly from runs **R01–R23**
   - include exact sample labels
   - assign biological replicate IDs
   - link each run to assay package P1/P2 and possible P3 trigger status

2. **Lock SOP references**
   - ultrasound settings = current lab default
   - dry aw handling = current aw 0.79 SOP
   - extraction/reconstitution = one fixed SOP across all runs
   - primary immunoassay platform = same as prior `reduction_pct_reported` workflow

3. **Pre-register the primary comparisons**
   - hexose donor ranking at 55 C and 60 C
   - arabinose vs ribose at 55 C and 60 C
   - 3 h vs 4 h for lactose, glucose, arabinose, ribose
   - +US vs –US for lactose, glucose, ribose

4. **Pre-register advancement thresholds**
   - Band A / Band B definitions
   - <10-point marginal-gain rule
   - recovery gate
   - pentose-specific advancement rule

5. **Prepare post-round analysis template now**
   - rank branches by efficacy
   - apply practical preference rules
   - apply recovery/state filters
   - assign ultrasound classification
   - determine whether to advance one donor, two donors, or no pentose

6. **Round-3 planning trigger**
   - if one donor clearly wins and is clean: move to focused time refinement
   - if two donors remain close: carry both forward
   - if a pentose is strong but interpretation-poor: do not advance to mainline optimization; consider separate side investigation
   - if 4 h does not earn its place: collapse next round to a **3 h-centered refinement program**

[end summary 1]

[begin summary 2]

### Agenda

We moved from project specification to **execution planning** for the next wet-lab round on **β-lactoglobulin A allergenicity reduction by glycation**. The goal was to produce **one directly executable wet-lab plan** that:

- keeps the main search in a **dry-state**, **aw-controlled**, **55–60 C**, **2–4 h**, **ultrasound-centered** window,
- includes a **matched hexose donor bridge** across:
  - lactose
  - glucose
  - galactose
  - mannose
- treats **reaction time as a trade-off variable**, not something to maximize automatically,
- includes the **minimum controls and validation runs** needed for interpretation,
- and explicitly includes a **pentose decision branch** using **both arabinose and ribose** so the project can decide whether any pentose donor should advance.

The deliverable had to be a **complete wet-lab plan**, not a strategy note, and had to specify the fields needed for run-sheet generation.

---

### Team Member Input

#### Principal Investigator

I framed the meeting around the need to stop discussing abstractly and instead produce a **single execution-ready next-round matrix**. I emphasized four required outputs for this round:

1. bridge the current local validated leaders (**lactose**, **glucose**) into the **55–60 C, 2–4 h dry-state window**,
2. test the key unvalidated hexose challengers (**galactose**, **mannose**),
3. experimentally resolve the pentose uncertainty (**arabinose vs ribose**),
4. and embed enough interpretation protection to avoid mistaking assay suppression caused by insolubility or aggregation for true allergenicity reduction.

My initial bias was:
- **full 4 h hexose bridge** at 55 C and 60 C under ultrasound,
- **2 h benchmark anchors** for lactose and glucose,
- a **small pentose decision branch** rather than full pentose optimization,
- and predefined validation rules for top hits.

After round 1, I synthesized the team’s convergence and made several provisional decisions:
- lock **dry state**, **aw 0.79**, **1:2 w/w**, and a common extraction workflow;
- lock the **8-run 4-donor hexose ultrasound bridge** at 55/60 C, 4 h;
- lock the **4-run hexose no-ultrasound comparison** at 55 C, 4 h;
- lock the **pentose core branch** at **55 C, 2 h and 3 h** for **arabinose** and **ribose**;
- include **55 C, 3 h lactose/glucose anchors** in addition to the **60 C, 2 h lactose/glucose benchmark anchors**;
- include **four heated no-sugar controls** at 55 C (2 h, 3 h, 4 h) and 60 C (4 h);
- and require **orthogonal immunological confirmation** before any branch is promoted beyond this round.

By round 2, my direction converged to a **24-run protected matrix** with an optional **26-run expansion** that adds two pentose no-ultrasound runs only if capacity is comfortable.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry/process input strongly supported **tight control of the dry-state backbone** and stressed that **moisture must not vary** in this round. The key chemistry recommendations were:

- lock the dry-state condition at **aw 0.79** using the same equilibration and sealed-handling workflow as the validated prior dry runs;
- use one common donor ratio across all donors:
  - **β-LG : donor = 1:2 (w/w)**;
- keep the **hexose bridge** as:
  - lactose / glucose / galactose / mannose
  - at **55 C and 60 C**
  - for **4 h**
  - with **ultrasound** as the main arm;
- but treat the **pentose branch more cautiously** than the hexose branch.

The chemistry lead explicitly disagreed with a symmetric pentose design and argued that pentoses should **not** be screened first at 4 h, because pentoses are more likely to enter chemically dirtier territory quickly. Instead, the recommendation was:

- test **both arabinose and ribose**,
- at **55 C only**,
- at **2 h and 3 h**,
- with ultrasound as the primary arm,
- and do not use **60 C** or **4 h** as the primary pentose decision window.

The chemistry rationale was that the proper pentose question is not “can a pentose generate the biggest numerical drop,” but rather:

> can either pentose generate a strong and interpretable reduction under a restrained practical window?

In round 2, the chemistry lead locked the ultrasound field operationally as:

- **probe sonication**
- **20 kHz**
- **30% amplitude**
- **5 s on / 5 s off**
- **10 min total sonication**
- maintain sample temperature **<=25 C**
- same ultrasound conditions for all donors

The chemistry lead also recommended additional execution wording for:
- **aw 0.79** dry-state equilibration and sealed reaction handling,
- temperature tolerance of **±0.5 C**,
- and immediate cooling / standardized extraction timing after reaction completion.

For promoted pentose hits, the minimal chemistry-risk validation package recommended was:
- **browning index** (e.g. A420),
- **fluorescent AGE trend screen** (e.g. Ex 370 / Em 440),
- preferably also **OPA/free amino group trend**.

The chemistry lead supported the **24-run protected matrix** and stated that the **2 pentose no-ultrasound runs should be cut first** if any reduction in scope is needed.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology input centered on the need to distinguish **true reduction in allergenic recognition** from:
- masking,
- aggregation,
- insolubility,
- extraction loss,
- or assay-format artifact.

A major point was that pentoses are the branch **most likely to look good for the wrong reasons**, so they require a stricter interpretation bar.

The immunology lead recommended that **every screening run** receive a minimum assay package containing:

1. the same **primary allergenicity assay** used to generate the historical `reduction_pct_reported`,
2. **extractable/recoverable β-LG** or soluble protein readout under the standardized extraction workflow,
3. **basic aggregation / size-state assessment**,
4. a **browning / overprocessing proxy**.

For promoted hits, the validation package should add:
- **orthogonal immunological confirmation**,
- stronger aggregation assessment,
- extractability normalization review,
- and for pentose-promoted branches, extra chemistry-risk readouts.

The immunology lead agreed with the chemistry recommendation that the pentose branch should be:
- **55 C only**
- **2 h and 3 h**
- **arabinose and ribose**
- ultrasound-centered

but also argued that pentoses should **not be interpreted in isolation**, which is why the **55 C, 3 h lactose/glucose anchors** were defended strongly.

By round 2, the immunology lead converted the interpretation criteria into operational thresholds:

- **acceptable extractability for screening:**  
  **>=60%** of untreated β-LG baseline
- **borderline:**  
  **50–59%**
- **unacceptable:**  
  **<50%**
- **preferred extractability for promoted pentose branches:**  
  **>=70%**

Aggregation-dominant artifact was operationalized as a run meeting **2 or more** of:
- marked monomer loss in soluble fraction,
- prominent high-MW smear / aggregated material,
- extractability <60%,
- orthogonal inconsistency if tested,
- signal loss mainly explained by disappearance from the soluble fraction.

Orthogonal confirmation was considered directionally consistent if:
- the orthogonal assay also showed reduced recognition,
- in the same practical direction,
- without collapsing the hit or reversing the practical conclusion.

The immunology lead supported automatic validation of:
- the **top 2 hexose branches**
- plus the **top pentose branch if it qualifies**

and explicitly preferred protecting the **55 C, 3 h lactose/glucose anchors** over the optional pentose no-ultrasound pair.

---

#### Experimental Design and Evidence Synthesis Scientist

The design input focused on finding the **smallest matrix that resolves the critical uncertainties** without producing uninterpretable apparent winners.

The six decision questions identified were:

1. matched **hexose donor ranking** outside the current local domain,
2. **55 C vs 60 C** at 4 h,
3. whether ultrasound is **broadly enabling or only locally helpful**,
4. whether **4 h earns its place** for benchmark donors relative to earlier anchors,
5. whether **either pentose deserves advancement at all**,
6. whether a pentose is competitive under a **restrained practical window**.

The design lead concluded that the cleanest default plan is a **24-run protected matrix** composed of five blocks:

- **Block 1: 8-run core hexose donor bridge**
- **Block 2: 4-run hexose no-ultrasound bridge**
- **Block 3: 4-run benchmark and practical anchors**
- **Block 4: 4-run pentose decision branch**
- **Block 5: 4-run heated no-sugar controls**

The design lead also proposed an **expanded 26-run version** that adds:
- arabinose, 55 C, 2 h, no ultrasound
- ribose, 55 C, 2 h, no ultrasound

but agreed by round 2 that these are optional only.

Replication logic was finalized as:
- **n = 2 independent process replicates for every matrix run**
- **technical duplicate** for the primary assay
- **n = 3 independent process replicates** for promoted validation reruns

The design lead also formalized the advancement criteria:

**Screen hit**
- primary allergenicity reduction **>=70%**
- at least **15 percentage points above matched heated no-sugar control**
- extractability **>=60%**
- no aggregation-dominant artifact flag

**Strong provisional candidate**
- a screen hit that is either:
  - **>=80% reduction**, or
  - **70–79%** with meaningful burden advantage (shorter time, lower temperature, or lower ultrasound dependence)

**Hexose advancement**
- validate the **top 2 hexose branches**
- reduce to one donor only if the best branch is **>=10 points** ahead of the next-best donor under matched conditions and is clean interpretively

**Pentose advancement**
- pentose best run must be a screen hit,
- be competitive with **55 C, 3 h lactose/glucose anchors**,
- not be clearly worse than the leading hexose in extractability / aggregation / browning,
- and pass orthogonal confirmation before promotion

**No-go**
- <70% reduction,
- <15-point gain above matched no-sugar control,
- extractability <50%,
- aggregation-dominant artifact,
- failed orthogonal confirmation for a promoted candidate,
- or pentose overprocessing burden that materially outweighs its numerical advantage

The design lead strongly endorsed the **24-run protected matrix** as the default final plan.

---

#### Scientific Critic

The critic’s role in round 1 was to warn against **overbuilding the matrix** and to press the team to ensure every run answered a distinct, important question.

The main criticisms were:
- the risk of a **too-large and too-complex matrix**,
- possible redundancy within the bridge design,
- the need for **very strict pentose advancement rules**,
- and the importance of making **orthogonal confirmation mandatory** rather than optional for promoted branches.

In round 2, after the matrix was simplified and better structured, the critic concluded that the **24-run protected matrix no longer represented hidden overreach**. The critic endorsed:

- the **24-run protected matrix** as appropriately scaled,
- the **26-run expansion** only if capacity allows,
- **n = 2** process replicates for matrix runs and **n = 3** for validation,
- and the run-block structure because each block now clearly maps to a specific decision question.

If two runs had to be cut, the critic agreed they should be:
- arabinose, 55 C, 2 h, no ultrasound
- ribose, 55 C, 2 h, no ultrasound

The critic also agreed that the **55 C, 3 h lactose/glucose anchors earn their place** and should be retained.

---

### Recommendation

My final recommendation is to proceed with a **24-run protected next-round wet-lab plan** built around a **dry-state, aw-controlled, ultrasound-centered donor bridge** with a restrained pentose decision branch and pre-specified interpretation and advancement rules.

This is the single preferred execution-ready plan.

I am choosing this option because it best satisfies all agenda requirements simultaneously:

- it preserves the **main hexose donor bridge** using:
  - lactose
  - glucose
  - galactose
  - mannose
- it remains inside the mandated **55–60 C**, **2–4 h**, **ultrasound-centered** window;
- it treats **time as a trade-off variable** by using:
  - 4 h as the **bridge screen** for the main hexose comparison,
  - 2 h benchmark anchors,
  - 3 h practical anchors,
  - and 2–3 h pentose testing rather than maximizing pentose time;
- it includes the **minimum necessary controls** for interpretation;
- it explicitly addresses **arabinose vs ribose experimentally**;
- it avoids broad expansion into wet mode, broad pH sweeps, donor-ratio sweeps, or other pretreatment families;
- and it includes the **minimum validation structure** needed to avoid promoting false positives.

The key design choice I am making is to **treat pentoses asymmetrically relative to hexoses**. This is justified because pentoses are not simply another donor class in the same practical-risk category. Testing arabinose and ribose under **55 C, 2–3 h** is the correct way to answer the project-relevant question:

> does any pentose deserve advancement under a restrained practical window?

rather than the less useful question:

> can a pentose force a larger numerical drop under harsher conditions?

I am also choosing to keep the **55 C, 3 h lactose/glucose anchors** in the protected matrix. These runs earn their place because they do double duty:
- they provide a fair comparator for pentose advancement,
- and they help determine whether the 4 h hexose bridge is actually worth carrying forward versus a milder shorter condition.

I am **not** including the pentose no-ultrasound pair in the preferred default plan. Those two runs remain the first optional add-on if capacity is comfortable, but they are not part of the protected recommendation.

---

## 1. Round objective

Execute a single next-round wet-lab matrix that:

1. ranks the four primary hexose donors under matched dry-state bridge conditions,
2. tests whether 55 C or 60 C is preferable at 4 h,
3. classifies the practical role of ultrasound within the hexose bridge,
4. determines whether 4 h earns its place relative to earlier benchmark/practical anchors,
5. determines whether either pentose donor (**arabinose** or **ribose**) should be advanced,
6. and does so with enough interpretation protection to distinguish meaningful allergenicity reduction from extraction / aggregation / overprocessing artifacts.

---

## 2. Fixed variables

These are fixed across the round unless explicitly noted otherwise.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **dry-state handling:** same validated pre-equilibration and sealed reaction workflow as prior dry runs
- **ultrasound settings for all ultrasound runs:**
  - probe sonication
  - 20 kHz
  - 30% amplitude
  - 5 s on / 5 s off
  - 10 min total sonication time
  - maintain sample temperature **<=25 C**
- **temperature tolerance during reaction:** **±0.5 C**
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction timeline
- **screening replicate count:** **2 independent process replicates**
- **primary assay technical replication:** technical duplicate
- **screening assay package:** Assay Package S
- **validation assay package:** Assay Package V

---

## 3. Scanned variables

The variables intentionally scanned in this round are:

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - plus no-sugar controls
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **pretreatment status**
  - ultrasound
  - selected no-ultrasound controls

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

## 4. Final experiment matrix

### Assay package definitions used in the matrix

- **Assay Package S**
  1. primary allergenicity assay matched to historical `reduction_pct_reported`
  2. extractable β-LG / soluble recovery readout
  3. non-reducing SDS-PAGE of soluble fraction
  4. browning / overprocessing proxy

- **Assay Package V**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable β-LG / soluble recovery
  4. higher-resolution aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branches: fluorescent AGE trend screen; preferably OPA/free amino group trend

### Primary 24-run protected matrix

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S |
| R02 | hexose_bridge | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R03 | hexose_bridge | galactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R04 | hexose_bridge | mannose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R05 | hexose_bridge | lactose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R06 | hexose_bridge | glucose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R07 | hexose_bridge | galactose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R08 | hexose_bridge | mannose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R09 | hexose_noUS | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R10 | hexose_noUS | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R11 | hexose_noUS | galactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R12 | hexose_noUS | mannose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R13 | benchmark_anchor | lactose | 1:2 w/w | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R14 | benchmark_anchor | glucose | 1:2 w/w | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R15 | practical_anchor | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R16 | practical_anchor | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R17 | pentose_branch | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R18 | pentose_branch | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R19 | pentose_branch | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R20 | pentose_branch | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R21 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S |
| R22 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S |
| R23 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S |
| R24 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S |

### Optional expansion only if capacity is comfortable

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R25 | pentose_noUS_optional | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | no ultrasound | no | yes | 2 | S |
| R26 | pentose_noUS_optional | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | no ultrasound | no | yes | 2 | S |

### Pre-specified validation reruns

These are not part of the fixed 24 screening runs but are part of the round plan and are triggered after screen review.

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

## 5. Pentose branch design

### Pentose branch runs
- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

### Pentose decision question
The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

### Why this design was chosen
- It does **not assume arabinose is better**
- It does **not assume ribose is better**
- It tests both under exactly matched conditions
- It avoids overcommitting to harsher pentose conditions that could bias the result toward chemically dirtier outcomes
- It compares pentoses against:
  - heated no-sugar controls,
  - and the **55 C, 3 h lactose/glucose practical anchors**

### Pentose advancement rule summary
A pentose can advance only if its best run:
- is a formal screen hit,
- is competitive with the 55 C, 3 h lactose/glucose anchors,
- is not clearly worse than the leading hexose in extractability / aggregation / browning burden,
- and passes orthogonal confirmation before promotion beyond this round.

---

## 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at the lower-severity temperature?

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter/milder benchmark-relevant conditions, and what are the practical comparator anchors for pentose interpretation?

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

---

## 7. Assay plan

### Screening assay package: Assay Package S
Apply to **R01–R24** (and R25–R26 if optional expansion is run):

1. **Primary allergenicity assay**
   - same platform used to generate historical `reduction_pct_reported`

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG batch control

3. **Basic aggregation / size-state assessment**
   - non-reducing SDS-PAGE on soluble fraction

4. **Browning / overprocessing proxy**
   - simple absorbance/color index

### Validation assay package: Assay Package V
Apply to **V01–V03**:

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

### Interpretation rules embedded in assay plan
A high apparent reduction will **not** be treated as meaningful allergenicity reduction if it is accompanied by:
- poor extractability,
- aggregation-dominant loss from the soluble fraction,
- or failure to reproduce directionally in orthogonal immunological confirmation.

---

## 8. Go / No-Go criteria

### Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

### Borderline
- extractability **50–59%** = borderline; do not promote without especially strong supporting evidence
- extractability **<50%** = fail for advancement

### Aggregation-dominant artifact flag
Flag if **2 or more** of the following are present:
- marked monomer loss in soluble fraction
- strong high-MW smear / aggregated material
- extractability <60%
- signal loss mainly explained by disappearance from soluble fraction
- orthogonal inconsistency when tested

### Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time,
  - lower temperature,
  - or lower ultrasound dependence

### Pentose-specific stricter bar
For a pentose to be promoted:
- preferred extractability should be **>=70%**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion beyond this round

### No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

## 9. Advancement logic

### Hexose advancement
Automatically send to validation:
- **top 2 hexose branches** from the screen that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond validation planning if:
- the best hexose branch is **>=10 percentage points** above the next-best matched hexose branch,
- the lead is stable,
- and there is no interpretability penalty

Otherwise keep two hexose donors active.

### Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit,
- the best pentose run is competitive with **R15/R16**,
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

### Time decision rule
Time is a trade-off variable. After the screen:
- do **not** automatically prefer 4 h over 3 h or 2 h
- prefer the earlier condition if the later condition does **not** give a clearly meaningful gain
- treat later time as justified only if it changes practical category or yields a substantial increase without interpretability penalty

### Ultrasound interpretation rule
For hexoses, classify ultrasound as:
- **necessary** if removing it drops the branch below practical competitiveness,
- **practically enabling** if removal materially worsens efficiency/severity,
- **marginally beneficial** if practical ranking is unchanged

---

## 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **Assay Package S on all screening runs**
- **Assay Package V on validation reruns**

Do **not** expand into:
- wet mode,
- pH sweep,
- donor-ratio sweep,
- additional aw points,
- or other pretreatment families in this round.

Do **not** add the pentose no-ultrasound pair unless capacity is comfortably available after the protected 24-run matrix is secured.

Most importantly, do **not** rank winners by apparent reduction alone. Promotion beyond this round requires that the leading branches remain:
- strong,
- early enough,
- mild enough,
- and interpretable enough.

---

### Next Steps

1. **Generate the run sheet from the 24-run protected matrix**
   - include all fixed fields exactly as specified above

2. **Lock SOP-linked execution details**
   - aw 0.79 equilibration workflow
   - sealed dry-state vessel format
   - ultrasound vessel volume / probe depth / cooling control
   - endpoint cooling and extraction timing

3. **Prepare assay batching**
   - Assay Package S for all matrix runs
   - untreated β-LG baseline included in each assay batch
   - matched control normalization templates prebuilt

4. **Pre-register decision rules before reading results**
   - screen hit
   - strong provisional candidate
   - hexose advancement
   - pentose advancement
   - no-go criteria

5. **Reserve validation capacity in advance**
   - V01 top hexose
   - V02 second hexose
   - V03 pentose only if qualified

6. **After round completion, make the next decision**
   - whether one or two hexose donors advance
   - whether any pentose donor advances
   - whether 4 h genuinely earns its place
   - and whether ultrasound is necessary, enabling, or marginal under the matched bridge conditions

This is my final meeting recommendation and execution-ready plan.
### Agenda

We moved from project specification to **execution planning** for the next wet-lab round on **β-lactoglobulin A allergenicity reduction by glycation**. The goal was to produce **one directly executable wet-lab plan** that:

- keeps the main search in a **dry-state**, **aw-controlled**, **55–60 C**, **2–4 h**, **ultrasound-centered** window,
- includes a **matched hexose donor bridge** across:
  - lactose
  - glucose
  - galactose
  - mannose
- treats **reaction time as a trade-off variable**, not something to maximize automatically,
- includes the **minimum controls and validation runs** needed for interpretation,
- and explicitly includes a **pentose decision branch** using **both arabinose and ribose** so the project can decide whether any pentose donor should advance.

The deliverable had to be a **complete wet-lab plan**, not a strategy note, and had to specify the fields needed for run-sheet generation.

---

### Team Member Input

#### Principal Investigator

I framed the meeting around the need to stop discussing abstractly and instead produce a **single execution-ready next-round matrix**. I emphasized four required outputs for this round:

1. bridge the current local validated leaders (**lactose**, **glucose**) into the **55–60 C, 2–4 h dry-state window**,
2. test the key unvalidated hexose challengers (**galactose**, **mannose**),
3. experimentally resolve the pentose uncertainty (**arabinose vs ribose**),
4. and embed enough interpretation protection to avoid mistaking assay suppression caused by insolubility or aggregation for true allergenicity reduction.

My initial bias was:
- **full 4 h hexose bridge** at 55 C and 60 C under ultrasound,
- **2 h benchmark anchors** for lactose and glucose,
- a **small pentose decision branch** rather than full pentose optimization,
- and predefined validation rules for top hits.

After round 1, I synthesized the team’s convergence and made several provisional decisions:
- lock **dry state**, **aw 0.79**, **1:2 w/w**, and a common extraction workflow;
- lock the **8-run 4-donor hexose ultrasound bridge** at 55/60 C, 4 h;
- lock the **4-run hexose no-ultrasound comparison** at 55 C, 4 h;
- lock the **pentose core branch** at **55 C, 2 h and 3 h** for **arabinose** and **ribose**;
- include **55 C, 3 h lactose/glucose anchors** in addition to the **60 C, 2 h lactose/glucose benchmark anchors**;
- include **four heated no-sugar controls** at 55 C (2 h, 3 h, 4 h) and 60 C (4 h);
- and require **orthogonal immunological confirmation** before any branch is promoted beyond this round.

By round 2, my direction converged to a **24-run protected matrix** with an optional **26-run expansion** that adds two pentose no-ultrasound runs only if capacity is comfortable.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry/process input strongly supported **tight control of the dry-state backbone** and stressed that **moisture must not vary** in this round. The key chemistry recommendations were:

- lock the dry-state condition at **aw 0.79** using the same equilibration and sealed-handling workflow as the validated prior dry runs;
- use one common donor ratio across all donors:
  - **β-LG : donor = 1:2 (w/w)**;
- keep the **hexose bridge** as:
  - lactose / glucose / galactose / mannose
  - at **55 C and 60 C**
  - for **4 h**
  - with **ultrasound** as the main arm;
- but treat the **pentose branch more cautiously** than the hexose branch.

The chemistry lead explicitly disagreed with a symmetric pentose design and argued that pentoses should **not** be screened first at 4 h, because pentoses are more likely to enter chemically dirtier territory quickly. Instead, the recommendation was:

- test **both arabinose and ribose**,
- at **55 C only**,
- at **2 h and 3 h**,
- with ultrasound as the primary arm,
- and do not use **60 C** or **4 h** as the primary pentose decision window.

The chemistry rationale was that the proper pentose question is not “can a pentose generate the biggest numerical drop,” but rather:

> can either pentose generate a strong and interpretable reduction under a restrained practical window?

In round 2, the chemistry lead locked the ultrasound field operationally as:

- **probe sonication**
- **20 kHz**
- **30% amplitude**
- **5 s on / 5 s off**
- **10 min total sonication**
- maintain sample temperature **<=25 C**
- same ultrasound conditions for all donors

The chemistry lead also recommended additional execution wording for:
- **aw 0.79** dry-state equilibration and sealed reaction handling,
- temperature tolerance of **±0.5 C**,
- and immediate cooling / standardized extraction timing after reaction completion.

For promoted pentose hits, the minimal chemistry-risk validation package recommended was:
- **browning index** (e.g. A420),
- **fluorescent AGE trend screen** (e.g. Ex 370 / Em 440),
- preferably also **OPA/free amino group trend**.

The chemistry lead supported the **24-run protected matrix** and stated that the **2 pentose no-ultrasound runs should be cut first** if any reduction in scope is needed.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology input centered on the need to distinguish **true reduction in allergenic recognition** from:
- masking,
- aggregation,
- insolubility,
- extraction loss,
- or assay-format artifact.

A major point was that pentoses are the branch **most likely to look good for the wrong reasons**, so they require a stricter interpretation bar.

The immunology lead recommended that **every screening run** receive a minimum assay package containing:

1. the same **primary allergenicity assay** used to generate the historical `reduction_pct_reported`,
2. **extractable/recoverable β-LG** or soluble protein readout under the standardized extraction workflow,
3. **basic aggregation / size-state assessment**,
4. a **browning / overprocessing proxy**.

For promoted hits, the validation package should add:
- **orthogonal immunological confirmation**,
- stronger aggregation assessment,
- extractability normalization review,
- and for pentose-promoted branches, extra chemistry-risk readouts.

The immunology lead agreed with the chemistry recommendation that the pentose branch should be:
- **55 C only**
- **2 h and 3 h**
- **arabinose and ribose**
- ultrasound-centered

but also argued that pentoses should **not be interpreted in isolation**, which is why the **55 C, 3 h lactose/glucose anchors** were defended strongly.

By round 2, the immunology lead converted the interpretation criteria into operational thresholds:

- **acceptable extractability for screening:**  
  **>=60%** of untreated β-LG baseline
- **borderline:**  
  **50–59%**
- **unacceptable:**  
  **<50%**
- **preferred extractability for promoted pentose branches:**  
  **>=70%**

Aggregation-dominant artifact was operationalized as a run meeting **2 or more** of:
- marked monomer loss in soluble fraction,
- prominent high-MW smear / aggregated material,
- extractability <60%,
- orthogonal inconsistency if tested,
- signal loss mainly explained by disappearance from the soluble fraction.

Orthogonal confirmation was considered directionally consistent if:
- the orthogonal assay also showed reduced recognition,
- in the same practical direction,
- without collapsing the hit or reversing the practical conclusion.

The immunology lead supported automatic validation of:
- the **top 2 hexose branches**
- plus the **top pentose branch if it qualifies**

and explicitly preferred protecting the **55 C, 3 h lactose/glucose anchors** over the optional pentose no-ultrasound pair.

---

#### Experimental Design and Evidence Synthesis Scientist

The design input focused on finding the **smallest matrix that resolves the critical uncertainties** without producing uninterpretable apparent winners.

The six decision questions identified were:

1. matched **hexose donor ranking** outside the current local domain,
2. **55 C vs 60 C** at 4 h,
3. whether ultrasound is **broadly enabling or only locally helpful**,
4. whether **4 h earns its place** for benchmark donors relative to earlier anchors,
5. whether **either pentose deserves advancement at all**,
6. whether a pentose is competitive under a **restrained practical window**.

The design lead concluded that the cleanest default plan is a **24-run protected matrix** composed of five blocks:

- **Block 1: 8-run core hexose donor bridge**
- **Block 2: 4-run hexose no-ultrasound bridge**
- **Block 3: 4-run benchmark and practical anchors**
- **Block 4: 4-run pentose decision branch**
- **Block 5: 4-run heated no-sugar controls**

The design lead also proposed an **expanded 26-run version** that adds:
- arabinose, 55 C, 2 h, no ultrasound
- ribose, 55 C, 2 h, no ultrasound

but agreed by round 2 that these are optional only.

Replication logic was finalized as:
- **n = 2 independent process replicates for every matrix run**
- **technical duplicate** for the primary assay
- **n = 3 independent process replicates** for promoted validation reruns

The design lead also formalized the advancement criteria:

**Screen hit**
- primary allergenicity reduction **>=70%**
- at least **15 percentage points above matched heated no-sugar control**
- extractability **>=60%**
- no aggregation-dominant artifact flag

**Strong provisional candidate**
- a screen hit that is either:
  - **>=80% reduction**, or
  - **70–79%** with meaningful burden advantage (shorter time, lower temperature, or lower ultrasound dependence)

**Hexose advancement**
- validate the **top 2 hexose branches**
- reduce to one donor only if the best branch is **>=10 points** ahead of the next-best donor under matched conditions and is clean interpretively

**Pentose advancement**
- pentose best run must be a screen hit,
- be competitive with **55 C, 3 h lactose/glucose anchors**,
- not be clearly worse than the leading hexose in extractability / aggregation / browning,
- and pass orthogonal confirmation before promotion

**No-go**
- <70% reduction,
- <15-point gain above matched no-sugar control,
- extractability <50%,
- aggregation-dominant artifact,
- failed orthogonal confirmation for a promoted candidate,
- or pentose overprocessing burden that materially outweighs its numerical advantage

The design lead strongly endorsed the **24-run protected matrix** as the default final plan.

---

#### Scientific Critic

The critic’s role in round 1 was to warn against **overbuilding the matrix** and to press the team to ensure every run answered a distinct, important question.

The main criticisms were:
- the risk of a **too-large and too-complex matrix**,
- possible redundancy within the bridge design,
- the need for **very strict pentose advancement rules**,
- and the importance of making **orthogonal confirmation mandatory** rather than optional for promoted branches.

In round 2, after the matrix was simplified and better structured, the critic concluded that the **24-run protected matrix no longer represented hidden overreach**. The critic endorsed:

- the **24-run protected matrix** as appropriately scaled,
- the **26-run expansion** only if capacity allows,
- **n = 2** process replicates for matrix runs and **n = 3** for validation,
- and the run-block structure because each block now clearly maps to a specific decision question.

If two runs had to be cut, the critic agreed they should be:
- arabinose, 55 C, 2 h, no ultrasound
- ribose, 55 C, 2 h, no ultrasound

The critic also agreed that the **55 C, 3 h lactose/glucose anchors earn their place** and should be retained.

---

### Recommendation

My final recommendation is to proceed with a **24-run protected next-round wet-lab plan** built around a **dry-state, aw-controlled, ultrasound-centered donor bridge** with a restrained pentose decision branch and pre-specified interpretation and advancement rules.

This is the single preferred execution-ready plan.

I am choosing this option because it best satisfies all agenda requirements simultaneously:

- it preserves the **main hexose donor bridge** using:
  - lactose
  - glucose
  - galactose
  - mannose
- it remains inside the mandated **55–60 C**, **2–4 h**, **ultrasound-centered** window;
- it treats **time as a trade-off variable** by using:
  - 4 h as the **bridge screen** for the main hexose comparison,
  - 2 h benchmark anchors,
  - 3 h practical anchors,
  - and 2–3 h pentose testing rather than maximizing pentose time;
- it includes the **minimum necessary controls** for interpretation;
- it explicitly addresses **arabinose vs ribose experimentally**;
- it avoids broad expansion into wet mode, broad pH sweeps, donor-ratio sweeps, or other pretreatment families;
- and it includes the **minimum validation structure** needed to avoid promoting false positives.

The key design choice I am making is to **treat pentoses asymmetrically relative to hexoses**. This is justified because pentoses are not simply another donor class in the same practical-risk category. Testing arabinose and ribose under **55 C, 2–3 h** is the correct way to answer the project-relevant question:

> does any pentose deserve advancement under a restrained practical window?

rather than the less useful question:

> can a pentose force a larger numerical drop under harsher conditions?

I am also choosing to keep the **55 C, 3 h lactose/glucose anchors** in the protected matrix. These runs earn their place because they do double duty:
- they provide a fair comparator for pentose advancement,
- and they help determine whether the 4 h hexose bridge is actually worth carrying forward versus a milder shorter condition.

I am **not** including the pentose no-ultrasound pair in the preferred default plan. Those two runs remain the first optional add-on if capacity is comfortable, but they are not part of the protected recommendation.

---

## 1. Round objective

Execute a single next-round wet-lab matrix that:

1. ranks the four primary hexose donors under matched dry-state bridge conditions,
2. tests whether 55 C or 60 C is preferable at 4 h,
3. classifies the practical role of ultrasound within the hexose bridge,
4. determines whether 4 h earns its place relative to earlier benchmark/practical anchors,
5. determines whether either pentose donor (**arabinose** or **ribose**) should be advanced,
6. and does so with enough interpretation protection to distinguish meaningful allergenicity reduction from extraction / aggregation / overprocessing artifacts.

---

## 2. Fixed variables

These are fixed across the round unless explicitly noted otherwise.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **dry-state handling:** same validated pre-equilibration and sealed reaction workflow as prior dry runs
- **ultrasound settings for all ultrasound runs:**
  - probe sonication
  - 20 kHz
  - 30% amplitude
  - 5 s on / 5 s off
  - 10 min total sonication time
  - maintain sample temperature **<=25 C**
- **temperature tolerance during reaction:** **±0.5 C**
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction timeline
- **screening replicate count:** **2 independent process replicates**
- **primary assay technical replication:** technical duplicate
- **screening assay package:** Assay Package S
- **validation assay package:** Assay Package V

---

## 3. Scanned variables

The variables intentionally scanned in this round are:

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - plus no-sugar controls
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **pretreatment status**
  - ultrasound
  - selected no-ultrasound controls

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

## 4. Final experiment matrix

### Assay package definitions used in the matrix

- **Assay Package S**
  1. primary allergenicity assay matched to historical `reduction_pct_reported`
  2. extractable β-LG / soluble recovery readout
  3. non-reducing SDS-PAGE of soluble fraction
  4. browning / overprocessing proxy

- **Assay Package V**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable β-LG / soluble recovery
  4. higher-resolution aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branches: fluorescent AGE trend screen; preferably OPA/free amino group trend

### Primary 24-run protected matrix

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S |
| R02 | hexose_bridge | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R03 | hexose_bridge | galactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R04 | hexose_bridge | mannose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R05 | hexose_bridge | lactose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R06 | hexose_bridge | glucose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R07 | hexose_bridge | galactose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R08 | hexose_bridge | mannose | 1:2 w/w | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S |
| R09 | hexose_noUS | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R10 | hexose_noUS | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R11 | hexose_noUS | galactose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R12 | hexose_noUS | mannose | 1:2 w/w | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R13 | benchmark_anchor | lactose | 1:2 w/w | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R14 | benchmark_anchor | glucose | 1:2 w/w | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R15 | practical_anchor | lactose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R16 | practical_anchor | glucose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R17 | pentose_branch | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R18 | pentose_branch | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R19 | pentose_branch | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S |
| R20 | pentose_branch | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S |
| R21 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S |
| R22 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S |
| R23 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S |
| R24 | heated_no_sugar_control | none | 0 | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S |

### Optional expansion only if capacity is comfortable

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R25 | pentose_noUS_optional | arabinose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | no ultrasound | no | yes | 2 | S |
| R26 | pentose_noUS_optional | ribose | 1:2 w/w | dry | aw 0.79 | 55 C | 2 h | no ultrasound | no | yes | 2 | S |

### Pre-specified validation reruns

These are not part of the fixed 24 screening runs but are part of the round plan and are triggered after screen review.

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

## 5. Pentose branch design

### Pentose branch runs
- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

### Pentose decision question
The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

### Why this design was chosen
- It does **not assume arabinose is better**
- It does **not assume ribose is better**
- It tests both under exactly matched conditions
- It avoids overcommitting to harsher pentose conditions that could bias the result toward chemically dirtier outcomes
- It compares pentoses against:
  - heated no-sugar controls,
  - and the **55 C, 3 h lactose/glucose practical anchors**

### Pentose advancement rule summary
A pentose can advance only if its best run:
- is a formal screen hit,
- is competitive with the 55 C, 3 h lactose/glucose anchors,
- is not clearly worse than the leading hexose in extractability / aggregation / browning burden,
- and passes orthogonal confirmation before promotion beyond this round.

---

## 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at the lower-severity temperature?

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter/milder benchmark-relevant conditions, and what are the practical comparator anchors for pentose interpretation?

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

---

## 7. Assay plan

### Screening assay package: Assay Package S
Apply to **R01–R24** (and R25–R26 if optional expansion is run):

1. **Primary allergenicity assay**
   - same platform used to generate historical `reduction_pct_reported`

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG batch control

3. **Basic aggregation / size-state assessment**
   - non-reducing SDS-PAGE on soluble fraction

4. **Browning / overprocessing proxy**
   - simple absorbance/color index

### Validation assay package: Assay Package V
Apply to **V01–V03**:

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

### Interpretation rules embedded in assay plan
A high apparent reduction will **not** be treated as meaningful allergenicity reduction if it is accompanied by:
- poor extractability,
- aggregation-dominant loss from the soluble fraction,
- or failure to reproduce directionally in orthogonal immunological confirmation.

---

## 8. Go / No-Go criteria

### Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

### Borderline
- extractability **50–59%** = borderline; do not promote without especially strong supporting evidence
- extractability **<50%** = fail for advancement

### Aggregation-dominant artifact flag
Flag if **2 or more** of the following are present:
- marked monomer loss in soluble fraction
- strong high-MW smear / aggregated material
- extractability <60%
- signal loss mainly explained by disappearance from soluble fraction
- orthogonal inconsistency when tested

### Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time,
  - lower temperature,
  - or lower ultrasound dependence

### Pentose-specific stricter bar
For a pentose to be promoted:
- preferred extractability should be **>=70%**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion beyond this round

### No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

## 9. Advancement logic

### Hexose advancement
Automatically send to validation:
- **top 2 hexose branches** from the screen that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond validation planning if:
- the best hexose branch is **>=10 percentage points** above the next-best matched hexose branch,
- the lead is stable,
- and there is no interpretability penalty

Otherwise keep two hexose donors active.

### Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit,
- the best pentose run is competitive with **R15/R16**,
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

### Time decision rule
Time is a trade-off variable. After the screen:
- do **not** automatically prefer 4 h over 3 h or 2 h
- prefer the earlier condition if the later condition does **not** give a clearly meaningful gain
- treat later time as justified only if it changes practical category or yields a substantial increase without interpretability penalty

### Ultrasound interpretation rule
For hexoses, classify ultrasound as:
- **necessary** if removing it drops the branch below practical competitiveness,
- **practically enabling** if removal materially worsens efficiency/severity,
- **marginally beneficial** if practical ranking is unchanged

---

## 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **Assay Package S on all screening runs**
- **Assay Package V on validation reruns**

Do **not** expand into:
- wet mode,
- pH sweep,
- donor-ratio sweep,
- additional aw points,
- or other pretreatment families in this round.

Do **not** add the pentose no-ultrasound pair unless capacity is comfortably available after the protected 24-run matrix is secured.

Most importantly, do **not** rank winners by apparent reduction alone. Promotion beyond this round requires that the leading branches remain:
- strong,
- early enough,
- mild enough,
- and interpretable enough.

---

### Next Steps

1. **Generate the run sheet from the 24-run protected matrix**
   - include all fixed fields exactly as specified above

2. **Lock SOP-linked execution details**
   - aw 0.79 equilibration workflow
   - sealed dry-state vessel format
   - ultrasound vessel volume / probe depth / cooling control
   - endpoint cooling and extraction timing

3. **Prepare assay batching**
   - Assay Package S for all matrix runs
   - untreated β-LG baseline included in each assay batch
   - matched control normalization templates prebuilt

4. **Pre-register decision rules before reading results**
   - screen hit
   - strong provisional candidate
   - hexose advancement
   - pentose advancement
   - no-go criteria

5. **Reserve validation capacity in advance**
   - V01 top hexose
   - V02 second hexose
   - V03 pentose only if qualified

6. **After round completion, make the next decision**
   - whether one or two hexose donors advance
   - whether any pentose donor advances
   - whether 4 h genuinely earns its place
   - and whether ultrasound is necessary, enabling, or marginal under the matched bridge conditions

This is my final meeting recommendation and execution-ready plan.

[end summary 2]

[begin summary 3]

### Agenda

We moved from project specification into **execution planning** for the next β-LG wet-lab round. The task was to produce **one directly executable wet-lab plan** that can be turned into a run sheet without leaving key parameters unspecified.

The round had to:

- keep the project centered on **dry-state glycation**,
- include a primary donor bridge across:
  - **lactose**
  - **glucose**
  - **galactose**
  - **mannose**
- stay within the practical operating window:
  - **55–60 C**
  - **2–4 h**
  - **ultrasound-centered**
- treat **reaction time as a trade-off variable**, not something to maximize,
- avoid broad expansion into:
  - wet-mode,
  - broad pH sweeps,
  - broad donor-ratio sweeps,
  - or alternative pretreatment families,
- include the **minimum validation structure** needed to interpret screening results,
- and explicitly include a **pentose branch** that experimentally resolves whether **arabinose** or **ribose** should be advanced, rather than leaving that question as discussion only.

The deliverable had to include:

1. round objective  
2. fixed variables  
3. scanned variables  
4. final experiment matrix  
5. pentose branch design  
6. experiment-to-question mapping  
7. assay plan  
8. go / no-go criteria  
9. advancement logic  
10. final recommendation to wet lab

with every run specifying:
- run_id
- run_role
- donor
- protein:sugar ratio or donor amount
- mode
- moisture-control condition
- temperature
- time
- pretreatment and parameters
- whether it is a no-sugar control
- whether it is a no-ultrasound control
- replicate count
- assay package

---

### Team Member Input

#### Principal Investigator

I framed the round as a **single execution-ready bridge round** whose purpose is to answer the main remaining practical questions without drifting into broad optimization.

My starting position was:

- keep the program centered on a **dry-state matched backbone**
- use:
  - **aw 0.79**
  - **1:2 protein:sugar**
  - **55–60 C**
  - **4 h** as the main screen time
  - **ultrasound** as the main arm
- preserve the **hexose bridge** as the main project engine,
- but explicitly add a **pentose decision branch** rather than deferring pentoses again.

I identified three design layers:

1. **main bridge screen**  
   - matched hexose donor bridge at 4 h, 55 C and 60 C, ultrasound

2. **minimal time and ultrasound resolution**  
   - only enough extra runs to determine whether 4 h is truly needed and whether ultrasound is necessary/enabling/marginal

3. **pentose decision branch**  
   - a compact but decisive arabinose-vs-ribose comparison within the same practical dry-state window

After round 1 input, I fixed the following as non-negotiable:
- **mode:** dry
- **moisture:** **aw 0.79**
- **ratio:** **1:2**
- **temperatures:** **55 C and 60 C**
- **main pretreatment:** ultrasound
- **main screen time:** **4 h**
- **one in-round benchmark anchor:** lactose, 60 C, 2 h, ultrasound
- **interpretability minimum:** heated no-sugar control, recovery, aggregation/size-state, orthogonal immunology for promoted candidates

I then narrowed the matrix decision to:
- a **15-run protected base**
- plus a compact **6-run add-on**
for a total of **21 runs**.

I also concluded that:
- **both pentoses must remain in both-temperature 4 h screening**
- **glucose no-US is the first no-US cut**
- and the main unresolved issue was how to spend the final 6 runs between:
  - no-ultrasound coverage,
  - and 3 h time-resolution.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry scientist strongly supported a **matched dry-state backbone** and emphasized that we should not optimize for rapid assay loss at the expense of chemically interpretable glycation.

Key chemistry points:

1. **Keep one fixed backbone across donors**
   - dry
   - aw 0.79
   - 1:2 protein:sugar
   - 55–60 C
   - ultrasound main arm

   Pentoses should **not** receive donor-specific ratio or moisture optimization in this round.

2. **Donor reactivity is not donor usefulness**
   - ribose is likely the most kinetically aggressive donor
   - arabinose also relatively reactive
   - a stronger apparent reduction from ribose may reflect:
     - overprocessing
     - crosslinking
     - browning
     - loss of extractability
     - early AGE burden
   rather than a better practical condition

3. **Pentoses should be tested at both 55 C and 60 C at 4 h**
   - one temperature alone is not enough to tell whether a pentose is broadly useful or only looks favorable at the harsher edge

4. **Minimum chemistry protection**
   - all screening runs should include:
     - browning proxy
     - extractable protein recovery
     - basic aggregation/size-state readout
   - any promoted pentose should additionally get:
     - free amino group loss
     - one AGE / advanced Maillard proxy

5. **Time logic**
   - 4 h is the right main screen
   - 3 h should be used sparingly to test whether 4 h is truly needed
   - 2 h should not be broadly repeated in this round

6. **Round-2 recommendation for 21-run plan**
   The chemistry scientist favored a compact add-on focused on:
   - lactose
   - galactose
   - ribose

   Specifically:
   - lactose 55 C 4 h no-US
   - galactose 55 C 4 h no-US
   - ribose 55 C 4 h no-US
   - lactose 55 C 3 h US
   - galactose 55 C 3 h US
   - ribose 55 C 3 h US

7. **Benchmark anchoring**
   - supported including **lactose 60 C 2 h US**
   - did **not** support adding a separate 2 h no-sugar anchor in this round

The chemistry scientist’s main compression bias was:
- if only one pentose gets deeper same-round resolution, it should be **ribose**.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology scientist agreed with the dry-state matched backbone, but pushed harder on **interpretability discipline** and the risk of selecting for **assay silence** rather than true reduction in allergenic potential.

Key interpretation points:

1. **Lower assay signal can mean multiple things**
   - true epitope disruption
   - masking
   - aggregation
   - insolubility
   - altered extractability
   - assay-format distortion

2. **Therefore, top hits need more than a single primary assay**
   Minimum interpretation structure should include:
   - heated no-sugar comparator
   - soluble recovery
   - aggregation/size-state
   - orthogonal immunological confirmation for promoted hits
   - independent repeat prep for promoted hits

3. **Pentoses need a higher interpretability threshold**
   - not a higher efficacy threshold,
   - but stronger skepticism because they are more likely to produce:
     - masking
     - overmodification
     - aggregation
     - insolubilization

4. **Operational recovery thresholds**
   - >=70% soluble recovery vs matched heated no-sugar = acceptable
   - 50–69% = caution
   - <50% = high artifact risk / promotion blocker unless unusually compelling orthogonal support exists

5. **Time logic**
   - 4 h is acceptable as the main screen
   - but same-round 3 h resolution is needed for at least selected branches if we are serious about time as a trade-off variable

6. **Strong support for in-round anchor**
   - specifically:
     - lactose 60 C 2 h US

7. **Round-2 recommendation for 21-run plan**
   The immunology scientist favored a 6-run add-on that preserved **both pentoses** as interpretable branches:

   - lactose 55 C 4 h no-US
   - arabinose 55 C 4 h no-US
   - ribose 55 C 4 h no-US
   - lactose 55 C 3 h US
   - galactose 55 C 3 h US
   - ribose 55 C 3 h US

8. **Reason for preferring this over the chemistry version**
   - both pentoses need at least one added robustness comparison
   - otherwise the pentose branch becomes asymmetrical, with ribose better characterized than arabinose

9. **Predefined V1 validation set**
   Recommended default higher-validation subset:
   - lactose 55 C 4 h US
   - lactose 60 C 4 h US
   - galactose 55 C 4 h US
   - mannose 55 C 4 h US
   - arabinose 55 C 4 h US
   - ribose 55 C 4 h US
   - lactose 60 C 2 h US anchor

10. **Trigger-based escalation**
   Additional V1 if:
   - any run reaches >=80%
   - any run is within <10 points of the top condition
   - any pentose run shows high reduction with recovery/aggregation concern
   - any 3 h or no-US run materially changes practical ranking

---

#### Experimental Design and Evidence Synthesis Scientist

The design scientist focused on converting the discussion into a **fully pre-specified, fixed run list** rather than a partly adaptive design.

Key design points:

1. A good design must answer six decision questions:
   - hexose donor ranking
   - 55 C vs 60 C
   - whether 4 h earns its place
   - whether ultrasound is necessary/enabling/marginal
   - whether any pentose should remain in the program
   - if so, whether arabinose or ribose should advance

2. The **irreducible core** is:
   - 8 hexose runs at 4 h US across 55 C and 60 C
   - 4 pentose runs at 4 h US across 55 C and 60 C
   - 2 heated no-sugar controls
   = 14 runs

3. Supported inclusion of:
   - one in-round benchmark anchor:
     - lactose 60 C 2 h US

4. Initially proposed a 25-run fixed matrix, but in round 2 accepted that a **21-run fixed matrix** could still meet the agenda.

5. Final preferred 21-run matrix matched the immunology recommendation:
   - protected 15-run base
   - plus:
     - lactose 55 C 4 h no-US
     - arabinose 55 C 4 h no-US
     - ribose 55 C 4 h no-US
     - lactose 55 C 3 h US
     - galactose 55 C 3 h US
     - ribose 55 C 3 h US

6. Key design rationale:
   - both pentoses should get at least one added robustness comparison
   - ribose should get the extra 3 h check
   - mannose can remain only in the protected base because the pentose branch is explicitly required by the agenda

7. Replicate structure recommendation:
   - screening runs: **n = 2** independent reaction replicates
   - no-sugar controls and anchor: **n = 3**
   - V1/promoted runs: add **1 extra independent prep** to bring effective n to 3

8. Role-based design logic:
   - global donor/temperature screen
   - in-round benchmark anchor
   - ultrasound classification subset
   - time trade-off subset

This role-based framing was important in justifying the 21-run design as coherent even though not fully factorial.

---

#### Scientific Critic

The critic’s main role was to constrain scope and prevent the plan from becoming too large or too assumption-heavy.

Key critical points:

1. The earlier **25-run matrix** risked becoming too large and burdensome.
2. The plan should remain:
   - compact
   - executable
   - interpretable
3. Initially argued for a smaller pentose branch, but after round 2 accepted the **21-run direction**.
4. Agreed that:
   - both pentoses should remain under scrutiny
   - both should receive no-ultrasound testing if possible
5. Continued to question whether lactose needed both:
   - 55 C 4 h no-US
   - and 55 C 3 h US
   but did not object strongly enough to overturn the consensus leaning
6. Endorsed the final compact structure in principle, with the caution that:
   - any further additions should be avoided
   - and unexpected assay artifacts should still be monitored closely

The critic’s contribution was especially important in pushing the group from a 25-run plan toward a tighter 21-run fixed matrix.

---

### Recommendation

My final recommendation is to proceed with a **21-run fixed dry-state execution matrix** built from:

- a **15-run protected base**
- plus a **6-run compact trade-off/robustness block**

This is the best balance between:
- answering all mandatory agenda questions,
- preserving the central hexose donor bridge,
- explicitly resolving the pentose branch,
- keeping time as a trade-off variable,
- and remaining compact enough for immediate wet-lab execution.

I am choosing the **21-run matrix** over the 25-run version because:
- the 25-run design adds breadth, but not enough incremental decision value to justify the extra burden in this round;
- the 21-run design still directly answers:
  - donor ranking
  - temperature comparison
  - pentose advancement question
  - limited ultrasound dependence
  - limited time trade-off resolution
- and it preserves interpretability protections without turning this round into broad optimization.

I am choosing the **immunology/design version** of the 6-run add-on over the chemistry version because:
- the agenda explicitly requires the pentose branch to determine **whether a pentose donor should be advanced and under what conditions**,
- and that requires **both arabinose and ribose** to receive at least one added robustness comparison beyond the main 4 h two-temperature screen,
- whereas the chemistry version gave deeper same-round resolution to ribose but left arabinose less well characterized.

So the final add-on block will be:

- lactose 55 C 4 h no-US
- arabinose 55 C 4 h no-US
- ribose 55 C 4 h no-US
- lactose 55 C 3 h US
- galactose 55 C 3 h US
- ribose 55 C 3 h US

This is the most balanced compact design.

---

## 1. Round objective

Execute a **single fixed next-round dry-state wet-lab program** that:

1. ranks the four main hexose donors (**lactose, glucose, galactose, mannose**) under matched dry-state conditions,
2. compares **55 C vs 60 C** at the matched 4 h screen,
3. determines whether **4 h** is justified or whether selected branches can be compressed to **3 h** without a meaningful loss,
4. classifies ultrasound effect for key branches at the milder practical edge,
5. resolves whether a **pentose donor** should remain in the project,
6. and if so, whether **arabinose** or **ribose** is the stronger and more interpretable pentose advancement candidate.

---

## 2. Fixed variables

These are fixed for this round unless explicitly varied in the matrix:

- **protein:** β-lactoglobulin A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w equivalent as lab default matched donor loading)**
- **pretreatment main arm:** ultrasound
- **ultrasound parameters:** **20 kHz probe sonication, 400 W nominal power, 30% amplitude, pulse 5 s on / 5 s off, 15 min total treatment, sample maintained in ice bath to keep bulk temperature <25 C before dry incubation**
- **post-sonication handling:** immediate equilibration to dry-state formulation and aw 0.79
- **reaction platform:** controlled dry incubation
- **temperature window:** **55 C and 60 C**
- **time window in this round:** **2 h, 3 h, 4 h**
- **pH:** no added pH experimental factor in this dry-state round
- **other pretreatments:** none
- **wet-mode expansion:** excluded
- **broad ratio sweep:** excluded
- **broad pH sweep:** excluded

---

## 3. Scanned variables

Variables intentionally varied in this round:

- **donor**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h for in-round lactose benchmark anchor only
  - 3 h for selected time-tradeoff runs
  - 4 h for main bridge screen
- **ultrasound status**
  - ultrasound main arm
  - selected no-ultrasound controls at 55 C, 4 h

---

## 4. Final experiment matrix

### Assay package codes
- **S** = screening package
- **V1** = screening package + predefined orthogonal validation
- **V1-trigger** = screening package initially; escalate to V1 if trigger met

### Replicate rules
- **n = 2** independent reaction replicates for standard screening runs
- **n = 3** independent reaction replicates for no-sugar controls and benchmark anchor
- if a run is promoted by trigger, prepare **1 additional independent reaction replicate** for confirmation

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, 20 kHz, 400 W, 30% amp, 5 s on/5 s off, 15 min, ice bath | no | no | 2 | V1 |
| R02 | hexose_bridge | glucose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R03 | hexose_bridge | galactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R04 | hexose_bridge | mannose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R05 | hexose_bridge | lactose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R06 | hexose_bridge | glucose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R07 | hexose_bridge | galactose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R08 | hexose_bridge | mannose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R09 | pentose_screen | arabinose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R10 | pentose_screen | ribose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R11 | pentose_screen | arabinose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R12 | pentose_screen | ribose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R13 | heated_control | none | 0 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | yes | no | 3 | S |
| R14 | heated_control | none | 0 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | yes | no | 3 | S |
| R15 | benchmark_anchor | lactose | 1:2 | dry | aw 0.79 | 60 C | 2 h | ultrasound, same as above | no | no | 3 | V1 |
| R16 | noUS_classification | lactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R17 | noUS_pentose | arabinose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R18 | noUS_pentose | ribose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R19 | time_tradeoff | lactose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |
| R20 | time_tradeoff | galactose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |
| R21 | time_tradeoff | ribose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |

---

## 5. Pentose branch design

### Pentose branch runs
- **R09** arabinose, 55 C, 4 h, US
- **R10** ribose, 55 C, 4 h, US
- **R11** arabinose, 60 C, 4 h, US
- **R12** ribose, 60 C, 4 h, US
- **R17** arabinose, 55 C, 4 h, no-US
- **R18** ribose, 55 C, 4 h, no-US
- **R21** ribose, 55 C, 3 h, US

### Pentose decision questions addressed
1. **Should a pentose remain in the project at all?**
   - compare pentose 4 h US performance to the best advancing hexose branches

2. **Which pentose is better: arabinose or ribose?**
   - direct matched comparison at:
     - 55 C, 4 h, US
     - 60 C, 4 h, US

3. **Is pentose performance robust at the milder edge?**
   - compare arabinose and ribose at 55 C, 4 h, no-US

4. **Is ribose only impressive because 4 h is too long/aggressive?**
   - compare ribose 55 C, 3 h, US vs ribose 55 C, 4 h, US

### Pentose advancement interpretation
A pentose advances only if it is:
- competitive in reduction,
- acceptable in recovery,
- not dominated by aggregation/insolubilization artifact,
- supported by orthogonal immunological confirmation,
- and not obviously dependent on an unjustified severity burden.

---

## 6. Experiment-to-question mapping

| Question | Runs answering it |
|---|---|
| Which hexose donor is strongest under matched dry-state 4 h ultrasound conditions? | R01–R08 |
| Is 55 C or 60 C better at 4 h for each donor? | R01 vs R05, R02 vs R06, R03 vs R07, R04 vs R08, R09 vs R11, R10 vs R12 |
| Do sugar donors outperform heated no-sugar controls? | donor runs vs R13/R14 |
| Does 4 h appear worth carrying forward for leading branches? | R19 vs R01, R20 vs R03, R21 vs R10, plus R15 historical anchor context |
| Is ultrasound necessary, enabling, or marginal for selected branches? | R16 vs R01, R17 vs R09, R18 vs R10 |
| Does a pentose donor deserve advancement? | R09–R12, R17–R18, R21 compared with advancing hexose runs |
| Which pentose is better under matched conditions? | R09 vs R10, R11 vs R12, R17 vs R18 |
| Does the current benchmark branch still anchor the space in this batch/assay context? | R15 vs prior benchmark context and vs R05 |

---

## 7. Assay plan

### Package S: screening package for all runs
Apply to **all 21 runs**.

Components:
1. **Primary allergenicity assay**
   - same primary assay format used for continuity with current β-LG dataset
2. **Matched soluble/extractable protein recovery**
   - quantify soluble recovered protein relative to matched heated no-sugar control
3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE as default
   - SEC may substitute if that is the lab default, but do not leave this unmeasured
4. **Browning proxy**
   - visual browning score plus absorbance index on reconstituted samples
5. **Normalization to matched heated no-sugar control**

### Package V1: predefined validation subset
Apply by default to:
- R01 lactose 55 C 4 h US
- R05 lactose 60 C 4 h US
- R03 galactose 55 C 4 h US
- R04 mannose 55 C 4 h US
- R09 arabinose 55 C 4 h US
- R10 ribose 55 C 4 h US
- R15 lactose 60 C 2 h US

V1 includes:
1. all Package S measurements
2. **orthogonal immunological confirmation**
   - use an assay format less dependent on the same presentation artifact as the primary screen
   - preferred: inhibition-format or alternate binding configuration per lab default
3. **soluble-phase normalized immunoreactivity interpretation**
4. **independent repeat preparation** if run is promoted

### Trigger-based V1 escalation
Escalate any additional run to V1 if:
- reported reduction is **>=80%**
- or within **<10 percentage points** of the top overall condition
- or it is a pentose condition with strong reduction plus recovery/aggregation concern
- or a 3 h / no-US run materially changes the preferred practical ranking

### Additional chemistry-risk readouts for promoted pentose hits
For any pentose branch being considered for advancement, add:
- **free amino group loss** assay
- **one AGE / advanced Maillard proxy**  
  (fluorescence AGE proxy or lab-default targeted AGE readout)

Do not apply this to all 21 runs; use it only for promoted pentose candidates.

---

## 8. Go / No-Go criteria

### General efficacy bands
- **Band A:** >=80% reduction
- **Band B:** 70–79% reduction if meaningfully faster, milder, or simpler
- **Below Band B:** generally do not advance unless there is a very strong interpretability or process advantage

### Practical time rule
Do **not** prefer the later timepoint if the extra hour gives **<10 percentage points** additional reduction, unless that later timepoint changes the branch into a meaningfully better practical category.

### Recovery / interpretability gates
- **>=70%** soluble recovery vs matched heated no-sugar = acceptable
- **50–69%** = caution
- **<50%** = no-go for advancement unless exceptionally strong orthogonal support exists

No branch advances if:
- orthogonal immunology fails to confirm the primary direction of effect,
- aggregation/insolubilization dominates the interpretation,
- or the apparent reduction depends mainly on loss of recoverable material.

### Ultrasound classification
At 55 C, 4 h:
- **necessary** if removing ultrasound drops the branch below Band B or forces unjustified severity
- **practically enabling** if no-US remains active but clearly less competitive
- **marginally beneficial** if no-US stays within the same efficacy band and within <10 points

### Pentose-specific go/no-go
A pentose advances only if:
- it is in Band A, or strong Band B and within **10 points** of the best advancing hexose,
- recovery is **>=70%**,
- aggregation is not dominant,
- orthogonal immunology confirms the effect,
- and its extra robustness comparison does not collapse its practical value.

For **ribose**, a byproduct-risk marker is required before promotion.

---

## 9. Advancement logic

### Step 1: Rank 4 h ultrasound donor branches
Primary ranking set:
- R01–R12

Use matched 4 h US runs to rank:
- hexoses
- pentoses
- and temperature preference

### Step 2: Apply interpretability filter
Before any branch is considered practical:
- review recovery
- aggregation/size-state
- browning
- orthogonal validation where assigned or triggered

### Step 3: Evaluate time trade-off
Compare:
- R19 vs R01
- R20 vs R03
- R21 vs R10

Decision rule:
- if 3 h is within **<10 points** of 4 h and remains in the same practical efficacy band, prefer **3 h**
- if 4 h gives a clearly meaningful gain, keep 4 h

### Step 4: Evaluate ultrasound dependence
Compare:
- R16 vs R01
- R17 vs R09
- R18 vs R10

Classify ultrasound as:
- necessary
- enabling
- or marginal

### Step 5: Branch advancement decisions

#### Hexose branch advancement
Advance one or two hexose donors if they:
- rank at the top or within <10 points of the top
- pass interpretability gates
- and show acceptable 3 h / 4 h trade-off logic where tested

If one hexose is clearly >10 points ahead and clean, advance one.  
If two are within <10 points and both are interpretable, advance two.

#### Pentose branch advancement
Advance a pentose only if:
- it is competitive with the best advancing hexose,
- passes recovery/aggregation/orthogonal confirmation,
- and does not require unjustified severity

Likely outcomes:
- **advance ribose only** if it is strong and clean and 3 h remains competitive
- **advance arabinose only** if it is more interpretable/robust and reasonably competitive
- **advance no pentose** if pentose reductions appear artifact-driven or practically inferior

### Step 6: Use round outcomes to define round 3
- If **galactose** wins or is near-top and clean:
  - move to local time refinement and possibly ratio refinement later
- If **mannose** unexpectedly ranks near-top:
  - add targeted time/ultrasound refinement next
- If **lactose** remains strongest:
  - refine within lactose branch around 55–60 C and 2–4 h
- If **ribose** is strong but chemically risky:
  - do not promote until byproduct-risk readout is acceptable
- If **no pentose** passes the gates:
  - terminate pentose branch for now

---

## 10. Final recommendation to wet lab

Proceed with the following **preferred execution-ready next round**:

### Core execution decision
Run a **21-run fixed dry-state matrix** using:
- **aw 0.79**
- **1:2 protein:sugar**
- **55 C and 60 C**
- **ultrasound-centered design**
- **4 h as the main screen**
- plus selected **55 C, 3 h** and **55 C, no-ultrasound** runs
- plus one **60 C, 2 h lactose ultrasound benchmark anchor**

### Why this is the right plan
This plan is the best available compromise because it:
- preserves the full required hexose donor bridge,
- explicitly resolves the pentose branch with both **arabinose** and **ribose**,
- keeps time as a trade-off variable,
- avoids broad low-value expansion,
- includes enough controls and validation to prevent obvious assay-artifact selection,
- and stays compact enough for immediate execution.

### Operational wet-lab instruction
Generate the run sheet exactly from **R01–R21** above, using the fixed backbone and assay package assignments provided.

Do **not** add:
- wet-mode runs
- pH variants
- ratio variants
- alternate pretreatments
- broad 2 h replication beyond the specified anchor
in this round.

### Protected interpretation priorities after data return
1. rank all 4 h US donor branches
2. compare 55 C vs 60 C
3. assess whether 3 h is sufficient for lactose, galactose, and ribose
4. classify ultrasound effect for lactose, arabinose, ribose
5. decide whether either pentose remains in the program
6. promote only branches that pass both efficacy and interpretability gates

---

### Next Steps

1. **Convert R01–R21 into the lab run sheet**
   - include exact sample prep order
   - sonication SOP
   - aw equilibration SOP
   - incubation order
   - assay batching plan

2. **Pre-register analysis rules before execution**
   - efficacy bands
   - <10 point per added hour rule
   - recovery thresholds
   - ultrasound classification rule
   - pentose promotion gate

3. **Lock assay packages before starting**
   - Package S for all runs
   - predefined V1 subset as listed
   - trigger rules for additional V1 escalation

4. **Ensure enough material is retained from every prep**
   - for primary assay
   - recovery
   - SDS-PAGE/SEC
   - browning proxy
   - and triggered orthogonal validation if needed

5. **Pre-plan post-round review**
   The first post-data meeting should answer, in order:
   - which donor wins at matched 4 h US,
   - whether 55 C is sufficient,
   - whether 3 h is enough for selected branches,
   - whether ultrasound is necessary or only enabling,
   - and whether arabinose or ribose deserves continuation.

This is my final execution recommendation for the round.
### Agenda

We moved from project specification into **execution planning** for the next β-LG wet-lab round. The task was to produce **one directly executable wet-lab plan** that can be turned into a run sheet without leaving key parameters unspecified.

The round had to:

- keep the project centered on **dry-state glycation**,
- include a primary donor bridge across:
  - **lactose**
  - **glucose**
  - **galactose**
  - **mannose**
- stay within the practical operating window:
  - **55–60 C**
  - **2–4 h**
  - **ultrasound-centered**
- treat **reaction time as a trade-off variable**, not something to maximize,
- avoid broad expansion into:
  - wet-mode,
  - broad pH sweeps,
  - broad donor-ratio sweeps,
  - or alternative pretreatment families,
- include the **minimum validation structure** needed to interpret screening results,
- and explicitly include a **pentose branch** that experimentally resolves whether **arabinose** or **ribose** should be advanced, rather than leaving that question as discussion only.

The deliverable had to include:

1. round objective  
2. fixed variables  
3. scanned variables  
4. final experiment matrix  
5. pentose branch design  
6. experiment-to-question mapping  
7. assay plan  
8. go / no-go criteria  
9. advancement logic  
10. final recommendation to wet lab

with every run specifying:
- run_id
- run_role
- donor
- protein:sugar ratio or donor amount
- mode
- moisture-control condition
- temperature
- time
- pretreatment and parameters
- whether it is a no-sugar control
- whether it is a no-ultrasound control
- replicate count
- assay package

---

### Team Member Input

#### Principal Investigator

I framed the round as a **single execution-ready bridge round** whose purpose is to answer the main remaining practical questions without drifting into broad optimization.

My starting position was:

- keep the program centered on a **dry-state matched backbone**
- use:
  - **aw 0.79**
  - **1:2 protein:sugar**
  - **55–60 C**
  - **4 h** as the main screen time
  - **ultrasound** as the main arm
- preserve the **hexose bridge** as the main project engine,
- but explicitly add a **pentose decision branch** rather than deferring pentoses again.

I identified three design layers:

1. **main bridge screen**  
   - matched hexose donor bridge at 4 h, 55 C and 60 C, ultrasound

2. **minimal time and ultrasound resolution**  
   - only enough extra runs to determine whether 4 h is truly needed and whether ultrasound is necessary/enabling/marginal

3. **pentose decision branch**  
   - a compact but decisive arabinose-vs-ribose comparison within the same practical dry-state window

After round 1 input, I fixed the following as non-negotiable:
- **mode:** dry
- **moisture:** **aw 0.79**
- **ratio:** **1:2**
- **temperatures:** **55 C and 60 C**
- **main pretreatment:** ultrasound
- **main screen time:** **4 h**
- **one in-round benchmark anchor:** lactose, 60 C, 2 h, ultrasound
- **interpretability minimum:** heated no-sugar control, recovery, aggregation/size-state, orthogonal immunology for promoted candidates

I then narrowed the matrix decision to:
- a **15-run protected base**
- plus a compact **6-run add-on**
for a total of **21 runs**.

I also concluded that:
- **both pentoses must remain in both-temperature 4 h screening**
- **glucose no-US is the first no-US cut**
- and the main unresolved issue was how to spend the final 6 runs between:
  - no-ultrasound coverage,
  - and 3 h time-resolution.

---

#### Maillard Reaction Chemistry and Process Scientist

The chemistry scientist strongly supported a **matched dry-state backbone** and emphasized that we should not optimize for rapid assay loss at the expense of chemically interpretable glycation.

Key chemistry points:

1. **Keep one fixed backbone across donors**
   - dry
   - aw 0.79
   - 1:2 protein:sugar
   - 55–60 C
   - ultrasound main arm

   Pentoses should **not** receive donor-specific ratio or moisture optimization in this round.

2. **Donor reactivity is not donor usefulness**
   - ribose is likely the most kinetically aggressive donor
   - arabinose also relatively reactive
   - a stronger apparent reduction from ribose may reflect:
     - overprocessing
     - crosslinking
     - browning
     - loss of extractability
     - early AGE burden
   rather than a better practical condition

3. **Pentoses should be tested at both 55 C and 60 C at 4 h**
   - one temperature alone is not enough to tell whether a pentose is broadly useful or only looks favorable at the harsher edge

4. **Minimum chemistry protection**
   - all screening runs should include:
     - browning proxy
     - extractable protein recovery
     - basic aggregation/size-state readout
   - any promoted pentose should additionally get:
     - free amino group loss
     - one AGE / advanced Maillard proxy

5. **Time logic**
   - 4 h is the right main screen
   - 3 h should be used sparingly to test whether 4 h is truly needed
   - 2 h should not be broadly repeated in this round

6. **Round-2 recommendation for 21-run plan**
   The chemistry scientist favored a compact add-on focused on:
   - lactose
   - galactose
   - ribose

   Specifically:
   - lactose 55 C 4 h no-US
   - galactose 55 C 4 h no-US
   - ribose 55 C 4 h no-US
   - lactose 55 C 3 h US
   - galactose 55 C 3 h US
   - ribose 55 C 3 h US

7. **Benchmark anchoring**
   - supported including **lactose 60 C 2 h US**
   - did **not** support adding a separate 2 h no-sugar anchor in this round

The chemistry scientist’s main compression bias was:
- if only one pentose gets deeper same-round resolution, it should be **ribose**.

---

#### Allergenicity and Immunoassay Interpretation Scientist

The immunology scientist agreed with the dry-state matched backbone, but pushed harder on **interpretability discipline** and the risk of selecting for **assay silence** rather than true reduction in allergenic potential.

Key interpretation points:

1. **Lower assay signal can mean multiple things**
   - true epitope disruption
   - masking
   - aggregation
   - insolubility
   - altered extractability
   - assay-format distortion

2. **Therefore, top hits need more than a single primary assay**
   Minimum interpretation structure should include:
   - heated no-sugar comparator
   - soluble recovery
   - aggregation/size-state
   - orthogonal immunological confirmation for promoted hits
   - independent repeat prep for promoted hits

3. **Pentoses need a higher interpretability threshold**
   - not a higher efficacy threshold,
   - but stronger skepticism because they are more likely to produce:
     - masking
     - overmodification
     - aggregation
     - insolubilization

4. **Operational recovery thresholds**
   - >=70% soluble recovery vs matched heated no-sugar = acceptable
   - 50–69% = caution
   - <50% = high artifact risk / promotion blocker unless unusually compelling orthogonal support exists

5. **Time logic**
   - 4 h is acceptable as the main screen
   - but same-round 3 h resolution is needed for at least selected branches if we are serious about time as a trade-off variable

6. **Strong support for in-round anchor**
   - specifically:
     - lactose 60 C 2 h US

7. **Round-2 recommendation for 21-run plan**
   The immunology scientist favored a 6-run add-on that preserved **both pentoses** as interpretable branches:

   - lactose 55 C 4 h no-US
   - arabinose 55 C 4 h no-US
   - ribose 55 C 4 h no-US
   - lactose 55 C 3 h US
   - galactose 55 C 3 h US
   - ribose 55 C 3 h US

8. **Reason for preferring this over the chemistry version**
   - both pentoses need at least one added robustness comparison
   - otherwise the pentose branch becomes asymmetrical, with ribose better characterized than arabinose

9. **Predefined V1 validation set**
   Recommended default higher-validation subset:
   - lactose 55 C 4 h US
   - lactose 60 C 4 h US
   - galactose 55 C 4 h US
   - mannose 55 C 4 h US
   - arabinose 55 C 4 h US
   - ribose 55 C 4 h US
   - lactose 60 C 2 h US anchor

10. **Trigger-based escalation**
   Additional V1 if:
   - any run reaches >=80%
   - any run is within <10 points of the top condition
   - any pentose run shows high reduction with recovery/aggregation concern
   - any 3 h or no-US run materially changes practical ranking

---

#### Experimental Design and Evidence Synthesis Scientist

The design scientist focused on converting the discussion into a **fully pre-specified, fixed run list** rather than a partly adaptive design.

Key design points:

1. A good design must answer six decision questions:
   - hexose donor ranking
   - 55 C vs 60 C
   - whether 4 h earns its place
   - whether ultrasound is necessary/enabling/marginal
   - whether any pentose should remain in the program
   - if so, whether arabinose or ribose should advance

2. The **irreducible core** is:
   - 8 hexose runs at 4 h US across 55 C and 60 C
   - 4 pentose runs at 4 h US across 55 C and 60 C
   - 2 heated no-sugar controls
   = 14 runs

3. Supported inclusion of:
   - one in-round benchmark anchor:
     - lactose 60 C 2 h US

4. Initially proposed a 25-run fixed matrix, but in round 2 accepted that a **21-run fixed matrix** could still meet the agenda.

5. Final preferred 21-run matrix matched the immunology recommendation:
   - protected 15-run base
   - plus:
     - lactose 55 C 4 h no-US
     - arabinose 55 C 4 h no-US
     - ribose 55 C 4 h no-US
     - lactose 55 C 3 h US
     - galactose 55 C 3 h US
     - ribose 55 C 3 h US

6. Key design rationale:
   - both pentoses should get at least one added robustness comparison
   - ribose should get the extra 3 h check
   - mannose can remain only in the protected base because the pentose branch is explicitly required by the agenda

7. Replicate structure recommendation:
   - screening runs: **n = 2** independent reaction replicates
   - no-sugar controls and anchor: **n = 3**
   - V1/promoted runs: add **1 extra independent prep** to bring effective n to 3

8. Role-based design logic:
   - global donor/temperature screen
   - in-round benchmark anchor
   - ultrasound classification subset
   - time trade-off subset

This role-based framing was important in justifying the 21-run design as coherent even though not fully factorial.

---

#### Scientific Critic

The critic’s main role was to constrain scope and prevent the plan from becoming too large or too assumption-heavy.

Key critical points:

1. The earlier **25-run matrix** risked becoming too large and burdensome.
2. The plan should remain:
   - compact
   - executable
   - interpretable
3. Initially argued for a smaller pentose branch, but after round 2 accepted the **21-run direction**.
4. Agreed that:
   - both pentoses should remain under scrutiny
   - both should receive no-ultrasound testing if possible
5. Continued to question whether lactose needed both:
   - 55 C 4 h no-US
   - and 55 C 3 h US
   but did not object strongly enough to overturn the consensus leaning
6. Endorsed the final compact structure in principle, with the caution that:
   - any further additions should be avoided
   - and unexpected assay artifacts should still be monitored closely

The critic’s contribution was especially important in pushing the group from a 25-run plan toward a tighter 21-run fixed matrix.

---

### Recommendation

My final recommendation is to proceed with a **21-run fixed dry-state execution matrix** built from:

- a **15-run protected base**
- plus a **6-run compact trade-off/robustness block**

This is the best balance between:
- answering all mandatory agenda questions,
- preserving the central hexose donor bridge,
- explicitly resolving the pentose branch,
- keeping time as a trade-off variable,
- and remaining compact enough for immediate wet-lab execution.

I am choosing the **21-run matrix** over the 25-run version because:
- the 25-run design adds breadth, but not enough incremental decision value to justify the extra burden in this round;
- the 21-run design still directly answers:
  - donor ranking
  - temperature comparison
  - pentose advancement question
  - limited ultrasound dependence
  - limited time trade-off resolution
- and it preserves interpretability protections without turning this round into broad optimization.

I am choosing the **immunology/design version** of the 6-run add-on over the chemistry version because:
- the agenda explicitly requires the pentose branch to determine **whether a pentose donor should be advanced and under what conditions**,
- and that requires **both arabinose and ribose** to receive at least one added robustness comparison beyond the main 4 h two-temperature screen,
- whereas the chemistry version gave deeper same-round resolution to ribose but left arabinose less well characterized.

So the final add-on block will be:

- lactose 55 C 4 h no-US
- arabinose 55 C 4 h no-US
- ribose 55 C 4 h no-US
- lactose 55 C 3 h US
- galactose 55 C 3 h US
- ribose 55 C 3 h US

This is the most balanced compact design.

---

## 1. Round objective

Execute a **single fixed next-round dry-state wet-lab program** that:

1. ranks the four main hexose donors (**lactose, glucose, galactose, mannose**) under matched dry-state conditions,
2. compares **55 C vs 60 C** at the matched 4 h screen,
3. determines whether **4 h** is justified or whether selected branches can be compressed to **3 h** without a meaningful loss,
4. classifies ultrasound effect for key branches at the milder practical edge,
5. resolves whether a **pentose donor** should remain in the project,
6. and if so, whether **arabinose** or **ribose** is the stronger and more interpretable pentose advancement candidate.

---

## 2. Fixed variables

These are fixed for this round unless explicitly varied in the matrix:

- **protein:** β-lactoglobulin A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w equivalent as lab default matched donor loading)**
- **pretreatment main arm:** ultrasound
- **ultrasound parameters:** **20 kHz probe sonication, 400 W nominal power, 30% amplitude, pulse 5 s on / 5 s off, 15 min total treatment, sample maintained in ice bath to keep bulk temperature <25 C before dry incubation**
- **post-sonication handling:** immediate equilibration to dry-state formulation and aw 0.79
- **reaction platform:** controlled dry incubation
- **temperature window:** **55 C and 60 C**
- **time window in this round:** **2 h, 3 h, 4 h**
- **pH:** no added pH experimental factor in this dry-state round
- **other pretreatments:** none
- **wet-mode expansion:** excluded
- **broad ratio sweep:** excluded
- **broad pH sweep:** excluded

---

## 3. Scanned variables

Variables intentionally varied in this round:

- **donor**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h for in-round lactose benchmark anchor only
  - 3 h for selected time-tradeoff runs
  - 4 h for main bridge screen
- **ultrasound status**
  - ultrasound main arm
  - selected no-ultrasound controls at 55 C, 4 h

---

## 4. Final experiment matrix

### Assay package codes
- **S** = screening package
- **V1** = screening package + predefined orthogonal validation
- **V1-trigger** = screening package initially; escalate to V1 if trigger met

### Replicate rules
- **n = 2** independent reaction replicates for standard screening runs
- **n = 3** independent reaction replicates for no-sugar controls and benchmark anchor
- if a run is promoted by trigger, prepare **1 additional independent reaction replicate** for confirmation

| run_id | run_role | donor | protein:sugar ratio | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, 20 kHz, 400 W, 30% amp, 5 s on/5 s off, 15 min, ice bath | no | no | 2 | V1 |
| R02 | hexose_bridge | glucose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R03 | hexose_bridge | galactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R04 | hexose_bridge | mannose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R05 | hexose_bridge | lactose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R06 | hexose_bridge | glucose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R07 | hexose_bridge | galactose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R08 | hexose_bridge | mannose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R09 | pentose_screen | arabinose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R10 | pentose_screen | ribose | 1:2 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | no | no | 2 | V1 |
| R11 | pentose_screen | arabinose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R12 | pentose_screen | ribose | 1:2 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | no | no | 2 | S |
| R13 | heated_control | none | 0 | dry | aw 0.79 | 55 C | 4 h | ultrasound, same as above | yes | no | 3 | S |
| R14 | heated_control | none | 0 | dry | aw 0.79 | 60 C | 4 h | ultrasound, same as above | yes | no | 3 | S |
| R15 | benchmark_anchor | lactose | 1:2 | dry | aw 0.79 | 60 C | 2 h | ultrasound, same as above | no | no | 3 | V1 |
| R16 | noUS_classification | lactose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R17 | noUS_pentose | arabinose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R18 | noUS_pentose | ribose | 1:2 | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S |
| R19 | time_tradeoff | lactose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |
| R20 | time_tradeoff | galactose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |
| R21 | time_tradeoff | ribose | 1:2 | dry | aw 0.79 | 55 C | 3 h | ultrasound, same as above | no | no | 2 | S |

---

## 5. Pentose branch design

### Pentose branch runs
- **R09** arabinose, 55 C, 4 h, US
- **R10** ribose, 55 C, 4 h, US
- **R11** arabinose, 60 C, 4 h, US
- **R12** ribose, 60 C, 4 h, US
- **R17** arabinose, 55 C, 4 h, no-US
- **R18** ribose, 55 C, 4 h, no-US
- **R21** ribose, 55 C, 3 h, US

### Pentose decision questions addressed
1. **Should a pentose remain in the project at all?**
   - compare pentose 4 h US performance to the best advancing hexose branches

2. **Which pentose is better: arabinose or ribose?**
   - direct matched comparison at:
     - 55 C, 4 h, US
     - 60 C, 4 h, US

3. **Is pentose performance robust at the milder edge?**
   - compare arabinose and ribose at 55 C, 4 h, no-US

4. **Is ribose only impressive because 4 h is too long/aggressive?**
   - compare ribose 55 C, 3 h, US vs ribose 55 C, 4 h, US

### Pentose advancement interpretation
A pentose advances only if it is:
- competitive in reduction,
- acceptable in recovery,
- not dominated by aggregation/insolubilization artifact,
- supported by orthogonal immunological confirmation,
- and not obviously dependent on an unjustified severity burden.

---

## 6. Experiment-to-question mapping

| Question | Runs answering it |
|---|---|
| Which hexose donor is strongest under matched dry-state 4 h ultrasound conditions? | R01–R08 |
| Is 55 C or 60 C better at 4 h for each donor? | R01 vs R05, R02 vs R06, R03 vs R07, R04 vs R08, R09 vs R11, R10 vs R12 |
| Do sugar donors outperform heated no-sugar controls? | donor runs vs R13/R14 |
| Does 4 h appear worth carrying forward for leading branches? | R19 vs R01, R20 vs R03, R21 vs R10, plus R15 historical anchor context |
| Is ultrasound necessary, enabling, or marginal for selected branches? | R16 vs R01, R17 vs R09, R18 vs R10 |
| Does a pentose donor deserve advancement? | R09–R12, R17–R18, R21 compared with advancing hexose runs |
| Which pentose is better under matched conditions? | R09 vs R10, R11 vs R12, R17 vs R18 |
| Does the current benchmark branch still anchor the space in this batch/assay context? | R15 vs prior benchmark context and vs R05 |

---

## 7. Assay plan

### Package S: screening package for all runs
Apply to **all 21 runs**.

Components:
1. **Primary allergenicity assay**
   - same primary assay format used for continuity with current β-LG dataset
2. **Matched soluble/extractable protein recovery**
   - quantify soluble recovered protein relative to matched heated no-sugar control
3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE as default
   - SEC may substitute if that is the lab default, but do not leave this unmeasured
4. **Browning proxy**
   - visual browning score plus absorbance index on reconstituted samples
5. **Normalization to matched heated no-sugar control**

### Package V1: predefined validation subset
Apply by default to:
- R01 lactose 55 C 4 h US
- R05 lactose 60 C 4 h US
- R03 galactose 55 C 4 h US
- R04 mannose 55 C 4 h US
- R09 arabinose 55 C 4 h US
- R10 ribose 55 C 4 h US
- R15 lactose 60 C 2 h US

V1 includes:
1. all Package S measurements
2. **orthogonal immunological confirmation**
   - use an assay format less dependent on the same presentation artifact as the primary screen
   - preferred: inhibition-format or alternate binding configuration per lab default
3. **soluble-phase normalized immunoreactivity interpretation**
4. **independent repeat preparation** if run is promoted

### Trigger-based V1 escalation
Escalate any additional run to V1 if:
- reported reduction is **>=80%**
- or within **<10 percentage points** of the top overall condition
- or it is a pentose condition with strong reduction plus recovery/aggregation concern
- or a 3 h / no-US run materially changes the preferred practical ranking

### Additional chemistry-risk readouts for promoted pentose hits
For any pentose branch being considered for advancement, add:
- **free amino group loss** assay
- **one AGE / advanced Maillard proxy**  
  (fluorescence AGE proxy or lab-default targeted AGE readout)

Do not apply this to all 21 runs; use it only for promoted pentose candidates.

---

## 8. Go / No-Go criteria

### General efficacy bands
- **Band A:** >=80% reduction
- **Band B:** 70–79% reduction if meaningfully faster, milder, or simpler
- **Below Band B:** generally do not advance unless there is a very strong interpretability or process advantage

### Practical time rule
Do **not** prefer the later timepoint if the extra hour gives **<10 percentage points** additional reduction, unless that later timepoint changes the branch into a meaningfully better practical category.

### Recovery / interpretability gates
- **>=70%** soluble recovery vs matched heated no-sugar = acceptable
- **50–69%** = caution
- **<50%** = no-go for advancement unless exceptionally strong orthogonal support exists

No branch advances if:
- orthogonal immunology fails to confirm the primary direction of effect,
- aggregation/insolubilization dominates the interpretation,
- or the apparent reduction depends mainly on loss of recoverable material.

### Ultrasound classification
At 55 C, 4 h:
- **necessary** if removing ultrasound drops the branch below Band B or forces unjustified severity
- **practically enabling** if no-US remains active but clearly less competitive
- **marginally beneficial** if no-US stays within the same efficacy band and within <10 points

### Pentose-specific go/no-go
A pentose advances only if:
- it is in Band A, or strong Band B and within **10 points** of the best advancing hexose,
- recovery is **>=70%**,
- aggregation is not dominant,
- orthogonal immunology confirms the effect,
- and its extra robustness comparison does not collapse its practical value.

For **ribose**, a byproduct-risk marker is required before promotion.

---

## 9. Advancement logic

### Step 1: Rank 4 h ultrasound donor branches
Primary ranking set:
- R01–R12

Use matched 4 h US runs to rank:
- hexoses
- pentoses
- and temperature preference

### Step 2: Apply interpretability filter
Before any branch is considered practical:
- review recovery
- aggregation/size-state
- browning
- orthogonal validation where assigned or triggered

### Step 3: Evaluate time trade-off
Compare:
- R19 vs R01
- R20 vs R03
- R21 vs R10

Decision rule:
- if 3 h is within **<10 points** of 4 h and remains in the same practical efficacy band, prefer **3 h**
- if 4 h gives a clearly meaningful gain, keep 4 h

### Step 4: Evaluate ultrasound dependence
Compare:
- R16 vs R01
- R17 vs R09
- R18 vs R10

Classify ultrasound as:
- necessary
- enabling
- or marginal

### Step 5: Branch advancement decisions

#### Hexose branch advancement
Advance one or two hexose donors if they:
- rank at the top or within <10 points of the top
- pass interpretability gates
- and show acceptable 3 h / 4 h trade-off logic where tested

If one hexose is clearly >10 points ahead and clean, advance one.  
If two are within <10 points and both are interpretable, advance two.

#### Pentose branch advancement
Advance a pentose only if:
- it is competitive with the best advancing hexose,
- passes recovery/aggregation/orthogonal confirmation,
- and does not require unjustified severity

Likely outcomes:
- **advance ribose only** if it is strong and clean and 3 h remains competitive
- **advance arabinose only** if it is more interpretable/robust and reasonably competitive
- **advance no pentose** if pentose reductions appear artifact-driven or practically inferior

### Step 6: Use round outcomes to define round 3
- If **galactose** wins or is near-top and clean:
  - move to local time refinement and possibly ratio refinement later
- If **mannose** unexpectedly ranks near-top:
  - add targeted time/ultrasound refinement next
- If **lactose** remains strongest:
  - refine within lactose branch around 55–60 C and 2–4 h
- If **ribose** is strong but chemically risky:
  - do not promote until byproduct-risk readout is acceptable
- If **no pentose** passes the gates:
  - terminate pentose branch for now

---

## 10. Final recommendation to wet lab

Proceed with the following **preferred execution-ready next round**:

### Core execution decision
Run a **21-run fixed dry-state matrix** using:
- **aw 0.79**
- **1:2 protein:sugar**
- **55 C and 60 C**
- **ultrasound-centered design**
- **4 h as the main screen**
- plus selected **55 C, 3 h** and **55 C, no-ultrasound** runs
- plus one **60 C, 2 h lactose ultrasound benchmark anchor**

### Why this is the right plan
This plan is the best available compromise because it:
- preserves the full required hexose donor bridge,
- explicitly resolves the pentose branch with both **arabinose** and **ribose**,
- keeps time as a trade-off variable,
- avoids broad low-value expansion,
- includes enough controls and validation to prevent obvious assay-artifact selection,
- and stays compact enough for immediate execution.

### Operational wet-lab instruction
Generate the run sheet exactly from **R01–R21** above, using the fixed backbone and assay package assignments provided.

Do **not** add:
- wet-mode runs
- pH variants
- ratio variants
- alternate pretreatments
- broad 2 h replication beyond the specified anchor
in this round.

### Protected interpretation priorities after data return
1. rank all 4 h US donor branches
2. compare 55 C vs 60 C
3. assess whether 3 h is sufficient for lactose, galactose, and ribose
4. classify ultrasound effect for lactose, arabinose, ribose
5. decide whether either pentose remains in the program
6. promote only branches that pass both efficacy and interpretability gates

---

### Next Steps

1. **Convert R01–R21 into the lab run sheet**
   - include exact sample prep order
   - sonication SOP
   - aw equilibration SOP
   - incubation order
   - assay batching plan

2. **Pre-register analysis rules before execution**
   - efficacy bands
   - <10 point per added hour rule
   - recovery thresholds
   - ultrasound classification rule
   - pentose promotion gate

3. **Lock assay packages before starting**
   - Package S for all runs
   - predefined V1 subset as listed
   - trigger rules for additional V1 escalation

4. **Ensure enough material is retained from every prep**
   - for primary assay
   - recovery
   - SDS-PAGE/SEC
   - browning proxy
   - and triggered orthogonal validation if needed

5. **Pre-plan post-round review**
   The first post-data meeting should answer, in order:
   - which donor wins at matched 4 h US,
   - whether 55 C is sufficient,
   - whether 3 h is enough for selected branches,
   - whether ultrasound is necessary or only enabling,
   - and whether arabinose or ribose deserves continuation.

This is my final execution recommendation for the round.

[end summary 3]

Here is the agenda for the meeting:

Please read the summaries of multiple separate meetings about the same agenda. Based on the summaries, provide a single answer that merges the best components of each individual answer. Please use the same format as the individual answers. Additionally, please explain what components of your answer came from each individual answer and why you chose to include them in your answer.

As a reference, here is the agenda from those meetings, which must be addressed here as well:

You are working on a research project to identify glycation conditions that reduce the allergenicity of β-lactoglobulin (β-LG, variant A). The project integrates literature evidence and wet-lab results to infer effective and practical parameter regions across variables such as sugar donor, protein:sugar ratio, reaction mode, temperature, reaction time, pH or aw/RH, and pretreatment. A key project principle is that reaction time is a trade-off variable: longer reactions may further reduce allergenicity, but they also increase AGE formation and other harmful byproducts. Therefore, the overall goal is not simply to maximize reduction at any cost, but to identify condition regions that balance efficacy, safety, and experimental practicality.

You are now in the execution planning stage.

Goal:
Generate a directly executable next-round wet-lab plan based on the current project specification, wet-lab summary, literature carryover summary, and lab defaults.

This stage must output a complete wet-lab plan, not abstract discussion.

Requirements:
- The plan must include a primary dry-state donor bridge using:
  - lactose
  - glucose
  - galactose
  - mannose
- The main comparison window should stay within:
  - 55–60 C
  - 2–4 h
  - ultrasound-centered design
- Reaction time must be treated as a trade-off variable, not simply maximized.
- Longer time should only be kept if it gives a clearly meaningful gain.
- Do not broadly expand into wet-mode, broad pH sweep, donor-ratio sweep, or other pretreatment families unless necessary.
- The plan must include not only screening runs, but also the minimum validation runs needed to interpret the results.

Important additional instruction:
The pentose branch must also be explicitly addressed in this round.

At present, the difference between arabinose and ribose is not yet clear enough to fix one as the only pentose choice.
Therefore, this uncertainty must be turned into actual experiments in the plan, rather than being left as discussion only.

You must:
- include pentose-related runs in the experiment matrix,
- provide directly executable parameter combinations for the pentose branch,
- consider both arabinose and ribose if needed,
- and explain what decision question the pentose experiments are meant to answer.

The purpose of the pentose branch is to determine whether a pentose donor should be advanced in this project, and if so, under what conditions.
Do not assume in advance that arabinose is better or that ribose is better.
Use experiments to resolve this uncertainty.

You must output one preferred execution-ready plan.
Do not stay at the strategy level.
Do not leave critical experimental fields blank.
Do not say “to be decided” for key wet-lab parameters.

The plan should include:
- a primary experiment matrix
- required controls
- validation runs for interpreting top results
- assay plan
- advancement criteria
- a pentose branch with full parameters

For every run, specify:
- run_id
- run_role
- donor
- protein:sugar ratio or donor amount
- mode
- moisture-control condition
- temperature
- time
- pretreatment and parameters
- whether it is a no-sugar control
- whether it is a no-ultrasound control
- replicate count
- assay package

Please output:

1. Round objective
2. Fixed variables
3. Scanned variables
4. Final experiment matrix
5. Pentose branch design
6. Experiment-to-question mapping
7. Assay plan
8. Go / No-Go criteria
9. Advancement logic
10. Final recommendation to wet lab

The answer must be directly usable for the next wet-lab run-sheet generation stage.




Principal Investigator, please provide your response to the agenda.

## Principal Investigator

Below is the single merged, execution-ready plan. I am deliberately combining the strongest elements from the three prior meeting lines while resolving their conflicts into one preferred design.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary severity.

This round must answer, in one matrix:

1. which of the required primary donors performs best under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its burden at the 4 h bridge screen,
3. whether **4 h** is actually needed, or whether selected branches can be carried at **3 h** with no meaningful loss,
4. whether ultrasound is **necessary, enabling, or marginal** for key branches,
5. whether a **pentose donor** should advance at all,
6. and if so, whether **arabinose** or **ribose** is the more credible advancement candidate and under what condition.

The round is designed to optimize the **practical and interpretable frontier**, not maximal apparent signal loss alone.

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = universal screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab batch workflow

- **S2 = confirmation-trigger screening package**
  - all of S1
  - plus repeat extraction consistency check
  - used automatically for all promoted validation reruns and any triggered concern runs if needed

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

> To maximize interpretability and simplify wet-lab execution, all matrix screening runs in this merged final plan receive **S1**.  
> Validation reruns receive **V**.

## Preferred primary matrix: 24-run protected design

This is the preferred merged plan.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

These are part of the round plan and should be reserved now, but are triggered after screening review.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Why this pentose design is the preferred merge

I am choosing the **55 C, 2–3 h restrained pentose branch** as the primary pentose decision window because it best enforces the project’s time-tradeoff principle and avoids biasing pentose evaluation toward harsher, chemically dirtier conditions.

This design:
- tests **both arabinose and ribose**
- does **not** assume one is better
- keeps both under exactly matched conditions
- compares both against:
  - matched heated no-sugar controls
  - **55 C, 3 h lactose/glucose** practical anchors
- asks the project-relevant question:
  - whether a pentose deserves advancement under **practical** conditions
  - not whether a pentose can produce the biggest numerical drop under harsher conditions

## Pentose advancement rule summary

A pentose can advance only if its best run:
- is a formal screen hit,
- is competitive with **R15/R16**,
- is not clearly worse than the leading hexose branch in extractability / aggregation / browning burden,
- and passes **orthogonal confirmation** before promotion.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at the lower-severity temperature?

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG batch control
   - also interpret versus matched heated no-sugar controls

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on soluble fraction

4. **Appearance / reconstitution notes**
   - include visible insolubility, unusual dispersibility, precipitation

5. **Browning / overprocessing proxy**
   - visual browning score for all runs
   - optional simple absorbance/color index if routine within same batch workflow

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## Interpretation rules embedded in assay plan

A high apparent reduction will **not** be treated as meaningful allergenicity reduction if it is accompanied by:
- poor extractability,
- aggregation-dominant loss from the soluble fraction,
- or failure to reproduce directionally in orthogonal immunological confirmation.

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = borderline; do not promote without unusually strong supporting evidence
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:
- marked monomer loss in soluble fraction
- strong high-MW smear / aggregated material
- extractability <60%
- signal loss mainly explained by disappearance from soluble fraction
- orthogonal inconsistency when tested

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be competitive with **R15/R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Use these to rank:
- donor performance
- donor-by-temperature interaction
- whether 55 C or 60 C is preferable for the main bridge

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE / aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose
- pentose interpretation uses **R17/R18/R19/R20** directly rather than assuming longer is better

Decision rule:
- do **not** automatically prefer 4 h
- prefer the earlier condition if the later condition does **not** deliver a clearly meaningful gain
- use **<10 percentage points** as the marginal-gain threshold

## Step 4 — Evaluate ultrasound dependence
Compare:
- **R09 vs R01**
- **R10 vs R02**
- **R11 vs R03**
- **R12 vs R04**

Ultrasound classification:
- **necessary** if removing ultrasound drops the branch below practical competitiveness
- **practically enabling** if removal materially worsens performance or severity burden
- **marginally beneficial** if practical ranking is unchanged

## Step 5 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 6 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is competitive with **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 7 — Next-round implication
- if one hexose clearly wins and is clean: move to focused local refinement
- if two hexoses remain close: carry both
- if a pentose is numerically strong but interpretation-poor: do not advance to mainline optimization
- if 4 h does not earn its place: collapse next round toward a **3 h-centered** program

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

---

## Source integration: what I took from each prior answer and why

## From summary 1
I kept:
- the strong emphasis on a **matched dry-state bridge**
- the **1:2 w/w** ratio and **aw 0.79**
- the rule that **time is a trade-off variable**
- the explicit **pentose advancement caution**
- the use of **browning as a universal low-burden chemistry-facing readout**
- the idea that promotion must be blocked by **poor recovery / aggregation / failed orthogonal confirmation**

Why included:
- Summary 1 was strongest on **interpretability discipline**, especially around false promotion of pentoses and artifact-driven “wins.”
- Its operational recovery and artifact logic improved decision quality.

## From summary 2
I adopted as the **core structure**:
- the **24-run protected matrix**
- the **asymmetric restrained pentose branch** at **55 C, 2–3 h**
- the **4-run hexose bridge at both temperatures, 4 h**
- the **4-run no-ultrasound hexose subset**
- the **55 C, 3 h lactose/glucose practical anchors**
- the **60 C, 2 h lactose/glucose benchmark anchors**
- the **4 heated no-sugar controls**
- the **n = 2 screening / n = 3 validation** replication logic
- the ultrasound field:
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min**
  - **<=25 C**
- the **screen-hit criteria**
- the requirement to validate **top 2 hexose branches** and **top pentose if qualified**

Why included:
- Summary 2 gave the best overall **balance between practicality and interpretability**.
- It was the most coherent single-screen design that directly answers the agenda while keeping the pentose branch project-relevant rather than severity-maximizing.

## From summary 3
I retained selectively:
- the insistence that the plan remain **compact and execution-ready**
- the useful framing that the round should answer:
  - donor ranking
  - temperature trade-off
  - time trade-off
  - ultrasound role
  - pentose advancement
- the emphasis that **both pentoses must be experimentally resolved**, not discussed abstractly
- the practical reminder that post-round decisions should be pre-registered before data readout

Why included:
- Summary 3 contributed a strong **decision-question framing** and helped keep the merged plan from drifting into overdesign.
- I did **not** use its 21-run matrix as the final choice because the 24-run plan gives better protection and cleaner comparators with only modest added burden.

## Why I chose the 24-run merged plan over the 21-run and 23-run alternatives

- Over the **21-run** version:
  - the 24-run plan gives a cleaner and fairer pentose test with **both arabinose and ribose at 2 h and 3 h**
  - retains both **55 C, 3 h practical anchors**
  - and classifies ultrasound more broadly for the required hexose bridge

- Over the **23-run** version:
  - the 23-run plan was strong, but its **4 h-focused pentose design** asks a less project-relevant question for pentoses
  - the 24-run plan better enforces the principle that **time should not be maximized by default**
  - and evaluates pentoses under a more restrained and defensible practical window

So the final merged recommendation is:

> **Use the 24-run protected matrix as the preferred execution-ready next-round wet-lab plan.**

If you want, I can now convert this directly into a **run-sheet table with sample labels, replicate IDs, assay batching order, and a pre-registered analysis template** for immediate lab handoff.
Below is the single merged, execution-ready plan. I am deliberately combining the strongest elements from the three prior meeting lines while resolving their conflicts into one preferred design.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary severity.

This round must answer, in one matrix:

1. which of the required primary donors performs best under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its burden at the 4 h bridge screen,
3. whether **4 h** is actually needed, or whether selected branches can be carried at **3 h** with no meaningful loss,
4. whether ultrasound is **necessary, enabling, or marginal** for key branches,
5. whether a **pentose donor** should advance at all,
6. and if so, whether **arabinose** or **ribose** is the more credible advancement candidate and under what condition.

The round is designed to optimize the **practical and interpretable frontier**, not maximal apparent signal loss alone.

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = universal screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab batch workflow

- **S2 = confirmation-trigger screening package**
  - all of S1
  - plus repeat extraction consistency check
  - used automatically for all promoted validation reruns and any triggered concern runs if needed

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

> To maximize interpretability and simplify wet-lab execution, all matrix screening runs in this merged final plan receive **S1**.  
> Validation reruns receive **V**.

## Preferred primary matrix: 24-run protected design

This is the preferred merged plan.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

These are part of the round plan and should be reserved now, but are triggered after screening review.

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Why this pentose design is the preferred merge

I am choosing the **55 C, 2–3 h restrained pentose branch** as the primary pentose decision window because it best enforces the project’s time-tradeoff principle and avoids biasing pentose evaluation toward harsher, chemically dirtier conditions.

This design:
- tests **both arabinose and ribose**
- does **not** assume one is better
- keeps both under exactly matched conditions
- compares both against:
  - matched heated no-sugar controls
  - **55 C, 3 h lactose/glucose** practical anchors
- asks the project-relevant question:
  - whether a pentose deserves advancement under **practical** conditions
  - not whether a pentose can produce the biggest numerical drop under harsher conditions

## Pentose advancement rule summary

A pentose can advance only if its best run:
- is a formal screen hit,
- is competitive with **R15/R16**,
- is not clearly worse than the leading hexose branch in extractability / aggregation / browning burden,
- and passes **orthogonal confirmation** before promotion.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at the lower-severity temperature?

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG batch control
   - also interpret versus matched heated no-sugar controls

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on soluble fraction

4. **Appearance / reconstitution notes**
   - include visible insolubility, unusual dispersibility, precipitation

5. **Browning / overprocessing proxy**
   - visual browning score for all runs
   - optional simple absorbance/color index if routine within same batch workflow

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## Interpretation rules embedded in assay plan

A high apparent reduction will **not** be treated as meaningful allergenicity reduction if it is accompanied by:
- poor extractability,
- aggregation-dominant loss from the soluble fraction,
- or failure to reproduce directionally in orthogonal immunological confirmation.

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = borderline; do not promote without unusually strong supporting evidence
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:
- marked monomer loss in soluble fraction
- strong high-MW smear / aggregated material
- extractability <60%
- signal loss mainly explained by disappearance from soluble fraction
- orthogonal inconsistency when tested

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be competitive with **R15/R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Use these to rank:
- donor performance
- donor-by-temperature interaction
- whether 55 C or 60 C is preferable for the main bridge

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE / aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose
- pentose interpretation uses **R17/R18/R19/R20** directly rather than assuming longer is better

Decision rule:
- do **not** automatically prefer 4 h
- prefer the earlier condition if the later condition does **not** deliver a clearly meaningful gain
- use **<10 percentage points** as the marginal-gain threshold

## Step 4 — Evaluate ultrasound dependence
Compare:
- **R09 vs R01**
- **R10 vs R02**
- **R11 vs R03**
- **R12 vs R04**

Ultrasound classification:
- **necessary** if removing ultrasound drops the branch below practical competitiveness
- **practically enabling** if removal materially worsens performance or severity burden
- **marginally beneficial** if practical ranking is unchanged

## Step 5 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 6 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is competitive with **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 7 — Next-round implication
- if one hexose clearly wins and is clean: move to focused local refinement
- if two hexoses remain close: carry both
- if a pentose is numerically strong but interpretation-poor: do not advance to mainline optimization
- if 4 h does not earn its place: collapse next round toward a **3 h-centered** program

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

---

## Source integration: what I took from each prior answer and why

## From summary 1
I kept:
- the strong emphasis on a **matched dry-state bridge**
- the **1:2 w/w** ratio and **aw 0.79**
- the rule that **time is a trade-off variable**
- the explicit **pentose advancement caution**
- the use of **browning as a universal low-burden chemistry-facing readout**
- the idea that promotion must be blocked by **poor recovery / aggregation / failed orthogonal confirmation**

Why included:
- Summary 1 was strongest on **interpretability discipline**, especially around false promotion of pentoses and artifact-driven “wins.”
- Its operational recovery and artifact logic improved decision quality.

## From summary 2
I adopted as the **core structure**:
- the **24-run protected matrix**
- the **asymmetric restrained pentose branch** at **55 C, 2–3 h**
- the **4-run hexose bridge at both temperatures, 4 h**
- the **4-run no-ultrasound hexose subset**
- the **55 C, 3 h lactose/glucose practical anchors**
- the **60 C, 2 h lactose/glucose benchmark anchors**
- the **4 heated no-sugar controls**
- the **n = 2 screening / n = 3 validation** replication logic
- the ultrasound field:
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min**
  - **<=25 C**
- the **screen-hit criteria**
- the requirement to validate **top 2 hexose branches** and **top pentose if qualified**

Why included:
- Summary 2 gave the best overall **balance between practicality and interpretability**.
- It was the most coherent single-screen design that directly answers the agenda while keeping the pentose branch project-relevant rather than severity-maximizing.

## From summary 3
I retained selectively:
- the insistence that the plan remain **compact and execution-ready**
- the useful framing that the round should answer:
  - donor ranking
  - temperature trade-off
  - time trade-off
  - ultrasound role
  - pentose advancement
- the emphasis that **both pentoses must be experimentally resolved**, not discussed abstractly
- the practical reminder that post-round decisions should be pre-registered before data readout

Why included:
- Summary 3 contributed a strong **decision-question framing** and helped keep the merged plan from drifting into overdesign.
- I did **not** use its 21-run matrix as the final choice because the 24-run plan gives better protection and cleaner comparators with only modest added burden.

## Why I chose the 24-run merged plan over the 21-run and 23-run alternatives

- Over the **21-run** version:
  - the 24-run plan gives a cleaner and fairer pentose test with **both arabinose and ribose at 2 h and 3 h**
  - retains both **55 C, 3 h practical anchors**
  - and classifies ultrasound more broadly for the required hexose bridge

- Over the **23-run** version:
  - the 23-run plan was strong, but its **4 h-focused pentose design** asks a less project-relevant question for pentoses
  - the 24-run plan better enforces the principle that **time should not be maximized by default**
  - and evaluates pentoses under a more restrained and defensible practical window

So the final merged recommendation is:

> **Use the 24-run protected matrix as the preferred execution-ready next-round wet-lab plan.**

If you want, I can now convert this directly into a **run-sheet table with sample labels, replicate IDs, assay batching order, and a pre-registered analysis template** for immediate lab handoff.

## User

Scientific Critic, please critique Principal Investigator's most recent answer. In your critique, suggest improvements that directly address the agenda and any agenda questions. Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. Only provide feedback; do not implement the answer yourself.

## Scientific Critic

**Critique of Principal Investigator's Answer**

1. **Adherence to Agenda:**
   - The Principal Investigator's answer largely adheres to the agenda by providing a comprehensive plan that includes a primary experiment matrix, required controls, validation runs, an assay plan, advancement criteria, and a pentose branch with full parameters. The plan is detailed and execution-ready, which aligns with the requirement to produce a complete wet-lab plan rather than an abstract discussion.

2. **Round Objective:**
   - The round objective is clearly stated and aligns with the agenda's goal of identifying practical glycation conditions that balance efficacy, safety, and experimental practicality. However, the objective could benefit from a more explicit mention of how the results will be used to inform future rounds, particularly regarding the decision-making process for advancing pentose donors.

3. **Fixed and Scanned Variables:**
   - The fixed and scanned variables are well-defined, providing clarity on the experimental conditions. However, the explanation for why certain variables are fixed or scanned could be expanded to justify their selection, particularly concerning the exclusion of wet-mode expansion and broad pH sweeps.

4. **Final Experiment Matrix:**
   - The experiment matrix is comprehensive and includes all necessary details. However, the rationale for selecting specific time points (2 h, 3 h, 4 h) and temperatures (55 C, 60 C) could be more explicitly linked to the project's overarching goals. Additionally, the matrix could benefit from a clearer explanation of how the selected conditions will address the trade-off between allergenicity reduction and byproduct formation.

5. **Pentose Branch Design:**
   - The pentose branch design is well-structured, but the decision criteria for advancing a pentose donor could be more detailed. Specifically, the criteria should include quantitative thresholds for what constitutes a "competitive" reduction and how "interpretability" will be assessed.

6. **Experiment-to-Question Mapping:**
   - The mapping effectively links experimental runs to specific research questions. However, it could be improved by providing more detail on how each question will be quantitatively assessed and what specific metrics will be used to evaluate success.

7. **Assay Plan:**
   - The assay plan is thorough, but it could benefit from more detail on the specific methodologies that will be used for each assay component. For instance, the plan should specify the type of SDS-PAGE to be used and any relevant controls or standards.

8. **Go / No-Go Criteria:**
   - The criteria are well-defined, but they could be strengthened by including more specific quantitative thresholds for each criterion. For example, the criteria for "aggregation-dominant artifact flag" could specify the exact percentage of monomer loss that would trigger a flag.

9. **Advancement Logic:**
   - The advancement logic is clear, but it could be improved by providing more detail on how the results will be used to inform future experimental designs. Additionally, the logic should include a contingency plan for unexpected results or failures to meet advancement criteria.

10. **Final Recommendation to Wet Lab:**
    - The recommendation is clear and actionable, but it could benefit from a more detailed explanation of how the results will be communicated to the wet-lab team and how feedback will be incorporated into future rounds.

**Suggestions for Improvement:**
- Provide more explicit justifications for the selection of fixed and scanned variables, linking them to the project's goals.
- Include more detailed quantitative criteria for decision-making, particularly for advancing pentose donors.
- Expand on the methodologies for each assay component, specifying controls and standards.
- Clarify how results will inform future rounds and include a contingency plan for unexpected outcomes.
- Enhance communication plans with the wet-lab team to ensure smooth execution and feedback integration.

Overall, the Principal Investigator's answer is well-structured and comprehensive, but it would benefit from additional detail and clarity in certain areas to fully meet the agenda's requirements.
**Critique of Principal Investigator's Answer**

1. **Adherence to Agenda:**
   - The Principal Investigator's answer largely adheres to the agenda by providing a comprehensive plan that includes a primary experiment matrix, required controls, validation runs, an assay plan, advancement criteria, and a pentose branch with full parameters. The plan is detailed and execution-ready, which aligns with the requirement to produce a complete wet-lab plan rather than an abstract discussion.

2. **Round Objective:**
   - The round objective is clearly stated and aligns with the agenda's goal of identifying practical glycation conditions that balance efficacy, safety, and experimental practicality. However, the objective could benefit from a more explicit mention of how the results will be used to inform future rounds, particularly regarding the decision-making process for advancing pentose donors.

3. **Fixed and Scanned Variables:**
   - The fixed and scanned variables are well-defined, providing clarity on the experimental conditions. However, the explanation for why certain variables are fixed or scanned could be expanded to justify their selection, particularly concerning the exclusion of wet-mode expansion and broad pH sweeps.

4. **Final Experiment Matrix:**
   - The experiment matrix is comprehensive and includes all necessary details. However, the rationale for selecting specific time points (2 h, 3 h, 4 h) and temperatures (55 C, 60 C) could be more explicitly linked to the project's overarching goals. Additionally, the matrix could benefit from a clearer explanation of how the selected conditions will address the trade-off between allergenicity reduction and byproduct formation.

5. **Pentose Branch Design:**
   - The pentose branch design is well-structured, but the decision criteria for advancing a pentose donor could be more detailed. Specifically, the criteria should include quantitative thresholds for what constitutes a "competitive" reduction and how "interpretability" will be assessed.

6. **Experiment-to-Question Mapping:**
   - The mapping effectively links experimental runs to specific research questions. However, it could be improved by providing more detail on how each question will be quantitatively assessed and what specific metrics will be used to evaluate success.

7. **Assay Plan:**
   - The assay plan is thorough, but it could benefit from more detail on the specific methodologies that will be used for each assay component. For instance, the plan should specify the type of SDS-PAGE to be used and any relevant controls or standards.

8. **Go / No-Go Criteria:**
   - The criteria are well-defined, but they could be strengthened by including more specific quantitative thresholds for each criterion. For example, the criteria for "aggregation-dominant artifact flag" could specify the exact percentage of monomer loss that would trigger a flag.

9. **Advancement Logic:**
   - The advancement logic is clear, but it could be improved by providing more detail on how the results will be used to inform future experimental designs. Additionally, the logic should include a contingency plan for unexpected results or failures to meet advancement criteria.

10. **Final Recommendation to Wet Lab:**
    - The recommendation is clear and actionable, but it could benefit from a more detailed explanation of how the results will be communicated to the wet-lab team and how feedback will be incorporated into future rounds.

**Suggestions for Improvement:**
- Provide more explicit justifications for the selection of fixed and scanned variables, linking them to the project's goals.
- Include more detailed quantitative criteria for decision-making, particularly for advancing pentose donors.
- Expand on the methodologies for each assay component, specifying controls and standards.
- Clarify how results will inform future rounds and include a contingency plan for unexpected outcomes.
- Enhance communication plans with the wet-lab team to ensure smooth execution and feedback integration.

Overall, the Principal Investigator's answer is well-structured and comprehensive, but it would benefit from additional detail and clarity in certain areas to fully meet the agenda's requirements.

## User

Principal Investigator, please modify your answer to address Scientific Critic's most recent feedback. Remember that your ultimate goal is to make improvements that better address the agenda.

## Principal Investigator

Principal Investigator: I accept the critic’s main points, but I am going to tighten them into **specific corrections**, not add unnecessary complexity. The earlier answer was close, but several parts need to be made more operational so the plan is truly ready for run-sheet generation and post-run decision-making.

The biggest needed improvements are:

1. make the **decision thresholds more explicit**,
2. make the **time-tradeoff logic more quantitative**,
3. make the **pentose competitiveness rule fully operational**,
4. add a small amount of **assay execution detail** where it affects interpretation,
5. and clarify exactly how this round determines the **next-round path**.

I am **not** changing the preferred matrix. I am keeping the **24-run protected design**, because the critic did not identify a simpler design that better answers the agenda. I am improving the specification around it.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary processing severity.

This round must produce a directly actionable decision on:

1. the ranking of the required primary donors under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its extra burden at **4 h**
3. whether **4 h** is justified, or whether selected branches should be carried forward at **3 h**
4. whether ultrasound is **necessary**, **practically enabling**, or **marginal**
5. whether a **pentose donor** should advance at all
6. and if so, whether **arabinose** or **ribose** should advance, and at **which restrained practical condition**

This round will directly feed the next round as follows:

- **one clear hexose winner** -> focused local refinement around that donor
- **two close hexose branches** -> carry both into the next refinement round
- **qualified pentose** -> validate and, only if confirmed, carry as a side-by-side advanced branch
- **no qualified pentose** -> terminate pentose advancement for the mainline program
- **4 h not justified** -> collapse the next round to a **3 h-centered refinement program**

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

## Why these are fixed
These variables are fixed because this round is a **matched donor decision experiment**, not a broad optimization campaign. Expanding wet mode, pH, aw, donor ratio, or pretreatment family in the same round would weaken interpretability and reduce our ability to answer the required donor, time, temperature, and pentose questions cleanly.

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

## Why these are scanned
These are the smallest variables needed to answer the agenda:
- donor ranking,
- practical temperature choice,
- whether 4 h earns its place,
- ultrasound role,
- and pentose advancement.

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab workflow

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

## Minimal assay execution detail required for interpretability
To avoid leaving critical assay details underspecified:
- **SDS-PAGE:** use the lab’s standard **reducing SDS-PAGE** workflow on the **soluble fraction**, with the same molecular-weight marker and batch controls across runs
- **primary assay:** run all conditions within balanced assay batches that include:
  - untreated β-LG baseline
  - matched heated no-sugar controls
  - internal inter-plate reference sample if used by the lab
- **recovery measurement:** quantify soluble recovered protein using the lab’s standard protein quantification method under one fixed extraction SOP
- **orthogonal immunology:** use the lab’s standard alternate binding-format assay or inhibition-format assay, provided it is less sensitive to the same presentation artifact as the primary assay

## Preferred primary matrix: 24-run protected design

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Explicit operational pentose competitiveness rule
A pentose branch is considered **competitive** only if all are true:

1. it is a **screen hit**
2. it is within **10 percentage points** of the better of **R15** and **R16**
3. it is not clearly worse than the leading validated hexose branch in:
   - extractability
   - aggregation pattern
   - browning burden
4. for promotion, it passes **orthogonal confirmation**
5. for ribose specifically, promotion also requires the added chemistry-risk readouts in **V03** to remain acceptable in direction

## Why this pentose design remains preferred
I am keeping the restrained **55 C, 2–3 h** pentose branch because it best tests whether a pentose can succeed under the same practical discipline we want for the main program. A pentose that only looks good under harsher chemistry is not the right mainline advancement candidate.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

**Quantitative readout used:**  
primary reduction, delta vs matched no-sugar control, extractability, aggregation pattern, browning

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at 55 C, 4 h?

**Quantitative readout used:**  
difference in reduction, change in efficacy band, change in extractability, change in interpretability burden

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

**Quantitative readout used:**  
difference in reduction between 2 h, 3 h, and 4 h, judged against the **<10-point marginal-gain rule**

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

**Quantitative readout used:**  
screen-hit status, closeness to **R15/R16**, extractability, aggregation, browning, orthogonal confirmation if triggered

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

**Quantitative readout used:**  
matched donor-minus-control improvement within each time/temperature context

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

**Quantitative readout used:**  
repeat effect direction, orthogonal concordance, repeat recovery, repeat aggregation profile

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`
   - run in technical duplicate
   - include untreated β-LG baseline in every assay batch

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG baseline
   - compare against matched heated no-sugar control

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on the soluble fraction
   - use the same gel system, marker, and batch control across all runs

4. **Appearance / reconstitution notes**
   - visible insolubility
   - precipitation
   - reconstitution difficulty
   - abnormal viscosity or clumping if observed

5. **Browning / overprocessing proxy**
   - visual browning score on 0–3 scale
   - optional simple absorbance/color index if routine in the lab

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## Trigger rule for validation entry
Send to validation if:
- it is one of the **top 2 hexose branches** meeting screen-hit criteria
- or it is the **top pentose branch** meeting pentose qualification criteria

Additional discretionary escalation is allowed if:
- a run reaches **>=80% reduction**
- or is within **<10 points** of the overall leader
- or a 3 h / no-ultrasound run materially changes practical ranking

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = borderline; do not promote without unusually strong supporting evidence
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:

1. **marked monomer loss in soluble fraction**  
   operationally: visually clear reduction of monomer band intensity relative to matched heated no-sugar control in the same gel batch

2. **strong high-MW smear / aggregated material**  
   operationally: obvious upper-region smear or retained high-MW material stronger than matched no-sugar control

3. **extractability <60%**

4. **signal loss mainly explained by disappearance from soluble fraction**

5. **orthogonal inconsistency when tested**

This flag remains partly expert-judgment based, but the decision rule is explicit: **2 or more criteria = artifact flag**.

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Practical time rule
Do **not** prefer the later timepoint if the added hour gives **<10 percentage points** additional reduction, unless the later condition changes the run into a meaningfully better practical category without adding interpretability burden.

## Ultrasound classification rule
At matched 55 C, 4 h conditions:
- **necessary** = removing ultrasound causes loss of screen-hit status or a drop of **>=10 percentage points** plus a worse practical category
- **practically enabling** = removing ultrasound worsens reduction by **5–9 points** or worsens interpretability burden enough to change preference
- **marginally beneficial** = difference is **<5 points** and practical ranking is unchanged

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be within **10 points** of the better of **R15** or **R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Rank by:
1. primary reduction
2. delta vs matched no-sugar control
3. extractability
4. aggregation/browning burden

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

Any run with an artifact flag is **not promotable**.

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose

Decision rule:
- if 3 h is within **<10 points** of 4 h and stays in the same efficacy band, prefer **3 h**
- if 4 h gives **>=10 points** extra reduction and no major interpretability penalty, keep **4 h**

For pentoses:
- compare **R17 vs R18** and **R19 vs R20**
- prefer **2 h** if 3 h gain is **<10 points**
- prefer **3 h** only if it gives a meaningful gain without worsening interpretability

## Step 4 — Evaluate temperature trade-off
Compare donor-matched 55 C vs 60 C at 4 h:
- R01 vs R05
- R02 vs R06
- R03 vs R07
- R04 vs R08

Decision rule:
- prefer **55 C** if 60 C gives **<10 points** additional reduction
- prefer **60 C** only if the gain is meaningful and does not worsen interpretability enough to offset the benefit

## Step 5 — Evaluate ultrasound dependence
Compare:
- R09 vs R01
- R10 vs R02
- R11 vs R03
- R12 vs R04

Classify ultrasound as:
- necessary
- practically enabling
- marginally beneficial

using the explicit thresholds in Section 8.

## Step 6 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 7 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is within **10 points** of the better of **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 8 — Contingency logic for ambiguous outcomes
- if no sugar-containing branch achieves screen-hit criteria:
  - do not force advancement; re-evaluate assay sensitivity and dry-state severity assumptions
- if all top branches fail interpretability:
  - do not promote numerically strong artifacts; redesign next round around milder conditions
- if multiple branches cluster within **<10 points** and all are interpretable:
  - carry forward more than one branch only if they differ in practical burden or donor class decision value

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

## Specific execution instructions for run-sheet generation
The wet-lab team should now:
1. generate sample labels for **R01–R24**
2. assign **2 independent process replicate IDs** to each matrix run
3. reserve material and schedule slots for **V01–V03**
4. batch assay plates so that each plate contains:
   - untreated β-LG baseline
   - matched no-sugar controls
   - a balanced mix of donor conditions
5. retain enough soluble fraction from every run for:
   - recovery measurement
   - SDS-PAGE
   - repeat testing if needed

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

---

## What I changed in response to the critic

I specifically addressed the critic’s feedback by:

- adding **explicit justification** for fixed vs scanned variables
- making the **pentose competitiveness rule quantitative**
- making the **time rule quantitative**
- making the **ultrasound classification thresholds quantitative**
- adding **minimal but necessary assay-method detail**
- clarifying how **future-round decisions** will be made from this round
- adding **contingency logic** for ambiguous or failed outcomes

I did **not** add broader complexity, because the right response to the critic was to make the plan **more operational**, not larger.

This is now my corrected preferred execution-ready plan.
Principal Investigator: I accept the critic’s main points, but I am going to tighten them into **specific corrections**, not add unnecessary complexity. The earlier answer was close, but several parts need to be made more operational so the plan is truly ready for run-sheet generation and post-run decision-making.

The biggest needed improvements are:

1. make the **decision thresholds more explicit**,
2. make the **time-tradeoff logic more quantitative**,
3. make the **pentose competitiveness rule fully operational**,
4. add a small amount of **assay execution detail** where it affects interpretation,
5. and clarify exactly how this round determines the **next-round path**.

I am **not** changing the preferred matrix. I am keeping the **24-run protected design**, because the critic did not identify a simpler design that better answers the agenda. I am improving the specification around it.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary processing severity.

This round must produce a directly actionable decision on:

1. the ranking of the required primary donors under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its extra burden at **4 h**
3. whether **4 h** is justified, or whether selected branches should be carried forward at **3 h**
4. whether ultrasound is **necessary**, **practically enabling**, or **marginal**
5. whether a **pentose donor** should advance at all
6. and if so, whether **arabinose** or **ribose** should advance, and at **which restrained practical condition**

This round will directly feed the next round as follows:

- **one clear hexose winner** -> focused local refinement around that donor
- **two close hexose branches** -> carry both into the next refinement round
- **qualified pentose** -> validate and, only if confirmed, carry as a side-by-side advanced branch
- **no qualified pentose** -> terminate pentose advancement for the mainline program
- **4 h not justified** -> collapse the next round to a **3 h-centered refinement program**

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

## Why these are fixed
These variables are fixed because this round is a **matched donor decision experiment**, not a broad optimization campaign. Expanding wet mode, pH, aw, donor ratio, or pretreatment family in the same round would weaken interpretability and reduce our ability to answer the required donor, time, temperature, and pentose questions cleanly.

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

## Why these are scanned
These are the smallest variables needed to answer the agenda:
- donor ranking,
- practical temperature choice,
- whether 4 h earns its place,
- ultrasound role,
- and pentose advancement.

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab workflow

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

## Minimal assay execution detail required for interpretability
To avoid leaving critical assay details underspecified:
- **SDS-PAGE:** use the lab’s standard **reducing SDS-PAGE** workflow on the **soluble fraction**, with the same molecular-weight marker and batch controls across runs
- **primary assay:** run all conditions within balanced assay batches that include:
  - untreated β-LG baseline
  - matched heated no-sugar controls
  - internal inter-plate reference sample if used by the lab
- **recovery measurement:** quantify soluble recovered protein using the lab’s standard protein quantification method under one fixed extraction SOP
- **orthogonal immunology:** use the lab’s standard alternate binding-format assay or inhibition-format assay, provided it is less sensitive to the same presentation artifact as the primary assay

## Preferred primary matrix: 24-run protected design

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Explicit operational pentose competitiveness rule
A pentose branch is considered **competitive** only if all are true:

1. it is a **screen hit**
2. it is within **10 percentage points** of the better of **R15** and **R16**
3. it is not clearly worse than the leading validated hexose branch in:
   - extractability
   - aggregation pattern
   - browning burden
4. for promotion, it passes **orthogonal confirmation**
5. for ribose specifically, promotion also requires the added chemistry-risk readouts in **V03** to remain acceptable in direction

## Why this pentose design remains preferred
I am keeping the restrained **55 C, 2–3 h** pentose branch because it best tests whether a pentose can succeed under the same practical discipline we want for the main program. A pentose that only looks good under harsher chemistry is not the right mainline advancement candidate.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

**Quantitative readout used:**  
primary reduction, delta vs matched no-sugar control, extractability, aggregation pattern, browning

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at 55 C, 4 h?

**Quantitative readout used:**  
difference in reduction, change in efficacy band, change in extractability, change in interpretability burden

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

**Quantitative readout used:**  
difference in reduction between 2 h, 3 h, and 4 h, judged against the **<10-point marginal-gain rule**

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

**Quantitative readout used:**  
screen-hit status, closeness to **R15/R16**, extractability, aggregation, browning, orthogonal confirmation if triggered

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

**Quantitative readout used:**  
matched donor-minus-control improvement within each time/temperature context

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

**Quantitative readout used:**  
repeat effect direction, orthogonal concordance, repeat recovery, repeat aggregation profile

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`
   - run in technical duplicate
   - include untreated β-LG baseline in every assay batch

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG baseline
   - compare against matched heated no-sugar control

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on the soluble fraction
   - use the same gel system, marker, and batch control across all runs

4. **Appearance / reconstitution notes**
   - visible insolubility
   - precipitation
   - reconstitution difficulty
   - abnormal viscosity or clumping if observed

5. **Browning / overprocessing proxy**
   - visual browning score on 0–3 scale
   - optional simple absorbance/color index if routine in the lab

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## Trigger rule for validation entry
Send to validation if:
- it is one of the **top 2 hexose branches** meeting screen-hit criteria
- or it is the **top pentose branch** meeting pentose qualification criteria

Additional discretionary escalation is allowed if:
- a run reaches **>=80% reduction**
- or is within **<10 points** of the overall leader
- or a 3 h / no-ultrasound run materially changes practical ranking

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = borderline; do not promote without unusually strong supporting evidence
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:

1. **marked monomer loss in soluble fraction**  
   operationally: visually clear reduction of monomer band intensity relative to matched heated no-sugar control in the same gel batch

2. **strong high-MW smear / aggregated material**  
   operationally: obvious upper-region smear or retained high-MW material stronger than matched no-sugar control

3. **extractability <60%**

4. **signal loss mainly explained by disappearance from soluble fraction**

5. **orthogonal inconsistency when tested**

This flag remains partly expert-judgment based, but the decision rule is explicit: **2 or more criteria = artifact flag**.

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Practical time rule
Do **not** prefer the later timepoint if the added hour gives **<10 percentage points** additional reduction, unless the later condition changes the run into a meaningfully better practical category without adding interpretability burden.

## Ultrasound classification rule
At matched 55 C, 4 h conditions:
- **necessary** = removing ultrasound causes loss of screen-hit status or a drop of **>=10 percentage points** plus a worse practical category
- **practically enabling** = removing ultrasound worsens reduction by **5–9 points** or worsens interpretability burden enough to change preference
- **marginally beneficial** = difference is **<5 points** and practical ranking is unchanged

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be within **10 points** of the better of **R15** or **R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Rank by:
1. primary reduction
2. delta vs matched no-sugar control
3. extractability
4. aggregation/browning burden

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

Any run with an artifact flag is **not promotable**.

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose

Decision rule:
- if 3 h is within **<10 points** of 4 h and stays in the same efficacy band, prefer **3 h**
- if 4 h gives **>=10 points** extra reduction and no major interpretability penalty, keep **4 h**

For pentoses:
- compare **R17 vs R18** and **R19 vs R20**
- prefer **2 h** if 3 h gain is **<10 points**
- prefer **3 h** only if it gives a meaningful gain without worsening interpretability

## Step 4 — Evaluate temperature trade-off
Compare donor-matched 55 C vs 60 C at 4 h:
- R01 vs R05
- R02 vs R06
- R03 vs R07
- R04 vs R08

Decision rule:
- prefer **55 C** if 60 C gives **<10 points** additional reduction
- prefer **60 C** only if the gain is meaningful and does not worsen interpretability enough to offset the benefit

## Step 5 — Evaluate ultrasound dependence
Compare:
- R09 vs R01
- R10 vs R02
- R11 vs R03
- R12 vs R04

Classify ultrasound as:
- necessary
- practically enabling
- marginally beneficial

using the explicit thresholds in Section 8.

## Step 6 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 7 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is within **10 points** of the better of **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 8 — Contingency logic for ambiguous outcomes
- if no sugar-containing branch achieves screen-hit criteria:
  - do not force advancement; re-evaluate assay sensitivity and dry-state severity assumptions
- if all top branches fail interpretability:
  - do not promote numerically strong artifacts; redesign next round around milder conditions
- if multiple branches cluster within **<10 points** and all are interpretable:
  - carry forward more than one branch only if they differ in practical burden or donor class decision value

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

## Specific execution instructions for run-sheet generation
The wet-lab team should now:
1. generate sample labels for **R01–R24**
2. assign **2 independent process replicate IDs** to each matrix run
3. reserve material and schedule slots for **V01–V03**
4. batch assay plates so that each plate contains:
   - untreated β-LG baseline
   - matched no-sugar controls
   - a balanced mix of donor conditions
5. retain enough soluble fraction from every run for:
   - recovery measurement
   - SDS-PAGE
   - repeat testing if needed

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

---

## What I changed in response to the critic

I specifically addressed the critic’s feedback by:

- adding **explicit justification** for fixed vs scanned variables
- making the **pentose competitiveness rule quantitative**
- making the **time rule quantitative**
- making the **ultrasound classification thresholds quantitative**
- adding **minimal but necessary assay-method detail**
- clarifying how **future-round decisions** will be made from this round
- adding **contingency logic** for ambiguous or failed outcomes

I did **not** add broader complexity, because the right response to the critic was to make the plan **more operational**, not larger.

This is now my corrected preferred execution-ready plan.

## User

Scientific Critic, please critique Principal Investigator's most recent answer. In your critique, suggest improvements that directly address the agenda and any agenda questions. Prioritize simple solutions over unnecessarily complex ones, but demand more detail where detail is lacking. Additionally, validate whether the answer strictly adheres to the agenda and any agenda questions and provide corrective feedback if it does not. Only provide feedback; do not implement the answer yourself.

## Scientific Critic

Scientific Critic: **Critique of Principal Investigator's Revised Answer**

1. **Adherence to Agenda:**
   - The revised answer adheres well to the agenda by providing a detailed and execution-ready plan. It includes a primary experiment matrix, required controls, validation runs, an assay plan, advancement criteria, and a pentose branch with full parameters. The plan is comprehensive and addresses the need for a complete wet-lab plan rather than an abstract discussion.

2. **Round Objective:**
   - The round objective is clearly stated and aligns with the agenda's goal. However, it could benefit from a more explicit connection to the project's overarching goals, particularly how the results will guide future rounds. Consider adding a brief statement on how the outcomes will influence the project's long-term strategy.

3. **Fixed and Scanned Variables:**
   - The justification for fixed and scanned variables is a positive addition. However, the explanation for excluding certain variables (e.g., wet-mode expansion, broad pH sweep) could be expanded to include any potential limitations this might impose on the study's findings.

4. **Final Experiment Matrix:**
   - The experiment matrix is well-structured and includes all necessary details. The addition of minimal assay execution detail is helpful. However, consider providing more specific examples of how the assay results will be interpreted, particularly in terms of quantifying reduction and assessing aggregation.

5. **Pentose Branch Design:**
   - The pentose branch design is clear and operational. The explicit operational pentose competitiveness rule is a strong addition. However, consider providing more detail on how the results will be compared to the hexose branches to ensure a fair assessment.

6. **Experiment-to-Question Mapping:**
   - The mapping effectively links experimental runs to specific research questions. However, it could be improved by providing more detail on the specific metrics that will be used to evaluate success for each question.

7. **Assay Plan:**
   - The assay plan is thorough and includes necessary execution details. However, consider specifying any potential sources of variability in the assays and how they will be controlled or accounted for in the analysis.

8. **Go / No-Go Criteria:**
   - The criteria are well-defined and include quantitative thresholds. However, consider providing more detail on how borderline cases will be handled, particularly if they fall close to the thresholds.

9. **Advancement Logic:**
   - The advancement logic is clear and includes contingency plans for ambiguous outcomes. However, consider providing more detail on how the results will be communicated to the wet-lab team and how feedback will be incorporated into future rounds.

10. **Final Recommendation to Wet Lab:**
    - The recommendation is clear and actionable. However, consider providing more detail on the communication plan with the wet-lab team to ensure smooth execution and feedback integration.

**Suggestions for Improvement:**
- Add a brief statement on how the round's outcomes will influence the project's long-term strategy.
- Expand on the potential limitations of excluding certain variables and how they might impact the study's findings.
- Provide more specific examples of how assay results will be interpreted, particularly in terms of quantifying reduction and assessing aggregation.
- Specify potential sources of variability in the assays and how they will be controlled.
- Provide more detail on handling borderline cases and how results will be communicated to the wet-lab team.

Overall, the Principal Investigator's revised answer is well-structured and comprehensive, but it would benefit from additional detail and clarity in certain areas to fully meet the agenda's requirements.
Scientific Critic: **Critique of Principal Investigator's Revised Answer**

1. **Adherence to Agenda:**
   - The revised answer adheres well to the agenda by providing a detailed and execution-ready plan. It includes a primary experiment matrix, required controls, validation runs, an assay plan, advancement criteria, and a pentose branch with full parameters. The plan is comprehensive and addresses the need for a complete wet-lab plan rather than an abstract discussion.

2. **Round Objective:**
   - The round objective is clearly stated and aligns with the agenda's goal. However, it could benefit from a more explicit connection to the project's overarching goals, particularly how the results will guide future rounds. Consider adding a brief statement on how the outcomes will influence the project's long-term strategy.

3. **Fixed and Scanned Variables:**
   - The justification for fixed and scanned variables is a positive addition. However, the explanation for excluding certain variables (e.g., wet-mode expansion, broad pH sweep) could be expanded to include any potential limitations this might impose on the study's findings.

4. **Final Experiment Matrix:**
   - The experiment matrix is well-structured and includes all necessary details. The addition of minimal assay execution detail is helpful. However, consider providing more specific examples of how the assay results will be interpreted, particularly in terms of quantifying reduction and assessing aggregation.

5. **Pentose Branch Design:**
   - The pentose branch design is clear and operational. The explicit operational pentose competitiveness rule is a strong addition. However, consider providing more detail on how the results will be compared to the hexose branches to ensure a fair assessment.

6. **Experiment-to-Question Mapping:**
   - The mapping effectively links experimental runs to specific research questions. However, it could be improved by providing more detail on the specific metrics that will be used to evaluate success for each question.

7. **Assay Plan:**
   - The assay plan is thorough and includes necessary execution details. However, consider specifying any potential sources of variability in the assays and how they will be controlled or accounted for in the analysis.

8. **Go / No-Go Criteria:**
   - The criteria are well-defined and include quantitative thresholds. However, consider providing more detail on how borderline cases will be handled, particularly if they fall close to the thresholds.

9. **Advancement Logic:**
   - The advancement logic is clear and includes contingency plans for ambiguous outcomes. However, consider providing more detail on how the results will be communicated to the wet-lab team and how feedback will be incorporated into future rounds.

10. **Final Recommendation to Wet Lab:**
    - The recommendation is clear and actionable. However, consider providing more detail on the communication plan with the wet-lab team to ensure smooth execution and feedback integration.

**Suggestions for Improvement:**
- Add a brief statement on how the round's outcomes will influence the project's long-term strategy.
- Expand on the potential limitations of excluding certain variables and how they might impact the study's findings.
- Provide more specific examples of how assay results will be interpreted, particularly in terms of quantifying reduction and assessing aggregation.
- Specify potential sources of variability in the assays and how they will be controlled.
- Provide more detail on handling borderline cases and how results will be communicated to the wet-lab team.

Overall, the Principal Investigator's revised answer is well-structured and comprehensive, but it would benefit from additional detail and clarity in certain areas to fully meet the agenda's requirements.

## User

Principal Investigator, please modify your answer to address Scientific Critic's most recent feedback. Remember that your ultimate goal is to make improvements that better address the agenda.

## Principal Investigator

Principal Investigator: I will improve the plan again, but I am going to be selective. The critic’s latest feedback is partly valid and partly drifting toward nonessential elaboration. I will add only the pieces that make the plan more executable, more interpretable, or more tightly aligned to the agenda.

I am **keeping the same preferred 24-run matrix**. The main needed changes are:

1. make the **project-level purpose and next-round linkage** more explicit,
2. state the **limitations of what this round does not test** so the wet lab and analysis team do not over-interpret the results,
3. make the **comparison of pentose branches to hexose branches more explicit and fair**,
4. make **assay variability controls** explicit,
5. define how **borderline cases** are handled,
6. and add a concise **results communication / decision workflow** for after data return.

I am not adding new experimental branches. That would make the plan larger without improving the core agenda fit.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary processing severity.

This round must produce a directly actionable decision on:

1. the ranking of the required primary donors under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its extra burden at **4 h**
3. whether **4 h** is justified, or whether selected branches should be carried forward at **3 h**
4. whether ultrasound is **necessary**, **practically enabling**, or **marginal**
5. whether a **pentose donor** should advance at all
6. and if so, whether **arabinose** or **ribose** should advance, and at **which restrained practical condition**

## Project-level purpose
This round is not just a screen for numerical reduction. Its purpose is to define the **best practical next-step condition region** for β-LG glycation by integrating:

- efficacy in the primary allergenicity readout,
- donor-specific effect beyond heated no-sugar controls,
- extractability / soluble recovery,
- aggregation behavior,
- and overprocessing burden.

## How this round determines the next round
This round directly sets the next-round path:

- **one clear hexose winner** -> focused refinement around that donor
- **two close hexose branches** -> carry both into the next refinement round
- **qualified pentose** -> validate and, only if confirmed, carry as an advanced comparator branch
- **no qualified pentose** -> terminate pentose advancement for the mainline program
- **4 h not justified** -> next round becomes **3 h-centered**
- **55 C sufficient** -> next round collapses toward the lower-temperature region

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

## Why these are fixed
These variables are fixed because this round is a **matched donor decision experiment**, not a broad optimization campaign. Expanding wet mode, pH, aw, donor ratio, or pretreatment family in the same round would weaken interpretability and reduce our ability to answer the required donor, time, temperature, ultrasound, and pentose questions cleanly.

## Important scope limitations
Because these variables are fixed, this round does **not** answer:
- whether a different **aw** would improve performance,
- whether a different **protein:sugar ratio** would rescue weak donors,
- whether **wet mode** outperforms dry mode,
- whether alternative **pretreatment families** outperform ultrasound,
- or whether pH control would materially change donor ranking.

That is intentional. Those questions remain for later only if this round yields a sufficiently clear donor/condition direction.

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

## Why these are scanned
These are the minimum variables needed to answer the agenda:
- donor ranking,
- practical temperature choice,
- whether 4 h earns its place,
- ultrasound role,
- and pentose advancement.

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab workflow

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

## Minimal assay execution detail required for interpretability

### Primary assay variability control
- run conditions in **balanced assay batches**
- include in every batch:
  - untreated β-LG baseline
  - matched heated no-sugar controls
  - the same internal reference sample if used routinely
- avoid placing one donor class disproportionately on a single plate or batch
- analyze technical duplicates together and flag gross within-pair inconsistency for repeat review

### Recovery assay variability control
- use one fixed extraction SOP and one fixed protein quantification method across all runs
- process matched comparison runs in the same extraction batch where practical

### SDS-PAGE variability control
- use the lab’s standard **reducing SDS-PAGE** workflow on the **soluble fraction**
- use the same gel system, marker, and batch controls across all runs
- compare banding patterns only within matched gel batches or against common control lanes

### Orthogonal immunology requirement
- use the lab’s standard alternate binding-format or inhibition-format assay
- it must be less sensitive to the same presentation artifact as the primary assay

## Preferred primary matrix: 24-run protected design

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Explicit fair-comparison rule versus hexose branches
Pentoses will **not** be compared to the most severe hexose condition by default. They will be compared in this order:

1. **primary comparator:** the better of **R15** and **R16**  
   - because these are the matched **55 C, 3 h practical anchors**
2. **secondary comparator:** the best advancing hexose branch overall  
   - to assess whether a pentose is merely acceptable or truly competitive
3. **control comparator:** the matched heated no-sugar control  
   - to verify that the apparent effect is donor-specific

This creates a fairer comparison than forcing pentoses to beat a harsher hexose branch first.

## Explicit operational pentose competitiveness rule
A pentose branch is considered **competitive** only if all are true:

1. it is a **screen hit**
2. it is within **10 percentage points** of the better of **R15** and **R16**
3. it is not clearly worse than the leading validated hexose branch in:
   - extractability
   - aggregation pattern
   - browning burden
4. it passes **orthogonal confirmation** before promotion
5. for ribose specifically, the added chemistry-risk readouts in **V03** must remain acceptable in direction

## Why this pentose design remains preferred
I am keeping the restrained **55 C, 2–3 h** pentose branch because it tests whether a pentose can succeed under the same practical discipline we want for the main program. A pentose that only looks good under harsher chemistry is not the right mainline advancement candidate.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

**Quantitative readout used:**  
primary reduction, delta vs matched no-sugar control, extractability, aggregation pattern, browning

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at 55 C, 4 h?

**Quantitative readout used:**  
difference in reduction, change in efficacy band, change in extractability, change in interpretability burden

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

**Quantitative readout used:**  
difference in reduction between 2 h, 3 h, and 4 h, judged against the **<10-point marginal-gain rule**

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

**Quantitative readout used:**  
screen-hit status, closeness to **R15/R16**, extractability, aggregation, browning, orthogonal confirmation if triggered

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

**Quantitative readout used:**  
matched donor-minus-control improvement within each time/temperature context

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

**Quantitative readout used:**  
repeat effect direction, orthogonal concordance, repeat recovery, repeat aggregation profile

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`
   - run in technical duplicate
   - include untreated β-LG baseline in every assay batch
   - include matched heated no-sugar controls in every batch

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG baseline
   - compare against matched heated no-sugar control

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on the soluble fraction
   - use the same gel system, marker, and batch control across all runs

4. **Appearance / reconstitution notes**
   - visible insolubility
   - precipitation
   - reconstitution difficulty
   - abnormal viscosity or clumping if observed

5. **Browning / overprocessing proxy**
   - visual browning score on 0–3 scale
   - optional simple absorbance/color index if routine in the lab

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## How assay results will be interpreted
- **primary reduction** answers whether recognition decreased
- **delta vs matched no-sugar control** answers whether the decrease is donor-specific rather than heating-only
- **recovery** answers whether the sample remains sufficiently extractable to trust the signal
- **SDS-PAGE** answers whether signal loss is likely dominated by aggregation or monomer disappearance from the soluble fraction
- **browning** acts as a low-burden overprocessing warning signal

No branch is promoted on primary reduction alone.

## Borderline-case handling
Borderline runs are handled as follows:

### Borderline efficacy
- **65–69% reduction** with clean interpretability is **not** a screen hit
- do not advance automatically
- may remain noted only if they are unusually mild and all stronger runs fail interpretability

### Borderline extractability
- **50–59%** extractability is caution zone
- cannot advance directly unless:
  - orthogonal confirmation supports the effect,
  - aggregation is not dominant,
  - and no cleaner comparable branch exists

### Borderline close-call ranking
- branches within **<10 points** of each other are considered practically close
- keep more than one branch active only if they differ on burden, donor class, or interpretability

## Trigger rule for validation entry
Send to validation if:
- it is one of the **top 2 hexose branches** meeting screen-hit criteria
- or it is the **top pentose branch** meeting pentose qualification criteria

Additional discretionary escalation is allowed if:
- a run reaches **>=80% reduction**
- or is within **<10 points** of the overall leader
- or a 3 h / no-ultrasound run materially changes practical ranking

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = caution; not directly promotable without stronger support
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:

1. **marked monomer loss in soluble fraction**  
   operationally: visually clear reduction of monomer band intensity relative to matched heated no-sugar control in the same gel batch

2. **strong high-MW smear / aggregated material**  
   operationally: obvious upper-region smear or retained high-MW material stronger than matched no-sugar control

3. **extractability <60%**

4. **signal loss mainly explained by disappearance from soluble fraction**

5. **orthogonal inconsistency when tested**

This remains partly expert-judgment based, but the rule is explicit: **2 or more criteria = artifact flag**.

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Practical time rule
Do **not** prefer the later timepoint if the added hour gives **<10 percentage points** additional reduction, unless the later condition changes the run into a meaningfully better practical category without adding interpretability burden.

## Ultrasound classification rule
At matched 55 C, 4 h conditions:
- **necessary** = removing ultrasound causes loss of screen-hit status or a drop of **>=10 percentage points** plus a worse practical category
- **practically enabling** = removing ultrasound worsens reduction by **5–9 points** or worsens interpretability burden enough to change preference
- **marginally beneficial** = difference is **<5 points** and practical ranking is unchanged

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be within **10 points** of the better of **R15** or **R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Rank by:
1. primary reduction
2. delta vs matched no-sugar control
3. extractability
4. aggregation/browning burden

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

Any run with an artifact flag is **not promotable**.

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose

Decision rule:
- if 3 h is within **<10 points** of 4 h and stays in the same efficacy band, prefer **3 h**
- if 4 h gives **>=10 points** extra reduction and no major interpretability penalty, keep **4 h**

For pentoses:
- compare **R17 vs R18** and **R19 vs R20**
- prefer **2 h** if 3 h gain is **<10 points**
- prefer **3 h** only if it gives a meaningful gain without worsening interpretability

## Step 4 — Evaluate temperature trade-off
Compare donor-matched 55 C vs 60 C at 4 h:
- R01 vs R05
- R02 vs R06
- R03 vs R07
- R04 vs R08

Decision rule:
- prefer **55 C** if 60 C gives **<10 points** additional reduction
- prefer **60 C** only if the gain is meaningful and does not worsen interpretability enough to offset the benefit

## Step 5 — Evaluate ultrasound dependence
Compare:
- R09 vs R01
- R10 vs R02
- R11 vs R03
- R12 vs R04

Classify ultrasound as:
- necessary
- practically enabling
- marginally beneficial

using the explicit thresholds in Section 8.

## Step 6 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 7 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is within **10 points** of the better of **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 8 — Contingency logic for ambiguous outcomes
- if no sugar-containing branch achieves screen-hit criteria:
  - do not force advancement; re-evaluate assay sensitivity and dry-state severity assumptions
- if all top branches fail interpretability:
  - do not promote numerically strong artifacts; redesign next round around milder conditions
- if multiple branches cluster within **<10 points** and all are interpretable:
  - carry forward more than one branch only if they differ in practical burden or donor class decision value

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

## Specific execution instructions for run-sheet generation
The wet-lab team should now:

1. generate sample labels for **R01–R24**
2. assign **2 independent process replicate IDs** to each matrix run
3. reserve material and schedule slots for **V01–V03**
4. batch assay plates so that each plate contains:
   - untreated β-LG baseline
   - matched no-sugar controls
   - a balanced mix of donor conditions
5. retain enough soluble fraction from every run for:
   - recovery measurement
   - SDS-PAGE
   - repeat testing if needed

## Results communication and decision workflow
After data return:

1. **wet-lab team** delivers the locked result table for R01–R24 with assay QC notes
2. **analysis team** applies the pre-registered rules:
   - screen-hit filter
   - interpretability filter
   - time rule
   - temperature rule
   - ultrasound classification
   - pentose competitiveness rule
3. **decision meeting 1**:
   - rank hexose branches
   - determine whether 55 C is sufficient
   - determine whether 4 h earns its place
   - determine whether any pentose qualifies for validation
4. **validation runs V01–V03** are executed if triggered
5. **decision meeting 2**:
   - finalize donor advancement
   - finalize whether pentose remains in the program
   - lock next-round scope

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

This is now my corrected preferred execution-ready plan.
Principal Investigator: I will improve the plan again, but I am going to be selective. The critic’s latest feedback is partly valid and partly drifting toward nonessential elaboration. I will add only the pieces that make the plan more executable, more interpretable, or more tightly aligned to the agenda.

I am **keeping the same preferred 24-run matrix**. The main needed changes are:

1. make the **project-level purpose and next-round linkage** more explicit,
2. state the **limitations of what this round does not test** so the wet lab and analysis team do not over-interpret the results,
3. make the **comparison of pentose branches to hexose branches more explicit and fair**,
4. make **assay variability controls** explicit,
5. define how **borderline cases** are handled,
6. and add a concise **results communication / decision workflow** for after data return.

I am not adding new experimental branches. That would make the plan larger without improving the core agenda fit.

---

# 1. Round objective

Execute **one next-round dry-state wet-lab program** to identify practical glycation conditions that reduce **β-lactoglobulin variant A** allergenicity while preserving interpretability and avoiding unnecessary processing severity.

This round must produce a directly actionable decision on:

1. the ranking of the required primary donors under a matched dry-state bridge:
   - **lactose**
   - **glucose**
   - **galactose**
   - **mannose**
2. whether **55 C** is sufficient or whether **60 C** earns its extra burden at **4 h**
3. whether **4 h** is justified, or whether selected branches should be carried forward at **3 h**
4. whether ultrasound is **necessary**, **practically enabling**, or **marginal**
5. whether a **pentose donor** should advance at all
6. and if so, whether **arabinose** or **ribose** should advance, and at **which restrained practical condition**

## Project-level purpose
This round is not just a screen for numerical reduction. Its purpose is to define the **best practical next-step condition region** for β-LG glycation by integrating:

- efficacy in the primary allergenicity readout,
- donor-specific effect beyond heated no-sugar controls,
- extractability / soluble recovery,
- aggregation behavior,
- and overprocessing burden.

## How this round determines the next round
This round directly sets the next-round path:

- **one clear hexose winner** -> focused refinement around that donor
- **two close hexose branches** -> carry both into the next refinement round
- **qualified pentose** -> validate and, only if confirmed, carry as an advanced comparator branch
- **no qualified pentose** -> terminate pentose advancement for the mainline program
- **4 h not justified** -> next round becomes **3 h-centered**
- **55 C sufficient** -> next round collapses toward the lower-temperature region

---

# 2. Fixed variables

These are fixed across the round unless explicitly varied in the matrix.

- **protein:** β-lactoglobulin variant A
- **mode:** dry-state glycation
- **moisture-control condition:** **aw 0.79**
- **protein:sugar ratio:** **1:2 (w/w)** for all sugar-containing runs
- **absolute handling example:** **100 mg β-LG + 200 mg donor per reaction unit**
- **dry-state handling:** same validated pre-equilibration, sealed-vessel, aw-controlled workflow as prior dry runs
- **reaction platform:** controlled dry incubation
- **temperature tolerance during incubation:** **±0.5 C**
- **ultrasound main-arm settings:**
  - probe sonication
  - **20 kHz**
  - **30% amplitude**
  - **5 s on / 5 s off**
  - **10 min total sonication**
  - maintain sample temperature **<=25 C**
- **no-ultrasound condition:** identical handling except ultrasound omitted
- **post-reaction handling:** immediate endpoint removal, prompt cooling, standardized extraction/reconstitution timeline
- **primary assay platform:** same assay family used for historical `reduction_pct_reported`
- **screening replicate count:** **n = 2 independent process replicates per matrix run**
- **primary assay technical replication:** technical duplicate
- **validation reruns:** **n = 3 independent process replicates**
- **visual browning score for all runs:**
  - 0 = none
  - 1 = slight
  - 2 = moderate
  - 3 = strong

## Why these are fixed
These variables are fixed because this round is a **matched donor decision experiment**, not a broad optimization campaign. Expanding wet mode, pH, aw, donor ratio, or pretreatment family in the same round would weaken interpretability and reduce our ability to answer the required donor, time, temperature, ultrasound, and pentose questions cleanly.

## Important scope limitations
Because these variables are fixed, this round does **not** answer:
- whether a different **aw** would improve performance,
- whether a different **protein:sugar ratio** would rescue weak donors,
- whether **wet mode** outperforms dry mode,
- whether alternative **pretreatment families** outperform ultrasound,
- or whether pH control would materially change donor ranking.

That is intentional. Those questions remain for later only if this round yields a sufficiently clear donor/condition direction.

Not scanned this round:
- wet-mode expansion
- broad pH sweep
- donor-ratio sweep
- alternative aw levels
- alternative pretreatment families

---

# 3. Scanned variables

- **donor identity**
  - lactose
  - glucose
  - galactose
  - mannose
  - arabinose
  - ribose
  - no-sugar control
- **temperature**
  - 55 C
  - 60 C
- **time**
  - 2 h
  - 3 h
  - 4 h
- **ultrasound status**
  - ultrasound
  - no ultrasound

## Why these are scanned
These are the minimum variables needed to answer the agenda:
- donor ranking,
- practical temperature choice,
- whether 4 h earns its place,
- ultrasound role,
- and pentose advancement.

---

# 4. Final experiment matrix

## Assay package definitions

- **S1 = screening package**
  1. primary allergenicity assay
  2. extractable / soluble β-LG recovery
  3. reducing SDS-PAGE of soluble fraction
  4. appearance / reconstitution notes
  5. visual browning score
  6. simple browning proxy if routine in lab workflow

- **V = validation package**
  1. repeat primary allergenicity assay
  2. orthogonal immunological assay
  3. repeat extractable / soluble β-LG recovery
  4. stronger aggregation assessment on soluble fraction
  5. repeat browning / overprocessing proxy
  6. for promoted pentose branch only:
     - fluorescent AGE trend screen
     - preferably OPA / free amino group trend

## Minimal assay execution detail required for interpretability

### Primary assay variability control
- run conditions in **balanced assay batches**
- include in every batch:
  - untreated β-LG baseline
  - matched heated no-sugar controls
  - the same internal reference sample if used routinely
- avoid placing one donor class disproportionately on a single plate or batch
- analyze technical duplicates together and flag gross within-pair inconsistency for repeat review

### Recovery assay variability control
- use one fixed extraction SOP and one fixed protein quantification method across all runs
- process matched comparison runs in the same extraction batch where practical

### SDS-PAGE variability control
- use the lab’s standard **reducing SDS-PAGE** workflow on the **soluble fraction**
- use the same gel system, marker, and batch controls across all runs
- compare banding patterns only within matched gel batches or against common control lanes

### Orthogonal immunology requirement
- use the lab’s standard alternate binding-format or inhibition-format assay
- it must be less sensitive to the same presentation artifact as the primary assay

## Preferred primary matrix: 24-run protected design

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| R01 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | ultrasound; probe 20 kHz, 30% amplitude, 5 s on/5 s off, 10 min, <=25 C | no | no | 2 | S1 |
| R02 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R03 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R04 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R05 | hexose_bridge | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R06 | hexose_bridge | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R07 | hexose_bridge | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R08 | hexose_bridge | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | no | no | 2 | S1 |
| R09 | hexose_noUS | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R10 | hexose_noUS | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R11 | hexose_noUS | galactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R12 | hexose_noUS | mannose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 4 h | no ultrasound | no | yes | 2 | S1 |
| R13 | benchmark_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R14 | benchmark_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 60 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R15 | practical_anchor | lactose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R16 | practical_anchor | glucose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R17 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R18 | pentose_branch | arabinose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R19 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | no | no | 2 | S1 |
| R20 | pentose_branch | ribose | 1:2 w/w; 100 mg β-LG + 200 mg donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | no | no | 2 | S1 |
| R21 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 2 h | same ultrasound settings | yes | no | 2 | S1 |
| R22 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 3 h | same ultrasound settings | yes | no | 2 | S1 |
| R23 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 55 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |
| R24 | heated_no_sugar_control | none | no donor | dry | aw 0.79 | 60 C | 4 h | same ultrasound settings | yes | no | 2 | S1 |

## Pre-specified validation reruns

| run_id | run_role | donor | protein:sugar ratio / donor amount | mode | moisture-control condition | temperature | time | pretreatment and parameters | no-sugar control | no-ultrasound control | replicate count | assay package |
|---|---|---|---|---|---|---:|---:|---|---|---|---:|---|
| V01 | validation_top_hexose_1 | top hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V02 | validation_top_hexose_2 | second hexose donor/condition from screen | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |
| V03 | validation_top_pentose_if_qualified | top pentose donor/condition if qualified | 1:2 w/w | dry | aw 0.79 | matched winning condition | matched winning time | matched winning pretreatment | no | matched | 3 | V |

If no pentose qualifies, **V03 is not run**.

---

# 5. Pentose branch design

## Pentose branch runs

- **R17** arabinose, 55 C, 2 h, ultrasound
- **R18** arabinose, 55 C, 3 h, ultrasound
- **R19** ribose, 55 C, 2 h, ultrasound
- **R20** ribose, 55 C, 3 h, ultrasound

## Pentose decision question

The pentose branch is designed to answer:

> Under a restrained practical dry-state window, does either pentose donor produce a sufficiently strong and interpretable allergenicity-reduction signal to justify advancement in this project, and if so, which donor and at what time?

## Explicit fair-comparison rule versus hexose branches
Pentoses will **not** be compared to the most severe hexose condition by default. They will be compared in this order:

1. **primary comparator:** the better of **R15** and **R16**  
   - because these are the matched **55 C, 3 h practical anchors**
2. **secondary comparator:** the best advancing hexose branch overall  
   - to assess whether a pentose is merely acceptable or truly competitive
3. **control comparator:** the matched heated no-sugar control  
   - to verify that the apparent effect is donor-specific

This creates a fairer comparison than forcing pentoses to beat a harsher hexose branch first.

## Explicit operational pentose competitiveness rule
A pentose branch is considered **competitive** only if all are true:

1. it is a **screen hit**
2. it is within **10 percentage points** of the better of **R15** and **R16**
3. it is not clearly worse than the leading validated hexose branch in:
   - extractability
   - aggregation pattern
   - browning burden
4. it passes **orthogonal confirmation** before promotion
5. for ribose specifically, the added chemistry-risk readouts in **V03** must remain acceptable in direction

## Why this pentose design remains preferred
I am keeping the restrained **55 C, 2–3 h** pentose branch because it tests whether a pentose can succeed under the same practical discipline we want for the main program. A pentose that only looks good under harsher chemistry is not the right mainline advancement candidate.

---

# 6. Experiment-to-question mapping

### Block 1: R01–R08
**Question answered:**  
What is the matched donor ranking among lactose, glucose, galactose, and mannose at 4 h, and is 55 C or 60 C preferable?

**Quantitative readout used:**  
primary reduction, delta vs matched no-sugar control, extractability, aggregation pattern, browning

### Block 2: R09–R12
**Question answered:**  
Is ultrasound necessary, practically enabling, or only marginally beneficial for the four-donor hexose bridge at 55 C, 4 h?

**Quantitative readout used:**  
difference in reduction, change in efficacy band, change in extractability, change in interpretability burden

### Block 3: R13–R16
**Question answered:**  
Does 4 h earn its place relative to shorter benchmark/practical anchors, and what are the correct practical comparators for pentose interpretation?

**Quantitative readout used:**  
difference in reduction between 2 h, 3 h, and 4 h, judged against the **<10-point marginal-gain rule**

### Block 4: R17–R20
**Question answered:**  
Should arabinose or ribose be advanced at all, and under which restrained practical condition if so?

**Quantitative readout used:**  
screen-hit status, closeness to **R15/R16**, extractability, aggregation, browning, orthogonal confirmation if triggered

### Block 5: R21–R24
**Question answered:**  
How much of the observed signal reduction is donor-specific rather than attributable to heating / ultrasound alone?

**Quantitative readout used:**  
matched donor-minus-control improvement within each time/temperature context

### Validation block: V01–V03
**Question answered:**  
Do the leading branches remain strong and interpretable under confirmation-level assessment, including orthogonal immunological evidence?

**Quantitative readout used:**  
repeat effect direction, orthogonal concordance, repeat recovery, repeat aggregation profile

---

# 7. Assay plan

## Screening assay package: S1
Apply to **R01–R24**.

1. **Primary allergenicity assay**
   - same platform used for historical `reduction_pct_reported`
   - run in technical duplicate
   - include untreated β-LG baseline in every assay batch
   - include matched heated no-sugar controls in every batch

2. **Extractable β-LG / soluble recovery**
   - same extraction workflow across all runs
   - normalize to untreated β-LG baseline
   - compare against matched heated no-sugar control

3. **Basic aggregation / size-state assessment**
   - reducing SDS-PAGE on the soluble fraction
   - use the same gel system, marker, and batch control across all runs

4. **Appearance / reconstitution notes**
   - visible insolubility
   - precipitation
   - reconstitution difficulty
   - abnormal viscosity or clumping if observed

5. **Browning / overprocessing proxy**
   - visual browning score on 0–3 scale
   - optional simple absorbance/color index if routine in the lab

## Validation assay package: V
Apply to **V01–V03**.

1. repeat primary allergenicity assay
2. orthogonal immunological assay
3. repeat extractable β-LG / soluble recovery
4. stronger aggregation assessment on soluble fraction
5. repeat browning / overprocessing proxy
6. for promoted pentose branch:
   - fluorescent AGE trend screen
   - preferably OPA/free amino group trend

## How assay results will be interpreted
- **primary reduction** answers whether recognition decreased
- **delta vs matched no-sugar control** answers whether the decrease is donor-specific rather than heating-only
- **recovery** answers whether the sample remains sufficiently extractable to trust the signal
- **SDS-PAGE** answers whether signal loss is likely dominated by aggregation or monomer disappearance from the soluble fraction
- **browning** acts as a low-burden overprocessing warning signal

No branch is promoted on primary reduction alone.

## Borderline-case handling
Borderline runs are handled as follows:

### Borderline efficacy
- **65–69% reduction** with clean interpretability is **not** a screen hit
- do not advance automatically
- may remain noted only if they are unusually mild and all stronger runs fail interpretability

### Borderline extractability
- **50–59%** extractability is caution zone
- cannot advance directly unless:
  - orthogonal confirmation supports the effect,
  - aggregation is not dominant,
  - and no cleaner comparable branch exists

### Borderline close-call ranking
- branches within **<10 points** of each other are considered practically close
- keep more than one branch active only if they differ on burden, donor class, or interpretability

## Trigger rule for validation entry
Send to validation if:
- it is one of the **top 2 hexose branches** meeting screen-hit criteria
- or it is the **top pentose branch** meeting pentose qualification criteria

Additional discretionary escalation is allowed if:
- a run reaches **>=80% reduction**
- or is within **<10 points** of the overall leader
- or a 3 h / no-ultrasound run materially changes practical ranking

---

# 8. Go / No-Go criteria

## Screen hit
A run is a **screen hit** only if all are true:

1. **Primary allergenicity reduction >=70%**
2. **At least 15 percentage points above nearest matched heated no-sugar control**
3. **Extractability >=60%** of untreated β-LG baseline
4. **No aggregation-dominant artifact flag**

## Borderline zone
- extractability **50–59%** = caution; not directly promotable without stronger support
- extractability **<50%** = fail for advancement

## Preferred extractability for promoted pentose branches
- **>=70%**

## Aggregation-dominant artifact flag
Flag if **2 or more** are present:

1. **marked monomer loss in soluble fraction**  
   operationally: visually clear reduction of monomer band intensity relative to matched heated no-sugar control in the same gel batch

2. **strong high-MW smear / aggregated material**  
   operationally: obvious upper-region smear or retained high-MW material stronger than matched no-sugar control

3. **extractability <60%**

4. **signal loss mainly explained by disappearance from soluble fraction**

5. **orthogonal inconsistency when tested**

This remains partly expert-judgment based, but the rule is explicit: **2 or more criteria = artifact flag**.

## Strong provisional candidate
A run is a strong provisional candidate if it is a screen hit and:
- **>=80% reduction**, or
- **70–79% reduction** with a meaningful burden advantage:
  - shorter time
  - lower temperature
  - or lower ultrasound dependence

## Practical time rule
Do **not** prefer the later timepoint if the added hour gives **<10 percentage points** additional reduction, unless the later condition changes the run into a meaningfully better practical category without adding interpretability burden.

## Ultrasound classification rule
At matched 55 C, 4 h conditions:
- **necessary** = removing ultrasound causes loss of screen-hit status or a drop of **>=10 percentage points** plus a worse practical category
- **practically enabling** = removing ultrasound worsens reduction by **5–9 points** or worsens interpretability burden enough to change preference
- **marginally beneficial** = difference is **<5 points** and practical ranking is unchanged

## Pentose-specific stricter bar
For a pentose to be promoted:
- best run must be a screen hit
- preferred extractability should be **>=70%**
- it must be within **10 points** of the better of **R15** or **R16**
- it must not be clearly worse than the leading hexose in aggregation / browning / chemistry-risk burden
- it must pass orthogonal confirmation before promotion

## No-go
No-go for advancement if any apply:
- reduction <70%
- sugar-specific gain <15 points over matched no-sugar control
- extractability <50%
- aggregation-dominant artifact
- failed orthogonal confirmation for promoted branch
- pentose branch is only numerically strong but materially dirtier than leading hexose branch

---

# 9. Advancement logic

## Step 1 — Rank the matched 4 h hexose bridge
Primary ranking set:
- **R01–R08**

Rank by:
1. primary reduction
2. delta vs matched no-sugar control
3. extractability
4. aggregation/browning burden

## Step 2 — Apply interpretability filter
Before any branch is considered practical:
- review recovery
- SDS-PAGE aggregation pattern
- reconstitution behavior
- browning
- donor-specific gain relative to matched no-sugar control

Any run with an artifact flag is **not promotable**.

## Step 3 — Evaluate whether 4 h earns its place
Compare:
- **R15 vs R01** for lactose
- **R16 vs R02** for glucose

Decision rule:
- if 3 h is within **<10 points** of 4 h and stays in the same efficacy band, prefer **3 h**
- if 4 h gives **>=10 points** extra reduction and no major interpretability penalty, keep **4 h**

For pentoses:
- compare **R17 vs R18** and **R19 vs R20**
- prefer **2 h** if 3 h gain is **<10 points**
- prefer **3 h** only if it gives a meaningful gain without worsening interpretability

## Step 4 — Evaluate temperature trade-off
Compare donor-matched 55 C vs 60 C at 4 h:
- R01 vs R05
- R02 vs R06
- R03 vs R07
- R04 vs R08

Decision rule:
- prefer **55 C** if 60 C gives **<10 points** additional reduction
- prefer **60 C** only if the gain is meaningful and does not worsen interpretability enough to offset the benefit

## Step 5 — Evaluate ultrasound dependence
Compare:
- R09 vs R01
- R10 vs R02
- R11 vs R03
- R12 vs R04

Classify ultrasound as:
- necessary
- practically enabling
- marginally beneficial

using the explicit thresholds in Section 8.

## Step 6 — Hexose advancement
Automatically send to validation:
- the **top 2 hexose branches** that meet screen-hit criteria and are not interpretation-flagged

Advance only one hexose donor beyond this if:
- best branch is **>=10 percentage points** ahead of next-best matched hexose branch
- and does not carry an interpretability penalty

Otherwise keep two hexose donors active.

## Step 7 — Pentose advancement
Automatically send **one pentose branch** to validation only if:
- at least one pentose run is a formal screen hit
- the best pentose run is within **10 points** of the better of **R15/R16**
- and it is not clearly worse than the leading hexose branch in interpretability / chemistry burden

If no pentose qualifies, no pentose branch advances.

## Step 8 — Contingency logic for ambiguous outcomes
- if no sugar-containing branch achieves screen-hit criteria:
  - do not force advancement; re-evaluate assay sensitivity and dry-state severity assumptions
- if all top branches fail interpretability:
  - do not promote numerically strong artifacts; redesign next round around milder conditions
- if multiple branches cluster within **<10 points** and all are interpretable:
  - carry forward more than one branch only if they differ in practical burden or donor class decision value

---

# 10. Final recommendation to wet lab

Proceed with the **24-run protected dry-state matrix R01–R24** exactly as listed above, using:

- **dry-state glycation**
- **aw 0.79**
- **β-LG : donor = 1:2 (w/w)**
- **ultrasound: probe 20 kHz, 30% amplitude, 5 s on / 5 s off, 10 min, <=25 C**
- **hexose bridge at 55/60 C, 4 h**
- **hexose no-ultrasound comparison at 55 C, 4 h**
- **benchmark anchors at 60 C, 2 h**
- **practical anchors at 55 C, 3 h**
- **pentose branch at 55 C, 2–3 h**
- **four heated no-sugar controls**
- **2 independent process replicates per matrix run**
- **technical duplicate for the primary assay**
- **validation reruns V01–V03 reserved in advance**

## Specific execution instructions for run-sheet generation
The wet-lab team should now:

1. generate sample labels for **R01–R24**
2. assign **2 independent process replicate IDs** to each matrix run
3. reserve material and schedule slots for **V01–V03**
4. batch assay plates so that each plate contains:
   - untreated β-LG baseline
   - matched no-sugar controls
   - a balanced mix of donor conditions
5. retain enough soluble fraction from every run for:
   - recovery measurement
   - SDS-PAGE
   - repeat testing if needed

## Results communication and decision workflow
After data return:

1. **wet-lab team** delivers the locked result table for R01–R24 with assay QC notes
2. **analysis team** applies the pre-registered rules:
   - screen-hit filter
   - interpretability filter
   - time rule
   - temperature rule
   - ultrasound classification
   - pentose competitiveness rule
3. **decision meeting 1**:
   - rank hexose branches
   - determine whether 55 C is sufficient
   - determine whether 4 h earns its place
   - determine whether any pentose qualifies for validation
4. **validation runs V01–V03** are executed if triggered
5. **decision meeting 2**:
   - finalize donor advancement
   - finalize whether pentose remains in the program
   - lock next-round scope

Do **not** expand in this round into:
- wet mode
- pH sweep
- donor-ratio sweep
- additional aw points
- alternative pretreatments

Most importantly, do **not** promote conditions on apparent reduction alone. Advancement requires that candidate branches remain:
- strong,
- sufficiently early / mild,
- and interpretable.

This is now my corrected preferred execution-ready plan.

