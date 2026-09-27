# Effective Package-Manager Semantics — Evidence Source, Type, and Data-Flow Design — 2026-09-27

**Status:** CLOSED R3 Evidence Source, Type, and Data-Flow Design. The semantic scope is inherited from the closed R2 supported-boundary design. This closure does **not** authorize Build/Implement; it hands off to R4 implementation/proof-sequence planning.

**Live owner:** `MEMORY.md`  
**Semantic boundary owner:** `working-memory/2026-09-24_effective-package-manager-semantics-system-design.md`  
**Compact decision index:** `working-memory/2026-09-24_effective-package-manager-semantics-decision-register.md`  
**Controlling program:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`

UP-SKILL:upgradepilot-planning-design

## 1. R3 responsibility

Translate the closed R2 semantic boundary into the smallest coherent evidence/data-flow architecture required by the first **Command-Derived Requirement-State Proof**.

Start from the proof result and work backward:

```text
exact proposed requirement is satisfied
in exact relevant Python package environment
at exact successful pip-command completion
                ↑
        what exact premises?
                ↑
source/applicability
+ effective package-manager semantics
+ exact environment/destination
+ exact successful occurrence execution
```

R3 owns **representation, producer/consumer responsibility, provenance/scope/time, and unresolved-edge flow**. It does not implement product behavior, broaden supported semantics, or select speculative Route-B acquisition.

## 2. Existing proof facts we should reuse

### 2.1 Exact dependency transition — REUSE

Owner:
- `dependency/change.py::DependencyVersionChange`

Already preserves:
- package presentation identity;
- normalized package identity;
- exact old version;
- exact proposed version;
- agreeing source evidence and limitations.

Do **not** create another proposed-version type for Route A.

### 2.2 Exact direct-requirements applicability and command occurrence — REUSE

Owners:
- `dependency/direct_install.py::DirectInstallDeclarationObservation`
- `ci/workflow_commands.py`
- `ci/consumption.py::StaticDependencyConsumptionEvidence`

For the normal direct-requirements path, `StaticDependencyConsumptionEvidence` already preserves:
- `mechanism="direct_requirements"`;
- normalized changed-package identity;
- exact workflow path/revision;
- exact job key;
- exact step source index;
- exact command source;
- exact dependency source path;
- canonical parsed `StaticCommandLocation`;
- parser structural context;
- whole-step relation;
- shell execution profile.

It already means: the trusted changed dependency source is statically consumed by this exact command occurrence. It deliberately does **not** mean execution or resulting package state.

**R3 consequence:** do not introduce a second “requirement applicability/command binding” record unless later evidence demonstrates a missing proposition that this type cannot carry.

### 2.3 Parser-backed command identity/structure — REUSE

Owners:
- `github/workflow_command_analysis.py`
- `github/workflow_command_location.py`

Reuse `StaticCommandOccurrence` / `StaticCommandLocation` and parser-neutral structural facts. Do not expose Tree-sitter nodes outside their current owner or reparse command text in downstream package-manager modules.

### 2.4 Static/runtime step identity — REUSE AND EXTEND AT OWNER

Owner:
- `ci/workflow_runtime_correlation.py`

Existing:
- `WorkflowRuntimeStepCorrelation` binds one static `run:`/`uses:` step to one factual runtime `WorkflowStep`;
- `WorkflowRuntimeCorrelationResult` preserves ambiguity as unresolved.

Known R2 gap:
- current correlation is too narrow for ordinary unnamed action/run steps and strategy/matrix cases;
- first-boundary design admits provider-accurate unnamed-step display identity, while matrix/job-expansion remains separate.

Do not create a package-manager-specific runtime correlator.

## 3. Missing layer A — public exact-execution evidence

Current runtime-success interpretation exists inside `ci/dependency_exercise.py`, but the useful result is private/internal and tied to dependency-consumption/direct-exercise aggregation.

R3 candidate responsibility:

```text
static/runtime step correlation
+ exact command occurrence eligibility
+ unmasked completed-successful runtime step
→ public bounded exact-occurrence execution evidence
```

Candidate semantic shape, **not final names/schema**:

```text
ExactCommandExecutionEvidence
- workflow/run/job/step identity
- command location
- execution state: supported | unresolved/not-established
- runtime step number/status/conclusion
- proof basis / limitation
```

Important:
- keep command execution separate from package-manager meaning;
- generic enough for setup-python effects, GITHUB_ENV writes, venv/fall-through commands, package-manager installs, and future Route-B self-verifying checks;
- do not claim every command in a successful step executed;
- bounded sequential reachability remains a separate CI/shell composition responsibility layered over this exact-execution fact.

### R3-A decision — two-level reusable execution evidence

**AGREED DESIGN DIRECTION:** refactor the existing runtime-strengthening logic into two reusable CI-owned evidence layers rather than promoting the current private dependency-exercise result unchanged or adding a parallel package-manager execution path.

#### A. Correlated user-step execution assessment

Proposition:

> Did this exact statically correlated user step complete successfully in a form whose positive interpretation is not masked?

Candidate shape, not final names:

```text
CorrelatedStepExecutionAssessment
- state: supported | not_established | unresolved
- static step identity
- runtime step number/status/conclusion
- reason/detail
```

Producer inputs:
- `WorkflowRuntimeStepCorrelation`;
- step-level `continue-on-error` semantics.

Rules:
- applies to both `RunStepDefinition` and `UsesStepDefinition`;
- completed + success is positive only when `continue-on-error` is absent or positively false under the admitted contract;
- dynamic/true masking remains unresolved;
- this fact says the **step** succeeded, not that every command inside a run script executed.

Primary consumers:
- setup-python action-effect semantics;
- future action/provider effects;
- command-level execution strengthening.

This extracts the currently duplicated/embedded continue-on-error + runtime-status interpretation from `dependency_exercise.py` into a reusable CI owner.

#### B. Exact command-occurrence execution assessment

Proposition:

> Given an unmasked successful owning run step, does the admitted shell/structure relation justify treating this exact parsed command occurrence as executed successfully?

Candidate shape, not final names:

```text
ExactCommandExecutionAssessment
- state: supported | not_established | unresolved
- workflow/job/step identity
- StaticCommandLocation
- structural / whole-step proof basis
- owning correlated-step execution evidence
- reason/detail
```

Producer inputs:
- parser-backed occurrence identity/structure;
- shell execution profile;
- existing `classify_runtime_strengthening_eligibility` logic;
- the correlated user-step execution assessment above.

Rules:
- sole ordinary top-level command remains supportable under admitted profiles;
- first ordinary sequential Bash/sh command remains supportable under the existing fail-fast contract;
- later commands require the separately designed bounded sequential-reachability/fall-through evidence;
- unsupported conditional/loop/background/control-transfer shapes remain unresolved/not-established;
- never infer “all commands in a successful step executed.”

Primary consumers:
- Route-A package-manager command execution;
- GITHUB_ENV write execution when that semantic producer is selected;
- venv creation/activation sequence composition;
- optional Route-B self-verifying command checks.

#### Why the current private result should not simply become public

`_RuntimeStrengtheningCandidateResult` in `ci/dependency_exercise.py` is currently:
- private;
- coupled to dependency-exercise aggregation and evidence labels;
- built only after proposition-specific `RuntimeStrengtheningCandidate` construction;
- limited to `RunStepDefinition`;
- carrying runtime-step facts mixed with command-eligibility decisions.

Promoting it unchanged would preserve accidental coupling and still fail to serve `uses:` action effects such as setup-python.

#### Reuse consequence

Do not discard current machinery. R3/R4 should refactor/rehome:
- workflow static/runtime correlation stays in `workflow_runtime_correlation.py`;
- generic unmasked step-success interpretation becomes reusable CI evidence;
- existing runtime-strengthening eligibility becomes the command-occurrence layer;
- `dependency_exercise.py` becomes a consumer/aggregator rather than the owner of generic execution truth.

This is one execution-evidence subsystem with two proof levels, not two competing systems.

## 4. Missing layer B — dependency-owned effective package-manager semantic facts

R2 requires semantic dimensions to remain independent and provenance-preserving. Avoid a single opaque `effective_config` blob and avoid one bespoke resolver per flag.

### R3-B decision — independent typed facts + shared bounded resolution provenance

**AGREED DESIGN DIRECTION:** represent each decision-critical effective semantic dimension as its own typed fact, while sharing one small provenance model for how that effective value was resolved.

Do **not** model all pip/uv configuration. Resolve only a requested semantic dimension and stop at the nearest decisive source under the accepted precedence contract.

#### A. Shared source/provenance vocabulary

Candidate source kinds, bounded to the R2-supported evidence families:

```text
command_line
process_environment
persistent_config
manager_default
provider_or_environment_relationship
```

The last source kind covers relational evidence such as a positively established setup-python/PATH, venv activation, or bare-executable ownership relation; it is not a substitute for package-manager CLI/config precedence.

A positive effective fact needs more than `winning_source=...`. It must preserve enough of the backward resolution to justify why that source was allowed to win.

Candidate conceptual structure, names/schema not final:

```text
SemanticResolutionProvenance
  dimension
  inspected_sources: ordered tuple of ResolutionStep
  winning_source

