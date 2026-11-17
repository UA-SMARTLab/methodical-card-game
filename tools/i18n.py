"""Translations for Methodical.

English is the source language. Card text lives in data/*.json; interface and card-label strings live in
i18n/en/ui.json under stable keys. Each other language has a folder i18n/<code>/ with:

  ui.json     the same keys as i18n/en/ui.json, translated (the "art" section translates labels drawn inside pictures)
  cards.json  card text keyed by card id, in the shape of the generated i18n/en/cards.json

Anything missing falls back to English, so a language can be added a little at a time.
To add a language: add it to i18n/languages.json, copy i18n/en/ui.json and i18n/en/cards.json into i18n/<code>/,
translate the values (never the keys or ids), and run python3 tools/build.py.
"""
import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
I18N = ROOT / "i18n"

# Which fields of each deck are text to translate. Everything else (ids, links, scores) stays as it is.
TEXT_FIELDS = {
    "questions": ["title", "field", "text", "why"],
    "designs": ["name", "short", "gist", "example"],
    "threats": ["name", "short", "text", "example"],
    "safeguards": ["name", "short", "text"],
    "twists": ["name", "text"],
    "programs": ["name", "brief"],
}


# The "Find your method" tree (data/method-tree.json) is nested, so its text is keyed by its path in the tree
# ("aims/CAUSE/options/2/label"). Only fields with these names are text; ids, links and sources stay as they are.
TREE_TEXT = {"intro", "q", "help", "label", "hint", "short", "plain", "term", "tag", "name", "what", "situation", "note", "def", "rule"}


def tree_text(tree):
    """The tree's translatable strings, {path: text}."""
    out = {}

    def walk(x, path, key):
        if isinstance(x, dict):
            for k, v in x.items():
                if not k.startswith("_") and k != "ref":
                    walk(v, path + [k], k)
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, path + [str(i)], key)
        elif isinstance(x, str) and key in TREE_TEXT:
            out["/".join(path)] = x
    walk(tree, [], None)
    return out


def apply_tree(tree, tr):
    """Lay translated strings {path: text} over the tree, in place. Paths that no longer exist are ignored."""
    for path, text in (tr or {}).items():
        *parents, last = path.split("/")
        node = tree
        for p in parents:
            node = node[int(p)] if isinstance(node, list) and p.isdigit() and int(p) < len(node) else node.get(p) if isinstance(node, dict) else None
            if node is None:
                break
        if text and isinstance(node, dict) and isinstance(node.get(last), str):
            node[last] = text


def load_json(path, default=None):
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def languages():
    return load_json(I18N / "languages.json")


def source_cards(data):
    """The English card text in the shape every cards.json uses: {deck: {id: {field: text}}}."""
    out = {"meta": {"tagline": data["meta"]["tagline"],
                    "suits": {s["id"]: {"name": s["name"], "ask": s["ask"]} for s in data["meta"]["suits"]},
                    "families": {f["id"]: {"name": f["name"]} for f in data["meta"]["families"]},
                    "constraints": {c["id"]: {"name": c["name"], "text": c["text"]} for c in data["meta"]["constraints"]}}}
    for deck, fields in TEXT_FIELDS.items():
        out[deck] = {}
        for x in data[deck]:
            entry = {f: x[f] for f in fields}
            if deck == "questions":
                entry["traps"] = dict(x["traps"])
            if deck == "programs":
                entry["stages"] = [st["ask"] for st in x["stages"]]
            out[deck][x["id"]] = entry
    if "tree" in data:
        out["tree"] = tree_text(data["tree"])
    if "classes" in data:
        out["classes"] = tree_text(data["classes"])
    return out


