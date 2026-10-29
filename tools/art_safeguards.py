"""Vector art for the 32 Safeguard cards (same kit and style rules as art.py)."""
from art import *
import math

DARK = "#0f172a"
OK = "#BBF7D0"  # light green check, readable on the emerald safeguard background


# --------------------------------------------------------------------------- local helpers
def _person_outline(x, y, s=1.0, c=INK, dash="3 3", w=2):
    return (circle(x, y - 9 * s, 4.3 * s, "none", c, w, dash=dash)
            + path(f"M{x - 7 * s:.1f},{y + 9 * s:.1f} V{y + 2 * s:.1f} Q{x - 7 * s:.1f},{y - 3 * s:.1f} {x:.1f},{y - 3 * s:.1f} "
                   f"Q{x + 7 * s:.1f},{y - 3 * s:.1f} {x + 7 * s:.1f},{y + 2 * s:.1f} V{y + 9 * s:.1f} Z", c, w, dash=dash))


def _drop(x, y, s=1.0, c=COOL, o=1):
    return path(f"M{x:.1f},{y - 9 * s:.1f} C{x + 7 * s:.1f},{y:.1f} {x + 6 * s:.1f},{y + 7 * s:.1f} {x:.1f},{y + 7 * s:.1f} "
                f"C{x - 6 * s:.1f},{y + 7 * s:.1f} {x - 7 * s:.1f},{y:.1f} {x:.1f},{y - 9 * s:.1f} Z", c, 1, fill=c, o=o)


def _bell(x0, mu, sd, base, h, c, w=3, fill="none", o=1):
    pts = []
    for k in range(41):
        x = mu - 3 * sd + k * 6 * sd / 40
        pts.append((x, base - h * math.exp(-((x - mu) / sd) ** 2 / 2)))
    return line(pts, c, w, fill=fill, o=o)


def _runner(x, y, s=1.0, c=INK):
    """Stick runner mid-stride, hips at (x, y)."""
    return (circle(x + 4 * s, y - 24 * s, 5 * s, c)
            + line([(x, y), (x + 3 * s, y - 16 * s)], c, 4 * s)
            + line([(x + 3 * s, y - 14 * s), (x + 12 * s, y - 8 * s), (x + 16 * s, y - 14 * s)], c, 3 * s)
            + line([(x + 2 * s, y - 14 * s), (x - 6 * s, y - 10 * s), (x - 10 * s, y - 4 * s)], c, 3 * s)
            + line([(x, y), (x + 9 * s, y + 7 * s), (x + 8 * s, y + 16 * s)], c, 3.5 * s)
            + line([(x, y), (x - 6 * s, y + 9 * s), (x - 14 * s, y + 11 * s)], c, 3.5 * s))


def _bottle(x, y, w=26, h=34, c=INK, label=ACC):
    return (rect(x - w / 2, y - h / 2, w, h, "#0f172a55", c, 2.5, 4) + rect(x - w / 2 - 2, y - h / 2 - 9, w + 4, 9, c, c, 0, 2)
            + rect(x - w / 2 + 4, y - 6, w - 8, 12, label, "none", 0, 1))


def _tube(x, y, liquid, h=70, c=INK):
    """Test tube: open top at y, rounded bottom at y + h."""
    lq = path(f"M{x - 10},{y + h * .45} V{y + h - 10} A10,10 0 0 0 {x + 10},{y + h - 10} V{y + h * .45} Z", liquid, 0, fill=liquid, o=.9)
    return (lq + path(f"M{x - 10},{y} V{y + h - 10} A10,10 0 0 0 {x + 10},{y + h - 10} V{y}", c, 3)
            + line([(x - 15, y), (x + 15, y)], c, 3))


def _map(x, y, w, h, c=INK, fill="#0f172a33"):
    t = w / 3
    out = path(f"M{x},{y + 6} L{x + t},{y} L{x + 2 * t},{y + 6} L{x + w},{y} V{y + h} L{x + 2 * t},{y + h + 6} L{x + t},{y + h} L{x},{y + h + 6} Z", c, 2.5, fill=fill)
    return out + line([(x + t, y), (x + t, y + h)], DIM, 1.5) + line([(x + 2 * t, y + 6), (x + 2 * t, y + h + 6)], DIM, 1.5)


