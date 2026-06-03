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

### 10. Keyvisual (nur Titelseiten)

```css
.keyvisual {
  position: absolute;
  right: 0;                     /* bündig mit rechtem Folienrand */
  top: 50%;
  transform: translateY(-50%);  /* vertikal zentriert */
  height: 560px;                /* ~52% der Folie, vollständig sichtbar */
  width: auto;                  /* nicht angeschnitten */
  opacity: 0.85;
  pointer-events: none;
  z-index: 0;                   /* hinter Inhalts-Cards/Text */
}
```

**Regeln:** Rechte Kante bündig mit dem Folienrand, vertikal zentriert, **vollständig
sichtbar** (nicht angeschnitten, oben/unten frei). Variante je Hintergrund: dunkel →
weiß, hell → grün. Nie links/mittig, nie gedreht/gespiegelt.

### 11. Innerer Glass-Glow (optional, nur Titel-Slides)

```css
.glass-card::before {
  content: ''; position: absolute; inset: 0; border-radius: 16px;
  background: linear-gradient(160deg, rgba(255,255,255,0.04) 0%, transparent 40%);  /* BKM AG */
  /* background: linear-gradient(160deg, rgba(255,255,255,0.3) 0%, transparent 40%); /* Fachbetrieb */
  pointer-events: none;
}
```

### 12. Bilder & Grafiken (Fotos, Diagramme)

Folien dürfen Bilder zeigen — nicht nur Text. Drei Muster:

**a) Gerahmtes Bild (Figure) — Text + Foto nebeneinander**

```css
.figure{position:relative;border-radius:24px;overflow:hidden;        /* Glas: 24px · Editorial/Bold: 8–16px */
  border:1px solid rgba(255,255,255,0.28);
  box-shadow:0 8px 32px rgba(0,0,0,0.28),inset 0 1px 0 rgba(255,255,255,0.4);}
.figure img{display:block;width:100%;height:100%;object-fit:cover;}  /* randscharf, nie verzerren */
.figure figcaption{position:absolute;left:0;right:0;bottom:0;padding:22px 28px;color:#fff;font-size:18px;
  background:linear-gradient(transparent,rgba(15,38,32,0.9));}
```

**b) Vollflächiges Foto + Overlay** (Hero/Kapitel; Glas/Text darüber)

```css
.bg-photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:0;}
.bg-photo + .overlay{position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(28,75,66,.78),rgba(15,38,32,.6));}
/* Glas-Card / Text mit z-index > 0 darüber */
```

**c) Bild in Card** — den `.img`-Bereich einer Card mit `<img style="object-fit:cover">`
füllen statt des Gradient-Platzhalters.

**Regeln:**
- Immer `object-fit: cover` (nie verzerren); Eckenradius der Familie folgen.
- Foto unter Glas/Overlay legen, damit Text lesbar bleibt — Kontrast per Screenshot prüfen.
- Bild austauschen = nur `src` ersetzen (im Skill **per Pfad**, im Standalone-Demo als Data-URI).
- Format: **JPEG** für Fotos (klein halten), **PNG** nur für Grafiken mit Transparenz.
- Das **Keyvisual ist kein Inhaltsbild** (eigene Regel, nur Deckblatt).

### 13. Texturierte Hintergründe + Rhythmus

Statt flacher Verläufe: **texturierte Hintergründe** (weiches Licht auf Deep Green,
BKM-Grün + Grain) in `assets/backgrounds/bg-green-texture-1…4.jpg`, im Deck `.bg.t1…t4`.

```css
.bg{position:absolute;inset:0;background-size:cover;background-position:center;}
.bg.t1{background:#0f2620 url(.../bg-green-texture-1.jpg) center/cover;}
/* t2…t4 analog */
```

**Regeln:**
- Varianten **rotieren** über die Folien (`t1,t2,t3,t4,t1,…`) — nie zweimal dieselbe nebeneinander.
  Pflicht bei langen Decks (Anti-Monotonie über 30–50+ Folien).
- Dunkel-links-Varianten (`t1`,`t4`) für links-bündigen Text; `t2`/`t3` für zentrierte Inhalte.
- Glas-Cards/Text müssen lesbar bleiben — Kontrast per Screenshot prüfen.
- Nur BKM-Grün; **kein** Lime-/Pure-Green-Vollflächen-Grund (Keyvisual-Verbot beachten).

### 14. Motion (Reveal) + Headline-Casing (Hybrid)

- **Reveal:** Inhaltselemente `reveal` + Stagger `d1…d5` (Fade + Hochgleiten beim Folienwechsel).
  Print/PDF & `prefers-reduced-motion` zeigen alles ruhig (in der Engine bereits gelöst).
- **Casing (Hybrid A+B):** Cover & Kapitel-Trenner **UPPERCASE**; Inhalts-/Section-Headlines
  **Mixed-Case** via Klasse `.mixed` (`text-transform:none`). Akzentwort über Lime, nie kursiv.

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
✓ Keyvisual (nur Deckblatt)           ✗ Wavy Backgrounds
✓ Bilder/Grafiken (Figure, Foto+Overlay)
✓ Texturierte Hintergründe (rotierend)
✓ Reveal-Motion + Hybrid-Casing
✓ Innerer Glass-Glow                  ✗ Border-Left auf Glass-Cards
```

---

## Positiv-Regeln (Anti-Slop)

> Nicht nur „was verboten ist", sondern **wie man aktiv gut gestaltet**.
> Idee adaptiert aus Open Design (nexu-io/open-design, Apache-2.0).

1. **Ein Akzent, max. 2× pro Folie.** Lime (bzw. Pure Green im Fachbetrieb) ist ein
   Signal, kein Dekor — pro Folie höchstens zweimal einsetzen, sonst verliert es Wirkung.
2. **Display- und Body-Schrift nie dieselbe Familie.** BKM = Unbounded (Display) +
   System-Sans/TT Norms Pro (Body). Headlines nie in der Body-Schrift, Fließtext nie in Unbounded.
3. **Farben mit `oklch()` ableiten statt Hex erfinden.** Wenn eine Zwischenstufe nötig ist
   (z. B. Hover, Verlauf), bestehende BKM-Token über `oklch()` aufhellen/abdunkeln —
   **nie** einen neuen, freien Hex-Wert außerhalb der Palette einführen.
4. **Hintergrund aus Marke/Domäne, nie generisch.** Deep-Green-/Sand-Flächen, Brand-Blobs,
   echte Bautenschutz-Fotos. **Kein** beiger/peach/„cozy"-Default-Canvas, kein App-Chrome-Grau.
5. **Eine dominante Aussage pro Folie.** Eine Headline + 3–4 Stützelemente. Kein
   konkurrierender Doppel-Fokus, keine gleichförmigen Kachel-Teppiche.
6. **Inhalte spezifisch.** Echte Zahlen/Projekte statt „Lorem"/generischer Stat-Slop.
