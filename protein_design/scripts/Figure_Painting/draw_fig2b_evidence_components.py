from __future__ import annotations

import html
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


REPO_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = REPO_ROOT / "protein_design" / "figures" / "fig2b_components"

INK = "#202124"
MUTED = "#5F6368"
BLUE = "#2F69B1"
BLUE_DARK = "#143E7D"
BLUE_LIGHT = "#EAF3FF"
CYAN = "#49C2D9"
GREEN = "#4E7D3A"
GRID = "#DDE7F5"
GREY_FILL = "#F7F9FC"
GREY_LINE = "#A8ADB5"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = (
        ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"]
        if bold
        else ["arial.ttf", "Arial.ttf", "DejaVuSans.ttf"]
    )
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def esc(text: str) -> str:
    return html.escape(text, quote=True)


class Svg:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.items: list[str] = []

    def add(self, raw: str) -> None:
        self.items.append(raw)

    def text(
        self,
        x: float,
        y: float,
        text: str,
        size: int = 24,
        fill: str = INK,
        weight: str = "400",
        anchor: str = "start",
    ) -> None:
        self.add(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}">{esc(text)}</text>'
        )

    def rect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        fill: str = WHITE,
        stroke: str = BLUE,
        sw: float = 2,
        rx: float = 12,
        dash: str | None = None,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.1f}"{dash_attr}/>'
        )

    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        stroke: str = BLUE,
        sw: float = 2,
        dash: str | None = None,
    ) -> None:
        dash_attr = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw:.1f}" stroke-linecap="round"{dash_attr}/>'
        )

    def circle(self, cx: float, cy: float, r: float, fill: str = WHITE, stroke: str = BLUE, sw: float = 2) -> None:
        self.add(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw:.1f}"/>'
        )

    def path(self, d: str, fill: str = "none", stroke: str = BLUE, sw: float = 2) -> None:
        self.add(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw:.1f}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>'
        )

    def save(self, path: Path) -> None:
        content = "\n".join(self.items)
        path.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}">\n'
            f'<rect width="100%" height="100%" fill="white"/>\n{content}\n</svg>\n',
            encoding="utf-8",
        )


def draw_doc_icon(svg: Svg, x: float, y: float, size: float = 42, color: str = BLUE_DARK) -> None:
    w, h = size * 0.72, size
    svg.path(f"M{x} {y} H{x+w*0.68} L{x+w} {y+h*0.28} V{y+h} H{x} Z", stroke=color, sw=2)
    svg.line(x + w * 0.68, y, x + w * 0.68, y + h * 0.28, color, 2)
    svg.line(x + w * 0.68, y + h * 0.28, x + w, y + h * 0.28, color, 2)
    for i in range(3):
        svg.line(x + w * 0.18, y + h * (0.45 + i * 0.16), x + w * 0.78, y + h * (0.45 + i * 0.16), color, 2)


def draw_people_icon(svg: Svg, x: float, y: float, color: str = BLUE_DARK) -> None:
    svg.circle(x + 20, y + 13, 8, stroke=color)
    svg.circle(x + 4, y + 20, 6, stroke=color)
    svg.circle(x + 36, y + 20, 6, stroke=color)
    svg.path(f"M{x+6} {y+42} C{x+8} {y+28}, {x+32} {y+28}, {x+34} {y+42}", stroke=color, sw=2)
    svg.path(f"M{x-5} {y+42} C{x-4} {y+32}, {x+10} {y+32}, {x+12} {y+42}", stroke=color, sw=2)
    svg.path(f"M{x+28} {y+42} C{x+30} {y+32}, {x+44} {y+32}, {x+45} {y+42}", stroke=color, sw=2)


def draw_pipette_icon(svg: Svg, x: float, y: float, color: str = BLUE_DARK) -> None:
    svg.path(f"M{x+9} {y+42} L{x+38} {y+13}", stroke=color, sw=3)
    svg.path(f"M{x+31} {y+6} L{x+45} {y+20}", stroke=color, sw=3)
    svg.path(f"M{x+32} {y+19} L{x+24} {y+11}", stroke=color, sw=3)
    svg.circle(x + 7, y + 46, 3, fill=color, stroke=color)
    svg.circle(x + 2, y + 36, 2, fill=color, stroke=color)


def draw_bar_icon(svg: Svg, x: float, y: float, color: str = BLUE_DARK) -> None:
    for idx, h in enumerate([18, 30, 42]):
        bx = x + idx * 13
        svg.rect(bx, y + 48 - h, 8, h, fill=BLUE_LIGHT, stroke=color, sw=2, rx=1)
    svg.line(x - 3, y + 48, x + 44, y + 48, color, 2)