def _pin(x, y, c=ACC):
    return path(f"M{x},{y} c-6,-8 -6,-16 0,-16 c6,0 6,8 0,16 z", c, 2, fill=c) + circle(x, y - 10, 2.5, DARK)


def _padlock(x, y, s=1.0, c=ACC):
    return (path(f"M{x - 8 * s:.1f},{y:.1f} V{y - 7 * s:.1f} A{8 * s:.1f},{8 * s:.1f} 0 0 1 {x + 8 * s:.1f},{y - 7 * s:.1f} V{y:.1f}", c, 3.5 * s)
            + rect(x - 12 * s, y, 24 * s, 20 * s, c, "none", 0, 3) + circle(x, y + 8 * s, 2.6 * s, DARK)
            + line([(x, y + 9 * s), (x, y + 14 * s)], DARK, 2.5 * s))


# --------------------------------------------------------------------------- safeguards
def art_randomization():
    out = dice(72, 82, 54, 5, rot=-16) + dice(140, 70, 44, 3, rot=20)
    out += path("M28,44 Q40,24 62,24", DIM, 2.5) + path("M24,58 Q30,46 42,40", DIM, 2.5)
    out += path("M168,112 Q182,104 184,88", DIM, 2.5)
    return out + line([(20, 128), (180, 128)], DIM, 2)


def art_allocation_concealment():
    out = rect(26, 36, 120, 80, "#0f172a44", INK, 3, 4)
    out += path("M26,40 L86,82 L146,40", INK, 3) + path("M26,114 L72,74 M146,114 L100,74", INK, 2, o=.6)
    out += circle(86, 84, 11, HOT) + circle(86, 84, 6, "none", "#ffffff88", 1.5)
    return out + _padlock(158, 100, 1.3) + text(86, 136, "", 1)


def art_blinding():
    out = circle(100, 70, 40, "#0f172a44", INK, 3)
    out += path("M60,62 Q100,52 140,62 L140,80 Q100,70 60,80 Z", ACC, 2, fill=ACC)
    out += path("M140,68 Q160,64 172,52 M140,74 Q160,80 170,96", ACC, 4)
    out += path("M86,96 Q100,104 114,96", INK, 3) + line([(100, 80), (98, 88)], INK, 2.5)
    out += path("M74,30 Q100,18 126,30", INK, 3, o=0)
    return out + path("M60,120 Q60,110 100,110 Q140,110 140,120 V138 H60 Z", INK, 0, fill=INK, o=0)


def art_placebo_sham():
    out = pill(52, 70, 70, 28, -30) + pill(148, 70, 70, 28, -30)
    out += text(100, 82, "=", 34, INK)
    return out + text(52, 128, "A", 18, DIM) + text(148, 128, "B", 18, DIM) + text(100, 128, "?", 18, DIM)


def art_itt():
    out = circle(100, 76, 60, "#0f172a33", ACC, 3.5)
    pos = [(72, 58), (100, 50), (128, 58), (68, 92), (100, 88), (132, 92), (100, 120)]
    for k, (x, y) in enumerate(pos):
        out += _person_outline(x, y, 1.1, INK, "3 3") if k in (2, 6) else person(x, y, 1.1, INK)
    out += arrow(140, 108, 172, 128, DIM, 2, "4 4", head=6) + cross(176, 132, 6, DIM)
    return out


def art_preregistration():
    out = doc(22, 22, 66, 90, INK, 5, fill="#0f172a55", sw=3)
    out += (f'<g transform="rotate(-14 84 104)">' + rect(52, 88, 64, 30, "#0f172a88", ACC, 3, 4)
            + rect(56, 92, 56, 22, "none", ACC, 1.5, 2) + text(84, 108, "DATED", 14, ACC) + "</g>")
    out += clock(152, 50, 26, INK, -30, 90, 3) + line([(152, 20), (152, 24)], INK, 4) + rect(146, 16, 12, 5, INK, INK, 0, 2)
    out += arrow(132, 96, 172, 96, DIM, 2.5) + cylinder(156, 104, 30, 30, DIM)
    return out


