---
name: bkm-app
description: Erstellt und prüft markenkonforme BKM-Anwendungsoberflächen — Cockpits, Portale, interne Werkzeuge und andere datendichte Web-Apps. Verwende diesen Skill für jede BKM-Oberfläche, in der gearbeitet wird (Formulare, Listen, Tabellen, Dashboards, Assistenten). Für Marketing-Seiten `bkm-website`, für Präsentationen `bkm-slides`.
---

# BKM App-UI — Skill (v1)

> Werkzeug-Oberflächen im BKM Mannesmann Design System. Mit Day/Night-Umschalter
> auf einer semantischen Token-Ebene.

---

## Warum es diesen Skill gibt

`DESIGN.md` beschreibt drei Medien: Marketing-Website, Editorial/Print und
Datenblätter. Eine **Arbeitsfläche**, die jemand 50-mal am Tag benutzt, kommt darin
nicht vor. Wer eine solche Oberfläche allein aus `DESIGN.md` ableitet, bekommt
zwangsläufig den Marketing-Look: 72-px-Headlines über einer Kundenliste, Lime als
Dekoration, Deep Green als einzige Fläche, kein Statussystem, keine Zustände.

Dieser Skill schließt die Lücke. Er **ersetzt nichts** aus `DESIGN.md` — er
übersetzt die Marke in den Anwendungskontext und definiert, was dort zusätzlich
gebraucht wird.

---

## Wann diesen Skill verwenden

- Cockpits, Portale, Admin-Bereiche, interne Werkzeuge
- Alles mit Formularen, Listen, Tabellen, Filtern, Assistenten, Auswertungen
- BKM AG **und** Fachbetrieb (die Kontexte sind eine eigene Achse, siehe unten)

**Nicht** für: Landing Pages und Produktseiten (→ `bkm-website`),
Decks (→ `bkm-slides`), technische Datenblätter (→ `docs/print-anwendungen.md`).

---

## Verbindliche Regeln (immer anwenden)

1. **Nur semantische Tokens.** Komponenten lesen ausschließlich `--surface-*`,
   `--text-*`, `--accent*`, `--status-*`, `--data-*`. Eine literale Markenfarbe
   (`#b4e717`, `var(--bkm-lime)`) in einer Komponente zerstört den Day/Night-Switch.
   Das ist die wichtigste Regel — alle anderen folgen daraus.
