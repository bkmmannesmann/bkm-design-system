# Text Hover Effect

> SVG-basierter Text-Effekt, bei dem die Buchstaben bei Hover einen animierten Strich-Effekt zeigen. Erzeugt einen technisch-präzisen Look, der zur BKM-Ästhetik passt.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Text Hover Effect](https://ui.aceternity.com/components/text-hover-effect) |
| **Lizenz** | MIT |
| **Tech** | React, SVG, Framer Motion |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Hero-Headlines, Sektions-Titel, Feature-Überschriften |

## BKM-Farbmapping

| Parameter | BKM AG (dunkler Hintergrund) | BKM AG (heller Hintergrund) | Fachbetrieb |
|-----------|------------------------------|----------------------------|-------------|
| Text-Stroke | `#b4e717` (Lime) | `#1c4b42` (Deep Green) | `#4daf46` (Pure Green) |
| Text-Fill (nach Animation) | `#ffffff` (Weiß) | `#1c4b42` (Deep Green) | `#287d4b` (Transition Green) |
| Hintergrund | `#1c4b42` (Deep Green) | `#ffffff` / `#f6f5f2` | `#ffffff` / `#f6f5f2` |

## Installation

```bash
npx shadcn@latest add @aceternity/text-hover-effect
```

## BKM-angepasster Code

```tsx
import { TextHoverEffect } from "@/components/ui/text-hover-effect";

// BKM AG — Auf dunklem Hintergrund
export function BkmHeroTitle() {
  return (
    <section className="bg-[#1c4b42] min-h-[400px] flex items-center justify-center">
      <TextHoverEffect
        text="SCHUTZ"
        className="font-['Unbounded'] font-black uppercase"
        strokeColor="#b4e717"    // Lime Stroke
        fillColor="#ffffff"       // Weiß Fill
      />
    </section>
  );
}

// BKM AG — Auf hellem Hintergrund
export function BkmSectionTitle() {
  return (
    <section className="bg-[#f6f5f2] py-20">
      <TextHoverEffect
        text="PRODUKTE"
        className="font-['Unbounded'] font-black uppercase"
        strokeColor="#1c4b42"    // Deep Green Stroke
        fillColor="#1c4b42"       // Deep Green Fill
      />
    </section>
  );
}

// Fachbetrieb — Auf hellem Hintergrund
export function FachbetriebSectionTitle() {
  return (
    <section className="bg-white py-20">
      <TextHoverEffect
        text="FACHBETRIEB"
        className="font-['Unbounded'] font-black uppercase"
        strokeColor="#4daf46"    // Pure Green Stroke
        fillColor="#287d4b"       // Transition Green Fill
      />
    </section>
  );
}
```

## Typografie-Regeln

Der Text Hover Effect muss die Unbounded-Regeln aus DESIGN.md einhalten:

- **Font:** Unbounded
- **Weight:** 900 (font-black)
- **Case:** UPPERCASE
- **Mindestgröße:** 36px (headline-sm) — der Effekt funktioniert nicht gut bei kleinen Größen
- **Empfohlene Größe:** 56px–72px (headline-lg bis headline-display)

## Einschränkungen

- **Nur für Headlines** — Nie für Body-Text, Labels oder Buttons verwenden.
- **Maximal ein Text Hover Effect pro Seite** — Mehrere gleichzeitig erzeugen visuelles Chaos.
- **Nicht mit Aurora Background kombinieren** — Beide Effekte konkurrieren um Aufmerksamkeit.
- **Barrierefreiheit:** Der SVG-Text muss ein `aria-label` haben, da Screen Reader SVG-Text nicht immer korrekt lesen.
- **Performance:** SVG-Stroke-Animationen sind CPU-intensiv bei sehr langen Texten. Maximal 2 Wörter empfohlen.

## Wann einsetzen

- Hero-Bereich als Hauptüberschrift
- Sektions-Einstiege bei Scroll
- Feature-Highlights (einzelnes Wort wie "SCHUTZ", "QUALITÄT", "TROCKEN")

## Wann NICHT einsetzen

- Fließtext oder Absätze
- Navigation oder UI-Elemente
- Technische Datenblätter
- Zusammen mit anderen animierten Text-Effekten
