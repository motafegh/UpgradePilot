# Group 3 — Early Implementation, M2 Experiments, and the Clean-Slate B2 Reset

**Learning-artifact date:** 2026-09-02  
**Evidence horizon:** `main@5eeb350fba2046c1c54f337a944bd2460fda2a57`  
**Historical code snapshot used where implementation detail matters:** `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`  
**Roadmap responsibility:** Group 3 from `../plans/UPGRADEPILOT_WHOLE_PROJECT_LEARNING_ARTIFACT_ROADMAP_PLAN.md`  
**Artifact role:** transition learning snapshot from early Python/M2 implementation through the B1/B2 clean-slate reset  
**Target depth:** implementation-adjacent; **must own the architecture/authority lesson**, understand representative historical mechanisms operationally, and treat obsolete source details as lookup-level

This note answers one question:

> **What did UpgradePilot build and learn before B2, and why did the project preserve that work as evidence while refusing to let it become the new B2 architecture by inheritance?**

The early work was not simply “wrong.” Several mechanisms were useful. The important transition was from **a narrow first implementation around known/manual inputs and reporting** to **an implementation responsibility derived from the fuller product evidence exposed by simulation**.

---

## 1. The transition in one view

```text
ADR-0001: small real Python package boundary
        ↓
M2-S01: trusted manual case transformation
        ↓
M2-S02: bounded semantic-extraction/model experiment
        ↓
valuable trust controls retained
but tested local models rejected for normal extraction
        ↓
M2-S03: evidence-to-report orientation
        ↓
S001–S005 expose a wider runtime responsibility
        ↓
D1 freezes a different minimum credible responsibility
        ↓
ADR-0003: preserve M2 exactly, reset active implementation authority
        ↓
B1/B2: re-derive methods from current responsibility/evidence
```

Keep three evidence roles separate:

1. **historical implementation evidence** — what M2 source/tests demonstrated;
2. **historical learning/design evidence** — what its experiments/plans taught;
3. **current controlling semantics/implementation** — later specifications, ADRs, plans, active source/tests, and observed evidence.

---

## 2. ADR-0001: enough structure to build, not enough to prejudge architecture

ADR-0001 established:

```text
repository: UpgradePilot
package/distribution: upgradepilot
source root: src/upgradepilot/
test root: tests/
```

It deliberately paired a professional installed-package boundary with a refusal to pre-create speculative internal layers such as `domain/`, `services/`, or `infrastructure/`.

The reusable lesson is:

```text
stable outer package boundary
+ smallest current responsibility
→ sufficient initial structure

later repeated responsibility evidence
→ may justify more internal structure
```

**Real responsibility earns architecture.**

ADR-0001 selected the layout; editable-install/import commands and tests were the implementation proof. The ADR itself did not prove the package worked.

---

## 3. M2-S01: raw/manual input was not the trusted domain state

M2-S01 accepted an eight-field manually assembled dependency-update case:

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

and produced distinct trusted concepts:

```text
PullRequestSnapshotIdentity
+
DependencyChange
+
ChangedFileEvidence
→ InitialCaseRecord
```

At historical snapshot `e7425dc...`, `case_identity.py` used strict frozen Pydantic v2 models. Representative behavior included:

- `owner/name` repository validation;
- positive PR number;
- exact 40-character hexadecimal SHAs normalized to lowercase;
- non-empty dependency/version values with old/new required to differ;
- non-empty unique changed paths;
- explicit flat-input → nested-record assembly.

The important engineering separation was:

```text
incoming adapter shape
→ validate / normalize
→ exact PR identity
→ dependency transition
→ changed-file evidence
→ trusted aggregate
```

This exposed useful concepts early: adapter shape vs domain concepts, identity vs change vs evidence, normalization vs interpretation, mutable caller data vs frozen trusted state, and validation failure vs partial trusted output.

### Proof/non-proof boundary

M2-S01 proved a bounded trusted transformation from supplied facts. It did **not** prove live acquisition, source authority, semantic upstream interpretation, CI authority, target applicability, complete decision semantics, or final B2 contract shapes.

---

## 4. ADR-0002: a justified method can later lose controlling authority

M2 selected Pydantic v2 for runtime contracts because it provided useful strict validation, frozen typed models, structured errors, explicit adapters, and machine-readable serialization.

That method was reasonable for the then-active responsibility. ADR-0002 is nevertheless now **superseded**.

```text
accepted implementation method for responsibility R1
!=
automatically accepted method for later responsibility R2
```

Working source/tests create implementation evidence; they do not grant a dependency or framework permanent architectural authority. When the owning responsibility changed, Pydantic had to become a fresh candidate rather than an inherited requirement.

