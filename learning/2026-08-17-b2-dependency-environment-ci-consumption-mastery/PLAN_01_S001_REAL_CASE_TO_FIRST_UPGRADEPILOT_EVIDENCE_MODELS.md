# Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Role:** learning execution map under `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Primary case:** S001 — `pydantic/pydantic#13432`, Soup Sieve `2.6 → 2.8.4`  
**Implementation anchor:** `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`  
**Live-state authority:** `../../MEMORY.md`  
**Depth companion:** `PLAN_01_MASTERY_AND_DEPTH_MAP.md`  
**Career ownership overlay:** `CAREER_DAY30_OWNERSHIP_HANDOFF.md` — evidence/participation rules only; no technical sequencing authority  
**Status:** `[~] CONTENT ROUTE COMPLETE — formal ownership/test gates deferred`  
**Content route completed:** 2026-08-21  
**Refined:** 2026-08-22 — execution map aligned with explicit depth-rationale and parallel-audit rules; historical learning status preserved

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

## Pace and depth rule

Background is just-in-time. Each first-contact topic gets only enough depth to make the next real evidence/code step coherent. One meaningful understanding check is normally enough to proceed; non-blocking gaps become `[~]` rather than a reason to stall.

Before asking Ali to learn a material concept/source responsibility at MASTER/OWN or non-obvious working depth, use `PLAN_01_MASTERY_AND_DEPTH_MAP.md` and state the brief project-local reason that depth matters. Do not deepen a topic merely because it is complex or because its file is large.

## Smart source-reading and parallel engineering-audit rule

This plan inherits the contract's source-walk and engineering-audit rules. In code-bearing chunks:

```text
orient to the responsibility
→ state why this responsibility deserves the planned depth
→ Ali predicts/reconstructs before key answers when enough context exists
→ read the real material code/syntax/control flow
→ explain only syntax that carries the mechanism
→ inspect a focused representative test
→ Ali explains setup → action → assertion → protected behavior → non-proof boundary
→ evaluate correctness/proof strength/ownership/design in parallel
→ distinguish essential invariants from current-design requirements, defensive/transitional checks, and uncertain rationale
→ preserve material findings at the proper owner
```

Do **not** turn source reading into compulsory line-by-line commentary. A whole function or file may be read closely when its lines are tightly coupled to the responsibility, but incidental imports, punctuation, boilerplate, or unrelated branches should not receive equal teaching weight.

Current source/tests establish what UpgradePilot does at the pinned snapshot; they do not automatically establish that the behavior is correct for the product or that every design choice is optimal. If a material field, validation, abstraction, or branch appears unnecessary or excessive, identify the failure mode/evidence that actually supports it before judging it. If the rationale cannot be established, classify it as uncertain instead of inventing a reason.

Comments/docstrings are legitimate orientation scaffolding but are **not** source-ownership evidence by themselves. A source gate requires Ali to reconstruct the executable constructs that carry the behavior. Likewise, merely watching a test pass is not test understanding.

Do not force a source/test mutation or manufacture a failure for Career evidence. If a legitimate modification or real failure naturally appears, use the handoff's pre-change or diagnosis protocol; otherwise continue the technical route normally.

Material durable audit findings should follow `../../audits/README.md`; small local observations may remain in `LEARNING_MEMORY.md`.

## Chunk map

### [x] Chunk 1 — S001 orientation + Soup Sieve first contact

**Main subjects**
- exact S001 event and dependency transition;
- what Pydantic is at the depth needed here;
- Soup Sieve, CSS-selector matching, and its immediate Beautiful Soup relationship;
- why Soup Sieve can exist in Pydantic's documentation/tooling dependency path rather than core runtime.

**Why this depth matters**
- this dependency relationship is the real-case anchor for every later relevance/environment/CI question;
- Soup Sieve/Beautiful Soup internals beyond that relation do not affect UpgradePilot's current responsibility.

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

**Why this depth matters**
- Plan 02 later reasons directly from exact lock evidence, so Ali must own the proof boundary `lock presence != selected environment`;
- uv resolver internals do not determine the current UpgradePilot proposition and remain operational/deferred.

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

**Why this depth matters**
- static-vs-runtime evidence is a recurring UpgradePilot proof boundary and must be durable;
- broad GitHub Actions runtime/provider internals are unnecessary unless later source work enters them.

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
- what repository/path/revision/blob/byte provenance fields mean and what failure/ambiguity each demonstrably protects against;
- how UpgradePilot establishes one canonical dependency version change;
- what role exact source provenance serves as the change moves downstream;
- how `DependencyChangeAnalysis.source_contexts` preserves source/environment meaning needed later;
- whether material validation/metadata choices are correct, essential, defensive, transitional, redundant, or candidates for future simplification.

**Why this depth matters**
- this is the first executable evidence pipeline later membership/CI logic trusts;
- `uv_lock.py` extraction and `change.py` reconciliation directly control what becomes the canonical dependency transition, so they deserve source/test ownership;
- provider/orchestration internals only need enough depth to verify trust/composition and audit repeated validation.

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

**Focused tests / Career test-ownership candidate**
- `tests/test_uv_lock_change.py` — inspect at least one successful exact-transition/provenance case and one discriminating problem case when useful;
- `tests/test_dependency_change.py` / comparison-contract tests as needed;
- `tests/test_dependency_analysis.py`.

For at least one representative test, Ali should predict the result before it is revealed where practical and then explain:

```text
setup/evidence state
→ action/function under test
→ assertion/expected state
→ behavior/invariant protected
→ what the test does NOT prove
```

