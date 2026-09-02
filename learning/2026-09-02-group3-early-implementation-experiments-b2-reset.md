# Group 3 — Early Implementation, M2 Experiments, and the Clean-Slate B2 Reset

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@5eeb350fba2046c1c54f337a944bd2460fda2a57`  
**Historical code snapshot used where implementation detail matters:** `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`  
**Roadmap responsibility:** Group 3 from `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** transition learning snapshot from early Python/M2 implementation through the B1/B2 clean-slate reset  
**Target depth:** implementation-adjacent; **must own the architecture/authority lesson**, understand representative historical mechanisms operationally, and treat obsolete source details as lookup-level

This note answers one question:

> **What did UpgradePilot build and learn before B2, and why did the project deliberately preserve that work as evidence while refusing to let it become the new B2 architecture by inheritance?**

The answer is not that the early work was useless or simply “wrong.” Several mechanisms were technically valuable. The important transition was from **building a narrow first slice around known inputs and reports** to **deriving implementation responsibility from the fuller product evidence exposed by simulation**.

---

## 1. The whole transition in one view

```text
initial Python package boundary
+ trusted typed case contracts
        ↓
M2-S01 trusted manual case transformation
        ↓
M2-S02 bounded semantic-extraction experiment
        ↓
useful trust/grounding lessons
BUT tested local models rejected for normal extraction
        ↓
M2-S03 evidence-to-report orientation
        ↓
product simulation exposes a wider runtime responsibility
        ↓
D1 freezes a different minimum credible responsibility
        ↓
B1 refuses automatic inheritance from old source/tests/dependencies
        ↓
ADR-0003 clean-slate active-source reset
        ↓
B2 rebuilds incrementally from current responsibilities and evidence
```

Three different things must stay separate:

1. **historical implementation evidence** — what the M2 source/tests actually demonstrated;
2. **historical learning/design evidence** — what the experiments and plans taught;
3. **current controlling semantics/implementation** — what later specifications, ADRs, plans, active source/tests, and evidence now own.

Group 3 is mainly about the transition between the first two and the third.

---

## 2. First foundation: a deliberately small Python product boundary

ADR-0001 established a professional but intentionally non-speculative Python baseline:

```text
repository: UpgradePilot
package/distribution: upgradepilot
source root: src/upgradepilot/
test root: tests/
```

The decision matters because it did **two opposite things at once**:

- created a real installed-package boundary suitable for a long-lived Python application;
- refused to pre-create `domain/`, `services/`, `adapters/`, `infrastructure/`, or other architecture merely because those names are common.

The original source was therefore allowed to begin as cohesive modules directly inside `src/upgradepilot/`.

### Architecture lesson

A clean project start does not require predicting the final package tree.

```text
stable outer package boundary
+
small current responsibility
→ enough structure to build honestly

future responsibility evidence
→ may later justify internal subpackages
```

This is a recurring UpgradePilot pattern: **real responsibility earns structure**.

### Proof boundary

ADR-0001 selected the layout. Editable install/import commands and tests were the implementation proof. The ADR itself never proved that the package actually installed or imported correctly.

---

## 3. M2-S01: turn a manually supplied case into trusted application contracts

The first bounded M2 responsibility did not start with live GitHub acquisition or a complete dependency-update investigation.

It accepted an eight-field manually assembled case input:

```text
repository
pr_number
base_sha
head_sha
dependency
old_version
new_version
changed_files
```

and transformed it into distinct trusted concepts:

```text
PullRequestSnapshotIdentity
+
DependencyChange
+
ChangedFileEvidence
→ InitialCaseRecord
```

At historical snapshot `e7425dc...`, `case_identity.py` used Pydantic v2 models with strict validation and frozen trusted records. Representative behavior included:

- `owner/name` repository validation;
- positive PR number;
- exact 40-character hexadecimal base/head SHAs, normalized to lowercase;
- non-empty dependency/version text;
- old/new versions must differ;
- non-empty unique changed-file paths;
- explicit flat-input → nested trusted-record assembly.

