# BKM Technical Drawings

> Erzeugt **originale technische BKM-Prinzipzeichnungen** als HTML mit Inline-SVG. Die Skill dient der klaren Systemkommunikation, nicht der automatischen Ausführungsplanung.

## Wann einsetzen

Diese Skill wird für schematische Bauwerksabdichtungsdetails, Innen- und Außenabdichtung, Übergänge, Fugen, Durchdringungen, Bodenanschlüsse, Prüfdetails und axonometrische Systemerklärungen genutzt. Jede Ausgabe bleibt ein `DRAFT`, bis eine zuständige Person die technische, normative und visuelle Prüfung dokumentiert hat.

## Unverhandelbare Grenzen

1. Lies zuerst `../../DESIGN.md`, `../../AGENTS.md`, `DRAWING_SPEC.md`, `REFERENCE_ALIGNMENT.md` und `checklist.md`.
2. Erzeuge Baukörper neutral; nutze **alle vier BKM-Grüntöne** als getrennte technische Rollen.
3. Codierung erfolgt nie ausschließlich über Farbe. Jede BKM-Rolle braucht zusätzlich Kontur, Linienart, Füllung, Symbol oder Text.
4. Nutze HTML mit **Inline-SVG** für alle Geometrien. Keine CSS-DIV-Konstruktionen für Bauteilschnitte.
5. Erzeuge keine normativen Aussagen, Produktwerte, Schichtdicken oder Maße ohne freigegebene Quelle.
6. WTA- und andere Regelwerksunterlagen dienen höchstens als fachliche Referenz. Zeichnungsgeometrie, Beschriftung, Nummerierung, Legende und Layout bleiben original für BKM.
7. Ein Agent setzt niemals `TECHNICALLY_REVIEWED`, `NORMATIVELY_REVIEWED`, `RELEASE_CANDIDATE` oder `RELEASED`.

## Vier-Grün-Systematik

| BKM-Farbton | Technische Rolle | Redundante Codierung |
|---|---|---|
| **Deep Green** `#1c4b42` | Primäre Systemkontur und kritischer Anschluss. | Höchstes Liniengewicht und durchlaufende Kontur. |
| **Transition Green** `#287d4b` | Funktions-, Übergangs- und Injektionspfad. | Gestrichelte Linie, gerichteter Marker oder Funktionssymbol. |
| **Pure Green** `#4daf46` | Primäre BKM-Lösungsfläche. | Transparente Flächenfüllung mit Deep-Green-Kontur. |
| **Lime Green** `#b4e717` | Sparsamer Prüf-, Richtungs- und Signalmarker. | Kreis/Fadenkreuz/Kennung; nie reine Flächenfarbe. |

Stone Grey und Sand White kennzeichnen neutralen Bestand, Schraffuren, Annotationen bzw. Papier- und Legendenflächen. Feuchte, Schaden und Bestand dürfen nicht mit BKM-Systemfarben verwechselt werden.

## Workflow

1. Den Zeichnungstyp und die fachliche Verwendung bestimmen.
2. Den Skalierungsstatus festlegen: `scale`, `NOT_TO_SCALE` oder `SCHEMATIC_LAYER_THICKNESS`.
3. Eine deklarative Zeichnungsspezifikation mit Layern, Komponenten und Review-Flags erstellen.
4. Den Builder ausführen: `python3 tools/technical_drawing_builder.py`.
5. Den Validator ausführen: `python3 tools/check_technical_drawing.py`.
6. Die Darstellung als Graustufe, bei 100 % auf A4/A3 und als Vektor-PDF manuell prüfen.
7. Offene technische, normative und Produktfragen sichtbar dokumentieren.

## Quellen der Wahrheit

| Datei | Funktion |
|---|---|
| `../../DESIGN.md` | Globale BKM-Farben, Fonts und Markenkontext. |
| `tokens/technical-drawing.css` | Abgeleitete technische Rollen und Hausstandards. |
| `DRAWING_SPEC.md` | Maschinenlesbarer Zeichnungsvertrag. |
| `components/` | Verträge für Bemaßung, Callouts, Material- und Symbolschichten. |
| `standards/registry.json` | Bibliografische Normhinweise ohne Volltexte. |
| `examples/wta-inspired/` | Originale BKM-Prinzipzeichnungen im Status `DRAFT`. |
| `tests/` | Manuelle und automatisierbare Quality Gates. |

## Zeichnungstypen im ersten Paket

Die vorhandenen Beispiele decken Außenabdichtung, Innenabdichtung, Fugen, Durchdringungen, Bodenflächen, Prüfdetails und axonometrische Systemdarstellungen ab. Ihre Zeichengrammatik nutzt bandartige Systemschichten, begrenzte technische Materialmuster, eigene Achs-/Verdecktlinien und nummerierte Komponentenlisten. Sie sind als wiederverwendbare Zeichnungstaxonomie zu verstehen, nicht als vollständige Bauausführungsbibliothek.

## Schnellstart

Siehe [QUICKSTART.md](QUICKSTART.md). Für JSON-Strukturen siehe [AUTHORING.md](AUTHORING.md). Für die verbindliche Zeichnungssprache siehe [DRAWING_SPEC.md](DRAWING_SPEC.md).
