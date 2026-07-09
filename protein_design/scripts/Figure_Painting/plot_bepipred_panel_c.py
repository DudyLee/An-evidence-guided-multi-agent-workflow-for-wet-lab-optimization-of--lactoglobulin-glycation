from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from figure_palette import GRID, INK, MUTED, PALETTE, WHITE, blend


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_INPUT = REPO_ROOT / "data" / "bepipred_data" / "bepipred3_results" / "raw_output.csv"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "evidence_stats"

# Threshold displayed by the BepiPred-3.0 interactive export used for the original panel.
DEFAULT_THRESHOLD = 0.1512

# Regions described in the manuscript text for Fig. 2c.
DEFAULT_WINDOWS = [(61, 69), (110, 115), (130, 148)]
DEFAULT_KEY_LYSINES = [69, 77]

# Original plasma-like palette for the BepiPred bar heatmap, ordered from low
# to high score.
COLOR_STOPS = [
    (0.00, "#2D0A80"),
    (0.25, "#8A209C"),
    (0.50, "#D95F02"),
    (0.75, "#F5B43F"),
    (1.00, "#F4F921"),
]

THRESHOLD_COLOR = "#335C67"
WINDOW_FILL = "#F5E8BF"
WINDOW_EDGE = "#D6AA42"
WINDOW_LABEL = "#6B5315"
LYSINE_COLOR = "#D95F02"


