---
name: sandro-wealth-brand
description: Create on-brand creative assets for Sandro Wealth — an SEC-registered wealth management firm serving elite advisors and their $5M+ high-net-worth clients. Use this skill whenever you're asked to design, create, draft, build, or mock up ANY visual or written asset for Sandro Wealth (also called Sandro or SandroWealth) — social graphics (LinkedIn posts, banners, ads), slide decks and presentations, one-pagers, flyers, web pages, HTML emails, landing pages, brochures, or any branded collateral. Trigger this skill even when the request doesn't say "brand" — if the deliverable is for Sandro Wealth and is something a person will see, use this skill so colors, typography, logo usage, voice, and compliance guardrails are applied correctly. This skill is specific to Sandro Wealth Management — do not apply it to other brands.
---

# Sandro Wealth Brand

This skill produces creative assets that are precisely on-brand for **Sandro Wealth Management™**, an SEC-registered RIA. Every asset must look institutional, restrained, and trustworthy — and must respect financial-services compliance guardrails.

The brand exists in a regulated category. Getting the *look* right is half the job; not generating non-compliant copy is the other half. Both matter on every asset.

## How to use this skill

1. **Identify the asset type and surface.** Social graphic, deck, one-pager, web/HTML, email. Each has layout norms — see `references/asset-playbook.md`.
2. **Load the brand fundamentals below** (colors, type, logo rules) — these are non-negotiable and apply to every asset.
3. **Pull the correct logo file** from `assets/logos/` based on the background (see Logo usage).
4. **Check the copy against the compliance guardrails** before finalizing. This is a do-not-generate list, not a disclaimer step — your compliance/legal team handles formal compliance review.
5. **Build the asset.** For web/HTML and decks, also consult the `frontend-design` skill for execution quality, but the brand tokens here override any generic styling guidance.

## Brand fundamentals (apply to every asset)

### Color palette

| Token | Hex | Role |
|---|---|---|
| Titanium Blue | `#232B36` | Primary brand color. Dark backgrounds, primary text on light, the anchor of the identity. |
| Grey | `#474747` | Secondary background, muted UI surfaces. |
| Ivory | `#FFFCEC` | Primary light/cream. Logo ink on dark; warm background fields. |
| Off-White | `#FFFEF6` | Lightest background. Cleanest light surface. |
| Gradient | `#232B36 → #0BA0BD` | Titanium-to-cyan. Use sparingly for accent bars, data viz, hero washes — never behind body text. |

**Rules:**
- Default pairing is **Titanium Blue + Ivory/Off-White**. This is the brand's signature: deep blue-black with a warm cream, not stark white.
- Use Off-White (`#FFFEF6`) for light backgrounds, not pure `#FFFFFF`. Pure white reads cheap against this palette.
- The cyan gradient is an *accent*, used in small doses. Sandro is conservative — never let the gradient dominate.
- Grey is for secondary surfaces only, never the primary background of a flagship asset.

### Typography

| Family | Weights | Role | Source |
|---|---|---|---|
| **Libre Baskerville** | Bold, Regular, Italic | Display, headlines, the "SandroWealth" feel. Serif elegance. | Google Fonts (free) |
| **DM Sans** | Regular | Body copy, UI, captions, labels, fine print. | Google Fonts (free) |

