# BKM Slides — Skill (v3)

> Generiert visuell ansprechende, brand-konforme HTML-Präsentationen im BKM Mannesmann Design System. Jede Slide ist eine einzelne HTML-Datei. Das Design nutzt **Glasmorphismus auf Foto-Hintergründen oder flachen BKM-Farben** im Corporate-Editorial-Stil.

## Wann diesen Skill verwenden

- Wenn Slides, Präsentationen oder Pitch-Decks im BKM-Stil erstellt werden sollen
- Wenn Broschüren-Layouts oder Print-nahe HTML-Dateien benötigt werden
- Wenn Slides für BKM AG oder Fachbetrieb-Kontexte erstellt werden sollen

---

## PFLICHT-WORKFLOW (in dieser Reihenfolge)

### Schritt 1: Kontext bestimmen

| Kontext | Wann | Hintergrund | Akzent | Headlines auf hell |
|---------|------|-------------|--------|-------------------|
| **BKM AG** | Corporate, Produkte, Marketing, Investor | Deep Green (#1c4b42) + Foto | Lime (#b4e717) | Weiß |
| **Fachbetrieb** | Fachbetrieb-Seiten, Partner, Kunden-Pitches | Sand (#f6f5f2) + Foto | Pure Green (#4daf46) | Deep Green (#1c4b42) |

### Schritt 2: STYLE_PRESETS.md lesen

**PFLICHT.** Lies `STYLE_PRESETS.md` in diesem Ordner. Diese Datei enthält die **exakten CSS-Werte** (rgba, blur, opacity, padding, gap) für alle Elemente. **Nicht interpretieren — 1:1 kopieren.**

### Schritt 3: html-template.md lesen

**PFLICHT.** Lies `html-template.md` in diesem Ordner. Diese Datei enthält **vollständige, kopierbare HTML-Templates** für Titel-Slides und Content-Slides in beiden Kontexten. **Als Startpunkt verwenden und nur Inhalte austauschen.**

### Schritt 4: Hintergrund-Fotos generieren

**PFLICHT.** Vor dem Erstellen der Slides MÜSSEN passende Hintergrund-Fotos generiert werden. Jede Slide braucht ein eigenes Foto (keine Wiederverwendung).

**Foto-Themen für BKM:**
- Architektur (Keller, Fundamente, Fassaden, Betonwände)
- Bau/Sanierung (Baustellen, Werkzeuge, Materialien)
- Labor/Technik (Materialprüfung, Mikroskop, Proben)
- Nachhaltigkeit (Grüne Gebäude, Natur, moderne Architektur)
- Business (Handshake, Tablet/Software, Teamwork)

**Generierungs-Prompt-Muster:**
```
Professional architectural photography of [MOTIV], dramatic natural lighting,
high contrast, shot on medium format camera, editorial quality,
muted earth tones with green accents, 16:9 aspect ratio
```

**Alternative:** Nicht jede Slide braucht ein Foto. Manche Slides können auch die flache BKM-Farbe (Deep Green oder Sand) als Hintergrund nutzen — der Glasmorphismus-Effekt hebt sich trotzdem gut ab.

### Schritt 5: Assets hochladen

Logo und Keyvisual aus `assets/` hochladen (oder CDN-URLs aus vorherigen Slides wiederverwenden).

| Asset | BKM AG | Fachbetrieb |
|-------|--------|-------------|
| Logo | `assets/logos/bkm-logo-white-puregreen.png` | `assets/logos/bkm-logo-stonegrey-puregreen.png` |
| Keyvisual | `assets/keyvisual/keyvisual-on-dark.svg` | `assets/keyvisual/keyvisual-on-light.svg` |

### Schritt 6: Slides erstellen

Templates aus `html-template.md` als Basis nehmen. **Nur Inhalte austauschen**, keine Strukturänderungen an den CSS-Werten.

### Schritt 7: Qualitätskontrolle

Vor Auslieferung jeder Slide diese Checkliste prüfen:

- [ ] Glasmorphismus-Werte exakt aus STYLE_PRESETS.md kopiert?
- [ ] Hintergrund-Foto generiert und eingebunden (oder bewusst flache Farbe)?
- [ ] Overlay-Gradient exakt aus STYLE_PRESETS.md?
- [ ] Unbounded 900 UPPERCASE für H1, KEIN Italic?
- [ ] Logo im richtigen Kontext (white-puregreen vs. stonegrey-puregreen)?
- [ ] Keyvisual: rechter Rand, 22% Breite, opacity 0.18/0.15, nur auf Titelseite?
- [ ] Footer-Bar auf Content-Slides vorhanden?
- [ ] Akzentlinie auf Titelseite vorhanden?
- [ ] Font Awesome CDN eingebunden?
- [ ] Google Fonts CDN für Unbounded eingebunden?

---

## Kritische Regeln

### Was BKM-Slides SIND:

1. **Glasmorphismus-basiert** — Frosted-Glass-Cards auf Foto-Hintergründen oder flachen BKM-Farben
2. **Fotografie-unterstützt** — Generierte Fotos als Hintergrund mit Overlay
3. **Großzügiger Weißraum** — Mindestens 25% der Fläche bleibt leer
4. **Nur 2 Farbkontexte:** BKM AG (dunkel) ODER Fachbetrieb (hell)
5. **Asymmetrische, editorial Layouts** — Nicht symmetrische Dashboard-Grids
6. **Vertikale Akzentlinie** auf Titelseiten (4px breit, ~60% Höhe)
7. **Footer-Bar** auf Content-Slides (volle Breite, Akzent-Icon + Weiß Text)
8. **Keyvisual** am rechten Rand, angeschnitten, subtil transparent

### Was BKM-Slides NICHT sind:

- ❌ Noise-Texturen (SVG fractal noise)
- ❌ Aurora-Gradients (animierte Farbverläufe)
- ❌ Bento-Grids (gleichförmige Kachel-Layouts)
- ❌ Floating Badges (absolut positionierte Labels)
- ❌ Spotlight/Glow-Effekte
- ❌ Animierte Text-Effekte
- ❌ Dashboard-artige symmetrische Grids
- ❌ Box-Shadows auf Cards
- ❌ Unbounded Italic (Faux-Italic sieht falsch aus)

### Typografie (nur 3 Stufen):

| Stufe | Schrift | Einsatz |
|-------|---------|---------|
| **Headline** | Unbounded 900 (UPPERCASE, kein Italic) | H1 56px, H2 48/38/36px, Card-Titel 17px |
| **Subtitle** | System-UI Bold 700 | Labels 11px, Subtitles 18/17/16px, Badges 10-11px |
| **Body** | System-UI Regular 400 | Body 17/15/14/13px, Footer 14px |

---

## Dateistruktur

```
skills/bkm-slides/
├── SKILL.md                  ← Diese Datei (Einstieg + Pflicht-Workflow)
├── STYLE_PRESETS.md          ← Exakte CSS-Token (PFLICHT lesen)
├── html-template.md          ← Vollständige HTML-Templates (PFLICHT lesen)
├── PATTERN_CATALOG.md        ← Erlaubte und verbotene Patterns
├── assets/
│   ├── logos/                ← BKM Logos (verschiedene Varianten)
│   ├── keyvisual/            ← Keyvisual on-dark und on-light
│   └── fonts/                ← TT Norms Pro (optional, system-ui als Fallback)
└── demo-editorial-*.html     ← Referenz-Slides (zur Inspiration, nicht als Template)
```
