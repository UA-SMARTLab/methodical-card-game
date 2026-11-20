"""Pilot or feasibility study: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, crowd
from art import check, cross


def question():
    out = ""
    for i, s in enumerate(("recruit?", "retain?", "deliver?", "measure?")):
        out += g("pop", text(60 + (i % 2) * 80, 46 + (i // 2) * 40, s, 14, ACC if i == 0 else INK), i)
    out += text(100, 136, "can it be done?", 12, DIM)
    return out


def criteria():
    out = ""
    for i, (lab, c) in enumerate((("go", "#86EFAC"), ("change", ACC), ("stop", HOT))):
        y = 40 + i * 32
        out += g("pop", circle(50, y, 11, c) + text(118, y + 5, lab, 14, c), i)
    out += text(100, 140, "agreed before starting", 11, INK)
    return out


def size():
    out = crowd(40, 50, 4, 2, 18, 30, 0.7, lambda i, j: INK)
    out += g("pop", text(140, 60, "enough to", 12, INK) + text(140, 76, "answer feasibility", 11, INK), 0)
    out += text(100, 136, "not powered for effect", 11, HOT)
    return out


def rehearse():
    out = rect(110, 30, 76, 88, "none", DIM, 2, 6, dash="5 4") + text(148, 24, "main study", 11, DIM)
    out += g("pop", rect(18, 58, 52, 40, "none", ACC, 2.5, 6) + text(44, 82, "pilot", 13, ACC), 0)
    out += g("draw", arrow(74, 78, 104, 78, INK, 2.5), 1)
    for i, (s, n) in enumerate((("approached", "40"), ("assigned", "30"), ("followed", "24"))):
        out += g("pop", text(148, 52 + i * 26, f"{s} {n}", 11, INK), 2 + i)
    return out


def decide():
    out = rect(20, 40, 70, 50, "none", "#86EFAC", 3, 6) + text(55, 70, "proceed?", 13, "#86EFAC")
    out += g("pop", check(55, 108, 12), 0)
    out += rect(112, 40, 70, 50, "none", DIM, 2, 6, dash="5 4") + text(147, 70, "p < 0.05?", 13, DIM)
    out += g("pop", cross(147, 108, 10), 1)
    out += text(100, 140, "decide, don't test", 11, INK)
    return out


PICTURES = {"question": question, "criteria": criteria, "size": size, "rehearse": rehearse, "decide": decide}
