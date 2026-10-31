"""Art for the 74 Question cards (Q01-Q74).

Each picture shows the SUBJECT of the research scenario (a vape, a butterfly, a bridge in a storm...), never the study
design, so the art cannot give the answer away. Built from the primitives in art.py.
"""
from art import *
import math
from art import _f

DARK = "#0f172a"
SHADOW = "#0f172a55"
GREEN = "#86EFAC"


# --------------------------------------------------------------------------- local helpers
def _rot(a, x, y, inner):
    return f'<g transform="rotate({_f(a)} {_f(x)} {_f(y)})">{inner}</g>'


def _ellipse(x, y, rx, ry, fill="none", c=INK, w=2.5, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(rx)}" ry="{_f(ry)}" fill="{fill}" stroke="{c}" '
            f'stroke-width="{w}" opacity="{o}"{da}/>')


def _cloud(x, y, w, c=INK, fill="none", sw=2.5, o=1):
    """Cloud whose flat base is centred at (x, y), width w."""
    d = (f"M{_f(x - w * .5)},{_f(y)} A{_f(w * .17)},{_f(w * .17)} 0 0 1 {_f(x - w * .3)},{_f(y - w * .22)} "
         f"A{_f(w * .23)},{_f(w * .23)} 0 0 1 {_f(x + w * .14)},{_f(y - w * .3)} "
         f"A{_f(w * .2)},{_f(w * .2)} 0 0 1 {_f(x + w * .5)},{_f(y)} Z")
    return path(d, c, sw, fill=fill, o=o)


def _heart(x, y, s=1.0, c=HOT, fill=None, sw=3):
    d = (f"M{_f(x)},{_f(y + 16 * s)} C{_f(x - 24 * s)},{_f(y + 2 * s)} {_f(x - 14 * s)},{_f(y - 16 * s)} {_f(x)},{_f(y - 5 * s)} "
         f"C{_f(x + 14 * s)},{_f(y - 16 * s)} {_f(x + 24 * s)},{_f(y + 2 * s)} {_f(x)},{_f(y + 16 * s)} Z")
    return path(d, c, sw, fill=fill or "none")


def _kidney(x, y, s=1.0, c=HOT, fill="#FB718533"):
    d = (f"M{_f(x - 2 * s)},{_f(y - 18 * s)} C{_f(x + 18 * s)},{_f(y - 21 * s)} {_f(x + 20 * s)},{_f(y + 21 * s)} {_f(x - 2 * s)},{_f(y + 18 * s)} "
         f"C{_f(x - 15 * s)},{_f(y + 16 * s)} {_f(x - 13 * s)},{_f(y + 5 * s)} {_f(x - 6 * s)},{_f(y)} "
         f"C{_f(x - 13 * s)},{_f(y - 5 * s)} {_f(x - 15 * s)},{_f(y - 16 * s)} {_f(x - 2 * s)},{_f(y - 18 * s)} Z")
    return path(d, c, 3, fill=fill) + path(f"M{_f(x - 6 * s)},{_f(y)} H{_f(x - 16 * s)}", c, 2.5)


def _liver(x, y, s=1.0, c=HOT, fill="#FB718533"):
    d = (f"M{_f(x - 32 * s)},{_f(y - 8 * s)} Q{_f(x - 12 * s)},{_f(y - 24 * s)} {_f(x + 26 * s)},{_f(y - 16 * s)} "
         f"Q{_f(x + 36 * s)},{_f(y - 12 * s)} {_f(x + 22 * s)},{_f(y + 2 * s)} Q{_f(x - 2 * s)},{_f(y + 22 * s)} {_f(x - 20 * s)},{_f(y + 12 * s)} "
         f"Q{_f(x - 36 * s)},{_f(y + 4 * s)} {_f(x - 32 * s)},{_f(y - 8 * s)} Z")
    return path(d, c, 3, fill=fill) + path(f"M{_f(x - 4 * s)},{_f(y - 18 * s)} Q{_f(x - 2 * s)},{_f(y - 4 * s)} {_f(x + 4 * s)},{_f(y + 8 * s)}", c, 2, o=.7)


def _brain(x, y, rx=34, ry=26, c=INK, fill=SHADOW):
    pts = []
    for k in range(73):
        t = k / 72 * 2 * math.pi
        r = 1 + 0.07 * abs(math.sin(5 * t))
        pts.append((x + rx * r * math.cos(t), y + ry * r * math.sin(t)))
    out = line(pts, c, 3, fill=fill, close=True)
    out += path(f"M{_f(x)},{_f(y - ry)} q-6,8 0,14 q6,8 0,14 q-6,8 0,{_f(ry * 2 - 28)}", c, 2.2, o=.8)
    out += path(f"M{_f(x - rx * .7)},{_f(y - 4)} q8,-8 16,0 M{_f(x + rx * .25)},{_f(y + 8)} q8,-8 16,0 "
                f"M{_f(x - rx * .6)},{_f(y + 12)} q6,6 14,2 M{_f(x + rx * .2)},{_f(y - 12)} q8,6 16,-2", c, 2, o=.7)
    return out


def _lungs(x, y, s=1.0, c=INK, fill=SHADOW):
    out = line([(x, y - 28 * s), (x, y - 6 * s)], c, 3)
    out += path(f"M{_f(x)},{_f(y - 6 * s)} L{_f(x - 8 * s)},{_f(y + 2 * s)} M{_f(x)},{_f(y - 6 * s)} L{_f(x + 8 * s)},{_f(y + 2 * s)}", c, 2.5)
    for sg in (-1, 1):
        d = (f"M{_f(x + sg * 5 * s)},{_f(y - 14 * s)} C{_f(x + sg * 20 * s)},{_f(y - 26 * s)} {_f(x + sg * 32 * s)},{_f(y + 6 * s)} "
             f"{_f(x + sg * 30 * s)},{_f(y + 24 * s)} Q{_f(x + sg * 18 * s)},{_f(y + 30 * s)} {_f(x + sg * 7 * s)},{_f(y + 22 * s)} "
             f"Q{_f(x + sg * 4 * s)},{_f(y + 6 * s)} {_f(x + sg * 5 * s)},{_f(y - 14 * s)} Z")
        out += path(d, c, 3, fill=fill)
    return out


def _virus(x, y, r=14, c=HOT, fill="#FB718533", spikes=10):
    out = ""
    for k in range(spikes):
        a = k * 2 * math.pi / spikes
        out += line([(x + r * math.cos(a), y + r * math.sin(a)), (x + (r + 6) * math.cos(a), y + (r + 6) * math.sin(a))], c, 2.2)
        out += circle(x + (r + 7) * math.cos(a), y + (r + 7) * math.sin(a), 2.6, c)
    return out + circle(x, y, r, fill, c, 2.8) + circle(x - r * .3, y - r * .2, r * .18, c) + circle(x + r * .3, y + r * .3, r * .14, c)


def _bacterium(x, y, w=40, h=16, rot=0, c=HOT, fill="#FB718533"):
    inner = (rect(x - w / 2, y - h / 2, w, h, fill, c, 2.5, h / 2)
             + path(f"M{_f(x + w / 2)},{_f(y)} q6,-6 12,0 t12,0", c, 2) + circle(x - w * .15, y, 2, c) + circle(x + w * .15, y, 2, c))
    return _rot(rot, x, y, inner)


def _phone(x, y, w=44, h=80, c=INK, fill=SHADOW):
    return (rect(x, y, w, h, fill, c, 3, 7) + line([(x + w / 2 - 6, y + 6), (x + w / 2 + 6, y + 6)], c, 2)
            + circle(x + w / 2, y + h - 7, 2.6, c))


def _laptop(x, y, w=96, h=60, c=INK, fill=SHADOW):
    return (rect(x, y, w, h, fill, c, 3, 4)
            + path(f"M{_f(x - 10)},{_f(y + h + 4)} H{_f(x + w + 10)} L{_f(x + w + 4)},{_f(y + h + 12)} H{_f(x - 4)} Z", c, 3, fill=fill)
            + line([(x + w / 2 - 10, y + h + 8), (x + w / 2 + 10, y + h + 8)], c, 2))


def _house(x, y, w=40, h=34, c=INK, fill=SHADOW, door=True):
    out = path(f"M{_f(x)},{_f(y + h)} V{_f(y + h * .42)} L{_f(x + w / 2)},{_f(y)} L{_f(x + w)},{_f(y + h * .42)} V{_f(y + h)} Z", c, 2.5, fill=fill)
    if door:
        out += rect(x + w / 2 - w * .12, y + h - h * .38, w * .24, h * .38, "none", c, 2, 1)
    return out


def _mountain(x0, x1, base, peak_x, peak_y, c=INK, fill=SHADOW, snow=True):
    out = path(f"M{_f(x0)},{_f(base)} L{_f(peak_x)},{_f(peak_y)} L{_f(x1)},{_f(base)} Z", c, 3, fill=fill)
    if snow:
        lx = peak_x - (peak_x - x0) * .28
        rx = peak_x + (x1 - peak_x) * .28
        sy = peak_y + (base - peak_y) * .28
        out += path(f"M{_f(peak_x)},{_f(peak_y)} L{_f(lx)},{_f(sy)} L{_f(lx + 7)},{_f(sy - 4)} L{_f(peak_x - 2)},{_f(sy + 3)} "
                    f"L{_f(rx - 7)},{_f(sy - 4)} L{_f(rx)},{_f(sy)} Z", INK, 1.5, fill=INK)
    return out


def _snowflake(x, y, r=12, c=COOL, w=2.5):
    out = ""
    for k in range(6):
        a = k * math.pi / 3
        ex, ey = x + r * math.cos(a), y + r * math.sin(a)
        out += line([(x, y), (ex, ey)], c, w)
        mx, my = x + r * .6 * math.cos(a), y + r * .6 * math.sin(a)
        for d in (-.6, .6):
            out += line([(mx, my), (mx + r * .3 * math.cos(a + d), my + r * .3 * math.sin(a + d))], c, w * .8)
    return out