def draw_shield_icon(svg: Svg, x: float, y: float, color: str = BLUE_DARK) -> None:
    svg.path(
        f"M{x+21} {y+3} L{x+40} {y+12} V{y+28} C{x+40} {y+39}, {x+30} {y+48}, {x+21} {y+52} "
        f"C{x+12} {y+48}, {x+2} {y+39}, {x+2} {y+28} V{y+12} Z",
        stroke=color,
        sw=2,
    )
    svg.path(f"M{x+12} {y+28} L{x+19} {y+35} L{x+31} {y+20}", stroke=color, sw=3)


def draw_database_icon(svg: Svg, x: float, y: float, color: str = BLUE_DARK) -> None:
    svg.add(f'<ellipse cx="{x+32:.1f}" cy="{y+10:.1f}" rx="30" ry="10" fill="{BLUE_LIGHT}" stroke="{color}" stroke-width="2"/>')
    svg.path(f"M{x+2} {y+10} V{y+52} C{x+2} {y+66}, {x+62} {y+66}, {x+62} {y+52} V{y+10}", stroke=color, sw=2)
    for yy in [24, 38, 52]:
        svg.add(f'<ellipse cx="{x+32:.1f}" cy="{y+yy:.1f}" rx="30" ry="10" fill="none" stroke="{color}" stroke-width="2"/>')


def data_extraction_svg() -> Svg:
    svg = Svg(620, 620)
    svg.rect(34, 28, 552, 504, fill="none", stroke=BLUE, sw=2, rx=18, dash="8 9")

    rows = [
        ("doc", "Define study unit", "paper, run, and comparator"),
        ("people", "Capture conditions", "donor, mode, temperature, time,\nratio, pH/aw, pretreatment"),
        ("pipette", "Capture assay context", "assay type, target, readout, unit"),
        ("bar", "Record outcome", "treated value, control value,\nreported reduction"),
        ("shield", "Standardize and QC", "harmonize fields, link comparators,\nflag missing values"),
    ]
    x, y = 78, 52
    row_w, row_h, gap = 462, 80, 14
    for idx, (icon, title, body) in enumerate(rows):
        top = y + idx * (row_h + gap)
        svg.rect(x, top, row_w, row_h, fill=WHITE, stroke=BLUE, sw=2, rx=12)
        svg.line(x + 88, top + 12, x + 88, top + row_h - 12, stroke=BLUE, sw=1.5)
        if icon == "doc":
            draw_doc_icon(svg, x + 32, top + 14, 38)
        elif icon == "people":
            draw_people_icon(svg, x + 30, top + 13)
        elif icon == "pipette":
            draw_pipette_icon(svg, x + 27, top + 9)
        elif icon == "bar":
            draw_bar_icon(svg, x + 30, top + 12)
        else:
            draw_shield_icon(svg, x + 29, top + 9)
        svg.text(x + 106, top + 30, title, size=18, fill=BLUE_DARK, weight="700")
        for line_no, line in enumerate(body.split("\n")):
            svg.text(x + 106, top + 56 + line_no * 19, line, size=16, fill=INK)

    draw_database_icon(svg, 510, 448, BLUE_DARK)
    svg.text(310, 592, "Data Extraction", size=25, fill=INK, weight="700", anchor="middle")
    return svg


