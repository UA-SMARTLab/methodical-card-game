# Methodical: answer key

Generated from `data/` by `tools/build.py`. Don't edit by hand.

Scoring: 🥇 best +3 · 🥈 defensible +1 · ⚠️ trap −2 · unlisted 0 (or +1 on a successful appeal).

## 📊 Describe: What is it? How much, how often, where, and is it changing?

### Q01 · City vape count (Public health, ★)

> The city council wants to know what share of adults vape right now, by age group, before it votes on a ban next quarter.

Constraints: 💸 Tight budget

- 🥇 **Best:** Cross-sectional survey
- 🥈 **Defensible:** Monitoring / surveillance
- ⚠️ **Trap, Prospective cohort:** Follows people for years to measure new cases. The council needs current prevalence next quarter.
- ⚠️ **Trap, Case–control study:** Sampling people by whether they vape destroys any estimate of how common vaping is.

'What share, right now?' is a prevalence question, answered by one well-sampled snapshot. Put the effort into the sampling frame and weighting, not into follow-up.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q02 · Tattoo rash (Dermatology, ★)

> Five patients at one clinic developed an unusual rash weeks after getting tattoos with the same new ink. Nothing like it has been published.

Constraints: 1️⃣ One unit, 🔎 Rare outcome, ❓ Uncharted

- 🥇 **Best:** Case report / case series
- 🥈 **Defensible:** none
- ⚠️ **Trap, Randomized controlled trial:** Deliberately exposing people to a suspected harm is unethical, and premature.
- ⚠️ **Trap, Systematic review & meta-analysis:** There is nothing yet to synthesize.

A careful case series is the fastest way to raise a signal that others can test. Its job is to describe and alert. A case-control study is the logical next step, not the first.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q03 · Vanishing butterflies (Ecology, ★)

> Is a migratory butterfly population declining over the decade, and is the decline steady or sudden?

Constraints: none

- 🥇 **Best:** Monitoring / surveillance
- 🥈 **Defensible:** none
- ⚠️ **Trap, Cross-sectional survey:** One snapshot can't show a trend.
- ⚠️ **Trap, Field experiment:** Nothing is being manipulated. The question is what is happening, not why.

Trends need standardized counts repeated over many years, the backbone of conservation science. Changes in observers, sites or methods over time are the main enemy.

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

### Q04 · Jupiter census (Astronomy, ★★)

> What fraction of nearby Sun-like stars host a Jupiter-mass planet?

Constraints: none

- 🥇 **Best:** Cross-sectional survey
- 🥈 **Defensible:** Monitoring / surveillance
- ⚠️ **Trap, Case report / case series:** One spectacular planetary system tells you nothing about the fraction.
- ⚠️ **Trap, Analytical / mathematical theory:** Formation theory can suggest a number, but this asks for an observed frequency.

It's a prevalence question in disguise: a defined sample of stars observed with a known detection completeness. Correcting for what the instrument can't see is the whole game.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q05 · After approval (Pharmacology, ★★)

> A new diabetes drug was approved after trials in 3,000 people. How often does it cause serious liver injury now that millions use it?

Constraints: 🔎 Rare outcome, 🗄️ Existing data

- 🥇 **Best:** Monitoring / surveillance
- 🥈 **Defensible:** Retrospective cohort
- ⚠️ **Trap, Randomized controlled trial:** Seeing a 1-in-50,000 harm would need an impossibly large trial. That is exactly why the approval trials missed it.
- ⚠️ **Trap, Cross-sectional survey:** Liver injury is an event over time, not a state at one moment.

Post-marketing pharmacovigilance (spontaneous reports plus active monitoring of health records) exists because rare harms are invisible in trials. Signals are then confirmed with analytical studies.

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

### Q65 · Newts in the pond (Ecology, ★)

> How many great crested newts live in a large, murky pond? You can net some on every visit, but never all of them.

Constraints: 💸 Tight budget

- 🥇 **Best:** Capture–recapture
- 🥈 **Defensible:** none
- ⚠️ **Trap, Cross-sectional survey:** One netting counts the newts you caught, not the ones you missed.
- ⚠️ **Trap, Monitoring / surveillance:** Repeated counts track a trend in catches, not how many newts there really are.

Photograph each newt's unique belly pattern, then net again: the share of already-seen newts in the second catch estimates the total (Lincoln–Petersen). It assumes no newts arrive or leave between visits and that every newt is equally likely to be caught.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

## 🧭 Explore: What is going on here? How and why do people experience or do it?

### Q55 · The ignored app (Nursing, ★)

> Night-shift nurses rarely use a new hand-hygiene reminder app, while day-shift nurses do. Nobody knows why.

Constraints: ❓ Uncharted

- 🥇 **Best:** Interviews & thematic analysis
- 🥈 **Defensible:** Ethnography, Mixed methods (sequential)
- ⚠️ **Trap, Cross-sectional survey:** A survey needs answer options, and you don't know the reasons yet.
- ⚠️ **Trap, Randomized controlled trial:** There's no intervention to test until you understand the problem.

When you don't know the variables, ask and listen. Sample night and day nurses purposively and interview them until new themes stop emerging.

*Watch out for:* **Thin data**, countered by Theoretical sampling to saturation, Triangulation.

### Q56 · Waste pickers (Urban anthropology, ★)

> How do informal waste pickers in a megacity organize their daily work, routes and trade?

Constraints: ❓ Uncharted

- 🥇 **Best:** Ethnography
- 🥈 **Defensible:** Case study (in-depth), Interviews & thematic analysis
- ⚠️ **Trap, Cross-sectional survey:** Official surveys rarely reach informal workers, and they miss tacit practices.
- ⚠️ **Trap, Prediction model (statistical / ML):** There's nothing to predict yet, and no data to train on.

Practices people don't put into words are best seen by being there: months of participant observation, field notes, trust. Reflect on how your presence changes what you see.

*Watch out for:* **Researcher bias**, countered by Reflexivity & double coding, Blinding, Triangulation.

### Q57 · The turnaround (Operations management, ★)

> One factory cut its defect rate by 80% in a year while its sister plants didn't. What happened, and what can others learn?

Constraints: 1️⃣ One unit

- 🥇 **Best:** Case study (in-depth)
- 🥈 **Defensible:** Interviews & thematic analysis, Mixed methods (sequential)
- ⚠️ **Trap, Randomized controlled trial:** The change already happened, in one factory.
- ⚠️ **Trap, Cross-sectional survey:** A survey of many plants can't reconstruct what happened in this one.

Study one bounded case in depth, using documents, data, interviews and observation. Compare it with a sister plant that didn't improve; otherwise you are only studying the survivor.

*Watch out for:* **Survivorship bias**, countered by Representative sampling, Time-zero alignment.

### Q58 · Back to work (Health sociology, ★★)

> There is no theory of how people with long COVID decide when (and whether) to return to work.

Constraints: ❓ Uncharted

- 🥇 **Best:** Grounded theory
- 🥈 **Defensible:** Interviews & thematic analysis
- ⚠️ **Trap, Prospective cohort:** It tells you how many return, not how they decide.
- ⚠️ **Trap, Systematic review & meta-analysis:** There's too little to synthesize, and the goal is new theory.

'No theory yet' is the signature of grounded theory: iterative interviewing and coding, and theoretical sampling of new cases to test emerging concepts, until a model of the decision process emerges.

*Watch out for:* **Thin data**, countered by Theoretical sampling to saturation, Triangulation.

### Q59 · What should we measure? (Clinical trials, ★★)

> Trials of therapies for a rare disease all use different endpoints, so none can be compared. Patients and experts disagree on which outcomes matter most.

Constraints: ❓ Uncharted

- 🥇 **Best:** Delphi consensus
- 🥈 **Defensible:** Interviews & thematic analysis, Systematic review & meta-analysis
- ⚠️ **Trap, Randomized controlled trial:** Another trial would just add another endpoint to the pile.

A Delphi process with patients, clinicians and researchers rates candidate outcomes over several anonymous rounds. It's the standard route to a 'core outcome set', usually preceded by a review of the outcomes in use and by patient interviews.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q60 · The rural gap (Digital health, ★★)

