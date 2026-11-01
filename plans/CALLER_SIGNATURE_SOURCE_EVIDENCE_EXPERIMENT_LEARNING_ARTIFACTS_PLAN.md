# Caller/signature source-evidence experiment learning-artifacts plan

**Plan responsibility:** preserve the caller/signature → source acquisition/correspondence → ordinary PR → blocker-resolution → bounded-transfer experiment program as a small, complete, commit-pinned learning package that Ali can later use to relearn, review, diagnose, modify and defend the engineering work.

**Planning branch:** `learning/caller-signature-source-evidence-artifacts-2026-11-01`

**Branch base:** `e7082e96df98d014a44d58637e985af7d3c9175c` (latest `main` when this plan was created).

**Frozen experiment learning horizon:** `c53430c6e3fb4f24147a28aa642ab94834233243`.

The branch base and the learning horizon intentionally differ. The branch starts from the current repository so governance and learning-package layout are current. The learning artifacts themselves explain the completed experiment program as it existed at the frozen experiment horizon. Later native/productization implementation must not be silently imported into this snapshot.

**Artifact status:** planning artifact prepared for review. It owns the learning-package coverage, authoring sequence, completion ledger and quality gates. It does not own UpgradePilot's live product position, does not prove learner mastery and does not authorize product/source/test repair.

`MEMORY.md` remains the sole live project-position owner. Checkbox state in this plan records only completion of this learning-artifact responsibility.

**Procedural owners:**

- `plans/README.md` — plan responsibility, position neutrality and stop-line rules;
- `.agents/skills/upgradepilot-learning-artifact/SKILL.md` — evidence-grounded learning-artifact authoring procedure;
- `learning/README.md` — snapshot, package, depth, maintenance and derived-transform policy;
- `.agents/skills/upgradepilot-planning-design/SKILL.md` — this plan's scoping/decomposition/proof method;
- applicable source/tests/plans/design/evidence/working-memory at the pinned horizon — implementation and historical evidence;
- accepted specifications/ADRs — only where stable product/architecture semantics materially explain an experiment boundary.

`UP-SKILL:upgradepilot-planning-design`

---

## 1. Outcome and completion standard

The package is complete when a technically competent reader who has not followed the October experiment sessions can use the notes to reconstruct and reason about all of the following without relying on chat history:

1. **Why the experiment program existed** — missing evidence, incorrect interpretation, correspondence and stronger runtime applicability are different failure classes.
2. **How deterministic caller/signature evidence works** — source facts, scoped bindings, argument shape, declared signatures, receiver assumptions, local comparison outcomes and unresolved premises.
3. **How curated proof became ordinary PR-driven evidence** — one PR/dependency observation horizon, exact old/proposed source acquisition, target-rooted correspondence, re-exports, initializers and bounded protocol/factory paths.
4. **How real fresh attempts drove engineering** — acquisition starvation, transient provider failures, stale priority, unsupported source relationships, retry-policy design, serialization/capacity failures and owner-specific repairs.
5. **How resource/capacity pressure changed the architecture** — source-first retention, whole-file partial analysis, explicit work admission, lossless representation and the invariant that unexamined evidence is not absent evidence.
6. **How transfer was qualified** — development cases versus untouched transfer cases, anti-cherry-picking case selection, method contamination, freezing and what an unchanged-method success does and does not establish.
7. **What the final experimental claim actually is** — bounded transfer of a source/caller-signature evidence method, not installed-environment proof, runtime dispatch, semantic compatibility, action authority, general Python correctness or product adoption.
8. **How to diagnose a changed future case** — identify whether the earliest sufficient owner is acquisition, source retention, binding/correspondence, local checking, representation/work admission, transport policy or a separately owned runtime/product responsibility.

The package must teach engineering ownership, not source memorization. It should leave Ali able to explain, inspect, challenge and modify the mechanisms with support from the named source/test anchors.

---

## 2. Scope and exclusions

### In scope

The package covers the coherent caller/signature source-evidence experiment program beginning with the source-versus-interpretation investigation and ending at the final bounded transfer proof before native productization.

Material subjects include:

- retained-source qualification and the original explanation gap;
- `api_python_bindings.py` scoped origin/binding model;
- `api_call_signature.py` source facts and local binder;
- the `inspect.Signature.bind` qualification/correction lesson;
- curated HTTPX and pytest/glyphsLib qualification;
- shared PR/dependency input horizon;
- exact dependency-source acquisition and constraint-selected samples;
- source correspondence and target-rooted discovery;
- direct/re-export/initializer candidate families;
- protocol/factory candidate family;
- ordinary retained results and fixed offline opening;
- staged acquisition policy and source-starvation controls;
- first fresh ordinary PR result;
- successor blocker-resolution attempts and repairs through the first useful ordinary paired-source result;
- later direct-use/transfer qualification pressure;
- capacity/representation/partial-analysis engineering;
- method freeze, case-selection discipline and untouched transfer proof;
- experiment proof classes, immutability, no-regrade discipline and explicit non-claims.

### Explicitly out of scope

- current native caller/signature productization implementation after the frozen horizon;
- a new tutorial for the entire UpgradePilot product;
- unrelated Investigator, LangGraph, CI, Workspace or report experiments except where one directly supplies a design lesson or boundary for this program;
- semantic/model interpretation as a complete separate learning package;
- installed-environment reconstruction, runtime dispatch solving or whole Python semantics;
- re-running historical experiments merely to write the notes;
- repairing experiment/product code while authoring learning material;
- claiming that reading these artifacts demonstrates mastery;
- permanent quiz/audio/flashcard derivatives by default.

