# BKM Mannesmann — Wiederverwendbarer Slide-Prompt (v3)

> Dieser Prompt wird vor jeder Slide-Erstellung eingefügt. Er enthält **exakte CSS-Werte** — nicht interpretieren, sondern 1:1 kopieren. Basierend auf getesteten, freigegebenen Slides.

---

## Grundprinzip

Du erstellst Präsentationsfolien für die BKM Mannesmann AG bzw. deren Fachbetriebe. Das Design nutzt **Glasmorphismus auf Foto-Hintergründen oder flachen BKM-Farben**. Jede Slide ist eine eigenständige HTML-Datei (1280x720px).

---

## PFLICHT: Hintergrund-Fotos generieren

**Vor dem Erstellen der Slides** MÜSSEN passende Hintergrund-Fotos generiert werden. Jede Slide braucht ein eigenes Foto (oder bewusst eine flache BKM-Farbe).

**Prompt-Muster:**
```
Professional architectural photography of [MOTIV], dramatic natural lighting,
high contrast, shot on medium format camera, editorial quality,
muted earth tones with green accents, 16:9 aspect ratio
```

**Motive:** Keller, Fundamente, Fassaden, Baustellen, Labor, Materialien, grüne Gebäude, Handshake, Tablet/Software.

**Alternative:** Flache BKM-Farbe (Deep Green `#1c4b42` oder Sand `#f6f5f2`) — Glasmorphismus hebt sich trotzdem ab.

---

## 1. Farbkontext bestimmen

### BKM AG Kontext (dunkel)

| Element | Exakter Wert |
|---------|-------------|
| Overlay (Titel) | `linear-gradient(140deg, rgba(28,75,66,0.80) 0%, rgba(28,75,66,0.60) 50%, rgba(28,75,66,0.75) 100%)` |
| Overlay (Content) | `linear-gradient(160deg, rgba(28,75,66,0.82) 0%, rgba(28,75,66,0.65) 60%, rgba(28,75,66,0.78) 100%)` |
| Glass-Card bg | `rgba(255, 255, 255, 0.07)` |
| Glass-Card border | `1px solid rgba(255, 255, 255, 0.12)` |
| Glass-Card blur | `backdrop-filter: blur(20px)` |
| Glass-Card radius | `16px` (Titel), `14px` (Content) |
| Inner Glow | `linear-gradient(160deg, rgba(255,255,255,0.04) 0%, transparent 40%)` |
| Headlines | `#ffffff` (Unbounded 900, UPPERCASE) |
| Body-Text | `rgba(255,255,255,0.85)` |
| Muted Text | `rgba(255,255,255,0.7)` |
| Section-Label | `#b4e717` (11px, uppercase, 0.12em spacing) |
| Checkmarks | `#b4e717` |
| Icon-Circle bg | `rgba(180, 231, 23, 0.12)` |
| Icon-Circle color | `#b4e717` |
| Status-Badge bg | `rgba(180, 231, 23, 0.1)` |
| Status-Badge border | `1px solid rgba(180, 231, 23, 0.25)` |
| Status-Badge color | `#b4e717` |
| Footer-Bar bg | `rgba(28, 75, 66, 0.95)` |
| Footer-Icon | `#b4e717` |
| Footer-Text | `#ffffff`, 14px |
| Page-Num | `rgba(255,255,255,0.3)`, 11px |
| Logo | `bkm-logo-white-puregreen.png` |
| Keyvisual | `keyvisual-on-dark.svg`, opacity `0.18`, width `22%` |
| Akzentlinie | `#b4e717`, 4px breit, left 7%, top 18%, height 60% |

### Fachbetrieb Kontext (hell)

| Element | Exakter Wert |
|---------|-------------|
| Overlay (Titel) | `linear-gradient(140deg, rgba(246,245,242,0.88) 0%, rgba(246,245,242,0.75) 50%, rgba(246,245,242,0.85) 100%)` |
| Overlay (Content) | `linear-gradient(160deg, rgba(246,245,242,0.88) 0%, rgba(246,245,242,0.78) 60%, rgba(246,245,242,0.86) 100%)` |
| Glass-Card bg | `rgba(255, 255, 255, 0.55)` |
| Glass-Card border | `1px solid rgba(255, 255, 255, 0.7)` |
| Glass-Card blur | `backdrop-filter: blur(20px)` |
| Glass-Card radius | `16px` (Titel), `14px` (Content) |
| Inner Glow | `linear-gradient(160deg, rgba(255,255,255,0.3) 0%, transparent 40%)` |
| Headlines | `#1c4b42` (Deep Green, Unbounded 900, UPPERCASE) |
| Body-Text | `#494949` (Stone Grey) |
| Muted Text | `rgba(73, 73, 73, 0.7)` |
| Section-Label | `#4daf46` (11px, uppercase, 0.12em spacing) |
| Checkmarks | `#4daf46` |
| Icon-Circle bg | `rgba(77, 175, 70, 0.1)` |
| Icon-Circle color | `#4daf46` |
| Status-Badge bg | `rgba(77, 175, 70, 0.12)` |
| Status-Badge border | `1px solid rgba(77, 175, 70, 0.35)` |
| Status-Badge color | `#287d4b` |
| Footer-Bar bg | `rgba(40, 125, 75, 0.95)` |
| Footer-Icon | `#b4e717` (Lime — auch im Fachbetrieb!) |
| Footer-Text | `#ffffff`, 14px |
| Page-Num | `rgba(73, 73, 73, 0.3)`, 11px |
| Logo | `bkm-logo-stonegrey-puregreen.png` |
| Keyvisual | `keyvisual-on-light.svg`, opacity `0.15`, width `22%` |
| Akzentlinie | `#4daf46`, 4px breit, left 7%, top 18%, height 60% |