def load_rows(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for idx, row in enumerate(reader, start=1):
            rows.append(
                {
                    "position": idx,
                    "residue": str(row["Residue"]).strip(),
                    "score": float(str(row["BepiPred-3.0 score"]).strip()),
                    "linear_score": float(
                        str(row["BepiPred-3.0 linear epitope score"]).strip()
                    ),
                }
            )
    return rows


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def score_color(score: float, vmin: float, vmax: float) -> str:
    if vmax <= vmin:
        t = 0.0
    else:
        t = max(0.0, min(1.0, (score - vmin) / (vmax - vmin)))

    for idx in range(len(COLOR_STOPS) - 1):
        left_t, left_hex = COLOR_STOPS[idx]
        right_t, right_hex = COLOR_STOPS[idx + 1]
        if left_t <= t <= right_t:
            local_t = (t - left_t) / (right_t - left_t)
            left_rgb = hex_to_rgb(left_hex)
            right_rgb = hex_to_rgb(right_hex)
            return rgb_to_hex(
                tuple(
                    int(round(lerp(left_rgb[channel], right_rgb[channel], local_t)))
                    for channel in range(3)
                )
            )
    return COLOR_STOPS[-1][1]


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


class PanelGeometry:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.left = 132
        self.right = 250
        self.top = 130
        self.bottom = 230
        self.plot_w = width - self.left - self.right
        self.plot_h = height - self.top - self.bottom
        self.x_min = 1
        self.x_max = 162
        self.y_min = 0.0
        self.y_max = 0.32

    def sx(self, x: float) -> float:
        return self.left + ((x - self.x_min) / (self.x_max - self.x_min)) * self.plot_w

    def sy(self, y: float) -> float:
        return self.top + ((self.y_max - y) / (self.y_max - self.y_min)) * self.plot_h


def parse_windows(value: str) -> list[tuple[int, int]]:
    windows: list[tuple[int, int]] = []
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        if "-" not in item:
            position = int(item)
            windows.append((position, position))
            continue
        start, end = item.split("-", 1)
        windows.append((int(start), int(end)))
    return windows


def draw_png(
    rows: list[dict[str, object]],
    output_path: Path,
    threshold: float,
    windows: list[tuple[int, int]],
    key_lysines: list[int],
    vmin: float,
    vmax: float,
    scale: int = 2,
) -> None:
    geom = PanelGeometry(width=1800 * scale, height=920 * scale)
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
    tick_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 36 * scale)
    small_font = find_font(["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"], 32 * scale)
    small_bold = find_font(["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"], 32 * scale)

    ink = INK
    muted = MUTED
    grid = GRID
    threshold_color = THRESHOLD_COLOR
    band_fill = WINDOW_FILL
    band_edge = WINDOW_EDGE
    lysine_color = LYSINE_COLOR

    draw_text_centered(
        draw,
        (geom.width / 2, s(52)),
        "BepiPred-3.0 epitope scores across beta-LG",
        title_font,
        ink,
    )

    # High-priority windows behind the bars, plus top labels.
    for start, end in windows:
        x0 = geom.sx(start - 0.5)
        x1 = geom.sx(end + 0.5)
        draw.rounded_rectangle(
            [(x0, geom.top), (x1, geom.top + geom.plot_h)],
            radius=int(s(7)),
            fill=band_fill,
        )
        draw.line([(x0, geom.top), (x0, geom.top + geom.plot_h)], fill=band_edge, width=int(s(2)))
        draw.line([(x1, geom.top), (x1, geom.top + geom.plot_h)], fill=band_edge, width=int(s(2)))
        draw_text_centered(
            draw,
            ((x0 + x1) / 2, geom.top - s(28)),
            f"{start}-{end}",
            small_bold,
            WINDOW_LABEL,
        )

    for tick in [0.00, 0.10, 0.20, 0.30]:
        y = geom.sy(tick)
        draw.line([(geom.left, y), (geom.left + geom.plot_w, y)], fill=grid, width=int(s(2)))
        draw_text_right(draw, (geom.left - s(16), y), f"{tick:.2f}", tick_font, muted)

    # Bars colored by BepiPred score.
    step = geom.plot_w / len(rows)
    bar_w = step * 0.78
    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        x_mid = geom.sx(position)
        x0 = x_mid - bar_w / 2
        x1 = x_mid + bar_w / 2
        y0 = geom.sy(0.0)
        y1 = geom.sy(score)
        draw.rectangle([(x0, y1), (x1, y0)], fill=score_color(score, vmin, vmax))

    # Threshold line, drawn after bars so it remains visible.
    y_threshold = geom.sy(threshold)
    dash = int(s(14))
    gap = int(s(8))
    x = geom.left
    while x < geom.left + geom.plot_w:
        draw.line(
            [(x, y_threshold), (min(x + dash, geom.left + geom.plot_w), y_threshold)],
            fill=threshold_color,
            width=int(s(3)),
        )
        x += dash + gap

    # Key lysine labels.
    label_offsets = {69: (-8, -34), 77: (18, -36)}
    for position in key_lysines:
        row = rows[position - 1]
        score = float(row["score"])
        px = geom.sx(position)
        py = geom.sy(score)
        radius = s(8)
        draw.ellipse(
            [(px - radius, py - radius), (px + radius, py + radius)],
            fill=WHITE,
            outline=lysine_color,
            width=int(s(3)),
        )
        dx, dy = label_offsets.get(position, (0, -34))
        draw.line([(px, py - s(11)), (px + s(dx), py + s(dy + 12))], fill=lysine_color, width=int(s(2)))
        draw_text_centered(draw, (px + s(dx), py + s(dy - 3)), f"K{position}", small_bold, lysine_color)

    # Axes and ticks.
    draw.line(
        [(geom.left, geom.top + geom.plot_h), (geom.left + geom.plot_w, geom.top + geom.plot_h)],
        fill=ink,
        width=int(s(3)),
    )
    draw.line([(geom.left, geom.top), (geom.left, geom.top + geom.plot_h)], fill=ink, width=int(s(3)))
    for tick in [1, 20, 40, 60, 80, 100, 120, 140, 160]:
        x_tick = geom.sx(tick)
        draw.line(
            [(x_tick, geom.top + geom.plot_h), (x_tick, geom.top + geom.plot_h + s(10))],
            fill=ink,
            width=int(s(2)),
        )
        draw_text_centered(draw, (x_tick, geom.top + geom.plot_h + s(42)), str(tick), tick_font, ink)

    draw.text((s(22), geom.top - s(28)), "BepiPred-3.0 score", font=label_font, fill=ink)
    draw_text_centered(
        draw,
        (geom.left + geom.plot_w / 2, geom.top + geom.plot_h + s(92)),
        "Sequence position",
        label_font,
        ink,
    )

    # Colorbar.
    cb_x0 = geom.left + geom.plot_w + s(74)
    cb_x1 = cb_x0 + s(32)
    cb_y0 = geom.top + s(25)
    cb_y1 = geom.top + geom.plot_h - s(20)
    for i in range(int(cb_y1 - cb_y0) + 1):
        frac = 1 - i / max(1, (cb_y1 - cb_y0))
        value = vmin + (vmax - vmin) * frac
        color = score_color(value, vmin, vmax)
        y = cb_y0 + i
        draw.line([(cb_x0, y), (cb_x1, y)], fill=color, width=1)
    draw.rectangle([(cb_x0, cb_y0), (cb_x1, cb_y1)], outline="#d0d0d0", width=int(s(1)))
    draw_text_centered(draw, ((cb_x0 + cb_x1) / 2, cb_y0 - s(30)), "Score", small_bold, ink)
    for tick in [vmin, threshold, 0.20, 0.25, 0.30]:
        if tick < vmin or tick > vmax:
            continue
        y = cb_y1 - ((tick - vmin) / (vmax - vmin)) * (cb_y1 - cb_y0)
        draw.line([(cb_x1, y), (cb_x1 + s(8), y)], fill=ink, width=int(s(1)))
        draw.text((cb_x1 + s(16), y - s(13)), f"{tick:.2f}", font=small_font, fill=ink)

    # Minimal legend.
    legend_y = geom.top + geom.plot_h + s(156)
    legend_x = geom.left + s(10)
    draw.line([(legend_x, legend_y), (legend_x + s(44), legend_y)], fill=threshold_color, width=int(s(3)))
    draw.text((legend_x + s(58), legend_y - s(17)), f"threshold {threshold:.4f}", font=small_font, fill=ink)

    lx2 = legend_x + s(425)
    draw.rounded_rectangle(
        [(lx2, legend_y - s(16)), (lx2 + s(44), legend_y + s(16))],
        radius=int(s(5)),
        fill=band_fill,
        outline=band_edge,
        width=int(s(2)),
    )
    draw.text((lx2 + s(58), legend_y - s(17)), "high-prior windows", font=small_font, fill=ink)

    lx3 = legend_x + s(840)
    draw.ellipse(
        [(lx3, legend_y - s(8)), (lx3 + s(16), legend_y + s(8))],
        fill=WHITE,
        outline=lysine_color,
        width=int(s(3)),
    )
    draw.text((lx3 + s(30), legend_y - s(17)), "Lysine residues", font=small_font, fill=ink)

    image.save(output_path)


