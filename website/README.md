# BKM Mannesmann — Website (Vertical Slice)

Statischer Prototyp der neuen Corporate Website. Kein Build-Schritt, keine Runtime-Dependencies.

## Vorschau

```bash
cd website && python3 -m http.server 8000
# → http://localhost:8000
```

## Seiten

| Pfad | Seite |
|------|-------|
| `/` | Startseite |
| `/feuchtigkeit-verstehen/` | Problem-Hub: Schadensbilder, Ursachen, Risiko, FAQ |
| `/feuchtigkeit-verstehen/feuchte-check/` | Geführte Selbstdiagnose (clientseitig) |
| `/loesungen/selbst-sanieren/` | Weg 1: Home Line / DIY |
| `/loesungen/fachbetrieb/` | Weg 2: Pro Line / Anfrage, Unternehmen, Partner |

## Architektur

- `css/tokens.css` — Design Tokens, 1:1 aus `/DESIGN.md` (dort ändern, nicht hier erfinden)
- `css/base.css` — Reset, Typografie, Layout, Komponenten, Signature Elements
- `js/main.js` — Navigation, Reveals, Feuchte-Check, Formular-Validierung (<8 KB, defer; Seite funktioniert vollständig ohne JS)
- `assets/` — entschlackte Kopien der Brand-Assets (Logos/Keyvisual ohne Illustrator-Metadaten)

Verbindliche Grundlagen: `/DESIGN.md` (Abschnitt „Website System"), `docs/design/creative-direction.md`, `docs/strategy/website-strategy.md`, `docs/architecture/website-architecture.md`. Qualitätsstand: `docs/reviews/final-design-audit.md`.

## Bewusste Prototyp-Grenzen (Go-Live-Aufgaben, siehe roadmap.md M5)

- Anfrageformular hat noch kein Backend (Erfolgszustand ist clientseitig).
- Fotografie fehlt (Image Direction definiert, Shooting ausstehend) — keine Fake-Fotos eingesetzt.
- TT-Norms-Pro-Webfont-Lizenz für die Zieldomain verifizieren.
- Header/Footer sind pro Seite dupliziert (Preis des Null-Build-Ansatzes); bei Skalierung SSG einführen.
