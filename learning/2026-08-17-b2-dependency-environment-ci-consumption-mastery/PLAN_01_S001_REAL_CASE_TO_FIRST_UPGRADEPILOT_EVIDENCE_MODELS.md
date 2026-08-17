# Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Live-state authority:** `../../MEMORY.md`  
**Status:** `[ ] NOT STARTED`

## Purpose and stop line

Build the minimum real-world understanding needed to enter UpgradePilot's dependency/source/workflow-selection code without treating unfamiliar target-project mechanisms as unexplained premises.

This plan stops once we can connect:

```text
real S001 dependency update
→ exact dependency/source evidence
→ bounded GitHub Actions workflow structure
→ static project-environment selection declaration
```

It does **not** yet prove selected-environment membership, CI dependency consumption, runtime execution, or CI coverage.

## Pace rule

Background is just-in-time. Each first-contact topic gets only enough depth to make the next real evidence/code step coherent. One meaningful understanding check is normally enough to proceed; non-blocking gaps become `[~]` rather than a reason to stall.

## Chunk map

### [ ] Chunk 1 — S001 orientation + Soup Sieve first contact

**Main subjects**
- exact S001 event and dependency transition;
- what Pydantic is at the depth needed here;
- Soup Sieve, CSS-selector matching, and its immediate Beautiful Soup relationship;
- why Soup Sieve can exist in Pydantic's documentation/tooling dependency path rather than core runtime.

**Real material**
- `product-simulation/scenarios/S001-pydantic-soupsieve-2.6-to-2.8.4/CASE.md`;
- exact historical dependency relation already preserved for S001.

**First-contact flags**
- Soup Sieve;
- CSS selector;
- Beautiful Soup;
- direct vs transitive dependency, only as far as needed for this case.

**Do not miss / assume**
- do not jump to `uv.lock`, docs CI, graph traversal, or UpgradePilot types before the dependency itself makes sense;
- S001 is historical manual evidence, not current product execution truth.

**Gate / proceed when**
- Ali can explain what Soup Sieve does and why its presence in Pydantic can be documentation/tooling-related rather than a Pydantic runtime dependency.

### [ ] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence

**Main subjects**
- package dependency resolution and why lockfiles exist;
- `uv` at the operational depth needed by S001;
- `uv.lock` as a universal lock, not one CI environment;
- relevant real lock structure and the Soup Sieve dependency path.

**Real material**
- exact historical S001 `uv.lock` evidence at head `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`;
- relevant workspace/docs/package records only.

**First-contact flags**
- dependency resolver;
- lockfile;
- universal lock;
- package record / dependency edge where encountered.

**Do not miss / assume**
- `soupsieve` being present in `uv.lock` does **not** establish that a particular environment selected or installed it;
- do not turn this into a course on uv's resolver internals.

**Gate / proceed when**
- Ali can read the relevant real lock fragment and explain why lock presence alone is insufficient for environment-selection/consumption claims.

### [ ] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI

**Main subjects**
- CI (Continuous Integration) practical purpose;
- GitHub Actions workflow → job → step → `run` command;
- what documentation CI means in this exact target project;
- relevant Pydantic documentation workflow/environment command.

**Real material**
- exact historical Pydantic workflow definition and S001 CI evidence;
- the documentation job's actual purpose and relevant dependency-selection command.

**First-contact flags**
- CI;
- GitHub Actions;
- workflow/job/step;
- documentation CI / docs CI.

**Do not miss / assume**
- static workflow definition is not runtime execution evidence;
- passing documentation CI may be relevant to a documentation dependency without proving unrelated Pydantic runtime behavior.

**Gate / proceed when**
- Ali can explain what Pydantic's docs CI is for and identify the relevant static command without claiming that merely reading YAML proves execution.

### [ ] Chunk 4 — Exact dependency transition + dependency-owned source context