This does **not** mean Pydantic was rejected as a technology.

---

## 5. M2-S02: semantic extraction exposed the model-authority problem

The next responsibility was genuinely semantic: derive structured meaning from known release-note text without collapsing source text, model interpretation, and truth.

The intended bounded flow was:

```text
known source text
→ candidate model extraction
→ deterministic schema/mechanical validation
→ mechanically grounded attributed claim
→ deterministic decision input
```

The key trust ladder was:

```text
raw source text
!= untrusted model output
!= mechanically grounded claim
!= independently corroborated fact
!= final decision
```

### Representative historical contracts

At `e7425dc...`, `extraction.py` distinguished:

- `CandidatePythonSupportClaim` — untrusted claim proposed by an extractor;
- `CandidateExtractionResult` — untrusted structured extraction output;
- `GroundedPythonSupportClaim` — claim passing mechanical grounding controls;
- `ExtractionResult` — grounded claims plus unresolved/validation-error state;
- `PythonSupportCandidateExtractor` — provider protocol;
- `PythonSupportExtractionService` — orchestration around extractor + deterministic validation.

A grounded claim retained source/evidence and transformation identity, including:

```text
evidence_id
source_quote
extractor_id
authority = model_derived
```

and preserved `model_derived` authority when converted into the decision contract.

That distinction is central:

> **Grounding can prove that an interpretation is tied to supplied source material; it does not turn model interpretation into independent truth.**

---

## 6. M2-S02’s most important output was a negative adoption result

The experiment did **not** close by adopting an LLM extractor into the normal product path.

The recorded evaluation rejected both tested local deployments for normal extraction:

- `gemma-4-e2b-it`;
- `qwen3-4b-instruct-2507`.

It also rejected:

- a mandatory second-model input-risk gate;
- instruction/category phrase or regex controls as product semantic grounding.

The decisive problems included semantic false positives/omissions despite valid structured output, instruction/deprecation errors with downstream decision effects, and extra detector complexity/false positives without established safety.

What *was* retained as valuable bounded control included strict schema, quotation/source grounding, provenance/transformation identity, explicit authority, unresolved/rejected states, and decision-effect limits.

### Why rejection counts as successful engineering

```text
plausible model output
+ valid schema
!= product adoption
```

The experiment asked whether the method could satisfy the **owning semantic responsibility** with acceptable error behavior, authority boundaries, generality, decision effects, cost, and failure characteristics.

At the tested boundary, the evidence said no.

That is stronger than vague dissatisfaction: it is an evidence-backed method disposition.

### Transfer lesson

**Structured output is not epistemic authority.** A model experiment may create high-value knowledge by proving that a candidate method should not be adopted yet.

For the detailed frozen model/evaluation path, reuse [`learning/m2-s02/`](m2-s02/README.md) rather than expanding this note.

---

## 7. M2-S03: report composition was real work, but the wrong center

The next historical orientation was roughly:

```text
supplied/replayed case + evidence
→ deterministic decision
→ machine-readable report
→ human-readable report
```

It contained useful candidate mechanisms:

- strict case/evidence contracts;
- explicit missing/rejected states;
- deterministic decision authority;
- separation of application state, machine output, and human rendering;
- provenance-backed report statements;
- no-model operation;
- changed/missing/invalid/security-boundary tests.

The problem was not that reports were useless. The problem was that the **report-first slice omitted or postponed too much upstream runtime responsibility**.

S001–S003 exposed missing needs such as:

- invocation vs discovered/frozen identity;
- operation/acquisition history;
- raw/reference preservation;
- richer evidence state/authority;
- observations vs interpretations vs findings and supersession;
- transparent-baseline comparison;
- decision transitions;
- follow-up/rerun/new-run boundaries;
- review/external-confirmation/ownership state;
- conditional investigations such as failure attribution.

The M2-S03 plan therefore now explicitly says it is **superseded and not resumable as written**.

The durable lesson is:

```text
reporting = downstream representation responsibility
!= complete first runtime responsibility
```

A polished output layer can make incomplete upstream state boundaries appear more settled than they really are.

For historical detail, reuse [`learning/m2-s03/`](m2-s03/README.md).

---

## 8. D1 changed the implementation question

S001–S005 were not merely additional examples. Their contrast evidence changed the minimum credible runtime responsibility.

The accepted D1 synthesis required, among other things:

- run identity distinct from invocation;
- exact repository/PR/base/head/dependency/version identity;
- operation and evidence states with provenance;
- observation → interpretation → finding lineage;
- transparent baseline comparison;
- conditional responsibility activation/non-activation;
- bounded action or abstention with limitations;
- machine/human outputs from shared accepted state;
- follow-up/rerun/supersession boundaries;
- structural identity/lineage validation;
- review/assistance/ownership state.