If a later productization fact is useful for comparison, it may be mentioned only in a clearly labelled **later consequence / outside snapshot** note and must not be used as proof for the frozen experiment mechanism.

---

## 3. Snapshot and evidence-integrity contract

All substantive implementation, test, plan, working-memory and evidence claims used to explain the experiment must be read at:

`c53430c6e3fb4f24147a28aa642ab94834233243`

unless a note intentionally compares another horizon and labels that comparison explicitly.

### Required snapshot rules

- Never link a mutable `main` source path and present it as the frozen implementation.
- Prefer commit-pinned GitHub links or repository-relative paths plus the pinned commit.
- Preserve historical attempt/result identities and outcomes; do not refresh them using current methods.
- A later fixed reader opening an old bundle is evidence of compatibility/readability only, not re-execution or regrading.
- Diagnostic computations used historically must remain diagnostics; do not promote them into admitted attempt results.
- Historical `S00x` attempt names may appear for provenance, but semantic descriptions should be the active learning vocabulary.
- Distinguish controlled fixtures, retained real-source component proof, fresh real-provider attempts and untouched transfer evidence.

### Required evidence roles

Every material claim in a note should be traceable to the smallest sufficient combination of:

- canonical owner / accepted design owner where applicable;
- pinned implementation source;
- pinned focused tests;
- retained public-safe review/verification evidence;
- directly relevant working-memory progression when it explains the correction or decision;
- real case/source flow.

Working-memory explains how and why understanding evolved. It does not override source/tests or accepted semantic owners.

---

## 4. Package topology

Target package:

`learning/2026-11-01-caller-signature-source-evidence-experiments/`

The package contains one navigation file and five substantive learning artifacts.

| File | Learning responsibility | Primary real substrate |
| --- | --- | --- |
| `README.md` | Snapshot/authority map, package reading order, depth map and fast package re-entry | Entire program |
| `01_deterministic_caller_signature_evidence_and_proof_boundaries.md` | Why source facts, correspondence and applicability must be separated; scoped bindings; call/signature extraction; binder semantics; curated proof | HTTPX + retained Starlette/FastAPI; focused binder controls |
| `02_ordinary_pr_source_acquisition_correspondence_and_protocol_paths.md` | How selected source pairs became PR-driven automatic evidence; source roles, exact/sample distinction, re-export/initializer/protocol paths and offline retention | controlled ordinary PR + HTTPX + glyphsLib/pytest |
| `03_failure_driven_blocker_resolution_and_experimental_engineering.md` | How fresh ordinary acquisition failures were diagnosed, repaired at the earliest sufficient owner and preserved without regrade | first fresh HTTPX PR and successor blocker-resolution attempts through useful paired evidence |
| `04_source_retention_partial_analysis_and_capacity_engineering.md` | Why retaining all source and analyzing all source are different; representation/capacity failures, measurement, source-first capture, partial whole-file admission and lossless structure | direct-use/capacity development cases, especially LifeLog-type pressure |
| `05_transfer_qualification_case_selection_and_final_proof_boundary.md` | Development evidence versus untouched transfer; eligibility, anti-cherry-picking, contamination, method freeze, final unchanged-method transfer and bounded claim | openDVP/LifeLog qualification pressure + final untouched Digimon-type transfer |

Five notes are justified because the underlying responsibilities are genuinely distinct. Combining blocker-resolution engineering with capacity/work-admission engineering would make one note too large and obscure two different diagnostic models. Combining transfer methodology with implementation mechanics would weaken the final proof lesson.

Do not create additional permanent files unless authoring demonstrates a distinct learning responsibility that cannot be studied coherently inside these five notes.

---

## 5. Package-wide learning depth

### Must master / own

The package must teach these deeply enough that Ali can later explain and defend them:

- evidence acquisition vs source retention vs source fact vs correspondence vs local comparison vs runtime applicability;
- established / conditional / unknown / unbound binding states;
- `bound` / `rejected` / `undetermined` local outcomes;
- receiver assumptions and remaining premises;
- exact old/proposed dependency-source roles vs constraint-selected sample roles;
- conditional source paths are candidates, not effective imports/dispatch;
- source correspondence is not runtime dispatch;
- `**kwargs` reception is not semantic acceptance or forwarding proof;
- complete retained evidence vs partial admitted analysis;
- unexamined / refused / missing / unavailable are not absence;
- local work budgets vs provider/account quota;
- source starvation and priority/allocation design;
- immutable attempts, successor methods and no historical regrade;
- earliest-sufficient-owner diagnosis;
- controlled proof vs retained-component proof vs fresh ordinary proof vs untouched transfer;
- development-case contamination and anti-cherry-picking selection;
- final claim and explicit non-claims.

### Understand operationally

Ali should be able to read and reason about:

- AST source spans and source identities;
- argument/parameter kinds and local slot binding;
- retained source catalogs;
- source acquisition runs and per-run caching;
- fixed saved formats/readers;
- source relationship steps and discovery gaps;
- analysis/resource limits;
- structural-token/serialization accounting;
- source-first retention;
- whole-file analysis admission;
- indexed/lossless binding-trace representation;
- transport receipts, retry histories and elapsed/body/request accounting;
- immutable attempt lifecycle and cold opening.

### Lookup-level

Do not turn these into memorization obligations:

- every dataclass field;
- every JSON key;
- every numerical hash/attempt UUID;
- every provider endpoint;
- every test helper name;
- exact implementation of Python `ast` traversal utilities;
- exact byte counts unless they explain a material resource decision.

