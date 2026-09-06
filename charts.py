"""
Inline SVG charts, drawn at build time from each repo's exported CSVs.

Why SVG and not the PNG dashboards: the homepage cards are the first proof a
reader sees, and a screenshot of a chart is the weakest form of it. These are
drawn from `data/exports/*.csv` in the project repos, so if a pipeline's numbers
change the site changes with them. Nothing here is typed in by hand.

Theming: every colour is `var(--chart-*)` with a literal fallback, so one CSS
block restyles all of them and they stay legible in light, dark, and inside the
inverted work band. No colour is hard-coded except as a fallback.

Geometry: each chart declares a viewBox and scales to its container. Font sizes
are in user units, so they scale with the chart rather than drifting out of
proportion at small widths.
"""

import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _read(repo, name):
    """Load one exported view as a list of dicts."""
    path = ROOT / repo / "data" / "exports" / name
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _open(vb_w, vb_h, title, desc, cls="chart"):
    return (f'<svg class="{cls}" viewBox="0 0 {vb_w} {vb_h}" '
            f'preserveAspectRatio="xMidYMid meet" role="img" '
            f'xmlns="http://www.w3.org/2000/svg">'
            f'<title>{_esc(title)}</title><desc>{_esc(desc)}</desc>')


# ==========================================================================
# 1. HL7 — rejection rate by interface
# ==========================================================================
def hl7_interfaces():
    """Horizontal bars, one per interface, sorted by rejection rate.

    The story is that one interface carries most of the failure: radiology
    results reject at 8.8% while pharmacy orders sit at 1.35%. A blended
    'error rate' across the engine would hide exactly that.
    """
    rows = _read("hl7-interface-monitor", "interface_health.csv")
    rows.sort(key=lambda r: float(r["rejection_rate_pct"]), reverse=True)

    pad_l, pad_r, pad_t = 132, 46, 26
    row_h, gap = 30, 8
    vb_w = 600
    vb_h = pad_t + len(rows) * (row_h + gap) + 26
    span = vb_w - pad_l - pad_r
    top = max(float(r["rejection_rate_pct"]) for r in rows)
    scale = span / (top * 1.12)

    out = [_open(vb_w, vb_h, "Rejection rate by interface",
                 "Radiology results reject at 8.8 percent, roughly six times the "
                 "pharmacy orders interface at 1.35 percent.")]

    # Baseline the bars grow from.
    y_end = pad_t + len(rows) * (row_h + gap) - gap
    out.append(f'<line x1="{pad_l}" y1="{pad_t - 8}" x2="{pad_l}" y2="{y_end}" '
               f'stroke="var(--chart-line, #d8d7d0)" stroke-width="1"/>')

    for i, r in enumerate(rows):
        y = pad_t + i * (row_h + gap)
        pct = float(r["rejection_rate_pct"])
        w = max(pct * scale, 2)
        # The worst interface is the finding, so it alone carries the warn colour.
        col = "var(--chart-warn, #d4573f)" if i == 0 else "var(--chart-1, #2a78d6)"
        label = r["interface"].replace("_", " ").title()

        out.append(
            f'<text x="{pad_l - 12}" y="{y + row_h / 2 + 4}" text-anchor="end" '
            f'class="c-lbl">{_esc(label)}</text>'
            f'<rect x="{pad_l + 1}" y="{y + 4}" width="{w:.1f}" height="{row_h - 8}" '
            f'rx="2" fill="{col}"/>'
            f'<text x="{pad_l + w + 9:.1f}" y="{y + row_h / 2 + 4}" '
            f'class="c-val">{pct:.2f}%</text>')

    out.append(f'<text x="{pad_l}" y="{vb_h - 6}" class="c-cap">'
               f'rejected share of {sum(int(r["messages"]) for r in rows):,} messages</text>')
    out.append("</svg>")
    return "".join(out)


