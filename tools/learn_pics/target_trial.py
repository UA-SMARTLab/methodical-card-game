"""Target trial emulation: five steps' pictures, from the question to the emulated comparison."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, TREAT, CONTROL, g, person, rect, text, arrow, line, dice
from art import check, cylinder


def question():
    out = g("pop", dice(50, 70, 36, 5, COOL), 0) + g("pop", text(50, 116, "ideal trial", 12, COOL), 1)
    out += g("draw", arrow(80, 70, 116, 70, INK, 2.5, dash="5 4"), 2)
    out += g("pop", cylinder(124, 44, 46, 54, INK), 3) + text(147, 116, "records", 12, INK)
    return out + text(100, 140, "emulate one with the other", 11, DIM)


def protocol():
    rows = ["eligibility", "strategies", "assignment", "follow-up", "outcome", "analysis"]
    out = rect(36, 14, 128, 128, "none", COOL, 2.5, 4, dash="5 4")
    for k, s in enumerate(rows):
        y = 34 + k * 19
        out += g("pop", check(54, y - 4, 6, COOL, 2.5) + text(70, y, s, 12, INK, "start"), k)
    return out


def time_zero():
    out = line([(14, 92), (186, 92)], DIM, 2) + text(100, 140, "time", 11, DIM)
    out += g("pop", line([(80, 60), (80, 120)], ACC, 3) + text(80, 52, "time zero", 12, ACC), 0)
    out += g("pop", text(46, 80, "eligible", 11, INK) + text(42, 112, "starts drug", 11, INK), 1)
    out += g("draw", arrow(84, 80, 180, 80, INK, 2.5), 2) + g("pop", text(140, 112, "outcomes count", 11, HOT), 3)
    return out


def assign():
    out = ""
    for k in range(3):
        out += person(30 + k * 20, 48, 0.75, TREAT) + person(30 + k * 20, 110, 0.75, CONTROL)
    out += text(50, 78, "started drug", 11, TREAT) + text(50, 140, "did not", 11, CONTROL)
    # Adjustment stands in for the coin: weights balance the measured confounders.
    out += g("pop", rect(110, 52, 80, 46, "none", INK, 2, 6) + text(150, 72, "adjust for", 12, INK) + text(150, 88, "confounders", 12, INK), 0)
    out += g("draw", arrow(76, 50, 106, 66, DIM, 2), 1) + g("draw", arrow(76, 108, 106, 86, DIM, 2), 2)
    return out + g("pop", text(150, 118, "as if random", 12, ACC), 3)


def compare():
    base = 120
    out = line([(30, base), (176, base)], DIM, 2)
    out += g("grow", rect(52, base - 44, 36, 44, TREAT, "none", 0, 3), 0) + g("grow", rect(118, base - 70, 36, 70, CONTROL, "none", 0, 3), 1)
    out += text(70, base + 16, "strategy A", 11, TREAT) + text(136, base + 16, "strategy B", 11, CONTROL)
    return out + g("pop", text(100, 24, "as the trial would", 13, ACC), 2)


PICTURES = {"question": question, "protocol": protocol, "time_zero": time_zero, "assign": assign, "compare": compare}
