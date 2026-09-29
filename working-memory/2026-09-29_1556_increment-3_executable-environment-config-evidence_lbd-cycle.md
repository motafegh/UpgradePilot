# Increment 3 — Bounded Executable / Environment / Config Evidence — Learning-by-Doing Cycle

**Date:** 2026-09-29  
**Cycle status:** ACTIVE — A0 DONE; A1 CURRENT at continuity/onboarding gate; A2/B/Verification/D/E not started  
**Primary responsibility:** add only the bounded executable/interpreter, exact-process environment, persistent-config/default evidence required to close Route-A package-manager semantic blockers  
**Controlling plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**R4 implementation sequence:** `working-memory/2026-09-27_runtime-dependency-state-proof-implementation-and-verification-planning.md`  
**Accepted architecture:** `docs/architecture/ADR-0010-package-manager-semantic-facts-and-runtime-dependency-state-composition.md`  
**Previous cycle:** `working-memory/2026-09-28_increment-2_package-manager-operation-semantic-facts_lbd-cycle.md`

**Procedure provenance:** `UP-SKILL:upgradepilot-learning-by-doing` + `UP-SKILL:upgradepilot-working-memory`

## Cycle status

```text
A0 — DONE: current main, owners, recent closure, source/tests and evidence seams reconciled; no route contradiction
A1 — DONE: continuity model confirmed; precedence-direction wording corrected; gate cleared
A2 — CURRENT: upcoming-responsibility orientation; STOP at pre-B understanding gate
B — PENDING
Verification gate — PENDING
D — PENDING
E — PENDING
C — CONTINUOUS: preserve meaningful engineering + learning progression through closure
```

## A0 — current-state reconciliation + cycle initialization — DONE

### Live repository truth

Current `main` entered this cycle from commit `b57c2377edf27293933dae56fecb2c646d1b9796` (`close Increment 2 and select Increment 3 re-entry`). No later product/source/test work preceded this A0.

Increment 2 is closed. Its verified implementation:
- introduced `dependency/package_manager_operation.py`;
- introduced `dependency/package_manager_semantics.py`;
- migrated existing pip direct-install/project-selection consumers onto the shared declaration;
- removed the superseded pip-prefix helper;
- preserved dynamic/unsupported material as explicit semantic problems rather than guessed facts.

Product verification #10 (`36463198913`) is GREEN on run head `e838fa656964a898c037cca6ef0d390983f106ad`; the closed cycle records 15 focused investigation tests and 653 deterministic product tests.

### Accepted proof architecture carried into Increment 3

ADR-0010 remains controlling:

```text
exact command execution
+ dependency-owned package-manager operation declaration
+ independent effective semantic facts
→ later command-derived RequirementSatisfiedAtCommandCompletion composition
```

For a semantic dimension, source precedence remains:

```text
command line
> exact process environment
> applicable persistent configuration
> manager default
```

A lower source may decide only after higher relevant sources are positively non-overriding/disabled/resolved. Missing higher-source evidence remains unresolved.

Provider/workflow/shell code owns manager-agnostic evidence such as environment declarations, propagation and executable/interpreter relationships. Dependency/package-manager code owns pip/uv meaning and precedence. Existing CI coverage meaning must not be upgraded into package-state meaning.

### Current source truth at the Increment-3 seam

#### `src/upgradepilot/github/workflow_definition.py`

The bounded GitHub Actions provider IR already preserves typed scalar/mapping values and workflow/job/step structure, including run defaults. It currently does **not** represent workflow/job/step `env:` mappings in the admitted material fields or the corresponding dataclasses.

This makes 3A a real missing provider-IR capability rather than a duplicate implementation.

#### `src/upgradepilot/ci/runtime_execution.py`

Reusable exact-command execution evidence already exists. It composes static structural eligibility with exact workflow/runtime step correlation and keeps step success distinct from exact-command success.

Increment 3 should consume/reuse this boundary for effects that require positive execution (for example later admitted `GITHUB_ENV` writes) rather than creating package-manager-specific runtime execution.

#### `src/upgradepilot/dependency/workflow_context.py`

