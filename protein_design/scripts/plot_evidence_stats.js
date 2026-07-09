const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..", "..");
const dataPath = path.join(root, "data", "paper_data", "Paper_run_data.computed_V2.jsonl");
const outDir = path.join(root, "protein_design", "figures", "evidence_stats");
fs.mkdirSync(outDir, { recursive: true });

const rows = fs
  .readFileSync(dataPath, "utf8")
  .trim()
  .split(/\r?\n/)
  .filter(Boolean)
  .map((line) => JSON.parse(line));

const finite = (v) => v !== null && v !== undefined && v !== "" && Number.isFinite(Number(v));
const count = (arr, pred) => arr.filter(pred).length;
const unique = (arr) => new Set(arr).size;
const fmt = (v) => (v === null || v === undefined || v === "" ? "Missing" : String(v));

const figurePalette = [
  "#7b95c6",
  "#49c2d9",
  "#a1d8e8",
  "#67a583",
  "#a2c986",
  "#d0e2c0",
  "#fded95",
  "#ffc1a6",
  "#f59c7c",
  "#f47254",
  "#c85e62",
];

const palette = [
  figurePalette[0],
  figurePalette[3],
  figurePalette[9],
  figurePalette[8],
  figurePalette[4],
  figurePalette[10],
  figurePalette[1],
  figurePalette[7],
  figurePalette[6],
  figurePalette[2],
  figurePalette[5],
];

const ink = "#202124";
const muted = "#5f6368";
const grid = "#e7e3dc";
const axis = "#3c4043";

function esc(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function groupBy(field, filter = () => true) {
  const m = new Map();
  for (const r of rows) {
    if (!filter(r)) continue;
    const key = fmt(typeof field === "function" ? field(r) : r[field]);
    m.set(key, (m.get(key) || 0) + 1);
  }
  return [...m.entries()]
    .map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value);
}

function normalizeDonor(sugar) {
  if (sugar === null || sugar === undefined || sugar === "") return "Missing";
  const s = String(sugar).trim();
  const lower = s.toLowerCase();
  if (lower === "galactose (gal)" || lower === "galactose") return "galactose";
  if (
    lower === "galactose oligosaccharide (gos)" ||
    lower === "galacto-oligosaccharides (gos)"
  ) {
    return "GOS";
  }
  if (lower.startsWith("dextran")) return "dextran";
  return s;
}

function svgWrap(width, height, title, body) {
  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
  <text x="${width / 2}" y="36" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="700" fill="${ink}">${esc(title)}</text>
  ${body}
</svg>`;
}

function save(name, svg) {
  fs.writeFileSync(path.join(outDir, name), svg, "utf8");
}

function barChart({ name, title, data, width = 980, height = 620, xLabel = "", yLabel = "Records" }) {
  const margin = { top: 72, right: 42, bottom: 150, left: 76 };
  const plotW = width - margin.left - margin.right;
  const plotH = height - margin.top - margin.bottom;
  const max = Math.max(...data.map((d) => d.value), 1);
  const step = plotW / data.length;
  const barW = Math.min(72, step * 0.62);
  const ticks = 5;
  let body = "";

  for (let i = 0; i <= ticks; i++) {
    const val = Math.round((max * i) / ticks);
    const y = margin.top + plotH - (plotH * i) / ticks;
    body += `<line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="${grid}" stroke-width="1"/>`;
    body += `<text x="${margin.left - 10}" y="${y + 4}" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="${muted}">${val}</text>`;
  }

  data.forEach((d, i) => {
    const h = (d.value / max) * plotH;
    const x = margin.left + i * step + (step - barW) / 2;
    const y = margin.top + plotH - h;
    const color = palette[i % palette.length];
    const label = d.label.length > 24 ? d.label.slice(0, 22) + "..." : d.label;
    body += `<rect x="${x}" y="${y}" width="${barW}" height="${h}" rx="4" fill="${color}"/>`;
    body += `<text x="${x + barW / 2}" y="${y - 8}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="13" font-weight="700" fill="${ink}">${d.value}</text>`;
    body += `<text x="${x + barW / 2}" y="${margin.top + plotH + 22}" transform="rotate(-40 ${x + barW / 2} ${margin.top + plotH + 22})" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="13" fill="${ink}">${esc(label)}</text>`;
  });

  body += `<line x1="${margin.left}" y1="${margin.top + plotH}" x2="${width - margin.right}" y2="${margin.top + plotH}" stroke="${ink}" stroke-width="1.2"/>`;
  body += `<line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${margin.top + plotH}" stroke="${ink}" stroke-width="1.2"/>`;
  body += `<text x="22" y="${margin.top + plotH / 2}" transform="rotate(-90 22 ${margin.top + plotH / 2})" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="${axis}">${esc(yLabel)}</text>`;
  if (xLabel) body += `<text x="${width / 2}" y="${height - 18}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="${axis}">${esc(xLabel)}</text>`;
  save(name, svgWrap(width, height, title, body));
}

