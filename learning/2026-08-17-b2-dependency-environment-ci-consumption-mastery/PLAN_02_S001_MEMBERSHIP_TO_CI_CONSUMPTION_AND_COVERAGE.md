# Plan 02 — S001 Membership → CI Consumption → Coverage

**Role:** active learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary case:** S001 — Pydantic / Soup Sieve `2.6 → 2.8.4`  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plan 01 gate reached sufficiently to proceed  
**Live-state authority:** `../../MEMORY.md`  
**Depth companion:** `PLAN_02_MASTERY_AND_DEPTH_MAP.md`  
**Career overlay:** `CAREER_DAY30_OWNERSHIP_HANDOFF.md`  
**Status:** `[~] ACTIVE — Chunk 1`  
**Opened:** 2026-08-21  
**Refined:** 2026-08-22 — Chunk-1 evidence roles and provenance framing corrected

## 1. Inheritance and purpose

This plan **inherits the global learning contract**. It records only Plan-02-specific route, traps, source/test targets, and gates. Global teaching rules, fair-checkpoint behavior, interruption/resume handling, Career evidence mechanics, and general proof-language discipline are not duplicated here.

Purpose:

```text
explicit static project-environment selection
→ selected-environment membership
→ static dependency consumption
→ separate direct-exercise evidence
→ separate exact-head runtime authority
→ bounded CI coverage
```

This is the main code-heavy plan. It stops at the implemented Cluster-5 proof boundary.

It does **not** establish:

```text
static↔runtime step/job correlation
exact runtime-version witness
resolver satisfiability/currentness
behavioral compatibility
safety/action recommendation
```

## 2. Plan-specific pace and depth rule

Do not study parser or graph internals beyond what is needed to explain the real S001 result, its important failure states, and the selected source responsibility.

Prefer:

```text
one real input/evidence slice
→ one coherent transformation responsibility
→ one typed output/problem state
→ one representative discriminating test
```

This plan is code-heavy, but **whole-file mastery is explicitly out of scope**. Use `PLAN_02_MASTERY_AND_DEPTH_MAP.md` to decide where to stop.

## 3. Plan-specific engineering-audit rule

This plan contains strict provenance validation, rebinding guards, typed evidence states, bounded traversal, and aggregation logic. For material checks, apply the contract's necessity classification:

```text
PROPOSITION-ESSENTIAL
CURRENT-IMPLEMENTATION REQUIREMENT
DEFENSIVE / BOUNDARY HARDENING
UNCERTAIN / AUDIT NEEDED
```

Do not assume a current check is proposition-essential merely because source/tests contain it.

Where several evidence artifacts overlap, identify the overlap and the current evaluator's actual use of each artifact rather than teaching an artificial one-fact-per-file split.

## 4. Chunk map

### [~] Chunk 1 — `pyproject.toml` + `uv.lock`: exact evidence boundary before membership semantics

#### Real question

> Given the already established `DependencyGroupSelector("docs")` and S001 `UvLockDependencyContext("soupsieve")`, what exact project/lock evidence and provenance does the current evaluator require before it may safely interpret selected-environment membership?

This chunk stops **before graph/BFS traversal**. Chunk 2 owns reachability.

#### First-contact/background subjects

At minimum-complete depth only:

- TOML and `pyproject.toml` as Python project configuration/declaration evidence;
- `[project]`, project name/root, dependency groups, and optional extras only as needed here;
- `uv.lock` as resolved lock evidence, not a single installed-environment inventory;
- difference between an explicit static environment-selection declaration and dependency/group information merely existing in project/lock files.

#### Correct evidence model

Do **not** teach `pyproject.toml` and `uv.lock` as completely disjoint evidence owners.

Use this model:

```text
STATIC ENVIRONMENT-SELECTION DECLARATION
→ establishes which project environment/group the inspected static command selected
  e.g. DependencyGroupSelector("docs")

EXACT pyproject.toml
→ primary project declaration/configuration evidence
→ current evaluator uses relevant project identity/root/group structure

EXACT uv.lock
→ resolved lock evidence
→ current evaluator uses package/dependency graph semantics
→ may also preserve overlapping project/group information
```

