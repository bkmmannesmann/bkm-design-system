# BKM Icon-System

## Verbindlicher Standard

Alle BKM-Ausgaben verwenden **Phosphor Icons** ausschließlich in den Gewichtungen **Bold** oder **Fill**. Diese Regel gilt ausnahmslos für Websites, Web-Anwendungen, Slides, Printdokumente, technische Datenblätter, Verarbeitungsanleitungen, Broschüren, Produktkataloge, Tabellen, Inhaltsverzeichnisse und alle zukünftigen Formate.

> **Standardentscheidung:** Nutze **Bold** als Regelgewicht für funktionale, technische und beschreibende Symbole. Nutze **Fill** nur für klar semantische Zustände wie Bestätigung, Warnung, Information, Energie oder Nachhaltigkeit.

Die kuratierten SVGs, die genaue Quellversion und der MIT-Lizenztext liegen im Repository unter [`assets/icons/phosphor/`](../assets/icons/phosphor/). Das verbindliche [Manifest](../assets/icons/phosphor/manifest.json) enthält Namen, Gewicht, lokalen Pfad und erlaubten Einsatzzweck jedes Icons.

## Gewicht und Bedeutung

| Gewicht | Verwenden für | Beispiele | Nicht verwenden für |
|---|---|---|---|
| **Bold** | Navigation, Dokumentstruktur, technische Informationen, Prozessschritte, Verpackung, Lagerung und Rechtliches. | `list-bullets`, `package`, `warehouse`, `scales`, `book-open`, `table` | Kritische Statusmeldungen oder dekorative Flächen. |
| **Fill** | Status, positive Bestätigung, Warnung, Information, Energie und Nachhaltigkeit. | `check-circle`, `warning`, `info`, `lightning`, `leaf` | Normale Navigations- oder Tabellenicons. |

Die Gewichtungen `thin`, `light`, `regular` und `duotone` sind nicht zulässig. Ebenfalls nicht zulässig sind Font Awesome, Heroicons, Lucide, Material Symbols, individuell nachgezeichnete Icons oder Emoji als Ersatz für Informations- und Funktionsicons.

## BKM-Farben und Container

Das Icon selbst wird einfarbig eingesetzt. Der Kontext bestimmt die Farbkombination. Für kompakte Abschnittssymbole in Print und Datenblättern bildet ein Deep-Green-Container mit Lime-Green-Icon den Standard. Für digitale BKM-AG-Oberflächen bleibt Lime Green eine interaktive Akzentfarbe. Im Fachbetriebs-Kontext nutzt du Transition Green als Container und Pure Green als Akzent. Die Farben folgen den zentralen Tokens aus `DESIGN.md`.

| Kontext | Container | Icon | Anwendung |
|---|---|---|---|
| BKM AG, Print und technische Unterlagen | Deep Green `#1c4b42` | Lime Green `#b4e717` | Abschnittskennzeichnung, technische Daten, Footer und Hinweise. |
| BKM AG, helle digitale Oberfläche | Deep Green oder transparent | Deep Green bzw. Lime Green bei Interaktion | Navigation, Links, Buttons und Funktionshinweise. |
| Fachbetrieb, helle Oberfläche | Transition Green `#287d4b` | Weiß oder Pure Green `#4daf46` | Prozessschritte, Vorteile und Services. |
| Warnung oder Bestätigung | Kontextkonforme Fläche | Fill-Icon mit ausreichendem Kontrast | Statusmarker, Prüfhinweis, Freigabe. |

Ein kreisförmiger Container bleibt zulässig, wenn ein isolierter Funktions- oder Statuspunkt benötigt wird. Für Abschnittsüberschriften, Tabellen, kleine Printbausteine und UI-Reihen sind abgerundete quadratische Container mit den im jeweiligen Ausgabeformat definierten Radien zulässig. Die Iconform wird nie durch CSS verändert, gestreckt oder aus einem Emoji nachgebaut.

## Lokale SVG-Nutzung

Für Print, PDFs und offlinefähige Websites verwendest du die kuratierten, lokalen SVGs. Die Vektordaten bleiben skalierbar und reproduzierbar. Die Icons sind standardmäßig für `currentColor` ausgelegt und erhalten ihre Farbe daher über CSS oder die SVG-umgebende Komponente.

```html
<span class="bkm-icon bkm-icon--section" aria-hidden="true">
  <img src="assets/icons/phosphor/bold/list-bullets.svg" alt="">
</span>
```

```css
.bkm-icon--section {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 3px;
  background: #1c4b42;
}

.bkm-icon--section img {
  width: 13px;
  height: 13px;
  filter: invert(88%) sepia(41%) saturate(951%) hue-rotate(31deg) brightness(99%) contrast(84%);
}
```

Bei Inline-SVG darf `fill="currentColor"` gesetzt werden. Das bevorzugte Verfahren für Websites mit JavaScript ist eine zentrale lokale Icon-Komponente; sie referenziert ausschließlich den BKM-Manifestnamen und nicht den Namen eines fremden Icon-Sets.

## Webfont-Nutzung

Wenn eine Website eine Icon-Webfont verwenden muss, wird ausschließlich die fest versionierte Phosphor-Webbibliothek verwendet. Lade nur die tatsächlich benötigten Gewichte, niemals pauschal alle Gewichte. Der Webfont ist für Webanwendungen geeignet, aber **nicht** die bevorzugte Quelle für Print-PDFs oder offline erzeugte Dokumente.

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/bold/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@phosphor-icons/web@2.1.2/src/fill/style.css">

<i class="ph-bold ph-list-bullets" aria-hidden="true"></i>
<i class="ph-fill ph-check-circle" aria-hidden="true"></i>
```

## Freigabeprüfung

Vor der Ausgabe prüfst du Icongewicht, Bedeutung, Kontrast und technische Quelle. Ein Icon darf nur verwendet werden, wenn es im Manifest steht oder über einen eigenen Pull Request in das Manifest aufgenommen wurde. Eine neue Iconaufnahme braucht einen klaren Einsatzzweck und muss verhindern, dass zwei Symbole dieselbe Bedeutung im selben Format tragen.

| Prüffrage | Erwartetes Ergebnis |
|---|---|
| Ist das Gewicht Bold oder Fill? | Ja. |
| Stammt das Icon aus dem BKM-Manifest? | Ja; andernfalls Manifest-Änderung beantragen. |
| Passt das Symbol zu einer eindeutigen Bedeutung? | Ja; keine dekorative Doppelung. |
| Erfüllt die Farbkombination ausreichenden Kontrast? | Ja; in finaler Größe visuell geprüft. |
| Werden lokale SVGs für Print/PDF genutzt? | Ja. |
| Wurden andere Iconbibliotheken oder Emoji vermieden? | Ja. |

## Herkunft und Lizenz

Die kuratierten Assets stammen aus [Phosphor Icons Core](https://github.com/phosphor-icons/core), Release `v2.0.8`, und stehen unter der MIT-Lizenz. Der vollständige Lizenztext wird mit den übernommenen SVGs im Asset-Ordner versioniert. Bei einem Upgrade werden Release, Manifest und Lizenznachweis gemeinsam aktualisiert.