D1 also distinguished deterministic candidates, interpretive/tool-assisted responsibilities, and human-controlled authority.

So the B1 question was no longer:

> How do we finish M2-S03?

It became:

> **What is the smallest complete executable responsibility justified by the product evidence, and which earlier mechanisms still belong after explicit re-evaluation?**

This is the responsibility-freeze transition.

---

## 9. ADR-0003: preserve historical evidence, reset active implementation authority

ADR-0003 responded by resetting active product source/tests to a clean package baseline while preserving the exact pre-reset implementation at immutable commit:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

The archive manifest records the historical M2 modules, tests, scripts, dependencies, and generated evaluation outputs.

The reset prevented automatic B2 inheritance of:

- old class/module boundaries;
- Pydantic and model/provider dependencies by default;
- old decision rules;
- report-first sequencing;
- historical tests as current acceptance authority.

The key change was therefore **authority**, not historical availability:

```text
before reset:
M2 source/tests = active implementation evidence

post reset:
M2 source/tests = historical comparison/learning evidence
```

### Non-reuse rule

A later current responsibility may inspect a specific archived mechanism, but must re-derive the needed behavior from current specifications/case evidence. Similarity to the old implementation is allowed when independently justified; copying/restoring it by inheritance is not.

---

## 10. Why this clean reset was justified here — and is not a universal rewrite rule

The recorded decision was unusually strong because several conditions aligned:

- D1 materially changed the product responsibility;
- M2 encoded a narrower manual/report-first implementation center;
- old tests/classes/dependencies could create design inertia;
- much of the implementation was AI-generated, and Ali explicitly wanted the new learning path to grow from the real current responsibility rather than reverse-engineering obsolete code;
- no recorded external-user compatibility obligation required an active migration layer.

The reset also accepted costs:

- previously passing tests stopped counting as active proof;
- useful concepts might need reimplementation;
- package/test proof had to be established again;
- archived code could not simply be copied back for convenience.

The transferable lesson is conditional:

> **When an implementation materially encodes a superseded responsibility and no real compatibility obligation requires migration, preserving it exactly as history while resetting active authority can be cleaner than allowing implementation inertia to choose the next architecture.**

In a deployed system with public API/schema/storage compatibility obligations, the same approach could be irresponsible; migration constraints would become first-class requirements.

---

## 11. Selective supersession: not everything was reset

ADR-0003 did not invalidate the whole project.

Still retained were the Charter/product boundary, simulation evidence, specifications, historical records, exact Git history, and ADR-0001’s outer `src/upgradepilot/` package/test boundary.

What lost automatic controlling authority was the M2 implementation method.

So:

```text
ADR-0001 outer package boundary → remains accepted
ADR-0002 Pydantic method       → superseded
M2 source/tests                → historical evidence
M2-S03 report-first plan       → superseded
```

This is a useful architecture concept: **supersession should follow responsibility boundaries**, not turn every nearby historical decision into collateral damage.

---

## 12. B1/B2 after the reset: responsibility first, implementation second

The controlling route defines B1 around:

- smallest complete real user-visible responsibility;
- public read-only permission boundary;
- exact identity/evidence-authority requirements;
- clean active source;
- simplest credible methods/dependencies;
- acceptance tests, claim limits, and stop lines;
- ownership-bearing work.

It states explicitly:

> **B1 must not inherit archived methods automatically.**

The broader B2 horizon then moves from a public repository/PR locator through acquisition, exact identity, evidence-backed reasoning, conditional impact/applicability/investigation, and bounded recommendation/abstention to concise traceable output.

The first case can establish a walking path, but not define the whole method horizon.

That gives the core transition:

```text
EARLY M2
known/manual inputs
→ bounded contracts and semantic experiment
→ report-oriented composition

B1/B2
accepted complete responsibility
→ admit only justified methods
→ implement in small testable increments
→ pressure-test central choices against real variation
```

---

## 13. Five engineering corrections worth retaining

### 13.1 Tested types are not permanent domain ownership

A strict, well-tested class can still belong to a superseded responsibility.

```text
well-tested implementation
!= permanent architecture
```

### 13.2 Grounded structured model output can still be semantically wrong

```text
schema-valid + source-grounded
!= semantically correct
!= independently corroborated
!= authorized final decision
```

### 13.3 Defensive-looking machinery must earn its risk reduction

The second-model gate added latency/failure dependency and false positives without establishing safety. Security-oriented appearance is not evidence of useful control.

### 13.4 Report completeness cannot substitute for runtime-responsibility completeness

