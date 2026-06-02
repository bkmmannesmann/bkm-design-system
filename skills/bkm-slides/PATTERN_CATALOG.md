# BKM Slides — Pattern-Katalog (v3)

> **Anti-Slop-Referenz (gültig in v5).** Welche Patterns erlaubt, eingeschränkt oder
> verboten sind. Gilt weiterhin für alle Familien. Ergänzend in v5: bewusster Dichte-Modus,
> Casing UPPERCASE **oder** Mixed-Case (nie kursiv), 8px-Rundung für Flächen-Elemente.

---

## Erlaubte Patterns

### 1. Glasmorphismus-Card (Hauptelement)

Das zentrale Gestaltungselement aller BKM-Slides. Funktioniert auf **zwei Hintergrund-Typen**: Foto mit Overlay ODER flache BKM-Farbe.

**BKM AG (auf dunklem Hintergrund):**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.07);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  padding: 52px 48px;   /* Titel-Slide */
  /* padding: 36px 40px; /* Content-Slide */
}
```

**Fachbetrieb (auf hellem Hintergrund):**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.55);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.7);
  border-radius: 16px;
  padding: 52px 48px;   /* Titel-Slide */
  /* padding: 36px 40px; /* Content-Slide */
}
```

### 2. Foto-Hintergrund mit Overlay

Generierte Fotos als Hintergrund, abgedunkelt/aufgehellt mit Gradient-Overlay.

**BKM AG:**
```css
.bg-overlay {
  background: linear-gradient(140deg,
    rgba(28, 75, 66, 0.80) 0%,
    rgba(28, 75, 66, 0.60) 50%,
    rgba(28, 75, 66, 0.75) 100%);
}
```

**Fachbetrieb:**
```css
.bg-overlay {
  background: linear-gradient(140deg,
    rgba(246, 245, 242, 0.88) 0%,
    rgba(246, 245, 242, 0.75) 50%,
    rgba(246, 245, 242, 0.85) 100%);
}
```

### 3. Flache BKM-Farbe als Hintergrund (Alternative zu Foto)

Nicht jede Slide braucht ein Foto. Glasmorphismus hebt sich auch auf flachen Farben ab.

```css
/* BKM AG */
.slide-container { background: #1c4b42; }

/* Fachbetrieb */
.slide-container { background: #f6f5f2; }
```

### 4. Vertikale Akzentlinie (Titelseiten)

```css
.accent-line {
  position: absolute; left: 7%; top: 18%;
  width: 4px; height: 60%;
  background: #b4e717;   /* BKM AG: Lime */
  /* background: #4daf46; /* Fachbetrieb: Pure Green */
  border-radius: 2px; z-index: 10;
}
```

### 5. Footer-Bar (Content-Slides)

```css
/* BKM AG */
.footer-bar {
  background: rgba(28, 75, 66, 0.95);
  padding: 16px 80px;
  display: flex; align-items: center; gap: 12px;
}

/* Fachbetrieb */
.footer-bar {
  background: rgba(40, 125, 75, 0.95);
  padding: 16px 80px;
  display: flex; align-items: center; gap: 12px;
}

.footer-icon { color: #b4e717; font-size: 16px; }  /* Lime in BEIDEN Kontexten */
.footer-text { font-weight: 400; font-size: 14px; color: #ffffff; }
```

### 6. Status-Badge

```css
/* BKM AG */
.status-badge {
  background: rgba(180, 231, 23, 0.1);
  border: 1px solid rgba(180, 231, 23, 0.25);
  border-radius: 20px; padding: 5px 14px;
  font-weight: 700; font-size: 10px;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: #b4e717;
}

/* Fachbetrieb */
.status-badge {
  background: rgba(77, 175, 70, 0.12);
  border: 1px solid rgba(77, 175, 70, 0.35);
  border-radius: 20px; padding: 6px 16px;
  font-weight: 700; font-size: 11px;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: #287d4b;
}
```

### 7. Checkmark-Listen

```css
.checklist { list-style: none; display: flex; flex-direction: column; gap: 16px; }
.checklist li { display: flex; align-items: center; gap: 14px; }
.check-icon { color: #b4e717; font-size: 16px; flex-shrink: 0; }  /* BKM AG */
/* .check-icon { color: #4daf46; }  /* Fachbetrieb */
.check-text { font-weight: 400; font-size: 15px; line-height: 1.4; }
```

### 8. Icon-Circles (Feature-Listen)

