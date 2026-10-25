#!/usr/bin/env python3
"""Validate the Methodical card data and generate the printable deck, the answer key and the web app.

Usage:  python3 tools/build.py          (from the methodical/ folder or anywhere)
Only the Python standard library is needed.
"""
import html
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def load(name):
    return json.loads((DATA / f"{name}.json").read_text(encoding="utf-8"))


meta = load("meta")
designs = load("designs")
questions = load("questions")
threats = load("threats")
safeguards = load("safeguards")
twists = load("twists")
programs = load("programs")

D = {d["id"]: d for d in designs}
T = {t["id"]: t for t in threats}
S = {s["id"]: s for s in safeguards}
SUIT = {s["id"]: s for s in meta["suits"]}
FAM = {f["id"]: f for f in meta["families"]}
CON = {c["id"]: c for c in meta["constraints"]}

# Safeguard -> threats it counters is derived from threats.countered_by (single source of truth).
counters = defaultdict(list)
for t in threats:
    for sid in t["countered_by"]:
        counters[sid].append(t["id"])
for s in safeguards:
    s["counters"] = counters.get(s["id"], [])


# --------------------------------------------------------------------------- validation
errors, warnings = [], []


def check_ids(ids, table, where, what):
    for i in ids:
        if i not in table:
            errors.append(f"{where}: unknown {what} '{i}'")


for coll, name in [(designs, "design"), (questions, "question"), (threats, "threat"),
                   (safeguards, "safeguard"), (twists, "twist"), (programs, "program")]:
    dupes = [i for i, n in Counter(x["id"] for x in coll).items() if n > 1]
    if dupes:
        errors.append(f"duplicate {name} ids: {dupes}")

for d in designs:
    w = f"design {d['id']}"
    if d["family"] not in FAM:
        errors.append(f"{w}: unknown family {d['family']}")
    check_ids(d["serves"], SUIT, w, "suit")
    check_ids(d["fits"] + d["struggles"], CON, w, "constraint")
    check_ids(d["weak_vs"], T, w, "threat")
    if set(d["fits"]) & set(d["struggles"]):
        errors.append(f"{w}: constraint both fits and struggles: {set(d['fits']) & set(d['struggles'])}")
    if len(d["gist"]) > 150:
        warnings.append(f"{w}: gist is {len(d['gist'])} chars (may overflow card)")
    if len(d["example"]) > 125:
        warnings.append(f"{w}: example is {len(d['example'])} chars (may overflow card)")

best_count = Counter()
for q in questions:
    w = f"question {q['id']}"
    if q["suit"] not in SUIT:
        errors.append(f"{w}: unknown suit {q['suit']}")
    check_ids(q["constraints"], CON, w, "constraint")
    check_ids(q["best"] + q["ok"] + list(q["traps"]), D, w, "design")
    if q["key_threat"] not in T:
        errors.append(f"{w}: unknown key_threat {q['key_threat']}")
    tiers = [set(q["best"]), set(q["ok"]), set(q["traps"])]
    if (tiers[0] & tiers[1]) or (tiers[0] & tiers[2]) or (tiers[1] & tiers[2]):
        errors.append(f"{w}: a design appears in two tiers")
    if not q["best"]:
        errors.append(f"{w}: no best design")
    for b in q["best"]:
        best_count[b] += 1
        if b in D and q["suit"] not in D[b]["serves"]:
            warnings.append(f"{w}: best design {b} does not list suit {q['suit']} in 'serves'")
    if q["key_threat"] in T and not any(q["key_threat"] in D[b]["weak_vs"] for b in q["best"] if b in D):
        warnings.append(f"{w}: key_threat {q['key_threat']} is not a weakness of any best design")
    if len(q["text"]) > 230:
        warnings.append(f"{w}: text is {len(q['text'])} chars (may overflow card)")

for d in designs:
    if best_count[d["id"]] == 0:
        warnings.append(f"design {d['id']} is never the best answer to any question")

