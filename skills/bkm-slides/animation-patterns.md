# BKM Slides — Animation Patterns

> CSS-only Animationen für Slides. Kein JavaScript erforderlich. Alle Animationen nutzen `@keyframes` und sind GPU-beschleunigt (`transform`, `opacity`).

## Grundregeln

1. **Animationen sind subtil** — Sie unterstützen den Inhalt, dominieren ihn nicht.
2. **Maximal 2 Animationen pro Slide** — Mehr erzeugt visuelles Rauschen.
3. **Dauer: 0.4s–1.2s** — Schnell genug für Aufmerksamkeit, langsam genug für Eleganz.
4. **Easing: ease-out oder cubic-bezier(0.16, 1, 0.3, 1)** — Natürliche Verzögerung.
5. **`prefers-reduced-motion`:** Alle Animationen müssen bei aktivierter Einstellung deaktiviert werden.

---

## 1. Fade In Up (Einblenden von unten)

Universelle Einblende-Animation für Textblöcke und Karten.

```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}

/* Gestaffelte Verzögerung */
.delay-1 { animation-delay: 0.1s; }
.delay-2 { animation-delay: 0.2s; }
.delay-3 { animation-delay: 0.3s; }
.delay-4 { animation-delay: 0.4s; }
.delay-5 { animation-delay: 0.5s; }
```

**Einsatz:** Headlines, Body-Text, Badges, Cards — alles was beim Slide-Wechsel eingeblendet werden soll.

---

## 2. Scale In (Skalierung von klein nach normal)

Für Statistik-Werte und Zahlen.

```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-scale-in {
  animation: scaleIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}
```

**Einsatz:** Große Zahlen (TT Norms Pro), Statistik-Blöcke, Icons.

---

## 3. Slide In Left (Einfahren von links)

Für Split-Layouts: Linke Hälfte fährt von links ein.

```css
@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-slide-left {
  animation: slideInLeft 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}
```

---

## 4. Slide In Right (Einfahren von rechts)

Für Split-Layouts: Rechte Hälfte fährt von rechts ein.

```css
@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.animate-slide-right {
  animation: slideInRight 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
}
```

---

## 5. Divider Grow (Akzentlinie wächst)

Für die BKM-Divider-Linie.

```css
@keyframes dividerGrow {
  from {
    width: 0;
    opacity: 0;
  }
  to {
    width: 60px;
    opacity: 1;
  }
}

.animate-divider {
  animation: dividerGrow 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  opacity: 0;
  width: 0;
}
```

---

## 6. Counter Up (Zähler-Animation)

Für Statistik-Werte. Nutzt CSS `@property` für animierte Zahlen.

```css
@property --num {
  syntax: '<integer>';
  initial-value: 0;
  inherits: false;
}

@keyframes countUp {
  from { --num: 0; }
  to { --num: var(--target); }
}

.animate-counter {
  animation: countUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  counter-reset: num var(--num);
}

.animate-counter::after {
  content: counter(num);
}
```

**Einsatz:** `<span class="animate-counter stat__value" style="--target: 96;">` → Zählt von 0 auf 96.

---

## 7. Pulse Glow (Subtiles Pulsieren)

Für Akzent-Elemente wie Badges oder Icons.

```css
@keyframes pulseGlow {
  0%, 100% {
    box-shadow: 0 0 0 0 var(--slide-accent);
  }
  50% {
    box-shadow: 0 0 20px 4px var(--slide-accent);
  }
}

.animate-pulse-glow {
  animation: pulseGlow 2s ease-in-out infinite;
}
```

**Einsatz:** Sparsam! Maximal ein Element pro Slide. Für "Live"-Indikatoren oder CTA-Buttons.

---

## 8. Noise Shimmer (Textur-Bewegung)

Subtile Bewegung der Noise-Textur für lebendige Hintergründe.

```css
@keyframes noiseShimmer {
  0% { background-position: 0 0; }
  100% { background-position: 256px 256px; }
}

.noise-animated::after {
  animation: noiseShimmer 8s linear infinite;
}
```

**Einsatz:** Auf dunklen Slides (Deep Green, Stone Grey) für subtile Lebendigkeit.

---

## Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Kombinations-Empfehlungen

| Slide-Typ | Animation 1 | Animation 2 |
|-----------|-------------|-------------|
| Titel | Headline: fadeInUp | Divider: dividerGrow (delay-2) |
| Inhalt (Text) | Label: fadeInUp | Body: fadeInUp (delay-2) |
| Inhalt (Split) | Links: slideInLeft | Rechts: slideInRight (delay-1) |
| Daten | Zahlen: scaleIn (gestaffelt) | Labels: fadeInUp (delay-3) |
| CTA | Headline: fadeInUp | Button: pulseGlow (delay-5) |
