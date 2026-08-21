# Plan 02 — Mastery and Depth Map

**Companion to:** `PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md`  
**Purpose:** define the exact ownership depth for the most code-heavy part of the current learning route  
**Authority:** subordinate to the learning contract, live `MEMORY.md`, active source/tests, and Plan 02  
**Important rule:** this plan contains large modules, but **Ali owns selected mechanisms, not every line in every file.**

## 1. Depth labels

### OWN / MASTER
Ali can reconstruct the selected responsibility with reduced assistance: real inputs → central types/functions → material control flow → important states/branches → output → proof boundary → representative test.

### STRONG WORKING UNDERSTANDING
Ali can follow the source and explain why it exists, its important inputs/outputs, and the branches that affect the current proposition. Detailed internals are learned only when they carry the mechanism.

### NAVIGATE / RECOGNIZE
Ali knows where the source lives, what it contributes, and when to inspect it, without broad source ownership.

### OPERATIONAL BACKGROUND
Ali understands the external concept well enough to reason correctly about UpgradePilot without mastering the external implementation.

### DEFER
Do not spend capacity here unless later real work makes it necessary.

## 2. Plan-02 end-state in one sentence

By the end of Plan 02, Ali should own the **selected-environment membership → static CI consumption → bounded CI coverage** mechanism strongly enough to reason through its current source and tests, while explicitly leaving parser breadth, generic graph theory, full workflow semantics, and stronger runtime/compatibility claims outside the mastery target.

Plan-02 proof ladder:

```text
explicit static project-environment selection
→ exact selected-environment membership
→ static dependency consumption
→ separate static direct exercise
+ separate exact-head runtime authority
→ bounded CI coverage = supported_not_correlated / no_successful_ci / unresolved
```

Still not established:

```text
static step ↔ runtime step correlation
exact proposed runtime version witness
resolver satisfiability/currentness
behavioral compatibility
safety/action recommendation
```

## 3. Chunk 1 — Exact project + lock evidence for membership

### `src/upgradepilot/dependency/uv_membership.py`

**OWN / MASTER — entry and evidence-boundary responsibility:**

- `evaluate_uv_selected_environment_membership(...)` as the public entry point;
- `_validate_exact_source_identity(...)` and the material provenance checks that determine whether semantic interpretation may proceed;
- the high-level sequence that parses exact `pyproject.toml` + exact `uv.lock` and returns typed membership evidence/problem state.

Ali should be able to explain:

```text
selected environment declaration
+ exact project evidence
+ exact lock evidence
+ changed package/source context
→ provenance/source validation
→ bounded semantic preparation
→ membership evaluation path
```

**STRONG WORKING UNDERSTANDING:** project/lock parsing stages only where they determine admitted structure, project identity, selected roots, or an explicit unresolved/problem state.

**NAVIGATE / DEFER:** every parser helper, every TOML field, every lock record shape, all marker semantics, and branches unrelated to the active S001 mechanism.

### `src/upgradepilot/dependency/environment_selection.py`

**NAVIGATE / REUSE FROM PLAN 01:** recognize selector/declaration types already learned. Do not re-master the whole file.

### `src/upgradepilot/github/repository.py`

**NAVIGATE / REUSE FROM PLAN 01:** recognize exact repository-file evidence/provenance contract. Do not reopen the entire provider client unless a real provenance question requires it.

### Representative test target

`tests/test_uv_selected_environment_membership.py` — one exact-identity/provenance case.

Ali should explain setup → evaluator call → expected state/problem → protected evidence boundary → what it does not prove.

## 4. Chunk 2 — S001 graph reachability + witness

### `src/upgradepilot/dependency/uv_membership.py`

**OWN / MASTER — selected traversal responsibility:**

- `UvSelectedEnvironmentMembership` result semantics;
- `_bind_workspace_package(...)`;
- `_selected_roots(...)`;
- `_traverse_selected_roots(...)`;
- only the private node/edge/traversal types needed to understand the actual algorithm.

Ali should be able to reconstruct:

