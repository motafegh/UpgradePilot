# AUDIT-015 — Workspace authority and consumer-cutover integrity

**Audit date:** 2026-10-20  
**Branch:** `audit/project-wide-system-audit-2026-10-20`  
**Main revision last reconciled:** `a1c291c6cf9238493eeb666b184192ed178b90f1`  
**Mode:** cross-responsibility architecture/source-flow audit  
**Authority:** non-controlling audit evidence. This record does not authorize source refactoring or cutover.

## 1. Question

Does the current implementation satisfy the accepted replacement-oriented Workspace direction, or has UpgradePilot created two independently authoritative investigation state paths?

Primary trace:

```text
public PR acquisition
→ native producers/evaluators
→ NativeInvestigationCapture
→ InvestigationWorkspaceHost / immutable revision
→ synthesis
→ report projection
→ save/open
```

Owners inspected include ADR-0012, ADR-0013, the Workspace implementation/migration plan, `investigation.py`, native capture/codecs/projections, Workspace consumer access, maintainer synthesis, report projection/file, CLI and focused Workspace/report tests.

## 2. Executive result

The accepted Workspace architecture remains technically coherent and should be retained.

The current implementation does **not** contain two complete independent acquisition/evaluation systems. Normal native producers run once; Workspace capture records those same produced native values rather than rerunning domain evaluation, and cold-reconstruction tests strongly protect the admitted CI/runtime/Python-support closure.

However, the replacement migration is **materially incomplete**:

- `PublicPullRequestInvestigation` is still assembled directly from orchestration-local native results;
- it is not a one-way projection reconstructed from Workspace;
- maintainer-action synthesis consumes that legacy object directly;
- report projection consumes the legacy object directly and calls synthesis from it;
- the CLI therefore follows `investigation → legacy result → report`, even though a Workspace revision is carried alongside;
- Workspace native codecs currently cover the initial CI/runtime/Python-support closure, not all facts currently used by report/synthesis;
- default Workspace publication is volatile unless a durable schema-2 host/store is explicitly supplied.

This is consistent with the implementation plan's staged Stage 3/4/5 boundary and therefore is **not an ADR violation by itself**. But it is a P1 migration/cutover blocker: UpgradePilot must not claim that the complete normal product path is already Workspace-canonical until family closure, direct consumer migration and parity/retirement proof are complete.

## 3. Current authority map

### Native/domain truth

Domain producers remain the semantic owners. Examples include dependency analysis, CI coverage/runtime state, upstream authority/claim, target relevance and impact evaluation.

Normal orchestration computes those results once. `NativeInvestigationCapture` receives the same values at explicit boundaries and encodes them. It does not fetch, rerun, retry or semantically rederive them.

This is aligned with ADR-0012/0013.

### Workspace truth

For admitted captured families, Workspace owns immutable investigation identity, composition, retained material relationships, lifecycle/revision history and recovery boundary. Native projections decode recorded values and validate their retained bindings; they do not rerun producers or strengthen truth.

Current native family contracts cover the initial closure:

- investigation inputs;
- CI inputs;
- CI coverage;
- runtime dependency state;
- upstream interval authority;
- upstream support-drop result;
- Python-support pre-assessment;
- Python-support investigation selection;
- target Python source/result;
- target relevance;
- Python-support post-assessment.

This is explicitly narrower than the complete legacy/report surface.

### Legacy/current user-facing truth path

`PublicPullRequestInvestigation` still carries the broader normal product result, including facts not currently reconstructed from Workspace such as package release/index data, upstream repository/tag/changelog states, old-package/artifact candidate state, target artifact-environment associations and artifact-serviceability impact.

The final object is assembled directly from local variables at the end of normal orchestration while `workspace_revision=workspace_host.current` is attached alongside.

`maintainer_action.synthesize_maintainer_action(...)` consumes `PublicPullRequestInvestigation` and reads its fields directly.

`report_projection.project_investigation_report(...)` also consumes `PublicPullRequestInvestigation`, projects its fields directly and invokes synthesis on that same legacy result.

The CLI calls:

```text
investigate_public_pull_request(...)
→ project_investigation_report(investigation)
→ render/save
```

