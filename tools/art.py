"""Vector art for Methodical cards.

Every illustration is drawn in a 200 x 150 art box (viewBox "0 0 200 150") as light line art on the
card's coloured background. Functions return SVG fragments (strings); `frame()` wraps a fragment into a
complete <svg> with the background, so art can be previewed or embedded anywhere.

Style rules (keep new art consistent):
  * main lines and figures in INK, highlights in ACC (amber), "bad"/outcome marks in HOT (rose),
    secondary or background elements in DIM;
  * stroke width 3 for main lines, 2 for detail; round caps and joins;
  * leave ~10 px margin to the art-box edge; one clear idea per picture.
"""
import math

INK = "#F8FAFC"
DIM = "rgba(248,250,252,.38)"
FAINT = "rgba(248,250,252,.16)"
ACC = "#FCD34D"
HOT = "#FB7185"
COOL = "#7DD3FC"


def _f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


# --------------------------------------------------------------------------- primitives
def line(pts, c=INK, w=3, dash=None, fill="none", close=False, o=1):
    d = " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
    tag = "polygon" if close else "polyline"
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<{tag} points="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity="{o}"{da}/>')


def path(d, c=INK, w=3, fill="none", dash=None, o=1):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-linejoin="round" opacity="{o}"{da}/>')


