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
3. **Tiefe über die Flächenleiter, nicht über Schatten.** Auf dunklem Grund trägt
   kein Schatten. Vier Stufen: `--surface-0` Arbeitsfläche, `--surface-1` Karte,
   `--surface-2` angehoben/Hover, `--surface-3` Overlay. Im Day-Theme greift
   stattdessen Shadow-as-Border (`--elevation-card`), wie in `DESIGN.md`.
4. **Form: 4 px Bedienelemente, 8 px Eingaben, 12 px Karten. Keine Pillen.**
   `--radius-avatar` ist ausschließlich für Avatare und Statuspunkte.
   (`DESIGN.md`: „Never pill-shaped in the primary brand context.")
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
9. **Icons ausschließlich aus `assets/icons/phosphor/` in Bold oder Fill.**
   Keine andere Bibliothek, keine Emoji, keine nachgezeichneten Symbole.
   Fehlt ein benötigtes Icon im Manifest, wird es dort ergänzt — nicht ersetzt.
10. **Zahlen tabellarisch.** `font-variant-numeric: tabular-nums` für alle Werte,
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

**Vor der Übergabe prüfen:** In beiden Themes rendern. Kein Text unter AA. Keine
literale Farbe außerhalb der Token-Blöcke. Tastaturfokus auf jedem Bedienelement
sichtbar. Genau eine Unbounded-Zeile.

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

- **Es gibt bisher eine Vorlage** (Startbildschirm). Noch offen: Fall-/Detailansicht
  mit Assistent, Datentabelle, Filterleiste, Formularseite, Leerzustände.
- **`components.html`** (lebende Komponenten-Referenz, wie bei `bkm-slides`) fehlt.
- **Deterministische Prüfregeln** (`rules.json`) sind konzipiert, aber nicht gebaut.
  Geplant: literale Farbe in Komponente, Pill-Radius, Unbounded < 18 px, Statusfarbe
  ohne Token, Kartenverschachtelung > 2, Kontrast unter AA, mehr als ein Primary-CTA.
- **Das Icon-Manifest deckt den App-Bedarf nicht.** Beim Bau der Vorlage fehlte
  bereits `sign-out` (Abmelden). Der Abmelde-Knopf läuft deshalb als Text. Weitere
  Kandidaten für `assets/icons/phosphor/manifest.json`: `sign-out`, `bell`,
  `dots-three`, `sort-ascending`, `funnel-simple`, `caret-up-down`, `upload-simple`.
  Regel 9 gilt unverändert — ergänzen statt ersetzen.
