"""Prior art review: the four steps' pictures (what was public, when, and whether the idea is new and not obvious)."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc
from art import magnifier, check, cross


def search():
    # Patents, papers, products, theses: everything that was public is searched, not only journals.
    out = ""
    items = [(doc(14, 20, 26, 34, INK, 3, "#0f172a"), "patent", 27, 66),
             (doc(58, 20, 26, 34, INK, 3, "#0f172a"), "paper", 71, 66),
             (path("M110,36 L126,28 L142,36 L126,44 Z", INK, 2.5, fill="#0f172a") + path("M110,36 V52 L126,60 L142,52 V36 M126,44 V60", INK, 2.5), "product", 126, 76),
             (rect(160, 22, 28, 34, "#0f172a", INK, 2.5, 2) + line([(166, 22), (166, 56)], DIM, 2), "thesis", 174, 66)]
    for k, (shape, lab, x, y) in enumerate(items):
        out += g("pop", shape + text(x, y + 10, lab, 11, DIM), k)
    out += g("pop", magnifier(92, 116, 16, ACC), 4)
    return out + g("pop", text(150, 124, "all public", 12, ACC), 5)


def date():
    # A timeline: only what was public before the filing date counts.
    out = line([(14, 92), (186, 92)], INK, 2.5) + text(100, 136, "time", 11, DIM)
    out += g("pop", line([(130, 40), (130, 108)], ACC, 3) + text(130, 32, "filing date", 12, ACC), 0)
    for k, x in enumerate((30, 62, 96)):
        out += g("pop", doc(x - 10, 56, 20, 26, INK, 2, "#0f172a", 2) + check(x, 108, 6), 1 + k)
    out += g("pop", doc(150, 56, 20, 26, DIM, 2, "#0f172a44", 2) + cross(160, 108, 5), 4)
    return out + g("pop", text(62, 128, "counts", 11, "#86EFAC") + text(160, 128, "too late", 11, HOT), 5)


def new():
    # Your idea's features against one earlier source: if it already has them all, the idea is not new.
    out = text(50, 20, "your idea", 12, ACC) + text(150, 20, "earlier source", 12, INK)
    for k in range(4):
        y = 36 + k * 24
        c = ACC if k < 4 else DIM
        out += g("pop", rect(22, y, 56, 16, "#0f172a66", c, 2, 3) + rect(122, y, 56, 16, "#0f172a66", INK, 2, 3), k)
        out += g("draw", line([(80, y + 8), (120, y + 8)], DIM, 2, "3 3"), k)
        out += g("pop", check(100, y + 8, 5), 4 + k)
    return out + g("pop", text(100, 142, "all there: not new", 12, HOT), 8)


def obvious():
    # Two known pieces that a skilled person would put together: new, but obvious.
    out = doc(16, 26, 28, 36, INK, 3, "#0f172a") + doc(16, 84, 28, 36, INK, 3, "#0f172a")
    out += text(30, 76, "A", 12, INK) + text(30, 134, "B", 12, INK)
    out += g("draw", arrow(50, 46, 100, 70, DIM, 2.5, head=6) + arrow(50, 102, 100, 80, DIM, 2.5, head=6), 1)
    out += g("pop", circle(124, 75, 20, "#FCD34D33", ACC, 3) + text(124, 81, "A+B", 13, ACC), 2)
    out += g("pop", text(170, 60, "skilled", 11, COOL) + text(170, 74, "person:", 11, COOL), 3)
    return out + g("pop", text(170, 96, "obvious?", 13, HOT), 4)


PICTURES = {"search": search, "date": date, "new": new, "obvious": obvious}
