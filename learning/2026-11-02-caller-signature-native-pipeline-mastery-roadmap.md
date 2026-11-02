# Caller-Signature Native Pipeline — Living Learning and Mastery Roadmap

**Created:** 2026-11-02  
**Initial evidence horizon:** `7a9bef12fb65ee075dab645a638adf5a3955dc48`  
**Working branch:** `learning/current-caller-signature-mastery-roadmap-2026-11-02`  
**Purpose:** living study/relearning roadmap for Ali's interactive learning track while UpgradePilot continues to evolve on `main`.  
**Authority boundary:** this file is a learning artifact, not a live project-position owner. `MEMORY.md`, current source/tests, accepted plans/specifications/ADRs, and dated evidence remain authoritative for implementation truth and current project continuation.

`UP-SKILL:upgradepilot-learning-artifact`

---

## 1. How to use this roadmap

This roadmap tracks **what Ali should understand and eventually own**, not merely which files have been read. It follows the actual UpgradePilot caller-signature/productization path and is updated when `main` materially changes.

### Status legend

- ✅ **Covered interactively** — we have already taught/traced this topic with current project evidence. This does **not** claim independent mastery.
- 🟡 **Introduced / partially covered** — the concept has appeared in prior explanations but still needs a dedicated learning pass.
- ⬜ **Planned** — not yet covered properly in this learning track.
- 🔁 **Revisit after implementation change** — prior understanding remains useful, but new `main` work materially extends the responsibility.

### Depth legend

- **MUST OWN** — Ali should be able to reason about, review, challenge, modify/test, and explain the responsibility with limited assistance.
- **OPERATIONAL** — Ali should understand the mechanism well enough to trace, debug, review, and safely work around it.
- **LOOKUP** — recognize the construct and know where/how to recover details; memorization is unnecessary.
- **DEFERRED** — real depth that does not currently unlock the project responsibility.

### Learning-session method

For each module, prefer:

`real UpgradePilot case → source/data/control flow → invariants → failure/uncertainty states → tests/evidence → proof/non-proof → ownership questions`

Use the Digimon Requests case, LifeLog partial-analysis case, HTTPX comparison cases, retained worker/family qualification, and concrete failure/repair incidents before synthetic examples whenever practical.

---

## 2. Main-sync protocol for this learning branch

When `main` materially advances while this learning branch is active:

1. Refresh the exact current `main` head and compare it with the roadmap's last synced horizon.
2. Inspect `MEMORY.md`, the active cycle/handoff, changed product code, focused tests, and material evidence.
3. Classify the new work as one of:
   - **extends a future roadmap module** → add it there without changing current learning order;
   - **changes a prerequisite already covered** → mark that module `🔁 Revisit` and add the exact delta before continuing;
   - **introduces a new architectural/trust/proof boundary** → insert a new module at the dependency-correct point;
   - **implementation-only detail with no ownership value now** → record as LOOKUP/deferred rather than expanding the roadmap.
4. Preserve completed historical learning truth. Do not silently relabel a covered topic as mastered, and do not erase earlier learning because implementation grew.
5. Update the **Last synchronized main horizon** section below.
6. Continue from the earliest roadmap point whose understanding is now required by the current product architecture.

This branch may be rebased/merged from `main` as needed for current-source access, but this roadmap itself must not become a second `MEMORY.md`.

### Last synchronized main horizon

- `7a9bef12fb65ee075dab645a638adf5a3955dc48` — installed native source/comparison family + checkpoint recovery milestone qualified; normal native source acquisition/application/CLI/report integration still pending.

---

# PART A — Foundations already covered

## Module A1 — Current caller-signature capability mental model

**Status:** ✅ Covered interactively  
**Required depth:** MUST OWN

### Core model already covered

- Caller/signature evidence is **source-only conditional evidence**, not runtime execution proof.
- The current reasoning stack is intentionally layered:
  - name/import origin;
  - source correspondence;
  - local argument/signature fit;
  - runtime dispatch/installed version/behavior remain separate unresolved questions unless another owner establishes them.
- `BindingAssessment`, source correspondence, `ArgumentComparison`, and runtime execution have distinct meanings.
- `bound` does not mean “upgrade compatible”; it means local argument reception succeeds under the selected declared-signature premise.
- `undetermined` is a first-class result, not a hidden success.
- Retained source, analyzed source, runtime evidence, and maintainer action authority are separate evidence/authority layers.

### Real anchor already used

