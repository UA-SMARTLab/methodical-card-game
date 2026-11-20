"""Mendelian randomization: five steps' pictures, from the shuffle at conception to the estimate."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line
from art import helix, node, cross


def shuffle():
    out = person(50, 40, 1.0, INK) + person(150, 40, 1.0, INK) + text(100, 28, "parents", 11, DIM)
    out += g("draw", arrow(60, 58, 90, 86, DIM, 2), 0) + g("draw", arrow(140, 58, 110, 86, DIM, 2), 0)
    for k in range(3):
        out += g("pop", person(60 + k * 40, 112, 0.85, ACC if k != 1 else COOL), 1 + k)
    return out + text(100, 144, "variants dealt at conception", 11, ACC)


def variants():
    out = g("draw", helix(14, 50, 186, 14, 4), 0)
    out += g("pop", rect(84, 32, 34, 36, "none", ACC, 2.5, 4), 1) + g("pop", text(101, 88, "variant", 12, ACC), 2)
    out += g("draw", arrow(101, 96, 101, 120, INK, 2.5), 3) + g("pop", text(101, 138, "higher LDL", 12, INK), 4)
    return out


def assumptions():
    out = node(36, 100, "G", 15, "none", ACC) + node(100, 100, "X", 15) + node(164, 100, "Y", 15) + node(132, 34, "U", 14, "none", DIM)
    out += arrow(124, 45, 106, 84, DIM, 2, "5 4") + arrow(140, 45, 158, 84, DIM, 2, "5 4")
    out += g("draw", arrow(52, 100, 83, 100, ACC, 3.5), 0) + arrow(117, 100, 147, 100, INK, 2.5)
    out += g("pop", line([(46, 86), (120, 42)], HOT, 2, dash="3 4") + cross(82, 64, 6), 1)
    from art import path
    out += g("pop", path("M44,116 Q100,150 156,116", HOT, 2, dash="3 4") + cross(100, 132, 6), 2)
    return out + g("pop", text(36, 28, "G: variant", 12, ACC, "start"), 3)


def two_samples():
    out = rect(14, 30, 80, 70, "none", INK, 2, 6) + rect(106, 30, 80, 70, "none", INK, 2, 6)
    out += g("pop", text(54, 58, "variant → LDL", 12, ACC) + text(54, 78, "study 1", 11, DIM), 0)
    out += g("pop", text(146, 58, "variant → CHD", 12, HOT) + text(146, 78, "study 2", 11, DIM), 1)
    out += g("draw", arrow(54, 104, 94, 124, INK, 2) + arrow(146, 104, 106, 124, INK, 2), 2)
    return out + g("pop", text(100, 142, "combine summaries", 12, INK), 3)


def estimate():
    from art import scatter
    out = line([(24, 128), (184, 128)], DIM, 2) + line([(24, 128), (24, 16)], DIM, 2)
    pts = [(46, 110), (70, 96), (92, 88), (116, 70), (140, 58), (162, 40)]
    out += "".join(g("pop", scatter([p], 4, ACC), i) for i, p in enumerate(pts))
    out += g("draw", line([(30, 124), (176, 32)], INK, 2.5), 6)
    return out + text(104, 144, "variant on LDL", 11, DIM) + text(30, 16, "variant on CHD", 11, DIM, "start")


PICTURES = {"shuffle": shuffle, "variants": variants, "assumptions": assumptions, "two_samples": two_samples, "estimate": estimate}