def art_power_analysis():
    out = line([(14, 96), (186, 96)], INK, 2.5)
    out += _bell(0, 66, 18, 96, 70, INK, 3, fill="rgba(248,250,252,.12)") + _bell(0, 134, 18, 96, 70, ACC, 3, fill="rgba(252,211,77,.18)")
    out += line([(66, 20), (66, 96)], DIM, 2, "4 4") + line([(134, 20), (134, 96)], DIM, 2, "4 4")
    out += arrow(80, 16, 120, 16, INK, 2, head=6) + arrow(120, 16, 80, 16, INK, 2, head=6)
    out += "".join(person(30 + i * 14, 126, 0.6, INK) for i in range(10))
    return out + text(178, 132, "N", 20, ACC)


def art_dag_adjustment():
    out = rect(78, 14, 44, 40, "none", ACC, 3.5, 4) + node(100, 34, "C", 14, DARK, size=15)
    out += node(38, 112, "X", 16, DARK, size=16) + node(162, 112, "Y", 16, DARK, size=16)
    out += arrow(86, 56, 50, 96, DIM, 2.5, "5 4") + arrow(114, 56, 150, 96, DIM, 2.5, "5 4")
    return out + arrow(56, 112, 144, 112, INK, 3.5)


def art_matching_ps():
    out = ""
    for k, (y, s) in enumerate(((36, 0.9), (78, 1.25), (120, 1.05))):
        out += person(44, y, s, INK) + person(156, y, s, ACC)
        out += line([(64, y), (136, y)], DIM, 2, "2 5")
        out += f'<ellipse cx="92" cy="{y}" rx="9" ry="5" fill="none" stroke="{ACC}" stroke-width="2.5"/>'
        out += f'<ellipse cx="108" cy="{y}" rx="9" ry="5" fill="none" stroke="{INK}" stroke-width="2.5"/>'
    return out


def art_negative_control():
    out = _tube(64, 30, ACC, 80) + _tube(136, 30, "rgba(248,250,252,.25)", 80)
    out += circle(60, 72, 3, INK) + circle(68, 82, 2.4, INK) + circle(62, 92, 3.4, INK) + circle(66, 60, 2, INK)
    out += bolt(38, 40, .8, ACC) + bolt(90, 50, .6, ACC)
    out += text(136, 26, "∅", 20, INK)
    return out + line([(30, 128), (170, 128)], DIM, 2) + check(160, 76, 10, OK)


def art_sensitivity_analysis():
    out = ""
    for k, a in enumerate((-50, 20, 70)):
        x = 46 + k * 54
        out += circle(x, 44, 20, "#0f172a44", INK, 3)
        out += "".join(circle(x + 24 * math.cos(math.radians(t)), 44 + 24 * math.sin(math.radians(t)), 1.4, DIM) for t in range(-210, 31, 30))
        ar = math.radians(a - 90)
        out += line([(x, 44), (x + 15 * math.cos(ar), 44 + 15 * math.sin(ar))], ACC, 3.5) + circle(x, 44, 3, ACC)
    out += rect(22, 96, 156, 22, "#0f172a44", INK, 3, 11)
    out += f'<ellipse cx="100" cy="107" rx="16" ry="7" fill="{OK}" opacity=".9"/>'
    return out + line([(84, 96), (84, 118)], INK, 2) + line([(116, 96), (116, 118)], INK, 2) + check(176, 136, 8, OK, 3)


def art_active_comparator():
    out = line([(100, 30), (100, 126)], INK, 3.5) + path("M78,130 H122 L114,122 H86 Z", INK, 2, fill=INK)
    out += line([(30, 44), (170, 44)], INK, 3.5) + circle(100, 44, 5, ACC)
    for x in (44, 156):
        out += line([(x, 44), (x - 22, 90)], DIM, 2) + line([(x, 44), (x + 22, 90)], DIM, 2)
        out += path(f"M{x - 30},90 H{x + 30} Q{x},104 {x - 30},90 Z", INK, 2.5, fill="#0f172a44")
    out += _bottle(44, 70, 22, 28, INK, ACC) + _bottle(156, 70, 22, 28, INK, COOL)
    return out


