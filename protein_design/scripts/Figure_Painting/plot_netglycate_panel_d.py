from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from figure_palette import GRID, INK, MUTED, PALETTE, WHITE


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = REPO_ROOT / "data" / "netglycate_data" / "netglycate_results.csv"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "evidence_stats"
SEQUENCE_LENGTH = 162
THRESHOLD = 0.0

THRESHOLD_COLOR = "#7A7F85"
OTHER_LYSINE_COLOR = "#9AA0A6"
PREDICTED_LYSINE_COLOR = "#E67E22"


def load_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for encoding in ("utf-8-sig", "gbk"):
        try:
            text = path.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = path.read_text(encoding="utf-8-sig", errors="replace")

    reader = csv.DictReader(text.splitlines())
    for row in reader:
        if not row.get("Position"):
            continue
        score = float(str(row["Probability"]).strip())
        rows.append(
            {
                "position": int(str(row["Position"]).strip()),
                "residue": str(row["Residue"]).strip(),
                "score": score,
                "predicted": score >= THRESHOLD,
            }
        )
    return sorted(rows, key=lambda item: int(item["position"]))


def find_font(candidates: Iterable[str], size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    font_dirs = [
        Path("C:/Windows/Fonts"),
        Path("/usr/share/fonts/truetype/dejavu"),
        Path("/usr/share/fonts/truetype/liberation2"),
    ]
    for directory in font_dirs:
        for name in candidates:
            path = directory / name
            if path.exists():
                return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def text_size(
    draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont | ImageFont.ImageFont
) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def draw_text_centered(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
) -> None:
    width, height = text_size(draw, text, font)
    draw.text((xy[0] - width / 2, xy[1] - height / 2), text, font=font, fill=fill)


def draw_text_right(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    font: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: str,
) -> None:
    width, height = text_size(draw, text, font)
    draw.text((xy[0] - width, xy[1] - height / 2), text, font=font, fill=fill)


class Geometry:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.left = 132
        self.right = 78
        self.top = 130
        self.bottom = 230
        self.plot_w = width - self.left - self.right
        self.plot_h = height - self.top - self.bottom
        self.x_min = 0
        self.x_max = SEQUENCE_LENGTH + 5
        self.y_min = -1.10
        self.y_max = 1.05

    def sx(self, x: float) -> float:
        return self.left + ((x - self.x_min) / (self.x_max - self.x_min)) * self.plot_w

    def sy(self, y: float) -> float:
        return self.top + ((self.y_max - y) / (self.y_max - self.y_min)) * self.plot_h


def draw_png(rows: list[dict[str, object]], output_path: Path, scale: int = 2) -> None:
    geom = Geometry(1800 * scale, 920 * scale)
    geom.left *= scale
    geom.right *= scale
    geom.top *= scale
    geom.bottom *= scale
    geom.plot_w = geom.width - geom.left - geom.right
    geom.plot_h = geom.height - geom.top - geom.bottom

    def s(value: float) -> float:
        return value * scale

    image = Image.new("RGB", (geom.width, geom.height), WHITE)
    draw = ImageDraw.Draw(image)

    title_font = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 48 * scale)
    label_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 36 * scale)
    tick_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 34 * scale)
    legend_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 32 * scale)
    label_bold = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 32 * scale)

    ink = INK
    muted = MUTED
    grid = GRID
    threshold_color = THRESHOLD_COLOR
    other_color = OTHER_LYSINE_COLOR
    yes_color = PREDICTED_LYSINE_COLOR

    draw_text_centered(
        draw,
        (geom.width / 2, s(52)),
        "NetGlycate-predicted glycation-prone lysine sites in beta-LG",
        title_font,
        ink,
    )

    for tick in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y = geom.sy(tick)
        is_zero = tick == 0.0
        draw.line(
            [(geom.left, y), (geom.left + geom.plot_w, y)],
            fill=threshold_color if is_zero else grid,
            width=int(s(3 if is_zero else 2)),
        )
        draw_text_right(
            draw,
            (geom.left - s(16), y),
            "0" if is_zero else f"{tick:.1f}",
            tick_font,
            muted,
        )

    label_offsets = {
        14: (0, -48),
        47: (0, -48),
        70: (0, -48),
        100: (-28, -52),
        101: (32, -30),
    }

    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        predicted = bool(row["predicted"])
        x = geom.sx(position)
        y0 = geom.sy(0)
        y = geom.sy(score)
        color = yes_color if predicted else other_color
        draw.line([(x, y0), (x, y)], fill=color, width=int(s(6 if predicted else 4)))
        radius = s(9 if predicted else 7)
        draw.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color)
        if predicted:
            dx, dy = label_offsets.get(position, (0, -46))
            label_x = x + s(dx)
            label_y = y + s(dy)
            draw.line([(x, y - s(13)), (label_x, label_y + s(18))], fill=yes_color, width=int(s(2)))
            draw_text_centered(draw, (label_x, label_y), f"K{position}", label_bold, yes_color)

    x_axis_y = geom.sy(geom.y_min)
    draw.line([(geom.left, x_axis_y), (geom.left + geom.plot_w, x_axis_y)], fill=ink, width=int(s(3)))
    draw.line([(geom.left, geom.top), (geom.left, x_axis_y)], fill=ink, width=int(s(3)))

    for tick in [0, 20, 40, 60, 80, 100, 120, 140, 160]:
        x = geom.sx(tick)
        draw.line([(x, x_axis_y), (x, x_axis_y + s(10))], fill=ink, width=int(s(2)))
        draw_text_centered(draw, (x, x_axis_y + s(42)), str(tick), tick_font, ink)

    draw.text((s(22), geom.top - s(28)), "NetGlycate score", font=label_font, fill=ink)
    draw_text_centered(
        draw,
        (geom.left + geom.plot_w / 2, geom.top + geom.plot_h + s(92)),
        "Sequence position",
        label_font,
        ink,
    )

    legend_y = geom.top + geom.plot_h + s(156)
    legend_x = geom.left + s(10)

    draw.line([(legend_x, legend_y), (legend_x + s(44), legend_y)], fill=other_color, width=int(s(4)))
    draw.ellipse(
        [(legend_x + s(18), legend_y - s(7)), (legend_x + s(32), legend_y + s(7))],
        fill=other_color,
    )
    draw.text((legend_x + s(58), legend_y - s(17)), "Other lysine residues", font=legend_font, fill=ink)

    lx2 = legend_x + s(500)
    draw.line([(lx2, legend_y), (lx2 + s(44), legend_y)], fill=yes_color, width=int(s(6)))
    draw.ellipse([(lx2 + s(17), legend_y - s(9)), (lx2 + s(35), legend_y + s(9))], fill=yes_color)
    draw.text((lx2 + s(58), legend_y - s(17)), "Predicted glycation-prone sites", font=legend_font, fill=ink)

    lx3 = legend_x + s(1115)
    draw.line([(lx3, legend_y), (lx3 + s(44), legend_y)], fill=threshold_color, width=int(s(3)))
    draw.text((lx3 + s(58), legend_y - s(17)), "Threshold = 0", font=legend_font, fill=ink)

    image.save(output_path)


