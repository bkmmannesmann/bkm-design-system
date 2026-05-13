# Colourful Text

> Animierter Farbverlauf-Text, bei dem die Farben durch die Buchstaben fließen. Erzeugt einen lebendigen, dynamischen Effekt für Akzent-Headlines.

## Metadaten

| Eigenschaft | Wert |
|-------------|------|
| **Quelle** | [Aceternity UI — Colourful Text](https://ui.aceternity.com/components/colourful-text) |
| **Lizenz** | MIT |
| **Tech** | React, CSS Gradient Animation |
| **Kontext** | **BKM AG only** |
| **Einsatz** | Einzelne Akzent-Wörter in Headlines, Feature-Highlights |

## BKM-Farbmapping

Der Farbverlauf nutzt die BKM-Grüntöne und Lime — die "Story of Green" (Feuchtigkeit → Trocknung → Schutz):

| Gradient-Stop | Farbe | Bedeutung |
|---------------|-------|-----------|
| 0% | `#1c4b42` (Deep Green) | Feuchtigkeit / Problem |
| 33% | `#287d4b` (Transition Green) | Trocknung / Prozess |
| 66% | `#4daf46` (Pure Green) | Trocken / Lösung |
| 100% | `#b4e717` (Lime) | Schutz / Ergebnis |

## BKM-angepasster Code

```tsx
import { ColourfulText } from "@/components/ui/colourful-text";

// Einzelnes Akzent-Wort in einer Headline
export function BkmFeatureHeadline() {
  return (
    <h2 className="font-['Unbounded'] text-3xl md:text-5xl font-black uppercase text-[#1a1a1a] tracking-tight">
      MAXIMALER{" "}
      <ColourfulText
        text="SCHUTZ"
        colors={["#1c4b42", "#287d4b", "#4daf46", "#b4e717"]}
        className="font-['Unbounded'] font-black uppercase"
      />
    </h2>
  );
}
```

## Einschränkungen

- **NUR im BKM AG Kontext** — Lime Green ist im Fachbetrieb verboten.
- **Nur für einzelne Wörter** — Maximal 1–2 Wörter pro Headline. Nie für ganze Sätze.
- **Nur auf hellen Hintergründen** — Der Gradient braucht Kontrast zu Weiß/Sand White.
- **Unbounded-Regeln gelten** — 900, uppercase, min. 36px.
- **Maximal einmal pro Seite** — Mehrere Colourful Texts wirken überladen.
