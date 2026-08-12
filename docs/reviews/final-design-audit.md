# Final Design Audit — BKM Website Vertical Slice

> Output 8. Stand: 2026-08-12, nach drei Review-Runden (Screenshots Mobile 390 / Tablet 768 / Desktop 1440 / Large 1920, automatisierte Interaktions- und Accessibility-Tests).

## 1. Geprüfter Umfang

`website/` — Startseite, Feuchtigkeit verstehen (Hub), Feuchte-Check, Selbst sanieren, Fachbetrieb. Statisches HTML/CSS + 7,5 KB Vanilla-JS, null Runtime-Dependencies.

## 2. Review-Verfahren

1. **Screenshot-Review** aller Seiten in 4 Viewports, drei Iterationsrunden.
2. **Funktionstests** (Playwright): Feuchte-Check-Komplettdurchlauf inkl. Validierung und Schwere-Logik, Mobile-Drawer inkl. Escape, Formular-Validierung + Erfolgszustand. Alle bestanden, keine JS-Fehler.
3. **axe-core-Audit** (WCAG 2.x A/AA) auf allen 5 Seiten: **0 Verstöße** (nach Fix).
4. **Council-Review** (LLM-Council-Verfahren aus dem Source-Audit): fünf unabhängige Perspektiven, Konfliktentscheidung am Projektziel.

## 3. In den Review-Runden gefundene und behobene Mängel