def _flame(x, y, s=1.0):
    outer = (f"M{_f(x)},{_f(y + 22 * s)} C{_f(x - 22 * s)},{_f(y + 20 * s)} {_f(x - 18 * s)},{_f(y - 6 * s)} {_f(x - 4 * s)},{_f(y - 26 * s)} "
             f"C{_f(x - 2 * s)},{_f(y - 12 * s)} {_f(x + 6 * s)},{_f(y - 10 * s)} {_f(x + 8 * s)},{_f(y - 18 * s)} "
             f"C{_f(x + 22 * s)},{_f(y - 2 * s)} {_f(x + 20 * s)},{_f(y + 20 * s)} {_f(x)},{_f(y + 22 * s)} Z")
    inner = (f"M{_f(x)},{_f(y + 18 * s)} C{_f(x - 10 * s)},{_f(y + 16 * s)} {_f(x - 8 * s)},{_f(y + 2 * s)} {_f(x)},{_f(y - 6 * s)} "
             f"C{_f(x + 8 * s)},{_f(y + 2 * s)} {_f(x + 10 * s)},{_f(y + 16 * s)} {_f(x)},{_f(y + 18 * s)} Z")
    return path(outer, HOT, 2.5, fill="#FB718566") + path(inner, ACC, 2, fill=ACC)


def _butterfly(x, y, s=1.0, c=ACC, o=1, rot=-15):
    inner = (path(f"M{_f(x)},{_f(y)} C{_f(x - 6 * s)},{_f(y - 22 * s)} {_f(x - 26 * s)},{_f(y - 20 * s)} {_f(x - 20 * s)},{_f(y - 4 * s)} "
                  f"C{_f(x - 26 * s)},{_f(y + 6 * s)} {_f(x - 10 * s)},{_f(y + 18 * s)} {_f(x)},{_f(y + 2 * s)}", c, 2, fill=c, o=o)
             + path(f"M{_f(x)},{_f(y)} C{_f(x + 6 * s)},{_f(y - 22 * s)} {_f(x + 26 * s)},{_f(y - 20 * s)} {_f(x + 20 * s)},{_f(y - 4 * s)} "
                    f"C{_f(x + 26 * s)},{_f(y + 6 * s)} {_f(x + 10 * s)},{_f(y + 18 * s)} {_f(x)},{_f(y + 2 * s)}", c, 2, fill=c, o=o)
             + line([(x, y - 8 * s), (x, y + 10 * s)], DARK, 3 * s, o=o)
             + path(f"M{_f(x)},{_f(y - 8 * s)} l-5,-7 M{_f(x)},{_f(y - 8 * s)} l5,-7", DARK, 1.5, o=o))
    return _rot(rot, x, y, inner)


def _bars(x, y, n_on, c_on=ACC, n=4):
    out = ""
    for k in range(n):
        h = 6 + k * 5
        on = k < n_on
        out += rect(x + k * 7, y - h, 5, h, c_on if on else "none", c_on if on else DIM, 1.5, 1)
    return out


def _skyline(y=136, c=DIM, fill="#0f172a33"):
    out = ""
    for x, w, h in ((10, 18, 34), (30, 14, 52), (46, 22, 26), (70, 16, 44), (88, 26, 30), (116, 14, 58),
                    (132, 20, 36), (154, 16, 48), (172, 18, 28)):
        out += rect(x, y - h, w, h, fill, c, 2, 1)
    return out + line([(6, y), (194, y)], c, 2)


def _ruler_ticks(x0, y, x1, step=8, c=INK):
    return "".join(line([(x, y), (x, y - (8 if i % 2 == 0 else 4))], c, 1.8) for i, x in enumerate(range(int(x0), int(x1), step)))


# --------------------------------------------------------------------------- DESCRIBE
def q01():  # City vape count
    out = _skyline()
    body = rect(36, 92, 64, 16, SHADOW, INK, 3, 5) + rect(100, 95, 16, 10, INK, INK, 0, 3) + circle(52, 100, 3.5, ACC)
    out += _rot(-28, 76, 100, body)
    for x, y, r, o in ((118, 74, 7, .35), (130, 62, 10, .3), (146, 50, 13, .25), (162, 38, 16, .2)):
        out += circle(x, y, r, INK, o=o)
    return out + _cloud(160, 52, 52, INK, "#ffffff22", 2.5)


def q02():  # Tattoo rash
    arm = path("M8,92 Q60,80 120,84 Q150,86 176,96 L176,128 Q150,122 120,122 Q60,124 8,132 Z", INK, 3, fill=SHADOW)
    out = arm + star(70, 104, 11, ACC)
    r = lcg(2)
    for _ in range(14):
        a, d = r() * 6.28, 16 + r() * 14
        out += circle(70 + d * math.cos(a) * 1.5, 104 + d * math.sin(a) * .5, 2 + r() * 1.6, HOT)
    gun = (rect(100, 50, 52, 16, SHADOW, INK, 3, 4) + rect(152, 53, 18, 10, INK, INK, 0, 3) + rect(86, 54, 14, 8, "none", INK, 2.5, 2)
           + line([(86, 58), (74, 58)], INK, 2) + circle(124, 46, 5, "none", INK, 2.5))
    return out + _rot(-40, 120, 58, gun)


def q03():  # Vanishing butterflies
    out = path("M12,128 Q60,120 90,88 T186,24", DIM, 2.5, dash="2 7")
    for x, y, s, o in ((40, 116, 1.15, 1), (88, 86, .95, .8), (134, 56, .75, .55), (172, 32, .55, .3)):
        out += _butterfly(x, y, s, ACC, o)
    return out + path("M14,140 q10,-14 20,0 q10,-14 20,0", GREEN, 2.5)


def q04():  # Jupiter census
    out = "".join(circle(x, y, 1.6, INK, o=.6) for x, y in ((20, 20), (60, 14), (110, 22), (178, 16), (30, 130), (150, 136), (186, 120), (96, 140)))
    out += _ellipse(100, 78, 84, 30, "none", DIM, 2, dash="4 5")
    for k in range(12):
        a = k * math.pi / 6
        out += line([(58 + 24 * math.cos(a), 78 + 24 * math.sin(a)), (58 + 32 * math.cos(a), 78 + 32 * math.sin(a))], ACC, 2.5)
    out += circle(58, 78, 18, ACC)
    planet = circle(150, 62, 17, "#f3c9a0", INK, 2.5)
    planet += path("M134,56 Q150,60 166,56 M133,66 Q150,70 167,66", "#b45309", 2.5, o=.8)
    ring_back = path("M122,66 A30,8 0 0 1 178,58", INK, 2.5)
    ring_front = path("M122,66 A30,8 0 0 0 178,58", INK, 3)
    return out + _rot(-12, 150, 62, ring_back + planet + ring_front)


def q05():  # After approval
    out = rect(26, 46, 52, 78, SHADOW, INK, 3, 6) + rect(22, 30, 60, 16, INK, INK, 0, 3)
    out += rect(32, 66, 40, 34, "#ffffff22", INK, 2, 2) + line([(38, 76), (66, 76)], INK, 2) + line([(38, 86), (58, 86)], INK, 2)
    out += pill(98, 126, 26, 11, 20) + pill(70, 138, 26, 11, -10, INK, COOL)
    return out + _liver(144, 72, 1.2) + text(150, 80, "!", 26, INK)


# --------------------------------------------------------------------------- ASSOCIATE
def q06():  # Smog atlas
    out = globe(128, 72, 36)
    out += path("M14,132 V96 L28,104 V92 L42,100 V84 H50 V60 H58 V84 H64 V52 H72 V132 Z", INK, 2.5, fill=SHADOW)
    out += path("M54,56 q-4,-10 4,-16 q10,-6 6,-16 M68,48 q-4,-10 4,-16", DIM, 3)
    out += _cloud(120, 60, 74, DIM, "rgba(148,163,184,.55)", 2.5) + _cloud(150, 98, 54, DIM, "rgba(148,163,184,.5)", 2.5)
    return out + line([(6, 132), (194, 132)], DIM, 2)


def q07():  # Rare cancer, common spray
    bottle = (path("M26,132 V82 Q26,72 36,70 H56 Q66,72 66,82 V132 Z", INK, 3, fill=SHADOW) + rect(38, 58, 16, 12, INK, INK, 0, 2)
              + path("M32,44 H70 L78,52 H70 L66,58 H34 Z", ACC, 2.5, fill=ACC) + path("M36,58 L30,76", ACC, 3)
              + line([(34, 98), (58, 98)], DIM, 2) + line([(34, 108), (52, 108)], DIM, 2))
    out = bottle
    r = lcg(5)
    for _ in range(18):
        t = r()
        out += circle(84 + t * 40, 50 + (r() - .5) * t * 34, 1.6 + r() * 1.2, ACC, o=.8 - t * .4)
    out += path("M118,132 Q120,108 116,92 M116,108 Q104,100 98,104 M117,100 Q128,90 136,94", GREEN, 3)
    return out + person(160, 106, 1.6) + line([(10, 132), (190, 132)], DIM, 2)


def q08():  # Clean-room workers
    worker = (path("M18,128 V96 Q18,76 40,76 Q62,76 62,96 V128 Z", INK, 3, fill=SHADOW)
              + path("M26,70 Q26,40 40,40 Q54,40 54,70 Z", INK, 3, fill=SHADOW) + rect(30, 50, 20, 10, COOL, COOL, 0, 4))
    chip = rect(82, 46, 40, 40, SHADOW, ACC, 3, 3) + rect(92, 56, 20, 20, ACC, ACC, 0, 2)
    for k in range(4):
        p = 52 + k * 9
        chip += line([(p, 46), (p, 38)], ACC, 2) + line([(p, 86), (p, 94)], ACC, 2)
        chip += line([(82, p), (74, p)], ACC, 2) + line([(122, p), (130, p)], ACC, 2)
    drop = path("M102,104 C94,116 94,124 102,126 C110,124 110,116 102,104 Z", COOL, 2.5, fill="#7DD3FC55")
    return worker + chip + drop + _kidney(162, 92, 1.3)