for t in threats:
    check_ids(t["countered_by"], S, f"threat {t['id']}", "safeguard")
for s in safeguards:
    for f in s["applies_to"]:
        if f != "any" and f not in FAM:
            errors.append(f"safeguard {s['id']}: unknown family {f}")
    if not s["counters"]:
        warnings.append(f"safeguard {s['id']} counters no threat")
for t in threats:
    if not any(t["id"] in d["weak_vs"] for d in designs):
        warnings.append(f"threat {t['id']} is not in any design's weak_vs list")
for x in twists:
    if x["adds"] is not None and x["adds"] not in CON:
        errors.append(f"twist {x['id']}: unknown constraint {x['adds']}")
for p in programs:
    for i, st in enumerate(p["stages"], 1):
        check_ids(st["accept"], D, f"program {p['id']} stage {i}", "design")
        if st["suit"] not in SUIT:
            errors.append(f"program {p['id']} stage {i}: unknown suit {st['suit']}")

# Defending a design's weaknesses must be possible: every weak_vs threat should have at least
# one safeguard that both counters it and is usable with that design's family.
for d in designs:
    for tid in d["weak_vs"]:
        usable = [s for s in T[tid]["countered_by"]
                  if s in S and ("any" in S[s]["applies_to"] or d["family"] in S[s]["applies_to"])]
        if tid in T and not usable:
            warnings.append(f"design {d['id']}: no usable safeguard against its weakness '{tid}'")


# --------------------------------------------------------------------------- helpers
e = html.escape


def dname(i):
    return D[i]["name"]


def chip(cid):
    c = CON[cid]
    return f'<span class="chip">{c["icon"]} {e(c["name"])}</span>'


def icons(cids):
    return " ".join(f'<span title="{e(CON[c]["name"])}">{CON[c]["icon"]}</span>' for c in cids) or "—"


def pips(n, sym):
    return sym * n + f'<span class="dim">{sym * (3 - n)}</span>'


# --------------------------------------------------------------------------- card renderers
def design_card(d):
    f = FAM[d["family"]]
    suits = " ".join(f'{SUIT[s]["icon"]}&nbsp;{SUIT[s]["name"]}' for s in d["serves"])
    weak = ", ".join(e(T[t]["name"]) for t in d["weak_vs"])
    return f'''<div class="card design" style="--c:{f["color"]}">
  <div class="band">{e(f["name"])}<span class="cid">{e(d["id"])}</span></div>
  <h3>{e(d["name"])}</h3>
  <div class="serves">{suits}</div>
  <p class="gist">{e(d["gist"])}</p>
  <div class="row"><b>Fits</b> {icons(d["fits"])}</div>
  <div class="row"><b>Struggles</b> {icons(d["struggles"])}</div>
  <div class="row weak"><b>Weak vs</b> {weak}</div>
  <div class="row"><b>Cost</b> {pips(d["cost"], "●")} &nbsp; <b>Time</b> {pips(d["time"], "◆")}</div>
  <p class="ex">{e(d["example"])}</p>
</div>'''


def question_card(q):
    s = SUIT[q["suit"]]
    cons = "".join(chip(c) for c in q["constraints"])
    return f'''<div class="card question">
  <div class="band"><span>{s["icon"]} {e(s["name"]).upper()}</span><span class="cid">{e(q["id"])} · {"★" * q["difficulty"]}</span></div>
  <div class="field">{e(q["field"])}</div>
  <h3>{e(q["title"])}</h3>
  <p class="qtext">{e(q["text"])}</p>
  <div class="chips">{cons}</div>
  <div class="hint">{s["icon"]} {e(s["ask"])}</div>
  <div class="foot">Which design answers it?</div>
</div>'''


