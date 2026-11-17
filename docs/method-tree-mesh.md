# The 60 Methods in MeSH 2026

What this is: each Method of Methodical (`data/designs.json`) matched to the NLM Medical Subject Headings
(MeSH), 2026 edition, and a small set of MeSH nodes to group them by. The machine-readable result is
`mesh-mapping.json` (same content as the table below). This extends section 1.1 A of
`method-tree-taxonomies.md`, which looked at MeSH family by family.

Checked on 2026-11-17 against the NLM MeSH RDF service (`year=current`). The edition is 2026: the
Evidence Synthesis publication type carries `dateIntroduced 2026-01-01`.

## Groups

Eight MeSH nodes. A Method belongs to a group when one of its descriptor's tree numbers starts with the
group's tree number. No Method matched two groups (the build script stops if one does).

| Group | UI | Tree | Kind | Methods |
|---|---|---|---|---|
| Case Reports | D002363 | V03.100 | publication type | 1 |
| Clinical Study | D000068397 | V03.175 | publication type | 6 |
| Epidemiologic Methods | D004812 | E05.318 | subject heading | 19 |
| Evidence Synthesis | D000099290 | V03.500 | publication type | 9 |
| Validation Study | D023361 | V03.950 | publication type | 2 |
| Empirical Research | D036262 | H01.770.644.241 | subject heading | 3 |
| Models, Theoretical | D008962 | E05.599 | subject heading | 1 |
| Computing Methodologies | D003205 | L01.224 | subject heading | 3 |
| Not classified by MeSH | | | | 16 |

Why these nodes:
- **Publication types first** (branch V03 "Study Characteristics"). Clinical Study (V03.175) holds both
  Clinical Trial (V03.175.250) and Observational Study (V03.175.500), so one group covers the trials and
  the Methods that MeSH only reaches through Observational Study.
- **Epidemiologic Methods (E05.318)** is used instead of the narrower Epidemiologic Studies
  (E05.318.372.500) because MeSH spreads the observational and measurement designs over four of its
  children: Epidemiologic Study Characteristics (.372: cohort, case-control, cross-sectional, before-after,
  interrupted time series, pilot projects, single-case trials), Epidemiologic Research Design (.370:
  cross-over, sensitivity and specificity, reproducibility), Molecular Epidemiology (.416: Mendelian
  randomization, GWAS) and Data Collection (.308: population surveillance). Its scope note: "Research
  techniques that focus on study designs and data gathering methods".
- **Empirical Research (H01.770.644.241)**, not Qualitative Research (.850), because Grounded Theory
  (.424) is a sibling of Qualitative Research, not a child.
- **Computing Methodologies (L01.224)** holds Computer Simulation (.160), Prediction Methods, Machine
  (.050.375.618) and User-Centered Design (.900.900, under Software).
- Not used: Evaluation Study (V03.400) and Comparative Study (V03.250). Their scope notes are broad
  enough to take almost any Method, so they would group nothing in particular.

## What MeSH does not do

- **Trials are split.** Randomized Controlled Trial and Adaptive Clinical Trial are publication types
  (V03.175.250), but Cross-Over Studies (E05.318.370.150) and Single-Case Studies as Topic (N-of-1,
  E05.318.372.250.250.682) are subject headings in E05. So the crossover and N-of-1 trials land in
  Epidemiologic Methods, not beside the other trials.
- **No experiments outside health.** Factorial experiments, online A/B tests and field experiments have
  no heading or entry term; MeSH's trial headings are defined by health outcomes.
- **Measurement is split.** Validation Study is a publication type (V03.950), but reliability
  (Reproducibility of Results) and diagnostic accuracy (Sensitivity and Specificity) sit in E05.318.370,
  and interlaboratory comparison (Laboratory Proficiency Testing) sits under quality assurance (N04, J01).
- **Some exact headings sit outside every group**: Delphi Technique (L01.906.197, under Systems Analysis),
  Cost-Effectiveness Analysis (N03.219.151.285), Laboratory Proficiency Testing, Benchmarking (N04,
  health-care sense), Organizational Case Studies (N03, N05), and Ethnography, which is only an entry
  term of Anthropology, Cultural (I01.076.201).