def q09():  # Snow shovel
    out = path("M10,134 Q50,108 96,118 Q140,108 190,134 Z", INK, 2.5, fill="#ffffffcc")
    out += line([(40, 30), (96, 104)], INK, 4) + line([(34, 26), (46, 34)], INK, 4)
    out += path("M80,104 L112,96 L118,118 L94,126 Z", INK, 3, fill=SHADOW)
    out += _snowflake(22, 70, 7, INK, 2) + _snowflake(76, 24, 6, INK, 2) + _snowflake(112, 52, 5, INK, 2)
    return out + _heart(156, 60, 1.6, HOT, "#FB718544") + bolt(156, 62, .9, ACC)


def q10():  # Diet and dementia
    out = _brain(62, 70, 44, 34)
    burger = (path("M126,42 Q126,22 152,22 Q178,22 178,42 Z", ACC, 2.5, fill=ACC) + rect(122, 44, 60, 6, GREEN, GREEN, 0, 3)
              + rect(124, 51, 56, 9, "#92400e", INK, 2, 4) + path("M126,62 H178 Q178,72 168,72 H136 Q126,72 126,62 Z", ACC, 2.5, fill=ACC))
    out += burger + "".join(circle(140 + k * 8, 30 + (k % 2) * 4, 1.4, DARK) for k in range(4))
    fries = ""
    for k in range(6):
        fries += rect(134 + k * 6, 90 - (k % 3) * 5, 4, 26, ACC, ACC, 0, 1)
    return out + fries + path("M128,138 L134,108 H170 L176,138 Z", HOT, 2.5, fill=HOT)


# --------------------------------------------------------------------------- CAUSE
def q11():  # New pill vs. old
    out = circle(66, 66, 40, SHADOW, INK, 3) + circle(66, 66, 32, "none", DIM, 2)
    for k in range(9):
        a = math.radians(150 + k * 30)
        out += line([(66 + 26 * math.cos(a), 66 + 26 * math.sin(a)), (66 + 32 * math.cos(a), 66 + 32 * math.sin(a))], INK, 2)
    out += line([(66, 66), (88, 46)], HOT, 3.5) + circle(66, 66, 4, INK)
    out += path("M66,106 Q66,130 96,132 Q120,132 120,118", DIM, 3) + _ellipse(126, 112, 10, 14, INK, INK, 2)
    return out + pill(158, 50, 44, 18, -30) + pill(160, 98, 36, 15, 20, DIM, "rgba(248,250,252,.6)")


def q12():  # Peer tutoring
    out = person(40, 96, 1.7) + person(160, 96, 1.7, ACC)
    out += line([(18, 120), (182, 120)], INK, 3) + line([(30, 120), (30, 140)], INK, 3) + line([(170, 120), (170, 140)], INK, 3)
    out += path("M100,118 L74,110 V92 L100,100 L126,92 V110 Z", INK, 2.5, fill=SHADOW) + line([(100, 100), (100, 118)], INK, 2)
    for x, y, s in ((84, 40, "+"), (104, 34, "×"), (124, 44, "÷"), (100, 62, "="), (72, 66, "2"), (132, 70, "3")):
        out += text(x, y + 6, s, 18, ACC if s in "+×÷=" else INK)
    return out


def q13():  # Soda tax
    bottle = path("M56,26 H72 V40 Q86,52 86,70 V126 Q86,134 78,134 H50 Q42,134 42,126 V70 Q42,52 56,40 Z", INK, 3, fill=SHADOW)
    bottle += path("M43,84 H85 V108 H43 Z", HOT, 0, fill="#FB718599") + rect(54, 18, 20, 8, INK, INK, 0, 2)
    bottle += "".join(circle(x, y, 2, INK, o=.6) for x, y in ((56, 70), (70, 62), (62, 120), (74, 116)))
    tag = path("M118,44 L176,44 L176,96 L118,96 L104,70 Z", ACC, 3, fill="#FCD34D33") + circle(116, 70, 4, "none", ACC, 2)
    tag += text(146, 80, "TAX", 22, ACC)
    return bottle + path("M72,34 Q100,40 112,70", DIM, 2) + tag + text(146, 118, "$", 26, INK)


def q14():  # Scholarship cutoff
    cap = path("M100,22 L162,44 L100,66 L38,44 Z", INK, 3, fill=DARK) + path("M70,56 V74 Q100,88 130,74 V56", INK, 3, fill=SHADOW)
    cap += path("M100,44 L148,52 V80", ACC, 2.5) + rect(144, 80, 8, 12, ACC, ACC, 0, 2)
    scroll = _rot(-8, 100, 116, rect(46, 104, 108, 22, "#ffffffdd", INK, 2.5, 10) + rect(94, 100, 12, 30, HOT, HOT, 0, 2))
    return cap + scroll + circle(100, 44, 3, ACC)


def q15():  # Sepsis alert
    out = rect(46, 22, 108, 74, SHADOW, INK, 3, 5) + rect(92, 96, 16, 14, INK, INK, 0, 0) + rect(72, 110, 56, 6, INK, INK, 0, 3)
    bell = path("M100,36 Q84,36 84,56 V68 L78,76 H122 L116,68 V56 Q116,36 100,36 Z", ACC, 2.5, fill=ACC) + circle(100, 80, 4, ACC)
    out += bell + path("M72,44 q-6,10 0,20 M128,44 q6,10 0,20 M64,40 q-8,14 0,28 M136,40 q8,14 0,28", ACC, 2.5)
    return out + _bacterium(30, 128, 34, 13, -20) + _bacterium(166, 124, 34, 13, 25) + _bacterium(176, 30, 26, 11, 60)


def q16():  # Reunification
    out = rect(26, 46, 128, 14, SHADOW, INK, 3, 1) + path("M34,46 L90,30 L146,46", INK, 3)
    out += rect(78, 16, 24, 14, ACC, ACC, 0, 2)
    for k in range(6):
        out += rect(32 + k * 22, 60, 10, 64, SHADOW, INK, 2.5, 1)
    out += line([(14, 126), (166, 126)], INK, 3)
    coin = circle(166, 96, 20, ACC, INK, 0) + circle(166, 96, 15, "none", DARK, 2) + text(166, 102, "DM", 15, DARK)
    return out + coin


def q17():  # Her migraine
    head = path("M40,140 V118 Q30,110 34,92 Q24,84 30,70 Q34,40 64,32 Q100,26 112,56 Q118,72 108,86 L116,98 L106,102 Q108,118 92,118 L88,140",
                INK, 3, fill=SHADOW)
    head += path("M34,92 Q20,70 40,44 Q60,24 90,32", ACC, 5)
    zig = line([(70, 46), (80, 58), (72, 64), (86, 76), (78, 82), (92, 92)], HOT, 4)
    return head + zig + circle(64, 36, 0.1, INK) + pill(160, 64, 40, 17, -35) + star(150, 112, 7, ACC) + star(178, 30, 5, DIM)


def q18():  # Two inhalers
    out = _lungs(100, 78, 1.5)

    def inhaler(x, c):
        return (rect(x, 30, 18, 52, c, c, 0, 4) + path(f"M{x - 4},82 H{x + 22} V112 H{x + 34} V128 H{x - 4} Z", INK, 3, fill=SHADOW))
    return out + inhaler(14, ACC) + _rot(0, 0, 0, path("M186,82 H160 V112 H148 V128 H186 Z", INK, 3, fill=SHADOW) + rect(164, 30, 18, 52, COOL, COOL, 0, 4))


def q19():  # Three knobs (farm)
    out = circle(170, 26, 12, ACC)
    for k in range(6):
        out += line([(100 + (k - 2.5) * 14, 72), (100 + (k - 2.5) * 40, 140)], GREEN if k % 2 else "#a3e635", 3, o=.8)
    out += path("M10,72 H190", INK, 2.5) + path("M10,140 H190", DIM, 2)
    can = path("M18,48 H54 V68 H18 Z", INK, 3, fill=SHADOW) + path("M54,52 L76,38", INK, 3) + path("M24,48 Q36,30 48,48", INK, 2.5)
    can += "".join(line([(80 + k * 4, 38 + k * 6), (82 + k * 4, 44 + k * 6)], COOL, 2) for k in range(3))
    sack = path("M120,66 L124,34 Q138,26 152,34 L156,66 Z", INK, 3, fill="#ffffff22") + line([(124, 38), (152, 38)], INK, 2)
    sack += "".join(circle(130 + k * 8, 52, 2.4, ACC) for k in range(3))
    wheat = path("M98,70 V22", ACC, 2.5) + "".join(_ellipse(98 + sg * 5, 28 + k * 9, 3, 6, ACC, ACC, 0) for k in range(4) for sg in (-1, 1))
    return out + can + sack + wheat


def q20():  # Weld strength
    plates = (path("M14,112 L96,104 L96,118 L14,128 Z", INK, 2.5, fill=SHADOW) + path("M104,104 L186,112 L186,128 L104,118 Z", INK, 2.5, fill=SHADOW))
    plates += line([(96, 104), (104, 104)], ACC, 4) + line([(96, 118), (104, 118)], ACC, 2)
    torch = _rot(38, 136, 54, rect(108, 46, 70, 16, SHADOW, INK, 3, 4) + rect(178, 49, 18, 10, INK, INK, 0, 2) + rect(92, 49, 16, 10, INK, INK, 0, 2))
    burst = ""
    for k in range(12):
        a = math.radians(k * 30 + 8)
        burst += line([(100 + 9 * math.cos(a), 96 + 9 * math.sin(a)), (100 + (24 + (k % 3) * 6) * math.cos(a), 96 + (24 + (k % 3) * 6) * math.sin(a))], ACC if k % 2 else INK, 2.5)
    return plates + burst + circle(100, 96, 7, "#fff") + circle(100, 96, 11, "none", ACC, 2.5) + torch