### Deliberately deferred

- complete Python object/value flow;
- general MRO/descriptor/runtime resolution;
- actual installed environment reconstruction;
- semantic compatibility/behavioral execution;
- maintainer action authority;
- current native productization implementation.

---

## 6. Common authoring contract for every substantive note

Each note should adapt to its subject, but all five must make the following recoverable where applicable:

1. **Snapshot and responsibility** — what this note owns and does not own.
2. **Mental model** — one compact diagram/table that gives the reader the governing model before source detail.
3. **Real flow** — at least one actual UpgradePilot case traced end to end.
4. **Source walkthrough** — only the functions/types/fields needed to understand the responsibility.
5. **Failure/correction lesson** — material wrong assumption, failed approach or boundary correction that changed the engineering model.
6. **Why the selected design exists** — evidenced rationale, not retrospective invention.
7. **Credible alternatives/rejected shortcuts** — only when the historical evidence makes the trade-off useful.
8. **Trust and authority boundary** — what remains conditional or belongs to another owner.
9. **Tests/proof** — a small set of discriminating tests/evidence and exactly what they prove.
10. **Non-proof** — claims a reader must not infer from green tests or successful attempts.
11. **Depth calibration** — must-own / operational / lookup / deferred topics for this note.
12. **Fast relearning route** — 1–3 source/test/evidence anchors and the shortest useful return sequence.
13. **3–5 transfer questions** — prediction/diagnosis/modification questions, not trivia.

Do not mechanically repeat a template section when it contributes no learning value.

---

## 7. Artifact-specific coverage contracts

### Artifact 01 — deterministic caller/signature evidence and proof boundaries

**File:** `01_deterministic_caller_signature_evidence_and_proof_boundaries.md`

**Reader outcome:** Ali can explain why source text alone is insufficient, trace a Python call into source facts and a local signature comparison, distinguish local structural evidence from actual runtime applicability, and reason about the supported binder without treating it as Python execution.

#### Required coverage

- [ ] Original October explanation problem: missing evidence vs misinterpretation vs stronger runtime proposition.
- [ ] `BindingAssessment`: established, conditional, unknown, unbound.
- [ ] Binding traces are source observations, not execution histories.
- [ ] Reuse of existing keyword/import facts rather than building another analyzer.
- [ ] Exact AST spans and why line/expression identity is insufficient.
- [ ] Call argument representation: positional, starred, keywords, `**` expansion.
- [ ] Declared signature representation: parameter kinds, defaults, `*args`, `**kwargs`, decorators/class context.
- [ ] Receiver modes: `as_written`, `one_receiver_assumed`, `unresolved`.
- [ ] `bound`, `rejected`, `undetermined` and keyword-reception distinctions.
- [ ] Why definite local keyword rejection may survive other unresolved checks.
- [ ] Positional-only / default / `**kwargs` corner and the `inspect.Signature.bind` discrepancy.
- [ ] Why a convenient standard-library helper was rejected as the sole oracle.
- [ ] Curated HTTPX old/proposed `Client.__init__` contrast.
- [ ] Newer Starlette forwarding contrast and why absence of one mismatch is not whole compatibility.
- [ ] `cert` presence lesson: source fact vs deprecation/behavior meaning.
- [ ] Curated pairing/receiver/source version remain premises.
- [ ] Saved/offline result boundary and no re-analysis on opening.
- [ ] Focused tests and proof/non-proof.

#### Primary pinned implementation anchors

- `experiments/api_python_bindings.py`
- `experiments/api_call_signature.py`
- `experiments/api_signature_evidence.py`
- `experiments/api_call_signature_trial.py`
- `experiments/tests/test_api_python_bindings.py`
- `experiments/tests/test_api_call_signature.py`
- `experiments/tests/test_api_call_signature_trial.py`

#### Historical/evidence anchors to inspect before authoring

- [ ] `working-memory/2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md`
- [ ] `working-memory/2026-10-28_reusable-caller-signature-evidence_design-cycle.md`
- [ ] `working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md`
- [ ] retained design/build review and validation evidence linked by those records.

#### Artifact completion

- [ ] Evidence set frozen and recorded.
- [ ] Draft complete.
- [ ] Source/test claims checked at the pinned horizon.
- [ ] Real HTTPX flow checked end to end.
- [ ] Non-claims explicit.
- [ ] Fast-relearning route and transfer questions present.
- [ ] Final QA complete.

---

### Artifact 02 — ordinary PR source acquisition, correspondence and protocol paths

**File:** `02_ordinary_pr_source_acquisition_correspondence_and_protocol_paths.md`

**Reader outcome:** Ali can trace repository/PR input into exact/sample source roles, explain how candidate source relationships are discovered without answer selectors, follow direct/re-export/initializer/protocol paths, and distinguish a source path from effective installed/runtime dispatch.

#### Required coverage

