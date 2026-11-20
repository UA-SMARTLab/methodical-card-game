"""Retrospective cohort: five steps' pictures, from old records to the comparison."""
from learn_pics._kit import INK, DIM, ACC, HOT, g, person, rect, text, arrow, line, doc, carrow


def records():
    out = "".join(g("pop", doc(20 + k * 34, 40 + (k % 2) * 10, 28, 38, INK, 3, fill="#0f172a33"), k) for k in range(5))
    out += text(100, 26, "records kept for another reason", 11, DIM)
    return out + text(100, 120, "payroll, registers", 12, ACC) + text(100, 138, "already there", 11, DIM)


def rewind():
    # The study starts today but places its starting line in the past.
    out = line([(14, 100), (186, 100)], DIM, 2) + text(176, 120, "today", 11, INK) + line([(176, 92), (176, 108)], INK, 3)
    out += g("draw", carrow(172, 84, 110, 30, 42, 84, ACC, 3), 0)
    out += g("pop", line([(42, 92), (42, 108)], ACC, 3) + text(42, 124, "cohort starts", 11, ACC), 1)
    return out + g("pop", text(110, 142, "idea came later", 11, DIM), 2)


def trace():
    out = doc(16, 40, 30, 40, INK, 3) + text(31, 98, "1950", 11, DIM)
    out += g("draw", arrow(52, 60, 96, 60, ACC, 2.5), 0)
    for k in range(4):
        out += g("pop", person(112 + k * 22, 60, 0.75, HOT if k in (0, 2) else INK), 1 + k)
    out += g("pop", doc(150, 88, 26, 34, INK, 2) + text(120, 112, "death", 11, HOT) + text(120, 126, "registry", 11, HOT), 5)
    return out


def compare():
    base = 118
    out = line([(30, base), (176, base)], DIM, 2)
    out += g("grow", rect(52, base - 70, 36, 70, ACC, "none", 0, 3), 0) + g("grow", rect(118, base - 28, 36, 28, INK, "none", 0, 3), 1)
    out += text(70, base + 16, "exposed jobs", 11, ACC) + text(136, base + 16, "other jobs", 11, INK)
    return out + g("pop", text(100, 26, "compare rates", 13, HOT), 2)


def gaps():
    out = doc(30, 30, 50, 70, INK, 0)
    for k in range(4):
        y = 50 + k * 12
        out += line([(38, y), (72, y)], INK, 2) if k != 2 else g("fade", line([(38, y), (72, y)], INK, 2), 0)
    out += g("pop", text(56, 124, "smoking?", 13, HOT), 1)
    out += g("pop", text(140, 60, "not recorded", 12, HOT) + text(140, 80, "cannot be", 12, DIM) + text(140, 96, "asked now", 12, DIM), 2)
    return out


PICTURES = {"records": records, "rewind": rewind, "trace": trace, "compare": compare, "gaps": gaps}