> A national survey shows rural clinics adopt telemedicine at half the urban rate. Policymakers ask why.

Constraints: 🗄️ Existing data

- 🥇 **Best:** Mixed methods (sequential)
- 🥈 **Defensible:** Interviews & thematic analysis, Case study (in-depth)
- ⚠️ **Trap, Cross-sectional survey:** You already have the 'what'. Another survey won't give the 'why'.
- ⚠️ **Trap, Randomized controlled trial:** There's nothing to randomize until you know the barriers.

An explanatory sequential design: use the survey to pick contrasting clinics (high and low adopters), interview staff to explain the numbers, then integrate the two strands.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

## 🔗 Associate: Do X and Y go together, and does X come first?

### Q06 · Smog atlas (Environmental health, ★)

> Before investing in a big study, you want a quick, cheap first look: do countries with more air pollution have higher asthma rates?

Constraints: 👥 Group-level, 🗄️ Existing data, 💸 Tight budget

- 🥇 **Best:** Ecological study
- 🥈 **Defensible:** Cross-sectional survey
- ⚠️ **Trap, Prospective cohort:** Years and millions spent on what should be a cheap first look.
- ⚠️ **Trap, Randomized controlled trial:** You can't assign air pollution.

Comparing aggregate data across countries is the cheapest hypothesis generator there is. Just never conclude that polluted individuals get asthma from it: that's the ecological fallacy.

*Watch out for:* **Ecological fallacy**, countered by Multilevel analysis.

### Q07 · Rare cancer, common spray (Paediatric oncology, ★)

> Is a rare childhood cancer (about 1 in 50,000 children) associated with the mother's use of a common pesticide during pregnancy?

Constraints: 🔎 Rare outcome, 🚫 Can't assign

- 🥇 **Best:** Case–control study
- 🥈 **Defensible:** Retrospective cohort
- ⚠️ **Trap, Prospective cohort:** You'd need to follow millions of pregnancies to collect a handful of cases.
- ⚠️ **Trap, Cross-sectional survey:** It can't establish that the exposure came before the cancer.

Rare outcome: start from the cases. Draw controls from the population that produced them, and take exposure from records rather than memory, because grieving parents remember differently. A record-linkage cohort works only if registries already capture the pesticide exposure.

*Watch out for:* **Recall bias**, countered by Validated, objective measures, Blinding.

### Q08 · Clean-room workers (Occupational health, ★★)

> A few hundred workers handle a novel solvent at a single chip factory. Is the exposure linked to later kidney disease?

Constraints: ☢️ Rare exposure, 🗄️ Existing data

- 🥇 **Best:** Retrospective cohort
- 🥈 **Defensible:** Prospective cohort
- ⚠️ **Trap, Case–control study:** The exposure is so rare that almost none of the kidney-disease cases in the population will have had it.
- ⚠️ **Trap, Ecological study:** One factory gives no groups to compare.

Rare exposure: sample on the exposure. Employment records let you assemble the exposed workforce and an unexposed comparison group (e.g. office staff) and trace their outcomes. Comparing with the general public invites the healthy-worker effect.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q09 · Snow shovel (Cardiology, ★★)

> Does a bout of heavy physical exertion trigger a heart attack within the following hour?

Constraints: ⚡ Brief trigger, 🔎 Rare outcome

- 🥇 **Best:** Case-crossover
- 🥈 **Defensible:** Case–control study
- ⚠️ **Trap, Cross-sectional survey:** It can't capture the hour before an event.
- ⚠️ **Trap, Prospective cohort:** You'd need hour-by-hour exertion logs from huge numbers of people to catch a few events.

Brief exposure, acute effect: compare each patient's exertion in the hour before their heart attack with their own usual exertion. Every stable personal confounder cancels out.

*Watch out for:* **Recall bias**, countered by Validated, objective measures, Blinding.

### Q10 · Diet and dementia (Neurology, ★)

> Is a high intake of ultra-processed food in midlife associated with dementia 20 years later?

Constraints: ⏳ Long latency, 🚫 Can't assign

- 🥇 **Best:** Prospective cohort
- 🥈 **Defensible:** Retrospective cohort
- ⚠️ **Trap, Randomized controlled trial:** Nobody sticks to an assigned diet for 20 years.
- ⚠️ **Trap, Case–control study:** People with dementia can't reliably report their diet from two decades ago.

Measure diet before anyone has dementia and wait, or (faster) analyse an existing cohort that recorded diet decades ago. Watch for reverse causation: early, pre-clinical dementia changes eating habits.

*Watch out for:* **Reverse causation**, countered by Lag & early-event exclusion, Randomization.

### Q66 · Migraine genes (Genetics, ★★)

> Which genetic variants are linked to migraine? A biobank holds genotypes and health records for half a million people, but nobody knows which genes to look at.

Constraints: 🗄️ Existing data, ❓ Uncharted

- 🥇 **Best:** Genome-wide association study
- 🥈 **Defensible:** Case–control study
- ⚠️ **Trap, Mendelian randomization:** Mendelian randomization uses variants you already know to test a cause. Here you are looking for the variants in the first place.
- ⚠️ **Trap, Case report / case series:** One family with migraine can hint at a gene, but it can't scan the genome across a population.

Test every variant across the genome against a threshold of about 5 × 10⁻⁸, so that millions of tests don't produce false hits. Adjust for ancestry so population structure doesn't fake associations, and replicate the hits in an independent cohort.

*Watch out for:* **Forking paths & p-hacking**, countered by Preregistration, Multiplicity correction, Independent replication.

### Q67 · The freezer (Cardiology, ★★)

> A biobank froze blood from 60,000 people 15 years ago; 900 have since had a heart attack. Does a new inflammation marker predict who? Each test costs €300.

Constraints: 🗄️ Existing data, 🔎 Rare outcome, 💸 Tight budget

- 🥇 **Best:** Case-cohort / nested case–control
- 🥈 **Defensible:** Case–control study
- ⚠️ **Trap, Prospective cohort:** Starting a new cohort means waiting 15 years for what is already in the freezer.
- ⚠️ **Trap, Retrospective cohort:** Testing all 60,000 samples would cost €18 million. You only need the cases and a sample of everyone else.

Test all 900 cases plus a random subcohort drawn from the whole cohort, blind to who is a case and in random order, so lab batches can't line up with the outcome. The same subcohort can later be reused for other outcomes.

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

## 🎯 Cause: Does changing X change Y? Does the intervention work?

### Q11 · New pill vs. old (Cardiology, ★)

> Does a new blood-pressure drug prevent more strokes than the current standard drug?

Constraints: none

- 🥇 **Best:** Randomized controlled trial
- 🥈 **Defensible:** Adaptive / platform trial
- ⚠️ **Trap, Retrospective cohort:** Doctors give new drugs to particular kinds of patients. Confounding by indication makes the comparison unreliable.
- ⚠️ **Trap, Case report / case series:** Anecdotes can't estimate a comparative effect.

A clean causal question about an intervention you can assign, with genuine uncertainty about which is better: randomize. Conceal allocation, blind if you can, analyse by intention to treat.

*Watch out for:* **Attrition & missing data**, countered by Intention-to-treat, Sensitivity analysis.

### Q12 · Peer tutoring (Education, ★)

> Does a new peer-tutoring method raise maths scores? Pupils in the same class share notes and talk constantly.

Constraints: 👥 Group-level

- 🥇 **Best:** Cluster randomized trial
- 🥈 **Defensible:** Stepped-wedge trial
- ⚠️ **Trap, Randomized controlled trial:** Randomizing pupils within classes lets the method leak to the controls, diluting the effect.

When an intervention spreads between individuals, randomize the group (class or school) instead. Then analyse at the right level, because pupils in the same class aren't independent.

*Watch out for:* **Unit-of-analysis error**, countered by Multilevel analysis.

### Q13 · Soda tax (Public health, ★★)

> One state introduced a sugary-drinks tax; its similar neighbour didn't. Supermarket sales data exist for both, three years before and after. Did the tax cut consumption?

Constraints: 🚫 Can't assign, 👥 Group-level, 🗄️ Existing data

