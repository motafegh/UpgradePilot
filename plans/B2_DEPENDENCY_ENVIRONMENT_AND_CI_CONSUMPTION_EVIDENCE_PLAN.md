# B2 Dependency Environment and CI Consumption Evidence Plan

**Status:** Approved bounded post-Tranche-1 implementation plan  
**Date:** 2026-08-16  
**Owner:** Ali Rajabi  
**Parent responsibility:** [`B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md)  
**Accepted source ownership:** [`../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](../docs/architecture/ADR-0007-responsibility-based-python-subpackages.md)  
**Accepted GitHub Actions architecture:** [`../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md`](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md)  
**Canonical decision semantics:** [`../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)  
**Generality standard:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Security boundary:** [`../SECURITY.md`](../SECURITY.md)  
**Resolver-evidence audit:** [`../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`](../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md)  
**Primary real-case pressure:** S001 Pydantic/Soup Sieve and S011 Dictare/MLX optional extra  
**Transfer pressure:** S005 ModelArrayIO lock-backed tox/uv path

## 1. Purpose

Broaden UpgradePilot's dependency/CI evidence responsibility from the current direct-requirements-file rule into the smallest useful **source-aware dependency-environment consumption model** justified by real cases.

The current accepted path can reason about:

```text
changed exact requirements file
+ visible direct pip -r installation declaration
+ visible direct changed-package invocation
+ separate exact-head successful CI evidence
→ bounded CI dependency-exercise support
```

That rule remains useful but is too narrow for already-admitted real Python dependency-update shapes.

S001 exposes a positive consumption gap:

```text
changed source: uv.lock
workflow: uv sync / uv run with selected project groups
changed package may be transitive in the selected locked environment
```

S011 exposes the complementary non-formation/selection gap:

```text
changed source: pyproject.toml optional extra `mlx`
workflow: pip install -e ".[dev]"
→ workflow context exists
→ affected `mlx` environment is not thereby established
```

The responsibility horizon is therefore:

```text
trusted dependency change
+
exact dependency-source/environment membership evidence
+
static workflow environment-selection/consumption declaration
+
separate exact-head runtime CI evidence
↓
bounded CI consumption/coverage evidence
↓
optional stronger exercise evidence only where independently justified
```

This plan does **not** reopen or amend accepted Phase-E / Tranche 1. Tranche 1 remains a completed historical implementation milestone. This is a separate evidence-earned generality increment selected after the Tranche-1 STOP/REVIEW learning pressure.

## 2. Owning product question

For admitted public Python dependency-update PRs:

> **Can UpgradePilot establish whether an exact CI workflow/job statically selects an environment that contains the changed dependency, while preserving the distinction between declaration, dependency membership, resolver satisfiability, runtime execution, exact-version observation, and behavioral exercise?**

The responsibility must support the first real source/environment families justified by current evidence without becoming a universal package-manager or CI interpreter.

## 3. Required proof ladder

Keep these propositions separate throughout source, types, tests, CLI detail, and learning documentation:

```text
A. dependency transition established
!=
B. dependency belongs to/selects an environment
!=
C. workflow statically declares selecting/consuming that environment
!=
D. dependency constraints are resolver-satisfiable
!=
E. environment selection/install command executed
!=
F. environment installation succeeded
!=
G. exact proposed dependency version was observed in that runtime
!=
H. changed dependency/package behavior was exercised
!=
I. relevant behavior succeeded
!=
J. dependency update is compatible/safe/actionable overall
```

A stronger later rung must never be manufactured from an earlier one.

In particular:

```text
CI green
!= changed dependency consumed

changed dependency consumed
!= changed package exercised

successful uv resolution
!= behavioral compatibility
```

## 4. Architecture and ownership constraints

### 4.1 Preserve ADR-0008 provider ownership

GitHub Actions source structure remains:

```text
RepositoryTextFile
→ upgradepilot.github bounded static workflow IR
```

Do not add package-manager or dependency semantics to `github/workflow_definition.py` merely because commands contain `pip` or `uv`.

Runtime Actions evidence remains separately owned by:

```text
upgradepilot.github.actions
→ WorkflowRun / WorkflowJob / WorkflowStep
```

This plan does not merge static and runtime models.

### 4.2 Dependency owns dependency-source/environment meaning

The dependency domain should own the relation among:

```text
dependency source
project root / source path
optional extra / dependency group / lock context
changed normalized package
selected dependency environment
```

Likely implementation may extend existing `upgradepilot.dependency` modules or add narrowly named modules there when real code enters them. Do not create a speculative generic `environment/`, `common/`, or package-manager framework.

The existing `dependency/direct_install.py` remains the narrow direct-requirements declaration primitive accepted by ADR-0008. **Do not stretch it into universal dependency consumption.** Introduce a distinct dependency-owned responsibility if broader environment-selection/consumption semantics are required.

### 4.3 CI owns CI-specific composition

`upgradepilot.ci` should own questions such as:

```text
successful exact-head CI evidence exists?
+
static workflow selects an environment containing the changed dependency?
+
static direct changed-package invocation exists?
→ what CI coverage/exercise evidence is justified?
```

CI must consume dependency-owned source/environment facts rather than reparse `pyproject.toml`, `uv.lock`, or requirements semantics itself.

### 4.4 Application owns sequencing only

`investigation.py` may orchestrate the new typed evidence once the bounded domain contracts are implemented. It must not become the parser or semantic owner for extras, groups, lock reachability, uv command meaning, or CI proof.

## 5. Initial admitted domain

The implementation horizon is deliberately broader than one fixture but smaller than the Python packaging ecosystem.

### Included first families

1. **Existing exact requirements files**
   - preserve current direct `pip` / `python -m pip -r <path>` behavior;
   - migrate only as required to fit the new typed consumption evidence without weakening existing proof.

2. **`uv.lock` + uv project selection**
   - exact project/lock identity;
   - bounded static recognition of relevant `uv sync` / `uv run` project selection forms actually required by S001-style evidence;
   - selected dependency groups/extras where statically readable;
   - bounded proof that the changed package belongs to the selected locked environment, including transitive membership when the exact admitted lock/project structure can establish it;
   - dynamic/ambiguous selection remains unresolved.

3. **`pyproject.toml` optional dependencies and dependency groups**
   - exact base/head TOML evidence;
   - generic group names and normalized package identities inside the admitted syntax;
   - S011-style exact pinned dependency transition inside `[project.optional-dependencies]` as the first concrete extraction pressure;
   - bounded recognition of environment selectors such as `.[extra]`, `--extra`, `--all-extras`, and admitted dependency-group selection forms where real cases justify them.

### Required transfer pressure, not automatic first support

S005 demonstrates that lock consumption may be mediated through:

```text
tox
+
uv-venv-lock-runner
```

The initial implementation does not need to execute or generally interpret tox. Before closing this plan, however, S005 must be used as a transfer check so the architecture does not incorrectly encode:

```text
uv.lock consumption
=
only a direct `uv sync` command
```

If S005 requires a materially different interpreter, record the boundary and defer it rather than broadening into generic tox/task-runner execution.

## 6. Explicit non-goals

This plan does **not** authorize:

- universal package-manager support;
- Poetry, PDM, Pipenv, Conda, Hatch, Rye, or arbitrary package-manager semantics without a new real pressure case;
- generic tox/nox/Make/script/task-runner tracing;
- shell interpretation beyond existing bounded command segmentation/recognition where safe;
- full PEP 508/735 ecosystem reconstruction beyond the admitted propositions;
- arbitrary project workspace resolution across every package manager;
- universal dependency graph framework;
- universal SAT/resolver implementation inside UpgradePilot;
- executing upstream/target project code merely to inspect a case;
- installing investigated dependencies as part of ordinary analysis;
- static↔runtime GitHub Actions step correlation;
- log interpretation;
- exact runtime version witness unless separately established;
- arbitrary indirect behavioral exercise inference;
- final compatibility/safety/recommendation synthesis.

Static↔runtime correlation remains the separately optional Phase-E Tranche-2 responsibility. This plan may produce better static consumption evidence without selecting Tranche 2.

## 7. Result semantics

Exact type names may be refined during implementation, but the design must make at least these distinctions representable.

### 7.1 Dependency-source/environment membership

Conceptually:

```text
changed dependency
+
exact source/project/lock context
+
selected group/extra/root environment
→ member / not established / unresolved
```

Do not use repository-wide union reasoning. Membership is scoped to an exact environment-selection proposition.

### 7.2 Static consumption declaration

Conceptually:

```text
static run step
+
effective working directory
+
package-manager/project selector
+
dependency environment membership
→ consumption declaration observed / not observed / unresolved
```

This is still static evidence:

```text
observed consumption declaration
!= executed
!= succeeded
```

### 7.3 CI coverage tiers

The CI result must not force distinct evidence strengths into one `exercise` Boolean/state.

It should be possible to preserve at least:

```text
successful exact-head CI exists

static changed-dependency consumption path supported

static changed-package direct exercise path supported

runtime correlation absent/present separately
```

One acceptable implementation direction is a typed ladder or separate fields/results; another is carefully named states. Choose the smallest shape that remains transparent under S001/S011 pressure.

Do not call static consumption `environment formation` or runtime package exercise.

## 8. Work sequence

### Cluster 0 — synchronize, freeze, and validate the current baseline

Before source changes:

1. synchronize `main`;
2. verify clean worktree;
3. record exact baseline revision;
4. run focused dependency/CI/GitHub workflow tests plus current end-to-end nearest tests;
5. run the complete deterministic product suite;
6. classify any baseline failure before changing source.

The accepted Tranche-1 source/test revision remains historical proof; a later documentation/audit/plan commit does not automatically become a new implementation-validation point.

### Cluster 1 — define the bounded dependency-environment evidence contract

Inspect active dependency and CI contracts and introduce the smallest typed representation needed to replace the format-specific handoff:

```text
direct_requirements_install_path: str | None
```

with a source/environment-aware input that can represent at least:

```text
exact requirements source
uv project/lock context
pyproject optional-extra context
pyproject dependency-group context
```

Requirements:

- preserve exact repository/revision/path/source provenance;
- preserve normalized changed-package identity;
- preserve environment/group/extra identity only when source evidence establishes it;
- do not encode runtime execution into source/environment state;
- do not introduce a universal environment graph merely for symmetry;
- preserve current requirements-file behavior through migration tests.

If this contract requires a consequential durable dependency direction not already implied by ADR-0007/ADR-0008, stop and create/amend an ADR before broad integration. A new ADR is not required merely because a new dependency-owned dataclass/module exists.

### Cluster 2 — admit exact `pyproject.toml` optional-extra transition evidence

Implement the first bounded structured-project dependency-change rule needed by S011.

Expected behavior:

```text
modified exact pyproject.toml
+ exact base/head repository files
+ valid TOML
+ [project.optional-dependencies]
→ conservatively compare admitted requirement entries
→ establish at most one exact dependency-version transition
→ preserve optional-extra identity in source/environment evidence
```

Initial accepted syntax should be broad enough for generic group/package names but bounded enough to make version-transition meaning unambiguous. Exact pins such as:

```text
numpy==1.26.4 → numpy==2.4.6
```

are the first required transition class.

Requirements:

- use `tomllib` for TOML syntax;
- use existing package normalization and `packaging` requirement parsing where appropriate;
- preserve markers/extras text when material rather than silently discarding it;
- reject/leave unresolved added/removed packages, multiple simultaneous transitions, ambiguous duplicate package entries, unsupported specifier-shape changes, or conflicting admitted evidence rather than guessing;
- integrate through `analyze_dependency_change()` so S011 no longer stops merely because its source is `pyproject.toml`;
- do not hardcode `mlx`, `numpy`, or Dictare.

### Cluster 3 — implement bounded project-environment selection semantics

Create the dependency-owned static interpretation needed to answer:

> What project environment does this run declaration visibly select?

Pressure forms include:

```text
pip install -e ".[dev]"
pip install ".[mlx]"
uv sync --group docs
uv sync --extra mlx
uv sync --all-extras
uv run ...
```

The implementation must account for effective working-directory context using the already accepted workflow/job/step precedence. It may consume `RunStepDefinition` plus independently established project/source context, but it must not move GitHub syntax ownership out of `upgradepilot.github`.

Requirements:

- literal supported selectors → typed observed selection;
- dynamic/expression-backed project path/group/extra → unresolved;
- multiple selectors preserved when semantics are explicit;
- selector omission must follow the package manager's admitted default semantics only where source/config evidence establishes those semantics;
- no claim that a selected environment was actually formed at runtime;
- S011 guard: `.[dev]` must not imply `.[mlx]`.

### Cluster 4 — implement bounded `uv.lock` membership/reachability for selected environments

S001 requires more than recognizing `uv sync --group docs`: Soup Sieve may be transitive rather than directly named in the selected project group.

Implement only the lock/project relationship needed to establish, under exact admitted uv source evidence:

```text
selected project/group/extra roots
→ exact locked dependency relationships
→ changed normalized package reachable/member?
```

Requirements:

- use exact-head `uv.lock` and exact-head project metadata from the same repository/revision/project root;
- preserve universal-lock semantics rather than flattening marker/platform/Python forks into one concrete environment;
- if marker/fork interpretation is material but exact context is not established, return unresolved rather than unioning all paths;
- preserve direct versus transitive membership when useful for explanation;
- detect cycles/bounds safely and use proportionate traversal limits if graph traversal is required;
- do not create a general dependency graph framework unless the bounded uv proof actually requires a reusable primitive;
- do not infer that every package present anywhere in `uv.lock` belongs to every selected environment;
- prove S001 through real generic lock/project structure, not package-name hardcoding.

If current uv lock schema/source evidence cannot establish the needed group-to-transitive-package relation proportionately, stop and record the precise unresolved boundary rather than inventing membership.

### Cluster 5 — migrate CI from direct-requirements-only input to typed consumption evidence

Migrate `ci/workflow_commands.py` / `ci/dependency_exercise.py` only after Clusters 1–4 provide stable inputs.

Required behavior:

```text
successful exact-head runtime CI evidence
+
exact static workflow IR
+
dependency-owned environment selection/membership/consumption evidence
→ transparent CI coverage result
```

Preserve:

- existing direct requirements path behavior;
- static install/selection ordering where relevant;
- CI-specific direct package invocation recognition;
- `supported_not_correlated`-style guard where static path and successful runtime evidence are not step-correlated;
- per-workflow evidence and heterogeneous weaker results;
- `no_successful_ci` separately from semantic unresolved states.

New CI semantics must be able to say, where evidence supports it:

```text
changed dependency is statically included/consumed by this CI environment
```

without also claiming:

```text
changed package was directly exercised
```

For S001, success of this cluster is **not** defined as forcing a direct Soup Sieve exercise claim. A valid result may establish static locked-environment consumption while leaving direct package exercise unresolved/not observed.

For S011, inspected `.[dev]` workflows must not become evidence that the changed `mlx` environment was consumed.

### Cluster 6 — application/CLI integration and real-case pressure

Integrate the new typed dependency-environment/CI evidence through the ordinary application path.

Required pressure:

#### S001 — positive locked-environment consumption

Establish only what exact evidence supports, ideally:

```text
soupsieve 2.6 → 2.8.4
+
exact-head uv project/lock context
+
static relevant uv environment selection
→ changed dependency consumption declaration/member evidence
```

while preserving:

```text
consumption != direct exercise
static declaration != runtime execution
```

#### S011 — optional-extra non-coverage guard

The normal dependency-analysis path must be able to establish the exact optional-extra dependency change. CI interpretation must preserve that ordinary `.[dev]` installation does not establish consumption of `.[mlx]`.

Do not upgrade non-observation into repository-wide absence unless evidence coverage justifies that negative claim.

#### S005 — architecture transfer check

Pressure the implemented result against the frozen lock-backed tox/uv case.

The required outcome is one of:

```text
existing abstractions naturally represent the evidence without interpreting tox
```

or:

```text
S005 requires a materially different tox/runner interpreter
→ record explicit deferred boundary
```

Do not add generic tox support merely to make S005 green.

### Cluster 7 — AUDIT-004 resolver-satisfiability reassessment gate

After static dependency-environment consumption evidence works, reassess whether an exact-head resolver observation would materially improve a still-unresolved proposition.

Keep the audit ladder:

```text
L1 lock exists/parses
L2 lock current against project metadata
L3 `uv lock --check` succeeds
L4 target-relevant `uv sync --locked` succeeds
L5 relevant runtime behavior succeeds
```

This cluster is a **gate**, not automatic permission to execute untrusted dependency resolution/install commands.

Before any product/runtime `uv lock --check` execution is added:

1. define exact repository/revision/project-root/config/index authority;
2. establish whether uv resolution can execute build backends or other untrusted package code in the admitted mode;
3. define network/cache/credential/isolation behavior;
4. verify compliance with `SECURITY.md`;
5. prove the observation materially discriminates a product proposition not already resolved statically.

Valid outcomes:

```text
A. implement a bounded safe resolver-satisfiability observation
B. retain audit finding for later because security/cost/value is not yet justified
C. prune resolver execution because static evidence already resolves the proposition
```

Do not let this gate block Clusters 1–6 if resolver execution is unnecessary for the bounded consumption responsibility.

### Cluster 8 — regression, acceptance, and stop/review

Required focused coverage should include at least:

- unchanged direct requirements behavior;
- exact pyproject optional-extra exact-pin transition extraction;
- arbitrary supported extra/group names, not fixture-specific names;
- ambiguous/multiple pyproject transitions abstain;
- malformed/unavailable/inconsistent exact project evidence;
- `.[dev]` vs `.[mlx]` distinction;
- `--extra`, `--all-extras`, and selected group semantics within admitted forms;
- working-directory/project-root resolution;
- dynamic selectors remain unresolved;
- uv lock selected-environment direct membership;
- uv lock selected-environment transitive membership;
- marker/fork context that cannot be safely projected remains unresolved;
- package present somewhere in lock does not imply membership in every selected environment;
- static consumption distinct from direct package exercise;
- successful runtime CI distinct from static consumption execution/success;
- S001 positive consumption pressure;
- S011 affected-extra non-formation/consumption guard;
- S005 transfer/deferred-boundary check;
- nearest investigation/CLI/end-to-end regressions;
- complete deterministic product suite;
- installed/import smoke if package surface changes.

Record exact validation evidence in one working-memory record for this implementation responsibility.

## 9. Expected source/test modification boundary

Expected owners, subject to exact implementation evidence:

```text
src/upgradepilot/dependency/
    analysis.py
    change.py
    uv_lock.py
    direct_install.py        # preserve narrow role; change only if migration requires
    new bounded pyproject/environment/consumption modules only when justified

src/upgradepilot/ci/
    workflow_commands.py
    dependency_exercise.py

src/upgradepilot/github/
    workflow_definition.py   # only if a demonstrated missing provider field is required

src/upgradepilot/investigation.py
src/upgradepilot/cli.py

tests/
    responsibility-owned focused regressions
```

Do not modify Target semantics merely for symmetry. Target may consume future environment evidence only if its own proposition requires it in a separately justified step.

## 10. Architecture decision gate

This plan is intended to fit ADR-0007 and ADR-0008 rather than supersede them.

A new/amended ADR becomes necessary only if implementation demonstrates a consequential durable decision such as:

- a new cross-domain dependency direction;
- a generic environment model shared by materially different domains;
- a universal lock/dependency graph representation;
- moving package-manager semantics into the GitHub provider;
- merging static and runtime workflow evidence;
- changing ADR-0008's separation of direct-install declaration from broader dependency consumption.

If no such change is required, keep architecture authority in existing ADRs and let source/tests own the bounded new behavior.

## 11. Pass conditions

The selected implementation passes only when:

```text
requirements-file behavior remains valid
+
S011-style optional-extra dependency change is admitted generically
+
static project environment selection is represented honestly
+
S001-style uv selected-environment membership/consumption is established or explicitly bounded by a demonstrated source limitation
+
CI distinguishes consumption coverage from package exercise
+
static and runtime evidence remain separate
+
S005 transfer does not expose fixture-shaped architecture
+
focused + nearest + complete deterministic validation is green
```

A successful implementation does **not** require resolver execution from Cluster 7 if the gate concludes it is unnecessary or not yet admissible.

## 12. Stop line

STOP / REVIEW after Cluster 8.

Do not automatically continue into:

- Phase-E Tranche 2 static↔runtime correlation;
- resolver execution beyond the Cluster-7 gate;
- tox/nox/task-runner support;
- additional package managers;
- Target environment broadening;
- final B2 synthesis/recommendation.

At the stop/review, compare the new evidence against the parent B2 responsibility and decide the next highest-value continuation explicitly.

## 13. Learning/ownership checkpoint

By the end of this responsibility, Ali should be able to explain and trace:

1. why dependency transition identity is separate from dependency-environment membership;
2. why a package appearing in `uv.lock` does not mean every environment consumes it;
3. how optional extras/dependency groups change environment selection;
4. how exact working-directory/project-root context affects package-manager meaning;
5. why transitive lock membership can establish consumption without direct package invocation;
6. why static consumption declaration is weaker than runtime execution;
7. why consumed dependency is weaker than behaviorally exercised dependency;
8. why `.[dev]` does not imply `.[mlx]`;
9. why successful resolver evidence addresses declared constraint satisfiability rather than API/runtime compatibility;
10. when a new source/runner mechanism justifies generalization versus explicit deferral.

Do not record mastery merely because AI-generated implementation and tests pass.

## 14. Relationship to Phase-E Tranche 2

This plan and optional Tranche 2 solve different problems:

```text
THIS PLAN
Can we recognize the relevant dependency environment and establish a static consumption path?

TRANCHE 2
Can we safely correlate an already-identified static job/step with runtime job/step evidence?
```

Therefore:

```text
better static consumption semantics
→ may later feed Tranche 2

but

Tranche 2
→ cannot substitute for missing dependency-environment semantics
```

Keep the responsibilities separately selectable and separately validated.