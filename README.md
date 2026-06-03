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
| `docs/icon-system.md` | Icon specifications | |
| `docs/referenzen.md` | External design system references (Vercel, MongoDB, NVIDIA, Mintlify, Supabase) | |
| `docs/verbesserungsvorschlaege.md` | Improvement proposals based on reference analysis | |
| `docs/bkm-slide-prompt.md` | Legacy v3 slide prompt — superseded by `skills/bkm-slides/QUICKSTART.md` | |
| `skills/bkm-slides/SKILL.md` | Slide skill entry point — mandatory workflow for slide creation | |
| `skills/bkm-slides/QUICKSTART.md` | **How to build an on-brand deck (start here)** — for Claude Code, Claude.ai & Manus | |
| `skills/bkm-slides/templates/<family>/demo.html` | **Self-contained golden-reference decks** (embedded fonts, logo, textures) — the actual starting point | |
| `skills/bkm-slides/STYLE_PRESETS.md` | Exact CSS tokens for glassmorphism slides (both contexts) | |
| `skills/bkm-slides/PATTERN_CATALOG.md` | Allowed and forbidden patterns with exact CSS values | |

## Quick Start

### For AI Agents (Cursor, Copilot, Manus, etc.)

**For Websites, Landing Pages, Web Apps:**

```
Read the DESIGN.md and AGENTS.md from https://github.com/bkmmannesmann/bkm-design-system
and create [a landing page / web app / etc.] following the BKM Mannesmann design.
```

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
Read the DESIGN.md from https://github.com/bkmmannesmann/bkm-design-system
and create [Instagram posts / print materials / etc.] following the BKM Mannesmann design.
```

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
4. **Single-Accent Strategy** — Lime Green (`#b4e717`) exclusively for interactive elements
5. **Two-Voice Typography** — Unbounded (announce), TT Norms Pro Regular + Bold (read + specify)

## Supported Output Formats

This design system can be applied to generate:

- Websites (React, HTML/CSS, Tailwind, Next.js)
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