- 🥇 **Best:** Difference-in-differences
- 🥈 **Defensible:** Synthetic control, Interrupted time series
- ⚠️ **Trap, Cross-sectional survey:** Comparing the two states once, after the tax, can't separate the tax from differences that were already there.

Compare the change in the taxed state with the change in the untaxed one. The key assumption, parallel trends, can be checked in the years before the tax.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

### Q14 · Scholarship cutoff (Education policy, ★★)

> Students scoring 70 or more on a national exam receive a scholarship. Does the scholarship make them more likely to graduate from university?

Constraints: ✂️ Cutoff rule, 🗄️ Existing data, 🚫 Can't assign

- 🥇 **Best:** Regression discontinuity
- 🥈 **Defensible:** none
- ⚠️ **Trap, Retrospective cohort:** Comparing all recipients with all non-recipients compares stronger students with weaker ones.
- ⚠️ **Trap, Cross-sectional survey:** A one-off comparison of graduates and non-graduates can't separate the scholarship from ability.

A student who scored 70 and one who scored 69 are nearly identical, except one got the money. The estimate is local to the cutoff. Check that nobody could nudge their score across it.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q15 · Sepsis alert (Health services, ★)

> A hospital switched on an electronic sepsis alert on a known date. Monthly sepsis deaths are available for five years before and two years after. Did the alert help?

Constraints: 🗄️ Existing data, 1️⃣ One unit

- 🥇 **Best:** Interrupted time series
- 🥈 **Defensible:** Difference-in-differences
- ⚠️ **Trap, Cross-sectional survey:** A snapshot can't see a change.
- ⚠️ **Trap, Case report / case series:** One dramatic rescue proves nothing about the death rate.

Many time points before and after a sharp date separate the alert's effect from the trend that was already under way. Add a control series (another hospital, or a condition the alert can't affect) to rule out coincident changes.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

### Q16 · Reunification (Economics, ★★)

> What did German reunification in 1990 do to West Germany's GDP per capita?

Constraints: 1️⃣ One unit, 🚫 Can't assign, 🗄️ Existing data

- 🥇 **Best:** Synthetic control
- 🥈 **Defensible:** Interrupted time series
- ⚠️ **Trap, Randomized controlled trial:** Countries can't be randomized to reunify.
- ⚠️ **Trap, Cross-sectional survey:** A one-year comparison with other countries ignores differences that existed before 1990.

One treated unit, many possible comparisons: build a weighted blend of other OECD countries that tracked West Germany before 1990, then watch where the paths split. Abadie, Diamond & Hainmueller did exactly this.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

### Q17 · Her migraine (Neurology, ★★)

> A patient has migraines several times a week. Does a new as-needed migraine drug relieve her attacks better than her usual painkiller?

Constraints: 1️⃣ One unit

- 🥇 **Best:** N-of-1 trial
- 🥈 **Defensible:** Crossover trial
- ⚠️ **Trap, Randomized controlled trial:** A trial's average effect doesn't tell you whether this one patient responds.
- ⚠️ **Trap, Case report / case series:** An uncontrolled before-and-after story is fooled by regression to the mean: she sought help at her worst.

Frequent attacks and a fast-acting drug: randomize which drug she takes for each attack (or block of attacks), blind it with identical capsules, and repeat. The answer is about her.

*Watch out for:* **Expectation effects**, countered by Blinding, Placebo or sham control, Reflexivity & double coding, Triangulation.

### Q18 · Two inhalers (Pharmacology, ★★)

> Do two inhaler formulations produce the same improvement in lung function in people with stable asthma?

Constraints: 💸 Tight budget

- 🥇 **Best:** Crossover trial
- 🥈 **Defensible:** Randomized controlled trial
- ⚠️ **Trap, Retrospective cohort:** Patients end up on one inhaler or the other for reasons tied to how severe their asthma is.

Stable chronic condition, short-acting reversible effect: each person tries both in random order with a washout. Between-person noise vanishes, so far fewer participants are needed.

*Watch out for:* **Carryover**, countered by Washout period.

### Q19 · Three knobs (Agriculture, ★★)

> Which combination of fertilizer dose, irrigation schedule and seed variety gives the best yield on real farms?

Constraints: none

- 🥇 **Best:** Field experiment, Factorial experiment (DoE)
- 🥈 **Defensible:** none
- ⚠️ **Trap, Cross-sectional survey:** Farmers who irrigate more also differ in soil, skill and wealth.
- ⚠️ **Trap, Case study (in-depth):** One farm can't separate three factors and their interactions.

Cross the three factors in a factorial layout, randomized to plots in blocks across several farms. One season yields main effects and interactions. This is Fisher's original idea.

*Watch out for:* **Limited generalizability**, countered by Multi-site, diverse sample, Representative sampling, Independent replication.

### Q20 · Weld strength (Manufacturing, ★)

> Which of six process parameters (current, speed, gas flow…) drive weld strength in the lab, and do any of them interact?

Constraints: 💸 Tight budget

- 🥇 **Best:** Factorial experiment (DoE)
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Retrospective cohort:** Past production logs confound settings that operators always changed together.
- ⚠️ **Trap, Case report / case series:** One great weld proves nothing.

A fractional-factorial screening design tests six factors in a few dozen runs and reveals interactions that one-factor-at-a-time testing misses. Randomize the run order to protect against drift. Simulation helps only if a validated process model exists.

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

### Q21 · Checkout button (Tech, ★)

> Will a redesigned checkout button increase completed purchases on a site with 2 million visitors a day?

Constraints: 💸 Tight budget

- 🥇 **Best:** Online A/B test
- 🥈 **Defensible:** Randomized controlled trial
- ⚠️ **Trap, Interrupted time series:** Even a long time series can't separate the redesign from concurrent campaigns, when randomizing visitors costs nothing.
- ⚠️ **Trap, Interviews & thematic analysis:** Users can't reliably predict their own clicking behaviour.

Randomize visitors to the old or new button and compare conversion. Fix the sample size and the metric in advance: peeking until it's significant is the classic A/B-test sin.

*Watch out for:* **Forking paths & p-hacking**, countered by Preregistration, Multiplicity correction, Independent replication.

### Q22 · Rat-free islands (Conservation, ★★)

> Does eradicating invasive rats increase seabird nesting success? There are 20 similar islands, and you have permits for 10 eradications.

Constraints: 👥 Group-level

- 🥇 **Best:** Field experiment
- 🥈 **Defensible:** Difference-in-differences
- ⚠️ **Trap, Cross-sectional survey:** Islands that never had rats differ from rat islands in many other ways.
- ⚠️ **Trap, Case report / case series:** One island's success story can't be separated from that year's weather.

Randomly choose which 10 islands get eradication and measure all 20 before and after (a randomized BACI design). Random allocation stops you from picking the 'easy' islands. Twenty units is few, so plan the power.

*Watch out for:* **Low power**, countered by Sample-size planning, Independent replication.

### Q23 · Triage rollout (Health systems, ★★)

> The ministry has decided that a new emergency triage protocol will be introduced in all 12 regional hospitals over the next year. Does it reduce deaths?

Constraints: 📅 Rollout, 👥 Group-level

- 🥇 **Best:** Stepped-wedge trial
- 🥈 **Defensible:** Cluster randomized trial, Interrupted time series
- ⚠️ **Trap, Randomized controlled trial:** Triage is a hospital-wide process. You can't randomize individual patients within a hospital.

Everyone gets it; only the order is open. Randomize the order in which hospitals switch, and every hospital contributes both control and intervention time. Model the background time trend carefully.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

### Q24 · Ten candidates (Infectious disease, ★★)

> A new respiratory virus is spreading fast and ten repurposed drugs have been proposed. Which of them, if any, reduce deaths in hospitalized patients? You have months.

Constraints: none

- 🥇 **Best:** Adaptive / platform trial
- 🥈 **Defensible:** Randomized controlled trial
- ⚠️ **Trap, Case report / case series:** Early case series claiming miracle cures were widespread and misleading.
- ⚠️ **Trap, Retrospective cohort:** Sicker patients get experimental drugs. Confounding by indication.

