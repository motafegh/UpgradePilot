# Workspace lifecycle, host admission and material-basis validity — LbD cycle

**Initialized:** 2026-10-13 20:30 Asia/Tehran.
**Session status:** ENGINEERING HANDOFF CLOSED through E on 2026-10-14 under Ali's explicit scheduling override; Stage 3 D and learner-ownership closure remain DEFERRED to a separate learning session. This is not an unqualified full learning-cycle closure.
**Engineering continuation:** [Common Investigator native inputs/source interfaces cycle](2026-10-14_2345_common-investigator-inputs-and-source-interfaces_lbd-cycle.md); this record retains the deferred Stage 3 learning/ownership responsibility.
**Primary operation:** authorized Build/Implement for the admitted Stage 3 responsibility, following completed Planning/Design reconciliation.
**Previous engineering foundation:** [Stages 1–2 cycle](2026-10-10_1552_workspace-native-capture-reconstruction-and-publication_lbd-cycle.md). Its remaining D/E progression is independently owned on `learning/d-native-ownership-2026-10-10`; this record does not take it over.
**Owners:** [live position](../MEMORY.md), [implementation/migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md#technical-stages-and-cycle-boundaries), [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [Core §6.4](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation), [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md), [Operating Guide](../OPERATING_GUIDE.md).
**Procedures:** `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`; `UP-SKILL:upgradepilot-build-implement`.

## Cycle status

```text
Cycle — Workspace lifecycle, host admission and material-basis validity
A0 — DONE: current main/owners/source/tests/proof reconciled; record and living A-phase map initialized.
A1 — DONE: Ali accepted the current-state model and explicitly requested A2; no independent D/E mastery inferred.
A2 — DONE for action entry: Ali explicitly adopted the reviewed sequence; two reasoning checks remain deferred to D, with no independent mastery claim.
B — DONE: generic host/current authority, published intent, outcomes, native reassessment, partial capture and material validity integrated through the normal selected-read caller; readiness disposition recorded.
Verification gate — GREEN for admitted Stage 3: 25 host tests; 875 checkout and 875 fresh-installed tests; 92 source/installed hashes match; historical compatibility and guarded normal-path interruption/restoration pass.
D — DEFERRED by Ali: separate evidence-backed learning/ownership session; both A2 reasoning checks remain unassessed.
E — DONE for engineering handoff under the recorded scheduling override: proof/non-proof, deferred learning and next responsibility consolidated; learner-ownership closure remains pending.
C — DONE for this engineering handoff: meaningful progression preserved; any later D findings must reconcile this record and the responsible owner.
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

## Pre-B AI/LLM engineering relationship review — 2026-10-14

Ali asked whether current and future work should include the LLM/AI engineering already explored under experiments, and requested checking/deciding before coding. This is a bounded read-only Repository Audit with Planning/Design judgment inside A2; it does not clear the pre-B gate or activate implementation/model runs. The dated findings below preserve C; no plan/specification/ADR/live-position owner is changed by the recommendation.

**Inspected horizons:** main `1297d729`, aligned with fetched origin; broader-agency research local/remote `253b48de`, inspected in its existing worktree without moving or editing it. The independent native D/E learning stream was not reopened. Source, selected tests and public-safe dated evidence were inspected; no runtime tests, provider inventory or inference were run. Existing test/model counts below are historical recorded results, not new executions. AST inspection finds 87 product Python files with no imports from experiments/tests/tools/LangGraph/LangChain; LangGraph remains an experiment dependency group.

### Evidence-backed classification

| Work | Implemented/evidenced responsibility | Consequence for this decision |
| --- | --- | --- |
| Accepted product support-drop extractor | [ADR-0006](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md), [extractor](../src/upgradepilot/upstream/support_drop_extractor.py), [runtime bridge](../src/upgradepilot/upstream/support_drop.py) and normal orchestration already compose one local structured-output extraction, exact source-line recovery and mandatory native candidate validation. Accepted historical evidence is bounded to this semantic role. | Main already includes actual LLM engineering. Preserve this owner and its scoped meaning; Workspace work is not a replacement for it or adoption of a general interpreter. |
| Bounded EvidenceGapPlanner, ordinary Python and LangGraph | [Model-visible context/strict decision boundary](../experiments/evidence_gap_planner_model_boundary.py), [fresh action admission](../experiments/evidence_gap_action_admission.py), [local transport](../experiments/local_evidence_gap_planner.py), [graph workflow](../experiments/langgraph/evidence_gap_workflow.py) and their tests separate untrusted selection from executable authority. The September 6 real pydantic proof records model selection, admitted exact read, native reassessment and normal-path parity; controlled four-scenario comparison records parity. | Retain reusable boundary ideas/control evidence. A single offered action proves the seam, not general planner advantage or framework adoption. The existing comparison plan explicitly withholds general ADOPT and leaves broader disposition/framework investigation separately owned. |
| Broader Fixed/Agent and H1 laboratory | Research `SourceWorkspace`, bounded source tools, trial budgets/tool receipts, typed references and model proposals exist on the separate research branch. Contract-2 public source reviews record 8/8 mechanically valid reports and 0/8 advice-ready in assisted two-known-case review. H1 is a design-only raw-navigation versus structured/native-fact comparison on a common main-owned lifecycle. | Useful discovery/tool/context/evaluation pressure should enter main's contract/proof. No demonstrated policy winner, generic adequacy method or accepted product Investigator is available to copy. Research source maps/transcripts remain laboratory state, not canonical Workspace. |
| Source-only API interpretation | [Versioned interpreter](../experiments/api_change_interpretation.py), saved-trial/evaluation machinery and [reviewed v2 comparison](evidence/2026-10-06-api-interpretation-contract-repair/README.md) preserve exact refs, context/completion capacity, whole-set meanings and historical roles. Gemma and MiMo both remain FAILED/REVISE despite clean mechanical delivery. | Repair/evaluate this semantic responsibility separately when selected. Better retrieval/storage or schema validity cannot by itself establish API meaning, target applicability or action permission. |
| Workspace seam experiments | [Typed seam](../experiments/workspace_investigator_seam.py) and [its tests](../experiments/tests/test_workspace_investigator_seam.py) exercise view/request/admission/attempt/result/proposal/evaluation separation, omissions/use, counterevidence, validity and recovery. Routing/semantic-owner stimuli are controlled, not a production general Investigator/evaluator. | These are direct Stage 3 requirements and oracle ideas under accepted owners, not code to import or fixture policy to promote. The preceding native/storage research already supplied evidence for the now implemented foundation. |

The prior A2 explanation foregrounded operational state/publication. Its accepted scope already includes AI-facing views, proposals and admission, but it did not make the experiment-to-product bridge explicit enough. The review sharpens that explanation; it does not infer that more infrastructure alone solves semantic failures.

### Engineering recommendation for Ali's review

1. Keep Stage 3 as the next coherent responsibility, with an explicit AI-facing acceptance lens: bounded native/source context views and truthful omissions; untrusted request/proposal submission; fresh host binding/admission; recorded attempts/results; evaluator availability/support boundaries; retained actual method/model/contract identity where available and explicit metadata gaps otherwise. Test malformed/authority-bearing proposals, context/reference limits, stale/material changes, no execution after rejection and procedural finish without invented adequacy. Use ordinary synchronous orchestration as the simpler baseline under the accepted method; no live model policy or framework is adopted by these tests.
2. Preserve broader native content/addressability instead of freezing human report summaries as maximum model context. H1's proposal-level evaluation does not require a nonexistent generic semantic/adequacy evaluator, but cannot claim evaluated generic applicability or justified stopping without one. Do not fabricate extra actions or deterministic semantic answers to create an agent comparison.
3. At Stage 3 verification, explicitly review readiness for the main-owned Investigator-mechanism seam under the implementation plan's existing trigger. Reconcile H1's G1/G3/G4/G6 interfaces against the real product contract; identify G2 common provenance/native-input closure and G5 evaluator limits. G7's accepted architecture/recovery status has advanced since the dated proposal; G8 requires coordinating the older bounded-planner/framework obligations. A reproducible supported seam can justify a separately authorized local-only integration/comparison before all later migration stages are finished. If required material is absent, name the exact coverage/preparation dependency and re-entry condition instead of postponing all AI work until unspecified Workspace completion.
4. Subsequent model selection/context/prompt/tool-loop work earns its own frozen claim, baseline, common inputs, versioned methods, measured resources and semantic/usefulness evaluation. Treat the source-only semantic repair and Investigator discovery/planning comparison as distinct responsibilities. Revisit LangGraph/LangChain against real orchestration pressure and the ordinary-Python baseline; existing experiment code/dependency or one successful case is not adoption authority.

**Decision boundary:** this is a recommendation, not an adopted model/framework, authorized H1 run, rewritten plan or cleared Build gate. Existing implementation-plan §6 already owns the follow-up trigger and requires explicit disposition; a new competing AI roadmap is unnecessary. If Ali chooses a changed live scope/sequence, reconcile the existing owners and A2 proof boundary before affected B. Product, research, mechanical, semantic and learner-ownership claims remain separate.

**Review verification:** only this dated cycle record is changed. All 27 local links, two anchors, balanced fences, phase consistency and diff whitespace pass. Product/test/experiment trees, plans, accepted owners and MEMORY.md are unchanged; no model execution or fresh test result is claimed. Procedure provenance: `UP-SKILL:upgradepilot-repository-audit`; existing Planning/Design, Learning-by-Doing and Working Memory procedures remain composed.

## Formal sequence adoption and Build entry — 2026-10-14

Ali replied: "Good and I agree with you lets go for your recommended sequence formally". This explicitly adopts the reviewed engineering sequence and directs progression through it. Formal reconciliation belongs in the existing implementation/migration plan and MEMORY.md; no competing AI roadmap, new ADR or laboratory run is created. The plan now carries the AI-facing acceptance/proof matrix and the lifecycle-verification readiness decision, including ready/named-prerequisite/defer/reject/reschedule dispositions and the subsequent protocol-freeze boundary.

### Action gate and learning evidence

The full A2 responsibility/flow/proof orientation and subsequent AI relationship challenge were presented before this instruction. Treat Ali's explicit direction to proceed as clearing the action gate. It is not independent reasoning/ownership proof. The material-validity and interrupted-attempt reasoning checks remain deferred core learning for D/E of this cycle; they were not answered or marked passed.

This is an explicit proportional cadence adaptation under the Smart Situational Override Rule: normal pre-B handling would seek the reasoning responses now; Ali has instead reviewed/challenged the upcoming responsibility and explicitly selected proceeding with the formal sequence. Requiring another approval would repeat his direction without adding engineering authorization. Proceed into entry preflight while preserving the deferred reasoning and requiring its repair/defer disposition in D/E. Scope, proof, native authority and later model-run gates do not change; independent Stages 1–2 D/E remains separate.

### Concrete entry responsibility

Build begins with the source-grounded publication representation and compatibility inventory required by the already reviewed A2 boundary. Current `CheckpointRevision` contains only `CapturedNativeBoundary`; native capture seals at completion and the boundary admits one record per native family. The new host must compose native material and separately encoded immutable lifecycle history with explicit references and supported-version handling. No routine implementation choice may silently reinterpret an existing format, manufacture native meaning, permit retry or create a second writable investigation.

Entry proof remains bounded: inspect active source/test constructors, storage schema/digest/read/backup assumptions and native projection/capture call sites; choose the simplest coherent composition under ADR-0012/0013; record exact old/new support/refusal and focused/broader test scope before executable edits. A material new method/semantic ownership question returns to Planning/Design at its proper owner. Live model runs, a general Investigator policy, framework adoption and future semantic-method repair are not part of this formal adoption increment.

**Formal increment verification:** validate changed plan/live/cycle links/anchors/fences, action-gate versus mastery/proof state, position-neutral plan ownership, unchanged accepted methods/source/tests and whitespace. Preserve actual outcomes before publication; documentation verification does not establish Stage 3 behavior.

### Source/test entry preflight and observed baseline

The Build/Implement procedure is active for entry preflight (`UP-SKILL:upgradepilot-build-implement`). ENVIRONMENT.md confirms the WSL checkout interpreter route. The inspected native capture/boundary, checkpoint revision/store, native projections and selected-read orchestration expose this concrete modification/proof inventory:

| Boundary | Preserved responsibility | Stage 3 change/proof consequence |
| --- | --- | --- |
| Native capture | Actual supplied owner inputs/results, one producer sequence and final completion seal. | Add declared coherent progress publication through explicit composition; retain the completed-capture contract and refuse fabricated completion. |
| Native envelope/projections | Fixed owner/type/version, one record per family, exact target/material closure and offline typed native reconstruction. | Native family bindings remain native; separately owned lifecycle history must preserve its own references/version/outcomes instead of masquerading as another native assessment. |
| Revision/digest | Lineage/revision/predecessor identity bound to encoded material. | Compose the new lifecycle closure into the declared publication identity; retain an explicit old/new representation support/refusal map. Current digest meaning cannot silently change for old retained data. |
| SQLite store/backup | Explicit schema 1/catalog, 1..4096 native records, immutable records/membership, coherent predecessors, commit-before-acknowledgement and validated backup. | Preserve this method and its corruption/interruption controls; an incompatible lifecycle layout needs an explicit supported schema/format boundary, without automatic migration or hidden retry. |
| Normal native read | Mechanism-specific unresolved declaration selection, exact repository/head/path, one acquisition and native relevance/impact reassessment. | Insert host admission and durable attempt intent before the selected read; retain real outcomes/evaluations and their basis. Protect original native no-reselect/problem behavior and existing report scope. |

Source inspection confirms current schema/format support is native-only version 1. This is the old-support inventory, not a selected or implemented new layout. The immediate source task is to finish the concrete versioned native/lifecycle composition under these owners, with old checkpoint inspectability/native support or explicit affected refusal, and then implement the admitted host path. Keep missing old lifecycle/method metadata explicit; do not backfill it as recovered state. No new substantive method conflict was found in entry preflight.

Fresh preflight execution on unchanged product source/test trees:

```text
PYTHONPATH=tests:src .venv/bin/python3 -m unittest
  test_workspace_checkpoint_store
  test_workspace_checkpoint_publication_coherence
  test_python_support_impact
→ 49 tests PASS in 8.213 s, no skips.
```

This verifies the selected existing storage/publication/native baseline, not new Stage 3 functionality. Full checkout/fresh-installed suites were not rerun for formal plan adoption; the October 11 132/833/833 result remains separately recorded historical evidence. No source/test/experiment changes, live-model calls or provider inventory occurred. The formal increment checks pass for three changed documents, 81 local links, seven anchors, fences/phase/action-gate/proof/owner consistency and whitespace. All nine governance checks ran: eight pass; only the inherited root `examples/` owner-marker mismatch remains.

**Formal adoption handoff:** the agreed sequence is now controlling execution coordination in the existing plan, with Build entry selected in MEMORY.md. B remains at representation/compatibility entry work; implementation and its Verification gate are incomplete. D/E and the readiness decision remain owed at their stated boundaries, and the deferred A2 reasoning is preserved. This increment publishes formal selection and an observed baseline, not lifecycle completion.

## Native/lifecycle publication implementation — 2026-10-14

Ali requested proceeding properly with the next coherent task: versioned publication containing native material and lifecycle history, explicit old-checkpoint handling and coherent cold reconstruction/refusals, before host-path wiring. Main/origin begin aligned at `8edfc64e`; the unrelated untracked October 3 audit record remains excluded. This is the first internal B publication boundary of the same Stage 3 cycle, not a smaller substitute for its full host responsibility.

### Chosen support and ownership map before integration

- Keep schema-1/native-only publication, its exact original digest and retained native codec support. Missing lifecycle history is explicitly `not_retained`, never invented empty/resumable state. Existing old stores are not migrated.
- Explicit `CheckpointStore.create(..., schema_version=2)` selects the additive private SQLite layout for lifecycle bodies and ordered revision membership. Native table/digest semantics stay compatible. An explicit empty lifecycle history is a composed revision and cannot be silently downgraded to a native-only successor.
- Immutable lifecycle envelopes retain scoped identity, original basis revision/native references, predecessor interactions, payload/kind/codec digest and supplied method/model/contract/configuration identity or unknown/gaps. A closed 12-kind codec preserves objectives, needs, requests, admissions, attempts, observations, evaluation outcomes, views/use, attributed proposals, termination and stopping proposals. No arbitrary class paths or evaluator calls are dispatched.
- Publication validates original native membership against the selected revision/ancestors in the same snapshot, causal identity closure, immutable cumulative history and native/lifecycle identity separation. Current material validity and present capability authority are distinct later host responsibilities. Encoded storage inspection preserves unsupported lifecycle codecs; separately typed reconstruction refuses affected unsupported/invalid history and validates known causal/representation relationships.
- Typed historical evaluation links admit the assessment-bearing roots in the existing CI/Python native ledger. A raw input cannot become an assessment through an owner label; native domain assessment cannot become canonical adequacy. Observation scope stays bound to its admitted request; observable-use receipts cannot claim omitted material. These are cross-record representation/authority-separation checks, not a semantic or adequacy evaluator.

This adds no dependency, framework, alternative acquisition path, automatic migration/retry or model execution. Native capture still seals normal completed investigations; production host/partial-progress capture integration follows the publication proof and remains owed. Lifecycle stimuli in the new tests are admitted boundary controls alongside real controlled native captures, not claimed production interactions or model-policy acceptance.

### Implementation evolution and focused evidence

The existing 49 storage/publication-coherence/Python-support tests pass after the initial source extension (8.619 s). The first 12 composed-publication tests pass in 5.080 s. Source inspection then added specific refusal/bounds controls for wrong observation scope, raw-input/stop authority inflation, malformed known payloads and combined native/lifecycle read size before lifecycle allocation. The resulting 16 tests pass in 5.511 s; broader/native/installed gates remain pending at this point.

The new tests compare all declared lifecycle fields against original pre-encoding stimuli and complete native projections in fresh store-selected readers. Eleven recovery children each exercise four provider/model/native-evaluator/synthesis entry refusals plus a network refusal. Five publisher children receive staging inputs and are actually SIGKILLed after a lifecycle body, lifecycle membership, head update, before commit and after commit; only the declared intact original or committed successor is recovered. Unknown acknowledgement is reconciled by the complete composed identity. These process controls do not establish power-loss guarantees or exactly-once capability effects.

Checkout Ruff was absent. A fresh temporary tool installation outside Git (`/tmp/upgradepilot-lifecycle-lint.xRapNH`, Ruff 0.17.0 from public PyPI) supplies lint/format verification without changing project/runtime dependencies. Initial lint reported formatting/import/test-helper issues; these were corrected locally. This is tooling preparation, not a missing runtime-proof substitute.

**Remaining proof at this point:** final touched-source inspection/lint; broader native/storage/orchestration regression; full checkout and fresh noneditable installed suite with source-origin/hash checks; independent old-source schema compatibility/refusal control; final owner/document reconciliation. The Stage 3 Verification gate and D/E remain pending even when this publication increment is sufficiently verified.

Final source inspection also exposed an aggregate original-basis read issue: individually bounded revisions could accumulate across many referenced historical bases. Before loading another basis, the store now checks combined retained body sizes against the 64 MiB encoded-material admission bound. Distinct bases are conservatively charged separately, including shared native bodies; this is neither a total history cap nor a Python heap guarantee. The plan owns the support limit and review trigger; capacity excess refuses without trimming history. A discriminating pre-allocation control brings the publication suite to **17 tests PASS in 5.649 s**. The final broader native/storage/orchestration selection passes **149 tests in 103.137 s**, no skips.

An independent compatibility control archives pre-change `8edfc64e:src` outside Git and asserts actual imported origins. That source writes a genuine schema-1 store; the current guarded fresh reader recovers unchanged digest and complete native projection parity with lifecycle `not_retained`. The old source separately refuses a current schema-2 store as `unsupported_storage_schema`; the database hash is unchanged. Four forbidden provider/model/native-evaluator/synthesis entry controls plus network refusal are exercised in this extra recovery child. No old-source Git dependency is added to permanent tests.

Local temporary proof root is `/tmp/upgradepilot-lifecycle-proof.LJqq65`: compatibility script/result, exact 89-file source manifest, full-test logs, isolated package source and noneditable installation. Before the installed suite, actual `upgradepilot` origin is inside that environment's `site-packages`; all 89 installed/source Python hashes match, pip check and installed console/module help parity pass. The final touched-source Ruff check/format and diff whitespace pass. AST dependency-direction review of all 89 product Python files finds no imports from tests/experiments/tools or agent frameworks. All nine governance functions run: eight pass, with only the inherited missing `examples/` root-owner marker; an ad hoc result assertion initially used different wording for that known diagnostic, without changing the actual checker outcomes.

### Verified publication increment and internal handoff

Final source is unchanged from the 89-file package manifest. Full checkout passes **850/850 tests in 103.211 s**; the fresh noneditable installed suite, run outside the repository with only the test directory on `PYTHONPATH`, passes **850/850 in 103.792 s**, no skips. Actual installed origin, all 89 source/installed hashes, pip check and console/module help parity pass again after the suite. Final source/diff review confirms closed codec dispatch, immutable cumulative history, original basis membership, schema-1 digest compatibility, separate typed support/refusal and transactional native/lifecycle publication. Three touched documents pass local-link/anchor/fence and phase/proof consistency checks; governance retains only the inherited root-marker debt. No hosted verification or live model/provider run is claimed.

**What this establishes:** a declared composed checkpoint can preserve and recover supported native material plus attributed lifecycle interactions, their original bases and explicit method/retention gaps. Saved admission/attempt/proposal/termination records remain historical facts; they supply no current execution, semantic support or adequacy authority. Native-only history remains honestly absent; explicit empty history is different. The separate typed decoder can refuse unsupported lifecycle material while unaffected native projections remain inspectable.

**What remains:** same-cycle Stage 3 B must integrate coherent partial capture and host admission/attempt-intent/observation/native reassessment on the existing normal selected-read path, evaluate original-versus-current material validity and preserve AI-facing view/request/proposal/use/termination limits with normal-path proof. This boundary's lifecycle events are controlled inputs, not evidence that that host path exists. Complete Stage 3 verification, its explicit Investigator-readiness decision and D/E (including deferred A2 reasoning) remain pending. The independent foundation D/E is unchanged; no second cycle, framework, model protocol or consumer cutover was selected.

## Generic host integration — 2026-10-14

Ali explicitly continued the full admitted Stage 3 responsibility, requiring a future-general host rather than a Python-specific lifecycle. The existing declaration-read selector/evaluator is its first real production caller/proof, not the architecture. D/E and deferred reasoning stay pending until sufficiently verified Stage 3 behavior; the readiness decision follows complete lifecycle verification, without launching model work.

Reconciliation starts at aligned `dd3affa8`. The generic host owns trusted capability/effect/scope installation, present admission, immutable intent before execution, actual observations/interruption and current validity. Native capture owns coherent partial encoded progress without declaring completion; domain owners still process once. The normal production caller uses the same generic host with volatile CheckpointRevision publication by default and an explicitly supplied schema-2 store for durable acknowledgement before effects. No implicit checkpoint location/user-facing recovery is introduced. The legacy report fields remain pending full-family/direct-consumer migration, with the immutable Workspace revision exposed separately.

Inspection requires observation codec v2 to retain returned content even when the subsequent native evaluator fails; observation v1 keeps its exact layout/support. A distinct generic interruption kind preserves known interruption with unknown external completion. These are supported format additions, not reinterpretation, migration or new semantic authority. Repository acquisition uses a generic exact-file adapter to the existing provider; no Python role enters host/capability policy. Present material validation compares transitive original native references, exact target, scope and installed method/capability independently of revision equality; unrelated same-target progress may remain valid.

The first focused regression exposed five no-grounded-claim closure errors after making partial capture explicit: a recorded relevance result referred to a pending placeholder identity that was refreshed afterward. Pending input references now refresh before recording a result; executed records retain actual captured inputs and cannot be silently rebound. This correction preserves the original evaluator path and immutable identities. Subsequent focused/normal-path and complete verification are still required; no Stage 3 acceptance or ownership inferred at implementation entry.

Focused evolution reaches 22 host tests: normal acquisition/native reassessment and normal absent/problem/empty/unresolved branches; generic scope/effects/current-authority/delayed-result controls; immutable original bases and unrelated/material/head/method/capability variation; malformed/authority misuse, duplicate/contradictory observations and multiple admission receipts; unknown completion/no automatic retry; views/use/proposals/unsupported conflict and adequacy; schema-1 refusal; actual normal-path process interruption plus guarded host restoration. Generic controls are disclosed future-interface/defensive proof, not new Python/Rust/domain capability claims. The final focused host run passes 22 tests in 15.235 s. The broader native/storage/orchestration selection passed 171 tests in 122.096 s before final selector/provider provenance clarification; full final-source suites remain required.

Inspection tightened two real contracts before broader acceptance: installed effects are retained in the capability identity (same name/method cannot conceal changed effects); executing either of two live admission receipts consumes the request once, so the other cannot duplicate acquisition. Needs are attributed to the native selector; only trusted composition registers purposes, while model suggestions remain proposals. The repository adapter records its actual method and any available injected-provider method, preserving unknown provider/version/authentication metadata as gaps rather than claiming the standard provider ran.

The first full checkout executes 872 tests but has 13 failures solely in new child launchers: discovery supplies the parent test-import path, which `PYTHONPATH=src` does not transmit to children. The focused command included `tests:src` and concealed that assumption. Child environments now explicitly include only the fixture directory plus inherited paths; installed proof must never add checkout `src`. A subsequent missing import in that test-only environment helper was corrected before rerunning. No product validator or semantic expectation was weakened; the complete verification gate remains pending until fresh passing discovery/checkout/installed evidence.

Historical compatibility is independently observed against actual archived `dd3affa8` source/tests with imported origins asserted. Its schema-2/v1 history recovers under the current guarded reader with unchanged digest/native parity and no invented retained observation content. Its old reader refuses current observation v2 as `unsupported_lifecycle_codec` while recovering complete unaffected native projections. Both children exercise four forbidden entry controls and network refusal; the database hash stays unchanged. Temporary script/result/source/package manifests live under `/tmp/upgradepilot-host-proof.kQmxZN`; this adds no historical-Git dependency to permanent tests.

Discovery-mode host proof passes 22 tests in 14.973 s after repairing the child environment; full checkout then passes 872 tests in 123.098 s. Final inspection reproduced a missing-history refusal when admitting a stale request: rejection used its original references against the current native revision. Rejection now retains the request's original basis, so it is publishable without rebinding old premises. Additional controls check authority withdrawal during intent publication, lost intent acknowledgement and competing head advancement before execution. Authority is rechecked after acknowledged intent; known non-execution is retained distinctly from external completion unknown. A changed declared head refuses execution for publication reconciliation, while independent material comparison still marks unrelated progress valid; there is no automatic merge/retry. Unknown references have explicit refusal. The resulting 25 host tests pass in discovery mode in 16.257 s; hardened full checkout/fresh-installed verification remains pending at this point.

### Final Stage 3 verification

Final hardened checkout passes **875/875 tests in 123.508 s**; a rebuilt fresh noneditable package, tested outside the repository with only the test directory on `PYTHONPATH`, passes **875/875 in 123.983 s**, no skips. All **92 source/installed Python hashes** match before/after; actual site-packages origin, pip check and console/module help parity pass. Tested source tree is `003a104db2f467664321da7195fb6560e0db9a5d`; test tree is `87bd762d75d16ce2b354c20d0a7c2fb6de4c281d`. Final source stays identical to the package manifest. Touched Ruff/format, dependency direction/generic-host checks and whitespace pass. Document/phase/link checks pass; all nine governance functions run with eight passing and only inherited root `examples/` marker debt. Final archived-source compatibility controls pass again on this source. Logs, manifest, install and compatibility controls are retained locally under `/tmp/upgradepilot-host-proof.kQmxZN`.

The normal path proves real product orchestration/native ownership with controlled provider and semantic ports: acknowledgement precedes the exact provider read, acquisition occurs once, the native impact owner executes pre/post once each, actual source is retained before interpretation, its reassessment is published and native projections survive cold restore/backup. Overlap, unresolved, unavailable and empty responses preserve their native meanings; native owner failure leaves the actual returned source and failed evaluation inspectable. No-candidate/dependency-problem branches retain unperformed native work. These are controlled product-composition proofs, not live public acquisition, independent model semantics or usefulness evidence.

Sixteen new guarded readers restore from store/selection only and exercise actual host restoration, historical admission refusal and attempt-completion distinctions, under four forbidden entry controls plus network refusal each. Four publishers run the normal production path and are SIGKILLed before intent, after intent, after observation or after native evaluation; provider-entry markers and selected cold boundaries discriminate actual entered/unentered work. Two additional guarded historical-source compatibility readers retain unchanged/native-only meanings and explicit v2 refusal. Generic/delayed/defensive controls separately prove original material closure, unrelated progress, method/scope/effect/capability withdrawal, duplicate/contradictory results, denied execution, lost receipts and competing heads. Process interruption establishes neither power-loss durability nor exactly-once external effects.

### Investigator-integration readiness decision

**Disposition: NAMED PREREQUISITE — common H1 native-input and source-capability preparation.** The main-owned canonical seam is available; the separately owned [H1 design at research `253b48de`](https://github.com/motafegh/UpgradePilot/blob/253b48de20b475eada48810d193bd420c51aa7d4/proposals/2026-10-08_H1_WORKSPACE_INVESTIGATOR_INTEGRATION_EXPERIMENT_DESIGN.md) is inspected as a proposed consumption requirement, not promoted or executed. Its old claim that main has no Workspace API/proposed-only recovery owners is superseded by accepted ADR-0012/0013/Core and the verified host. Neither research worktree nor independent foundation D/E is changed.

| Required interface/evidence | Tested product offering | H1 consequence |
| --- | --- | --- |
| Revision/target/basis and lifecycle (G1/G6/G7) | [Host](../src/upgradepilot/workspace/lifecycle_host.py), immutable schema-2 publication, [material validation](../src/upgradepilot/workspace/material_validity.py), offline native/lifecycle reconstruction. Historical admission supplies no execution authority; original bases are never rebound. | The absent-seam blocker is resolved. Recovery/replay and user-facing continuation remain separate; H1 can use the canonical host rather than emulate Workspace. |
| Purpose/view/request/proposal and operation trace (G3/G4) | Native owner supplies genuine needs; trusted composition admits objectives; typed bounded native views retain delivered/omitted IDs and limits; adapter use receipts, attributed proposals, host admission/intent/result/duplicate accounting and termination are separate. | Both arms need a common frozen wire/reference/packing and accounting bridge. Model suggestions cannot install purposes, methods, observations or execution authority themselves. |
| Native families and actual inputs (G2/G4) | Eleven CI/Python roots retain PR/changed-file/dependency/source contexts, workflow/run/job/source inputs, CI/runtime results, upstream association/claim and declaration/relevance/pre-selection/post assessments. Supplied source content is retained; unsupplied acquisition/call metadata remains explicit gaps. | H1 CASE_SPECS/text diffs do not supply validated PR/changed-file metadata and sufficient workflow/release/tag inputs. Map genuine common inputs for each offered family, or explicitly exclude that family/claim. A raw-text-only arm is not proof of the structured-native-fact hypothesis. |
| Source scope/format/capability (G4) | [Exact repository-read adapter](../src/upgradepilot/workspace/repository_read_capability.py) uses normalized paths at the admitted target head, preserving bounded UTF-8 and actual empty/problem outcomes. Generic host can register separately admitted capabilities. | Frozen source listing/search, upstream pinned-source/reference resolution and raw RST fallback required by H1 are not offered by this first target-head adapter. Qualify the exact common source bridge or select an explicitly supported narrower comparison before runs; do not invent a research parser/truth engine. |
| Evaluation and adequacy (G5) | Existing native Python relevance/impact methods keep bounded meanings and receive full owner inputs independently of citations. General semantic/API/refinement/conflict/adequacy methods are absent; outcomes remain unsupported/failed/stale, and procedural finish grants no action/stop truth. | External proposal-quality review may measure attributed proposals with these limits. It cannot establish generic applicability, canonical adequacy or action permission. Source-only API semantic repair stays separately selected. |
| Method/resource and experiment coordination (G4/G8) | Actual adapter/available provider identity, native-selector/evaluator identities, effects and configuration are retained with unknown version/model/authentication metadata explicit. Existing synchronous host is the product baseline. | Common budgets, prompt/schema/tools, local deployments and semantic/usefulness protocol still require separate freeze/qualification. Older B2/X1/planner/framework mechanism obligations are retained for explicit coordination in that preparation; H1 neither completes nor activates them, and no LangGraph/LangChain adoption occurs. |

**Smallest re-entry evidence:** prepare a case-by-family matrix with genuine PR/change/dependency/workflow/release/tag/source provenance and explicit unsupported rows; a main-owned common source/reference and native-view bridge for both arms; exact offered effects/formats/methods, operation accounting and refusal canaries against this tested seam. This is a bounded preparation/interface responsibility, not an unspecified wait for full Stage 4–6 migration. If the selected comparison needs an absent native family, identify that exact Stage 4 expansion and affected claim. Once those prerequisites are evidenced, separately select/freeze the local comparison and qualification protocol before any model runs.

**Verification-boundary handoff (before the E scheduling decision below):** Stage 3 B/Verification are complete for the declared supported host/native scope. D/E remained pending at that boundary, including both deferred A2 reasoning checks; no learner ownership was inferred. Full-family/direct report/synthesis cutover, user-facing continuation, replay, general semantic/adequacy competence and independent usefulness remain separate obligations.

## E engineering handoff and explicit D deferral — 2026-10-14

Ali explicitly requested deferring D to another session and proceeding with E and the next engineering-cycle decision. Reconciliation fetched `origin/main` and confirmed exact alignment at `9d394819`, the verified product horizon. Only the unrelated untracked October 3 audit record is outside this increment. The Stage 3 source/test tree identities still match the final verification above; no new product execution or learning assessment is claimed.

### Scheduling exception and ownership disposition

```text
Circumstance/evidence — Stage 3 B/Verification are green for the admitted generic-host/native
scope; Ali explicitly defers D and asks for E and the next engineering responsibility.
→ Normal route — complete evidence-backed D, then repair/defer its identified gaps in E
before closing the cycle and entering the next responsibility.
→ Why worse here — requiring D now contradicts Ali's scheduling choice and needlessly
couples evidenced engineering progression to a separately scheduled learning session.
→ Override — complete E's engineering handoff and explicitly defer D, both A2 checks
and learner-ownership closure; allow the next responsibility to enter its own A-phase.
→ Effect — engineering handoff is closed; full learning-cycle closure and mastery are
not claimed. No evidence, architecture, capability scope or Build gate is weakened.
→ Reconciliation — keep the learning debt in this single cycle record and its compact
status in MEMORY.md; reconcile a material learning contradiction before affected work.
```

The deferred Stage 3 learning is retained here for a separate session; no destination agent, task or branch has been selected or contacted. The existing `learning/d-native-ownership-2026-10-10` branch continues to own only the independently scheduled foundation learning; this E decision neither assigns Stage 3 learning to it nor changes its records.

| Deferred learning / ownership question | E disposition and re-entry evidence |
| --- | --- |
| Why unrelated same-target progress differs from a material premise change for a delayed result. | Original A2 reasoning check remains unassessed. D must use the verified host/material-validity controls and distinguish original basis, current use and publication predecessor. |
| What published attempt intent without recorded completion proves, and what is needed before another execution. | Original A2 reasoning check remains unassessed. D must use actual interruption, known non-execution, lost-acknowledgement and historical-admission refusal evidence; no automatic retry authority is inferred. |
| Generic host versus the first Python caller; native evaluation versus attributed proposals and unsupported adequacy. | Evidence-backed teaching and ownership assessment are deferred, not passed or diagnosed as a specific learner deficit. Use the actual normal flow and controlled proposal/stop refusals. |
| Partial native capture, immutable closure, schema compatibility and the implementation failures/corrections. | Deeper source/test ownership is deferred. Recover the final verified horizon plus the C progression above; distinguish controlled composition, generic defensive controls and live semantic/usefulness proof. |

When that separate learning session occurs, assess these topics before claiming ownership and repair or explicitly defer any discovered material gaps. A learning finding that contradicts an engineering premise reopens the affected owner/responsibility; ordinary pending learning does not require repeating Build or waiting on the foundation stream.

### Engineering result, proof and residual responsibility

The delivered responsibility is one future-general synchronous Workspace host with present request admission/execution authority, intent before capability entry, retained actual outcomes, native-owned reassessment, original material bases and separately checked current validity. The real selected declaration-read path supplies its first production integration case; acquisition/evaluation still run through their existing owners. Immutable cumulative history and explicit schema-1/schema-2 support/refusal remain preserved. Default publication is volatile; supplying a schema-2 store is the durable acknowledgement path.

The final Stage 3 evidence at `9d394819` remains **25 host tests, 875 checkout and 875 fresh-installed tests, 92 matching hashes**, with the normal controlled-provider flow, guarded recovery, interruption and historical compatibility controls described above. This E increment changes records/planning only; product suites are not rerun. It adds no live provider/model, independent semantic/usefulness, general concurrency, power-loss, exactly-once, user-facing continuation or replay proof. The inherited governance `examples/` marker mismatch remains separate debt.

Full native-family coverage, direct report/synthesis migration, recovery/continuation consumer activation and replay retain their owning gates. Missing general semantic/adequacy competence remains unsupported. These are later capability/proof obligations, not silently completed by Stage 3 or renamed as learning debt.

### Next engineering responsibility and stop line

Recommend **common Investigator native-input and source-interface preparation**, the named prerequisite already identified at Stage 3 readiness. Its outcome is genuine common provenance/native inputs plus a product-owned, mechanically qualified source/reference/native-view bridge that both raw-navigation and structured-Workspace comparison arms can consume. Preserve H1's dependency/source-context and workflow/CI-strength hypothesis; a raw-text-only substitute cannot satisfy it. Missing release/tag or other family inputs must be honestly unsupported or separately admitted for expansion.

The existing [implementation plan preparation boundary](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md#prepare-common-investigator-inputs-and-source-interfaces) owns scope, outputs, proof and stop conditions. Full migration is not a blanket prerequisite; any required Stage 4 expansion must name the affected family/claim and re-entry evidence. H1 remains a separately owned proposed comparison, not an adopted model protocol.

**E stop:** this engineering handoff is complete with explicit learning deferral. The next responsibility begins with its own A0 reconciliation/cycle initialization and A1 continuity gate, then A2 before Build. No new cycle, implementation, evidence acquisition, model run, framework or external task dispatch is performed by this handoff.

**E record/plan validation:** three changed documents pass 96 local links, nine anchors, balanced fences, qualified phase/learning-deferral/continuation and scope/proof checks. Exact source/test trees match the final Stage 3 proof; accepted specifications/ADRs are unchanged. All nine governance functions ran: eight pass, with only the inherited root `examples/` owner-marker mismatch. Whitespace and three-file publication scope pass. Product suites were not rerun for this records/planning-only increment; the prior verified result remains the product evidence. The unrelated untracked audit record is excluded from publication.