`RiceKrisBs/digimon_scraper` PR16, Requests `2.32.4 → 2.33.0`:

- module-level `requests.get(BASE_URL)` has an established static imported origin;
- selected `get(url, params=None, **kwargs)` signatures locally bind on both versions;
- Requests' forwarded `request("get", url, params=params, **kwargs)` remains undetermined because the keyword expansion is unresolved;
- none of these facts proves installed runtime dispatch or semantic compatibility.

### Ownership check to revisit later

Explain, without using the labels as definitions, why:

`established origin → selected declaration → bound arguments`

does not imply:

`actual runtime call → compatible behavior`.

---

## Module A2 — Product-kernel ownership transfer and proof boundaries

**Status:** ✅ Covered interactively  
**Required depth:** OPERATIONAL

### Covered

- The qualified analyzer moved from active experiment implementations into product owners under `src/upgradepilot/caller_signature/`.
- Historical experiment modules delegate/act as compatibility surfaces instead of maintaining a second evolving analyzer.
- Definition-level transfer evidence is weaker than retained semantic equivalence; both were used.
- Retained equivalence preserved thousands of facts/comparisons plus paths/premises/admission/gaps.
- Installed-wheel proof matters because “works from checkout” is weaker than “works as packaged product code.”
- Kernel/product ownership proof is still not the same as a complete normal product feature.

### Source anchors

- `src/upgradepilot/caller_signature/bindings.py`
- `src/upgradepilot/caller_signature/analysis.py`
- `src/upgradepilot/caller_signature/correspondence.py`
- `src/upgradepilot/caller_signature/evidence.py`

---

## Module A3 — `bindings.py`: scoped imported-origin analysis

**Status:** ✅ Covered interactively  
**Required depth:** MUST OWN

### Covered mechanism

- `ImportFact` versus `ReferenceFact`.
- `BindingAssessment` primitive evidence and canonical derived states:
  - `established`;
  - `conditional`;
  - `unknown`;
  - `unbound`.
- `_Frame` as lexical namespace state.
- module/class/function scope distinctions.
- branch fork/join and preservation of alternatives.
- simple reassignment and alias copying.
- delayed global reads: definition time is not invocation time.
- `global` and `nonlocal` effects and cross-scope uncertainty.
- wildcard import uncertainty.
- dynamic namespace operations (`exec`, `eval`, `globals`, `locals`, `vars`, `setattr`, `delattr`).
- attribute/subscript mutation and bounded alias invalidation.
- unsupported control flow: retain observable calls but degrade certainty rather than silently ignore.
- parameter values begin unknown without interprocedural call-value propagation.
- trace versus semantic assessment:
  - trace = source/provenance history;
  - assessment = current possibility state;
  - trace order is not fabricated runtime execution order through mutually exclusive branches.
- origin/trace resource ceilings must degrade certainty rather than silently truncate and retain “established.”

### Real anchor

Digimon module-level `import requests` → `requests.get(...)` as the straightforward established baseline, then progressive reasoning through rebinding/branches/scope mutations.

### Revisit trigger

Revisit only if future `main` changes binding semantics, supported control-flow scope, origin propagation, or the truth-state model.

---

# PART B — Semantic analysis core still to master

## Module B1 — `analysis.py`: AST source facts and local argument binding

**Status:** ⬜ Planned  
**Required depth:** MUST OWN

### Why this is next

Everything later stores, validates, transports, or publishes `CallArguments`, `CallableSignature`, and `ArgumentComparison`. We must understand their semantics before learning their codecs/Workspace forms.

### Must learn

- Python AST coordinates and why columns are UTF-8 byte offsets.
- stable `fact_identity(kind, unit_id, span)` and what identity does/does not guarantee.
- `CallArguments`:
  - expression;
  - ordinary/starred positional items;
  - explicit keyword names versus `None` for `**kwargs`;
  - argument spans;
  - completeness;
  - binding assessment.
- `CallableSignature`:
  - qualified name;
  - function/async/initializer kind;
  - parameter kinds;
  - defaults;
  - decorators/class bases;
  - limitations.
- `_SignatureVisitor` and source extraction boundaries.
- Python parameter kinds:
  - positional-only;
  - positional-or-keyword;
  - `*args`;
  - keyword-only;
  - `**kwargs`.
- `receiver_mode`:
  - `as_written`;
  - `one_receiver_assumed`;
  - `unresolved`.
- `compare_arguments()` outcomes:
  - `bound`;
  - `rejected`;
  - `undetermined`.
