# Sandro Wealth Brand — Claude Code Skill

A [Claude Code](https://claude.com/claude-code) Agent Skill that teaches Claude to produce **precisely on-brand** creative assets for **Sandro Wealth Management™** — colors, typography, logo usage, voice, and financial-services compliance guardrails applied automatically.

Once installed, Claude will use this skill whenever you ask it to design, draft, or build anything for Sandro Wealth: social graphics, slide decks, one-pagers, flyers, web pages, HTML emails, landing pages, or brochures.

## What's inside

```
sandro-wealth-brand/
├── SKILL.md                  ← the skill (brand fundamentals, voice, compliance rules)
├── references/
│   ├── brand-spec.md         ← full color/type/logo spec + firm positioning
│   ├── voice.md              ← voice guide with on-brand / off-brand copy examples
│   └── asset-playbook.md     ← per-asset-type layout norms, dimensions, dos & don'ts
├── scripts/
│   └── embed_fonts.py        ← emits a ready-to-paste @font-face <style> block (base64-embedded fonts)
└── assets/
    ├── fonts/                ← Libre Baskerville + DM Sans (the real .ttf files)
    └── logos/               ← official sunburst logo lockups & symbols (10 SVG variants)
```

The fonts and logos are bundled directly, so assets render correctly with **no network access** required.

## Installation

This skill installs as a personal (user-level) skill, available across all your Claude Code projects.

### Option A — Clone with git

```bash
# macOS / Linux
git clone https://github.com/siv-digital/sandro-wealth-brand.git \
  ~/.claude/skills/sandro-wealth-brand
```

```powershell
# Windows (PowerShell)
git clone https://github.com/siv-digital/sandro-wealth-brand.git `
  "$env:USERPROFILE\.claude\skills\sandro-wealth-brand"
```

### Option B — Download the ZIP

1. On the GitHub page, click **Code → Download ZIP**.
2. Unzip it.
3. Move the **inner** `sandro-wealth-brand` folder (the one containing `SKILL.md`) into your skills directory:
   - macOS / Linux: `~/.claude/skills/`
   - Windows: `%USERPROFILE%\.claude\skills\`

The final path must be `…/.claude/skills/sandro-wealth-brand/SKILL.md` — `SKILL.md` sits directly inside the `sandro-wealth-brand` folder, not nested another level down.

### Project-level install (optional)

To make the skill available only inside one project (and shareable with teammates via that repo), clone it into the project instead:

```bash
git clone https://github.com/siv-digital/sandro-wealth-brand.git \
  ./.claude/skills/sandro-wealth-brand
```

## Verify it's installed

1. Restart Claude Code (or start a new session).
2. Run `/skills` — you should see **sandro-wealth-brand** listed.
3. Try: *"Build a LinkedIn banner for Sandro Wealth announcing our advisor platform."* Claude should automatically apply the brand colors, fonts, and logo.

## Requirements

- **Claude Code** (CLI, desktop, or IDE extension).
- **Python 3** — only needed for `scripts/embed_fonts.py`, which uses the standard library only (no `pip install` required).

## Using the embedded fonts

When Claude builds any HTML/SVG asset, it should embed the brand fonts rather than linking to Google Fonts (a CDN link can silently fail and fall back to the wrong typeface). The bundled script does this for you:

```bash
python scripts/embed_fonts.py        # prints a <style> block to paste into <head>
python scripts/embed_fonts.py --css-only   # prints just the @font-face rules
```

## Compliance note

Sandro Wealth is an SEC-registered investment adviser. This skill is built to **avoid generating** non-compliant copy (performance guarantees, specific investment advice, unsubstantiated superlatives, testimonials, "risk-free" framing). It does **not** write or add disclaimers — formal compliance review remains with your compliance/legal team. Where a disclosure belongs, the skill leaves a `[DISCLOSURE: insert approved disclaimer]` placeholder for your team to fill in.

---

*Maintained by [SIV Digital](https://sivdigital.com). Brand assets © Sandro Wealth Management.*
