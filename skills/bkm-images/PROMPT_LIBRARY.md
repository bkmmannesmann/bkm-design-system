# BKM Image Prompt Library

> Brand-konforme Prompt-Bausteine für `gpt-image-1` (OpenAI Images). Das Skript
> `generate.mjs` setzt den finalen Prompt zusammen aus:
>
> **`[BASE STYLE]` + `[CONTEXT]` + `[USE CASE]` + `[MOTIV vom Nutzer]` + `[NEGATIVE]`**
>
> Diese Datei ist die Quelle dieser Bausteine — sie wird vom Skript inline
> gespiegelt, kann aber auch manuell in der ChatGPT-/DALL·E-Oberfläche genutzt
> werden. Bei Änderungen hier **auch `generate.mjs` anpassen** (Konstanten am
> Dateianfang).

---

## 1. BASE STYLE (immer)

```
Editorial documentary photograph in the BKM Mannesmann visual language.
Shot on a medium format camera, dramatic natural lighting, high contrast,
shallow depth of field, muted earth-tone color grade, realistic materials and
textures (concrete, masonry, mineral surfaces, water, greenery). Authentic and
emotional, never generic stock photography. Generous negative space for a later
text overlay. Photorealistic.
```

## 2. CONTEXT

### BKM AG (`ag`) — dark, corporate

```
Mood: deep, protective, authoritative. Dominant deep teal-green tonality
(#1c4b42) in shadows and atmosphere, cool muted palette, dramatic low-key
lighting. A single subtle lime-green highlight accent (#b4e717) as a light edge
or one small material detail — used sparingly, never covering large areas.
```

### Fachbetrieb (`fachbetrieb`) — light, on-site

```
Mood: clean, trustworthy, hands-on. Bright warm daylight, sand-white ambience
(#f6f5f2), airy and documentary. Fresh pure-green accents (#4daf46) from
vegetation, signage edges or treated surfaces. Absolutely no lime-green.
```

## 3. USE CASE

### Slide background (`slide`)

```
Composition for a 16:9 presentation background. Keep the right third and the
upper area calm and uncluttered for a glassmorphism card and a chevron keyvisual
overlay. Cinematic wide framing.
```

### Website / Hero (`website`)

```
Wide hero composition for a website header. Strong focal subject on the left,
clean negative space on the right for headline text. Cinematic, premium,
landscape framing.
```

### Social feed (`social`, ratio square)

```
Square social-media composition. Centered, bold focal subject with breathing
room around it (10% safe margin on every side). Scroll-stopping but editorial.
```

### Social story (`social --ratio story`)

```
Vertical 9:16 story composition. Strong subject in the central safe zone,
calm space at the top and bottom thirds for overlaid text and a logo.
```

### Product / Architecture (`product`)

```
Product-and-architecture hero. Clean, deliberate staging of the material,
detail or building element as the hero. Studio-grade natural light, precise
focus on texture and surface. Premium, technical, trustworthy.
```

## 4. MOTIV (vom Nutzer, `--motif`)

Konkretes Motiv aus einem der erlaubten Felder. Beispiele:

| Feld | Beispiel-Motiv (englisch, für die API) |
|------|----------------------------------------|
| Architektur | `concrete basement wall with a visible horizontal moisture barrier line` |
| Architektur | `weathered brick masonry facade with rising damp pattern` |
| Bau / Sanierung | `renovation construction site, scaffolding against a restored facade` |
| Bau / Sanierung | `injection drilling pattern in a brick wall, close documentary view` |
| Labor / Technik | `laboratory bench with mineral material samples under examination` |
| Labor / Technik | `macro of a water droplet beading on a treated mineral surface` |
| Nachhaltigkeit | `modern sustainable building with greenery integrated into the facade` |
| Business | `two professionals reviewing building plans on a tablet on a job site` |

> Motive immer **auf Englisch** an die API geben (bessere Ergebnisse).

## 5. NEGATIVE (immer angehängt)

```
No text, no words, no letters, no numbers, no captions, no logos, no brand
marks, no watermarks, no signatures, no UI elements or browser chrome.
No aurora gradients, no neon, no noise overlay, no 3D render look, no cartoon
or illustration style, no oversaturated HDR. Not a flat graphic — a real
photograph.
```

---

## Vollständiges Beispiel (zusammengesetzt)

**Befehl:**
```bash
node generate.mjs --usecase slide --context ag \
  --motif "concrete basement wall with a visible horizontal moisture barrier line"
```

**Resultierender Prompt:**
> Editorial documentary photograph in the BKM Mannesmann visual language. Shot on
> a medium format camera, dramatic natural lighting, high contrast, shallow depth
> of field, muted earth-tone color grade, realistic materials and textures
> (concrete, masonry, mineral surfaces, water, greenery). Authentic and emotional,
> never generic stock photography. Generous negative space for a later text
> overlay. Photorealistic. Mood: deep, protective, authoritative. Dominant deep
> teal-green tonality (#1c4b42) in shadows and atmosphere, cool muted palette,
> dramatic low-key lighting. A single subtle lime-green highlight accent (#b4e717)
> as a light edge or one small material detail — used sparingly, never covering
> large areas. Composition for a 16:9 presentation background. Keep the right
> third and the upper area calm and uncluttered for a glassmorphism card and a
> chevron keyvisual overlay. Cinematic wide framing. Subject: concrete basement
> wall with a visible horizontal moisture barrier line. No text, no words, no
> letters, no numbers, no captions, no logos, no brand marks, no watermarks, no
> signatures, no UI elements or browser chrome. No aurora gradients, no neon, no
> noise overlay, no 3D render look, no cartoon or illustration style, no
> oversaturated HDR. Not a flat graphic — a real photograph.