- [ ] Curated proof vs ordinary PR-driven discovery.
- [ ] One native PR/dependency observation horizon and why duplicate acquisition is dangerous.
- [ ] `acquire_dependency_inputs` / ordinary experimental composition responsibility boundary.
- [ ] `PythonSourceAcquisitionRun` per-run cache, release/module limits and typed failures.
- [ ] Exact native old/proposed version source vs constraint-selected adapter sample.
- [ ] Source association/provenance basis vs installed package identity.
- [ ] Target inventory, imports/declarations/references and omission accounting.
- [ ] Internal module closure and why work selection is not a callable edge.
- [ ] Direct alias/declaration source relationship.
- [ ] Re-export and relative import paths.
- [ ] Initializer/base/super path with explicit MRO/receiver premises.
- [ ] Conditional Try-import superclass hypotheses and refusal when rebinding/deletion/dynamic namespace makes them unsafe.
- [ ] Local/external namespace collision alternatives.
- [ ] Repeated/decorated definitions remain alternatives.
- [ ] Missing source/cycles/depth/pair limits become explicit gaps, not global absence.
- [ ] Protocol/factory chain: module allocation → own `__getattr__` → returned class → own `__call__`.
- [ ] Overload declarations vs undecorated implementation; no automatic effective signature selection.
- [ ] Async/generator/factory limitations.
- [ ] Ordinary result formats, complete retained source and fixed cold opening.
- [ ] Why controlled ordinary composition is not fresh real-provider proof.

#### Primary pinned implementation anchors

- `experiments/api_adapter_exploration.py`
- `experiments/api_change_source_acquisition.py`
- `experiments/api_target_context.py`
- `experiments/api_target_context_smoke.py`
- `experiments/api_source_correspondence.py`
- `experiments/api_ordinary_call_signature_trial.py`
- `experiments/tests/test_api_adapter_exploration.py`
- `experiments/tests/test_api_public_pr_context.py`
- `experiments/tests/test_api_source_correspondence.py`
- `experiments/tests/test_api_ordinary_call_signature_trial.py`

#### Required historical/evidence anchors

- [ ] `working-memory/2026-10-28_second-real-caller-signature-case_qualification-and-evaluation-cycle.md`
- [ ] `working-memory/2026-10-28_pr-driven-caller-signature-integration_design-cycle.md`
- [ ] `working-memory/2026-10-29_pr-source-acquisition-integration_build-cycle.md`
- [ ] `working-memory/2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md`
- [ ] `working-memory/2026-10-30_protocol-factory-source-correspondence_build-cycle.md`
- [ ] corresponding controlled/retained evidence reviews.

#### Real teaching flows

- [ ] controlled direct old/proposed source path;
- [ ] HTTPX/FastAPI/Starlette mediated path;
- [ ] glyphsLib/pytest `mark.parametrize` protocol/factory path.

#### Artifact completion

- [ ] Evidence set frozen and recorded.
- [ ] Draft complete.
- [ ] All source-path premises represented honestly.
- [ ] Exact/sample/runtime roles clearly separated.
- [ ] At least one failure/gap path traced.
- [ ] Cold-reader/proof boundary explained.
- [ ] Final QA complete.

---

### Artifact 03 — failure-driven blocker resolution and experimental engineering

**File:** `03_failure_driven_blocker_resolution_and_experimental_engineering.md`

**Reader outcome:** Ali can diagnose a failed fresh experiment without guessing, identify the earliest sufficient repair owner, explain why old attempts remain immutable, and reconstruct how each blocker strengthened the generic method without forcing a desired answer.

This note is causal rather than merely chronological. Each material incident must use:

```text
symptom
→ tempting but unsupported diagnosis
→ measurement/evidence
→ actual owner
→ repair or explicit non-repair
→ discriminating regression/qualification
→ successor attempt
→ transferable lesson
```

#### Required failure atlas

- [ ] Acquisition policy/source starvation problem and staged-source policy rationale.
- [ ] Local request budget vs provider/account quota distinction.
- [ ] First fresh ordinary PR: FastAPI exact-release timeout; why provider failure was not a checker/correspondence defect.
- [ ] Separate endpoint diagnostic and why later availability did not regrade the failed attempt.
- [ ] Two-candidate frontier omits relevant implementation sources.
- [ ] Re-export/member-priority repair and renamed control.
- [ ] Sampled internal modules consume source question budget before native definitions.
- [ ] Native-first paired closure selection.
- [ ] Conditional superclass source hypotheses without promoting unknown binding.
- [ ] Stale pending priority discovered by stronger later evidence.
- [ ] Monotonic pending-priority promotion and no requeue of completed work.
- [ ] Missing wildcard module falsely reinterpreted through parent package / recursive state explosion.
- [ ] Exact required-module boundary repair; missing remains missing/unavailable, not absent.
- [ ] One-sided native evidence caused by transient source/provenance acquisition failure.
- [ ] Repeated pre-response PyPI timeouts and justification for narrow opt-in retry semantics.
- [ ] Retry policy: one pre-response timeout retry per logical PyPI GET, bounded globally, every physical attempt charged and retained; no retry for status/body/integrity/GitHub/auth/policy failures.
- [ ] Fresh attempt reaches both native sources but fails at result serialization.
- [ ] Wrong initial explanation vs D004/D005 measurement: input fits; computed output exceeds structural guard.
- [ ] Why this is a representation owner problem, not a Workspace-parser defect and not a reason to raise the guard.
- [ ] Exact interning/projection hypotheses tested rather than assumed.
- [ ] Purpose-specific receipt-summary projection: remove unconsumed duplicate broad binding tables while preserving outer acquisition evidence and independent source/comparison facts.
- [ ] D006 retained-component proof vs fresh successor proof.
- [ ] Fresh S008 useful partial ordinary evidence.
- [ ] S008 does **not** reproduce historical `app` mismatch; acceptance criterion does not require rejection.
- [ ] Four native comparison records are witnesses for one root/forwarded call, not four independent cases.
- [ ] Explicit remaining gaps/refusals/candidate omissions.

#### Primary evidence anchors

