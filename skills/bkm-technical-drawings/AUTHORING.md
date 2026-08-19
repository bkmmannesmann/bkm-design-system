# Authoring

## Prinzip

Ein Agent beschreibt das Detail als strukturierte Daten; der Generator besitzt die wiederkehrende SVG-Geometrie, Farbe, Layerreihenfolge, Legende und Statushinweise. So bleiben BKM-CD, Zeichnungssprache und Qualitätsgates unabhängig vom verwendeten Agenten reproduzierbar.

```text
Zeichnungsbrief + freigegebene Fachinformationen
                    ↓
        Zeichnungsmanifest / strukturierte Inhalte
                    ↓
      BKM Technical Drawing Builder (Python)
                    ↓
     HTML + Inline-SVG + Manifest + Validator
```

## Erlaubte Autorenentscheidungen

Autoren dürfen Zeichnungstyp, Titel, Statushinweise, freigegebene Komponenten, Beschriftungen, Layerinhalt und vorhandene Projektwerte bestimmen. Sie dürfen keine Normwerte, Produktdaten, fachlichen Freigaben oder Statuswerte oberhalb `DRAFT` erfinden.

## Mindestdaten für eine neue Zeichnung

```json
{
  "id": "BKM-TD-201",
  "title": "Innenabdichtung – Projektprinzip",
  "type": "interior-waterproofing-section",
  "status": "DRAFT",
  "scale": "NOT_TO_SCALE",
  "schematic_layer_thickness": true,
  "layers": ["existing-masonry", "concrete", "bkm-waterproofing", "injection", "inspection", "annotation"],
  "review": {"technical": false, "normative": false, "visual": false}
}
```

## Beschriftungsregeln

Technische Callouts beschreiben Funktion und Prüfbedarf knapp. Verwende keine WTA-Originalbeschriftungen, Originalnummerierungen oder übernommenen Maßtexte als Produkttext. Die BKM-Zeichnung formuliert ihre eigene technische Erklärung und referenziert bei Bedarf eine geprüfte Registry-ID.