- **One tree gap.** Network Meta-Analysis has a single tree number, V03.600.001, under Meta-Analysis at
  V03.600. Meta-Analysis is also V03.500.004 under Evidence Synthesis, but the 2026 tree did not repeat
  its child there. It is grouped with Evidence Synthesis through that shared parent descriptor, the only
  grouping not shown by a direct tree-number prefix.

Corrections to `method-tree-taxonomies.md` §1.1 A: Ethnography is an entry term (of Anthropology,
Cultural), and "Case Study" is an entry term of Case Reports; both were listed there as having no MeSH
heading. Their exact-label lookups do return nothing, which is what that section tested.

## All 60 Methods

"Link" says how the descriptor relates to the Method: *names it* (the descriptor is the design),
*entry term* (the Method's name is an entry term of the descriptor), *nearest broader* (no heading names
the Method, so the narrowest heading whose scope note covers it), or *none*. "Evidence" is a verbatim part
of the descriptor's scope note, or the entry term. PT = publication type; others are subject headings.
Tree numbers in N05/N06 (health care, public health) repeat the E05 ones and do not affect the groups.

| Method (id) | MeSH descriptor (UI) | Link | Tree numbers | Group | Evidence | Note |
|---|---|---|---|---|---|---|
| Case report / case series (`case-report`) | Case Reports (D002363) PT | names it | V03.100 | Case Reports | "Clinical presentations that may be followed by evaluative studies" | Publication type for reports of individual cases. |
| Cross-sectional survey (`cross-sectional`) | Cross-Sectional Studies (D003430) | names it | E05.318.372.500.875, N05.715.360.330.500.875, N06.850.520.450.500.875 | Epidemiologic Methods | "in a representative sample at one particular time" | Own heading, under Epidemiologic Studies. |
| Ecological study (`ecological`) | Epidemiologic Studies (D016021) | nearest broader | E05.318.372.500, N05.715.360.330.500, N06.850.520.450.500 | Epidemiologic Methods | "Studies designed to examine associations" | No heading; 'ecological' appears only as Ecological Fallacy/Bias under Bias. Nearest is Epidemiologic Studies. |
| Monitoring / surveillance (`surveillance`) | Population Surveillance (D011159) | names it | E05.318.308.980.438.700, N05.715.360.300.800.438.625, N06.850.520.308.980.438.700, N06.850.780.675 | Epidemiologic Methods | "Ongoing scrutiny of a population" | Own heading, filed under Data Collection > Surveys and Questionnaires. |
| Capture–recapture (`capture-recapture`) | none | none |  | not classified |  | No heading or entry term (searched capture-recapture, mark-recapture, recapture). |
| Prospective cohort (`cohort-prospective`) | Prospective Studies (D011446) | names it | E05.318.372.500.750.625, N05.715.360.330.500.750.650, N06.850.520.450.500.750.650 | Epidemiologic Methods | "to generate incidence or mortality rates" | Own heading, under Cohort Studies. |
| Retrospective cohort (`cohort-retrospective`) | Retrospective Studies (D012189) | names it | E05.318.372.500.500.500, E05.318.372.500.750.750, N05.715.360.330.500.500.500, N05.715.360.330.500.750.825, N06.850.520.450.500.500.500, N06.850.520.450.500.750.825 | Epidemiologic Methods | "derived from data relating to characteristics of persons under study" | Own heading, filed under both Case-Control and Cohort Studies. |
| Case–control study (`case-control`) | Case-Control Studies (D016022) | names it | E05.318.372.500.500, N05.715.360.330.500.500, N06.850.520.450.500.500 | Epidemiologic Methods | "start with the identification of persons with the disease or outcome" | Own heading, under Epidemiologic Studies. |
| Case-crossover (`case-crossover`) | Epidemiologic Studies (D016021) | nearest broader | E05.318.372.500, N05.715.360.330.500, N06.850.520.450.500 | Epidemiologic Methods | "Studies designed to examine associations" | No heading or entry term; nearest is Epidemiologic Studies. |
| Target trial emulation (`target-trial`) | Observational Study (D064888) PT | nearest broader | V03.175.500 | Clinical Study | "the investigator does not assign participants to specific interventions" | No heading; it analyses observational data, so nearest is the Observational Study publication type. |
| Instrumental variable analysis (`iv`) | Observational Study (D064888) PT | nearest broader | V03.175.500 | Clinical Study | entry term "Natural Experiment" | No heading; 'Natural Experiment' is an entry term of Observational Study. Doubtful: IV is an analysis, not a design. |
| Mendelian randomization (`mendelian`) | Mendelian Randomization Analysis (D057182) | names it | E05.318.416.500 | Epidemiologic Methods | "to correlate the causal effects of those functions or phenotypes" | Own heading, under Molecular Epidemiology. |
| Genome-wide association study (`gwas`) | Genome-Wide Association Study (D055106) | names it | E05.318.370.392, E05.318.416.249, E05.393.385.500, E05.393.522.500, E05.393.760.640.500, N06.850.520.445.392, N06.850.520.470.500 | Epidemiologic Methods | "comparing the allele frequencies of all available" | Own heading, under Epidemiologic Research Design and Molecular Epidemiology. |
| Case-cohort / nested case–control (`case-cohort`) | Case-Control Studies (D016022) | entry term | E05.318.372.500.500, N05.715.360.330.500.500, N06.850.520.450.500.500 | Epidemiologic Methods | entry term "Nested Case-Control Studies" | 'Nested Case-Control Studies' is an entry term of Case-Control Studies; case-cohort itself has no term. |
| Difference-in-differences (`did`) | Controlled Before-After Studies (D065187) | names it | E05.318.372.500.812, N05.715.360.330.500.812, N06.850.520.450.500.812 | Epidemiologic Methods | "both in a group that receives the intervention and in a control group" | Controlled Before-After Studies is the design that difference-in-differences analyses. |
| Regression discontinuity (`rdd`) | Non-Randomized Controlled Trials as Topic (D065228) | nearest broader | E05.318.372.250.250.365.250, N05.715.360.330.250.250.365.250, N06.850.520.450.250.250.365.250 | Epidemiologic Methods | entry term "Quasi-Experimental Studies" | No heading; 'Quasi-Experimental Studies' is an entry term of Non-Randomized Controlled Trials as Topic. |
| Interrupted time series (`its`) | Interrupted Time Series Analysis (D065186) | names it | E05.318.372.500.931, N05.715.360.330.500.912, N06.850.520.450.500.912 | Epidemiologic Methods | "observations at multiple time points before and after an intervention" | Own heading, under Epidemiologic Studies. |
| Synthetic control (`synthetic-control`) | Non-Randomized Controlled Trials as Topic (D065228) | nearest broader | E05.318.372.250.250.365.250, N05.715.360.330.250.250.365.250, N06.850.520.450.250.250.365.250 | Epidemiologic Methods | entry term "Quasi-Experimental Studies" | No heading; nearest is Non-Randomized Controlled Trials as Topic (entry term Quasi-Experimental Studies). Doubtful. |
| Randomized controlled trial (`rct`) | Randomized Controlled Trial (D016449) PT | names it | V03.175.250.500.500 | Clinical Study | "selected by a random process" | Publication type, under Controlled Clinical Trial. |
| Cluster randomized trial (`cluster-rct`) | Randomized Controlled Trial (D016449) PT | nearest broader | V03.175.250.500.500 | Clinical Study | "selected by a random process" | No heading or entry term for cluster randomization; nearest is Randomized Controlled Trial. |
| Crossover trial (`crossover`) | Cross-Over Studies (D018592) | names it | E05.318.370.150, N05.715.360.325.150, N06.850.520.445.150 | Epidemiologic Methods | "upon completion of the course of one treatment, are switched to another" | Own heading, but MeSH files it under Epidemiologic Research Design, not under Clinical Trial. |
| Factorial experiment (DoE) (`factorial-doe`) | none | none |  | not classified |  | No heading or entry term ('factorial', 'design of experiments'); Research Design is too broad to count. |
| N-of-1 trial (`n-of-1`) | Single-Case Studies as Topic (D000080907) | entry term | E05.318.372.250.250.682, N05.715.360.330.250.250.682, N06.850.520.450.250.250.682 | Epidemiologic Methods | entry term "N-of-1 Trials as Topic" | 'N-of-1 Trials as Topic' is an entry term of Single-Case Studies as Topic, under Clinical Trials as Topic (E05). |
| Stepped-wedge trial (`stepped-wedge`) | Randomized Controlled Trial (D016449) PT | nearest broader | V03.175.250.500.500 | Clinical Study | "selected by a random process" | No heading or entry term; nearest is Randomized Controlled Trial. |
| Online A/B test (`ab-test`) | none | none |  | not classified |  | No heading; MeSH trial headings are for health outcomes, and Random Allocation is a technique, not a design. |
| Adaptive / platform trial (`adaptive-platform`) | Adaptive Clinical Trial (D000076362) PT | names it | V03.175.250.050 | Clinical Study | "opportunity is included to modify trial designs" | Own publication type; 'Platform Trial' is one of its entry terms. |
| Field experiment (`field-experiment`) | none | none |  | not classified |  | No heading or entry term ('field experiment', 'field trial'). |
| Ethnography (`ethnography`) | Anthropology, Cultural (D000884) | entry term | I01.076.201 | not classified | entry term "Ethnography" | 'Ethnography' is an entry term of Anthropology, Cultural (I01), outside every group. |
| Grounded theory (`grounded-theory`) | Grounded Theory (D066296) | names it | H01.770.644.241.424 | Empirical Research | "The generation of theories from analysis of empirical data." | Own heading, under Empirical Research beside Qualitative Research. |
| Interviews & thematic analysis (`interviews-thematic`) | Qualitative Research (D036301) | nearest broader | H01.770.644.241.850 | Empirical Research | "employs nonnumeric information to explore individual or group characteristics" | No heading for thematic analysis; Interviews as Topic is a data-collection technique, so Qualitative Research. |
| Case study (in-depth) (`case-study`) | Organizational Case Studies (D019982) | names it | N03.349.380.710, N05.715.360.455 | not classified | "Descriptions and evaluations of specific health care organizations." | Organizational Case Studies (N03/N05); 'Case Study' is also an entry term of the clinical Case Reports. |
| Process tracing (`process-tracing`) | none | none |  | not classified |  | No heading or entry term; Empirical Research would cover it only in the broadest sense. |
| Delphi consensus (`delphi`) | Delphi Technique (D003697) | names it | L01.906.197 | not classified | "An iterative questionnaire designed to measure consensus" | Own heading, filed under Systems Analysis (L01), outside every group. |
| Mixed methods (sequential) (`mixed-sequential`) | Empirical Research (D036262) | nearest broader | H01.770.644.241 | Empirical Research | "direct observation, use of statistical records, interviews" | No heading or entry term for mixed methods; nearest heading covering both strands is Empirical Research. |
| Systematic review & meta-analysis (`systematic-review`) | Systematic Review (D000078182) PT | names it | V02.912.625.509, V03.500.009 | Evidence Synthesis | "identify, appraise, and synthesize all the empirical evidence" | Publication type under Evidence Synthesis; Meta-Analysis is its sibling. |
| Scoping review (`scoping-review`) | Scoping Review (D000098583) PT | names it | V02.912.625.506, V03.500.006 | Evidence Synthesis | "scope a body of literature" | Publication type under Evidence Synthesis. |
| Network meta-analysis (`network-meta`) | Network Meta-Analysis (D000099094) PT | names it | V03.600.001 | Evidence Synthesis | "from a network of interventions" | Only tree V03.600.001 under Meta-Analysis, which is also V03.500.004; grouped through that parent. |
| Individual participant data meta-analysis (`ipd-meta`) | Meta-Analysis (D017418) PT | nearest broader | V02.912.625.504, V03.500.004, V03.600 | Evidence Synthesis | "a quantitative method of combining the results of independent studies" | No heading for individual participant data; nearest is Meta-Analysis (V03.500.004). |
| Umbrella review (`umbrella-review`) | Systematic Review (D000078182) PT | entry term | V02.912.625.509, V03.500.009 | Evidence Synthesis | entry term "Umbrella Review" | 'Umbrella Review' is an entry term of Systematic Review. |
| Rapid review (`rapid-review`) | Evidence Synthesis (D000099290) PT | nearest broader | V02.912.625, V03.500 | Evidence Synthesis | "combines data and insights from multiple sources" | No heading or entry term; nearest is Evidence Synthesis. |
| Realist review (`realist-review`) | Evidence Synthesis (D000099290) PT | nearest broader | V02.912.625, V03.500 | Evidence Synthesis | "combines data and insights from multiple sources" | No heading or entry term; nearest is Evidence Synthesis. |
| Prior art review (`prior-art`) | Evidence Synthesis (D000099290) PT | nearest broader | V02.912.625, V03.500 | Evidence Synthesis | "to summarize existing literature and support informed decisions" | No heading; Evidence Synthesis covers it only by its broad scope note. Doubtful. |
| Co-citation analysis (`co-citation`) | Bibliometrics (D015706) | nearest broader | L01.462.500.682.099.325, L01.462.750.183.291 | not classified | "statistical methods in the analysis of a body of literature" | No heading for co-citation; nearest is Bibliometrics (L01), outside every group. |
| Bibliographic coupling (`bibliographic-coupling`) | Bibliometrics (D015706) | nearest broader | L01.462.500.682.099.325, L01.462.750.183.291 | not classified | "statistical methods in the analysis of a body of literature" | No heading for coupling; nearest is Bibliometrics (L01), outside every group. |
| Multivocal literature review (`multivocal-review`) | Evidence Synthesis (D000099290) PT | nearest broader | V02.912.625, V03.500 | Evidence Synthesis | "combines data and insights from multiple sources" | No heading; Gray Literature is a topic, so nearest is Evidence Synthesis. |
| Diagnostic accuracy study (`diagnostic-accuracy`) | Sensitivity and Specificity (D012680) | nearest broader | E05.318.370.800, E05.318.740.872, G17.800, N05.715.360.325.700, N05.715.360.750.725, N06.850.520.445.800, N06.850.520.830.872 | Epidemiologic Methods | "Binary classification measures to assess test results." | No heading for the study design; Sensitivity and Specificity names the measures it estimates. |
| Reliability & agreement study (`reliability`) | Reproducibility of Results (D015203) | names it | E05.318.370.725, E05.337.851, N05.715.360.325.685, N06.850.520.445.725 | Epidemiologic Methods | "statistical reproducibility of measurements" | Own heading ('Test-Retest Reliability' is an entry term), under Epidemiologic Research Design. |
| Instrument development & validation (`validation`) | Validation Study (D023361) PT | names it | V03.950 | Validation Study | "reliability and relevance of a procedure for a specific purpose" | Validation Study publication type. |
| Nomological network study (`nomological`) | Validation Study (D023361) PT | nearest broader | V03.950 | Validation Study | "reliability and relevance of a procedure for a specific purpose" | No heading for nomological networks or construct validity; nearest is Validation Study. |
| Discrete choice experiment (`discrete-choice`) | none | none |  | not classified |  | No heading or entry term ('discrete choice', 'conjoint'); Choice Behavior is the topic, not the method. |
| Interlaboratory comparison (`interlab`) | Laboratory Proficiency Testing (D059021) | names it | J01.897.608.500, N04.761.700.512 | not classified | "Identical survey samples are distributed to participating laboratories" | Laboratory Proficiency Testing names the design but is filed under quality assurance (N04/J01). |
| Analytical / mathematical theory (`analytical-model`) | Models, Theoretical (D008962) | names it | E05.599 | Models, Theoretical | "They include the use of mathematical equations" | Own heading; 'Mathematical Model' is an entry term. |
| Computational simulation (`simulation`) | Computer Simulation (D003198) | names it | L01.224.160 | Computing Methodologies | "Computer-based representation of physical systems and phenomena" | Own heading, under Computing Methodologies. |
| Prediction model (statistical / ML) (`prediction-model`) | Prediction Methods, Machine (D000098411) | names it | G17.035.250.625, L01.224.050.375.618 | Computing Methodologies | "Methods of making prediction about a new measurement" | Prediction Methods, Machine; its label says machine, but its scope note covers statistical models too. |
| Cost-effectiveness analysis (`economic-evaluation`) | Cost-Effectiveness Analysis (D000094703) | names it | N03.219.151.285 | not classified | "Cost effectiveness compares alternative ways to achieve a specific set of results." | Own heading, filed under Costs and Cost Analysis (N03), outside every group. |
| Design science (build & evaluate) (`design-science`) | none | none |  | not classified |  | No heading; Equipment Design is hardware only and Proof of Concept Study only partly fits. |
| Pilot / feasibility study (`pilot`) | Pilot Projects (D010865) | names it | E05.318.372.750, E05.337.737, N05.715.360.330.720, N06.850.520.450.720 | Epidemiologic Methods | "Small-scale tests of methods and procedures" | Own heading ('Pilot Study' is an entry term), under Epidemiologic Study Characteristics. |
| Usability test (think-aloud) (`think-aloud`) | User-Centered Design (D000086825) | entry term | E05.320.775, J01.293.910.500, L01.224.900.900 | Computing Methodologies | entry term "Usability Testing" | 'Usability Testing' is an entry term of User-Centered Design, filed under Software. |
| Plan–Do–Study–Act cycles (`pdsa`) | Quality Improvement (D058996) | nearest broader | J01.293.754, N04.761.744 | not classified | "process of attaining a new level of performance or quality" | No heading or entry term for PDSA; nearest is Quality Improvement (N04/J01), outside every group. |
| Benchmark evaluation (`benchmark`) | Benchmarking (D019985) | names it | N04.452.500.150, N04.761.685.150, N04.761.700.150, N05.700.150, N05.715.360.650.150 | not classified | "Method of measuring performance against established standards" | Benchmarking is filed under health-care quality (N04); its sense differs from method benchmarks. |

