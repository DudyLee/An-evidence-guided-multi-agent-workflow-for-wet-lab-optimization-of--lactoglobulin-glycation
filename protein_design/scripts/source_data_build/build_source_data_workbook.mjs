import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, "../../..");
const buildDir = path.join(repoRoot, "tmp/source_data_build");

const sources = {
  bepipred: path.join(repoRoot, "data/bepipred_data/bepipred3_results/raw_output.csv"),
  netglycate: path.join(repoRoot, "data/netglycate_data/netglycate_results.csv"),
  fig3: path.join(repoRoot, "protein_design/figures/wetlab_results_v2/Figure_3_v2_source_data.csv"),
  fig3c: path.join(repoRoot, "protein_design/figures/wetlab_results_v2/Figure_3c_v2_source_data.csv"),
  workflowCounts: path.join(repoRoot, "protein_design/figures/workflow_analysis/workflow_word_counts.csv"),
  workflowSummary: path.join(repoRoot, "protein_design/figures/workflow_analysis/workflow_analysis_summary.json"),
  longTimecourse: path.join(repoRoot, "protein_design/tables/glycation_results_organized/long_timecourse.csv"),
  riboseValidation: path.join(repoRoot, "protein_design/tables/glycation_results_organized/ribose_validation.csv"),
};

const outputPath = path.join(repoRoot, "data/Source_Data.xlsx");

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let inQuotes = false;
  const normalized = text.replace(/^\uFEFF/, "");
  for (let i = 0; i < normalized.length; i += 1) {
    const char = normalized[i];
    const next = normalized[i + 1];
    if (inQuotes) {
      if (char === '"' && next === '"') {
        field += '"';
        i += 1;
      } else if (char === '"') {
        inQuotes = false;
      } else {
        field += char;
      }
    } else if (char === '"') {
      inQuotes = true;
    } else if (char === ",") {
      row.push(field);
      field = "";
    } else if (char === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (char !== "\r") {
      field += char;
    }
  }
  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }
  if (rows.length === 0) return [];
  const headers = rows[0].map((value, index) => value.trim() || `unnamed_${index + 1}`);
  return rows
    .slice(1)
    .filter((values) => values.some((value) => value !== ""))
    .map((values) => Object.fromEntries(headers.map((header, index) => [header, values[index] ?? ""])));
}

async function readCsv(filePath) {
  return parseCsv(await fs.readFile(filePath, "utf8"));
}

async function readCsvWithEncoding(filePath, encoding) {
  const buffer = await fs.readFile(filePath);
  return parseCsv(new TextDecoder(encoding).decode(buffer));
}

function num(value) {
  if (value === undefined || value === null || value === "") return null;
  const cleaned = String(value).trim();
  if (cleaned === "") return null;
  const parsed = Number(cleaned);
  return Number.isFinite(parsed) ? parsed : value;
}

function sheetNameSafe(value) {
  return value.slice(0, 31);
}

function columnName(indexZeroBased) {
  let n = indexZeroBased + 1;
  let name = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    name = String.fromCharCode(65 + rem) + name;
    n = Math.floor((n - 1) / 26);
  }
  return name;
}

function writeSheet(workbook, name, headers, rows, options = {}) {
  const sheet = workbook.worksheets.add(sheetNameSafe(name));
  sheet.showGridLines = false;
  const values = [
    headers,
    ...rows.map((row) => headers.map((header) => row[header] ?? null)),
  ];
  const range = sheet.getRangeByIndexes(0, 0, values.length, headers.length);
  range.values = values;
  const headerRange = sheet.getRangeByIndexes(0, 0, 1, headers.length);
  headerRange.format = {
    fill: "#245F78",
    font: { bold: true, color: "#FFFFFF" },
    wrapText: true,
  };
  range.format.borders = { preset: "outside", style: "thin", color: "#B7C7D9" };
  sheet.getRangeByIndexes(1, 0, Math.max(rows.length, 1), headers.length).format = {
    wrapText: true,
  };
  sheet.freezePanes.freezeRows(1);
  const lastColumn = columnName(headers.length - 1);
  if (rows.length > 0) {
    const table = sheet.tables.add(`A1:${lastColumn}${rows.length + 1}`, true, `${name.replace(/[^A-Za-z0-9]/g, "")}Table`.slice(0, 240));
    table.style = "TableStyleMedium2";
    table.showFilterButton = true;
  }
  sheet.getUsedRange(true).format.autofitColumns();
  sheet.getUsedRange(true).format.autofitRows();
  if (options.numericColumns) {
    for (const col of options.numericColumns) {
      const index = headers.indexOf(col);
      if (index >= 0 && rows.length > 0) {
        sheet.getRangeByIndexes(1, index, rows.length, 1).format.numberFormat = options.numberFormat || "0.000";
      }
    }
  }
  return sheet;
}

