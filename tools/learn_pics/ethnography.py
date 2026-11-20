"""Ethnography: the five steps' pictures. Argued in words, so no exercise."""
from art import bubble
from learn_pics._kit import INK, DIM, ACC, g, rect, text, arrow, carrow, line, circle, path, doc, person


def tent():
    return path("M10,128 L46,70 L82,128 Z", INK, 3, fill="#0f172a33") + path("M38,128 L46,108 L54,128", INK, 2.5)


def enter():
    # The researcher arrives at the edge of the group and is let in by one member, a key informant.
    out = line([(10, 128), (190, 128)], DIM, 2)
    out += "".join(person(x, 110, 1.1, DIM) for x in (120, 146, 172))
    out += g("draw", arrow(20, 100, 76, 100, ACC, 3), 0)
    out += g("pop", person(88, 110, 1.2, ACC), 1)
    out += g("pop", person(120, 110, 1.1, INK), 2) + g("pop", text(120, 76, "key informant", 11, INK), 3)
    out += text(40, 144, "outsider", 11, ACC)
    return out


def take_part():
    # Watching and taking part at once: the researcher works among the others and writes it down afterwards.
    out = line([(10, 128), (190, 128)], DIM, 2) + rect(30, 92, 140, 10, "none", DIM, 2, 2)
    out += "".join(person(x, 116, 1.1, DIM) for x in (48, 84, 152))
    out += g("pop", person(118, 116, 1.2, ACC), 0)
    out += g("pop", rect(96, 30, 44, 34, "#0f172a66", ACC, 2.5, 2) + line([(104, 42), (132, 42)], ACC, 2) + line([(104, 52), (124, 52)], ACC, 2), 1)
    out += g("draw", arrow(118, 66, 118, 86, ACC, 2.5, head=6), 2)
    out += text(56, 46, "field notes", 12, ACC)
    return out


def stay():
    # Months, not days: the calendar fills while the notebook pile grows.
    out = tent() + line([(10, 128), (190, 128)], DIM, 2)
    for k in range(6):
        out += g("pop", rect(100 + (k % 3) * 28, 20 + (k // 3) * 26, 22, 20, "none", INK if k < 5 else ACC, 2, 2), k)
    out += g("grow", "".join(rect(104 + k * 6, 120 - 8 * k, 60, 7, "#0f172a66", ACC, 2, 1) for k in range(4)), 6)
    out += text(142, 92, "months", 12, INK)
    return out


def follow():
    # One conversation raises a question nobody planned, which leads to the next conversation.
    out = person(30, 112, 1.2, ACC) + person(84, 112, 1.1, INK)
    out += g("pop", bubble(56, 30, 52, 30, INK), 0) + g("pop", text(82, 52, "?", 18, ACC), 1)
    out += g("draw", carrow(108, 44, 150, 40, 158, 88, ACC, 3), 2)
    out += g("pop", person(160, 112, 1.1, INK), 3)
    out += text(130, 144, "new question", 11, ACC)
    return out


def interpret():
    # The notes are read through the group's own culture: a lens between the notes and the account.
    out = "".join(doc(14 + k * 10, 34 + k * 8, 26, 34, DIM, 3) for k in range(3))
    out += g("pop", circle(100, 72, 24, "#0f172a33", ACC, 3.5) + text(100, 77, "culture", 12, ACC), 0)
    out += g("draw", arrow(60, 72, 74, 72, INK, 2.5, head=6) + arrow(126, 72, 142, 72, INK, 2.5, head=6), 1)
    out += g("pop", doc(150, 50, 34, 44, INK, 4), 2)
    out += text(167, 112, "account", 12, INK) + text(34, 112, "notes", 12, DIM)
    return out


PICTURES = {"enter": enter, "take_part": take_part, "stay": stay, "follow": follow, "interpret": interpret}
