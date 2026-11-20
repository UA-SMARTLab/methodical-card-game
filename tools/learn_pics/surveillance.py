"""Monitoring / surveillance: the five steps' pictures. No exercise."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, doc
from art import axes, clock, check


def define():
    out = doc(22, 30, 60, 80, INK, 0)
    for k, lab in enumerate(("symptoms", "lab test", "place, time")):
        out += g("pop", check(34, 56 + k * 18, 5, ACC, 2.5) + text(62, 60 + k * 18, lab, 11, INK), k)
    out += g("draw", arrow(92, 70, 124, 70, ACC, 3), 3)
    out += g("pop", person(156, 70, 1.4, HOT), 4) + text(156, 124, "counts as a case", 11, HOT)
    return out


def collect():
    out = line([(14, 124), (186, 124)], DIM, 2)
    for k in range(8):
        x = 22 + k * 22
        out += g("grow", rect(x - 6, 124 - (24 + (k * 7) % 30), 12, 24 + (k * 7) % 30, ACC, "none", 0, 2), k)
    out += text(100, 24, "every week, same way", 12, INK) + text(100, 142, "ongoing", 11, DIM)
    return out


def report():
    out = ""
    for k, (x, lab) in enumerate([(30, "clinic"), (100, "health office"), (170, "action")]):
        out += g("pop", rect(x - 26, 58, 52, 30, "none", INK, 2.5, 5) + text(x, 78, lab, 11, INK), 2 * k)
        if k < 2:
            out += g("draw", arrow(x + 28, 73, x + 42, 73, ACC, 3), 2 * k + 1)
    out += clock(100, 118, 12) + text(100, 30, "how fast?", 12, ACC)
    return out


def signal():
    pts = [(24 + i * 10, 104 - (i % 3) * 4) for i in range(12)] + [(144, 80), (154, 60), (164, 42), (174, 34)]
    out = axes(16, 18, 172, 108)
    out += line([(20, 92), (188, 92)], DIM, 2, "5 4") + text(40, 86, "usual", 11, DIM)
    out += g("draw", line(pts, INK, 3), 0)
    out += g("pop", circle(164, 42, 12, "none", HOT, 3) + text(140, 30, "signal", 12, HOT), 1)
    return out


def missed():
    out = ""
    for k in range(10):
        seen = k % 3 != 2
        x, y = 22 + (k % 5) * 26, 50 + (k // 5) * 52
        out += g("pop" if seen else "fade", person(x, y, 0.8, INK if seen else DIM), k)
    out += g("pop", text(166, 66, "7 of 10", 15, ACC) + text(166, 88, "reported", 11, INK), 10)
    out += text(100, 142, "keep the share steady", 11, COOL)
    return out


PICTURES = {"define": define, "collect": collect, "report": report, "signal": signal, "missed": missed}
