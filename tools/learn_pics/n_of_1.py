"""N-of-1 trial: the five steps' pictures (one patient, randomised pairs of periods, blinded, repeated, then a decision)."""
from learn_pics._kit import INK, DIM, HOT, TREAT, CONTROL, g, pill, person, rect, text, arrow, line, circle, dice, doc

# One patient's three pairs of periods: the order inside each pair is chance's (example order, not from a real trial).
ORDER = ["AB", "BA", "BA"]


def _periods(y, upto, i0=0):
    out = ""
    for k, pair in enumerate(ORDER[:upto]):
        for j, t in enumerate(pair):
            x = 40 + (2 * k + j) * 26
            c = TREAT if t == "A" else CONTROL
            out += g("draw", rect(x, y, 24, 18, c, "none", 0, 3) + text(x + 12, y + 14, t, 12, "#0f172a"), i0 + 2 * k + j)
    return out


def one():
    out = g("pop", person(60, 80, 1.6, INK), 0)
    out += g("pop", pill(130, 52, TREAT), 1) + g("pop", pill(130, 104, CONTROL), 2)
    out += g("pop", text(166, 57, "A", 14, TREAT), 1) + g("pop", text(166, 109, "B", 14, CONTROL), 2)
    out += g("pop", text(100, 22, "which works for me?", 13, HOT), 3) + text(60, 132, "one patient", 11, DIM)
    return out


def randomise():
    out = g("roll", dice(22, 50, 26, 2))
    out += _periods(42, 3, 1)
    out += g("pop", text(118, 92, "order by chance", 12, INK), 7)
    for k in range(3):
        out += line([(40 + k * 52, 66), (88 + k * 52, 66)], DIM, 1.5)
        out += text(64 + k * 52, 82, f"pair {k + 1}", 11, DIM)
    return out


def blind():
    out = g("pop", pill(56, 66, INK), 0) + g("pop", pill(112, 66, INK), 1)
    out += g("pop", text(84, 30, "look the same", 13, INK), 2)
    out += person(160, 82, 1.0, INK) + g("pop", text(160, 118, "patient", 11, DIM), 3)
    out += g("pop", doc(18, 100, 22, 28, DIM), 4) + g("pop", text(84, 128, "code kept apart", 11, DIM), 5)
    return out


def repeat():
    out = _periods(28, 3)
    # Symptom score at the end of every period: lower is better; A wins in all three pairs.
    scores = [3.0, 6.0, 6.5, 2.5, 5.5, 3.5]
    pts = []
    for p, s in enumerate(scores):
        x = 52 + p * 26
        y = 72 + s * 8
        pts.append((x, y))
    out += g("draw", line(pts, DIM, 1.5), 6)
    for p, ((x, y), t) in enumerate(zip(pts, "".join(ORDER))):
        out += g("pop", circle(x, y, 4.5, TREAT if t == "A" else CONTROL), 7 + p)
    out += text(100, 140, "symptoms each period", 11, DIM)
    return out


def decide():
    out = person(36, 80, 1.3, INK)
    out += g("draw", arrow(62, 80, 98, 80, INK, 2.5), 0)
    out += g("pop", pill(130, 80, TREAT), 1) + g("pop", text(130, 112, "A, for this patient", 12, TREAT), 2)
    out += g("pop", text(100, 26, "A better in 3 of 3 pairs", 12, HOT), 3)
    return out


PICTURES = {"one": one, "randomise": randomise, "blind": blind, "repeat": repeat, "decide": decide}