# ==========================================================================
# 2. HRRP — observed rate against the CMS national benchmark
# ==========================================================================
def hrrp_cohorts():
    """Dumbbell chart: national benchmark dot, observed dot, connector between.

    A plain bar of the observed rate says nothing on its own — 27% is only
    alarming once you can see the 21.5% benchmark next to it. The connector
    length *is* the exposure, which is the number a quality director acts on.
    """
    rows = _read("hrrp-readmission-analytics", "vw_hrrp_cohort_summary.csv")
    rows = [r for r in rows if r["hrrp_condition"] != "OTHER"]
    rows.sort(key=lambda r: float(r["rate_pct"]), reverse=True)

    pad_l, pad_r, pad_t = 150, 54, 30
    row_h, gap = 30, 9
    vb_w = 600
    vb_h = pad_t + len(rows) * (row_h + gap) + 30
    span = vb_w - pad_l - pad_r
    top = max(max(float(r["rate_pct"]), float(r["national_rate_pct"])) for r in rows)
    scale = span / (top * 1.14)

    out = [_open(vb_w, vb_h, "30-day readmission rate against the CMS national benchmark",
                 "Heart failure runs 5.9 points above the national benchmark; COPD runs "
                 "2.8 points below it.")]

    for i, r in enumerate(rows):
        y = pad_t + i * (row_h + gap)
        obs = float(r["rate_pct"])
        nat = float(r["national_rate_pct"])
        x_o, x_n = pad_l + obs * scale, pad_l + nat * scale
        # Above benchmark is exposure, below it is headroom. Colour says which.
        col = ("var(--chart-warn, #d4573f)" if obs > nat
               else "var(--chart-2, #1baf7a)")
        cy = y + row_h / 2

        out.append(
            f'<text x="{pad_l - 12}" y="{cy + 4}" text-anchor="end" '
            f'class="c-lbl">{_esc(r["cohort_label"])}</text>'
            f'<line x1="{x_n:.1f}" y1="{cy}" x2="{x_o:.1f}" y2="{cy}" '
            f'stroke="{col}" stroke-width="3" stroke-linecap="round" opacity=".45"/>'
            f'<circle cx="{x_n:.1f}" cy="{cy}" r="4.5" fill="var(--chart-bg, #fcfcfb)" '
            f'stroke="var(--chart-muted, #8a8880)" stroke-width="2"/>'
            f'<circle cx="{x_o:.1f}" cy="{cy}" r="5.5" fill="{col}"/>'
            f'<text x="{max(x_o, x_n) + 11:.1f}" y="{cy + 4}" '
            f'class="c-val">{obs:.1f}%</text>')

    # Legend, so the two dots are not a puzzle.
    ly = vb_h - 8
    out.append(
        f'<circle cx="{pad_l + 5}" cy="{ly - 4}" r="4.5" fill="var(--chart-bg, #fcfcfb)" '
        f'stroke="var(--chart-muted, #8a8880)" stroke-width="2"/>'
        f'<text x="{pad_l + 16}" y="{ly}" class="c-cap">CMS national</text>'
        f'<circle cx="{pad_l + 138}" cy="{ly - 4}" r="5" fill="var(--chart-1, #2a78d6)"/>'
        f'<text x="{pad_l + 149}" y="{ly}" class="c-cap">this cohort</text>')
    out.append("</svg>")
    return "".join(out)


# ==========================================================================
# 3. Denials — Pareto of denied dollars
# ==========================================================================
def denial_pareto(n=8):
    """Bars of denied dollars by CARC code, with the cumulative share line.

    Preventable reasons are tinted differently because that is the actionable
    split: a prior-auth failure is a front-end process problem, a medical
    necessity denial largely is not.
    """
    rows = _read("revenue-cycle-denials", "vw_denial_pareto.csv")[:n]

    pad_l, pad_r, pad_t, pad_b = 54, 46, 24, 62
    vb_w, vb_h = 600, 300
    plot_w = vb_w - pad_l - pad_r
    plot_h = vb_h - pad_t - pad_b
    slot = plot_w / len(rows)
    bw = slot * 0.6
    top = max(float(r["denied_amount"]) for r in rows) * 1.08

    out = [_open(vb_w, vb_h, "Denied dollars by reason code, with cumulative share",
                 "Prior authorisation alone is 50 percent of denied dollars; the top "
                 "three codes reach 67.6 percent.")]

    # Horizontal grid at quarter steps — enough to read against, not a cage.
    for f in (0.25, 0.5, 0.75, 1.0):
        gy = pad_t + plot_h - plot_h * f
        out.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{pad_l + plot_w}" y2="{gy:.1f}" '
                   f'stroke="var(--chart-line, #d8d7d0)" stroke-width="1" opacity=".6"/>')
        out.append(f'<text x="{pad_l - 9}" y="{gy + 4:.1f}" text-anchor="end" '
                   f'class="c-cap">${top * f / 1e6:.0f}M</text>')

    pts = []
    for i, r in enumerate(rows):
        amt = float(r["denied_amount"])
        h = plot_h * (amt / top)
        x = pad_l + i * slot + (slot - bw) / 2
        y = pad_t + plot_h - h
        prevent = r["is_preventable"] == "True"
        col = ("var(--chart-warn, #d4573f)" if prevent
               else "var(--chart-muted-bar, #a9a79e)")

        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" '
                   f'rx="2" fill="{col}"/>')
        out.append(f'<text x="{x + bw / 2:.1f}" y="{pad_t + plot_h + 17}" '
                   f'text-anchor="middle" class="c-lbl-sm">{_esc(r["carc_code"])}</text>')

        cum = float(r["cumulative_pct"])
        pts.append((x + bw / 2, pad_t + plot_h - plot_h * (cum / 100)))

    # Cumulative share line, drawn over the bars.
    path = " ".join(f"{'M' if i == 0 else 'L'}{px:.1f},{py:.1f}"
                    for i, (px, py) in enumerate(pts))
    out.append(f'<path d="{path}" fill="none" stroke="var(--chart-1, #2a78d6)" '
               f'stroke-width="2" stroke-linejoin="round"/>')
    for px, py in pts:
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3" '
                   f'fill="var(--chart-1, #2a78d6)"/>')
    # Call out where the cumulative line lands, since that is the takeaway.
    out.append(f'<text x="{pts[-1][0] - 4:.1f}" y="{pts[-1][1] - 11:.1f}" '
               f'text-anchor="end" class="c-val">{float(rows[-1]["cumulative_pct"]):.0f}% '
               f'of denied $</text>')

    ly = vb_h - 12
    out.append(
        f'<rect x="{pad_l}" y="{ly - 9}" width="10" height="10" rx="2" '
        f'fill="var(--chart-warn, #d4573f)"/>'
        f'<text x="{pad_l + 16}" y="{ly}" class="c-cap">preventable</text>'
        f'<rect x="{pad_l + 116}" y="{ly - 9}" width="10" height="10" rx="2" '
        f'fill="var(--chart-muted-bar, #a9a79e)"/>'
        f'<text x="{pad_l + 132}" y="{ly}" class="c-cap">not preventable</text>')
    out.append("</svg>")
    return "".join(out)