---

## 2. Typografie (nur 3 Stufen, KEIN Italic)

| Stufe | Font | Gewicht | Größen | Regeln |
|-------|------|---------|--------|--------|
| **Headline** | Unbounded | 900 | 56px (Titel), 48/38/36px (Content), 17px (Card-Titel) | UPPERCASE, letter-spacing -0.04em (Titel) / -0.03em (Content), **KEIN Italic** |
| **Subtitle** | system-ui | 700 | 18/17/16/13px (Subtitles), 11px (Labels), 10-11px (Badges) | Labels: uppercase + 0.12em spacing |
| **Body** | system-ui | 400 | 17/15/14/13px (Body), 14px (Footer) | line-height 1.6 |

**Google Fonts CDN:**
```html
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@900&display=swap" rel="stylesheet">
```

**Font Awesome CDN:**
```html
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
```

---

## 3. Slide-Container

```css
.slide-container {
  width: 1280px;
  min-height: 720px;
  position: relative;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
```

---

## 4. Spacing

| Element | Wert |
|---------|------|
| Horizontal-Padding | `80px` |
| Top-Padding (Titel) | `56px` |
| Top-Padding (Content) | `48px` |
| Glass-Card Padding (Titel) | `52px 48px` |
| Glass-Card Padding (Content) | `36px 40px` |
| Glass-Card Padding (Kompakt) | `32px 32px 28px 32px` |
| Card-Gap | `28px` |
| Content-Gap | `40px` |
| Footer-Bar Padding | `16px 80px` |
| Checklist-Gap | `16px` |
| Feature-List-Gap | `18px` |

---

## 5. Signatur-Elemente

### Vertikale Akzentlinie (Titelseiten)
- Position: `left: 7%`, `top: 18%`, `height: 60%`
- Breite: `4px`, border-radius: `2px`
- Farbe: `#b4e717` (BKM AG) / `#4daf46` (Fachbetrieb)

### Footer-Bar (Content-Slides)
- Volle Breite, `padding: 16px 80px`
- BKM AG: `rgba(28, 75, 66, 0.95)`
- Fachbetrieb: `rgba(40, 125, 75, 0.95)`
- Icon: `#b4e717` (Lime in beiden Kontexten)
- Text: `#ffffff`, 14px

### Keyvisual (nur Titelseiten)
- Position: `top: 0`, `right: 0`, `height: 100%`, `width: 22%`
- `object-fit: cover`, `object-position: left center`
- Opacity: `0.18` (BKM AG) / `0.15` (Fachbetrieb)
- **Regeln:** Immer rechts, immer angeschnitten, nie links/mittig/gedreht/gespiegelt

### Logo
- Titel-Slide: `top: 36px`, `right: 48px`, `height: 38px`
- Content-Slide: `top: 32px`, `right: 44px`, `height: 32px`

---

## 6. Was NICHT in BKM-Slides gehört

- ❌ Noise-Texturen
- ❌ Aurora-Gradients
- ❌ Bento-Grids
- ❌ Floating Badges
- ❌ Spotlight/Glow-Effekte
- ❌ Animierte Text-Effekte
- ❌ Box-Shadows auf Cards
- ❌ Unbounded Italic (Faux-Italic sieht falsch aus)
- ❌ Border-Left auf Glass-Cards
- ❌ Dashboard-artige symmetrische Grids
- ❌ Wavy Backgrounds

---

## 7. Qualitätskontrolle

Vor Auslieferung jeder Slide:

- [ ] Hintergrund-Foto generiert ODER bewusst flache BKM-Farbe?
- [ ] Glasmorphismus-Werte exakt aus diesem Prompt kopiert?
- [ ] Overlay-Gradient exakt kopiert?
- [ ] Unbounded 900 UPPERCASE, KEIN Italic?
- [ ] Logo im richtigen Kontext?
- [ ] Keyvisual: rechts, 22%, korrekte Opacity, nur Titelseite?
- [ ] Footer-Bar auf Content-Slides?
- [ ] Akzentlinie auf Titelseite?
- [ ] Font Awesome + Google Fonts CDN eingebunden?
- [ ] Mindestens 25% Weißraum?
