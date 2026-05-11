# AGENTS.md – BKM Mannesmann Design System

## Projektübersicht

Dieses Repository enthält das offizielle Design System der BKM Mannesmann AG. Es dient als Single Source of Truth für alle visuellen und kommunikativen Richtlinien der Marke.

## Für AI-Coding-Agenten

Wenn du UI-Komponenten oder Layouts für BKM Mannesmann erstellst, lies zuerst die `DESIGN.md` im Hauptverzeichnis. Sie enthält alle Design-Tokens (Farben, Typografie, Spacing, Komponenten) in einem maschinenlesbaren Format.

### Wichtige Regeln

1. **Headlines** sind immer in `Unbounded Black` (weight 900) und **VERSALIEN**.
2. **Fließtext** ist immer in `TT Norms Pro Regular` (weight 400).
3. **Zeilenabstand** ist durchgehend **125%** der Schriftgröße.
4. **CTA-Buttons** verwenden Deep Green Hintergrund mit Lime Green Text (Standard) oder invertiert (Hover).
5. **Keyvisual** (Chevron-Muster) wird immer **rechts, angeschnitten** platziert.
6. **Logo** wird auf Printmedien immer **links oben** positioniert.
7. **Bilder** im Hero-Bereich sind immer im Format **16:9**.
8. **Farben** dürfen nur aus der definierten Palette verwendet werden.
9. **Ansprache** ist standardmäßig **"Du"** (außer in formellen Dokumenten).
10. **WCAG-AA-Konformität** (mindestens 4.5:1 Kontrast) ist Pflicht.

### Dateistruktur

```
bkm-design-system/
├── DESIGN.md          # Maschinenlesbare Design-Tokens
├── AGENTS.md          # Diese Datei (Anweisungen für Agenten)
├── README.md          # Projektbeschreibung
├── CONTRIBUTING.md    # Beitragsrichtlinien
├── CHANGELOG.md       # Versionshistorie
└── docs/
    ├── brand-voice.md         # Tonalität und Ansprache
    ├── digitale-medien.md     # Web, Banner, CSS
    ├── icon-system.md         # Icon-Spezifikationen
    ├── keyvisual.md           # Chevron-Muster Regeln
    ├── logo.md                # Logo-Varianten und Schutzraum
    ├── microporex-und-technik.md  # Ingredient Brand & Technik
    ├── print-anwendungen.md   # Broschüren, TDS, Etiketten
    └── referenzen.md          # Externe Inspirationsquellen
```

### Schnellstart für Agenten

```
1. Lies DESIGN.md für Tokens und Komponenten
2. Verwende die CSS-Variablen oder Tailwind-Konfiguration aus docs/digitale-medien.md
3. Beachte die Brand Voice aus docs/brand-voice.md für Texte
4. Prüfe docs/keyvisual.md für die korrekte Platzierung des Chevron-Musters
```
