"""Computational simulation: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, doc, dice
from art import gear, check, cylinder


def concept():
    out = rect(14, 40, 62, 50, "none", INK, 2.5, 6) + text(45, 32, "real system", 11, INK) + gear(45, 65, 14, INK)
    out += g("draw", arrow(80, 65, 104, 65, DIM, 2.5), 0)
    out += g("pop", rect(108, 40, 30, 50, "none", ACC, 2.5, 4) + text(123, 70, "f(x)", 11, ACC), 1)
    out += g("draw", arrow(140, 65, 158, 65, DIM, 2.5), 2)
    out += g("pop", rect(160, 46, 30, 38, "none", COOL, 2.5, 4) + text(175, 70, "</>", 11, COOL), 3)
    out += text(100, 128, "concept, then code", 12, INK)
    return out


def data():
    out = cylinder(60, 44, 46, 50, INK)
    out += g("draw", arrow(90, 70, 130, 70, DIM, 2.5), 0) + g("pop", check(150, 70, 12), 1)
    out += text(100, 130, "inputs adequate, correct", 11, ACC)
    return out


def verify():
    out = doc(34, 30, 40, 52, COOL, 5) + text(54, 100, "program", 11, COOL)
    out += g("draw", arrow(82, 56, 118, 56, DIM, 2.5), 0) + g("pop", text(150, 52, "does what", 11, INK) + text(150, 66, "the concept says", 11, INK), 1)
    out += g("pop", check(150, 96, 12), 2) + text(100, 136, "verification", 12, ACC)
    return out


def validate():
    out = line([(24, 120), (186, 120)], DIM, 2) + line([(24, 120), (24, 26)], DIM, 2)
    real = [(30, 108), (60, 94), (90, 70), (120, 62), (150, 44), (180, 40)]
    out += "".join(circle(x, y, 3.5, INK) for x, y in real)
    out += g("draw", line([(30, 112), (60, 92), (90, 74), (120, 58), (150, 48), (180, 36)], ACC, 2.5), 0)
    out += text(70, 40, "real", 11, INK) + g("pop", text(150, 84, "model", 11, ACC), 1)
    out += text(105, 140, "output vs system", 11, DIM)
    return out


def experiment():
    out = g("roll", dice(34, 48, 30, 3))
    for k in range(5):
        out += g("draw", line([(64, 48), (184, 30 + k * 10)], ACC if k == 2 else DIM, 1.5), 1 + k)
    out += g("pop", text(124, 104, "many seeded runs", 12, INK), 6)
    out += g("pop", text(124, 124, "± Monte Carlo SE", 11, HOT), 7)
    return out


PICTURES = {"concept": concept, "data": data, "verify": verify, "validate": validate, "experiment": experiment}
