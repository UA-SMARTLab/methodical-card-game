"""Rapid review: the five steps' pictures (a systematic review with named shortcuts, after Tricco et al. 2015)."""
import math

from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc, person
from art import bubble, check, cross


def scope():
    # The reviewer and the decision-maker agree a narrow question and a deadline.
    out = person(36, 70, 1.1, COOL) + person(164, 70, 1.1, ACC)
    out += text(36, 120, "reviewer", 11, COOL) + text(164, 120, "decision-maker", 11, ACC)
    out += g("pop", bubble(62, 26, 76, 26, INK, "#0f172a", "left", 2) + text(100, 44, "narrow question", 11, INK), 1)
    out += g("pop", rect(70, 70, 60, 26, "#0f172a", HOT, 2.5, 4) + text(100, 88, "6 weeks", 13, HOT), 2)
    return out


def search():
    # Of five sources, two are searched; date and language limits cut the rest.
    out = ""
    for k in range(5):
        x = 22 + k * 38
        on = k < 2
        out += g("pop", path(f"M{x - 14},40 a14,5 0 0 0 28,0 a14,5 0 0 0 -28,0 V70 a14,5 0 0 0 28,0 V40", INK if on else DIM, 2.5, fill="#0f172a66"), k)
        if not on:
            out += g("pop", cross(x, 56, 7), 5 + k)
    out += g("pop", text(100, 104, "since 2015, English only", 12, ACC), 8)
    return out + text(100, 134, "fewer sources", 11, DIM)


def screen():
    # One reviewer screens everything; a second checks a sample.
    out = person(40, 56, 1.0, INK) + text(40, 104, "screens all", 11, INK)
    for k in range(6):
        out += g("pop", doc(76 + (k % 3) * 22, 22 + (k // 3) * 34, 18, 24, INK, 0, "#0f172a", 1.5), k)
    out += person(166, 56, 1.0, COOL) + text(166, 104, "checks some", 11, COOL)
    out += g("pop", check(120, 84, 6), 6)
    return out + g("draw", arrow(148, 50, 128, 40, COOL, 2, head=5), 7)


def summarise():
    # Findings written as a short narrative, not a forest plot.
    out = doc(28, 18, 76, 104, INK, 0, "#0f172a", 3)
    for k in range(6):
        out += g("draw", line([(38, 36 + k * 13), (94 - (k * 11) % 24, 36 + k * 13)], INK if k else ACC, 3), k)
    out += g("pop", path("M144,62 L156,54 L168,62 L156,70 Z", DIM, 2) + cross(156, 62, 14), 6)
    return out + text(156, 96, "no pooling", 12, DIM)


def report():
    # A clock and the list of cut corners, each one named.
    out = circle(46, 70, 32, "none", INK, 3) + line([(46, 70), (46, 48)], ACC, 3) + line([(46, 70), (62, 78)], INK, 2.5)
    out += "".join(line([(46 + 27 * math.cos(math.radians(a)), 70 + 27 * math.sin(math.radians(a))),
                         (46 + 32 * math.cos(math.radians(a)), 70 + 32 * math.sin(math.radians(a)))], INK, 2) for a in range(0, 360, 30))
    for k, lab in enumerate(("1 database", "English only", "1 screener")):
        out += g("pop", text(96, 50 + k * 22, "✂", 13, HOT, "start") + text(112, 50 + k * 22, lab, 12, INK, "start"), k)
    return out + text(100, 136, "every shortcut named", 11, ACC)


PICTURES = {"scope": scope, "search": search, "screen": screen, "summarise": summarise, "report": report}