One master protocol, one shared control arm; arms are dropped for futility and new ones added. RECOVERY found that dexamethasone saves lives within about 100 days of launch.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

### Q25 · Older than the trials (Pharmacoepidemiology, ★★★)

> Do two classes of diabetes drug differ in their effect on kidney failure in adults over 80, a group excluded from the trials? Insurance claims cover 5 million people.

Constraints: 🗄️ Existing data

- 🥇 **Best:** Target trial emulation
- 🥈 **Defensible:** Retrospective cohort
- ⚠️ **Trap, Cross-sectional survey:** It can't capture who started which drug, and when.
- ⚠️ **Trap, Case report / case series:** There's no comparison.

Write the protocol of the trial you'd like to run (eligibility, treatment strategies, time zero, follow-up) and emulate it in the claims data with new users and an active comparator. This designs out immortal-time and prevalent-user bias; what remains is confounding by indication.

*Watch out for:* **Confounding by indication**, countered by Randomization, Active comparator, new users, Matching / propensity scores, Sensitivity analysis, Negative controls.

### Q26 · Does school pay? (Economics, ★★★)

> Does an extra year of schooling raise later earnings? Compulsory-schooling laws let people born early in the year leave school with slightly less education.

Constraints: 🚫 Can't assign, 🗄️ Existing data

- 🥇 **Best:** Instrumental variable analysis
- 🥈 **Defensible:** Regression discontinuity
- ⚠️ **Trap, Cross-sectional survey:** Ability and family background drive both schooling and earnings.

Quarter of birth nudges schooling but (arguably) affects earnings only through schooling, which makes it an instrument. Interrogate that 'only through' assumption hard, and check the instrument isn't weak.

*Watch out for:* **Confounding**, countered by Randomization, Causal diagram (DAG), Matching / propensity scores, Negative controls, Self or sibling comparison, Sensitivity analysis.

### Q27 · LDL: cause or marker? (Cardiology, ★★★)

> Is lifelong higher LDL cholesterol a cause of coronary heart disease, or merely a marker of other risk factors?

Constraints: 🚫 Can't assign, ⏳ Long latency, 🗄️ Existing data

- 🥇 **Best:** Mendelian randomization
- 🥈 **Defensible:** Randomized controlled trial
- ⚠️ **Trap, Cross-sectional survey:** It can't separate cause from marker, or tell which came first.
- ⚠️ **Trap, Ecological study:** Country-level cholesterol averages say nothing about mechanisms in individuals.

People inherit LDL-raising or LDL-lowering variants at conception, essentially at random: a natural lifelong trial. Large genetic consortia make it fast. Pleiotropy (genes acting through other paths) is the threat to check. Trials of LDL-lowering drugs answer a shorter-term version.

*Watch out for:* **Confounding**, countered by Randomization, Causal diagram (DAG), Matching / propensity scores, Negative controls, Self or sibling comparison, Sensitivity analysis.

## 🔮 Predict: What will happen, and to whom?

### Q28 · Who crashes next? (Critical care, ★★)

> Using vital signs and lab values from the electronic record, can we flag ICU patients likely to deteriorate in the next six hours?

Constraints: 🗄️ Existing data

- 🥇 **Best:** Prediction model (statistical / ML)
- 🥈 **Defensible:** Benchmark evaluation
- ⚠️ **Trap, Case–control study:** Artificially balancing cases and controls distorts the predicted risks (calibration).
- ⚠️ **Trap, Randomized controlled trial:** Trials test interventions. First you need a model; an RCT of using it comes later.

Develop on one period, then validate on a later period and at another hospital. Guard ruthlessly against leakage, e.g. a lab test that was ordered because the doctor already suspected deterioration.

*Watch out for:* **Overfitting & leakage**, countered by External validation, Preregistration.

### Q29 · Spring flood (Hydrology, ★)

> How much water will flow into a reservoir next spring, given this winter's snowpack and 40 years of records?

Constraints: 🗄️ Existing data

- 🥇 **Best:** Prediction model (statistical / ML)
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Field experiment:** You can't manipulate the snowpack.
- ⚠️ **Trap, Case study (in-depth):** One past flood year can't forecast the next one.

Decades of snowpack and inflow records support a statistical forecast; a physically based hydrological simulation is a strong alternative or complement. Judge either one by its skill on years it never saw.

*Watch out for:* **Overfitting & leakage**, countered by External validation, Preregistration.

### Q30 · Next superconductor (Materials science, ★★)

> Which of 100,000 hypothetical compounds are most likely to superconduct at high temperature, so the lab can synthesize the top 20?

Constraints: 🗄️ Existing data, 💸 Tight budget

- 🥇 **Best:** Prediction model (statistical / ML)
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Factorial experiment (DoE):** Synthesizing 100,000 compounds isn't a plan.
- ⚠️ **Trap, Systematic review & meta-analysis:** The compounds are hypothetical. There's no literature on them yet.

Train a model on known materials to rank the candidates, optionally refine the shortlist with first-principles simulation, then test the top hits. Report performance on genuinely new chemistries, not near-duplicates of the training set.

*Watch out for:* **Overfitting & leakage**, countered by External validation, Preregistration.

### Q31 · Biomarker add-on (Cardiology, ★★★)

> Does adding a new blood biomarker to an established heart-attack risk score actually improve prediction?

Constraints: 🗄️ Existing data

- 🥇 **Best:** Prediction model (statistical / ML)
- 🥈 **Defensible:** Prospective cohort
- ⚠️ **Trap, Case–control study:** Showing that cases have higher levels proves association, not added predictive value.
- ⚠️ **Trap, Randomized controlled trial:** No intervention is being tested.

Association isn't prediction. Compare the model with and without the biomarker on discrimination, calibration and net benefit, in data the model hasn't seen.

*Watch out for:* **Overfitting & leakage**, countered by External validation, Preregistration.

### Q32 · Range in 2070 (Ecology, ★★)

> Where will a mountain plant species be able to live in 2070 under different climate scenarios?

Constraints: 🚫 Can't assign

- 🥇 **Best:** Prediction model (statistical / ML)
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Case study (in-depth):** One population's story can't map a future range.
- ⚠️ **Trap, Randomized controlled trial:** You can't randomize climates.

Species distribution models link today's occurrences to climate, then project them onto scenarios. Mechanistic (physiological) simulations are a valuable cross-check when the future climate falls outside anything in the training data.

*Watch out for:* **Limited generalizability**, countered by Multi-site, diverse sample, Representative sampling, Independent replication.

### Q69 · Worth the price? (Health economics, ★★)

> Trials show a new RSV vaccine protects older adults. Is it worth what the manufacturer is asking the national health service to pay?

Constraints: 🗄️ Existing data

- 🥇 **Best:** Cost-effectiveness analysis
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Randomized controlled trial:** The trials already show that it works. Another trial won't tell you whether it's worth the money.
- ⚠️ **Trap, Systematic review & meta-analysis:** Pooling the efficacy evidence is one input, but it doesn't weigh the costs.

Build a decision model of who catches RSV, who is admitted to hospital and who dies, with and without vaccination. Feed it trial efficacy, costs and quality of life, and report the extra cost per QALY gained, with a probabilistic sensitivity analysis to show how certain that answer is.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

## 📏 Measure: Can we measure it accurately, reliably, and validly?

### Q33 · Rapid strep (Paediatrics, ★)

> How accurate is a new 5-minute strep test compared with throat culture, in children who come to clinics with a sore throat?

Constraints: none

- 🥇 **Best:** Diagnostic accuracy study
- 🥈 **Defensible:** none
- ⚠️ **Trap, Case–control study:** Testing obvious culture-proven cases against healthy volunteers inflates accuracy (spectrum bias).
- ⚠️ **Trap, Randomized controlled trial:** An RCT asks whether using the test improves outcomes. That's a different, later question.

Recruit consecutive children with sore throats, do both tests on everyone, and read each test blind to the other. Sensitivity and specificity only mean something in the population where the test will be used.

*Watch out for:* **Spectrum bias**, countered by Representative sampling.

### Q34 · Burnout scale (Occupational psychology, ★★)

> No good questionnaire exists for 'research burnout' among academics. Build one that others can trust.

