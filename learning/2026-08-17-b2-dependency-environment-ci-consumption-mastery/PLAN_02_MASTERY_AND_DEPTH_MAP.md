# Plan 02 — Mastery and Depth Map

**Companion to:** `PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md`  
**Purpose:** define the exact ownership depth for the most code-heavy part of the current learning route  
**Authority:** subordinate to the learning contract, live `../../MEMORY.md`, active source/tests, and Plan 02  
**Important rule:** Ali owns selected mechanisms, not every line in every file.  
**Refined:** 2026-08-22 — Chunk-1 evidence overlap and necessity-vs-implementation mastery aligned

## 1. Depth labels

### OWN / MASTER

Ali can reconstruct the selected responsibility with reduced assistance:

```text
real input/precondition
→ central types/functions
→ material executable control flow
→ important states/branches
→ output/problem
→ representative test
→ proof/non-proof boundary
```

When material, Ali can also distinguish:

```text
CURRENT IMPLEMENTATION FACT
PROPOSITION-ESSENTIAL REQUIREMENT
CURRENT-IMPLEMENTATION REQUIREMENT
DEFENSIVE / BOUNDARY HARDENING
UNCERTAIN / AUDIT NEEDED
plausible alternative design
```

### STRONG WORKING UNDERSTANDING

Ali can follow the source and explain why it exists, its important inputs/outputs, and branches that affect the current proposition. Detailed internals are learned only when they carry the mechanism.

### NAVIGATE / RECOGNIZE

Ali knows where the source lives, what it contributes, and when to inspect it, without broad ownership.

### OPERATIONAL BACKGROUND

Ali understands the external concept enough to reason correctly about UpgradePilot without mastering the external implementation.

### DEFER

Do not spend capacity here unless later real work makes it causally necessary.

## 2. Plan-02 end state

By the end of Plan 02, Ali should own the selected-environment membership → static CI consumption → bounded CI coverage mechanism strongly enough to reason through the current source and representative tests, while explicitly leaving parser breadth, generic graph theory, full workflow/runtime semantics, and stronger compatibility/safety claims outside the target.

Proof ladder:

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
exact proposed runtime-version witness
resolver satisfiability/currentness
behavioral compatibility
safety/action recommendation
```

## 3. Chunk 1 — Exact project + lock evidence before semantic membership

### `src/upgradepilot/dependency/uv_membership.py`

**OWN / MASTER — evaluator entry + evidence boundary:**

- `evaluate_uv_selected_environment_membership(...)` as public entry;
- `_validate_exact_source_identity(...)` and material checks that determine whether semantic interpretation may proceed;
- high-level control flow from exact source validation to project/lock parsing or explicit unresolved/problem state.

Ali should be able to reconstruct:

```text
selected environment declaration
+ exact project evidence
+ exact lock evidence
+ changed package/source context
→ provenance/source validation
→ bounded semantic preparation
→ later membership evaluation path
```

### Correct evidence-role mastery

Ali should **not** memorize a false clean split such as:

```text
pyproject.toml = selection
uv.lock = graph
```

Instead Ali should understand:

```text
STATIC SELECTION DECLARATION
→ tells the current analysis which project environment/group the inspected static command selected

EXACT pyproject.toml
→ primary project declaration/configuration evidence used by the current evaluator for relevant project identity/root/group semantics

EXACT uv.lock
→ resolved lock evidence used by the current evaluator for dependency graph semantics
→ may also contain overlapping project/group information
```

OWN / MASTER includes being able to explain:

- where `pyproject.toml` and `uv.lock` overlap;
- what the current evaluator actually consumes from each;
- why the current evaluator requires both exact artifacts;
- why that current requirement is not automatically proof that every valid architecture must use the same two artifacts;
- what the static selection declaration contributes separately;
- what none of these artifacts proves alone;
- why exact-revision/source agreement still does not establish lock freshness/resolver currentness.

### Provenance/defensive-boundary mastery

Ali should distinguish:

```text
NORMAL / EXPECTED PATH
all evidence for one frozen case should already agree on repository/revision/root

