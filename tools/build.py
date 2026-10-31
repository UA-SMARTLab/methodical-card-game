#!/usr/bin/env python3
"""Validate the Methodical card data and generate, for every language in i18n/languages.json,
the printable deck, the answer-key booklet and the web app (plus the English ANSWER_KEY.md).

Usage:  python3 tools/build.py   (from anywhere)
Only the Python standard library is needed.
"""
import html
import json
import re
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
    if not (d.get("ref") or {}).get("url", "").startswith("https://"):
        errors.append(f"{w}: no key reference (ref.url)")
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
for x in threats + safeguards:
    if not (x.get("ref") or {}).get("url", "").startswith("https://"):
        errors.append(f"{x['id']}: no key reference (ref.url)")
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


# --------------------------------------------------------------------------- languages
sys.path.insert(0, str(Path(__file__).resolve().parent))
import art  # noqa: E402  (needs the tools/ folder on sys.path)
import cards  # noqa: E402
import i18n  # noqa: E402

e = html.escape
DATA_ALL = {"meta": meta, "designs": designs, "questions": questions, "threats": threats,
            "safeguards": safeguards, "twists": twists, "programs": programs}


class Lang:
    """Everything one language's outputs need: translated data, its strings, and where its files go."""

    def __init__(self, info):
        self.code, self.info = info["code"], info
        self.rtl = info.get("dir") == "rtl"
        d = i18n.translated(DATA_ALL, self.code)
        self.d = d
        self.D = {x["id"]: x for x in d["designs"]}
        self.T = {x["id"]: x for x in d["threats"]}
        table = i18n.ui_strings(self.code)
        self.ui, self.art = table["ui"], table["art"]
        self.S = i18n.Strings(self.ui)
        sub = "" if self.code == "en" else self.code
        self.print_dir = ROOT / "print" / sub
        self.app_dir = ROOT / "app" / sub

    def activate(self):
        """Point the card renderer at this language and return its rendering context."""
        cards.S = self.S
        art.TR = self.art
        return cards.Ctx(self.d["meta"], self.d["designs"], self.d["threats"], self.d["safeguards"])

    def html_attrs(self):
        return f'lang="{self.code}" dir="{"rtl" if self.rtl else "ltr"}"'

    def fonts(self):
        extra = self.info.get("font")
        return cards.FONTS_URL + (f"&family={extra.replace(' ', '+')}:wght@400;600;700" if extra else "")

    def extra_font_link(self):
        extra = self.info.get("font")
        return f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={extra.replace(" ", "+")}:wght@400;600;700&display=swap">' if extra else ""

    def lang_css(self):
        extra = self.info.get("font")
        if not extra:
            return ""
        # Scripts such as Arabic need their own font everywhere, and letter-spacing would break the joined letters.
        return (f'html[lang="{self.code}"] body, html[lang="{self.code}"] body * {{ font-family: "{extra}", "IBM Plex Sans", system-ui, sans-serif !important;'
                " letter-spacing: 0 !important; }"
                # Such scripts sit taller than Latin, so card names need more line height (and a bit less size on two lines).
                f' html[lang="{self.code}"] .tcg .nm b {{ line-height: 1.45; padding-block: .1em; }}'
                f' html[lang="{self.code}"] .tcg .nm b.s3 {{ font-size: calc(var(--u) * 2.7); line-height: 1.25; }}'
                f' html[lang="{self.code}"] .tcg .nm b.s4 {{ font-size: calc(var(--u) * 2.35); line-height: 1.25; }}')