**Career source-ownership checkpoint**
- After independent study/orientation, Ali reconstructs one meaningful current source responsibility from executable code rather than comments alone.
- Preferred first candidate: `src/upgradepilot/dependency/uv_lock.py` file-level exact transition extraction.
- Required shape: real input/precondition → owning function/type → material control flow → output/problem → established purpose → proof boundary → design/correctness judgment where material.
- Assistance level should be recorded honestly in `LEARNING_MEMORY.md` at a meaningful boundary; no Career promotion is implied.

**Engineering-audit prompts**
- Is `repository + path + revision` the core identity, and what extra protection does `blob_sha` demonstrably add?
- What do reported/decoded byte counts protect: semantic truth, acquisition consistency, boundedness, or something else?
- Which validations are already guaranteed by the GitHub provider and which are repeated because the evidence type still admits weaker/manual fixtures?
- Would stronger distinct evidence types reduce repeated downstream validation, or would that create other costs? Treat this as a design question, not an automatic refactor conclusion.
- Reuse `../../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md` when this issue is revisited; do not invent a new rationale unless new evidence changes the finding.

**Do not miss / assume**
- package/version transition != dependency environment membership;
- source provenance is not decorative metadata, but not every provenance field is equally fundamental;
- do not claim blob SHA is independently cryptographically recomputed from downloaded bytes unless source actually does so;
- `UvLockDependencyContext` says where the changed dependency evidence came from; it does not invent a selected group/extra;
- package-name normalization and exact revision/source identity matter before later composition;
- current code is implementation truth, not automatic proof that its evidence model is correct or minimal;
- source comments/docstrings may orient the study but do not satisfy the ownership gate without executable-code reconstruction.

**Gate / proceed when**
- Ali can trace the real S001 change through exact file evidence → file-level extraction → PR-wide canonical change → source context;
- Ali can state the inputs, outputs, proof boundary, why the selected source responsibilities deserve their depth, and the evidence-supported purpose/proportionality of material provenance/validation choices;
- Ali can explain the important Python syntax/control flow carrying that path without needing a line-by-line script;
- Ali has independently explained at least one representative focused test at setup → action → assertion → protected behavior → non-proof depth;
- at least one material design/proof choice has been critically evaluated rather than presumed correct.

### [~] Chunk 5 — Static workflow IR + project-environment selection

**Content status:** guided content route complete; independent prediction/test-ownership gate deferred.

**Main subjects**
- why GitHub owns workflow structure while Dependency interprets project-environment selectors in the current design, and whether that split is coherent;
- provider-owned bounded workflow IR;
- effective working-directory context only when it changes command meaning;
- recognition of explicit pip/uv project environment selectors.

**Why this depth matters**
- `environment_selection.py` establishes the static project-environment selection proposition consumed by Plan 02, so it deserves ownership;
- workflow IR/context is supporting evidence representation and needs only enough depth to verify correct interpretation and ambiguity handling.

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
- challenge strictness/abstention decisions by asking what unsupported/dynamic ambiguity they prevent rather than assuming every branch is necessary;
- audit whether the provider/dependency ownership split is actually coherent at the inspected boundary.

**Focused tests / ownership checkpoint**
- `tests/test_github_workflow_definition.py`;
- `tests/test_project_environment_selection.py`;
- working-directory tests only when needed by the real command.

Ali should predict the typed S001 selector before the answer is revealed, then use one focused test to explain the exact static-selection invariant and its non-proof boundary.

**Do not miss / assume**
- static selector observation != command execution;
- workflow/job/step structure and dependency/environment semantics have different owners in the current design, but that ownership split remains auditable;
- dynamic/unsupported context should become unresolved rather than guessed if that behavior is supported by the current contract;
- provider/parser complexity should be learned only to the degree needed to understand and audit the admitted evidence boundary.

**Gate / proceed when**
- Ali can start from the real S001 workflow command, follow the provider IR into `observe_project_environment_selection(...)`, predict the typed static selection without adding runtime meaning, explain why this source deserves the selected depth, explain the material control flow/syntax, critically evaluate one material admission/ownership choice, and explain one representative focused test.

## Plan-level TODO / gate

- [x] S001 dependency itself makes sense before package-management reasoning.
- [x] Relevant `uv.lock` structure is readable at the minimum useful depth.
- [x] CI/docs-CI terminology is grounded in the exact Pydantic workflow.
- [x] Canonical change + source context can be traced through current executable source and audited at the material design boundaries.
- [ ] At least one representative Chunk-4 test can be explained as setup → action → assertion → protected behavior → non-proof.
- [x] Static workflow selection can be traced through current source.
- [x] Ali can state what Plan 01 still **does not prove**.
- [ ] Ali can explain why the selected OWN/MASTER targets deserve their depth and why adjacent internals do not.

## Depth / deliberate deferral

**Must master across the route:** exact change/source provenance, static-vs-runtime distinction, source context vs selection, central inputs/outputs, material source control flow/syntax, representative-test reasoning, and ability to question correctness/design choices proportionately.  
**Why:** these are foundational evidence/proposition boundaries consumed by Plan 02 and likely future debugging/modification surfaces.  
**Operational only here:** Soup Sieve internals, uv resolver internals, full GitHub Actions semantics, full YAML/TOML theory, incidental Python syntax not carrying the mechanism.  
**Why not deeper:** they explain the external evidence or implementation syntax but do not own the selected UpgradePilot propositions.  
**Deferred to Plan 02:** `pyproject.toml` + lock membership proof, graph reachability, CI consumption, direct exercise, runtime authority, coverage aggregation.

## Handoff

Plan 01's content route is complete and Plan 02 may proceed. Formal source/test/depth-rationale ownership checks remain visible as non-blocking `[~]` work and must not be silently promoted to full mastery until independently demonstrated. The durable Plan-01 study artifacts live under `notes/01_...` through `notes/04_...`.
