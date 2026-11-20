"""Umbrella review: the four steps' pictures (a review of reviews, after Ioannidis 2009)."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, path, doc
from art import check, cross


def frame():
    # The umbrella's canopy names every treatment and outcome before any review is opened.
    out = path("M20,70 Q100,-6 180,70 Z", ACC, 3, fill="#FCD34D22") + line([(100, 30), (100, 128)], INK, 3)
    for k, lab in enumerate(("drug A", "drug B", "exercise", "surgery")):
        out += g("pop", text(46 + k * 36, 62, lab, 11, INK), k)
    return out + g("pop", text(150, 112, "set up front", 12, ACC), 4)


def gather():
    # Several systematic reviews, each with its own forest plot, pulled under one roof.
    out = path("M20,50 Q100,0 180,50 Z", ACC, 2.5, fill="#FCD34D22")
    for k in range(4):
        x = 22 + k * 42
        out += g("pop", doc(x, 66, 32, 42, INK, 0, "#0f172a", 2) + line([(x + 16, 72), (x + 16, 102)], DIM, 1.5, "2 2")
                 + path(f"M{x + 8},96 L{x + 14},92 L{x + 20},96 L{x + 14},100 Z", ACC, 1.5, fill=ACC), k)
    return out + text(100, 132, "reviews, not studies", 11, DIM)


def compare():
    # One row per comparison: benefit and harm side by side.
    out = text(40, 22, "comparison", 11, DIM) + text(118, 22, "benefit", 11, "#86EFAC") + text(166, 22, "harm", 11, HOT)
    for k, (b, h) in enumerate(((44, 10), (26, 24), (36, 4), (12, 30))):
        y = 34 + k * 24
        out += text(40, y + 12, f"A vs {'BCDE'[k]}", 12, INK)
        out += g("grow", rect(96, y + 2, b, 12, "#86EFAC", "none", 0, 2), k) + g("grow", rect(150, y + 2, h, 12, HOT, "none", 0, 2), k)
    return out + text(100, 142, "side by side", 11, ACC)


def seams():
    # Reviews with different criteria and dates, and one option nobody reviewed.
    out = ""
    for k, (yr, ok) in enumerate((("2009", True), ("2015", True), ("2021", True))):
        x = 16 + k * 46
        out += doc(x, 30, 32, 42, INK, 2, "#0f172a", 2) + g("pop", text(x + 16, 90, yr, 12, ACC), k)
    out += g("pop", rect(156, 30, 32, 42, "none", HOT, 2, 3, dash="4 3") + text(172, 56, "?", 18, HOT), 3)
    out += g("pop", text(172, 90, "no review", 11, HOT), 4)
    return out + text(70, 126, "different criteria, dates", 11, DIM)


PICTURES = {"frame": frame, "gather": gather, "compare": compare, "seams": seams}
