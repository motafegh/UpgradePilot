# Cycle 2 Phase B Hosted Proof Repair — Working Memory

**Date:** 2026-09-16  
**Session status:** ACTIVE — repair committed; fresh hosted verification required  
**Primary mode:** Learning-by-Doing — Cycle 2 / Phase B proof gate and bounded repair  
**Continues:** [`2026-09-15_cycle2-static-consumer-build.md`](2026-09-15_cycle2-static-consumer-build.md)  
**Selected plan:** [`../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md`](../plans/STATIC_WORKFLOW_COMMAND_ANALYSIS_AND_RUNTIME_STRENGTHENING_IMPLEMENTATION_PLAN.md)

## Starting point

Phase B B1–B5 implementation had been completed and source/diff audited, but executable proof was still missing because the repository verification workflow is manual `workflow_dispatch` only and the assistant runtime could not clone GitHub for local execution.

Ali manually dispatched `.github/workflows/product-verification.yml` on `main`.

## Hosted verification run 1

Run:

```text
Product verification
run id: 35105369516
head: 90a33cb85daee41c6448c91d5f094a820c67aa01
result: FAILURE
```

Environment/setup evidence was healthy:

```text
checkout selected revision              PASS
Python 3.12.14 setup                    PASS
fresh package build/install             PASS
python -m pip check                      PASS
installed CLI --help checks             PASS
```

The failure was isolated to:

```text
Check focused investigation composition
python -m unittest discover -s tests -p test_investigation.py -v
```

Result:

```text
15 tests run
14 passed
1 ERROR
```

Failing test:

```text
test_target_artifact_environment_uses_supported_direct_requirements_relationship
```

Exact exception:

```text
TypeError: observe_direct_installation_declaration()
missing 1 required keyword-only argument: 'command_analysis'
```

Trace path:

```text
tests/test_investigation.py
→ investigate_public_pull_request(...)
→ _compose_target_artifact_environments(...)
→ interpret_target_artifact_environment(...)
→ _interpret_dependency_installation(...)
→ observe_direct_installation_declaration(...)
```

Because the focused step failed, the workflow's complete deterministic regression step was skipped. Therefore this run does **not** establish Phase B executable proof.

## Diagnosis

This is a real Cycle-2 downstream migration regression, not a hosted environment problem.

During B2 the direct-install observer was deliberately made strict:

```text
caller must supply StaticCommandAnalysis
```

The normal CI consumer was migrated correctly, but the separate Target artifact-environment consumer still called the observer through its pre-Cycle-2 API.

This escaped the source audit because the missed call site sits outside the main CI static-evidence traversal. The hosted focused investigation test exposed the cross-layer consumer that the migration audit had missed.

Important engineering lesson retained for later learning:

```text
changing an internal evidence contract
→ update primary producer/consumer path
→ source audit may still look coherent
→ end-to-end/integration proof can reveal a secondary downstream consumer
```

This is exactly why the accepted plan requires nearby/application proof after focused migration tests.

## Repair decision

Do **not** make `command_analysis` optional and do **not** restore a textual fallback merely to preserve the old Target call.

`target/artifact_environment.py` already owns a parsed `WorkflowDefinition` and selected `StepsJobDefinition`, so it has the exact provider context required to establish command analysis safely.

Correct repair:

```text
for each Target RunStepDefinition
→ analyze_run_step_commands(definition, job, step)
→ pass that StaticCommandAnalysis to observe_direct_installation_declaration(...)
```

This preserves the Phase-B ownership rule:

```text
GitHub/provider owns shell parsing + command IR
dependency observer owns pip requirements meaning
Target consumes the shared analysis; it does not parse shell text itself
```

## Repair committed

Commit:

```text
a9b31ea7f97036538829ccbf9340db91c88e5198
fix: migrate target install observation to parsed commands
```

File:

```text
src/upgradepilot/target/artifact_environment.py
```

Diff size:

```text
+ import analyze_run_step_commands
+ command_analysis=analyze_run_step_commands(definition, job, step)
```

No observer compatibility fallback, runtime-strengthening policy change, Target semantic broadening, or Cycle-3 behavior was introduced.

Existing `tests/test_target_artifact_environment.py` already contains focused Target cases for positive direct requirements, absence, dynamic working directory, workflow working directory, container limitation, and other Target boundaries. The first hosted investigation test already demonstrated the missed API boundary. A fresh complete hosted run remains the authoritative proof step rather than manufacturing another redundant fixture solely for this TypeError.

## Proof state after repair

```text
B1–B5 implementation                 complete
hosted run 1 environment/setup       proven healthy
hosted run 1 focused investigation   failed on missed Target caller
repair                               committed
fresh hosted verification            REQUIRED
full deterministic suite             NOT YET EXECUTED after repair
Phase B                              NOT YET CLOSED
integrated learning phase            NOT YET STARTED
```

## Exact next action

Dispatch `Product verification` again from current `main` after the repair commit.

On the next run:

1. inspect focused investigation composition;
2. if green, inspect the full deterministic regression result and exact test count;
3. if any failure appears, diagnose/repair only the demonstrated responsibility;
4. once focused + full deterministic proof is green, update the prior Phase-B working memory / `MEMORY.md` with the final proof and close the Phase-B proof gate;
5. only then enter the agreed integrated B1–B5 learning session.

## Learning entry preserved from this proof failure

When teaching Phase B later, include this hosted-proof event alongside the final source:

- why strict API migration was correct;
- why making `command_analysis` optional would have been the wrong repair;
- difference between the main CI traversal and the independent Target consumer;
- why integration/application proof detects contract consumers that focused unit migration tests can miss;
- how the final Target path now reuses provider-owned command analysis without gaining runtime authority.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
