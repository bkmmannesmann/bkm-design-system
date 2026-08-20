# BKM Mannesmann — Brand Assets

Dieses Verzeichnis enthält alle offiziellen Marken-Assets für die digitale und analoge Anwendung.

## Ordnerstruktur

```
assets/
├── icons/
│   ├── phosphor/       ← Kuratierte Phosphor-Bold- und Fill-Rohpfade mit Manifest
│   └── tds/            ← Fester, rendererfester Satz für technische Datenblätter
├── keyvisual/          ← Keyvisual-Varianten (SVG + PNG)
├── logos/              ← Logo-Varianten (SVG + PNG)
└── README.md           ← Diese Datei
```

## TDS-Abschnittsicons

Der Ordner `icons/tds/` enthält genau neun rendererfeste Abschnittsicons für technische Datenblätter. Die Dateien sind nach ihrem Inhaltsblock benannt und ihre verbindliche Zuordnung, Phosphor-Bold-Quelle sowie Quell- und Rendererprüfsummen stehen in `icons/tds/manifest.json`.

Der TDS-Satz ist über Phosphor-Bold-Quell- und Rendererprüfsummen als eigene freigegebene Version gepinnt; er darf nicht stillschweigend durch eine andere Version aus `icons/phosphor/` ersetzt werden. Die Dateien in `icons/tds/` enthalten zusätzlich die feste Lime-Füllung `#b4e717`, da WeasyPrint die per CSS gesetzte `currentColor`-Variable in Inline-SVGs nicht zuverlässig übernimmt. Details und die vollständige Blockzuordnung stehen in [`docs/icon-system.md`](../docs/icon-system.md).

## Keyvisual

Das Keyvisual besteht aus drei Chevron-Elementen in den BKM-Grüntönen. Es symbolisiert den Trocknungsprozess: von Pure Green (Frische/Aufbruch) über Transition Green (Übergang/Transformation) zu Deep Green (Tiefe/Schutz).

**CRITICAL: Das Keyvisual darf NIEMALS in Code nachgebaut werden. Es wird ausschließlich als Bild-Asset eingebunden.**

| Datei | Farben | Einsatz auf Hintergrund |
|-------|--------|------------------------|
| `keyvisual-on-light.svg` | Pure Green + Transition Green + Deep Green | White (#ffffff), Sand White (#f6f5f2) |
| `keyvisual-on-dark.svg` | Komplett Weiß | Deep Green (#1c4b42), Transition Green (#287d4b), Stone Grey (#494949) |

**Verboten:** Keyvisual auf Pure Green (#4daf46) oder Lime Green (#b4e717) Hintergrund platzieren — ein Chevron würde visuell verschwinden.

## Logo-Varianten

Das BKM Mannesmann Logo besteht aus der Wortmarke "BKM" und dem Claim "Für eine lebenswerte Zukunft".

| Datei | Wortmarke | Claim | Einsatz auf Hintergrund |
|-------|-----------|-------|------------------------|
| `bkm-logo-on-light.svg` | Deep Green (#1c4b42) | Deep Green (#1c4b42) | White, Sand White |
| `bkm-logo-on-dark.svg` | Weiß (#ffffff) | Weiß (#ffffff) | Deep Green, Transition Green, Stone Grey |
| `bkm-logo-on-deep-green.svg` | Weiß (#ffffff) | Lime Green (#b4e717) | Deep Green (#1c4b42) |
| `bkm-logo-fachbetrieb-on-light.svg` | Stone Grey (#494949) | Transition Green (#287d4b) | White, Sand White |
| `bkm-logo-black.svg` | Schwarz (#000000) | Schwarz (#000000) | White, Sand White (Reserve/Print) |

### Kontrast-Validierung (WCAG AA)

Alle Kombinationen sind auf ausreichenden Kontrast geprüft:

| Kombination | Kontrast | Status |
|-------------|----------|--------|
| Deep Green auf White | 9.84 | PASS |
| Deep Green auf Sand White | 9.02 | PASS |
| Weiß auf Deep Green | 9.84 | PASS |
| Weiß auf Transition Green | 5.09 | PASS |
| Weiß auf Stone Grey | 9.00 | PASS |
| Lime Green auf Deep Green | 6.74 | PASS |
| Stone Grey auf White | 9.00 | PASS |
| Transition Green auf White | 5.09 | PASS |
| Schwarz auf White | 21.00 | PASS |

### Warum Pure Green nicht als Claim-Farbe?

Pure Green (#4daf46) auf White hat nur **2.79 Kontrast** — das reicht nicht für kleinen Text (WCAG AA erfordert 4.5). Deshalb wird im Fachbetrieb-Logo **Transition Green** (#287d4b, Kontrast 5.09) für den Claim verwendet.

## Formate

- **SVG** (Primärformat): Verlustfrei skalierbar, Farben als Präsentationsattribute eingebettet (`fill="#hex"`)
- **PNG** (Fallback): Transparenter Hintergrund, 2x-Auflösung für Retina-Displays

### SVG-Export-Einstellungen (Adobe Illustrator)

| Einstellung | Wert |
|-------------|------|
| SVG-Profile | SVG 1.1 |
| CSS-Eigenschaften | **Präsentationsattribute** (nicht Stilelemente!) |
| Bildposition | Einbetten |
| Responsiv | **Deaktiviert** |
| Dezimalstellen | 2 |
| Kodierung | Unicode (UTF-8) |
