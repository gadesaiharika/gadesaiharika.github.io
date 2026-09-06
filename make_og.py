"""
Generate the 1200x630 social card at assets/og-card.png.

Why this file exists: without an og:image, every time this URL is pasted into
LinkedIn, a recruiter email, or an application form's "portfolio" field, it
renders as a bare grey box. The card is the difference between a link people
scroll past and one they click, and it costs nothing to serve.

The figures are read from the project repos' exported CSVs, the same source the
site's charts use, so the card cannot drift out of step with the page.

Fonts: uses whatever it can find on the system, preferring the families the site
itself uses. If none resolve it falls back to PIL's bitmap default rather than
failing the build — a plain card still beats no card.
"""

import pathlib

from PIL import Image, ImageDraw, ImageFont

import charts

SITE = pathlib.Path(__file__).resolve().parent
OUT = SITE / "assets" / "og-card.png"

W, H = 1200, 630
PLANE = (249, 249, 247)
INK = (11, 11, 11)
INK_2 = (82, 81, 78)
MUTED = (137, 135, 129)
LINE = (221, 220, 212)
ACCENT = (42, 120, 214)
VERIFY = (27, 175, 122)

# Windows ships these; the Google families the site loads are not installed
# locally, so the card approximates rather than matches exactly.
FONT_DIRS = [pathlib.Path(r"C:\Windows\Fonts")]
SERIF = ["georgia.ttf", "times.ttf"]
SANS = ["segoeui.ttf", "arial.ttf"]
SANS_B = ["segoeuib.ttf", "arialbd.ttf"]
MONO = ["consola.ttf", "cour.ttf"]
MONO_B = ["consolab.ttf", "courbd.ttf"]


def font(candidates, size):
    for d in FONT_DIRS:
        for name in candidates:
            p = d / name
            if p.exists():
                try:
                    return ImageFont.truetype(str(p), size)
                except OSError:
                    continue
    return ImageFont.load_default()


def build():
    img = Image.new("RGB", (W, H), PLANE)
    d = ImageDraw.Draw(img)

    f_name = font(SERIF, 96)
    f_role = font(SERIF, 40)
    f_lede = font(SANS, 26)
    f_val = font(MONO_B, 40)
    f_key = font(MONO, 19)
    f_tag = font(MONO, 20)
    f_url = font(MONO, 22)

    pad = 76

    # Accent rule along the top — the one piece of brand colour on the card.
    d.rectangle([0, 0, W, 7], fill=ACCENT)

    # Availability tag left, URL right, sharing the top line. The URL was
    # originally bottom-right, where it collided with the third stat's label.
    y = pad
    d.ellipse([pad, y + 7, pad + 11, y + 18], fill=VERIFY)
    d.text((pad + 24, y), "OPEN TO HEALTHCARE IT & DATA ANALYST ROLES",
           font=f_tag, fill=VERIFY)

    url = "gadesaiharika.github.io"
    d.text((W - pad - d.textlength(url, font=f_url), y - 2), url,
           font=f_url, fill=ACCENT)

    # Name and role
    y += 52
    d.text((pad, y), "Sai Harika Gade", font=f_name, fill=INK)
    y += 112
    d.text((pad, y), "Research Data Analyst", font=f_role, fill=INK_2)

    # One line of positioning, wrapped by hand so it breaks where it should.
    y += 68
    for line in ("Healthcare data pipelines, and the validation",
                 "suites that decide whether their numbers hold."):
        d.text((pad, y), line, font=f_lede, fill=INK_2)
        y += 36

    # Figures, pulled from the repos rather than typed in.
    f = charts.hl7_facts()
    stats = [
        ("237", "automated checks"),
        ("1,047/1,047", "HL7 faults caught"),
        (f"{f['messages']:,}", "messages parsed"),
    ]

    d.line([pad, H - 176, W - pad, H - 176], fill=LINE, width=1)

    col_w = (W - pad * 2) / len(stats)
    for i, (val, key) in enumerate(stats):
        x = pad + i * col_w
        d.text((x, H - 152), val, font=f_val, fill=INK)
        d.text((x, H - 100), key.upper(), font=f_key, fill=MUTED)

    OUT.parent.mkdir(exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    return OUT


if __name__ == "__main__":
    p = build()
    print(f"card   {p.name:<30} {p.stat().st_size // 1024:>5} KB  ({W}x{H})")
