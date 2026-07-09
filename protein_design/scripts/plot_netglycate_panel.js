const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const root = path.resolve(__dirname, "..", "..");
const outDir = path.join(root, "protein_design", "figures", "evidence_stats");
fs.mkdirSync(outDir, { recursive: true });

const sequenceLength = 162;
const data = [
  [8, -0.916, false],
  [14, 0.804, true],
  [47, 0.925, true],
  [60, -0.942, false],
  [69, -0.907, false],
  [70, 0.818, true],
  [75, -0.832, false],
  [77, -0.862, false],
  [83, -0.707, false],
  [91, -0.905, false],
  [100, 0.803, true],
  [101, 0.801, true],
  [135, -0.923, false],
  [138, -0.96, false],
  [141, -0.858, false],
];

const width = 900;
const height = 380;
const margin = { top: 62, right: 28, bottom: 72, left: 78 };
const plotW = width - margin.left - margin.right;
const plotH = height - margin.top - margin.bottom;
const yMin = -1.1;
const yMax = 1.1;

const xScale = (x) => margin.left + (x / (sequenceLength + 5)) * plotW;
const yScale = (y) => margin.top + ((yMax - y) / (yMax - yMin)) * plotH;

const svgPath = path.join(outDir, "netglycate_panel_d.svg");
const pdfPath = path.join(outDir, "netglycate_panel_d.pdf");

