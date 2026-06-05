# Sandro Wealth — Full Brand Spec

Lookup reference. The SKILL.md body carries the operative rules; this file is the complete spec for when precise values or context are needed.

## Firm positioning (context for messaging)

Sandro Wealth Management™ is an SEC-registered, privately-owned investment adviser. It is a **platform and partner for elite financial advisors**, giving them the expertise, technology, and investment access to win and serve high-net-worth clients ($5M+).

- **Audience:** elite advisors (primary), and the HNW clients those advisors serve (secondary).
- **Core promise:** advisors get a proven team + full-spectrum platform so they can serve discerning clients with the scope of a leading wealth firm — under their own advisory relationship.
- **Six advisory solutions:** investment management, private market investments, estate planning, business succession planning, asset protection & risk management, banking as a service.
- **Values:** independence (privately owned, no conflicts), fiduciary standard, ethics, diligence, clarity, conviction.
- **Trademark:** "Sandro Wealth Management™" — use the ™ on first/formal reference where appropriate.

## Color (complete)

| Name | Hex | RGB | Use |
|---|---|---|---|
| Titanium Blue | `#232B36` | 35, 43, 54 | Primary. Dark bg, primary text on light. |
| Grey | `#474747` | 71, 71, 71 | Secondary surface. |
| Ivory | `#FFFCEC` | 255, 252, 236 | Warm light field; logo ink on dark. |
| Off-White | `#FFFEF6` | 255, 254, 246 | Lightest background. |
| Gradient start | `#232B36` | — | Titanium end of accent gradient. |
| Gradient end | `#0BA0BD` | 11, 160, 189 | Cyan end. Accent only. |

- Signature pairing: Titanium Blue + Ivory/Off-White.
- Cyan (`#0BA0BD`) only appears inside the gradient as an accent — not as a standalone fill behind text.
- Avoid pure `#FFFFFF` and pure `#000000`; the brand's neutrals are warm.

## Typography (complete)

**Libre Baskerville** — serif, display.
- Bold: H1, H2, hero statements.
- Regular: large supporting display, subheads.
- Italic: pull quotes, attributions, editorial emphasis.
- Do not use below ~16px or for long paragraphs.

**DM Sans** — sans, functional.
- Regular/Medium: body, UI, buttons, captions, labels, legal/fine print, data.

Hierarchy pattern (from brand sheet):
- H1/H2 → Libre Baskerville Bold
- Lead paragraph → DM Sans Regular, slightly larger
- Body → DM Sans Regular
- Fine print / disclosures → DM Sans Regular, small
- Pull quote → Libre Baskerville Italic with a thin left rule

Font embedding (required — Google Fonts CDN is unreachable in this environment):
```bash
python scripts/embed_fonts.py   # emits a <style> block with base64 @font-face rules
```
Real font files live in `assets/fonts/`: `LibreBaskerville.ttf` (variable, wght 400–700), `LibreBaskerville-Italic.ttf`, `DMSans.ttf` (variable). Both are SIL Open Font License. Never rely on a `<link>` to fonts.googleapis.com — it fails silently and renders a system fallback.

## Logo asset index

All in `assets/logos/`. Source art was sliced from the official brand-sheet frames into per-background variants.

Full lockup (symbol + wordmark):
- `logo-lockup-titanium.svg` — Titanium Blue panel
- `logo-lockup-offwhite.svg` — Off-White panel
- `logo-lockup-grey.svg` — Grey panel
- `logo-lockup-ivory-transparent.svg` — ivory ink, transparent (dark photos/custom)
- `logo-lockup-dark-transparent.svg` — dark ink, transparent (light photos/custom)

Symbol only (sunburst square):
- `symbol-titanium.svg`, `symbol-offwhite.svg`, `symbol-grey.svg`
- `symbol-ivory-transparent.svg`, `symbol-dark-transparent.svg`

Each SVG is 448×344 (the panel ratio). For square needs (avatars/favicons), crop the symbol-only variant to its square sunburst region or place it centered on a square brand-color field.

Logo integrity rules: no stretch, recolor, rotate, drop-shadow, glow, or outline. Maintain clear space ≥ symbol height. Ensure contrast on any background.