**Main subjects**
- how UpgradePilot establishes one canonical dependency version change;
- why exact source provenance travels with the change;
- how `DependencyChangeAnalysis.source_contexts` preserves source/environment meaning needed later.

**UpgradePilot source / functions / types**
- `src/upgradepilot/dependency/change.py`
  - `DependencyChangeSourceEvidence`;
  - `DependencyVersionChange`;
  - `compare_extracted_dependency_changes(...)`;
- `src/upgradepilot/dependency/analysis.py`
  - `DependencyChangeAnalysis`;
  - `analyze_dependency_change(...)`;
  - source-context construction;
- `src/upgradepilot/dependency/environment.py`
  - especially `UvLockDependencyContext`;
- `src/upgradepilot/dependency/uv_lock.py`
  - inspect the source-specific extraction path only as needed.

**Focused tests**
- `tests/test_dependency_change.py` / comparison-contract tests as needed;
- `tests/test_dependency_analysis.py`;
- `tests/test_uv_lock_change.py`.

**Do not miss / assume**
- package/version transition != dependency environment membership;
- `UvLockDependencyContext` says where the changed dependency evidence came from; it does not invent a selected group/extra;
- package-name normalization and exact revision/source identity matter before later composition.

**Gate / proceed when**
- Ali can trace the real S001 change into the canonical change + source context and state their inputs, outputs, and proof boundary.

### [ ] Chunk 5 — Static workflow IR + project-environment selection

**Main subjects**
- why GitHub owns workflow structure while Dependency interprets project-environment selectors;
- provider-owned bounded workflow IR;
- effective working-directory context only when it changes command meaning;
- recognition of explicit pip/uv project environment selectors.

**UpgradePilot source / functions / types**
- `src/upgradepilot/github/workflow_definition.py`
  - `parse_workflow_definition(...)`;
  - `WorkflowDefinition`;
  - `StepsJobDefinition`;
  - `RunStepDefinition`;
  - `RunDefaults`;
- `src/upgradepilot/dependency/environment_selection.py`
  - `observe_project_environment_selection(...)`;
  - `ProjectEnvironmentSelectionObservation`;
  - `ProjectEnvironmentSelectionDeclaration`;
  - `OptionalExtraSelector` / `DependencyGroupSelector` / all-selector variants;
- `src/upgradepilot/dependency/workflow_context.py`
  - effective working-directory/path resolution helpers only where causally relevant.

**Focused tests**
- `tests/test_github_workflow_definition.py`;
- `tests/test_project_environment_selection.py`;
- working-directory tests only when needed by the real command.

**Do not miss / assume**
- static selector observation != command execution;
- workflow/job/step structure and dependency/environment semantics have different owners;
- dynamic/unsupported context should become unresolved rather than guessed.

**Gate / proceed when**
- Ali can start from the real S001 workflow command, follow the provider IR into `observe_project_environment_selection(...)`, and predict the typed static selection without adding runtime meaning.

## Plan-level TODO / gate

- [ ] S001 dependency itself makes sense before package-management reasoning.
- [ ] Relevant `uv.lock` structure is readable at the minimum useful depth.
- [ ] CI/docs-CI terminology is grounded in the exact Pydantic workflow.
- [ ] Canonical change + source context can be traced through current source.
- [ ] Static workflow selection can be traced through current source.
- [ ] Ali can state what Plan 01 still **does not prove**.

## Depth / deliberate deferral

**Must master across the route:** exact change/source provenance, static-vs-runtime distinction, source context vs selection, central inputs/outputs.  
**Operational only here:** Soup Sieve internals, uv resolver internals, full GitHub Actions semantics, full YAML/TOML theory.  
**Deferred to Plan 02:** `pyproject.toml` + lock membership proof, graph reachability, CI consumption, direct exercise, runtime authority, coverage aggregation.

## Handoff

Proceed to Plan 02 when the real S001 event can be followed into a typed static environment-selection declaration without silently assuming membership or execution.
