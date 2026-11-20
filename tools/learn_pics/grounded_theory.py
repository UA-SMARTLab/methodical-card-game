"""Grounded theory: the six steps' pictures. Argued in words, so no exercise."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, carrow, line, circle, doc, person

GREEN = "#86EFAC"


def sample():
    # A few chosen people, and a loop: collect, analyse, collect again, from the very start.
    out = "".join(g("pop", person(28 + k * 22, 112, 1.0, INK), k) for k in range(3))
    out += g("pop", doc(110, 92, 26, 34, DIM, 3), 3)
    out += g("draw", carrow(80, 92, 104, 50, 120, 86, ACC, 3), 4)
    out += g("draw", carrow(136, 128, 112, 148 - 6, 84, 122, ACC, 3), 5)
    out += text(100, 30, "collect + analyse", 12, ACC) + text(160, 112, "at once", 11, ACC)
    return out


def code():
    # A transcript broken into fragments, each tagged with a short code.
    out = rect(16, 20, 80, 110, "none", DIM, 2, 4)
    for k in range(6):
        out += line([(24, 34 + k * 16), (88 - (k % 3) * 10, 34 + k * 16)], DIM, 2.5)
    for k, (y, lab) in enumerate(((34, "waiting"), (66, "trust"), (98, "hiding"))):
        out += g("pop", line([(24, y), (78, y)], ACC, 4) + arrow(98, y, 118, y, ACC, 2, head=5)
                 + rect(122, y - 9, 66, 18, "#0f172a66", ACC, 2, 4) + text(155, y + 4, lab, 12, ACC), k)
    return out


def compare():
    # Codes compared with each other and gathered into a category.
    pts = [(30, 40), (60, 26), (40, 76), (24, 112), (64, 120), (70, 74)]
    out = "".join(g("pop", rect(x - 12, y - 7, 24, 14, "none", DIM, 2, 3), k) for k, (x, y) in enumerate(pts))
    out += g("draw", line([(30, 40), (60, 26), (70, 74), (40, 76), (30, 40)], DIM, 1.5, dash="3 3")
             + line([(24, 112), (64, 120)], DIM, 1.5, dash="3 3"), 6)
    out += g("draw", arrow(86, 60, 118, 60, ACC, 3) + arrow(86, 112, 118, 112, ACC, 3), 7)
    out += g("pop", rect(124, 44, 64, 32, "#0f172a44", GREEN, 3, 6) + text(156, 65, "category", 12, GREEN), 8)
    out += g("pop", rect(124, 96, 64, 32, "#0f172a44", GREEN, 3, 6) + text(156, 117, "category", 12, GREEN), 9)
    return out


def theoretical():
    # The next person is chosen because the emerging category needs them, not to mirror the population.
    out = rect(14, 56, 64, 32, "#0f172a44", GREEN, 3, 6) + text(46, 77, "category", 12, GREEN)
    out += g("pop", text(46, 110, "gap?", 13, HOT), 0)
    out += "".join(person(124 + (k % 3) * 24, 40 + (k // 3) * 46, 0.9, DIM) for k in range(6))
    out += g("draw", arrow(82, 72, 136, 82, ACC, 3), 1)
    out += g("pop", person(148, 86, 0.9, ACC) + circle(148, 82, 15, "none", ACC, 2.5), 2)
    out += text(150, 140, "who fills it", 11, ACC)
    return out


def memo():
    # Memos pile up beside the analysis: why a code was split, why two were joined.
    out = ""
    for k in range(3):
        x, y = 30 + k * 50, 30 + k * 16
        out += g("pop", rect(x, y, 56, 46, "#0f172a66", ACC, 2.5, 2) + line([(x + 8, y + 14), (x + 46, y + 14)], ACC, 2)
                 + line([(x + 8, y + 24), (x + 38, y + 24)], ACC, 2) + line([(x + 8, y + 34), (x + 42, y + 34)], ACC, 2), k)
    out += text(100, 132, "memos: why", 13, ACC)
    return out


def saturate():
    # New interviews stop adding anything; the categories join into one theory around a core.
    out = ""
    for k in range(5):
        h = (26, 16, 8, 3, 1)[k]
        out += g("grow", rect(18 + k * 14, 70 - h, 9, h, ACC, "none", 0, 1), k)
    out += line([(14, 70), (90, 70)], DIM, 2) + text(52, 88, "new codes", 11, ACC)
    out += text(52, 102, "per interview", 11, DIM)
    out += g("pop", circle(150, 74, 15, GREEN) + text(150, 79, "core", 11, "#0f172a"), 5)
    for k, (x, y) in enumerate(((118, 36), (184, 40), (122, 116), (182, 114))):
        out += g("draw", line([(150, 74), (x, y)], GREEN, 2.5) + circle(x, y, 7, "none", GREEN, 2.5), 6 + k)
    out += text(150, 140, "theory", 13, GREEN)
    return out


PICTURES = {"sample": sample, "code": code, "compare": compare, "theoretical": theoretical, "memo": memo, "saturate": saturate}
