# Animated Testimonials

> Testimonial-Karussell mit sanften Übergangsanimationen zwischen Kundenstimmen. Zeigt Zitat, Name, Rolle und optionales Bild.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Animated Testimonials](https://ui.aceternity.com/components/animated-testimonials) |
| **Lizenz** | MIT |
| **Tech** | React, Framer Motion, Tailwind CSS |
| **Kontext** | Beide (BKM AG + Fachbetrieb) |
| **Einsatz** | Kundenstimmen, Partner-Zitate, Fachbetrieb-Referenzen |

## BKM-Farbmapping

| Parameter | BKM AG | Fachbetrieb |
|-----------|--------|-------------|
| Sektions-Hintergrund | `#1c4b42` (Deep Green) | `#f6f5f2` (Sand White) |
| Zitat-Text | `#ffffff` | `#1a1a1a` |
| Name | `#ffffff` | `#1a1a1a` |
| Rolle/Firma | `#b4e717` (Lime) | `#4daf46` (Pure Green) auf dunklem Hintergrund, `#287d4b` (Transition Green) auf hellem |
| Anführungszeichen-Icon | `#b4e717` (Lime, 20% Opazität) | `#4daf46` (Pure Green, 20% Opazität) |
| Navigation-Dots aktiv | `#b4e717` (Lime) | `#4daf46` (Pure Green) |
| Navigation-Dots inaktiv | `rgba(255,255,255,0.3)` | `#c8c5be` (Outline) |

## BKM-angepasster Code

```tsx
import { AnimatedTestimonials } from "@/components/ui/animated-testimonials";

interface BkmTestimonial {
  quote: string;
  name: string;
  role: string;
  company?: string;
  image?: string;
}

interface BkmTestimonialsProps {
  testimonials: BkmTestimonial[];
  context?: "ag" | "fachbetrieb";
}

export function BkmTestimonials({
  testimonials,
  context = "ag",
}: BkmTestimonialsProps) {
  const isAg = context === "ag";

  return (
    <section className={isAg ? "bg-[#1c4b42] py-20" : "bg-[#f6f5f2] py-20"}>
      <div className="max-w-[1280px] mx-auto px-8 md:px-16">
        <h2
          className={`font-['Unbounded'] text-3xl font-black uppercase tracking-tight mb-12 ${
            isAg ? "text-white" : "text-[#1a1a1a]"
          }`}
        >
          {isAg ? "WAS UNSERE PARTNER SAGEN" : "KUNDENSTIMMEN"}
        </h2>
        <AnimatedTestimonials
          testimonials={testimonials.map((t) => ({
            quote: t.quote,
            name: t.name,
            designation: `${t.role}${t.company ? ` — ${t.company}` : ""}`,
            src: t.image || "",
          }))}
          autoplay
        />
      </div>
    </section>
  );
}
```

## Anwendungsbeispiel

```tsx
const kundenstimmen: BkmTestimonial[] = [
  {
    quote: "Die Horizontalsperre hat unser Feuchtigkeitsproblem nach 30 Jahren endlich gelöst. Professionelle Arbeit vom ersten Beratungsgespräch bis zur Abnahme.",
    name: "Thomas Müller",
    role: "Hausbesitzer",
    company: "Düsseldorf",
  },
  {
    quote: "Als zertifizierter BKM Fachbetrieb können wir unseren Kunden eine Lösung bieten, die wirklich funktioniert. Die MicroPorex® Technologie überzeugt.",
    name: "Stefan Weber",
    role: "Geschäftsführer",
    company: "Weber Bautenschutz GmbH",
  },
];

<BkmTestimonials testimonials={kundenstimmen} context="fachbetrieb" />
```

## Einschränkungen

- **Zitate in Inter** — Nicht in Unbounded. Zitate sind Fließtext, keine Headlines.
- **Name in Inter 600** — Hervorgehoben, aber nicht in Unbounded.
- **Rolle/Firma als Akzent** — Lime (BKM AG) oder Transition Green (Fachbetrieb auf hell).
- **Autoplay: 5–8 Sekunden** — Genug Zeit zum Lesen.
- **Mindestens 3 Testimonials** — Unter 3 wirkt es dünn.
- **Echte Zitate** — Keine erfundenen Testimonials. Lieber weniger, aber authentisch.
