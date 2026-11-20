"""Field experiment: the five steps' pictures (a rocky shore, replicate plots, a consumer kept out, a fence-only control)."""
from learn_pics._kit import INK, DIM, FAINT, HOT, ACC, COOL, TREAT, CONTROL, g, rect, text, line, path, circle, dice

PLOTS = [(20, 40), (66, 40), (112, 40), (158, 40), (20, 92), (66, 92), (112, 92), (158, 92)]
ARMS = ["x", "c", "p", "x", "c", "x", "p", "c"]  # x: consumers excluded, c: untouched control, p: fence-only control
COL = {"x": TREAT, "c": CONTROL, "p": DIM}


def _shore():
    return path("M6,130 Q50,118 100,126 T194,120", COOL, 2) + text(184, 144, "sea", 11, COOL, anchor="end")


def _snail(x, y, c=INK):
    return circle(x, y, 3.2, c) + path(f"M{x - 4},{y + 2} h8", c, 1.5)


def place():
    out = _shore() + path("M6,40 Q60,24 120,36 T194,30", DIM, 2)
    for k, (x, y) in enumerate([(40, 70), (70, 86), (110, 64), (140, 92), (170, 72), (90, 104)]):
        out += g("pop", _snail(x, y), k)
    out += g("pop", text(100, 20, "a real shore", 13, INK), 6)
    return out


def replicate():
    out = g("roll", dice(100, 22, 18, 3))
    for k, ((x, y), a) in enumerate(zip(PLOTS, ARMS)):
        out += g("pop", rect(x, y, 26, 26, "none", COL[a], 2.5, 3), 1 + k)
    out += text(100, 140, "many plots, roles by chance", 11, INK)
    return out


def manipulate():
    out = ""
    for k, ((x, y), a) in enumerate(zip(PLOTS, ARMS)):
        out += rect(x, y, 26, 26, "none", COL[a], 2.5, 3)
        if a == "x":
            # Mesh cage: consumers removed and kept out.
            out += g("pop", "".join(line([(x + 2 + i * 5.5, y + 2), (x + 2 + i * 5.5, y + 24)], TREAT, 1) for i in range(5)), k)
        else:
            out += _snail(x + 13, y + 13)
    out += text(100, 26, "consumers removed", 12, TREAT) + text(100, 140, "caged plots", 11, TREAT)
    return out


def controls():
    out = ""
    for k, ((x, y), a) in enumerate(zip(PLOTS, ARMS)):
        out += rect(x, y, 26, 26, "none", COL[a], 2.5, 3)
        if a == "p":
            # A half cage: the fence's own side effects (shade, flow), with consumers still free to enter.
            out += g("pop", "".join(line([(x + 2 + i * 5.5, y + 2), (x + 2 + i * 5.5, y + 12)], INK, 1) for i in range(5)), k)
            out += _snail(x + 13, y + 19)
        elif a == "c":
            out += _snail(x + 13, y + 13)
    out += g("pop", text(100, 26, "fence only, no exclusion", 12, INK), 8) + text(100, 140, "procedural control", 11, DIM)
    return out


def compare():
    base = 124
    out = line([(20, base), (184, base)], DIM, 2)
    for k, (v, c, lab) in enumerate([(84, TREAT, "caged"), (30, CONTROL, "open"), (34, DIM, "fence only")]):
        x = 34 + k * 52
        out += g("grow", rect(x, base - v, 30, v, c, "none", 0, 3), k) + text(x + 15, base + 16, lab, 11, c)
    out += g("pop", text(100, 22, "algal cover, months later", 12, INK), 3)
    return out


PICTURES = {"place": place, "replicate": replicate, "manipulate": manipulate, "controls": controls, "compare": compare}
