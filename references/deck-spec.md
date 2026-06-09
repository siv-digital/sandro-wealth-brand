# Sandro Wealth — Deck Spec

The format authority for **all PowerPoint / .pptx work**. Every Sandro deck is built by
**copying and populating the bundled template** — never rebuilt from scratch, and never
restyled to other brand tokens.

**Template asset:** `assets/templates/sandro-deck-template.pptx`

---

## Build rule (read first)

1. **Copy the template** to your working directory. Build into the copy.
2. **Populate the existing slide layouts** — duplicate the layout slide that matches the
   content, then fill it. Do not invent new layouts or restyle existing ones.
3. **Do not swap fonts.** The deck is built in **Georgia** (headings) and **Inter / DM Sans**
   (body) — these are the template-native fonts, Office-safe and installed on the Sandro
   team's machines. The Libre Baskerville / DM Sans pairing in SKILL.md is for **web and
   social only** and must NOT be forced into the deck. Leave the template's fonts intact.
4. **Keep the footer.** Every content slide carries the disclaimer line
   *"This presentation is for professional use only and is not intended for distribution"*
   (lower-left, small muted DM Sans) and a page number (lower-right). Preserve both.
5. **Use the `pptx` skill mechanics** (unpack → edit → repack, plus QA) to manipulate the
   file — but the *design* comes from this template, not from the `pptx` skill's generic
   "design ideas." Where they conflict, the template wins.
6. **Do not use the `frontend-design` skill for decks** — that's for HTML/web/social only.

---

## Format fundamentals

- **Aspect ratio:** 16:9. Slide size 13.333 in × 7.5 in (12192000 × 6858000 EMU).
- **Fonts:** Georgia (serif, headings/display) + Inter / DM Sans (sans, body/labels/data).
- **Grounds:** Titanium-blue dark grounds for title/divider/closing; Off-White light grounds
  for content. Light content panels use a pale blue-grey fill (not pure white).
- **Sunburst motif:** the rays emanate from bottom-center on dark slides. Already baked into
  the title and divider layouts — use those layouts rather than recreating the effect.

---

## Slide-type library (what's in the template)

Duplicate the slide that matches the content need.

| Template slide | Type | Use for |
|---|---|---|
| 1 | **Title** | Cover. Dark sunburst ground, ivory logo lockup left-of-center with vertical divider rule, title/subtitle to the right of the rule. |
| 2 | **Section divider (mid-tone)** | Section breaks. Titanium ground, thin accent rule, section title. |
| 3 | **Content — single column** | One block of prose or a single focal point. |
| 4 | **Content — header + body** | Headline with supporting paragraph. |
| 5 | **Content — full panel** | One large light content panel. |
| 6, 7 | **Content — two column** | Side-by-side blocks, comparisons. |
| 8, 9 | **Content — three column** | Three parallel points or steps. |
| 10, 11 | **Content + side panel / image** | Text with a contrasting titanium panel or image rail. |
| 12, 13 | **Section divider (dark sunburst)** | Heavier section breaks / part openers. |
| 14, 15, 16 | **Multi-block / gradient panels** | Grouped content blocks; the asset-class gradient panels. |
| 17 | **Stat callout — 3 numbered** | Three numbered points (circled numerals). |
| 18 | **Stat callout — 4 numbered** | Four numbered points. |
| 19, 20 | **Quad / 2×2** | Four-quadrant content. |
| 21 | **Light gradient ground** | Quiet transitional or quote slide. |
| 22, 23 | **Icon library (REFERENCE)** | Do not present. Source icons from here. |
| 24 | **Table / row layout (REFERENCE)** | Pattern for tabular rows. |
| 25 | **Asset-class color system (REFERENCE)** | Do not present. The data-viz palette — see below. |
| 26 | **Chart examples (REFERENCE)** | Do not present. Pie / bar / donut conventions. |

Slides 22–26 are **brand-direction reference**, not content slides. Delete them from any
finished client deck.

---

## Data-viz palette (asset classes)

When a chart shows asset allocation or financial data, color the series by asset class using
these ramps (from template slide 25). Each class has a 10-step tint ramp; use the darker
steps for primary series, lighter for secondary.

**Equity**
- Public Equity (blue-grey): `4F7893` `5E869F` `6D94AB` `7DA3B7` `8DB2C3` `9EC1CF` `B0D0DA` `C2DFE6` `D6EBF0` `E7F3F8`
- Private Equity (bright blue): `1781BF` `2E8FCA` `459DD4` `5DABDE` `76B9E7` `90C7EE` `AAD5F4` `C3E2F8` `DAEDFB` `EEF6FE`

**Fixed Income**
- Core Fixed Income (brown): `4A331E` `563E27` `624A30` `6F5739` `7C6542` `8A734C` `998257` `C9BCA3` `E2DACB` `F3EFE7`
- Opportunistic Income (gold): `9C6F2F` `A97B36` `B6873E` `C39446` `D0A14F` `DDAD58` `E9BA62` `E0C28E` `F0DEC1` `FAF2E4`
- Private Credit (tan): `C49A5A` `C79F62` `CAA46A` `D0AE7B` `D6888B` `D6888B` `DCC29C` `E7D7BD` `EDE1CD` `F3EBDE`

**Real Assets**
- Public (purple): `4F3B78` `5A4686` `655195` `715DA4` `7E6AB2` `8C78C0` `9A87CE` `C7C0EA` `DDD9F4` `F0EEFA`
- Private (mauve): `AE86A4` `B28CA9` `B692AD` `BA98B2` `BE9EB6` `C6AABF` `CEB6C8` `DFCFDB` `E7DAE4` `EFE7ED`

**Chart conventions (template slide 26):** restrained pies/donuts with class-coded segments;
bar charts with a single highlighted bar in the gradient and the rest in titanium/grey; data
labels in DM Sans; no 3-D effects, no heavy gridlines.

---

## Compliance on decks

Same do-not-generate list as SKILL.md applies. Where a slide makes a claim that would carry
disclosure, leave a `[DISCLOSURE: insert approved disclaimer]` placeholder. The footer
"professional use only / not for distribution" line is part of the template, not a substitute
for claim-level disclosure.

---

## QA

Run the `pptx` skill QA loop (extract-text for placeholder leftovers, then visual subagent
inspection). Render at 2× and confirm the Georgia headings and Inter/DM Sans body render true
— if they fall back to a generic serif/sans, the deck will look off-brand. Confirm slides
22–26 were removed from the final client deck.
