# Plan 02 — S001 Membership → CI Consumption → Coverage

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary case:** S001 — Pydantic / Soup Sieve `2.6 → 2.8.4`  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Prerequisite:** Plan 01 gate reached sufficiently to proceed  
**Live-state authority:** `../../MEMORY.md`  
**Status:** `[ ] NOT STARTED`

## Purpose and stop line

Trace the main implemented evidence path from one explicit static project-environment selection to:

```text
selected-environment membership
→ static dependency consumption
→ separate direct-exercise evidence
→ separate exact-head runtime authority
→ bounded CI coverage
```

This is the main code-heavy plan. It stops at the implemented Cluster-5 proof boundary. It does **not** create static↔runtime step correlation, exact runtime-version witness, resolver satisfiability, or compatibility/safety conclusions.

## Pace rule

Do not study parser or graph internals beyond what explains the real S001 result and its failure states. Prefer one real input → transformation → output trace and one focused test per important boundary.

## Smart source-reading and engineering-audit rule

This is the most code-heavy plan, so the contract's source-walk rule is mandatory here:

```text
responsibility first
→ smallest coherent source slice
→ material syntax + control flow
→ real input/output
→ focused test
→ proof boundary
→ engineering judgment when a design choice needs justification
```

Do not walk every line mechanically. Read a whole helper/function closely only when its lines form one inseparable mechanism. Teach Python constructs such as dataclasses, unions, private typed records, comprehensions, `deque`, visited-state handling, `isinstance` narrowing, early returns, and rebinding checks only where they carry the current evidence semantics.

Current source/tests tell us what is implemented. For strict bounds, provenance guards, repeated validation, state models, or abstraction boundaries, ask what concrete ambiguity/failure they prevent and whether the protection appears proportionate; preserve uncertain design questions as `[~]` rather than silently praising or changing them.

## Chunk map

### [ ] Chunk 1 — `pyproject.toml` + `uv.lock`: evidence needed for one membership question

**Main subjects**
- `pyproject.toml`/TOML at the minimum depth needed for project name, optional extras, and dependency groups;
- why selected environment identity and exact resolved lock relationships are separate evidence owners;
- exact-source/provenance validation before semantic interpretation.

**Real material**
- exact S001 `pyproject.toml` and `uv.lock` fragments needed by the docs-group path;
- previously established `DependencyGroupSelector("docs")` and `UvLockDependencyContext`.

**UpgradePilot source / functions**
- `src/upgradepilot/dependency/uv_membership.py`
  - `evaluate_uv_selected_environment_membership(...)`;
  - `_validate_exact_source_identity(...)`;
  - bounded project/lock parsing stages as encountered;
- `src/upgradepilot/dependency/environment_selection.py` selector/declaration types;
- exact repository-file evidence types from `src/upgradepilot/github/repository.py` only as needed.

**Code/audit focus**
- trace the exact identity checks and their early-return/problem-state control flow;
- distinguish parser syntax that carries semantic admission from incidental parsing detail;
- audit repeated provenance validation using the Plan-01 distinction between provider guarantees and downstream strict-boundary guarantees.

**Do not miss / assume**
- provenance/identity is checked before graph meaning;
- `pyproject.toml` alone cannot prove the resolved transitive path;
- `uv.lock` alone cannot tell us which project environment was selected;
- malformed/ambiguous exact evidence must not be guessed through.

**Gate / proceed when**
- Ali can explain why both exact project metadata and exact lock evidence are required for this selected-environment membership proposition and can trace the material code that enforces that evidence boundary.

### [ ] Chunk 2 — S001 graph reachability + membership witness

**Main subjects**
- graph/node/edge/reachability only at the depth needed here;
- selected roots from the explicit docs group;
- direct vs transitive membership;
- bounded traversal and explicit witness path;
- `member` vs `not_established` vs `unresolved`.

**Real S001 witness**

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

**UpgradePilot source / functions / types**
- `src/upgradepilot/dependency/uv_membership.py`
  - `UvSelectedEnvironmentMembership`;
  - `evaluate_uv_selected_environment_membership(...)`;
  - `_bind_workspace_package(...)`;
  - `_selected_roots(...)`;
  - `_traverse_selected_roots(...)`;
  - private lock-node/edge/traversal types only where they explain the algorithm;
- Breadth-First Search (BFS), `deque`, visited/path bounds only when we reach `_traverse_selected_roots(...)`.

**Focused tests**
- `tests/test_uv_selected_environment_membership.py`.

**Code/audit focus**
- understand the actual traversal state, queue/visited/witness-path control flow, not just the label “BFS”;
- inspect why safety bounds/marker ambiguity produce `unresolved` rather than `not_established`;
- question whether each bound/state distinction protects a real false-negative/termination risk and note any non-blocking design concern explicitly.

**Do not miss / assume**
- universal-lock presence != reachability from selected roots;
- a bound/marker/ambiguous branch that prevents a safe answer yields `unresolved`, not a fabricated negative fact;
- witness path is evidence provenance, not proof of runtime installation/execution.

**Gate / proceed when**
- Ali can narrate the S001 witness, identify the main traversal stages and material control flow, and distinguish `not_established` from `unresolved`.

### [ ] Chunk 3 — Membership → exact static CI consumption

