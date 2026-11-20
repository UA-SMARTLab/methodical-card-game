"""Design science (build and evaluate): the five steps' pictures."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, person, rect, text, arrow, line, circle, carrow
from art import gear, bubble, check, cross, doc, eye


def problem():
    out = person(50, 92, 1.0, INK) + g("pop", bubble(70, 26, 110, 40, HOT), 0)
    out += g("pop", text(125, 51, "this keeps failing", 12, HOT), 1)
    out += text(100, 140, "unsolved and important", 11, DIM)
    return out


def build():
    out = g("roll", gear(70, 70, 22, ACC, 9), 0) + g("roll", gear(112, 92, 16, INK, 7), 1)
    out += g("pop", rect(138, 44, 44, 30, "none", COOL, 2.5, 4) + text(160, 64, "app", 12, COOL), 2)
    out += text(100, 138, "a purposeful artifact", 11, INK)
    return out


def evaluate():
    out = rect(20, 46, 60, 44, "none", ACC, 2.5, 6) + text(50, 73, "artifact", 12, ACC)
    out += person(120, 80, 0.85, INK) + g("pop", eye(166, 56, 0.9, INK), 0)
    out += g("pop", check(120, 30), 1) + g("pop", cross(146, 30), 2)
    out += text(100, 130, "with users, in context", 11, INK)
    return out


def iterate():
    out = g("draw", carrow(60, 50, 100, 18, 140, 50, ACC, 2.5), 0) + text(100, 14 + 22, "build", 12, ACC)
    out += g("draw", carrow(140, 92, 100, 124, 60, 92, COOL, 2.5), 1) + text(100, 104, "evaluate", 12, COOL)
    out += circle(50, 70, 14, "none", INK, 2.5) + circle(150, 70, 14, "none", INK, 2.5)
    out += text(100, 142, "until good enough", 11, INK)
    return out


def communicate():
    out = doc(90, 40, 22, 30, INK, 3)
    out += g("draw", arrow(86, 56, 40, 56, ACC, 2.5), 0) + g("draw", arrow(116, 56, 160, 56, COOL, 2.5), 0)
    out += g("pop", person(28, 92, 0.75, ACC), 1) + g("pop", person(172, 92, 0.75, COOL), 2)
    out += text(40, 128, "technical", 11, ACC) + text(160, 128, "managerial", 11, COOL)
    return out


PICTURES = {"problem": problem, "build": build, "evaluate": evaluate, "iterate": iterate, "communicate": communicate}