ResolutionStep
  source_kind
  disposition:
      non_overriding
      disabled
      decisive
  source-specific locator/reference
  detail
```

For example, a justified manager-default dry-run value may require:

```text
CLI dry-run source       → non_overriding
process env dry-run      → non_overriding
persistent config        → non_overriding
pip default              → decisive: apply changes
```

If process-environment dry-run is unresolved, do **not** emit a positive default fact with an unresolved step hidden in its provenance. Emit an explicit semantic problem instead.

Candidate negative/unresolved structure:

```text
PackageManagerSemanticProblem
  dimension
  reason
  detail
  resolved_prefix_of_provenance
  blocking_source
```

This follows the existing UpgradePilot pattern of positive typed evidence versus explicit problem/abstention states.

Demand-driven consequence:
- provenance contains only the sources actually needed before resolution stopped;
- lower-priority sources after a decisive winner need not be inspected or stored;
- earlier/higher-priority non-overriding evidence remains available for explanation;
- this is a bounded resolution trace, not a full environment/config snapshot.

#### B. Minimum first-boundary semantic fact variants

The first Route-A proof needs four independent fact families.

##### 1. Manager environment selection

Proposition:

> Which Python/package environment does this exact package-manager operation manage?

Candidate fact:

```text
ManagerEnvironmentSelectionFact
  manager
  command_location
  environment_identity / relationship
  provenance