function makeReadmeRows() {
  return [
    {
      item: "Workbook purpose",
      detail: "Source Data workbook for the main and supplementary quantitative figures in the beta-lactoglobulin glycation manuscript.",
    },
    {
      item: "Scope",
      detail: "Sheets contain plotted values or values directly used to calculate plotted quantities. Full raw workbooks, complete prompt archives, meeting records and code are intended for the project data/code repositories.",
    },
    {
      item: "Experimental endpoint",
      detail: "IgG-binding reduction relative to native untreated beta-lactoglobulin.",
    },
    {
      item: "Reduction formula",
      detail: "[1 - (treated/native)] x 100%.",
    },
    {
      item: "Error definition",
      detail: "Error columns labelled error_pct, error_pct_vs_native or error_pct_vs_untreated_N refer to standard deviation unless otherwise stated in the manuscript or Supplementary Information.",
    },
    {
      item: "Fig. 3c marginal gain definition",
      detail: "For adjacent time points t1 and t2, marginal gain = [R(t2) - R(t1)] / (t2 - t1), reported as percentage points per hour.",
    },
    {
      item: "Generated file",
      detail: "Source_Data.xlsx generated from project CSV/JSON source files on 2026-06-29.",
    },
  ];
}

function buildBepipredRows(rows) {
  return rows.map((row, index) => ({
    panel_id: "Fig. 2c",
    accession: row.Accession,
    position: index + 1,
    residue: row.Residue,
    bepipred_3_score: num(row["BepiPred-3.0 score"]),
    bepipred_3_linear_epitope_score: num(row["BepiPred-3.0 linear epitope score"]),
    plotted_score: num(row["BepiPred-3.0 score"]),
    is_lysine_residue: row.Residue === "K" ? "yes" : "no",
    source_file: path.basename(sources.bepipred),
    note: "Residue position was assigned from row order in the BepiPred-3.0 output.",
  }));
}

function buildNetglycateRows(rows) {
  return rows.map((row, index) => ({
    panel_id: "Fig. 2d",
    rank_in_source_file: index + 1,
    position: num(row.Position),
    residue: row.Residue,
    netglycate_probability: num(row.Probability),
    plotted_score: num(row.Probability),
    source_note: row.unnamed_4 || "",
    source_file: path.basename(sources.netglycate),
  }));
}

function buildFig3Rows(rows, panel) {
  return rows
    .filter((row) => row.current_figure_panel === panel)
    .map((row) => ({
      panel_id: panel,
      run_id: row.run_id,
      decision_block: row.decision_block,
      donor: row.donor,
      temperature_C: num(row.temperature_C),
      time_h: num(row.time_h),
      ultrasound: row.ultrasound,
      mode: row.mode,
      aw: num(row.aw),
      protein_sugar_ratio: row.protein_sugar_ratio,
      no_sugar_control: row.no_sugar_control,
      result_status: row.result_status,
      reduction_pct_vs_native_untreated: num(row.reduction_pct_vs_untreated_N),
      error_pct_sd: num(row.error_pct),
      source_workbook: row.source_workbook,
      source_file: row.source_file,
      source_sheet_or_label: row.source_sheet_or_label,
      sample_label: row.sample_label,
      note: row.note,
    }));
}