Constraints: ❓ Uncharted

- 🥇 **Best:** Instrument development & validation
- 🥈 **Defensible:** Mixed methods (sequential)
- ⚠️ **Trap, Cross-sectional survey:** A big survey with an untested questionnaire measures… something.
- ⚠️ **Trap, Systematic review & meta-analysis:** Reviewing studies can't validate a tool that doesn't exist yet.

Generate items from theory and interviews, refine them with experts and cognitive testing, then test factor structure, reliability and validity in fresh samples. An exploratory sequential mixed-methods design is essentially this.

*Watch out for:* **Wrong construct**, countered by Validated, objective measures, Triangulation.

### Q35 · Two readers (Radiology, ★)

> Do two radiologists give the same osteoarthritis grade when they read the same knee X-rays?

Constraints: none

- 🥇 **Best:** Reliability & agreement study
- 🥈 **Defensible:** none
- ⚠️ **Trap, Diagnostic accuracy study:** Accuracy needs a reference standard. The question is agreement between readers.
- ⚠️ **Trap, Cross-sectional survey:** Grades from different patients read by different radiologists can't measure agreement.

Both read the same representative set of images, independently and blind to each other; quantify agreement with weighted kappa. The images must span the full range of severity.

*Watch out for:* **Spectrum bias**, countered by Representative sampling.

### Q36 · Wrist vs. cuff (Biomedical engineering, ★★)

> Can a cheap wrist-worn sensor replace the hospital's validated blood-pressure monitor?

Constraints: none

- 🥇 **Best:** Reliability & agreement study
- 🥈 **Defensible:** Diagnostic accuracy study
- ⚠️ **Trap, Ecological study:** Comparing average readings across clinics hides how far the two devices disagree in each person.
- ⚠️ **Trap, Randomized controlled trial:** No one needs to be randomized. The question is whether two instruments agree.

This is a method-comparison study: measure the same people with both devices and compute Bland–Altman limits of agreement. Decide in advance what difference is clinically acceptable, and don't trust correlation: one device could read 15 mmHg high every time and still correlate perfectly. Include people across the whole blood-pressure range.

*Watch out for:* **Spectrum bias**, countered by Representative sampling.

### Q37 · Lead in the water (Analytical chemistry, ★)

> Fifteen labs measure lead in drinking water using the same standard method. Do they get the same answer from the same sample?

Constraints: none

- 🥇 **Best:** Interlaboratory comparison
- 🥈 **Defensible:** Reliability & agreement study
- ⚠️ **Trap, Systematic review & meta-analysis:** Published results come from different samples and can't isolate lab-to-lab variation.
- ⚠️ **Trap, Monitoring / surveillance:** Monitoring tap water over time tells you about the water, not about the labs.

Send identical, homogeneous samples (ideally with a certified reference value) to every lab, and quantify repeatability and reproducibility (ISO 5725).

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

### Q64 · Grit or not? (Educational psychology, ★★)

> A popular 'grit' scale predicts which students finish their degrees. Critics say it's just conscientiousness under a new name. Does it measure something distinct?

Constraints: none

- 🥇 **Best:** Nomological network study
- 🥈 **Defensible:** Instrument development & validation
- ⚠️ **Trap, Prospective cohort:** Showing that grit predicts graduation proves nothing new: conscientiousness predicts it too.
- ⚠️ **Trap, Reliability & agreement study:** A highly reliable scale can reliably measure the wrong thing.

Write down the predicted pattern before collecting data: grit should correlate with conscientiousness, but not so highly that they are the same thing, and it should predict outcomes beyond it. Measure both traits by more than one method (self-report, teacher ratings, behaviour), so shared questionnaire habits don't fake the overlap.

*Watch out for:* **Measurement error**, countered by Validated, objective measures, Blinding, Triangulation.

### Q68 · Seeds of choice (Agricultural economics, ★★)

> Would smallholder farmers pay for drought-tolerant maize seed? And what matters most to them: yield, price, taste, or seed they can save for next year?

Constraints: 💸 Tight budget

- 🥇 **Best:** Discrete choice experiment
- 🥈 **Defensible:** Mixed methods (sequential)
- ⚠️ **Trap, Cross-sectional survey:** Asking farmers to rate each feature from 1 to 5 makes everything important and hides the trade-offs.
- ⚠️ **Trap, Randomized controlled trial:** Handing out seed at random tests whether it raises yields, not what farmers value or would pay.

Offer choices between seed packages whose yield, price, taste and saveability vary by an experimental design; choice models turn the answers into the weight of each feature and a willingness to pay. Pick the attributes with farmers first, and remember that stated choices overstate real purchases.

*Watch out for:* **Limited generalizability**, countered by Multi-site, diverse sample, Representative sampling, Independent replication.

## 🧮 Explain: What mechanism or law must hold? What follows from the theory?

### Q38 · Engine limit (Physics, ★)

> What is the maximum possible efficiency of ANY heat engine operating between a hot and a cold reservoir?

Constraints: none

- 🥇 **Best:** Analytical / mathematical theory
- 🥈 **Defensible:** none
- ⚠️ **Trap, Factorial experiment (DoE):** Testing engines shows what has been achieved, never what is impossible for every engine.
- ⚠️ **Trap, Computational simulation:** It simulates particular engines. A universal bound needs a derivation.

'Any engine' is a universal claim, and only a derivation from the laws of thermodynamics can establish it. Carnot's bound came from reasoning, not measurement.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q39 · Bridge in a storm (Civil engineering, ★)

> How will a long, slender bridge deck respond to wind speeds you can't safely test on the real structure?

Constraints: 🚫 Can't assign

- 🥇 **Best:** Computational simulation
- 🥈 **Defensible:** Factorial experiment (DoE)
- ⚠️ **Trap, Case report / case series:** Tacoma Narrows teaches a lot, but one collapse isn't a design check.
- ⚠️ **Trap, Cross-sectional survey:** Surveying other bridges doesn't tell you how this one will respond.

Coupled fluid–structure simulation lets you push the virtual bridge to failure. Validate the model against wind-tunnel tests of scale models (the 'ok' answer) before trusting the extreme cases.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q40 · School closures (Epidemiology, ★★)

> How might closing schools change the peak of a flu pandemic in a city of two million?

Constraints: 🚫 Can't assign, 💸 Tight budget

- 🥇 **Best:** Computational simulation
- 🥈 **Defensible:** Interrupted time series
- ⚠️ **Trap, Randomized controlled trial:** Randomizing closures in the middle of a pandemic is rarely feasible, and far too slow.
- ⚠️ **Trap, Cross-sectional survey:** A snapshot can't show the dynamics of an epidemic.

An agent-based model with households, schools and workplaces lets you play out scenarios. Present results as ranges under varied assumptions, and check them against data from past epidemics.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q41 · Clock in a cell (Systems biology, ★★★)

> A three-gene loop in a bacterium seems to oscillate. Is the negative-feedback loop alone enough to cause oscillations, and under what parameter conditions?

Constraints: none

- 🥇 **Best:** Analytical / mathematical theory
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Cross-sectional survey:** Snapshots of gene expression can't establish sufficiency of a mechanism.
- ⚠️ **Trap, Case–control study:** There are no cases and controls in this question.

Write the dynamics as differential equations and analyse their stability; the conditions for oscillation fall out of the mathematics. Simulation explores the parameter space, and the lab then builds and tests the circuit.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q42 · Neutron-star crash (Astrophysics, ★★)

> What gravitational-wave signal should detectors expect when two neutron stars merge?

Constraints: 🚫 Can't assign

- 🥇 **Best:** Computational simulation
- 🥈 **Defensible:** Analytical / mathematical theory
- ⚠️ **Trap, Case report / case series:** One observed merger (GW170817) can't supply templates across all masses and spins.
- ⚠️ **Trap, Factorial experiment (DoE):** Neutron stars can't be collided in a lab.

The equations are known but have no closed-form solution in this regime, so numerical-relativity simulations produce the waveform templates that detectors search for. Approximate analytical models cover the early inspiral.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q43 · Price war (Economics, ★★)

