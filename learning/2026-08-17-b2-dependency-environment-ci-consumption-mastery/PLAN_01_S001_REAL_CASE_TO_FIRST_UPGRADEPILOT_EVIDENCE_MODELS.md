# Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Live-state authority:** `../../MEMORY.md`  
**Status:** `[~] ACTIVE — Chunk 4`

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

## Smart source-reading and engineering-audit rule

This plan inherits the contract's source-walk and engineering-audit rules. In code-bearing chunks:

```text
orient to the responsibility
→ read the real material code/syntax/control flow
→ explain only syntax that carries the mechanism
→ inspect focused tests
→ ask why the design is shaped that way
→ distinguish essential invariants from defensive/transitional/redundant machinery
→ challenge questionable design when justified
```

Do **not** turn source reading into compulsory line-by-line commentary. A whole function or file may be read closely when its lines are tightly coupled to the responsibility, but incidental imports, punctuation, boilerplate, or unrelated branches should not receive equal teaching weight.

Current source/tests establish what UpgradePilot does at the pinned snapshot; they do not automatically establish that every design choice is optimal. If a material field, validation, abstraction, or branch appears unnecessary or excessive, identify the failure mode it protects before judging it.

## Chunk map

### [x] Chunk 1 — S001 orientation + Soup Sieve first contact

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

### [x] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence

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

### [x] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI

**Main subjects**
- CI (Continuous Integration) practical purpose;
- GitHub Actions workflow → job → step → `run` and material `uses:`/`with:` steps;
- what documentation CI means in this exact target project;
- relevant Pydantic documentation workflow/environment command.

**Real material**
- exact historical Pydantic workflow definition and S001 CI evidence;
- the documentation job's actual purpose and relevant dependency-selection command;
- material reusable Actions such as `actions/checkout` and `astral-sh/setup-uv` when they affect the job's meaning.

**First-contact flags**
- CI;
- GitHub Actions;
- workflow/job/step;
- `run:` versus packaged `uses:` Action invocation and `with:` inputs;
- documentation CI / docs CI.

**Do not miss / assume**
- static workflow definition is not runtime execution evidence;
- passing documentation CI may be relevant to a documentation dependency without proving unrelated Pydantic runtime behavior.

**Gate / proceed when**
- Ali can explain what Pydantic's docs CI is for and identify the relevant static command without claiming that merely reading YAML proves execution.

### [~] Chunk 4 — Exact dependency transition + dependency-owned source context

**Main subjects**
- how exact repository-file evidence is represented and validated before dependency semantics;
- what repository/path/revision/blob/byte provenance fields mean and what failure/ambiguity each protects against;
- how UpgradePilot establishes one canonical dependency version change;
- why exact source provenance travels with the change;
- how `DependencyChangeAnalysis.source_contexts` preserves source/environment meaning needed later;
- whether material validation/metadata choices are essential, defensive, transitional, redundant, or candidates for future simplification.

**UpgradePilot source / functions / types**
- `src/upgradepilot/github/repository.py`
  - `RepositoryTextFile` / historical alias `ExactRepositoryTextFile`;
  - exact base/head acquisition path and response validation only as needed to understand provenance;
- `src/upgradepilot/dependency/change.py`
  - `DependencyChangeSourceEvidence`;
  - `ExtractedDependencyVersionChange`;
  - `DependencyVersionChange`;
  - `compare_extracted_dependency_changes(...)`;
- `src/upgradepilot/dependency/analysis.py`
  - `DependencyChangeAnalysis`;
  - `analyze_dependency_change(...)`;
  - `_source_contexts(...)`;
- `src/upgradepilot/dependency/environment.py`
  - especially `UvLockDependencyContext`;
- `src/upgradepilot/dependency/uv_lock.py`
  - `extract_uv_lock_changes(...)`;
  - `_build_source_evidence(...)`;
  - parse/compare helpers only where they carry the exact-transition responsibility.