This module already demonstrates the useful fail-closed precedence pattern for static working-directory resolution:

```text
step > job > workflow > repository root
```

A dynamic higher-precedence value blocks fallback instead of fabricating a lower-level result. This is a relevant design pattern, not automatically the implementation owner for environment values.

#### `src/upgradepilot/dependency/package_manager_semantics.py`

Increment 2's semantic resolvers already:
- emit decisive command-line facts when the CLI closes a dimension;
- preserve `resolved_prefix` / semantic provenance;
- identify the next blocking source such as `process_environment`;
- refuse to infer manager defaults merely from absent CLI flags.

They currently do not consume exact-process environment evidence, persistent-config evidence, or manager-default closure inputs. That handoff is exactly what Increment 3 must make possible.

### Missing evidence producers confirmed by the accepted R3/R4 design

The current architecture still needs bounded forms conceptually equivalent to:
- exact executable/interpreter selection evidence;
- exact-process environment-value evidence for one requested variable at one exact command occurrence;
- dependency-owned package-manager persistent-config setting evidence when actually demanded;
- tiny manager-default adapters usable only after higher sources are closed.

Potential evidence adapters remain demand-driven:
- workflow/job/step `env:`;
- positively executed same-job `GITHUB_ENV` writes/propagation;
- admitted shell-local assignment/export effects;
- setup-python/PATH relationships;
- bounded venv activation/executable relationships;
- bare executable provenance only where the selected chain closes.

No universal shell simulator, Actions expression evaluator, PATH emulator, user/system config inventory, or universal pip/uv option model is authorized by this responsibility.

### Real-case continuity anchor

S002 remains a useful real boundary example. Its Python workflow contains:

```text
actions/setup-python@v4  python-version: "3.10"
→ python -m pip install --no-cache-dir --upgrade pip -r requirements.txt
→ ruff check .
→ pytest --cov
```

For the historical dependency PR, that Python workflow did not trigger because its path filters excluded `requirements.txt`. Therefore S002 is useful for understanding setup-python/interpreter/environment authority and missing evidence, but it is **not** itself positive proof that the dependency-state proposition held for that PR.

### A0 conclusion

No stale owner or technical contradiction changes the selected route.

```text
Increment 1
→ exact-command execution evidence exists

Increment 2
→ command-local operation + semantic facts exist
→ unresolved lower-source blockers are explicit

Increment 3
→ now supply only the bounded executable/process-env/config evidence
  needed to close those blockers

Increment 4
→ later compose RequirementSatisfiedAtCommandCompletion
```

The normal R4 Increment-3 responsibility therefore remains valid.

## Living A-phase orientation / learning map

### A1 continuity topics — CURRENT

Ali should leave A1 with a clear bridge from the closed Increment-2 model to the current source seam:

1. what Increment 2 can decide from the command itself;
2. why absence of a CLI flag is not enough to use a default;
3. what kinds of evidence now belong to provider/workflow/shell versus dependency/package-manager ownership;
4. why exact command execution from Increment 1 is reusable but does not establish environment/config semantics;
5. why Increment 3 is evidence acquisition/resolution, not the final package-state composer.

### A2 upcoming-responsibility topics — CURRENT

Orient proportionately before Build:
- 3A bounded declarative workflow/job/step environment representation;
- 3B executable/interpreter identity and relational environment identity;
- 3C one-variable exact-process environment queries and precedence;
- 3D persistent config/default closure only when demanded;
- likely producer → semantic-consumer data/evidence flow;
- close-defeaters and explicit unresolved states;
- coherent Build slice choice and proof owners;
- explicit non-goals and stop lines.

### Expected Increment-3 result / proof boundary

Pass condition from R4:

> the first selected Route-A fixture can obtain all required semantic facts from bounded evidence, while ordinary-looking cases with materially unknown ambient sources remain explicitly unresolved.

This increment does **not** establish the final `RequirementSatisfiedAtCommandCompletion` witness; that remains Increment 4.

### Important failure / unresolved states

