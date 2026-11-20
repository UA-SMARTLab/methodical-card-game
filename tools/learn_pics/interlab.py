"""Interlaboratory comparison: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle
from art import flask, building, check, cross

LABS = [(30, 110), (70, 110), (110, 110), (150, 110), (184, 110)]


def items():
    out = flask(100, 40, 1.0, INK) + text(156, 36, "one batch", 12, INK)
    for i, (x, y) in enumerate(LABS[:4]):
        out += g("draw", arrow(100, 62, x + 8, y - 22, DIM, 2), i) + g("pop", rect(x, y - 14, 16, 20, ACC, "none", 0, 3), i + 1)
    out += text(100, 140, "same item to every lab", 11, ACC)
    return out


def measure():
    out = ""
    for i, x in enumerate((32, 78, 124, 170)):
        out += g("pop", building(x - 17, 92, 34, 30, INK), i) + g("pop", flask(x, 56, 0.7, ACC), i + 1)
    out += text(100, 140, "each its own method", 11, INK)
    return out


def assign():
    out = line([(20, 80), (186, 80)], DIM, 2)
    vals = [70, 82, 92, 98, 101, 104, 110, 118, 130]
    out += "".join(g("pop", circle(22 + (v - 66) * 2.3, 80 + (i % 2) * 10 - 5, 5, INK), i // 3) for i, v in enumerate(vals))
    out += g("draw", line([(100, 50), (100, 112)], ACC, 3), 3) + g("pop", text(100, 40, "assigned value", 12, ACC), 4)
    out += text(100, 140, "robust centre or reference", 11, DIM)
    return out


def score():
    out = line([(20, 76), (186, 76)], ACC, 2) + text(176, 70, "target", 11, ACC)
    res = [(36, 70, 1), (68, 84, 1), (100, 62, 1), (132, 120, 0), (164, 80, 1)]
    for i, (x, y, ok) in enumerate(res):
        out += line([(x, 76), (x, y)], DIM, 1.5) + g("pop", circle(x, y, 5, INK if ok else HOT), i)
        out += g("pop", check(x, 34, 8) if ok else cross(x, 34, 7), 5 + i)
    out += text(132, 140, "find the cause", 11, HOT)
    return out


def spread():
    out = line([(20, 126), (186, 126)], DIM, 2) + text(100, 142, "round after round", 11, DIM)
    for i, (x, w) in enumerate(((44, 34), (100, 22), (156, 12))):
        out += g("grow", line([(x - w, 120), (x - w / 2, 70), (x, 40), (x + w / 2, 70), (x + w, 120)], ACC, 2.5), i)
    out += g("pop", text(100, 24, "spread narrows", 12, INK), 3)
    return out


PICTURES = {"items": items, "measure": measure, "assign": assign, "score": score, "spread": spread}
