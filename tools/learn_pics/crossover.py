"""Crossover trial: the five steps' pictures (two sequences, AB and BA, with a washout between the periods)."""
from learn_pics._kit import INK, DIM, FAINT, HOT, TREAT, CONTROL, g, person, rect, text, arrow, line, dice, circle


def _bar(x, y, w, c, label, i):
    return g("draw", rect(x, y, w, 20, c, "none", 0, 4) + text(x + w / 2, y + 15, label, 13, "#0f172a"), i)


def sequence():
    out = g("roll", dice(34, 75, 34, 3))
    out += g("draw", arrow(56, 66, 92, 44, INK, 2.5), 1) + g("draw", arrow(56, 84, 92, 106, INK, 2.5), 1)
    for k in range(3):
        out += g("pop", person(108 + k * 16, 42, 0.7, INK), 2 + k) + g("pop", person(108 + k * 16, 108, 0.7, INK), 2 + k)
    out += g("pop", text(172, 46, "AB", 14, TREAT), 5) + g("pop", text(172, 112, "BA", 14, CONTROL), 6)
    out += text(34, 124, "CHANCE", 12, INK)
    return out


def period1():
    out = person(22, 44, 0.75, INK) + person(22, 108, 0.75, INK)
    out += _bar(40, 34, 56, TREAT, "A", 0) + _bar(40, 98, 56, CONTROL, "B", 1)
    out += rect(104, 34, 86, 20, "none", FAINT, 1.5, 4, dash="3 3") + rect(104, 98, 86, 20, "none", FAINT, 1.5, 4, dash="3 3")
    out += g("pop", text(68, 78, "period 1", 12, INK), 2) + text(147, 78, "still to come", 11, DIM)
    return out


def washout():
    out = person(22, 44, 0.75, INK) + person(22, 108, 0.75, INK)
    out += rect(40, 34, 56, 20, TREAT, "none", 0, 4) + rect(40, 98, 56, 20, CONTROL, "none", 0, 4)
    # The drug's level falls away during the gap, before the second treatment starts.
    out += g("draw", line([(96, 36), (104, 44), (112, 50), (124, 53)], TREAT, 2.5), 0)
    out += g("draw", line([(96, 100), (104, 108), (112, 114), (124, 117)], CONTROL, 2.5), 1)
    out += g("pop", text(112, 80, "washout", 13, INK), 2) + g("pop", text(112, 140, "nothing given", 11, DIM), 3)
    return out


def period2():
    out = person(22, 44, 0.75, INK) + person(22, 108, 0.75, INK)
    out += rect(40, 34, 56, 20, TREAT, "none", 0, 4) + rect(40, 98, 56, 20, CONTROL, "none", 0, 4)
    out += text(68, 49, "A", 13, "#0f172a") + text(68, 113, "B", 13, "#0f172a")
    out += _bar(130, 34, 56, CONTROL, "B", 0) + _bar(130, 98, 56, TREAT, "A", 1)
    out += g("pop", text(158, 78, "period 2", 12, INK), 2) + g("pop", text(113, 140, "same people, swapped", 11, DIM), 3)
    return out


def within():
    base = 120
    out = line([(20, base), (184, base)], DIM, 2)
    # Each person's own two results, joined: the difference is read inside the person.
    pairs = [(40, 70, 52), (80, 62, 46), (120, 80, 60), (160, 66, 50)]
    for k, (x, a, b) in enumerate(pairs):
        out += g("pop", circle_pair(x, a, b), k)
    out += g("pop", text(100, 22, "each is own control", 13, HOT), 5)
    out += text(60, 140, "on A", 11, TREAT) + text(140, 140, "on B", 11, CONTROL)
    return out


def circle_pair(x, a, b):
    return (line([(x - 8, a), (x + 8, b)], INK, 1.5) + circle(x - 8, a, 4.5, TREAT) + circle(x + 8, b, 4.5, CONTROL))


PICTURES = {"sequence": sequence, "period1": period1, "washout": washout, "period2": period2, "within": within}
