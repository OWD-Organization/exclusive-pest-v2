# DESIGN.md — Exclusive Pest Solutions

## Aesthetic lane
Neobrutalism on a dark desert-night ground. Named reference: Arizona highway signage at night
crossed with a pesticide label's stencilled compliance block. Hard 2.5px bone borders, flat
blocks, hard offset shadows in BRAND COLOR (not black, which is invisible on a dark ground),
zero radius, giant stencil numerals, a strict visible grid.

Deliberately NOT the Homemade By Colleen system in this same repo: that one is a light warm
cream ground with ink borders, ink shadows, rotated kitchen-label stickers and Bricolage
Grotesque. This one is dark, neutral-cool, colour-shadowed, numbered rather than rotated,
and uses a different type pairing. Same architecture, opposite expression.

## Color  (strategy: Drenched dark + gold carries the brand)
Derived from the official brand style guide PDF, not from the live site (the live site has
drifted: its charcoal #4b4f52 is 12 lightness points off the guide's #2E2E2E and carries a
blue cast the guide does not have).

Primitives (all oklch)
  --c-ink          oklch(15.5% 0.012 250)   #080d11   ground
  --c-ink-2        oklch(21.5% 0.014 250)   #151a20   raised block
  --c-ink-3        oklch(28.5% 0.014 250)   #252b31   hairline / third level
  --c-bone         oklch(96.5% 0.008 85)    #f6f3ed   primary text, borders
  --c-bone-dim     oklch(78.0% 0.012 85)    #bbb7af   secondary text
  --c-gold         oklch(77.5% 0.155 72.5)  #f1a328   from Owl Orange #F59E1B / Golden #F5A623
  --c-gold-deep    oklch(70.0% 0.155 62)    #e18518   from Dark Orange #D67F0F
  --c-cactus       oklch(65.5% 0.155 142)   #52a74a   from Cactus Green #4FA64F
  --c-cactus-deep  oklch(50.0% 0.120 145)   #2f7434   from Darker Green #2F7D32
  --c-sand         oklch(83.0% 0.135 82)    #f3be55   from Sand Yellow #F4B942

Measured contrast (all AA or better)
  bone on ink        17.65:1     gold on ink        9.35:1
  bone on ink-2      15.81:1     gold on ink-2      8.38:1
  bone on ink-3      12.95:1     cactus on ink      6.53:1
  bone-dim on ink     9.76:1     cactus on ink-2    5.85:1
  bone-dim on ink-2   8.74:1     sand on ink       11.45:1
  ink on gold         9.35:1     ink on sand       11.45:1
  ink on cactus       6.53:1     bone on cactus-deep 5.14:1

Hard rules: gold, sand and cactus blocks always take INK text, never bone.
bone on gold-deep is 2.51:1 and is forbidden.

## Typography (2 families)
Display: Archivo (variable, wdth 62-125, wght 400-900). Chosen for its signage and
utility-printing heritage and its squared terminals, which echo the logo's squarish
wordmark. Expanded widths for headings, condensed for the compliance register.
Body: Public Sans 400/500/700. Descends from the US Web Design System: the register of
a licensed, label-compliant, government-audited trade. Not Inter.

Semantic tracking tokens (architecture inherited from nicepest.com):
  --tr-display -0.025em | --tr-heading -0.012em | --tr-register 0.18em
  --tr-button 0.06em    | --tr-nav 0.02em       | --tr-numeral -0.045em
Scale: fluid clamp(), ratio >= 1.25. Body 62-72ch. Dark ground gets +0.06 line-height.

## Elevation
No blur, ever. Hard offset shadow via zero-blur box-shadow.
  --sh-x -6px --sh-y 6px           blocks, shadow in --c-gold or --c-cactus by role
  --btn-sh-x -5px --btn-sh-y 5px   collapses to -1/1 on press
Borders: --bd-hard 2.5px solid var(--c-bone). Hairlines 1.5px in --c-ink-3.
Radius: 0 everywhere. No exceptions on this brand.

## Components
--btn-*   primary (gold fill, ink text), secondary (bone border, transparent), tertiary (underline)
--reg-*   SECTION REGISTER: a numbered compliance plate (01 / ABOUT US) at each section's head.
          This is the named system that carries the source's section eyebrows. Numbered and
          squared, never rotated: it belongs to an inspection form, not a sticker sheet.
--stat-*  giant stencil numerals. Real values in the HTML, never JS-initialised at 0.
--cred-*  credential chips for the license and certification row

## Motion
ease-out-expo only. Transform and opacity only, never layout properties.
Staggered entrance via IntersectionObserver. Button lift on hover, shadow collapse on press.
Full prefers-reduced-motion block disables everything.
