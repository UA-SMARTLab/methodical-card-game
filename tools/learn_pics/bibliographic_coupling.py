"""Bibliographic coupling: the five steps' pictures. The exercise is co-citation's, run from the other side of the same
citation graph, so it is imported rather than written twice."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, doc
from learn_pics.co_citation import CITED, CITING, REFS, exercise  # noqa: F401  (exercise is this page's too)


def gather():
    # Each paper brings its own reference list.
    out = ""
    for k, x in enumerate((30, 100, 170)):
        out += g("pop", doc(x - 14, 16, 28, 36, COOL, 0, "#0f172a", 2), k)
        out += g("draw", "".join(line([(x - 18, 66 + r * 14), (x + 18 - (r * 9) % 20, 66 + r * 14)], DIM, 3) for r in range(4)), 3 + k)
    return out + text(100, 136, "each paper's references", 11, DIM)


def shared():
    # Papers 1 and 2 both cite works A and B: their coupling strength is 2, fixed the day the later one appears.
    out = ""
    for p, refs in enumerate(REFS):
        for r in refs:
            on = p in (0, 1) and r in (0, 1)
            out += g("draw" if on else "fade", arrow(CITING[p][0], CITING[p][1] - 4, CITED[r][0], CITED[r][1] + 30,
                                                     ACC if on else DIM, 2 if on else 1.5, head=5), 1 if on else 0)
    out += "".join(doc(x - 11, y, 22, 28, ACC if k in (0, 1) else INK, 0, "#0f172a", 2) for k, (x, y) in enumerate(CITED))
    out += "".join(doc(x - 11, y, 22, 28, COOL if k in (0, 1) else DIM, 2, "#0f172a44", 2) for k, (x, y) in enumerate(CITING))
    return out + g("pop", text(100, 144, "2 shared references", 13, ACC), 3)


def measure():
    # Raw count or correlation: two ways to turn shared references into a strength.
    out = text(54, 24, "count", 12, INK) + text(146, 24, "correlation", 12, INK)
    out += g("pop", text(54, 76, "2", 40, ACC), 1)
    for k, (x, y) in enumerate(((114, 112), (126, 96), (138, 90), (150, 74), (162, 66), (174, 50))):
        out += g("pop", f'<circle cx="{x}" cy="{y}" r="4" fill="{ACC}"/>', 2 + k)
    out += line([(110, 118), (180, 44)], DIM, 2, "4 3")
    return out + line([(100, 30), (100, 130)], DIM, 2) + text(146, 136, "r = 0.9", 12, ACC)


def fronts():
    # Papers linked by shared references form groups: today's research fronts.
    pts = [(36, 44), (64, 34), (50, 72), (140, 50), (168, 78), (128, 92)]
    out = ""
    for k, (a, b, w) in enumerate(((0, 1, 4), (0, 2, 3), (1, 2, 5), (3, 4, 3), (4, 5, 4), (3, 5, 5), (2, 5, 1))):
        out += g("draw", line([pts[a], pts[b]], COOL if w > 1 else DIM, w), k)
    for k, (x, y) in enumerate(pts):
        out += g("pop", doc(x - 9, y - 12, 18, 24, COOL, 2, "#0f172a", 2), k)
    return out + g("pop", text(52, 116, "front 1", 12, COOL) + text(148, 124, "front 2", 12, COOL), 7)


def now():
    # A paper published today already has its references, so it is coupled at once; generic references blur links.
    out = line([(18, 120), (182, 120)], DIM, 2) + text(100, 140, "published today", 11, DIM)
    out += doc(30, 50, 26, 34, COOL, 2, "#0f172a", 2) + doc(146, 50, 26, 34, COOL, 2, "#0f172a", 2)
    out += g("draw", line([(60, 66), (142, 66)], ACC, 5), 1) + g("pop", text(100, 56, "linked now", 12, ACC), 2)
    out += g("pop", rect(76, 82, 48, 22, "#0f172a", HOT, 2, 4) + text(100, 97, "a textbook", 11, HOT), 3)
    return out + g("pop", text(100, 30, "shared by all: blurs", 11, HOT), 4)


PICTURES = {"gather": gather, "shared": shared, "measure": measure, "fronts": fronts, "now": now}
