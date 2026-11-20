"""Benchmark evaluation: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, doc
from art import gear, star, cylinder


def compare():
    out = g("pop", gear(52, 66, 18, ACC), 0) + text(52, 106, "method A", 11, ACC)
    out += text(100, 70, "vs", 14, INK)
    out += g("pop", gear(148, 66, 18, COOL), 1) + text(148, 106, "method B", 11, COOL)
    out += text(100, 28, "same question", 12, INK) + text(100, 136, "who runs it?", 11, DIM)
    return out


def tasks():
    out = ""
    for i in range(4):
        out += g("pop", cylinder(20 + i * 44, 40, 32, 44, ACC if i == 3 else INK), i)
    out += g("pop", star(148 + 16, 34, 7), 4) + text(160, 104, "known truth", 11, ACC)
    out += text(100, 130, "representative tasks", 11, INK)
    return out


def methods():
    out = ""
    for i, (lab, c) in enumerate((("A", ACC), ("B", COOL), ("baseline", DIM))):
        y = 40 + i * 32
        out += text(40, y + 5, lab, 12, c)
        out += g("grow", rect(80, y - 8, 90, 14, "none", c, 2, 3), i)
    out += text(124, 140, "same tuning budget", 11, INK)
    return out


def metrics():
    base = 120
    out = line([(24, base), (186, base)], DIM, 2)
    for i, (h, c) in enumerate(((70, ACC), (52, COOL), (34, DIM))):
        x = 48 + i * 48
        out += g("grow", rect(x - 14, base - h, 28, h, c, "none", 0, 3), i)
        out += line([(x, base - h - 10), (x, base - h + 10)], INK, 2)
    out += text(104, 140, "same metric, repeats", 11, INK)
    return out


def evolve():
    out = doc(30, 40, 30, 40, DIM, 3) + text(45, 96, "v1", 12, DIM)
    out += g("draw", arrow(66, 60, 90, 60, INK, 2), 0) + g("pop", doc(96, 40, 30, 40, INK, 3) + text(111, 96, "v2", 12, INK), 1)
    out += g("draw", arrow(132, 60, 156, 60, INK, 2), 2) + g("pop", doc(160, 40, 30, 40, ACC, 3) + text(175, 96, "v3", 12, ACC), 3)
    out += text(100, 132, "so nobody tunes to the test", 11, HOT)
    return out


PICTURES = {"compare": compare, "tasks": tasks, "methods": methods, "metrics": metrics, "evolve": evolve}