No direct Workspace projection currently mediates that user-facing path.

## 4. Findings

### AUDIT-015-F1 — P1: direct synthesis/report cutover is not complete

**Classification:** architecture/migration debt, not accepted-architecture failure.

ADR-0012's target is:

```text
native producers/evaluators
→ Workspace
→ explicit one-way consumer projections
```

Current normal user-facing path is still:

```text
native producers/evaluators
├→ Workspace capture/revision
└→ orchestration-local legacy result
      → synthesis
      → report
```

The implementation plan explicitly reserves direct synthesis/report migration for a later stage, so this state is expected during migration. It nevertheless blocks any claim that the complete normal product is already Workspace-canonical.

**Required eventual proof:** direct synthesis/report consumers operate from the admitted Workspace projection/retained conclusion boundary with equivalent meanings/unknowns, and the legacy bridge has an explicit remaining caller/purpose or is retired.

### AUDIT-015-F2 — P1 before default cutover: Workspace family coverage is narrower than current report responsibility

The native codec table deliberately covers an initial 11-root CI/Python-support closure. Current report/synthesis logic also consumes package, repository, release-index/tag/changelog, artifact candidate/environment/serviceability and other legacy facts not represented in that closure.

This means current Workspace cannot yet be the sole input for an equivalent complete report without either:

- adding the missing admitted native families/material closure; or
- deliberately narrowing the supported report/product responsibility with an owning decision.

The implementation plan already requires a complete legacy-field/material ledger and forbids an unsupported codec from silently suppressing a supported report fact. Preserve that requirement.

### AUDIT-015-F3 — P2: overlapping legacy/Workspace values are same-origin but not structurally one-way

For captured families, normal orchestration computes a native result and then:

1. stores the local value used later for `PublicPullRequestInvestigation`;
2. passes that same value to `NativeInvestigationCapture`.

This avoids duplicate evaluation and is substantially better than two independent semantic paths.

But the final legacy object is not rebuilt from the published Workspace revision. Consequently a future code change can update a legacy field path without updating capture, or vice versa, unless tests catch the divergence. `NativeInvestigationCapture` placeholders can honestly remain `not_evaluated`; they cannot know that a separately held local result was produced but never captured.

Existing integration/cold-reconstruction tests strongly protect known admitted families, but this remains a migration proof risk until direct consumer cutover.

**Required control before cutover:** named field/family ledger plus normal-path parity tests proving every overlapping consumed fact is represented once with the same semantic meaning, including problem/unresolved/not-evaluated variants. Prefer retiring the parallel path over indefinitely growing parity machinery.

### AUDIT-015-F4 — RETAIN: native processing is not duplicated for Workspace

The audit found no evidence that normal Workspace publication reruns CI/runtime/Python-support evaluation merely to populate canonical state.

`NativeInvestigationCapture` explicitly records producer values; native reconstruction is offline decoding plus binding validation. Selected target-Python reassessment runs through the host as an admitted native operation, then capture records its actual result.

This is aligned with ADR-0012/0013 and should be preserved.

### AUDIT-015-F5 — RETAIN with scope: `prepare_dependency_ci_workspace` is a shared-owner bootstrap, not a competing semantic implementation

The model-free preparation entry point does perform a separate invocation when explicitly used, but it delegates to the same shared `acquire_dependency_inputs` and `prepare_ci_evidence` owners as normal investigation. It intentionally stops after the dependency/CI prefix and labels upstream/semantic families unperformed.

That is acceptable for bounded Investigator/common-input preparation while it has a real consumer. Do not let it evolve into an independent fork of acquisition/evaluation semantics. Shared producer functions remain the correct boundary.

### AUDIT-015-F6 — RETAIN: report reopening, Workspace recovery and deterministic replay remain correctly separate

Current `--open-report` reads/validates the saved report and renders it offline. It does not invoke Workspace recovery, acquisition or evaluation.

The report itself states that it cannot replay analysis or resume an agent. ADR-0012/0013 separately define canonical Workspace recovery, while deterministic replay remains a separately activated Charter/B3 obligation.

No collapse of these three concepts was found in the active source path.

### AUDIT-015-F7 — P2 staged limitation: normal CLI does not currently provide durable Workspace recovery