def build_svg(
    rows: list[dict[str, object]],
    threshold: float,
    windows: list[tuple[int, int]],
    key_lysines: list[int],
    vmin: float,
    vmax: float,
) -> str:
    geom = PanelGeometry(width=1800, height=920)

    def esc(value: object) -> str:
        return (
            str(value)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    def line(x1, y1, x2, y2, color, width=1.0, dash: str | None = None) -> str:
        dash_part = f' stroke-dasharray="{dash}"' if dash else ""
        return (
            f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" '
            f'stroke="{color}" stroke-width="{width:.2f}" stroke-linecap="round"{dash_part}/>'
        )

    def text(x, y, value, size=18, anchor="middle", weight=400, color=INK) -> str:
        return (
            f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" '
            f'font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}">{esc(value)}</text>'
        )

    parts: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{geom.width}" height="{geom.height}" viewBox="0 0 {geom.width} {geom.height}">',
        "<defs>",
        '<linearGradient id="scoreGradient" x1="0%" y1="100%" x2="0%" y2="0%">',
        *[
            f'<stop offset="{frac * 100:.1f}%" stop-color="{color}"/>'
            for frac, color in COLOR_STOPS
        ],
        "</linearGradient>",
        "</defs>",
        f'<rect width="100%" height="100%" fill="{WHITE}"/>',
        text(geom.width / 2, 62, "BepiPred-3.0 epitope scores across beta-LG", 48, "middle", 700),
    ]

    for start, end in windows:
        x0 = geom.sx(start - 0.5)
        x1 = geom.sx(end + 0.5)
        parts.append(
            f'<rect x="{x0:.2f}" y="{geom.top:.2f}" width="{x1 - x0:.2f}" height="{geom.plot_h:.2f}" rx="7" fill="{WINDOW_FILL}"/>'
        )
        parts.append(line(x0, geom.top, x0, geom.top + geom.plot_h, WINDOW_EDGE, 2))
        parts.append(line(x1, geom.top, x1, geom.top + geom.plot_h, WINDOW_EDGE, 2))
        parts.append(text((x0 + x1) / 2, geom.top - 20, f"{start}-{end}", 30, "middle", 700, WINDOW_LABEL))

    for tick in [0.00, 0.10, 0.20, 0.30]:
        y = geom.sy(tick)
        parts.append(line(geom.left, y, geom.left + geom.plot_w, y, GRID, 1.2))
        parts.append(text(geom.left - 16, y + 12, f"{tick:.2f}", 36, "end", 400, MUTED))

    step = geom.plot_w / len(rows)
    bar_w = step * 0.78
    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        x_mid = geom.sx(position)
        x0 = x_mid - bar_w / 2
        y1 = geom.sy(score)
        y0 = geom.sy(0.0)
        parts.append(
            f'<rect x="{x0:.2f}" y="{y1:.2f}" width="{bar_w:.2f}" height="{y0 - y1:.2f}" fill="{score_color(score, vmin, vmax)}"/>'
        )

    parts.append(
        line(
            geom.left,
            geom.sy(threshold),
            geom.left + geom.plot_w,
            geom.sy(threshold),
            THRESHOLD_COLOR,
            2.4,
            "14 8",
        )
    )

    for position, (dx, dy) in {69: (-8, -34), 77: (18, -36)}.items():
        row = rows[position - 1]
        px = geom.sx(position)
        py = geom.sy(float(row["score"]))
        parts.append(
            f'<circle cx="{px:.2f}" cy="{py:.2f}" r="8" fill="{WHITE}" stroke="{LYSINE_COLOR}" stroke-width="3"/>'
        )
        parts.append(line(px, py - 11, px + dx, py + dy + 12, LYSINE_COLOR, 2))
        parts.append(text(px + dx, py + dy + 5, f"K{position}", 32, "middle", 700, LYSINE_COLOR))

    parts.append(line(geom.left, geom.top + geom.plot_h, geom.left + geom.plot_w, geom.top + geom.plot_h, INK, 2.2))
    parts.append(line(geom.left, geom.top, geom.left, geom.top + geom.plot_h, INK, 2.2))
    for tick in [1, 20, 40, 60, 80, 100, 120, 140, 160]:
        x_tick = geom.sx(tick)
        parts.append(line(x_tick, geom.top + geom.plot_h, x_tick, geom.top + geom.plot_h + 10, INK, 1.8))
        parts.append(text(x_tick, geom.top + geom.plot_h + 52, str(tick), 36))

    parts.append(text(22, geom.top - 20, "BepiPred-3.0 score", 36, "start"))
    parts.append(text(geom.left + geom.plot_w / 2, geom.top + geom.plot_h + 106, "Sequence position", 36))

    cb_x0 = geom.left + geom.plot_w + 74
    cb_x1 = cb_x0 + 32
    cb_y0 = geom.top + 25
    cb_y1 = geom.top + geom.plot_h - 20
    parts.append(
        f'<rect x="{cb_x0:.2f}" y="{cb_y0:.2f}" width="{cb_x1 - cb_x0:.2f}" height="{cb_y1 - cb_y0:.2f}" fill="url(#scoreGradient)" stroke="#d0d0d0" stroke-width="1"/>'
    )
    parts.append(text((cb_x0 + cb_x1) / 2, cb_y0 - 26, "Score", 32, "middle", 700))
    for tick in [vmin, threshold, 0.20, 0.25, 0.30]:
        if tick < vmin or tick > vmax:
            continue
        y = cb_y1 - ((tick - vmin) / (vmax - vmin)) * (cb_y1 - cb_y0)
        parts.append(line(cb_x1, y, cb_x1 + 8, y, INK, 1))
        parts.append(text(cb_x1 + 16, y + 12, f"{tick:.2f}", 32, "start"))

    legend_y = geom.top + geom.plot_h + 156
    legend_x = geom.left + 10
    parts.append(line(legend_x, legend_y, legend_x + 44, legend_y, THRESHOLD_COLOR, 2.4))
    parts.append(text(legend_x + 58, legend_y + 14, f"threshold {threshold:.4f}", 32, "start"))
    parts.append(
        f'<rect x="{legend_x + 425:.2f}" y="{legend_y - 16:.2f}" width="44" height="32" rx="5" fill="{WINDOW_FILL}" stroke="{WINDOW_EDGE}" stroke-width="2"/>'
    )
    parts.append(text(legend_x + 483, legend_y + 14, "high-prior windows", 32, "start"))
    parts.append(
        f'<circle cx="{legend_x + 848:.2f}" cy="{legend_y:.2f}" r="8" fill="{WHITE}" stroke="{LYSINE_COLOR}" stroke-width="3"/>'
    )
    parts.append(text(legend_x + 870, legend_y + 14, "Lysine residues", 32, "start"))

    parts.append("</svg>")
    return "\n".join(parts)


