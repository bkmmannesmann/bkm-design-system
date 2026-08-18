#!/usr/bin/env python3
"""Generate original BKM technical principle drawings as HTML with inline SVG.

The renderer uses a visually verified, WTA-oriented drawing grammar without
copying WTA geometry, labels, dimensions, numbering or page layout. Generated
files remain DRAFT, NOT_TO_SCALE and require human technical/normative review.
"""

from __future__ import annotations

import argparse
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "skills" / "bkm-technical-drawings" / "examples" / "wta-inspired"

DRAWINGS = [
    ("BKM-TD-101", "exterior-primary-waterproofing", "exterior", "primary", "Außenabdichtung – Systemprinzip", "Primäre Abdichtungsführung an erdberührter Wand"),
    ("BKM-TD-102", "exterior-floor-transition", "exterior", "floor", "Außenabdichtung – Bodenanschluss", "Systemband mit konstruktivem Bodenanschluss"),
    ("BKM-TD-103", "exterior-rehabilitation", "exterior", "rehab", "Außenabdichtung – Überarbeitung Bestand", "Bestandslage, Übergangszone und neue Systemführung"),
    ("BKM-TD-104", "exterior-protection-layer", "exterior", "protection", "Außenabdichtung – Schutzschichtprinzip", "Abdichtung, Drainage-/Schutzlage und Erdreich"),
    ("BKM-TD-105", "joint-waterproofing-axonometric", "axonometric", "joint", "Fugenabdichtung – räumliches Prinzip", "Fuge, Band und Systemüberlappung"),
    ("BKM-TD-106", "penetration-manschette", "penetration", "manschette", "Durchdringung – Manschettenprinzip", "Rohr, Manschette und Anschlussband"),
    ("BKM-TD-107", "penetration-sleeve", "penetration", "sleeve", "Durchdringung – Futterrohrprinzip", "Futterrohr, Dichteinsatz und Systemanschluss"),
    ("BKM-TD-108", "penetration-flange", "penetration", "flange", "Durchdringung – Flanschprinzip", "Flansch, Leitung und Abdichtungsband"),
    ("BKM-TD-109", "penetration-clamping-flange", "penetration", "clamp", "Durchdringung – Klemmsystemprinzip", "Mehrteilige Flansch- und Dichtbaugruppe"),
    ("BKM-TD-110", "penetration-liquid-applied", "penetration", "liquid", "Durchdringung – flüssige Systemschicht", "Flüssig verarbeitete Anschlusszone"),
    ("BKM-TD-111", "inspection-reference-area", "inspection", "reference", "Systemprüfung – Referenzfläche", "Definierte Prüf- und Dokumentationsfläche"),
    ("BKM-TD-112", "interior-waterproofing-section", "interior", "section", "Innenabdichtung – Wand-Sohlen-Prinzip", "Innenband, Kehle und horizontale Sperrzone"),
    ("BKM-TD-113", "interior-crosswall-transition", "interior", "crosswall", "Innenabdichtung – Querwandübergang", "Getrennter Übergang an einbindender Querwand"),
    ("BKM-TD-114", "interior-exterior-transition", "interior", "transition", "Innen zu Außen – Systemübergang", "Gekoppelte Innen-, Übergangs- und Außenebene"),
    ("BKM-TD-115", "wall-installation-interior", "interior", "installation", "Innenabdichtung – Wandinstallation", "Installationsnische und geschlossene Innenebene"),
    ("BKM-TD-116", "interior-penetration", "penetration", "interior", "Innenabdichtung – Rohrdurchdringung", "Rohr, Dichtzone und Innenabdichtung"),
    ("BKM-TD-117", "floor-waterproofing-section", "floor", "section", "Bodenflächenabdichtung – Systemprinzip", "Schichtenfolge einer Bodenflächenabdichtung"),
    ("BKM-TD-118", "floor-slab-transition", "floor", "slab", "Bodenplatte – Übergangsdetail", "Bestand, neue Bodenplatte und Anschlussband"),
]


def drawing_tuple(item: tuple[str, str, str, str, str, str]) -> dict:
    keys = ("id", "slug", "family", "variant", "title", "focus")
    return dict(zip(keys, item, strict=True))