```

The environment identity must support relational identity, not only a naked path. Positive families include explicit interpreter invocation, pip `--python`, resolved bare-pip executable ownership, setup-python/PATH, bounded venv selection, and admitted uv environment selection.

Exact environment-reference subtypes belong to R3.3 producer design; do not force every environment into one filesystem path if the established evidence is relational.

##### 2. Installation destination

Proposition:

> Where is package state written/managed for this exact operation?

Candidate fact:

```text
InstallationDestinationFact
  manager
  command_location
  destination
  provenance
```

The destination should distinguish at minimum:
- normal installation scheme of the selected manager environment;
- explicit target directory;
- recognized alternate scheme/root selectors where supported.

For the normal first Route-A family, the destination should reference/bind to the selected manager environment rather than duplicate an inferred site-packages path that has not been independently established.

Environment selection and destination remain separate facts because `--target`/`--prefix` and related selectors can decouple them.

##### 3. Package mutation / dry-run mode

Proposition:

> Is this operation permitted to apply installation-state changes, or is it an observation/planning-only dry run?

Candidate fact:

```text
PackageMutationModeFact
  manager
  command_location
  mode: apply_changes | dry_run
  provenance
```

This fact is intentionally narrower than a generic operation-mode/config object. A decisive `dry_run` result can stop Route-A state production for that occurrence.

##### 4. Direct requirement handling

Proposition:

> Under the effective operation semantics relevant to this exact command, is the changed direct requirement itself handled by the package-manager operation?

Candidate fact:

```text
DirectRequirementHandlingFact
  manager
  command_location
  handling: handled | excluded
  provenance / semantic basis
```

Examples:
- normal `pip install -r requirements.txt`: direct requirements are handled;
- `--no-deps`: does not exclude the directly listed requirement;
- effective direct-requirement exclusion such as an admitted `--only-deps` case defeats the direct-requirement state claim.

**Important execution-conditioned nuance:** some manager contracts make a semantic mode incompatible with the observed successful command shape. For example, the selected pip requirements-file family cannot successfully execute with effective `--only-deps`. Do not force every such case into ambient config reconstruction merely to produce a pre-runtime boolean. R3 should permit a dependency-owned semantic rule to be discharged by exact successful execution during proof composition when the manager contract is explicitly “this incompatible mode would have prevented this successful command shape.” This is still manager-specific semantic knowledge; CI does not learn pip rules.

Therefore the first data flow may be:

```text
static/effective manager semantics
+ exact command execution evidence
→ direct-requirement handling established
```

for such execution-conditioned cases, while ordinary decisive CLI/env/config values may produce the fact earlier.

#### C. Starting-state/update modifiers are conditional facts, not core always-present fields

Do not add universal fields such as `upgrade`, `force_reinstall`, `ignore_installed`, or every resolver option to every operation result.

If a selected destination/proof family requires a starting-state premise—for example pip `--target` replacement semantics—produce a narrowly owned additional semantic fact for that proof family.

The first normal-environment exact-pin Route-A family does not require a universal inventory/update-modifier object.

#### D. Result shape

Prefer positive facts plus explicit semantic problems over nullable fields:

```text
type EffectivePackageManagerSemanticResult =
    ManagerEnvironmentSelectionFact
  | InstallationDestinationFact
  | PackageMutationModeFact
  | DirectRequirementHandlingFact
  | PackageManagerSemanticProblem
  | <future narrowly justified fact>