- violations:
  - unexpected keyword;
  - positional-only by keyword;
  - duplicate argument/keyword;
  - excess positional;
  - missing required argument.
- unresolved checks:
  - starred positional expansion;
  - keyword expansion;
  - receiver uncertainty;
  - incomplete source;
  - signature limitations.
- `remaining_premises` and why a local successful bind does not collapse dispatch/runtime uncertainty.

### Real cases

1. Digimon `requests.get(BASE_URL)` → both old/new `get` bind.
2. Requests `get()` forwarding to `request(..., **kwargs)` → undetermined.
3. Retained curated rejection case → understand a real `rejected` outcome rather than only synthetic examples.

### Exit condition

Ali should be able to predict the outcome and unresolved/violation set for a changed real call/signature pair, then locate the corresponding logic in `analysis.py`.

---

## Module B2 — `correspondence.py` + work admission as one responsibility

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Already introduced

- source correspondence is not runtime dispatch;
- bounded direct/import/initializer/factory/protocol paths;
- `SourceRelationshipStep`;
- atomic old/proposed analysis groups;
- whole-file analysis profile;
- retained-but-unexamined is not absence evidence;
- fact/comparison structural-budget allocation.

### Still to learn properly

- `PythonSourceModule` roles and source/module identity.
- relative/absolute import resolution within captured source namespaces.
- declaration discovery versus effective exports.
- lexical-body traversal and why nested callbacks/scopes are excluded in some paths.
- direct imported-call paths.
- module/member correspondence.
- initializer/class paths.
- supported factory / returned-class / call-protocol paths.
- unresolved `Try`-import superclass hypotheses and their premises.
- candidate IDs, root calls, selected declaration roles, path steps, and premises.
- discovery gaps and gap budgets.
- static import-component selection.
- root priority and whole-file admission.
- old/proposed atomic group admission and why torn comparison pairs are refused.
- aggregate fact budget, per-file fact budget, structural budget, pair budget.
- distinction among:
  - scanned;
  - retained;
  - analyzed;
  - unexamined;
  - no candidate discovered;
  - unresolved candidate.

### Real cases

- Digimon direct `requests.get` source relationship.
- LifeLog: 28 retained texts, 10 analyzed Python units, 17 unexamined Python units + one non-Python unit.
- HTTPX / glyphsLib protocol cases for more complex correspondence paths.

### Exit condition

Ali should be able to explain why a completed analysis may leave files unexamined and why that does not mean either “analysis failed” or “those files contain no relevant evidence.”

---

# PART C — Native analysis execution and integrity

## Module C1 — Typed analysis lifecycle: input → worker → run → result

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Source anchors

- `src/upgradepilot/caller_signature/evidence.py`
- `src/upgradepilot/caller_signature/worker.py`
- `src/upgradepilot/caller_signature/result_codec.py`

### Must learn

- `SourceAnalysisInput` is prepared offline analysis material, **not acquisition proof**.
- exact input contents:
  - retained catalog;
  - module roles;
  - bounded limits.
- `SourceAnalysisResult` versus `SourceAnalysisRun`.
- why:
  - run state = execution/lifecycle truth;
  - result coverage = semantic analysis coverage;
  - usefulness = separate downstream judgment.
- valid run states:
  - completed;
  - failed;
  - timed_out;
  - interrupted.
- completed result can contain `unexamined` units.
- failed/timed-out/interrupted runs must not masquerade as empty successful results.
- parent versus child responsibilities.
- temporary private input/output files.
- monotonic deadline ownership.
- address-space limit and result-size limit.
- kill/reap behavior on timeout.
- bounded failure detail.
- why the direct producer exists for owned qualification but normal callers should use the bounded parent.
- installed module-origin proof and what it proves.
- dependency reuse versus true dependency isolation.

### Real anchor

LifeLog completed worker with 17 unexamined Python units.

### Exit condition

Ali should be able to answer: “How can the worker be `completed` while coverage is partial?” and identify which type owns each fact.

---

## Module C2 — Fixed reconstruction and cross-record integrity

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Must learn

- encode/decode is preservation/reconstruction, not producer execution.
- cold decode must not reacquire, parse AST, rediscover correspondence, or rerun argument checking.
- exact input digest binding.
- unit/fact/candidate identity checks.
- source span validation.
- call/signature reference closure.
- candidate path/premise closure.
- shared trace-table referential integrity.
- malformed/foreign reference refusal.
- structural/byte capacity guards.

