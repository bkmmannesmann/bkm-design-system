# Quick Start

## Ziel

Erzeuge eine **originale BKM-Prinzipzeichnung** mit neutralem Bestand, vier klaren BKM-Grünrollen und maschinenlesbaren SVG-Layern. Die Ausgabe ist ein Systemkommunikationsmittel im Status `DRAFT`, keine Ausführungsplanung.

## Bestehende Beispielbibliothek öffnen

Im Repository liegen 18 originale Zeichnungen unter `examples/wta-inspired/`. Jede Datei ist eine A4-Querformat-HTML-Datei mit Inline-SVG und zugehörigem Manifest.

```bash
python3 tools/technical_drawing_builder.py
python3 tools/check_technical_drawing.py
```

## Vorgehen für ein neues Detail

| Schritt | Ergebnis |
|---|---|
| 1. Zeichnungstyp wählen | Beispielsweise Außenabdichtung, Innenabdichtung, Durchdringung, Fuge, Bodenanschluss oder Prüfdetail. |
| 2. Fachlichen Scope bestimmen | Nur freigegebene Projekt- und Produktinformationen verwenden; sonst eindeutig schematisch bleiben. |
| 3. Manifest erstellen | ID, Titel, Status, Maßstabsstatus, Review-Flags und offene Normprüfung setzen. |
| 4. Layer modellieren | Bestand, Material, System, Phänomene, Bemaßung, Callouts und Legende voneinander trennen. |
| 5. Vier Grüntöne anwenden | Deep = Kontur, Transition = Funktion, Pure = Lösungsfläche, Lime = Prüfung/Signal. |
| 6. Validator ausführen | Strukturelle Verstöße korrigieren. |
| 7. Manuell prüfen | Geometrie, Konstruktion, Systemlogik, Graustufen, Druck und PDF beurteilen. |

## Mindestprüfung vor der Weitergabe

Die Ausgabe muss einen klaren Status `DRAFT`, `NOT_TO_SCALE` oder einen konkreten Maßstab, `SCHEMATIC_LAYER_THICKNESS` bei überhöhten Schichten sowie `NORMATIVE_VERIFICATION_REQUIRED` bei ungeprüften Normbezügen enthalten. Jede in Lime, Pure, Transition oder Deep Green dargestellte Information muss zusätzlich über eine nichtfarbliche Zeichnungssemantik verständlich sein.
