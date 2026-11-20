"""Discrete choice experiment: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle
from art import check, clock, bubble


def attributes():
    out = ""
    rows = [("wait", "1 wk · 4 wk"), ("cost", "€0 · €50"), ("risk", "1% · 5%")]
    for i, (a, lv) in enumerate(rows):
        y = 40 + i * 36
        out += g("pop", text(40, y, a, 13, ACC) + text(126, y, lv, 12, INK), i)
    out += g("pop", person(30, 132, 0.6, DIM) + bubble(48, 112, 40, 18, DIM) , 3) + text(130, 140, "from interviews", 11, DIM)
    return out


def design():
    out = ""
    grid = [[1, 0, 1], [0, 1, 1], [1, 1, 0], [0, 0, 0]]
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            out += g("pop", rect(52 + c * 34, 26 + r * 24, 28, 18, ACC if v else "none", ACC if v else DIM, 2, 3), r)
    out += text(30, 36, "set 1", 11, DIM) + text(30, 108, "set 4", 11, DIM)
    out += text(100, 138, "levels mixed by design", 11, INK)
    return out


def choose():
    out = rect(20, 30, 70, 74, "none", INK, 2.5, 6) + text(55, 24, "option A", 12, INK)
    out += rect(110, 30, 70, 74, "none", INK, 2.5, 6) + text(145, 24, "option B", 12, INK)
    for k, (a, b) in enumerate((("1 wk", "4 wk"), ("€50", "€0"), ("5%", "1%"))):
        out += text(55, 54 + k * 20, a, 12, DIM) + text(145, 54 + k * 20, b, 12, DIM)
    out += g("pop", rect(110, 30, 70, 74, "none", ACC, 4, 6), 1) + g("pop", check(170, 118), 2)
    out += text(100, 140, "pick one", 12, ACC)
    return out


def model():
    base = 124
    out = line([(24, base), (186, base)], DIM, 2)
    for i, (lab, h, c) in enumerate((("wait", 40, HOT), ("cost", 62, HOT), ("risk", 92, HOT))):
        out += g("grow", rect(40 + i * 50, base - h, 30, h, c, "none", 0, 3), i) + text(55 + i * 50, base + 16, lab, 11, INK)
    out += g("pop", text(100, 22, "weight of each", 13, ACC), 3)
    return out


def check_():
    out = rect(18, 36, 70, 56, "none", DIM, 2, 6, dash="5 4") + text(53, 68, "said", 13, DIM)
    out += rect(112, 36, 70, 56, "none", INK, 2.5, 6) + text(147, 68, "did", 13, INK)
    out += g("draw", arrow(90, 64, 110, 64, ACC, 2.5), 0)
    out += g("pop", text(100, 118, "stated vs revealed", 12, ACC), 1)
    return out


PICTURES = {"attributes": attributes, "design": design, "choose": choose, "model": model, "check": check_}