### Real defect to understand deeply

The swapped-call-ID defect:

- two calls could have identical argument shapes;
- changing a comparison's call ID could preserve an old witness path;
- local argument/accounting validation alone did not prove the witness path belonged to the selected call;
- repair required validating that the compared call actually occurs as a call step at the exact unit/span in the retained path.

### Transfer lesson

A valid node plus a valid node does not imply a valid edge. Evidence graphs need relationship/integrity validation in addition to per-record validation.

### Exit condition

Ali should be able to propose a corruption mutation and identify which reader/projection invariant should refuse it.

---

# PART D — Native source/comparison families and provenance

## Module D1 — `caller_signature_sources`: acquisition/source evidence family

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Source anchors

- `src/upgradepilot/caller_signature/source_evidence.py`
- `src/upgradepilot/caller_signature/source_codec.py`

### Must learn

`CallerSignatureSources` contains:

- retained exact source catalog;
- module roles;
- analysis limits;
- typed `SourceAcquisitionReceipt`.

Learn the distinction between **source material** and **the observations/premises that justify selecting/associating that material**.

### Acquisition/provenance records to understand operationally

- target source receipt;
- dependency declarations;
- import candidates;
- package release/source association;
- publisher/provenance inspection;
- module source request;
- tag→commit evidence;
- dependency metadata;
- module examined/refused/unavailable states;
- source selection;
- material omissions;
- transport request/retry/stop accounting;
- source work and acquisition limits;
- retention gaps;
- method-file identity.

### Critical states

- native observation;
- retained experiment projection;
- controlled observation.

Historical summarized receipts must remain explicitly incomplete; they must never be upgraded into fresh provider proof by reconstruction.

### Real case

Understand why glyphsLib's retained selected-catalog/result evidence remains useful for worker/protocol qualification but is **not admitted to the source family** because the necessary ordinary acquisition premises are missing.

### Exit condition

Ali should be able to distinguish:

`exact source bytes available`

from

`source acquisition/provenance sufficient for this native family`.

---

## Module D2 — `caller_signature_comparison`: analysis-run evidence family

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Source anchors

- `src/upgradepilot/caller_signature/comparison_codec.py`
- `src/upgradepilot/caller_signature/result_codec.py`
- `src/upgradepilot/workspace/native_codecs.py`

### Must learn

- comparison family reuses the earned analysis run/result rather than duplicating source text.
- decoding comparison requires the exact decoded source family.
- exact dependency edges:
  - `investigation_inputs`;
  - `caller_signature_sources`.
- no silent source substitution under an old comparison.
- source-only revision can exist without comparison.
- failed comparison run is still recorded evidence.
- completed comparison may still be partial/unexamined.

### Exit condition

Trace a comparison record back to the exact source material and explain what prevents it from silently rebinding to a later source-family record.

---

## Module D3 — Codec version versus semantic producer method/version

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Must learn

Keep these independent:

- `codec_version` — how bytes are represented/read;
- `producer_method` — which semantic producer operation created the evidence;
- `producer_version` — which admitted semantic method version produced it.

Understand why readable codec1 bytes are **not** automatic authority to interpret arbitrary producer semantics.

### Current caller-signature support

- exact source-family producer method/version1;
- exact comparison-family producer method/version1;
- old unrelated families keep their existing unavailable-version gaps;
- no blanket producer-version admission.

### Exit condition

Ali should be able to explain why “decoder can parse the payload” is weaker than “this family/method/version is semantically supported.”

---

# PART E — Workspace material graph and recovery

## Module E1 — Native capture state machine

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Source anchor

- `src/upgradepilot/workspace/native_capture.py`

### Must learn

- `_StagedCapture` fields and immutable encoded staging.
- family placeholders created at investigation start.
- missing record versus explicit `not_evaluated`.
- `capture_caller_signature_sources()`.
- `capture_caller_signature_comparison()`.
- `input_record_ids` as actual provenance/material edges.
- why pending unevaluated records can rebind to current inputs, but evaluated records cannot silently rebind.
- `partial_snapshot()` versus completed/sealed `snapshot()`.
- capture does not acquire evidence, evaluate, retry, or publish by itself.

### Critical three-state distinction

1. `not_evaluated` — operation never ran;
2. recorded + failed/timed_out/interrupted — operation ran and did not produce a completed result;
3. recorded + completed — operation ran and produced a result, possibly with partial coverage.

### Exit condition

Ali should be able to describe what survives if source publication succeeds and analysis then fails.