def build_svg(rows: list[dict[str, object]]) -> str:
    geom = Geometry(1800, 920)

    def esc(value: object) -> str:
        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def line(x1, y1, x2, y2, color, width=1.0) -> str:
        return (
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{color}" stroke-width="{width:.2f}" stroke-linecap="round"/>'
        )

    def text(x, y, value, size=32, anchor="middle", weight=400, color=INK) -> str:
        return (
            f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}">{esc(value)}</text>'
        )

    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{geom.width}" height="{geom.height}" viewBox="0 0 {geom.width} {geom.height}">',
        f'<rect width="100%" height="100%" fill="{WHITE}"/>',
        text(
            geom.width / 2,
            62,
            "NetGlycate-predicted glycation-prone lysine sites in beta-LG",
            48,
            "middle",
            700,
        ),
    ]

    for tick in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y = geom.sy(tick)
        is_zero = tick == 0
        parts.append(line(geom.left, y, geom.left + geom.plot_w, y, THRESHOLD_COLOR if is_zero else GRID, 3 if is_zero else 2))
        parts.append(text(geom.left - 16, y + 12, "0" if is_zero else f"{tick:.1f}", 34, "end", 400, MUTED))

    label_offsets = {14: (0, -48), 47: (0, -48), 70: (0, -48), 100: (-28, -52), 101: (32, -30)}
    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        predicted = bool(row["predicted"])
        x = geom.sx(position)
        y0 = geom.sy(0)
        y = geom.sy(score)
        color = PREDICTED_LYSINE_COLOR if predicted else OTHER_LYSINE_COLOR
        parts.append(line(x, y0, x, y, color, 6 if predicted else 4))
        r = 9 if predicted else 7
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{color}"/>')
        if predicted:
            dx, dy = label_offsets.get(position, (0, -46))
            parts.append(line(x, y - 13, x + dx, y + dy + 18, color, 2))
            parts.append(text(x + dx, y + dy + 10, f"K{position}", 32, "middle", 700, color))

    x_axis_y = geom.sy(geom.y_min)
    parts.append(line(geom.left, x_axis_y, geom.left + geom.plot_w, x_axis_y, INK, 3))
    parts.append(line(geom.left, geom.top, geom.left, x_axis_y, INK, 3))
    for tick in [0, 20, 40, 60, 80, 100, 120, 140, 160]:
        x = geom.sx(tick)
        parts.append(line(x, x_axis_y, x, x_axis_y + 10, INK, 2))
        parts.append(text(x, x_axis_y + 52, tick, 34))

    parts.append(text(22, geom.top - 20, "NetGlycate score", 36, "start"))
    parts.append(text(geom.left + geom.plot_w / 2, geom.top + geom.plot_h + 106, "Sequence position", 36))

    legend_y = geom.top + geom.plot_h + 156
    legend_x = geom.left + 10
    parts.append(line(legend_x, legend_y, legend_x + 44, legend_y, OTHER_LYSINE_COLOR, 4))
    parts.append(f'<circle cx="{legend_x + 25:.2f}" cy="{legend_y:.2f}" r="7" fill="{OTHER_LYSINE_COLOR}"/>')
    parts.append(text(legend_x + 58, legend_y + 14, "Other lysine residues", 32, "start"))

    lx2 = legend_x + 500
    parts.append(line(lx2, legend_y, lx2 + 44, legend_y, PREDICTED_LYSINE_COLOR, 6))
    parts.append(f'<circle cx="{lx2 + 26:.2f}" cy="{legend_y:.2f}" r="9" fill="{PREDICTED_LYSINE_COLOR}"/>')
    parts.append(text(lx2 + 58, legend_y + 14, "Predicted glycation-prone sites", 32, "start"))

    lx3 = legend_x + 1115
    parts.append(line(lx3, legend_y, lx3 + 44, legend_y, THRESHOLD_COLOR, 3))
    parts.append(text(lx3 + 58, legend_y + 14, "Threshold = 0", 32, "start"))

    parts.append("</svg>")
    return "\n".join(parts)


