# Cycle 2 Phase B Hosted Proof Repair 3 — Working Memory

**Date:** 2026-09-16  
**Session status:** ACTIVE — third hosted failure diagnosed and bounded test repair committed; fresh hosted verification required  
**Primary mode:** Learning-by-Doing — Cycle 2 / Phase B executable proof gate  
**Continues:** [`2026-09-16_phase-b-hosted-proof-repair.md`](2026-09-16_phase-b-hosted-proof-repair.md)  
**Phase-B build record:** [`2026-09-15_cycle2-static-consumer-build.md`](2026-09-15_cycle2-static-consumer-build.md)

## Hosted verification run 3

```text
Product verification
run id: 35107464677
head: dbe1e16fca80834ed053019ba989d4b4fed3ec21
result: FAILURE
```

Healthy proof layers:

```text
checkout selected revision              PASS
Python 3.12.14 setup                    PASS
fresh package build/install             PASS
python -m pip check                      PASS
installed CLI entry-point checks        PASS
focused investigation composition       PASS — 15/15
```

The complete deterministic suite executed:

```text
587 tests
586 passed
1 failed
0 errors
```

The sole failure was:

```text
test_r6_project_environment_workflow_integration.
R6ProjectEnvironmentWorkflowIntegrationTests.
test_dynamic_uv_group_remains_unresolved_through_ci_coverage
```

Standalone derivation already produced the intended conservative result:

```text
state  = unresolved
reason = project_environment_command_analysis_unresolved
command = uv sync --group "${{ matrix.group }}"
```

But the coverage half of the test fed that precomputed unresolved evidence back through:

```text
WorkflowDependencyCoverageInput(
    ...,
    project_environment_consumptions=consumptions,
)
```

Coverage then correctly reported:

```text
project_environment_consumption_command_identity_mismatch
```

instead of the test's expected:

```text
project_environment_command_analysis_unresolved
```

## Diagnosis

This was not a new product-code regression. The test still exercised a transitional two-stage architecture after B4/B5 had established the final production ownership model.

The final normal product route is:

```text
WorkflowProjectEnvironmentSource
→ inspect_workflow_dependency_evidence(...)
→ one WorkflowDefinition / one job-step traversal
→ one StaticCommandAnalysis per RunStepDefinition
→ project-environment interpretation inside that traversal
```

The `project_environment_consumptions=` input remains only a bounded focused-test seam for **precomposed evidence that preserves canonical parsed command identity**.

The dynamic GitHub-expression command is different:

```text
uv sync --group "${{ matrix.group }}"
```

The provider cannot establish an analyzable command occurrence for this bounded proposition, so the unresolved result legitimately has no canonical inner `StaticCommandLocation`.

Therefore:

```text
step-scoped parser uncertainty
!= exact inner-command identity
```

Re-injecting such detached evidence through the canonical-identity compatibility seam must fail closed. Weakening the validator, fabricating a location, or rebinding only from job/step text would undo the identity correction established by B2–B5.

## Repair decision

Preserve both useful test responsibilities but use the correct owner for each:

1. keep `derive_project_environment_consumptions(...)` in the first half to prove the standalone wrapper conservatively emits `project_environment_command_analysis_unresolved`;
2. for end-to-end CI coverage, supply the exact source bundle through the final production input:

```text
project_environment_sources=(source,)
```

instead of re-injecting the detached consumption.

This lets coverage derive the uncertainty inside the same single traversal that owns command analysis and preserves A1/A2/A3.

No product source code, validator weakening, fabricated command identity, textual fallback, expression evaluation, or Cycle-3 runtime policy was introduced.

## Repair committed

```text
7e1ecb3b5a6c1b98eb8252a31c0f86d3866badc6
test: use final project environment coverage seam
```

Exact diff:

```text
tests/test_r6_project_environment_workflow_integration.py
1 addition / 1 deletion

project_environment_consumptions=consumptions
→ project_environment_sources=(source,)
```

## Learning entry for the integrated Phase-B session

Retain this incident because it demonstrates several important engineering distinctions:

- a compatibility/test seam can have a **stronger identity precondition** than normal source-driven production composition;
- unresolved evidence may validly identify a step/proposition without identifying one exact inner command occurrence;
- canonical identity must not be invented merely so detached evidence can be reattached later;
- B4's single-traversal architecture is not just an optimization — it prevents semantic identity loss between derivation and composition;
- end-to-end tests themselves can become stale architectural clients after a migration, even when their high-level semantic expectation (`unresolved`) remains correct;
- proof failures should be used to distinguish source defects, stale fixtures, stale architectural test paths, and real semantic regressions rather than reflexively changing product behavior.

## Current proof state

```text
Phase-B implementation                 complete
Target missed-consumer repair           complete
B5 stale ordinal fixture repair         complete
provider-level unresolved expectation   reconciled
old two-stage R6 coverage test seam      repaired
latest hosted full suite                586/587 before this repair
fresh hosted verification               REQUIRED
Phase B                                 NOT YET CLOSED
integrated B1–B5 learning               NOT YET STARTED
```

## Exact next action

Manually dispatch `Product verification` from current `main` again.

If the fresh run is green, preserve the exact run/head/environment/test counts, close the Phase-B executable-proof gate in `MEMORY.md` and the active Phase-B working memory, then enter the agreed integrated B1–B5 implementation-learning session before Cycle 3.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