def circle(x, y, r, fill=INK, stroke="none", w=2, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<circle cx="{_f(x)}" cy="{_f(y)}" r="{_f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" opacity="{o}"{da}/>'


def rect(x, y, w, h, fill="none", stroke=INK, sw=3, rx=3, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}" opacity="{o}"{da}/>')


def text(x, y, s, size=14, c=INK, anchor="middle", weight=700, family="'Barlow Condensed', 'Arial Narrow', sans-serif", o=1):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{_f(x)}" y="{_f(y)}" font-size="{size}" fill="{c}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-family="{family}" opacity="{o}">{s}</text>')


def arrow(x1, y1, x2, y2, c=INK, w=3, dash=None, head=8, o=1):
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * 0.8 * math.cos(a), y2 - head * 0.8 * math.sin(a)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (line([(x1, y1), (bx, by)], c, w, dash, o=o)
            + line([p1, (x2, y2), p2], c, w, fill=c, close=True, o=o))


def carrow(x1, y1, cx, cy, x2, y2, c=INK, w=3, dash=None, head=8, o=1):
    """Quadratic curved arrow from (x1,y1) to (x2,y2) bending toward control point (cx,cy)."""
    a = math.atan2(y2 - cy, x2 - cx)
    p1 = (x2 - head * math.cos(a - 0.45), y2 - head * math.sin(a - 0.45))
    p2 = (x2 - head * math.cos(a + 0.45), y2 - head * math.sin(a + 0.45))
    return (path(f"M{_f(x1)},{_f(y1)} Q{_f(cx)},{_f(cy)} {_f(x2)},{_f(y2)}", c, w, dash=dash, o=o)
            + line([p1, (x2, y2), p2], c, w, fill=c, close=True, o=o))


def person(x, y, s=1.0, c=INK, o=1):
    """Pictogram person standing with feet near y + 9s, head centred on x."""
    return (circle(x, y - 9 * s, 4.3 * s, c, o=o)
            + f'<path d="M{_f(x - 7 * s)},{_f(y + 9 * s)} V{_f(y + 2 * s)} Q{_f(x - 7 * s)},{_f(y - 3 * s)} {_f(x)},{_f(y - 3 * s)} '
              f'Q{_f(x + 7 * s)},{_f(y - 3 * s)} {_f(x + 7 * s)},{_f(y + 2 * s)} V{_f(y + 9 * s)} Z" fill="{c}" opacity="{o}"/>')


def crowd(x0, y0, cols, rows, dx=18, dy=24, s=0.8, color=lambda i, j: INK):
    return "".join(person(x0 + i * dx, y0 + j * dy, s, color(i, j)) for j in range(rows) for i in range(cols))


def dice(x, y, size=34, face=5, c=INK, pip="#0f172a", rot=-12):
    h = size / 2
    pos = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
           5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[face]
    pips = "".join(circle(x + px * size * 0.27, y + py * size * 0.27, size * 0.085, pip) for px, py in pos)
    return (f'<g transform="rotate({rot} {_f(x)} {_f(y)})">' + rect(x - h, y - h, size, size, c, "none", 0, rx=size * 0.18)
            + pips + "</g>")


def doc(x, y, w=26, h=34, c=INK, lines=3, fill="none", sw=2.5, lc=None):
    fold = w * 0.3
    out = path(f"M{_f(x)},{_f(y)} H{_f(x + w - fold)} L{_f(x + w)},{_f(y + fold)} V{_f(y + h)} H{_f(x)} Z", c, sw, fill=fill)
    out += path(f"M{_f(x + w - fold)},{_f(y)} V{_f(y + fold)} H{_f(x + w)}", c, sw * 0.8)
    for i in range(lines):
        ly = y + fold + 5 + i * (h - fold - 8) / max(lines, 1)
        out += line([(x + 5, ly), (x + w - 5 - (i % 2) * 5, ly)], lc or c, 2)
    return out


def axes(x, y, w, h, c=INK, sw=2.5):
    return arrow(x, y + h, x, y, c, sw, head=6) + arrow(x, y + h, x + w, y + h, c, sw, head=6)


def cylinder(x, y, w=40, h=46, c=INK, fill="none"):
    ry = w * 0.18
    out = path(f"M{_f(x)},{_f(y + ry)} V{_f(y + h - ry)} A{_f(w / 2)},{_f(ry)} 0 0 0 {_f(x + w)},{_f(y + h - ry)} V{_f(y + ry)}", c, 2.5, fill=fill)
    out += f'<ellipse cx="{_f(x + w / 2)}" cy="{_f(y + ry)}" rx="{_f(w / 2)}" ry="{_f(ry)}" fill="{fill}" stroke="{c}" stroke-width="2.5"/>'
    for k in (1, 2):
        yy = y + ry + k * (h - 2 * ry) / 3
        out += path(f"M{_f(x)},{_f(yy)} A{_f(w / 2)},{_f(ry)} 0 0 0 {_f(x + w)},{_f(yy)}", c, 2, o=.7)
    return out


def building(x, y, w=34, h=30, c=INK, fill="none", roof=12):
    return (path(f"M{_f(x)},{_f(y + h)} V{_f(y + roof)} L{_f(x + w / 2)},{_f(y)} L{_f(x + w)},{_f(y + roof)} V{_f(y + h)} Z", c, 2.5, fill=fill))


def magnifier(x, y, r=16, c=INK, w=3.5):
    a = math.radians(45)
    return circle(x, y, r, "none", c, w) + line([(x + r * math.cos(a), y + r * math.sin(a)), (x + r * 2 * math.cos(a), y + r * 2 * math.sin(a))], c, w + 2)


def bubble(x, y, w, h, c=INK, fill="none", tail="left", sw=2.5):
    tx = x + w * 0.25 if tail == "left" else x + w * 0.75
    td = -8 if tail == "left" else 8
    return path(f"M{_f(x + 6)},{_f(y)} H{_f(x + w - 6)} Q{_f(x + w)},{_f(y)} {_f(x + w)},{_f(y + 6)} V{_f(y + h - 6)} "
                f"Q{_f(x + w)},{_f(y + h)} {_f(x + w - 6)},{_f(y + h)} H{_f(tx + 6)} L{_f(tx + td)},{_f(y + h + 9)} L{_f(tx - 2)},{_f(y + h)} "
                f"H{_f(x + 6)} Q{_f(x)},{_f(y + h)} {_f(x)},{_f(y + h - 6)} V{_f(y + 6)} Q{_f(x)},{_f(y)} {_f(x + 6)},{_f(y)} Z", c, sw, fill=fill)


def pill(x, y, w=34, h=14, rot=-25, c1=INK, c2=ACC):
    r = h / 2
    return (f'<g transform="rotate({rot} {_f(x)} {_f(y)})">'
            f'<path d="M{_f(x)},{_f(y - r)} H{_f(x - w / 2 + r)} A{_f(r)},{_f(r)} 0 0 0 {_f(x - w / 2 + r)},{_f(y + r)} H{_f(x)} Z" fill="{c1}"/>'
            f'<path d="M{_f(x)},{_f(y - r)} H{_f(x + w / 2 - r)} A{_f(r)},{_f(r)} 0 0 1 {_f(x + w / 2 - r)},{_f(y + r)} H{_f(x)} Z" fill="{c2}"/></g>')


def star(x, y, r=8, c=ACC, pts=5):
    p = []
    for k in range(pts * 2):
        rr = r if k % 2 == 0 else r * 0.45
        a = -math.pi / 2 + k * math.pi / pts
        p.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return line(p, c, 1, fill=c, close=True)


def check(x, y, s=10, c="#86EFAC", w=3.5):
    return line([(x - s * 0.6, y), (x - s * 0.15, y + s * 0.5), (x + s * 0.7, y - s * 0.5)], c, w)


def cross(x, y, s=8, c=HOT, w=3.5):
    return line([(x - s, y - s), (x + s, y + s)], c, w) + line([(x - s, y + s), (x + s, y - s)], c, w)


def clock(x, y, r=14, c=INK, h1=-60, h2=60, sw=2.5):
    a1, a2 = math.radians(h1 - 90), math.radians(h2 - 90)
    return (circle(x, y, r, "none", c, sw) + line([(x, y), (x + r * .5 * math.cos(a1), y + r * .5 * math.sin(a1))], c, sw)
            + line([(x, y), (x + r * .75 * math.cos(a2), y + r * .75 * math.sin(a2))], c, sw))


def hourglass(x, y, s=1.0, c=INK, sand=ACC):
    w, h = 14 * s, 20 * s
    return (line([(x - w, y - h), (x + w, y - h)], c, 3) + line([(x - w, y + h), (x + w, y + h)], c, 3)
            + path(f"M{_f(x - w + 2)},{_f(y - h)} Q{_f(x - w + 2)},{_f(y)} {_f(x)},{_f(y)} Q{_f(x - w + 2)},{_f(y)} {_f(x - w + 2)},{_f(y + h)} "
                   f"M{_f(x + w - 2)},{_f(y - h)} Q{_f(x + w - 2)},{_f(y)} {_f(x)},{_f(y)} Q{_f(x + w - 2)},{_f(y)} {_f(x + w - 2)},{_f(y + h)}", c, 2.5)
            + path(f"M{_f(x - w * .55)},{_f(y + h - 1)} Q{_f(x)},{_f(y + h * .35)} {_f(x + w * .55)},{_f(y + h - 1)} Z", sand, 1, fill=sand))


def gear(x, y, r=14, c=INK, teeth=8, fill="none", sw=2.5):
    p = []
    for k in range(teeth * 4):
        a = k * 2 * math.pi / (teeth * 4)
        rr = r if (k % 4) in (0, 1) else r * 0.78
        p.append((x + rr * math.cos(a), y + rr * math.sin(a)))
    return line(p, c, sw, fill=fill, close=True) + circle(x, y, r * 0.32, "none", c, sw)


def flask(x, y, s=1.0, c=INK, liquid=ACC):
    n, b = 6 * s, 20 * s
    top, neck, bot = y - 22 * s, y - 6 * s, y + 18 * s
    return (path(f"M{_f(x - b * .5)},{_f(bot - 10 * s)} L{_f(x - n)},{_f(neck)} V{_f(top)}", c, 0)
            + path(f"M{_f(x - b + 6 * s)},{_f(y + 6 * s)} L{_f(x + b - 6 * s)},{_f(y + 6 * s)} L{_f(x + b)},{_f(bot)} H{_f(x - b)} Z", liquid, 0, fill=liquid, o=.9)
            + path(f"M{_f(x - n)},{_f(top)} V{_f(neck)} L{_f(x - b)},{_f(bot)} H{_f(x + b)} L{_f(x + n)},{_f(neck)} V{_f(top)}", c, 3)
            + line([(x - n - 4 * s, top), (x + n + 4 * s, top)], c, 3))


def eye(x, y, s=1.0, c=INK, pupil=ACC):
    w, h = 22 * s, 12 * s
    return (path(f"M{_f(x - w)},{_f(y)} Q{_f(x)},{_f(y - h * 2)} {_f(x + w)},{_f(y)} Q{_f(x)},{_f(y + h * 2)} {_f(x - w)},{_f(y)} Z", c, 3)
            + circle(x, y, 7 * s, pupil) + circle(x, y, 3 * s, "#0f172a"))


def globe(x, y, r=22, c=INK):
    return (circle(x, y, r, "none", c, 3) + f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(r * .45)}" ry="{_f(r)}" fill="none" stroke="{c}" stroke-width="2"/>'
            + line([(x - r, y), (x + r, y)], c, 2) + path(f"M{_f(x - r * .87)},{_f(y - r * .5)} Q{_f(x)},{_f(y - r * .3)} {_f(x + r * .87)},{_f(y - r * .5)}", c, 2)
            + path(f"M{_f(x - r * .87)},{_f(y + r * .5)} Q{_f(x)},{_f(y + r * .7)} {_f(x + r * .87)},{_f(y + r * .5)}", c, 2))