def question_back(q):
    best = ", ".join(e(dname(i)) for i in q["best"])
    ok = ", ".join(e(dname(i)) for i in q["ok"]) or "—"
    traps = "".join(f'<li><b>{e(dname(i))}</b>: {e(r)}</li>' for i, r in q["traps"].items())
    return f'''<div class="card qback">
  <div class="band"><span>ANSWER · {e(q["title"])}</span><span class="cid">{e(q["id"])}</span></div>
  <div class="tier gold"><b>🥇 Best</b> {best}</div>
  <div class="tier silver"><b>🥈 Defensible</b> {ok}</div>
  <ul class="traps"><li class="th">⚠️ Traps</li>{traps}</ul>
  <p class="why">{e(q["why"])}</p>
  <div class="watch">Watch out for: <b>{e(T[q["key_threat"]]["name"])}</b></div>
</div>'''


def threat_card(t):
    by = ", ".join(e(S[s]["name"]) for s in t["countered_by"])
    return f'''<div class="card threat">
  <div class="band">THREAT<span class="cid">{e(t["id"])}</span></div>
  <h3>{e(t["name"])}</h3>
  <p class="gist">{e(t["text"])}</p>
  <p class="ex">{e(t["example"])}</p>
  <div class="row"><b>Countered by</b> {by}</div>
</div>'''


def safeguard_card(s):
    c = ", ".join(e(T[t]["name"]) for t in s["counters"])
    if "any" in s["applies_to"]:
        fams = "any design"
    else:
        fams = " ".join(f'<span class="dot" style="background:{FAM[f]["color"]}"></span>{e(FAM[f]["name"])}'
                        for f in s["applies_to"])
    return f'''<div class="card safeguard">
  <div class="band">SAFEGUARD<span class="cid">{e(s["id"])}</span></div>
  <h3>{e(s["name"])}</h3>
  <p class="gist">{e(s["text"])}</p>
  <div class="row"><b>Counters</b> {c}</div>
  <div class="row fams"><b>Usable with</b> {fams}</div>
</div>'''


def twist_card(x):
    add = f'<div class="chips">Adds: {chip(x["adds"])}</div>' if x["adds"] else '<div class="chips"><span class="chip">Event</span></div>'
    return f'''<div class="card twist">
  <div class="band">TWIST<span class="cid">{e(x["id"])}</span></div>
  <h3>{e(x["name"])}</h3>
  <p class="gist">{e(x["text"])}</p>
  {add}
</div>'''


def program_card(p):
    st = "".join(f'<li>{SUIT[s["suit"]]["icon"]} {e(s["ask"])}</li>' for s in p["stages"])
    return f'''<div class="card program">
  <div class="band">RESEARCH PROGRAMME<span class="cid">{e(p["id"])}</span></div>
  <h3>{e(p["name"])}</h3>
  <p class="brief">{e(p["brief"])}</p>
  <ol>{st}</ol>
</div>'''


def program_back(p):
    st = "".join(f'<li>{", ".join(e(dname(a)) for a in s["accept"])}</li>' for s in p["stages"])
    return f'''<div class="card program qback">
  <div class="band">PROGRAMME KEY<span class="cid">{e(p["id"])}</span></div>
  <h3>{e(p["name"])}</h3>
  <ol>{st}</ol>
</div>'''


def reference_cards():
    suits = "".join(f'<li><b>{s["icon"]} {e(s["name"])}</b>: {e(s["ask"])}</li>' for s in meta["suits"])
    cl = [f'<li>{c["icon"]} <b>{e(c["name"])}</b>: {e(c["text"])}</li>' for c in meta["constraints"]]
    half = (len(cl) + 1) // 2
    fams = "".join(f'<li><span class="dot" style="background:{f["color"]}"></span>{e(f["name"])}</li>' for f in meta["families"])
    sc = meta["scoring"]
    return [
        f'<div class="card ref"><div class="band">REFERENCE · SUITS</div><ul>{suits}</ul></div>',
        f'<div class="card ref"><div class="band">REFERENCE · CONSTRAINTS 1/2</div><ul>{"".join(cl[:half])}</ul></div>',
        f'<div class="card ref"><div class="band">REFERENCE · CONSTRAINTS 2/2</div><ul>{"".join(cl[half:])}</ul></div>',
        f'''<div class="card ref"><div class="band">REFERENCE · FAMILIES & SCORING</div><ul>{fams}</ul>
  <ul class="score"><li>🥇 Best <b>+{sc["best"]}</b></li><li>🥈 Defensible <b>+{sc["ok"]}</b></li>
  <li>⚠️ Trap <b>{sc["trap"]}</b></li><li>Unlisted <b>{sc["unlisted"]}</b>, or <b>+{sc["appeal_win"]}</b> if the table upholds your appeal</li></ul></div>''',
    ]


