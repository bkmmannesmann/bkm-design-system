# Inspiration: Open Design → BKM Weiterentwicklung

> Ideen-Sammlung aus der Analyse von **[nexu-io/open-design](https://github.com/nexu-io/open-design)**
> (Apache-2.0), einer Open-Source-Alternative zu „Claude Design". Ziel: konkrete Hebel,
> um das BKM Design System weiterzuentwickeln. Übernommene Konzepte sind im Code mit
> Quellenhinweis markiert.

## Validierung unseres Fundaments

- Ihre Deck-Engine (`apps/daemon/src/prompts/deck-framework.ts`) ist **deckungsgleich**
  mit unserer Fixed-Stage-Engine (1920×1080, `transform: scale()` to fit, Print = eine
  Seite je Folie). Unser Ansatz ist also state of the art.
- Ihr „Direction-Picker" (5 Schulen) entspricht unseren **4 Familien** + Auswahl-Workflow.

## ✅ Umgesetzt (Quick Wins)

| # | Idee | Quelle | Umsetzung in BKM |
|---|------|--------|------------------|
| 1 | **P0/P1/P2-Self-Check + 5-Dim-Selbstkritik** (Philosophy/Hierarchy/Execution/Specificity/Restraint, <3/5 nachbessern) | `discovery.ts` Step 7–8 | `skills/bkm-slides/checklist.md`, verdrahtet in `SKILL.md` Schritt 6 |
| 2 | **Anti-Slop-Positivregeln** (1 Akzent ≤2×/Folie, Display≠Body, Farben via `oklch()` ableiten, kein generischer Beige-Canvas, eine dominante Aussage) | `discovery.ts` §C | neuer Abschnitt in `PATTERN_CATALOG.md` |
| 3 | **Engine-Drift-Fixes** (Capture-Keydown auf window+document, Body-Autofokus, `localStorage`-Positions-Merker) | `deck-framework.ts` | gehärtete Deck-JS in `ENGINE.md` |
| 4 | **Turn-1-Kurzbrief** (≤7 Fragen vor dem Bauen: Zweck, Kontext, Track, Folienzahl, Dichte, Speaker Notes) | `discovery.ts` Rule 1 | `SKILL.md` Schritt 1 |

## 🟡 Offene Kandidaten (noch nicht umgesetzt)

| Idee | Quelle | Nutzen für BKM |
|------|--------|----------------|
| **Kanonische `tokens.css`** (alle Marken-Token als CSS-Variablen, von allen Familien importiert) | `design-systems/<brand>/tokens.css` | Single Source of Truth, kein per-Familie-Copy-Paste der `:root`-Token |
| **`components.html`** (gerendertes Bauteil-Schaufenster) | `design-systems/<brand>/components.html` | bündelt `patterns/` + `examples/` zu einer „lebenden" Referenz |
| **Multi-Format-Export** (HTML/PDF/**PPTX**/ZIP/Markdown) | `OpenCoworkAI/open-codesign` (peer) | PDF haben wir (Print-CSS); PPTX wäre praktisch wertvoll |
| **Maschinen-validiertes Schema** (`manifest.json` + 4-Schichten-Token-Contract + CI-Guard) | `design-systems/_schema/` | erst sinnvoll bei mehreren BKM-Sub-Marken — vorerst Overkill |
| **Spezial-Skills** (`design-review`, `brandkit`, `color-expert`) | `skills/` (154 Skills) | eigenständige Review-/Asset-Workflows neben `bkm-slides` |

## Lizenz / Attribution

Open Design steht unter **Apache-2.0**. Übernommene Konzepte sind hier und an den
Code-Stellen vermerkt. Bei wörtlicher Code-Übernahme Lizenz/Urheber beibehalten.
