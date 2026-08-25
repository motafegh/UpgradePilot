# Working Memory — B2 R6 Real Workflow Reachability Integration

**Date:** 2026-08-25  
**Status:** IMPLEMENTED TO STATIC/SOURCE-REVIEW DEPTH; RUNTIME ACCEPTANCE DEFERRED  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. R6 responsibility

R6 must pressure the reconciled R3/R4/R5 architecture against real-case flow rather than preserve a test-side composition shortcut.

The required production proposition is:

```text
exact admitted PR-head workflow definition
+ changed-package dependency source context
+ exact project/lock evidence required by that context
→ inspect every readable local run step
→ R3 static selection declaration
→ dependency-domain relation
   - R4 uv selected-root reachability
   - project-source environment membership for S011-style evidence
→ R5 exact CI consumption evidence
→ CI coverage aggregation
```

No production caller supplies a preferred group, a prebuilt `ProjectEnvironmentSelectionDeclaration`, a prebuilt `UvSelectedRootReachability`, or a prebuilt `StaticDependencyConsumptionEvidence`.

## 2. Integration-seam decision

The smallest legitimate seam is `src/upgradepilot/ci/workflow_commands.py`.

Reason:

- `github.workflow_definition` already owns static GitHub Actions YAML parsing;
- `workflow_commands.py` already receives the exact admitted workflow definition and iterates every readable `StepsJobDefinition` / `RunStepDefinition`;
- R3 owns command-selection semantics;
- R4 / project-source membership own dependency-domain semantics;
- R5 owns mapping those dependency facts to static CI consumption;
- `investigation.py` should acquire and route exact evidence, not learn dependency graph or selector semantics.

New production seam:

```text
derive_project_environment_consumptions(...)
```

It considers every readable run step and every admitted declaration independently. It does not stop after the first positive command.

## 3. Explicit `investigation.py` migration decision

**Decision: migrate the normal application path in R6. Do not defer it.**

Evidence/authority:

- the pre-R6 CI modules explicitly described the legacy application path as temporary until ordinary Cluster-6 migration;
- the active reconciliation plan blocks the old `B2_DEPENDENCY_ENVIRONMENT_AND_CI_CONSUMPTION_EVIDENCE_PLAN` at completed Cluster 5 and forbids starting its old Cluster 6 before this reconciliation reaches R7;
- R6 is the current authorized real-case transfer gate;
- leaving `investigation.py` on `evaluate_dependency_ci_exercise()` would let R7 freeze a deterministic baseline where R3→R4→R5 existed only through test/manual `external_consumptions`, contradicting the current R6 purpose and the user's explicit requirement.

Therefore normal orchestration now uses:

```text
get_exact_head_workflow_runs(...)
→ get_workflow_jobs(...)
→ get_exact_head_workflow_file(...)
→ acquire exact project-environment source bundle(s)
→ derive_project_environment_consumptions(...)
→ WorkflowDependencyExerciseInput.external_consumptions
→ evaluate_dependency_ci_coverage(...)
```

The legacy evaluator remains callable for transitional/historical callers, but the normal public-PR investigation no longer depends on it.

## 4. Exact source acquisition

For a `UvLockDependencyContext`, normal orchestration acquires:

```text
exact changed head uv.lock
+ exact sibling pyproject.toml at the lock/workspace root
```

The sibling project file supplies the exact project-root path needed by the existing R3 observer. R4 still does **not** parse or require pyproject content for lock-backed reachability.

For `PyprojectOptionalExtraDependencyContext` / `PyprojectDependencyGroupContext`, orchestration acquires the exact project source itself and preserves the separate project-source membership proposition.

Requirements and constraints remain on their existing direct-install path and are not reclassified as project-environment sources.

## 5. PR-CI admission boundary preserved

R6 does not search arbitrary workflow files and does not treat every repository workflow as PR evidence.

Normal acquisition remains:

```text
PullRequestIdentity.head_sha
→ GitHubActionsClient.get_exact_head_workflow_runs(...)
   event = pull_request
   head_sha = exact PR head
→ exact jobs for each admitted run
→ GitHubRepositoryClient.get_exact_head_workflow_file(...)
   exact workflow path from the admitted run
   exact PR-head revision
```

Only after that provider admission does R3/R4/R5 inspect command meaning.

Real S001 exact-head PR runs confirmed during R6 review include:

```text
CI                 completed / success
Third party tests  completed / skipped
codspeed           completed / success
```

The real codspeed definition contains:

```text
uv sync --all-packages --group testing-extra --extra email --frozen
```

It is evaluated independently; it is not treated as relevant merely because another workflow's docs command reaches SoupSieve.

## 6. Preserve every matching command

R6 explicitly rejects a singular "correct command" model.

```text
for each admitted workflow
  for each readable local job
    for each readable run step
      for each admitted project-selection declaration
        evaluate changed-package relation
        retain resulting consumption
```

`WorkflowDependencyCoverageResult.consumptions` preserves the complete tuple. The CLI now renders all retained consumptions and their witness/candidate paths instead of presenting only one selected command.

The aggregate coverage classifier may use one supported item to establish the existential workflow/PR proposition, but that does not delete other supported items.

## 7. S001 pressure

Changed package:

```text
soupsieve 2.6 → 2.8.4
```

Real Pydantic command spellings represented in the focused regression include:

```text
uv sync --all-packages --group linting --all-extras
uv sync --all-packages --group docs
uv sync --all-packages --group testing-extra
uv sync --only-group build
```

Only a command whose own selected roots establish a witness becomes positive.

S001 positive path remains:

```text
uv sync --all-packages --group docs
→ R3: docs + all_workspace_packages
→ R4:
   mkdocs-llmstxt
   → beautifulsoup4
   → soupsieve
→ reachable / transitive
→ R5 supported static consumption
```

Irrelevant selectors remain non-positive (`not_established` or `unresolved` according to the exact scope/proof boundary).

Focused regression:

```text
tests/test_r6_project_environment_workflow_integration.py
```

It does not construct a selector/declaration/reachability/consumption in the caller.

Normal-application regression:

```text
tests/test_r6_investigation_ci_integration.py
```

It controls provider returns but requires `investigate_public_pull_request()` itself to acquire exact project/lock sources and derive the docs witness from workflow text.

Real external verification surface:

```text
tools/verification/2026-08-25_r6_s001_real_ci_reachability.py
```

It accepts only:

```text
repository = pydantic/pydantic
PR = 13432
```

and requires the production path to discover the dependency, exact PR workflows, exact `uv.lock`, selections, reachability, and consumptions. It intentionally does not assert that the docs command is unique; it prints/preserves every supported match.

**Runtime execution of this verifier is deferred; no live PASS is claimed.**

## 8. S011 transfer

S011-style project-source evidence remains separate from uv lock reachability.

Regression:

```text
tests/test_r6_project_source_workflow_integration.py
```

Shape:

```text
changed numpy belongs to mlx optional environment
workflow command selects dev
→ R3 observes dev
→ project-source membership says affected mlx environment not selected
→ R5 not_established
```

No uv lock or R4 reachability is introduced for this proposition.

## 9. S005 transfer

Real S005 evidence is mediated:

```text
tox latest environment
→ uv-venv-lock-runner
→ exact uv.lock consumption
→ pytest execution
```

R6 does not make `uv_reachability.py` interpret tox and does not reinterpret a `tox ...` workflow command as if it were a direct `uv sync` selection.

Regression:

```text
tests/test_r6_s005_mediated_uv_boundary.py
```

A tox command with uv lock context produces no direct project-environment consumption through the R3/R4 direct-command seam. A future tox/runner proposition requires its own admitted owner.

## 10. Workspace proof guard

The existing changed-case workspace pressure is now aligned with R4 rather than the legacy membership evaluator:

```text
tests/test_uv_package_scope.py
```

Shape:

```text
uv sync --all-packages --group docs
root project docs does not reach SoupSieve
workspace member docs does reach SoupSieve
complete workspace roots are not enumerated by R4
→ unresolved
→ never not_established
```

This preserves the positive/negative proof asymmetry under the new public reachability contract.

## 11. Presentation/result migration

`PublicPullRequestInvestigation` now owns:

```text
ci_coverage_result: DependencyCICoverageResult | None
```

The CLI presents `CI dependency coverage` and renders all retained static consumption evidence.

A transitional read-only `ci_exercise_result` property remains for pre-R6 application assertions. It returns `ci_coverage_result` and is explicitly an R7 cleanup candidate; it is not the authoritative new contract.

## 12. Changed implementation/test surfaces

Production:

```text
src/upgradepilot/ci/workflow_commands.py
src/upgradepilot/investigation.py
src/upgradepilot/cli.py
```

Focused tests/verification:

```text
tests/test_r6_project_environment_workflow_integration.py
tests/test_r6_investigation_ci_integration.py
tests/test_r6_project_source_workflow_integration.py
tests/test_r6_s005_mediated_uv_boundary.py
tests/test_uv_package_scope.py
tests/test_source_topology.py
tests/test_cli.py
tools/verification/2026-08-25_r6_s001_real_ci_reachability.py
```

Primary executable/source commits:

```text
dcdf6165f03aa5706015425a1538edc9eaf938cd  workflow-derived production seam
4286a4d7687114a42e0fbd3b898bca903ff05b26  normal investigation migration
5b5f789cdc677cf14b70dffbaa7fdf62d5a796ac  CLI all-consumption presentation
fefbc3307864299fc6d5c476276834e0fceaeb64  S001 seam regression
6e1e4f5a4f9a41b3acc009b2c6313b9a465682b4  real S001 verifier
bf1568537db8aa79f3f545e8c8f5b120fd09b391  normal investigation regression
7d780394f30d249dfd9f054c1e3c29a798d006de  transitional result alias
0fa6901ad93bdf7cfffc0a1c999fa9754556d2b9  workspace R4 regression
96ca78aea8a7317787ac18da6745212f95481d89  S011 transfer regression
82f3c52cd999cb2ad597b8598d0d1ff0d5f1e340  S005 mediated-boundary regression
```

## 13. Verification state

Current evidence:

```text
production ownership/orchestration trace               COMPLETE
normal investigation migration                         IMPLEMENTED
all-readable-run-step R3→R4/R5 seam                    IMPLEMENTED
all supported matching consumptions preserved          IMPLEMENTED
PR-head workflow admission boundary                    PRESERVED
S001 focused source/test pressure                       IMPLEMENTED
S001 complete-real-source verification tool            IMPLEMENTED / NOT RUN
S011 separate source-membership pressure                IMPLEMENTED
S005 mediated tox boundary pressure                     IMPLEMENTED
workspace negative-proof guard on R4                    IMPLEMENTED
post-write connector changed-file review                PASS to static/source-review depth
local focused runtime                                   DEFERRED
real S001 verifier runtime                              DEFERRED
nearest integration/runtime suites                      DEFERRED
complete standard suite                                 DEFERRED
compileall                                              DEFERRED
```

No R3/R4/R5/R6 runtime PASS is claimed.

## 14. Operational hygiene incident

During write-tool discovery, four empty root files (`noop`, `noop2`, `noop3`, `noop4`) were accidentally created and immediately deleted. They are absent from the final tree. Their create/delete commits remain in Git history; history was not rewritten. The final R5→R6 tree comparison contains no `noop*` files.

## 15. R6 disposition

**R6 implementation is complete to static/source-review depth. Runtime acceptance remains deferred.**

R7 must not describe this baseline as executable/real-source PASS until the deferred focused/integration/live-S001 validation is actually run and recorded. R7 cleanup should also explicitly review the transitional `ci_exercise_result` alias and remaining legacy CI evaluator surface.