# --------------------------------------------------------------------------- print sheet
PER_PAGE = 9


def pages(fronts, backs=None, title=""):
    """Lay cards out 3x3 per A4 page. Backs are mirrored per row for long-edge duplex printing."""
    out = []
    for start in range(0, len(fronts), PER_PAGE):
        chunk = fronts[start:start + PER_PAGE]
        out.append(f'<section class="sheet"><div class="label">{e(title)} · fronts</div><div class="grid">{"".join(chunk)}</div></section>')
        if backs:
            b = backs[start:start + PER_PAGE]
            b += ['<div class="card blank"></div>'] * (len(chunk) - len(b))
            b += ['<div class="card blank"></div>'] * ((-len(b)) % 3)
            mirrored = []
            for r in range(0, len(b), 3):
                mirrored += list(reversed(b[r:r + 3]))
            out.append(f'<section class="sheet"><div class="label">{e(title)} · backs (print duplex, flip on long edge)</div><div class="grid">{"".join(mirrored)}</div></section>')
    return "".join(out)


PRINT_CSS = """
@page { size: A4; margin: 0; }
* { box-sizing: border-box; }
body { margin: 0; font-family: "Inter", "Segoe UI", "Helvetica Neue", Arial, sans-serif; color: #1a1a1a; background: #e5e5e5; }
.sheet { width: 210mm; height: 297mm; padding: 14mm 10.5mm 0; margin: 0 auto 8mm; background: #fff; page-break-after: always; position: relative; }
.label { position: absolute; top: 5mm; left: 10.5mm; font-size: 7pt; color: #888; }
.grid { display: grid; grid-template-columns: repeat(3, 63mm); grid-auto-rows: 88mm; }
.card { width: 63mm; height: 88mm; border: 0.2mm dashed #bbb; padding: 0 3mm 2.5mm; overflow: hidden; font-size: 8.4pt; line-height: 1.3; display: flex; flex-direction: column; gap: 1.5mm; }
.band { margin: 0 -3mm; padding: 1.6mm 3mm; color: #fff; background: var(--c, #222); font-weight: 700; font-size: 7.4pt; letter-spacing: .04em; display: flex; justify-content: space-between; gap: 2mm; }
.cid { font-weight: 400; opacity: .8; }
h3 { margin: .8mm 0 0; font-size: 12.5pt; line-height: 1.12; }
p { margin: 0; }
b { font-weight: 700; }
.dim { opacity: .25; }
.gist { font-size: 8.8pt; }
.serves { font-size: 8pt; color: #444; }
.row { font-size: 8pt; }
.row b { color: #555; text-transform: uppercase; font-size: 6.6pt; letter-spacing: .05em; margin-right: .8mm; }
.ex { margin-top: auto; font-style: italic; color: #555; font-size: 7.4pt; border-top: .2mm solid #ddd; padding-top: 1mm; }
.question .band { background: #111; }
.question .field { font-size: 7.4pt; text-transform: uppercase; letter-spacing: .06em; color: #777; margin-top: .6mm; }
.question h3 { margin-top: 0; }
.qtext { font-size: 10.4pt; line-height: 1.34; }
.hint { margin-top: auto; font-size: 7.6pt; font-style: italic; color: #666; border-top: .2mm solid #ddd; padding-top: 1.2mm; }
.chips { display: flex; flex-wrap: wrap; gap: 1.2mm; font-size: 7.6pt; }
.chip { border: .25mm solid #999; border-radius: 3mm; padding: .2mm 1.6mm; white-space: nowrap; }
.foot { text-align: center; color: #888; font-size: 6.8pt; letter-spacing: .05em; text-transform: uppercase; }
.qback { font-size: 7.4pt; }
.qback .band { background: #444; }
.tier { font-size: 8pt; }
.tier.gold b { color: #8a6d00; }
.tier.silver b { color: #666; }
.traps { margin: 0; padding-left: 3mm; font-size: 7.1pt; }
.traps .th { list-style: none; margin-left: -3mm; font-weight: 700; color: #b91c1c; }
.why { font-size: 7.4pt; }
.watch { margin-top: auto; font-size: 7.6pt; border-top: .2mm solid #ddd; padding-top: 1mm; }
.threat .band { background: #7f1d1d; }
.threat h3 { color: #7f1d1d; }
.safeguard .band { background: #065f46; }
.safeguard h3 { color: #065f46; }
.fams { margin-top: auto; }
.dot { display: inline-block; width: 2mm; height: 2mm; border-radius: 50%; margin: 0 .6mm 0 1mm; vertical-align: middle; }
.twist .band { background: #5b21b6; }
.twist h3 { color: #5b21b6; }
.twist .chips { margin-top: auto; }
.program .band { background: #0c4a6e; }
.program ol { margin: 0; padding-left: 3.5mm; font-size: 7.6pt; display: flex; flex-direction: column; gap: 1.2mm; }
.brief { font-size: 8pt; font-style: italic; }
.ref .band { background: #333; }
.ref ul { margin: 0; padding-left: 0; list-style: none; font-size: 7.3pt; display: flex; flex-direction: column; gap: .9mm; }
.ref .score { margin-top: 1.5mm; border-top: .2mm solid #ddd; padding-top: 1mm; }
.blank { border-color: transparent; }
@media print { body { background: #fff; } .sheet { margin: 0; } .label { display: none; } }
.cover { width: 210mm; margin: 0 auto 8mm; background: #fff; padding: 14mm; font-size: 10pt; line-height: 1.5; }
.cover h1 { margin: 0 0 2mm; } .cover table { border-collapse: collapse; } .cover td { padding: 1mm 4mm 1mm 0; }
@media print { .cover { page-break-after: always; margin: 0; } }
"""