def defs() -> str:
    return """<defs>
  <pattern id="td-masonry-bond" width="12" height="6" patternUnits="userSpaceOnUse"><path d="M0 3H12M6 0V3M0 3V6" class="hatch"/></pattern>
  <pattern id="td-concrete-stipple" width="6" height="6" patternUnits="userSpaceOnUse"><circle cx="1.2" cy="1.3" r=".28" fill="#494949"/><circle cx="4.6" cy="4.3" r=".22" fill="#494949"/></pattern>
  <pattern id="td-drainage-honeycomb" width="8" height="7" patternUnits="userSpaceOnUse"><path d="M2 0L6 0L8 3.5L6 7H2L0 3.5Z" class="hatch"/></pattern>
  <pattern id="td-protection-crosshatch" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 0L5 5M5 0L0 5" class="hatch"/></pattern>
  <pattern id="td-soil-grain" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r=".25" fill="#494949"/><circle cx="6" cy="5" r=".28" fill="#494949"/><path d="M0 7L2 6.5" class="hatch"/></pattern>
  <style>
    .section{stroke:#1a1a1a;stroke-width:.70;fill:none}.object{stroke:#494949;stroke-width:.50;fill:none}.secondary{stroke:#494949;stroke-width:.35;fill:none}.annotation{stroke:#494949;stroke-width:.22;fill:none}.hatch{stroke:#494949;stroke-width:.18;fill:none}.axis{stroke:#494949;stroke-width:.22;stroke-dasharray:6 1.4 1.1 1.4;fill:none}.hidden{stroke:#494949;stroke-width:.22;stroke-dasharray:2 1.2;fill:none}.system-band{fill:#4daf46;fill-opacity:.12;stroke:#1c4b42;stroke-width:.78}.system-edge{stroke:#1c4b42;stroke-width:.78;fill:none}.system-segment{fill:#fff;stroke:#1c4b42;stroke-width:.22}.function-path{stroke:#287d4b;stroke-width:.35;stroke-dasharray:2.8 1.2;fill:none}.check{fill:#b4e717;stroke:#1c4b42;stroke-width:.35}.detail-arc{stroke:#494949;stroke-width:.30;stroke-dasharray:3 1.2;fill:none}.title{font-family:Unbounded,Arial,sans-serif;font-size:4.2px;font-weight:900;fill:#1c4b42}.meta{font-family:'TT Norms Pro',Arial,sans-serif;font-size:2.25px;fill:#494949}.label{font-family:'TT Norms Pro',Arial,sans-serif;font-size:2.6px;font-weight:700;fill:#1c4b42}.body{font-family:'TT Norms Pro',Arial,sans-serif;font-size:2.65px;fill:#1a1a1a}.number{font-family:'TT Norms Pro',Arial,sans-serif;font-size:3px;font-weight:700;fill:#1a1a1a}
  </style>
</defs>"""


def sheet(d: dict) -> str:
    return f"""<g data-layer="sheet"><rect width="297" height="210" fill="#fff"/><rect x="10" y="10" width="277" height="190" fill="none" stroke="#c8c5be" stroke-width=".25"/><line x1="10" y1="29" x2="287" y2="29" class="secondary"/>
<text x="14" y="18" class="label">BKM TECHNICAL DRAWINGS · DRAFT</text><text x="14" y="25" class="title">{escape(d['title'].upper())}</text>
<text x="229" y="18" class="meta">{escape(d['id'])}</text><text x="229" y="22" class="meta">NOT_TO_SCALE · SCHEMATIC_LAYER_THICKNESS</text>
<line x1="229" y1="25" x2="237" y2="25" class="system-edge"/><line x1="240" y1="25" x2="248" y2="25" class="function-path"/><rect x="251" y="23.7" width="6" height="2.6" class="system-band"/><circle cx="261" cy="25" r="1.35" class="check"/></g><g data-layer="legend" id="legend"><text x="264" y="25.8" class="meta">BKM-KEY</text></g>"""


def point_callout(n: int, x: float, y: float, label_y: float, label: str) -> str:
    return f"""<g data-layer="annotation" id="callout-{n}"><circle cx="{x}" cy="{y}" r="1.7" fill="#1a1a1a"/><polyline points="{x},{y} 44,{label_y} 31,{label_y}" class="annotation"/><text x="22" y="{label_y + 1}" class="number">{n}.</text><text x="34" y="{label_y + 1}" class="body">{escape(label)}</text></g>"""


