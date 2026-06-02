# BKM Fonts

## Enthaltene Schriften

| Datei | Schrift | Gewicht | Rolle |
|-------|---------|---------|-------|
| `Unbounded_400.woff2` | Unbounded | Regular (400) | Display (selten) |
| `Unbounded_700.woff2` | Unbounded | Bold (700) | Display |
| `Unbounded_900.woff2` | Unbounded | Black (900) | **H1-Headlines, primäre Buttons** |
| `TT_Norms_Pro_Compact_Regular.woff2` | TT Norms Pro Compact | Regular (400) | Body, Labels, technische Werte, UI-Elemente |
| `TT_Norms_Pro_Bold.woff2` | TT Norms Pro | Bold (700) | Hervorgehobene Informationen, wichtige Labels |

> **Unbounded ist selbst gehostet** (Latin-Subset inkl. Umlauten, von Google Fonts) —
> **nicht** mehr per CDN laden. Beide Schriften per `@font-face` einbinden; in
> eigenständigen/verschickten Decks als Base64 einbetten (`@font-face` für Unbounded
> analog zu TT Norms unten).

## Einbindung (CSS @font-face)

```css
@font-face {
  font-family: 'TT Norms Pro';
  src: url('./assets/fonts/TT_Norms_Pro_Compact_Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'TT Norms Pro';
  src: url('./assets/fonts/TT_Norms_Pro_Bold.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
```

## Typografie-System (Zwei Stimmen)

| Stimme | Schrift | Einsatz |
|--------|---------|---------|
| **Ankündigen** | Unbounded 900 UPPERCASE | H1-Headlines, primäre Buttons |
| **Lesen & Spezifizieren** | TT Norms Pro 400/700 | Alles andere: Body, H2–H6, Labels, technische Werte, Preise, UI |

## Lizenz

Proprietär — BKM Mannesmann AG. Nur für interne Nutzung und BKM-Projekte.
