# Bestehende Anwendung umstellen

> Von der laufenden Fassung des Support-Cockpits auf `bkm-app`. Dieses Dokument
> nennt die Unterschiede einzeln — was heute da ist, was daraus wird, warum, und
> wo es in der Golden Reference steht.

**Für neue Ansichten ist dieses Dokument nicht gedacht.** Dafür `SKILL.md` und
`templates/bkm-cockpit/demo.html`.

---

## Worauf sich der Ist-Stand bezieht

Aufgenommen aus Bildschirmfotos von **support.bkm-pro.de**, Stand 20.08.2026 und
04.09.2026: Startbildschirm, Feuchte-Check (7 Schritte), Sanierungssysteme,
Produkt suchen, Menge berechnen, Wissens-Hub, Angebots-Center,
Produkt-Management, Vertriebs-Center sowie der Admin-Bereich
(Anwendungsfälle, Richtlinien, Auswertungen).

**Kein Zugriff auf den Quellcode.** Alles unten beschreibt sichtbares Verhalten,
keine Implementierung. Wo die laufende Fassung inzwischen abweicht, gilt sie —
dann ist dieser Abschnitt zu korrigieren, nicht die Anwendung.

---

## Was übernommen wird — und was nicht

Die wichtigste Unterscheidung in diesem Dokument. Sie wird in beide Richtungen
falsch gelesen.

### Übernommen wird: Gestaltung **und** Verhalten

Nicht nur Farben und Abstände, sondern auch **Ablauf, Struktur und Logik** der
Oberfläche — was wann sichtbar ist, was ein Zustand bedeutet, was ein Klick
auslöst, in welcher Reihenfolge Informationen stehen. Die Umstellung ist
ausdrücklich auch eine UX-Änderung, nicht nur ein Anstrich.

Konkret sind das unter anderem:

| Verhalten | Was sich ändert |
|---|---|
| Navigationsmodell | Von Hub-and-Spoke zu einem Netz: der Bereichswechsler springt direkt weiter, statt über die Startseite zu zwingen |
| Informationsarchitektur | Einstellungen (Sprache, Darstellung, Admin) verlassen die Kopfleiste und liegen im Kontomenü |
| Schrittzustand | Die Schrittleiste **kennt** den Erfassungsstand: erledigt, lückenhaft mit Anzahl, offen — sie muss dafür an die Vollständigkeitsprüfung angebunden werden |
| Priorisierung | Die Bewertungsspalte ordnet nach Handlungsfähigkeit: Ergebnis, dann was fehlt, dann Belege |
| Progressive Offenlegung | Belege, Sperren und Gegenprüfungen liegen eingeklappt statt ausgekippt |
| Zerstörende Aktionen | Rückfrage, die die **Folgen benennt** — dafür müssen Referenzen gezählt werden („in 3 Angeboten referenziert") |
| Änderungsstand | Die Sicherungsleiste zeigt ungesicherte Änderungen — dafür muss der Formularzustand verfolgt werden |
| Auswahl und Filter | Reiter, Filter und Kategorien schalten tatsächlich um, mit korrekter Semantik (`aria-selected`, `aria-pressed`, `aria-current`) |
| Tastatur | Escape schließt, der Fokus springt in den Dialog und beim Schließen zurück auf den Auslöser |
| Vorbelegung | Die Theme-Wahl bleibt im `localStorage` erhalten |
| Kacheln | Zeigen ihren Bestand — das setzt eine Datenanbindung voraus, die es heute nicht gibt |

### Nicht übernommen wird: Inhalt

**Keine Zahl, kein Name, kein Text aus der Vorlage geht in die Anwendung.** Alle
Inhalte dort sind Beispieldaten, aus Bildschirmfotos abgeschrieben und teils
gekürzt:

- Kundennamen und Falldaten (Petersen, Großenwiehe, die Messwerte)
- Produktnamen, Mengenangaben, Verbrauchswerte, Preise und Staffeln
- Kennzahlen, Zeitreihe, Nutzerliste und E-Mail-Adressen im Admin
- Fachliche Aussagen zu Normen, Wassereinwirkungsklassen und Diagnosen
- Bestandszahlen auf den Kacheln (85 Produkte, 44 Regelwerke, 8 Analysen)

Diese Werte stammen aus der laufenden Anwendung und gehören dorthin — die
Vorlage ist keine Datenquelle. Fachliche Formulierungen sind sinngemäß
nachgeschrieben und **nicht fachlich geprüft**.

---

## Reihenfolge

Vier Stufen, absteigend nach Wirkung je Aufwand. Stufe 1 allein bringt den
größten Teil des Unterschieds, ohne ein einziges Layout anzufassen.

| Stufe | Inhalt | Layoutarbeit |
|---|---|---|
| 1 | Token-Ebene, Statussystem, Kontraste, Form | keine |
| 2 | Kopfleiste, Navigation, Zustände | gering |
| 3 | Die einzelnen Ansichten | je Ansicht |
| 4 | Querschnittsmuster (Bestätigung, Sicherung, Tabellen) | mittel |

---

## Stufe 1 — Tokens, Status, Kontrast, Form

Ohne Layoutänderung. Danach sieht die Anwendung anders aus, ohne dass sich etwas
verschoben hat.

**1.1 Semantische Token-Ebene einziehen.** `tokens.css` übernehmen. Jede
Komponente liest ab jetzt `--surface-1`, `--text-secondary`, `--accent`,
`--status-*` statt `#1c4b42`, `#b4e717` oder `var(--bkm-lime)`.
→ Regel 1. Ohne diesen Schritt funktioniert nichts Weitere.

**1.2 Flächenleiter statt fast gleicher Grüntöne.** Heute stapeln sich Karte auf
Karte auf Panel in kaum unterscheidbaren Grüns. Neu: vier definierte Stufen im
selben Farbton — Arbeitsfläche 13,5 %, Karte 20,2 %, angehoben 25 %, Overlay 29 %
Helligkeit. Deep Green bleibt die Kartenfarbe.
→ Regel 3.

**1.3 Lime auf interaktiv beschränken.** Heute limefarben: Sektionslabels,
Diagrammbalken, Icons im Ruhezustand, Fließtext-Hervorhebungen, ganze Kacheln.
Neu: nur Buttons, Links, aktive Zustände, Fokusringe.
→ Regel 2. Labels laufen auf `--text-muted`, Balken auf `--progress-fill`.

**1.4 Statussystem.** Heute mindestens drei verschiedene Orangetöne (OFFEN-Badge,
W2.1-E-Chip, Hinweiskästen), zwei Rottöne, zwei Grüns. Neu: vier semantische
Zustände mit je Text- und Flächentoken.
→ Regel 6.

**1.5 Kontraste ersetzen.** Graue Sekundärtexte auf Deep Green (Zeitstempel,
„Verschiebt die Aussagekraft", Quellenangaben) und Platzhalter in Suchfeldern
liegen unter AA. Neu: gerechnete Tokens, Tabelle in `SKILL.md`.
→ Regel 7.

**1.6 Form.** Heute durchgehend Pillen: Schritt-Reiter, DE/ES, Badges, CTAs. Neu:
4 px für Bedienelemente, 8 px Eingaben, 12 px Karten; Umschalter, Filter und
Reiter auf 10 px (`--radius-switch`). Pillen bleiben Avataren und Statuspunkten.
→ Regel 4.

**1.7 Icons erben die Textfarbe.** `fill: currentColor` statt fester Farbe. Damit
greift automatisch: auf Deep Green Lime, auf Transition Green Weiß.
→ Regel 12.

---

## Stufe 2 — Kopfleiste, Navigation, Zustände

**2.1 Kopfleiste ausdünnen.**

| Heute | Neu |
|---|---|
| Logo · Support-Cockpit · DE/ES · Suche mit ⌘K · Materialliste · Admin · Uhrzeit + Datum · Avatar + Name + Rolle · Abmelden-Icon | Logo · Suche · Avatar-Menü |

Sprache, Darstellung, Admin und Abmelden ziehen ins Kontomenü hinter dem Avatar.
Die Uhrzeit entfällt — die zeigt das Betriebssystem. Das Tastenkürzel entfällt,
es ist auf dem Tablet unwahr.
→ Regel 15. Vorlage: `.app-bar`, `.menu`.

**2.2 Day/Night-Umschalter.** Neu. Sonne und Mond im Kontomenü, ohne Wortmarke,
mit `aria-label`. Die Wahl liegt im `localStorage`, das Attribut heißt
`data-bkm-theme` — bewusst nicht `data-theme`, das kollidiert mit dem, was
Host-Umgebungen selbst setzen.
→ Vorlage: `.theme-toggle`.

**2.3 Die Kopfleiste wechselt mit dem Theme.** Nacht Deep Green mit Lime, Tag
Transition Green mit **Weiß**. Lime auf Transition Green liegt bei 3.49 und ist
für Bedienelemente ausgeschlossen.
→ Regel 9. Chrome-Farben laufen über `--chrome-*`, nie über Marken-Konstanten.

**2.4 „Zurück zur Übersicht" ersetzen.** Heute am Kopf des Inhalts, also
mitscrollend und weg, sobald man ihn braucht. Neu: eine Brotkrume, die mit der
Kopfleiste zusammen klebt, und deren Bereichsname zugleich ein Wechsler über
alle acht Bereiche ist. Damit wird aus Hub-and-Spoke ein Netz.
→ Regel 16. Vorlage: `.topbar`, `.crumbs`, `.menu--section`.

**2.5 Zustände nachrüsten.** Tastaturfokus fehlt heute vollständig. Neu:
`:focus-visible` mit Akzentring auf jedem Bedienelement, dazu Hover, Aktiv,
Deaktiviert, Leer.
→ Regel 8.

**2.6 Auswahl vereinheitlichen.** Heute unterschiedlich gelöst — im Wissens-Hub
eine vollflächig limefarbene Karte, anderswo gefüllte Pillen. Neu: die
Akzentfarbe gilt immer, die **Größe** entscheidet nur die Form. Kleine
Bedienelemente werden gefüllt, große Flächen bekommen Ring plus gedämpfte
Fläche.
→ Regel 13.

**2.7 Fingerbedienung.** Sieben Bedienelemente liegen unter 44 px. Neu: ein
`@media (pointer:coarse)`-Block **am Ende** des Stylesheets — steht er weiter
oben, gewinnen die späteren Komponentenregeln und die Ziele bleiben zu klein.
→ Regel 14.

---

## Stufe 3 — Die Ansichten

### Startbildschirm

| Heute | Neu |
|---|---|
| 6 Kacheln in Reihe 1, 2 verwaiste in Reihe 2 | 4 × 2 · *Optik* |
| Kacheln ohne Information | Bestandszahl je Kachel · **Verhalten**, braucht Datenanbindung |
| Sektionslabels in Lime | `--text-muted` |
| Balken in Lime, je Balken eine andere Farbe | ein Verlauf für alle; die Länge trägt den Wert |

### Feuchte-Check · Fallansicht

| Heute | Neu |
|---|---|
| 7 gleich aussehende Pillen | Schrittleiste mit Zustand: Haken = erledigt, orange Zahl = lückenhaft, grau = offen · **Verhalten**, braucht die Vollständigkeitsprüfung |
| Kundenname in Unbounded 900 | TT Norms Bold — ein Name ist Inhalt, keine Ankündigung (Regel 5) |
| Rechte Spalte: zehn gleich gewichtete Abschnitte, der handlungsfähige Teil ganz unten | Ergebnis, dann **„Was die Einschätzung jetzt hebt"**, erst danach die Belege — und die in `<details>` · **Verhalten**, die Reihenfolge ist die Änderung (Regel 19) |
| Geodaten als Fließtextwand | Befundliste: Merkmal, Aussage, Bewertung als Chip |
| Fakten als Fließtext | Schlüssel-Wert-Paare |

### Produkt suchen

Produktkarten sind heute komplett weiß mit dunklem Text — eine helle Insel im
dunklen Theme. Neu: **nur die Medienfläche** bleibt weiß, der Kartenkörper läuft
auf `--surface-1`. Freigestellte Produktfotos brauchen Weiß, der Text nicht.

### Wissens-Hub

Die ausgewählte Kategorie ist heute vollflächig Lime. Das verstößt gegen
„never on large surfaces". Neu: Ring plus gedämpfte Akzentfläche, Titel im
Akzent. Bei sieben Karten nebeneinander bleibt das lesbar, eine limefarbene
Fläche ist ein Schrei.

### Angebots-Center und Produkt-Management

Struktur bleibt. Kennzahl-Kacheln verlieren die Lime-Schiene links, Reiter laufen
auf `--radius-switch`, Statusbadges kommen aus dem Statussystem.

### Admin

| Heute | Neu |
|---|---|
| 19 Reiter, umbrechend auf drei Zeilen | gruppierte Seitenleiste: Inhalte, Regeln & Berechnung, Organisation, System — mit Zählern (Regel 22) |
| Zwölf Abschnitte über vier Bildschirme ohne sichtbare Sicherung | Abschnittsnavigation plus Sicherungsleiste mit Änderungsstand · **Verhalten**, der Formularzustand muss verfolgt werden (Regel 21) |
| Systemaufbau → Baustein → Option → Produktzeile als vier Flächen | Akzentschiene und Kopfzeile ab Ebene drei (Regel 23) |
| „Fall löschen" ohne erkennbare Rückfrage | Bestätigungsdialog, der die Folgen benennt · **Verhalten**, die Referenzen müssen gezählt werden (Regel 20) |
| Kennzahlen mit Lime-Schiene, Zeitreihe komplett in Lime | Kennzahlen ohne Schiene, Zeitreihe in der Datenrampe |
| Hilfetexte als lange Prosa neben der Beschriftung | `.help` unter der Beschriftung |

---

## Stufe 4 — Muster, die überall greifen

**4.1 Bestätigung für zerstörende Aktionen.** Nicht „Wirklich löschen?", sondern
*was* verloren geht und *was daran hängt*. Die Seitenbeschreibung des
Admin-Bereichs dokumentiert einen Datenverlust vom 28.07.2026 — dieses Muster ist
dort keine Kür. Die bestätigende Taste trägt `--status-danger`, nicht den Akzent.
→ Regel 20.

**4.2 Sicherungsleiste in langen Formularen.** `position: sticky` allein genügt
nicht; die Spalte braucht `min-height`, sonst sitzt die Leiste bei kurzen
Abschnitten am Inhaltsende statt unten.
→ Regel 21.

**4.3 Lange Seitenspalten scrollen in sich selbst.** Die Bewertungsspalte im Fall
ist höher als der Bildschirm. Mit bloßem `sticky` bleibt ihr unterer Teil
unerreichbar.
→ Regel 18.

**4.4 Datentabellen.** Sortierbare Kopfzeile, tabellarische Zahlen, Hover auf der
Zeile, waagerechtes Scrollen im eigenen Container.

---

## Was aus der Vorlage *nicht* übernommen wird

- **Die Inhalte.** Kundennamen, Produktzahlen, Kennzahlen, Zeitreihe — alles
  Beispieldaten aus den Bildschirmfotos. Siehe „Was übernommen wird" oben:
  Verhalten ja, Werte nein.
- **Der Knopf „Was ist anders?" und das Erklär-Panel.** Nur für die Vorstellung.
- **Die eingebetteten Assets.** Schriften, Logo, Keyvisual und Texturen liegen als
  data-URI in der Vorlage, damit sie an einen Chat angehängt werden kann. Im
  Einbau werden sie normal verlinkt — `tokens.css` macht das bereits so.
- **Der Platzhalter-Bereich „nicht ausgebaut".** Gerüst der Vorlage, kein Muster.

---

## Prüfen

Nach jeder Stufe, nicht erst am Ende:

- In **beiden Themes** rendern. Keine literale Markenfarbe außerhalb der
  Token-Blöcke — `grep -n '#b4e717\|#1c4b42\|#287d4b' ` über die Komponenten
  darf nichts finden.
- In **drei Breiten** prüfen: 1440, 834, 390. Kein seitliches Scrollen, auf Touch
  kein Bedienelement unter 44 px.
- **Kein Text unter AA.** Neue Farbkombinationen gegen `--surface-2` (Nacht) bzw.
  `--surface-0` (Tag) rechnen, nicht schätzen.
- **Tastaturfokus** auf jedem Bedienelement sichtbar.
- **Genau eine Unbounded-Zeile** pro Screen.
- **Jedes Icon im Manifest freigegeben.**