SHEET_CSS = """
@page { size: A4; margin: 0; }
body { margin: 0; background: #d7dbe0; font-family: "IBM Plex Sans Condensed", "Arial Narrow", sans-serif; }
.sheet { width: 210mm; height: 297mm; margin: 0 auto 8mm; background: #fff; position: relative; break-after: page; display: grid; place-items: center; }
.grid { display: grid; grid-template-columns: repeat(3, 63mm); grid-auto-rows: 88mm; gap: 1mm; }
.mats { display: grid; gap: 8mm; }
.label { position: absolute; top: 6mm; inset-inline-start: 10mm; font-size: 8pt; color: #888; }
.cover, .key { width: 210mm; min-height: 297mm; margin: 0 auto 8mm; background: #fff; padding: 16mm; box-sizing: border-box; break-after: page; font-size: 10pt; line-height: 1.45; }
.cover h1, .key h1 { font: 800 26pt/1.1 "Bricolage Grotesque", sans-serif; margin: 0 0 4mm; }
.cover table { border-collapse: collapse; margin: 4mm 0; } .cover td { padding: 1mm 6mm 1mm 0; border-bottom: .2mm solid #ddd; }
.key table { border-collapse: collapse; width: 100%; font-size: 8.4pt; }
.key th, .key td { text-align: start; vertical-align: top; padding: 1.2mm 2mm; border-bottom: .2mm solid #ddd; }
.key th { font: 700 8pt "Barlow Condensed", sans-serif; letter-spacing: .06em; text-transform: uppercase; color: #555; }
.key td.id { font-weight: 600; white-space: nowrap; } .key .trap { color: #b42318; }
.key h2 { font: 700 13pt "Barlow Condensed", sans-serif; letter-spacing: .04em; text-transform: uppercase; margin: 5mm 0 1mm; }
.langs { float: inline-end; font-size: 9pt; } .langs a { margin-inline-start: 2mm; color: #2340A8; }
@media print { body { background: #fff; } .sheet, .cover, .key { margin: 0; } .label, .langs { display: none; } }
"""


def lang_links(g, langs, page_name):
    """Links to the same print page in every other language."""
    up = "" if g.code == "en" else "../"
    return '<span class="langs">' + "".join(
        f'<a href="{up}{"" if x["code"] == "en" else x["code"] + "/"}{page_name}" hreflang="{x["code"]}">{e(x["name"])}</a>'
        for x in langs if x["code"] != g.code) + "</span>"


def sheets(g, cards_html, title, per=9):
    out = []
    for k in range(0, len(cards_html), per):
        out.append(f'<section class="sheet"><div class="label">{e(g.S("print.page", deck=title, n=k // per + 1))}</div>'
                   f'<div class="grid">{"".join(cards_html[k:k + per])}</div></section>')
    return "".join(out)


def page(g, title, body):
    return f"""<!doctype html>
<html {g.html_attrs()}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title><link rel="stylesheet" href="{g.fonts()}">
<style>{cards.CARD_CSS}{SHEET_CSS}{g.lang_css()}</style></head><body>{body}<script>{cards.FIT_JS}</script></body></html>"""


def build_print(g, langs):
    cx = g.activate()
    d, S = g.d, g.S
    decks = [
        (S("print.reference"), cards.reference_cards(cx)),
        (S("deck.questions"), [cards.question_card(cx, q) for q in d["questions"]]),
        (S("deck.designs"), [cards.design_card(cx, x) for x in d["designs"]]),
        (S("deck.threats"), [cards.threat_card(cx, t, i + 1) for i, t in enumerate(d["threats"])]),
        (S("deck.safeguards"), [cards.safeguard_card(cx, x, i + 1) for i, x in enumerate(d["safeguards"])]),
        (S("deck.twists"), [cards.twist_card(cx, x) for x in d["twists"]]),
    ]
    total = sum(len(c) for _, c in decks)
    progs = d["programs"]
    rows = "".join(f'<tr><td>{e(n)}</td><td>{e(S("print.cards", n=len(c)))}</td><td>{e(S("print.pages", n=-(-len(c) // 9)))}</td></tr>' for n, c in decks)
    title = d["meta"]["title"]
    cover = f"""<div class="cover">{lang_links(g, langs, "cards.html")}<h1>{e(S("print.title", game=title))}</h1>
<p>{e(S("print.intro", tagline=d["meta"]["tagline"], version=d["meta"]["version"], total=total, mats=len(progs)))}</p>
<table>{rows}<tr><td>{e(S("print.mats"))}</td><td>{e(S("print.mats_n", n=len(progs)))}</td><td>{e(S("print.pages", n=-(-len(progs) // 2)))}</td></tr></table>
<p>{S("print.printing_html")}</p>
<p>{S("print.answers_html")}</p></div>"""
    mats = [cards.program_mat(cx, p) for p in progs]
    mat_pages = "".join(f'<section class="sheet"><div class="label">{e(S("print.mats"))}</div><div class="mats">{"".join(mats[k:k + 2])}</div></section>'
                        for k in range(0, len(mats), 2))
    body = cover + "".join(sheets(g, c, n) for n, c in decks) + mat_pages
    g.print_dir.mkdir(parents=True, exist_ok=True)
    out = g.print_dir / "cards.html"
    out.write_text(page(g, f"{title}: print sheets", body), encoding="utf-8")
    (g.print_dir / "backs.html").write_text(page(g, f"{title}: card backs", sheets(g, [cards.card_back()] * 9, S("print.backs"))), encoding="utf-8")
    build_answer_booklet(g, langs)
    return out, total