def write_source(data):
    """Regenerate i18n/en/cards.json from data/. It is the reference translators work from; don't edit it by hand."""
    path = I18N / "en" / "cards.json"
    path.write_text(json.dumps(source_cards(data), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def translated(data, code):
    """A deep copy of the card data with language `code` laid over it."""
    data = copy.deepcopy(data)
    if code == "en":
        return data
    tr = load_json(I18N / code / "cards.json", {})
    m = tr.get("meta", {})
    data["meta"]["tagline"] = m.get("tagline") or data["meta"]["tagline"]
    for key, items in (("suits", data["meta"]["suits"]), ("families", data["meta"]["families"]), ("constraints", data["meta"]["constraints"])):
        for x in items:
            for f, v in m.get(key, {}).get(x["id"], {}).items():
                if v:
                    x[f] = v
    for deck, fields in TEXT_FIELDS.items():
        for x in data[deck]:
            t = tr.get(deck, {}).get(x["id"], {})
            for f in fields:
                if t.get(f):
                    x[f] = t[f]
            if deck == "questions":
                for d, reason in t.get("traps", {}).items():
                    if d in x["traps"] and reason:
                        x["traps"][d] = reason
            if deck == "programs":
                for st, ask in zip(x["stages"], t.get("stages", [])):
                    if ask:
                        st["ask"] = ask
    if "tree" in data:
        apply_tree(data["tree"], tr.get("tree"))
    if "classes" in data:
        apply_tree(data["classes"], tr.get("classes"))
    return data


def ui_strings(code):
    """English strings with language `code` laid over them: {"ui": {...}, "art": {...}}."""
    base = load_json(I18N / "en" / "ui.json")
    if code == "en":
        return base
    tr = load_json(I18N / code / "ui.json", {})
    return {sec: {**base.get(sec, {}), **{k: v for k, v in tr.get(sec, {}).items() if v}} for sec in base}


def coverage(code):
    """Share of English strings that have a translation, for the build report."""
    def leaves(x):
        if isinstance(x, dict):
            for v in x.values():
                yield from leaves(v)
        elif isinstance(x, list):
            for v in x:
                yield from leaves(v)
        elif isinstance(x, str) and x:
            yield x
    src_cards = load_json(I18N / "en" / "cards.json")
    src_ui = load_json(I18N / "en" / "ui.json")
    tr_cards = load_json(I18N / code / "cards.json", {})
    tr_ui = load_json(I18N / code / "ui.json", {})

    def count(src, tr):
        total = done = 0
        if isinstance(src, dict):
            for k, v in src.items():
                t, d = count(v, (tr or {}).get(k) if isinstance(tr, dict) else None)
                total += t; done += d
        elif isinstance(src, list):
            for i, v in enumerate(src):
                t, d = count(v, tr[i] if isinstance(tr, list) and i < len(tr) else None)
                total += t; done += d
        else:
            total, done = 1, 1 if tr else 0
        return total, done
    a = count(src_cards, tr_cards)
    b = count(src_ui, tr_ui)
    return (a[0] + b[0], a[1] + b[1])


class Strings:
    """Look up an interface string by key and fill in {placeholders}: S("play.verdict_on", design=name)."""

    def __init__(self, table):
        self.table = table

    def __call__(self, key, **kw):
        s = self.table.get(key, key)
        return re.sub(r"\{(\w+)\}", lambda m: str(kw.get(m.group(1), m.group(0))), s)


CONTROL = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
PLACEHOLDER = re.compile(r"\{\w+\}")


def problems(code):
    """Mistakes a translation must not contain: control characters, and {placeholders} that differ from English."""
    out = []
    for name in ("ui.json", "cards.json"):
        src = load_json(I18N / "en" / name, {})
        tr = load_json(I18N / code / name, {})

        def walk(en, t, path):
            if isinstance(t, dict):
                for k, v in t.items():
                    yield from walk(en.get(k) if isinstance(en, dict) else None, v, f"{path}/{k}")
            elif isinstance(t, list):
                for i, v in enumerate(t):
                    yield from walk(en[i] if isinstance(en, list) and i < len(en) else None, v, f"{path}/{i}")
            elif isinstance(t, str):
                yield path, en if isinstance(en, str) else None, t
        for path, en, t in walk(src, tr, name):
            if CONTROL.search(t):
                out.append(f"{code}/{path}: contains a control character")
            if en is not None and not path.endswith("_comment") and set(PLACEHOLDER.findall(en)) != set(PLACEHOLDER.findall(t)):
                out.append(f"{code}/{path}: placeholders differ from English")
    return out
