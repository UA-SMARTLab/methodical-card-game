"""Case-cohort design: five steps' pictures, from the stored samples to the weighted analysis."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line
from art import cylinder


def _grid(color):
    return "".join(person(24 + c * 19, 34 + r * 26, 0.6, color(r, c)) for r in range(4) for c in range(6))


CASE = {(0, 4), (1, 1), (2, 5), (3, 2), (2, 0)}
SUB = {(0, 0), (0, 2), (1, 3), (1, 5), (2, 2), (3, 4), (0, 4)}


def cohort():
    out = _grid(lambda r, c: INK)
    out += g("pop", cylinder(146, 40, 36, 48, ACC), 0) + g("pop", text(164, 104, "stored", 12, ACC) + text(164, 120, "blood", 12, ACC), 1)
    return out + text(72, 142, "whole cohort", 11, DIM)


def subcohort():
    out = _grid(lambda r, c: DIM)
    out += "".join(g("pop", person(24 + c * 19, 34 + r * 26, 0.6, COOL), i) for i, (r, c) in enumerate(sorted(SUB)))
    return out + text(164, 70, "random", 12, COOL) + text(164, 86, "subcohort", 12, COOL)


def all_cases():
    out = _grid(lambda r, c: COOL if (r, c) in SUB else DIM)
    out += "".join(g("pop", person(24 + c * 19, 34 + r * 26, 0.6, HOT), i) for i, (r, c) in enumerate(sorted(CASE)))
    return out + text(164, 70, "+ every", 12, HOT) + text(164, 86, "case", 12, HOT)


def many():
    out = rect(14, 40, 60, 60, "none", COOL, 2.5, 6) + text(44, 74, "subcohort", 12, COOL)
    for k, (s, c) in enumerate((("diabetes", HOT), ("stroke", ACC), ("cancer", INK))):
        y = 34 + k * 34
        out += g("draw", arrow(78, 70, 112, y, DIM, 2), k) + g("pop", text(148, y + 4, s, 12, c), k + 1)
    return out + text(100, 144, "one subcohort, many outcomes", 11, DIM)


def weights():
    out = line([(100, 24), (100, 120)], DIM, 2) + line([(30, 120), (170, 120)], INK, 3)
    out += g("pop", "".join(person(50 + k * 14, 104, 0.6, HOT) for k in range(4)), 0)
    out += g("pop", person(150, 104, 0.6, COOL) + text(150, 80, "× 1/fraction", 12, COOL), 1)
    out += text(56, 140, "cases over-sampled", 11, HOT) + text(150, 140, "weighted up", 11, COOL)
    return out + g("pop", text(100, 18, "rebalance", 12, ACC), 2)


PICTURES = {"cohort": cohort, "subcohort": subcohort, "all_cases": all_cases, "many": many, "weights": weights}
