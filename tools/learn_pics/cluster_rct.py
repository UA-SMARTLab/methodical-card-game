"""Cluster randomized trial: the five steps' pictures (whole schools are allocated, and analysed as schools)."""
from learn_pics._kit import INK, DIM, HOT, TREAT, CONTROL, g, person, rect, text, arrow, line, dice, path

SCHOOLS = [(14, 22), (76, 22), (138, 22), (14, 86), (76, 86), (138, 86)]


def _school(x, y, c=DIM, fill="none"):
    """A school: a roofed box with pupils inside."""
    out = path(f"M{x},{y + 14} L{x + 24},{y} L{x + 48},{y + 14}", c, 2) + rect(x, y + 14, 48, 34, fill, c, 2, 3)
    out += "".join(person(x + 10 + k * 14, y + 36, 0.5, INK if fill == "none" else "#0f172a") for k in range(3))
    return out


def groups():
    out = "".join(g("pop", _school(x, y), k) for k, (x, y) in enumerate(SCHOOLS))
    out += g("pop", text(100, 144, "the cluster is the unit", 11, HOT), 6)
    return out


def why():
    out = _school(20, 40, TREAT) + _school(132, 40, CONTROL)
    out += text(44, 112, "new lessons", 11, TREAT) + text(156, 112, "usual lessons", 11, CONTROL)
    # Pupils talk across the fence: if classmates were split, the lesson would leak to the control.
    out += g("draw", path("M70,70 Q100,40 130,70", HOT, 2.5, dash="4 3"), 0)
    out += g("pop", text(100, 32, "ideas spill over", 12, HOT), 1)
    out += g("pop", text(100, 136, "so allocate whole schools", 11, INK), 2)
    return out


def allocate():
    out = g("roll", dice(100, 22, 22, 4))
    cols = [TREAT, CONTROL, CONTROL, TREAT, TREAT, CONTROL]
    for k, ((x, y), c) in enumerate(zip(SCHOOLS, cols)):
        y2 = y + 16 if y < 50 else y + 8
        out += g("pop", _school(x, y2, c), 1 + k)
    return out


def icc():
    out = ""
    # Pupils in the same school score alike: each school's dots sit close together.
    centres = [(34, 60), (100, 96), (166, 48)]
    offs = [(-8, -6), (6, -4), (-4, 6), (8, 7), (0, 0)]
    for k, (cx, cy) in enumerate(centres):
        out += g("pop", rect(cx - 22, cy - 20, 44, 40, "none", DIM, 1.5, 8)
                 + "".join(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="3.5" fill="{INK}"/>' for dx, dy in offs), k)
    out += g("pop", text(100, 22, "alike within, apart between", 12, HOT), 3)
    out += text(100, 140, "fewer independent pieces", 11, DIM)
    return out


def analyse():
    base = 122
    out = line([(20, base), (184, base)], DIM, 2)
    t = [70, 78, 64]
    c = [52, 58, 46]
    for k, v in enumerate(t):
        out += g("grow", rect(24 + k * 24, base - v, 18, v, TREAT, "none", 0, 3), k)
    for k, v in enumerate(c):
        out += g("grow", rect(112 + k * 24, base - v, 18, v, CONTROL, "none", 0, 3), 3 + k)
    out += text(57, base + 16, "schools: new", 11, TREAT) + text(145, base + 16, "schools: usual", 11, CONTROL)
    out += g("pop", text(100, 24, "allow for clustering", 12, HOT), 6)
    return out


PICTURES = {"groups": groups, "why": why, "allocate": allocate, "icc": icc, "analyse": analyse}