Preserve at least:
- dynamic workflow/job/step environment value;
- effective dry-run environment value that defeats mutation;
- unresolved ambient/config source blocking a default;
- setup-python `update-environment: false`;
- closer PATH/executable selector superseding an earlier relation;
- arbitrary third-party action effects not guessed;
- mismatched/dynamic venv paths;
- unsupported shell/control-flow reachability.

### Explicit non-goals

Do not:
- build a universal GitHub Actions environment/expression model;
- simulate arbitrary shell state;
- infer runner ambient variables as absent;
- reconstruct all user/system/project pip/uv config;
- add generic log/stdout/artifact ingestion;
- compose final package state yet;
- alter maintainer-action permission or CI-coverage semantics.

### Ownership depth target

**Primary:** understand the evidence ownership/data-flow boundary between provider/workflow/shell facts and dependency-owned package-manager semantics.

**Secondary:** understand why the system uses demand-driven precedence and relational executable/environment identity instead of universal environment reconstruction.

Exact final class/function names and broad pip/uv catalogs remain lookup-level until A2/Build evidence justifies them.

## A1 — continuity / recent-work onboarding — DONE

A1 begins from the established Increment-2 ownership state. No additional technical work occurred between Increment-2 closure and this cycle's A0. The meaningful continuity delta is therefore architectural rather than a hidden implementation delta:

```text
Increment 2 asks:
"what semantic source blocks this dimension?"

Increment 3 answers:
"can we establish that exact source for this exact command,
without pretending to know the whole ambient environment?"
```

Ali cleared the continuity gate with the following working model:

1. A literal `python` is insufficient by itself because the effective executable/environment may be selected by surrounding evidence such as setup-python/PATH, virtual-environment activation, shell-local changes, or another closer selector. The exact relationship must be established rather than assumed.
2. Absence of `--dry-run` on the CLI is not enough to assert mutation because command line is only the highest-precedence source. If it is non-overriding, resolution must continue through exact process environment, then applicable persistent configuration, and only then may a manager default be admitted.

Precision correction recorded during A1: the accepted precedence is read from highest to lower source (`CLI → process environment → persistent config → default`). Ali's substantive point was correct: do not skip unresolved intermediate sources and jump to the default.

No material continuity gap remains. **A1 continuity/onboarding gate CLEARED.**

## C — continuous preservation

A0 established:
- current `main` and previous cycle closure are coherent;
- Increment 3 is still the correct next responsibility;
- existing workflow IR lacks admitted `env:` representation;
- exact-command execution already exists and is reusable;
- working-directory logic provides an existing fail-closed precedence pattern;
- package-manager semantic problems already expose the lower-source evidence demand;
- no universal environment/config subsystem should be introduced merely to make ordinary cases positive;
- S002 is a useful environment-authority learning anchor but not a positive runtime-state proof for its dependency PR.

No Smart Situational Override was required in A0.


## C update — A1 gate result

Ali demonstrated the required continuity model. No contradiction or new technical gap changed the Increment-3 route. The only correction was terminology around precedence direction; the proof behavior itself was understood correctly.

A2 is now the active phase. No Build authorization has been inferred from clearing A1.


## A2 — upcoming responsibility orientation — CURRENT

### Why this increment exists

Increment 2 deliberately stops when a semantic dimension needs a lower source. Increment 3 supplies manager-agnostic evidence for those exact blockers and lets dependency-owned package-manager semantics continue the accepted precedence chain.

The intended responsibility is **demand-backward**, not universal reconstruction:

```text
semantic fact needed
→ current blocking source
→ smallest trustworthy producer/evidence chain for that source
→ semantic resolver resumes
→ stop when the dimension is settled
```

A command-line decisive fact does not trigger unnecessary environment/config work.

### 3A — bounded declarative environment representation

Extend the GitHub workflow IR only enough to preserve workflow/job/step `env:` mappings needed by exact-process variable queries.

Required distinctions:
- absent;
- literal;
- dynamic/expression-bearing.

Provider-level precedence must fail closed. A dynamic higher-precedence declaration must not silently fall through to a lower declaration.

This layer records environment declarations; it does not interpret pip/uv variable meaning.

### 3B — executable / interpreter identity evidence