- [ ] `working-memory/2026-10-30_staged-source-acquisition-policy_build-cycle.md`
- [ ] first-fresh ordinary execution/freeze records and contract.
- [ ] `working-memory/2026-10-31_first-fresh-ordinary-pr-live-attempt_cycle.md`
- [ ] `working-memory/2026-10-31_ordinary-source-blocker-resolution_cycle.md`
- [ ] `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/S008/REVIEW.md`
- [ ] D001–D006 public-safe diagnostics/designs relevant to actual decisions.
- [ ] focused tests that reproduce every repaired defect class.

#### Required engineering diagnosis matrix

The note must end with a reusable classification model covering at least:

| Symptom class | Earliest likely owner | Wrong shortcut to avoid |
| --- | --- | --- |
| evidence never acquired | acquisition/source owner | patch checker |
| retained evidence but relationship unresolved/wrong | binding/correspondence | fetch more blindly |
| correct analysis but representation too large | retention/serialization/work admission | raise semantic caps or weaken integrity |
| provider transient failure | transport policy | reclassify as source absence |
| useful work starved by ordering | allocation/prioritization | enlarge every ceiling |
| request asks for runtime/installed truth | another evidence owner | strengthen static source claim |

#### Artifact completion

- [ ] Failure ledger verified against frozen evidence.
- [ ] Every repair has a corresponding proof/regression anchor.
- [ ] Every no-repair decision explains why.
- [ ] Historical attempts remain explicitly immutable/final.
- [ ] S008 result and partiality explained precisely.
- [ ] Engineering diagnosis matrix complete.
- [ ] Final QA complete.

---

### Artifact 04 — source retention, partial analysis and capacity engineering

**File:** `04_source_retention_partial_analysis_and_capacity_engineering.md`

**Reader outcome:** Ali can explain why retaining evidence and analyzing evidence are separate responsibilities, diagnose capacity failures by measurement, and reason about a bounded whole-file partial-analysis architecture without converting unexamined material into negative evidence.

#### Required coverage

- [ ] Entry pressure from a real direct-use development case with much larger target/source material.
- [ ] Why “just analyze everything retained” is not a durable architecture rule.
- [ ] Source-first capture: persist exact acquired text before large derived receipt/analysis representation.
- [ ] Why retained source must survive even if derived receipt or analysis later fails.
- [ ] File count/source byte/node/fact/comparison/structural-token limits as different dimensions.
- [ ] Measurement before repair: identify which dimension actually failed.
- [ ] Why simply raising one fact ceiling can move the failure to final representation.
- [ ] Difference between machine capacity and product/method admission.
- [ ] Conservative static-import component selection.
- [ ] Whole-file atomic analysis: analyze a file/group completely or record it unexamined; do not use partial facts to imply complete absence.
- [ ] Pair native old/proposed counterparts where needed for useful comparison pressure.
- [ ] Root/work priority is a work-allocation policy, not runtime binding.
- [ ] Explicit omission reasons such as outside component, aggregate fact budget, per-file budget and structural budget.
- [ ] Preserve all retained source text for inspection even when no facts are admitted.
- [ ] Lossless indexed binding-trace tables / normalization to remove repeated structure without dropping premises.
- [ ] Structural representation budget allocation among facts, comparisons and fixed metadata/gaps.
- [ ] Final invariant: **reduce admitted analysis work, not retained evidence**.
- [ ] Final invariant: **unexamined is not absent**.
- [ ] Fixed reader reconstruction and no re-analysis of saved partial results.
- [ ] What this architecture still does not solve: dynamic import/value flow, runtime dispatch, complete target coverage, semantic compatibility.

#### Primary pinned source anchors

- `experiments/api_source_correspondence.py`
- `experiments/api_signature_evidence.py`
- `experiments/api_ordinary_call_signature_trial.py`
- relevant source-first acquisition helpers in `experiments/api_change_source_acquisition.py` / ordinary driver;
- `experiments/tests/test_api_source_correspondence.py`
- `experiments/tests/test_api_ordinary_call_signature_trial.py`

#### Required historical/evidence anchors

- [ ] identify and record the exact direct-use capacity-development cycle(s) and evidence directories at the pinned horizon before drafting;
- [ ] retained measurements for pre-repair capture/output capacity;
- [ ] source-first capture proof;
- [ ] full-analysis counterfactual/measurement results;
- [ ] partial-analysis method design/qualification;
- [ ] lossless-trace/structural-work-allocation qualification;
- [ ] final method hashes/freeze used for later transfer.

This evidence-index task is mandatory before authoring because the capacity program contains several diagnostics and successor methods whose proof classes must not be merged.

#### Artifact completion

- [ ] Exact capacity-development evidence inventory completed.
- [ ] Every numerical example is tied to its exact method/result role.
- [ ] Retention vs analysis vs representation mental model complete.
- [ ] At least one before/after capacity calculation shown.
- [ ] Whole-file partiality and negative-evidence rule explained.
- [ ] Final source/work allocation flow traced.
- [ ] Final QA complete.

---

### Artifact 05 — transfer qualification, case selection and final proof boundary

**File:** `05_transfer_qualification_case_selection_and_final_proof_boundary.md`

**Reader outcome:** Ali can design and review a credible transfer/generalization experiment, distinguish method-development evidence from untouched qualification evidence, prevent case-selection leakage, and state exactly what the final unchanged-method result earns.

#### Required coverage