Outputs are downstream projections. Their quality cannot repair missing identity, evidence, transition, or conditional-investigation state.

### 13.5 Tests can become architecture inertia

Tests prove the behavior they exercise. Once the owning responsibility is superseded, keeping those tests as active acceptance requirements can silently preserve the old architecture. Historical tests remain evidence until a new responsibility independently re-admits their behavior.

---

## 14. Current facts, rationale, and judgment

### Current facts at this artifact horizon

- ADR-0001 remains accepted for the outer Python package boundary.
- ADR-0002 is superseded.
- ADR-0003 controls the clean-slate B2 reset/non-reuse boundary.
- M2-S03 is superseded and explicitly not resumable as written.
- `learning/m2-s02/` and `learning/m2-s03/` are historical snapshots.
- pre-reset implementation is preserved at `e7425dc...` and indexed by the archive manifest.

### Evidenced rationale

The controlling records explicitly tie the reset to D1’s broader runtime responsibility, avoidance of obsolete source/test/method inheritance, exact preservation of history, and learning clarity around substantially AI-generated prior implementation.

### Engineering judgment

The reset was proportionate in this pre-production context because no recorded compatibility contract demanded migration and the implementation center had materially changed. That judgment should not be copied blindly into a mature product.

---

## 15. What Group 3 does not claim

This note does not establish that:

- Pydantic is a bad current choice;
- LLM semantic extraction is permanently rejected;
- M2 source quality was poor;
- reports are unimportant;
- clean-slate rewrites are generally preferable;
- all old mechanisms were permanently discarded;
- historical passing tests prove current behavior;
- current B2 source details are covered here.

Later groups cover the reimplemented/current responsibilities.

---

## 16. Learning depth

### Must master / own

Be able to explain:

1. why ADR-0001 established a real package boundary without pre-designing internal architecture;
2. why M2-S01 separated manual/raw adapter input from trusted domain concepts;
3. raw text vs model output vs grounded attributed claim vs corroborated fact vs decision authority;
4. why M2-S02’s rejection was a successful engineering result;
5. why report generation was real but insufficient as the first runtime center;
6. why old source/tests were preserved but demoted from active authority;
7. why ADR-0002 could be superseded while ADR-0001 remained valid;
8. when clean-slate authority reset is justified versus when migration compatibility must dominate.

### Understand operationally

- `ManualCaseInput → InitialCaseRecord`;
- candidate extraction → mechanical grounding → attributed decision claim;
- major M2-S02 failure/disposition classes;
- D1’s expanded minimum responsibility;
- archive + non-reuse mechanics.

### Lookup-level

- exact Pydantic validators/types;
- model/provider/LM Studio details;
- historical score counts;
- individual M2 tests/scripts/evaluation outputs;
- exact M2-S03 report schema.

### Deferred deliberately

- dependency/version/upstream mechanics — Group 4;
- target/uv environment reasoning — Groups 5–6;
- artifact serviceability — Group 7;
- CI evidence — Group 8;
- current impact/applicability/investigation — Group 9;
- current end-to-end application composition — Group 10;
- broader architecture/proof retrospective — Group 11;
- later B2/X1 agentic experiments — Group 12.

---

## 17. Fast relearning route

1. Read Sections **1, 6, 7, and 9**.
2. Inspect historical `case_identity.py` only for the concrete trusted-contract example.
3. Inspect historical `extraction.py` plus [`learning/m2-s02/README.md`](m2-s02/README.md) for the model-authority boundary.
4. Compare the superseded M2-S03 plan with D1’s minimum runtime responsibility.
5. Re-read ADR-0003 and explain how preserving evidence differs from preserving implementation authority.

### Transfer questions

1. If an old module has excellent tests, what else must be established before its abstraction is admitted into a new responsibility?
2. Why does a mechanically grounded claim still retain `model_derived` authority?
3. What made M2-S02’s rejection stronger than “the models were not good enough”?
4. Which missing responsibilities made report-first sequencing inadequate?
5. Give one type of project where this clean-reset decision would be unsafe without a migration plan.

---

## 18. Primary evidence anchors

Decision/method owners:

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

Frozen learning material reused by reference:

- [`learning/m2-s02/`](m2-s02/README.md)
- [`learning/m2-s03/`](m2-s03/README.md)

Historical implementation anchors at immutable snapshot `e7425dcfc20f093ac10c9a903f1c4ae50a8b2638`:

- `src/upgradepilot/case_identity.py`
- `src/upgradepilot/extraction.py`
- archive-listed related tests/scripts/evaluation outputs.

No new bounded Audit was required: the ADRs, superseded plans, archive record, D1 synthesis, and frozen learning snapshots provide a coherent and explicit rationale/evidence trail for this transition.