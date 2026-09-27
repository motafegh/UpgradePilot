# Effective Package-Manager Semantics — Evidence Source, Type, and Data-Flow Design — 2026-09-27

**Status:** ACTIVE R3 Planning/Design + Learning-by-Doing record; semantic scope is inherited from the closed R2 supported-boundary design. This record does **not** authorize Build/Implement and does not reopen R2 unless concrete source/evidence exposes a contradiction.

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

**Open design decision R3-A:** should this be a small public fact extracted from the existing runtime-strengthening machinery, or should the existing runtime-strengthening result itself be promoted/refactored into the reusable public type? Prefer reuse/refactor over a parallel execution subsystem.

## 4. Missing layer B — dependency-owned effective package-manager semantic facts

R2 requires semantic dimensions to remain independent and provenance-preserving. Avoid a single opaque `effective_config` blob and avoid one bespoke resolver per flag.

The dependency/package-manager owner should consume:
- parser-neutral command occurrence;
- exact command/source applicability where relevant;
- provider/process-environment/config facts admitted by R2;
- manager-specific precedence/semantics;

and produce only facts needed by the selected proof.

Candidate semantic fact families, **not final schema**:

### 4.1 Manager environment selection

Proposition:

> Which Python/package environment does this exact package-manager operation manage?

Examples of positive provenance:
- explicit interpreter `<path>/python -m pip`;
- positively resolved `python -m pip` interpreter;
- pip effective `--python`;
- resolved bare pip executable ownership;
- uv `--python`, `--system`, or supported default venv discovery.

Preserve the relation/provenance; do not reduce this to an unqualified string path when the evidence is relational.

### 4.2 Installation destination/scheme

Proposition:

> Where does this exact operation place/manage package state for the claim?

Examples:
- normal scheme of the selected Python environment;
- explicit `--target`;
- recognized user/prefix/root modifiers.

Environment selection and destination are distinct facts.

### 4.3 Installing/direct-requirement handling

Proof-critical propositions include:
- effective dry-run/non-installing state;
- whether the proposed direct requirement itself is handled;
- only update/start-state semantics required by the selected destination family.

A decisive dry-run fact may stop Route-A proof before destination work for that command-derived installation claim.

### 4.4 Shared provenance

Every established effective semantic fact should preserve:
- semantic dimension;
- effective value/relationship;
- winning source class (CLI / process env / persistent config / manager default / provider relationship);
- source-specific provenance sufficient to explain the value;
- unresolved/defeating reason when the dimension cannot support the claim.

**Open design decision R3-B:** choose the smallest typed representation that preserves independent dimensions and shared provenance without creating either:
1. one giant nullable package-manager result object, or
2. one unrelated resolver/type hierarchy per option.

A typed union of small semantic facts with shared provenance is the current strongest candidate.

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

**Open design decision R3-C:** select the correct module/owner for this composition. Current evidence suggests a CI/dependency-state composition owner above dependency semantics and runtime execution, rather than inflating `dependency/pip_command.py` or `ci/dependency_exercise.py`.

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
Design shared provenance and the independent facts for:
- manager environment;
- destination/scheme;
- installing/direct-requirement semantics.

### R3.3 — environment/provenance producers
Map only the first Route-A evidence sources required to produce those facts, then add setup-python/venv/bare-pip relations in dependency order where the normal case requires them.

### R3.4 — Route-A state-proof composer
Define the bounded requirement-satisfaction result and exact fail-closed composition rules.

### R3.5 — optional Route-B seam
Define interface compatibility only; do not select new output acquisition without real pressure.

### R3.6 — closure
Verify every first-boundary proposition has one owner/producer/consumer path, unresolved edges are expressive, and no R2 semantic case has been silently widened or dropped.

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