def components(items: list[str]) -> str:
    start = 170
    lines = ["<g data-layer=\"component-list\"><line x1=\"14\" y1=\"166\" x2=\"283\" y2=\"166\" class=\"secondary\"/><text x=\"14\" y=\"171\" class=\"label\">KOMPONENTEN / PRINZIP</text>"]
    for index, item in enumerate(items, start=1):
        col = 14 if index <= 3 else 147
        row = (index - 1) % 3
        lines.append(f"<text x=\"{col}\" y=\"{start + row * 5}\" class=\"body\"><tspan class=\"number\">{index}.</tspan> {escape(item)}</text>")
    lines.append("</g>")
    return "".join(lines)


def footer(d: dict) -> str:
    return f"""<g data-layer="footer"><line x1="10" y1="192" x2="287" y2="192" class="secondary"/><text x="14" y="197" class="meta">{escape(d['id'])} · REV 01 · DRAFT · NOT_TO_SCALE · NORMATIVE_VERIFICATION_REQUIRED</text><text x="265" y="197" class="meta">A4 · LANDSCAPE</text></g>"""


def system_band(path: str, segments: list[tuple[float, float, float, float]] = []) -> str:
    pieces = [f'<path d="{path}" class="system-band"/>']
    for x, y, w, h in segments:
        pieces.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="system-segment"/>')
    return "".join(pieces)


def exterior(d: dict) -> str:
    variant = d["variant"]
    drainage = "<rect x=\"78\" y=\"52\" width=\"13\" height=\"103\" fill=\"url(#td-drainage-honeycomb)\" class=\"object\"/>" if variant == "protection" else "<rect x=\"82\" y=\"52\" width=\"9\" height=\"103\" fill=\"url(#td-protection-crosshatch)\" class=\"object\"/>"
    existing = "<path d=\"M100 54V146Q100 150 106 150H159\" class=\"hidden\"/>" if variant == "rehab" else ""
    band_path = "M92 50H98V143Q98 149 104 149H165V156H101Q91 156 91 146Z"
    if variant == "floor":
        band_path = "M92 50H98V143Q98 149 104 149H172V157H100Q91 157 91 146Z"
    soil = "<path d=\"M20 50H78V158H20Z\" fill=\"url(#td-soil-grain)\" class=\"object\"/>"
    content = f"""{soil}<g data-layer="protection">{drainage}</g><g data-layer="existing-masonry"><rect x="100" y="50" width="45" height="99" fill="url(#td-masonry-bond)" class="section"/></g><g data-layer="concrete"><path d="M66 149H175V162H74V157H66Z" fill="url(#td-concrete-stipple)" class="section"/></g><g data-layer="bkm-waterproofing">{system_band(band_path, [(93, 72, 5, 7), (93, 94, 5, 7), (93, 116, 5, 7), (93, 138, 5, 7)])}{existing}</g><g data-layer="axis"><path d="M63 149H176" class="axis"/></g><g data-layer="inspection"><circle cx="150" cy="152.5" r="2.35" class="check"/><path d="M147 152.5H153M150 149.5V155.5" class="annotation"/><text x="149.2" y="153.3" class="meta">P</text></g>{point_callout(1, 95, 83, 68, 'BKM-Systemband')}{point_callout(2, 85, 111, 76, 'Schutz-/Drainagelage')}{point_callout(3, 150, 152.5, 84, 'Prüfposition')}"""
    return content + components(["BKM-Systemband", "Schutz- bzw. Drainagelage", "Prüfposition", "Baukörper / Mauerwerk", "Bodenplatte", "Erdreich"]) + footer(d)