```text
explicit selected docs group
→ bind exact workspace package
→ derive selected roots
→ traverse dependency graph
→ find soupsieve
→ preserve witness path
→ member(direct/transitive)
```

Real S001 witness:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

Ali must also understand why a bounded-analysis obstacle can produce `unresolved` rather than a fabricated `not_established` result.

### Python / algorithm constructs to MASTER IN CONTEXT

- directed graph node/edge/reachability;
- Breadth-First Search (BFS) only at this implementation's depth;
- `collections.deque` as the queue structure;
- visited-state protection;
- path/witness propagation;
- depth/node/analysis bounds where they affect truth state;
- loop and branch control flow carrying the traversal.

### OPERATIONAL ONLY

- general graph-theory taxonomy;
- complexity proofs beyond practical understanding;
- alternative graph algorithms;
- generic package dependency graph engines.

### DEFER

- reimplementing BFS from memory;
- every private record/helper in `uv_membership.py`;
- marker/resolver semantics not required by the selected S001 path.

### Representative test target

`tests/test_uv_selected_environment_membership.py` — one S001 member/witness test and one discriminating `not_established` or `unresolved` case.

## 5. Chunk 3 — Membership → static CI consumption

### `src/upgradepilot/dependency/environment_membership.py`

**OWN / MASTER — small domain comparison responsibility:** understand how a dependency-owned source environment is compared with a statically selected project environment and why the result is `member`, `not_established`, or `unresolved` without adding runtime meaning.

This file is relatively bounded; Ali should understand the central comparison branches, normalization, and project-root/source identity guards. No need to memorize every validation message or model field.

### `src/upgradepilot/ci/consumption.py`

**OWN / MASTER — composition responsibility:**

- `StaticDependencyConsumptionEvidence` semantics;
- `compose_project_environment_consumption(...)`;
- mapping dependency-owned membership evidence into CI static-consumption meaning without inventing runtime execution.

Ali should explain:

```text
dependency/environment membership evidence
+ exact static CI location/context
→ CI-owned static consumption evidence
```

and why this ownership split exists.

### `src/upgradepilot/ci/workflow_commands.py`

**STRONG WORKING UNDERSTANDING — selected slices only:**

- `inspect_workflow_dependency_evidence(...)` as the whole-workflow static inspector;
- `_validate_external_consumption_source(...)` / exact rebinding behavior;
- `WorkflowStaticDependencyEvidence` only to the depth required to understand output composition;
- direct package invocation as a separate static axis.

**MASTER THE REBINDING INVARIANT, NOT THE WHOLE FILE:** Ali should understand why external consumption must match exact changed package, workflow path/revision, static job, run-step source index, command text, and bounded segment identity before it may be attached to a CI location.

**NAVIGATE / DEFER:** generic command scanning, all shell tokenization details, legacy branches unrelated to the selected typed path, every workflow shape, and all helper functions in the ~large module.

### Representative test targets

- `tests/test_project_source_environment_membership.py`;
- `tests/test_workflow_dependency_evidence.py`.

At least one rebinding test should be understood deeply enough to explain what wrong attachment/regression it prevents.

## 6. Chunk 4 — Whole-workflow evidence + bounded CI coverage

### `src/upgradepilot/ci/dependency_exercise.py`

**OWN / MASTER — new coverage evaluator responsibility:**

- `WorkflowDependencyExerciseInput` only as the input carrier needed for this path;
- `WorkflowDependencyCoverageResult` / `DependencyCICoverageResult` semantics;
- `evaluate_dependency_ci_coverage(...)`;
- `_evaluate_workflow_dependency_coverage(...)`;
- classifiers/aggregation branches only where they determine the final evidence state.

Ali should be able to reconstruct the three independent axes:

```text
STATIC CONSUMPTION
STATIC DIRECT EXERCISE
RUNTIME AUTHORITY
```

and the bounded combination:

```text
successful exact-head CI
+ supported static consumption
→ supported_not_correlated
```

He should know exactly what remains uncorrelated and why direct exercise is not required for the coverage result.

### STRONG WORKING UNDERSTANDING

