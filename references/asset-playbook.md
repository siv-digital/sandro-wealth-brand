# Sandro Wealth — Asset Playbook

Per-asset-type layout norms, dimensions, and dos/don'ts. Apply the brand fundamentals from SKILL.md on top of these.

## Universal layout principles

- **Generous negative space.** Affluence reads as restraint. Don't fill the canvas.
- **Anchor with Titanium Blue.** Most flagship assets are deep blue-black grounds with Ivory/Off-White content.
- **One focal element.** A headline, the symbol, or one image — not three competing things.
- **Logo placement.** Top-left or centered for headers; bottom corner as a sign-off. Always with clear space.
- **The sunburst symbol** can be used large and faint as a background watermark/texture — but it is optional and easy to get wrong. If used: (1) use the **symbol-only** variant, never the lockup; (2) crop tightly to the sunburst rays (viewBox roughly `89 129 230 135`) so no square panel edge shows; (3) keep opacity ≤4–5%; (4) bleed it off a corner. If a clean feathered edge can't be achieved, **omit the watermark** — a clean empty ground is more on-brand than a visible grey square. Negative space is the safer default for this brand.

## Social graphics

Deliver as standalone HTML or SVG artifacts at exact dimensions; embed the logo SVG inline.

| Format | Dimensions |
|---|---|
| LinkedIn / IG square | 1200 × 1200 |
| LinkedIn link/share | 1200 × 627 |
| LinkedIn banner (company) | 1128 × 191 |
| Story / vertical | 1080 × 1920 |

Dos:
- Titanium ground, Ivory headline in Libre Baskerville, small DM Sans support line, logo sign-off bottom corner.
- Use the gradient as a thin accent rule or a subtle corner wash — not the whole field.
- Keep copy to one idea. Quote cards (Baskerville Italic) work well for the brand.

Don'ts:
- No stock-photo collages, no busy patterns, no more than two type sizes per graphic.
- No CTA urgency. "Request a meeting" / "Learn more" only.
- If the graphic makes any claim, drop `[DISCLOSURE: ...]` placeholder in fine print.

## Slide decks

**Build from the bundled template — see `references/deck-spec.md`.** Decks are produced by
copying and populating `assets/templates/sandro-deck-template.pptx`, not built from scratch
and not styled with the web tokens. The template ships the title, divider, content (1–3
column, content+panel), stat-callout, and quad layouts, the asset-class data-viz palette, an
icon library, and the "professional use only / not for distribution" footer. The deck-spec is
the authority for fonts (Georgia + Inter/DM Sans, template-native), layout selection, and
chart color-coding. Do not use `frontend-design` for decks.

## One-pagers

HTML (print-friendly) or .docx via `docx` skill if you want Word. (For a single-slide PPTX one-pager, use the deck template — see `references/deck-spec.md`.)

- Header band in Titanium with logo lockup (ivory/offwhite variant).
- Body on Off-White: Baskerville H2s, DM Sans body, generous leading.
- Optional right rail or footer for the six advisory solutions as a clean list.
- Sign-off: symbol + contact, disclosure placeholder at the very bottom in small DM Sans.

## Web / HTML / landing pages / email

Working code. Fonts via Google Fonts. Brand tokens as CSS variables (see SKILL.md). Consult `frontend-design` for execution quality; brand tokens here override generic styling.

- **Hero:** Titanium ground or Titanium-with-gradient-wash, Baskerville headline, DM Sans subhead, one restrained CTA button (Ivory text on a subtle border or Off-White fill).
- **Sections:** alternate Off-White and Titanium grounds for rhythm.
- **Buttons:** rectangular or lightly rounded; no loud colors. Ivory/Off-White on Titanium, or outlined.
- **Motion:** subtle only — soft fade-ins, the sunburst rays animating in slowly on load at most. Nothing bouncy or playful.
- **Email:** table-based layout for client compatibility; inline styles; logo as a hosted PNG fallback if SVG unsupported. Keep to one column, Titanium header, Off-White body.

## Quick reference — what makes it feel like Sandro

- Deep blue-black + warm cream, never stark white.
- Serif headline (Baskerville) + clean sans body (DM Sans).
- Lots of room. One idea per surface.
- The sunburst as a quiet hero, sometimes a faint watermark.
- Measured copy. No hype. No urgency. No emoji.
