"""Realist review: the six steps' pictures (context, mechanism, outcome, after RAMESES)."""
from learn_pics._kit import INK, DIM, ACC, HOT, COOL, g, rect, text, arrow, line, circle, path, doc, person
from art import gear, star, check, cross, bubble, magnifier


def ask():
    # Not "does it work?" but four questions around the programme.
    out = g("pop", gear(100, 76, 20, ACC, 10), 0)
    for k, (x, y, lab) in enumerate(((44, 28, "for whom?"), (156, 28, "where?"), (44, 128, "how?"), (156, 128, "why?"))):
        out += g("pop", text(x, y, lab, 13, INK), 1 + k)
        out += g("draw", line([(x + (12 if x < 100 else -12), y + (8 if y < 76 else -14)), (100 + (-24 if x < 100 else 24), 76 + (-14 if y < 76 else 14))], DIM, 2, "3 3"), 1 + k)
    return out


def theory():
    # The programme theory as a chain: if we do this, people respond so, and this happens.
    out = ""
    for k, (x, lab) in enumerate(((34, "do"), (100, "respond"), (166, "result"))):
        out += g("pop", rect(x - 26, 54, 52, 30, "#0f172a66", INK, 2.5, 6) + text(x, 74, lab, 12, INK), 2 * k)
        if k < 2:
            out += g("draw", arrow(x + 28, 69, x + 38, 69, ACC, 2.5, head=5), 2 * k + 1)
    return out + text(100, 30, "programme theory", 13, ACC) + text(100, 118, "how it should work", 11, DIM)


def search():
    # A loop: search, read, change what you search for.
    out = path("M100,30 A44,44 0 1 1 56,74", DIM, 2.5) + arrow(58, 70, 60, 56, DIM, 2.5, head=6)
    out += g("pop", magnifier(100, 74, 16, ACC), 0)
    for k, (x, y, c) in enumerate(((156, 36, INK), (166, 92, COOL), (40, 112, DIM))):
        out += g("pop", doc(x - 10, y - 12, 20, 26, c, 2, "#0f172a", 2), 1 + k)
    return out + g("pop", text(100, 142, "search again", 12, ACC), 4)


def appraise():
    # Pieces of one document judged one by one: relevant and rigorous, or not.
    out = doc(16, 20, 60, 108, DIM, 0, "#0f172a44", 2)
    for k, ok in enumerate((True, False, True, True)):
        y = 34 + k * 24
        out += g("draw", rect(24, y, 44, 12, ACC if ok else DIM, "none", 0, 2), k)
        out += g("draw", arrow(72, y + 6, 96, y + 6, DIM, 2, head=5), k)
        out += g("pop", (check(108, y + 6, 6) if ok else cross(108, y + 6, 5)), 4 + k)
    out += text(152, 46, "relevant?", 12, INK) + text(152, 70, "rigorous?", 12, INK)
    return out + text(152, 112, "piece by", 11, DIM) + text(152, 126, "piece", 11, DIM)


def cmo():
    # Context, mechanism, outcome: the same programme fires in one context and not in another.
    out = ""
    for k, (y, fires) in enumerate(((40, True), (106, False))):
        out += g("pop", circle(36, y, 22, "none", COOL, 2.5, dash="4 3") + text(36, y + 4, f"C{k + 1}", 13, COOL), 3 * k)
        out += g("pop", gear(98, y, 14, ACC if fires else DIM, 9), 3 * k + 1)
        out += g("draw", arrow(60, y, 80, y, INK, 2.5, head=5) + arrow(116, y, 140, y, INK if fires else DIM, 2.5, head=5), 3 * k + 1)
        out += g("pop", star(162, y, 14, ACC) if fires else cross(162, y, 8), 3 * k + 2)
    return out + text(36, 76, "context", 11, COOL) + text(98, 76, "mechanism", 11, ACC) + text(162, 76, "outcome", 11, INK)


def refine():
    # Version 1 of the theory, tested against patterns, becomes version 2.
    out = rect(14, 44, 56, 34, "#0f172a66", DIM, 2.5, 6) + text(42, 66, "theory v1", 12, DIM)
    out += g("draw", arrow(72, 61, 128, 61, INK, 3, head=7), 1) + g("pop", text(100, 50, "test", 11, INK), 1)
    out += g("pop", rect(130, 44, 56, 34, "#0f172a66", ACC, 2.5, 6) + text(158, 66, "theory v2", 12, ACC), 2)
    out += g("draw", path("M158,82 Q158,122 100,122 Q42,122 42,82", DIM, 2, dash="4 3"), 3)
    return out + g("pop", text(100, 140, "and again", 11, DIM), 4)


PICTURES = {"ask": ask, "theory": theory, "search": search, "appraise": appraise, "cmo": cmo, "refine": refine}
