# Schnellstart — Anweisungen zum Kopieren

> Fertige Prompts für den Umbau des Support-Cockpits auf `bkm-app`.
> Einer davon wird kopiert, die Klammern ausgefüllt, abgeschickt.

## Vorher: welcher Weg?

| Situation | Weg |
|---|---|
| Claude Code oder Claude mit GitHub-Zugriff auf das Repo | **A** |
| Claude.ai ohne Repo-Zugriff | **B** |
| Es soll eine **neue** Ansicht entstehen, keine bestehende umgestellt | **C** |

---

## A — Bestehende Anwendung umstellen (mit Repo-Zugriff)

```
Im Repo bkmmannesmann/bkm-design-system liegt ein Skill für
Anwendungs-Oberflächen: skills/bkm-app.

Lies zuerst, in dieser Reihenfolge:
  1. skills/bkm-app/SKILL.md        — 24 verbindliche Regeln
  2. skills/bkm-app/MIGRATION.md    — Ist-Stand, jede Abweichung einzeln, Reihenfolge
  3. skills/bkm-app/tokens.css      — die semantische Token-Ebene
  4. DESIGN.md und AGENTS.md        — die Marke darunter, unverändert gültig

Die Golden Reference liegt unter
skills/bkm-app/templates/bkm-cockpit/demo.html (748 KB, Schriften und Bilder
eingebettet). Lies sie erst, wenn du eine konkrete Ansicht baust, und dann
gezielt den Abschnitt, den du brauchst — nicht vorsorglich komplett.

Setze anschließend Stufe 1 aus MIGRATION.md um: Token-Ebene, Statussystem,
Kontraste, Form. Das ist reine Token-Arbeit ohne Layoutänderung.

WICHTIG — die Abgrenzung steht in MIGRATION.md unter „Was übernommen wird":
- Übernommen wird Gestaltung UND Verhalten: Navigationsmodell, Reihenfolge der
  Informationen, Zustände, Rückfragen, Tastaturverhalten. Das ist ausdrücklich
  auch eine UX-Änderung, nicht nur ein Anstrich.
- NICHT übernommen wird Inhalt: keine Kundennamen, Produktdaten, Preise,
  Kennzahlen oder Bestandszahlen aus der Vorlage. Das sind Beispieldaten aus
  Bildschirmfotos, teils gekürzt, fachlich ungeprüft. Die echten Werte kommen
  aus der Anwendung.

Zeig mir vor dem Umsetzen, was du in Stufe 1 ändern würdest.
```

Danach Stufe für Stufe weiter — 2 (Kopfleiste, Navigation, Zustände),
3 (Ansichten), 4 (Muster, die überall greifen). Jede Stufe einzeln beauftragen; die
Reihenfolge in `MIGRATION.md` ist nach Wirkung je Aufwand sortiert.

---

## B — Ohne Repo-Zugriff

`skills/bkm-app/templates/bkm-cockpit/demo.html` aus dem Repo herunterladen und
an den Chat anhängen. Die Datei ist eigenständig — Schriften, Logo, Keyvisual,
Texturen und Icons sind eingebettet. Dazu `SKILL.md` und `MIGRATION.md` als Text
einfügen. Dann:

```
Anbei die Golden Reference des BKM Support-Cockpits sowie die Regeln und der
Migrationsleitfaden.

Stelle [Ansicht / Bereich] unserer laufenden Anwendung darauf um.

Halte dich an die Regeln in SKILL.md. Verwende ausschließlich die semantischen
Tokens aus der Vorlage (--surface-*, --text-*, --accent, --status-*), nie eine
feste Markenfarbe — das würde den Day/Night-Umschalter zerstören.

Übernimm Gestaltung UND Verhalten. Übernimm KEINE Inhalte: die Namen, Zahlen,
Preise und Kennzahlen in der Vorlage sind Beispieldaten und fachlich ungeprüft.

Zeig mir das Ergebnis in beiden Themes und bei 1440, 834 und 390 Pixeln Breite.
```

---

## C — Eine neue Ansicht bauen

```
Baue die Ansicht [Name] für das BKM Support-Cockpit.

Nutze den bkm-app-Skill.
Baue auf skills/bkm-app/templates/bkm-cockpit/demo.html auf: kopiere die
Struktur, ersetze nur den Inhalt im <main>. Lass Tokens, Komponenten-CSS,
Schriften, Icons und den Theme-Umschalter unverändert.

Halte die 24 Regeln aus SKILL.md ein. Rendere zur Kontrolle in beiden Themes
und in drei Breiten (1440 / 834 / 390).
```

---

## Was zurückkommen sollte

Wenn die Anweisung greift, erkennt man es an diesen Punkten:

- **Keine feste Markenfarbe** außerhalb der Token-Blöcke. Prüfbar:
  `grep -n '#b4e717\|#1c4b42\|#287d4b'` über die Komponenten findet nichts.
- **Beide Themes funktionieren**, und im Tag-Theme ist der Akzent Transition
  Green, nicht Lime.
- **Kein Bedienelement unter 44 px** auf Touch, kein seitliches Scrollen bei
  390 px.
- **Tastaturfokus sichtbar** auf jedem Bedienelement.
- **Genau eine Unbounded-Zeile** je Ansicht.
- **Keine Beispieldaten** aus der Vorlage in der Anwendung.

Stimmt einer dieser Punkte nicht, wurde die Vorlage nachgebaut statt übernommen.
Dann hilft der Hinweis: *„Bau nicht neu — kopiere die Struktur aus demo.html und
ersetze nur den Inhalt."*

---

## Bekannte Stolpersteine

**Die Vorlage wird komplett gelesen und der Kontext ist voll.** 748 KB, das
meiste davon eingebettete Schriften und Bilder. Anweisen, gezielt den benötigten
Abschnitt zu lesen.

**Die Beispieldaten landen in der Anwendung.** Der häufigste Fehler. Der Absatz
zur Abgrenzung gehört in jeden Prompt, nicht nur in den ersten.

**Es wird nur umgefärbt.** Dann fehlt der Hinweis, dass auch Verhalten übernommen
wird — Navigationsmodell, Reihenfolge der Informationen, Rückfragen, Zustände.
Die Tabelle dazu steht in `MIGRATION.md` unter „Übernommen wird: Gestaltung und
Verhalten", inklusive dem, was jeder Punkt technisch voraussetzt.