> Two firms compete by setting prices. Under what conditions will they settle at a stable equilibrium instead of an endless price war?

Constraints: none

- 🥇 **Best:** Analytical / mathematical theory
- 🥈 **Defensible:** Computational simulation
- ⚠️ **Trap, Case study (in-depth):** One price war's story doesn't establish general conditions.
- ⚠️ **Trap, Online A/B test:** Testing prices on customers doesn't reveal the strategic logic between firms.

Game theory derives equilibria, and the conditions for them, from stated assumptions. The answer is only as good as those assumptions: state them explicitly and test how robust the result is.

*Watch out for:* **Unvalidated model**, countered by Verification & validation, Sensitivity analysis.

### Q70 · Why this deal? (Political science, ★★★)

> Colombia's 2016 peace agreement led most FARC fighters to disarm, where earlier talks had failed. Three rival explanations are on the table. Which one holds?

Constraints: 1️⃣ One unit, 🗄️ Existing data

- 🥇 **Best:** Process tracing
- 🥈 **Defensible:** Case study (in-depth)
- ⚠️ **Trap, Ecological study:** Cross-country correlations about peace deals can't test which mechanism worked in Colombia.
- ⚠️ **Trap, Cross-sectional survey:** A survey of today's opinions can't reconstruct the sequence of decisions that led to the deal.

Write down what each explanation predicts you should find (who met when, what was offered, what the leadership said in private), then look for hoop tests that can eliminate an explanation and smoking guns that strongly confirm one. Weigh evidence against your favourite account as hard as evidence for it.

*Watch out for:* **Researcher bias**, countered by Reflexivity & double coding, Blinding, Triangulation.

## 🛠️ Build: Can we make something that works, and is the plan feasible?

### Q44 · Grasp benchmark (Robotics, ★)

> Your lab has a new robot-grasping algorithm. Is it actually better than the state of the art?

Constraints: 🗄️ Existing data, 💸 Tight budget

- 🥇 **Best:** Benchmark evaluation
- 🥈 **Defensible:** Factorial experiment (DoE)
- ⚠️ **Trap, Case report / case series:** A cherry-picked demo video isn't evidence.
- ⚠️ **Trap, Interviews & thematic analysis:** Opinions about the algorithm don't measure grasp success.

Same objects, same robot, same metrics and published baselines, plus ablations and repeated trials with confidence intervals. Report the failures, and test beyond the benchmark: sim-to-real gaps are where claims die.

*Watch out for:* **Forking paths & p-hacking**, countered by Preregistration, Multiplicity correction, Independent replication.

### Q45 · A hand for kids (Rehabilitation engineering, ★)

> Design a low-cost prosthetic hand for children that clinicians and families will actually adopt.

Constraints: ❓ Uncharted

- 🥇 **Best:** Design science (build & evaluate)
- 🥈 **Defensible:** Mixed methods (sequential), Pilot / feasibility study
- ⚠️ **Trap, Randomized controlled trial:** There's nothing to test yet.
- ⚠️ **Trap, Systematic review & meta-analysis:** Useful background, but it won't build the hand.

Iterate: understand the needs, prototype, test with users, refine. Evaluation is built into every cycle, and later the finished device can face a trial.

*Watch out for:* **Researcher bias**, countered by Reflexivity & double coding, Blinding, Triangulation.

### Q46 · Review workbench (Research software, ★)

> Build a tool that guides researchers through a scoping review, and show that it actually helps them.

Constraints: ❓ Uncharted

- 🥇 **Best:** Design science (build & evaluate)
- 🥈 **Defensible:** Mixed methods (sequential), Pilot / feasibility study
- ⚠️ **Trap, Randomized controlled trial:** A large trial of a tool that doesn't exist yet is premature.
- ⚠️ **Trap, Case report / case series:** One happy user isn't an evaluation.

Build in short cycles with real researchers, and evaluate each version on real tasks: usability, time taken, and completeness of the resulting review. You are not a neutral judge of your own tool, so let others test it.

*Watch out for:* **Researcher bias**, countered by Reflexivity & double coding, Blinding, Triangulation.

### Q47 · Will they come? (Geriatrics, ★)

> Before a costly multi-site trial: can you recruit frail 85-year-olds into a home-exercise programme, keep them in it for 6 months, and measure falls reliably?

Constraints: 💸 Tight budget

- 🥇 **Best:** Pilot / feasibility study
- 🥈 **Defensible:** none
- ⚠️ **Trap, Randomized controlled trial:** Launching the full trial blind risks a very expensive failure to recruit.
- ⚠️ **Trap, Systematic review & meta-analysis:** Other trials' recruitment rates help, but they won't tell you about your setting.

A feasibility study measures recruitment, retention, adherence and data quality against pre-set progression criteria. Resist reporting its effect estimates: it isn't powered for them.

*Watch out for:* **Low power**, countered by Sample-size planning, Independent replication.

### Q48 · Therapy over a bad line (Global health, ★)

> Can an app-based talking therapy be delivered in rural clinics with unreliable internet? Will staff use it, and will patients finish it?

Constraints: 💸 Tight budget, ❓ Uncharted

- 🥇 **Best:** Pilot / feasibility study
- 🥈 **Defensible:** Design science (build & evaluate), Mixed methods (sequential)
- ⚠️ **Trap, Randomized controlled trial:** Testing effectiveness before you know it can be delivered wastes the trial.
- ⚠️ **Trap, Ecological study:** Country-level internet statistics say nothing about your clinics.

Feasibility first: run it in a few clinics, measure uptake, completion and technical failures, and interview staff and patients about what got in the way.

*Watch out for:* **Limited generalizability**, countered by Multi-site, diverse sample, Representative sampling, Independent replication.

### Q61 · The tangle clip (Medical devices, ★)

> A nurse has invented a clip that stops IV lines from tangling. Before the hospital pays for prototypes and a patent filing: is it actually new?

Constraints: 🗄️ Existing data, 💸 Tight budget

- 🥇 **Best:** Prior art review
- 🥈 **Defensible:** Scoping review
- ⚠️ **Trap, Design science (build & evaluate):** Building and testing first risks a year spent reinventing, or infringing, someone else's patent.
- ⚠️ **Trap, Systematic review & meta-analysis:** There's no effect to pool, and most prior art for a gadget like this sits in patents and product catalogues, not journals.

Novelty is judged against everything made public anywhere, in any language: patents, products, catalogues, theses and papers. Search patent databases by classification code as well as by keyword, because patents rarely use everyday words like 'clip'.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q72 · The abandoned form (Human–computer interaction, ★)

> Older patients keep abandoning a hospital's online booking form halfway through. The redesign is frozen in a week.

Constraints: 💸 Tight budget

- 🥇 **Best:** Usability test (think-aloud)
- 🥈 **Defensible:** Design science (build & evaluate), Interviews & thematic analysis
- ⚠️ **Trap, Online A/B test:** An A/B test tells you which version wins, not where and why people get stuck, and there is no new version yet.
- ⚠️ **Trap, Cross-sectional survey:** A satisfaction survey misses exactly the people who gave up.

Ask five or so representative older users to book an appointment while thinking aloud; watch without helping and log every hesitation and error. Fix the worst problems and test again: several small rounds find more than one big one.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q73 · No-shows (Primary care, ★)

> A quarter of a clinic's appointments are missed. The team wants to start text reminders this month, then adjust the wording and timing until the rate falls.

Constraints: 💸 Tight budget, 1️⃣ One unit

- 🥇 **Best:** Plan–Do–Study–Act cycles
- 🥈 **Defensible:** Interrupted time series
- ⚠️ **Trap, Cluster randomized trial:** One clinic can't be a cluster trial, and the team wants to learn and adapt month by month.
- ⚠️ **Trap, Systematic review & meta-analysis:** Reviews say reminders help on average. The question is what works in this clinic.

Run small cycles: plan a change, try it for a week or two, study the run chart, act on what you learn. Mark every change on the chart, and keep measuring long enough to tell real improvement from seasonal swings.

*Watch out for:* **History & secular trends**, countered by Concurrent control group, Pre-trend check & control series, Run charts & control limits.

## 📚 Synthesize: What does all the existing evidence say?