Important precision:

> Presence of dependency/group information in `uv.lock` does not itself establish that the inspected static CI command selected that environment. The selection proposition comes from the explicit static selection declaration; project and lock evidence then contribute to the current membership mechanism according to their actual roles.

The learning task is not to memorize **"both files are inherently required."** It is to determine:

- what each exact artifact contributes in current source;
- where their information overlaps;
- what the selection declaration contributes separately;
- why the **current evaluator** consumes both project and lock evidence;
- which requirements appear proposition-essential;
- which are implementation-specific or defensive;
- what remains outside the proof boundary.

Lock freshness / resolver currentness remains outside this chunk's proof boundary unless current source/spec explicitly establishes it.

#### Exact S001 material

Use the historical head revision and real fragments already preserved for S001:

```text
repository: pydantic/pydantic
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
changed dependency: soupsieve 2.6 → 2.8.4
selected static group: docs
```

Relevant real relation:

```text
pyproject.toml:
docs includes mkdocs-llmstxt

uv.lock:
mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve 2.8.4
```

Do not infer selected-environment membership from these fragments until the current evaluator's evidence boundary is understood.

#### UpgradePilot source / functions

Primary:

`src/upgradepilot/dependency/uv_membership.py`

- `evaluate_uv_selected_environment_membership(...)`;
- `_validate_exact_source_identity(...)`;
- project/lock parsing stages only where they determine admitted structure, project identity, selected roots, or explicit problem state.

Reuse/navigation only:

`src/upgradepilot/dependency/environment_selection.py`
- established selector/declaration types from Plan 01.

`src/upgradepilot/github/repository.py`
- exact repository-file evidence types only where a provenance question requires them.

#### Normal path vs defensive failure path

Keep these explicit:

```text
NORMAL / EXPECTED PATH
case already frozen to one immutable target revision
context + project evidence + lock evidence should refer to that same exact case/revision/root

DEFENSIVE / INVALID-INPUT PATH
_validate_exact_source_identity(...) rejects inconsistent or misbound evidence if a caller/provider/cache/test fixture violates those invariants
```

Do not teach HEAD-A project + HEAD-B lock mixing as a normal expected workflow. It is a defensive boundary case.

#### Code/audit focus

Trace in this order:

```text
evaluator entry
→ exact source/provenance validation
→ early unresolved result on invalid evidence
→ only then project/lock semantic parsing
```

For material checks ask:

- what exact mismatch is being prevented?
- should an upstream boundary normally have guaranteed it already?
- is this proposition-essential or defensive revalidation?
- if the rationale is unclear, mark `[~]` / `UNCERTAIN` rather than inventing necessity.

Do not enter traversal queue/visited/BFS mechanics in this chunk.

#### Representative test checkpoint

Use one focused exact-identity/provenance case from:

`tests/test_uv_selected_environment_membership.py`

Prefer a test that demonstrates one discriminating mismatch such as revision/source/blob/path/root identity.

Ali should explain:

```text
setup / deliberately inconsistent evidence
→ evaluator call
→ expected unresolved/problem state
→ protected boundary
→ what the test does NOT prove
```

A failure test should be clearly labeled as a **test fixture**, not normal pipeline behavior.

#### Do not miss / assume

- static selection declaration != project/lock contents;
- `pyproject.toml` and `uv.lock` may overlap in information;
- current evaluator requiring both != proof that every valid architecture must require the same two artifacts;
- `pyproject.toml` alone does not establish the exact resolved transitive lock path;
- lock/group information alone does not establish that the inspected CI command selected that group;
- provenance/identity validation happens before semantic interpretation;
- malformed/misbound evidence must not be guessed through;
- exact-revision agreement still does not prove lock freshness/resolver currentness.

#### Gate / proceed when

Ali can, with reduced assistance:

