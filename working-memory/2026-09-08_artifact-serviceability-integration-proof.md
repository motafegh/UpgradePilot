# Artifact Serviceability Integration Proof — Working Memory

**Date:** 2026-09-08  
**Session status:** ACTIVE — Slice-5 A/B/C complete; D post-validation learning/ownership is next  
**Primary responsibility/mode:** Build/Implement + Learning-by-Doing  
**Related plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)  
**Previous:** [`2026-09-08_artifact-serviceability-cli-rendering.md`](2026-09-08_artifact-serviceability-cli-rendering.md)

## Slice 5 A–E status

```text
A — DONE
    Re-oriented on the accumulated integration responsibility and selected the executable proof
    order from narrow focused checks through nearest regressions and the full deterministic suite.
    The normal WSL2 repository/venv control plane remained the required proof boundary.

B — DONE
    Executable validation was run on WSL2. Two stale test-harness defects were exposed and
    repaired without changing production source. After those repairs, the focused investigation
    regression, remaining focused/nearest checks, targeted Step-7F end-to-end regression, and
    final deterministic suite were reported green.

C — DONE
    This record preserves the actual validation path, failures, repairs, proof meaning, and
    current closure boundary. MEMORY.md is reconciled separately to make Slice-5 D the live
    continuation.

D — NEXT
    Post-validation learning should distinguish production defects from stale-fixture defects,
    explain why the production invariant checks were valuable, and review what the green proof
    does and does not establish.

E — PENDING
    Repair any remaining reasoning gap, decide whether the integration plan completion line is
    satisfied, then reconcile the plan/live state and identify the next concrete product question.
```

## A — selected proof sequence

The final proof order was intentionally narrow-to-broad:

```text
control-plane / interpreter / editable-install sanity
→ compile + core imports
→ focused investigation
→ focused CLI
→ artifact-serviceability owner regression
→ Target artifact-environment owner regression
→ nearest CI / dependency-environment / direct-install / interface regressions
→ CLI entry-point smoke
→ full deterministic suite
→ targeted repair reruns when failures exposed stale fixtures
```

No live network or LM Studio proof was required for this integration responsibility because the product claims under validation were deterministic composition/presentation contracts, not fresh external availability claims.

## B — environment and executable entry proof

WSL2 execution established the expected control plane:

```text
repository: /home/motafeq/projects/UpgradePilot
branch: main
Python: 3.12.3
interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
editable install: successful
compileall src/tests: successful
core imports: successful
```

The initial working-tree guard also surfaced an unrelated untracked `.zsh_history`; it was moved outside the repository before proof continued. That was environment hygiene, not a product failure.

## B — first executable failure and repair

The first focused investigation run executed 15 tests and produced four errors. All four failed at the same downstream Python-support relevance boundary:

```text
TypeError:
upstream_result must be a grounded support-drop claim or its problem result
```

Diagnosis:

- production `evaluate_target_python_relevance(...)` correctly accepts only the owned typed result union;
- the shared investigation `_Harness` left `support_drop_evaluator` as a bare `Mock()` by default;
- artifact-focused tests that were not testing Python-support semantics could therefore accidentally send an impossible third type into production;
- neighboring tests already used `UpstreamSupportDropClaimProblem(state="no_support_drop_claim", ...)` as the explicit unresolved value.

Repair commit:

`191aaa5b242ab5ef9b6aa74ae1699410841a337d` — `test: make investigation harness return typed unresolved claim`

Change scope: only `tests/test_investigation.py`.

The harness now defaults to a typed `UpstreamSupportDropClaimProblem`; tests that require a grounded claim still override that value explicitly. Production type checking was not weakened.

Focused rerun result:

```text
15 investigation tests
OK
```

## B — second executable failure and repair

After the focused/nearest stages advanced to the full deterministic suite, the suite ran 528 tests and exposed exactly two errors, both in the historical Step-7F controlled end-to-end harness:

```text
ValueError:
old package release must match the exact dependency transition version
```

Diagnosis:

- current application composition now performs exact proposed and old release lookups;
- production artifact-serviceability identity validation correctly requires old release version `1.0` for transition `1.0 → 1.1`;
- the Step-7F harness still used `package_client.get_release.return_value = self.package`, where `self.package` was always the proposed `1.1` release;
- therefore the old-release lookup incorrectly returned `1.1`, and the production invariant correctly rejected the stale fixture.

Repair commit:

`af534cc55e1b3daff121ba6f5209250e9bff389e` — `test: align Step 7F harness with exact release lookup`

Change scope: only `tests/test_step7f_end_to_end.py`.

The repaired harness now owns distinct old/proposed `PackageReleaseEvidence` values and selects them by exact requested version.

Post-repair proof reported by Ali:

```text
targeted tests/test_step7f_end_to_end.py → green
full deterministic tests/ suite         → green
```

## What the executable proof establishes

At the current deterministic repository boundary, evidence now establishes that:

- source/tests compile and the affected modules import in the normal WSL venv;
- current `PublicPullRequestInvestigation` composition works with the updated artifact-serviceability contract;
- exact old/proposed release identity is enforced rather than silently tolerated;
- supported direct-requirements Target composition coexists with existing Python-support orchestration;
- CLI presentation remains executable-compatible with the typed investigation result;
- historical controlled end-to-end Python-support behavior remains compatible with the new second mechanism after its fixture is updated to the current exact-release contract;
- the focused, nearest, targeted Step-7F, and final deterministic suites are green after the two test-only fixture repairs.

## What this proof does not establish

The green deterministic suite does not strengthen unrelated product propositions. In particular it does not prove:

- fresh live PyPI/GitHub availability;
- that a selected static workflow step actually executed in a real target repository;
- exact target wheel compatibility from runner/Python labels;
- source-build success merely because an sdist is published;
- overall upgrade safety or maintainer recommendation;
- deferred multi-job/uv-project-environment Target capability.

Those remain owned by their existing proof boundaries and re-entry conditions.

## Immediate continuation

Perform Slice-5 D from the actual validation story rather than re-teaching implementation details. Focus on:

1. why both failures were stale test fixtures rather than production defects;
2. why strict production type/identity checks were useful because they exposed those stale fixtures;
3. what a green deterministic suite proves versus what still requires stronger/live evidence.

Do not declare the integration plan closed until D/E ownership closure and final plan/live-state reconciliation are complete.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