```

This is conceptual; implementation may expose per-dimension result aliases/functions rather than one public heterogeneous collection.

The important invariant is:

```text
one semantic dimension
→ one typed proposition/result
→ shared resolution provenance
→ explicit unresolved blocker
```

not:

```text
one giant EffectivePipConfig with many nullable fields
```

and not:

```text
one independent precedence framework per option
```

#### E. Ownership

```text
provider/workflow/shell evidence
→ source-visible declarations, writes, propagation, executable/environment relationships

dependency/package-manager semantics
→ effective-value precedence + pip/uv interpretation
→ typed semantic facts above

CI/state-proof composition
→ combines those facts with exact execution and dependency applicability
→ does not reinterpret pip/uv options
```

### R3-B consequence for the first Route-A proof

The normal requirements-file pip proof should request exactly these facts:

```text
ManagerEnvironmentSelectionFact
InstallationDestinationFact(normal scheme of that environment)
PackageMutationModeFact(apply_changes)
DirectRequirementHandlingFact(handled)
```

If any required fact is unresolved, defeating, or belongs to an unsupported destination family, Route A remains unresolved/defeated with that exact missing edge preserved.


## 5. Missing layer C — bounded requirement-state proof composition

The final proposition does not belong in the static parser, pip parser, or runtime correlator individually.

Candidate composition boundary:

```text
DependencyVersionChange
+ supported direct-requirements StaticDependencyConsumptionEvidence
+ effective package-manager semantic facts
+ exact environment/destination relationship
+ public exact-command execution evidence
→ RequirementSatisfiedAtCommandCompletion evidence
```

Candidate result must preserve at least:
- normalized distribution/package identity;
- exact proposed version;
- exact environment/destination scope;
- exact command occurrence / workflow-job context;
- observation boundary = command completion;
- proof route = command-derived;
- supporting provenance/limitations;
- explicit unresolved result/reason when one required edge cannot close.

It must **not** claim:
- fresh-install causality;
- selected wheel/sdist;
- whole-environment consistency;
- later persistence or use;
- compatibility;
- maintainer-action permission.

**R3-C resolved:** the command-derived requirement-state proposition belongs to a focused CI/runtime dependency-state composition owner above dependency semantics and exact execution evidence. Do not inflate `dependency/pip_command.py`, `workflow_runtime_correlation.py`, or the existing CI coverage/exercise result with this stronger meaning.

## 6. First Route-A data-flow map

```text
DependencyVersionChange
  package + exact proposed version
              |
              v
RequirementsFileDependencyContext
              |
              v
StaticDependencyConsumptionEvidence
  source path + exact workflow/job/step/command occurrence
              |
              +-------------------------+
              |                         |
              v                         v
parser-neutral occurrence       runtime-correlation path
              |                         |
              v                         v
effective pip semantics      exact-command execution evidence
  - direct requirement              |
  - dry-run                         |
  - manager env                     |
  - destination                     |
              |                     |
              +----------+----------+
                         v
      RequirementSatisfiedAtCommandCompletion