def art_time_zero():
    out = ""
    for k in range(6):
        for m in range(2):
            out += rect(46 + m * 7, 20 + k * 18 + (9 if m else 0), 7, 9, INK if (k + m) % 2 == 0 else "none", "none", 0, 0)
    out += rect(46, 20, 14, 108, "none", INK, 2, 0)
    out += person(26, 44, 1.0, ACC) + person(26, 80, 1.0, ACC) + person(26, 116, 1.0, ACC)
    out += arrow(70, 76, 96, 76, DIM, 2.5)
    out += circle(144, 80, 36, "#0f172a44", INK, 4) + rect(136, 34, 16, 9, INK, INK, 0, 2)
    out += line([(144, 80), (144, 52)], ACC, 4) + circle(144, 80, 4, ACC)
    return out + text(144, 110, "0:00", 14, INK)


def art_lag_analysis():
    out = arrow(14, 100, 188, 100, INK, 3)
    out += pill(34, 100, 30, 13, 0) + text(34, 124, "", 1)
    out += path("M52,72 Q52,64 60,64 H96 Q104,64 104,56 Q104,64 112,64 H148 Q156,64 156,72", ACC, 3)
    out += text(104, 44, "LAG", 14, ACC)
    out += circle(76, 100, 5, DIM) + cross(76, 100, 6, DIM, 2.5) + circle(118, 100, 5, DIM) + cross(118, 100, 6, DIM, 2.5)
    return out + bolt(174, 80, 1.0, HOT) + line([(52, 92), (52, 108)], ACC, 2.5) + line([(156, 92), (156, 108)], ACC, 2.5)


def art_concurrent_control():
    out = ""
    for y in (34, 76, 118):
        out += line([(12, y), (188, y)], INK, 2.5)
    out += line([(150, 34), (150, 118)], DIM, 2, "4 4")
    out += _runner(90, 52, 0.95, INK) + _runner(90, 94, 0.95, ACC)
    out += "".join(line([(52, y), (66, y)], DIM, 2) for y in (46, 52, 88, 94))
    return out + clock(176, 136, 10, INK, 0, 90, 2.5) + text(14, 140, "SAME TIME", 10, DIM, "start")


def art_parallel_trends():
    out = axes(14, 14, 176, 120) + line([(116, 18), (116, 128)], DIM, 2, "4 4")
    out += line([(24, 104), (116, 80)], INK, 3) + line([(24, 74), (116, 50)], ACC, 3)
    out += line([(116, 80), (182, 63)], INK, 3) + line([(116, 50), (182, 22)], ACC, 3)
    for x in (48, 84):
        for dy in (-3, 3):
            yb = 104 - (x - 24) * 24 / 92
            out += line([(x - 6 + dy, yb - 8), (x + 6 + dy, yb + 8)], INK, 2)
            out += line([(x - 6 + dy, yb - 38), (x + 6 + dy, yb - 22)], ACC, 2)
    return out + check(176, 112, 10, OK)


def art_cluster_allocation():
    out = ""
    for k, (x, c) in enumerate(((16, ACC), (106, INK))):
        out += rect(x, 30, 78, 92, "#0f172a33", c, 3, 6, dash="10 4")
        for i in range(2):
            for j in range(2):
                out += building(x + 10 + i * 34, 44 + j * 38, 24, 26, c, "#0f172a44", 9)
    return out + dice(100, 136, 18, 2, rot=10)


def art_washout():
    out = path("M60,62 L70,134 H130 L140,62", INK, 3.5, fill="rgba(248,250,252,.08)")
    out += path("M64,92 L68,124 Q100,130 132,124 L136,92 Z", COOL, 0, fill="rgba(125,211,252,.55)")
    out += scatter([(80, 104), (96, 112), (116, 102), (124, 116)], 2.4, ACC, .45)
    out += line([(100, 34), (100, 86)], COOL, 6, o=.8) + _drop(100, 26, 1.5, COOL)
    out += _drop(84, 46, .6, COOL, .7) + _drop(118, 52, .5, COOL, .7)
    out += path("M152,40 Q162,30 172,40 M150,58 Q164,48 178,58", DIM, 2.5)
    return out + _sparkle_ink(160, 102) + _sparkle_ink(44, 118, 5)


def _sparkle_ink(x, y, r=8):
    return star(x, y, r, INK, pts=4)