def penetration(d: dict) -> str:
    v = d["variant"]
    side = "right" if v == "interior" else "left"
    wall_x = 83 if side == "right" else 112
    tube_y = 103
    wall = f'<rect x="{wall_x}" y="50" width="48" height="108" fill="url(#td-masonry-bond)" class="section"/>'
    tube = f'<path d="M31 {tube_y}H184V116H31Q24 109 31 {tube_y}Z" fill="#fff" class="section"/><g data-layer="axis"><path d="M31 109H184" class="axis"/></g>'
    bx = wall_x - 10 if side == "left" else wall_x + 48
    band = system_band(f"M{bx} 54H{bx+7}V97Q{bx+7} 101 {bx+12} 101H{bx+24}V118H{bx+12}Q{bx+7} 118 {bx+7} 122V154H{bx}Z", [(bx+1, 72, 5, 7), (bx+1, 92, 5, 7), (bx+1, 122, 5, 7), (bx+1, 142, 5, 7)])
    if v == "manschette":
        component = f'<path d="M{bx+16} 95Q{bx+33} 101 {bx+16} 108Q{bx+33} 115 {bx+16} 121" class="system-edge"/>'
        label = "Dichtmanschette"
    elif v == "sleeve":
        component = f'<rect x="{bx+18}" y="94" width="16" height="29" fill="#fff" class="section"/><rect x="{bx+21}" y="99" width="7" height="19" fill="url(#td-protection-crosshatch)" class="object"/>'
        label = "Futterrohr / Dichteinsatz"
    elif v == "clamp":
        component = f'<rect x="{bx+16}" y="94" width="5" height="30" fill="#fff" class="section"/><rect x="{bx+32}" y="94" width="5" height="30" fill="#fff" class="section"/><path d="M{bx+21} 98H{bx+32}M{bx+21} 120H{bx+32}" class="secondary"/>'
        label = "Los-/Festflansch"
    elif v == "liquid":
        component = f'<path d="M{bx+13} 95Q{bx+31} 108 {bx+13} 121" class="system-edge"/><path d="M{bx+17} 97Q{bx+27} 108 {bx+17} 119" class="function-path"/>'
        label = "flüssige Anschlusszone"
    elif v == "interior":
        component = f'<path d="M{bx-6} 96Q{bx-20} 108 {bx-6} 120" class="system-edge"/>'
        label = "Innen-Dichtzone"
    else:
        component = f'<rect x="{bx+18}" y="93" width="6" height="31" fill="#fff" class="section"/><path d="M{bx+24} 99H{bx+37}M{bx+24} 117H{bx+37}" class="secondary"/>'
        label = "Dichtflansch"
    content = f"""<g data-layer="existing-masonry">{wall}</g><g data-layer="penetration">{tube}</g><g data-layer="bkm-waterproofing">{band}</g><g data-layer="component">{component}</g><g data-layer="protection"><rect x="{wall_x-13 if side == 'left' else wall_x+48}" y="52" width="9" height="104" fill="url(#td-protection-crosshatch)" class="object"/></g><g data-layer="inspection"><circle cx="{bx+39}" cy="108" r="2.35" class="check"/><path d="M{bx+36} 108H{bx+42}M{bx+39} 105V111" class="annotation"/></g>{point_callout(1, bx+8, 91, 68, 'BKM-Systemband')}{point_callout(2, bx+21, 108, 76, label)}{point_callout(3, bx+39, 108, 84, 'Prüfposition')}"""
    return content + components(["BKM-Systemband", label, "Prüfposition", "Baukörper", "Durchdringungsobjekt", "Schutzlage"]) + footer(d)


def interior(d: dict) -> str:
    v = d["variant"]
    add_crosswall = '<rect x="128" y="94" width="23" height="45" fill="url(#td-masonry-bond)" class="section"/>' if v == "crosswall" else ""
    add_installation = '<rect x="87" y="80" width="13" height="31" fill="#fff" class="section"/><circle cx="94" cy="95" r="2.3" class="object"/>' if v == "installation" else ""
    transition = '<path d="M68 138H91" class="function-path"/><path d="M68 142H91" class="function-path"/>' if v == "transition" else '<path d="M76 126H100" class="function-path"/>'
    band_path = "M106 53H113V143Q113 149 119 149H169V156H117Q106 156 106 145Z"
    content = f"""<g data-layer="existing-masonry"><rect x="60" y="53" width="46" height="96" fill="url(#td-masonry-bond)" class="section"/>{add_crosswall}{add_installation}</g><g data-layer="concrete"><path d="M60 149H174V163H60Z" fill="url(#td-concrete-stipple)" class="section"/></g><g data-layer="bkm-waterproofing">{system_band(band_path, [(107, 72, 5, 7), (107, 94, 5, 7), (107, 116, 5, 7), (107, 138, 5, 7)])}<path d="M107 143Q113 133 120 144" class="system-edge"/></g><g data-layer="injection">{transition}</g><g data-layer="axis"><path d="M54 149H177" class="axis"/></g><g data-layer="inspection"><circle cx="139" cy="152" r="2.35" class="check"/><path d="M136 152H142M139 149V155" class="annotation"/></g>{point_callout(1, 109, 88, 68, 'Innen-Systemband')}{point_callout(2, 86, 126, 76, 'Funktionszone')}{point_callout(3, 139, 152, 84, 'Prüfposition')}"""
    parts = ["Innen-Systemband", "Funktionszone", "Prüfposition", "Baukörper / Mauerwerk", "Bodenplatte", "Kehlenzone"]
    return content + components(parts) + footer(d)


