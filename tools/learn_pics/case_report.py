"""Case report / case series: the six steps' pictures. No exercise: the Method is argued in words."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, doc


def notice():
    # Many ordinary patients, one that doesn't fit the pattern.
    out = ""
    for k, (x, y) in enumerate([(30, 50), (54, 50), (78, 50), (30, 96), (54, 96), (78, 96)]):
        out += g("pop", person(x, y, 0.8, DIM), k)
    out += g("pop", person(140, 74, 1.5, HOT), 6)
    out += g("pop", circle(140, 64, 30, "none", ACC, 3), 7) + g("pop", text(140, 128, "unusual", 13, ACC), 8)
    return out


def describe():
    out = person(44, 78, 1.6, INK)
    out += g("draw", arrow(70, 74, 100, 74, DIM, 2.5), 1)
    out += g("pop", doc(110, 30, 64, 84, INK, 5), 2)
    for k, w in enumerate(("history", "symptoms", "findings")):
        out += g("pop", text(142, 66 + k * 16, w, 11, ACC), 3 + k)
    return out


def timeline():
    out = g("draw", arrow(14, 90, 188, 90, INK, 3), 0)
    for k, (x, lab) in enumerate([(34, "onset"), (78, "tests"), (122, "treat"), (166, "follow-up")]):
        out += g("pop", circle(x, 90, 6, ACC) + text(x, 70 if k % 2 == 0 else 116, lab, 12, INK), 1 + k)
    out += text(100, 140, "dates in order", 11, DIM)
    return out


def diagnose():
    out = person(36, 80, 1.4, INK)
    for k, (y, lab, c) in enumerate([(40, "diagnosis A", DIM), (76, "diagnosis B", ACC), (112, "diagnosis C", DIM)]):
        out += g("draw", arrow(62, 80, 104, y, c, 2.5), k) + g("pop", text(146, y + 4, lab, 12, c), k + 1)
    out += g("pop", line([(110, 40), (182, 40)], HOT, 2) + line([(110, 112), (182, 112)], HOT, 2), 4)
    return out


def follow():
    out = line([(18, 120), (186, 120)], DIM, 2)
    for k, x in enumerate((40, 90, 140)):
        out += g("pop", person(x, 92, 1.0, INK) + rect(x - 14, 50, 28, 18, "none", COOL, 2, 3) + text(x, 64, "visit", 11, COOL), k)
    out += g("pop", text(172, 66, "!", 26, HOT), 3) + text(100, 142, "outcomes and harms", 11, DIM)
    return out


def hypothesise():
    out = doc(22, 44, 46, 62, INK, 4)
    out += g("draw", arrow(76, 76, 118, 76, ACC, 3), 1)
    out += g("pop", text(156, 84, "?", 46, ACC), 2)
    out += g("pop", text(150, 128, "test it next", 12, INK), 3)
    return out


PICTURES = {"notice": notice, "describe": describe, "timeline": timeline, "diagnose": diagnose, "follow": follow,
            "hypothesise": hypothesise}
