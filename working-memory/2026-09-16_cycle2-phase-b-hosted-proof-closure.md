# Cycle 2 Phase B Hosted Proof Closure — Working Memory

**Date:** 2026-09-16  
**Session status:** CLOSED — Phase B implementation and hosted executable proof complete  
**Primary mode:** Learning-by-Doing — Cycle 2 / Phase B proof closure  
**Phase-B build record:** [`2026-09-15_cycle2-static-consumer-build.md`](2026-09-15_cycle2-static-consumer-build.md)  
**Hosted repair record:** [`2026-09-16_phase-b-hosted-proof-repair.md`](2026-09-16_phase-b-hosted-proof-repair.md)  
**Third hosted repair record:** [`2026-09-16_phase-b-hosted-proof-repair-3.md`](2026-09-16_phase-b-hosted-proof-repair-3.md)

## Closure result

Cycle 2 Phase B is now closed at its intended bounded implementation/proof horizon.

The final hosted proof was:

```text
workflow: Product verification
run id: 35108271298
run attempt: 1
event: workflow_dispatch
head branch: main
tested revision: ee93143b58c3cf0dbb191c543ef4a66a437d0aec
job id: 104835021439
result: SUCCESS
```

The tested revision includes the full B1–B5 implementation, all bounded hosted-proof repairs, and the working-memory preservation for the third repair.

## Executable proof

The hosted job established all configured proof layers successfully:

```text
checkout exact selected revision                 PASS
CPython 3.12.14 setup                            PASS
fresh virtual environment                        PASS
pip install .                                    PASS
python -m pip check                              PASS — no broken requirements
installed CLI entry point --help                 PASS
python -m upgradepilot --help                    PASS
installed package import                         PASS
focused investigation composition               PASS — 15/15
full deterministic product regression            PASS — 587/587
```

The characterized parser stack installed in the fresh environment was:

```text
tree-sitter==0.25.0
tree-sitter-bash==0.25.1
tree-sitter-batch==0.11.1
tree-sitter-pwsh==0.38.1
```

The full suite finished:

```text
Ran 587 tests in 0.293s
OK
```

The previously failing R6 dynamic-project-selection integration test also passed on this exact run:

```text
test_dynamic_uv_group_remains_unresolved_through_ci_coverage ... ok
```

## What this closes

This proof closes the Phase-B gate for the accepted A1–A6 migration:

```text
A1  one normal workflow traversal and one StaticCommandAnalysis per run step
A2  canonical outer workflow/job/step identity + inner StaticCommandLocation
A3  obsolete segment_index identity/ordering overload removed
A4  dependency observers consume parser-neutral typed command analysis
A5  package invocation comes from real parsed command occurrences
A6  CI owns bounded ordered_after | not_after | unresolved static ordering
```

The stable final consumer path is therefore proven as:

```text
one WorkflowDefinition
→ one CI job/step traversal
→ one analyze_run_step_commands(...) per RunStepDefinition
→ same StaticCommandAnalysis reused by:
     direct requirements
     project environment
     package invocation
→ canonical StaticCommandLocation + structural_context
→ bounded static CI composition/order
```

This proof does **not** turn static occurrence/order into command execution or command success. Cycle 3 remains the separate runtime-strengthening responsibility.

## Hosted proof failures retained as learning evidence

The hosted proof gate was useful because it exposed migration responsibilities that source/diff audit alone did not prove.

The repair records preserve the details. The important lessons to carry into the integrated learning session are:

1. a strict evidence-contract migration must update secondary downstream consumers as well as the primary path;
2. removing an obsolete identity field can leave stale test fixtures even after production contracts are clean;
3. parser-backed architecture can move uncertainty to an earlier trustworthy owner without changing the final conservative proposition;
4. step-scoped unresolved evidence does not imply an exact inner-command occurrence identity;
5. B4's single-traversal architecture is a correctness boundary because it prevents command identity from being detached and later guessed/rebound;
6. proof failures should be classified before repair: real source regression, stale fixture, stale architectural test path, or legitimate changed ownership boundary.

The final repair intentionally changed only the stale R6 test handoff from detached precomposed consumptions to the normal `project_environment_sources` production seam. The canonical identity validator was not weakened.

## Current project responsibility after closure

Do **not** start Cycle 3 yet.

The next selected responsibility is the previously agreed integrated Phase-B implementation-learning / ownership check over the now-stable proven source.

Use this trace:

```text
workflow run step
→ effective shell resolution
→ StaticCommandAnalysis
→ StaticCommandOccurrence
→ StaticCommandLocation
→ direct requirements interpretation
→ project-environment interpretation
→ direct package invocation
→ CI evidence composition
→ bounded static ordering
```

Use one or two real UpgradePilot/product-simulation cases end-to-end and explicitly distinguish:

```text
what existed before
→ what was wrong or overloaded
→ what B changed
→ why each ownership boundary exists
→ what the final implementation guarantees
→ what it deliberately does not guarantee
```

If that ownership check exposes a real understanding or implementation gap, repair the bounded gap and preserve it before advancing. Only after the learning/ownership check closes should Cycle 3 runtime-strengthening work begin.

## Final Phase-B state

```text
Cycle 1                                  CLOSED
Cycle 2 Phase A                          COMPLETE
Cycle 2 Phase B implementation           COMPLETE
Cycle 2 Phase B hosted executable proof  PASS
Cycle 2 Phase B                          CLOSED
Integrated B1–B5 learning/check          NEXT
Cycle 3                                  NOT STARTED
```

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