function buildFig3cRows(rows) {
  const glucoseRows = rows
    .filter((row) => row.series === "glucose_55C_plusUS_marginal_evidence")
    .sort((a, b) => Number(a.time_h) - Number(b.time_h));
  const marginalByTime = new Map();
  for (let i = 1; i < glucoseRows.length; i += 1) {
    const prev = glucoseRows[i - 1];
    const current = glucoseRows[i];
    const gain = (Number(current.reduction_pct) - Number(prev.reduction_pct)) / (Number(current.time_h) - Number(prev.time_h));
    marginalByTime.set(String(current.time_h), gain);
  }
  return rows.map((row) => ({
    panel_id: "Fig. 3c",
    series: row.series,
    condition: row.condition,
    time_h: num(row.time_h),
    reduction_pct_vs_native_untreated: num(row.reduction_pct),
    error_pct_sd: num(row.error_pct),
    range_low_pct: num(row.range_low),
    range_high_pct: num(row.range_high),
    marginal_gain_from_previous_time_pp_per_h: row.series === "glucose_55C_plusUS_marginal_evidence" ? num(marginalByTime.get(String(row.time_h)) ?? null) : null,
    baseline: "native untreated beta-lactoglobulin",
    note: row.series === "agent_prediction"
      ? "Evidence-weighted pre-validation estimate and plausible range."
      : row.series === "wetlab_validation"
        ? "Focused wet-lab validation of final ribose recommendation."
        : "Glucose time-course used as marginal-effect calibration evidence.",
  }));
}

function buildFunnelRows() {
  return [
    {
      panel_id: "Fig. 4a",
      stage_order: 1,
      stage: "Literature-visible envelope",
      narrowing_basis: "Semantically grouped variable levels",
      displayed_metric: "~1.12 million plausible combinations",
      numeric_value: 1123584,
      note: "Conceptual upper bound from literature-derived variable grouping; not treated as a planned experiment count.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 2,
      stage: "Study-feasible envelope",
      narrowing_basis: "Scope and feasibility constraints",
      displayed_metric: "",
      numeric_value: null,
      note: "Stage shown in funnel without a plotted numerical count.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 3,
      stage: "Project-specified candidates",
      narrowing_basis: "High-value scientific questions",
      displayed_metric: "",
      numeric_value: null,
      note: "Stage shown in funnel without a plotted numerical count.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 4,
      stage: "Operational decision space",
      narrowing_basis: "Matched comparisons",
      displayed_metric: "",
      numeric_value: null,
      note: "Stage shown in funnel without a plotted numerical count.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 5,
      stage: "Execution-ready matrix",
      narrowing_basis: "Completeness audit",
      displayed_metric: "24 planned / 24 result-bearing",
      numeric_value: 24,
      note: "All planned rows had directly attributable result records after supplemental ELISA incorporation.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 6,
      stage: "Comparator-aware refinement",
      narrowing_basis: "Focused adjudication",
      displayed_metric: "",
      numeric_value: null,
      note: "Stage shown in funnel without a plotted numerical count.",
    },
    {
      panel_id: "Fig. 4a",
      stage_order: 7,
      stage: "Final validation candidate",
      narrowing_basis: "Locked recommendation",
      displayed_metric: "1 candidate",
      numeric_value: 1,
      note: "Single pre-validation recommendation selected for focused validation.",
    },
  ];
}

function buildFig4bRows(rows) {
  return rows.map((row) => ({
    panel_id: "Fig. 4b",
    phase: row.phase,
    contributor: row.contributor,
    words: num(row.words),
    phase_pct: num(row.phase_pct),
    counting_rule: "Whitespace-delimited word counts from retained prompts, questions, discussion messages and merged records.",
  }));
}

function buildFig4cRows(summary) {
  return Object.entries(summary.contributor_totals).map(([contributor, total]) => ({
    panel_id: "Fig. 4c",
    contributor,
    contributor_group: contributor === "Human Researcher" ? "human" : "agent",
    total_words: total,
    human_total_words: summary.human_total,
    agent_total_words: summary.agent_total,
    counting_rule: "Cumulative word counts across the same five analysed discussion phases used for Fig. 4b.",
  }));
}

