"""Vector art for the 28 Threat cards (same kit and style rules as art.py)."""
from art import *
import math

DARK = "#0f172a"


# --------------------------------------------------------------------------- local helpers
def _qpt(p0, p1, p2, t):
    return ((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
            (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])


def _smooth(pts):
    """Catmull-Rom spline through all points, as an SVG path d string."""
    d = f"M{pts[0][0]:.1f},{pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d


def _sparkle(x, y, r=7, c=ACC):
    return star(x, y, r, c, pts=4)


def _drop(x, y, s=1.0, c=COOL, o=1):
    return path(f"M{x:.1f},{y - 9 * s:.1f} C{x + 7 * s:.1f},{y:.1f} {x + 6 * s:.1f},{y + 7 * s:.1f} {x:.1f},{y + 7 * s:.1f} "
                f"C{x - 6 * s:.1f},{y + 7 * s:.1f} {x - 7 * s:.1f},{y:.1f} {x:.1f},{y - 9 * s:.1f} Z", c, 1, fill=c, o=o)


def _target(x, y, r, c=INK, centre=ACC, rings=3, fill="none"):
    out = circle(x, y, r, fill, c, 3)
    for k in range(1, rings):
        out += circle(x, y, r * (1 - k / rings), "none", c, 2.5)
    return out + circle(x, y, r / rings * 0.6, centre)


# --------------------------------------------------------------------------- threats
def art_confounding():
    out = circle(100, 34, 20, "#0f172a88", HOT, 2.5, dash="4 3") + text(100, 41, "U", 20, HOT)
    out += arrow(84, 48, 52, 92, HOT, 3) + arrow(116, 48, 148, 92, HOT, 3)
    out += node(40, 110, "X", 17, DARK, size=16) + node(160, 110, "Y", 17, DARK, size=16)
    out += arrow(60, 110, 138, 110, ACC, 3, "6 6") + text(100, 136, "?", 22, ACC)
    return out


def art_confounding_indication():
    out = line([(24, 54), (24, 128)], INK, 4) + line([(176, 84), (176, 128)], INK, 4)
    out += line([(24, 104), (176, 104)], INK, 3) + line([(24, 114), (176, 114)], INK, 3)
    out += f'<ellipse cx="46" cy="94" rx="16" ry="8" fill="{DARK}55" stroke="{INK}" stroke-width="2.5"/>'
    out += circle(50, 80, 11, INK)
    out += path("M60,100 Q64,80 90,82 L172,84 V104 H60 Z", INK, 3, fill="#0f172a66")
    out += line([(58, 84), (74, 74)], HOT, 3) + circle(75, 73, 3, HOT)
    out += "".join(path(f"M{x},62 q-4,-6 0,-11 q4,-5 0,-11", HOT, 2.5) for x in (40, 52, 64))
    out += pill(142, 48, 46, 18, -25) + _sparkle(170, 30, 6) + _sparkle(116, 34, 4)
    return out


def art_selection_bias():
    cols = [INK, ACC, INK, ACC, INK, INK, ACC]
    out = "".join(person(34 + i * 22, 28, 0.75, c) for i, c in enumerate(cols))
    out += path("M22,52 H178 L118,92 V104 H82 V92 Z", INK, 3, fill="#0f172a44")
    out += "".join(line([(34 + k * 18, 56), (34 + k * 18 + 10, 60)], DIM, 2) for k in range(8))
    out += line([(54, 68), (146, 68)], DIM, 2, "3 4") + line([(72, 80), (128, 80)], DIM, 2, "3 4")
    out += cross(22, 82, 6) + cross(178, 82, 6)
    return out + "".join(person(80 + i * 20, 126, 0.75, ACC) for i in range(3))


def art_attrition():
    out = line([(12, 118), (188, 118)], DIM, 2)
    out += rect(150, 30, 36, 88, DARK + "aa", INK, 3, 2) + path("M150,30 L136,40 V122 L150,118", INK, 2.5, fill="#0f172a44")
    out += circle(142, 80, 2.5, ACC)
    for k, o in enumerate((1, .85, .65, .45, .28)):
        out += person(22 + k * 25, 98, 1.3, INK, o)
    return out + person(146, 100, 1.1, INK, .14) + arrow(30, 132, 126, 132, DIM, 2)


def art_recall_bias():
    out = person(44, 110, 2.1)
    out += circle(66, 74, 3.5, INK, o=.7) + circle(76, 62, 5.5, INK, o=.7)
    blobs = ((112, 54, 24), (140, 44, 24), (166, 56, 20), (128, 72, 22), (156, 76, 20), (98, 70, 16))
    out += '<g opacity=".32">' + "".join(circle(x, y, r, INK) for x, y, r in blobs) + "</g>"
    out += text(134, 76, "?", 44, ACC)
    out += "".join(path(f"M{x0},{y} q8,-5 16,0 t16,0 t16,0 t16,0", INK, 2, o=.55) for x0, y in ((92, 34), (104, 96), (120, 22)))
    return out


def art_measurement_error():
    out = _target(72, 76, 52, INK, ACC, 3)
    r = lcg(11)
    for _ in range(9):
        x, y = 92 + (r() - .5) * 46, 54 + (r() - .5) * 42
        out += circle(x, y, 4.2, DARK, HOT, 2.5)
    a, b, c_ = (152, 18), (186, 76), (152, 134)
    out += path(f"M152,18 Q186,76 152,134 L170,134 Q204,76 170,18 Z", INK, 2.5, fill="#0f172a55")
    for k in range(1, 12):
        x, y = _qpt(a, b, c_, k / 12)
        out += line([(x, y), (x + (8 if k % 3 == 0 else 5), y)], ACC if k % 3 == 0 else INK, 2)
    return out


def art_reverse_causation():
    out = node(46, 104, "X", 19, DARK, size=18) + node(154, 104, "Y", 19, DARK, size=18)
    out += arrow(68, 104, 132, 104, DIM, 2.5, "5 5") + cross(100, 104, 6)
    out += carrow(154, 82, 100, -12, 52, 80, ACC, 5, head=12)
    return out


def art_regression_mean():
    r = lcg(13)
    cloud = [(16 + r() * 168, 76 + (r() + r() + r() - 1.5) * 30) for _ in range(40)]
    out = scatter(cloud, 2.2, DIM) + line([(14, 76), (186, 76)], ACC, 3, "8 5") + text(186, 70, "AVG", 11, ACC, "end")
    for x, up in ((40, True), (78, False), (122, True), (160, False)):
        y0, y1 = (20, 62) if up else (132, 90)
        out += circle(x, y0, 7, HOT, INK, 2) + arrow(x, y0 + (10 if up else -10), x, y1 + (-8 if up else 8), INK, 3, head=8)
        out += circle(x, y1, 5.5, INK)
    return out


def art_expectation():
    out = pill(76, 92, 92, 34, -28)
    out += _sparkle(34, 56, 9) + _sparkle(126, 112, 7) + _sparkle(52, 128, 5) + _sparkle(118, 58, 6, INK)
    out += eye(152, 38, 1.05)
    out += line([(138, 54), (110, 74)], DIM, 2, "3 4") + line([(152, 58), (132, 86)], DIM, 2, "3 4")
    return out


def art_contamination():
    out = rect(94, 18, 12, 46, DARK + "88", INK, 2.5, 2) + rect(94, 90, 12, 46, DARK + "88", INK, 2.5, 2)
    out += "".join(line([(94, y), (106, y)], DIM, 1.5) for y in (30, 42, 54, 102, 114, 126))
    out += crowd(26, 46, 2, 3, 26, 36, 0.85, lambda i, j: ACC)
    out += crowd(148, 46, 2, 3, 26, 36, 0.85, lambda i, j: ACC if (i, j) in ((0, 1), (1, 2)) else INK)
    out += scatter([(70, 77), (82, 75), (94, 78), (106, 76), (118, 78), (128, 74)], 3.2, ACC)
    return out + arrow(60, 77, 138, 77, ACC, 2, "3 6", head=7)


def art_immortal_time():
    out = arrow(14, 110, 188, 110, INK, 3)
    out += rect(30, 98, 74, 24, ACC, "none", 0, 2, o=.3)
    out += "".join(line([(34 + k * 10, 120), (42 + k * 10, 100)], ACC, 2, o=.8) for k in range(7))
    out += line([(30, 96), (30, 124)], INK, 2.5) + line([(104, 96), (104, 124)], INK, 2.5)
    out += path("M67,24 L94,34 V56 Q94,76 67,88 Q40,76 40,56 V34 Z", INK, 3, fill="#0f172a55") + star(67, 56, 13, ACC)
    out += pill(130, 92, 30, 12, 0) + bolt(168, 92, 0.9, HOT)
    return out


def art_collider():
    out = rect(76, 16, 48, 40, DARK + "88", ACC, 3, 4) + "".join(line([(86 + k * 10, 20), (86 + k * 10, 52)], ACC, 2) for k in range(3))
    out += node(38, 112, "X", 17, DARK, size=16) + node(162, 112, "Y", 17, DARK, size=16)
    out += arrow(50, 98, 80, 60, INK, 3) + arrow(150, 98, 120, 60, INK, 3)
    out += line([(58, 112), (142, 112)], HOT, 3, "6 6") + text(100, 102, "?", 20, HOT)
    return out


def art_ecological_fallacy():
    out = axes(16, 14, 174, 120)
    out += arrow(30, 124, 184, 28, ACC, 3, "7 5")
    for k, (x, y) in enumerate(((54, 104), (104, 76), (154, 48))):
        out += f'<ellipse cx="{x}" cy="{y}" rx="26" ry="20" fill="#0f172a55" stroke="{INK}" stroke-width="2.5"/>'
        pts = [(x - 14 + i * 7, y - 9 + i * 4.5) for i in range(5)]
        out += scatter(pts, 2.6, INK) + arrow(x - 16, y - 12, x + 17, y + 11, HOT, 2.5, head=6)
    return out


def art_unit_of_analysis():
    out = ""
    for k, x in enumerate((14, 60)):
        out += building(x, 34, 38, 54, INK, "#0f172a55", 14)
        out += "".join(circle(x + 9 + (i % 3) * 10, 58 + (i // 3) * 9, 2.4, ACC) for i in range(9))
    out += arrow(106, 64, 128, 64, INK, 3)
    r = lcg(5)
    pts = [(136 + (i % 6) * 9 + (r() - .5) * 4, 30 + (i // 6) * 11 + (r() - .5) * 4) for i in range(36)]
    out += scatter(pts, 2.4, INK)
    return out + text(160, 116, "N = 360", 15, HOT) + text(56, 116, "2 SCHOOLS", 11, DIM)


def art_survivorship():
    body = ("M16,75 Q16,69 28,69 L84,69 L100,18 H114 L110,69 H158 L168,52 H180 L176,75 L180,98 H168 L158,81 "
            "H110 L114,132 H100 L84,81 L28,81 Q16,81 16,75 Z")
    out = path(body, INK, 3, fill="#0f172a55")
    out += rect(92, 38, 10, 14, DARK, INK, 2, 2) + rect(92, 98, 10, 14, DARK, INK, 2, 2)
    holes = [(104, 30), (101, 46), (106, 56), (99, 62), (108, 92), (102, 106), (106, 120), (98, 96),
             (164, 62), (170, 88), (172, 74), (136, 72), (148, 78), (60, 74)]
    return out + "".join(circle(x, y, 2.6, HOT) for x, y in holes)


def art_publication_bias():
    out = rect(96, 50, 74, 88, "#0f172a55", INK, 3, 3) + line([(96, 94), (170, 94)], INK, 2.5)
    out += line([(124, 116), (142, 116)], INK, 3)
    for k, (x, rot) in enumerate(((40, -14), (52, -4), (64, 8), (74, -10), (84, 4))):
        out += (f'<g transform="rotate({rot} {x} 70)">' + rect(x - 9, 48, 20, 28, "#e2e8f0", "none", 0, 1)
                + line([(x - 5, 54), (x + 6, 54)], DIM, 1.5) + "</g>")
    out += rect(28, 62, 70, 32, DARK + "aa", INK, 3, 2) + line([(54, 78), (72, 78)], INK, 3)
    out += path("M98,62 L96,66 M98,94 L96,90", INK, 2)
    out += rect(108, 30, 54, 18, ACC, "none", 0, 2) + line([(108, 44), (162, 44)], "#0f172a55", 2)
    out += _sparkle(170, 22, 8, INK) + _sparkle(102, 24, 5, INK) + text(133, 40, "", 1)
    return out


def art_forking_paths():
    root = (100, 140)
    xs3 = [16 + k * 24 for k in range(8)]
    lv1 = [(60, 104), (140, 104)]
    lv2 = [(36, 70), (84, 70), (116, 70), (164, 70)]
    lv3 = [(x, 36) for x in xs3]
    chosen = (0, 1, 3)
    out = ""
    for i, p in enumerate(lv1):
        out += path(f"M{root[0]},{root[1]} Q{p[0]},{root[1] - 6} {p[0]},{p[1]}", INK, 3)
        for j in range(2):
            q = lv2[i * 2 + j]
            out += path(f"M{p[0]},{p[1]} Q{q[0]},{p[1] - 4} {q[0]},{q[1]}", INK, 2.5)
            for m in range(2):
                r_ = lv3[(i * 2 + j) * 2 + m]
                out += path(f"M{q[0]},{q[1]} Q{r_[0]},{q[1] - 4} {r_[0]},{r_[1]}", INK, 2)
                if (i * 2 + j) * 2 + m != 3:
                    out += circle(r_[0], r_[1], 3.5, DIM)
    p, q, r_ = lv1[0], lv2[1], lv3[3]
    out += path(f"M{root[0]},{root[1]} Q{p[0]},{root[1] - 6} {p[0]},{p[1]}", ACC, 4)
    out += path(f"M{p[0]},{p[1]} Q{q[0]},{p[1] - 4} {q[0]},{q[1]}", ACC, 4)
    out += path(f"M{q[0]},{q[1]} Q{r_[0]},{q[1] - 4} {r_[0]},{r_[1]}", ACC, 4)
    out += star(r_[0], r_[1] - 4, 11, ACC) + text(r_[0] + 14, 22, "p<.05", 13, ACC, "start")
    return out + circle(root[0], root[1] - 2, 4, INK)


def art_low_power():
    r = lcg(21)
    out = scatter([(14 + r() * 172, 16 + r() * 118) for _ in range(70)], 1.8, DIM)
    out += path("M24,108 L46,110 L110,62 L114,86 Z", INK, 0, fill="rgba(248,250,252,.22)")
    out += f'<g transform="rotate(-36 30 110)">' + rect(6, 104, 24, 12, INK, INK, 0, 3) + rect(28, 101, 8, 18, INK, INK, 0, 2) + "</g>"
    out += star(160, 52, 12, ACC) + circle(160, 52, 22, "none", ACC, 2, dash="3 4")
    return out + cross(124, 74, 6)


def art_overfitting_leakage():
    r = lcg(8)
    pts = [(22 + k * 15, 98 - k * 4 + (r() - .5) * 46) for k in range(11)]
    out = axes(12, 16, 178, 118, DIM, 2)
    out += path(_smooth(pts), ACC, 3) + scatter(pts, 3.6, INK)
    out += path("M128,14 H170 Q180,14 180,24 V36", INK, 6) + rect(173, 34, 14, 6, INK, INK, 0, 1)
    out += _drop(180, 52, 0.75, COOL) + _drop(180, 72, 0.6, COOL, .7)
    return out


def art_spectrum_bias():
    n = 12
    out = ""
    for k in range(n):
        t = k / (n - 1)
        c = "#%02x%02x%02x" % tuple(round(a + (b - a) * t) for a, b in ((0x7D, 0xFB), (0xD3, 0x71), (0xFC, 0x85)))
        out += rect(18 + k * 14, 66, 13, 24, c, "none", 0, 1, o=1 if k < 2 or k > 9 else .45)
    out += path("M14,58 V96 M14,58 H22 M14,96 H22 M50,58 V96 M50,58 H42 M50,96 H42", ACC, 3)
    out += path("M150,58 V96 M150,58 H158 M150,96 H158 M186,58 V96 M186,58 H178 M186,96 H178", ACC, 3)
    out += person(32, 36, 1.1, INK) + person(168, 36, 1.1, INK) + bolt(184, 28, .6, HOT)
    out += person(100, 36, 1.1, INK, .35) + person(78, 38, .9, INK, .25) + person(122, 38, .9, INK, .25)
    return out + text(100, 120, "?", 26, DIM)


def art_history_trend():
    pts = [(22 + k * 16, 40 + k * 8 + (3 if k % 2 else -3)) for k in range(11)]
    out = axes(14, 14, 176, 120) + line([(100, 18), (100, 128)], DIM, 2, "4 4")
    out += line(pts, INK, 3) + scatter(pts, 3, INK)
    out += line([(100, 74), (100, 30)], INK, 3) + path("M100,30 L132,38 L100,48 Z", ACC, 2, fill=ACC)
    return out


def art_carryover():
    out = rect(18, 40, 76, 62, ACC, "none", 0, 4) + rect(106, 40, 76, 62, COOL, "none", 0, 4)
    for k, (w, o) in enumerate(((40, .85), (28, .7), (18, .55))):
        y = 46 + k * 18
        out += path(f"M94,{y} H{106 + w} q6,0 6,6 q0,6 -6,6 H94 Z", ACC, 0, fill=ACC, o=o)
    out += _drop(140, 116, 0.7, ACC, .6) + line([(140, 102), (140, 108)], ACC, 3, o=.6)
    out += text(48, 82, "A", 30, DARK) + text(164, 82, "B", 30, DARK)
    return out + arrow(18, 136, 182, 136, DIM, 2.5)


def art_researcher_lens():
    out = eye(32, 75, 0.85)
    out += path("M66,62 L188,18 V132 L66,88 Z", "none", 0, fill="rgba(252,211,77,.18)")
    out += f'<ellipse cx="62" cy="75" rx="9" ry="22" fill="rgba(252,211,77,.55)" stroke="{INK}" stroke-width="3"/>'
    out += line([(62, 53), (52, 44)], INK, 2.5)
    shapes = [(110, 56), (122, 92), (148, 44), (160, 76), (150, 110), (176, 100)]
    for k, (x, y) in enumerate(shapes):
        out += rect(x - 6, y - 6, 12, 12, ACC, "none", 0, 2) if k % 2 else circle(x, y, 6.5, ACC)
    out += circle(120, 136, 6, INK) + rect(168, 132, 12, 12, INK, "none", 0, 2) + circle(176, 16, 6, INK, o=0)
    return out + rect(100, 12, 12, 12, INK, "none", 0, 2)


def art_external_validity():
    out = path("M24,62 Q18,62 18,70 Q10,124 54,128 Q98,124 90,70 Q90,62 84,62", INK, 3, fill="#0f172a44")
    out += path("M18,82 Q54,78 90,82 Q96,124 54,126 Q12,124 18,82 Z", COOL, 0, fill="rgba(125,211,252,.35)")
    out += path("M44,104 q10,-10 20,0 q-10,10 -20,0 z", ACC, 2, fill=ACC) + line([(44, 104), (36, 98), (36, 110), (44, 104)], ACC, 2, fill=ACC, close=True)
    out += circle(58, 102, 1.5, DARK)
    out += text(110, 92, "≠", 34, INK)
    return out + globe(156, 80, 32) + circle(156, 80, 32, "none", ACC, 0)


def art_heterogeneity():
    out = path("M54,52 C40,40 18,48 18,74 C18,104 38,124 54,116 C70,124 90,104 90,74 C90,48 68,40 54,52 Z", INK, 3, fill=HOT)
    out += path("M54,52 Q52,40 58,32", INK, 3) + path("M58,40 Q72,28 80,38 Q68,46 58,40 Z", "#86EFAC", 2, fill="#86EFAC")
    out += circle(150, 80, 36, "#FDBA74", INK, 3)
    r = lcg(2)
    out += scatter([(150 + (r() - .5) * 46, 80 + (r() - .5) * 46) for _ in range(14)], 1.3, "#c2410c")
    out += circle(150, 46, 3, "#86EFAC") + path("M120,36 Q122,30 128,32", INK, 0)
    return out + text(103, 92, "+", 30, INK) + text(100, 140, "AVERAGE = ?", 12, ACC)


def art_model_assumptions():
    out = line([(14, 134), (186, 134)], DIM, 2)

    def card(x1, y1, x2, y2, c=INK):
        return line([(x1, y1), (x2, y2)], DARK, 8) + line([(x1, y1), (x2, y2)], c, 5)
    for k in range(3):
        x = 34 + k * 46
        out += card(x, 130, x + 16, 96) + (card(x + 32, 130, x + 16, 96) if k < 2 else card(x + 44, 132, x + 32, 104, HOT))
    out += card(36, 92, 152, 92, ACC)
    for k in range(2):
        x = 56 + k * 46
        out += card(x, 88, x + 16, 56) + card(x + 32, 88, x + 16, 56)
    out += card(58, 52, 128, 52, ACC) + card(80, 48, 96, 18) + card(112, 48, 96, 18)
    return out + path("M176,96 q6,6 4,14 M184,90 q7,8 5,18", HOT, 2.5)


def art_construct_validity():
    out = line([(70, 104), (70, 136)], DIM, 3) + line([(58, 136), (82, 136)], DIM, 3)
    out += rect(36, 34, 68, 72, "#0f172a55", DIM, 2.5, 4) + _target(70, 70, 28, DIM, DIM, 3)
    out += _target(154, 70, 30, INK, ACC, 3) + star(154, 24, 9, ACC)
    out += arrow(12, 128, 66, 74, INK, 3, head=10) + path("M14,126 l-6,2 M18,122 l-6,2", INK, 2)
    return out + text(70, 26, "PROXY", 11, DIM)


def art_thin_data():
    out = axes(14, 14, 176, 120)
    pts = [(48, 112), (70, 104), (88, 98)]
    out += path("M28,122 C70,108 92,96 120,70 S166,20 184,16", ACC, 4) + line([(176, 14), (186, 16), (178, 24)], ACC, 3)
    out += scatter(pts, 5, INK)
    return out + text(150, 112, "N = 3", 16, HOT)


THREAT_ART = {
    "confounding": art_confounding,
    "confounding-indication": art_confounding_indication,
    "selection-bias": art_selection_bias,
    "attrition": art_attrition,
    "recall-bias": art_recall_bias,
    "measurement-error": art_measurement_error,
    "reverse-causation": art_reverse_causation,
    "regression-mean": art_regression_mean,
    "expectation": art_expectation,
    "contamination": art_contamination,
    "immortal-time": art_immortal_time,
    "collider": art_collider,
    "ecological-fallacy": art_ecological_fallacy,
    "unit-of-analysis": art_unit_of_analysis,
    "survivorship": art_survivorship,
    "publication-bias": art_publication_bias,
    "forking-paths": art_forking_paths,
    "low-power": art_low_power,
    "overfitting-leakage": art_overfitting_leakage,
    "spectrum-bias": art_spectrum_bias,
    "history-trend": art_history_trend,
    "carryover": art_carryover,
    "researcher-lens": art_researcher_lens,
    "external-validity": art_external_validity,
    "heterogeneity": art_heterogeneity,
    "model-assumptions": art_model_assumptions,
    "construct-validity": art_construct_validity,
    "thin-data": art_thin_data,
}
