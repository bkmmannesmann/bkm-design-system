# BKM Mannesmann Design System

> The single source of truth for all visual and communicative guidelines of BKM Mannesmann AG — optimized for AI agents, developers, and designers.

[![Version](https://img.shields.io/badge/version-1.1.0-brightgreen)]()
[![Format](https://img.shields.io/badge/format-DESIGN.md-blue)]()
[![awesome-design-md](https://img.shields.io/badge/awesome--design--md-compatible-orange)](https://github.com/VoltAgent/awesome-design-md)

## Overview

This repository contains the complete design system for BKM Mannesmann AG, a manufacturer of building protection products specializing in moisture barriers and injection technologies. The system is structured in the [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) format — machine-readable YAML tokens + human-readable prose documentation.

### What's Inside

| File | Purpose | Lines |
|------|---------|-------|
| `DESIGN.md` | Complete design tokens (colors, typography, spacing, shadows, components, animations, responsive) + documentation | 700+ |
| `AGENTS.md` | Instructions for AI coding agents + CSS variables template + Tailwind v4 config | 200+ |
| `docs/brand-voice.md` | Tone, claims, copy patterns, UI text guidelines | |
| `docs/digitale-medien.md` | Web/app implementation details, CSS variables, Dark Mode | |
| `docs/print-anwendungen.md` | Print specifications (brochures, TDS, labels, vehicles) | |
| `docs/microporex-und-technik.md` | Ingredient brand rules, naming, file formats | |
| `docs/keyvisual.md` | Chevron pattern specifications and placement | |
| `docs/logo.md` | Logo variants, clear space, positioning | |
| `docs/icon-system.md` | Verbindlicher Phosphor-Standard für Bold- und Fill-Icons in allen Ausgabeformaten | |
| `docs/repository-architecture.md` | Zielarchitektur für getrennte BKM-Fachrepositories und gemeinsame Governance | |
| `assets/icons/phosphor/manifest.json` | Kuratierte, versionierte Icon-Auswahl mit erlaubtem Einsatzzweck | |
| `assets/icons/tds/manifest.json` | Fester, rendererfester Abschnittsiconsatz für technische Datenblätter | |
| `docs/referenzen.md` | External design system references (Vercel, MongoDB, NVIDIA, Mintlify, Supabase) | |
| `docs/verbesserungsvorschlaege.md` | Improvement proposals based on reference analysis | |
| `docs/bkm-slide-prompt.md` | Legacy v3 slide prompt — superseded by `skills/bkm-slides/QUICKSTART.md` | |
| `skills/bkm-slides/SKILL.md` | Slide skill entry point — mandatory workflow for slide creation | |
| `skills/bkm-slides/QUICKSTART.md` | **How to build an on-brand deck (start here)** — for Claude Code, Claude.ai & Manus | |
| `skills/bkm-slides/templates/<family>/demo.html` | **Self-contained golden-reference decks** (embedded fonts, logo, textures) — the actual starting point | |
| `skills/bkm-slides/STYLE_PRESETS.md` | Exact CSS tokens for glassmorphism slides (both contexts) | |
| `skills/bkm-slides/PATTERN_CATALOG.md` | Allowed and forbidden patterns with exact CSS values | |
| `skills/bkm-app/SKILL.md` | App-UI skill entry point — 24 binding rules for tools people work in daily | |
| `skills/bkm-app/QUICKSTART.md` | **How to build or convert an on-brand app UI (start here)** — ready-to-copy prompts | |
| `skills/bkm-app/tokens.css` | **Canonical app tokens** — semantic layer, Day/Night themes, computed contrasts | |
| `skills/bkm-app/templates/bkm-cockpit/demo.html` | **Self-contained golden-reference cockpit** (eight views, embedded fonts, logo, icons) | |
| `skills/bkm-app/MIGRATION.md` | Converting a running application — current state, deltas, four stages | |

## Quick Start

### For AI Agents (Cursor, Copilot, Manus, etc.)

**For Websites and Landing Pages:**

```
Read the DESIGN.md and AGENTS.md from https://github.com/bkmmannesmann/bkm-design-system
and create [a landing page / marketing site / etc.] following the BKM Mannesmann design.
```

**For Web Apps, Cockpits, Portals and Internal Tools — read `skills/bkm-app/QUICKSTART.md` first.**

> ⚠️ A **working surface** someone uses 50 times a day is not a landing page. Deriving one from
> `DESIGN.md` alone yields the marketing look: display headlines above a customer list, Lime as
> decoration, no status system, no states. `skills/bkm-app/` adds the missing medium — a semantic
> token layer (so the Day/Night switch works at all), a status system, and a self-contained
> reference cockpit. Same rule as for decks: **start from the template and replace only the
> content.** To convert an application that already exists, follow `skills/bkm-app/MIGRATION.md`.

**For Slide Presentations — read `skills/bkm-slides/QUICKSTART.md` first.**

> ⚠️ The on-brand look depends on **embedded assets** (brand fonts, real logo, textured
> backgrounds) that live **inside** the family template files. These **cannot be
> reconstructed from the Markdown docs.** Always **start from a self-contained template and
> replace only the content** — never "read the docs and generate from scratch" (that yields
> a generic, off-brand deck).

**A — Claude Code with the repo (recommended):**
```
Erstelle ein BKM-Deck zu [Thema] für [BKM AG / Fachbetrieb].
Nutze die bkm-slides-Skill, baue auf templates/bkm-glass-ag/demo.html auf,
ersetze nur den Inhalt und rendere zur Kontrolle.
```

**B — Claude.ai or Manus (no repo): attach the template file.**
Download `skills/bkm-slides/templates/bkm-glass-ag/demo.html` (self-contained — embedded
fonts, logo, textured backgrounds, motion) and **attach it** to the chat, then:
```
Anbei die BKM-Folienvorlage. Dupliziere die Folien und ersetze NUR Text/Inhalt
mit [Thema]. Lass CSS, Schriften, Logo, Hintergründe und Engine unverändert.
Folge den Mustern in der Datei.
```

**For Other Formats (Instagram, Print, Social Media):**

```
Read DESIGN.md, AGENTS.md and docs/icon-system.md from
https://github.com/bkmmannesmann/bkm-design-system. Use only the curated
Phosphor Bold or Fill icons from assets/icons/phosphor/manifest.json and create
[Instagram posts / print materials / etc.] following the BKM Mannesmann design.
For technical data sheets, use only the fixed block-to-icon mapping and the
renderer-safe files from assets/icons/tds/manifest.json.
```

**For a New BKM Document Repository:** Read [`docs/repository-architecture.md`](docs/repository-architecture.md) first. Select the matching BKM Fachrepository, pin the design-system revision and use the common repository structure before creating content.

The agent will parse the YAML tokens and prose documentation to produce brand-consistent output.

### For Developers

1. Clone the repository
2. Copy the CSS Custom Properties from `AGENTS.md` into your project's root CSS
3. Or use the Tailwind v4 configuration block from `AGENTS.md`
4. Reference `DESIGN.md` for component specifications

### For Designers

Read the prose sections of `DESIGN.md` for visual guidelines, then reference the specific `docs/` files for your medium (digital, print, social).

## Design Philosophy

The BKM system is built on five pillars:

1. **Dual-Mode Architecture** — Deep Green marketing surfaces alternate with Sand White documentation surfaces
2. **Shadow-as-Border** — Multi-layer box-shadow stacks replace traditional CSS borders (inspired by Vercel)
3. **Product-Line Geometry** — Angular (0–4px) for Pro Line, Rounded (pill) for Home Line
4. **Single-Accent Strategy** — Lime Green (`#b4e717`) exclusively for interactive elements, on dark surfaces. On light surfaces the accent shifts to Transition Green (`#287d4b`) — Lime on Sand White has a contrast ratio of 1.34 and fails
5. **Two-Voice Typography** — Unbounded (announce), TT Norms Pro Regular + Bold (read + specify)
6. **Icon Continuity** — Only curated Phosphor Bold and Fill icons, used consistently across digital and print media; technical data sheets use the fixed renderer-safe set in `assets/icons/tds/`

## Supported Output Formats

This design system can be applied to generate:

- Websites (React, HTML/CSS, Tailwind, Next.js)
- Web applications (cockpits, portals, internal tools — see `skills/bkm-app/`)
- Slide presentations (PowerPoint, Google Slides, image-based)
- Instagram Carousel Posts (4:5 or 1:1)
- Print documents (brochures, technical data sheets, labels)
- Email templates
- Social media graphics
- Video title cards

## Compatibility

This design system follows the [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) specification and is compatible with:

- **Cursor** — Add as project context
- **GitHub Copilot** — Reference in workspace
- **Manus** — Share as project file or reference via GitHub URL
- **Claude** — Paste DESIGN.md content as context
- **ChatGPT** — Upload DESIGN.md as file
- **Any AI agent** that can read Markdown with YAML frontmatter

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to propose changes to the design system.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## License

Proprietary — BKM Mannesmann AG. Internal use only.
