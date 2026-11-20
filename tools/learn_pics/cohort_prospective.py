"""Prospective cohort: five steps' pictures, from recruiting the cohort to comparing risks."""
from learn_pics._kit import INK, DIM, ACC, HOT, g, person, rect, text, arrow, line
from art import clock


def recruit():
    out = rect(60, 30, 110, 96, "none", DIM, 2, 8) + text(115, 24, "COHORT", 12, INK)
    spots = [(80, 58), (104, 58), (128, 58), (152, 58), (80, 100), (104, 100), (128, 100), (152, 100)]
    out += "".join(g("pop", person(x, y, 0.8, INK), i) for i, (x, y) in enumerate(spots))
    out += g("pop", person(38, 80, 0.8, DIM), 8) + text(38, 112, "not eligible", 11, DIM)
    return out + text(115, 142, "free of the disease", 11, DIM)


def baseline():
    out = text(100, 22, "measured at the start", 11, DIM)
    for k in range(4):
        out += person(40 + k * 40, 60, 0.85, INK) + person(40 + k * 40, 110, 0.85, INK)
    # Exposure is recorded now, before anyone could have the outcome.
    out += "".join(g("pop", person(40 + k * 40, 60, 0.85, ACC), k) for k in range(4))
    return out + g("pop", text(196 - 6, 70, "exposed", 11, ACC, "end") + text(194, 120, "unexposed", 11, INK, "end"), 4)


def follow():
    out = line([(16, 128), (186, 128)], DIM, 2) + g("draw", arrow(16, 128, 186, 128, ACC, 2.5), 0)
    out += text(100, 144, "years of follow-up", 11, ACC)
    for k, x in enumerate((40, 100, 160)):
        out += g("pop", clock(x, 36, 12) + person(x, 92, 0.8, INK), 1 + k)
    out += g("fade", person(124, 92, 0.8, DIM), 4) + text(124, 70, "lost?", 11, HOT)
    return out


def incidence():
    out = text(60, 22, "exposed", 12, ACC) + text(150, 22, "unexposed", 12, INK)
    for r in range(3):
        for c in range(3):
            out += person(36 + c * 24, 46 + r * 34, 0.75, ACC) + person(126 + c * 24, 46 + r * 34, 0.75, INK)
    # New cases appear during follow-up: more of them among the exposed.
    new = [(36, 46), (84, 80), (60, 114)]
    out += "".join(g("pop", person(x, y, 0.75, HOT), i) for i, (x, y) in enumerate(new))
    out += g("pop", person(150, 80, 0.75, HOT), 3)
    return out + g("pop", text(100, 143, "new cases", 11, HOT), 4)


def compare():
    base = 120
    out = line([(30, base), (176, base)], DIM, 2)
    out += g("grow", rect(52, base - 72, 36, 72, ACC, "none", 0, 3), 0) + g("grow", rect(118, base - 24, 36, 24, INK, "none", 0, 3), 1)
    out += text(70, base + 16, "risk, exposed", 11, ACC) + text(136, base + 16, "risk, unexposed", 11, INK)
    return out + g("pop", text(100, 26, "risk ratio = 3/9 ÷ 1/9", 13, HOT), 2)


PICTURES = {"recruit": recruit, "baseline": baseline, "follow": follow, "incidence": incidence, "compare": compare}
