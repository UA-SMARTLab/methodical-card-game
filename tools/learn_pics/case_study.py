"""Case study (in-depth): the five steps' pictures. Argued in words, so no exercise."""
from art import building, bubble, axes, magnifier
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, doc, person


def define():
    # One organisation inside a dashed boundary, with a timeline that marks where the case begins and ends.
    out = building(70, 34, 60, 50, INK, "#0f172a44", 18) + rect(92, 62, 16, 22, "none", INK, 2, 1)
    out += g("draw", rect(46, 20, 108, 82, "none", ACC, 3, 14, dash="6 5"), 0)
    out += line([(30, 122), (170, 122)], DIM, 2)
    out += g("pop", line([(52, 112), (52, 132)], ACC, 3), 1) + g("pop", line([(148, 112), (148, 132)], ACC, 3), 2)
    out += g("draw", line([(52, 122), (148, 122)], ACC, 4), 3)
    out += text(52, 144, "start", 11, ACC) + text(148, 144, "end", 11, ACC) + text(100, 16, "THE CASE", 12, ACC)
    return out


def select():
    # Many possible cases; one is picked for what it can teach, not because it is average.
    spots = [(30, 40), (60, 34), (30, 80), (60, 76), (30, 120), (60, 118)]
    out = "".join(building(x - 12, y - 14, 24, 22, DIM) for x, y in spots)
    out += g("pop", building(130, 46, 44, 44, INK, "#0f172a44", 16), 1)
    out += g("draw", arrow(78, 76, 118, 70, ACC, 3), 0)
    out += g("pop", circle(152, 70, 36, "none", ACC, 3, dash="3 5"), 2)
    out += text(152, 126, "chosen case", 12, ACC) + text(45, 144, "other cases", 11, DIM)
    return out


def collect():
    # Several kinds of evidence point at the same case: documents, interviews, numbers, observation.
    out = building(82, 58, 36, 34, INK, "#0f172a44", 12)
    out += g("pop", doc(18, 18, 24, 30, INK, 2), 0) + text(36, 62, "documents", 11, INK)
    out += g("pop", bubble(150, 20, 34, 22, INK), 1) + text(166, 62, "interviews", 11, INK)
    out += g("pop", axes(20, 96, 30, 30, INK, 2) + "".join(rect(26 + k * 8, 126 - h, 5, h, ACC, "none", 0, 1) for k, h in enumerate((10, 20, 14))), 2)
    out += text(36, 142, "records", 11, ACC)
    out += g("pop", magnifier(160, 104, 12, COOL, 3), 3) + text(160, 142, "observation", 11, COOL)
    out += g("draw", arrow(46, 42, 78, 64, DIM, 2) + arrow(146, 46, 120, 64, DIM, 2)
             + arrow(56, 108, 80, 92, DIM, 2) + arrow(146, 104, 120, 90, DIM, 2), 4)
    return out


def analyse():
    # Each case is described on its own first; only then are the cases set side by side.
    out = ""
    for k, x in enumerate((40, 100, 160)):
        out += g("pop", building(x - 16, 24, 32, 30, INK, "#0f172a44", 10) + doc(x - 11, 62, 22, 28, DIM, 3), k)
    out += g("draw", line([(22, 106), (178, 106)], ACC, 3), 3)
    out += g("pop", arrow(40, 96, 40, 118, ACC, 2.5, head=6) + arrow(100, 96, 100, 118, ACC, 2.5, head=6)
             + arrow(160, 96, 160, 118, ACC, 2.5, head=6), 4)
    out += text(100, 138, "then compare", 12, ACC)
    return out


def generalise():
    # From the case to a theory, not to a population: the arrow goes up to an idea, not out to a crowd.
    out = building(24, 88, 40, 40, INK, "#0f172a44", 14)
    out += g("draw", arrow(70, 98, 116, 60, ACC, 3.5), 0)
    out += g("pop", circle(146, 44, 24, "none", ACC, 3) + text(146, 49, "theory", 13, ACC), 1)
    out += "".join(person(126 + k * 14, 124, 0.6, DIM) for k in range(5))
    out += g("pop", line([(118, 112), (190, 136)], HOT, 3) + line([(118, 136), (190, 112)], HOT, 3), 2)
    out += text(148, 143, "not a population", 11, HOT) + text(44, 144, "the case", 11, INK)
    return out


PICTURES = {"define": define, "select": select, "collect": collect, "analyse": analyse, "generalise": generalise}