- explain the static selection declaration's role;
- explain what exact `pyproject.toml` contributes in current source;
- explain what exact `uv.lock` contributes in current source;
- identify meaningful overlap between those artifacts;
- explain why the **current evaluator** consumes both without overclaiming universal necessity;
- distinguish proposition-essential, implementation-specific, defensive, or still-uncertain requirements where material;
- trace the material source-validation/early-return path;
- explain one representative provenance test and its non-proof boundary.

Then proceed to Chunk 2.

---

### [ ] Chunk 2 — S001 graph reachability + membership witness

#### Main question

> Once exact evidence is admitted, can the explicitly selected `docs` environment reach Soup Sieve in the exact lock graph, and what evidence state/witness may UpgradePilot return?

#### Main subjects

- graph/node/edge/reachability only at this implementation's depth;
- exact workspace/project binding;
- selected roots from the explicit docs group;
- direct vs transitive membership;
- bounded traversal and witness path;
- `member` vs `not_established` vs `unresolved`.

#### Real S001 witness

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

#### UpgradePilot source / functions / types

`src/upgradepilot/dependency/uv_membership.py`

- `UvSelectedEnvironmentMembership`;
- `evaluate_uv_selected_environment_membership(...)`;
- `_bind_workspace_package(...)`;
- `_selected_roots(...)`;
- `_traverse_selected_roots(...)`;
- only private node/edge/traversal records needed to explain the algorithm.

Teach Breadth-First Search (BFS), `collections.deque`, visited-state handling, path propagation, and analysis bounds **only when this traversal is reached**.

#### Ownership/audit focus

- Ali predicts one meaningful next queue/witness/state before the result is revealed;
- understand actual queue/visited/witness control flow, not only the label `BFS`;
- explain why marker ambiguity, analysis bounds, or unsafe ambiguity yield `unresolved` rather than a fabricated negative;
- audit bounds only to the depth needed to understand false-negative/termination protection.

#### Representative tests

`tests/test_uv_selected_environment_membership.py`

Use:

- one positive S001-shaped member/witness test;
- one discriminating `not_established` or `unresolved` test.

#### Gate / proceed when

Ali can narrate the S001 witness, trace the selected-root/traversal stages, explain the material Python control flow, distinguish `not_established` from `unresolved`, and explain a discriminating test/proof boundary.

---

### [ ] Chunk 3 — Membership → exact static CI consumption

#### Main question

> Why does valid dependency/environment membership still need exact binding to the inspected CI location before CI may call it static dependency consumption?

#### Main subjects

- Dependency-owned membership semantics vs CI-owned consumption composition;
- conversion into `StaticDependencyConsumptionEvidence`;
- exact workflow/job/step/segment/package rebinding;
- static consumption remains non-runtime evidence.

#### UpgradePilot source / functions / types

`src/upgradepilot/dependency/environment_membership.py`
- source-environment comparison primitive, especially useful for later S011 transfer.

`src/upgradepilot/ci/consumption.py`
- `StaticDependencyConsumptionEvidence`;
- `compose_project_environment_consumption(...)`.

`src/upgradepilot/ci/workflow_commands.py`
- `inspect_workflow_dependency_evidence(...)`;
- `_validate_external_consumption_source(...)`;
- `WorkflowStaticDependencyEvidence`;
- direct invocation evidence only as a separate static axis.

#### Plan-specific audit focus

- before one concrete S001 composition result is shown, Ali predicts supported/not-established/unresolved static consumption;
- trace rebinding fields only where a mismatch could attach valid evidence to the wrong CI location;
- classify essential provenance binding vs defensive repetition where material;
- audit the ownership split between Dependency and CI as architecture, not scripture.

#### Do not miss / assume

- membership support is not CI consumption until bound to exact static CI location;
- same-looking job/command is not enough when exact identity is part of the current contract;
- supported static consumption says nothing about whether the command ran.

#### Gate / proceed when

Ali can explain the ownership split, trace the material composition/rebinding checks, classify their necessity where relevant, and explain one focused rebinding test/non-proof boundary.