**Rules:**
- Headlines and big statements → **Libre Baskerville**. It carries the institutional, old-money gravitas.
- Everything functional (paragraphs, buttons, captions, data) → **DM Sans**. Clean, neutral, legible.
- Never set body copy in Baskerville at small sizes — it gets fussy. Baskerville for impact, DM Sans for reading.
- **CRITICAL — embed fonts, never rely on the Google Fonts CDN.** `fonts.googleapis.com` is NOT reachable from this environment. A `<link>` to Google Fonts will silently fail and the asset will render in a system fallback serif/sans that looks subtly wrong (the #1 cause of "the fonts look off"). Instead, always embed the bundled font files as base64 `@font-face`. The real font files are in `assets/fonts/` (Libre Baskerville variable wght, Libre Baskerville Italic, DM Sans variable). Generate the ready-to-paste `<style>` block by running:
  ```bash
  python scripts/embed_fonts.py
  ```
  Paste its output into the `<head>` before any other styles. Then reference `font-family:'Libre Baskerville',serif` (weight 400 or 700, italic supported) and `font-family:'DM Sans',sans-serif` (weight 400–600).
- **Always verify fonts actually loaded** before trusting a render. After rasterizing, check `document.fonts` is non-empty and shows `-> loaded`. If it's empty, the fonts didn't embed and the output is fallback — fix before delivering.
- Give fonts a moment to apply before rasterizing (wait ~1.5–2s after navigation).
- Type hierarchy reference: Baskerville Bold for H1/H2, Baskerville Regular or Italic for pull quotes, DM Sans for H3 down through body and captions.

### Logo usage

Real vector logo files are bundled in `assets/logos/`. **Always use the bundled SVGs — never recreate the sunburst symbol from scratch.** Pick the variant that matches the background:

**Full lockup** (sunburst symbol + "SandroWealth" wordmark) — the default. Use when there's room.
- `logo-lockup-titanium.svg` — on Titanium Blue background
- `logo-lockup-offwhite.svg` — on Off-White / light background
- `logo-lockup-grey.svg` — on Grey background
- `logo-lockup-ivory-transparent.svg` — ivory ink, no panel — for placing on dark photos / custom dark backgrounds
- `logo-lockup-dark-transparent.svg` — dark ink, no panel — for placing on light photos / custom light backgrounds

**Symbol only** (sunburst square, no wordmark) — for favicons, avatars, tight spaces, or as a decorative brand mark when the wordmark already appears elsewhere.
- `symbol-titanium.svg`, `symbol-offwhite.svg`, `symbol-grey.svg`
- `symbol-ivory-transparent.svg`, `symbol-dark-transparent.svg`

**Rules:**
- Give the logo room. Clear space around it ≥ the height of the sunburst symbol. Never crowd it.
- **Size the logo for visibility.** On a 1200px-wide social canvas the lockup should be ~300–360px wide minimum — the ivory sunburst rays are thin and disappear if the logo is too small. Place it as a clear header (top-left or top-center), not a tiny afterthought.
- **Align everything to one grid.** Logo, kicker, headline, accent rule, and attribution should share the same left edge (or all be centered). Mixing a left-floated logo with centered content reads as a layout error.
- Never stretch, recolor, rotate, add effects (shadows, glows, outlines), or place on a busy/low-contrast background.
- On photography, use a transparent-ink variant and ensure the background area behind the mark is dark or light enough for contrast — add a subtle scrim if needed.
- Prefer the full lockup. Use symbol-only only when the wordmark is redundant or space is genuinely tight.

### Voice & tone

Sandro speaks to **elite financial advisors and high-net-worth individuals ($5M+)**. The register is:

- **Institutional and assured** — "clarity, conviction." Confident without selling hard.
- **Fiduciary and restrained** — independence, trust, care, ethics, diligence. Quiet authority, not hype.
- **Spare** — short, declarative sentences. Minimal adjectives. No exclamation points. No emoji.
- **Partnership-framed** — Sandro empowers advisors *to serve their clients*; it is a platform and partner, not a retail brand.

Avoid: startup energy, casual slang, urgency tactics ("act now"), growth-hacky CTAs, hype words ("revolutionary," "game-changing"), emoji.
Favor: measured nouns and verbs, specifics over superlatives, white space in copy as in layout.

See `references/voice.md` for on-brand vs. off-brand copy examples.

## Compliance guardrails (do NOT generate)

Sandro Wealth is an SEC-registered investment adviser. **This skill does not add disclaimers — your compliance/legal team handles formal compliance review.** But never *generate* copy that creates compliance exposure. Do not write:

- **Performance promises or guarantees** — no "guaranteed returns," "we'll grow your wealth," "you will earn," projected/implied return figures, or anything that promises an outcome.
- **Specific investment advice or recommendations** — no "you should buy/sell," no recommending specific securities, allocations, or products as advice.
- **Superlative or unsubstantiated claims** — "best," "#1," "top-performing," "safest" — unless given verbatim, substantiated, approved source text.
- **Testimonials or client endorsements** — RIAs face strict rules here; don't invent client quotes or success stories.
- **"Risk-free," "safe," "no downside"** framing — investments carry risk; never imply otherwise.
- **Comparisons that disparage named competitors** or claim superiority without basis.

If a request would require any of the above, **build the asset but flag the specific line for compliance review** ("This headline implies a performance guarantee — you'll want compliance to review or reword"). Don't silently comply, and don't refuse the whole task — flag the narrow issue and proceed with the rest.

When an asset would normally carry a disclosure (ads, anything making a claim), leave a clearly marked placeholder — `[DISCLOSURE: insert approved disclaimer]` — rather than writing one, so your compliance team can drop in approved language.

## Output conventions

- **Render at 2× resolution.** When rasterizing any HTML/SVG asset to PNG (e.g., via Playwright screenshot), always set `device_scale_factor=2` (or width 2× the target and downscale). Rendering at 1× produces grainy, soft type that looks low-quality and off-brand. This is the single most common quality failure — do not skip it.
- **Social graphics**: deliver as standalone HTML/SVG artifacts at the right dimensions (LinkedIn post 1200×1200 or 1200×627; story 1080×1920). Embed the logo SVG inline.
- **Decks / one-pagers**: use the `pptx` skill for .pptx, or HTML for a one-pager. Apply the palette and type tokens above.
- **Web / HTML / email**: working code, fonts via Google Fonts, brand tokens as CSS variables. Consult `frontend-design` for polish; brand tokens here win on any conflict.
- Set up brand tokens as variables at the top of any build:
  ```css
  :root {
    --titanium: #232B36;
    --grey: #474747;
    --ivory: #FFFCEC;
    --offwhite: #FFFEF6;
    --gradient: linear-gradient(90deg, #232B36, #0BA0BD);
  }
  ```

## Reference files

- `references/asset-playbook.md` — per-asset-type layout norms, dimensions, and dos/don'ts (social, deck, one-pager, web, email).
- `references/voice.md` — expanded voice guide with on-brand / off-brand copy examples.
- `references/brand-spec.md` — full color/type/logo spec for lookup, plus the firm positioning summary.
