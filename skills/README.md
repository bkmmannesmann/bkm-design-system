# BKM Skills

> Generierungs-Workflows, die aus dem BKM Design System (DESIGN.md, AGENTS.md) und der Pattern Library (patterns/) lesen, um brand-konforme Outputs zu erzeugen.

## Verfügbare Skills

| Skill | Beschreibung | Output |
|-------|-------------|--------|
| [bkm-slides](bkm-slides/SKILL.md) | Visuell ansprechende HTML-Präsentationen (v5: 4 Stil-Familien, Fixed-Stage, Auswahl-Workflow) | Einzelne HTML-Dateien |
| [bkm-website](bkm-website/SKILL.md) | React-Websites und Web-Apps | React + Tailwind Projekte |
| [bkm-social](bkm-social/SKILL.md) | Social-Media-Grafiken und Vorlagen | PNG/JPG oder HTML-Vorlagen |

## Architektur

```
DESIGN.md + AGENTS.md (Source of Truth)
         ↓
    patterns/ (Component Library)
         ↓
    skills/ (Generierungs-Workflows)
         ↓
    Output (Slides, Websites, Social)
```

Jeder Skill **liest** aus dem Design System und der Pattern Library. Er verändert sie nicht.

## Einen Skill verwenden

1. Lies die `SKILL.md` des gewünschten Skills
2. Folge dem dort beschriebenen Workflow
3. Konsultiere DESIGN.md und AGENTS.md für Token-Referenzen
4. Nutze Patterns aus patterns/ als Bausteine