---

### [ ] Chunk 4 — Whole-workflow evidence + bounded CI coverage

#### Main question

> How does UpgradePilot combine static consumption, separate direct-exercise evidence, and separate exact-head runtime authority without inventing static↔runtime correlation?

#### Main subjects

```text
STATIC CONSUMPTION
STATIC DIRECT EXERCISE
RUNTIME AUTHORITY
```

plus:

- multi-job static inspection;
- exact-head successful workflow/job authority;
- aggregate CI coverage state;
- strongest current bounded conclusion.

#### UpgradePilot source / functions / types

`src/upgradepilot/ci/workflow_commands.py`
- `inspect_workflow_dependency_evidence(...)` outputs needed here.

`src/upgradepilot/ci/dependency_exercise.py`
- `WorkflowDependencyExerciseInput` only as input carrier where required;
- `WorkflowDependencyCoverageResult` / `DependencyCICoverageResult`;
- `evaluate_dependency_ci_coverage(...)`;
- `_evaluate_workflow_dependency_coverage(...)`;
- selected aggregation/classifier branches only where they change evidence strength.

#### S001 expected bounded meaning

```text
supported docs-environment membership
+ exact static CI consumption
+ successful exact-head CI
→ supported_not_correlated

separate direct Soup Sieve invocation
→ not_established
```

#### Ownership/audit focus

- Ali predicts the aggregate state before it is shown;
- explain exactly what remains uncorrelated;
- trace state aggregation only at branches that change claim strength;
- audit whether the state model prevents overclaiming without unnecessary fragmentation;
- explain one representative coverage test as a claim-strength test, not merely a Python branch test.

#### Do not miss / assume

- direct exercise is an independent stronger static proposition and is not required for `supported_not_correlated`;
- successful runtime CI + static consumption does not prove the exact consuming static step ran successfully;
- successful CI does not prove exact Soup Sieve runtime installation/version, resolver currentness, behavioral compatibility, or safety.

#### Gate / proceed when

Ali can reconstruct why S001 reaches `supported_not_correlated`, explain what remains uncorrelated, state the strongest forbidden stronger claims, trace the core aggregation logic, and explain a representative focused test.

## 5. Plan-level completion gate

Plan 02 is complete enough for Plan 03 when Ali can, with reduced assistance:

- explain the corrected exact project/lock/selection evidence model and overlap;
- reconstruct selected-environment membership/traversal for S001;
- distinguish `member`, `not_established`, and `unresolved` from executable control flow;
- explain Dependency → CI consumption ownership and exact rebinding;
- keep static consumption, static direct exercise, and runtime authority separate;
- reconstruct why S001 yields `supported_not_correlated`;
- explain representative semantic tests beyond `green`;
- distinguish current implementation requirements from proposition necessity/defensive hardening where material;
- state which nearby large-file internals remain navigation/deferred.

A behavior/test modification is **not** required merely to complete this learning plan. Real failure diagnosis is recorded only if a real failure naturally occurs.

## 6. Deliberate deferral

**Must master across the route:** exact provenance/evidence boundary, selected-environment membership, three-state evidence semantics, witness path, CI consumption composition, exact rebinding integrity, coverage proof boundary, material Python control flow/syntax, representative-test reasoning, and proportionate engineering critique.

**Operational only:** TOML/`pyproject.toml` structure relevant here, uv lock semantics relevant here, GitHub Actions static semantics already established, graph/BFS background required by the actual traversal.

**Deferred:** full TOML grammar, uv resolver internals, complete marker/resolution theory, generic graph algorithms, generic shell parsing, static↔runtime correlation, resolver satisfiability/currentness, exact runtime-version witness, behavioral compatibility/safety/action.

## 7. Handoff

Proceed to Plan 03 only after the Plan-02 gate is sufficiently met. Preserve non-blocking `[~]` design questions or incidental syntax gaps rather than converting them into a perfection loop.

Before any later return to product implementation, re-read live `../../MEMORY.md`; this plan never selects the post-learning product action.
