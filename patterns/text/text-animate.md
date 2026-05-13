# Text Animate

> Buchstaben-weise Einblende-Animation für Überschriften. Jeder Buchstabe erscheint einzeln mit konfigurierbarem Timing und Richtung.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Componentry — Text Animate](https://www.componentry.fun/docs/text-animate) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Hero-Headlines, Sektions-Titel, Scroll-Reveal-Überschriften |

## BKM-Typografie-Regeln

Der Text Animate Effekt muss die Unbounded-Regeln einhalten:

| Regel | Wert |
|-------|------|
| Font | Unbounded |
| Weight | 900 (font-black) |
| Case | UPPERCASE |
| Mindestgröße | 36px (headline-sm) |
| Empfohlene Größe | 44px–72px |
| Letter-Spacing | -0.02em bis -0.04em |

## BKM-angepasster Code

```tsx
import { TextAnimate } from "@/components/ui/text-animate";

// BKM AG — Hero-Headline auf dunklem Hintergrund
export function BkmAnimatedHero() {
  return (
    <section className="bg-[#1c4b42] min-h-[560px] flex items-center">
      <div className="max-w-[1280px] mx-auto px-8 md:px-16">
        <TextAnimate
          text="SCHUTZ DER HÄLT"
          className="font-['Unbounded'] text-5xl md:text-7xl font-black uppercase text-white tracking-[-0.04em] leading-none"
          animation="slideUp"
          delay={0.05}
          duration={0.4}
        />
      </div>
    </section>
  );
}

// Fachbetrieb — Sektions-Titel auf hellem Hintergrund
export function FachbetriebAnimatedTitle() {
  return (
    <TextAnimate
      text="UNSERE LEISTUNGEN"
      className="font-['Unbounded'] text-3xl md:text-4xl font-black uppercase text-[#1a1a1a] tracking-tight"
      animation="fadeIn"
      delay={0.03}
      duration={0.3}
    />
  );
}
```

## Animations-Varianten

| Variante | Beschreibung | BKM-Empfehlung |
|----------|-------------|----------------|
| `slideUp` | Buchstaben gleiten von unten ein | Hero-Headlines |
| `fadeIn` | Buchstaben blenden ein | Sektions-Titel |
| `blurIn` | Buchstaben werden scharf | Akzent-Wörter |

## Einschränkungen

- **Nur für Unbounded-Headlines** — Nie für TT Norms Pro-Body-Text oder TT-Norms-Pro-Specs.
- **Maximal eine Animation pro Viewport** — Mehrere gleichzeitig erzeugen Chaos.
- **Delay max. 0.05s pro Buchstabe** — Längere Delays wirken träge.
- **`prefers-reduced-motion`:** Bei aktivierter Einstellung sofort alle Buchstaben zeigen.
- **Nicht bei Seitenlade** — Nur bei Scroll-Reveal oder nach bewusster User-Interaktion.