def bolt(x, y, s=1.0, c=ACC):
    return line([(x + 3 * s, y - 16 * s), (x - 7 * s, y + 2 * s), (x, y + 2 * s), (x - 4 * s, y + 16 * s), (x + 8 * s, y - 3 * s), (x + 1 * s, y - 3 * s)], c, 1.5, fill=c, close=True)


def helix(x0, y0, x1, h=18, turns=3, c1=INK, c2=ACC):
    n = 60
    out1, out2, rungs = [], [], ""
    for k in range(n + 1):
        t = k / n
        xx = x0 + (x1 - x0) * t
        ph = t * turns * 2 * math.pi
        out1.append((xx, y0 + h * math.sin(ph)))
        out2.append((xx, y0 - h * math.sin(ph)))
        if k % 4 == 2:
            rungs += line([(xx, y0 + h * math.sin(ph)), (xx, y0 - h * math.sin(ph))], DIM, 2)
    return rungs + line(out1, c1, 3) + line(out2, c2, 3)


def node(x, y, label, r=13, fill="none", c=INK, tc=None, size=14):
    return circle(x, y, r, fill, c, 2.5) + text(x, y + size * 0.36, label, size, tc or c)


def scatter(points, r=2.6, c=INK, o=1):
    return "".join(circle(x, y, r, c, o=o) for x, y in points)


def lcg(seed):
    """Tiny deterministic random generator, so art is identical on every build."""
    state = [seed]

    def rnd():
        state[0] = (state[0] * 1103515245 + 12345) % 2 ** 31
        return state[0] / 2 ** 31
    return rnd


# --------------------------------------------------------------------------- frame
def frame(inner, uid, c1="#334155", c2="#0f172a", pattern=True, vb="0 0 200 150"):
    """Wrap art into a full SVG with a two-tone gradient background and a faint blueprint dot grid."""
    pat = (f'<pattern id="d{uid}" width="10" height="10" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".9" fill="#fff" opacity=".13"/></pattern>'
           if pattern else "")
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" role="img">'
            f'<defs><linearGradient id="g{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>{pat}'
            f'<radialGradient id="r{uid}" cx=".5" cy=".42" r=".65"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="100%" height="100%" fill="url(#g{uid})"/>'
            + (f'<rect width="100%" height="100%" fill="url(#d{uid})"/>' if pattern else "")
            + f'<rect width="100%" height="100%" fill="url(#r{uid})"/>{inner}</svg>')