- [ ] Why two curated/retained cases were insufficient for ordinary transfer claims.
- [ ] Difference between method qualification, fresh ordinary acquisition, generalization/transfer and product integration.
- [ ] Direct-use eligibility reassessment: a failed candidate can expose bad screening assumptions without proving a method defect.
- [ ] Positive adapter exploration vs explicit conditional exact-source acquisition.
- [ ] Direct-dependency eligibility: declaration + matching import/source-form + real call witness, without outcome screening.
- [ ] Candidate-pool preservation and reasons for eligibility/ineligibility.
- [ ] Anti-cherry-picking rule: choose structural contrast, not a visible expected comparison result.
- [ ] Transfer-contamination rule: if a case causes a material method/semantic repair, it becomes development evidence for the successor method and cannot also qualify that successor.
- [ ] Development/stress role of the large capacity case.
- [ ] Method freeze after repairs and qualification cohort.
- [ ] Why one untouched contrasting case can be sufficient for the bounded adoption gate when the frozen method succeeds unchanged.
- [ ] Final untouched real case selection and freeze before expected outcome inspection.
- [ ] Same unchanged method executes without post-selection semantic repair.
- [ ] Paired old/proposed result and useful partial coverage.
- [ ] Why success does not imply statistical generality, runtime compatibility, installed-version truth, maintainer usefulness or product reliability.
- [ ] Why an all-unknown result would not count as positive transfer.
- [ ] When inconclusive/unsupported/defect outcomes require explicit disposition rather than undisclosed case cycling.
- [ ] Relationship between the final experiment result and the later native-adoption decision — boundary only, no post-horizon implementation details.

#### Required historical/evidence anchors

- [ ] `working-memory/2026-10-31_direct-usage-eligibility-and-target-frontier-review_cycle.md`
- [ ] contrasting-case screening/selection records at the pinned horizon;
- [ ] exact capacity-development/qualification records used before the final method freeze;
- [ ] frozen method/source/runtime identity record;
- [ ] final untouched transfer case selection/freezes/result/review;
- [ ] tests/compatibility evidence proving no post-selection method drift.

#### Required final proof statement

The note must end with a short claim ladder similar to:

```text
proved:
  frozen method can acquire/analyze/retain useful partial caller-signature source evidence
  on an untouched structurally contrasting real Python dependency-update PR
  within its declared source forms and resource bounds

not proved:
  installed versions
  runtime dispatch/execution
  behavioral compatibility
  complete repository/API coverage
  statistical reliability/general Python generality
  maintainer usefulness
  product/native delivery
  action permission
```

#### Artifact completion

- [ ] Candidate-selection methodology reconstructed exactly.
- [ ] Development vs untouched evidence labels verified.
- [ ] Method-freeze identity verified.
- [ ] Final transfer result reconstructed from fixed evidence.
- [ ] No later productization fact used as experiment proof.
- [ ] Final claim/non-claim ladder complete.
- [ ] Final QA complete.

---

## 8. Package README contract

**File:** `learning/2026-11-01-caller-signature-source-evidence-experiments/README.md`

The README is a navigation and authority map, not a sixth tutorial.

It must contain:

- [ ] educational snapshot date and exact commit;
- [ ] branch/base context only if useful for provenance;
- [ ] one-sentence central question;
- [ ] five-note reading order with reader outcomes;
- [ ] authority/evidence map;
- [ ] explicit statement that experiment output is not native product authority;
- [ ] package-wide must-own / operational / lookup / deferred map;
- [ ] recommended first-study route;
- [ ] fast return route for later relearning;
- [ ] `git show <snapshot>:<path>` guidance for local source inspection;
- [ ] warning against mixing mutable `main` files into this frozen snapshot;
- [ ] note that derived quizzes/audio/etc. should be generated on demand from pinned sources;
- [ ] statement that reading/approval is not mastery;
- [ ] provenance marker `UP-SKILL:upgradepilot-learning-artifact`.

README completion:

- [ ] Draft complete.
- [ ] All five note links correct.
- [ ] All links/anchors pinned or repository-relative with snapshot context.
- [ ] Package authority/non-authority is unambiguous.
- [ ] Final QA complete.

---

## 9. Evidence-indexing phase before prose authoring

Because several experiments have multiple diagnostics, development successors and immutable attempts, do not start writing long-form prose until a compact evidence index exists for the selected note.

For each note, build an in-session evidence table containing:

```text
teaching proposition
→ canonical/source owner
→ exact pinned source/function/type
→ focused test(s)
→ real case/evidence review
→ directly relevant history/correction
→ proof class
→ prohibited stronger interpretation
```

This table normally remains in-session working material. Do not create a permanent evidence-index file unless it independently improves package usability.

### Evidence-index completion ledger

- [ ] Artifact 01 evidence index complete.
- [ ] Artifact 02 evidence index complete.
- [ ] Artifact 03 evidence index complete.
- [ ] Artifact 04 evidence index complete.
- [ ] Artifact 05 evidence index complete.
- [ ] README common authority/snapshot anchors complete.

---

## 10. Authoring sequence

Default order is intentional:

```text
01 foundational evidence model
→ 02 ordinary discovery/composition
→ 03 real blocker-resolution engineering
→ 04 capacity/partial-analysis engineering
→ 05 transfer qualification/final proof
→ README final integration pass
```

The README may be initialized early as a package skeleton, but its final reader outcomes and cross-links should be verified after all five notes exist.

Why this order:

- Note 01 establishes the vocabulary required by everything else.
- Note 02 explains the pipeline whose failures Note 03 diagnoses.
- Note 03 teaches real operational failure and owner repair before Note 04 introduces the more abstract capacity/work-admission architecture.
- Note 04 explains the successor method that Note 05 later freezes and transfers.
- Note 05 depends on all previous distinctions to explain why the final evidence is credible but bounded.