def q21():  # Checkout button
    out = rect(16, 14, 168, 120, SHADOW, INK, 3, 6) + line([(16, 28), (184, 28)], INK, 2)
    out += "".join(circle(24 + k * 7, 21, 2, INK) for k in range(3)) + rect(70, 18, 100, 6, "none", DIM, 1.5, 3)
    cart = path("M34,46 H44 L52,78 H82 L90,54 H48", INK, 3) + circle(56, 86, 4, INK) + circle(78, 86, 4, INK)
    cart += rect(58, 44, 12, 12, ACC, ACC, 0, 2) + rect(70, 48, 10, 8, COOL, COOL, 0, 2)
    out += cart + line([(104, 50), (166, 50)], INK, 3) + line([(104, 62), (150, 62)], DIM, 2.5) + line([(104, 72), (140, 72)], DIM, 2.5)
    out += rect(100, 92, 70, 26, ACC, ACC, 0, 13) + text(135, 111, "BUY", 18, DARK)
    return out + path("M150,104 l0,26 l6,-6 l5,11 l5,-2.4 l-5,-11 l8.5,0 z", INK, 1.5, fill=INK) + path("M150,104 l0,26 l6,-6 l5,11 l5,-2.4 l-5,-11 l8.5,0 z", DARK, 1.2)


def q22():  # Rat-free islands
    out = path("M20,108 Q50,70 96,66 Q150,64 176,108 Z", INK, 3, fill=SHADOW)
    out += path("M8,116 q12,-8 24,0 t24,0 t24,0 t24,0 t24,0 t24,0 t24,0 t24,0", COOL, 2.5) + path("M14,132 q12,-8 24,0 t24,0 t24,0 t24,0 t24,0 t24,0 t24,0", COOL, 2, o=.6)
    out += path("M60,82 Q76,92 92,82", INK, 3) + _ellipse(70, 79, 5, 4, INK, INK, 0) + _ellipse(80, 79, 5, 4, ACC, ACC, 0)
    out += path("M30,34 q10,-10 20,0 q10,-10 20,0", INK, 3) + path("M120,22 q7,-7 14,0 q7,-7 14,0", INK, 2.5)
    rat = _ellipse(138, 82, 15, 9, DIM, DIM, 0) + circle(152, 77, 6, DIM) + circle(149, 71, 3, DIM) + path("M123,84 Q108,92 112,76", DIM, 2)
    return out + rat + cross(140, 80, 14, HOT, 4)


def q23():  # Triage rollout
    amb = rect(14, 56, 90, 50, "#ffffffdd", INK, 3, 4) + path("M104,68 H130 L146,88 V106 H104 Z", INK, 3, fill="#ffffffdd")
    amb += path("M110,72 H128 L138,86 H110 Z", COOL, 0, fill=COOL)
    amb += rect(52, 66, 10, 30, HOT, HOT, 0, 1) + rect(42, 76, 30, 10, HOT, HOT, 0, 1)
    amb += rect(30, 46, 20, 10, HOT, HOT, 0, 3) + path("M28,40 l-6,-6 M40,38 v-8 M52,40 l6,-6", HOT, 2.5)
    amb += circle(38, 108, 10, DARK, INK, 3) + circle(124, 108, 10, DARK, INK, 3)
    tag = path("M156,40 H186 V120 H156 Z", INK, 2.5, fill="#ffffff22") + circle(171, 48, 4, "none", INK, 2)
    tag += rect(156, 62, 30, 14, HOT, HOT, 0, 0) + rect(156, 80, 30, 14, ACC, ACC, 0, 0) + rect(156, 98, 30, 14, GREEN, GREEN, 0, 0)
    return amb + tag + path("M171,44 Q160,26 146,34", INK, 2) + line([(6, 118), (150, 118)], DIM, 2)


def q24():  # Ten candidates
    out = _virus(100, 76, 22)
    cols = [(INK, ACC), (INK, COOL), (INK, HOT), (ACC, COOL), (INK, GREEN)]
    for k in range(10):
        a = -math.pi / 2 + k * 2 * math.pi / 10
        c1, c2 = cols[k % 5]
        out += pill(100 + 78 * math.cos(a), 76 + 56 * math.sin(a), 24, 10, math.degrees(a) + 90, c1, c2)
    return out


def q25():  # Older than the trials
    elder = person(46, 98, 2.0)
    elder += line([(66, 94), (72, 134)], ACC, 3.5) + path("M60,94 Q66,86 72,94", ACC, 3.5)
    cards = ""
    for k in range(3):
        cards += rect(96 + k * 6, 30 + k * 8, 56, 34, "#0f172a99", INK, 2.5, 4)
    cards += rect(108, 54, 56, 6, ACC, ACC, 0, 0) + line([(116, 70), (140, 70)], DIM, 2)
    return elder + cards + _kidney(150, 110, 1.05) + line([(14, 136), (90, 136)], DIM, 2)


def q26():  # Does school pay?
    school = path("M14,132 V76 L58,50 L102,76 V132 Z", INK, 3, fill=SHADOW) + rect(50, 30, 16, 20, "none", INK, 2.5, 1)
    school += path("M58,30 V18", INK, 2.5) + path("M58,18 h12 l-3,4 l3,4 h-12", ACC, 2, fill=ACC) + circle(58, 40, 3, ACC)
    school += rect(48, 106, 20, 26, "none", INK, 2.5, 1) + rect(24, 86, 14, 12, "none", INK, 2, 1) + rect(78, 86, 14, 12, "none", INK, 2, 1)
    notes = ""
    for k, (dx, a) in enumerate(((0, -14), (8, -4), (16, 8))):
        notes += _rot(a, 150 + dx, 82, rect(124 + dx, 64, 56, 32, "#bbf7d0" if k == 2 else "#86efac88", INK, 2.5, 3)
                      + circle(152 + dx, 80, 8, "none", DARK, 2) + text(152 + dx, 85, "$", 13, DARK))
    return school + notes + "".join(circle(130 + k * 14, 126, 6, ACC, DARK, 1.5) for k in range(4))


def q27():  # LDL: cause or marker?
    out = path("M10,46 Q100,30 190,46", INK, 3.5) + path("M10,108 Q100,124 190,108", INK, 3.5)
    out += path("M10,46 Q100,30 190,46 V108 Q100,124 10,108 Z", "none", 0, fill="#FB718522")
    for x, y in ((30, 64), (64, 82), (96, 70), (132, 90), (162, 66), (48, 98), (118, 58)):
        out += _ellipse(x, y, 7, 5, HOT, DARK, 1)
    for x, y, r in ((80, 42, 9), (104, 41, 7), (150, 112, 10), (126, 114, 7), (40, 104, 6)):
        out += circle(x, y, r, ACC, o=.95)
    return out + _heart(178, 22, .65, HOT, "#FB7185aa", 2)


# --------------------------------------------------------------------------- PREDICT
def q28():  # Who crashes next?
    mon = rect(70, 14, 116, 66, DARK, INK, 3, 5)
    mon += line([(78, 50), (104, 50), (110, 36), (116, 64), (122, 28), (128, 50), (148, 50), (154, 40), (160, 56), (166, 50), (178, 50)], GREEN, 2.5)
    mon += text(84, 32, "", 10) + circle(172, 26, 4, HOT)
    bed = path("M14,104 H186 M24,104 V136 M176,104 V136 M14,92 V136", INK, 3)
    bed += rect(26, 92, 40, 12, "#ffffff55", INK, 2.5, 4) + path("M64,104 Q90,84 176,96 V104", INK, 2.5, fill=SHADOW)
    bed += circle(48, 86, 8, INK)
    drip = rect(24, 16, 22, 30, "#7DD3FC55", COOL, 2.5, 6) + path("M35,46 V60 Q35,78 54,88", COOL, 2) + line([(35, 8), (35, 16)], INK, 2.5)
    return mon + bed + drip


def q29():  # Spring flood
    out = _mountain(4, 120, 98, 52, 16) + _mountain(70, 190, 98, 132, 30)
    out += path("M60,98 Q50,112 74,116 Q104,120 94,130 L132,136 H190 V112 H150 Q120,110 120,100 Z", COOL, 0, fill="#7DD3FC66")
    out += path("M60,98 Q50,112 74,116 Q104,120 94,130", COOL, 3)
    out += path("M150,112 H190 V140 H132 Z", COOL, 2, fill="#7DD3FC88")
    out += path("M132,100 L150,100 L156,142 L126,142 Z", INK, 3, fill="#475569") + line([(10, 98), (60, 98)], DIM, 2)
    return out + _snowflake(178, 18, 8, INK, 2) + _snowflake(30, 116, 6, INK, 2)


def q30():  # Next superconductor
    out = _ellipse(100, 120, 56, 14, "#7DD3FC44", COOL, 3) + path("M44,120 V106", COOL, 3) + path("M156,120 V106", COOL, 3)
    out += _ellipse(100, 106, 56, 14, "#7DD3FC88", COOL, 3)
    for x in (52, 70, 140, 158):
        out += path(f"M{x},104 q-4,-8 2,-14", INK, 2, o=.5)
    cube = (path("M84,48 L104,40 L124,48 L104,56 Z", ACC, 2.5, fill="#FCD34Dcc") + path("M84,48 V70 L104,78 V56 Z", ACC, 2.5, fill="#FCD34D88")
            + path("M124,48 V70 L104,78 V56 Z", ACC, 2.5, fill="#FCD34D55"))
    out += cube + path("M104,84 v8 M94,82 v6 M114,82 v6", DIM, 2, dash="2 3")
    out += path("M84,60 Q40,60 40,30 Q40,10 70,16 M124,60 Q168,60 168,30 Q168,10 138,16", COOL, 2, dash="4 4")
    return out + "".join(circle(20 + k * 20, 140, 2.2, INK, o=.6) for k in range(9))