```

This is a proof graph, not a proposal to implement a generic graph engine.

## 7. Current source gaps carried into R3

Provider/workflow:
- workflow/job/step `env:` not preserved in current bounded workflow IR;
- unnamed static/runtime step identity needs provider-accurate derived names;
- generic unmasked correlated-step success should be reusable across `run:` and `uses:`.

Shell/environment:
- no bounded `GITHUB_ENV` write/propagation producer;
- no bounded setup-python PATH-effect evidence type;
- no bounded venv creation/activation semantic producer;
- no bounded sequential fall-through/reachability evidence type.

Package manager:
- `pip_command.py` does not recognize supported explicit interpreter paths;
- it does not recognize pip global options such as `--python` before `install`;
- no effective pip environment/destination semantic producer;
- no `uv pip install` effective-semantics producer;
- no bounded admitted process-env/config source adapters.

Proof composition:
- current `supported_runtime_correlated` state deliberately stops before exact package-state satisfaction;
- no public Route-A requirement-state evidence/result exists.

Route B:
- preserve only a seam in R3;
- no stdout/log/artifact acquisition is selected for the first slice.

## 8. R3 sequencing

Proceed demand-driven from the first Route-A proof, not by implementing every R2-supported family at once.

### R3.1 — execution evidence ownership
Decide/refine the reusable public exact-command execution fact and how existing runtime-strengthening/correlation produces it.

### R3.2 — package-manager semantic fact model

**CLOSED:** four independent typed semantic facts share one bounded demand-driven provenance model with explicit semantic problems. The selected facts are:
- manager environment;
- destination/scheme;
- installing/direct-requirement semantics.

### R3.3 — concrete environment/provenance producers

**AGREED DESIGN DIRECTION:** produce the first Route-A semantic facts through a small chain of reusable owner-specific facts. Parse one package-manager occurrence once, keep provider/shell process facts manager-agnostic, and keep pip/uv precedence/meaning dependency-owned.

#### A. Static package-manager operation declaration — dependency owner

Current `pip_command.py` is a bounded prefix recognizer. R3 should evolve that responsibility into one reusable static package-manager operation declaration rather than making every semantic resolver inspect raw `StaticCommandAtom` sequences independently.

Candidate shape, names/schema not final:

```text
PackageManagerOperationDeclaration
  manager: pip | uv
  operation: install
  command_location
  invocation_form
  launcher/interpreter token relation
  raw/admitted option atoms needed by semantic adapters
```

For pip, invocation forms need to distinguish at minimum:
- bare `pip` / `pip3`;
- `python -m pip`;
- supported explicit interpreter path `<path>/python -m pip`;
- effective/global `--python` manager retargeting where admitted.

For uv pip, preserve uv's own launcher and target-Python selectors rather than pretending uv is Python-launched.

This declaration is **static command meaning only**:
- no runtime execution;
- no effective env/config/default inference;
- no package-state claim.

Existing `StaticCommandLocation` remains the source identity. Do not duplicate parser source spans/order.

#### B. Exact executable / interpreter selection evidence — provider/shell/CI relationship owner

Package-manager semantics should not implement PATH lookup, setup-python propagation, or venv activation itself.

Candidate manager-agnostic proposition:

> Which executable/interpreter is positively selected for this exact command occurrence, under the admitted provider/shell model?

Candidate fact family:

```text
ExecutableSelectionEvidence
  command_location
  executable role
  selected executable/environment relationship
  provenance
  state/reason/detail
```

Positive producers may include:
- explicit executable/interpreter path;
- provider-backed setup-python PATH relation;
- bounded venv activation/PATH relation;
- bounded bare-executable selection;
- uv `--system` PATH selection when its exact concrete interpreter identity is required.

Do not require every producer to resolve to an absolute filesystem path. Preserve a stable relational identity when that is what the evidence establishes.

Dependency-owned manager-environment semantics consume this evidence and turn it into `ManagerEnvironmentSelectionFact`.

#### C. Exact-process environment-value evidence — provider/workflow/shell owner

Package-manager-specific variables should not cause a pip-aware GitHub workflow parser.

Create/query a manager-agnostic bounded proposition:

> What value, if any, is positively established for environment variable `X` at this exact command process?

Candidate result:

```text
ProcessEnvironmentValueEvidence
  command_location
  variable_name
  state: established | absent | unresolved
  value when established
  provenance / override chain
  reason/detail
```

Potential source adapters, only when demanded:
- workflow/job/step `env:` declarations;
- positively executed same-job `GITHUB_ENV` writes and propagation;
- shell-local assignment/export/wrapper effects;
- provider-established environment relationships.

This evidence stops at the exact process value. It does **not** interpret `PIP_DRY_RUN`, `PIP_TARGET`, `UV_SYSTEM_PYTHON`, etc.

R2's precedence distinction remains:

```text
provider/shell:
  establish exact process env value

dependency/package manager:
  interpret that value against CLI/config/default precedence
```

If runner/ambient process environment cannot be positively ruled out for a required variable, return `unresolved`; do not synthesize absence.

#### D. Persistent package-manager config evidence — dependency-owned manager adapter

Persistent config discovery/precedence is manager-specific, so its interpretation belongs in the dependency/package-manager layer.

Candidate query/result:

```text
PackageManagerConfigSettingEvidence
  manager
  semantic setting/dimension
  state: established | absent | disabled | unresolved
  effective persistent-config value if established
  source file/section/key provenance when known
  reason/detail
