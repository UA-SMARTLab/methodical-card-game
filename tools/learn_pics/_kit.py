"""Shared pieces for the learn pages' moving pictures (200 x 150, drawn with tools/art.py's primitives).

Wrap a shape in g(cls, inner, i) to make it move: cls is one of the motions in learn.CSS ("pop" arrives, "draw"
wipes in from the left, "grow" rises from its bottom edge, "fade" drops out to a ghost, "roll" spins in), and i is
its place in the sequence (each step 0.32 s later). Everything not wrapped stays still. The last frame must be the
whole picture.
"""
from art import INK, DIM, FAINT, ACC, HOT, COOL, line, path, circle, rect, text, arrow, carrow, person, crowd, dice, doc  # noqa: F401

TREAT, CONTROL = ACC, COOL


def g(cls, inner, i=0):
    return f'<g class="{cls}" style="--i:{i}">{inner}</g>'


def pill(x, y, c, filled=True):
    return (f'<g transform="rotate(-30 {x} {y})">' + rect(x - 14, y - 6, 28, 12, c if filled else "none", c, 2, 6)
            + line([(x, y - 6), (x, y + 6)], "#0f172a" if filled else c, 2) + "</g>")


# Seeded random numbers for an exercise (Mulberry32), so the same input gives the same output on every visit.
RNG_JS = r"""function rng(seed) { return () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
  t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const $ = id => document.getElementById(id);
"""