def q31():  # Biomarker add-on
    tube = _rot(-14, 52, 76, rect(40, 18, 24, 104, SHADOW, INK, 3, 11) + path("M40,70 H64 V111 Q64,122 52,122 Q40,122 40,111 Z", HOT, 0, fill=HOT)
                + rect(36, 12, 32, 12, COOL, COOL, 0, 3))
    drop = path("M98,56 C88,72 88,82 98,84 C108,82 108,72 98,56 Z", HOT, 2.5, fill=HOT)
    plus = line([(98, 100), (98, 120)], ACC, 4) + line([(88, 110), (108, 110)], ACC, 4)
    return tube + drop + plus + _heart(152, 70, 1.8, HOT, "#FB718533") + path("M130,72 h10 l4,-8 l6,16 l5,-10 h12", INK, 2.5)


def q32():  # Range in 2070
    out = _mountain(10, 190, 136, 100, 20, INK, SHADOW)
    for x, y, s, c in ((54, 104, 1, ACC), (146, 104, 1, ACC), (82, 70, .9, ACC), (122, 64, .8, DIM)):
        out += line([(x, y), (x, y + 12 * s)], GREEN, 2.5) + "".join(circle(x + 5 * s * math.cos(k * 1.256), y + 5 * s * math.sin(k * 1.256), 3.2 * s, c) for k in range(5)) + circle(x, y, 2.4 * s, DARK)
    therm = rect(170, 18, 12, 56, SHADOW, INK, 2.5, 6) + circle(176, 80, 9, HOT, INK, 2.5) + rect(173, 40, 6, 36, HOT, HOT, 0, 3)
    return out + therm + circle(28, 28, 11, ACC) + "".join(line([(28 + 15 * math.cos(a), 28 + 15 * math.sin(a)), (28 + 20 * math.cos(a), 28 + 20 * math.sin(a))], ACC, 2.5) for a in [k * math.pi / 4 for k in range(8)])


# --------------------------------------------------------------------------- MEASURE
def q33():  # Rapid strep
    face = circle(62, 72, 42, SHADOW, INK, 3) + circle(48, 60, 4, INK) + circle(76, 60, 4, INK)
    face += path("M44,86 Q62,108 80,86 Z", INK, 2.5, fill="#7f1d1d") + _ellipse(62, 98, 6, 4, HOT, HOT, 0)
    face += path("M24,44 Q40,22 62,30 Q84,22 100,44", INK, 3)
    swab = line([(178, 26), (72, 92)], INK, 3) + _ellipse(70, 93, 7, 4.5, "#ffffff", INK, 1.5)
    cassette = rect(118, 98, 66, 28, "#ffffffdd", INK, 2.5, 6) + rect(150, 106, 22, 12, DARK, DARK, 0, 2) + line([(158, 107), (158, 117)], HOT, 2.5)
    return face + swab + cassette + circle(132, 112, 5, "none", DARK, 2)


def q34():  # Burnout scale
    desk = line([(10, 112), (190, 112)], INK, 3) + line([(24, 112), (24, 140)], INK, 3) + line([(176, 112), (176, 140)], INK, 3)
    slumped = person(62, 98, 1.9) + path("M48,108 Q62,100 78,108", DARK, 2.5, o=.5)
    papers = "".join(rect(118 - k * 1, 102 - k * 7, 44, 6, "#ffffffbb" if k % 2 else "#ffffff77", INK, 1.5, 1) for k in range(7))
    batt = rect(22, 24, 52, 26, SHADOW, INK, 3, 4) + rect(74, 31, 6, 12, INK, INK, 0, 1) + rect(27, 29, 9, 16, HOT, HOT, 0, 1)
    return desk + slumped + papers + batt + path("M84,70 q4,-6 0,-12", DIM, 2.5)


def q35():  # Two readers
    box = rect(52, 16, 96, 104, DARK, INK, 3, 4)
    bone = path("M84,20 V56 Q78,70 88,74 Q100,66 112,74 Q122,70 116,56 V20", INK, 3, fill="#e2e8f0aa")
    bone += path("M80,108 V88 Q78,80 90,80 H110 Q122,80 120,88 V108", INK, 3, fill="#e2e8f0aa") + path("M92,76 L108,76", ACC, 2.5)
    return box + bone + person(24, 104, 1.7, INK) + person(176, 104, 1.7, COOL) + line([(10, 134), (190, 134)], DIM, 2)


def q36():  # Wrist vs. cuff
    arm = path("M6,62 Q60,56 120,70 Q160,78 176,86 L172,104 Q150,98 118,92 Q60,84 6,90 Z", INK, 3, fill=SHADOW)
    cuff = rect(22, 52, 44, 44, "#7DD3FC77", COOL, 3, 4) + path("M44,96 Q44,128 74,128 H82", COOL, 2.5)
    cuff += _ellipse(92, 128, 11, 8, COOL, COOL, 0)
    gauge = circle(54, 26, 14, SHADOW, INK, 2.5) + line([(54, 26), (62, 18)], HOT, 2.5) + path("M54,40 V52", INK, 2)
    band = _rot(18, 148, 82, rect(138, 64, 20, 36, ACC, ACC, 0, 4) + rect(140, 72, 16, 20, DARK, DARK, 0, 2))
    return arm + cuff + gauge + band + _heart(160, 34, .7, HOT, HOT, 2) + path("M152,48 Q150,62 148,70", DIM, 2, dash="3 3")


def q37():  # Lead in the water
    tap = path("M14,26 H72 Q92,26 92,46 V54 H80 V46 Q80,40 72,40 H14 Z", INK, 3, fill=SHADOW) + rect(40, 14, 12, 12, INK, INK, 0, 2)
    tap += rect(30, 8, 32, 6, ACC, ACC, 0, 3)
    drip = path("M86,62 C80,72 80,76 86,78 C92,76 92,72 86,62 Z", COOL, 2, fill=COOL)
    glass = path("M60,92 L68,140 H104 L112,92", INK, 3) + path("M63,108 L68,140 H104 L109,108 Z", COOL, 0, fill="#7DD3FC66")
    big = path("M150,34 C124,72 124,98 150,104 C176,98 176,72 150,34 Z", COOL, 3, fill="#7DD3FC33") + text(150, 92, "Pb", 24, ACC)
    return tap + drip + glass + big


# --------------------------------------------------------------------------- EXPLAIN
def q38():  # Engine limit
    out = _flame(30, 76, 1.2) + _snowflake(172, 76, 18, COOL, 3)
    out += rect(70, 34, 60, 92, SHADOW, INK, 3, 3) + rect(76, 62, 48, 14, INK, INK, 0, 2) + line([(100, 76), (100, 112)], INK, 4)
    out += circle(100, 116, 8, "none", INK, 3) + path("M70,34 V22 H130 V34", "none", 0)
    out += arrow(52, 50, 68, 50, ACC, 3, head=7) + arrow(132, 50, 150, 50, COOL, 3, head=7)
    return out + "".join(line([(80 + k * 10, 54), (80 + k * 10, 46)], ACC, 2, o=.7) for k in range(5))


def q39():  # Bridge in a storm
    out = _cloud(150, 30, 70, INK, "rgba(148,163,184,.6)") + bolt(150, 44, .8, ACC)
    out += path("M8,112 Q16,108 24,112 T40,112 T56,112 T72,112 T88,112 T104,112 T120,112 T136,112 T152,112 T168,112 T184,112", COOL, 2, o=.7)
    out += line([(48, 120), (48, 44)], INK, 4) + line([(152, 120), (152, 44)], INK, 4)
    out += path("M6,92 Q28,80 48,44 Q100,96 152,44 Q172,80 194,92", INK, 2.5)
    for x in range(58, 150, 12):
        t = (x - 48) / 104
        cy = (1 - t) ** 2 * 44 + 2 * t * (1 - t) * 96 + t ** 2 * 44
        out += line([(x, cy), (x, 96 + 5 * math.sin((x - 48) / 104 * math.pi * 2))], DIM, 1.5)
    out += path("M6,96 H48 Q74,86 100,96 T152,96 H194", INK, 4)
    return out + "".join(path(f"M{x},{y} h22 q8,0 8,-6", INK, 2.5, o=.8) for x, y in ((10, 60), (14, 74), (6, 40)))


def q40():  # School closures
    out = "".join(rect(x, 136 - h, w, h, "#0f172a33", DIM, 2, 1) for x, w, h in ((8, 18, 60), (132, 16, 72), (174, 18, 54), (150, 22, 40)))
    out += path("M34,136 V78 L82,52 L130,78 V136 Z", INK, 3, fill=SHADOW) + rect(66, 98, 32, 38, "none", INK, 3, 1)
    lock = rect(70, 108, 24, 20, ACC, ACC, 0, 3) + path("M75,108 V102 Q82,92 89,102 V108", ACC, 3) + circle(82, 117, 3, DARK)
    out += lock + rect(44, 86, 14, 12, "none", INK, 2, 1) + rect(106, 86, 14, 12, "none", INK, 2, 1)
    return out + _virus(30, 34, 9) + _virus(160, 26, 11) + _virus(116, 32, 6) + line([(6, 136), (194, 136)], DIM, 2)


def q41():  # Clock in a cell
    cell = rect(14, 34, 158, 82, "#86EFAC22", GREEN, 3.5, 41)
    cell += path("M172,74 q8,-10 16,0 t12,4", GREEN, 2.5) + path("M24,46 l-8,-10 M20,104 l-8,10", GREEN, 2)
    face = circle(92, 75, 28, SHADOW, INK, 3) + "".join(line([(92 + 22 * math.cos(a), 75 + 22 * math.sin(a)), (92 + 26 * math.cos(a), 75 + 26 * math.sin(a))], INK, 2) for a in [k * math.pi / 6 for k in range(12)])
    face += line([(92, 75), (92, 58)], ACC, 3) + line([(92, 75), (104, 82)], INK, 3)
    genes = ""
    for k, c in enumerate((ACC, COOL, HOT)):
        a = -math.pi / 2 + k * 2 * math.pi / 3
        genes += circle(92 + 46 * math.cos(a) * 1.15, 75 + 30 * math.sin(a), 6, c)
    return cell + face + genes


