# Quality Checklist

## P0 — Ausgabe stoppen, bis behoben

- [ ] Die Zeichnung enthält `DRAFT`, einen Maßstabsstatus und alle Review-Flags.
- [ ] Alle vier BKM-Grüntöne besitzen eindeutige, getrennte Rollen und eine nichtfarbliche Zusatzcodierung.
- [ ] Bestand, Feuchte/Schaden und BKM-Systemmaßnahme sind semantisch getrennte SVG-Layer.
- [ ] Keine unregistrierten Farben, Gradients, Schatten, Glasmorphismus, Rasterbilder oder `foreignObject`.
- [ ] Alle Pflichtlayer, Callout-IDs und Metadaten sind vorhanden.
- [ ] Keine erfundenen Produktwerte, Maßwerte oder normativen Behauptungen.
- [ ] Keine Überlappungen von Texten, Leadern, Dimensionen oder kritischen Geometrien.
- [ ] Die Zeichnung bleibt in Graustufen ohne Informationsverlust verständlich.

## P1 — Vor Draft PR abschließen

- [ ] A4/A3 bei 100 % geprüft; Linien und Mikrotexte bleiben lesbar.
- [ ] Vektor-PDF kontrolliert; keine Rasterung oder abgeschnittenen Inhalte.
- [ ] Materialschraffuren sind von Systemflächen und Phänomenen unterscheidbar.
- [ ] Callouts führen nicht durch Beschriftungen oder kritische Anschlüsse.
- [ ] WTA-/DIN-/ISO-Bezüge stehen ausschließlich in der Registry, nie als unüberprüfter Zeichnungsanspruch.

## P2 — Feinschliff

- [ ] Titelblock, Legende, Statuszeile und Layernamen sind über die Bibliothek konsistent.
- [ ] Die Zeichnung erklärt ein dominantes technisches Prinzip und vermeidet Überladung.
- [ ] Detailfokus, Axonometrie oder Prüfmarker werden nur eingesetzt, wenn sie den Informationsgewinn erhöhen.

## Menschliche Freigabe

`TECHNICALLY_REVIEWED`, `NORMATIVELY_REVIEWED`, `RELEASE_CANDIDATE` und `RELEASED` dürfen nur nach dokumentierter menschlicher Prüfung gesetzt werden.
