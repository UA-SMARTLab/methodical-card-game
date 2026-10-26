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


# --------------------------------------------------------------------------- print sheets
sys.path.insert(0, str(Path(__file__).resolve().parent))
import cards  # noqa: E402  (needs the tools/ folder on sys.path)

e = html.escape
cx = cards.Ctx(meta, designs, threats, safeguards)


def dname(i):
    return D[i]["name"]


SHEET_CSS = """
@page { size: A4; margin: 0; }
body { margin: 0; background: #d7dbe0; font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; }
.sheet { width: 210mm; height: 297mm; margin: 0 auto 8mm; background: #fff; position: relative; break-after: page; display: grid; place-items: center; }
.grid { display: grid; grid-template-columns: repeat(3, 63mm); grid-auto-rows: 88mm; gap: 1mm; }
.mats { display: grid; gap: 8mm; }
.label { position: absolute; top: 6mm; left: 10mm; font-size: 8pt; color: #888; }
.cover, .key { width: 210mm; min-height: 297mm; margin: 0 auto 8mm; background: #fff; padding: 16mm; box-sizing: border-box; break-after: page; font-size: 10pt; line-height: 1.45; }
.cover h1, .key h1 { font: 800 26pt/1.1 "Bricolage Grotesque", sans-serif; margin: 0 0 4mm; }
.cover table { border-collapse: collapse; margin: 4mm 0; } .cover td { padding: 1mm 6mm 1mm 0; border-bottom: .2mm solid #ddd; }
.key table { border-collapse: collapse; width: 100%; font-size: 8.4pt; }
.key th, .key td { text-align: left; vertical-align: top; padding: 1.2mm 2mm; border-bottom: .2mm solid #ddd; }
.key th { font: 700 8pt "Barlow Condensed", sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #555; }
.key td.id { font-weight: 600; white-space: nowrap; } .key .trap { color: #b42318; }
.key h2 { font: 700 13pt "Barlow Condensed", sans-serif; letter-spacing: .04em; text-transform: uppercase; margin: 5mm 0 1mm; }
@media print { body { background: #fff; } .sheet, .cover, .key { margin: 0; } .label { display: none; } }
"""


def sheets(cards_html, title, per=9):
    out = []
    for k in range(0, len(cards_html), per):
        out.append(f'<section class="sheet"><div class="label">{e(title)} · page {k // per + 1}</div><div class="grid">{"".join(cards_html[k:k + per])}</div></section>')
    return "".join(out)


def page(title, body):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><link rel="stylesheet" href="{cards.FONTS_URL}">
<style>{cards.CARD_CSS}{SHEET_CSS}</style></head><body>{body}</body></html>"""


def build_print():
    decks = [
        ("Reference", cards.reference_cards(cx)),
        ("Questions", [cards.question_card(cx, q) for q in questions]),
        ("Designs", [cards.design_card(cx, d) for d in designs]),
        ("Threats", [cards.threat_card(cx, t, i + 1) for i, t in enumerate(threats)]),
        ("Safeguards", [cards.safeguard_card(cx, s, i + 1) for i, s in enumerate(safeguards)]),
        ("Twists", [cards.twist_card(cx, x) for x in twists]),
    ]
    total = sum(len(c) for _, c in decks)
    rows = "".join(f"<tr><td>{n}</td><td>{len(c)} cards</td><td>{-(-len(c) // 9)} pages</td></tr>" for n, c in decks)
    cover = f"""<div class="cover"><h1>{e(meta["title"])}: print and play</h1>