### Package authoring ledger

- [ ] Artifact 01 authored and QA-complete.
- [ ] Artifact 02 authored and QA-complete.
- [ ] Artifact 03 authored and QA-complete.
- [ ] Artifact 04 authored and QA-complete.
- [ ] Artifact 05 authored and QA-complete.
- [ ] README finalized.
- [ ] Package-wide QA complete.
- [ ] `learning/README.md` package index updated only after package contents are stable.

---

## 11. Cross-artifact anti-duplication rules

Repeated concepts should have one primary teaching owner and concise references elsewhere.

| Concept | Primary learning owner | Other notes may do |
| --- | --- | --- |
| binding states and local comparison semantics | Note 01 | reference/result interpretation only |
| exact vs sampled source roles | Note 02 | use in failures/qualification |
| source relationship/path premises | Note 02 | show specific failure/transfer examples |
| attempt immutability/successor discipline | Note 03 | invoke in transfer methodology |
| acquisition starvation/transport retry | Note 03 | mention only as prior method input |
| source retention vs analysis | Note 04 | use as final method property |
| structural/work budgets | Note 04 | cite in final transfer bounds |
| anti-cherry-picking/contamination | Note 05 | not re-teach earlier |
| final proof/non-proof claim | Note 05 | README summarizes only |

Do not copy entire working-memory passages, plan contracts or source code between notes.

---

## 12. Real-case teaching ladder

Each major case receives a distinct educational role so the package does not repeatedly retell the same example.

| Case/evidence family | Primary lesson |
| --- | --- |
| retained HTTPX/Starlette/FastAPI | local source facts, explicit `app` mismatch under a selected pairing, and runtime/version premises |
| retained glyphsLib/pytest | protocol/factory path, overload alternatives, `**kwargs` reception and receiver uncertainty |
| controlled ordinary PR | automatic source discovery/composition without answer selectors |
| first fresh HTTPX attempt | procedural completion is not useful paired evidence; provider failure vs method failure |
| HTTPX successor blocker-resolution attempts | failure-driven allocation/source/transport/representation engineering |
| useful fresh HTTPX ordinary result | fresh evidence may contradict the expected historical story; do not force rejection |
| openDVP-type qualification candidate | case eligibility/screening failure is not automatically a method defect |
| LifeLog-type development/capacity case | source-first retention, capacity measurement, partial analysis and method development contamination |
| final Digimon-type untouched case | unchanged-method transfer/generalization evidence |

Before finalizing, verify that each case's name/identity and role match the actual retained evidence at the pinned horizon.

---

## 13. Failure/correction coverage ledger

The following material corrections must appear somewhere in the package. This ledger exists specifically to prevent the learning artifacts from presenting only the successful final design.

- [ ] source available but semantic interpretation still wrong;
- [ ] curated source pair is not ordinary discovery;
- [ ] line/expression identity is weaker than full source span identity;
- [ ] `inspect.Signature.bind` not accepted blindly as sole oracle;
- [ ] conditional origin/source success does not promote binding to established;
- [ ] source relationship does not establish installed namespace/dispatch;
- [ ] local namespace collision preserves alternatives;
- [ ] multiple bases/overloads remain alternatives without MRO/effective selection;
- [ ] provider timeout not mistaken for source absence or semantic defect;
- [ ] candidate frontier too narrow;
- [ ] sampled/internal work starves native source;
- [ ] stale pending priority prevents useful later evidence from being promoted;
- [ ] missing wildcard source causes incorrect recursive reinterpretation;
- [ ] provider retry justified only after repeated bounded pre-response timeouts;
- [ ] initial S007 input-size explanation corrected by measurement;
- [ ] result structural size, not input, was the actual capacity failure;
- [ ] representation repair chosen instead of raising native guard;
- [ ] fresh successful S008 result did not reproduce historical expected mismatch;
- [ ] record-count inflation avoided: witnesses are not independent cases;
- [ ] direct-use eligibility inference corrected prospectively without regrading old case;
- [ ] large development case cannot qualify the successor method it helped change;
- [ ] source retention survives analysis/representation refusal;
- [ ] partial analysis cannot support global absence;
- [ ] final untouched transfer is bounded, not universal product reliability.

No artifact package is complete until every checked correction is supported by a source/test/evidence anchor.

---

## 14. Practical source-reading requirements

Every note should include a small set of code-reading anchors, not dozens of links.

For each primary source anchor:

- name the function/type/constant that matters;
- explain the input → transformation → output responsibility;
- identify at least one important failure/unknown path;
- identify the nearest focused test;
- state what remains outside the function's authority.

