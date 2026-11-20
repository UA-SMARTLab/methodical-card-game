"""Multivocal literature review: the five steps' pictures (white and grey literature, after Garousi et al. 2019)."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc
from art import bubble, magnifier, check, cross


def decide():
    # Papers on one side, blogs, talks and white papers on the other; the review decides whether to take both.
    out = text(44, 22, "papers", 12, INK) + text(156, 22, "grey", 12, DIM)
    out += "".join(g("pop", doc(22 + k * 16, 32 + k * 6, 22, 28, INK, 2, "#0f172a"), k) for k in range(3))
    out += g("pop", bubble(130, 34, 30, 20, DIM, "#0f172a44", "left", 2), 3)
    out += g("pop", rect(152, 60, 30, 20, "#0f172a44", DIM, 2, 2) + path("M162,64 L174,70 L162,76 Z", DIM, 0, fill=DIM), 4)
    out += g("pop", doc(136, 88, 22, 28, DIM, 2, "#0f172a44"), 5)
    out += g("draw", arrow(66, 100, 92, 124, INK, 2.5, head=6) + arrow(140, 118, 110, 128, DIM, 2.5, head=6), 6)
    return out + g("pop", circle(100, 130, 11, "#0f172a", ACC, 2.5) + text(100, 135, "?", 14, ACC), 7)


def search():
    # A database for papers, the open web for grey sources, and a person to ask.
    out = path("M22,40 a22,8 0 0 0 44,0 a22,8 0 0 0 -44,0 V84 a22,8 0 0 0 44,0 V40", INK, 2.5, fill="#0f172a66")
    out += text(44, 110, "database", 11, INK)
    out += g("pop", circle(150, 58, 30, "#0f172a44", DIM, 2) + line([(120, 58), (180, 58)], DIM, 1.5)
             + path("M150,28 Q132,58 150,88 Q168,58 150,28", DIM, 1.5), 1)
    out += g("pop", text(150, 110, "web", 11, DIM), 2)
    out += g("pop", magnifier(96, 66, 16, ACC), 3)
    out += g("draw", arrow(80, 58, 66, 58, ACC, 2, head=5) + arrow(112, 58, 118, 58, ACC, 2, head=5), 4)
    return out + g("pop", text(100, 136, "+ ask people, backlinks", 11, ACC), 5)


def stop():
    # A ranked list of search hits; the search stops at a rule fixed in advance.
    out = text(60, 20, "search hits", 12, DIM)
    for k in range(8):
        y = 30 + k * 13
        c = INK if k < 5 else DIM
        out += g("draw", rect(24, y, 10, 9, "none", c, 1.5, 2) + line([(40, y + 5), (40 + 60 - (k * 7) % 30, y + 5)], c, 3), k if k < 5 else 6)
    out += g("pop", line([(16, 94), (110, 94)], HOT, 3, "5 4") + text(150, 98, "stop at N", 13, HOT), 5)
    return out + g("pop", text(150, 60, "no new ideas?", 11, ACC) + text(150, 130, "fixed in advance", 11, DIM), 7)


def grade():
    # One grey source, five questions asked of it.
    out = doc(14, 34, 46, 60, DIM, 3, "#0f172a44")
    labels = ["authority", "method", "objectivity", "date", "outlet"]
    for k, lab in enumerate(labels):
        y = 24 + k * 24
        out += g("pop", text(118, y + 5, lab, 12, INK, "middle"), k)
        mark = cross(176, y, 5) if k == 2 else check(176, y, 6)
        out += g("pop", mark, k + 1)
    return out + g("draw", arrow(64, 64, 84, 64, INK, 2.5, head=6), 0) + text(37, 112, "blog post", 11, DIM)


def synthesise():
    # Sources become coded findings, each still traceable to where it came from.
    out = ""
    for k, (c, y) in enumerate(((INK, 22), (DIM, 58), (DIM, 94))):
        out += g("pop", doc(12, y, 22, 28, c, 2, "#0f172a44"), k)
        out += g("draw", line([(38, y + 14), (70, 30 + k * 34)], c, 2, "3 3"), k + 1)
    for k, (lab, c) in enumerate((("theme A", ACC), ("theme B", COOL), ("theme C", ACC))):
        out += g("pop", rect(72, 20 + k * 34, 52, 20, "#0f172a66", c, 2, 10) + text(98, 34 + k * 34, lab, 11, c), 3 + k)
    out += g("draw", arrow(128, 64, 148, 64, INK, 3, head=7), 6)
    out += g("pop", doc(152, 40, 34, 46, INK, 3, "#0f172a"), 7)
    return out + text(169, 104, "review", 11, INK) + text(100, 136, "linked to sources", 11, DIM)


PICTURES = {"decide": decide, "search": search, "stop": stop, "grade": grade, "synthesise": synthesise}