```

The adapter must preserve manager-specific discovery ordering and explicit config disabling/replacement semantics from R2.

Important:
- do not build universal filesystem/user-home config inventory;
- inspect only a setting requested by a proof-critical semantic dimension;
- if ambient user/system config cannot be positively established/ruled out and no higher source decides the dimension, keep the dimension unresolved;
- decisive CLI or exact-process environment evidence should stop before config discovery.

#### E. Manager-default adapter — dependency owner

Manager defaults are not environment facts. They are admitted package-manager semantic constants used only after every higher relevant source is positively non-overriding/disabled.

A default producer should be tiny and manager/version-contract scoped:

```text
manager semantic contract
+ resolved absence/non-override of higher sources
→ default candidate
```

The shared semantic resolver records those higher-source checks in `SemanticResolutionProvenance`.

Do not emit a manager-default fact merely because no visible CLI flag was found.

#### F. First Route-A semantic resolvers

The four R3.2 facts should be produced by dependency-owned resolvers that share the provenance engine but request only their own source inputs.

##### Manager environment

```text
PackageManagerOperationDeclaration
+ ExecutableSelectionEvidence when invocation requires it
+ effective manager retargeting sources (--python / env / config)
→ ManagerEnvironmentSelectionFact | PackageManagerSemanticProblem
```

Examples:
- explicit interpreter `-m pip`: interpreter relationship is the baseline manager environment unless a higher effective pip `--python` retargets it;
- bare pip: requires positive executable/environment ownership;
- uv: uses uv-specific `--python`, `--system`, or admitted venv discovery semantics.

##### Installation destination

```text
PackageManagerOperationDeclaration
+ ManagerEnvironmentSelectionFact
+ target/user/root/prefix CLI/env/config evidence
→ InstallationDestinationFact | PackageManagerSemanticProblem
```

For the first normal family:
- require no unresolved effective retargeter;
- return “normal scheme of selected manager environment,” not a guessed site-packages path.

##### Package mutation mode

```text
PackageManagerOperationDeclaration
+ dry-run CLI/process-env/config/default evidence
→ PackageMutationModeFact(apply_changes | dry_run)
  | PackageManagerSemanticProblem
```

A decisive CLI dry-run stops immediately.
A manager-default `apply_changes` is valid only after all higher dry-run sources are positively non-overriding/disabled.

##### Direct requirement handling

```text
PackageManagerOperationDeclaration
+ exact direct-requirements applicability
+ material exclusion-mode semantic evidence
+ exact command execution only when needed to discharge
  a manager-defined incompatible-success condition
→ DirectRequirementHandlingFact
  | PackageManagerSemanticProblem
```

Do not make CI interpret `--only-deps` or pip option compatibility.

#### G. First normal Route-A producer graph

```text
StaticCommandOccurrence
        |
        v
PackageManagerOperationDeclaration
        |
        +--------------------+
        |                    |
        v                    v
ExecutableSelection     ProcessEnvironmentValueEvidence
        |                    |
        |              PackageManagerConfigSettingEvidence
        |                    |
        |              ManagerDefault contract
        |                    |
        +---------+----------+
                  |
                  v
       dependency-owned semantic resolvers
          |       |       |       |
          v       v       v       v
       manager   destination mutation  direct
       env fact     fact     mode    handling
          \         |        |        /
           \        |        |       /
            +--------+--------+------+
                     |
          exact command execution
                     |
                     v
          Route-A state-proof composer
```

This is a data-flow design, not a generic runtime graph engine.

#### H. First-slice pressure and honest limitation

For a plain-looking command such as:

```text
python -m pip install -r requirements.txt
```

R3 must not assume:
- literal `python` identifies a package environment without executable-selection evidence;
- dry-run is false merely because `--dry-run` is absent;
- destination is the normal environment merely because `--target` is absent.

If exact-process environment/config provenance needed for one of those dimensions is unavailable, that semantic fact remains unresolved.

This may make some ordinary-looking workflows unresolved until additional bounded evidence producers are implemented or a direct state witness exists. That is consistent with R2. Real-case verification in R4+/Build will determine which admitted producers are worth implementing first; R3 should not weaken the proof to improve apparent coverage.

#### I. Ownership / module direction

Do not force all new responsibilities into `pip_command.py` or `environment_selection.py`.

Current architectural direction:
- existing parser/workflow owners keep syntax and static provider facts;
- dependency/package-manager code gets a coherent runtime-operation semantics owner, potentially a new focused module/family rather than overloading project-environment selection;
- CI gets reusable step/command execution evidence from R3.1;
- Route-A state composition sits above both.

Exact filenames/classes remain R4 implementation-planning responsibility unless a durable architecture owner/ADR is required.


### R3.4 — Route-A state-proof composer

**AGREED DESIGN DIRECTION:** keep runtime dependency-state proof separate from existing CI coverage/exercise evidence.

The existing `DependencyCICoverageResult` contract stops at static dependency consumption/direct exercise plus bounded runtime execution. It must not be redefined to mean package-state satisfaction.

Use a separate per-command positive witness, conceptually:

```text
RequirementSatisfiedAtCommandCompletion
  normalized_package
  proposed_version
  dependency source/context identity
  workflow/revision/job/step/StaticCommandLocation
  ManagerEnvironmentSelectionFact
  InstallationDestinationFact
  PackageMutationModeFact
  DirectRequirementHandlingFact
  ExactCommandExecutionAssessment
  observation_boundary = command_completion
  proof_route = command_derived
  limitations