**Main subjects**
- why Dependency owns membership semantics while CI owns consumption composition;
- conversion of dependency-owned membership into `StaticDependencyConsumptionEvidence`;
- exact workflow/job/step/segment/package rebinding and provenance guards.

**UpgradePilot source / functions / types**
- `src/upgradepilot/dependency/environment_membership.py`
  - source-environment comparison primitive, needed especially for later S011 transfer;
- `src/upgradepilot/ci/consumption.py`
  - `StaticDependencyConsumptionEvidence`;
  - `compose_project_environment_consumption(...)`;
- `src/upgradepilot/ci/workflow_commands.py`
  - `inspect_workflow_dependency_evidence(...)`;
  - `_validate_external_consumption_source(...)`;
  - `WorkflowStaticDependencyEvidence`;
  - direct invocation evidence only as a separate static axis.

**Focused tests**
- `tests/test_project_source_environment_membership.py`;
- `tests/test_workflow_dependency_evidence.py`.

**Code/audit focus**
- trace typed-object construction and exact rebinding checks field by field only where a mismatch could attach valid evidence to the wrong CI location;
- distinguish essential provenance binding from potentially repetitive defensive checks;
- inspect the ownership split (Dependency establishes membership; CI composes consumption) as an architectural choice and challenge it if a concrete coupling problem appears.

**Do not miss / assume**
- membership support is not yet CI consumption until it is bound to the exact static CI location;
- same-looking job name is not enough: exact package/workflow revision/step/command/segment identity matters;
- supported static consumption still says nothing about whether the command ran.

**Gate / proceed when**
- Ali can explain why valid membership evidence requires exact CI rebinding before CI may call it consumption, and can trace the material checks without relying on a line-by-line script.

### [ ] Chunk 4 — Whole-workflow evidence + bounded CI coverage

**Main subjects**
- multi-job static inspection without pretending static jobs are correlated to runtime jobs;
- STATIC CONSUMPTION vs STATIC DIRECT EXERCISE vs RUNTIME AUTHORITY;
- exact-head successful workflow/job evidence;
- aggregate CI coverage state.

**UpgradePilot source / functions / types**
- `src/upgradepilot/ci/workflow_commands.py`
  - `inspect_workflow_dependency_evidence(...)`;
- `src/upgradepilot/ci/dependency_exercise.py`
  - `WorkflowDependencyExerciseInput`;
  - `WorkflowDependencyCoverageResult` / `DependencyCICoverageResult`;
  - `evaluate_dependency_ci_coverage(...)`;
  - `_evaluate_workflow_dependency_coverage(...)`;
  - static consumption/direct-exercise classifiers as needed.

**Focused tests**
- `tests/test_ci_dependency_coverage.py`;
- `tests/test_workflow_dependency_evidence.py`;
- `tests/test_ci_dependency_exercise.py` only where useful to contrast the retained legacy path.

**S001 expected bounded meaning**

```text
supported docs-environment membership
+ exact static CI consumption
+ successful exact-head CI
→ supported_not_correlated

separate direct Soup Sieve invocation
→ not_established
```

**Code/audit focus**
- trace how separate axes/states are aggregated without silently adding correlation;
- inspect enum/literal/state-branch control flow only where it changes evidence strength;
- ask whether the state model is expressive enough to prevent overclaiming without becoming unnecessarily fragmented; preserve any critique as an audit finding, not an unauthorized redesign.

**Do not miss / assume**
- direct exercise is a stronger independent static proposition and is not required for coverage support;
- successful runtime CI + static consumption does **not** prove that the exact consuming static step ran successfully;
- successful CI does not prove exact Soup Sieve 2.8.4 runtime installation, resolver currentness, behavioral exercise, compatibility, or safety.

**Gate / proceed when**
- Ali can reconstruct why S001 reaches `supported_not_correlated`, explain what remains uncorrelated, state the strongest claims that are still forbidden, and trace the core aggregation logic in source/tests.

## Plan-level TODO / gate

- [ ] Exact project/lock provenance requirements are understood and audited at the material boundary.
- [ ] S001 selected-root witness can be reconstructed from the actual traversal logic.
- [ ] `member` / `not_established` / `unresolved` are distinguished correctly.
- [ ] Membership → CI consumption ownership boundary is clear.
- [ ] Exact rebinding guards are understood at the mechanism and rationale level.
- [ ] Consumption / direct exercise / runtime authority remain separate.
- [ ] `supported_not_correlated` can be explained without overclaiming.
- [ ] Important Python syntax/control flow has been learned where it carries the mechanism; incidental code has not become a line-by-line detour.

## Depth / deliberate deferral

**Must master across the route:** exact provenance, selected-environment membership logic, three-state evidence semantics, witness path, CI consumption composition, rebinding integrity, coverage proof boundary, material Python control flow/syntax, and proportional engineering critique.  
**Operational only:** full TOML parser theory, uv resolver internals, general graph algorithms beyond this bounded traversal, full GitHub Actions runtime semantics, incidental source syntax.  
**Deferred:** static↔runtime job/step correlation, resolver-satisfiability/currentness, exact runtime-version witness, behavioral compatibility/safety/action.

## Handoff

Proceed to Plan 03 once Ali can explain the S001 positive path through current Cluster-5 typed machinery, trace its central code rather than only conceptual labels, and distinguish implementation facts from any remaining non-blocking design/audit questions.