```css
/* BKM AG */
.feature-icon {
  width: 32px; height: 32px; border-radius: 8px;
  background: rgba(180, 231, 23, 0.12);
  display: flex; align-items: center; justify-content: center;
}
.feature-icon i { color: #b4e717; font-size: 14px; }

/* Fachbetrieb */
.feature-icon {
  width: 32px; height: 32px; border-radius: 8px;
  background: rgba(77, 175, 70, 0.1);
  display: flex; align-items: center; justify-content: center;
}
.feature-icon i { color: #4daf46; font-size: 14px; }
```

### 9. Prozess-Flow (CTA-Slides)

```css
.process-flow { display: flex; align-items: center; justify-content: center; gap: 12px; }
.step-circle {
  width: 48px; height: 48px; border-radius: 50%;
  background: rgba(77, 175, 70, 0.1);  /* Fachbetrieb */
  /* background: rgba(180, 231, 23, 0.08); /* BKM AG */
  border: 1px solid rgba(77, 175, 70, 0.25);
  display: flex; align-items: center; justify-content: center;
}
.process-arrow { color: rgba(77, 175, 70, 0.45); font-size: 18px; }
```

### 10. Keyvisual-Überlappung (nur Titelseiten)

```css
.keyvisual {
  position: absolute; top: 0; right: 0;
  height: 100%; width: 22%;
  object-fit: cover; object-position: left center;
  opacity: 0.18;   /* BKM AG */
  /* opacity: 0.15; /* Fachbetrieb */
  z-index: 5;
}
```

**Regeln:** Immer rechts, immer angeschnitten, nie links/mittig, nie gedreht/gespiegelt.

### 11. Innerer Glass-Glow (optional, nur Titel-Slides)

```css
.glass-card::before {
  content: ''; position: absolute; inset: 0; border-radius: 16px;
  background: linear-gradient(160deg, rgba(255,255,255,0.04) 0%, transparent 40%);  /* BKM AG */
  /* background: linear-gradient(160deg, rgba(255,255,255,0.3) 0%, transparent 40%); /* Fachbetrieb */
  pointer-events: none;
}
```

---

## Eingeschränkte Patterns

| Pattern | Einschränkung | Exakte Werte |
|---------|--------------|--------------|
| **Transition Green Fläche** | Max 1–2 Slides pro Deck, nur Fachbetrieb | `background: #287d4b` |
| **Dual-Card-Layout** | Max 2 Cards nebeneinander | `gap: 28px`, `padding: 32px 32px 28px 32px` |
| **Trends-Bar** (unterer Rand) | Nur auf Titelseiten | `padding: 16px 48px`, `gap: 40px` |

---

## Verbotene Patterns

Diese Patterns dürfen NICHT in BKM-Slides verwendet werden:

| Pattern | Warum verboten |
|---------|---------------|
| **Noise Texture** (SVG fractal noise) | BKM-Slides haben saubere Flächen |
| **Aurora Gradient** (animierte Farbverläufe) | Web-Dekoration, nicht Corporate |
| **Bento Grid** (gleichförmige Kacheln) | Dashboard-Ästhetik |
| **Floating Badges** (absolut positioniert) | Web-UI-Pattern |
| **Spotlight/Glow Effects** | Cursor-basiert |
| **3D Card Effect** | Zu verspielt |
| **Animated Text Effects** | Lenkt ab |
| **Wavy Background** | Verletzt harte Schnitte |
| **Box-Shadow auf Cards** | Nur Glasmorphismus-Effekt |
| **Unbounded Italic** | Kein echter Italic-Schnitt, Faux-Italic sieht falsch aus |
| **Border-Left auf Glass-Cards** | Glass-Cards nutzen den Frosted-Effekt als Differenzierung |
| **Mehrere konkurrierende Shadows** | Verwässert visuelle Hierarchie |

---

## Zusammenfassung

```
ERLAUBT:                              VERBOTEN:
──────────────────────────────        ──────────────────────────────
✓ Glasmorphismus-Cards                ✗ Noise-Texturen
✓ Foto-Hintergründe mit Overlay       ✗ Aurora-Gradients
✓ Flache BKM-Farben als Hintergrund   ✗ Bento-Grids
✓ Vertikale Akzentlinie               ✗ Floating Badges
✓ Footer-Bar                          ✗ Spotlight/Glow
✓ Status-Badges                       ✗ Animierte Hintergründe
✓ Checkmark-Listen                    ✗ Dashboard-Grids
✓ Icon-Circles                        ✗ Box-Shadows auf Cards
✓ Prozess-Flows                       ✗ Unbounded Italic
✓ Keyvisual-Überlappung               ✗ Wavy Backgrounds
✓ Innerer Glass-Glow                  ✗ Border-Left auf Glass-Cards
```