---

## Module E2 — Workspace family DAG, checkpoint publication, and fresh-process recovery

**Status:** 🟡 Introduced / partially covered  
**Required depth:** MUST OWN

### Source anchors

- `src/upgradepilot/workspace/native_codecs.py`
- `src/upgradepilot/workspace/native_capture.py`
- `src/upgradepilot/workspace/native_projection.py`
- Workspace host/store/checkpoint owners referenced by the current native-family tests.

### Must learn

Current material DAG:

`investigation_inputs → caller_signature_sources → caller_signature_comparison`

(with comparison also explicitly dependent on investigation inputs).

Learn:

- family owner versus representation owner.
- family contract inputs.
- record identity versus payload digest versus family identity.
- exact target binding.
- partial publication.
- successor revision publication.
- schema2 store responsibility.
- cold reopening by target/revision selection.
- fixed projection versus reevaluation.
- why fresh-process recovery forbids producer/worker/AST/network calls.
- source-only checkpoint versus source+comparison checkpoint.
- immutable material/history semantics.

### Real cases

LifeLog, HTTPX, and Digimon native source/comparison publication and cold recovery.

### Capacity lesson

Understand actual LifeLog family pressure under unchanged guards and why passing family/storage capacity still does not prove report/application capacity.

### Exit condition

Trace one checkpoint from source capture through publication, store, fresh interpreter reopen, and typed projection without invoking the producer again.

---

# PART F — Next implementation responsibilities to add when `main` reaches them

These are already known from the current live plan/memory but are **not yet implemented enough to learn as finished product behavior**. Keep them queued and replace plan-level expectations with actual source/evidence when `main` delivers them.

## Module F1 — Native source acquisition / target-context composition

**Status:** ⬜ Planned / waiting for implementation  
**Required depth:** MUST OWN when built

Expected topics:

- reuse existing GitHub/PyPI/provider owners;
- target source acquisition;
- dependency source association;
- declaration/import candidate formation;
- module requests and selection;
- exact provenance/association receipts;
- partial source progress before analysis;
- no duplicated provider ownership.

Do not teach this as completed product behavior until current `main` implements and verifies it.

---

## Module F2 — Shared request/policy/physical-attempt ledger

**Status:** ⬜ Planned / waiting for implementation  
**Required depth:** MUST OWN when built

Expected topics:

- shared physical-request accounting across source acquisition;
- request reserves and aggregate limits;
- retry policy ownership;
- source-progress publication before downstream analysis;
- failed provider attempt retention;
- relationship to existing GitHub/PyPI clients and project-wide acquisition accounting.

---

## Module F3 — Normal application composition

**Status:** ⬜ Planned / waiting for implementation  
**Required depth:** MUST OWN when built

Expected flow:

`AcquiredDependencyInputs → caller-signature source acquisition → source checkpoint → bounded analysis worker → comparison checkpoint → normal investigation result/consumer`

Must understand where orchestration belongs and prevent `investigation.py` from becoming an unbounded god-function.

---

## Module F4 — CLI/profile/report/source navigation

**Status:** ⬜ Planned / waiting for implementation  
**Required depth:** OPERATIONAL to MUST OWN depending on final responsibility

Expected topics:

- explicit `caller-signature` evidence profile;
- preserving current default behavior;
- CLI outcome/exit distinctions;
- report evidence versus interpretation;
- source navigation from findings back to exact retained material;
- fresh-process recovery and failure UX;
- no automatic compatibility/action claim.

---

## Module F5 — Actual normal-product qualification and usefulness/adoption

**Status:** ⬜ Planned / waiting for implementation  
**Required depth:** MUST OWN

Expected topics:

- retained equivalence after integration;
- separately frozen actual product path;
- normal fresh product run;
- capacity and recovery under complete application/report envelope;
- maintainer task/usefulness review;
- capability claim boundary;
- what constitutes adoption versus merely functioning machinery.

---

# PART G — Cross-cutting concepts that must be reinforced throughout

These should not become detached theory sessions; reinforce them whenever the corresponding real implementation appears.