def art_external_validation():
    out = _map(12, 36, 72, 66, INK) + _map(116, 36, 72, 66, COOL)
    out += path("M18,58 Q36,40 48,44 Q66,48 78,40 L78,70 Q60,84 46,92 Q30,96 18,90 Z", "#86EFAC", 0, fill="rgba(134,239,172,.35)", o=1)
    out += path("M126,46 Q140,60 160,52 Q178,50 182,62 L180,94 Q160,100 140,96 Q124,90 122,76 Z", "#86EFAC", 0, fill="rgba(134,239,172,.25)")
    out += path("M20,92 Q48,50 80,44", ACC, 3) + path("M124,96 Q152,54 184,48", ACC, 3)
    out += arrow(88, 70, 112, 70, INK, 3) + check(152, 126, 11, OK)
    return out + text(48, 124, "TRAINED", 11, DIM) + text(152, 26, "NEW DATA", 11, COOL)


def art_multiplicity():
    r = lcg(31)
    out = line([(14, 132), (186, 132)], INK, 2.5)
    for k in range(12):
        x = 22 + k * 14.5
        y = 120 - r() * 62
        if k == 7:
            y = 26
        out += circle(x, y, 6.5, ACC if k == 7 else INK) + circle(x, y, 2.6, DARK)
    out += line([(14, 76), (186, 76)], DIM, 2, "5 5") + line([(14, 40), (186, 40)], ACC, 3, "8 5")
    return out + arrow(8, 74, 8, 44, ACC, 2.5, head=6)


def art_replication():
    out = flask(56, 82, 1.35) + flask(144, 82, 1.35)
    out += carrow(84, 52, 100, 36, 116, 52, INK, 2.5, "4 4", head=7)
    out += circle(56, 22, 12, "#0f172a55", OK, 2.5) + check(56, 22, 7, OK, 3)
    out += circle(144, 22, 12, "#0f172a55", OK, 2.5) + check(144, 22, 7, OK, 3)
    return out + text(56, 140, "LAB 1", 11, DIM) + text(144, 140, "LAB 2", 11, DIM)


def art_comprehensive_search():
    out = cylinder(18, 70, 34, 26, INK) + cylinder(18, 42, 34, 26, INK) + cylinder(18, 98, 34, 26, INK)
    out += rect(130, 64, 56, 64, "#0f172a44", INK, 3, 3) + line([(130, 96), (186, 96)], INK, 2.5)
    out += rect(120, 74, 56, 20, DARK + "aa", INK, 2.5, 2) + line([(140, 84), (156, 84)], INK, 2.5)
    out += doc(126, 56, 16, 20, INK, 1, fill="#0f172a88", sw=2) + doc(148, 54, 16, 20, INK, 1, fill="#0f172a88", sw=2)
    out += circle(92, 64, 24, "rgba(252,211,77,.18)", ACC, 4) + line([(110, 82), (126, 98)], ACC, 7)
    return out + doc(82, 52, 18, 22, INK, 2, fill="#0f172a55", sw=2)


def art_heterogeneity_plan():
    out = line([(104, 12), (104, 140)], DIM, 2, "3 3")
    rows = [(INK, 18, 96, 128), (INK, 32, 88, 120), (INK, 46, 100, 140), (None, 0, 0, 0),
            (COOL, 78, 112, 150), (COOL, 92, 122, 168), (COOL, 106, 118, 160)]
    for c, y, lo, hi in rows:
        if c:
            mid = (lo + hi) / 2
            out += line([(lo, y), (hi, y)], c, 2.5) + rect(mid - 4, y - 4, 8, 8, c, c, 0, 1)
    out += path("M98,62 L112,57 L126,62 L112,67 Z", INK, 2, fill=INK)
    out += path("M120,124 L138,119 L156,124 L138,129 Z", COOL, 2, fill=COOL)
    out += line([(16, 70), (186, 70)], ACC, 2, "6 4")
    return out + text(18, 40, "A", 18, INK, "start") + text(18, 106, "B", 18, COOL, "start")