def draw_pdf(rows: list[dict[str, object]], output_path: Path) -> None:
    geom = Geometry(900, 470)
    geom.left = 66
    geom.right = 42
    geom.top = 68
    geom.bottom = 122
    geom.plot_w = geom.width - geom.left - geom.right
    geom.plot_h = geom.height - geom.top - geom.bottom

    def py(y: float) -> float:
        return geom.height - y

    def set_fill(pdf: canvas.Canvas, hex_color: str) -> None:
        pdf.setFillColor(colors.HexColor(hex_color))

    def set_stroke(pdf: canvas.Canvas, hex_color: str) -> None:
        pdf.setStrokeColor(colors.HexColor(hex_color))

    def draw_text(
        pdf: canvas.Canvas,
        x: float,
        y: float,
        value: str,
        size: float,
        font: str = "Helvetica",
        fill: str = INK,
        anchor: str = "middle",
    ) -> None:
        pdf.setFont(font, size)
        set_fill(pdf, fill)
        width = pdf.stringWidth(value, font, size)
        if anchor == "middle":
            x -= width / 2
        elif anchor == "end":
            x -= width
        pdf.drawString(x, py(y), value)

    def draw_line(pdf: canvas.Canvas, x1, y1, x2, y2, stroke, width=1.0) -> None:
        set_stroke(pdf, stroke)
        pdf.setLineWidth(width)
        pdf.line(x1, py(y1), x2, py(y2))

    def draw_circle(pdf: canvas.Canvas, x, y, r, fill) -> None:
        set_fill(pdf, fill)
        set_stroke(pdf, fill)
        pdf.circle(x, py(y), r, stroke=0, fill=1)

    pdf = canvas.Canvas(str(output_path), pagesize=(geom.width, geom.height))
    pdf.setTitle("NetGlycate-predicted glycation-prone lysine sites in beta-LG")

    ink = INK
    muted = MUTED
    grid = GRID
    threshold_color = THRESHOLD_COLOR
    other_color = OTHER_LYSINE_COLOR
    yes_color = PREDICTED_LYSINE_COLOR

    set_fill(pdf, WHITE)
    pdf.rect(0, 0, geom.width, geom.height, stroke=0, fill=1)

    draw_text(
        pdf,
        geom.width / 2,
        34,
        "NetGlycate-predicted glycation-prone lysine sites in beta-LG",
        24,
        "Helvetica-Bold",
        ink,
    )

    for tick in [-1.0, -0.5, 0.0, 0.5, 1.0]:
        y = geom.sy(tick)
        is_zero = tick == 0.0
        draw_line(pdf, geom.left, y, geom.left + geom.plot_w, y, threshold_color if is_zero else grid, 1.2 if is_zero else 0.8)
        draw_text(pdf, geom.left - 8, y + 5.5, "0" if is_zero else f"{tick:.1f}", 18, "Helvetica", muted, "end")

    label_offsets = {14: (0, -24), 47: (0, -24), 70: (0, -24), 100: (-16, -27), 101: (20, -12)}
    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        predicted = bool(row["predicted"])
        x = geom.sx(position)
        y0 = geom.sy(0)
        y = geom.sy(score)
        color = yes_color if predicted else other_color
        draw_line(pdf, x, y0, x, y, color, 3.0 if predicted else 2.0)
        draw_circle(pdf, x, y, 4.8 if predicted else 3.8, color)
        if predicted:
            dx, dy = label_offsets.get(position, (0, -23))
            label_x = x + dx
            label_y = y + dy
            draw_line(pdf, x, y - 6.5, label_x, label_y + 9, color, 1.0)
            draw_text(pdf, label_x, label_y + 2, f"K{position}", 16, "Helvetica-Bold", color)

    x_axis_y = geom.sy(geom.y_min)
    draw_line(pdf, geom.left, x_axis_y, geom.left + geom.plot_w, x_axis_y, ink, 1.2)
    draw_line(pdf, geom.left, geom.top, geom.left, x_axis_y, ink, 1.2)
    for tick in [0, 20, 40, 60, 80, 100, 120, 140, 160]:
        x = geom.sx(tick)
        draw_line(pdf, x, x_axis_y, x, x_axis_y + 5, ink, 0.9)
        draw_text(pdf, x, x_axis_y + 24, str(tick), 18, "Helvetica", ink)

    draw_text(pdf, 11, geom.top - 5, "NetGlycate score", 18, "Helvetica", ink, "start")
    draw_text(pdf, geom.left + geom.plot_w / 2, geom.top + geom.plot_h + 54, "Sequence position", 18, "Helvetica", ink)

    legend_y = geom.top + geom.plot_h + 86
    legend_x = geom.left + 5
    draw_line(pdf, legend_x, legend_y, legend_x + 22, legend_y, other_color, 2)
    draw_circle(pdf, legend_x + 11, legend_y, 3.8, other_color)
    draw_text(pdf, legend_x + 29, legend_y + 6, "Other lysine residues", 18, "Helvetica", ink, "start")

    lx2 = legend_x + 230
    draw_line(pdf, lx2, legend_y, lx2 + 22, legend_y, yes_color, 3)
    draw_circle(pdf, lx2 + 11, legend_y, 4.8, yes_color)
    draw_text(pdf, lx2 + 29, legend_y + 6, "Predicted glycation-prone sites", 18, "Helvetica", ink, "start")

    lx3 = legend_x + 540
    draw_line(pdf, lx3, legend_y, lx3 + 22, legend_y, threshold_color, 1.2)
    draw_text(pdf, lx3 + 29, legend_y + 6, "Threshold = 0", 18, "Helvetica", ink, "start")

    pdf.showPage()
    pdf.save()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Draw Fig. 2d NetGlycate sequence-prior panel from netglycate_results.csv."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--basename", default="netglycate_panel_d")
    args = parser.parse_args()

    rows = load_rows(args.input)
    if not rows:
        raise RuntimeError(f"No NetGlycate rows found in {args.input}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    png_path = args.output_dir / f"{args.basename}.png"
    svg_path = args.output_dir / f"{args.basename}.svg"
    pdf_path = args.output_dir / f"{args.basename}.pdf"

    draw_png(rows, png_path)
    svg_path.write_text(build_svg(rows), encoding="utf-8")
    draw_pdf(rows, pdf_path)

    predicted = [row for row in rows if bool(row["predicted"])]
    print(f"Wrote {png_path}")
    print(f"Wrote {svg_path}")
    print(f"Wrote {pdf_path}")
    print(
        "Predicted sites: "
        + ", ".join(f"K{row['position']}={float(row['score']):.3f}" for row in predicted)
    )


if __name__ == "__main__":
    main()