2. **Lime ist interaktiv, nie dekorativ.** Buttons, Links, aktive Zustände,
   Fokusringe. Nicht für Sektionslabels, nicht für Diagrammbalken, nicht für Icons
   im Ruhezustand, nicht als Fläche. (`DESIGN.md`: „never decorative, never on
   large surfaces".)
3. **Tiefe aus Flächenleiter *und* Material.** Vier Stufen tragen die Hierarchie:
   `--surface-0` Arbeitsfläche, `--surface-1` Karte, `--surface-2` angehoben/Hover,
   `--surface-3` Overlay. Dazu Material über `--card-sheen` und `--elevation-card`:
   auf dunklem Grund eine Lichtkante oben plus enger Schatten unten (ein großer
   weicher Schatten trägt dort nicht), auf hellem Grund Shadow-as-Border wie in
   `DESIGN.md`. Die Lichtkante ist derselbe „inset highlight", den `DESIGN.md`
   für die Stufe *Featured* vorsieht — kein neuer Effekt.
   Ohne Material wirkt eine Oberfläche flach, auch wenn alle Tokens stimmen.
4. **Form: 4 px Bedienelemente, 8 px Eingaben, 12 px Karten. Keine Pillen.**
   `--radius-avatar` ist ausschließlich für Avatare und Statuspunkte.
   (`DESIGN.md`: „Never pill-shaped in the primary brand context.")
   Ausnahme mit eigenem Token: Umschalter, Filter und Reiter laufen auf
   `--radius-switch` (10 px) statt 4 px — sie sind Schienen, keine Knöpfe, und
   wirken bei 4 px hart. 10 px ist bewusst die Obergrenze; alles darüber wird
   zur Pille und bricht die Regel. Ein Wert, zentral drehbar.
5. **Unbounded trägt genau eine Zeile pro Screen.** Weight 900, nie unter 18 px.
   Kartentitel, Zeilentitel, Kundennamen und Panel-Köpfe laufen in TT Norms Bold —
   sie sind Inhalt, keine Ankündigung.
6. **Status nur aus dem Statussystem.** Vier Zustände (`success`, `warning`,
   `danger`, `info`) mit je Text- und Flächentoken. Keine ad hoc gewählten Orange-
   oder Rottöne.
7. **Kontrast wird gerechnet, nicht geschätzt.** Jede neue Farbkombination gegen
   `--surface-2` (Night) bzw. `--surface-0` (Day) prüfen. `--text-muted` hält im
   Night-Theme AA nur auf `--surface-0`/`--surface-1`, nicht auf `--surface-2`.
8. **Zustände sind Pflicht.** Hover, Aktiv, Fokus (`:focus-visible`), Deaktiviert,
   Leer, Ladend. Tastaturfokus ist keine Kür — in einem Werkzeug ist er die
   halbe Bedienung.
9. **Die Kopfleiste wechselt mit dem Theme — und mit ihr der Akzent.**
   Nacht: Deep Green mit Lime. Tag: Transition Green mit **Weiß**. Lime auf
   Transition Green liegt bei 3.49 und ist nur für großen Text zulässig; für
   Bedienelemente ist es ausgeschlossen. Chrome-Farben laufen deshalb über
   eigene Tokens (`--chrome-*`), nie über die Marken-Konstanten direkt —
   ein hart geschriebenes `var(--bkm-deep-green)` in einer Chrome-Komponente
   bricht den Wechsel. Achtung beim gedämpften Ton: auf Transition Green
   erreicht selbst Weiß nur 5.09, ein echter Sekundärton ist dort kaum
   möglich (`#eaf4ee` = 4.53 ist das Maximum).
10. **Markenmaterial statt Selbsterfundenem.** Der Grund nutzt die Texturen aus
   `assets/backgrounds/`, mit dem Flächentoken überdeckt (`--ground`), damit die
   gerechneten Kontraste gültig bleiben. Das Keyvisual aus `assets/keyvisual/`
   gehört genau in ein Hero-Band, bündig rechts, vertikal zentriert, nie
   angeschnitten und nie in Code nachgebaut. Glasmorphismus ist erlaubt,
   maximal ein bis zwei Elemente pro Viewport — im Cockpit die Kopfleiste.
11. **Icons ausschließlich aus `assets/icons/phosphor/` in Bold oder Fill.**
   Keine andere Bibliothek, keine Emoji, keine nachgezeichneten Symbole.
   Fehlt ein benötigtes Icon im Manifest, wird es dort ergänzt — nicht ersetzt.
12. **Ein Icon setzt nie seine eigene Farbe.** Es erbt die Textfarbe seines
    Kontextes (`fill: currentColor`), damit die Farbregel automatisch greift:

    | Fläche | Icon-/Textfarbe | Kontrast |
    |---|---|---|
    | Deep Green `#1c4b42` | **Lime** `#b4e717` | 6.74 |
    | Transition Green `#287d4b` | **Weiß** `#ffffff` | 5.09 |
    | Pure Green `#4daf46` | **Weiß** `#ffffff` | — |
    | Weiß / Sand White | **Transition Green** `#287d4b` | 5.09 / 4.67 |

    Lime auf Transition Green ist mit 3.49 nur für großen Text zulässig und
    deshalb für Icons und Beschriftungen ausgeschlossen (Kontrastmatrix,
    `DESIGN.md`). Beim Einbetten von SVGs als `<symbol>` darauf achten, dass
    `fill="currentColor"` erhalten bleibt — sonst fallen die Pfade still auf
    Schwarz zurück.
13. **Auswahl trägt immer die Akzentfarbe.** Ausgewählt, aktiv, aktueller
    Bereich, gesetzter Filter — alles über `--selected-*`, nie über eine
    eigene Farbe. Die **Größe** des Elements entscheidet nur die *Form*:

    | | Behandlung |
    |---|---|
    | Kleines Bedienelement (Tab, Chip, Umschalter, Filter) | mit `--selected-fill` gefüllt, Text `--selected-on-fill` |
    | Große Fläche (Karte, Kachel, Panel) | `--selected-ring` plus `--selected-surface`, Titel in `--accent` |

    Eine große Fläche vollflächig in Lime zu füllen verstößt gegen `DESIGN.md`
    („never on large surfaces"). Der Ring erreicht dasselbe, ohne die Regel zu
    brechen — und bleibt bei zwanzig Karten auf einem Screen lesbar.
14. **Überall gleich bedienbar.** Zwei getrennte Achsen, die oft verwechselt
    werden: die **Breite** entscheidet, was sichtbar bleibt und wie umgebrochen
    wird; die **Eingabeart** entscheidet, wie groß Bedienelemente sein müssen.
    Ein Tablet ist breit *und* fingerbedient — beides muss zusammen greifen.
    Unter `@media (pointer:coarse)` hält jedes Bedienelement mindestens 44 px
    (WCAG 2.5.5). Dieser Block gehört ans **Ende** des Stylesheets: steht er
    weiter oben, gewinnen die späteren Komponentenregeln bei gleicher
    Spezifität und die Ziele bleiben zu klein — ein Fehler, den man am
    Bildschirm nicht sieht. Vor der Übergabe in drei Größen prüfen
    (Desktop 1440, Tablet 834, Handy 390): kein seitliches Scrollen,
    kein Ziel unter 44 px auf Touch.
15. **In die Kopfleiste gehört nur, was man beim Arbeiten braucht.** Was man
    einmal einstellt — Sprache, Darstellung, Konto, Admin — gehört ins
    Kontomenü hinter dem Avatar, nicht dauerhaft in die oberste Zeile.
    Faustregel: höchstens vier Gruppen. Zeigt ein Element eine Zahl, die
    beim Arbeiten zählt (offene Positionen, ungelesene Meldungen), gehört
    sie sichtbar dazu; die Uhrzeit gehört nicht dazu, die zeigt das
    Betriebssystem. Tastenkürzel nur einblenden, wo sie wahr sind —
    ein „⌘K" auf einem Tablet ist eine Lüge.
16. **Der Rückweg gehört ins Chrome, nicht in die Seite.** Ein
    „Zurück zur Übersicht" am Kopf des Inhalts scrollt weg und ist damit
    genau dann verschwunden, wenn man ihn braucht. Stattdessen eine
    **Brotkrume, die mit der Kopfleiste zusammen klebt** (`.topbar` als
    gemeinsamer Sticky-Container — kein gerechneter `top`-Versatz, der
    bricht, sobald die Leiste umbricht).
    Der Bereichsname darin ist zugleich ein **Wechsler**: er listet alle
    Bereiche und markiert den aktuellen. Damit wird aus Hub-and-Spoke ein
    Netz — man springt direkt weiter, statt jedes Mal über die Startseite
    zu gehen. Auf der Startseite selbst ist die Brotkrume verborgen.
17. **Fortschritt und Balken über `--progress-fill`.** Nacht: Lime → Weiß.
    Tag: Transition Green → Pure Green. Kein Farbunterschied je Balken — die
    Länge trägt den Wert, Farbe würde ihn doppelt kodieren; die `--data-*`-Rampe
    bleibt für Diagramme, in denen Farbe tatsächlich eine Kategorie unterscheidet.
    Grafische Elemente brauchen 3:1 gegen ihre Umgebung (WCAG 1.4.11). Wo eine
    Markenfarbe das nicht schafft — Pure Green auf hellem Grund erreicht
    höchstens 2.79 — übernimmt eine Kontur (`--progress-edge`) statt die Farbe
    zu ändern. Vorsicht: die Spur abzudunkeln hilft bei Pure Green **nicht**,
    es liegt luminanznah an einem Mittelgrau und der Kontrast sinkt dadurch.
18. **Lange Seitenspalten scrollen in sich selbst.** Eine Bewertungs- oder
    Kontextspalte, die höher ist als der Bildschirm, wird mit bloßem
    `position:sticky` unbrauchbar: der obere Rand klebt, der untere Teil bleibt
    unerreichbar. Richtig ist `sticky` **plus** `max-height:calc(100vh − Versatz)`
    und `overflow-y:auto`. Der Versatz ist die Summe aus Kopfleiste und Brotkrume.
    Unterhalb der Zweispaltigkeit fällt beides weg — dort steht die Spalte
    normal unter dem Inhalt.
19. **Die Bewertung zeigt zuerst, was zu tun ist.** In einem Werkzeug ist die
    Frage nicht „was weiß das System", sondern „was fehlt mir noch". Deshalb
    steht direkt unter dem Ergebnis der handlungsfähige Block („Was die
    Einschätzung jetzt hebt"), und die Belege — Indizien, Sperren, Gegenprüfungen —
    liegen darunter in `<details>`: verfügbar, aber nicht als Textwand
    ausgekippt. Fakten laufen als Schlüssel-Wert-Paare, nicht als Fließtext.
20. **Zerstörende Aktionen brauchen eine Rückfrage, die den Schaden benennt.**
    Nicht „Wirklich löschen?", sondern *was* verloren geht und *was daran hängt*
    („21-mal aufgerufen, in 3 Angeboten referenziert"). Die bestätigende Taste
    trägt `--status-danger`, nicht den Akzent — der Akzent führt sonst zum
    Löschen. Escape und Klick daneben brechen ab, der Fokus springt in den
    Dialog und beim Schließen zurück auf den Auslöser.
21. **Ein langes Formular braucht Orientierung und eine feste Sicherung.**
    Ab etwa sechs Abschnitten eine Abschnittsnavigation, die zeigt, wo man ist.
    Dazu eine Sicherungsleiste am unteren Rand, die den Änderungsstand nennt.
    `position:sticky` allein genügt dafür **nicht** — es wirkt nur innerhalb der
    Elternbox, und die ist bei kurzen Abschnitten kürzer als der Bildschirm;
    dann sitzt die Leiste am Inhaltsende statt unten. Die Spalte braucht
    `min-height:calc(100vh − Versatz)` und `margin-top:auto` auf der Leiste.
22. **Mehr als etwa zwölf gleichrangige Bereiche sind keine Reiter.**
    Eine umbrechende Pillenwand ist keine Navigation, sondern eine Liste.
    Ab dieser Größe eine gruppierte Seitenleiste mit Zählern — die Gruppen
    tragen die Orientierung, die Zähler den Zustand.
23. **Verschachtelung endet bei zwei Flächen.** Ab der dritten Ebene trägt die
    Flächenleiter nicht mehr: Karte in Karte in Karte wird zu Brei. Tiefere
    Strukturen bekommen eine Akzentschiene links und eine eigene Kopfzeile
    (`.block`), nicht eine weitere Fläche.
24. **Zahlen tabellarisch.** `font-variant-numeric: tabular-nums` für alle Werte,
    Mengen, Zeitstempel und Prozentangaben, damit Spalten stehen.

---

## Zwei unabhängige Achsen

Day/Night und BKM AG/Fachbetrieb werden regelmäßig verwechselt. Sie sind getrennt:

| | **Achse 1 — Theme** | **Achse 2 — Markenkontext** |
|---|---|---|
| Werte | `night` · `day` | BKM AG · Fachbetrieb |
| Wählt | Nutzer, jederzeit umschaltbar | Projekt, einmal festgelegt |
| Steuert | Flächen, Textfarben | Akzentfarbe, Logovariante |
| Akzent BKM AG | Night: Lime · Day: Transition Green | — |
| Akzent Fachbetrieb | Night: Pure Green · Day: Transition Green | — |

Ein helles Theme im BKM-AG-Kontext ist **nicht** der Fachbetrieb-Kontext.

**Warum der Akzent im Day-Theme wechselt:** Lime auf Sand White hat einen
Kontrast von 1.34, auf Weiß 1.46 — beides klarer Durchfall (Kontrastmatrix in
`DESIGN.md`). Transition Green liegt bei 4.67 bzw. 5.09 und ist laut `DESIGN.md`
ohnehin die vorgesehene Farbe für „links, secondary actions and hover states on
light surfaces". Der Wechsel ist also die Regel, nicht ihre Umgehung.

---

## Dichte-Dial

Ein Wert steuert, wie eng die Oberfläche läuft. Über `--density-row` und
`--density-pad` in `tokens.css`.

| Stufe | Zeile / Innenabstand | Wofür |
|---|---|---|
| 1 — luftig | 56 px / 28 px | Einstiegsseiten, Leerzustände, wenige Objekte |
| 2 — Standard | 44 px / 20 px | Cockpit-Startseite, Karten, Übersichten |
| 3 — dicht | 36 px / 14 px | Tabellen, Suchergebnisse, lange Listen |

Nicht innerhalb einer Ansicht mischen.

---

## Vorgehen

**Der Weg, der funktioniert — Vorlage kopieren, Inhalt ersetzen.**

Wie bei `bkm-slides`: Der markenkonforme Eindruck hängt an eingebetteten Assets
(Schriften, Logo, Icons) und an der Token-Architektur. Beides lässt sich aus
Markdown nicht rekonstruieren. Wer „liest die Doku und generiert neu" versucht,
bekommt eine generische Oberfläche.

**A — Claude Code mit dem Repo:**
```
Baue die Ansicht [Name] für das BKM Support-Cockpit.
Nutze den bkm-app-Skill, baue auf templates/bkm-cockpit/demo.html auf,
ersetze nur den Inhalt und rendere zur Kontrolle in beiden Themes.
```

**B — Claude.ai oder ein anderes Werkzeug ohne Repo:** `templates/bkm-cockpit/demo.html`
herunterladen (vollständig eigenständig — Schriften, Logo, Icons eingebettet) und
an den Chat anhängen:
```
Anbei die BKM-Cockpit-Vorlage. Baue daraus die Ansicht [Name].
Ersetze NUR Inhalt und Struktur im <main>. Lass Tokens, Komponenten-CSS,
Schriften, Logo, Icons und den Theme-Umschalter unverändert.
Verwende ausschließlich die semantischen Tokens, nie eine feste Farbe.
```

**Vor der Übergabe prüfen:** In beiden Themes rendern. In drei Breiten prüfen
(1440 / 834 / 390) — kein seitliches Scrollen, auf Touch kein Ziel unter 44 px.
Kein Text unter AA. Keine literale Farbe außerhalb der Token-Blöcke.
Tastaturfokus auf jedem Bedienelement sichtbar. Genau eine Unbounded-Zeile.

---

## Source of Truth

| Datei | Inhalt |
|---|---|
| `../../DESIGN.md`, `../../AGENTS.md` | Verbindliche Marken-Token und -Regeln |
| `../../docs/digitale-medien.md` | Web-App-Vorgaben (Header Deep Green, Fläche Sand White) |
| `../../docs/icon-system.md`, `../../assets/icons/phosphor/manifest.json` | Iconstandard |
| `tokens.css` | **Kanonische App-Tokens** — beide Themes, gerechnete Kontraste |
| `templates/bkm-cockpit/demo.html` | **Golden Reference** — Startbildschirm, eigenständig |

---

## Gerechnete Kontraste

Alle Werte nach WCAG 2.1, nicht geschätzt. Night gegen `--surface-1` (#1c4b42),
in Klammern gegen `--surface-2` (#235d52).

| Token | Wert | Night | Day (auf Sand White) |
|---|---|---|---|
| `--text-primary` | #fff / #1c4b42 | 9.84 (7.61) AA | 9.02 AA |
| `--text-secondary` | #c3d6d0 / #494949 | 6.49 (5.02) AA | 8.26 AA |
| `--text-muted` | #a8c2ba / #5f6b64 | 5.20 (4.02) AA¹ | 5.10 AA |
| `--accent` | #b4e717 / #287d4b | 6.74 (5.21) AA | 4.67 AA |
| `--status-warning` | #facc5e / #8a5a00 | 6.50 (5.02) AA | 5.44 AA |
| `--status-danger` | #ffa99c / #b91c1c | 5.34 (4.13) AA¹ | 5.93 AA |
| `--status-success` | #8fd96e / #1f7a3d | 5.77 (4.46) AA¹ | 4.93 AA |
| `--status-info` | #9ad8e8 / #1f6b7a | 6.26 (4.84) AA | 5.60 AA |

¹ Auf `--surface-2` nur AA-large (≥3:1). Diese Tokens nicht für Fließtext auf
angehobenen Flächen verwenden — dort `--text-secondary` nehmen.

Datenrampe Night: #cfe8dd · #a9d2c3 · #84bca9 · #63a690 — jede Stufe ≥3.46:1
gegen die Karte. Auf dunklem Grund läuft die Rampe **aufwärts**; eine ins Dunkle
laufende Rampe macht die unteren Werte unsichtbar.

---

## Bekannte Lücken (v1)

Ehrlich benannt, damit niemand improvisiert:

- **Sechs Ansichten sind gebaut**: Startbildschirm, Produkt suchen, Wissens-Hub,
  Angebots-Center, Produkt-Management, Fallansicht. Im Fall sind fünf der sieben
  Schritte ausgeführt (Kunde, Objekt, Geodaten, Fragen, Fotos, Ergebnis);
  die Mengenberechnung fehlt. Dazu der Admin-Bereich mit gruppierter
  Bereichsnavigation, Master-Detail, langem Formular und Auswertung.
  Noch offen: Ladezustände, Meldungen/Toasts, Paginierung, Mehrfachauswahl
  in Tabellen.
- **`components.html`** (lebende Komponenten-Referenz, wie bei `bkm-slides`) fehlt.
- **Deterministische Prüfregeln** (`rules.json`) sind konzipiert, aber nicht gebaut.
  Geplant: literale Farbe in Komponente, Pill-Radius, Unbounded < 18 px, Statusfarbe
  ohne Token, Kartenverschachtelung > 2, Kontrast unter AA, mehr als ein Primary-CTA.
- **Das Icon-Manifest ist nachgezogen.** Zwölf Icons ergänzt, alle aus der
  gepinnten Phosphor-Version 2.0.8: `sun`, `moon`, `sign-out`, `bell`,
  `dots-three`, `sort-ascending`, `funnel-simple`, `caret-up-down`,
  `upload-simple`, `camera`, `video`, `youtube-logo`. Der Bauprozess der
  Vorlage bricht seitdem ab, wenn ein verwendetes Icon nicht im Manifest
  freigegeben ist — Regel 11 kann damit nicht mehr unbemerkt verletzt werden.
  Offen bleibt nur, was künftige Ansichten zusätzlich brauchen.