def build_answer_booklet(g, langs):
    d, S = g.d, g.S
    name = lambda i: g.D[i]["name"]
    by_suit = defaultdict(list)
    for q in d["questions"]:
        by_suit[q["suit"]].append(q)
    body = (f'<div class="key">{lang_links(g, langs, "answer-key.html")}<h1>{e(S("print.key_title", game=d["meta"]["title"]))}</h1>'
            f'<p>{e(S("print.key_intro"))}</p>')
    head_row = "".join(f"<th>{e(S(k))}</th>" for k in ("print.key_card", "print.key_best", "print.key_ok", "print.key_traps", "print.key_why"))
    for st in d["meta"]["suits"]:
        body += f'<h2>{e(st["name"])}</h2><table><tr>{head_row}</tr>'
        for q in by_suit[st["id"]]:
            traps = "<br>".join(f'<span class="trap">{e(name(i))}</span>' for i in q["traps"])
            body += (f'<tr><td class="id">{q["id"]} {e(q["title"])}</td><td>{e(", ".join(name(i) for i in q["best"]))}</td>'
                     f'<td>{e(", ".join(name(i) for i in q["ok"])) or "–"}</td><td>{traps}</td>'
                     f'<td>{e(q["why"])} <i>{e(S("print.key_watch", threat=g.T[q["key_threat"]]["name"]))}</i></td></tr>')
        body += "</table>"
    body += f'<h2>{e(S("print.key_programmes"))}</h2><table><tr><th>{e(S("print.key_mat"))}</th><th>{e(S("print.key_accepted"))}</th></tr>'
    for p in d["programs"]:
        body += f'<tr><td class="id">{p["id"]} {e(p["name"])}</td><td>' + "<br>".join(
            f'{i}. {e(", ".join(name(a) for a in st["accept"]))}' for i, st in enumerate(p["stages"], 1)) + "</td></tr>"
    body += "</table></div>"
    (g.print_dir / "answer-key.html").write_text(page(g, S("print.key_title", game=d["meta"]["title"]), body), encoding="utf-8")