def literature_evidence_svg() -> Svg:
    svg = Svg(780, 600)
    table_x, table_y = 50, 64
    col_w = [88, 95, 132, 104, 140, 105]
    row_h = 58
    headers = ["Study", "Run", "Condition", "Assay", "Comparator", "Outcome"]
    table_w = sum(col_w)
    table_h = row_h * 5
    svg.rect(table_x, table_y, table_w, table_h, fill=WHITE, stroke=BLUE, sw=2, rx=8)

    x = table_x
    for idx, width in enumerate(col_w):
        if idx > 0:
            svg.line(x, table_y, x, table_y + table_h, BLUE, 1.5)
        svg.text(x + width / 2, table_y + 34, headers[idx], size=17, fill=BLUE_DARK, weight="700", anchor="middle")
        x += width
    for row in range(1, 5):
        y = table_y + row * row_h
        svg.line(table_x, y, table_x + table_w, y, BLUE, 1.5)

    icon_drawers = [draw_doc_icon, draw_pipette_icon, draw_people_icon, draw_bar_icon]
    for row in range(4):
        cy = table_y + row_h * (row + 1) + row_h / 2
        icon_drawers[row](svg, table_x + 28, cy - 22, color=BLUE_DARK)
        x = table_x + col_w[0]
        for width in col_w[1:-1]:
            svg.line(x + 26, cy, x + width - 26, cy, GREY_LINE, 6)
            x += width
        check_x = table_x + sum(col_w[:-1]) + col_w[-1] / 2
        svg.path(f"M{check_x-13} {cy-2} L{check_x-3} {cy+9} L{check_x+18} {cy-15}", stroke=BLUE_DARK, sw=4)

    badge_y = table_y + table_h + 28
    badges = [
        (50, 150, "auditable", "shield"),
        (220, 220, "comparator-aware", "people"),
        (465, 220, "ready for ranking", "target"),
    ]
    for bx, bw, text, icon in badges:
        svg.rect(bx, badge_y, bw, 42, fill=WHITE, stroke=BLUE, sw=2, rx=10)
        if icon == "shield":
            draw_shield_icon(svg, bx + 14, badge_y + 8, BLUE_DARK)
        elif icon == "people":
            draw_people_icon(svg, bx + 16, badge_y + 8, BLUE_DARK)
        else:
            svg.circle(bx + 28, badge_y + 21, 12, stroke=BLUE_DARK, sw=2)
            svg.circle(bx + 28, badge_y + 21, 4, stroke=BLUE_DARK, sw=2)
            svg.line(bx + 28, badge_y + 5, bx + 28, badge_y + 37, BLUE_DARK, 2)
            svg.line(bx + 12, badge_y + 21, bx + 44, badge_y + 21, BLUE_DARK, 2)
        svg.text(bx + 54, badge_y + 27, text, size=16, fill=BLUE_DARK, weight="700")

    svg.text(table_x + table_w / 2, badge_y + 102, "Literature Evidence", size=25, fill=INK, weight="700", anchor="middle")
    svg.text(
        table_x + table_w / 2,
        badge_y + 134,
        "Run-level evidence records for synthesis",
        size=18,
        fill=MUTED,
        anchor="middle",
    )
    svg.text(
        table_x + table_w / 2,
        badge_y + 160,
        "and experiment planning",
        size=18,
        fill=MUTED,
        anchor="middle",
    )
    return svg


def combined_svg() -> Svg:
    svg = Svg(1420, 560)
    svg.text(710, 64, "Literature Evidence Construction", size=44, fill=GREEN, weight="700", anchor="middle")
    svg.rect(420, 22, 580, 68, fill="none", stroke=GREEN, sw=2, rx=34)

    left = data_extraction_svg()
    right = literature_evidence_svg()
    svg.add(f'<g transform="translate(0, 50) scale(0.92)">{"".join(left.items)}</g>')
    svg.add(f'<g transform="translate(630, 52) scale(0.92)">{"".join(right.items)}</g>')
    svg.line(545, 282, 616, 282, stroke=CYAN, sw=3, dash="4 8")
    svg.path("M610 270 L626 282 L610 294", stroke=CYAN, sw=3)
    svg.text(580, 252, "assemble", size=17, fill=INK, anchor="middle")
    svg.text(580, 274, "structured", size=17, fill=INK, anchor="middle")
    svg.text(580, 296, "records", size=17, fill=INK, anchor="middle")
    return svg


def render_data_extraction_png(path: Path, scale: int = 2) -> None:
    width, height = 620 * scale, 620 * scale
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    s = lambda value: int(round(value * scale))

    draw.rounded_rectangle([s(34), s(28), s(586), s(532)], radius=s(18), outline=BLUE, width=s(2))
    rows = [
        ("Define study unit", "paper, run, and comparator"),
        ("Capture conditions", "donor, mode, temperature, time,\nratio, pH/aw, pretreatment"),
        ("Capture assay context", "assay type, target, readout, unit"),
        ("Record outcome", "treated value, control value,\nreported reduction"),
        ("Standardize and QC", "harmonize fields, link comparators,\nflag missing values"),
    ]
    x, y, row_w, row_h, gap = 78, 52, 462, 80, 14
    for idx, (title, body) in enumerate(rows):
        top = y + idx * (row_h + gap)
        draw.rounded_rectangle([s(x), s(top), s(x + row_w), s(top + row_h)], radius=s(12), fill=WHITE, outline=BLUE, width=s(2))
        draw.line([s(x + 88), s(top + 12), s(x + 88), s(top + row_h - 12)], fill=BLUE, width=s(2))
        # Simple preview glyph; the SVG output contains fully editable line icons.
        draw.rounded_rectangle([s(x + 28), s(top + 18), s(x + 58), s(top + 48)], radius=s(4), outline=BLUE_DARK, width=s(2))
        draw.text((s(x + 106), s(top + 14)), title, fill=BLUE_DARK, font=font(s(18), True))
        for line_no, line in enumerate(body.split("\n")):
            draw.text((s(x + 106), s(top + 41 + line_no * 19)), line, fill=INK, font=font(s(15)))
    draw.text((s(310), s(592)), "Data Extraction", fill=INK, font=font(s(25), True), anchor="mm")
    img.save(path)