def build_print():
    sections = [
        ("Reference", reference_cards(), None),
        ("Questions", [question_card(q) for q in questions], [question_back(q) for q in questions]),
        ("Designs", [design_card(d) for d in designs], None),
        ("Threats", [threat_card(t) for t in threats], None),
        ("Safeguards", [safeguard_card(s) for s in safeguards], None),
        ("Twists", [twist_card(x) for x in twists], None),
        ("Programmes", [program_card(p) for p in programs], [program_back(p) for p in programs]),
    ]
    rows = "".join(f"<tr><td>{n}</td><td>{len(f)} cards</td><td>{'duplex (answers on back)' if b else 'single-sided'}</td></tr>"
                   for n, f, b in sections)
    total = sum(len(f) for _, f, _ in sections)
    cover = f'''<div class="cover"><h1>{e(meta["title"])}: print-and-play sheets</h1>
<p>{e(meta["tagline"])} Version {e(meta["version"])}. {total} cards, standard poker size (63 × 88 mm), 9 per A4 page.</p>
<table>{rows}</table>
<p>Print at <b>100% / actual size</b>. Question and Programme sheets alternate fronts and backs; print those pages duplex,
flipping on the long edge, so each answer lands behind its question. Everything else can be printed single-sided.
Cut along the dashed lines. Sleeve the cards with a playing card behind them if you want them to shuffle well.</p></div>'''
    body = cover + "".join(pages(f, b, n) for n, f, b in sections)
    doc = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{e(meta["title"])}: print sheets</title>