### Why the separation was useful

The flat input was an adapter shape, not the domain model.

```text
incoming mapping
→ validate / normalize
→ separate exact PR identity
→ separate dependency transition
→ separate changed-file evidence
→ trusted aggregate
```

That made several concepts visible early:

- input shape vs trusted internal representation;
- identity vs dependency change vs evidence;
- normalization vs semantic interpretation;
- mutable caller data vs frozen trusted state;
- validation failure vs partial trusted output.

These are still valuable engineering lessons even though the exact M2 classes are historical.

### What M2-S01 did not prove

It did not establish:

- live acquisition;
- real evidence authority;
- semantic upstream interpretation;
- repository-specific applicability;
- CI authority;
- complete decision semantics;
- reporting architecture;
- final B2 contract shapes.

A strong contract around manually supplied facts is useful, but it can only be trusted **for the responsibility it actually owns**.

---

## 4. ADR-0002: why Pydantic was initially reasonable — and why that did not make it permanent

M2 selected Pydantic v2 for its runtime contracts.

The historical method provided:

- strict validation;
- frozen typed models;
- structured validation errors;
- explicit adapters;
- machine-readable serialization.

For the then-active responsibility, this was a credible implementation method.

But ADR-0002 is now **superseded**.

That distinction is important:

```text
method was useful and accepted for responsibility R1
!=
method must remain accepted for later responsibility R2
```

A dependency or framework does not gain permanent architecture authority merely because working source/tests already use it.

When the owning product responsibility changed materially, the method had to earn admission again against the new needs and a simpler credible baseline.

This is one of the central architecture lessons of Group 3.

---

## 5. M2-S02: semantic extraction was an experiment in controlled model authority

The next problem was genuinely semantic.

UpgradePilot had accepted source text such as release notes and needed to derive structured meaning without pretending that source text, model output, and confirmed truth were the same thing.

The historical intended flow was:

```text
known source text
→ candidate model extraction
→ deterministic schema/mechanical validation
→ mechanically grounded attributed claim
→ deterministic decision input
```

The experiment preserved a crucial trust ladder:

```text
raw source text
!= untrusted model output
!= mechanically grounded claim
!= independently corroborated fact
!= final decision
```

### Representative historical contracts

At `e7425dc...`, `extraction.py` distinguished:

- `CandidatePythonSupportClaim` — an untrusted structured claim proposed by an extractor;
- `CandidateExtractionResult` — untrusted structured model output;
- `GroundedPythonSupportClaim` — a claim that passed mechanical grounding controls;
- `ExtractionResult` — validated application result including grounded claims, unresolved items, and validation errors;
- `PythonSupportCandidateExtractor` — a provider protocol;
- `PythonSupportExtractionService` — orchestration that called the extractor, then a separate deterministic validator.

A grounded claim retained:

```text
evidence_id
source_quote
extractor_id
authority = model_derived
```

and preserved `model_derived` authority when crossing into the decision contract.

That is a strong trust-boundary idea:

> **Mechanical grounding can establish that the interpretation is tied to the supplied source span; it does not magically convert model interpretation into independent truth.**

---

## 6. The most important M2-S02 result was negative

M2-S02 did not end with “we successfully added an LLM extractor.”

It ended by rejecting the tested local model deployments for the normal extraction responsibility.

The recorded evaluation found, among other failures:

- semantic false positives/omissions despite valid structured output;
- repeated instruction-shaped or deprecation-related errors;
- downstream decision effects from missed/incorrect claims;
- a second-model input-risk gate that added latency/failure dependency and false positives without establishing safety;
- phrase/regex controls that would encode fixture/category-shaped semantics rather than solve the real interpretation responsibility.

The plan records these dispositions:

- `gemma-4-e2b-it` — rejected for normal extraction;
- `qwen3-4b-instruct-2507` — rejected for normal extraction;
- mandatory second-model risk gate — rejected;
- phrase/regex semantic controls — rejected as product grounding;
- strict schema, quotation, provenance, authority, and decision limits — retained as valuable bounded controls.

