# Taxonomy sources: method families and research fields

Which published classification each category in Methodical can be quoted from, checked on 2026-11-16.
Every entry says what was read and where. Nothing here is from memory. Sources already verified in
`method-tree-sources.md` (Saunders et al. 2019, Gregor 2006, Shmueli 2010, Hernán et al. 2019, Grimes & Schulz 2002,
Grant & Booth 2009) are not re-checked, except that the Grimes & Schulz abstract has now been read in its
PubMed record (see below).

Game data read: `data/meta.json` (9 families), `data/designs.json` (60 methods with `family` and `ref`),
`data/questions.json` (74 questions, 61 distinct `field` values).

---

## 1. Method families

### 1.1 Candidate sources

#### A. NLM Medical Subject Headings (MeSH), 2026 edition

Read through the NLM MeSH SPARQL endpoint and lookup service (https://id.nlm.nih.gov/mesh/, `year=current`;
the Evidence Synthesis record carries `dateIntroduced 2026-01-01`, so this is MeSH 2026). Tree numbers and
labels below are copied from the query results; scope notes from each descriptor's preferred concept.

MeSH has two relevant parts:

**(i) Publication types, branch V03 "Study Characteristics" (D052182)**, scope note "Type of empirical method used."
Its direct children (own words):

| Tree | Publication type |
|---|---|
| V03.100 | Case Reports |
| V03.150 | Clinical Conference |
| V03.175 | Clinical Study, with V03.175.250 **Clinical Trial** (Adaptive, Phase I–IV, Controlled, Human Challenge, Pragmatic) and V03.175.500 **Observational Study** |
| V03.250 | Comparative Study |
| V03.400 | Evaluation Study |
| V03.500 | **Evidence Synthesis** (new in 2026): Consensus Statement, Guideline, Meta-Analysis, Scoping Review, Systematic Review |
| V03.600 | Meta-Analysis, with Network Meta-Analysis |
| V03.650 | Multicenter Study |
| V03.800 | Scientific Integrity Review |
| V03.900 | Twin Study |
| V03.950 | **Validation Study** |

Clinical Trial vs Observational Study is defined by whether the investigator assigns the intervention
(Observational Study scope note: the investigator "does not assign participants to specific interventions").

**(ii) Subject headings in E05 "Investigative Techniques" and H01 "Research"**:
- E05.318.372 Epidemiologic Study Characteristics → E05.318.372.500 **Epidemiologic Studies** (Case-Control,
  Cohort [Prospective, Retrospective, Longitudinal], Controlled Before-After Studies, Cross-Sectional Studies,
  Historically Controlled Study, Interrupted Time Series Analysis, Seroepidemiologic Studies); also Clinical Studies
  as Topic (Clinical Trials, Observational Studies), Feasibility Studies, Pilot Projects, Twin Studies.
  Epidemiologic Studies scope note: studies "designed to examine associations", and it names cross-sectional
  studies among the "common types of analytic study".
- E05.318.416 Molecular Epidemiology → Genome-Wide Association Study, Mendelian Randomization Analysis.
- E05.318.370 Epidemiologic Research Design → includes Cross-Over Studies, Reproducibility of Results,
  Sensitivity and Specificity, Meta-Analysis as Topic.
- E05.337 Evaluation Studies as Topic → Feasibility Studies, Pilot Projects, Program Evaluation, Validation Studies
  as Topic, Reproducibility of Results.
- E05.599 Models, Theoretical (Models, Biological / Statistical / Psychological, Nonlinear Dynamics…);
  L01.224.160 Computer Simulation; N03.219.151.125 Cost-Benefit Analysis; E05.320 Equipment Design
  (E05.320.775 User-Centered Design); N04 Benchmarking; J01/N04 Quality Improvement.
- H01.770.644.241 Empirical Research → Grounded Theory, **Qualitative Research** (scope note: research that uses
  "nonnumeric information to explore individual or group characteristics").
- L01.462.500.682.759 Review Literature as Topic → Scoping Reviews, Systematic Reviews as Topic.
- Also present: Delphi Technique (L01.906.197), Bibliometrics (L01.462…), Interviews as Topic, Focus Groups,
  Psychometrics (F04.711.780), Surveys and Questionnaires, Population Surveillance.