def dname(i):
    return D[i]["name"]


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
    L += ["## Coverage", "", "| Method | Family | Best answer to |", "|---|---|---|"]
    for d in designs:
        qs = [q["id"] for q in questions if d["id"] in q["best"]]
        L.append(f"| {d['name']} | {FAM[d['family']]['name']} | {', '.join(qs)} |")
    (ROOT / "ANSWER_KEY.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- web app
PAGES_URL = "https://ua-smartlab.github.io/methodical-card-game/app/"


def fill_template(tpl, g):
    """Replace {{key}} in the page template with this language's string (escaped, unless the key ends in _html)."""
    def sub(m):
        key = m.group(1)
        if key not in g.ui:
            raise KeyError(f"app/template.html uses unknown string key {key!r}; add it to i18n/en/ui.json")
        return g.ui[key] if key.endswith("_html") else e(g.ui[key])
    return re.sub(r"\{\{([\w.]+)\}\}", sub, tpl)


def build_app(g, langs, artifact=None):
    cx = g.activate()
    d = g.d
    tpl = fill_template((ROOT / "app" / "template.html").read_text(encoding="utf-8"), g)
    rendered = {
        "designs": {x["id"]: cards.design_card(cx, x) for x in d["designs"]},
        "questions": {q["id"]: cards.question_card(cx, q) for q in d["questions"]},
        "threats": {t["id"]: cards.threat_card(cx, t, i + 1) for i, t in enumerate(d["threats"])},
        "safeguards": {x["id"]: cards.safeguard_card(cx, x, i + 1) for i, x in enumerate(d["safeguards"])},
        "twists": {x["id"]: cards.twist_card(cx, x) for x in d["twists"]},
        "programs": {p["id"]: cards.program_mat(cx, p) for p in d["programs"]},
    }
    bundle = {**d, "cards": rendered}

    def href(x, absolute):
        if absolute:
            return PAGES_URL + ("" if x["code"] == "en" else x["code"] + "/")
        return ("" if g.code == "en" else "../") + ("" if x["code"] == "en" else x["code"] + "/")

    def js(v):
        return json.dumps(v, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    def page_for(absolute):
        lang = {"code": g.code, "dir": "rtl" if g.rtl else "ltr",
                "langs": [{"code": x["code"], "name": x["name"], "href": href(x, absolute), "current": x["code"] == g.code} for x in langs]}
        return (tpl.replace("/*__DATA__*/null", js(bundle))
                .replace("/*__CARD_CSS__*/", cards.CARD_CSS + g.lang_css())
                .replace("/*__UI__*/{}", js(g.ui))
                .replace("/*__LANG__*/{}", js(lang))
                .replace("/*__FIT__*/", cards.FIT_JS)
                .replace("<!--__EXTRA_FONTS__-->", g.extra_font_link()))
    # The template is page content only (the hosted version wraps it); the local copy gets its own skeleton.
    g.app_dir.mkdir(parents=True, exist_ok=True)
    out = g.app_dir / "index.html"
    out.write_text(f'<!doctype html>\n<html {g.html_attrs()}><head><meta charset="utf-8">'
                   '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
                   '<style>[hidden]{display:none!important}body{margin:0}</style></head><body>\n'
                   + page_for(False) + "\n</body></html>\n", encoding="utf-8")
    if artifact:
        Path(artifact).write_text(page_for(True), encoding="utf-8")
    return out


if __name__ == "__main__":
    for w in warnings:
        print("warning:", w)
    for err in errors:
        print("ERROR:", err)
    if errors:
        sys.exit(1)
    i18n.write_source(DATA_ALL)
    langs = i18n.languages()
    bad = [msg for info in langs if info["code"] != "en" for msg in i18n.problems(info["code"])]
    for msg in bad:
        print("ERROR:", msg)
    if bad:
        sys.exit(1)
    artifact = sys.argv[sys.argv.index("--artifact") + 1] if "--artifact" in sys.argv else None
    build_answer_key()
    for info in langs:
        g = Lang(info)
        _, n = build_print(g, langs)
        if (ROOT / "app" / "template.html").exists():
            build_app(g, langs, artifact if info["code"] == "en" else None)
        if info["code"] == "en":
            print(f"ok: {len(questions)} questions, {len(designs)} designs, {len(threats)} threats, "
                  f"{len(safeguards)} safeguards, {len(twists)} twists, {len(programs)} programmes ({n} printable cards)")
            print("  en: source language")
        else:
            total, done = i18n.coverage(info["code"])
            print(f"  {info['code']}: {100 * done // max(total, 1)}% translated ({done}/{total} strings)")
