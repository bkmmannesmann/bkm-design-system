# Focus Cards

> Bild-Galerie bei der alle Karten außer der gehoverten abdunkeln. Erzeugt einen natürlichen Fokus-Effekt ohne zusätzliche UI-Elemente.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Focus Cards](https://ui.aceternity.com/components/focus-cards) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, Tailwind CSS |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Bild-Galerien, Referenz-Übersichten, Team-Seiten, Leistungsübersichten |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Card-Radius | `12px` (rounded.lg) | `12px` (rounded.lg) |
| Overlay (inaktiv) | `rgba(28, 75, 66, 0.6)` (Deep Green 60%) | `rgba(73, 73, 73, 0.6)` (Stone Grey 60%) |
| Text auf Overlay | `#ffffff` | `#ffffff` |
| Akzent-Label | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Sektions-Hintergrund | `#f6f5f2` (Sand White) | `#f6f5f2` (Sand White) |

## Installation

```bash
npx shadcn@latest add @aceternity/focus-cards
```

## BKM-angepasster Code

```tsx
import { FocusCards } from "@/components/ui/focus-cards";

interface BkmFocusItem {
  title: string;
  subtitle?: string;
  image: string;
}

interface BkmFocusCardsProps {
  items: BkmFocusItem[];
  context?: "ag" | "fachbetrieb";
}

export function BkmFocusCards({ items, context = "ag" }: BkmFocusCardsProps) {
  const overlayColor =
    context === "ag"
      ? "rgba(28, 75, 66, 0.6)"   // Deep Green 60%
      : "rgba(73, 73, 73, 0.6)";  // Stone Grey 60%

  const cards = items.map((item) => ({
    title: item.title,
    src: item.image,
  }));

  return (
    <section className="bg-[#f6f5f2] py-20">
      <FocusCards
        cards={cards}
        overlayColor={overlayColor}
        className="rounded-[12px]"
      />
    </section>
  );
}
```

## Einschränkungen

- **Mindestens 3 Karten** — Unter 3 wirkt der Fokus-Effekt nicht.
- **Bilder gleicher Proportion** — Alle Bilder sollten dasselbe Seitenverhältnis haben.
- **Overlay-Farbe kontextabhängig** — Deep Green für BKM AG, Stone Grey für Fachbetrieb.
- **Keine CSS `border`** — Shadow-as-border oder gar kein Rahmen (Bilder sind selbst-definierend).
