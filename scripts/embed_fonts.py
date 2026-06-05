#!/usr/bin/env python3
"""
Emit a ready-to-paste <style> block with the Sandro Wealth brand fonts embedded
as base64 @font-face rules. Use this whenever building an HTML/SVG asset so the
fonts render correctly WITHOUT any network access to Google Fonts (which is not
reachable in this environment).

Usage:
    python scripts/embed_fonts.py            # prints the <style> block to stdout
    python scripts/embed_fonts.py --css-only # prints just the @font-face rules

Then paste the output into the <head> of the asset. Reference the families as:
    font-family: 'Libre Baskerville', serif;   /* weight 400 or 700; italic supported */
    font-family: 'DM Sans', sans-serif;        /* weight 400-600 */
"""
import base64, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "assets", "fonts")

FACES = [
    ("Libre Baskerville", "normal", "400 700", "LibreBaskerville.ttf"),
    ("Libre Baskerville", "italic", "400 700", "LibreBaskerville-Italic.ttf"),
    ("DM Sans",           "normal", "400 600", "DMSans.ttf"),
]

def b64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def build_css():
    out = []
    for family, style, weight, fn in FACES:
        data = b64(os.path.join(FONTS, fn))
        out.append(
            f"@font-face{{font-family:'{family}';font-style:{style};"
            f"font-weight:{weight};font-display:swap;"
            f"src:url(data:font/ttf;base64,{data}) format('truetype');}}"
        )
    return "\n".join(out)

if __name__ == "__main__":
    css = build_css()
    if "--css-only" in sys.argv:
        print(css)
    else:
        print("<style>\n" + css + "\n</style>")