def q42():  # Neutron-star crash
    out = ""
    for k, r in enumerate((30, 46, 62, 78, 94)):
        out += circle(100, 75, r, "none", COOL, 2.5 - k * .3, o=.75 - k * .12)
    pts1, pts2 = [], []
    for k in range(60):
        t = k / 59 * 3 * math.pi
        rr = 46 - k * .5
        pts1.append((100 + rr * math.cos(t), 75 + rr * .6 * math.sin(t)))
        pts2.append((100 - rr * math.cos(t), 75 - rr * .6 * math.sin(t)))
    out += line(pts1, ACC, 2.5, o=.7) + line(pts2, INK, 2.5, o=.7)
    return out + circle(pts1[-1][0], pts1[-1][1], 9, ACC) + circle(pts2[-1][0], pts2[-1][1], 9, INK)


def q43():  # Price war
    def shop(x, c):
        out = rect(x, 66, 52, 66, SHADOW, INK, 3, 1)
        out += "".join(path(f"M{x + k * 13},52 H{x + k * 13 + 13} V64 Q{x + k * 13 + 6.5},72 {x + k * 13},64 Z", INK, 2, fill=c if k % 2 == 0 else "#ffffffcc") for k in range(4))
        return out + rect(x + 18, 104, 16, 28, "none", INK, 2.5, 1) + rect(x + 6, 76, 40, 18, "none", INK, 2, 1)
    tag = lambda x, y, a, c: _rot(a, x, y, path(f"M{x - 18},{y - 12} H{x + 14} L{x + 24},{y} L{x + 14},{y + 12} H{x - 18} Z", c, 2.5, fill=c) + text(x, y + 6, "$", 16, DARK))
    return shop(12, HOT) + shop(136, COOL) + tag(100, 46, -35, ACC) + tag(100, 46, 35, INK) + line([(8, 132), (192, 132)], DIM, 2)


# --------------------------------------------------------------------------- BUILD
def q44():  # Grasp benchmark
    out = line([(100, 6), (100, 32)], INK, 6) + rect(70, 32, 60, 14, SHADOW, INK, 3, 3) + circle(100, 18, 6, ACC)
    out += path("M74,46 V82 L84,92 V100", INK, 4) + path("M126,46 V82 L116,92 V100", INK, 4)
    cube = path("M80,92 L100,84 L120,92 L100,100 Z", ACC, 2.5, fill="#FCD34Dcc") + path("M80,92 V116 L100,124 V100 Z", ACC, 2.5, fill="#FCD34D99") + path("M120,92 V116 L100,124 V100 Z", ACC, 2.5, fill="#FCD34D66")
    return out + cube + line([(30, 132), (170, 132)], DIM, 2) + path("M40,124 h18 v8 M150,124 h-14 l-4,8", DIM, 2)


def q45():  # A hand for kids
    palm = rect(66, 72, 56, 50, "#7DD3FC55", INK, 3, 10) + rect(74, 120, 40, 22, SHADOW, INK, 3, 4)
    out = palm
    for k, (x, h) in enumerate(((70, 40), (84, 48), (98, 46), (112, 36))):
        out += rect(x, 72 - h, 11, h, "#7DD3FC55", INK, 2.5, 5) + circle(x + 5.5, 72 - h * .45, 2.4, ACC)
    out += _rot(-40, 64, 96, rect(42, 90, 30, 11, "#7DD3FC55", INK, 2.5, 5)) + circle(94, 96, 8, "none", ACC, 2.5) + gear(94, 96, 6, ACC, 6, sw=1.5)
    return out + star(150, 40, 9, ACC) + star(40, 40, 6, HOT) + _heart(156, 100, .7, HOT, HOT, 2)


def q46():  # Review workbench
    out = _laptop(30, 26, 112, 72)
    for k in range(4):
        y = 40 + k * 14
        out += rect(42, y - 5, 10, 10, "none", INK, 2, 2) + line([(58, y), (110 - (k % 2) * 16, y)], DIM, 2.5)
        if k < 3:
            out += check(47, y, 5, ACC, 2.5)
    out += "".join(rect(156 + k * 3, 60 - k * 6, 26, 34, "#0f172a99", INK, 2, 2) for k in range(3))
    return out + line([(164, 70), (180, 70)], DIM, 2) + line([(164, 78), (176, 78)], DIM, 2)