def floor(d: dict) -> str:
    v = d["variant"]
    slab_extra = '<rect x="123" y="132" width="48" height="17" fill="url(#td-concrete-stipple)" class="section"/>' if v == "slab" else ''
    band = system_band("M97 145H175V152H97Z", [(106, 146, 7, 5), (128, 146, 7, 5), (150, 146, 7, 5)])
    content = f"""<g data-layer="existing-masonry"><rect x="55" y="54" width="42" height="95" fill="url(#td-masonry-bond)" class="section"/></g><g data-layer="concrete"><path d="M55 149H178V164H55Z" fill="url(#td-concrete-stipple)" class="section"/>{slab_extra}</g><g data-layer="protection"><rect x="97" y="132" width="80" height="13" fill="url(#td-protection-crosshatch)" class="object"/></g><g data-layer="bkm-waterproofing">{band}</g><g data-layer="axis"><path d="M52 156H181" class="axis"/></g><g data-layer="detail-focus"><path d="M128 130A21 21 0 0 1 157 151" class="detail-arc"/><line x1="151" y1="130" x2="179" y2="94" class="annotation"/><text x="181" y="94" class="number">A</text></g><g data-layer="inspection"><circle cx="141" cy="148.5" r="2.35" class="check"/><path d="M138 148.5H144M141 145.5V151.5" class="annotation"/></g>{point_callout(1, 132, 138, 68, 'Schutzlage')}{point_callout(2, 141, 148.5, 76, 'BKM-Systemband')}{point_callout(3, 141, 148.5, 84, 'Prüfposition')}"""
    return content + components(["Schutz-/Nutzlage", "BKM-Systemband", "Prüfposition", "Wandbestand", "Bodenplatte", "Detailbezug A"]) + footer(d)


def axonometric(d: dict) -> str:
    content = f"""<g data-layer="existing-masonry"><polygon points="56,76 126,50 180,80 110,106" fill="url(#td-masonry-bond)" class="section"/><polygon points="56,76 110,106 110,153 56,123" fill="#fff" class="section"/><polygon points="110,106 180,80 180,127 110,153" fill="url(#td-concrete-stipple)" class="section"/></g><g data-layer="bkm-waterproofing">{system_band('M105 101L114 98L188 72L188 82L114 110L105 113Z', [(116, 98, 5, 5), (138, 90, 5, 5), (160, 82, 5, 5)])}</g><g data-layer="injection"><polyline points="62,79 111,108 176,84" class="function-path"/></g><g data-layer="axis"><path d="M105 110L183 81" class="axis"/></g><g data-layer="inspection"><circle cx="112" cy="106" r="2.35" class="check"/><path d="M109 106H115M112 103V109" class="annotation"/></g>{point_callout(1, 112, 106, 69, 'Fugen-/Bandzone')}{point_callout(2, 148, 93, 77, 'Systemüberlappung')}"""
    return content + components(["Fugen-/Bandzone", "Systemüberlappung", "Prüfposition", "Baukörper", "BKM-Systemband"]) + footer(d)