```

The witness retains the typed supporting facts so their provenance remains inspectable. It proves only that the exact proposed direct requirement is satisfied in the resolved package-state scope at completion of that exact successful package-manager command.

Use an explicit problem result for failed candidates, conceptually:

```text
CommandDerivedRequirementStateProblem
  state: not_established | unresolved
  reason
  detail
  exact command identity when known
  blocking semantic dimension / producer when known
```

Examples:
- positive dry-run -> not established for command-derived state production;
- known unsupported destination family -> not established for the first normal-scheme proof;
- unresolved process-env/config input -> unresolved;
- runtime command not successful -> not established;
- exact execution relation unresolved -> unresolved.

A failed proof is never package-absence evidence.

First-family composition inputs:

```text
DependencyVersionChange
+ matching RequirementsFileDependencyContext
+ supported direct-requirements StaticDependencyConsumptionEvidence
+ ManagerEnvironmentSelectionFact
+ InstallationDestinationFact
+ PackageMutationModeFact
+ DirectRequirementHandlingFact
+ ExactCommandExecutionAssessment
→ RequirementSatisfiedAtCommandCompletion
```

No new requirement-applicability type is needed.

Positive composition requires identity alignment across all inputs: same normalized package, trusted exact source/revision, same workflow/job/step/command occurrence, same package-manager operation, normal destination bound to the selected manager environment for the first family, mutation mode `apply_changes`, direct requirement handling `handled`, and supported exact execution.

Impossible mismatches between typed inputs are programming-contract errors. Real evidence ambiguity must already be represented by the upstream producer.

The exact proposed version remains owned by `DependencyVersionChange` plus its trusted source context; matching a package name alone is insufficient.

Preserve multiple command witnesses independently. A workflow/PR aggregate may later expose witnesses plus problems, but it must not merge different environments into one fictional global state.

Strong owner direction:
- dependency semantics stay in `dependency/`;
- exact execution stays in CI runtime evidence;
- a focused CI/runtime dependency-state composition layer above both owns this witness;
- a module such as `ci/dependency_state.py` is a plausible implementation direction;
- `investigation.py` should eventually carry this result alongside, not instead of, `ci_coverage_result`.

The witness does not prove fresh installation, artifact identity, whole-environment consistency, later persistence/use, behavioral compatibility, or maintainer-action permission.

Demand-driven composition should preserve the earliest material blocker rather than collapse all failures to generic insufficient evidence.


### R3.5 — optional Route-B seam

**AGREED DESIGN DIRECTION:** preserve Route B as a sibling evidence path with compatible scope/time/provenance fields, but do not create a common base-class hierarchy or output-acquisition subsystem merely for symmetry.

First low-acquisition Route-B family:

```text
resolved Python interpreter/environment
+ target-owned self-verifying importlib.metadata.version(...) predicate
+ expected version positively tied to DependencyVersionChange.proposed_version
+ explicit nonzero mismatch behavior
+ exact successful command execution
→ DirectDistributionVersionObservation
```

Candidate sibling result, names/schema not final:

```text
DirectDistributionVersionObservation
  normalized_package
  observed_version
  interpreter/environment observation scope
  workflow/revision/job/step/command identity
  observation_boundary = direct_observation
  observation_method = importlib_metadata
  ExactCommandExecutionAssessment
  limitations