### Why this is a high-value engineering result

A model experiment can succeed as an experiment by producing **credible rejection evidence**.

```text
interesting model behavior
+ valid JSON/schema
!= product adoption
```

The decision criterion was not “can a local model produce plausible output?” It was closer to:

```text
can this method satisfy the owning semantic responsibility
with acceptable error behavior, authority boundaries,
generality, decision effects, cost, and failure modes?
```

The answer for the tested deployments was no.

### Architecture lesson

UpgradePilot learned early that **structured output is not epistemic authority**.

This lesson survives the specific models, Pydantic schemas, LM Studio adapter, and evaluation scripts.

Those exact implementations remain historical; the trust distinction remains broadly useful.

---

## 7. What was retained from the semantic experiment

Rejecting model adoption did not mean discarding every mechanism.

The experiment produced reusable lessons about:

- raw evidence preservation;
- explicit source identity;
- attribution;
- quote/span grounding;
- transformation identity;
- deterministic mechanical validation around model output;
- explicit unresolved/rejected states;
- keeping model-derived authority visible;
- preventing a model-derived claim from independently creating a favorable final recommendation;
- evaluating downstream decision effects rather than only extraction accuracy.

The existing `learning/m2-s02/` package preserves the detailed frozen experiment and should be used when deeper study is needed.

This Group 3 note deliberately does not reproduce its model-by-model evaluations or every historical type/test.

---

## 8. M2-S03: the report-first vertical slice was coherent but too narrow

After the semantic-extraction experiment closed, the old route moved toward an evidence-to-report slice.

Its intended responsibility was approximately:

```text
supplied/replayed case + evidence
→ deterministic decision
→ machine-readable report
→ human-readable report
```

Useful ideas in that orientation included:

- strict case/evidence contracts;
- explicit missing/rejected states;
- deterministic decision authority;
- separation between application state, machine output, and human rendering;
- provenance-backed report statements;
- no-model operation;
- changed/missing/invalid/security-boundary testing.

Those are not bad ideas. The problem was **scope and sequencing**.

### Why the route became superseded

Real product-simulation cases exposed additional runtime responsibilities that the report-first route omitted or deferred too casually:

- invocation separate from discovered/frozen identity;
- material operation/acquisition history;
- raw/reference preservation;
- richer evidence states and authority;
- observations vs interpretations vs findings;
- supersession;
- transparent-baseline comparison;
- complete decision transitions;
- follow-up, rerun, replay, and new-run boundaries;
- review / Ali acceptance / external confirmation / capability state;
- conditional responsibilities such as causal failure attribution.

The historical M2-S03 plan therefore now says explicitly that it is **superseded and not resumable as written**.

### The architecture mistake to avoid learning

Do **not** summarize this as:

```text
reports are unimportant
```

The actual lesson is:

```text
reporting is a downstream representation responsibility
!= the entire first executable product responsibility
```

If the upstream state/evidence/transition model is incomplete, building a polished report layer first can make the wrong boundaries feel permanent.

---

## 9. Product simulation changed the implementation question

S001–S005 did more than add test cases. They changed what the first credible runtime had to represent.

The accepted D1 synthesis required a minimum responsibility capable of preserving, among other things:

- stable run identity distinct from invocation;
- exact repository/PR/base/head/dependency/version identity;
- material operation and evidence states;
- observation → interpretation → finding lineage;
- a transparent baseline;
- conditional responsibility activation;
- bounded action or abstention with limitations;
- machine and human outputs from the same accepted state;
- follow-up/rerun/supersession boundaries;
- structural identity/lineage validation;
- review/assistance/ownership state.

D1 also separated:

```text
strong deterministic candidates
from
interpretive/tool-assisted responsibilities
from
human-controlled authority
```

This meant the implementation question was no longer:

> How do we finish the next report-oriented M2 step?

It became:

> What is the smallest complete executable responsibility justified by the real product evidence, and which old mechanisms — if any — still belong after re-evaluation?

That is the B1 responsibility-freeze question.

---

## 10. The clean-slate reset: preserve evidence, remove inherited authority

ADR-0003 made a deliberately strong move before B2 implementation expanded.

The active product source was reset to a minimal package skeleton while the exact pre-reset implementation was preserved at immutable commit:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

The archive manifest records the removed M2 modules, tests, scripts, dependencies, and generated evaluation outputs.

### What the reset did

It removed from the **active product path** the M2-era implementation and its tests/dependencies so that B2 could not accidentally inherit:

- old class boundaries;
- old module names;
- Pydantic by default;
- OpenAI/model dependencies by default;
- old decision rules;
- old report-first sequencing;
- historical tests as if they were current coverage.

At the same time, it preserved the old implementation exactly through Git and an archive manifest.

So the reset was not deletion of history. It was a change in **authority**:

```text
old source/tests
BEFORE RESET:
active implementation evidence for the then-current M2 responsibility

old source/tests
AFTER RESET:
historical comparison/learning evidence only
```

### The non-reuse rule

ADR-0003 states that an archived mechanism may be inspected later only when a current responsibility names the need.

Then the behavior must be re-derived from current specifications/case evidence and implemented without automatically restoring the old module.

Similarity is allowed when independently justified.

Inheritance is not.

---

## 11. Why this reset was not ordinary “rewrite from scratch” dogma

Starting over is often a poor engineering choice. UpgradePilot's reset was justified by a specific combination of conditions recorded in ADR-0003:

- the product responsibility had materially changed after D1;
- the old source encoded a narrower M2/report-first orientation;
- old tests could exert design pressure even when testing obsolete boundaries;
- old dependencies/method choices could become implicit architecture by inertia;
- much of the old implementation was AI-generated, and Ali explicitly wanted the new learning path to grow from the real current responsibility rather than reverse-engineering obsolete code;
- there were no stated external-user compatibility obligations requiring a migration layer.

The decision also accepted real costs:

- working old code/tests stopped counting as active proof;
- some concepts would need reimplementation;
- installation/test proof had to be re-established;
- potentially useful mechanisms could not simply be copied back.

This is why the correct transferable lesson is **not** “clean slate is better than refactoring.”

It is:

> **When the active implementation substantially encodes a superseded responsibility and there is no real compatibility obligation, preserving it as exact history while resetting active authority can be cleaner than allowing implementation inertia to choose the new architecture.**

That is a conditional engineering judgment, not a universal rule.

---

## 12. What remained accepted across the reset

A clean-slate reset did not reset the whole project.

It preserved upstream owners/evidence such as:

- the project Charter and product boundary;
- simulation evidence;
- accepted specifications;
- the outer Python package/source/test boundary from ADR-0001;
- historical plans/learning records as history;
- exact archived source through Git.

It specifically reset **active implementation-method inheritance**.

ADR-0002's Pydantic method became superseded, while ADR-0001's outer `src/upgradepilot/` layout remained accepted.

This is a useful example of selective supersession:

```text
new product evidence
→ invalidate one implementation-method decision
→ keep unrelated stable boundaries
```

A transition does not require declaring everything before it obsolete.

---

## 13. B1/B2 after the reset: responsibility first, implementation second

The controlling route now states the B1 responsibility in terms such as:

- smallest complete real user-visible responsibility;
- public read-only permission boundary;
- exact identity and evidence-authority requirements;
- clean active source boundary;
- simplest credible methods/dependencies;
- acceptance tests, claim limits, and stop lines;
- ownership-bearing work before B2.

And explicitly:

> **B1 must not inherit archived methods automatically.**

The broader B2 route is now a real public-PR vertical slice moving toward:

```text
public repository + PR locator
→ acquisition
→ exact identity
→ evidence
→ impact/applicability/investigation where activated
→ bounded recommendation or abstention
→ concise output + traceability
```

