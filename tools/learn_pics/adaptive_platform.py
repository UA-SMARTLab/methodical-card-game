"""Adaptive / platform trial: the five steps' pictures (one protocol, a shared control, arms dropped and added)."""
from learn_pics._kit import INK, DIM, FAINT, HOT, ACC, COOL, g, rect, text, arrow, line, doc

ARM_Y = [30, 56, 82, 108]


def _arm(y, label, c, x0=56, x1=180, i=0, cls="draw"):
    return g(cls, rect(x0, y, x1 - x0, 16, c, "none", 0, 4) + text(x0 + 6, y + 12, label, 11, "#0f172a", anchor="start"), i)


def protocol():
    out = g("pop", doc(10, 54, 30, 40, INK, 4), 0) + text(32, 110, "one protocol", 11, INK)
    out += _arm(ARM_Y[0], "control", COOL, i=1)
    for k, name in enumerate(["drug 1", "drug 2", "drug 3"]):
        out += _arm(ARM_Y[k + 1], name, ACC, i=2 + k)
    out += text(118, 142, "shared control", 11, COOL)
    return out


def rules():
    out = g("pop", doc(20, 30, 50, 70, INK, 5), 0)
    out += g("pop", text(130, 46, "if worse: stop", 12, HOT), 1) + g("pop", text(130, 70, "if better: confirm", 12, ACC), 2)
    out += g("pop", text(130, 94, "new drug: add", 12, INK), 3)
    out += text(100, 136, "written before any data", 11, DIM)
    return out


def interim():
    out = line([(56, 24), (56, 128)], DIM, 1.5) + _arm(ARM_Y[0], "control", COOL, 56, 120, cls="pop")
    for k, name in enumerate(["drug 1", "drug 2", "drug 3"]):
        out += _arm(ARM_Y[k + 1], name, ACC, 56, 120, cls="pop", i=0)
    out += g("pop", line([(124, 22), (124, 130)], HOT, 2.5, dash="4 3"), 1)
    out += g("pop", text(160, 70, "look at", 12, HOT) + text(160, 86, "the data", 12, HOT), 2)
    out += text(88, 142, "interim analysis", 11, DIM)
    return out


def adapt():
    out = _arm(ARM_Y[0], "control", COOL, 20, 184, cls="pop")
    out += _arm(ARM_Y[1], "drug 1", ACC, 20, 100, cls="pop") + g("fade", rect(100, ARM_Y[1], 84, 16, FAINT, "none", 0, 4), 1)
    out += g("pop", text(142, ARM_Y[1] + 12, "dropped", 11, HOT), 2)
    out += _arm(ARM_Y[2], "drug 2", ACC, 20, 184, cls="pop")
    out += _arm(ARM_Y[3], "drug 4", ACC, 100, 184, i=3) + g("pop", text(60, ARM_Y[3] + 12, "added", 11, INK), 4)
    out += text(100, 142, "time", 11, DIM)
    return out


def concurrent():
    out = rect(20, 34, 164, 16, FAINT, "none", 0, 4) + text(26, 46, "control", 11, INK, anchor="start")
    out += rect(100, 34, 84, 16, COOL, "none", 0, 4) + text(142, 46, "same time", 11, "#0f172a")
    out += _arm(72, "drug 4", ACC, 100, 184, cls="pop", i=0)
    out += g("pop", line([(100, 28), (100, 96)], HOT, 2, dash="4 3"), 1)
    out += g("pop", arrow(142, 70, 142, 54, HOT, 2.5, head=6), 2)
    out += g("pop", text(60, 112, "earlier controls:", 11, DIM) + text(60, 126, "not comparable", 11, DIM), 3)
    out += g("pop", text(142, 112, "compare with", 11, HOT) + text(142, 126, "these", 11, HOT), 4)
    return out


PICTURES = {"protocol": protocol, "rules": rules, "interim": interim, "adapt": adapt, "concurrent": concurrent}
