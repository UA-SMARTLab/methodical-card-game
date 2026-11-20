"""Nomological network study: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle
from art import node, check, cross

NODES = [(100, 70, "A"), (40, 36, "B"), (160, 36, "C"), (44, 112, "D"), (156, 112, "E")]


def theory():
    out = ""
    for i, (x, y, s) in enumerate(NODES[1:]):
        out += g("draw", line([(100, 70), (x, y)], DIM, 2), i)
    out += g("draw", line([(40, 36), (44, 112)], DIM, 2), 4)
    out += "".join(g("pop", node(x, y, s, 13, "#0f172a", ACC if s == "A" else INK), 1 + i) for i, (x, y, s) in enumerate(NODES))
    out += text(100, 142, "a net of laws", 12, INK)
    return out


def converge():
    out = node(100, 70, "you", 16, "#0f172a", ACC, size=12)
    out += g("draw", line([(86, 62), (40, 36)], "#86EFAC", 4), 0) + g("pop", text(40, 26, "should track", 11, "#86EFAC"), 1)
    out += g("draw", line([(114, 78), (160, 112)], HOT, 1.5, dash="2 4"), 2) + g("pop", text(156, 132, "should not", 11, HOT), 3)
    out += node(40, 36, "X", 11) + node(160, 112, "Y", 11)
    return out


def groups():
    out = line([(20, 124), (186, 124)], DIM, 2)
    out += g("grow", rect(46, 54, 40, 70, ACC, "none", 0, 3), 0) + g("grow", rect(116, 90, 40, 34, COOL, "none", 0, 3), 1)
    out += text(66, 140, "group 1", 11, ACC) + text(136, 140, "group 2", 11, COOL)
    out += g("pop", text(100, 30, "predicted: 1 > 2", 13, INK), 2)
    return out


def test():
    out = ""
    for i, (x, y, ok) in enumerate(((40, 40, 1), (100, 40, 1), (160, 40, 1), (40, 96, 1), (100, 96, 0), (160, 96, 1))):
        out += rect(x - 22, y - 18, 44, 36, "none", DIM, 2, 5) + g("pop", check(x, y) if ok else cross(x, y), i)
    out += text(100, 140, "five of six hold", 12, INK)
    return out


def miss():
    out = ""
    pts = [(28, 70), (76, 70), (124, 70), (172, 70)]
    labels = ["theory", "measure", "other test", "result"]
    for i, ((x, y), s) in enumerate(zip(pts, labels)):
        out += circle(x, y, 12, "none", INK, 2.5) + text(x, y + 30, s, 11, DIM)
        if i:
            out += line([(pts[i - 1][0] + 12, y), (x - 12, y)], INK, 2.5)
    out += g("pop", cross(172, 70), 0)
    out += "".join(g("pop", text(x, 44, "?", 16, HOT), 1 + i) for i, (x, _) in enumerate(pts[:3]))
    out += text(100, 130, "which link broke?", 12, HOT)
    return out


PICTURES = {"theory": theory, "converge": converge, "groups": groups, "test": test, "miss": miss}
