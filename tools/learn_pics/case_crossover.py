"""Case-crossover: five steps' pictures, from taking only cases to what self-comparison removes."""
from learn_pics._kit import INK, DIM, ACC, HOT, g, person, rect, text, arrow, line
from art import bolt, cross


def cases_only():
    out = ""
    for k in range(4):
        out += g("pop", person(30 + k * 26, 60, 0.85, HOT), k)
    for k in range(4):
        out += person(30 + k * 26, 112, 0.85, DIM)
    out += g("pop", cross(66, 112, 14, HOT, 3), 4)
    return out + text(156, 64, "events: in", 12, HOT) + text(156, 116, "no event: out", 11, DIM)


def hazard():
    out = line([(14, 96), (186, 96)], DIM, 2) + text(100, 140, "time", 11, DIM)
    out += g("grow", rect(126, 70, 34, 26, ACC, "none", 0, 3), 0) + g("pop", bolt(176, 66, 1.3, HOT), 1)
    out += g("pop", text(143, 118, "hazard window", 11, ACC), 2) + g("pop", text(176, 30, "event", 12, HOT), 3)
    return out


def referent():
    out = line([(14, 96), (186, 96)], DIM, 2) + rect(126, 70, 34, 26, ACC, "none", 0, 3) + bolt(176, 66, 1.3, HOT)
    for k, x in enumerate((24, 74)):
        out += g("pop", rect(x, 70, 34, 26, "none", INK, 2, 3, dash="4 3"), k)
    out += g("pop", text(66, 118, "control windows", 11, INK), 2)
    return out + g("pop", text(66, 40, "same person, earlier", 11, DIM), 3)


def within():
    out = ""
    rows = [(36, True, False), (72, True, True), (108, False, False)]
    for k, (y, haz, ref) in enumerate(rows):
        out += person(20, y + 4, 0.7, HOT) + line([(34, y + 8), (186, y + 8)], DIM, 1.5)
        out += rect(70, y - 6, 30, 14, INK if ref else "none", INK, 2, 2) + rect(140, y - 6, 30, 14, ACC if haz else "none", ACC, 2, 2)
        out += g("pop", text(186, y + 4, "≠" if haz != ref else "=", 13, HOT if haz != ref else DIM, "end"), k)
    return out + text(85, 140, "control", 11, INK) + text(155, 140, "hazard", 11, ACC)


def removes():
    out = person(44, 76, 1.6, INK)
    labels = ["genes", "personality", "chronic illness"]
    for k, s in enumerate(labels):
        y = 40 + k * 30
        out += text(140, y, s, 12, DIM) + g("pop", line([(100, y - 4), (180, y - 4)], HOT, 2.5), k)
    return out + g("pop", text(140, 136, "constant: cancels", 12, ACC), 3)


PICTURES = {"cases_only": cases_only, "hazard": hazard, "referent": referent, "within": within, "removes": removes}
