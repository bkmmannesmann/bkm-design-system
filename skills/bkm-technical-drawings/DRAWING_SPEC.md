# Drawing Specification

## 1. Zeichnungsmanifest

Jede Zeichnung benötigt eine nebenstehende `.manifest.json` mit mindestens folgender Struktur:

```json
{
  "id": "BKM-TD-101",
  "title": "Außenabdichtung – Systemprinzip",
  "status": "DRAFT",
  "scale": "NOT_TO_SCALE",
  "schematic_layer_thickness": true,
  "review": {
    "technical": false,
    "normative": false,
    "visual": false
  },
  "normative_text_in_repository": false,
  "normative_verification_required": true,
  "bkm_color_roles": {
    "deep_green": "primäre Systemkontur / kritischer Anschluss",
    "transition_green": "Funktions- und Injektionspfad",
    "pure_green": "primäre BKM-Lösungsfläche",
    "lime_green": "Prüf- und Signalmarker"
  }
}
```

`status` darf durch automatisierte Erzeugung ausschließlich `DRAFT` sein. Eine Zeichnung enthält entweder einen konkreten Maßstab oder den eindeutigen Status `NOT_TO_SCALE`; bewusst überhöhte Schichten erhalten zusätzlich `schematic_layer_thickness: true`.

## 2. Semantische SVG-Layer

| Layer | Aufgabe |
|---|---|
| `sheet` | Papier, Rahmen, Titel- und Statusbereich. |
| `existing-masonry` | Neutraler Bestandsbaukörper und Mauerwerk. |
| `concrete` | Beton, Bodenplatten, Fundamente oder Tragzonen. |
| `soil` | Erdreich und neutrale Umgebungszonen. |
| `protection` | Schutz-, Nutz- oder Trennschichten. |
| `bkm-waterproofing` | Primäre BKM-Abdichtung; Deep- und Pure-Green-Rolle. |
| `injection` | BKM-Funktions-/Injektionszonen; Transition-Green-Rolle. |
| `penetration` | Rohr, Futterrohr oder sonstige Durchdringungsobjekte. |
| `moisture` | Feuchte- oder Schadensphänomen; neutral codiert. |
| `inspection` | Lime-Green-Prüf-/Signalmarker mit redundanter Form. |
| `dimension` | Vollständige Bemaßungskomponenten. |
| `annotation` | Callouts, Leader und technische Erläuterungen. |
| `legend` | Erklärung der Systeme und Statushinweise. |
| `footer` | ID, Revision, Status und Skalierungskennzeichnung. |

## 3. Komponentenvertrag

### Dimension

Eine Bemaßung besteht aus `extensionA`, `extensionB`, `dimensionLine`, `terminatorStart`, `terminatorEnd`, `value`, optional `unit` und optional `tolerance`. Freie Maßtexte ohne Maßlinie sind unzulässig.

### Callout

Ein Callout besitzt `id`, `anchor`, `leader.points`, `number`, `title`, `description`, optional `product`, optional `system` und optionale `standardReferences`. Leader sollen keine Texte oder kritische Geometrien schneiden.

### Material und System

Materialmuster beantworten **was vorhanden ist**. BKM-Systemobjekte beantworten **welche Funktion die Maßnahme übernimmt**. Schadensphänomene sind immer eine eigene Schicht; sie dürfen nicht wie BKM-Lösungsflächen erscheinen.

## 4. Erlaubte SVG-Mittel

Verwende `path`, `line`, `polyline`, `polygon`, `pattern`, `marker`, `symbol`, `use`, `clipPath`, `text` und `g`. Inline-SVG bleibt die Geometriequelle. Verboten sind `foreignObject`, Rasterbilder, dekorative Verläufe, Schatten, Glasmorphismus und pseudo-technische HUD-Optik.

## 5. Zeichen- und Farbhierarchie

Die Liniengewichte in `tokens/technical-drawing.css` sind **BKM-Hausstandard im Entwurfsstatus**. Farbe ergänzt die technische Hierarchie, ersetzt sie aber nie. In Graustufen müssen Bestand, BKM-Maßnahme, Funktionspfad, Prüfung und Feuchtephänomen weiterhin anhand von Gewicht, Muster, Form, Kontur und Text unterscheidbar bleiben.