<p>{e(meta["tagline"])} Version {e(meta["version"])}. {total} cards in standard poker size (63 × 88 mm), 9 per A4 page,
plus {len(programs)} research-programme mats (A6, 2 per page).</p>
<table>{rows}<tr><td>Programme mats</td><td>{len(programs)} mats</td><td>{-(-len(programs) // 2)} pages</td></tr></table>
<p><b>Printing.</b> Print at <b>100% / actual size</b> with background graphics on. Cut along the card edges.
All cards share one back (<code>backs.html</code>): print it on the reverse of each sheet, or skip it and use opaque card sleeves,
the easiest way to make a print-and-play deck shuffle like a real one.</p>
<p><b>Answers</b> are in the separate answer-key booklet (<code>answer-key.html</code>), so the top card of a face-down deck never gives its answer away.</p></div>"""
    mats = [cards.program_mat(cx, p) for p in programs]
    mat_pages = "".join(f'<section class="sheet"><div class="label">Programme mats</div><div class="mats">{"".join(mats[k:k + 2])}</div></section>'
                        for k in range(0, len(mats), 2))
    body = cover + "".join(sheets(c, n) for n, c in decks) + mat_pages
    out = ROOT / "print" / "cards.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(page(f'{meta["title"]}: print sheets', body), encoding="utf-8")
    (ROOT / "print" / "backs.html").write_text(page(f'{meta["title"]}: card backs', sheets([cards.card_back()] * 9, "Card backs")), encoding="utf-8")
    build_answer_booklet()
    return out, total


def build_answer_booklet():
    by_suit = defaultdict(list)
    for q in questions:
        by_suit[q["suit"]].append(q)
    body = f'<div class="key"><h1>{e(meta["title"])}: answer key</h1><p>🥇 best +3 · 🥈 defensible +1 · ⚠️ trap −2 · unlisted 0 (appeal for +1). Read the <i>why</i> aloud: that is where the learning happens.</p>'
    for st in meta["suits"]:
        body += f'<h2>{e(st["name"])}</h2><table><tr><th>Card</th><th>🥇 Best</th><th>🥈 Defensible</th><th>⚠️ Traps</th><th>Why</th></tr>'
        for q in by_suit[st["id"]]:
            traps = "<br>".join(f'<span class="trap">{e(dname(i))}</span>' for i in q["traps"])
            body += (f'<tr><td class="id">{q["id"]} {e(q["title"])}</td><td>{e(", ".join(dname(i) for i in q["best"]))}</td>'
                     f'<td>{e(", ".join(dname(i) for i in q["ok"])) or "–"}</td><td>{traps}</td><td>{e(q["why"])} <i>Watch out for: {e(T[q["key_threat"]]["name"])}.</i></td></tr>')
        body += "</table>"
    body += "<h2>Research programmes</h2><table><tr><th>Mat</th><th>Accepted designs, stage by stage</th></tr>"
    for p in programs:
        body += f'<tr><td class="id">{p["id"]} {e(p["name"])}</td><td>' + "<br>".join(
            f'{i}. {e(", ".join(dname(a) for a in st["accept"]))}' for i, st in enumerate(p["stages"], 1)) + "</td></tr>"
    body += "</table></div>"
    (ROOT / "print" / "answer-key.html").write_text(page(f'{meta["title"]}: answer key', body), encoding="utf-8")


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
    rendered = {
        "designs": {d["id"]: cards.design_card(cx, d) for d in designs},
        "questions": {q["id"]: cards.question_card(cx, q) for q in questions},
        "threats": {t["id"]: cards.threat_card(cx, t, i + 1) for i, t in enumerate(threats)},
        "safeguards": {x["id"]: cards.safeguard_card(cx, x, i + 1) for i, x in enumerate(safeguards)},
        "twists": {x["id"]: cards.twist_card(cx, x) for x in twists},
        "programs": {p["id"]: cards.program_mat(cx, p) for p in programs},
    }
    bundle = {"meta": meta, "designs": designs, "questions": questions, "threats": threats,
              "safeguards": safeguards, "twists": twists, "programs": programs, "cards": rendered}
    data = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = tpl.replace("/*__DATA__*/null", data).replace("/*__CARD_CSS__*/", cards.CARD_CSS)
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