DEFENSIVE / INVALID-INPUT PATH
_validate_exact_source_identity(...) rejects misbound/inconsistent evidence if upstream/caller/provider/cache/test construction violates that invariant
```

Where material, Ali should classify individual checks as proposition-essential, current-implementation-specific, defensive hardening, or still uncertain rather than treating all guards as equally fundamental.

### STRONG WORKING UNDERSTANDING

Project/lock parsing only where it determines:

- admitted project structure;
- project identity/root binding;
- selected roots;
- explicit unresolved/problem states.

Do not master every parser helper or TOML/lock field.

### NAVIGATE / REUSE

`src/upgradepilot/dependency/environment_selection.py`
- selector/declaration types already established in Plan 01.

`src/upgradepilot/github/repository.py`
- exact repository-file evidence/provenance contract only when a real provenance question requires reopening it.

### NAVIGATE / DEFER

- every parser helper;
- every TOML field;
- every lock-record shape;
- broad marker/resolver semantics;
- unrelated branches;
- graph/BFS traversal mechanics, which belong to Chunk 2.

### Representative test target

`tests/test_uv_selected_environment_membership.py` — one exact-identity/provenance case.

Ali should explain:

```text
fixture setup / deliberate mismatch
→ evaluator call
→ unresolved/problem state
→ protected evidence boundary
→ what the test does not prove
```

The test's malformed/mismatched input must be recognized as a **test fixture**, not normal expected pipeline behavior.

### Chunk-1 mastery gate

Proceed when Ali can, with reduced assistance:

1. distinguish static environment selection from project/lock contents;
2. explain what exact `pyproject.toml` contributes in current source;
3. explain what exact `uv.lock` contributes in current source;
4. identify meaningful overlap between the artifacts;
5. explain why the **current evaluator** consumes both without overclaiming universal necessity;
6. classify material checks as essential / current-design / defensive / uncertain where appropriate;
7. trace source validation → early unresolved → semantic preparation;
8. explain one representative provenance test and proof boundary.

## 4. Chunk 2 — S001 graph reachability + membership witness

### `src/upgradepilot/dependency/uv_membership.py`

**OWN / MASTER — selected traversal responsibility:**

- `UvSelectedEnvironmentMembership` result semantics;
- `_bind_workspace_package(...)`;
- `_selected_roots(...)`;
- `_traverse_selected_roots(...)`;
- only private node/edge/traversal records required to understand the actual algorithm.

Ali should reconstruct:

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

Ali must also understand why bounded-analysis obstacles can yield `unresolved` rather than a fabricated `not_established` result.

### Python / algorithm constructs to MASTER IN CONTEXT

- directed graph node/edge/reachability;
- Breadth-First Search (BFS) at this implementation's depth;
- `collections.deque`;
- visited-state protection;
- path/witness propagation;
- depth/node/analysis bounds where they affect truth state;
- loop/branch control flow carrying traversal.

### OPERATIONAL ONLY / DEFER

- broad graph-theory taxonomy;
- complexity proofs beyond practical reasoning;
- alternative graph algorithms;
- generic package graph engines;
- reimplementing BFS from memory;
- every private helper;
- marker/resolver semantics not required by the selected S001 path.

### Representative test targets

`tests/test_uv_selected_environment_membership.py`

- one S001 member/witness case;
- one discriminating `not_established` or `unresolved` case.

## 5. Chunk 3 — Membership → static CI consumption

### `src/upgradepilot/dependency/environment_membership.py`

**OWN / MASTER — bounded comparison responsibility:** understand how dependency-owned source environment meaning is compared with a statically selected project environment and why the result is `member`, `not_established`, or `unresolved` without adding runtime meaning.

Own central comparison branches, normalization, and material project-root/source guards. Do not memorize every validation message/model field.

### `src/upgradepilot/ci/consumption.py`

**OWN / MASTER — composition responsibility:**

- `StaticDependencyConsumptionEvidence` semantics;
- `compose_project_environment_consumption(...)`;
- mapping dependency/environment membership into CI-owned static consumption without inventing runtime execution.

Ali should explain:

```text
dependency/environment membership evidence
+ exact static CI location/context
→ CI-owned static consumption evidence
```

and why this ownership split exists.

### `src/upgradepilot/ci/workflow_commands.py`

**STRONG WORKING UNDERSTANDING — selected slices only:**

- `inspect_workflow_dependency_evidence(...)` as whole-workflow static inspector;
- `_validate_external_consumption_source(...)` / exact rebinding;
- `WorkflowStaticDependencyEvidence` only to the depth needed for output composition;
- direct package invocation as a separate static axis.

**MASTER THE REBINDING INVARIANT, NOT THE WHOLE FILE.** Understand why external consumption must match the exact changed package and selected static CI location at the strength required by the current contract before attachment.

Where repeated checks appear, classify essential binding versus defensive duplication rather than assuming all are proposition-essential.

### NAVIGATE / DEFER

- generic command scanning;
- complete shell tokenization;
- legacy branches unrelated to the selected typed path;
- every workflow shape/helper.

### Representative tests

- `tests/test_project_source_environment_membership.py`;
- `tests/test_workflow_dependency_evidence.py`.

At least one rebinding test should be understood deeply enough to explain the wrong-attachment/overclaim it prevents.

## 6. Chunk 4 — Whole-workflow evidence + bounded CI coverage

### `src/upgradepilot/ci/dependency_exercise.py`

**OWN / MASTER — coverage evaluator responsibility:**

- `WorkflowDependencyExerciseInput` only as the input carrier needed by this path;
- `WorkflowDependencyCoverageResult` / `DependencyCICoverageResult` semantics;
- `evaluate_dependency_ci_coverage(...)`;
- `_evaluate_workflow_dependency_coverage(...)`;
- selected aggregation/classification branches that determine final claim strength.

Ali should reconstruct three independent axes:

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

Ali should know exactly what remains uncorrelated and why direct exercise is not required for that result.

### STRONG WORKING UNDERSTANDING

- multiple workflow result/problem aggregation;
- precedence of `no_successful_ci` / unresolved conditions where material;
- state/literal/union branches that change evidence strength.

### NAVIGATE / DEFER

- legacy `evaluate_dependency_ci_exercise(...)` internals beyond later Plan-04 contrast;
- old compatibility result types;
- formatting/detail fields that do not change evidence semantics;
- whole-file memorization.

### `src/upgradepilot/ci/workflow_commands.py`

**REUSE / STRONG WORKING:** revisit only static outputs consumed by coverage evaluation.

### Representative tests

`tests/test_ci_dependency_coverage.py`

- one S001 `supported_not_correlated` case;
- one discriminating unresolved/no-successful-CI case.

Ali should explain why the test protects **claim strength**, not merely one branch.

## 7. Plan-02 concepts to MASTER

By the end of Plan 02, these should be durable:

- exact provenance before semantic interpretation;
- static environment selection vs artifact contents;
- overlapping evidence across `pyproject.toml` and `uv.lock`;
- current-evaluator requirements vs proposition necessity;
- normal-path invariants vs defensive invalid-input guards;
- selected-environment identity vs universal-lock presence;
- direct vs transitive selected-environment membership;
- witness path as evidence provenance;
- `member/supported` vs `not_established` vs `unresolved`;
- bounded analysis failure must not become a negative fact;
- Dependency owns environment/source membership semantics;
- CI owns static consumption composition;
- exact rebinding prevents valid evidence from being attached to the wrong static location;
- static consumption != static direct exercise != runtime authority;
- `supported_not_correlated` and exactly why it is weaker than correlated runtime execution;
- successful CI != exact changed version observed != compatibility/safety.

## 8. Python mastery

### MASTER IN CONTEXT

- dataclasses/unions/literal-style states where they model evidence;
- guard clauses and early returns;
- typed private records where they carry parser/traversal state;
- loops/comprehensions used by the selected mechanism;
- `deque`, visited sets/maps, path accumulation;
- `isinstance(...)` narrowing;
- exact rebinding comparisons;
- aggregation across results where it determines final state.

### OPERATIONAL / DEFER

- obscure typing syntax not affecting the responsibility;
- parser tricks that do not change the active proposition;
- generic graph-algorithm theory;
- shell parsing internals;
- performance micro-optimization unless a real issue appears.

## 9. External technologies — depth limit

### OPERATIONAL BACKGROUND ONLY

- TOML / `pyproject.toml` structure relevant to project name, dependency groups, extras;
- uv lock semantics relevant to exact dependency graph;
- GitHub Actions static workflow semantics already established;
- BFS terminology/general idea before entering the actual traversal.

### DEFER

- full TOML grammar;
- uv resolver internals;
- GitHub Actions runtime engine;
- generic graph libraries/algorithms;
- resolver satisfiability/currentness.

## 10. What Plan 02 must NOT become

Do not turn this plan into:

- mastering all of `uv_membership.py`;
- mastering all of `workflow_commands.py` or `dependency_exercise.py`;
- reading every helper because it exists;
- learning every parser/marker branch;
- a TOML course;
- a uv resolver course;
- a graph algorithms course;
- a shell interpreter course;
- memorizing every state field;
- manually reproducing the implementation without AI.

For each large module, stop when Ali can own the **selected responsibility**, representative state transitions, representative test meaning, necessity/design distinction where material, and proof boundary.

## 11. Completion evidence

Plan 02 is strong enough to hand to Plan 03 when Ali can, with reduced assistance:

1. explain static selection vs exact project/lock evidence and their overlap;
2. explain why the current evaluator consumes both project + lock evidence without confusing that with universal design necessity;
3. reconstruct the selected `uv_membership.py` membership/traversal mechanism;
4. narrate the S001 witness and distinguish direct/transitive membership;
5. distinguish `not_established` from `unresolved` using real control-flow reasoning;
6. explain the environment-membership → CI-consumption ownership split;
7. explain exact CI rebinding and the bug/overclaim it prevents;
8. reconstruct the core coverage aggregation;
9. explain why S001 yields `supported_not_correlated`;
10. explain meaningful provenance/rebinding/coverage tests beyond `green`;
11. distinguish implementation fact from essential/defensive/uncertain design rationale where material;
12. state which large-file internals remain navigation-only/deferred.

Plan 02 should normally produce strong current source/test ownership candidates, but it does not require a forced code modification or artificial failure.