function escXml(s) {
  return String(s)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function buildSvg() {
  let body = "";
  body += `<rect x="0" y="0" width="${width}" height="${height}" fill="#ffffff"/>`;
  body += `<text x="${width / 2}" y="30" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="18" font-weight="700" fill="#202124">NetGlycate-predicted glycation-prone lysine sites in beta-LG</text>`;

  [-1, -0.5, 0, 0.5, 1].forEach((tick) => {
    const y = yScale(tick);
    const isZero = tick === 0;
    body += `<line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="${isZero ? "#7a7f85" : "#e3e1dc"}" stroke-width="${isZero ? 1.2 : 0.8}"/>`;
    body += `<text x="${margin.left - 12}" y="${y + 4}" text-anchor="end" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#4f555b">${tick.toFixed(tick === 0 ? 0 : 1)}</text>`;
  });

  for (const [position, score, predicted] of data) {
    const x = xScale(position);
    const y0 = yScale(0);
    const y = yScale(score);
    const color = predicted ? "#e67e22" : "#9aa0a6";
    const strokeWidth = predicted ? 2.2 : 1.5;
    const radius = predicted ? 4.4 : 3.4;
    body += `<line x1="${x}" y1="${y0}" x2="${x}" y2="${y}" stroke="${color}" stroke-width="${strokeWidth}" opacity="${predicted ? 0.98 : 0.9}"/>`;
    body += `<circle cx="${x}" cy="${y}" r="${radius}" fill="${color}"/>`;
    if (predicted) {
      body += `<text x="${x}" y="${y - 10}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#202124">K${position}</text>`;
    }
  }

  const xAxisY = yScale(yMin);
  body += `<line x1="${margin.left}" y1="${xAxisY}" x2="${width - margin.right}" y2="${xAxisY}" stroke="#202124" stroke-width="1.2"/>`;
  body += `<line x1="${margin.left}" y1="${margin.top}" x2="${margin.left}" y2="${xAxisY}" stroke="#202124" stroke-width="1.2"/>`;

  [0, 20, 40, 60, 80, 100, 120, 140, 160].forEach((tick) => {
    const x = xScale(tick);
    body += `<line x1="${x}" y1="${xAxisY}" x2="${x}" y2="${xAxisY + 5}" stroke="#202124" stroke-width="1"/>`;
    body += `<text x="${x}" y="${xAxisY + 22}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#202124">${tick}</text>`;
  });

  body += `<text x="${margin.left + plotW / 2}" y="${height - 16}" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#202124">Sequence position</text>`;
  body += `<text x="22" y="${margin.top + plotH / 2}" transform="rotate(-90 22 ${margin.top + plotH / 2})" text-anchor="middle" font-family="Arial, Helvetica, sans-serif" font-size="14" fill="#202124">NetGlycate score</text>`;

  const legendX = 92;
  const legendY = 304;
  body += `<line x1="${legendX}" y1="${legendY}" x2="${legendX + 26}" y2="${legendY}" stroke="#9aa0a6" stroke-width="1.5"/><circle cx="${legendX + 13}" cy="${legendY}" r="3.6" fill="#9aa0a6"/>`;
  body += `<text x="${legendX + 36}" y="${legendY + 4}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#202124">Other lysine residues</text>`;
  body += `<line x1="${legendX + 210}" y1="${legendY}" x2="${legendX + 236}" y2="${legendY}" stroke="#e67e22" stroke-width="2.2"/><circle cx="${legendX + 223}" cy="${legendY}" r="4.2" fill="#e67e22"/>`;
  body += `<text x="${legendX + 246}" y="${legendY + 4}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#202124">Predicted glycation-prone sites (YES)</text>`;
  body += `<line x1="${legendX + 508}" y1="${legendY}" x2="${legendX + 534}" y2="${legendY}" stroke="#7a7f85" stroke-width="1.2"/>`;
  body += `<text x="${legendX + 544}" y="${legendY + 4}" font-family="Arial, Helvetica, sans-serif" font-size="12" fill="#202124">Threshold = 0</text>`;

  return `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}" viewBox="0 0 ${width} ${height}">
${body}
</svg>
`;
}

function hexToRgb(hex) {
  const h = hex.replace("#", "");
  return [parseInt(h.slice(0, 2), 16) / 255, parseInt(h.slice(2, 4), 16) / 255, parseInt(h.slice(4, 6), 16) / 255];
}

function pdfEscape(s) {
  return String(s).replaceAll("\\", "\\\\").replaceAll("(", "\\(").replaceAll(")", "\\)");
}

function buildPdf() {
  const pageW = 9 * 72;
  const pageH = 3.8 * 72;
  const sx = pageW / width;
  const sy = pageH / height;
  const px = (x) => x * sx;
  const py = (y) => pageH - y * sy;
  const ps = (s) => s * sx;
  const commands = [];

  const stroke = (hex) => {
    const [r, g, b] = hexToRgb(hex);
    commands.push(`${r.toFixed(3)} ${g.toFixed(3)} ${b.toFixed(3)} RG`);
  };
  const fill = (hex) => {
    const [r, g, b] = hexToRgb(hex);
    commands.push(`${r.toFixed(3)} ${g.toFixed(3)} ${b.toFixed(3)} rg`);
  };
  const line = (x1, y1, x2, y2, color, w = 1) => {
    stroke(color);
    commands.push(`${ps(w).toFixed(3)} w ${px(x1).toFixed(3)} ${py(y1).toFixed(3)} m ${px(x2).toFixed(3)} ${py(y2).toFixed(3)} l S`);
  };
  const text = (x, y, s, size = 10, color = "#202124", align = "left") => {
    fill(color);
    const approx = s.length * size * 0.29;
    const tx = align === "center" ? px(x) - approx : align === "right" ? px(x) - approx * 2 : px(x);
    commands.push(`BT /F1 ${ps(size).toFixed(3)} Tf ${tx.toFixed(3)} ${py(y).toFixed(3)} Td (${pdfEscape(s)}) Tj ET`);
  };
  const circle = (x, y, r, color) => {
    fill(color);
    const c = 0.5522847498;
    const X = px(x), Y = py(y), R = ps(r), C = R * c;
    commands.push(`${X.toFixed(3)} ${(Y + R).toFixed(3)} m ${(X + C).toFixed(3)} ${(Y + R).toFixed(3)} ${(X + R).toFixed(3)} ${(Y + C).toFixed(3)} ${(X + R).toFixed(3)} ${Y.toFixed(3)} c ${(X + R).toFixed(3)} ${(Y - C).toFixed(3)} ${(X + C).toFixed(3)} ${(Y - R).toFixed(3)} ${X.toFixed(3)} ${(Y - R).toFixed(3)} c ${(X - C).toFixed(3)} ${(Y - R).toFixed(3)} ${(X - R).toFixed(3)} ${(Y - C).toFixed(3)} ${(X - R).toFixed(3)} ${Y.toFixed(3)} c ${(X - R).toFixed(3)} ${(Y + C).toFixed(3)} ${(X - C).toFixed(3)} ${(Y + R).toFixed(3)} ${X.toFixed(3)} ${(Y + R).toFixed(3)} c f`);
  };

  fill("#ffffff");
  commands.push(`0 0 ${pageW} ${pageH} re f`);
  text(width / 2, 30, "NetGlycate-predicted glycation-prone lysine sites in beta-LG", 18, "#202124", "center");

  [-1, -0.5, 0, 0.5, 1].forEach((tick) => {
    const y = yScale(tick);
    line(margin.left, y, width - margin.right, y, tick === 0 ? "#7a7f85" : "#e3e1dc", tick === 0 ? 1.2 : 0.8);
    text(margin.left - 12, y + 4, tick.toFixed(tick === 0 ? 0 : 1), 10, "#4f555b", "right");
  });

  for (const [position, score, predicted] of data) {
    const x = xScale(position), y0 = yScale(0), y = yScale(score);
    const color = predicted ? "#e67e22" : "#9aa0a6";
    line(x, y0, x, y, color, predicted ? 2.2 : 1.5);
    circle(x, y, predicted ? 4.4 : 3.4, color);
    if (predicted) text(x, y - 10, `K${position}`, 10, "#202124", "center");
  }

  const xAxisY = yScale(yMin);
  line(margin.left, xAxisY, width - margin.right, xAxisY, "#202124", 1.2);
  line(margin.left, margin.top, margin.left, xAxisY, "#202124", 1.2);
  [0, 20, 40, 60, 80, 100, 120, 140, 160].forEach((tick) => {
    const x = xScale(tick);
    line(x, xAxisY, x, xAxisY + 5, "#202124", 1);
    text(x, xAxisY + 22, String(tick), 10, "#202124", "center");
  });
  text(margin.left + plotW / 2, height - 16, "Sequence position", 12, "#202124", "center");
  text(8, margin.top + plotH / 2, "NetGlycate score", 12, "#202124", "left");

  const legendX = 92, legendY = 304;
  line(legendX, legendY, legendX + 26, legendY, "#9aa0a6", 1.5);
  circle(legendX + 13, legendY, 3.6, "#9aa0a6");
  text(legendX + 36, legendY + 4, "Other lysine residues", 10, "#202124");
  line(legendX + 210, legendY, legendX + 236, legendY, "#e67e22", 2.2);
  circle(legendX + 223, legendY, 4.2, "#e67e22");
  text(legendX + 246, legendY + 4, "Predicted glycation-prone sites (YES)", 10, "#202124");
  line(legendX + 508, legendY, legendX + 534, legendY, "#7a7f85", 1.2);
  text(legendX + 544, legendY + 4, "Threshold = 0", 10, "#202124");

  const stream = commands.join("\n");
  const objects = [
    "<< /Type /Catalog /Pages 2 0 R >>",
    "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
    `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${pageW} ${pageH}] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>`,
    "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    `<< /Length ${Buffer.byteLength(stream)} >>\nstream\n${stream}\nendstream`,
  ];
  let pdf = "%PDF-1.4\n";
  const offsets = [0];
  objects.forEach((obj, i) => {
    offsets.push(Buffer.byteLength(pdf));
    pdf += `${i + 1} 0 obj\n${obj}\nendobj\n`;
  });
  const xref = Buffer.byteLength(pdf);
  pdf += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n`;
  offsets.slice(1).forEach((o) => {
    pdf += `${String(o).padStart(10, "0")} 00000 n \n`;
  });
  pdf += `trailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xref}\n%%EOF\n`;
  return pdf;
}

fs.writeFileSync(svgPath, buildSvg(), "utf8");
fs.writeFileSync(pdfPath, buildPdf(), "binary");
console.log(`Wrote ${svgPath}`);
console.log(`Wrote ${pdfPath}`);
console.log("PNG export: open the SVG in the browser and screenshot, or use the browser plugin workflow.");
