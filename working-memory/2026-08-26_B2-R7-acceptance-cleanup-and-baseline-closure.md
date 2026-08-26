# Working Memory — B2 R7 Acceptance, Cleanup, and Baseline Closure

**Date:** 2026-08-26  
**Status:** R7 SELECTED; R7.0 COMPLETE; R7.1 REMOTE SOURCE/TEST AUDIT COMPLETE; R7.2 NEXT  
**Execution branch:** `main`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Purpose and execution mode

This is the primary progressive execution record for R7. R7 closes the R1–R6 reconciliation; it is not another feature-expansion phase.

Ali selected a remote-first R7 execution mode:

```text
R7.0–R7.8
→ work fully remotely against GitHub main
→ source/test/commit/diff/real-case/ownership/proof review
→ implement justified cleanup remotely
→ NO local runtime acceptance claims

R7.9
→ after all remote work is finished
→ pull exact frozen main candidate locally
→ run the final validation bundle once

R7.10
→ record accepted executable baseline + handoff
```

If the final local gate fails, preserve its exact output, return to the smallest owning remote R7 slice, repair on GitHub, refreeze the candidate, and rerun the required local gate.

Use this one record for ordinary R7 checkpoints:

```text
R7.0  exact entry-state re-anchor
R7.1  remote focused R3–R6 source/test contract audit
R7.2  remote normal investigation/CI orchestration trace
R7.3  remote real-case GitHub evidence pressure
R7.4  architecture/naming/retention review
R7.5  bounded remote cleanup
R7.6  remote post-cleanup source/diff + proof-boundary audit
R7.7  audit lifecycle reconciliation
R7.8  freeze final remote candidate + local validation bundle
R7.9  final local pull + executable validation
R7.10 accepted baseline freeze + mandatory AI/agentic handoff
```

The Learning-by-Doing-and-Building loop remains active proportionately:

```text
small orientation
→ real bounded remote work
→ inspect actual evidence
→ preserve material state
→ concise post-action learning closure
→ ownership/reasoning when useful
→ next bounded slice
```

## 2. R7.0 exact entry state

Exact `main` revision entering R7:

```text
fa12852598a8f687eac6827a296b87c66b7f932f
```

Latest source/test-changing revision before R7 execution:

```text
71df95cb60a0a476dce2ca090de504a77bde1d99
```

Later R7 preparation/execution-mode commits changed only plan/memory/working-memory material. A fresh comparison from `71df95cb...` to current `main` during R7.1 confirmed no source/test file changed after that executable candidate; only `MEMORY.md`, the active plan, and working-memory records differ.

### Revision semantics

```text
R7 ENTRY REVISION
→ exact repository HEAD when R7 began

REMOTE CANDIDATE REVISION
→ final code/test SHA after all remote R7 review/cleanup
→ not yet runtime accepted

ACCEPTED EXECUTABLE REVISION
→ exact remote candidate SHA after R7.9 local deterministic validation passes

CLOSURE REVISION
→ possible later audit/memory/docs-only SHA
→ not newly execution-tested
```

## 3. Latest R6 corrective slice carried into R7

Post-R6 review found:

```text
R3 selection = unresolved
→ R6 derivation seam skipped it
→ no project-environment consumption evidence
→ CI static classification could fall through to not_established
```

The implemented correction in `src/upgradepilot/ci/workflow_commands.py` is:

```text
R3 not_observed
→ no project-environment evidence

R3 unresolved
→ unresolved StaticDependencyConsumptionEvidence
→ preserve workflow/job/step/command + dependency-source identity
→ do not invoke R4 / project-source membership / R5 positive-or-negative composition

R3 observed
→ existing R3 → dependency-domain relation → R5 flow
```

Focused regression pressure uses:

```yaml
- run: uv sync --group "${{ matrix.group }}"
```

Required semantics:

```text
project_environment_selection_unresolved
→ unresolved CI consumption
→ unresolved coverage consumption state

NOT
→ static_dependency_consumption_not_observed / not_established
```

This correction remains pending the final R7.9 local runtime gate.

## 4. Executable model under R7 review

Normal production route:

```text
public PR
→ dependency analysis + typed changed-dependency source context
→ exact admitted PR-head workflow runs
→ exact workflow definition for each admitted run
→ exact project/lock evidence required by the changed-dependency context
→ ci/workflow_commands.py
   → every readable local run step
   → R3 project selection
   → R4 uv selected-root reachability OR separate project-source membership
   → R5 static CI consumption
   → preserve every resulting consumption
→ evaluate_dependency_ci_coverage(...)
→ application/CLI result surface
```

Retained proof boundaries:

```text
dependency transition
!= selected-root reachability
!= project-source membership
!= static selection
!= static consumption
!= direct exercise
!= runtime execution/success
!= exact-version runtime witness
!= resolver/currentness
!= behavioral compatibility/safety/action
```

and:

```text
one changed package may have zero, one, or multiple supported CI selection commands
supported summary evidence != unique correct command
R3 unresolved != absence != not_established
conditional candidate != reachable
all-workspace no complete negative domain != not_established
```

## 5. R7.1 remote source/test contract audit — evidence reviewed

R7.1 inspected current source and focused tests together. No code was executed and no runtime PASS is claimed.

### R3 — project-environment selection

Source review of `src/upgradepilot/dependency/environment_selection.py` confirms:

```text
literal --all-packages
→ package_scope = all_workspace_packages

ordinary uv/pip project selection
→ bound_project

unsupported/dynamic package targeting or selection
→ unresolved

uv without explicit positive group/extra selector
→ unresolved rather than inferred default environment
```

Focused `tests/test_project_environment_selection.py` protects:

- S001-shaped `--all-packages` + groups/extras;
- bound-project default scope;
- `uv run` option-prefix handling;
- include vs `--only-group` spelling;
- dynamic groups/project paths/working directories;
- unsupported `--package` scope;
- negative selectors remaining unresolved;
- multi-segment declaration indices;
- unrelated expressions not erasing literal selection.

### R4 — selected-root reachability

Source review of `src/upgradepilot/dependency/uv_reachability.py` confirms the public proposition remains selected-root reachability, not complete environment formation. `not_established` is bounded to complete modeled roots; all-workspace no-witness remains unresolved; conditional paths retain candidate diagnostics without promotion.

Focused `tests/test_uv_selected_root_reachability.py` protects:

- S001 transitive witness;
- direct root witness;
- bounded-project no-witness `not_established`;
- all-workspace no-witness `unresolved`;
- explicit project-root binding;
- missing selector root `unresolved`;
- all-groups roots from the lock;
- edge-marker and resolution-marker candidates remaining unresolved;
- incompatible marker combinations not being treated as reachable;
- exact source identity/unavailability remaining unresolved.

`tests/test_uv_package_scope.py` adds changed-case workspace pressure where another workspace member contains the target. Inspecting only the bound project therefore must stay `unresolved` and must not produce false `not_established`.

### R5 — CI consumption calibration

Source review of `src/upgradepilot/ci/consumption.py` confirms:

```text
R4 reachable
→ supported static consumption

R4 not_established
→ not_established only for bound_project scope

R4 unresolved
→ unresolved + conditional diagnostics preserved

project-source membership
→ separate S011 path attributed to pyproject.toml
```

The explicit all-workspace negative guard prevents a bounded-project `not_established` result from being rebound to wider workspace scope.

`tests/test_ci_dependency_coverage.py` protects static consumption vs direct exercise/runtime separation, conditional-candidate non-promotion, bounded negative mapping, the all-workspace guard, S001 positive static consumption, and S011 not-established project-source consumption.

`tests/test_workflow_dependency_evidence.py` protects exact workflow/job/step rebinding for externally composed project-environment evidence; a consumption with the wrong command cannot be silently accepted into another static workflow step.

### R6 — real workflow derivation and transfer boundaries

Source review of `src/upgradepilot/ci/workflow_commands.py` confirms the production seam:

```text
exact readable workflow
→ every local run step
→ R3 observation
→ observed: each declaration enters R4/project-source membership then R5
→ unresolved: one unresolved CI-consumption item is preserved
→ not_observed: no project-environment contribution
```

`tests/test_r6_project_environment_workflow_integration.py` protects:

- S001 real command spellings from workflow text;
- `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve` without prebuilt declaration/reachability/consumption;
- irrelevant lint/testing/build selections staying non-positive;
- more than one supported matching docs command being preserved;
- dynamic uv group uncertainty surviving through CI coverage instead of disappearing into `static_dependency_consumption_not_observed`.

`tests/test_r6_project_source_workflow_integration.py` protects S011 separation: `pip install -e ".[dev]"` does not become consumption of a dependency that belongs to the `mlx` optional environment.

`tests/test_r6_s005_mediated_uv_boundary.py` protects the S005 boundary: a `tox` command does not manufacture direct uv selected-root evidence merely because the target repository uses uv through a mediated runner.

## 6. R7.1 disposition

### Required R3–R6 contract set

Disposition:

```text
REMOTE SOURCE/TEST CONTRACT AUDIT: PASS TO SOURCE/TEST-REVIEW DEPTH
RUNTIME EXECUTION: PENDING R7.9
SOURCE/TEST REPAIR REQUIRED BY R7.1: NO
```

The required R3–R6 responsibilities are represented coherently in current source and focused tests. R7.1 found no demonstrated missing regression or test-only shortcut that blocks the planned R7.2 normal-path trace.

### Non-blocking review note — mixed safe + unresolved shell segments

R3 observations are step-scoped while declarations carry segment indices. Therefore a hypothetical run step containing one independently readable uv segment plus a different material unresolved uv segment can make the overall observation `unresolved`, after which the R6 seam conservatively preserves unresolved evidence rather than evaluating the retained declaration(s).

This can under-report an independently safe positive segment in that mixed step. It does **not** strengthen proof, and no current admitted R6 real case or selected R7 requirement demonstrates that this behavior must be solved now. R7 therefore does not broaden R3 semantics or redesign the observation contract for this hypothetical edge.

Disposition:

```text
current R7 blocker: NO
current admitted real-case requirement: NOT ESTABLISHED
proof risk: conservative under-reporting, not false support
future trigger: real admitted workflow evidence or selected product responsibility requiring independent mixed-segment preservation
```

If such evidence appears, the right design question is segment-level uncertainty ownership in R3—not a downstream R6 guess about which declarations are safe.

## 7. Current R7 state

```text
R7.0 exact state re-anchor                                  COMPLETE
R7.1 remote focused R3–R6 source/test contract audit       COMPLETE
R7.2 remote normal investigation/CI orchestration trace     NEXT / NOT STARTED
R7.3 remote real-case GitHub evidence pressure              NOT STARTED
R7.4 architecture/naming/retention review                   NOT STARTED
R7.5 bounded remote cleanup                                 NOT STARTED
R7.6 remote post-cleanup source/diff + proof audit          NOT STARTED
R7.7 audit lifecycle reconciliation                        NOT STARTED
R7.8 final remote candidate + local bundle freeze           NOT STARTED
R7.9 final local pull + executable validation               DEFERRED UNTIL R7.8
R7.10 accepted baseline + mandatory handoff                 NOT STARTED
```

Runtime status remains pending R7.9 for R3/R4/R5/R6 focused, integration, full deterministic, and required compile/static executable checks.

## 8. R7.2 next bounded slice

Trace the **normal application route** remotely from current source/tests rather than direct helpers:

```text
exact PR identity/change
→ investigation.py
→ exact admitted PR-head workflow run/definition
→ exact project/lock source bundle
→ derive_project_environment_consumptions(...)
→ CI coverage aggregation
→ application/CLI result
```

R7.2 must establish whether the R6 product integration is genuinely the normal path, preserves PR-CI admission boundaries and multiple evidence items, and does not silently retain a test-only/legacy dependency for ordinary operation.

## 9. Final local validation principle

At R7.8, after all remote executable work is finished, freeze one exact candidate and one exact validation bundle. Ali runs that bundle locally only in R7.9. The exact output becomes acceptance evidence. A failure reopens remote work; it does not authorize a local-only patch.

## 10. Post-R7 mandatory handoff

Only successful R7.9 executable validation allows R7.10 to accept the baseline and activate:

```text
plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md
```

That checkpoint must reach an explicit evidence-backed disposition before old Cluster 6 or another ordinary B2 expansion becomes live work.
