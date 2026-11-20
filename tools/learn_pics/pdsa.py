"""Plan–do–study–act cycles: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, carrow, doc
from art import check, cross


def plan():
    out = doc(40, 34, 44, 60, INK, 4)
    out += g("pop", text(130, 50, "change:", 12, DIM) + text(130, 66, "call-back list", 12, INK), 0)
    out += g("pop", text(130, 92, "predict:", 12, DIM) + text(130, 108, "fewer no-shows", 12, ACC), 1)
    return out


def do():
    out = rect(16, 30, 168, 90, "none", DIM, 2, 6, dash="5 4") + text(100, 136, "one clinic first", 11, INK)
    out += g("grow", rect(30, 70, 34, 38, "none", ACC, 2.5, 4), 0)
    out += g("pop", person(47, 90, 0.6, ACC), 1)
    out += "".join(person(90 + k * 22, 90, 0.6, DIM) for k in range(4))
    return out


def study():
    out = line([(20, 120), (186, 120)], DIM, 2) + line([(20, 120), (20, 26)], DIM, 2)
    ys = [62, 70, 58, 66, 64, 72, 60, 84, 90, 86, 96, 92]
    pts = [(28 + i * 14, y) for i, y in enumerate(ys)]
    out += line([(20, 66), (186, 66)], DIM, 1.5, dash="3 3") + g("draw", line(pts, ACC, 2.5), 0)
    out += g("pop", line([(118, 30), (118, 120)], HOT, 2, dash="4 3") + text(118, 24, "change", 11, HOT), 1)
    out += text(104, 140, "weeks", 11, DIM)
    return out


def act():
    out = ""
    for i, (lab, c, sym) in enumerate((("adopt", "#86EFAC", "c"), ("adapt", ACC, "a"), ("abandon", HOT, "x"))):
        x = 36 + i * 64
        out += g("pop", rect(x - 26, 50, 52, 40, "none", c, 2.5, 6) + text(x, 76, lab, 12, c), i)
    out += g("pop", check(36, 112), 3)
    out += text(100, 140, "then plan the next", 11, INK)
    return out


def iterate():
    out = ""
    for i, (x, r) in enumerate(((40, 16), (92, 22), (154, 30))):
        out += g("draw", circle(x, 74, r, "none", ACC if i == 2 else INK, 2.5), i)
        out += g("pop", text(x, 79, f"{i + 1}", 13, ACC if i == 2 else INK), i)
        if i:
            out += arrow([40, 92][i - 1] + [16, 22][i - 1] + 2, 74, x - r - 2, 74, DIM, 2)
    out += text(100, 136, "linked, growing cycles", 11, INK)
    return out


PICTURES = {"plan": plan, "do": do, "study": study, "act": act, "iterate": iterate}
