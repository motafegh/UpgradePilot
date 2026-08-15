# UpgradePilot Current Memory

**Last updated:** 2026-08-15  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Selected responsibility:** Phase E / Tranche 1 of [`plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md`](plans/B2_CROSS_RESPONSIBILITY_ARCHITECTURE_IMPLEMENTATION_PLAN.md).
- **Accepted architecture:** [`docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md).
- **Current implementation evidence record:** [`working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md`](working-memory/2026-08-15_B2-cross-responsibility-architecture-tranche-1-implementation.md).
- **Canonical product-decision semantics:** [`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md).
- **Source ownership baseline:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).
- **Execution/learning/code-documentation rules:** [`OPERATING_GUIDE.md`](OPERATING_GUIDE.md).

### Current Phase-E status

```text
✓ Cluster 0 — synchronized green baseline
✓ Cluster 1 — PyYAML dependency/parser boundary
✓ Cluster 2 — typed static GitHub Actions workflow IR
✓ Cluster 3 — shared direct-install declaration observation
✓ Cluster 4 — Target migration / proof-strength correction
→ Cluster 5 — CI migration / proof-claim narrowing: implementation written, validation pending
[ ] Cluster 6 — repository-path reconciliation
[ ] Cluster 7 — Tranche-1 acceptance gate
[ ] Tranche-1 stop/review
```

**Learning mode:** continue learning-by-doing/building. Deep mastery, full current-system walkthrough, and real end-to-end data-flow study remain deferred until a meaningful implementation milestone. Explain only prerequisites/reasoning needed to build or decide correctly unless the user requests a learning pause.

**Source documentation rule:** new/materially modified source should include useful docstrings/comments that explain responsibility, proof boundaries, invariants, precedence/abstention behavior, or other non-obvious reasoning. Avoid comments that merely restate syntax. Improve older nearby documentation proportionately when touching it rather than starting broad comment-only refactors.

## Accepted architecture governing the work

```text
RepositoryTextFile
        ↓
bounded provider-specific GitHub Actions static workflow-definition IR
owner = upgradepilot.github
        ↓
   ┌────┴────┐
   ▼         ▼
  CI       Target
```

Runtime GitHub Actions evidence remains separate:

```text
WorkflowRun
WorkflowJob
WorkflowStep
```

Canonical proof boundary:

```text
static declaration
!= runtime execution
!= runtime success
!= environment formation
!= dependency exercise
```

## Verification truth

- Cluster 0 validated baseline: `92e6ea6cb6dbfad7c50986d95e23de924a9b36c1`; `403 tests / OK`.
- Cluster 1 validated implementation: `0d2c7f9eba08bd3c80f1b128d5b223b4e10a9667`.
- Cluster 2 validated implementation: `1e3027f87fa5b187c7d333472fe849aa6a49b049`; `416 tests / OK`.
- Cluster 3 validated implementation: `2980e22994216c069b2f4fb36dc31ea80398367f`; `425 tests / OK`.
- Cluster 4 validated implementation: `f40e7348a38966e7e30b462846a4962a116a9e80`; `430 tests / OK`.

Cluster-4 final validation state was aligned `main`, `HEAD == origin/main == f40e7348...`, and clean worktree.

## Current implementation truth — Cluster 5

Cluster 5 source/tests are written but **not yet runtime-validated**.

### CI static reading now consumes shared owners

`src/upgradepilot/ci/workflow_commands.py` now consumes:

```text
parse_workflow_definition(...)
observe_direct_installation_declaration(...)
```

instead of owning another indentation/regex GitHub Actions parser and another direct-pip requirements matcher.

CI retains only CI-specific static interpretation:

```text
direct changed-package invocation recognition
+ current one-static-job selection boundary
+ install-before-invocation source-order check
```

Multiple jobs remain unresolved because static↔runtime job correlation and cross-job environment continuity are not established in Tranche 1.

### Shared dependency observer refinement

`DirectInstallDeclarationObservation` now exposes:

```text
matched_segment_index: int | None
```

This is a zero-based static shell-segment ordinal used only to compare declaration order without reimplementing install parsing in CI.

```text
matched_segment_index
!= runtime command identity
!= WorkflowStep identity
```

### CI proof-state narrowing

The old strongest CI state:

```text
proven
```

has been removed from active Cluster-5 source and replaced by:

```text
supported_not_correlated
```

The strongest current result now means:

```text
successful exact-head workflow/run evidence
+ at least one successful runtime job record
+ exact-head static definition with ordered direct install→package invocation path
```

while explicitly preserving:

```text
those static declarations
!= matched runtime steps
!= observed command execution
!= observed command success
```

Top-level reason:

```text
successful_exact_head_ci_with_static_dependency_path
```

Workflow-level reason:

```text
successful_ci_with_ordered_static_dependency_path
```

Successful runtime CI without the admitted static path remains `unresolved`; static path recognition is no longer described as proof that the exact commands executed successfully.

### Static order correction

CI now compares static locations as:

```text
(step source_index, bounded shell segment index)
```

and requires an admitted direct install declaration to precede a direct changed-package invocation. Invocation-before-install is explicitly unresolved.

This ordering is static source evidence only and does not perform shell execution or runtime correlation.

### Cluster-5 source/test commits

```text
c18e6a57e2c80f7ea2e6d360280d0239f24ed10d
→ Expose static install segment location

e6431b76ab64b109681672d636fe8d256fe3a03a
→ Test static install segment location

f222b7c4975c4b98b4e9be834dafa5cc46d4e6ff
→ Migrate CI static command reading to shared workflow IR

01330c3e9d9895c0a76f50a9fcd62797c664bd10
→ Narrow CI dependency exercise proof state

80d187edf6d1b0e0089a32d757c77c3c0a7e02d3
→ Update CI static path regressions for shared IR

f561b4b271092af08412c91b49de27f7a754bc8f
→ Update CI exercise regressions for narrowed proof state
```

No repository-path cleanup, runtime step correlation, logs, matrix runtime mapping, reusable-workflow execution, or application orchestration change has begun.

## Immediate project action

**Validate Cluster 5 before beginning Cluster 6.**

Required gate should cover:

```text
test_workflow_commands.py
+ test_ci_dependency_exercise.py
+ test_direct_install_declaration.py
+ test_github_workflow_definition.py
+ test_target_artifact_environment.py
+ test_source_topology.py
+ investigation/CLI nearest regressions
+ complete deterministic suite
+ clean aligned worktree
```

If green, close Cluster 5 and only then select Cluster 6. If failures appear, classify them inside the CI migration before changing repository-path ownership.

## Continuation-critical guards

- `MEMORY.md` alone owns current continuation/latest verification;
- latest validated implementation revision remains `f40e7348a38966e7e30b462846a4962a116a9e80` until Cluster 5 is validated;
- later source/documentation commits may advance `main` without constituting new validation;
- static CI path recognition is not runtime step execution/success evidence;
- `supported_not_correlated` must not be described as stronger than its two separate premises;
- package invocation/exercise remains CI-specific;
- multiple jobs/`needs`/source order do not prove environment continuity;
- dynamic/uninterpretable context remains unresolved;
- static↔runtime job/step correlation remains outside Cluster 5 and outside Tranche 1;
- do not introduce logs, shell tracing, a shell interpreter, generic dependency tracer, universal workflow engine, or broader abstraction merely to avoid unresolved;
- Tranche 2 remains separately reviewed and must not start automatically.

## Learning state

Current demonstrated depth remains substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment. Deep system/data-flow learning remains intentionally deferred until a meaningful milestone selected with the user.