```

Compatibility invariant between Route A and Route B:

Both witnesses must make these dimensions recoverable:
- exact normalized distribution/package identity;
- exact version;
- package-state/environment or inspection scope;
- exact workflow/runtime occurrence provenance;
- observation boundary/time semantics;
- proof route/method;
- explicit claim limitations.

Do not force both witnesses to use one identical “destination” type:
- Route A proves satisfaction in a manager environment/destination at command completion;
- Route B observes distribution metadata through a specific interpreter's metadata-discovery scope.

Their scopes can later be related when a downstream proposition requires it, but they are not automatically identical.

No new stdout/log/artifact acquisition is selected in R3. The self-verifying command family can reuse R3.1 exact-command execution evidence because successful exit already encodes the predicate. Structured `pip inspect`, `pip list --format=json`, uv inventories, logs, or uploaded artifacts remain future adapters only if real evidence/action value justifies them.

A common protocol/union over Route-A and Route-B witnesses may be introduced in R4 only if a real consumer benefits from handling both uniformly. Do not add one solely for type elegance.

Later-use composition remains downstream:
```text
state witness
+ ordering
+ same relevant package-state scope
+ material continuity/non-mutation
+ supported changed-package consumption
→ later-use proposition
```

R3 does not design a universal continuity engine here.

### R3.6 — closure

**R3 PASS — producer/type/consumer paths are now explicit enough for R4.**

First Route-A proof ownership:

```text
DependencyVersionChange
  owner: dependency/change.py
        |
RequirementsFileDependencyContext
+ StaticDependencyConsumptionEvidence
  owners: dependency/environment.py
          dependency/direct_install.py
          ci/workflow_commands.py
          ci/consumption.py
        |
StaticCommandOccurrence / StaticCommandLocation
  owner: github/workflow_command_analysis.py
         github/workflow_command_location.py
        |
        +---------------- execution branch ----------------+
        |                                                  |
        |  WorkflowRuntimeStepCorrelation                  |
        |    owner: ci/workflow_runtime_correlation.py      |
        |          ↓                                       |
        |  CorrelatedStepExecutionAssessment               |
        |          ↓                                       |
        |  ExactCommandExecutionAssessment                 |
        |    owner: reusable CI runtime-execution layer     |
        |                                                  |
        +---------------- semantics branch ----------------+
        |                                                  |
        |  PackageManagerOperationDeclaration              |
        |          ↓                                       |
        |  ExecutableSelectionEvidence                     |
        |  ProcessEnvironmentValueEvidence                 |
        |  PackageManagerConfigSettingEvidence             |
        |  manager-default semantic contract               |
        |          ↓                                       |
        |  ManagerEnvironmentSelectionFact                 |
        |  InstallationDestinationFact                     |
        |  PackageMutationModeFact                         |
        |  DirectRequirementHandlingFact                   |
        |    owner: dependency/package-manager semantics    |
        |                                                  |
        +----------------------+---------------------------+
                               |
                               v
             RequirementSatisfiedAtCommandCompletion
             owner: focused CI/runtime dependency-state
                    composition layer
```

R3 preserves explicit unresolved edges rather than weakening them:
- unresolved exact executable/environment ownership;
- unresolved exact-process environment value;
- unresolved persistent config needed by a material dimension;
- unresolved/default destination because a higher source is not ruled out;
- unsupported shell/control-flow reachability;
- unsuccessful/masked/unresolved runtime execution;
- unsupported retargeted destination family.

No R2 semantic family was silently widened. Recognized/deferred cases remain recognized/deferred, and Route B remains an optional sibling seam rather than a mandatory first-slice producer.

The following are implementation-shape details for R4, not open R3 architecture:
- final class/function names;
- exact new module filenames;
- whether a small public aggregate wraps per-command state witnesses;
- exact migration sequence out of private runtime-strengthening helpers;
- which bounded env/config producers are implemented in the first Build slice based on representative real-case pressure.

**R3 handoff to R4:** turn this evidence architecture into an ordered implementation/proof plan, reconcile the controlling runtime dependency-state plan only where this concrete architecture changes execution sequencing, define focused/integration/real-case verification, and stop for explicit Build authorization before source mutation.

## 9. R3 stop line

Do not:
- implement source/tests;
- reopen R2 semantic scope without contradictory evidence;
- design universal environment/config reconstruction;
- add a generic graph engine;
- select Conditional Cycle 2;
- redesign maintainer actions;
- create Route-B log acquisition merely because it is possible.

R3 is complete when the first Route-A proof can be traced as:

```text
existing/new producer
→ exact typed fact
→ provenance/scope/time
→ exact consumer/composer
→ bounded state result or explicit unresolved edge
```

and the design is concrete enough for R4 implementation/proof-sequence planning.
