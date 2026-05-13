# BKM Slides — Pattern-Katalog (Editorial)

> Übersicht welche Patterns in BKM-Slides erlaubt, eingeschränkt oder verboten sind. Basierend auf der Analyse echter BKM-Broschüren und PDFs. BKM-Slides folgen dem **Corporate Editorial**-Ansatz — nicht dem Web-Design-Ansatz.

## Erlaubte Patterns (Editorial)

| Pattern | Beschreibung | Einsatz |
|---------|-------------|---------|
| **Colored Border-Left Cards** | Weiße Cards mit 4px farbiger linker Borderlinie | Standard für alle Content-Cards |
| **Deep Green Footer-Bar** | Volle Breite, Lime Icon + Weiß Text | Auf Content-Slides |
| **Vertikale Lime-Linie** | 4px breit, ~60% Höhe, links vom Content | Titelseiten (BKM AG) |
| **Glasmorphismus** | Frosted-Glass-Effekt auf Foto-Hintergründen | Optional, max 1–2 pro Slide |
| **Split Layout (50/50)** | Text links, Foto rechts (oder umgekehrt) | Foto-Slides |
| **Große Statistik-Zahlen** | TT Norms Pro Bold, 48–96px, Akzentfarbe | Daten-Slides |
| **Checkmark-Listen** | Lime ✓ + TT Norms Pro Bold Titel | Zusammenfassungen |
| **Zentriertes Zitat** | Große Anführungszeichen + Zitat + Attribution | Testimonials |
| **Keyvisual-Überlappung** | Chevrons am rechten Rand über Fotos | Titelseiten |
| **Subtile Entrance-Animationen** | fadeInUp, scaleIn, slideIn (CSS-only) | Optional für Präsentationsmodus |

## Eingeschränkte Patterns

| Pattern | Einschränkung | Wann erlaubt |
|---------|--------------|--------------|
| **Colourful Text** (CSS Gradient) | Nur auf dunklen Hintergründen | Einzelne Akzent-Wörter in Headlines |
| **Transition Green Fläche** | Max 1–2 Slides pro Deck | Fachbetrieb-Akzent-Slides |
| **Foto-Overlay** | Nur mit Deep Green 55–70% Opacity | Emotionale Titel-Slides |

## Verbotene Patterns (Web-Design — NICHT für Slides)

Diese Patterns gehören zum **Web/Digital-Kontext** und dürfen NICHT in Slides, Broschüren oder Print-Materialien verwendet werden:

| Pattern | Warum verboten |
|---------|---------------|
| **Noise Texture** (SVG fractal noise) | Echte BKM-Slides haben saubere, flache Flächen |
| **Aurora Gradient** (animierte Farbverläufe) | Web-Dekoration, nicht Corporate Editorial |
| **Bento Grid** (gleichförmige Kacheln) | Dashboard-Ästhetik, nicht Magazin-Ästhetik |
| **Floating Badges** (absolut positioniert) | Web-UI-Pattern, nicht Print |
| **Spotlight/Glow Effects** | Cursor-basiert, nicht für statische Medien |
| **3D Card Effect** | Braucht JS, zu verspielt für Corporate |
| **Animated Text Effects** | Zu verspielt, lenkt von Inhalt ab |
| **Wavy Background** | Verletzt die "harte Schnitte"-Regel |
| **Shadow-as-Border auf Cards** | Nur für Website — Slides nutzen Border-Left |
| **Multiple competing shadows** | Zu komplex, verwässert visuelle Hierarchie |

## Glasmorphismus — Implementierung für Slides

Glasmorphismus ist das EINZIGE dekorative Web-Pattern, das in BKM-Slides erlaubt ist. Es funktioniert besonders gut auf Foto-Hintergründen.

```css
/* Standard Glass Card */
.glass {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 12px;
  padding: 40px;
}

/* Dunklere Variante (auf hellen Fotos) */
.glass--dark {
  background: rgba(28, 75, 66, 0.7);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 40px;
}
```

**Regeln für Glasmorphismus:**
- Nur auf Foto-Hintergründen verwenden (nie auf flachen Farbflächen)
- Maximum 1–2 Glass-Elemente pro Slide
- Nie für kleine Text-Elemente (Lesbarkeit!)
- Immer mit ausreichend Kontrast für Text (WCAG AA)
- Foto muss mit dunklem Overlay (50–70%) abgedunkelt werden

## Zusammenfassung: Die BKM-Slide-Ästhetik

```
ERLAUBT:                          VERBOTEN:
─────────────────────────────     ─────────────────────────────
✓ Saubere flache Flächen         ✗ Noise-Texturen
✓ Große Fotos (40%+ Fläche)      ✗ Aurora-Gradients
✓ Großzügiger Weißraum (25%+)    ✗ Bento-Grids
✓ Cards mit Border-Left           ✗ Floating Badges
✓ Deep Green Footer-Bar           ✗ Spotlight/Glow
✓ Vertikale Lime-Linie            ✗ Animierte Hintergründe
✓ Glasmorphismus (auf Fotos)      ✗ Dashboard-Grids
✓ Asymmetrische Layouts           ✗ Box-Shadows auf Cards
✓ Keyvisual-Überlappung           ✗ Wavy Backgrounds
```