function donutChart({ name, title, data, width = 760, height = 520 }) {
  const cx = 260;
  const cy = 270;
  const outerR = 155;
  const innerR = 102;
  const total = data.reduce((s, d) => s + d.value, 0);
  let angle = -Math.PI / 2;
  let body = "";

  function point(radius, a) {
    return {
      x: cx + radius * Math.cos(a),
      y: cy + radius * Math.sin(a),
    };
  }

  function donutSlice(start, end, color) {
    const largeArc = end - start > Math.PI ? 1 : 0;
    const p1 = point(outerR, start);
    const p2 = point(outerR, end);
    const p3 = point(innerR, end);
    const p4 = point(innerR, start);
    return [
      `<path d="`,
      `M ${p1.x.toFixed(3)} ${p1.y.toFixed(3)} `,
      `A ${outerR} ${outerR} 0 ${largeArc} 1 ${p2.x.toFixed(3)} ${p2.y.toFixed(3)} `,
      `L ${p3.x.toFixed(3)} ${p3.y.toFixed(3)} `,
      `A ${innerR} ${innerR} 0 ${largeArc} 0 ${p4.x.toFixed(3)} ${p4.y.toFixed(3)} `,
      `Z" fill="${color}"/>`,
    ].join("");
  }

  data.forEach((d, i) => {
    const nextAngle = angle + (d.value / total) * Math.PI * 2;
    body += donutSlice(angle, nextAngle, palette[i % palette.length]);
    angle = nextAngle;
  });

  body += `<text x="${cx}" y="${cy - 6}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="34" font-weight="700" fill="${ink}">${total}</text>`;
  body += `<text x="${cx}" y="${cy + 22}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="${muted}">records</text>`;

  const lx = 475;
  let ly = 190;
  data.forEach((d, i) => {
    const pct = ((d.value / total) * 100).toFixed(1);
    body += `<rect x="${lx}" y="${ly - 13}" width="18" height="18" rx="3" fill="${palette[i % palette.length]}"/>`;
    body += `<text x="${lx + 30}" y="${ly + 1}" font-family="Arial, Helvetica, sans-serif" font-size="15" fill="${ink}">${esc(d.label)}: ${d.value} (${pct}%)</text>`;
    ly += 34;
  });

  save(name, svgWrap(width, height, title, body));
}

const totalRecords = rows.length;
const uniqueRuns = unique(rows.map((r) => `${r.paper_id}|${r.run_id}`));
const papers = unique(rows.map((r) => r.paper_id));
const controls = count(rows, (r) => r.comparator_run_id == null);
const comparisons = count(rows, (r) => r.comparator_run_id != null);
const numericReduction = count(rows, (r) => finite(r.reduction_pct_reported));
const noReduction = totalRecords - numericReduction;

barChart({
  name: "overview_counts_bar.svg",
  title: "Curated Evidence Base Overview",
  data: [
    { label: "Papers", value: papers },
    { label: "Unique runs", value: uniqueRuns },
    { label: "Metric-level records", value: totalRecords },
    { label: "Treatment records", value: comparisons },
    { label: "Control records", value: controls },
    { label: "Numeric reductions", value: numericReduction },
  ],
  yLabel: "Count",
});

donutChart({
  name: "record_type_donut.svg",
  title: "Treatment vs Control Records",
  data: [
    { label: "Treatment/comparison", value: comparisons },
    { label: "Comparator/control", value: controls },
  ],
});

donutChart({
  name: "reduction_availability_donut.svg",
  title: "Reduction Evidence Availability",
  data: [
    { label: "Numeric reduction", value: numericReduction },
    { label: "No numeric reduction", value: noReduction },
  ],
});

donutChart({
  name: "mode_donut.svg",
  title: "Reaction Mode Coverage",
  data: [
    { label: "Dry", value: count(rows, (r) => r.mode === "dry") },
    { label: "Wet", value: count(rows, (r) => r.mode === "wet") },
    { label: "Missing", value: count(rows, (r) => r.mode == null) },
  ],
});

donutChart({
  name: "pretreatment_all_records_donut.svg",
  title: "Pretreatment Coverage (All Records)",
  data: [
    { label: "No pretreatment", value: count(rows, (r) => r.pretreatment_used === false) },
    { label: "With pretreatment", value: count(rows, (r) => r.pretreatment_used === true) },
  ],
});

donutChart({
  name: "pretreatment_treatment_records_donut.svg",
  title: "Pretreatment Coverage (Treatment Records)",
  data: [
    {
      label: "No pretreatment",
      value: count(rows, (r) => r.comparator_run_id != null && r.pretreatment_used === false),
    },
    {
      label: "With pretreatment",
      value: count(rows, (r) => r.comparator_run_id != null && r.pretreatment_used === true),
    },
  ],
});

const redVals = rows.map((r) => Number(r.reduction_pct_reported)).filter(Number.isFinite);
barChart({
  name: "reduction_thresholds_bar.svg",
  title: "Reported Reduction Thresholds",
  data: [
    { label: ">= 50%", value: redVals.filter((x) => x >= 50).length },
    { label: ">= 80%", value: redVals.filter((x) => x >= 80).length },
    { label: ">= 90%", value: redVals.filter((x) => x >= 90).length },
  ],
  width: 760,
  height: 520,
  yLabel: "Records",
});

barChart({
  name: "top_donors_bar.svg",
  title: "Most Frequent Donors",
  data: groupBy((r) => normalizeDonor(r.sugar), (r) => r.sugar != null).slice(0, 10),
  yLabel: "Records",
});

barChart({
  name: "top_metrics_bar.svg",
  title: "Most Frequent Allergenicity-Related Metrics",
  data: groupBy("metric_name").slice(0, 10),
  yLabel: "Records",
});

barChart({
  name: "top_assays_bar.svg",
  title: "Most Frequent Assay Types",
  data: groupBy("assay_name").slice(0, 10),
  yLabel: "Records",
});

console.log(`Wrote SVG figures to ${outDir}`);