- **No MeSH heading** (exact-label lookup returned nothing): Mixed Methods Research, Ethnography, Case Studies,
  Ecological Studies, Natural Experiment, Difference-in-Differences Analysis, Regression Discontinuity Design,
  Discrete Choice Experiment, Instrumental Variable Analysis.

Mapping of the 9 families:

| Family | MeSH home | Fit |
|---|---|---|
| Descriptive observational | Case Reports (V03.100); Population Surveillance; Cross-Sectional Studies | **Partial.** No "descriptive" node; MeSH files cross-sectional studies as analytic. |
| Analytical observational | Epidemiologic Studies (E05.318.372.500); Molecular Epidemiology for GWAS and Mendelian randomization | **Clean** (but IV analysis has no heading) |
| Quasi-experimental | Interrupted Time Series Analysis and Controlled Before-After Studies (under Epidemiologic Studies); Non-Randomized Controlled Trials as Topic | **No home as a group.** The designs are split between observational and trial branches. |
| Experimental | Clinical Trial (V03.175.250) / Clinical Trials as Topic; Cross-Over Studies; also Animal Experimentation, Games, Experimental (E05) | **Clean** for clinical trials; A/B tests, factorial DoE and field experiments have no specific heading |
| Qualitative & mixed | Qualitative Research, Grounded Theory (H01.770.644.241) | **Clean for qualitative**; mixed methods has no heading; Delphi sits in L01 |
| Evidence synthesis | Evidence Synthesis (V03.500), Meta-Analysis / Network Meta-Analysis (V03.600) | **Clean** (the 2026 publication type uses the game's own term); bibliometric methods (co-citation, coupling) sit under Bibliometrics (L01), prior art review has no heading |
| Measurement | Validation Study (V03.950); Reproducibility of Results; Sensitivity and Specificity; Psychometrics | **Partial**, scattered over several branches |
| Theory & computation | Models, Theoretical (E05.599); Computer Simulation (L01.224.160); Cost-Benefit Analysis (N03); Machine Learning (G17/L01) | **No home as a group**, scattered |
| Design & development | Equipment Design / User-Centered Design (E05.320); Pilot Projects, Feasibility Studies; Evaluation Study (V03.400); Quality Improvement; Benchmarking | **No home as a group**, scattered |

Verdict: 4 clean (analytical, experimental, qualitative, synthesis), 2 partial, 3 with no home.
MeSH is authoritative, freely checkable and versioned, but it is an indexing vocabulary for biomedicine, not a
typology of designs, and it disagrees with the game on cross-sectional studies.

#### B. EQUATOR Network reporting guidelines

Read the live pages on 2026-11-16 (saved HTML, parsed with a script):
- Home page https://www.equator-network.org/, panel "Most commonly used reporting guidelines". Groups (own words):
  **Observational epidemiology** (STROBE: cohort, case-control, cross-sectional), **Systematic reviews**
  (PRISMA, PRISMA-P, MOOSE), **Randomized trials** (CONSORT, SPIRIT), **Diagnosis and prognosis** (STARD,
  TRIPOD+AI), **Qualitative research** (COREQ, SRQR), **Case reports** (CARE), **Animal research** (ARRIVE),
  **Quality improvement in healthcare** (SQUIRE), **Economic evaluations** (CHEERS).
- Database list https://www.equator-network.org/reporting-guidelines/, column "Study type". Every label used
  (count of guidelines tagged): Experimental studies (262), Clinical trials (254), Observational studies (244),
  No study design specified (130), Systematic reviews/Meta-analyses/Reviews/HTA/Overviews (66), Qualitative
  research (58), Diagnostic and prognostic studies (40), Artificial intelligence/Machine learning studies (31),
  Economic evaluations (30), Study protocols (30), Animal pre-clinical research (24), Mixed methods studies (21),
  Other (20), Clinical practice guidelines (19), Quality improvement studies (14), Reliability and agreement
  studies (4), Letters to the editor/Correspondence (1), Patent landscapes (1).

| Family | EQUATOR home | Fit |
|---|---|---|
| Descriptive observational | Observational studies; Case reports | Clean (but not separated from analytical) |
| Analytical observational | Observational studies / Observational epidemiology | Clean (merged with descriptive) |
| Quasi-experimental | none | **No home** |
| Experimental | Experimental studies; Clinical trials | Clean |
| Qualitative & mixed | Qualitative research; Mixed methods studies | Clean |
| Evidence synthesis | Systematic reviews/Meta-analyses/Reviews/HTA/Overviews | Clean |
| Measurement | Diagnostic and prognostic studies; Reliability and agreement studies | Clean for diagnostic accuracy and reliability; no home for instrument validation or discrete choice |
| Theory & computation | Economic evaluations; Artificial intelligence/Machine learning studies; prediction models under Diagnosis and prognosis (TRIPOD) | Partial: no home for analytical models or simulation |
| Design & development | Quality improvement studies (PDSA) | Partial: no home for design science, usability tests, benchmarks |

Verdict: 6 clean, 2 partial, 1 no home (quasi-experimental). Best coverage, but these are website filter tags
for health-research reporting guidelines, not a published classification with a citable document, and they
change without versioning.

#### C. Grimes & Schulz (2002)

Abstract now read in the PubMed record (PMID 11809203, via NCBI E-utilities), DOI 10.1016/S0140-6736(02)07283-5
(Crossref check already in `method-tree-sources.md`). Categories (own words): research is **experimental** or
**observational**, "based on whether the investigator assigns the exposures"; experimental trials are randomised
or non-randomised; observational studies are **analytical** (with a comparison group) or **descriptive**. The
abstract lists cohort, case-control **and cross-sectional** studies within analytical studies, and case series as
descriptive.

| Family | Fit |
|---|---|
| Descriptive observational | Clean (but cross-sectional surveys are analytical in this scheme) |
| Analytical observational | Clean |
| Experimental | Clean |
| Quasi-experimental | Ambiguous: "non-randomised" trials are experimental, but natural experiments (DiD, RDD, ITS, synthetic control: the investigator does not assign) fall under observational |
| The other 5 families | No home (out of scope: clinical research designs only) |

#### D. ERIC Thesaurus (education)

Read the descriptor pages https://eric.ed.gov/?ti=Research+Methodology, …?ti=Research+Design,
…?ti=Quasiexperimental+Design. "Research Methodology" (broader term: Methods) has narrower terms including
Grounded Theory, Mixed Methods Research, Randomized Controlled Trials, Control Groups; related terms include
Meta Analysis, Literature Reviews, Evaluation Research, Field Studies, Monte Carlo Methods, Participant Observation,
Qualitative Research, Quasiexperimental Design. "Research Design" has one narrower term, **Quasiexperimental
Design** (scope note: research where "normal experimental controls are not, or cannot be" applied).
Verdict: a flat set of related terms, not a classification of designs; useful only as a citable home for the term
"quasi-experimental". Other descriptors were not checked one by one.

#### E. SAGE Research Methods "Methods Map"

https://methods.sagepub.com/methods-map redirects to a SAGE sign-in page. **Not verified**; not freely checkable,
so unsuitable as the game's citation anyway.

### 1.2 Recommendation for method families

No single source covers all nine families. The smallest quotable set:

1. **Grimes & Schulz (2002)** for the spine: experimental vs observational (who assigns the exposure), and
   observational split into descriptive vs analytical. Covers families 1, 2, 4.
2. **MeSH 2026 publication types (V03 "Study Characteristics")** for **Evidence synthesis** (V03.500, the exact
   term), **Qualitative research** (descriptor D036301) and **Validation study** (V03.950). Free, versioned,
   checkable record by record.
3. For the families neither covers, cite the family's anchor paper and call the grouping the game's own:
   - **Quasi-experimental**: ERIC "Quasiexperimental Design" gives the term; the classic book (Shadish, Cook &
     Campbell 2002) was **not verified**.
   - **Design & development**: Hevner et al. (2004), *MIS Quarterly* 28(1): 75–106, doi:10.2307/25148625
     (Crossref checked: title, authors, volume, pages), together with Gregor's (2006) "design and action"
     (already in `method-tree-sources.md`).
   - **Theory & computation** and **Measurement**: no published grouping found; say "own grouping".

Points to settle before quoting:
- **Cross-sectional survey and ecological study** are in the game's *descriptive* family; Grimes & Schulz and MeSH
  both treat cross-sectional studies as analytical. Either move them, or say the game follows the
  descriptive-epidemiology use (a prevalence survey with no comparison) and flag the difference.
- **Quasi-experimental** needs a decision: as its own family it has no home in MeSH, EQUATOR or Grimes & Schulz.
- **Measurement** would map better if renamed "Measurement & validation" (MeSH Validation Study; EQUATOR
  "Diagnostic and prognostic" and "Reliability and agreement"). Discrete choice experiments fit poorly here.
- **Theory & computation** mixes kinds: prediction models are "Diagnosis and prognosis" in EQUATOR and
  cost-effectiveness is "Economic evaluations"; only analytical models and simulation are truly theory/computation.
- **Evidence synthesis** includes co-citation, bibliographic coupling and prior art review; MeSH files bibliometrics
  under information science, not evidence synthesis.
- **Delphi** sits in "Qualitative & mixed"; MeSH files Delphi Technique under L01 (information science), not
  qualitative research.

---

## 2. Research fields

### 2.1 Recommended classification

**OECD Fields of Research and Development (FORD)**, Frascati Manual 2015, Table 2.2 "Fields of R&D
classification", p. 59 (§2.6, ¶2.42–2.45). OECD (2015), *Frascati Manual 2015: Guidelines for Collecting and
Reporting Data on Research and Experimental Development*, OECD Publishing, Paris,
doi:10.1787/9789264239012-en (Crossref checked: title "Frascati Manual 2015", OECD Publishing, issued
2015-10-08, type book). Read in the official PDF from oecd.org
(`.../frascati-manual-2015_g1g57dcb/9789264239012-en.pdf`, 402 pages).

Table 2.2 gives names only. What each subfield covers is in its predecessor, **OECD (2007), Revised Field of
Science and Technology (FOS) Classification in the Frascati Manual**, DSTI/EAS/STP/NESTI(2006)19/FINAL,
26 Feb 2007, Annex 1 (pp. 6–11), read in the official PDF at one.oecd.org. The 2015 Manual says FORD is
"closely related to and consistent with" UNESCO (1978) and that later versions sit in online annexes (¶2.44–2.45).
The 2015 names differ slightly from 2007 (e.g. 5.1 "Psychology and cognitive sciences", 5.3 "Education",
6 "Humanities and the arts"); codes are the same. The mapping below uses 2015 names and 2007 descriptions.

Top level (2015): 1 Natural sciences; 2 Engineering and technology; 3 Medical and health sciences;
4 Agricultural and veterinary sciences; 5 Social sciences; 6 Humanities and the arts.

FORD is suitable: it covers every field in the game at two-digit level, and its notes resolve most borderline cases
explicitly (e.g. "medical genetics to be 3", robotics in 2.2, infectious diseases in 3.3). Alternatives (ANZSRC FoR
2020, ISCED-F 2013) were not needed and not checked.

### 2.2 Mapping of the 61 `field` values

"Evidence" quotes the 2007 Annex 1 description that places the topic. ⚠ = not a clean fit (reason given).

| Field (questions) | FORD code and subfield | Evidence / note |
|---|---|---|
| Agriculture (Q19) | 4.1 Agriculture, forestry, and fisheries | "Agronomy, plant breeding and plant protection" |
| Agricultural economics (Q68) | 5.2 Economics and business | ⚠ Not named; 4.5 Other agricultural sciences is the alternative |
| Analytical chemistry (Q37) | 1.4 Chemical sciences | "Analytical chemistry" |
| Astronomy (Q04) | 1.3 Physical sciences | "Astronomy (including astrophysics, space science)" |
| Astrophysics (Q42) | 1.3 Physical sciences | as above |
| Biomedical engineering (Q36) | 2.6 Medical engineering | "Medical engineering" |
| Cardiology (Q09, Q11, Q27, Q31, Q67) | 3.2 Clinical medicine | "Cardiac and Cardiovascular systems" |
| Civil engineering (Q39) | 2.1 Civil engineering | "Municipal and structural engineering" |
| Clinical trials (Q59) | 3.2 Clinical medicine | ⚠ A method, not a field; the question is about a rare disease ("other clinical medicine subjects") |
| Conservation (Q22) | 1.6 Biological sciences | "Biodiversity conservation" |
| Critical care (Q28) | 3.2 Clinical medicine | "Critical care medicine and Emergency medicine" |
| Dermatology (Q02) | 3.2 Clinical medicine | "Dermatology and venereal diseases" |
| Digital health (Q60) | 3.3 Health sciences | ⚠ Not named; closest "Health care sciences and services" (telemedicine adoption) |
| Ecology (Q03, Q32, Q65) | 1.6 Biological sciences | "Ecology" |
| Economics (Q16, Q26, Q43) | 5.2 Economics and business | "Economics, Econometrics" |
| Education (Q12) | 5.3 Education | "Education, general; including training, pedagogy, didactics" |
| Education policy (Q14) | 5.3 Education | ⚠ Minor: policy aspects could be 5.6 (public administration) |
| Educational psychology (Q64) | 5.1 Psychology and cognitive sciences | ⚠ Sits between 5.1 and 5.3; the question (scale validity) is psychological |
| Environmental health (Q06) | 3.3 Health sciences | "Public and environmental health" |
| Environmental science (Q50) | 1.5 Earth and related environmental sciences | "Environmental sciences" |
| Epidemiology (Q40) | 3.3 Health sciences | "epidemiology" |
| Genetics (Q66) | 3.1 Basic medicine | "Human genetics"; 1.6 says "medical genetics to be 3" (migraine GWAS) |
| Geriatrics (Q47) | 3.2 Clinical medicine | "Geriatrics and gerontology" |
| Global health (Q48, Q54) | 3.3 Health sciences | "Public and environmental health; Tropical medicine" |
| Health economics (Q69) | 3.3 Health sciences | ⚠ "health care financing" is in 3.3; economic method points to 5.2 |
| Health policy (Q52) | 3.3 Health sciences | "Health policy and services" |
| Health services (Q15) | 3.3 Health sciences | "Health care sciences and services" |
| Health sociology (Q58) | 5.4 Sociology | ⚠ Or 3.3 "Social biomedical sciences"; both defensible |
| Health systems (Q23) | 3.3 Health sciences | "Health policy and services" |
| Human–computer interaction (Q72) | 5.1 Psychology and cognitive sciences | ⚠ FOS places "human - machine relations" in psychology; many would expect 1.2 |
| Hydrology (Q29) | 1.5 Earth and related environmental sciences | "Oceanography, Hydrology, Water resources" |
| Infectious disease (Q24) | 3.3 Health sciences | "Infectious diseases" (in health sciences, not clinical medicine) |
| Manufacturing (Q20) | 2.3 Mechanical engineering | ⚠ Welding/manufacturing not named; 2.5 Materials engineering or 2.11 Other are alternatives |
| Materials science (Q30) | 1.3 Physical sciences | ⚠ The question is about superconductors: "Condensed matter physics (including … superconductivity)"; the label suggests 2.5 Materials engineering |
| Medical devices (Q61) | 2.6 Medical engineering | "Medical engineering" |
| Neurology (Q10, Q17) | 3.2 Clinical medicine | "Clinical neurology" |
| Nursing (Q55) | 3.3 Health sciences | "Nursing" |
| Nutrition (Q53) | 3.3 Health sciences | "Nutrition, Dietetics" |
| Occupational health (Q08) | 3.3 Health sciences | "Occupational health" |
| Occupational psychology (Q34) | 5.1 Psychology and cognitive sciences | "Psychology" |
| Oncology (Q71) | 3.2 Clinical medicine | "Oncology" |
| Operations management (Q57) | 5.2 Economics and business | "Business and Management" |
| Paediatric oncology (Q07) | 3.2 Clinical medicine | "Paediatrics"; "Oncology" |
| Paediatrics (Q33) | 3.2 Clinical medicine | "Paediatrics" |
| Pharmacoepidemiology (Q25) | 3.3 Health sciences | ⚠ Splits between 3.1 "Pharmacology and pharmacy" and 3.3 "epidemiology" |
| Pharmacology (Q05, Q18) | 3.1 Basic medicine | "Pharmacology and pharmacy" |
| Physics (Q38) | 1.3 Physical sciences | ⚠ Minor: "Thermodynamics" is listed under 2.3 Mechanical engineering; theoretical physics stays 1.3 |
| Political science (Q70) | 5.6 Political science | "Political science" |
| Primary care (Q73) | 3.3 Health sciences | ⚠ Q73 is service improvement ("Health care sciences and services"); 3.2 "General and internal medicine" is the alternative |
| Psychiatry (Q49, Q51) | 3.2 Clinical medicine | "Psychiatry" |
| Public health (Q01, Q13) | 3.3 Health sciences | "Public and environmental health" |
| Radiology (Q35) | 3.2 Clinical medicine | "Radiology, nuclear medicine and medical imaging" |
| Rehabilitation engineering (Q45) | 2.6 Medical engineering | ⚠ Minor: prosthetics not named |
| Research software (Q46) | 1.2 Computer and information sciences | ⚠ Minor: "Computer sciences, information science"; the field label is unusual |
| Robotics (Q44) | 2.2 Electrical engineering, electronic engineering, information engineering | "Robotics and automatic control" |
| Science of science (Q63) | 5.8 Media and communications | ⚠ Not named; bibliometrics fits "Information science (social aspects); Library science". 6.3 (history and philosophy of science) is the alternative |
| Software engineering (Q74) | 1.2 Computer and information sciences | "Computer sciences" |
| Sustainability science (Q62) | 5.9 Other social sciences | ⚠ No home; interdisciplinary ("Social sciences, interdisciplinary"); 1.5 or 5.7 "Environmental sciences (social aspects)" are alternatives |
| Systems biology (Q41) | 1.6 Biological sciences | "Biology (theoretical, mathematical …)" |
| Tech (Q21) | 5.2 Economics and business | ⚠ Not a field; an e-commerce A/B test is business/marketing. 1.2 is the alternative. Suggest relabelling (e.g. "E-commerce") |
| Urban anthropology (Q56) | 5.4 Sociology | "Anthropology, ethnology" |

Summary: 61 distinct fields; **43 map cleanly**, **18 flagged** (⚠). Of the flagged, 2 labels are not fields at
all ("Clinical trials", "Tech"), 1 has a label that contradicts its question's FORD home ("Materials science"),
and the rest sit between two subfields or are not named in the descriptions. Every field has at least one
defensible FORD home; none is unclassifiable. By broad field: 3 Medical and health sciences holds 28 of 61 fields.

---

## 3. Not verified

- **SAGE Research Methods "Methods Map"**: requires sign-in; its categories were not read.
- **Shadish, Cook & Campbell (2002)**, *Experimental and Quasi-Experimental Designs for Generalized Causal
  Inference*: not read; named only as the likely anchor for the quasi-experimental family.
- **Frascati Manual 2015 online annexes** (¶2.45 says FORD is updated there): not located; any post-2015 changes to
  subfield descriptions were not checked. The mapping relies on the 2007 FOS descriptions.
- **ERIC** descriptors other than Research Methodology, Research Design and Quasiexperimental Design.
- **EQUATOR** has no versioned or citable document for its study-type tags; the counts are a snapshot of the live
  page on 2026-11-16 and will change.
- **Grant & Booth (2009)** 14 review types were not re-read, so whether co-citation analysis, bibliographic coupling,
  prior art review or multivocal review appear among them is not checked.
- **ANZSRC FoR 2020** and **UNESCO ISCED-F 2013**: not checked (not needed).
- Full texts of Grimes & Schulz (2002) and Hevner et al. (2004): only the PubMed abstract and the Crossref record
  respectively were read.
