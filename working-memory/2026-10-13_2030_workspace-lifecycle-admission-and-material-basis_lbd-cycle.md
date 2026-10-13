# Workspace lifecycle, host admission and material-basis validity — LbD cycle

**Initialized:** 2026-10-13 20:30 Asia/Tehran.
**Session status:** ACTIVE in A2; upcoming responsibility orientation presented, pre-B understanding gate pending.
**Primary operation:** Planning/Design for responsibility reconciliation and A-phase entry; Build/Implement is gated separately.
**Previous engineering foundation:** [Stages 1–2 cycle](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md). Its remaining D/E progression is independently owned on `learning/d-native-ownership-2026-10-10`; this record does not take it over.
**Owners:** [live position](../MEMORY.md), [implementation/migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md#technical-stages-and-cycle-boundaries), [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [Core §6.4](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Operating Guide](../OPERATING_GUIDE.md).
**Procedures:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.

## Cycle status

```text
Cycle — Workspace lifecycle, host admission and material-basis validity
A0 — DONE: current main/owners/source/tests/proof reconciled; record and living A-phase map initialized.
A1 — DONE: Ali accepted the current-state model and explicitly requested A2; no independent D/E mastery inferred.
A2 — CURRENT: upcoming responsibility/flow/proof orientation presented; pre-B understanding gate remains pending.
B — PENDING: no lifecycle product source/test implementation begun.
Verification gate — PENDING: future Stage 3 behavior requires its own product proof.
D — PENDING: learn from the sufficiently verified new result.
E — PENDING: gap disposition and closure after D.
C — CONTINUOUS: meaningful reconciliation, learning, decisions and evidence preserved here.
```

## A0 reconciliation and responsibility decision

Ali requested continuing current main, treating Stages 1–2 engineering as verified, keeping its remaining D/E learning independent, selecting the next coherent responsibility from evidence, and completing the required A-phase before Build.

Initial checkout was `main` `f8047c5b`, with one unrelated untracked October 3 audit record. Fetch found the newer records-only coordination commit `e9dea055`; a fast-forward brought main to it. That commit already acknowledges the independent learning stream. The unrelated record was not read, changed or staged.

Source/test identity was verified independently of the live-state wording:

- `e9dea055:src` and `4f502989:src` both equal `8cc3d25ba87867f2af62ad4579c0ef5cd09552f9`.
- `e9dea055:tests` and `4f502989:tests` both equal `bd9d036f4451e8074df6d7528352633a15d7f91c`.
- The fetched learning head is `f0f37d13`; compared with main, its changes are `MEMORY.md`, the prior cycle record and a branch-progress record. No product source/tests, plan, accepted specification or ADR differ. The local learning branch still points to `276bc4ac`; neither branch nor its worktree was moved, merged or edited here. The October 13 main coordination records its learning handoff; individual learning blocks were not reopened or reassessed.

Both ADR-0012 and ADR-0013 are Accepted. Core §6.4 and Product Decision Model §§11–13 control historical recovery, execution admission, material validity and stopping limits. The implementation plan has six technical stages, with Stages 1–2 grouped as the native-foundation responsibility. Its later integration section covers several stages; it does not require full report/CLI cutover inside Stage 3. No new ADR, framework, research spike or competing plan is required merely to enter the accepted lifecycle responsibility.

### Actual implementation and proof boundary

- [Orchestration](../src/upgradepilot/investigation.py) still runs the existing native sequence and returns the 24-field frozen `PublicPullRequestInvestigation`. An opt-in [native capture](../src/upgradepilot/workspace/native_capture.py) retains supplied inputs/results, encodes fixed owner families and seals only after normal completion. Its staged family values do not constitute admission/attempt/observation history.
- [Native boundary](../src/upgradepilot/workspace/native_boundary.py), [family contracts](../src/upgradepilot/workspace/native_codecs.py) and [native projections](../src/upgradepilot/workspace/native_projection.py) preserve the admitted 11-root CI/Python closure. Missing/unsupported material is explicit; reconstruction validates retained bindings without rerunning native evaluators. Thirteen legacy fields have native equivalents; eleven remain later-family/consumer obligations. The prior cycle retains the exact disposition ledger.
- [Checkpoint revision](../src/upgradepilot/workspace/checkpoint_revision.py) and [store](../src/upgradepilot/workspace/checkpoint_store.py) protect immutable identity/material, conditional predecessor publication, retained history, unconfirmed acknowledgement and validated backup. The native orchestration does not yet invoke that store as a lifecycle host. Structural coherence precedes publication-conflict classification after the October 11 repair.
- [Combined reconstruction tests](../tests/test_workspace_checkpoint_reconstruction.py) inspect a declared durable revision and reconstruct supported native projections in guarded fresh processes. They cover historical prefixes/earlier progress, WAL/backup, unsupported roots/bindings and actual pre/postcommit interruption. Test-constructed historical states are boundary controls, not evidence that normal orchestration already publishes every lifecycle transition.
- Recorded October 11 proof at `4f502989`: 132 focused tests, 833 checkout and 833 fresh noneditable installed tests passed without skips. The 98 guarded recovery children, 11-root refusals, 18 edge substitutions and six decoded binding controls remain historical evidence. Source/test trees match that tested horizon; these suites were not rerun during this records-only A-phase entry. They do not establish semantic correctness, usefulness, learner ownership, complete lifecycle coverage or replay.

Historical implementation research and migration evidence were reconciled as non-controlling input: their live-value/legacy bridge and fixture routing are not production mechanisms to copy. Production codecs/storage now resolve part of their former cold-reconstruction gap; full-family and direct-consumer obligations remain.

### Why Stage 3 follows

The full target remains native producers/evaluators → canonical evolving Workspace → typed consumers → historical recovery and separately validated continuation. The missing cross-domain responsibility is now the host's lifecycle and authority path: preserve why work was requested/admitted, what was attempted/observed/evaluated, and whether its original material basis remains usable in a successor state.

Stage 3 joins those responsibilities around the existing native path and proven publication boundary. The concrete current anchor is the Python-support unresolved assessment → native investigation selection → exact-head declaration read → relevance/impact reassessment in `investigation.py`. Native owners keep assessment meaning. This is a production flow for integration evidence, without selecting a general Investigator or copying a fixture scheduler.

Expanding codecs first would grow completed-result coverage without resolving this host boundary. Early report cutover would risk suppressing the eleven remaining fields and absent lifecycle state. Stage 3 remains the coherent next responsibility; the exact in-process interfaces and modification/proof inventory belong in A2 and the subsequent admitted Build preflight. Additional lifecycle contract controls must disclose whether they exercise current normal flow, future accepted pressure or defensive misuse.

### Explicit scheduling override

```text
Circumstance/evidence — Stages 1–2 B/Verification are complete for their admitted scope;
Ali explicitly schedules their remaining D/E learning independently and requests the next A-phase.
→ Normal route — finish that cycle's D/E before entering the next substantive cycle.
→ Why worse here — redoing or waiting on separate ownership learning duplicates its owner
and blocks engineering whose prerequisites are already evidenced.
→ Override — initialize this separate Stage 3 engineering cycle through its normal A gates;
leave the foundation cycle OPEN and its D/E progression on the learning branch.
→ Effect — scheduling changes only; no closure/mastery claim, product proof expansion,
semantic/architecture change, branch merge, or premature Build.
→ Reconciliation — MEMORY.md owns main's new selection; this record owns its phase progression;
reconcile a material learning contradiction at the responsible owner before affected work.
```

The older main copy of the foundation cycle is read as its dated handoff. It is not relabeled CLOSED or replaced; updating its detailed D/E progression would compete with the branch Ali designated as its owner.

## Living A-phase orientation/learning map

This map supports the existing plan; it is not another execution or semantic owner.

**A1 continuity topics:** native capture versus a complete canonical investigation; durable publication versus execution history/current authority; supported projection coverage versus full report replacement; recorded proof versus fresh execution; independent D/E ownership versus this engineering cycle.

**A2 upcoming topics, after the continuity gate:**

1. Trace the real selected declaration-read/reassessment flow through the native owners, host admission, published attempt intent, observation/problem, owner evaluation and immutable successors.
2. Explain separate discovery objectives, proposition-relative needs, proposals/structural admission, views/observable use, evaluation outcomes and procedural termination/adequacy. Implementing their lifecycle cannot create missing evaluator or action authority.
3. Distinguish expected-predecessor publication from material-basis validity: preserve original target/revision/request/premises, allow unrelated same-target progress where valid, and refuse silent target or material rebinding. Material basis includes relevant input/candidate/scope/capability/method bindings; uncertainty or missing provenance stays explicit.
4. Locate the earliest sufficient owner of each admission/reference/validity check. Establish the minimal retained publication representation for unfinished lifecycle state and its explicit compatibility/refusal relationship with existing native checkpoints before code depends on it.
5. Explain the proof matrix: justified request versus executable admission; failed/empty/scoped-negative reads; duplicate versus contradictory delivery; unrelated/material same-target change; target movement; method/capability withdrawal; counterevidence and preserved prior assessment; unsupported semantic/adequacy evaluation; interruption after published intent without invented completion or retry authority.
6. Review acceptance and exclusions: reproducible native/host/lifecycle/publication integration plus offline historical-state inspection for the admitted path; focused then appropriate complete/installed regressions. General concurrency scheduling, full family coverage, synthesis/report cutover, user-facing continuation, replay, new evaluation methods and autonomous actions remain separately activated obligations. Their temporary exclusion retains product cost and later entry conditions under the existing plan.

**Ownership targets:** reason about useful evidence versus executable authority; explain why revision change alone cannot settle current material validity. These are orientation targets, not assessed mastery.

## A1 presentation and gate

The established foundation, its evidence/limits and the missing lifecycle responsibility were presented without repeating the independent native D lessons. Ali replied: "good and now we can go to A2". This clears the continuity gate and explicitly selects A2; it does not establish independent mastery of the foundation or clear the separate pre-B understanding gate.

## A2 orientation — real flow, ownership and proof

The admission/lifecycle/basis responsibility is clarified in the existing implementation plan, separating its subsection from later synthesis/report and recovery/continuation consumer migration. This is execution-boundary clarification under the accepted six stages and ADRs; no new semantic or storage-method owner is created. Main/origin remain aligned at the A0/A1 publication `1da3175b` on the A2 entry fetch; product trees are unchanged.

The concrete existing path is `impact.python_support`: a grounded support-drop candidate has an unresolved exact-target declaration proposition; `select_python_support_drop_investigation` selects `acquire_exact_target_python_declaration` for `pyproject.toml` at the candidate's exact head. Orchestration checks repository/head, calls the existing provider, interprets the declaration, evaluates target relevance, then reevaluates impact. Existing tests distinguish not-yet-acquired material from an attempted declaration problem; a recorded problem does not reselect the same acquisition. This normal path supplies the production integration anchor, not a universal discovery policy.

Upcoming B builds the Workspace-owned history/authority path around that sequence:

```text
native unresolved assessment and selection / proposition-relative need
→ exact capability request with retained original target, revision, scope and material basis
→ host admission/rejection under present capability/effects/authority
→ durable admission/attempt intent before the read
→ existing read and native interpretation, with actual observation/problem retained
→ result identity/current material-basis validation
→ existing owner reassessment and immutable successor with retained basis/history
```

Native owners retain factual/evaluation meaning; the Workspace owns cross-record identity/reference/history/current-basis relationships; the host owns executable admission; persistence owns atomic predecessor publication. New evaluation is explicit owner activity. Offline reconstruction reads historical results/history without provider/model/evaluator calls. A source read succeeding is not a support/applicability conclusion. Procedural finish is not an adequacy assessment; missing semantic/adequacy competence remains unsupported.

### Concrete representation and interface boundary

Inspected source shows `CapturedNativeBoundary` admits one record per native family, `NativeInvestigationCapture.snapshot()` requires completed staging, and `CheckpointRevision` currently carries only that native boundary. Repeated attempts and unfinished interaction history therefore require an explicit logical composition of native material and separately encoded typed lifecycle records. Reusing family slots as a changing global status or inventing native authority for host annotations would lose the accepted distinction.

The logical design is fixed at this depth: one canonical Workspace revision retains native closure plus lifecycle history and their scoped links; typed in-process views expose admitted consumer material; publication uses the existing private SQLite method. The concrete format/codec/schema support map must be reconciled before the first capture/store edit in B. Preserve explicitly tested old-format inspection/native support where supported, otherwise refuse affected reconstruction; do not silently reinterpret old formats or add automatic migration. Exact classes/table layout remain routine implementation choices under ADR-0012/0013, with a Planning/Design return if a consequential method departure is needed.

The primary code boundaries are existing orchestration, `workspace/` composition/capture/representation/projection/persistence, and native owner call sites/tests. Do not duplicate native acquisition/evaluation, introduce a second writable investigation, or add a framework/scheduler. Ordinary report behavior retains its current scope until full native coverage and consumer cutover earn replacement; no Stage 3 user-facing resume promise is made.

### Validity and failure model taught

Material basis means the specific native inputs, candidate/proposition, request meaning, scope and method/capability bindings on which work relied. A Workspace revision is the whole composed state; a material basis is the relevant dependency set. They are not interchangeable.

- An unrelated same-target CI/history addition need not invalidate a delayed declaration result. Exact target/result/request and relevant premises must still match.
- Changed candidate/source association, premise, scope or method cannot silently inherit an old assessment. Retain old history; validate/rebind explicitly or classify affected current use as stale/unsupported/unresolved as appropriate. A different head is a different exact target.
- Loss of current execution authority prevents a new read. It does not erase an already recorded historical observation or grant authority merely because an old admission exists. Current evidential use remains subject to its separate basis validation.
- Failed acquisition, successful empty result and scoped negative evidence remain distinct. Duplicate delivery is checked by request/attempt/result identity and content; it cannot become independent support. Contradictory content under one identity is an ingestion problem before semantic conflict evaluation.
- Published intent followed by interruption without retained completion leaves unknown completion. Do not invent a result or retry automatically. Failed/unconfirmed publication cannot authorize the capability to proceed from an unestablished admission boundary.
- Proposals/structural admission do not establish truth. Available, delivered, observably used, cited, evaluated support and sufficiency remain separate relationships; missing observable use remains unknown. Pre-candidate discovery objectives and proposition-relative needs stay distinct. Counterevidence retains earlier assessment and triggers the admitted owner's successor evaluation; no missing generic evaluator is replaced with a fabricated unresolved assessment.

### Acceptance, exclusions and ownership gate

Acceptance requires the real normal selected-read/reassessment path through the host plus cold retained native/lifecycle inspection and discriminating controls: admission/refusal, intent before execution, no operation after publication refusal/uncertainty, unrelated/material same-target change, target change, duplicate/contradictory identity, method/capability withdrawal, native/problem branches, counterevidence/unsupported assessment, views/omission/use truth, and unfinished attempt/procedural/adequacy state. Classify controlled future/defensive cases honestly; they do not establish production concurrency or Investigator competence.

Verification proceeds focused lifecycle/native/storage/normal orchestration tests → affected cross-owner regressions → full checkout and fresh noneditable installed regression for the material source change. Include guarded fresh-process offline reconstruction and interruption controls; static checks cannot substitute for these tests. Product source/test inventory and exact supported version map are Build preflight obligations, not proof already earned by A2.

Full family coverage, synthesis/report cutover, user-facing recovery/continuation, replay, new evaluators/discovery policy, concurrency scheduling, private data and external mutation remain later/separately admitted responsibilities. Their exclusion keeps Stage 3 coherent around lifecycle ownership while retaining all existing product facts and the explicit later gates. No claim of complete resumability, useful recommendations, semantic accuracy, power-loss durability or learner mastery follows.

Two pre-B reasoning opportunities: explain why unrelated same-target progress differs from a material premise change for a delayed result; explain what published attempt intent without recorded completion proves and what is needed before another execution. A2 remains CURRENT until Ali has had the orientation/challenge opportunity and its understanding gate is addressed. Build has not begun.

## Record-increment validation and handoff

Validation for this A0/A1 increment: both changed documents pass 26 local link and three anchor checks, balanced fences and phase/live-owner consistency. All nine governance functions ran: eight pass; only the inherited root `examples/` owner-marker mismatch remains. Whitespace passes. Product source/test Git trees remain identical to the verified foundation; no runtime tests were rerun and no Stage 3 Verification result is claimed. Publication scope is this cycle record and MEMORY.md only under the standing commit/push cadence; the unrelated untracked audit record is excluded.

The preceding validation is the A0/A1 increment's historical evidence. The A2 update changes only this record, MEMORY.md and a position-neutral clarification of the existing implementation plan. Final scope checks pass: three documents, 69 local links, seven anchors, balanced fences, phase/live-state alignment, identical product source/test trees and whitespace. All nine governance checks ran: eight pass, retaining only the inherited root `examples/` owner-marker mismatch. No runtime product test is required or claimed for this orientation-only increment. Accepted specification/ADR methods and the independent learning branch were not changed.

As of the A2 handoff, STOP at the separate pre-B understanding gate. A1 is DONE, A2 is CURRENT, B/Verification/D/E remain PENDING. The independent foundation D/E work continues without a timing dependency. Main's current selection is owned only by MEMORY.md.
