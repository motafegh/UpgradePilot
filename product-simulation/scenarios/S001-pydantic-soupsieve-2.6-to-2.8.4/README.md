# S001 — Pydantic Soup Sieve 2.6 → 2.8.4

**Scenario:** `S001`  
**Run:** `s001-retrofit-20260722-r1`  
**Execution mode:** retrospective artifact reconstruction  
**Execution status:** complete  
**Factual review:** corrected  
**Ali review:** challenged; final acceptance pending  
**External/behavioral confirmation:** not independently confirmed  
**Current outcome:** **merge after normal maintainer review**

## Read in this order

1. [`CASE.md`](CASE.md) — complete human-auditable investigation and retrofit.
2. [`artifacts/RUN_MANIFEST.json`](artifacts/RUN_MANIFEST.json) — run and bundle index.
3. [`artifacts/DECISION.json`](artifacts/DECISION.json) — bounded decision state.
4. [`artifacts/HUMAN_REPORT.md`](artifacts/HUMAN_REPORT.md) — maintainer-facing output.
5. [`artifacts/MACHINE_REPORT.json`](artifacts/MACHINE_REPORT.json) — external machine representation.
6. Other records under [`artifacts/`](artifacts/) for operation/evidence/finding lineage.

## Honesty boundary

The original S001 investigation did not create this artifact bundle
progressively. This run reconstructs it from retained tool history, the original
narrative and commits, exact repository revisions, and freshly reacquired public
sources.

It does not invent missing historical timestamps, search ordering, raw connector
payloads, or target-code executions.

The original July 9 advisory date and strong security-trigger inference are
preserved as superseded history. The corrected official date is June 1, 2026;
the exact Dependabot trigger remains unresolved.

## Baseline comparison

Transparent baseline `simulation-transparent-baseline-v0.1` reaches the same
action, but with weaker reasons, miscalibrated certainty, and a less actionable
explanation because it cannot inspect dependency path, target use, advisory
authority, or CI responsibility.

## Target-mutation and execution boundary

No target repository was changed. No Pydantic or Soup Sieve code was executed
locally. The secret-bearing publication path was not reproduced.

## Validation

Validated at `2026-07-22T19:11:25Z` with zero structural errors. See `artifacts/checks/artifact-validation.json`.
