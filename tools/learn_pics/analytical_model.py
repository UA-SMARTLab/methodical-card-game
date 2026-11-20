"""Analytical or mathematical theory: the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle
from art import bubble, check, cross, globe


def claim():
    out = person(40, 96, 1.0, INK) + g("pop", bubble(60, 30, 124, 46, INK), 0)
    out += g("pop", text(122, 52, "X because of Y", 13, ACC), 1) + g("pop", text(122, 68, "in words", 11, DIM), 2)
    return out


def assume():
    out = ""
    for i, s in enumerate(("A1: x ≥ 0", "A2: y = f(x)", "A3: no limit on z")):
        out += g("draw", text(100, 46 + i * 30, s, 14, ACC if i < 2 else DIM), i)
    out += text(100, 140, "every assumption written", 11, INK)
    return out


def derive():
    out = text(100, 34, "A1 + A2", 14, ACC)
    out += g("draw", arrow(100, 44, 100, 64, INK, 2.5), 0) + g("pop", text(100, 82, "lemma", 13, INK), 1)
    out += g("draw", arrow(100, 90, 100, 108, INK, 2.5), 2) + g("pop", text(100, 126, "theorem ∎", 15, ACC), 3)
    return out


def compare():
    out = rect(18, 40, 70, 50, "none", DIM, 2, 6, dash="5 4") + text(53, 32, "words say", 11, DIM) + text(53, 70, "rises", 14, INK)
    out += rect(112, 40, 70, 50, "none", ACC, 2.5, 6) + text(147, 32, "maths says", 11, ACC) + text(147, 70, "rises, then falls", 11, ACC)
    out += g("pop", text(100, 118, "gap found", 14, HOT), 1)
    return out


def reality():
    out = rect(18, 44, 60, 40, "none", ACC, 2.5, 6) + text(48, 69, "model", 13, ACC)
    out += globe(150, 64, 22, INK)
    out += g("draw", arrow(82, 64, 124, 64, INK, 2.5), 0)
    out += g("pop", check(48, 108), 1) + g("pop", text(48, 132, "logic: sure", 11, "#86EFAC"), 2)
    out += g("pop", text(150, 108, "?", 18, HOT), 3) + g("pop", text(146, 132, "assumptions: test", 11, HOT), 4)
    return out


PICTURES = {"claim": claim, "assume": assume, "derive": derive, "compare": compare, "reality": reality}
