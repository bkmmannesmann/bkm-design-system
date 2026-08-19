# Referenzorientierte Zeichengrammatik

> **Geltungsbereich:** Diese Regeln leiten sich aus der visuellen Analyse der intern bereitgestellten WTA-Prinzipskizzen und des BKM-Planungsratgebers ab. Sie sind kein Ersatz für den Volltext von ISO-, DIN- oder WTA-Regelwerken und begründen keine normative Freigabe.

## Nachgewiesene Abweichungen des ersten Entwurfs

| Thema | Erster Entwurf | Referenzorientierte Korrektur |
|---|---|---|
| Abdichtung | Einzelne Deep-Green-Linie mit großflächiger, transparenter Pure-Green-Füllung. | Geschlossenes, bandförmiges Systemobjekt mit zwei deutlich getrennten Kanten, kontrollierter innerer Markierung und begrenzter BKM-Farbakzentuierung. |
| Schichten | Überwiegend grafische Flächen; Schichtbeziehung war nicht immer als Geometrie lesbar. | Jede Schutz-, Abdichtungs-, Dämm-/Drainage- und Bestandslage wird als separates, begrenztes Profil gezeichnet. |
| Materialmuster | Generische Ziegel- und Punktmuster. | Wiederkehrende technische Muster für Mauerwerksverband, Beton, Schutzlage, Drainage/Dämmung und ggf. Erdreich; Muster bleiben unter Systemkonturen. |
| Achsen/verdeckt | Freie gestrichelte Linien wurden mehrfach als Funktionspfad verwendet. | Achs-/Verdecktlinien erhalten einen eigenen Langstrich-Punkt- bzw. Strich-Typ. Funktions-/Injektionspfade bleiben als eigene BKM-Rolle getrennt. |
| Callouts | Farbige Nummernkreise und Pfeil-Leader in einem Seitensystem. | Schwarzer Punktanker, dünner gerader Leader, nummerierte Komponentenliste im Blattfuß; kein dekorativer Pfeil. |
| Detailbezug | Vollständiger gestrichelter Kreis mit Pfeil-Leader. | Teilkreis bzw. Abschnittsbogen, Kennbuchstabe und einfache Bezugslinie. |
| Farbe | BKM-Farbe war primärer Informationsträger. | Monochrome technische Lesbarkeit ist primär. Die vier BKM-Grüntöne ergänzen das System band-, pfad- oder markerbasiert und bleiben in Graustufen redundanzfähig. |

## Linienvertrag

| Rolle | SVG-Klasse | Visuelle Regel | BKM-Farbe |
|---|---|---|---|
| Schnitt-/Profilkante | `td-section` | Durchgezogen, stärkste Linie. | Ink / Deep Green nur bei BKM-Systemkante. |
| Sichtbare Bauteilkante | `td-object` | Durchgezogen, mittlere Linie. | Stone Grey. |
| Material-/Schraffurlinie | `td-hatch` | Durchgezogen, fein und nur innerhalb einer Clipfläche. | Stone Grey. |
| Bemaßung/Leader | `td-annotation` | Durchgezogen, fein, ohne dekorativen Pfeil. | Stone Grey. |
| Achse | `td-axis` | Langstrich–Punkt-Folge; nur Achs-/Bezugslinien. | Stone Grey. |
| Verdeckt | `td-hidden` | Gleichmäßige Strichfolge; nur verdeckte Geometrie. | Stone Grey. |
| BKM-Systemband | `td-system-band` | Geschlossene Bandgeometrie, zwei Kanten, innere Semantik. | Deep/Pure Green. |
| BKM-Funktionspfad | `td-function-path` | Dünner, gerichteter Pfad mit eigener Strichfolge. | Transition Green. |
| BKM-Prüfmarker | `td-check-marker` | Kleiner Kreis plus Kennung und Kreuz; nie allein über Farbe. | Lime Green. |

## Patternvertrag

| Materialrolle | Pattern | Regel |
|---|---|---|
| Mauerwerk | `td-masonry-bond` | Rechteckiger Verband mit klaren Lager- und Stoßfugen. |
| Beton | `td-concrete-stipple` | Feine, unregelmäßige Punktstruktur; keine dekorative Textur. |
| Schutzlage | `td-protection-crosshatch` | Begrenzte Kreuzschraffur zwischen zwei Bauteilkanten. |
| Drainage/Dämmung | `td-drainage-honeycomb` | Wabenstruktur in einem klaren Bauteilband. |
| Erdreich | `td-soil-grain` | Sparsame Punkt-/Kurzkornstruktur; keine dominante Fläche. |

## Beschriftungs- und Listenvertrag

Die Komponentenliste steht in der Detailzone unterhalb der Zeichnung. Ihre Nummern entsprechen ausschließlich den Punktankern auf dem Blatt. BKM-Farben werden nicht für die Nummerierung benötigt. Der Zeichenschlüssel bleibt separat und klein, damit die technische Detaillegende nicht mit Marken- oder Systeminformation überladen wird.

## Farbvertrag

Die Farbe liegt **nach** Linienhierarchie, Profilgeometrie, Materialmuster und Beschriftung. Deep Green markiert die zwei Kanten eines BKM-Systembands; Pure Green füllt dessen Kern sehr zurückhaltend; Transition Green kennzeichnet funktionale oder injektive Teilpfade; Lime Green kennzeichnet eine seltene, beschriftete Prüfposition. Bei Schwarzweißdruck bleiben Systemband, Funktion, Prüfstelle und Bestand durch unterschiedliche Konturen, Muster, Stricharten und Text unterscheidbar.