def shade(hex_color, f):
    """Mix a hex colour toward black (f<0) or white (f>0)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    t = 255 if f > 0 else 0
    f = abs(f)
    return "#%02x%02x%02x" % tuple(round(v + (t - v) * f) for v in (r, g, b))


# --------------------------------------------------------------------------- small icons (24x24, currentColor)
def _icon(body):
    return (f'<svg viewBox="0 0 24 24" class="ic" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')


SUIT_ICONS = {
    "DESCRIBE": _icon('<path d="M4 20V10M10 20V4M16 20v-7M21 20H3"/>'),
    "EXPLORE": _icon('<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z" fill="currentColor"/>'),
    "ASSOCIATE": _icon('<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>'),
    "CAUSE": _icon('<circle cx="16" cy="8" r="5"/><circle cx="16" cy="8" r="1.5" fill="currentColor"/><path d="M3 21l9.5-9.5M3 21h4M3 21v-4"/>'),
    "PREDICT": _icon('<circle cx="12" cy="10" r="7"/><path d="M7 21h10M9 17.5 8 21M15 17.5l1 3.5"/><path d="M9 8a3 3 0 0 1 3-2"/>'),
    "MEASURE": _icon('<rect x="2" y="8" width="20" height="8" rx="1"/><path d="M6 8v3M10 8v4M14 8v3M18 8v4"/>'),
    "EXPLAIN": _icon('<path d="M18 4H6l6 8-6 8h12"/>'),
    "BUILD": _icon('<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8 6.2 21l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.6-.6-2.4z"/>'),
    "SYNTHESIZE": _icon('<path d="m12 3 9 4.5-9 4.5-9-4.5z"/><path d="m3 12 9 4.5 9-4.5M3 16.5 12 21l9-4.5"/>'),
}

CONSTRAINT_ICONS = {
    "no-assign": _icon('<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/><path d="M9.5 11.5h5" />'),
    "rare-outcome": _icon('<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3l3 18 3-18"/>'),
    "rare-exposure": _icon('<circle cx="12" cy="12" r="2" fill="currentColor"/><path d="M12 3a9 9 0 0 1 7.8 4.5L14 10.8M4.2 7.5A9 9 0 0 1 12 3M4.2 16.5 10 13.2M19.8 16.5 14 13.2M12 21a9 9 0 0 1-7.8-4.5M19.8 16.5A9 9 0 0 1 12 21"/>'),
    "long-latency": _icon('<path d="M6 2h12M6 22h12M7 2c0 6 10 6 10 10S7 16 7 22M17 2c0 6-10 6-10 10s10 4 10 10"/>'),
    "transient": _icon('<path d="M13 2 4 14h7l-1 8 9-12h-7z" fill="currentColor"/>'),
    "existing-data": _icon('<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>'),
    "single-unit": _icon('<circle cx="12" cy="6" r="3.5"/><path d="M5 21v-3a7 7 0 0 1 14 0v3"/>'),
    "group-level": _icon('<circle cx="12" cy="7" r="3"/><circle cx="5" cy="9" r="2.4"/><circle cx="19" cy="9" r="2.4"/><path d="M7 20v-2a5 5 0 0 1 10 0v2M1.5 19v-1.5A3.5 3.5 0 0 1 6 14M22.5 19v-1.5A3.5 3.5 0 0 0 18 14"/>'),
    "cutoff": _icon('<path d="M12 2v20" stroke-dasharray="2 3"/><path d="M3 16l4-3 4-2M13 7l4-2 4-3"/>'),
    "rollout": _icon('<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/><path d="M7 18h3v-3h3v-3h4" />'),
    "fast-cheap": _icon('<circle cx="9" cy="14" r="6"/><path d="M9 11v3l2 1"/><path d="M17 3v6M14 6h6"/>'),
    "unknown-territory": _icon('<path d="M7 18a5 5 0 1 1 .9-9.9A6 6 0 0 1 19 9a4.5 4.5 0 0 1-1 9z"/><path d="M11 10.5a1.8 1.8 0 1 1 2 1.8c-.6.2-1 .7-1 1.2"/><circle cx="12" cy="16" r=".6" fill="currentColor"/>'),
    "many-studies": _icon('<rect x="4" y="9" width="13" height="12" rx="1"/><path d="M7 6h13v12M10 3h13v12" />'),
}


# --------------------------------------------------------------------------- design art (50)
def _arms(x, y, n, dx, c):
    return "".join(person(x + i * dx, y, 0.75, c) for i in range(n))


def art_case_report():
    return (person(78, 80, 2.2, INK) + circle(78, 64, 40, "none", ACC, 4) + line([(106, 92), (126, 112)], ACC, 8)
            + rect(134, 34, 44, 58, "none", INK, 2.5) + rect(147, 29, 18, 9, INK, INK, 0, 2)
            + text(156, 74, "!", 34, HOT) + line([(142, 84), (170, 84)], DIM, 2))


def art_cross_sectional():
    r = lcg(4)
    pc = lambda i, j: HOT if r() < .3 else INK
    return (crowd(30, 46, 8, 3, 20, 32, 0.75, pc) + rect(16, 22, 168, 100, "none", ACC, 3, 6, dash="7 6")
            + line([(14, 136), (186, 136)], DIM, 2) + circle(100, 136, 5, ACC) + text(100, 18, "NOW", 12, ACC))


def art_ecological():
    pts = [(48, 108, 9), (72, 92, 12), (98, 86, 8), (120, 66, 14), (148, 54, 11), (170, 36, 9)]
    out = axes(24, 18, 166, 112)
    for x, y, r in pts:
        out += circle(x, y, r, "none", INK, 2.5) + "".join(circle(x + dx, y + dy, 1.5, ACC) for dx, dy in ((-3, -2), (3, 1), (0, 3), (-2, 3), (2, -3)))
    return out + line([(36, 116), (184, 30)], ACC, 2.5, dash="6 5")


def art_surveillance():
    ys = [44, 48, 46, 54, 52, 60, 58, 66, 72, 70, 80, 84, 88, 96, 98, 106]
    pts = [(24 + i * 10.5, y) for i, y in enumerate(ys)]
    return (axes(16, 24, 172, 106) + line(pts, INK, 3) + scatter(pts, 3.2, ACC)
            + eye(158, 38, 0.9))


def art_cohort_prospective():
    out = crowd(28, 42, 2, 3, 20, 30, 0.75, lambda i, j: ACC if i == 0 else INK)
    out += arrow(74, 72, 122, 72, INK, 3) + clock(98, 46, 11)
    out += crowd(140, 42, 2, 3, 20, 30, 0.75, lambda i, j: HOT if (i + j) % 3 == 0 else INK)
    return out + arrow(18, 138, 186, 138, ACC, 2.5) + text(182, 131, "TIME", 11, ACC, "end")


def art_cohort_retrospective():
    out = "".join(doc(14 + k * 7, 34 + k * 7, 30, 40, INK, 3, fill="#0f172a33") for k in range(3))
    out += arrow(64, 76, 112, 76, INK, 3)
    out += crowd(132, 46, 2, 3, 20, 28, 0.72, lambda i, j: HOT if (i + j) % 2 == 0 else INK)
    out += carrow(120, 30, 98, 8, 74, 26, ACC, 3) + text(98, 42, "REWIND", 10, ACC)
    return out


def art_case_control():
    out = text(150, 24, "CASES", 12, HOT) + _arms(130, 46, 3, 20, HOT)
    out += text(150, 84, "CONTROLS", 12, INK) + _arms(130, 108, 3, 20, INK)
    out += arrow(116, 44, 66, 56, ACC, 3) + arrow(116, 106, 66, 92, ACC, 3)
    out += text(40, 86, "?", 46, ACC)
    return out + arrow(186, 140, 16, 140, DIM, 2.5)


def art_case_crossover():
    out = person(30, 70, 1.6, INK) + line([(56, 110), (190, 110)], INK, 3)
    for x in (64, 100):
        out += rect(x, 96, 26, 14, "none", DIM, 2, 2, dash="4 3")
    out += rect(138, 92, 26, 18, ACC, ACC, 0, 2) + bolt(176, 82, 1.3, HOT)
    return out + text(151, 128, "HAZARD", 11, ACC) + text(90, 128, "CONTROL WINDOWS", 11, DIM)


def art_target_trial():
    out = rect(18, 26, 52, 70, "none", COOL, 2.5, 3, dash="5 4") + "".join(
        check(30, 42 + k * 15, 7, COOL, 2.5) + line([(38, 42 + k * 15), (60, 42 + k * 15)], COOL, 2) for k in range(4))
    out += arrow(76, 62, 100, 62, INK, 3) + cylinder(104, 38, 40, 50, INK)
    out += arrow(148, 54, 176, 38, ACC, 3) + arrow(148, 72, 176, 90, INK, 3)
    return out + text(44, 116, "PROTOCOL", 11, COOL) + text(124, 116, "REAL DATA", 11, INK)


def _dag_zxy(zart, crossed=True):
    out = zart + node(100, 106, "X", 15) + node(168, 106, "Y", 15)
    out += arrow(54, 98, 83, 104) + arrow(116, 106, 151, 106)
    out += node(134, 34, "U", 14, "none", DIM) + arrow(124, 45, 106, 90, DIM, 2.5, "5 4") + arrow(142, 46, 162, 90, DIM, 2.5, "5 4")
    if crossed:
        out += path("M48,86 Q110,60 156,96", DIM, 2, dash="3 5") + cross(104, 72, 6)
    return out


def art_iv():
    return _dag_zxy(dice(36, 100, 30, 3) + text(36, 136, "Z", 14, ACC))


def art_mendelian():
    return _dag_zxy(helix(12, 100, 58, 12, 1.6) + text(36, 136, "GENES", 12, ACC))


def art_did():
    out = axes(16, 18, 174, 114) + line([(100, 18), (100, 128)], DIM, 2, "4 4")
    out += line([(24, 104), (100, 88), (180, 72)], INK, 3) + line([(24, 82), (100, 66)], ACC, 3)
    out += line([(100, 66), (180, 50)], ACC, 2.5, "5 4") + line([(100, 66), (180, 26)], ACC, 3.5)
    out += line([(186, 28), (186, 48)], HOT, 3) + text(100, 146, "", 1)
    return out


def art_rdd():
    r = lcg(9)
    out = axes(16, 16, 174, 116) + line([(104, 16), (104, 130)], ACC, 2.5, "6 5")
    pts = []
    for k in range(34):
        x = 24 + k * 4.8
        base = 112 - (x - 24) * 0.32 - (26 if x > 104 else 0)
        pts.append((x, base + (r() - .5) * 18))
    out += scatter(pts, 2.4, DIM) + line([(24, 112), (104, 86.4)], INK, 3.5) + line([(104, 60.4), (184, 34.8)], INK, 3.5)
    return out + line([(110, 86), (110, 61)], HOT, 3.5) + text(104, 12, "CUTOFF", 11, ACC)


def art_its():
    pts1 = [(24 + i * 8, 52 + i * 3.2 + (2 if i % 2 else -2)) for i in range(10)]
    pts2 = [(110 + i * 8, 96 + i * 2.5 + (2 if i % 2 else -2)) for i in range(10)]
    return (axes(16, 18, 174, 114) + line([(104, 18), (104, 128)], ACC, 2.5, "6 5")
            + line([(104, 84), (186, 116)], DIM, 2, "5 4") + scatter(pts1, 3.2) + scatter(pts2, 3.2, ACC)
            + line([(24, 52), (96, 81)], INK, 2.5) + line([(110, 96), (182, 118)], ACC, 2.5))


def art_synthetic_control():
    out = axes(16, 18, 174, 114) + line([(110, 18), (110, 128)], DIM, 2, "4 4")
    for k, dy in enumerate((-18, 14, 26, -30)):
        out += line([(24, 96 + dy * .6), (110, 70 + dy), (182, 60 + dy * 1.2)], FAINT, 2)
    out += line([(24, 96), (60, 86), (110, 70), (150, 64), (182, 58)], COOL, 3, "6 4")
    out += line([(24, 97), (60, 85), (110, 70), (150, 86), (182, 98)], ACC, 3.5)
    return out + text(178, 50, "TWIN", 11, COOL, "end")


def art_rct():
    out = crowd(22, 56, 2, 3, 18, 26, 0.7)
    out += arrow(54, 80, 74, 80) + dice(94, 80, 32, 5)
    out += arrow(114, 70, 136, 48, INK, 3) + arrow(114, 90, 136, 112, INK, 3)
    out += _arms(146, 46, 3, 17, ACC) + _arms(146, 116, 3, 17, INK)
    return out


def art_cluster_rct():
    out = ""
    for k, x in enumerate((14, 60, 106, 152)):
        treated = k in (0, 3)
        c = ACC if treated else INK
        out += building(x, 30, 36, 34, c) + "".join(circle(x + 8 + i * 10, 56, 2.4, c) for i in range(3))
        out += line([(x + 18, 70), (x + 18, 90)], DIM, 2, "3 3")
    return out + dice(100, 112, 30, 4, rot=8) + text(38, 104, "", 1)


def art_crossover():
    out = ""
    for row, (a, b) in enumerate(((ACC, COOL), (COOL, ACC))):
        y = 44 + row * 52
        out += person(24, y + 8, 1.0, INK)
        out += rect(44, y, 56, 18, a, a, 0, 4) + rect(124, y, 56, 18, b, b, 0, 4)
        out += text(72, y + 14, "A" if a == ACC else "B", 14, "#0f172a") + text(152, y + 14, "B" if b == COOL else "A", 14, "#0f172a")
    out += path("M100,53 L124,105 M100,105 L124,53", DIM, 2, dash="4 4")
    return out + text(112, 138, "WASHOUT", 11, DIM)


def art_factorial_doe():
    o, s, dx, dy = (54, 112), 64, 34, -26
    P = lambda i, j, k: (o[0] + i * s + k * dx, o[1] - j * s + k * dy)
    out = ""
    edges = [((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (0, 1, 0)), ((0, 0, 0), (0, 0, 1)), ((1, 0, 0), (1, 1, 0)), ((1, 0, 0), (1, 0, 1)),
             ((0, 1, 0), (1, 1, 0)), ((0, 1, 0), (0, 1, 1)), ((0, 0, 1), (1, 0, 1)), ((0, 0, 1), (0, 1, 1)), ((1, 1, 0), (1, 1, 1)),
             ((1, 0, 1), (1, 1, 1)), ((0, 1, 1), (1, 1, 1))]
    for a, b in edges:
        out += line([P(*a), P(*b)], DIM if 0 in (a[2] + b[2],) else INK, 2.5)
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                x, y = P(i, j, k)
                out += circle(x, y, 6.5, ACC if (i + j + k) % 2 else INK)
    return out


def art_n_of_1():
    seq = "ABBABAAB"
    out = person(100, 44, 1.7, INK)
    for k, ch in enumerate(seq):
        c = ACC if ch == "A" else COOL
        out += rect(18 + k * 21, 92, 18, 22, c, c, 0, 3) + text(27 + k * 21, 108, ch, 13, "#0f172a")
    return out + line([(18, 124), (184, 124)], DIM, 2)


def art_stepped_wedge():
    out = ""
    for row in range(4):
        for col in range(5):
            on = col > row
            out += rect(28 + col * 30, 22 + row * 26, 26, 22, ACC if on else "none", ACC if on else DIM, 2, 2)
    return out + arrow(28, 134, 176, 134, DIM, 2) + text(102, 148, "TIME", 10, DIM)


def art_ab_test():
    out = ""
    for k, (lab, c, h) in enumerate((("A", INK, 40), ("B", ACC, 62))):
        x = 18 + k * 92
        out += rect(x, 18, 76, 82, "#0f172a44", INK, 2.5, 6) + line([(x, 30), (x + 76, 30)], INK, 2)
        out += "".join(circle(x + 7 + i * 6, 24, 1.8, INK) for i in range(3))
        out += text(x + 38, 62, lab, 26, c) + rect(x + 18, 76, 40, 12, c, c, 0, 6)
        out += rect(x + 30, 136 - h * .6, 16, h * .6, c, c, 0, 2)
    return out + path("M152,92 l0,16 l4,-4 l3,7 l3,-1.5 l-3,-7 l5.5,0 z", INK, 1.5, fill=INK)


def art_adaptive_platform():
    out = line([(14, 76), (188, 76)], INK, 4)
    arms = ((30, 30, 150, ACC, False), (60, 52, 104, COOL, True), (40, 122, 128, COOL, True), (76, 100, 176, ACC, False), (118, 30, 184, HOT, False))
    for x, y, end, c, dead in arms:
        out += path(f"M{x},76 Q{x + 4},{y} {x + 22},{y} H{end}", c, 3)
        out += cross(end + 6, y, 6) if dead else circle(end, y, 5, c)
    return out + text(186, 92, "SHARED CONTROL", 10, DIM, "end") + text(118, 22, "NEW ARM", 10, HOT, "start")


def art_field_experiment():
    r = lcg(3)
    out = circle(170, 24, 12, ACC)
    for row in range(3):
        for col in range(5):
            x, y = 14 + col * 34 - row * 6, 54 + row * 28
            treated = r() < .5
            out += path(f"M{x + 6},{y} H{x + 34} L{x + 28},{y + 24} H{x} Z", ACC if treated else DIM, 2, fill="#0f172a22")
            out += "".join(line([(x + 10 + i * 7, y + 18), (x + 10 + i * 7, y + 10 - (5 if treated else 0))], "#86EFAC", 2) for i in range(3))
    return out


def art_ethnography():
    out = path("M10,128 L46,70 L82,128 Z", INK, 3, fill="#0f172a33") + path("M38,128 L46,108 L54,128", INK, 2.5)
    out += person(112, 104, 1.3) + person(140, 108, 1.1, DIM) + person(166, 104, 1.3, DIM)
    out += rect(120, 56, 32, 24, "#0f172a66", ACC, 2.5, 2) + line([(126, 64), (146, 64)], ACC, 2) + line([(126, 71), (140, 71)], ACC, 2)
    out += path("M10,128 H190", DIM, 2)
    return out + circle(176, 26, 10, "none", ACC, 2.5) + path("M162,26 h-6 M190,26 h6 M176,12 v-6", ACC, 2.5)


def art_grounded_theory():
    out = line([(10, 96), (190, 96)], INK, 3)
    out += path("M100,96 C100,70 92,58 82,46 M100,72 C110,60 122,54 134,52 M98,58 C96,46 100,36 106,28", "#86EFAC", 4)
    out += circle(82, 44, 7, "#86EFAC") + circle(136, 51, 7, "#86EFAC") + circle(107, 25, 8, ACC)
    out += path("M100,96 C96,112 84,122 66,132 M100,96 C104,114 122,124 140,134 M100,96 V140", DIM, 2.5)
    return out + scatter([(60, 134), (70, 116), (88, 138), (120, 116), (146, 132), (100, 128), (40, 120), (162, 118)], 3.5, ACC)


def art_interviews():
    out = person(40, 108, 2.0) + person(160, 108, 2.0, DIM)
    out += bubble(52, 22, 62, 34, INK, "#0f172a55", "left") + bubble(98, 50, 54, 28, ACC, "#0f172a55", "right")
    out += line([(62, 34), (102, 34)], INK, 2) + line([(62, 43), (90, 43)], INK, 2)
    return out + rect(24, 136, 34, 10, ACC, ACC, 0, 5) + rect(64, 136, 46, 10, COOL, COOL, 0, 5) + rect(116, 136, 28, 10, HOT, HOT, 0, 5)


def art_case_study():
    out = path("M74,112 V68 L92,56 V68 L110,56 V68 L128,56 V112 Z", INK, 3, fill="#0f172a44") + rect(132, 40, 10, 72, "none", INK, 2.5, 1)
    out += circle(102, 82, 46, "none", ACC, 3.5, dash="2 6")
    out += doc(16, 22, 22, 28, INK, 2) + bubble(162, 18, 28, 20, INK) + axes(16, 104, 30, 30, INK, 2)
    out += arrow(42, 40, 62, 56, DIM, 2) + arrow(162, 44, 146, 56, DIM, 2) + arrow(50, 118, 66, 108, DIM, 2)
    return out


def art_delphi():
    out = circle(100, 76, 14, ACC) + circle(100, 76, 26, "none", ACC, 2, dash="3 5") + circle(100, 76, 40, "none", DIM, 2, dash="3 6")
    for k in range(7):
        a = -math.pi / 2 + k * 2 * math.pi / 7
        out += person(100 + 64 * math.cos(a), 82 + 56 * math.sin(a), 0.8)
    return out + carrow(150, 26, 170, 60, 160, 92, INK, 2.5) + text(100, 81, "", 1)


def art_mixed_sequential():
    out = axes(14, 40, 60, 66, INK, 2.5) + "".join(rect(22 + k * 14, 106 - h, 10, h, ACC, ACC, 0, 1) for k, h in enumerate((20, 46, 30, 54)))
    out += arrow(84, 76, 116, 76, INK, 3.5)
    out += bubble(124, 34, 62, 36, INK, "#0f172a55") + line([(134, 46), (176, 46)], INK, 2) + line([(134, 56), (162, 56)], INK, 2)
    return out + person(150, 112, 1.2, DIM) + text(44, 132, "NUMBERS", 11, ACC) + text(156, 142, "STORIES", 11, INK)


def art_systematic_review():
    out = "".join(doc(12 + (k % 3) * 9, 22 + (k // 3) * 32, 22, 28, DIM, 2, sw=2) for k in range(9))
    out += path("M60,30 L82,30 L76,70 L66,70 Z", INK, 2.5) + arrow(71, 72, 71, 92, INK, 2.5)
    out += line([(132, 16), (132, 112)], DIM, 2, "3 3")
    for k, (c, lo, hi) in enumerate(((128, 104, 160), (140, 120, 162), (124, 98, 148), (136, 112, 170), (130, 116, 146))):
        y = 26 + k * 16
        out += line([(lo, y), (hi, y)], INK, 2.5) + rect(c - 4, y - 4, 8, 8, INK, INK, 0, 1)
    return out + path("M114,120 L132,112 L150,120 L132,128 Z", ACC, 2, fill=ACC)


def art_scoping_review():
    out = path("M18,28 L72,18 L128,28 L182,18 V124 L128,134 L72,124 L18,134 Z", INK, 3, fill="#0f172a33")
    out += line([(72, 18), (72, 124)], DIM, 2) + line([(128, 28), (128, 134)], DIM, 2)
    for x, y in ((40, 56), (56, 90), (96, 62), (108, 100), (88, 44)):
        out += path(f"M{x},{y} c-6,-8 -6,-16 0,-16 c6,0 6,8 0,16 z", ACC, 2, fill=ACC) + circle(x, y - 10, 2.5, "#0f172a")
    return out + path("M140,48 Q170,40 168,72 Q170,104 142,110 Q150,80 140,48 Z", INK, 2, dash="4 4") + text(156, 84, "?", 22, ACC)


def art_network_meta():
    pos = {"A": (40, 40), "B": (100, 24), "C": (160, 44), "D": (170, 108), "E": (100, 124), "F": (34, 104)}
    edges = [("A", "B", 6), ("B", "C", 2.5), ("A", "F", 4), ("F", "E", 2), ("E", "D", 5), ("C", "D", 3), ("B", "E", 2), ("A", "E", 2.5)]
    out = "".join(line([pos[a], pos[b]], DIM if w < 3 else INK, w) for a, b, w in edges)
    for k, (lab, (x, y)) in enumerate(pos.items()):
        out += node(x, y, lab, 13, "#0f172a", ACC if k == 4 else INK, size=13)
    return out


def art_umbrella_review():
    out = path("M30,66 Q100,-4 170,66 Q158,56 146,66 Q134,54 122,66 Q110,54 100,66 Q88,54 76,66 Q64,54 52,66 Q42,56 30,66 Z", ACC, 3, fill="#FCD34D33")
    out += line([(100, 30), (100, 116)], INK, 3) + path("M100,116 q0,10 -9,10 q-9,0 -9,-8", INK, 3)
    for k in range(4):
        out += doc(34 + k * 34, 82, 24, 30, INK, 2, fill="#0f172a55")
    return out + line([(100, 22), (100, 30)], INK, 3)


def art_rapid_review():
    out = circle(80, 82, 44, "none", INK, 4) + rect(72, 26, 16, 10, INK, INK, 0, 2) + line([(80, 82), (80, 50)], ACC, 4) + line([(80, 82), (104, 92)], INK, 3)
    out += "".join(line([(80 + 38 * math.cos(math.radians(a)), 82 + 38 * math.sin(math.radians(a))), (80 + 44 * math.cos(math.radians(a)), 82 + 44 * math.sin(math.radians(a)))], INK, 2) for a in range(0, 360, 30))
    out += doc(136, 42, 34, 44, INK, 3, fill="#0f172a55")
    return out + "".join(line([(132 - k * 4, 100 + k * 9), (180 - k * 4, 100 + k * 9)], ACC, 2.5) for k in range(3))


def art_realist_review():
    out = circle(62, 76, 46, "none", COOL, 3, dash="5 5") + gear(62, 76, 22, ACC, 10) + text(62, 138, "CONTEXT", 11, COOL)
    out += arrow(114, 76, 146, 76, INK, 3.5) + star(168, 76, 18, ACC)
    return out + text(62, 26, "MECHANISM", 10, ACC) + text(168, 108, "OUTCOME", 10, INK)


def art_prior_art():
    patent = doc(14, 16, 34, 44, INK, 3, "#0f172a55") + line([(37, 60), (34, 72)], ACC, 3) + line([(43, 60), (46, 72)], ACC, 3) + circle(40, 56, 7, ACC)
    books = "".join(rect(x, y, w, 11, "#0f172a55", INK, 2.5, 2) for x, y, w in ((16, 86, 42), (20, 99, 42), (12, 112, 50)))
    box = path("M72,108 L94,100 L116,108 L94,116 Z", INK, 2.5, fill="#0f172a33") + path("M72,108 V128 L94,136 L116,128 V108 M94,116 V136", INK, 2.5)
    bulb = circle(162, 56, 22, "#FCD34D33", ACC, 3) + rect(152, 77, 20, 11, "#0f172a", INK, 2.5, 2) + line([(155, 92), (169, 92)], INK, 2.5)
    return (patent + books + box + magnifier(84, 50, 18, INK) + carrow(108, 34, 122, 22, 136, 40, DIM, 2, "4 4", 6)
            + bulb + text(162, 65, "?", 24, ACC) + text(162, 120, "NEW?", 13, ACC))


def art_co_citation():
    out = ""
    for x in (24, 84, 144):
        out += doc(x, 98, 30, 36, DIM, 2, "#0f172a44", 2)
        out += arrow(x + 12, 96, 58, 58, DIM, 2, head=6) + arrow(x + 18, 96, 142, 58, DIM, 2, head=6)
    out += doc(40, 14, 32, 40, INK, 0, "#0f172a") + doc(128, 14, 32, 40, INK, 0, "#0f172a")
    out += text(56, 43, "A", 18, INK) + text(144, 43, "B", 18, INK)
    return out + line([(76, 34), (124, 34)], ACC, 6) + text(100, 26, "×3", 12, ACC)


def art_bibliographic_coupling():
    out = ""
    for k, x in enumerate((14, 60, 106, 152)):
        shared = k in (1, 2)
        out += doc(x, 12, 30, 34, ACC if shared else DIM, 2, "#FCD34D33" if shared else "#0f172a44", 2)
    for cx, refs in ((56, (0, 1, 2)), (144, (1, 2, 3))):
        for k in refs:
            out += arrow(cx + (k - 1.5) * 5, 94, 29 + k * 46, 50, DIM, 2, head=6)
    out += doc(40, 96, 32, 40, INK, 0, "#0f172a") + doc(128, 96, 32, 40, INK, 0, "#0f172a")
    out += text(56, 125, "A", 18, INK) + text(144, 125, "B", 18, INK)
    return out + line([(76, 116), (124, 116)], ACC, 6) + text(100, 138, "×2", 12, ACC)


def art_diagnostic_accuracy():
    out = rect(14, 40, 30, 80, "#0f172a55", INK, 2.5, 8) + rect(22, 54, 14, 30, "#ffffff22", INK, 2, 3)
    out += line([(22, 64), (36, 64)], HOT, 3) + line([(22, 74), (36, 74)], HOT, 3)
    out += rect(70, 22, 116, 104, "none", INK, 2.5, 4) + line([(128, 22), (128, 126)], INK, 2.5) + line([(70, 74), (186, 74)], INK, 2.5)
    return (out + check(99, 48, 13) + cross(157, 48, 9) + cross(99, 100, 9) + check(157, 100, 13)
            + text(99, 18, "+", 14, INK) + text(157, 18, "−", 14, INK))


def art_reliability():
    r = lcg(7)
    out = axes(18, 16, 170, 116) + line([(18, 74), (184, 74)], INK, 2) + line([(18, 46), (184, 46)], ACC, 2.5, "6 4") + line([(18, 102), (184, 102)], ACC, 2.5, "6 4")
    pts = [(30 + k * 5, 74 + (r() - .5) * 46) for k in range(30)]
    return out + scatter(pts, 3, INK) + text(184, 40, "+LIMIT", 10, ACC, "end") + text(184, 116, "−LIMIT", 10, ACC, "end")


def art_validation():
    out = rect(18, 26, 76, 106, "#0f172a55", INK, 3, 4) + rect(42, 18, 28, 12, INK, INK, 0, 3)
    for k in range(4):
        y = 46 + k * 20
        out += rect(28, y, 11, 11, "none", INK, 2, 2) + line([(46, y + 6), (84, y + 6)], DIM, 2)
        if k != 2:
            out += check(33.5, y + 5, 6, ACC, 2.5)
    out += circle(144, 78, 40, "none", INK, 3) + circle(144, 78, 26, "none", INK, 3) + circle(144, 78, 11, ACC)
    return out + arrow(186, 36, 150, 74, INK, 3)


def art_nomological():
    hub = (100, 76)
    spokes = [((34, 30), INK, 5, None, "+"), ((166, 30), INK, 3, None, "+"), ((32, 122), DIM, 2.5, "5 5", "0"), ((168, 122), HOT, 3, None, "−")]
    out = ""
    for (x, y), c, w, dash, lab in spokes:
        mx, my = (hub[0] + x) / 2, (hub[1] + y) / 2
        out += line([hub, (x, y)], c, w, dash) + circle(mx, my, 9, "#0f172a", c, 2) + text(mx, my + 5, lab, 14, c)
    for k, ((x, y), *_) in enumerate(spokes):
        out += node(x, y, "BCDE"[k], 13, "#0f172a", INK, size=13)
    return out + circle(*hub, 20, ACC, INK, 3) + text(100, 83, "M", 20, "#0f172a")


def art_interlab():
    out = flask(100, 76, 1.0)
    for k in range(5):
        a = -math.pi / 2 + k * 2 * math.pi / 5
        x, y = 100 + 70 * math.cos(a), 78 + 54 * math.sin(a)
        out += building(x - 15, y - 14, 30, 26, INK, "#0f172a66", 9)
        out += arrow(100 + 30 * math.cos(a), 78 + 26 * math.sin(a), 100 + 50 * math.cos(a), 78 + 38 * math.sin(a), DIM, 2, head=6)
    return out


def art_analytical_model():
    out = rect(12, 14, 176, 122, "#0f172a66", INK, 3, 4)
    out += text(30, 62, "dS ≥ 0", 32, INK, "start", 400, "serif")
    out += text(30, 108, "∑F = m·a", 30, ACC, "start", 400, "serif")
    return out + path("M138,52 Q152,24 166,52 T194,52", DIM, 2.5) + text(176, 128, "∎", 16, ACC, "end", 400, "serif")


def art_simulation():
    out = ""
    for k in range(9):
        y = 28 + k * 12
        out += path(" ".join(("M" if i == 0 else "L") + f"{_f(14 + i * 8.6)},{_f(y + 10 * math.sin(i * .5 + k * .35) * (k / 8))}" for i in range(21)), INK if k % 2 == 0 else DIM, 1.8)
    for i in range(0, 21, 2):
        out += path(" ".join(("M" if k == 0 else "L") + f"{_f(14 + i * 8.6)},{_f(28 + k * 12 + 10 * math.sin(i * .5 + k * .35) * (k / 8))}" for k in range(9)), DIM, 1.5)
    return out + circle(160, 60, 10, ACC) + circle(150, 92, 6, HOT) + circle(52, 46, 5, COOL)


def art_prediction_model():
    layers = [(28, (40, 76, 112)), (82, (28, 60, 92, 124)), (136, (52, 100)), (178, (76,))]
    out = ""
    for (x1, ys1), (x2, ys2) in zip(layers, layers[1:]):
        for y1 in ys1:
            for y2 in ys2:
                out += line([(x1, y1), (x2, y2)], FAINT, 1.6)
    for li, (x, ys) in enumerate(layers):
        for y in ys:
            out += circle(x, y, 8, ACC if li == 3 else ("#0f172a" if li else INK), INK, 2.5)
    return out + text(178, 104, "NEXT", 11, ACC)


def art_design_science():
    out = carrow(100, 20, 170, 24, 172, 88, INK, 3) + carrow(170, 104, 150, 140, 70, 132, INK, 3) + carrow(46, 118, 18, 70, 72, 26, INK, 3)
    out += gear(92, 78, 24, ACC, 9) + gear(124, 64, 14, INK, 7)
    return out + text(178, 62, "BUILD", 10, INK, "start") + text(110, 148, "TEST", 10, INK) + text(14, 54, "LEARN", 10, INK, "start")


def art_pilot():
    out = path("M24,96 L176,40 L92,110 Z", INK, 3, fill="#0f172a44") + path("M92,110 L104,76 L176,40", INK, 2.5) + path("M24,96 L104,76", DIM, 2)
    out += path("M18,120 Q60,132 90,122", ACC, 2.5, dash="5 5")
    return out + rect(130, 92, 50, 46, "#0f172a66", INK, 2.5, 3) + check(142, 104, 7, ACC, 2.5) + check(142, 122, 7, ACC, 2.5) + line([(152, 104), (172, 104)], DIM, 2) + line([(152, 122), (168, 122)], DIM, 2)


def art_benchmark():
    out = rect(76, 56, 48, 80, ACC, ACC, 0, 2) + rect(28, 80, 48, 56, INK, INK, 0, 2) + rect(124, 96, 48, 40, DIM, DIM, 0, 2)
    out += text(100, 104, "1", 32, "#0f172a") + text(52, 118, "2", 26, "#0f172a") + text(148, 124, "3", 22, "#0f172a")
    return out + star(100, 34, 14, ACC) + line([(14, 136), (186, 136)], INK, 3)


DESIGN_ART = {k.replace("art_", "").replace("_", "-"): v for k, v in dict(globals()).items() if k.startswith("art_")}
DESIGN_ART["ab-test"] = art_ab_test
DESIGN_ART["n-of-1"] = art_n_of_1
DESIGN_ART["interviews-thematic"] = art_interviews
