# Workspace native capture, reconstruction and durable publication — LbD cycle

**Initialized:** 2026-10-10 15:52 Asia/Tehran.
**Session status:** ACTIVE at A2 upcoming-responsibility orientation / pre-B understanding gate; substantive B has not started.
**Primary operation:** Build/Implement; A0 initialization includes proportional execution-plan reconciliation.
**Previous cycle:** [closed implementation/usefulness planning](2026-10-09_2045_workspace-implementation-and-usefulness-planning_lbd-cycle.md).
**Owners:** [live position](../MEMORY.md), [implementation/migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md), [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [Core §6.4](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation).
**Procedures:** `UP-SKILL:upgradepilot-build-implement`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`. The previously loaded Planning/Design procedure applies to the bounded plan reconciliation, without changing accepted architecture/specification methods.

## Cycle status

```text
Cycle — Workspace native capture, reconstruction and durable publication
A0 — DONE: accepted owners/current source/research reconciled; single record and living map created; stage/cycle boundary corrected.
A1 — DONE: starting-state onboarding delivered; Ali had a meaningful challenge opportunity and replied "Good and we can continue" on October 10.
A2 — CURRENT: source/input/consumer and reconstruction/publication/proof model oriented; pre-B reasoning response pending.
B — PENDING: no product source/test changes or native Workspace implementation in this cycle.
Verification gate — PENDING: new product proofs not run; initialization-document checks are separate.
D — PENDING: combined result/evidence-backed ownership after sufficient verification.
E — PENDING: gap repair/defer decision, closure and evidence-based next-boundary handoff.
C — CONTINUOUS: meaningful reconciliation, learning, implementation/proof and handoff preserved here.
```

## User selection and cycle boundary

Ali explicitly requested retaining the six technical responsibilities as implementation/proof stages, combining capture/reconstruction and durable publication in one coherent Workspace native-foundation cycle, using internal verification/learning stops, and reassessing cycle boundaries before semantic integration/product cutover.

The earlier provisional one-stage/one-cycle estimate is not a governing cycle count. Native reconstruction and coherent retained publication share a recovery boundary; separating them into mandatory full cycles would prescribe learning/closure overhead before the evidence exists. The user-selected route keeps one A0/A1/A2 and one final D/E, with focused proof/learning reviews during B. It changes execution grouping, not accepted semantics, authority or proof obligations. The execution plan and live owner are reconciled; no new architecture decision is needed.

## A0 current-state reconciliation

- Baseline: fetched `main` at `e805150aa04a11d6f145c5e14c0bf7b442b9ddbe`, aligned with `origin/main` (0/0). This commit closed planning and accepted ADR-0013 with its limits. ADR-0012/Core §6.4 were already accepted. Both preceding cycles are closed; this is a new record.
- Product `src/` and normal `tests/` have no changes since executable head `aa67a1f5`. [Investigation orchestration](../src/upgradepilot/investigation.py) still constructs the frozen 24-field `PublicPullRequestInvestigation`. Producer inputs such as source contexts/CI coverage inputs can matter beyond that final snapshot.
- [CI/runtime state](../src/upgradepilot/ci/dependency_state.py) and [Python support](../src/upgradepilot/impact/python_support.py) retain typed, bounded native assessment authority. Capture must preserve actual inputs/results and uncertainty without rerunning these owners during historical reconstruction.
- [Migration experiment](../experiments/workspace_replacement_migration.py) and its [tests](../experiments/tests/test_workspace_replacement_migration.py) expose the cold native gap: opaque bytes alone cannot hydrate native values; the experiment's projection still uses a live-value map and refuses absent support with `unsupported_native_codec`. Its parity/storage results remain research evidence, not production recovery.
- [Report projection](../src/upgradepilot/report_projection.py) currently invokes synthesis. Historical synthesis/report migration therefore remains a later explicit boundary; the first CI/impact reconstruction proof cannot claim full offline report parity.
- The prior planning cycle's unsupported-codec and changed-synthesis ownership checks remain explicitly deferred, not passed. Revisit only when concrete source/result orientation makes their implications tangible.
- Pre-existing untracked `2026-10-03_broad-project-and-future-plans-audit_lbd-cycle.md` is unrelated and preserved untouched. No research branch or other agent work is activated.

## Scope and full-product connection

The full target remains native producers/evaluators → canonical evolving Workspace → typed investigation/evaluation/synthesis/report consumers, coherent offline checkpoint recovery and separately validated continuation. This cycle covers implementation/proof stages 1 and 2, not full product replacement.

Included: concrete owner/consumer/input/version contracts; first supported CI/runtime and Python-support native families with their shared identity/dependency/upstream/source material; supported positive/problem/unresolved/not-evaluated variants; immutable encoded capture and version-aware cold reconstruction; immutable revision/reference closure; host-controlled coherent local SQLite publication, refusal/interruption/conflict behavior and validated backup; integrated fresh-process reconstruction of those supported native projections from a declared checkpoint.

All 24 legacy fields and hidden material inputs remain an inventory obligation; not all families acquire codecs in this cycle. Their expansion is temporary staged debt, not a claim that unsupported facts are unnecessary. The narrowing follows the prepared plan's exercised native owners and keeps capture completeness/native meaning independently provable before expanding coverage. Additional codecs enter when a required consumer/input closure or representative branch exposes the need; material expansion requires boundary reassessment.

Later stage obligations: lifecycle/material-basis semantic integration; complete admitted-family coverage; direct synthesis/report migration; user-facing offline recovery/explicit continuation; final legacy retirement. No new semantic/adequacy evaluator, Investigator policy, model/framework topology, deterministic replay, pruning/schema migration, power-loss guarantee, arbitrary untrusted import or user usefulness study is selected. Storage/publication retains identity/material basis needed for later semantics without claiming that those later semantics are implemented.

## Living A-phase orientation/learning map

| Phase / bridge | Required understanding and source/evidence |
| --- | --- |
| A1 continuity | Planning is closed and the reconstruction/storage method accepted; actual product remains the fixed snapshot; research exposes cold native recovery debt; one coherent combined cycle replaces the provisional stage-per-cycle count. |
| A2 native ownership/input closure | Trace orchestration → native CI/runtime and Python-support owners → consumed values. Distinguish capture completeness from byte round-trip; identify material source/scope/problem variants and the remaining-family ledger. |
| A2 reconstruction | Owner-specific version codecs reconstruct retained native meaning without provider/model/evaluator re-entry. Codec/schema refusal, missing/corrupt/wrong-target material and unknowns must remain truthful. Return to the deferred unsupported-codec question here when concrete. |
| A2 publication | Explain immutable revision/content/reference identity, expected predecessor versus material basis, commit versus acknowledgement, interrupted/unknown outcomes, local WAL/FULL limits, initial retention and validated online backup. |
| A2 proof/non-goals | First supported native projections from a fresh process/durable checkpoint, not complete report recovery, semantic adequacy, current continuation authority, deterministic replay or power-loss proof. Historical synthesis remains retained-result consumption at its later boundary. |

A1's continuity gate cleared after the starting-state model and challenge opportunity were delivered and Ali explicitly requested continuation. This establishes continuity to A2, not technical mastery or the pre-B understanding gate. A2 owns the minimum-complete upcoming responsibility model and pre-B gate; selecting this cycle does not itself prove understanding. Refine this map if onboarding or exact source/input tracing exposes a gap.

## A2 upcoming responsibility — October 10

The selected production path is existing native acquisition/evaluation → capture actual inputs/results and source/method bindings → explicit owner/version encoding → immutable revision → coherent local checkpoint → offline validation/reconstruction → supported native projections. The domain owner still evaluates; Workspace retains/composes/publishes the material. The SQLite adapter stores and validates the boundary without owning CI/impact semantics. The first supported consumers are CI/runtime and Python-impact native projections; synthesis/report migration remains later.

Concrete input/consumer trace:

- [CI coverage](../src/upgradepilot/ci/dependency_exercise.py) takes the dependency transition, `WorkflowDependencyCoverageInput` values and `source_contexts`; [runtime composition](../src/upgradepilot/ci/dependency_state.py) additionally consumes the coverage result. Retain exact run/jobs/steps/workflow text, relevant project/source contexts, command/environment/semantic provenance, results and blockers before local inputs disappear. The [real-producer command test](../tests/test_ci_dependency_state.py) distinguishes launcher `/opt/bootstrap/bin/python` from pip target `/opt/target/bin/python`. Its command-completion witness cannot expand into installation freshness, later use or compatibility during reconstruction.
- [Python impact](../src/upgradepilot/impact/python_support.py) consumes the exact PR/dependency/upstream claim, then optional exact-target relevance. Retain candidate, pre-assessment, selection, supplied declaration/problem, relevance and post-assessment with their bases. [Impact tests](../tests/test_python_support_impact.py) distinguish a declaration not acquired from an attempted unavailable declaration; [orchestration tests](../tests/test_investigation.py) preserve pre-acquisition unresolved and later applicable/not-applicable/unresolved outcomes. These are existing controlled product cases, not a fresh external/model or semantic acceptance run.
- Current [synthesis](../src/upgradepilot/maintainer_action.py) and [report projection](../src/upgradepilot/report_projection.py) consume runtime/impact uncertainty, identity and limitations. This consumer reading establishes preservation obligations; it does not admit full report reconstruction with unsupported remaining families.

A codec is an explicit encoder/decoder for one admitted family and version. Preserve meaningful ordering, optionality, exact strings and nested variants. Decoding reconstructs retained typed values and validates representation/bindings; it does not rerun source parsers or evaluators. Compatible bytes alone do not establish supported semantics or trust. A host-owned checkpoint with an unsupported codec leaves unaffected inspectable history available where valid, but refuses the affected native projection; no live cache, current defaults, dynamic class import or producer rerun may substitute for support. Arbitrary untrusted import remains out of scope. The earlier unsupported-codec question is now concrete enough to revisit in the pre-B reasoning point; changed-synthesis ownership remains deferred to its historical-consumer boundary.

Publication stores immutable records and revision membership, then conditionally advances the lineage head in one validated transaction. Expected predecessor prevents a concurrent overwrite; it is separate from whether an assessment's material premises remain valid. Pre-commit interruption leaves the last declared boundary; commit plus lost acknowledgement requires explicit identity reconciliation rather than retry. Initial retention keeps all declared revisions/material closure; validated SQLite online backup must restore that closure. Local WAL/FULL/process-kill tests do not establish device/power-loss guarantees. Present execution authority belongs to later explicit continuation.

B will first finalize the concrete contract/remaining-family ledger, implement normal-path capture and supported native codecs, and obtain the independent cold-reconstruction proof before its internal result/learning stop. It will then implement coherent publication and its failure/backup proofs, review that result internally, and finally prove reconstruction from the durable checkpoint. Exact field layouts/table names remain implementation choices. Representative unsupported native outcomes and missing-input negative controls are mandatory alongside positives; no full consumer/default CLI cutover occurs in this cycle.

Proof scope before implementation: native owner/codec/closure checks → normal-orchestration capture and fresh child-process native projection proof with independently forbidden provider/model/evaluator re-entry → real publication interruption/conflict/refusal/backup checks → combined durable-checkpoint reconstruction and justified broader product regressions. Compare complete supported native values, scopes, unknowns and consumer meanings, not only JSON/checksums. The initial proof does not earn complete canonical product recovery, new semantic evaluation, usefulness, replay, continuation or power-loss claims. This turn inspects source/tests; no new runtime proof is claimed.

Pre-B reasoning point: in the existing runtime-witness case, explain what a new process may restore from a supported checkpoint without evaluating again, and what it should expose/refuse if the needed codec version is unsupported despite a valid checksum. Ali's response/questions will determine prerequisite repair or gate completion; passive continuation alone is not recorded as ownership.

## Internal verification and learning stops

These are connected stops inside this cycle, not separate full LbD cycles. Actual source results may justify changing their implementation order or boundaries; preserve the reason and affected proof before proceeding.

1. **Native capture/reconstruction:** verify independent consumer/input closure, complete supported values/scopes/unknowns, fresh-process recovery without a live cache or provider/model/evaluator calls, and corrupt/missing/wrong-target/unsupported-version refusal. Stop to teach/review the actual result and ownership gaps before durable publication work.
2. **Durable publication:** verify stable prior views/revisions, identity/reference closure, expected-revision conflicts, real process interruption before/after commit/acknowledgement, storage/schema refusal and validated backup. Stop to teach/review outcomes and actual durability limits before combined proof. Process kill does not establish power-loss behavior.
3. **Combined boundary:** reconstruct supported native projections from a declared durable checkpoint in a fresh child process; run justified focused/broader product proof and preserve remaining-family/report/semantic debt. Then perform final D/E for the combined responsibility and reassess the next cycle boundary before semantic integration or cutover.

## Initialization evidence and continuation

Current evidence is owner/source inspection and Git reconciliation. Product verification is PENDING. Historical proof remains 743 product and 121 focused Workspace experiment tests from the preceding reconciliation; those tests are not freshly rerun or promoted into this cycle's native/publication proof.

Initialization-document verification: this record, the existing implementation plan's stage/cycle distinction and `MEMORY.md`'s changed live responsibility; three documents with 58 local links including seven anchors, fences and truthful phase status PASS. Owner/scope alignment and `git diff --check` PASS. All nine governance check functions executed: eight PASS; only the inherited root responsibility-map missing `examples/` marker remains. This is documentation proof, not the cycle's product Verification gate. No executable/accepted-specification files changed and no runtime tests rerun.

A2 orientation/state verification: two documents changed; the same three relevant documents checked with 66 local links including seven anchors, fences and A0/A1 DONE → A2 CURRENT → B PENDING phase consistency PASS. Whitespace and owner/scope checks PASS; nine governance functions retain eight PASS and the same inherited `examples/` mismatch. No product source/tests changed or runtime tests run. Source/test inspection supplies the teaching examples, not a new product verification result.

Next: finish A2's pre-B reasoning/understanding gate, then begin the bounded capture/reconstruction responsibility in this same cycle. No product Build result or cycle closure is claimed.