Create or extend manager-agnostic evidence that answers:

> Which executable/interpreter relationship is positively established for this exact command occurrence?

Demand-driven producer order remains:
1. supported explicit interpreter path;
2. `python -m pip` relation when positive executable provenance exists;
3. setup-python/PATH relation;
4. bounded venv activation/executable relation;
5. bare-pip provenance only when the chain closes.

Relational identity is acceptable when stronger than a guessed absolute path. A later/closer selector may supersede an earlier PATH relation.

### 3C — exact-process environment value

Support a bounded query:

> What is the effective value of variable X for this exact command occurrence?

Potential producers are added only when demanded:
- workflow/job/step `env:`;
- positively executed same-job `GITHUB_ENV` propagation;
- admitted shell-local assignment/export;
- provider-established values.

The provider/shell/CI layer returns the value/provenance/state. It does **not** decide what `PIP_DRY_RUN`, `PIP_TARGET`, or another manager variable means.

Unknown runner/ambient state remains unresolved unless positively closed.

### 3D — persistent config / default closure

Persistent pip/uv configuration remains dependency/package-manager-owned because its precedence/meaning is manager-specific.

Inspect only a proof-critical requested setting. Do not inventory the user's machine or all possible config files.

A manager default may decide only after every higher relevant source is positively non-overriding/disabled/resolved.

### Cross-layer evidence flow

```text
workflow / provider / shell declaration & execution evidence
          ↓
ExecutableSelectionEvidence
ProcessEnvironmentValueEvidence
          ↓
dependency-owned config/default adapters when still required
          ↓
existing package-manager semantic resolvers
          ↓
ManagerEnvironmentSelectionFact
InstallationDestinationFact
PackageMutationModeFact
DirectRequirementHandlingFact
          ↓
Increment 4 later composes package state
```

### Build-shape decision carried to the pre-B gate

Do **not** blindly implement every 3A–3D producer first.

B should begin from the first admitted Route-A semantic blockers and work backward to the smallest **coherent** evidence path that can close a controlled positive family, while preserving ordinary unresolved cases. This follows the accepted demand-driven architecture and the project's earlier backward/data-flow reasoning.

The Build remains responsible for the real Increment-3 pass condition, not merely adding an `env` field that passes unit tests.

### Expected proof

Focused proof should cover the provider IR/evidence producers and their semantic consumption. The accepted close-defeaters include:
- dynamic step/job/workflow environment;
- effective dry-run environment value;
- unresolved ambient/config blocking a default;
- setup-python `update-environment: false`;
- a closer PATH/executable selector superseding an earlier relation;
- arbitrary third-party action effects not guessed;
- mismatched/dynamic venv paths.

Representative real workflows may validly remain unresolved. Positive coverage must not be manufactured by weakening evidence requirements.

### Explicit non-goals

Increment 3 does not:
- create universal GitHub Actions or shell simulation;
- reconstruct all runner environment variables;
- inventory all pip/uv configuration;
- add generic logs/stdout/artifact acquisition;
- produce `RequirementSatisfiedAtCommandCompletion`;
- prove later use, compatibility, or maintainer-action permission.

### A2 pre-B reasoning gate

Before B, Ali should be able to reason about:

1. If workflow-level `PIP_DRY_RUN=false` exists but step-level `PIP_DRY_RUN=${{ matrix.mode }}` is dynamic, why must the result stay unresolved instead of using the workflow value?
2. Why should the GitHub/provider layer expose an exact variable value/provenance but **not** interpret whether that value means pip dry-run or normal mutation?
3. If setup-python establishes a PATH relation but a later admitted venv activation changes executable selection before `python -m pip`, which relation should control and why?

**STOP at the A2 pre-B understanding gate. No Build has begun.**

## C update — A2 orientation

A2 formalized the Increment-3 responsibility as demand-backward evidence closure rather than universal reconstruction. The planned implementation must preserve provider-neutral environment/executable evidence and dependency-owned package-manager interpretation. The Build should be selected from proof-critical blockers and must satisfy the Increment-3 pass condition rather than treating one IR field addition as completion.