<meta name="viewport" content="width=device-width, initial-scale=1"><style>{PRINT_CSS}</style></head>
<body>{body}</body></html>'''
    out = ROOT / "print" / "cards.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return out, total


# --------------------------------------------------------------------------- answer key (markdown)
def build_answer_key():
    L = [f"# {meta['title']}: answer key", "",
         "Generated from `data/` by `tools/build.py`. Don't edit by hand.", "",
         "Scoring: 🥇 best +3 · 🥈 defensible +1 · ⚠️ trap −2 · unlisted 0 (or +1 on a successful appeal).", ""]
    by_suit = defaultdict(list)
    for q in questions:
        by_suit[q["suit"]].append(q)
    for s in meta["suits"]:
        L += [f"## {s['icon']} {s['name']}: {s['ask']}", ""]
        for q in by_suit[s["id"]]:
            cons = ", ".join(f"{CON[c]['icon']} {CON[c]['name']}" for c in q["constraints"]) or "none"
            L += [f"### {q['id']} · {q['title']} ({q['field']}, {'★' * q['difficulty']})", "",
                  f"> {q['text']}", "",
                  f"Constraints: {cons}", "",
                  f"- 🥇 **Best:** {', '.join(dname(i) for i in q['best'])}",
                  f"- 🥈 **Defensible:** {', '.join(dname(i) for i in q['ok']) or 'none'}"]
            for i, r in q["traps"].items():
                L.append(f"- ⚠️ **Trap, {dname(i)}:** {r}")
            L += ["", q["why"], "", f"*Watch out for:* **{T[q['key_threat']]['name']}**, countered by "
                  + ", ".join(S[x]["name"] for x in T[q["key_threat"]]["countered_by"]) + ".", ""]
    L += ["## Research programmes (cooperative mode)", ""]
    for p in programs:
        L += [f"### {p['id']} · {p['name']}", "", p["brief"], ""]
        for i, st in enumerate(p["stages"], 1):
            L.append(f"{i}. {SUIT[st['suit']]['icon']} {st['ask']} → **{', '.join(dname(a) for a in st['accept'])}**")
        L.append("")
    L += ["## Coverage", "", "| Design | Family | Best answer to |", "|---|---|---|"]
    for d in designs:
        qs = [q["id"] for q in questions if d["id"] in q["best"]]
        L.append(f"| {d['name']} | {FAM[d['family']]['name']} | {', '.join(qs)} |")
    (ROOT / "ANSWER_KEY.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- web app
def build_app():
    tpl = (ROOT / "app" / "template.html").read_text(encoding="utf-8")
    bundle = {"meta": meta, "designs": designs, "questions": questions, "threats": threats,
              "safeguards": safeguards, "twists": twists, "programs": programs}
    data = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = tpl.replace("/*__DATA__*/null", data)
    # The template is page content only (the hosted version wraps it); the local copy gets its own skeleton.
    out = ROOT / "app" / "index.html"
    out.write_text('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                   '<style>[hidden]{display:none!important}body{margin:0}</style></head><body>\n'
                   + page + "\n</body></html>\n", encoding="utf-8")
    if "--artifact" in sys.argv:
        Path(sys.argv[sys.argv.index("--artifact") + 1]).write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    for w in warnings:
        print("warning:", w)
    for err in errors:
        print("ERROR:", err)
    if errors:
        sys.exit(1)
    p, n = build_print()
    build_answer_key()
    print(f"ok: {len(questions)} questions, {len(designs)} designs, {len(threats)} threats, "
          f"{len(safeguards)} safeguards, {len(twists)} twists, {len(programs)} programmes ({n} printable cards)")
    if (ROOT / "app" / "template.html").exists():
        print("app:", build_app())