**Material Python syntax / control flow to learn here**
- `@dataclass(frozen=True, slots=True)` where evidence-model design depends on it;
- union/optional annotations such as `str | None` and result unions;
- typed function signatures as responsibility contracts;
- `isinstance(...)` narrowing and early-return problem propagation;
- assertions/invariants after prior type-state checks;
- construction of typed evidence/results and `**common` / `**kwargs` style unpacking when `_source_contexts(...)` is reached;
- comprehensions/sets only where they explain PR-wide comparison semantics.

**Focused tests**
- `tests/test_uv_lock_change.py`;
- `tests/test_dependency_change.py` / comparison-contract tests as needed;
- `tests/test_dependency_analysis.py`.

**Engineering-audit prompts**
- Is `repository + path + revision` the core identity, and what extra protection does `blob_sha` add?
- What do reported/decoded byte counts protect: semantic truth, acquisition consistency, boundedness, or something else?
- Which validations are already guaranteed by the GitHub provider and which are repeated because the evidence type still admits weaker/manual fixtures?
- Would stronger distinct evidence types reduce repeated downstream validation, or would that create other costs? Treat this as a design question, not an automatic refactor conclusion.

**Do not miss / assume**
- package/version transition != dependency environment membership;
- source provenance is not decorative metadata, but not every provenance field is equally fundamental;
- do not claim blob SHA is independently cryptographically recomputed from downloaded bytes unless source actually does so;
- `UvLockDependencyContext` says where the changed dependency evidence came from; it does not invent a selected group/extra;
- package-name normalization and exact revision/source identity matter before later composition;
- current code is implementation truth, not automatic proof that its evidence model is perfectly minimal.

**Gate / proceed when**
- Ali can trace the real S001 change through exact file evidence → file-level extraction → PR-wide canonical change → source context;
- Ali can state the inputs, outputs, proof boundary, and the purpose/proportionality of the material provenance/validation choices;
- Ali can explain the important Python syntax/control flow carrying that path without needing a line-by-line script.

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

**Material code-reading focus**
- typed IR dataclasses/unions only where they explain which workflow shapes are admitted;
- parser branching/problem states only where they affect evidence interpretation;
- selector recognition/control flow and working-directory precedence;
- challenge strictness/abstention decisions by asking what unsupported/dynamic ambiguity they prevent rather than assuming every branch is necessary.

**Focused tests**
- `tests/test_github_workflow_definition.py`;
- `tests/test_project_environment_selection.py`;
- working-directory tests only when needed by the real command.

**Do not miss / assume**
- static selector observation != command execution;
- workflow/job/step structure and dependency/environment semantics have different owners;
- dynamic/unsupported context should become unresolved rather than guessed;
- provider/parser complexity should be learned only to the degree needed to understand the admitted evidence boundary.

**Gate / proceed when**
- Ali can start from the real S001 workflow command, follow the provider IR into `observe_project_environment_selection(...)`, predict the typed static selection without adding runtime meaning, and explain the material control flow/syntax that carries that interpretation.

## Plan-level TODO / gate

- [x] S001 dependency itself makes sense before package-management reasoning.
- [x] Relevant `uv.lock` structure is readable at the minimum useful depth.
- [x] CI/docs-CI terminology is grounded in the exact Pydantic workflow.
- [ ] Canonical change + source context can be traced through current source and audited at the material design boundaries.
- [ ] Static workflow selection can be traced through current source.
- [ ] Ali can state what Plan 01 still **does not prove**.

## Depth / deliberate deferral

**Must master across the route:** exact change/source provenance, static-vs-runtime distinction, source context vs selection, central inputs/outputs, material source control flow/syntax, and the ability to question design choices proportionately.  
**Operational only here:** Soup Sieve internals, uv resolver internals, full GitHub Actions semantics, full YAML/TOML theory, incidental Python syntax not carrying the mechanism.  
**Deferred to Plan 02:** `pyproject.toml` + lock membership proof, graph reachability, CI consumption, direct exercise, runtime authority, coverage aggregation.

## Handoff

Proceed to Plan 02 when the real S001 event can be followed into a typed static environment-selection declaration without silently assuming membership or execution, and when the important current design choices encountered in Plan 01 have been understood or explicitly left as non-blocking `[~]` audit questions rather than blindly accepted.