### Q49 · Run it again? (Psychiatry, ★)

> Forty randomized trials of exercise for depression report conflicting results. What is the overall effect?

Constraints: 🗂️ Many studies

- 🥇 **Best:** Systematic review & meta-analysis
- 🥈 **Defensible:** none
- ⚠️ **Trap, Randomized controlled trial:** A 41st trial adds one more data point to a pile nobody has weighed.
- ⚠️ **Trap, Case study (in-depth):** Examining one trial in depth can't settle a conflict among forty.

Search exhaustively, appraise risk of bias, pool with a random-effects model and explore why the trials disagree. Look for missing small negative trials.

*Watch out for:* **Publication bias**, countered by Comprehensive search, Preregistration.

### Q50 · Plastic in the soil (Environmental science, ★)

> What has been studied about microplastics in farm soils (which methods, which regions, which outcomes), and where are the gaps?

Constraints: 🗂️ Many studies, ❓ Uncharted

- 🥇 **Best:** Scoping review
- 🥈 **Defensible:** none
- ⚠️ **Trap, Field experiment:** One more experiment doesn't map a field of research.
- ⚠️ **Trap, Network meta-analysis:** There's no set of competing treatments to rank.

This is a mapping question: chart the literature systematically (PRISMA-ScR) without pooling effects. The output is a map of evidence and gaps that tells everyone what to study next.

*Watch out for:* **Publication bias**, countered by Comprehensive search, Preregistration.

### Q51 · Six pills, few duels (Psychiatry, ★★)

> Six antidepressants exist, but few trials compare them head to head; most compare each with placebo. Which works best?

Constraints: 🗂️ Many studies

- 🥇 **Best:** Network meta-analysis
- 🥈 **Defensible:** Systematic review & meta-analysis
- ⚠️ **Trap, Randomized controlled trial:** A six-arm head-to-head trial would be enormous, and the indirect evidence already exists.
- ⚠️ **Trap, Retrospective cohort:** Prescribing patterns are confounded by indication.

Combine direct and indirect comparisons in one network to rank the treatments. Check that the trials are similar enough for indirect comparisons to be fair (transitivity).

*Watch out for:* **Apples & oranges**, countered by Pre-planned heterogeneity analysis, Sensitivity analysis.

### Q52 · Three weeks (Health policy, ★★)

> A ministry must decide on a school-ventilation policy in three weeks, and asks what the evidence says.

Constraints: 💸 Tight budget, 🗂️ Many studies

- 🥇 **Best:** Rapid review
- 🥈 **Defensible:** Umbrella review
- ⚠️ **Trap, Systematic review & meta-analysis:** A full systematic review typically takes a year or more. The decision will be made without it.
- ⚠️ **Trap, Cluster randomized trial:** A school trial would report long after the deadline.

Streamline a systematic review transparently: a narrower question, fewer databases, single screening with verification. Report what you cut, so readers can judge.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q53 · Vitamin D for everything (Nutrition, ★★)

> Dozens of systematic reviews link vitamin D to outcomes from fractures to cancer to depression. What's the overall picture, and how credible is each claim?

Constraints: 🗂️ Many studies

- 🥇 **Best:** Umbrella review
- 🥈 **Defensible:** none
- ⚠️ **Trap, Randomized controlled trial:** One trial can't test dozens of outcomes at once.
- ⚠️ **Trap, Case report / case series:** Individual stories can't grade a body of evidence.

Review the reviews: grade each claimed association by its size and credibility, and watch for overlapping primary studies being counted twice.

*Watch out for:* **Apples & oranges**, countered by Pre-planned heterogeneity analysis, Sensitivity analysis.

### Q54 · Works here, fails there (Global health, ★★★)

> Community health-worker programmes succeed brilliantly in some countries and fail in others. Why, for whom, and in what contexts?

Constraints: 🗂️ Many studies

- 🥇 **Best:** Realist review
- 🥈 **Defensible:** Systematic review & meta-analysis, Mixed methods (sequential)
- ⚠️ **Trap, Randomized controlled trial:** One more trial in one more context won't explain the variation.
- ⚠️ **Trap, Ecological study:** Country-level correlations can't reveal the mechanisms.

Realist synthesis asks how context triggers mechanisms that produce outcomes, drawing on trials, process evaluations and qualitative studies alike.

*Watch out for:* **Apples & oranges**, countered by Pre-planned heterogeneity analysis, Sensitivity analysis.

### Q62 · Roots of a field (Sustainability science, ★★)

> Research on 'ecosystem services' has grown for thirty years across ecology and economics. Which classic works form its foundations, and which schools of thought do they fall into?

Constraints: 🗂️ Many studies, 🗄️ Existing data

- 🥇 **Best:** Co-citation analysis
- 🥈 **Defensible:** Bibliographic coupling
- ⚠️ **Trap, Systematic review & meta-analysis:** There's no single effect to pool. The question is how the field is structured.
- ⚠️ **Trap, Delphi consensus:** Experts tend to nominate the classics of their own school. The citation record shows what the whole field builds on.

Two works are linked each time a later paper cites both, so clusters of co-cited works are the field's schools of thought, and the works that bridge clusters show where ecology and economics meet. Normalize for how often each work is cited, and remember that a citation isn't an endorsement.

*Watch out for:* **Wrong construct**, countered by Validated, objective measures, Triangulation.

### Q63 · Paper flood (Science of science, ★★)

> Thousands of papers on AI for drug discovery appeared in the last two years. What are the active research fronts right now, and how do they group?

Constraints: 🗂️ Many studies, 🗄️ Existing data, 💸 Tight budget

- 🥇 **Best:** Bibliographic coupling
- 🥈 **Defensible:** Scoping review
- ⚠️ **Trap, Co-citation analysis:** Papers this new have barely been cited, so almost nothing links them yet. Co-citation would map their foundations, not today's fronts.
- ⚠️ **Trap, Systematic review & meta-analysis:** There's no focused question or effect to pool, and thousands of papers is far beyond manual appraisal.

Papers that cite the same sources are probably working on the same problem, and that link exists the day a paper is published. Down-weight references that nearly everyone cites (here, the classic deep-learning papers), or they glue every paper into one blob. Then name each cluster by reading its core papers.

*Watch out for:* **Wrong construct**, countered by Validated, objective measures, Triangulation.

### Q71 · Under fifty (Oncology, ★★★)

> Twelve trials of a breast-cancer drug show an overall benefit. Do women under 50 benefit too? Most papers don't report results by age, or use different age cut-offs.

Constraints: 🗂️ Many studies

- 🥇 **Best:** Individual participant data meta-analysis
- 🥈 **Defensible:** Systematic review & meta-analysis
- ⚠️ **Trap, Network meta-analysis:** There is one treatment against control. Nothing needs ranking.
- ⚠️ **Trap, Retrospective cohort:** Who gets the drug in routine care is confounded by indication.

Ask every trial team for its patient-level data, check it, and analyse age the same way in every trial: ideally as a continuous variable, with the treatment-by-age interaction estimated within each trial. Report which trials couldn't share data and whether their results differ.

*Watch out for:* **Selection bias**, countered by Representative sampling, Allocation concealment, Causal diagram (DAG), Comprehensive search, Intention-to-treat, Time-zero alignment.

### Q74 · The blogs know more (Software engineering, ★★)

> Teams keep asking when automating their software tests pays off. Practitioners have written hundreds of blog posts, talks and white papers about it, but only a handful of peer-reviewed studies exist. What is known?

Constraints: 📰 Practice-led

- 🥇 **Best:** Multivocal literature review
- 🥈 **Defensible:** Scoping review, Delphi consensus
- ⚠️ **Trap, Systematic review & meta-analysis:** Restricted to peer-reviewed studies, you'd throw away most of what is actually known, and there's no effect to pool.
- ⚠️ **Trap, Randomized controlled trial:** One more experiment adds a single data point; the question is what the field already knows.

When practice runs ahead of research, a multivocal review follows Garousi et al. (2019): search academic databases and the grey literature (Google, practitioner sites, conference talks), grade each grey source for authority, method and objectivity, stop by saturation, and report the white and grey evidence side by side.