def q47():  # Will they come?
    out = _house(10, 22, 180, 116, INK, "#0f172a33", door=False)
    chair = path("M40,134 V86 M40,108 H66 V134", INK, 3)
    elder = person(62, 98, 1.5) + line([(78, 96), (90, 132)], ACC, 3)
    db = line([(112, 92), (138, 92)], ACC, 3) + rect(106, 84, 8, 16, ACC, ACC, 0, 2) + rect(136, 84, 8, 16, ACC, ACC, 0, 2)
    cal = rect(150, 68, 30, 30, "#ffffff22", INK, 2.5, 2) + rect(150, 68, 30, 8, HOT, HOT, 0, 2) + "".join(circle(156 + (k % 3) * 9, 82 + (k // 3) * 8, 2, INK) for k in range(6))
    return out + chair + elder + db + cal


def q48():  # Therapy over a bad line
    out = path("M6,120 Q50,94 100,112 T194,104 V140 H6 Z", INK, 0, fill="#0f172a44") + path("M6,120 Q50,94 100,112 T194,104", DIM, 2.5)
    out += path("M18,110 V92 L32,80 L46,92 V110", DIM, 2.5)
    out += _phone(78, 14, 50, 92)
    out += bubble(86, 28, 34, 24, ACC, "#FCD34D33") + _heart(103, 37, .45, HOT, HOT, 1.5)
    out += bubble(90, 62, 28, 18, INK, "none", "right") + line([(96, 71), (112, 71)], INK, 2)
    return out + _bars(150, 46, 1) + cross(186, 22, 5, HOT, 3)


# --------------------------------------------------------------------------- SYNTHESIZE
def q49():  # Run it again?
    run = circle(110, 40, 9, INK) + line([(106, 52), (96, 84)], INK, 6)
    run += line([(104, 58), (122, 66), (130, 56)], INK, 4.5) + line([(104, 58), (88, 68), (80, 60)], INK, 4.5)
    run += line([(96, 84), (114, 98), (110, 120)], INK, 5) + line([(96, 84), (82, 104), (64, 108)], INK, 5)
    rain = _cloud(42, 46, 56, DIM, "rgba(148,163,184,.55)") + "".join(line([(28 + k * 10, 54), (24 + k * 10, 66)], COOL, 2.5) for k in range(4))
    sun = circle(164, 36, 12, ACC) + "".join(line([(164 + 16 * math.cos(a), 36 + 16 * math.sin(a)), (164 + 22 * math.cos(a), 36 + 22 * math.sin(a))], ACC, 2.5) for a in [k * math.pi / 4 for k in range(8)])
    shoe = path("M118,130 V118 Q130,118 136,110 L146,116 Q170,120 176,130 Z", ACC, 2.5, fill="#FCD34D55") + line([(116, 132), (178, 132)], INK, 3)
    return rain + sun + run + shoe + line([(12, 134), (104, 134)], DIM, 2)


def q50():  # Plastic in the soil
    out = rect(10, 60, 180, 80, "#78350f88", INK, 0, 2) + path("M10,60 H190", INK, 3)
    out += path("M10,92 Q60,86 100,94 T190,90", DIM, 2) + path("M10,118 Q60,112 100,120 T190,114", DIM, 2)
    for x in (42, 100, 156):
        out += path(f"M{x},60 V36 M{x},46 Q{x - 14},34 {x - 18},40 Q{x - 10},48 {x},46 M{x},40 Q{x + 14},26 {x + 18},32 Q{x + 10},42 {x},40", GREEN, 2.5, fill="#86EFAC66")
        out += path(f"M{x},60 q-4,10 2,18 M{x},60 q6,8 2,16", DIM, 2)
    r = lcg(11)
    shapes = ""
    for k in range(18):
        x, y = 18 + r() * 164, 70 + r() * 62
        c = (HOT, COOL, ACC, INK)[k % 4]
        shapes += _rot(r() * 180, x, y, rect(x - 3, y - 2, 6 + r() * 4, 4, c, c, 0, 1))
    return out + shapes


def q51():  # Six pills, few duels
    out = rect(20, 52, 160, 60, SHADOW, INK, 3, 8)
    cols = [(INK, ACC), (COOL, INK), (HOT, INK), (ACC, ACC), (GREEN, INK), (INK, HOT)]
    for k in range(6):
        x = 20 + k * 26.7
        if k:
            out += line([(x, 52), (x, 112)], INK, 2)
        out += rect(x + 3, 42, 20.7, 8, DIM, DIM, 0, 2)
        c1, c2 = cols[k]
        if k == 3:
            out += circle(x + 13.3, 82, 8, ACC)
        elif k == 4:
            out += _ellipse(x + 13.3, 82, 6, 10, GREEN, GREEN, 0)
        else:
            out += pill(x + 13.3, 82, 22, 10, 70, c1, c2)
    return out


def q52():  # Three weeks (school ventilation)
    win = rect(20, 18, 76, 96, "#7DD3FC33", INK, 3, 2) + line([(58, 18), (58, 114)], INK, 2.5) + line([(20, 66), (96, 66)], INK, 2.5)
    win += path("M58,18 L82,30 V110 L58,114", INK, 2.5, fill="#7DD3FC22")
    air = carrow(92, 42, 130, 30, 150, 52, COOL, 3) + carrow(92, 70, 130, 64, 164, 82, COOL, 3) + path("M118,98 q14,-10 28,0 t28,0", COOL, 2.5, o=.7)
    desk = rect(120, 112, 60, 6, INK, INK, 0, 2) + line([(128, 118), (128, 138)], INK, 3) + line([(172, 118), (172, 138)], INK, 3)
    return win + air + desk + person(150, 100, 1.0, ACC) + line([(10, 140), (190, 140)], DIM, 2)


def q53():  # Vitamin D for everything
    sun = circle(44, 40, 16, ACC) + "".join(line([(44 + 21 * math.cos(a), 40 + 21 * math.sin(a)), (44 + 28 * math.cos(a), 40 + 28 * math.sin(a))], ACC, 3) for a in [k * math.pi / 4 for k in range(8)])
    caps = _rot(-30, 104, 90, _ellipse(104, 90, 34, 18, "#FCD34Daa", ACC, 3) + path("M84,82 Q94,76 104,78", "#fff", 3, o=.8)) + text(104, 96, "D", 18, DARK)
    bone = _rot(30, 162, 64, rect(148, 58, 28, 12, INK, INK, 0, 2) + circle(147, 58, 7, INK) + circle(147, 70, 7, INK) + circle(177, 58, 7, INK) + circle(177, 70, 7, INK))
    return sun + caps + bone + _heart(160, 120, .7, HOT, HOT, 2) + _brain(34, 116, 18, 13, INK, "none")


def q54():  # Works here, fails there
    road = path("M10,128 Q60,104 100,112 T190,98", ACC, 3, dash="6 6")
    out = road + _house(14, 90, 34, 30, INK, SHADOW) + _house(152, 60, 34, 30, INK, SHADOW)
    out += path("M14,102 L31,84 L48,102", "#a16207", 4) + path("M152,72 L169,54 L186,72", "#a16207", 4)
    worker = person(96, 82, 1.7) + rect(108, 82, 18, 14, "#ffffffdd", INK, 2.5, 2) + rect(115, 85, 4, 8, HOT, HOT, 0, 0) + rect(113, 87, 8, 4, HOT, HOT, 0, 0)
    return out + worker + check(31, 64, 9, GREEN, 3.5) + cross(170, 34, 7, HOT, 3.5)


# --------------------------------------------------------------------------- EXPLORE
def q55():  # The ignored app
    moon = path("M54,22 A22,22 0 1 0 78,52 A17,17 0 1 1 54,22 Z", ACC, 2, fill=ACC)
    stars = star(98, 20, 4, INK) + star(176, 30, 5, INK) + star(30, 70, 3.5, INK)
    out = moon + stars + _phone(104, 36, 60, 104)
    tap = path("M118,52 H138 Q146,52 146,60 V64", INK, 3) + rect(124, 46, 8, 6, INK, INK, 0, 1)
    hand = lambda x, a: _rot(a, x, 92, path(f"M{x - 7},106 V84 Q{x - 7},78 {x - 3},78 V72 Q{x},68 {x + 3},72 V78 Q{x + 7},78 {x + 7},84 V106 Z", INK, 2.5, fill="#ffffff33"))
    hands = hand(128, -18) + hand(140, 18)
    drops = "".join(path(f"M{x},{y} c-3,5 -3,8 0,8 c3,0 3,-3 0,-8 z", COOL, 1.5, fill=COOL) for x, y in ((146, 68), (152, 76), (118, 70)))
    zz = text(36, 120, "Z", 16, DIM) + text(54, 106, "Z", 12, DIM)
    return out + hands + drops + path("M114,114 q6,-5 12,0 t12,0 t12,0", COOL, 2.5) + zz


def q56():  # Waste pickers
    out = "".join(rect(x, 100 - h, w, h, "#0f172a33", DIM, 2, 1) for x, w, h in ((110, 20, 80), (134, 26, 60), (164, 22, 88)))
    cart = path("M76,72 H158 L150,118 H84 Z", INK, 3, fill=SHADOW) + circle(96, 126, 9, DARK, INK, 3) + circle(140, 126, 9, DARK, INK, 3)
    cart += path("M80,72 Q96,40 118,50 Q134,30 154,72 Z", INK, 2.5, fill="#ffffff33")
    cart += rect(100, 40, 8, 20, COOL, COOL, 0, 2) + rect(102, 34, 4, 6, COOL, COOL, 0, 1) + rect(128, 44, 14, 18, ACC, ACC, 0, 2)
    puller = person(36, 104, 1.8) + line([(48, 98), (78, 86)], INK, 3.5)
    return out + cart + puller + line([(6, 136), (194, 136)], DIM, 2)


def q57():  # The turnaround
    roof = path("M14,48 L40,30 V48 L66,30 V48 L92,30 V48 L118,30 V48 H186", INK, 3) + line([(160, 48), (160, 14)], INK, 4)
    belt = rect(10, 96, 180, 14, SHADOW, INK, 3, 7) + "".join(circle(20 + k * 22.5, 103, 4, "none", INK, 2) for k in range(8))
    boxes = ""
    for k, x in enumerate((22, 62, 102, 142)):
        bad = k == 1
        c = HOT if bad else ACC
        boxes += rect(x, 70, 28, 26, c if not bad else "#FB718555", c, 2.5, 2) + line([(x + 14, 70), (x + 14, 80)], DARK if not bad else HOT, 2)
    return roof + belt + boxes + cross(76, 58, 6, HOT, 3) + gear(170, 128, 12, INK, 8) + gear(150, 132, 8, DIM, 6) + check(116, 58, 8, GREEN, 3)


def q58():  # Back to work
    door = rect(110, 18, 66, 118, "#FCD34D44", INK, 3, 2) + path("M110,18 L136,30 V128 L110,136 Z", INK, 3, fill=SHADOW) + circle(130, 80, 3, INK)
    light = path("M176,136 L196,146 H110 Z", ACC, 0, fill="#FCD34D33")
    p = person(70, 104, 2.0) + rect(84, 104, 20, 16, ACC, ACC, 0, 2) + path("M89,104 V100 H99 V104", ACC, 2)
    return door + light + p + _virus(32, 32, 9, DIM, "none", 8) + path("M46,62 q6,-8 0,-14", DIM, 2.5) + line([(10, 136), (190, 136)], DIM, 2)


def q59():  # What should we measure?
    ribbon = path("M60,24 Q40,24 44,50 L72,110 M60,24 Q80,24 76,50 L48,110", COOL, 10)
    stripes = path("M60,24 Q40,24 44,50 L72,110 M60,24 Q80,24 76,50 L48,110", INK, 2.5)
    tape = circle(144, 56, 30, ACC, INK, 0) + circle(144, 56, 10, DARK) + rect(140, 82, 52, 20, ACC, ACC, 0, 2) + _ruler_ticks(146, 102, 190, 6, DARK)
    return ribbon + stripes + tape + text(144, 118, "?", 22, INK) + text(106, 40, "?", 18, DIM) + text(60, 120, "?", 18, DIM)


def q60():  # The rural gap
    barn = path("M12,128 V78 L36,58 L60,78 V128 Z", INK, 3, fill="#B91C1C99") + path("M26,128 V100 H46 V128 M26,100 L46,128 M46,100 L26,128", INK, 2)
    silo = rect(62, 64, 18, 64, SHADOW, INK, 3, 1) + path("M62,64 Q71,52 80,64", INK, 3)
    road = path("M80,140 Q120,116 120,100", DIM, 3, dash="5 5")
    screen = rect(100, 18, 86, 62, DARK, INK, 3, 4) + person(143, 54, 1.4, INK) + rect(140, 58, 6, 2, HOT, HOT, 0, 0) + rect(142, 56, 2, 6, HOT, HOT, 0, 0)
    screen += rect(134, 80, 18, 8, INK, INK, 0, 0) + rect(124, 88, 38, 4, INK, INK, 0, 2)
    return barn + silo + road + screen + line([(6, 128), (100, 128)], DIM, 2)


def q61():  # The tangle clip
    pole = line([(54, 14), (54, 136)], INK, 4) + line([(34, 136), (74, 136)], INK, 4) + path("M38,14 H70", INK, 3)
    bag = rect(36, 22, 36, 46, "#7DD3FC44", INK, 2.5, 8) + line([(42, 36), (66, 36)], DIM, 2) + line([(42, 44), (60, 44)], DIM, 2) + rect(50, 68, 8, 8, INK, INK, 0, 1)
    tubes = path("M54,76 C54,104 112,82 120,106 S86,138 126,130 S174,94 150,74 S108,98 136,118 S180,132 188,112", COOL, 3)
    tubes += path("M58,76 C70,96 92,70 128,82 S170,118 138,100 S116,60 160,52 S190,78 172,96", INK, 2.5)
    clip = _rot(-20, 140, 92, rect(127, 85, 28, 14, ACC, DARK, 2, 4) + line([(132, 92), (150, 92)], DARK, 2))
    return tubes + pole + bag + clip + star(176, 26, 7)


def q62():  # Roots of a field
    roots = path("M100,86 Q96,104 70,118 M100,86 Q104,110 128,130 M100,86 Q100,112 96,140 M90,96 Q72,96 52,108 M110,96 Q134,98 156,112", "#D6B98C", 3)
    trunk = rect(92, 46, 16, 40, "#78350f", "none", 0, 0)
    canopy = circle(76, 46, 17, "#2f7d4f", GREEN, 2.5) + circle(124, 46, 17, "#2f7d4f", GREEN, 2.5) + circle(100, 32, 25, "#3a9160", GREEN, 2.5)
    coin = circle(162, 50, 14, ACC, DARK, 2) + text(162, 56, "$", 16, DARK)
    bee = _ellipse(38, 50, 10, 6.5, ACC, DARK, 1.5) + line([(35, 44), (35, 56)], DARK, 2) + line([(41, 44), (41, 56)], DARK, 2)
    bee += _ellipse(34, 41, 6, 3.5, "#ffffffaa", INK, 1) + _ellipse(42, 41, 6, 3.5, "#ffffffaa", INK, 1)
    return roots + trunk + canopy + line([(10, 86), (190, 86)], INK, 3) + coin + bee


def q63():  # Paper flood
    wave = path("M8,142 V98 Q40,72 66,94 Q86,110 104,88 Q124,64 150,82 Q170,96 192,78 V142 Z", COOL, 2.5, fill="#7DD3FC44")
    r = lcg(63)
    papers = ""
    for k in range(16):
        x, y = 16 + r() * 168, 100 + r() * 26
        papers += _rot(r() * 50 - 25, x, y, doc(x - 7, y - 9, 14, 18, INK, 2, DARK, 1.5))
    ring = line([(150 + 17 * math.cos(math.radians(60 * k + 30)), 36 + 17 * math.sin(math.radians(60 * k + 30))) for k in range(6)], INK, 3, close=True)
    ring += circle(150, 36, 8, "none", ACC, 2.5) + line([(165, 27), (180, 18)], INK, 3) + circle(183, 16, 4.5, HOT)
    chip = rect(30, 20, 34, 34, DARK, INK, 2.5, 3) + rect(39, 29, 16, 16, ACC, "none", 0, 2)
    chip += "".join(line([(35 + k * 8, 14), (35 + k * 8, 20)], INK, 2) + line([(35 + k * 8, 54), (35 + k * 8, 60)], INK, 2) for k in range(4))
    return wave + papers + ring + chip + text(100, 46, "+", 24, DIM)


def q64():  # Grit or not?
    mountain = path("M6,142 L70,58 L96,88 L124,44 L194,142 Z", INK, 3, fill=SHADOW) + path("M111,64 L124,44 L137,64 L130,60 L124,66 L117,60 Z", INK, 2, fill="#F8FAFCcc")
    trail = path("M30,140 Q60,124 52,112 Q48,100 74,96 Q100,92 96,80", ACC, 2.5, dash="4 5")
    flag = line([(124, 44), (124, 24)], INK, 2.5) + path("M124,24 L142,29 L124,34 Z", HOT, 2, fill=HOT)
    climber = person(96, 72, 1.0, INK) + line([(102, 67), (110, 56)], INK, 2.5)
    cap = path("M14,30 L38,22 L62,30 L38,38 Z", INK, 2, fill=DARK) + path("M24,34 V44 Q38,50 52,44 V34", INK, 2) + line([(58, 31), (58, 44)], ACC, 2.5)
    return mountain + trail + flag + climber + cap


def q65():  # Newts in the pond
    pond = _ellipse(100, 98, 92, 38, "#0e749088", COOL, 3) + path("M30,96 Q60,88 90,96 M110,108 Q140,100 170,108", "#7DD3FC88", 2)
    newt = lambda x, y, s, c: _rot(-12, x, y, path(f"M{x - 22 * s},{y} Q{x - 6 * s},{y - 7 * s} {x + 12 * s},{y - 2 * s} Q{x + 26 * s},{y} {x + 30 * s},{y - 8 * s} M{x - 22 * s},{y} Q{x - 6 * s},{y + 6 * s} {x + 12 * s},{y + 2 * s}", c, 3.5) + circle(x - 18 * s, y - 2 * s, 1.6, DARK))
    net = path("M150,18 L118,72 M118,72 q-14,8 -6,24 q14,8 28,-4 q4,-16 -22,-20 z", INK, 2.5, fill="#F8FAFC22")
    return pond + newt(64, 98, 1, "#F59E0B") + newt(122, 112, .8, "#F59E0B") + newt(98, 84, .7, "#FBBF24") + net + _cloud(40, 40, 50, DIM, "rgba(148,163,184,.4)")


def q66():  # Migraine genes
    head = path("M44,132 V108 Q22,100 26,70 Q30,26 72,22 Q112,20 116,64 L124,80 L114,84 V104 Q114,112 100,112 H84 V132", INK, 3, fill=SHADOW)
    pain = bolt(78, 56, 1.2, HOT) + path("M56,40 l10,8 M96,36 l-8,10", HOT, 3)
    return head + pain + helix(130, 76, 192, 16, 2.5)


def q67():  # The freezer
    box = rect(22, 20, 88, 116, "#7DD3FC22", INK, 3, 6) + line([(22, 58), (110, 58)], INK, 2.5) + line([(22, 98), (110, 98)], INK, 2.5) + rect(98, 30, 6, 18, INK, INK, 0, 2)
    tubes = "".join(rect(32 + i * 12, 66 + (k * 40) - 34, 7, 22, "#FB718599" if (i + k) % 3 == 0 else "#F8FAFC55", INK, 1.5, 2) for k in (0, 1, 2) for i in range(6))
    heart = path("M152,128 C116,104 118,72 140,72 C150,72 152,82 152,86 C152,82 154,72 164,72 C186,72 188,104 152,128 Z", HOT, 3, fill="#FB718566")
    return box + tubes + heart + path("M128,96 H140 L146,84 L154,110 L160,96 H176", INK, 2.5)


def q68():  # Seeds of choice
    stalk = line([(70, 136), (70, 30)], GREEN, 4) + "".join(path(f"M70,{y} Q{70 + s * 40},{y - 12} {70 + s * 54},{y + 8}", GREEN, 3, fill="#86EFAC44") for y, s in ((110, 1), (90, -1), (70, 1), (52, -1)))
    cob = _rot(18, 82, 60, _ellipse(82, 60, 9, 22, ACC, "#B45309", 2) + "".join(line([(76, 48 + k * 6), (88, 48 + k * 6)], "#B45309", 1.2) for k in range(5)))
    sun = circle(166, 32, 14, ACC) + "".join(line([(166 + 18 * math.cos(a), 32 + 18 * math.sin(a)), (166 + 24 * math.cos(a), 32 + 24 * math.sin(a))], ACC, 2.5) for a in [k * math.pi / 4 for k in range(8)])
    coins = "".join(_ellipse(150, 126 - k * 7, 18, 6, ACC, DARK, 1.5) for k in range(4))
    cracked = path("M10,136 L190,136 M24,136 l8,-8 l-4,-6 M120,136 l6,-7 l6,7", "#D6B98C", 2.5)
    return cracked + stalk + cob + sun + coins


def q69():  # Worth the price?
    syringe = _rot(-35, 70, 70, rect(34, 62, 66, 18, "#7DD3FC55", INK, 2.5, 3) + rect(100, 66, 18, 10, INK, INK, 0, 1) + line([(118, 71), (138, 71)], INK, 2) + line([(24, 71), (34, 71)], INK, 4) + line([(20, 60), (20, 82)], INK, 4))
    scale = line([(150, 30), (150, 130)], INK, 3) + line([(116, 50), (184, 40)], INK, 3) + line([(126, 136), (174, 136)], INK, 3)
    pans = path("M104,50 Q116,70 128,50 Z", INK, 2, fill=SHADOW) + path("M172,40 Q184,60 196,40 Z", INK, 2, fill=SHADOW)
    return syringe + scale + pans + text(116, 46, "£", 16, ACC) + person(184, 30, .8, INK)


def q70():  # Why this deal?
    flag = rect(118, 18, 66, 22, "#FACC15", "none", 0, 0) + rect(118, 40, 66, 11, "#2563EB", "none", 0, 0) + rect(118, 51, 66, 11, "#DC2626", "none", 0, 0) + line([(118, 18), (118, 136)], INK, 3)
    hands = path("M14,104 L52,96 Q62,92 72,96 L98,106 Q104,110 98,114 L80,116 M98,106 Q112,100 126,104 L170,92", INK, 4) + path("M60,98 Q70,110 86,112", ACC, 3)
    dove = path("M40,48 Q54,32 72,40 Q82,30 96,34 Q84,42 80,52 Q64,62 46,56 Z", INK, 2, fill="#F8FAFCdd")
    return flag + hands + dove + doc(150, 86, 30, 38, INK, 3, SHADOW)


def q71():  # Under fifty
    ribbon = path("M78,28 Q60,28 64,56 L94,118 M78,28 Q96,28 92,56 L62,118", "#F472B6", 9)
    docs = "".join(doc(118 + k * 8, 28 + k * 10, 34, 44, INK, 3, "#0f172acc") for k in range(4))
    return ribbon + docs + text(160, 123, "< 50 ?", 16, ACC)


def q72():  # The abandoned form
    laptop = rect(52, 22, 112, 76, DARK, INK, 3, 5) + path("M40,106 H176 L166,98 H50 Z", INK, 2.5, fill=SHADOW)
    form = rect(64, 34, 88, 9, "none", DIM, 1.8, 2) + rect(64, 50, 88, 9, "none", DIM, 1.8, 2) + rect(64, 66, 54, 9, "none", HOT, 2.2, 2) + cross(140, 84, 7)
    return laptop + form + person(26, 112, 1.8, INK) + text(26, 62, "?", 22, ACC)


def q73():  # No-shows
    cal = rect(18, 26, 92, 92, "#F8FAFC22", INK, 3, 5) + rect(18, 26, 92, 18, HOT, "none", 0, 5)
    days = "".join(rect(26 + (k % 4) * 21, 52 + (k // 4) * 21, 15, 15, "none", DIM, 1.5, 2) for k in range(12))
    misses = cross(33.5, 59.5, 5) + cross(75.5, 80.5, 5) + cross(54.5, 101.5, 5)
    phone = rect(128, 40, 52, 92, DARK, INK, 3, 8) + bubble(134, 54, 40, 26, ACC, "#FCD34D33") + line([(140, 64), (166, 64)], ACC, 2) + circle(154, 122, 4, DIM)
    return cal + days + misses + phone


def q74():  # The blogs know more
    journals = "".join(doc(14 + k * 18, 84, 16, 22, INK, 2, DARK, 1.5) for k in range(3))
    shelf = line([(10, 108), (74, 108)], INK, 3) + text(42, 124, "5", 14, INK)
    r = lcg(74)
    posts = ""
    for k in range(14):
        x, y = 96 + r() * 86, 30 + r() * 66
        posts += (bubble(x - 12, y - 8, 24, 16, COOL, DARK, "left", 1.5) if k % 3 else
                  rect(x - 12, y - 8, 24, 16, DARK, ACC, 1.5, 2) + path(f"M{x - 3},{y - 4} L{x + 5},{y} L{x - 3},{y + 4} Z", ACC, 0, fill=ACC))
    gear_ = gear(42, 50, 20, INK, 8, DARK) + check(42, 50, 8)
    return journals + shelf + posts + gear_ + text(140, 124, "500", 14, COOL)


QUESTION_ART = {f"Q{k:02d}": globals()[f"q{k:02d}"] for k in range(1, 75)}