- how multiple workflow results/problems are aggregated;
- precedence of `no_successful_ci` / unresolved conditions where material;
- state/literal/union branches that change claim strength.

### NAVIGATE / DEFER

- legacy `evaluate_dependency_ci_exercise(...)` internals beyond the contrast needed for Plan 04;
- every old compatibility result type;
- all formatting/detail fields that do not change evidence semantics;
- whole-file memorization.

### `src/upgradepilot/ci/workflow_commands.py`

**REUSE / STRONG WORKING UNDERSTANDING:** revisit only the static evidence outputs consumed by coverage evaluation. Do not reread the whole module.

### Representative test target

`tests/test_ci_dependency_coverage.py` — one S001 `supported_not_correlated` test and one discriminating unresolved/no-successful-CI case.

Ali should explain why the test protects **claim strength**, not merely a Python branch.

## 7. Plan-02 core concepts to MASTER

By the end of this plan, these concepts should be durable:

- exact provenance before semantic interpretation;
- selected environment identity versus universal-lock presence;
- direct versus transitive selected-environment membership;
- witness path as evidence provenance;
- `member/supported` versus `not_established` versus `unresolved`;
- bounded analysis failure must not become a negative fact;
- Dependency owns environment/source membership semantics;
- CI owns static consumption composition;
- exact rebinding prevents valid evidence from being attached to the wrong static location;
- static consumption != static direct exercise != runtime authority;
- `supported_not_correlated` and exactly why it is weaker than correlated runtime execution;
- successful CI != exact changed version observed != compatibility/safety.

## 8. Plan-02 Python mastery

### MASTER IN CONTEXT

- dataclasses/unions/literal-style states when they model evidence;
- guard clauses and early returns;
- typed private records only when they carry parser/traversal state;
- loops/comprehensions used by the selected algorithm;
- `deque`, visited sets/maps, path accumulation;
- `isinstance(...)` narrowing;
- exact rebinding comparisons;
- aggregation across tuples/results where it determines final state.

### OPERATIONAL / DEFER

- obscure typing syntax not affecting the responsibility;
- parser tricks that do not change the active case;
- generic graph algorithm theory;
- shell parsing internals;
- performance micro-optimization unless a real issue appears.

## 9. External technologies — depth limit

### OPERATIONAL BACKGROUND ONLY

- TOML / `pyproject.toml` structure relevant to project name, dependency groups, extras;
- uv lock semantics relevant to exact dependency graph;
- GitHub Actions static workflow semantics already established;
- BFS terminology/general idea.

### DEFER

- full TOML grammar;
- uv resolver internals;
- GitHub Actions runtime engine;
- generic graph libraries/algorithms;
- resolver satisfiability/currentness.

## 10. What Plan 02 must NOT become

Do not turn this plan into:

- mastering all ~30 KB of `uv_membership.py`;
- mastering all ~22–25 KB of `workflow_commands.py` or `dependency_exercise.py`;
- reading every helper because it exists;
- learning every parser branch;
- a graph algorithms course;
- a shell interpreter course;
- a requirement to memorize every state field;
- a requirement to manually reproduce implementation without AI.

For each large module, stop when Ali can own the **selected responsibility**, representative state transitions, proof boundary, and one meaningful test.

## 11. Plan-02 completion evidence

Plan 02 is strong enough to hand to Plan 03 when Ali can, with reduced assistance:

1. explain why exact project + lock evidence are both required;
2. reconstruct the selected `uv_membership.py` membership/traversal mechanism;
3. narrate the S001 witness and distinguish direct/transitive membership;
4. distinguish `not_established` from `unresolved` using real control-flow reasoning;
5. explain the environment-membership → CI-consumption ownership split;
6. explain exact CI rebinding and the bug/overclaim it prevents;
7. reconstruct the core `evaluate_dependency_ci_coverage(...)` aggregation;
8. explain why S001 yields `supported_not_correlated`;
9. explain at least one meaningful membership/rebinding/coverage test beyond “green”;
10. state which large-file internals are navigation-only/deferred.

Plan 02 should normally produce the strongest current **source + test ownership candidates**, but it does not require a forced code modification or artificial failure.