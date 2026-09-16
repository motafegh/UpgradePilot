# Cycle 2 Phase B Hosted Proof Repair — Working Memory

**Date:** 2026-09-16  
**Session status:** ACTIVE — two hosted proof layers inspected; bounded test-contract repairs committed; fresh hosted verification required  
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

## Diagnosis from run 1

This was a real Cycle-2 downstream migration regression, not a hosted environment problem.

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

## Repair 1 decision

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

## Repair 1 committed

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

Existing `tests/test_target_artifact_environment.py` already contains focused Target cases for positive direct requirements, absence, dynamic working directory, workflow working directory, container limitation, and other Target boundaries. The first hosted investigation test already demonstrated the missed API boundary. A fresh complete hosted run remained the authoritative proof step.

---

## Hosted verification run 3 — focused layer green, full deterministic layer exposes two residues

Latest inspected rerun:

```text
Product verification
run id: 35106389584
head: c754aeeaed08ba10744703a8ac782e8213a37b70
result: FAILURE
```

Healthy layers:

```text
checkout selected revision              PASS
Python 3.12.14 setup                    PASS
fresh package build/install             PASS
python -m pip check                      PASS
installed CLI entry-point checks        PASS
focused investigation composition       PASS — 15/15
```

This establishes that Repair 1 fixed the actual Target consumer regression.

The workflow then reached the full deterministic suite for the first time after Repair 1:

```text
python -m unittest discover -s tests -v
587 tests run
1 failure
1 error
```

### Full-suite residue A — stale removed ordinal in uv-lock structural test

Failing test:

```text
test_uv_lock_structure.UvLockStructureTests.
test_versionless_registry_record_is_rejected_once_for_all_consumers
```

Exception:

```text
TypeError: ProjectEnvironmentSelectionDeclaration.__init__()
got an unexpected keyword argument 'segment_index'
```

Diagnosis:

This was a purely mechanical B5 migration residue in a lower-domain test fixture. The production declaration contract correctly removed `segment_index`; this test still constructed the old argument even though its responsibility is uv-lock structural admission/reachability, not workflow command identity.

Repair:

```text
c4cb7dacfd57b8a059f8eb43eeb6fa1cff2ff919
test: remove stale uv lock segment ordinal
```

Only the obsolete constructor argument was removed. The test remains intentionally uncoupled from workflow command location because that is outside its responsibility.

### Full-suite residue B — dynamic GitHub-expression uncertainty moved to the provider boundary

Failing integration test:

```text
test_r6_project_environment_workflow_integration.
R6ProjectEnvironmentWorkflowIntegrationTests.
test_dynamic_uv_group_remains_unresolved_through_ci_coverage
```

Observed difference:

```text
expected: project_environment_selection_unresolved
actual:   project_environment_command_analysis_unresolved
```

Input shape:

```yaml
run: uv sync --group "${{ matrix.group }}"
```

The important semantic invariant still held:

```text
dynamic project selector
→ unresolved project-environment consumption
→ unresolved CI coverage
→ never becomes supported or not-observed
```

What changed is the **earliest owner of the uncertainty**. Under the parser-backed architecture, the shell parser sees the GitHub-expression syntax before the dependency selector interpreter. Because arbitrary GitHub expression evaluation is explicitly outside the current plan, a material parser-level ambiguity may conservatively stop the step at:

```text
project_environment_command_analysis_unresolved
```

rather than manufacturing a dependency-level parsed selector and reporting:

```text
project_environment_selection_unresolved
```

### Why we did not broaden the implementation here

During diagnosis we considered whether to add GitHub-expression masking/evaluation solely so Tree-sitter could recover a dynamic argument atom. That would widen the provider responsibility during a proof-gate repair and could create new expression-language correctness obligations.

The controlling plan explicitly excludes arbitrary GitHub expression evaluation, and the current product result is already conservative and proposition-correct. Therefore the bounded repair is to reconcile the integration test with the new ownership boundary, not to make the parser pretend it has stronger source understanding than it currently earns.

This preserves an important distinction for later learning:

```text
same final uncertainty proposition
can move to an earlier trustworthy owner
when architecture changes
```

The test now verifies that provider-level command-analysis uncertainty is preserved through R6/CI composition and is not collapsed into absence.

Repair:

```text
ea74add45ebd4224cffecd3d7d85e822f61b25e8
test: preserve provider-level dynamic command uncertainty
```

The exact two-commit repair diff from `c754aee...` to `ea74add...` touches only:

```text
tests/test_uv_lock_structure.py
tests/test_r6_project_environment_workflow_integration.py
```

No product source, parser behavior, dependency semantics, CI ordering, runtime strengthening, or Cycle-3 behavior changed.

---

## Proof state after second hosted repair

```text
B1–B5 implementation                          complete
hosted environment/fresh install              proven healthy
Target downstream strict-API repair            proven by focused 15/15 rerun
full deterministic suite                       executed: 587 tests
full suite at c754aee                           585 pass-equivalent + 1 failure + 1 error
stale ordinal fixture repair                    committed
provider-level uncertainty expectation repair  committed
fresh hosted verification at current main      REQUIRED
Phase B                                        NOT YET CLOSED
integrated learning phase                      NOT YET STARTED
```

## Exact next action

Dispatch `Product verification` again from current `main` after `ea74add45ebd4224cffecd3d7d85e822f61b25e8` and this state-preservation commit.

On the next run:

1. verify fresh install / `pip check` / CLI steps remain green;
2. verify focused investigation remains 15/15 green;
3. verify the full deterministic suite is completely green and record the exact current test count;
4. if another failure appears, diagnose/repair only the demonstrated responsibility and preserve the event;
5. once all layers are green, update the main Phase-B working memory and `MEMORY.md`, formally close the Phase-B proof gate, and enter the agreed integrated B1–B5 learning session.

## Learning entries preserved from hosted proof

When teaching Phase B later, include both proof failures alongside the final source:

- why strict API migration was correct;
- why making `command_analysis` optional would have been the wrong repair;
- difference between the main CI traversal and the independent Target consumer;
- why integration/application proof detects contract consumers that focused unit migration tests can miss;
- how B5 removal of an identity field can leave stale lower-domain test constructors even after production contracts are clean;
- how a parser-backed architecture can move an unresolved result to an earlier owner without strengthening or weakening the final evidence proposition;
- why we did not silently expand into GitHub-expression evaluation during a bounded proof repair;
- how the final Target path reuses provider-owned command analysis without gaining runtime authority.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-working-memory`