def art_sampling_frame():
    r = lcg(17)
    pool = [(14 + r() * 172, 108 + r() * 32) for _ in range(40)]
    cols = (INK, ACC, COOL, HOT)
    out = "".join(circle(x, y, 3.2, cols[k % 4], o=.55) for k, (x, y) in enumerate(pool))
    out += line([(186, 14), (128, 54)], INK, 4)
    out += f'<ellipse cx="96" cy="62" rx="36" ry="12" fill="none" stroke="{INK}" stroke-width="3.5"/>'
    out += path("M60,62 Q66,104 96,108 Q126,104 132,62", INK, 2)
    out += "".join(path(f"M{60 + k * 12},{62 + (2 if 0 < k < 6 else 0)} Q{66 + k * 9},{90} {96 + (k - 3) * 6},{106}", DIM, 1.5) for k in range(7))
    out += "".join(line([(64 + k * 1.5, 74 + k * 10), (128 - k * 1.5, 74 + k * 10)], DIM, 1.5) for k in range(3))
    picks = [(80, 74, 0), (92, 84, 1), (106, 76, 2), (100, 96, 3), (114, 86, 0), (86, 94, 2), (96, 70, 3), (110, 98, 1)]
    return out + "".join(circle(x, y, 4, cols[c]) for x, y, c in picks)


def art_validated_measures():
    out = rect(20, 54, 164, 20, "#0f172a44", INK, 3, 2)
    out += "".join(line([(30 + k * 8, 54), (30 + k * 8, 54 + (9 if k % 5 == 0 else 5))], INK, 1.8) for k in range(20))
    out += path("M20,54 V122 L34,122 L40,74", INK, 3, fill="#0f172a44")
    out += rect(104, 48, 30, 32, "#0f172a66", ACC, 3, 3) + path("M104,80 L110,122 L124,122 L124,80", ACC, 3, fill="#0f172a44")
    out += line([(34, 108), (110, 108)], DIM, 2, "3 3") + circle(72, 108, 2, DIM)
    out += path("M30,16 V40 M54,16 V40 M30,28 H54", ACC, 0)
    return out + circle(164, 30, 16, "#0f172a55", OK, 3) + check(164, 30, 9, OK, 3.5)


def art_reflexivity():
    out = f'<ellipse cx="140" cy="66" rx="34" ry="48" fill="rgba(125,211,252,.18)" stroke="{INK}" stroke-width="4"/>'
    out += line([(140, 114), (140, 134)], INK, 4) + line([(122, 136), (158, 136)], INK, 4)
    out += path("M118,40 Q128,30 138,36", "#ffffff88", 2.5)
    out += person(146, 72, 1.7, INK, .38)
    out += person(54, 82, 2.4, INK)
    out += rect(64, 92, 28, 34, ACC, "none", 0, 2) + line([(70, 102), (86, 102)], DARK, 2) + line([(70, 110), (82, 110)], DARK, 2)
    return out + line([(78, 92), (78, 126)], "#0f172a66", 2)


def art_triangulation():
    tgt = (100, 78)
    out = ""
    srcs = [(30, 34), (170, 34), (100, 136)]
    for x, y in srcs:
        out += line([(x, y), tgt], ACC, 2.5, "6 5")
    out += circle(100, 78, 18, "#0f172a55", ACC, 3) + star(100, 78, 10, ACC)
    out += eye(30, 30, 0.6)
    out += doc(158, 14, 24, 30, INK, 2, fill=DARK + "88")
    out += rect(86, 122, 28, 22, DARK + "88", INK, 2.5, 2) + "".join(rect(91 + k * 7, 140 - h, 5, h, INK, "none", 0, 1) for k, h in enumerate((6, 12, 9)))
    return out


def art_saturation_sampling():
    out = path("M54,24 L66,132 H134 L146,24", INK, 4)
    out += path("M55,30 Q100,22 145,30 L134,130 H66 Z", ACC, 0, fill="rgba(252,211,77,.75)")
    out += path("M55,30 Q100,20 145,30", ACC, 3)
    out += "".join(circle(x, y, 2.5, "#ffffff66") for x, y in ((84, 96), (110, 70), (96, 112), (120, 104)))
    out += _drop(100, 4, .7, ACC, .6)
    return out + check(170, 64, 12, OK) + "".join(line([(28, 34 + k * 20), (40, 34 + k * 20)], DIM, 2) for k in range(5))


