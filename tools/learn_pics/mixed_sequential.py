"""Mixed methods (sequential): the five steps' pictures. Argued in words, so no exercise."""
from art import axes, bubble
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, person

GREEN = "#86EFAC"


def bars(x, y, c=ACC, hs=(14, 34, 22, 40)):
    return axes(x, y, 48, 48, INK, 2) + "".join(rect(x + 6 + k * 10, y + 48 - h, 7, h, c, "none", 0, 1) for k, h in enumerate(hs))


def talk(x, y, c=INK):
    return bubble(x, y, 44, 28, c, "#0f172a55") + line([(x + 8, y + 10), (x + 36, y + 10)], c, 2) + line([(x + 8, y + 19), (x + 28, y + 19)], c, 2)


def order():
    # Two orders: numbers then stories (explanatory), or stories then numbers (exploratory).
    out = g("pop", bars(14, 12), 0) + g("draw", arrow(72, 36, 104, 36, INK, 3), 1) + g("pop", talk(116, 18), 2)
    out += text(170, 64, "explain", 11, INK)
    out += g("pop", talk(16, 90), 3) + g("draw", arrow(72, 108, 104, 108, INK, 3), 4) + g("pop", bars(116, 86), 5)
    out += text(182, 140, "test", 11, INK)
    out += text(38, 140, "explore", 11, INK)
    return out


def phase1():
    # The survey comes first and finds a gap between two groups.
    out = axes(30, 24, 130, 90, INK, 2.5)
    out += g("grow", rect(54, 54, 34, 60, ACC, "none", 0, 2), 0) + g("grow", rect(110, 92, 34, 22, ACC, "none", 0, 2), 1)
    out += g("pop", arrow(160, 58, 160, 88, HOT, 2.5, head=6) + arrow(160, 88, 160, 58, HOT, 2.5, head=6), 2)
    out += g("pop", text(164, 50, "why?", 13, HOT), 3)
    out += text(71, 132, "group A", 11, INK) + text(127, 132, "group B", 11, INK) + text(100, 16, "SURVEY", 12, ACC)
    return out


def connect():
    # Interviewees are picked from among the survey respondents, chosen by what the survey found.
    out = "".join(person(22 + (k % 6) * 18, 38 + (k // 6) * 28, 0.75, DIM) for k in range(18))
    picks = [(40, 38), (94, 66), (58, 94)]
    out += "".join(g("pop", person(x, y, 0.75, ACC) + circle(x, y - 3, 11, "none", ACC, 2), k) for k, (x, y) in enumerate(picks))
    out += g("draw", arrow(128, 66, 150, 66, INK, 3), 3)
    out += g("pop", talk(150, 50), 4)
    out += text(70, 132, "survey sample", 11, DIM) + text(166, 100, "interviews", 11, INK)
    return out


def build():
    # The other way round: words heard in interviews become the items of a questionnaire.
    out = talk(14, 30, ACC) + talk(30, 76, ACC)
    out += g("draw", arrow(82, 72, 108, 72, INK, 3), 0)
    out += rect(114, 22, 72, 104, "none", INK, 2.5, 4)
    for k in range(4):
        out += g("pop", rect(122, 34 + k * 22, 10, 10, "none", INK, 2, 1) + line([(138, 39 + k * 22), (176, 39 + k * 22)], ACC, 2.5), 1 + k)
    out += text(150, 142, "new items", 11, ACC) + text(50, 130, "their words", 11, ACC)
    return out


def integrate():
    # Both results side by side in one display; they confirm, expand or clash.
    out = rect(14, 20, 172, 88, "none", DIM, 2, 4) + line([(100, 20), (100, 108)], DIM, 2)
    out += g("pop", bars(30, 36), 0) + g("pop", talk(122, 44), 1)
    out += text(57, 102, "numbers", 11, ACC) + text(144, 102, "stories", 11, INK)
    out += g("pop", text(46, 132, "confirm", 12, GREEN), 2) + g("pop", text(100, 132, "expand", 12, COOL), 3)
    out += g("pop", text(156, 132, "clash", 12, HOT), 4)
    return out


PICTURES = {"order": order, "phase1": phase1, "connect": connect, "build": build, "integrate": integrate}
