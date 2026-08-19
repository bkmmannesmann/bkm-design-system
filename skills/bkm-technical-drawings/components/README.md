# Komponenten

Die Komponenten beschreiben einen stabilen Vertrag zwischen strukturiertem Zeichnungsauftrag, Builder und Inline-SVG. Sie sind keine Sammlung dekorativer Illustrationen.

| Komponente | Erforderliche Bestandteile | Technische Regel |
|---|---|---|
| **Dimension** | zwei Hilfslinien, Maßlinie, zwei Terminatoren, Wert, optional Einheit und Toleranz | Maßtext wird nie ohne Maßlinie simuliert. |
| **Callout** | eindeutige ID, Anchor, Leader, Nummer, Titel, Beschreibung | Leader schneiden weder Text noch kritische Anschlüsse. |
| **Materialpattern** | neutrales Pattern, Bauteilkontur, Layer-ID | Muster identifiziert Material, nicht BKM-Funktion. |
| **Systemschicht** | Pure-Green-Fläche, Deep-Green-Kontur, Layer-ID | Die Farbe benötigt eine Kontur und eine semantische Legende. |
| **Funktionspfad** | Transition-Green-Linie, Strichmuster, optional Richtungspfeil | Funktions- und Injektionspfade bleiben von Feuchtephänomenen getrennt. |
| **Prüfmarker** | Lime-Green-Kreis, Fadenkreuz, Kennung | Lime wird nie nur als Farbe oder dominante Fläche verwendet. |

Die aktuelle Referenzimplementierung liegt im Builder `tools/technical_drawing_builder.py`. Neue Komponenten müssen den strukturellen Validator bestehen und in Graustufen überprüft werden.