| Concept | Current status | Required depth | Where reinforced |
|---|---|---:|---|
| Evidence vs authority | ✅ Covered | MUST OWN | every module |
| Static evidence vs runtime fact | ✅ Covered | MUST OWN | A1, A3, B1/B2 |
| Positive / negative / unknown / unresolved distinctions | 🟡 | MUST OWN | B1/B2, C1, D1 |
| Provenance and exact material identity | 🟡 | MUST OWN | D1/D2/E1/E2 |
| Node validity vs edge validity | 🟡 | MUST OWN | C2/E2 |
| Result state vs coverage vs usefulness | 🟡 | MUST OWN | C1/E1/F5 |
| Resource bounds as semantic completeness constraints | 🟡 | MUST OWN | A3/B2/C1 |
| Partiality without false absence | 🟡 | MUST OWN | B2/C1/E1 |
| Codec version vs producer semantic version | 🟡 | MUST OWN | D3 |
| Historical evidence immutability / no regrading | 🟡 | OPERATIONAL | D1/E2/F5 |
| Reconstruction vs reevaluation | 🟡 | MUST OWN | C2/E2 |
| Installed artifact proof vs checkout proof | ✅ Introduced | OPERATIONAL | C1/E2 |
| Test failure classification | 🟡 | OPERATIONAL | C2/D/E |
| Dependency closure versus global registry assumptions | 🟡 | OPERATIONAL | E2 |
| Responsibility ownership / no duplicate analyzers/providers | ✅ Introduced | MUST OWN | all architecture modules |

---

# PART H — Practical ownership exercises

Do these progressively after the corresponding teaching module rather than all at the end.

### H1 — Prediction exercises

Given a small modification to a real retained source flow, predict:

- binding state;
- extracted call/signature shape;
- comparison outcome;
- unresolved premises;
- analyzed/unexamined effect;
- run state versus result coverage.

### H2 — Integrity review exercises

Given a plausible corrupted record, identify whether the correct refusal owner is:

- component codec;
- result codec;
- source/comparison family codec;
- native boundary;
- projection;
- Workspace store/checkpoint layer.

### H3 — Failure diagnosis exercises

Classify real failures as:

- product semantic defect;
- source/provenance insufficiency;
- resource-limit refusal;
- worker lifecycle failure;
- representation/integrity defect;
- stale/incorrect test assumption;
- packaging/environment proof failure;
- unsupported but honest evidence state.

### H4 — Small learner-owned changes/tests

When appropriate and explicitly authorized, Ali should eventually perform or direct small bounded changes such as:

- add a discriminating argument-binding test;
- add a binding uncertainty case;
- add a corrupted reference test;
- trace/add a projection invariant;
- explain expected retained-result changes before executing the test.

These are ownership practice, not prerequisites for every learning conversation.

---

# PART I — Mastery / completion criteria for this roadmap

This roadmap is not complete because every checkbox is read. It is complete when Ali can, with limited assistance:

1. Trace a real caller-signature case from retained source acquisition through binding, extraction, correspondence, argument comparison, work admission, bounded worker execution, native source/comparison capture, Workspace publication, and cold reconstruction.
2. Identify the owner of each important fact and uncertainty.
3. Distinguish source/provenance truth, analysis truth, execution/run truth, runtime truth, interpretation, and maintainer-action authority.
4. Predict major success/failure/partial states before running tests.
5. Review a change for overclaiming, provenance loss, silent rebinding, accidental reevaluation, unbounded work, or responsibility duplication.
6. Explain what the strongest verification proves and what it does not prove.
7. Diagnose at least one real failure or corrupted-evidence case and locate the earliest sufficient repair owner.
8. Make or direct at least one bounded central test/change and explain its consequences.
9. Re-enter the capability after a gap by using the source/test/evidence anchors rather than relying on chat memory.

Independent mastery should be recorded only when demonstrated; this roadmap's ✅ marks mean **covered**, not mastered.

---

# PART J — Immediate next learning sequence

Unless a new `main` update changes prerequisites, continue in this order:

1. **B1 — `analysis.py` deeply** using Digimon `get → request` plus a real rejection case.
2. **B2 — `correspondence.py` + work admission** using Digimon and LifeLog.
3. **C1 — typed analysis lifecycle + bounded worker** using LifeLog partial completion and worker failure/timeout cases.
4. **C2 — fixed reconstruction + integrity** centered on the swapped-call-ID defect.
5. **D1/D2/D3 — native source/comparison families + semantic version admission** using LifeLog/HTTPX/Digimon and glyphsLib non-admission.
6. **E1/E2 — native capture + Workspace checkpoint/recovery** through actual source-only and source+comparison revisions.
7. Refresh `main`; then activate the earliest implemented F-module whose prerequisites are satisfied.

Stop and sync `main` before starting a new major module if the parallel build has materially advanced.