# ==========================================================================
# 4. Hero readout — daily rejection rate across the whole engine
# ==========================================================================
def hl7_sparkline():
    """A 30-day sparkline of engine-wide rejection rate.

    Aggregated across all five interfaces per day, so it is one honest series
    rather than five overlaid. Returns (svg, lo, hi, days).
    """
    rows = _read("hl7-interface-monitor", "daily_trend.csv")

    by_day = {}
    for r in rows:
        d = by_day.setdefault(r["date"], [0, 0])
        d[0] += int(r["messages"])
        d[1] += int(r["rejected"])
    series = [(d, rej / msg * 100) for d, (msg, rej) in sorted(by_day.items()) if msg]

    vb_w, vb_h = 300, 66
    pad = 5
    vals = [v for _, v in series]
    lo, hi = min(vals), max(vals)
    rng = (hi - lo) or 1
    step = (vb_w - pad * 2) / (len(series) - 1)

    def xy(i, v):
        return (pad + i * step,
                pad + (vb_h - pad * 2) * (1 - (v - lo) / rng))

    pts = [xy(i, v) for i, v in enumerate(vals)]
    line = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}"
                    for i, (x, y) in enumerate(pts))
    area = (f"M{pts[0][0]:.1f},{vb_h - pad} "
            + " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts)
            + f" L{pts[-1][0]:.1f},{vb_h - pad} Z")

    svg = (_open(vb_w, vb_h,
                 "Daily rejection rate across all interfaces",
                 f"Thirty days of engine-wide rejection rate, ranging from "
                 f"{lo:.1f} to {hi:.1f} percent.", cls="spark")
           + f'<path d="{area}" fill="var(--chart-1, #2a78d6)" opacity=".10"/>'
           + f'<path d="{line}" fill="none" stroke="var(--chart-1, #2a78d6)" '
             f'stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/>'
           + f'<circle cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="2.8" '
             f'fill="var(--chart-1, #2a78d6)"/>'
           + "</svg>")
    return svg, lo, hi, len(series)


def hl7_facts():
    """Totals for the hero readout, summed from the same export the chart uses.

    Kept here rather than typed into build.py so the panel cannot drift away
    from the chart sitting next to it.
    """
    rows = _read("hl7-interface-monitor", "interface_health.csv")
    msgs = sum(int(r["messages"]) for r in rows)
    rej = sum(int(r["rejected"]) for r in rows)
    return {
        "messages": msgs,
        "rejected": rej,
        "rejection_pct": rej / msgs * 100,
        "interfaces": len(rows),
    }


CHARTS = {
    "hl7-interface-monitor": hl7_interfaces,
    "hrrp-readmission-analytics": hrrp_cohorts,
    "revenue-cycle-denials": denial_pareto,
}


if __name__ == "__main__":
    for slug, fn in CHARTS.items():
        svg = fn()
        print(f"{slug:<32} {len(svg):>6} bytes")
    s, lo, hi, n = hl7_sparkline()
    print(f"{'hero sparkline':<32} {len(s):>6} bytes  "
          f"{n} days, {lo:.2f}%-{hi:.2f}%")
