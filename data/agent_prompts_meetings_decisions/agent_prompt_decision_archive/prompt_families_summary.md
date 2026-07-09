# Prompt families represented in Supplementary Data 5

## Role-construction prompts
Used to instantiate the Principal Investigator, Scientific Critic, Evidence Curator and domain-scientist roles. The retained records are in `retained_discussion_records/team_selection/`.

## Evidence extraction prompt
Used by the Evidence Curator to convert full-text papers into schema-controlled JSONL records with run-level condition fields, comparator links and reported reduction information. The full extraction rules are described in Supplementary Methods 2 and Supplementary Table 1; the prompt family is represented in the literature-facing workflow records and the manuscript prompt notes.

For this review package, the exact web-interface prompt used for the structured literature extraction workflow is archived separately at `Knowledge_Extraction/literature_evidence_extraction_prompt.md`.

## Tool-selection and feasibility-screening prompt
Used to ask the agent team to propose computational tools while explicitly distinguishing glycation-relevant methods from glycosylation-specific or over-interpretable tools. The retained records are in `retained_discussion_records/tools_selection/`.

## Project-specification prompt
Used to define the ?-LG glycation objective, IgG-binding endpoint, fixed feasibility envelope and decision questions. The retained records are in `retained_discussion_records/project_specification/`.

## Question-structured run-sheet prompt
Used to translate unresolved questions into a protected experimental matrix with donor, temperature, time, ultrasound, process-control and comparator fields. The retained records are in `retained_discussion_records/execution_planning/` and `retained_discussion_records/wetlab_runsheet_generation/`.

## Wet-lab feedback and recommendation-locking prompt
Used to return result packets to the agent team, interpret them under matched-comparator logic and lock the final ribose recommendation before validation. The retained records are in `retained_discussion_records/iteration1_discussion/`, `retained_discussion_records/wetlab_feedback*/` and `retained_discussion_records/wetlab_feedback_90%/`.