def draw_pdf(
    rows: list[dict[str, object]],
    output_path: Path,
    threshold: float,
    windows: list[tuple[int, int]],
    key_lysines: list[int],
    vmin: float,
    vmax: float,
) -> None:
    geom = PanelGeometry(width=900, height=470)
    geom.left = 66
    geom.right = 126
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
        text: str,
        size: float = 9,
        font: str = "Helvetica",
        fill: str = INK,
        anchor: str = "middle",
    ) -> None:
        pdf.setFont(font, size)
        set_fill(pdf, fill)
        width = pdf.stringWidth(text, font, size)
        if anchor == "middle":
            x -= width / 2
        elif anchor == "end":
            x -= width
        pdf.drawString(x, py(y), text)

    def draw_line(
        pdf: canvas.Canvas,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke: str,
        width: float = 1,
        dash: tuple[float, float] | None = None,
    ) -> None:
        set_stroke(pdf, stroke)
        pdf.setLineWidth(width)
        if dash:
            pdf.setDash(dash[0], dash[1])
        else:
            pdf.setDash()
        pdf.line(x1, py(y1), x2, py(y2))
        pdf.setDash()

    def draw_rect(
        pdf: canvas.Canvas,
        x: float,
        y: float,
        width: float,
        height: float,
        fill: str,
        stroke: str | None = None,
        stroke_width: float = 1,
    ) -> None:
        set_fill(pdf, fill)
        if stroke is None:
            pdf.setStrokeColor(colors.HexColor(fill))
            pdf.setLineWidth(0)
        else:
            set_stroke(pdf, stroke)
            pdf.setLineWidth(stroke_width)
        pdf.rect(x, py(y + height), width, height, stroke=1 if stroke else 0, fill=1)

    pdf = canvas.Canvas(str(output_path), pagesize=(geom.width, geom.height))
    pdf.setTitle("BepiPred-3.0 epitope scores across beta-LG")

    ink = INK
    muted = MUTED
    grid = GRID
    threshold_color = THRESHOLD_COLOR
    band_fill = WINDOW_FILL
    band_edge = WINDOW_EDGE
    lysine_color = LYSINE_COLOR

    draw_rect(pdf, 0, 0, geom.width, geom.height, WHITE)
    draw_text(
        pdf,
        geom.width / 2,
        34,
        "BepiPred-3.0 epitope scores across beta-LG",
        24,
        "Helvetica-Bold",
        ink,
    )

    for start, end in windows:
        x0 = geom.sx(start - 0.5)
        x1 = geom.sx(end + 0.5)
        draw_rect(pdf, x0, geom.top, x1 - x0, geom.plot_h, band_fill)
        draw_line(pdf, x0, geom.top, x0, geom.top + geom.plot_h, band_edge, 1)
        draw_line(pdf, x1, geom.top, x1, geom.top + geom.plot_h, band_edge, 1)
        draw_text(pdf, (x0 + x1) / 2, geom.top - 8, f"{start}-{end}", 16, "Helvetica-Bold", WINDOW_LABEL)

    for tick in [0.00, 0.10, 0.20, 0.30]:
        y = geom.sy(tick)
        draw_line(pdf, geom.left, y, geom.left + geom.plot_w, y, grid, 0.6)
        draw_text(pdf, geom.left - 8, y + 5.5, f"{tick:.2f}", 18, "Helvetica", muted, "end")

    step = geom.plot_w / len(rows)
    bar_w = step * 0.78
    for row in rows:
        position = int(row["position"])
        score = float(row["score"])
        x_mid = geom.sx(position)
        x0 = x_mid - bar_w / 2
        y1 = geom.sy(score)
        y0 = geom.sy(0.0)
        draw_rect(pdf, x0, y1, bar_w, y0 - y1, score_color(score, vmin, vmax))

    draw_line(
        pdf,
        geom.left,
        geom.sy(threshold),
        geom.left + geom.plot_w,
        geom.sy(threshold),
        threshold_color,
        1.2,
        (7, 4),
    )

    for position, (dx, dy) in {69: (-4, -17), 77: (9, -18)}.items():
        row = rows[position - 1]
        px = geom.sx(position)
        py_score = geom.sy(float(row["score"]))
        set_fill(pdf, WHITE)
        set_stroke(pdf, lysine_color)
        pdf.setLineWidth(1.5)
        pdf.circle(px, py(py_score), 4, stroke=1, fill=1)
        draw_line(pdf, px, py_score - 5.5, px + dx, py_score + dy + 6, lysine_color, 1)
        draw_text(pdf, px + dx, py_score + dy + 2, f"K{position}", 16, "Helvetica-Bold", lysine_color)

    draw_line(pdf, geom.left, geom.top + geom.plot_h, geom.left + geom.plot_w, geom.top + geom.plot_h, ink, 1.1)
    draw_line(pdf, geom.left, geom.top, geom.left, geom.top + geom.plot_h, ink, 1.1)
    for tick in [1, 20, 40, 60, 80, 100, 120, 140, 160]:
        x_tick = geom.sx(tick)
        draw_line(pdf, x_tick, geom.top + geom.plot_h, x_tick, geom.top + geom.plot_h + 5, ink, 0.9)
        draw_text(pdf, x_tick, geom.top + geom.plot_h + 24, str(tick), 18, "Helvetica", ink)

    draw_text(pdf, 11, geom.top - 5, "BepiPred-3.0 score", 18, "Helvetica", ink, "start")
    draw_text(pdf, geom.left + geom.plot_w / 2, geom.top + geom.plot_h + 54, "Sequence position", 18, "Helvetica", ink)

    cb_x0 = geom.left + geom.plot_w + 37
    cb_x1 = cb_x0 + 16
    cb_y0 = geom.top + 12.5
    cb_y1 = geom.top + geom.plot_h - 10
    steps = 220
    for i in range(steps):
        frac = 1 - i / max(1, steps - 1)
        value = vmin + (vmax - vmin) * frac
        y0 = cb_y0 + i * (cb_y1 - cb_y0) / steps
        y1 = cb_y0 + (i + 1) * (cb_y1 - cb_y0) / steps
        draw_rect(pdf, cb_x0, y0, cb_x1 - cb_x0, y1 - y0, score_color(value, vmin, vmax))
    draw_rect(pdf, cb_x0, cb_y0, cb_x1 - cb_x0, cb_y1 - cb_y0, WHITE, "#d0d0d0", 0.5)
    # Repaint gradient inside after border helper filled white.
    for i in range(steps):
        frac = 1 - i / max(1, steps - 1)
        value = vmin + (vmax - vmin) * frac
        y0 = cb_y0 + i * (cb_y1 - cb_y0) / steps
        y1 = cb_y0 + (i + 1) * (cb_y1 - cb_y0) / steps
        draw_rect(pdf, cb_x0, y0, cb_x1 - cb_x0, y1 - y0, score_color(value, vmin, vmax))
    draw_line(pdf, cb_x0, cb_y0, cb_x1, cb_y0, "#d0d0d0", 0.5)
    draw_line(pdf, cb_x0, cb_y1, cb_x1, cb_y1, "#d0d0d0", 0.5)
    draw_line(pdf, cb_x0, cb_y0, cb_x0, cb_y1, "#d0d0d0", 0.5)
    draw_line(pdf, cb_x1, cb_y0, cb_x1, cb_y1, "#d0d0d0", 0.5)
    draw_text(pdf, (cb_x0 + cb_x1) / 2, cb_y0 - 12, "Score", 16, "Helvetica-Bold", ink)
    for tick in [vmin, threshold, 0.20, 0.25, 0.30]:
        if tick < vmin or tick > vmax:
            continue
        y = cb_y1 - ((tick - vmin) / (vmax - vmin)) * (cb_y1 - cb_y0)
        draw_line(pdf, cb_x1, y, cb_x1 + 4, y, ink, 0.5)
        draw_text(pdf, cb_x1 + 7, y + 4.5, f"{tick:.2f}", 14, "Helvetica", ink, "start")

    legend_y = geom.top + geom.plot_h + 86
    legend_x = geom.left + 5
    draw_line(pdf, legend_x, legend_y, legend_x + 22, legend_y, threshold_color, 1.2)
    draw_text(pdf, legend_x + 29, legend_y + 6, f"threshold {threshold:.4f}", 18, "Helvetica", ink, "start")

    lx2 = legend_x + 230
    draw_rect(pdf, lx2, legend_y - 8, 22, 16, band_fill, band_edge, 0.8)
    draw_text(pdf, lx2 + 29, legend_y + 6, "high-prior windows", 18, "Helvetica", ink, "start")

    lx3 = legend_x + 500
    set_fill(pdf, WHITE)
    set_stroke(pdf, lysine_color)
    pdf.setLineWidth(1.5)
    pdf.circle(lx3 + 4, py(legend_y), 4, stroke=1, fill=1)
    draw_text(pdf, lx3 + 15, legend_y + 6, "Lysine residues", 18, "Helvetica", ink, "start")

    pdf.showPage()
    pdf.save()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Draw Fig. 2c as a static BepiPred-3.0 residue-level bar heatmap."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--basename", default="bepipred_panel_c")
    parser.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    parser.add_argument("--vmin", type=float, default=None)
    parser.add_argument("--vmax", type=float, default=0.30)
    parser.add_argument(
        "--windows",
        default=",".join(f"{start}-{end}" for start, end in DEFAULT_WINDOWS),
        help="Comma-separated high-prior windows, e.g. 61-69,110-115,130-148.",
    )
    parser.add_argument(
        "--key-lysines",
        default=",".join(str(position) for position in DEFAULT_KEY_LYSINES),
        help="Comma-separated lysine positions to label, e.g. 69,77.",
    )
    args = parser.parse_args()

    rows = load_rows(args.input)
    if not rows:
        raise RuntimeError(f"No BepiPred rows found in {args.input}")

    scores = [float(row["score"]) for row in rows]
    vmin = min(scores) if args.vmin is None else args.vmin
    vmax = args.vmax
    if vmax <= vmin:
        raise ValueError(f"--vmax must be greater than --vmin; got {vmax} <= {vmin}")

    windows = parse_windows(args.windows)
    key_lysines = [int(item.strip()) for item in args.key_lysines.split(",") if item.strip()]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    png_path = args.output_dir / f"{args.basename}.png"
    svg_path = args.output_dir / f"{args.basename}.svg"
    pdf_path = args.output_dir / f"{args.basename}.pdf"

    draw_png(rows, png_path, args.threshold, windows, key_lysines, vmin, vmax)
    svg_path.write_text(
        build_svg(rows, args.threshold, windows, key_lysines, vmin, vmax), encoding="utf-8"
    )
    draw_pdf(rows, pdf_path, args.threshold, windows, key_lysines, vmin, vmax)

    top_rows = sorted(rows, key=lambda row: float(row["score"]), reverse=True)[:12]
    print(f"Wrote {png_path}")
    print(f"Wrote {svg_path}")
    print(f"Wrote {pdf_path}")
    print(f"Residues: {len(rows)}; score range: {min(scores):.4f}-{max(scores):.4f}")
    print(
        "Top residues: "
        + ", ".join(
            f"{row['residue']}{row['position']}={float(row['score']):.3f}" for row in top_rows
        )
    )


if __name__ == "__main__":
    main()


