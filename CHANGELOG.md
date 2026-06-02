# Changelog

Alle wesentlichen Änderungen am BKM Mannesmann Design System werden hier dokumentiert.

## [Unreleased]

### Hinzugefügt
- Neuer Skill `bkm-images` für brand-konforme Bildgenerierung über die OpenAI
  Image-API (`gpt-image-1`, "OpenAI Images 2.0")
  - `skills/bkm-images/SKILL.md` — Pflicht-Workflow, Bildsprache, Kontext-Regeln
  - `skills/bkm-images/PROMPT_LIBRARY.md` — Prompt-Bausteine pro Use Case + Kontext
  - `skills/bkm-images/generate.mjs` — lauffähiges CLI (Node ≥ 18, ohne npm install)
- Unterstützte Use Cases: Slide-Hintergründe (16:9), Social Media (1:1 / 9:16),
  Website/Hero (landscape), Produkt/Architektur
- Verweise aus `bkm-slides` (Schritt 4) und der Skills-Übersicht auf `bkm-images`

## [1.0.0] - 2026-05-11

### Hinzugefügt
- Initiale Veröffentlichung des Design Systems
- `DESIGN.md` mit maschinenlesbaren Tokens (Farben, Typografie, Spacing, Komponenten)
- Dokumentation für digitale Medien (`docs/digitale-medien.md`)
- Dokumentation für Print-Anwendungen (`docs/print-anwendungen.md`)
- Dokumentation für MicroPorex und Technik (`docs/microporex-und-technik.md`)
- README mit Nutzungshinweisen für AI-Agenten
- CONTRIBUTING-Richtlinien
