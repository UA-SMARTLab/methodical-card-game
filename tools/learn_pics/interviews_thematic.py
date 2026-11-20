"""Interviews and thematic analysis: the six steps' pictures. Argued in words, so no exercise."""
from art import bubble
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, doc, person

GREEN = "#86EFAC"


def interview():
    # One interviewer, one participant, open questions and long answers.
    out = person(40, 112, 1.8, INK) + person(160, 112, 1.8, DIM)
    out += g("pop", bubble(18, 22, 60, 30, INK) + text(48, 42, "how? why?", 12, INK), 0)
    out += g("pop", bubble(94, 30, 88, 44, ACC, "#0f172a55", "right"), 1)
    out += g("draw", line([(104, 44), (172, 44)], ACC, 2) + line([(104, 54), (164, 54)], ACC, 2) + line([(104, 64), (150, 64)], ACC, 2), 2)
    return out


def transcribe():
    # The recording becomes a checked transcript.
    out = rect(16, 50, 50, 34, "none", INK, 2.5, 6) + circle(41, 67, 9, "none", INK, 2.5) + circle(41, 67, 3, INK)
    out += g("draw", "".join(line([(78 + k * 6, 67 - h), (78 + k * 6, 67 + h)], ACC, 2.5) for k, h in enumerate((4, 10, 6, 12, 3, 8))), 0)
    out += g("draw", arrow(118, 67, 134, 67, INK, 2.5, head=6), 1)
    out += g("pop", doc(140, 34, 44, 64, INK, 6), 2)
    out += text(41, 104, "recording", 11, INK) + text(162, 116, "transcript", 11, INK)
    return out


def code():
    # Coloured highlights on the transcript, each a code.
    out = rect(20, 16, 92, 120, "none", DIM, 2, 4)
    cols = (ACC, COOL, HOT, ACC, None, COOL)
    for k, c in enumerate(cols):
        y = 32 + k * 18
        out += line([(30, y), (102, y)], DIM, 2.5)
        if c:
            out += g("draw", line([(30, y), (30 + 40 + (k % 2) * 20, y)], c, 6, o=.8), k)
    for k, (c, lab) in enumerate(((ACC, "cost"), (COOL, "harms"), (HOT, "distrust"))):
        out += g("pop", rect(122, 34 + k * 30, 12, 12, c, "none", 0, 2) + text(140, 45 + k * 30, lab, 11, c, "start"), 6 + k)
    return out


def agree():
    # Two coders compare; where they differ, they talk it through and fix the codebook.
    out = doc(16, 30, 34, 44, INK, 4) + doc(150, 30, 34, 44, INK, 4)
    out += person(33, 112, 1.1, INK) + person(167, 112, 1.1, INK)
    out += g("pop", rect(72, 40, 56, 66, "#0f172a66", ACC, 2.5, 3) + text(100, 58, "codebook", 11, ACC)
             + line([(80, 72), (120, 72)], ACC, 2) + line([(80, 84), (112, 84)], ACC, 2) + line([(80, 96), (116, 96)], ACC, 2), 0)
    out += g("draw", arrow(54, 60, 68, 66, DIM, 2, head=5) + arrow(146, 60, 132, 66, DIM, 2, head=5), 1)
    out += g("pop", text(100, 132, "discuss, agree", 12, INK), 2)
    return out


def themes():
    # Codes that belong together are gathered under a theme.
    codes = [(ACC, 30, 108), (ACC, 60, 120), (COOL, 100, 112), (COOL, 132, 122), (HOT, 170, 110)]
    out = "".join(g("pop", rect(x - 13, y - 7, 26, 14, c, "none", 0, 3), k) for k, (c, x, y) in enumerate(codes))
    out += g("draw", arrow(45, 98, 60, 62, INK, 2.5) + arrow(116, 102, 100, 62, INK, 2.5) + arrow(168, 100, 150, 62, INK, 2.5), 5)
    out += g("pop", rect(26, 26, 150, 34, "#0f172a44", GREEN, 3, 8) + text(101, 48, "THEME: cost of feeling ill", 11, GREEN), 6)
    return out


def interpret():
    # The themes answer the research question: an arrow from the theme map back to the question.
    out = "".join(rect(18, 26 + k * 32, 70, 22, "#0f172a44", GREEN, 2.5, 6) for k in range(3))
    out += "".join(g("pop", text(53, 41 + k * 32, f"theme {k + 1}", 11, GREEN), k) for k in range(3))
    out += g("draw", arrow(94, 70, 128, 70, ACC, 3.5), 3)
    out += g("pop", circle(158, 70, 26, "none", ACC, 3) + text(158, 78, "?", 26, ACC), 4)
    out += text(158, 120, "the question", 12, ACC)
    return out


PICTURES = {"interview": interview, "transcribe": transcribe, "code": code, "agree": agree, "themes": themes, "interpret": interpret}
