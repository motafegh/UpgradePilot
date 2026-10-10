# Workspace native capture, reconstruction and durable publication — LbD cycle

**Initialized:** 2026-10-10 15:52 Asia/Tehran.
**Session status:** ACTIVE in B at the first internal result/learning stop: native capture/cold reconstruction verified; durable publication pending.
**Primary operation:** Build/Implement; A0 initialization includes proportional execution-plan reconciliation.
**Previous cycle:** [closed implementation/usefulness planning](2026-10-09_2045_workspace-implementation-and-usefulness-planning_lbd-cycle.md).
**Owners:** [live position](../MEMORY.md), [implementation/migration plan](../plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md), [ADR-0012](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [ADR-0013](../docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md), [Core §6.4](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation).
**Procedures:** `UP-SKILL:upgradepilot-build-implement`; `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`. The previously loaded Planning/Design procedure applies to the bounded plan reconciliation, without changing accepted architecture/specification methods.

## Cycle status

```text
Cycle — Workspace native capture, reconstruction and durable publication
A0 — DONE: accepted owners/current source/research reconciled; single record and living map created; stage/cycle boundary corrected.
A1 — DONE: starting-state onboarding delivered; Ali had a meaningful challenge opportunity and replied "Good and we can continue" on October 10.
A2 — DONE: Ali explicitly cleared the pre-B understanding gate and requested B on October 10; the deferred reasoning response is not independently demonstrated mastery.
B — CURRENT: first native capture/cold reconstruction implemented and verified; internal result/learning review before durable publication.
Verification gate — PENDING for the combined cycle: native reconstruction internal gate GREEN; SQLite publication/backup/interruption and combined durable-checkpoint proof not implemented/run.
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

At initialization, evidence was owner/source inspection and Git reconciliation; product verification was PENDING. The earlier 743 product and 121 focused Workspace experiment tests belonged to the preceding reconciliation and were not promoted into this cycle's native/publication proof. The B-result section below records this cycle's actual implementation verification.

Initialization-document verification: this record, the existing implementation plan's stage/cycle distinction and `MEMORY.md`'s changed live responsibility; three documents with 58 local links including seven anchors, fences and truthful phase status PASS. Owner/scope alignment and `git diff --check` PASS. All nine governance check functions executed: eight PASS; only the inherited root responsibility-map missing `examples/` marker remains. This is documentation proof, not the cycle's product Verification gate. No executable/accepted-specification files changed and no runtime tests rerun.

A2 orientation/state verification: two documents changed; the same three relevant documents checked with 66 local links including seven anchors, fences and A0/A1 DONE → A2 CURRENT → B PENDING phase consistency PASS. Whitespace and owner/scope checks PASS; nine governance functions retain eight PASS and the same inherited `examples/` mismatch. No product source/tests changed or runtime tests run. Source/test inspection supplies the teaching examples, not a new product verification result.

## B entry and contract decisions

Ali explicitly said the A2 gate can be considered cleared and to proceed to B. This controls the process gate; it does not retroactively pass an unanswered ownership question. Revisit the actual result and ownership at the internal learning stop/D.

The focused existing baseline (`test_ci_dependency_state`, `test_python_support_impact`, `test_investigation`, `test_r6_investigation_ci_integration`) passes 42 tests. Source inventory finds 77 reachable native record types across the selected CI/runtime and Python-support roots/shared material. This is concrete representation work, not a new evaluator or all-family cutover.

Implementation route: fixed version-1 family/root/variant layouts and bounded scalar/sequence/record helpers; no runtime dataclass discovery, checkpoint-driven imports or arbitrary class hydration. Representation layouts remain with CI/impact and shared-input ownership. An opt-in capture seam on normal orchestration retains inputs/results without adding a second acquisition/evaluation sequence or changing the current report return contract. Separate CI and Python-support projections allow unsupported unrelated families to remain inspectable without inventing complete report recovery. Owner/method provenance missing from present interfaces is explicitly retained as a gap.

## First native capture/reconstruction result — 2026-10-10 17:45

Delivered production source:

- [Normal orchestration](../src/upgradepilot/investigation.py) accepts an explicit `native_capture` and supplies its existing inputs/results at the native boundaries. Default acquisition/evaluation/report behavior remains the original path; capture adds no second producer sequence. Failed staging cannot be sealed as completed recovery.
- [Capture](../src/upgradepilot/workspace/native_capture.py) holds encoded bytes, seals immutable records once and retains actual supplied inputs, outcomes, scoped identity, material references and explicit method/content gaps. Generated record IDs are separate from content digests and from target identity. There is no live-native-value recovery map.
- [Family contracts](../src/upgradepilot/workspace/native_codecs.py) define 11 version-1 roots. The [shared-input](../src/upgradepilot/workspace/native_inputs_codec.py), [CI](../src/upgradepilot/ci/native_codec.py) and [Python impact](../src/upgradepilot/impact/python_support_codec.py) tables enumerate 44 + 27 + 6 = 77 fixed native layouts. Source inventory helped author these static declarations; production never discovers dataclass fields or imports checkpoint-supplied names. Uniform representation helpers avoid duplicated scalar/sequence validation without becoming an evidence evaluator.
- [Boundary inspection](../src/upgradepilot/workspace/native_boundary.py) validates format, digests, exact target and material-reference closure. [Separate typed projections](../src/upgradepilot/workspace/native_projection.py) validate owner/version and cross-record scopes/bases before exposing supported CI/runtime or Python-support values. Unsupported unrelated codecs remain inspectable and need not block the unaffected projection. Unknown fields, missing optional fields, substituted identity and constructor normalization cannot silently produce repaired native truth.

### Retention and remaining-field disposition

All 24 legacy fields were traced. Thirteen have native material/projection equivalents here: PR identity, changed files, dependency result, target Python result, workflow run/jobs (from supplied CI inputs), CI coverage, runtime state, upstream interval authority, support-drop result, target relevance, pre-assessment, selection and final Python-impact assessment. Hidden source contexts, workflow/project-environment text and target declaration source are retained where supplied to the selected native owners.

Eleven remain separate later-family/consumer obligations: proposed/old package release results, upstream repository result, release index/crossed selection, tag resolution, changelog discovery/separate tagged-changelog result, artifact candidate, target artifact environments and artifact impact. Shared upstream authority may contain tagged source content without preserving every earlier acquisition/problem branch. This first projection therefore cannot replace the complete report path. Initial shared layouts admit the context variants used by CI; the existing public-source uv regression now proves that its actual project/lock inputs and native results survive this capture seam.

Available producer method labels are retained; absent producer versions are explicit gaps. Present producer interfaces declare no admitted semantic-version identities, so reconstruction refuses any declared version until a tested compatibility mapping exists. Representation codec support does not confer semantic-method support. Dependency-analysis call metadata/unsupplied source content and upstream interpretation call metadata are not fabricated. No raw model trace, hidden reasoning or credential capture is added. Fresh continuation and stronger source/semantic claims cannot be earned by these gaps or by representation fidelity.

### Verification, correction and claim limits

- Focused existing baseline: 42 PASS before implementation. Final focused native/CI/impact/orchestration scope: 54 PASS (`test_workspace_native_reconstruction`, `test_ci_dependency_state`, `test_python_support_impact`, `test_investigation`, `test_r6_investigation_ci_integration`).
- Checkout product regression: 755/755 PASS. Rebuilt fresh-installed package: 755/755 PASS from outside the checkout with `PYTHONPATH` pointing only to tests; all 85 installed/source Python-file hashes match. Pip check and both installed CLI help entry points PASS. Temporary isolated validation root: `/tmp/upgradepilot-native-installed-xluejfg8` (not a checkpoint or committed product artifact).
- [Native reconstruction tests](../tests/test_workspace_native_reconstruction.py) compare every native field with an independent test-only renderer in six fresh child-process cases: positive/outside, dry-run/applicable, ambient/unresolved, unavailable declaration, unsupported upstream claim and dependency-problem/not-evaluated branches. Four actual provider/model-bound/native-evaluator/synthesis entry-point negative controls prove the guard can fail; network connection is independently blocked during reconstruction. Existing controlled extraction/claim answers are disclosed; this is not a fresh external/model semantic acceptance run.
- Refusal proof covers missing hidden input closure, damaged bytes, wrong envelope/payload target, wrong owner, unsupported codec with valid digest, unsupported declared producer version, unknown injected variant, omitted optional field, ambiguous JSON, unsupported boundary format and prohibited constructor repair. The field-layout drift check prevents new native fields from silently entering an old codec through defaults. An unsupported runtime codec or producer version blocks CI while supported Python history remains usable.
- First child proof FAILED because a blanket native-module guard also blocked RepositoryTextFile's representation-only locator/text validators. Source inspection established those two helpers are pure structural checks allowed by ADR-0013; only those helpers were admitted. Acquisition/evaluation guards remain intact and their independent negative controls PASS. Decoder review also added refusal when an existing constructor normalizes a retained field; this is representation validation, not re-evaluation.
- All 12 touched Python files pass Ruff lint/format. Source/owner/retention/dependency-direction review, AST parsing and whitespace checks pass. Three owner/cycle documents have 78 valid local links including seven anchors plus balanced fences and truthful phase status. All nine governance functions ran: eight PASS; only the inherited root `examples/` marker mismatch remains. No accepted specification/ADR methods or unrelated work are changed.

The native reconstruction internal gate is GREEN for this exercised supported scope. The combined cycle gate remains PENDING: no SQLite revision publication, validated durable backup/interruption proof, complete canonical lifecycle history, report cutover, continuation, replay, power-loss or usefulness proof is claimed.

### Internal learning review and continuation

A2 expected that exact encoded bytes alone would not recover trusted native values. The actual result now reconstructs fixed supported native types with their complete retained scopes/unknowns, including pip launcher versus target identity and Python pre/post applicability history, without evaluator re-entry. Original method gaps remain distinct from codec version. Checksum integrity, supported reconstruction, scope binding and present execution authority remain separate.

Ali has not yet reviewed this implementation result or demonstrated the deferred codec reasoning against it. Teach the actual result at this internal stop; permit questions/challenge and assess only meaningful ownership evidence. After that review, continue durable publication in this same cycle. D/E stay pending for the combined result; this is not a new cycle or a full cycle closure.