function buildSuppFigRows(rows) {
  return rows.map((row) => ({
    panel_id: "Supplementary Fig. 1",
    dataset: row.dataset,
    donor: row.donor,
    donor_cn: row.donor_cn,
    time_h: num(row.time_h),
    temperature_C: num(row.temperature_C),
    temperature_note: row.temperature_note,
    ultrasound: row.ultrasound,
    mode: row.mode,
    aw: num(row.aw),
    native_baseline: num(row.native_baseline),
    binding_capacity_mean: num(row.binding_capacity_mean),
    binding_capacity_sd: num(row.binding_capacity_sd),
    reduction_pct_vs_native: num(row.reduction_pct_vs_native),
    error_pct_vs_native_sd: num(row.error_pct_vs_native),
    source_file: row.source_file,
    source_sheet: row.source_sheet,
    source_row: num(row.source_row),
    use_in_manuscript: row.use_in_manuscript,
  }));
}

function buildValidationRows(rows) {
  return rows.map((row) => ({
    panel_id: "Fig. 3c / Supplementary Fig. 1 reference point",
    dataset: row.dataset,
    source_label: row.source_label,
    donor: row.donor,
    time_h: num(row.time_h),
    temperature_C: num(row.temperature_C),
    ultrasound: row.ultrasound,
    mode: row.mode,
    aw: num(row.aw),
    binding_capacity_mean: num(row.binding_capacity_mean),
    reduction_pct_vs_native: num(row.reduction_pct_vs_native),
    error_pct_sd: num(row.error_pct),
    source_file: row.source_file,
    source_sheet: row.source_sheet,
    source_cells: row.source_cells,
    use_in_manuscript: row.use_in_manuscript,
    note: row.note,
  }));
}

