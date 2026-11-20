"""Cross-sectional survey: the five steps' pictures. No exercise: the pictures carry it."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, crowd


def sample():
    # A source population; a planned sample is drawn from it.
    out = crowd(16, 40, 5, 4, 14, 24, 0.55, lambda i, j: DIM)
    out += rect(8, 22, 78, 104, "none", DIM, 2, 6) + text(46, 142, "population", 11, DIM)
    out += g("draw", arrow(92, 74, 120, 74, ACC, 3), 0)
    for k, (x, y) in enumerate([(138, 50), (160, 50), (182, 50), (138, 96), (160, 96), (182, 96)]):
        out += g("pop", person(x, y, 0.75, INK), 1 + k)
    out += text(160, 142, "sample", 11, ACC)
    return out


def snapshot():
    out = line([(14, 132), (186, 132)], DIM, 2) + circle(100, 132, 5, ACC) + text(100, 20, "ONE MOMENT", 12, ACC)
    for k in range(6):
        out += person(34 + k * 26, 74, 0.85, INK)
    out += g("pop", rect(16, 34, 168, 72, "none", ACC, 3, 6, dash="7 6"), 0)
    out += g("fade", rect(16, 34, 168, 72, "#FCD34D33", "none", 0, 6), 1)
    return out


def respond():
    out = ""
    for k in range(8):
        x, y = 22 + (k % 4) * 22, 50 + (k // 4) * 50
        took = k not in (2, 5, 7)
        out += g("fade" if not took else "pop", person(x, y, 0.8, INK if took else DIM), k)
    out += g("draw", arrow(112, 74, 140, 74, INK, 2.5), 8)
    out += g("pop", text(166, 62, "5 of 8", 16, ACC) + text(166, 84, "took part", 11, INK), 9)
    out += text(100, 140, "who said no?", 11, HOT)
    return out


def prevalence():
    out = ""
    for k in range(10):
        c = HOT if k in (1, 4, 8) else INK
        out += g("pop", person(18 + k * 17, 66, 0.7, c), k)
    out += g("pop", text(100, 112, "3 / 10 = 30%", 18, ACC), 10)
    out += text(100, 136, "has it now", 11, DIM)
    return out


def compare():
    base = 120
    out = line([(30, base), (176, base)], DIM, 2)
    out += g("grow", rect(52, base - 70, 38, 70, HOT, "none", 0, 3), 0)
    out += g("grow", rect(116, base - 30, 38, 30, COOL, "none", 0, 3), 1)
    out += text(71, base + 16, "exposed", 11, HOT) + text(135, base + 16, "not exposed", 11, COOL)
    out += g("pop", text(100, 26, "prevalence by group", 12, INK), 2)
    return out


PICTURES = {"sample": sample, "snapshot": snapshot, "respond": respond, "prevalence": prevalence, "compare": compare}