The first specimen may establish a walking path, but it must not become the entire method horizon.

This is structurally different from the earlier approach:

```text
EARLIER
known/manual inputs
→ narrow contracts / semantic experiment
→ report-oriented composition

B1/B2 RESET DIRECTION
accepted complete responsibility
→ re-admit only required methods
→ implement small increments
→ pressure-test central choices against real variation
```

---

## 14. Mistakes/corrections worth learning without overgeneralizing

### 14.1 Useful typed contracts can still be premature architecture

The M2 contracts were technically useful. The mistake would be assuming that because they were strict and tested, their exact shapes were therefore the correct B2 contracts.

```text
well-tested implementation
!= permanent domain ownership
```

### 14.2 Structured LLM output can still be semantically wrong

Schema validation and source quotation helped constrain output, but they did not eliminate semantic mistakes or prove source truth.

```text
syntactically valid
+ source-grounded
!= semantically correct / corroborated / safe to decide from
```

### 14.3 Security-looking machinery can add risk without earning authority

The second-model input-risk gate sounded defensive, but evaluation showed false positives, latency, and another failure dependency without proving safety.

Controls must be evaluated by the risk/proposition they actually improve, not by how security-oriented they sound.

### 14.4 Report completeness can hide responsibility incompleteness

A complete machine/human report is only as good as the state/evidence model feeding it.

Product simulation showed that runtime identity, evidence states, transitions, conditional stages, and review boundaries had to be first-class before report shape could define the implementation center.

### 14.5 Existing tests can become inertia

Tests prove behavior of the implementation they exercise. When the responsibility itself is superseded, retaining those tests as active requirements can silently preserve the wrong architecture.

Historical tests remain evidence; they stop being current acceptance authority unless the new responsibility independently re-admits the behavior.

---

## 15. Current fact, evidenced rationale, and engineering judgment

### Current fact

- ADR-0001 remains accepted for the outer Python `src/upgradepilot/` boundary.
- ADR-0002 is superseded.
- ADR-0003 controls the clean-slate B2 reset/non-reuse boundary.
- the M2-S03 plan is superseded and explicitly not resumable as written.
- `learning/m2-s02/` and `learning/m2-s03/` are historical learning snapshots, not current implementation owners.
- the exact pre-reset implementation is retained at `e7425dc...` and indexed by the archive manifest.

### Evidenced rationale

The controlling records explicitly tie the reset to:

- D1 exposing a different, more complete first runtime responsibility;
- preventing obsolete M2 classes/tests/method choices from becoming implicit B2 design;
- preserving learning clarity and avoiding forced reverse-engineering of substantially AI-generated obsolete implementation;
- retaining historical evidence exactly while rebuilding current behavior from accepted responsibilities.

### Engineering judgment

The reset was proportionate because the project was still pre-production, had no stated external compatibility contract requiring migration, and the implementation center had materially changed.

In a mature deployed system with public API/storage/schema compatibility obligations, an equivalent clean reset could be irresponsible. Migration constraints would become first-class evidence.

---

## 16. What Group 3 does not claim

This note does not establish that:

- Pydantic is a bad choice for UpgradePilot today;
- LLM semantic extraction is permanently rejected;
- the old M2 source was low quality;
- reports are unimportant;
- clean-slate rewrites are generally preferable;
- all old mechanisms were removed forever;
- the current B2 implementation equals the D1 candidate exactly;
- historical passing tests prove current product behavior;
- current B2 source details are covered here.

Later groups teach the reimplemented B2 mechanisms and current source/test flows.

---

## 17. What to master vs what to look up

### Must master / own

Be able to explain:

1. why a stable package boundary did not require pre-creating the final architecture;
2. why M2-S01 separated raw/manual input from trusted internal concepts;
3. the difference between raw text, model output, grounded attributed claim, corroborated meaning, and decision authority;
4. why a negative model-adoption result can be a successful engineering experiment;
5. why report generation was a real responsibility but an insufficient center for the first complete runtime;
6. why tested old code and tests were demoted to historical evidence rather than allowed to control B2 by inheritance;
7. why ADR-0002 could be superseded while ADR-0001 remained valid;
8. when a clean-slate authority reset is justified versus when migration/compatibility would make it unsafe.

