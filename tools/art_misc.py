"""Vector art for Twist cards (T01-T16) and Research Programme cards (P1-P6).

Same style as art.py's DESIGN_ART: 200 x 150 art box, INK line art with ACC / HOT / COOL accents.
"""
from art import *
from art import _f
import math

DARK = "#0f172a"
GREEN = "#86EFAC"


# --------------------------------------------------------------------------- local helpers
def g(content, rot=0, cx=0, cy=0, tx=0, ty=0, s=1):
    """Group with translate / rotate / scale."""
    t = ""
    if tx or ty:
        t += f"translate({_f(tx)} {_f(ty)}) "
    if rot:
        t += f"rotate({_f(rot)} {_f(cx)} {_f(cy)}) "
    if s != 1:
        t += f"scale({s}) "
    return f'<g transform="{t.strip()}">{content}</g>'


def poly(pts, fill=INK, stroke="none", w=2, o=1):
    d = " ".join(f"{_f(x)},{_f(y)}" for x, y in pts)
    return (f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" '
            f'stroke-linejoin="round" opacity="{o}"/>')


def ellipse(x, y, rx, ry, fill=INK, stroke="none", w=2, o=1, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<ellipse cx="{_f(x)}" cy="{_f(y)}" rx="{_f(rx)}" ry="{_f(ry)}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{w}" opacity="{o}"{da}/>')


def scissors(x, y, rot=0, s=1.0, c=INK, open_=14):
    """Scissors with pivot at (x, y), blades pointing right (before rotation)."""
    a = math.radians(open_)
    L = 40
    out = ""
    for sg in (-1, 1):
        tip = (L * math.cos(a), sg * L * math.sin(a))
        nx, ny = -math.sin(a) * sg, math.cos(a)  # normal-ish
        blade = [(-3 * nx, -3 * ny * sg), tip, (5 * nx, 5 * ny * sg)]
        out += poly([(px, py) for px, py in blade], c)
        # handle on the opposite side
        hx, hy = -18, -sg * 12
        out += line([(0, 0), (hx + 6, hy * 0.6)], c, 4)
        out += circle(hx, hy, 8, "none", c, 3.5)
    out += circle(0, 0, 2.6, ACC)
    return f'<g transform="translate({_f(x)} {_f(y)}) rotate({_f(rot)}) scale({s})">{out}</g>'


def sun(x, y, r=12, c=ACC, rays=10, rl=7, w=2.5):
    out = circle(x, y, r, c)
    for k in range(rays):
        a = k * 2 * math.pi / rays
        out += line([(x + (r + 4) * math.cos(a), y + (r + 4) * math.sin(a)),
                     (x + (r + 4 + rl) * math.cos(a), y + (r + 4 + rl) * math.sin(a))], c, w)
    return out


def phone(x, y, w=12, h=20, rot=0, glow=COOL):
    out = rect(x - w / 2, y - h / 2, w, h, DARK, INK, 2, 2.5) + rect(x - w / 2 + 2, y - h / 2 + 3, w - 4, h - 7, glow, "none", 0, 1)
    return g(out, rot, x, y) if rot else out


def heart(x, y, s=1.0, c=HOT):
    return path(f"M{_f(x)},{_f(y + 6 * s)} C{_f(x - 10 * s)},{_f(y - 1 * s)} {_f(x - 6 * s)},{_f(y - 9 * s)} {_f(x)},{_f(y - 4 * s)} "
                f"C{_f(x + 6 * s)},{_f(y - 9 * s)} {_f(x + 10 * s)},{_f(y - 1 * s)} {_f(x)},{_f(y + 6 * s)} Z", c, 1, fill=c)


def cloud(x, y, s=1.0, c=INK, fill="none", w=2.5, o=1):
    return path(f"M{_f(x - 18 * s)},{_f(y + 8 * s)} a{_f(8 * s)},{_f(8 * s)} 0 0 1 {_f(2 * s)},{_f(-15 * s)} "
                f"a{_f(11 * s)},{_f(11 * s)} 0 0 1 {_f(20 * s)},{_f(-4 * s)} a{_f(8 * s)},{_f(8 * s)} 0 0 1 {_f(14 * s)},{_f(19 * s)} Z",
                c, w, fill=fill, o=o)


# --------------------------------------------------------------------------- twists
def tw_ethics_no():
    # sound block + gavel mid-strike + impact lines, NO stamp on a document
    out = rect(18, 112, 70, 14, "#0f172a66", INK, 3, 3) + line([(26, 108), (80, 108)], DIM, 2)
    head = rect(-26, -11, 52, 22, INK, INK, 0, 4) + rect(-30, -13, 8, 26, ACC, ACC, 0, 2) + rect(22, -13, 8, 26, ACC, ACC, 0, 2)
    handle = line([(0, -11), (0, -66)], INK, 6)
    out += g(handle + head, 28, 0, 0, 54, 94)
    for a in (-160, -125, -55, -20):
        r = math.radians(a)
        out += line([(53 + 34 * math.cos(r), 108 + 18 * math.sin(r)), (53 + 46 * math.cos(r), 108 + 24 * math.sin(r))], ACC, 3)
    stamp = (rect(-36, -21, 72, 42, "none", HOT, 5, 6) + rect(-30, -15, 60, 30, "none", HOT, 2, 3)
             + text(0, 13, "NO", 34, HOT, weight=800))
    out += doc(118, 30, 64, 84, DIM, 0, fill="#0f172a44", sw=2.5)
    return out + g(stamp, -14, 0, 0, 150, 76)


def tw_funding_cut():
    # banknote cut in two, scissors at the cut
    def note(x, y, w, h):
        return (rect(x, y, w, h, "#86EFAC33", GREEN, 3, 3) + rect(x + 6, y + 6, w - 12, h - 12, "none", GREEN, 1.5, 2, o=.6))
    left = note(14, 50, 72, 56) + circle(62, 78, 12, "none", GREEN, 2.5) + text(62, 84, "$", 17, GREEN)
    right = note(96, 50, 46, 56) + line([(108, 66), (130, 66)], GREEN, 2) + line([(108, 90), (124, 90)], GREEN, 2)
    out = g(left, -6, 50, 78) + g(right, 7, 120, 78)
    out += line([(91, 36), (91, 124)], ACC, 2.5, "5 5")
    out += scissors(150, 104, -118, 1.05, INK, 16)
    out += text(170, 28, "−90%", 16, HOT, "end")
    return out


def tw_rarer():
    r = lcg(31)
    out = ""
    # haystack: a mound filled with straw strokes
    out += path("M14,132 Q22,60 100,42 Q178,60 186,132 Z", "#FCD34D", 2, fill="#FCD34D33", o=.8)
    for k in range(70):
        x = 20 + r() * 160
        top = 132 - (88 * (1 - ((x - 100) / 86) ** 2)) * 0.98
        y = top + r() * (130 - top)
        a = (r() - .5) * 1.6
        L = 10 + r() * 10
        out += line([(x, y), (x + L * math.cos(a), y + L * math.sin(a))], ACC if r() < .6 else DIM, 1.8, o=.75)
    out += line([(10, 134), (190, 134)], DIM, 2)
    # the diamond
    cx, cy = 128, 92
    out += circle(cx, cy, 20, "#7DD3FC33")
    out += poly([(cx - 13, cy - 5), (cx - 7, cy - 13), (cx + 7, cy - 13), (cx + 13, cy - 5), (cx, cy + 14)], COOL, INK, 2)
    out += line([(cx - 13, cy - 5), (cx + 13, cy - 5)], INK, 1.5) + line([(cx - 4, cy - 13), (cx - 5, cy - 5), (cx, cy + 14), (cx + 5, cy - 5), (cx + 4, cy - 13)], INK, 1.5)
    out += star(cx + 22, cy - 20, 6, INK, 4) + star(cx - 22, cy - 18, 4, INK, 4) + star(cx + 18, cy + 12, 3.5, INK, 4)
    return out + text(30, 26, "1 IN 20,000", 13, INK, "start")


def tw_registry():
    out = line([(10, 134), (190, 134)], DIM, 2)
    # light beam pouring out of the doorway onto the floor
    out += poly([(64, 26), (120, 26), (190, 134), (40, 134)], ACC, o=.18)
    out += rect(64, 26, 56, 108, "#FCD34D", "none", 0, 2, o=.5)
    out += rect(64, 26, 56, 108, "none", INK, 3.5, 2)
    # door swung open (toward the viewer, on the left hinge)
    out += poly([(64, 26), (36, 16), (36, 144), (64, 134)], DARK, INK, 3)
    out += circle(42, 82, 3, ACC)
    # the database inside
    out += cylinder(72, 52, 40, 52, DARK, fill=INK)
    return out + text(156, 120, "20 YRS", 13, DARK)


def tw_threshold():
    out = line([(16, 126), (186, 126)], INK, 3)
    hs = [14, 22, 28, 38, 44, 54, 62, 74, 84, 96]
    for k, h in enumerate(hs):
        x = 22 + k * 16.5
        above = k >= 5
        out += rect(x, 126 - h, 12, h, ACC if above else "none", ACC if above else DIM, 2, 1)
    out += line([(100, 14), (100, 132)], HOT, 3, "6 5")
    out += scissors(100, 26, 90, 0.7, INK, 18)
    out += text(110, 146, "60", 13, HOT, "start")
    return out


def tw_rollout():
    # calendar grid being flattened by a steamroller rolling left -> right
    out = rect(14, 30, 172, 100, "#0f172a33", INK, 3, 4) + line([(14, 46), (186, 46)], INK, 2.5)
    out += line([(44, 22), (44, 36)], INK, 3) + line([(156, 22), (156, 36)], INK, 3)
    for row in range(3):
        for col in range(6):
            x, y = 20 + col * 27.5, 52 + row * 25
            done = col < 3 or (col == 3 and row < 2)
            out += rect(x, y, 23, 20, ACC if done else "none", ACC if done else DIM, 2, 2)
    # steamroller
    out += rect(78, 44, 30, 30, "#4c1d95", INK, 3, 3) + rect(84, 50, 18, 14, "#C4B5FD", "none", 0, 2)
    out += rect(74, 72, 72, 30, INK, DARK, 2, 4) + line([(130, 60), (130, 72)], INK, 4) + rect(124, 54, 12, 7, DIM, "none", 0, 2)
    out += circle(152, 106, 26, INK, DARK, 3) + circle(152, 106, 10, "none", DARK, 3)
    out += circle(88, 114, 16, INK, DARK, 3) + circle(88, 114, 5, DARK)
    return out + "".join(line([(46 - k * 8, 94 + k * 12), (66 - k * 8, 94 + k * 12)], INK, 3) for k in range(3))


def tw_talk():
    out = person(36, 116, 1.6) + person(100, 120, 1.6, ACC) + person(164, 116, 1.6)
    out += bubble(14, 22, 64, 34, INK, "#0f172a66", "left") + bubble(68, 38, 64, 34, ACC, "#0f172a66", "left")
    out += bubble(122, 22, 64, 34, INK, "#0f172a66", "right")
    for (x, y, c) in ((30, 39, INK), (84, 55, ACC), (138, 39, INK)):
        out += "".join(circle(x + 8 + i * 12, y, 3, c) for i in range(3))
    out += carrow(54, 88, 70, 76, 84, 90, DIM, 2.5, head=6) + carrow(146, 88, 130, 76, 116, 90, DIM, 2.5, head=6)
    return out


def tw_only_one():
    out = poly([(84, 8), (116, 8), (150, 128), (50, 128)], ACC, o=.22)
    out += ellipse(100, 128, 52, 10, ACC, o=.45)
    out += rect(82, 2, 36, 12, INK, INK, 0, 3)
    for x in (24, 176):
        out += person(x, 116, 1.3, FAINT)
    return out + person(100, 104, 2.4) + text(100, 148, "N = 1", 12, ACC)


def tw_thirty():
    r = lcg(77)
    out = ""
    # pile at the bottom
    for k in range(10):
        x = 16 + (k % 5) * 25 + (r() - .5) * 6
        y = 108 - (k // 5) * 14 + (r() - .5) * 4
        out += g(doc(x, y, 30, 22, INK, 2, fill="#1e1b4b", sw=2), (r() - .5) * 30, x + 15, y + 11)
    # falling papers
    for k, (x, y) in enumerate(((28, 22), (70, 34), (110, 16), (146, 40), (176, 18), (52, 66), (122, 66), (170, 70))):
        out += g(doc(x - 12, y - 15, 24, 30, INK, 2, fill="#1e1b4b", sw=2), (r() - .5) * 80, x, y)
        out += line([(x - 4, y - 26), (x - 4, y - 36)], DIM, 2) + line([(x + 6, y - 24), (x + 6, y - 32)], DIM, 2)
    return out + line([(10, 140), (190, 140)], DIM, 2) + text(188, 132, "+30", 22, ACC, "end")


def tw_fog():
    out = line([(10, 136), (190, 136)], DIM, 2)
    out += rect(96, 26, 8, 110, INK, INK, 0, 2)
    boards = (((104, 34, 54), 1, -8), ((96, 58, 50), -1, 6), ((104, 84, 46), 1, 10))
    for (x, y, w), d, rot in boards:
        tip = x + d * (w + 10)
        pts = [(x, y), (x + d * w, y), (tip, y + 9), (x + d * w, y + 18), (x, y + 18)]
        out += g(poly(pts, DARK, INK, 2.5) + text(x + d * w / 2, y + 14.5, "?", 15, ACC), rot, x, y + 9)
    # fog bands drifting across
    for k, (y, o) in enumerate(((44, .26), (76, .32), (108, .38), (126, .3))):
        dx = (k % 2) * 30
        out += path(f"M{-10 + dx},{y} q20,-12 40,0 q20,12 40,0 q20,-12 40,0 q20,12 40,0 q20,-12 40,0 v14 h-200 z", "none", 0, fill="#e2e8f0", o=o)
    return out


def tw_slow_burn():
    # very long candle with a tiny flame, hourglass beside, long timeline
    out = rect(60, 30, 22, 100, INK, INK, 0, 3) + ellipse(71, 30, 11, 3, "#e2e8f0")
    out += path("M60,40 q-3,8 0,14", INK, 3) + line([(71, 30), (71, 22)], DARK, 2)
    out += path("M71,6 C78,14 76,22 71,22 C66,22 64,14 71,6 Z", ACC, 1, fill=ACC) + circle(71, 17, 2.5, HOT)
    out += rect(46, 128, 50, 8, DIM, "none", 0, 2)
    out += hourglass(140, 62, 1.5)
    out += arrow(20, 144, 186, 144, DIM, 2.5, head=6) + text(140, 118, "15 YEARS", 14, ACC)
    return out


def tw_brief_trigger():
    out = cloud(64, 34, 1.6, INK, DARK, 3) + cloud(128, 28, 1.2, DIM, "none", 2.5)
    out += bolt(76, 76, 2.6, ACC)
    out += line([(10, 124), (190, 124)], INK, 3)
    for a in range(200, 345, 24):
        r = math.radians(a)
        out += line([(70 + 14 * math.cos(r), 122 + 14 * math.sin(r)), (70 + 26 * math.cos(r), 122 + 22 * math.sin(r))], HOT, 3)
    out += clock(150, 84, 22, INK, 0, 20, 3)
    out += path("M150,62 A22,22 0 0 1 157.5,63.3 L150,84 Z", "none", 0, fill=ACC, o=.85)
    return out + text(150, 142, "MINUTES", 12, ACC)


def tw_few_exposed():
    out = ""
    # crowd outside the zone
    pos = [(24, 58), (24, 98), (24, 136), (176, 58), (176, 98), (176, 136), (52, 136), (148, 136), (54, 20), (146, 20)]
    for x, y in pos:
        out += person(x, y, 0.85, DIM)
    out += circle(100, 82, 46, "#FB718522", HOT, 3, dash="7 5")
    out += person(86, 96, 0.95, HOT) + person(114, 96, 0.95, HOT) + person(100, 112, 0.95, HOT)
    # hazard sign
    out += poly([(100, 38), (120, 72), (80, 72)], ACC, DARK, 1) + rect(98, 48, 4, 13, DARK, "none", 0, 1) + circle(100, 66, 2.3, DARK)
    return out


def tw_reviewer2():
    out = circle(74, 78, 46, "#0f172a66", INK, 3.5)
    out += line([(44, 60), (66, 68)], INK, 4.5) + line([(104, 60), (82, 68)], INK, 4.5)
    out += circle(56, 76, 9, "none", INK, 2.5) + circle(92, 76, 9, "none", INK, 2.5) + line([(65, 76), (83, 76)], INK, 2.5)
    out += circle(56, 77, 3, INK) + circle(92, 77, 3, INK)
    out += path("M54,108 Q74,94 94,108", INK, 3.5)
    out += path("M104,40 q6,-6 12,0 q6,6 12,0", DIM, 2)
    # red pen
    pen = rect(-5, -34, 10, 56, HOT, DARK, 1.5, 2) + poly([(-5, 22), (5, 22), (0, 34)], INK) + rect(-5, -34, 10, 10, DARK, "none", 0, 1)
    out += g(pen, 30, 0, 0, 120, 112)
    out += path("M100,138 q10,-8 20,0 t20,0", HOT, 3)
    return out + text(164, 92, "2", 92, HOT, weight=800)


def tw_replication():
    # classical column cracking, roof tilting, fragments falling
    out = line([(14, 136), (186, 136)], INK, 3) + rect(56, 124, 88, 12, "none", INK, 3, 1)
    out += g(poly([(46, 30), (100, 10), (154, 30)], "#0f172a66", INK, 3) + rect(48, 30, 104, 12, "#0f172a66", INK, 3, 1), 7, 100, 36)
    out += rect(68, 48, 64, 8, "none", INK, 3, 1)
    out += path("M74,56 V124 M126,56 V124", INK, 3)
    out += "".join(line([(84 + k * 11, 62), (84 + k * 11, 118)], DIM, 2) for k in range(4))
    out += line([(102, 56), (92, 72), (110, 84), (94, 98), (106, 110), (98, 124)], HOT, 4)
    out += poly([(150, 92), (160, 88), (158, 98)], INK) + poly([(160, 112), (170, 110), (166, 120)], INK) + poly([(146, 120), (152, 116), (154, 124)], DIM)
    out += flask(30, 98, 0.8) + line([(28, 82), (36, 100), (30, 108)], HOT, 2.5)
    return out


def tw_open_prize():
    out = path("M68,24 H132 V58 Q132,92 100,96 Q68,92 68,58 Z", ACC, 3, fill="#FCD34D")
    out += path("M68,34 H48 Q46,62 72,70 M132,34 H152 Q154,62 128,70", ACC, 4)
    out += rect(92, 96, 16, 16, ACC, "none", 0, 1) + rect(72, 112, 56, 14, ACC, "none", 0, 3)
    # unlocked padlock emblem
    out += rect(88, 48, 24, 20, DARK, "none", 0, 3) + path("M92,48 V40 a8,8 0 0 1 16,0 V36", DARK, 3.5)
    out += circle(100, 56, 3, ACC) + line([(100, 56), (100, 62)], ACC, 2.5)
    out += star(36, 30, 7, INK) + star(168, 40, 9, INK) + star(158, 108, 6, ACC) + star(40, 104, 5, ACC)
    return out + line([(20, 134), (180, 134)], DIM, 2)


TWIST_ART = {
    "T01": tw_ethics_no, "T02": tw_funding_cut, "T03": tw_rarer, "T04": tw_registry,
    "T05": tw_threshold, "T06": tw_rollout, "T07": tw_talk, "T08": tw_only_one,
    "T09": tw_thirty, "T10": tw_fog, "T11": tw_slow_burn, "T12": tw_brief_trigger,
    "T13": tw_few_exposed, "T14": tw_reviewer2, "T15": tw_replication, "T16": tw_open_prize,
}


# --------------------------------------------------------------------------- programmes
def pr_teens():
    out = ""
    for k, (x, glow) in enumerate(((44, COOL), (100, ACC), (156, COOL))):
        out += person(x, 108, 2.0, INK)
        out += phone(x + (6 if k != 1 else 0), 104, 13, 21, (-14 if k == 0 else 14 if k == 2 else 0), glow)
        out += path(f"M{x - 10},96 Q{x - 4},110 {x + 4},108", DARK, 2.5)
    out += bubble(18, 18, 30, 20, INK, "#0f172a66") + heart(33, 28, 0.8)
    out += bubble(152, 18, 30, 20, INK, "#0f172a66", "right") + text(167, 33, "99+", 11, ACC)
    out += cloud(102, 40, 1.0, DIM, "#0f172a55", 2) + "".join(line([(x, 46), (x - 2, 54)], COOL, 2) for x in (90, 98, 106))
    return out + line([(10, 136), (190, 136)], DIM, 2)


def pr_microplastics():
    r = lcg(55)
    out = path("M0,30 C50,18 120,44 200,28 V122 C120,138 50,112 0,124 Z", "none", 0, fill="#FB718522")
    out += path("M0,30 C50,18 120,44 200,28", HOT, 4) + path("M0,124 C50,112 120,138 200,122", HOT, 4)
    for x, y, rot in ((30, 64, 20), (66, 98, -15), (104, 62, 40), (150, 92, -30), (176, 56, 10), (122, 112, 0)):
        out += g(ellipse(x, y, 13, 9, HOT, "#be123c", 1.5) + ellipse(x, y, 6, 3.5, "#be123c", o=.7), rot, x, y)
    cols = (COOL, ACC, INK, "#C4B5FD")
    for k in range(13):
        x, y = 16 + r() * 168, 46 + r() * 64
        n = 3 + int(r() * 3)
        s = 3 + r() * 3
        pts = [(x + s * (0.6 + r() * .6) * math.cos(i * 2 * math.pi / n + r()), y + s * (0.6 + r() * .6) * math.sin(i * 2 * math.pi / n + r())) for i in range(n)]
        out += poly(pts, cols[k % 4])
    return out + arrow(18, 140, 70, 140, DIM, 2.5, head=6) + text(184, 146, "PARTICLES", 11, COOL, "end")


def pr_gripper():
    out = rect(84, 4, 32, 14, "#0f172a66", INK, 3, 2) + rect(94, 18, 12, 18, INK, INK, 0, 2)
    out += rect(74, 36, 52, 12, INK, INK, 0, 4)
    # soft bellows fingers curling around the fruit
    for sg in (-1, 1):
        x0 = 100 + sg * 22
        pts = []
        for k in range(9):
            t = k / 8
            ang = math.radians(10 + 70 * t)
            bx = x0 + sg * 18 * math.sin(ang * 1.1) - sg * 26 * t * t
            by = 48 + 62 * t
            pts.append((bx, by))
        out += line(pts, COOL, 13)
        out += "".join(line([(px - 6, py), (px + 6, py)], "#0369a1", 2) for px, py in pts[1:-1:1])
    # strawberry
    out += path("M100,128 C78,118 72,88 82,78 C90,72 110,72 118,78 C128,88 122,118 100,128 Z", HOT, 2.5, fill=HOT)
    out += "".join(ellipse(x, y, 1.4, 2.2, ACC) for x, y in ((88, 88), (100, 86), (112, 88), (92, 100), (106, 100), (98, 112), (112, 104)))
    out += poly([(100, 80), (88, 70), (96, 74), (100, 64), (104, 74), (112, 70)], GREEN)
    out += path("M18,140 H182", DIM, 2) + check(40, 120, 10, GREEN) + text(40, 100, "NO BRUISE", 10, GREEN)
    return out


def pr_four_day():
    out = rect(14, 26, 172, 106, "#0f172a44", INK, 3, 5) + rect(14, 26, 172, 22, INK, INK, 0, 5) + rect(14, 40, 172, 8, INK, INK, 0, 0)
    for x in (40, 160):
        out += rect(x - 3, 16, 6, 18, ACC, "none", 0, 3)
    days = "MTWTF"
    for k, d in enumerate(days):
        x = 20 + k * 33
        out += text(x + 14, 43, d, 14, DARK)
        if k < 4:
            out += rect(x, 56, 28, 68, "none", DIM, 2, 3)
            out += rect(x + 6, 82, 16, 12, "none", INK, 2.5, 2) + path(f"M{x + 10},82 v-4 h8 v4", INK, 2)
            out += line([(x + 6, 104), (x + 22, 104)], DIM, 2) + line([(x + 6, 112), (x + 18, 112)], DIM, 2)
        else:
            out += rect(x - 2, 54, 34, 72, "#FCD34D33", ACC, 2.5, 3)
            out += sun(x + 15, 90, 9, ACC, 8, 5, 2.5)
            out += line([(x + 2, 58), (x + 28, 122)], HOT, 3)
    return out + text(184, 146, "32 HOURS", 11, ACC, "end")


def pr_post_viral():
    # virus particle
    vx, vy, vr = 50, 54, 22
    out = ""
    for k in range(12):
        a = k * 2 * math.pi / 12
        out += line([(vx + vr * math.cos(a), vy + vr * math.sin(a)), (vx + (vr + 9) * math.cos(a), vy + (vr + 9) * math.sin(a))], HOT, 3)
        out += circle(vx + (vr + 11) * math.cos(a), vy + (vr + 11) * math.sin(a), 3.5, HOT)
    out += circle(vx, vy, vr, "#FB718555", HOT, 3) + circle(vx - 7, vy - 4, 4, HOT) + circle(vx + 8, vy + 6, 3, HOT) + circle(vx + 4, vy - 9, 2.5, HOT)
    out += path("M84,74 Q100,92 104,96", DIM, 2.5, dash="4 5")
    # tired figure: slumped seated person
    out += line([(98, 136), (190, 136)], DIM, 2)
    out += path("M128,106 Q116,118 122,132", INK, 15)
    out += path("M122,132 L150,116 L160,134 H168", INK, 9)
    out += path("M134,108 Q146,116 152,118", INK, 5)
    out += circle(140, 102, 8, INK)
    # battery low + fog
    out += rect(150, 34, 32, 16, "none", INK, 2.5, 2) + rect(182, 39, 4, 6, INK, "none", 0, 1) + rect(154, 38, 6, 8, HOT, "none", 0, 1)
    out += cloud(126, 78, 0.9, DIM, "#e2e8f033", 2) + text(160, 96, "Z", 13, DIM) + text(170, 84, "Z", 11, DIM)
    return out + text(50, 116, "MONTHS LATER", 11, DIM)


def pr_ai_triage():
    out = rect(12, 18, 116, 82, "#0f172a99", INK, 3, 5) + rect(56, 100, 28, 10, INK, INK, 0, 1) + rect(42, 110, 56, 6, INK, INK, 0, 3)
    pts = [(18, 64), (36, 64), (42, 58), (48, 64), (56, 64), (60, 40), (66, 82), (72, 60), (80, 64), (96, 64), (100, 56), (106, 64), (122, 64)]
    out += line(pts, GREEN, 2.5)
    out += text(22, 36, "HR 128", 12, INK, "start") + text(122, 36, "SpO2 89", 12, HOT, "end")
    out += text(22, 92, "BP 92/58", 11, DIM, "start") + circle(116, 88, 5, HOT)
    # AI chip
    cx, cy = 160, 64
    out += rect(cx - 20, cy - 20, 40, 40, DARK, ACC, 3, 4)
    for k in range(4):
        o = -12 + k * 8
        out += line([(cx + o, cy - 20), (cx + o, cy - 28)], ACC, 2.5) + line([(cx + o, cy + 20), (cx + o, cy + 28)], ACC, 2.5)
        out += line([(cx - 20, cy + o), (cx - 28, cy + o)], ACC, 2.5) + line([(cx + 20, cy + o), (cx + 28, cy + o)], ACC, 2.5)
    out += text(cx, cy + 7, "AI", 20, ACC)
    out += line([(128, 64), (132, 64)], ACC, 2.5)
    # alert flag
    out += rect(138, 108, 46, 24, HOT, "none", 0, 4) + text(161, 125, "ICU?", 14, DARK)
    out += line([(160, 92), (160, 108)], HOT, 2.5, "3 3")
    return out + line([(10, 138), (190, 138)], DIM, 2)


PROGRAM_ART = {
    "P1": pr_teens, "P2": pr_microplastics, "P3": pr_gripper,
    "P4": pr_four_day, "P5": pr_post_viral, "P6": pr_ai_triage,
}
