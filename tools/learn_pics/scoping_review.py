"""Scoping review: the six steps' pictures (Arksey & O'Malley's five stages, plus consultation after Levac et al.)."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc, person
from art import magnifier, bubble, check, cross


def question():
    # A wide lens on a topic, with its facets named.
    out = path("M100,30 L30,120 H170 Z", ACC, 2.5, fill="#FCD34D22")
    out += g("pop", circle(100, 30, 10, "#0f172a", INK, 2.5) + text(100, 35, "?", 13, INK), 0)
    for k, lab in enumerate(("population", "concept", "context")):
        out += g("pop", text(54 + k * 46, 112, lab, 11, INK), 1 + k)
    return out + g("pop", text(100, 140, "broad question", 12, ACC), 4)


def search():
    # Many kinds of source, published and unpublished, pulled into one pool.
    out = ""
    for k, (x, y, c) in enumerate(((22, 20, INK), (60, 14, INK), (98, 20, DIM), (136, 14, DIM), (168, 22, DIM))):
        out += g("pop", doc(x - 2, y, 22, 28, c, 2, "#0f172a44", 2), k)
        out += g("draw", arrow(x + 9, y + 32, 100, 92, c, 1.5, head=5), 5)
    out += g("pop", rect(60, 96, 80, 30, "#0f172a66", ACC, 2.5, 6) + text(100, 116, "all hits", 12, ACC), 6)
    return out + text(48, 144, "published", 11, INK) + text(150, 144, "unpublished", 11, DIM)


def select():
    # Two reviewers sift the hits against criteria; some go through, some are set aside.
    out = path("M40,26 H160 L118,74 V104 L82,116 V74 Z", INK, 2.5, fill="#0f172a44")
    for k, x in enumerate((60, 84, 108, 132)):
        out += g("pop", doc(x - 8, 6, 16, 18, DIM, 0, "#0f172a", 1.5), k)
    out += g("pop", doc(92, 120, 16, 20, ACC, 0, "#0f172a", 1.5) + check(126, 130, 6), 5)
    out += g("pop", cross(176, 40, 6) + cross(176, 62, 6), 4)
    return out + person(24, 72, .7, COOL) + person(24, 108, .7, COOL) + text(28, 140, "2 reviewers", 11, COOL)


def chart():
    # A data-charting form: one row per study, the same columns for all.
    cols = ("study", "where", "method")
    out = "".join(text(40 + k * 60, 26, c, 11, ACC) for k, c in enumerate(cols))
    out += line([(14, 32), (186, 32)], ACC, 2)
    for r in range(5):
        y = 42 + r * 19
        out += g("draw", "".join(rect(18 + k * 60, y, 48, 12, "#0f172a66", INK if r < 4 else DIM, 1.5, 2) for k in range(3)), r)
    return out + text(100, 144, "same items, every study", 11, DIM)


def map():
    # Counts per area: a bar for each theme, and an empty column that is a gap. No pooled effect.
    base = 120
    out = line([(20, base), (184, base)], DIM, 2)
    for k, h in enumerate((70, 44, 26, 0, 54)):
        x = 30 + k * 32
        if h:
            out += g("grow", rect(x, base - h, 22, h, COOL, "none", 0, 2), k)
        else:
            out += g("pop", rect(x, base - 40, 22, 40, "none", HOT, 2, 2, dash="3 3") + text(x + 11, base - 46, "gap", 12, HOT), k)
    return out + text(100, 140, "studies per theme", 11, DIM) + g("pop", text(100, 22, "no pooling, no grading", 11, ACC), 6)


def consult():
    # Stakeholders look at the map and answer back.
    out = rect(70, 30, 60, 46, "#0f172a66", INK, 2.5, 4)
    out += "".join(rect(78 + k * 12, 64 - h, 8, h, COOL, "none", 0, 1) for k, h in enumerate((24, 16, 8, 0, 20)))
    for k, x in enumerate((40, 100, 160)):
        out += g("pop", person(x, 112, .9, ACC), k)
    out += g("pop", bubble(10, 64, 44, 22, INK, "#0f172a", "left", 2) + text(32, 79, "missing!", 11, INK), 3)
    return out + g("pop", bubble(146, 64, 44, 22, INK, "#0f172a", "left", 2) + text(168, 79, "this gap", 11, INK), 4)


PICTURES = {"question": question, "search": search, "select": select, "chart": chart, "map": map, "consult": consult}