`investigate_public_pull_request` creates a default volatile `InvestigationWorkspaceHost` unless a host backed by the supported schema-2 store is explicitly supplied. The CLI supplies no durable host/store and exposes no Workspace-recovery/continuation command.

This is consistent with the migration plan, which reserves user-facing recovery/explicit continuation for later work. It is therefore not a current defect **provided documentation does not claim the capability is already implemented**.

Do not infer durable canonical recovery from the existence of `workspace_revision` or from checkpoint-store tests.

### AUDIT-015-F8 — P3 clarity risk: “canonical” wording should remain scoped during migration

The orchestration docstring calls `workspace_revision` “the immutable canonical boundary” while the same function still returns uncaptured broader legacy facts used by synthesis/report.

Within the admitted Workspace subset this wording is defensible, and the same docstring discloses later consumer migration. Still, during the incomplete Stage 4/5 period, documentation should prefer wording such as **canonical Workspace boundary for the admitted captured families/lifecycle** rather than implying the entire current user-facing investigation is already sourced exclusively from Workspace.

Do not churn terminology before the cutover plan is acted on; treat this as a source-clarity correction bundled with migration work unless it causes an actual misleading external claim.

## 5. Test/proof assessment

Current Workspace proof is strong for its admitted subset:

- normal host integration verifies selected read intent before provider execution and native reassessment through the host;
- result `workspace_revision` equals host current revision;
- cold readers reconstruct retained CI/Python material without provider/model/evaluator calls;
- interruption, backup and lifecycle recovery controls are substantial;
- source/native consumer access keeps delivery, use, citation and semantic support separate.

Current report proof is also strong for the **legacy input path**: report tests validate source retention, unresolved states, artifact distinctions and action uncertainty from `PublicPullRequestInvestigation`.

What is not yet proven is exactly the migration target: complete direct report/synthesis parity from Workspace across all current supported evidence families followed by legacy retirement.

This gap is already named by the implementation plan and should not be hidden by aggregate test counts.

## 6. Recommended architectural disposition

Do **not** redesign ADR-0012/0013.

Do **not** create a second generic evidence model.

Do **not** immediately remove `PublicPullRequestInvestigation`; current report/synthesis still depend on facts Workspace does not yet reconstruct.

Instead preserve the existing migration route and make its remaining closure explicit:

```text
complete family/material ledger
→ add/reuse missing owner-specific capture + reconstruction only where current consumers require it
→ prove normal/recovered semantic parity
→ cut synthesis to Workspace-native/retained conclusion inputs
→ cut report/CLI to explicit Workspace projections
→ retain old type only for named compatibility/proof caller if one remains
→ retire obsolete legacy plumbing
```

The cheapest important control before that work is not another abstraction; it is an exact **legacy-field → native-family/material → consumer** ledger with missing-family disposition.

## 7. Stop line

This audit does not authorize Stage 4/5 Workspace migration Build.

The next program stage should audit tests/proof/operational coverage, including whether the current suite adequately protects the transitional dual-surface state and what proof is actually needed for eventual cutover. That stage can convert F1–F3 into a minimal verification/cutover checklist before implementation is selected.

## References

- `docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md`
- `docs/architecture/ADR-0013-versioned-native-reconstruction-and-workspace-checkpoint-storage.md`
- `plans/INVESTIGATION_WORKSPACE_IMPLEMENTATION_AND_MIGRATION_PLAN.md`
- `src/upgradepilot/investigation.py`
- `src/upgradepilot/investigation_inputs.py`
- `src/upgradepilot/workspace/native_capture.py`
- `src/upgradepilot/workspace/native_codecs.py`
- `src/upgradepilot/workspace/native_projection.py`
- `src/upgradepilot/workspace/consumer_access.py`
- `src/upgradepilot/workspace/preparation.py`
- `src/upgradepilot/maintainer_action.py`
- `src/upgradepilot/report_projection.py`
- `src/upgradepilot/report_file.py`
- `src/upgradepilot/cli.py`
- `tests/test_workspace_host_integration.py`
- `tests/test_workspace_consumer_access.py`
- `tests/test_report.py`

`UP-SKILL:upgradepilot-repository-audit`