def inspection(d: dict) -> str:
    content = f"""<g data-layer="existing-masonry"><rect x="54" y="59" width="116" height="82" fill="url(#td-masonry-bond)" class="section"/></g><g data-layer="bkm-waterproofing">{system_band('M76 80H149V116H76Z', [(81, 84, 8, 5), (102, 84, 8, 5), (123, 84, 8, 5)])}</g><g data-layer="axis"><path d="M72 98H152M112 72V124" class="axis"/></g><g data-layer="inspection"><circle cx="112" cy="98" r="7" class="check"/><path d="M101 98H123M112 87V109" class="annotation"/><text x="110.6" y="99.2" class="number">P</text></g><g data-layer="detail-focus"><path d="M69 77A28 28 0 0 1 151 117" class="detail-arc"/></g>{point_callout(1, 112, 90, 69, 'Referenzfläche')}{point_callout(2, 112, 98, 77, 'Prüfposition')}"""
    return content + components(["Referenzfläche", "Prüfposition", "BKM-Systemfläche", "Referenzuntergrund"]) + footer(d)


def body(d: dict) -> str:
    return {"exterior": exterior, "penetration": penetration, "interior": interior, "floor": floor, "axonometric": axonometric, "inspection": inspection}[d["family"]](d)


def render(d: dict) -> str:
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(d['id'])} – {escape(d['title'])}</title><link rel="stylesheet" href="../../tokens/technical-drawing.css"><style>@font-face{{font-family:'TT Norms Pro';font-weight:400;src:url('../../../../assets/fonts/TT_Norms_Pro_Compact_Regular.woff2') format('woff2')}}@font-face{{font-family:'TT Norms Pro';font-weight:700;src:url('../../../../assets/fonts/TT_Norms_Pro_Bold.woff2') format('woff2')}}@font-face{{font-family:Unbounded;font-weight:900;src:url('../../../../assets/fonts/Unbounded_900.woff2') format('woff2')}}*{{box-sizing:border-box}}body{{margin:0;background:#f6f5f2}}main{{padding:18px}}.notice{{max-width:1120px;margin:0 auto 10px;padding:10px 14px;border-left:4px solid #287d4b;background:#fff;color:#494949;font:14px/1.45 'TT Norms Pro',Arial,sans-serif}}svg{{display:block;width:min(100%,1120px);height:auto;margin:auto;background:#fff}}@media print{{@page{{size:A4 landscape;margin:0}}main{{padding:0}}.notice{{display:none}}svg{{width:297mm;height:210mm}}}}</style></head><body><main><aside class="notice"><strong>Schematische BKM-Prinzipzeichnung:</strong> {escape(d['focus'])}. Zeichensprache referenzorientiert; keine Ausführungsplanung und keine normative Freigabe.</aside><svg width="297mm" height="210mm" viewBox="0 0 297 210" role="img" aria-labelledby="title description"><title id="title">{escape(d['title'])}</title><desc id="description">Originale BKM-Prinzipzeichnung mit referenzorientierter Linien-, Layer- und Musterlogik.</desc>{defs()}{sheet(d)}{body(d)}</svg></main></body></html>"""


def manifest(d: dict) -> dict:
    return {"id": d["id"], "title": d["title"], "family": d["family"], "variant": d["variant"], "status": "DRAFT", "scale": "NOT_TO_SCALE", "schematic_layer_thickness": True, "reference_basis": "visuelle interne Referenzanalyse WTA Merkblatt 4-6 und BKM-Planungsratgeber; originale BKM-Geometrie und -Beschriftung", "review": {"technical": False, "normative": False, "visual": False}, "bkm_color_roles": {"deep_green": "Systembandkanten", "transition_green": "Funktionspfad", "pure_green": "Systembandkern", "lime_green": "Prüfmarker"}, "normative_text_in_repository": False, "normative_verification_required": True}


def build(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    index = []
    for item in DRAWINGS:
        d = drawing_tuple(item)
        (output / f"{d['slug']}.html").write_text(render(d), encoding="utf-8")
        (output / f"{d['slug']}.manifest.json").write_text(json.dumps(manifest(d), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        index.append({key: d[key] for key in ("id", "slug", "family", "variant", "title")})
    (output / "index.json").write_text(json.dumps({"package": "bkm-reference-aligned-principle-drawings", "status": "DRAFT", "drawings": index}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate reference-aligned BKM Technical Drawings")
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    build(args.output.resolve())
    print(f"Generated {len(DRAWINGS)} reference-aligned BKM principle drawings in {args.output.resolve()}")


if __name__ == "__main__":
    main()