### Understand operationally

- the M2-S01 `ManualCaseInput → InitialCaseRecord` transformation;
- the M2-S02 candidate → grounding → attributed decision-claim boundary;
- the major model-evaluation failure classes;
- the D1 minimum-runtime expansion;
- the archive/non-reuse mechanism.

### Lookup-level

- exact Pydantic validators/models;
- LM Studio/provider details;
- historical model names and score counts;
- every M2 test/script/evaluation output;
- exact M2-S03 report schema.

### Deliberately deferred

- current dependency/version/upstream implementation — Group 4;
- current target environment and uv reasoning — Groups 5–6;
- artifact serviceability — Group 7;
- current CI evidence implementation — Group 8;
- current impact/applicability/investigation source — Group 9;
- current full application composition — Group 10;
- broader architecture/proof retrospective — Group 11;
- later B2/X1 agentic experimentation — Group 12.

---

## 18. Fast relearning route

1. Read Sections **1, 6, 8, and 10** to recover the main transition.
2. Inspect historical `case_identity.py` only if you need a concrete trusted-contract example.
3. Inspect historical `extraction.py` plus `learning/m2-s02/README.md` if the model-authority boundary is fuzzy.
4. Compare the superseded M2-S03 plan with D1's minimum runtime responsibility.
5. Re-read ADR-0003 and explain why the archive preserves evidence while removing implementation authority.

---

## 19. Transfer questions

1. If an old module has excellent tests, what additional evidence would you need before declaring its exact abstraction part of a new responsibility?
2. Why does a mechanically grounded LLM claim still retain `model_derived` authority?
3. What made the M2-S02 rejection stronger than simply saying “the models were not good enough”?
4. Which missing responsibilities made report-first sequencing inadequate?
5. Why was deleting historical evidence unnecessary for a clean active reset?
6. Give one scenario where UpgradePilot's 2026-07-23 clean reset logic would **not** be safe to copy into another project.

---

## 20. Primary evidence anchors

Current/historical decision owners:

- [`ADR-0001 — Initial Python Source Layout`](../docs/architecture/ADR-0001-initial-python-source-layout.md)
- [`ADR-0002 — Pydantic for Runtime Contract Models`](../docs/architecture/ADR-0002-pydantic-runtime-contract-models.md)
- [`ADR-0003 — Clean-Slate B2 Source Reset`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)
- [`UpgradePilot Evidence-Derived Learning and Building Plan`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)

Historical M2 plans:

- [`M2-S01 — Initial Trusted Case`](../plans/M2_S01_INITIAL_TRUSTED_CASE_PLAN.md)
- [`M2-S02 — Known-Text Semantic Extraction`](../plans/M2_S02_KNOWN_TEXT_SEMANTIC_EXTRACTION_PLAN.md)
- [`M2-S03 — Evidence-to-Report Vertical Slice`](../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md)

Transition evidence:

- [`D1 Final Synthesis and B1 Entry`](../product-simulation/D1_FINAL_SYNTHESIS_AND_B1_ENTRY.md)
- [`Pre-B2 M2 Implementation Archive`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

Existing frozen learning material reused by reference:

- [`learning/m2-s02/`](m2-s02/README.md) — detailed semantic-extraction/model-evaluation snapshot;
- [`learning/m2-s03/`](m2-s03/README.md) — superseded report-first learning orientation.

Historical code anchors at exact immutable snapshot `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`:

- `src/upgradepilot/case_identity.py`
- `src/upgradepilot/extraction.py`
- archive-listed related tests/scripts/evaluation outputs.

No new bounded Audit was required for Group 3: the current ADRs, superseded plans, archive record, D1 synthesis, and frozen learning snapshots give a coherent, explicit account of the transition and its rationale.