The notes should make it possible to return to source with a command such as:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_source_correspondence.py
```

Do not reproduce entire implementations in Markdown.

---

## 15. Proof and QA strategy

Learning-artifact QA is evidence verification, not a rerun of the entire experiment campaign.

### Per-note QA

- [ ] responsibility/non-responsibility is explicit;
- [ ] evidence horizon is explicit;
- [ ] every material implementation claim matches pinned source/tests;
- [ ] every historical rationale/correction has a directly relevant record/evidence basis;
- [ ] current fact, evidenced rationale, engineering judgment and alternative are not conflated;
- [ ] real case is used where available;
- [ ] controlled fixture is labelled controlled;
- [ ] fresh/retained/diagnostic/transfer proof classes are labelled correctly;
- [ ] no stronger runtime/product claim is inferred from source evidence;
- [ ] important failure branch included;
- [ ] tests are presented with proof/non-proof, not merely counts;
- [ ] learning depth is calibrated;
- [ ] fast-relearning route is short and usable;
- [ ] transfer questions require reasoning rather than recall trivia;
- [ ] local links resolve and pinned links use the correct horizon;
- [ ] `git diff --check` / equivalent Markdown hygiene passes when available.

### Package-wide QA

- [ ] no contradiction among the five notes;
- [ ] vocabulary is stable across notes;
- [ ] no duplicate active owner for one concept;
- [ ] no historical attempt is silently regraded;
- [ ] no diagnostic is promoted to admitted result;
- [ ] no development case is presented as untouched transfer;
- [ ] no `main` productization source silently enters the experiment snapshot;
- [ ] all five case roles in the teaching ladder are accurate;
- [ ] all required corrections in §13 are covered;
- [ ] final claim/non-claim ladder matches retained evidence;
- [ ] package remains small enough to study and revisit;
- [ ] `learning/README.md` receives one concise package entry, not a duplicated summary.

---

## 16. Stop/reassessment conditions

Pause authoring and reconcile this plan if any of the following occurs:

1. the pinned horizon does not actually contain evidence required for one of the promised learning responsibilities;
2. a case/result identity in this plan is found to be mistaken or conflated;
3. a note would require current productization source to explain the historical experiment mechanism;
4. the five-note decomposition produces major duplication or one note becomes too broad to study;
5. the historical evidence reveals a materially different causal progression from the current plan;
6. a supposed rationale cannot be evidenced and would have to be invented;
7. authoring exposes a real product/source defect whose repair would exceed learning-artifact authorization;
8. a private/raw artifact would need to be published to support the note; use public-safe evidence or explain the limitation instead;
9. a later package file would become a second live tracker or authority owner.

A justified decomposition change may update this plan. Do not silently drift.

---

## 17. Prohibited scope during authoring

Unless Ali separately authorizes it, do not:

- modify product or experiment source/tests to make the notes easier to write;
- rerun live provider attempts;
- rerun historical frozen results to produce cleaner evidence;
- widen experiment/resource limits;
- create new semantic/product claims;
- merge current productization behavior into the frozen experiment snapshot;
- create permanent quizzes/audio/flashcards/condensed duplicates;
- create another overlapping plan or learning tracker;
- treat user approval of the notes as mastery.

---

## 18. Branch and merge discipline

This learning work proceeds only on:

`learning/caller-signature-source-evidence-artifacts-2026-11-01`

The branch was created from current `main` at `e7082e96df98d014a44d58637e985af7d3c9175c` so parallel native productization can continue independently.

### While main continues moving

- Do not continually rebase merely to follow productization.
- Keep all historical learning evidence pinned to `c53430c6...`.
- Reconcile from `main` only if governance/learning-package ownership changes materially affect this responsibility or before eventual merge when necessary.
- If a conflict occurs in `learning/README.md`, preserve current main's index plus this package's concise new entry; do not let an old branch version overwrite newer packages.
- Productization commits after the snapshot can be acknowledged in the package README only as later/outside-snapshot context when necessary.

---

## 19. Completion ledger

### Planning/setup

- [x] Latest `main` inspected before branching: `e7082e96df98d014a44d58637e985af7d3c9175c`.
- [x] Separate learning branch created.
- [x] Learning-artifact Skill inspected.
- [x] Planning/Design Skill and `plans/README.md` inspected.
- [x] `learning/README.md` snapshot/depth/package policy inspected.
- [x] Frozen experiment learning horizon selected: `c53430c6e3fb4f24147a28aa642ab94834233243`.
- [x] Small ordered package shape selected: README + five substantive notes.
- [x] Learning responsibilities and non-responsibilities separated.
- [x] Package-wide depth calibration defined.
- [x] Failure/correction ledger defined.
- [x] QA/pass/stop/prohibited-scope rules defined.

### Evidence indexing

- [ ] Artifact 01 evidence index complete.
- [ ] Artifact 02 evidence index complete.
- [ ] Artifact 03 evidence index complete.
- [ ] Artifact 04 evidence index complete.
- [ ] Artifact 05 evidence index complete.

### Authoring

- [ ] Artifact 01 complete.
- [ ] Artifact 02 complete.
- [ ] Artifact 03 complete.
- [ ] Artifact 04 complete.
- [ ] Artifact 05 complete.
- [ ] Package README complete.

### Final package closure

- [ ] Cross-artifact anti-duplication review complete.
- [ ] Required failure/correction ledger fully covered.
- [ ] All source/test/evidence links checked.
- [ ] Final proof/non-proof statement checked against frozen evidence.
- [ ] Snapshot contamination check complete.
- [ ] Fast-relearning routes checked.
- [ ] Transfer questions checked for practical reasoning value.
- [ ] `learning/README.md` updated with the finished package.
- [ ] Final branch review confirms only intended learning/plan artifacts changed.
- [ ] Package ready for merge decision.

---

## 20. Pass condition

This plan passes when all five substantive learning artifacts plus the package README exist, their completion boxes and package-wide QA are checked with evidence, and a later reader can recover the engineering model, real flows, failures, repairs, proof classes and final bounded transfer claim from the package without depending on chat history or current productization source.

The pass condition is about artifact completeness and evidence quality. It does not certify Ali's independent mastery. Interactive mastery or ownership practice can later use these artifacts under Learning-Only/Learning-by-Doing as a separate responsibility.
