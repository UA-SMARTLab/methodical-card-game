# Methodical

**A card game for scientists that teaches research design.** Read a research problem, pick the study design that can
actually answer it, then defend that design when a reviewer attacks it with a bias.

![A Question card, the matching Design card, its typical Threat, the Safeguard that counters it, and a Twist](print/preview.png)

*One full chain:* a 🔗 **Associate** question with a rare outcome → **case–control study** (best) → its typical threat, **recall bias** →
countered by **validated, objective measures**, until a **Twist** changes the situation.

The cards are laid out like a trading-card game: name bar, attribute, level pips, one illustration, a type line and one sentence of effect text.
On the 60 Design cards the illustration is the study's own diagram, so the picture teaches the method. In the app, the **?** on every Design, Threat and Safeguard card opens the paper that defines it or made it standard.

## What's in the box

| Deck | Cards | Role |
|---|---:|---|
| Question | 74 | Research problems from medicine, ecology, astronomy, economics, engineering, robotics, chemistry, education… each with its own illustration |
| Design | 60 | Study types in 9 colour-coded families, from case reports and capture–recapture to genome-wide association, process tracing and design science, each with a key reference |
| Threat | 29 | Biases and validity threats (the "fallacy" deck); the app adds a real historical example for each |
| Safeguard | 34 | Design and analysis features that counter specific threats (the "refutation" deck) |
| Twist | 17 | Mid-round changes: "The ethics board says no", "Funding cut", "Thirty studies just dropped" |
| Research Programme | 6 | Five-stage cooperative challenges on A6 mats, e.g. *Screens & teen mental health*, *A soft gripper for fruit picking* |
| Answer key | booklet | Three-tier answers and reasoning for every question and programme |
| Reference | 4 | Suits, constraints, families, scoring |

## Start here

- **Play online:** **[ua-smartlab.github.io/methodical-card-game/app](https://ua-smartlab.github.io/methodical-card-game/app/)**. Nothing to install.
- **Play offline:** open [`app/index.html`](app/index.html) in any browser.
  Its **Duel** mode (switched off for now: set `duel: true` in `FEATURES` in `app/template.html` to bring it back) pits you against a computer opponent (Student, Postdoc or Reviewer 2): both of you are dealt hands of Design and tactics cards,
  play designs face down onto four open questions, challenge each other's designs by naming a weakness and rebut by naming a Safeguard, and draft one of four
  face-up designs after every round. Highest score after 8 rounds wins.
  Or double-click the launcher for your system, which opens it in your default browser:

  | System | Launcher | Notes |
  |---|---|---|
  | Windows | [`play-windows.bat`](play-windows.bat) | Double-click in File Explorer. |
  | Mac | [`play-mac.command`](play-mac.command) | Double-click in Finder. If macOS blocks it, right-click it and choose **Open**. |
  | Ubuntu | [`play-ubuntu.sh`](play-ubuntu.sh) | In Files, right-click it and choose **Run as a Program**, or run `./play-ubuntu.sh`. |

  If a launcher won't run because its executable bit was lost (for example when it was unzipped), run `sh play-mac.command` or `sh play-ubuntu.sh`.
- **Print a prototype:** open [`print/cards.html`](print/cards.html) in Chrome and print at 100% on A4 with background graphics on, then cut. That gives 218 poker-size cards and 6 programme mats.
  All cards share one back ([`print/backs.html`](print/backs.html)); opaque card sleeves are the easiest alternative. The answers are in [`print/answer-key.html`](print/answer-key.html).
- **Rules:** [`RULES.md`](RULES.md) has four modes: *Methods Map* (classroom), *Peer Review* (competitive), *Research Programme* (cooperative) and *Reviewer 2* (drill).
- **Why it's built this way:** [`DESIGN.md`](DESIGN.md) covers the taxonomy, the learning goals, the answer-key philosophy and open questions.
- **Answer key:** [`ANSWER_KEY.md`](ANSWER_KEY.md) lists every question with its tiers and rationale.

## How it works in one paragraph

Every question has a **suit**, the kind of knowledge wanted (Describe, Explore, Associate, Cause, Predict, Measure,
Explain, Build, Synthesize), and **constraint** icons such as *can't assign*, *rare outcome*, *cutoff rule*, *one unit*
or *many studies*. Every design card says which suits it serves and which constraints it fits or struggles with.
Constraints, not topics, decide between otherwise good designs, and learning to see that is the point of the game.
Answers are scored **best +3 / defensible +1 / trap −2**, and an unlisted answer can be **appealed** to the table,
because methodologists disagree.

## Editing the cards

All content lives in [`data/`](data) as JSON, one file per deck. After editing, run:

```sh
python3 tools/build.py
```

The script (standard library only) validates every cross-reference and regenerates the print sheets, the answer key
and the app. Card layout lives in `tools/cards.py`; the art is hand-built SVG in `tools/art*.py` (`art.py` holds the drawing kit
and the design diagrams). The build also checks that every design is the best answer somewhere, that every design weakness has a usable
safeguard, and that each question's key threat is one its best design is actually weak to.

## Status

Prototype v0.2: complete content in trading-card format, fully illustrated, printable, playable solo. The answer key has had one independent methodological
review pass, and its corrections are applied. Next steps are in [`DESIGN.md` §7](DESIGN.md#7-open-questions-and-next-steps),
starting with playtesting the Peer Review scoring and expert review per field.
