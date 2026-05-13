# BKM Slides — Skill (v4)

> Generiert visuell ansprechende, brand-konforme HTML-Präsentationen im BKM Mannesmann Design System. Das Design nutzt **Glasmorphismus auf Foto-Hintergründen oder flachen BKM-Farben** im Corporate-Editorial-Stil.

---

## WICHTIGSTE REGEL

> **KOPIEREN, NICHT INTERPRETIEREN.** Jede Slide MUSS aus einem der 5 Templates in `html-template.md` kopiert werden. Nur Platzhalter (Texte, Bild-URLs, Icons) dürfen ersetzt werden. CSS-Werte, Klassen, Strukturen dürfen NICHT verändert werden. Eigene CSS-Erfindungen sind VERBOTEN.

---

## Wann diesen Skill verwenden

- Wenn Slides, Präsentationen oder Pitch-Decks im BKM-Stil erstellt werden sollen
- Wenn Broschüren-Layouts oder Print-nahe HTML-Dateien benötigt werden
- Wenn Slides für BKM AG oder Fachbetrieb-Kontexte erstellt werden sollen

---

## PFLICHT-WORKFLOW (in dieser Reihenfolge, kein Schritt darf übersprungen werden)

### Schritt 1: Kontext bestimmen

| Kontext | Wann | Overlay-Basis | Akzent | Headlines |
|---------|------|---------------|--------|-----------|
| **BKM AG** | Corporate, Produkte, Marketing, Investor | Deep Green rgba(28,75,66) | Lime #b4e717 | Weiß #ffffff |
| **Fachbetrieb** | Fachbetrieb-Seiten, Partner, Kunden-Pitches | Sand rgba(246,245,242) | Pure Green #4daf46 | Deep Green #1c4b42 |

### Schritt 2: html-template.md lesen

**PFLICHT.** Lies `html-template.md` in diesem Ordner. Diese Datei enthält:
- **5 vollständige, kopierbare HTML-Templates** (Titel, Checklist, Feature-Liste, Dual-Card, CTA/Closing)
- **Kontext-Umschaltungstabelle** (alle Farbwerte BKM AG → Fachbetrieb)
- **Platzhalter-Referenz** (welche `{{VARIABLEN}}` wo eingesetzt werden)

**Du MUSST eines dieser 5 Templates als Basis für jede Slide verwenden.**

### Schritt 3: Golden References ansehen

**EMPFOHLEN.** Lies `examples/bkm-ag-showroom-glasmorphismus.html` und/oder `examples/fachbetrieb-showroom-glasmorphismus.html` um das fertige Ergebnis zu sehen. Diese Dateien zeigen alle 5 Slide-Typen in einer navigierbaren Präsentation.

### Schritt 4: Hintergrund-Fotos generieren

**PFLICHT.** Vor dem Erstellen der Slides MÜSSEN passende Hintergrund-Fotos generiert werden.

**Regeln:**
- Jede Slide braucht ein **eigenes** Foto (keine Wiederverwendung)
- Alle Fotos in einem Batch generieren (nicht einzeln während der Slide-Erstellung)
- Format: 16:9, editorial Qualität, gedämpfte Erdtöne

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

**Alternative:** Nicht jede Slide braucht ein Foto. Manche Slides können auch die **flache BKM-Farbe** (Deep Green `#1c4b42` oder Sand `#f6f5f2`) als Hintergrund nutzen — der Glasmorphismus-Effekt hebt sich trotzdem gut ab. In diesem Fall: `<img class="bg-photo">` durch `<div class="bg-photo" style="background: #1c4b42;"></div>` ersetzen.

### Schritt 5: Assets hochladen

Logo und Keyvisual aus dem Repository hochladen (oder CDN-URLs aus vorherigen Slides wiederverwenden).

| Asset | BKM AG | Fachbetrieb |
|-------|--------|-------------|
| Logo | `assets/logos/bkm-logo-white-puregreen.png` | `assets/logos/bkm-logo-stonegrey-puregreen.png` |
| Keyvisual | `assets/keyvisual/keyvisual-on-dark.svg` | `assets/keyvisual/keyvisual-on-light.svg` |

### Schritt 6: Slides erstellen

1. Wähle für jede Slide den passenden **Slide-Typ** (1–5) aus `html-template.md`
2. **Kopiere das komplette HTML** des gewählten Typs
3. Ersetze **nur die `{{PLATZHALTER}}`** mit echten Inhalten
4. Wenn Fachbetrieb-Kontext: Ersetze die Farbwerte gemäß der **Kontext-Umschaltungstabelle** in `html-template.md`
5. Passe die Anzahl der Checklist-Items / Features / Prozess-Schritte an (3–6 erlaubt)

### Schritt 7: Qualitätskontrolle

Vor Auslieferung JEDER Slide diese Checkliste prüfen:

- [ ] Template aus html-template.md kopiert (nicht frei erfunden)?
- [ ] CSS-Werte NICHT verändert?
- [ ] Hintergrund-Foto generiert und eingebunden (oder bewusst flache Farbe)?
- [ ] Unbounded 900 UPPERCASE für Headlines, KEIN Italic?
- [ ] Logo im richtigen Kontext?
- [ ] Keyvisual: nur auf Titelseite, rechter Rand, 22% Breite, opacity 0.18/0.15?
- [ ] Footer-Bar auf Content-Slides (Typ 2–5) vorhanden?
- [ ] Vertikale Akzentlinie auf Titelseite vorhanden?
- [ ] Font Awesome CDN eingebunden?
- [ ] Google Fonts CDN für Unbounded eingebunden?
- [ ] Keine verbotenen Patterns verwendet (siehe unten)?

---

## Die 5 Slide-Typen (Übersicht)

| Typ | Name | Wann verwenden |
|-----|------|----------------|
| 1 | **Titel-Slide** | Erste Folie. Keyvisual + Akzentlinie + Glass-Card + optionale Trends-Bar |
| 2 | **Checklist + Status-Card** | Features/Vorteile als Liste mit Status-Badge |
| 3 | **Feature-Liste mit Icon-Chips** | Funktionen mit Icons + Beschreibungen, asymmetrisch |
| 4 | **Dual-Card** | Zwei Themen/Produkte nebeneinander vergleichen |
| 5 | **CTA / Closing** | Letzte Folie. Zentriertes Panel + Prozess-Flow + Closing-Statement |

---

## Kritische Regeln

### Was BKM-Slides SIND:

1. **Glasmorphismus-basiert** — Frosted-Glass-Cards (`backdrop-filter: blur(20px)`)
2. **Fotografie-unterstützt** — Generierte Fotos als Hintergrund mit Overlay
3. **Großzügiger Weißraum** — Mindestens 25% der Fläche bleibt leer
4. **Nur 2 Farbkontexte:** BKM AG (dunkel) ODER Fachbetrieb (hell)
5. **Asymmetrische, editorial Layouts** — Nicht symmetrische Dashboard-Grids
6. **Vertikale Akzentlinie** auf Titelseiten (4px breit, ~60% Höhe)
7. **Footer-Bar** auf Content-Slides (volle Breite, Akzent-Icon + Text)
8. **Keyvisual** am rechten Rand, angeschnitten, subtil transparent (nur Titelseite)

### Was BKM-Slides NICHT sind (VERBOTEN):

- ❌ Noise-Texturen (SVG fractal noise)
- ❌ Aurora-Gradients (animierte Farbverläufe)
- ❌ Bento-Grids (gleichförmige Kachel-Layouts)
- ❌ Floating Badges (absolut positionierte Labels)
- ❌ Spotlight/Glow-Effekte
- ❌ Animierte Text-Effekte
- ❌ Dashboard-artige symmetrische Grids
- ❌ Box-Shadows auf Cards
- ❌ Unbounded Italic (Faux-Italic sieht falsch aus)
- ❌ Eigene CSS-Erfindungen die nicht in den Templates stehen

### Typografie (nur 3 Stufen):

| Stufe | Schrift | Einsatz |
|-------|---------|---------|
| **Headline** | Unbounded 900 (UPPERCASE, kein Italic) | H1 56px, H2 48/42/38/36px, Card-Titel 17px |
| **Subtitle** | System-UI Bold 700 | Labels 11px, Subtitles 18/17/16px, Badges 10-11px |
| **Body** | System-UI Regular 400 | Body 17/15/14/13px, Footer 14/13px |

---

## Dateistruktur

```
skills/bkm-slides/
├── SKILL.md                  ← Diese Datei (Einstieg + Pflicht-Workflow)
├── STYLE_PRESETS.md          ← Exakte CSS-Token (Referenz)
├── html-template.md          ← 5 VOLLSTÄNDIGE HTML-Templates (PFLICHT-BASIS)
├── PATTERN_CATALOG.md        ← Erlaubte und verbotene Patterns
├── assets/
│   ├── logos/                ← BKM Logos (verschiedene Varianten)
│   └── keyvisual/            ← Keyvisual on-dark und on-light
└── examples/
    ├── bkm-ag-showroom-glasmorphismus.html      ← Golden Reference (5 Slides, dunkel)
    └── fachbetrieb-showroom-glasmorphismus.html  ← Golden Reference (5 Slides, hell)
```

---

## Zusammenfassung für Agents

```
1. Lies html-template.md → enthält 5 kopierbare Templates
2. Bestimme Kontext (BKM AG dunkel / Fachbetrieb hell)
3. Generiere Hintergrund-Fotos (oder nutze flache BKM-Farbe)
4. Lade Logo + Keyvisual hoch
5. Kopiere Template → ersetze nur {{PLATZHALTER}}
6. Für Fachbetrieb: Farben gemäß Umschaltungstabelle ersetzen
7. Qualitätskontrolle durchführen
```
