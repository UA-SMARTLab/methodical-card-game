# Methodical: design notes

How the game is put together, why it's built this way, and what is still open.

## 1. Starting point

The game you heard about pairs **fallacy cards** with **refutation cards**, and you learn logic by matching an error to its fix.
A version for scientists keeps that matching mechanic and moves it up one level of abstraction:

| Logic game | Methodical |
|---|---|
| An argument | A **research question** in a situation |
| Spot the fallacy | Pick the **study design** that can answer it |
| Fallacy card | **Threat** card (bias, validity threat) |
| Refutation card | **Safeguard** card (design or analysis feature) |

So there are two matching layers. **Question → Design** is the main skill. **Threat → Safeguard** is the
"logic game" layer, and it gives the game its back-and-forth: one player proposes, another attacks, the first defends.

## 2. What a player should learn

In rough order of difficulty (an informal Bloom's ladder):

1. **Classify the question.** Is this asking *how much*, *why*, *whether X causes Y*, *what will happen*, or *what the evidence says*?
   Most bad designs start from a misread question, e.g. a prevalence question answered with a cohort,
   or a mapping question answered with a meta-analysis.
2. **Read the constraints.** The same causal question needs an RCT, a case-control study, a regression discontinuity
   or Mendelian randomization depending on whether you can assign the exposure, how rare the outcome is,
   whether a cutoff rule exists, and whether genes can act as instruments. *Constraints, not topics, pick the design.*
3. **Anticipate the weakness.** Every design has a characteristic way of failing (case-control → recall bias;
   retrospective cohort → immortal time; benchmark → leakage).
4. **Defend under pressure.** Know which safeguard answers which threat, and that some safeguards are impossible for
   some designs (you can't add randomization to a case-control study).
5. **Think in programmes.** Real questions need a *sequence* of designs: explore, describe, associate, test, synthesize.

Modes 1→3 climb the same ladder.

## 3. The taxonomy: the hard part

### 3.1 "Analytical vs. synthetic" means different things in different fields

The words you used are a good example of why a naive taxonomy fails for scientists:

- In **epidemiology**, *analytical* studies (cohort, case-control) test hypotheses about associations, as opposed to
  *descriptive* ones.
- In **physics, engineering and maths**, an *analytical* study derives closed-form results from first principles,
  as opposed to numerical or experimental ones.
- In **chemistry**, *analytical* means measurement (analytical chemistry), and *synthetic* means making compounds.
- In **evidence-based research**, *synthesis* means combining existing studies (systematic reviews).
- In **philosophy** (Kant), analytic vs. synthetic is about whether a statement is true by definition.

So Methodical doesn't sort designs by those words. It uses **two separate axes**:

- **Suits** classify the *question*, i.e. what kind of knowledge is wanted. There are nine:
  Describe, Explore, Associate, Cause, Predict, Measure, Explain, Build, Synthesize.
- **Families** classify the *design*, i.e. how the knowledge is produced. There are nine:
  descriptive observational, analytical observational, quasi-experimental, experimental,
  qualitative & mixed, evidence synthesis, measurement, theory & computation, design & development.

The two axes don't map one-to-one, and that's deliberate. A 🎯 Cause question can be answered from five
families (experimental, quasi-experimental, analytical observational, theory & computation, even synthesis).
The player's job is to navigate that many-to-many map.

### 3.2 Why these nine suits

They come from the familiar split of research purposes (descriptive / exploratory / explanatory / evaluative),
widened to cover research that isn't health research:

- **Predict** is separate from **Associate** and **Cause** because prediction and causation need different designs
  and different validation, and confusing them is one of the most common modern errors.
- **Measure** is separate because measurement studies (diagnostic accuracy, reliability, psychometrics,
  interlaboratory trials) are a big, under-taught part of science with their own designs.
- **Explain** covers theory: analytical derivation and simulation. Physicists and engineers spend most of their time here.
- **Build** covers design science, engineering research and feasibility work, where the output is an artifact or a plan.

### 3.3 Why constraints are the engine

Constraints are what make this a game for scientists rather than a vocabulary quiz.
Each of the 13 constraint icons stands for a classic *reason a design is chosen*:

| Constraint | Classic consequence |
|---|---|
| 🔎 Rare outcome | Sample on the outcome → case-control |
| ☢️ Rare exposure | Sample on the exposure → cohort |
| ⚡ Brief trigger | Self-matched → case-crossover |
| 🚫 Can't assign | No RCT → natural experiments, instruments, target trial emulation |
| ✂️ Cutoff rule | Regression discontinuity |
| 1️⃣ One unit | N-of-1, synthetic control, case study |
| 👥 Group-level | Cluster randomization, difference-in-differences |
| 📅 Rollout | Stepped wedge |
| 🗂️ Many studies | Synthesis instead of yet another primary study |
| 💸 Tight budget | Rapid review, pilot, retrospective designs |
| ❓ Uncharted | Qualitative, grounded theory, scoping review |

**Twist** cards add constraints mid-round, which trains the most useful habit of all: re-deciding when the situation changes.

## 4. The answer key: three tiers, not one right answer

Scientists will (rightly) argue with any single "correct" answer. So every question has:

- 🥇 **Best**: what most methodologists would choose given the constraints.
- 🥈 **Defensible**: reasonable, with a known cost.
- ⚠️ **Traps**: designs that *look* plausible but fail for a specific, teachable reason, which is printed.
- **Unlisted**: everything else, open to **appeal**.

The trap reasons do as much teaching as the right answers. Writing a good trap means finding the design a smart
novice would actually pick (e.g. a classic case-control design for a diagnostic-accuracy question → spectrum bias).

The appeal mechanic keeps the key honest and gives experts something to do: a well-argued appeal is worth points,
and the best ones should be fed back into the deck.

## 5. Balance and coverage

- 60 questions over 9 suits. 🎯 Cause has 17 because causal inference has the most designs. The other suits have 5–6 each.
- Fields include medicine, public health, ecology, astronomy, economics, education, engineering, robotics, materials,
  chemistry, physics, HCI and anthropology, so that the deck is not secretly a medical-school exam.
- The build script **checks** that every one of the 46 designs is the best answer to at least one question,
  that every threat appears on at least one design, and that every design weakness has at least one usable safeguard.
  Mode 2 can't deal a threat that has no possible counter.
- Difficulty ★ to ★★★: ★ is a first-year methods course; ★★★ (target trials, Mendelian randomization,
  instrumental variables, realist review, incremental predictive value) is postdoc level.

## 6. Card data and tooling

All content lives in `data/*.json`, one file per deck. The cards, the answer key and the web app are generated from it,
so fixing a typo is a one-line change followed by `python3 tools/build.py`.

Rules the validator enforces (see `tools/build.py`):
- all ids referenced across files exist; no design sits in two tiers of the same question;
- every design is the best answer somewhere; every safeguard counters something;
- every `weak_vs` threat has a safeguard that is usable with that design's family;
- text-length warnings so that cards don't overflow (the print layout is also checked for overflow in a headless browser).

## 7. Open questions and next steps

1. **Playtest Mode 2's economy.** Is +1/−1 for review too small compared with +3 for the design? Possibly
   make rebuttals worth +2 at expert tables.
2. **Expert review per field.** The key was checked by a second methodological read, but each field
   (ecology, econometrics, metrology…) deserves a domain expert's pass.
3. **More fields.** Social sciences beyond economics, the earth sciences and software engineering could each add ~10 questions.
4. **Reverse cards.** "Here is an abstract. What design is this, and what's wrong with it?" would train the reader's skill
   as well as the designer's.
5. **Reporting-guideline layer.** Each design could carry its reporting guideline (CONSORT, STROBE, PRISMA, STARD, TRIPOD,
   SRQR…) as a collectible bonus.
6. **Art and print.** v0.2 uses hand-built vector art (see section 9). A print-on-demand run would fit a standard two-deck box.
   Painted art could later replace the illustrations on Question cards, but the Design diagrams should stay diagrams.
7. **Name.** "Methodical" is a working title. Alternatives: *Fit for Purpose*, *Design Space*, *Reviewer 2*, *Study Hall*.

## 8. Trading-card format (v0.2)

Version 0.1 printed paragraphs on cards. They were accurate but read like flashcards. v0.2 follows trading-card conventions,
so the cards feel like a game and the table can read them at a glance:

- **One picture, one sentence.** Each card has an illustration and a single sentence of effect text. The long explanations,
  examples and citations moved to the app and the answer-key booklet.
- **The picture is the content.** On Design cards the art is the study's own diagram: arms splitting after a die, arrows pointing
  backwards from cases, a jump at a cutoff, a staircase of clusters switching over. Players learn the shape of each design.
  Question art shows the *subject* of the problem, never the design, so it can't give the answer away.
- **Trading-card colour language.** Design cards take their family's colour (like monster types). Threats are crimson
  (like trap cards), Safeguards emerald (like spell cards), Twists violet.
- **Icons instead of words** for suits and constraints, decoded by the four reference cards.
- **Uniform backs, answers in a booklet.** In v0.1 the answers were printed on the backs of the question cards, so the top card
  of a face-down deck showed its own answer. v0.2 gives every card the same back.

## 9. Key sources the design leans on

- Shadish, Cook & Campbell (2002), *Experimental and Quasi-Experimental Designs*: validity typology, threats.
- Hernán & Robins (2020), *Causal Inference: What If*: target trials, DAGs, immortal time.
- Rothman, Greenland & Lash, *Modern Epidemiology*: observational designs and biases.
- Creswell & Plano Clark, *Designing and Conducting Mixed Methods Research*.
- Higgins et al., *Cochrane Handbook*; Tricco et al. (2018) PRISMA-ScR; Pawson (2006) on realist synthesis.
- Hevner et al. (2004) on design science in information systems; Montgomery, *Design and Analysis of Experiments*.
- The EQUATOR reporting guidelines (CONSORT, STROBE, STARD, TRIPOD, PRISMA).
