# UpgradePilot Current Memory

**Last updated:** 2026-09-08  
**Authority:** sole owner of the live project position, current blockers, selected continuation, and current learning depth.

## Live position

- **Current responsibility:** finish the admitted artifact-serviceability public-investigation integration through final Learning-by-Doing closure after successful deterministic executable proof.
- **Mode:** Build/Implement + Learning-by-Doing.
- **Selected plan:** `plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`.
- **Active working memory:** `working-memory/2026-09-08_artifact-serviceability-integration-proof.md`.
- **Previous Slice-4 record:** `working-memory/2026-09-08_artifact-serviceability-cli-rendering.md`.
- **Previous Slice-3 record:** `working-memory/2026-09-07_2149_target-artifact-environment-composition.md`.
- **Previous Slice-2 record:** `working-memory/2026-09-07_1748_artifact-serviceability-candidate-composition.md`.
- **Contract/design record:** `working-memory/2026-09-06_artifact-serviceability-public-investigation-integration-session.md`.
- **Framework status:** bounded ordinary-Python / LangGraph / LangChain investigation remains closed for now; re-entry evidence lives in `working-memory/2026-09-06_1853_framework-experiment-deferral-and-core-capability-return.md`.

## Current checkpoint

Plan Slices 1–4 are closed through A–E. Slice 5 now has real WSL executable proof and is at post-validation learning:

```text
Slice 5
A — DONE: exact narrow-to-broad WSL proof sequence selected
B — DONE: executable proof completed after two stale test-fixture repairs
C — DONE: proof/failure/repair evidence preserved in the active working memory
D — NEXT: post-validation learning / ownership check
E — pending: gap repair + final plan/live-state reconciliation
```

Current implementation state:

```text
result contract                                  → implemented
old release acquisition                          → implemented
artifact-serviceability candidate composition    → implemented
initial unresolved artifact assessment           → implemented
target artifact-environment composition          → implemented for supported direct-requirements relations
exact target compatibility composition           → not admitted from current static evidence
artifact applicability re-evaluation             → not performed; remains unresolved
CLI / human-facing artifact explanation          → implemented at typed proof strength
```

The application path preserves:

```text
proposed exact PackageReleaseEvidence
→ exact old PackageReleaseResult
→ artifact-serviceability candidate/problem/no-candidate
→ for a real candidate, initial unresolved assessment
→ reuse CI-owned exact workflow definitions
→ select only supported direct-requirements consumption relationships
→ exact join to one RequirementsFileDependencyContext
→ TargetArtifactEnvironmentEvidence | TargetArtifactEnvironmentProblem
→ preserve dependency-source ↔ Target association
→ render artifact/Target/applicability state through CLI without inventing stronger evidence
```

## Slice-5 executable proof

The normal WSL2 control plane was used:

```text
repository: /home/motafeq/projects/UpgradePilot
branch: main
Python: 3.12.3
interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
editable install: successful
compileall src/tests: successful
core imports: successful
```

The proof sequence covered focused investigation/CLI, artifact-serviceability, Target artifact-environment, nearest CI/dependency-environment/direct-install/interface regressions, CLI entry-point smoke, targeted Step-7F controlled end-to-end behavior, and the final deterministic suite.

Two stale fixtures were exposed by strict production invariants and repaired without changing production source:

1. `tests/test_investigation.py` defaulted the support-drop evaluator to a bare `Mock`, which is not a valid `UpstreamSupportDropClaimResult`.  
   Repair: `191aaa5b242ab5ef9b6aa74ae1699410841a337d` (`test: make investigation harness return typed unresolved claim`).  
   Focused investigation rerun: **15 tests, OK**.

2. `tests/test_step7f_end_to_end.py` returned the proposed `1.1` package release for both proposed and old release lookups, violating the exact `1.0 → 1.1` transition identity.  
   Repair: `af534cc55e1b3daff121ba6f5209250e9bff389e` (`test: align Step 7F harness with exact release lookup`).

After the second repair, Ali reported both the targeted Step-7F regression and the final deterministic suite green. The earlier full-suite run had reached **528 tests with only those two Step-7F fixture errors**, so the failures were tightly localized before repair.

## What current proof establishes

At the deterministic repository boundary:

- affected source/tests compile and import in the normal project venv;
- exact old/proposed release identity is enforced;
- artifact-serviceability composition coexists with existing Python-support orchestration;
- supported direct-requirements Target composition remains bounded by its current owner;
- CLI rendering is compatible with the typed investigation result;
- historical controlled end-to-end Python-support behavior remains compatible after its fixture was aligned with the current exact-release contract;
- focused, nearest, targeted Step-7F, and final deterministic regression proof is green.

## Proof limits that remain unchanged

The green deterministic suite does **not** establish:

- fresh live PyPI/GitHub availability;
- runtime execution of a selected static target workflow step;
- exact target wheel compatibility from broad runner/Python labels;
- source-build success from sdist presence;
- overall upgrade safety or maintainer recommendation;
- deferred multi-job or uv/project-environment Target support.

These are not blockers for the current integration completion line unless Slice-5 D/E reveals a contradiction.

## Deferred capability re-entry from Slice 3

1. **Multi-job Target selection** — revisit only if real candidate cases are materially blocked by recurring `ambiguous_target_job_selection`.
2. **uv/project-environment Target formation** — revisit when real repositories make direct-requirements-only Target coverage materially insufficient; reuse existing CI/dependency uv evidence rather than reimplementing it.
3. **Static declaration ↔ runtime execution correlation** — revisit only when a product proposition requires proof that the relevant static install/exercise step itself executed successfully.
4. **Exact target wheel compatibility** — revisit when the product needs to strengthen artifact applicability from `unresolved` to established applicable/not-applicable; broad runner/Python labels are not sufficient evidence.

## Immediate continuation

Perform **Slice 5 D — post-validation learning / ownership check** from the actual executable failures and repairs.

Focus on:

```text
why both failures were stale test fixtures rather than production defects
why strict production type/identity checks were valuable
what green deterministic proof establishes
what still requires stronger/live evidence
```

After D, perform Slice-5 E, then reconcile the selected plan and `MEMORY.md` to close this integration responsibility if no material gap remains. Do not start a new product mechanism or framework experiment before that closure unless Ali explicitly redirects.

## Active engineering constraints

- Provider/domain truth stays with its owner; `investigation.py` coordinates rather than reimplementing PyPI, wheel, workflow, Target, or applicability semantics.
- CLI rendering consumes typed state; it does not manufacture evidence or recommendation semantics.
- Candidate discovery and target applicability remain separate propositions.
- Static workflow facts do not establish runtime execution or exact target wheel compatibility.
- Supported CI static consumption establishes a workflow/source relationship only at its own proof strength; unresolved relationships are not silently promoted.
- Existing uv/project-environment CI evidence is real but is not rebound into a Target interpreter that does not own that mechanism.
- Presence of an sdist does not prove source-build success or overall installability.
- Artifact-serviceability is mechanism-specific technical evidence, not an overall maintainer recommendation.
- Independently earned CI, Python-support, package, artifact, and Target evidence survives unrelated later stops.
- Repository, PR revision, dependency identity, release versions, workflow source, source path, and Target evidence must remain exactly aligned.
- Test fixtures must obey the same typed/identity contracts they are exercising; production guards should not be weakened merely to accommodate stale mocks.
- Framework experimentation remains deferred until richer real product pressure earns re-entry.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
