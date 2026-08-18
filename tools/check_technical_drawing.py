#!/usr/bin/env python3
"""Structural validation for BKM Technical Drawing System outputs.

The validator intentionally checks only deterministic technical contracts. It
cannot approve geometry, construction plausibility, normative applicability or
human review. Those checks remain explicit manual gates.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "skills" / "bkm-technical-drawings" / "examples" / "wta-inspired"
ALLOWED_COLORS = {
    "#1c4b42", "#287d4b", "#4daf46", "#b4e717", "#494949",
    "#1a1a1a", "#f6f5f2", "#ffffff", "#fff", "#c8c5be",
}
REQUIRED_LAYERS = {"sheet", "legend", "footer", "bkm-waterproofing", "inspection", "component-list"}
BANNED = ("linear-gradient", "radial-gradient", "box-shadow", "backdrop-filter", "filter:", "foreignObject")
REQUIRED_GRAMMAR = ("td-masonry-bond", "td-concrete-stipple", "system-band", "axis", "component-list")
LEGACY_DRAWING_TOKENS = ("system-primary", "system-solution", "phenomenon")


def errors_for_html(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    for term in BANNED:
        if term.lower() in text.lower():
            errors.append(f"{path.name}: forbidden visual effect/token '{term}'")
    colors = {color.lower() for color in re.findall(r"#[0-9a-fA-F]{3,6}\b", text)}
    unknown = colors - ALLOWED_COLORS
    if unknown:
        errors.append(f"{path.name}: unregistered colors {', '.join(sorted(unknown))}")
    layers = set(re.findall(r'data-layer="([^"]+)"', text))
    missing = REQUIRED_LAYERS - layers
    if missing:
        errors.append(f"{path.name}: missing required layers {', '.join(sorted(missing))}")
    for marker in ("NOT_TO_SCALE", "SCHEMATIC_LAYER_THICKNESS", "NORMATIVE_VERIFICATION_REQUIRED"):
        if marker not in text:
            errors.append(f"{path.name}: missing required status marker '{marker}'")
    for token in REQUIRED_GRAMMAR:
        if token not in text:
            errors.append(f"{path.name}: missing reference-aligned grammar token '{token}'")
    for token in LEGACY_DRAWING_TOKENS:
        if token in text:
            errors.append(f"{path.name}: legacy illustrative drawing token '{token}' remains")
    if 'data-layer="axis"' not in text:
        errors.append(f"{path.name}: missing semantic axis layer")
    return errors


def errors_for_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON ({exc.msg})"]
    for field in ("id", "title", "family", "variant", "status", "scale", "review", "bkm_color_roles"):
        if field not in data:
            errors.append(f"{path.name}: missing field '{field}'")
    if data.get("status") != "DRAFT":
        errors.append(f"{path.name}: automated output must remain DRAFT")
    if data.get("scale") != "NOT_TO_SCALE":
        errors.append(f"{path.name}: expected scale NOT_TO_SCALE")
    review = data.get("review", {})
    if any(review.get(flag) for flag in ("technical", "normative", "visual")):
        errors.append(f"{path.name}: automated output must not mark reviews as complete")
    colors = data.get("bkm_color_roles", {})
    required_roles = {"deep_green", "transition_green", "pure_green", "lime_green"}
    if required_roles - set(colors):
        errors.append(f"{path.name}: incomplete four-green role map")
    if colors.get("deep_green") != "Systembandkanten":
        errors.append(f"{path.name}: Deep Green must be reserved for system-band edges")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate BKM Technical Drawing outputs")
    parser.add_argument("directory", nargs="?", type=Path, default=DEFAULT_DIR)
    args = parser.parse_args()
    directory = args.directory.resolve()
    html_files = sorted(directory.glob("*.html"))
    manifests = sorted(directory.glob("*.manifest.json"))
    errors: list[str] = []
    if not html_files:
        errors.append(f"No HTML drawings found in {directory}")
    if len(html_files) != len(manifests):
        errors.append(f"HTML/manifest count mismatch: {len(html_files)} HTML vs {len(manifests)} manifests")
    for path in html_files:
        errors.extend(errors_for_html(path))
    for path in manifests:
        errors.extend(errors_for_manifest(path))
    if errors:
        print("FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"PASSED: {len(html_files)} HTML drawings and {len(manifests)} manifests comply with the structural contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