| Fund | Schwere | Fix |
|------|---------|-----|
| Outline-Button im Hero unsichtbar (Dark-Kontext-Regel griff nicht auf `.hero`) | hoch | `.hero .btn-outline` weiß |
| `hidden`-Attribut von `display:flex` überschrieben → DIY-Panel blieb bei schweren Schadensbildern sichtbar (Bruch der Ehrlichkeits-Logik!) | hoch | globales `[hidden]{display:none!important}` |
| Kontrast `--on-dark-faint` (50 % Weiß auf Deep Green ≈ 3,4:1) — 5 Elementtypen unter AA | hoch | Token auf 62 % (≈ 4,9:1), axe danach clean |
| Wandschnitt-Labels liefen aus dem SVG-viewBox | mittel | Labelgröße/Umbruch/Positionen |
| `text-wrap: balance` + `overflow-wrap: break-word` brach Wörter falsch („Kellerwan d") | mittel | break-word entfernt, `&shy;` in Komposita |
| Zwei-Wege-Weiche mit ausgeblendetem Panel ließ leere Grid-Spalte | mittel | `:has()`-Regel auf einspaltig |
| Symptom-Raster 4+2 unruhig | niedrig | `.grid-3` (2×3) |
| „MicroPorex®" im Messwert-Block umgebrochen | niedrig | `value-word`-Variante |
| Fehlendes Favicon (404) | niedrig | SVG-Favicon im Icon-System |

## 4. Bewertung (1–10)

| Kategorie | Score | Begründung / Maßnahme |
|-----------|:---:|------------------------|
| Brand Distinctiveness | **8** | Grün-Geschichte, Sperrschicht-Kante, Wandschnitt, Messwert-Blöcke sind unverwechselbar BKM; keine SaaS-Muster. **Unter 9, weil echte Fotografie fehlt** (Material-/Baustellenbilder gem. Image Direction). Maßnahme: Foto-Shooting gem. `creative-direction.md` §6, Einbau in Hero/Verstehen — Roadmap M5. |
| Visual Hierarchy | **9** | Kicker→Headline→Lead→Aktion konsequent; ein H1 pro Seite; klare Sektionsrhythmik dunkel/hell. |
| Typography | **9** | Unbounded 900 nur ≥18px, H1 uppercase/H2+ sentence case, fluid Scale, 68ch-Maß, deutsche Komposita mit Trennstellen. |
| Layout | **9** | 12-col-Logik, 7/5-Splits, harte Schnitte, keine Cardisierung von Erklärinhalten. |
| UX Clarity | **9** | Symptom-Einstieg → Verstehen → Check → Zwei Wege in ≤2 Klicks von jeder Seite; ehrliche Empfehlung bei schweren Schäden verifiziert. |
| Conversion | **8** | Beide Pfade durchgängig, ein Primary-CTA pro Fold, Mikro-Conversions vorhanden. **Unter 9, weil das Anfrageformular noch kein Backend hat** (Prototyp-Erfolgszustand). Maßnahme: Formular-Endpoint + Spam-Schutz beim Go-Live — Roadmap M5, offene Entscheidung #4. |
| Motion | **9** | Nur Feedback (150ms), Reveals (einmalig, 600ms, 16px) und Trocknungslinie; komplett `prefers-reduced-motion`-gesichert; Seite funktioniert ohne JS vollständig. |
| Mobile | **9** | Eigene Kompositionsentscheidungen (Keyvisual entfällt, Drawer-Nav, gestapelte Weiche), 48px-Targets. |
| Accessibility | **9** | axe: 0 Verstöße; Skip-Link, Landmarks, Fokusführung im Check (Heading-Focus je Schritt), `aria-live`-Ergebnis, `aria-current`-Nav, Escape schließt Drawer. Screenreader-Testing mit echter AT bleibt Go-Live-Gate. |
| Performance | **10** | Startseite 317 KB unkomprimiert inkl. aller 3 Fonts; 7,5 KB JS (defer); SVG statt Bildern; Fonts preloaded, `font-display: swap`; Logos von 508 KB auf 12 KB entschlackt; keine Third-Party-Requests. |
| Maintainability | **9** | Tokens 1:1 aus DESIGN.md, keine Dependencies, framework-neutral (SSG-Migration 1:1 möglich). Header/Footer-Duplikation über 5 Seiten ist der bewusste Preis für Null-Build — bei Skalierung auf >10 Seiten SSG einführen (Roadmap M5). |
| Perceived Quality | **9** | Wirkt gestaltet, nicht generiert: eigenes Diagrammsystem, echte Inhalte, keine erfundenen Beweise, keine Anti-Slop-Muster. |

**Kategorien unter 9:** Brand Distinctiveness (8) und Conversion (8) — beide hängen an externen Ressourcen (Fotoproduktion, Formular-Backend), nicht an Gestaltungs- oder Codequalität. Maßnahmen sind oben definiert und in `roadmap.md` M5 verankert; sie sind vor dem Go-Live zu erledigen, nicht im Prototyp simulierbar (erfundene Fotos/Fake-Submit wären ein Verstoß gegen die Anti-Slop-Regeln).

## 5. Council-Protokoll (Kurzfassung)

- **Creative Director:** Signature Elements tragen; Wandschnitt ist das stärkste Asset — auf Ursachen-Detailseiten ausbauen. Kein Widerspruch zur Marke gefunden.
- **UX Lead:** Zwei-Wege-Anatomie überall identisch ✓; Wunsch: Check-Ergebnis teilbar machen (URL-Parameter) — M5.
- **Frontend Architect:** Null Dependencies, Tokens sauber; Duplikation akzeptiert, SSG-Punkt dokumentiert.
- **Conversion Specialist:** PLZ-Feld früh im Formular ✓; Telefon optional ✓; Backend fehlt (siehe Score).
- **A11y/Perf Engineer:** axe clean, Budget exzellent; TT-Norms-Webfont-Lizenz bleibt rechtliches Go-Live-Gate (Source-Audit §7.1).

## 6. Definition-of-Done-Abgleich

| Kriterium | Status |
|-----------|:---:|
| Nutzer versteht in Sekunden, was BKM macht (Hero: Claim + Klartext-Lead) | ✓ |
| Betroffene verstehen ihren nächsten Schritt (Symptom-Einstieg + Check) | ✓ |
| DIY-Weg auffindbar und vollständig | ✓ |
| Profi-Weg auffindbar mit Anfrage | ✓ (Backend: Go-Live) |
| Marke wirkt kompetent, etabliert, modern | ✓ |
| Design wirkt intentional statt generiert | ✓ |
| Code ruhig, verständlich, wartbar | ✓ |
| Motion subtil und selbstverständlich | ✓ |
| Erkennbare eigene visuelle Handschrift (5 Signature Elements) | ✓ |
