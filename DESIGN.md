# DESIGN.md — Exclusive Pest Solutions (v2, current)

v1 was a dark desert-night system. Rejected by the client: too dark, not as cheerful as
nicepest.com. Kept for reference in DESIGN-v1-night.md.

## Aesthetic lane
Cheerful neobrutalism in full desert daylight. Named reference: a 1960s Arizona roadside
attraction billboard crossed with a national-park trail sign. Heavy slab display type, flat
blocks of hot orange and cactus green on a peachy sand ground, hard offset shadows in warm
ink, softly rounded corners (10px, not zero), a layered dune horizon, and the great horned
owl used as an actual mascot rather than a logo lockup.

The brief is cheerful, so the mechanics are cheerful: rounded blocks instead of razor corners,
a sun, dunes, the owl, and the brand's own hot orange carrying most of the surface.

Deliberately NOT the two neighbouring systems in this repo:
- Homemade By Colleen: pale cream ground (chroma 0.014), chartreuse + school-bus yellow,
  BLUE-black ink, zero radius, rotated sticker labels, Bricolage Grotesque + Hanken Grotesk.
- Exclusive v1: dark ink ground, colour-cast shadows, numbered register plates, Archivo.
This one: peachy SAND ground (chroma 0.030), hot orange dominant, WARM BROWN-black ink,
10px radius, dune-and-sun scenery, Bevan slab + Figtree.

## Color  (strategy: Full palette, orange dominant)
Derived from the official brand style guide PDF. The live site's charcoal #4b4f52 is 12
lightness points off the guide's #2E2E2E and carries a blue cast the guide does not have,
so it is not used. Ink here is warmed further to brown-black, which reads desert and leather
rather than office.

Primitives (all oklch)
  --c-ink          oklch(24.5% 0.035 55)   #2d1c10   warm brown-black: text, borders, shadows
  --c-ink-soft     oklch(45.5% 0.038 55)   #685143   secondary text
  --c-sky          oklch(96.5% 0.030 78)   #fff2de   ground: peachy sand
  --c-sky-2        oklch(92.5% 0.048 72)   #fbe2c4   deeper sand band
  --c-paper        oklch(99.2% 0.012 80)   #fffcf4   raised blocks
  --c-orange       oklch(71.5% 0.178 52)   #f67c16   dominant accent (from Dark Orange #D67F0F)
  --c-orange-deep  oklch(57.5% 0.150 48)   #bd5711   large text on light, link hover
  --c-gold         oklch(84.5% 0.155 80)   #ffbf40   secondary accent (from Golden #F5A623)
  --c-gold-pale    oklch(95.5% 0.062 84)   #ffedc1   tint fill
  --c-cactus       oklch(71.5% 0.170 143)  #59bd56   tertiary (from Cactus Green #4FA64F)
  --c-cactus-deep  oklch(50.5% 0.130 146)  #267732   green text on light

Measured contrast (all AA unless noted)
  ink on sky        14.74:1     ink on orange        6.11:1
  ink on sky-2      13.04:1     ink on cactus        6.88:1
  ink on paper      15.91:1     ink-soft on sky      6.64:1
  ink on gold        9.97:1     ink-soft on paper    7.17:1
  ink on gold-pale  14.16:1     paper on cactus-deep 5.40:1
  paper on orange-deep 4.51:1   cactus-deep on sky   5.00:1
  orange-deep on sky 4.18:1  -> AA-large only, never body copy

Hard rules: orange, gold and cactus blocks always take INK text.
paper on orange is 2.61:1 and paper on cactus is 2.31:1. Both forbidden.

## Typography (2 families)
Display: Bevan, a heavy slab serif, for h1 and h2 only. Slab display is the Western roadside
register the brief asks for, and it is the loudest possible departure from the two grotesk
systems next door. Single weight, so hierarchy comes from size, not weight.
Everything else: Figtree 400/500/700/800/900. Friendly geometric humanist, carries h3/h4,
buttons, labels and body. Not Inter, not Hanken, not Public Sans.

Semantic tracking tokens (architecture inherited from nicepest.com):
  --tr-display -0.015em | --tr-heading -0.01em | --tr-label 0.14em
  --tr-button 0.04em    | --tr-nav 0.01em      | --tr-numeral -0.03em
Scale: fluid clamp(), ratio >= 1.25. Body 62-70ch.

## Elevation
No blur, ever. Hard offset shadow via zero-blur box-shadow, always in --c-ink.
  --sh-x -6px --sh-y 6px           blocks
  --btn-sh-x -5px --btn-sh-y 5px   collapses to -1/1 on press
Borders: --bd-hard 2.5px solid var(--c-ink). Hairlines 1.5px.
Radius: --r 10px on blocks, buttons and photos. --r-pill 999px on tags.
The radius is the cheerful signal and the deliberate break from Colleen's zero-radius system.

## Scenery
--dune-*  a layered SVG dune horizon at the foot of the hero and above the footer, in
          gold / orange / cactus, echoing the logo's own dunes.
--sun-*   a flat sun disc with straight rays behind the hero photo.
owl-mark.png, cropped from the brand logo, used as a mascot: it holds a scorpion in its
talons, which IS the wildlife-conscious argument. It appears at the owl paragraph and as
the process-section marker.

## Components
--btn-*   primary (orange fill, ink text), secondary (paper + ink border), tertiary (underline)
--tag-*   SECTION TAG: a pill in gold or cactus with a hard ink shadow. Rounded, not rotated,
          not numbered. This is the named system carrying the source's section eyebrows.
--stat-*  giant numerals in orange. Real values in the HTML, never JS-initialised at 0.
--cred-*  credential pills for the license and certifications

## Motion
ease-out-expo only. Transform and opacity only, never layout properties.
Staggered entrance via IntersectionObserver. Button lift on hover, shadow collapse on press.
Full prefers-reduced-motion block disables everything.