async function main() {
  const [
    bepipred,
    netglycate,
    fig3,
    fig3c,
    workflowCounts,
    longTimecourse,
    riboseValidation,
  ] = await Promise.all([
    readCsv(sources.bepipred),
    readCsvWithEncoding(sources.netglycate, "gb18030"),
    readCsv(sources.fig3),
    readCsv(sources.fig3c),
    readCsv(sources.workflowCounts),
    readCsv(sources.longTimecourse),
    readCsv(sources.riboseValidation),
  ]);
  const workflowSummary = JSON.parse(await fs.readFile(sources.workflowSummary, "utf8"));

  const workbook = Workbook.create();

  writeSheet(workbook, "README", ["item", "detail"], makeReadmeRows());
  writeSheet(
    workbook,
    "Fig2c_BepiPred",
    ["panel_id", "accession", "position", "residue", "bepipred_3_score", "bepipred_3_linear_epitope_score", "plotted_score", "is_lysine_residue", "source_file", "note"],
    buildBepipredRows(bepipred),
    { numericColumns: ["position", "bepipred_3_score", "bepipred_3_linear_epitope_score", "plotted_score"], numberFormat: "0.000" },
  );
  writeSheet(
    workbook,
    "Fig2d_NetGlycate",
    ["panel_id", "rank_in_source_file", "position", "residue", "netglycate_probability", "plotted_score", "source_note", "source_file"],
    buildNetglycateRows(netglycate),
    { numericColumns: ["rank_in_source_file", "position", "netglycate_probability", "plotted_score"], numberFormat: "0.000" },
  );
  writeSheet(
    workbook,
    "Fig3a_hexose_bridge",
    ["panel_id", "run_id", "decision_block", "donor", "temperature_C", "time_h", "ultrasound", "mode", "aw", "protein_sugar_ratio", "no_sugar_control", "result_status", "reduction_pct_vs_native_untreated", "error_pct_sd", "source_workbook", "source_file", "source_sheet_or_label", "sample_label", "note"],
    buildFig3Rows(fig3, "Fig. 3a"),
    { numericColumns: ["temperature_C", "time_h", "aw", "reduction_pct_vs_native_untreated", "error_pct_sd"], numberFormat: "0.00" },
  );
  writeSheet(
    workbook,
    "Fig3b_short_controls",
    ["panel_id", "run_id", "decision_block", "donor", "temperature_C", "time_h", "ultrasound", "mode", "aw", "protein_sugar_ratio", "no_sugar_control", "result_status", "reduction_pct_vs_native_untreated", "error_pct_sd", "source_workbook", "source_file", "source_sheet_or_label", "sample_label", "note"],
    buildFig3Rows(fig3, "Fig. 3b"),
    { numericColumns: ["temperature_C", "time_h", "aw", "reduction_pct_vs_native_untreated", "error_pct_sd"], numberFormat: "0.00" },
  );
  writeSheet(
    workbook,
    "Fig3c_time_validation",
    ["panel_id", "series", "condition", "time_h", "reduction_pct_vs_native_untreated", "error_pct_sd", "range_low_pct", "range_high_pct", "marginal_gain_from_previous_time_pp_per_h", "baseline", "note"],
    buildFig3cRows(fig3c),
    { numericColumns: ["time_h", "reduction_pct_vs_native_untreated", "error_pct_sd", "range_low_pct", "range_high_pct", "marginal_gain_from_previous_time_pp_per_h"], numberFormat: "0.00" },
  );
  writeSheet(
    workbook,
    "Fig4a_funnel",
    ["panel_id", "stage_order", "stage", "narrowing_basis", "displayed_metric", "numeric_value", "note"],
    buildFunnelRows(),
    { numericColumns: ["stage_order", "numeric_value"], numberFormat: "0" },
  );
  writeSheet(
    workbook,
    "Fig4b_phase_role",
    ["panel_id", "phase", "contributor", "words", "phase_pct", "counting_rule"],
    buildFig4bRows(workflowCounts),
    { numericColumns: ["words", "phase_pct"], numberFormat: "0.000" },
  );
  writeSheet(
    workbook,
    "Fig4c_role_totals",
    ["panel_id", "contributor", "contributor_group", "total_words", "human_total_words", "agent_total_words", "counting_rule"],
    buildFig4cRows(workflowSummary),
    { numericColumns: ["total_words", "human_total_words", "agent_total_words"], numberFormat: "0" },
  );
  writeSheet(
    workbook,
    "SuppFig1_donor_time",
    ["panel_id", "dataset", "donor", "donor_cn", "time_h", "temperature_C", "temperature_note", "ultrasound", "mode", "aw", "native_baseline", "binding_capacity_mean", "binding_capacity_sd", "reduction_pct_vs_native", "error_pct_vs_native_sd", "source_file", "source_sheet", "source_row", "use_in_manuscript"],
    buildSuppFigRows(longTimecourse),
    { numericColumns: ["time_h", "temperature_C", "aw", "native_baseline", "binding_capacity_mean", "binding_capacity_sd", "reduction_pct_vs_native", "error_pct_vs_native_sd", "source_row"], numberFormat: "0.000" },
  );
  writeSheet(
    workbook,
    "SuppFig1_validation",
    ["panel_id", "dataset", "source_label", "donor", "time_h", "temperature_C", "ultrasound", "mode", "aw", "binding_capacity_mean", "reduction_pct_vs_native", "error_pct_sd", "source_file", "source_sheet", "source_cells", "use_in_manuscript", "note"],
    buildValidationRows(riboseValidation),
    { numericColumns: ["time_h", "temperature_C", "aw", "binding_capacity_mean", "reduction_pct_vs_native", "error_pct_sd"], numberFormat: "0.00" },
  );

  await fs.mkdir(path.dirname(outputPath), { recursive: true });
  await fs.mkdir(path.join(buildDir, "previews"), { recursive: true });
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

  const sheetNames = [
    "README",
    "Fig2c_BepiPred",
    "Fig2d_NetGlycate",
    "Fig3a_hexose_bridge",
    "Fig3b_short_controls",
    "Fig3c_time_validation",
    "Fig4a_funnel",
    "Fig4b_phase_role",
    "Fig4c_role_totals",
    "SuppFig1_donor_time",
    "SuppFig1_validation",
  ];
  for (const sheetName of sheetNames) {
    const preview = await workbook.render({ sheetName, autoCrop: "all", scale: 1, format: "png" });
    await fs.writeFile(
      path.join(buildDir, "previews", `${sheetName}.png`),
      new Uint8Array(await preview.arrayBuffer()),
    );
  }

  const errors = await workbook.inspect({
    kind: "match",
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 300 },
    summary: "final formula error scan",
  });
  console.log(errors.ndjson);

  const overview = await workbook.inspect({
    kind: "sheet",
    include: "id,name,index,range",
    maxChars: 4000,
  });
  console.log(overview.ndjson);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

  const output = await SpreadsheetFile.exportXlsx(workbook);
  await output.save(outputPath);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });
  console.log(JSON.stringify({ outputPath, sheetCount: sheetNames.length }));
}

await main();
