import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const outDir = path.resolve(__dirname, "../../tables/glycation_results_organized");
const payloadPath = path.join(outDir, "glycation_results_organized_payload.json");
const outputPath = path.join(outDir, "glycation_results_organized_review.xlsx");
const previewPath = path.join(outDir, "glycation_results_organized_preview.png");

const payload = JSON.parse(await fs.readFile(payloadPath, "utf8"));

function sanitizeValue(value) {
  if (value === undefined) return null;
  if (value === null) return null;
  if (typeof value === "number") {
    if (!Number.isFinite(value)) return null;
    return value;
  }
  if (typeof value === "boolean") return value;
  return String(value);
}

function colName(index) {
  let n = index + 1;
  let s = "";
  while (n > 0) {
    const r = (n - 1) % 26;
    s = String.fromCharCode(65 + r) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function addTableSheet(workbook, sheetName, rows, options = {}) {
  const sheet = workbook.worksheets.add(sheetName.slice(0, 31));
  sheet.showGridLines = false;
  const allKeys = [];
  for (const row of rows) {
    for (const key of Object.keys(row)) {
      if (!allKeys.includes(key)) allKeys.push(key);
    }
  }
  const headers = options.headers || allKeys;
  const matrix = [headers, ...rows.map((row) => headers.map((key) => sanitizeValue(row[key])))];
  const rowCount = Math.max(matrix.length, 1);
  const colCount = Math.max(headers.length, 1);
  sheet.getRangeByIndexes(0, 0, rowCount, colCount).values = matrix;

  const header = sheet.getRangeByIndexes(0, 0, 1, colCount);
  header.format = {
    fill: options.headerFill || "#315F7D",
    font: { bold: true, color: "#FFFFFF" },
    wrapText: true,
  };

  if (rowCount > 1) {
    const body = sheet.getRangeByIndexes(1, 0, rowCount - 1, colCount);
    body.format = { wrapText: true };
  }

  const used = sheet.getRangeByIndexes(0, 0, rowCount, colCount);
  used.format.borders = { preset: "outside", style: "thin", color: "#B7C9D6" };
  used.format.autofitColumns();
  used.format.autofitRows();
  sheet.freezePanes.freezeRows(1);

  if (rowCount > 1 && colCount > 1 && rowCount < 20000) {
    try {
      const range = `A1:${colName(colCount - 1)}${rowCount}`;
      sheet.tables.add(range, true, `${sheetName.replace(/[^A-Za-z0-9]/g, "")}Table`.slice(0, 48));
    } catch {
      // Tables are helpful but not essential for this handoff workbook.
    }
  }

  return sheet;
}

function addReadme(workbook) {
  const sheet = workbook.worksheets.add("README");
  sheet.showGridLines = false;
  const rows = [
    ["Glycation wet-lab data organization", ""],
    ["Generated at", payload.generated_at],
    ["Source folder", payload.source_dir],
    ["Purpose", "Non-destructive organization of all glycation-result workbooks for manuscript figures, Supplementary Tables and Supplementary Data."],
    ["Source workbook count", payload.summary.source_workbook_count],
    ["Source sheet count", payload.summary.sheet_count],
    ["Raw non-empty cell index rows", payload.summary.raw_cell_index_rows],
    ["Protected 24-run matrix rows", payload.summary.protected_24_run_rows],
    ["Long donor-time panel rows", payload.summary.long_timecourse_rows],
    ["Supplemental ELISA 2026-06-15 rows", payload.summary.elisa_2026_0615_rows],
    ["Ribose validation rows", payload.summary.ribose_validation_rows],
    ["Important interpretation", "Raw workbooks are unchanged. Structured sheets normalize only fields that could be mapped reliably. Use Raw_Cell_Index for cell-level tracing."],
    ["Endpoint", "IgG-binding reduction relative to native untreated beta-LG."],
    ["Reduction formula", "[1 - (treated/native)] x 100%; structured sheets use standard-curve-derived binding capacity when available."],
  ];
  sheet.getRangeByIndexes(0, 0, rows.length, 2).values = rows;
  sheet.getRange("A1:B1").format = {
    fill: "#315F7D",
    font: { bold: true, color: "#FFFFFF", size: 14 },
  };
  sheet.getRange("A2:A14").format = {
    fill: "#EAF2F8",
    font: { bold: true },
  };
  sheet.getRange("A1:B14").format.borders = { preset: "outside", style: "thin", color: "#B7C9D6" };
  sheet.getRange("A1:B14").format.autofitColumns();
  sheet.getRange("B4:B14").format = { wrapText: true };
  return sheet;
}

const workbook = Workbook.create();
addReadme(workbook);

addTableSheet(workbook, "File_Inventory", payload.datasets.file_inventory);
addTableSheet(workbook, "Sheet_Summary", payload.datasets.sheet_summary);
addTableSheet(workbook, "Figure_Data_Map", payload.datasets.figure_data_map);
addTableSheet(workbook, "Protected_24_Run", payload.datasets.protected_24_run_matrix);
addTableSheet(workbook, "Long_Timecourse", payload.datasets.long_timecourse);
addTableSheet(workbook, "ELISA_2026_0615", payload.datasets.elisa_2026_0615);
addTableSheet(workbook, "Ribose_Validation", payload.datasets.ribose_validation);
addTableSheet(workbook, "Fig3_Source_Data", payload.datasets.fig3_source_data);
addTableSheet(workbook, "Fig3c_Source_Data", payload.datasets.fig3c_source_data);
addTableSheet(workbook, "Raw_Cell_Index", payload.datasets.raw_cell_index);

const readmePreview = await workbook.render({
  sheetName: "README",
  autoCrop: "all",
  scale: 1,
  format: "png",
});
await fs.writeFile(previewPath, new Uint8Array(await readmePreview.arrayBuffer()));

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

const check = await workbook.inspect({
  kind: "workbook,sheet,table",
  maxChars: 6000,
  tableMaxRows: 4,
  tableMaxCols: 8,
});
console.log(check.ndjson);
console.log(JSON.stringify({ outputPath, previewPath }, null, 2));