## How it was checked

All on 2026-11-17, with a generic User-Agent and no personal details:
- Exact-label lookup for every candidate heading:
  `https://id.nlm.nih.gov/mesh/lookup/descriptor?label=<label>&match=exact&year=current`, and
  `match=contains` for the Methods with no exact hit.
- Records: `https://id.nlm.nih.gov/mesh/<UI>.json` for the type (`PublicationType` or
  `TopicalDescriptor`), tree numbers and `dateIntroduced`; the preferred concept's JSON
  (`https://id.nlm.nih.gov/mesh/<M...>.json`) for the scope note.
- Entry terms: SPARQL on `https://id.nlm.nih.gov/mesh/sparql` (graph `http://id.nlm.nih.gov/mesh`),
  every term of every concept whose label contains a phrase, for about 90 phrases (for example
  "capture-recapture", "case-crossover", "stepped wedge", "ethnograph", "usability", "umbrella review").
- Group contents: SPARQL listing of every descriptor whose tree number starts with V03, E05.318.372,
  E05.318.370, E05.318.416, E05.318.308, E05.318.740, E05.337, E05.599, E05.581, H01.770.644, L01.224.900
  and others.
- A script took every label, type and tree number from those records, checked each evidence phrase is
  verbatim in the scope note (or that the entry term was returned by SPARQL), and computed the groups from
  tree-number prefixes. The script and cached records are in the session scratchpad only.

## Not verified

- The MeSH facts above are verified. What is a judgement, not a MeSH fact, is each "nearest broader"
  choice (20 Methods) and the reading of a scope note as covering a Method. The doubtful ones:
  - Instrumental variable analysis via the entry term "Natural Experiment" of Observational Study: an
    instrumental variable is an analysis, not a design.
  - Regression discontinuity and synthetic control via the entry term "Quasi-Experimental Studies" of
    Non-Randomized Controlled Trials as Topic: in both, the investigator does not assign treatment.
  - Prior art review in Evidence Synthesis: covered only by the broad scope note.
  - Prediction model as Prediction Methods, Machine: the scope note fits statistical models, the label
    does not.
  - Mixed methods in Empirical Research, and process tracing left out of it, are a line drawn by hand.
  - Benchmark evaluation and Benchmarking share a name, but MeSH's sense is health-care quality.
- The search for entry terms used phrases I chose; a heading reachable only through a wording I did not
  try would have been missed.
- That the RDF service's `current` year is the full 2026 release was inferred from `dateIntroduced`
  dates, not from a stated release number.
