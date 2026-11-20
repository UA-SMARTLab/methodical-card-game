"""Instrument development and validation: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, doc
from art import check, cross


def define():
    out = g("pop", circle(100, 66, 30, "none", ACC, 3), 0) + g("pop", text(100, 71, "burnout", 13, ACC), 1)
    for i, (x, y, s) in enumerate(((36, 30, "stress"), (164, 30, "depression"), (36, 116, "fatigue"), (164, 116, "job strain"))):
        out += g("pop", text(x, y, s, 11, DIM), 2 + i) + g("draw", line([(x + (12 if x < 100 else -12), y + (6 if y < 66 else -14)), (100 + (-26 if x < 100 else 26), 66 + (-14 if y < 66 else 14))], DIM, 1.5, dash="3 3"), 2 + i)
    out += text(100, 142, "written definition", 11, INK)
    return out


def pool():
    out = ""
    for k in range(12):
        x, y = 22 + (k % 6) * 30, 30 + (k // 6) * 50
        out += g("pop", doc(x, y, 22, 28, INK, 3), k // 2)
    out += text(100, 128, "more items than needed", 12, ACC)
    return out


def sample():
    cols = [ACC, COOL, INK, HOT, "#86EFAC"]
    out = "".join(g("pop", person(24 + k * 19, 70 + (k % 2) * 16, 0.7, cols[k % 5]), k) for k in range(9))
    out += text(100, 30, "varied people", 12, INK)
    out += g("pop", doc(160, 108, 18, 22, DIM, 2) + doc(182, 108, 18, 22, DIM, 2), 9) + text(100, 140, "plus related measures", 11, DIM)
    return out


def select():
    out = ""
    keep = [True, True, False, True, False, True, True, False]
    for k, ok in enumerate(keep):
        x, y = 30 + (k % 4) * 44, 40 + (k // 4) * 52
        out += doc(x, y, 22, 28, INK, 3)
        out += g("pop" if ok else "fade", check(x + 18, y + 18) if ok else cross(x + 18, y + 18), k)
    out += text(100, 142, "one dimension kept", 12, ACC)
    return out


def pattern():
    out = rect(76, 56, 48, 30, "none", ACC, 3, 6) + text(100, 76, "scale", 13, ACC)
    out += g("draw", line([(76, 64), (34, 36)], "#86EFAC", 4), 0) + g("pop", text(44, 28, "should track", 11, "#86EFAC"), 1)
    out += g("draw", line([(124, 64), (166, 36)], "#86EFAC", 4), 0)
    out += g("draw", line([(100, 86), (100, 112)], HOT, 1.5, dash="2 4"), 2) + g("pop", text(100, 126, "should not track", 11, HOT), 3)
    return out


PICTURES = {"define": define, "pool": pool, "sample": sample, "select": select, "pattern": pattern}