*Watch out for:* **Unvetted sources**, countered by Grey-literature appraisal, Triangulation.

## Research programmes (cooperative mode)

### P1 · Screens & teen mental health

Is social media harming adolescents' mental health? Parents, platforms and governments want an answer.

1. 🧭 How do teenagers themselves describe their social-media use and its effects? → **Interviews & thematic analysis, Ethnography, Grounded theory**
2. 📊 How common are heavy use and depressive symptoms, and do they co-occur? → **Cross-sectional survey**
3. 🔗 Does heavy use come before rising symptoms, or the other way round? → **Prospective cohort, Retrospective cohort**
4. 🎯 Does cutting use for four weeks improve mood? → **Randomized controlled trial, Cluster randomized trial**
5. 📚 What do all the trials and cohorts add up to? → **Systematic review & meta-analysis**

### P2 · Microplastics in our bodies

Microplastics turn up in blood, placentas and arteries. Are they a health problem?

1. 📚 What has been studied so far, with which methods, and where are the gaps? → **Scoping review**
2. 📏 Do different labs measuring the same tissue sample find the same particle counts? → **Interlaboratory comparison, Reliability & agreement study**
3. 📊 How much do people carry, and does it vary by region and age? → **Cross-sectional survey, Monitoring / surveillance**
4. 🔗 Do people with more microplastics in arterial plaque have more heart attacks later? → **Prospective cohort, Retrospective cohort**
5. 🧮 Through what cellular mechanism could particles cause inflammation, and at what dose? → **Factorial experiment (DoE), Computational simulation, Analytical / mathematical theory**

### P3 · A soft gripper for fruit picking

Growers can't find seasonal workers. Can a soft robotic gripper pick strawberries without bruising them?

1. 📚 What gripper designs exist, and how have they been evaluated? → **Scoping review, Systematic review & meta-analysis, Prior art review**
2. 🛠️ Design a gripper that growers and pickers find usable. → **Design science (build & evaluate)**
3. 🎯 Which combination of finger material, pressure and approach speed minimizes bruising? → **Factorial experiment (DoE)**
4. 🛠️ Does it beat existing grippers on a shared set of fruits and metrics? → **Benchmark evaluation**
5. 🛠️ Can it run a full shift in a real greenhouse? Will staff keep using it? → **Pilot / feasibility study, Field experiment, Mixed methods (sequential)**

### P4 · The four-day week

A government wants to know if a 32-hour week at full pay is good for workers and firms.

1. 🧭 How did the first companies that tried it make it work, or fail? → **Case study (in-depth), Interviews & thematic analysis**
2. 🛠️ Can firms be recruited, and can productivity and well-being be measured consistently? → **Pilot / feasibility study**
3. 🎯 Sixty firms volunteered and all will switch eventually. Does it affect burnout and output? → **Stepped-wedge trial, Cluster randomized trial**
4. 🎯 A whole country adopted it by law in one year. What happened to national productivity? → **Synthetic control, Interrupted time series, Difference-in-differences**
5. 📚 Why does it work in some sectors and not in others? → **Realist review**

### P5 · A new post-viral syndrome

Months after a new infection, some people report exhaustion and brain fog. What is it, and what helps?

1. 📊 What do the first patients look like? → **Case report / case series**
2. 📊 How common is it among people who were infected? → **Cross-sectional survey, Prospective cohort**
3. 🔗 Who is at risk? Does vaccination before infection change the odds? → **Retrospective cohort, Prospective cohort, Target trial emulation**
4. 🎯 Twelve candidate treatments are proposed. Which work? → **Adaptive / platform trial, Randomized controlled trial**
5. 📚 Ranking the treatments when few were compared head-to-head. → **Network meta-analysis**

### P6 · AI triage in the emergency department

A hospital group wants an AI tool that flags patients who will need intensive care.

1. 🔮 Can routine data predict ICU admission within 24 hours? → **Prediction model (statistical / ML)**
2. 🔮 Does it still work at another hospital, a year later? → **Prediction model (statistical / ML), Benchmark evaluation**
3. 📏 Do nurses agree with each other, and with the tool, on the triage level? → **Reliability & agreement study**
4. 🎯 The tool will be switched on in all 8 hospitals this year. Does it save lives? → **Stepped-wedge trial, Cluster randomized trial, Interrupted time series**
5. 🧭 Why do some clinicians override it so often? → **Interviews & thematic analysis, Ethnography, Mixed methods (sequential)**

## Coverage

| Design | Family | Best answer to |
|---|---|---|
| Case report / case series | Descriptive observational | Q02 |
| Cross-sectional survey | Descriptive observational | Q01, Q04 |
| Ecological study | Descriptive observational | Q06 |
| Monitoring / surveillance | Descriptive observational | Q03, Q05 |
| Capture–recapture | Descriptive observational | Q65 |
| Prospective cohort | Analytical observational | Q10 |
| Retrospective cohort | Analytical observational | Q08 |
| Case–control study | Analytical observational | Q07 |
| Case-crossover | Analytical observational | Q09 |
| Target trial emulation | Analytical observational | Q25 |
| Instrumental variable analysis | Analytical observational | Q26 |
| Mendelian randomization | Analytical observational | Q27 |
| Genome-wide association study | Analytical observational | Q66 |
| Case-cohort / nested case–control | Analytical observational | Q67 |
| Difference-in-differences | Quasi-experimental | Q13 |
| Regression discontinuity | Quasi-experimental | Q14 |
| Interrupted time series | Quasi-experimental | Q15 |
| Synthetic control | Quasi-experimental | Q16 |
| Randomized controlled trial | Experimental | Q11 |
| Cluster randomized trial | Experimental | Q12 |
| Crossover trial | Experimental | Q18 |
| Factorial experiment (DoE) | Experimental | Q19, Q20 |
| N-of-1 trial | Experimental | Q17 |
| Stepped-wedge trial | Experimental | Q23 |
| Online A/B test | Experimental | Q21 |
| Adaptive / platform trial | Experimental | Q24 |
| Field experiment | Experimental | Q19, Q22 |
| Ethnography | Qualitative & mixed | Q56 |
| Grounded theory | Qualitative & mixed | Q58 |
| Interviews & thematic analysis | Qualitative & mixed | Q55 |
| Case study (in-depth) | Qualitative & mixed | Q57 |
| Process tracing | Qualitative & mixed | Q70 |
| Delphi consensus | Qualitative & mixed | Q59 |
| Mixed methods (sequential) | Qualitative & mixed | Q60 |
| Systematic review & meta-analysis | Evidence synthesis | Q49 |
| Scoping review | Evidence synthesis | Q50 |
| Network meta-analysis | Evidence synthesis | Q51 |
| Individual participant data meta-analysis | Evidence synthesis | Q71 |
| Umbrella review | Evidence synthesis | Q53 |
| Rapid review | Evidence synthesis | Q52 |
| Realist review | Evidence synthesis | Q54 |
| Prior art review | Evidence synthesis | Q61 |
| Co-citation analysis | Evidence synthesis | Q62 |
| Bibliographic coupling | Evidence synthesis | Q63 |
| Multivocal literature review | Evidence synthesis | Q74 |
| Diagnostic accuracy study | Measurement | Q33 |
| Reliability & agreement study | Measurement | Q35, Q36 |
| Instrument development & validation | Measurement | Q34 |
| Nomological network study | Measurement | Q64 |
| Discrete choice experiment | Measurement | Q68 |
| Interlaboratory comparison | Measurement | Q37 |
| Analytical / mathematical theory | Theory & computation | Q38, Q41, Q43 |
| Computational simulation | Theory & computation | Q39, Q40, Q42 |
| Prediction model (statistical / ML) | Theory & computation | Q28, Q29, Q30, Q31, Q32 |
| Cost-effectiveness analysis | Theory & computation | Q69 |
| Design science (build & evaluate) | Design & development | Q45, Q46 |
| Pilot / feasibility study | Design & development | Q47, Q48 |
| Usability test (think-aloud) | Design & development | Q72 |
| Plan–Do–Study–Act cycles | Design & development | Q73 |
| Benchmark evaluation | Design & development | Q44 |