def render_literature_evidence_png(path: Path, scale: int = 2) -> None:
    width, height = 780 * scale, 600 * scale
    img = Image.new("RGB", (width, height), WHITE)
    draw = ImageDraw.Draw(img)
    s = lambda value: int(round(value * scale))

    table_x, table_y = 50, 64
    col_w = [88, 95, 132, 104, 140, 105]
    row_h = 58
    headers = ["Study", "Run", "Condition", "Assay", "Comparator", "Outcome"]
    table_w = sum(col_w)
    table_h = row_h * 5
    draw.rounded_rectangle([s(table_x), s(table_y), s(table_x + table_w), s(table_y + table_h)], radius=s(8), fill=WHITE, outline=BLUE, width=s(2))
    x = table_x
    for idx, width in enumerate(col_w):
        if idx > 0:
            draw.line([s(x), s(table_y), s(x), s(table_y + table_h)], fill=BLUE, width=s(1.5))
        draw.text((s(x + width / 2), s(table_y + 18)), headers[idx], fill=BLUE_DARK, font=font(s(17), True), anchor="mm")
        x += width
    for row in range(1, 5):
        y = table_y + row * row_h
        draw.line([s(table_x), s(y), s(table_x + table_w), s(y)], fill=BLUE, width=s(1.5))
    for row in range(4):
        cy = table_y + row_h * (row + 1) + row_h / 2
        x = table_x + col_w[0]
        for width in col_w[1:-1]:
            draw.line([s(x + 26), s(cy), s(x + width - 26), s(cy)], fill=GREY_LINE, width=s(6))
            x += width
        check_x = table_x + sum(col_w[:-1]) + col_w[-1] / 2
        draw.line([s(check_x - 13), s(cy - 2), s(check_x - 3), s(cy + 9), s(check_x + 18), s(cy - 15)], fill=BLUE_DARK, width=s(4))
    badge_y = table_y + table_h + 28
    for bx, bw, text in [(50, 150, "auditable"), (220, 220, "comparator-aware"), (465, 220, "ready for ranking")]:
        draw.rounded_rectangle([s(bx), s(badge_y), s(bx + bw), s(badge_y + 42)], radius=s(10), fill=WHITE, outline=BLUE, width=s(2))
        draw.text((s(bx + 54), s(badge_y + 21)), text, fill=BLUE_DARK, font=font(s(16), True), anchor="lm")
    draw.text((s(table_x + table_w / 2), s(badge_y + 102)), "Literature Evidence", fill=INK, font=font(s(25), True), anchor="mm")
    draw.text((s(table_x + table_w / 2), s(badge_y + 134)), "Run-level evidence records for synthesis", fill=MUTED, font=font(s(18)), anchor="mm")
    draw.text((s(table_x + table_w / 2), s(badge_y + 160)), "and experiment planning", fill=MUTED, font=font(s(18)), anchor="mm")
    img.save(path)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    outputs = {
        "Fig2b_data_extraction_component.svg": data_extraction_svg(),
        "Fig2b_literature_evidence_component.svg": literature_evidence_svg(),
        "Fig2b_evidence_modules_combined.svg": combined_svg(),
    }
    for name, svg in outputs.items():
        path = OUTPUT_DIR / name
        svg.save(path)
        print(f"Wrote {path}")

    render_data_extraction_png(OUTPUT_DIR / "Fig2b_data_extraction_component.png")
    render_literature_evidence_png(OUTPUT_DIR / "Fig2b_literature_evidence_component.png")
    print(f"Wrote {OUTPUT_DIR / 'Fig2b_data_extraction_component.png'}")
    print(f"Wrote {OUTPUT_DIR / 'Fig2b_literature_evidence_component.png'}")


if __name__ == "__main__":
    main()