def art_multilevel_analysis():
    out = circle(100, 76, 64, "#0f172a22", INK, 3) + text(100, 30, "", 1)
    for k, (x, y, c) in enumerate(((72, 60, ACC), (130, 62, COOL), (100, 108, INK))):
        out += circle(x, y, 26, "#0f172a33", c, 3)
        out += "".join(circle(x + 12 * math.cos(a), y + 12 * math.sin(a), 3.6, c) for a in (0.3, 2.4, 4.5))
        out += circle(x, y, 3.6, c)
    return out


def art_verification_validation():
    out = rect(14, 30, 92, 74, "#0f172a55", INK, 3, 6) + line([(14, 44), (106, 44)], INK, 2)
    out += "".join(circle(22 + i * 6, 37, 1.6, INK) for i in range(3))
    out += text(60, 84, "</>", 30, ACC)
    out += flask(150, 70, 1.25, INK, COOL)
    out += circle(60, 124, 12, "#0f172a55", OK, 2.5) + check(60, 124, 7, OK, 3)
    return out + circle(150, 124, 12, "#0f172a55", OK, 2.5) + check(150, 124, 7, OK, 3)


def art_multi_site():
    out = globe(100, 78, 54)
    pins = ((70, 50, ACC), (122, 44, COOL), (138, 86, ACC), (82, 100, HOT), (106, 72, INK), (60, 80, COOL))
    return out + "".join(_pin(x, y, c) for x, y, c in pins)


def art_within_comparison():
    out = line([(24, 128), (176, 128)], DIM, 2)
    out += person(62, 80, 2.6, INK) + person(138, 80, 2.6, ACC)
    out += text(100, 92, "=", 30, INK)
    out += path("M62,22 V14 H138 V22", DIM, 2.5) + line([(100, 14), (100, 6)], DIM, 2.5)
    return out


def art_spc():
    ys = [70, 64, 74, 68, 72, 66, 71, 69, 50, 46, 52, 44, 48, 42]
    pts = [(22 + i * 12, y) for i, y in enumerate(ys)]
    out = line([(16, 52), (184, 52)], HOT, 2, "6 5") + line([(16, 88), (184, 88)], HOT, 2, "6 5") + line([(16, 70), (112, 70)], DIM, 2)
    out += line([(118, 47), (184, 47)], ACC, 2.5) + line([(115, 26), (115, 120)], INK, 2, "3 4")
    out += line(pts, INK, 3) + scatter(pts[:8], 3.2, INK) + scatter(pts[8:], 3.6, ACC)
    return out + text(18, 46, "UCL", 10, HOT, "start") + text(18, 102, "LCL", 10, HOT, "start") + text(120, 136, "CHANGE", 10, INK, "start")


SAFEGUARD_ART = {
    "randomization": art_randomization,
    "allocation-concealment": art_allocation_concealment,
    "blinding": art_blinding,
    "placebo-sham": art_placebo_sham,
    "itt": art_itt,
    "preregistration": art_preregistration,
    "power-analysis": art_power_analysis,
    "dag-adjustment": art_dag_adjustment,
    "matching-ps": art_matching_ps,
    "negative-control": art_negative_control,
    "sensitivity-analysis": art_sensitivity_analysis,
    "active-comparator": art_active_comparator,
    "time-zero": art_time_zero,
    "lag-analysis": art_lag_analysis,
    "concurrent-control": art_concurrent_control,
    "parallel-trends": art_parallel_trends,
    "cluster-allocation": art_cluster_allocation,
    "washout": art_washout,
    "external-validation": art_external_validation,
    "multiplicity": art_multiplicity,
    "replication": art_replication,
    "comprehensive-search": art_comprehensive_search,
    "heterogeneity-plan": art_heterogeneity_plan,
    "sampling-frame": art_sampling_frame,
    "validated-measures": art_validated_measures,
    "reflexivity": art_reflexivity,
    "triangulation": art_triangulation,
    "saturation-sampling": art_saturation_sampling,
    "multilevel-analysis": art_multilevel_analysis,
    "verification-validation": art_verification_validation,
    "multi-site": art_multi_site,
    "within-comparison": art_within_comparison,
    "spc": art_spc,
}
