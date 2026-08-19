# BKM Repository-Architektur

## Zweck

BKM pflegt unterschiedliche Kommunikations- und Dokumenttypen in **getrennten, klar verantworteten Repositories**. Das verhindert, dass technische Inhalte, druckreife Layouts, Websites und Präsentationslogik vermischt werden. Gleichzeitig bleiben Corporate Design, Markenassets, Icon-Standard und Qualitätsregeln über das zentrale Repository [`bkm-design-system`](https://github.com/bkmmannesmann/bkm-design-system) einheitlich.

> **Grundsatz:** Jede Ausgabeart erhält ihr eigenes Fachrepository. Markenregeln und wiederverwendbare Gestaltungsbausteine werden nicht kopiert oder lokal abgeändert, sondern aus dem zentralen Design-System übernommen und auf eine konkrete Version festgelegt.

## Zielbild

| Ebene | Repository | Aufgabe | Typische Ergebnisse |
|---|---|---|---|
| Marken-Governance | `bkm-design-system` | Verbindliche Markenregeln, Tokens, freigegebene Assets, Icon-System und Umsetzungsleitfäden. | `DESIGN.md`, `AGENTS.md`, Logos, Schriften, Key Visuals, Icon-Manifest. |
| Technische Datenblätter | `bkm-technical-data-sheets` | Fachlich geprüfte TDS mit Content, Freigabe und PDF-Build. | Produktbezogene TDS-PDFs und geprüfte JSON-Daten. |
| Verarbeitungsanleitungen | `bkm-application-guides` | Arbeits- und Verarbeitungsschritte mit technischen Freigaben. | Verarbeitungsanleitungen, Schrittfolgen, Freigabeprotokolle. |
| Broschüren und Flyer | `bkm-brochures` | Marketing- und Vertriebsunterlagen im Printformat. | Broschüren, Flyer, Anzeigen, Druck-PDFs. |
| Produktkataloge | `bkm-product-catalogs` | Produktportfolios, Preis- und Sortimentsstände. | Kataloge, Preislisten, Katalog-Tabellen. |
| Tabellen und Verzeichnisse | `bkm-data-publications` | Kuratierte Tabellen, Inhaltsverzeichnisse, Übersichten und Datenexporte. | Tabellenwerke, Inhaltsverzeichnisse, CSV/XLSX/PDF-Ausgaben. |
| Präsentationen | `bkm-presentations` | Vertriebs-, Schulungs- und Unternehmenspräsentationen. | Folien, Speaker Notes, Präsentations-PDFs. |
| Websites und Apps | `bkm-digital-experiences` | Websites, Web-Anwendungen und digitale Prototypen. | Quellcode, Komponenten, Deployments und Dokumentation. |

Die genannten Fachrepositories werden **bei tatsächlichem Bedarf** angelegt. Bis dahin bleibt die Architektur als verbindliche Namens- und Verantwortungsregel bestehen. Bestehende Projekte werden nicht automatisch verschoben; sie erhalten bei der nächsten fachlichen Überarbeitung einen dokumentierten Migrationsentscheid.

## Verbindliche Abgrenzung

Ein Repository besitzt genau einen primären Ausgabezweck. Eine technische Quelle oder ein Produktdatensatz darf in mehreren Repositories referenziert werden, aber keine Redaktion soll dieselben technischen Werte parallel kopieren und pflegen. Fachlich verbindliche Daten bleiben beim verantwortlichen Produkt- oder Dokumentrepository. Ausgaben für andere Formate verweisen auf die freigegebene Quelle und dokumentieren die übernommene Revision.

| Fragestellung | Entscheidung |
|---|---|
| Entsteht ein neues Datenblatt? | Im Fachrepository für technische Datenblätter anlegen. |
| Entsteht ein neues Layout-Grundmodul? | Im zentralen Design-System oder einem dokumentierten Layout-Repository pflegen. |
| Entsteht eine einmalige Kampagnenbroschüre? | Im Broschüren-Repository mit Verweis auf die zugrunde liegende Produktrevision. |
| Wird ein Icon, Farbwert oder Logo benötigt? | Ausschließlich aus `bkm-design-system` beziehen. |
| Wird eine fachliche Produktangabe verändert? | In der primären Fachquelle korrigieren; abhängige Ausgaben danach aktualisieren. |

## Gemeinsame Mindeststruktur

Jedes neue BKM-Fachrepository enthält mindestens eine `README.md`, eine `AGENTS.md`, einen Verweis auf die festgelegte Version des `bkm-design-system`, eine kurze Freigaberegel und einen Ordner für nicht versionierte Ausgaben. Generierte PDFs, Präsentations-Exports und temporäre Rendervorschauen werden nicht eingecheckt, sofern sie nicht ausdrücklich als freigegebene Archivfassung vorgesehen sind.

```text
bkm-<fachbereich>/
├── README.md                 # Zweck, Verantwortliche, Schnellstart
├── AGENTS.md                 # Ausführbare BKM-Regeln und Prozessgrenzen
├── BRAND-SOURCE.md           # Pin auf bkm-design-system und Icon-Manifest
├── content/                  # Fach- oder Redaktionsinhalte
├── templates/                # Ausgabeformat-spezifische Vorlagen
├── assets/                   # Nur fachbereichsspezifische Assets
├── docs/                     # Freigaben, Datenquellen, Arbeitsanweisungen
├── scripts/                  # Reproduzierbare Prüf- und Build-Schritte
└── output/                   # Generiert; standardmäßig ignoriert
```

## Pflicht: gemeinsames Icon-System

Alle BKM-Ausgaben verwenden Phosphor Icons ausschließlich im Gewicht **Bold** oder **Fill**. Die verbindliche Auswahl, Herkunft, Lizenzinformation und Anwendungsregeln stehen in [`docs/icon-system.md`](icon-system.md) und im Icon-Manifest unter `assets/icons/phosphor/manifest.json`. Eigene Icons, Outline-Varianten, gemischte Icon-Bibliotheken und symbolische Emoji sind nicht zulässig, sofern keine ausdrückliche Markenfreigabe dokumentiert ist.

## Einführung in neuen Repositories

Vor dem ersten inhaltlichen Commit wird das zentrale Design-System auf eine konkrete Commit-ID oder einen Release-Tag festgelegt. Danach kopiert das Fachrepository ausschließlich die benötigten Assets aus dem festgelegten Stand oder nutzt eine dokumentierte Abhängigkeitslösung. Ein späterer Marken-Update erfolgt bewusst über einen eigenen Pull Request, damit Layoutänderungen nachvollziehbar bleiben.

Die Pull-Request-Vorlage des Fachrepositorys enthält mindestens die Fragen nach Fachfreigabe, referenzierter Markenrevision, korrektem Phosphor-Gewicht und Sichtprüfung der endgültigen Ausgabe.
