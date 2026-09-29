# Increment 3 — Bounded Executable / Environment / Config Evidence — Learning-by-Doing Cycle

**Date:** 2026-09-29  
**Cycle status:** ACTIVE — A0/A1/A2/B DONE; Verification GREEN through Product verification #14; D CURRENT; E PENDING  
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
A2 — DONE: responsibility/proof model understood; terminology correction recorded; gate cleared
B — DONE: B1-B5 implemented; first controlled Route-A fixture closes all four semantic facts while ordinary ambient cases abstain
Verification gate — GREEN: Product verification #14 on exact B5 head; focused 15/15 and deterministic 699/699
D — CURRENT: integrated post-work evidence-backed learning and ownership
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


## A2 — upcoming responsibility orientation — DONE

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

Ali cleared the A2 gate with the correct proof model:

1. A later venv activation may supersede an earlier setup-python/PATH executable relation for a later `python -m pip` command. Precision correction: venv activation is not itself a pip CLI-precedence source; it is a shell/environment executable-selection effect. The controlling relationship is the closest positively established effective executable-selection relation for that command.
2. If no CLI `--dry-run` exists and the exact process/config sources cannot be established, mutation remains `unresolved`. If all higher relevant sources are positively non-overriding/disabled, the manager default may then establish normal apply-changes behavior.

No material understanding gap remains.

**A2 pre-B understanding gate CLEARED. B may begin under the accepted Increment-3 responsibility.**

## C update — A2 orientation

A2 formalized the Increment-3 responsibility as demand-backward evidence closure rather than universal reconstruction. The planned implementation must preserve provider-neutral environment/executable evidence and dependency-owned package-manager interpretation. The Build should be selected from proof-critical blockers and must satisfy the Increment-3 pass condition rather than treating one IR field addition as completion.


### A2 real-case grounding — S002 / S011 / S008

A2 was grounded in existing product-simulation cases rather than synthetic-only examples.

#### S002 — closest positive Increment-3 pressure

Existing evidence:
- workflow declares `actions/setup-python@v4` with Python 3.10;
- a later run step uses `python -m pip install ... -r requirements.txt`;
- the workflow also contains Ruff and pytest;
- for the historical PR, the Python workflow did not trigger because `requirements.txt` was outside its PR path filter;
- the historical Docker build succeeded, but exact resolved dependency environment is no longer recoverable from expired logs.

Current UpgradePilot can separately reason about static command occurrence/consumption and exact-command execution when runtime correlation exists, and Increment 2 can parse `python -m pip install` into a package-manager declaration. But the semantic layer cannot yet turn the literal `python` plus setup-python declaration into a trustworthy effective manager-environment relation, nor can it close relevant process environment/config sources needed before manager defaults.

Increment 3 would add the bounded evidence machinery needed for a suitable live/controlled Route-A variant:
```text
setup-python provider declaration/effect
+ exact later command location
+ PATH/executable-selection relationship
→ executable/interpreter environment evidence

workflow/job/step env (+ later admitted propagation where needed)
→ exact-process variable evidence

dependency package-manager resolver
→ consumes those facts under CLI > process env > config > default
```

What would still not be established merely by Increment 3:
- that S002's historical skipped Python workflow executed;
- the expired historical resolver state;
- pytest/TestClient behavior;
- final RequirementSatisfiedAtCommandCompletion (Increment 4);
- compatibility or maintainer action.

#### S011 — useful counterexample: Increment 3 does not repair a missing affected environment

The inspected Ubuntu and macOS test workflows both install `.[dev]`, not `.[mlx]`.

Therefore the already-established bounded result is:
```text
affected dependency is inside mlx optional family
+ inspected workflows install dev family
→ those workflows do not form the affected mlx dependency environment
```

This conclusion does not depend on resolving which `python` executable or `PIP_DRY_RUN` value applied. Even perfect Increment-3 environment identity would not turn `.[dev]` into `.[mlx]`.

Increment 3 may later strengthen environment identity for some command in this repository, but it must not blur the more fundamental S011 proposition: the affected optional environment was never requested by those inspected workflows.

#### S008 — useful counterexample: interpreter/version relevance remains proposition-specific

S008 established a Python-3.6-relevant artifact transition: the newer OpenCV release loses the CPython-3.6 Linux prebuilt-wheel path while retaining source-distribution fallback.

The inspected CI installs requirements but does not pin/matrix Python 3.6, so it does not establish coverage of that exact Python-3.6 wheel-to-source transition.

Increment 3 could strengthen a workflow only if bounded evidence can positively establish the exact interpreter/environment relation for the relevant install command. If the workflow simply lacks proof that the install ran under Python 3.6, Increment 3 should preserve that uncertainty; it must not infer Python 3.6 merely from unrelated repository context such as a Dockerfile.

Even if Python-3.6 environment identity were established, the separate proposition "source fallback build succeeds" would still require its own evidence and is not created by Increment 3.

#### Cross-case lesson

```text
S002:
missing edge can be executable/environment/config identity
→ Increment 3 directly targets this class

S011:
missing edge is affected optional family never installed
→ Increment 3 cannot repair it

S008:
missing edge is exact Python-3.6 execution/artifact-path coverage
→ Increment 3 may help only if executable/interpreter evidence can actually close that identity
→ source-build success remains separate
```

This is the product-faithful reason for demand-driven Increment 3: add evidence only where it closes the actual proposition blocker, not because environment modeling is generally useful.


## C update — A2 gate result

Ali demonstrated the required pre-B model. The only correction was that venv activation belongs to executable/environment selection, not pip CLI precedence. The substantive ordering judgment was correct: a later positively established environment selector can supersede an earlier PATH relation for the exact later command.

Build is now authorized only inside the existing Increment-3 responsibility. The first Build slice must be chosen from real Route-A semantic blockers and remain connected to the increment pass condition.


## B — implementation progression

### Child responsibility B1 — bounded declarative GitHub Actions environment evidence

Implemented on `main`:

- `f3b5ab0` — `workflow_definition.py` now preserves workflow/job/step `env:` mappings as bounded provider IR, including expression-bearing values;
- `a5bc2cc` — focused workflow-definition coverage for workflow/job/run-step/uses-step environment mappings;
- `0007530` — new `github/workflow_environment.py` resolves one requested declaration through step > job > workflow precedence without claiming runtime process state;
- `07ef6a4` — focused precedence/unresolved tests for the declarative environment observation.

The provider observation preserves:
- literal established declaration;
- dynamic/ambiguous declaration as unresolved;
- no declaration as `not_declared`, explicitly **not** process-variable absence.

### B model correction discovered during source preflight

The initial route pressure was “workflow/job/step env → exact-process value.” Source/semantics inspection exposed a missing closer layer:

```text
workflow/job/step env declaration
!= automatically exact process value
```

For example:

```bash
PIP_DRY_RUN=1 pip install -r requirements.txt
```

can override an inherited declarative value for that exact command process. Earlier positively executed `GITHUB_ENV` writes and other admitted provider/shell effects may also contribute.

Therefore the implementation deliberately stops the new `WorkflowEnvironmentValueObservation` at **static declaration evidence**. It is not fed directly into pip semantics as exact-process truth.

This is not a route change; it is the accepted 3C boundary becoming concrete. The next B child should establish parser/provider-owned command-local environment-assignment evidence and then compose the smallest trustworthy exact-process query rather than reparsing shell text inside dependency/package-manager code.

### Verification state

No runtime/focused test execution has yet been obtained for these commits. Post-change source inspection is complete and coherent, but this is **not** a Verification PASS. Product verification remains deferred until the coherent Build slice has enough cross-layer behavior to justify the gate.

No Smart Situational Override has been used.


### Child responsibility B2 — command-local exact-process environment evidence + pip dry-run consumption

Implemented on `main`:

- `63a3add` — parser-neutral `StaticCommandOccurrence` now preserves bounded Bash command-local environment assignments rather than forcing downstream layers to reparse raw shell text;
- `6e010dc` — focused command-analysis cases cover literal, dynamic and ordered multiple Bash command-local assignments;
- `d04e5cf` — new `github/process_environment.py` introduces bounded exact-command process-variable evidence;
- `2167b45` — focused exact-process evidence cases preserve literal local assignment, dynamic unresolved state, declarative-only unresolved state and ambient unresolved state;
- `d0026be` — pip mutation semantics can consume exact `PIP_DRY_RUN` process evidence while preserving package-manager meaning in the dependency layer;
- `6f2b62f` — semantic tests cover true/false/invalid/unresolved process values;
- `5eadf5d` — workflow-IR environment fields were made constructor-compatible by defaulting the new fields to `None`;
- `0c5b1fd` — cross-layer integration proof covers workflow text → exact command → process env → package-manager mutation semantics.

Current semantic behavior:

```text
--dry-run on CLI
→ PackageMutationModeFact(dry_run)

no CLI --dry-run
+ exact command-local PIP_DRY_RUN=1
→ PackageMutationModeFact(dry_run)
  provenance: command_line(non-overriding) → process_environment(decisive)

no CLI --dry-run
+ exact command-local PIP_DRY_RUN=0
→ process environment proven non-overriding
→ blocker moves to persistent_configuration

no CLI --dry-run
+ dynamic/unknown exact process value
→ remains unresolved at process_environment
```

This is the intended precedence behavior: proving a higher source non-overriding advances the proof one source; it does not authorize skipping the next source.

### Current B boundary

The first exact-process producer intentionally establishes positive values only from literal Bash command-local assignments. Workflow/job/step declarations are preserved and queried, but not yet promoted to exact-process truth because same-step shell state, previous `GITHUB_ENV` writes, provider effects and ambient state still require bounded composition.

The next coherent Build pressure is now explicit:
- persistent pip configuration/default closure for dimensions whose process value is positively non-overriding; and/or
- executable/interpreter identity for `python -m pip` / setup-python / venv relations.

Increment 3 remains B CURRENT; no Verification PASS has been claimed.


### B child verification — Product verification #11 GREEN

Hosted Product verification run #11:
- run: https://github.com/motafegh/UpgradePilot/actions/runs/36585040140
- event: `workflow_dispatch`
- attempt: 1
- head: `24d28c03495b063de817946c6faf54cd2ba8255d`
- conclusion: **success**
- job `Installed package and deterministic product tests`: success
- fresh install / CLI entry-point checks: success
- focused investigation composition: **15 tests, OK**
- full deterministic product regression: **672 tests, OK**

The hosted logs explicitly contain the new Increment-3 proof cases, including:
- workflow env precedence;
- Bash command-local environment assignment preservation;
- exact-process command-local environment establishment;
- end-to-end command-local PIP_DRY_RUN → mutation semantic fact;
- pip semantic consumption of exact-process dry-run evidence.

Supported claim:
> The first Increment-3 declarative/process-environment/pip-mutation slice executes successfully in the installed product environment and does not regress the current deterministic product suite.

Non-proof:
- this does not yet satisfy the whole Increment-3 pass condition;
- job/workflow/step env alone is still not exact-process truth;
- GITHUB_ENV / same-step prior export / provider effects remain unmodeled;
- persistent pip configuration/default closure is not yet implemented;
- executable/interpreter identity is not yet implemented;
- no command-derived RequirementSatisfiedAtCommandCompletion claim exists yet.

Therefore B remains CURRENT. This is a verified child slice, not the cycle Verification gate.


### B continuation after Product verification #11

#### Child responsibility B3 — bounded persistent pip-config closure

Implemented:
- `22bc656` — dependency-owned `package_manager_config.py` with setting-scoped persistent-config evidence;
- `ae8ccb8` — focused config evidence tests;
- `68c2ffb` — mutation semantics consume disabled persistent-config evidence;
- `7d05747` — semantic tests for manager-default application only after higher sources close;
- `22cf8ec` — cross-layer integration case for exact `PIP_DRY_RUN=0` + `PIP_CONFIG_FILE=/dev/null`.

Source-backed pip semantics inspected from current upstream `pypa/pip`:
- `src/pip/_internal/configuration.py`: exact `PIP_CONFIG_FILE=os.devnull` causes pip to skip loading all configuration files;
- the same module keeps environment variables and configuration files as distinct sources;
- pip boolean parsing accepts true/false forms including 1/0.

Current supported composition:

```text
no CLI --dry-run
+ exact-process PIP_DRY_RUN=0
+ exact-process PIP_CONFIG_FILE=/dev/null
→ command line non-overriding
→ process env non-overriding
→ persistent config disabled
→ manager default decisive
→ PackageMutationModeFact(apply_changes)
```

A concrete non-null config path remains unresolved until its contents/precedence are actually acquired.

#### Child responsibility B4 — executable/interpreter selection evidence

Implemented:
- `7aebef2` + `0d3b79b` — provider-owned static executable selection distinguishes explicit paths from bare PATH-dependent names;
- `73efab5` — clarified this first layer as a static observation rather than runtime-strengthened evidence;
- `bc1b1db` + `101f16d` — CI-owned bounded executable-selection composition for:
  - explicit executable path;
  - immediately preceding `actions/setup-python` v4-v7;
  - default/explicit `update-environment: true`;
  - exact-attempt successful setup step;
  - first/sole bare `python` command in the later run step;
  - no closer workflow/job/step or command-local PATH override.

Explicit close-defeaters are preserved:
- `update-environment: false` → unresolved;
- failed/non-proven setup-python runtime execution → unresolved;
- intervening user step → unresolved for this first family;
- command-local PATH override → unresolved;
- prior same-step command such as venv activation before `python` → unresolved rather than allowing the older setup-python relation to win.

External source evidence inspected:
- `actions/setup-python` action manifests v4, v5, v6, v7: `update-environment` defaults to true;
- setup-python implementation calls `core.addPath` for the selected Python install/bin directories when environment updating is enabled;
- `actions/toolkit/packages/core/src/core.ts`: `addPath` prepends PATH for the action and future actions;
- `actions/runner` records added paths and reverses/prepends them when constructing later step PATH, so the most recently added setup-python bin path has precedence absent a closer override.

This is deliberately not a general PATH simulator and does not yet model arbitrary GITHUB_PATH writers or non-adjacent provider chains.

### Current verification boundary after B3/B4

Product verification #11 proves through head `24d28c0` only.

Current main head after B3/B4 source/test additions is `101f16d94998def51631926abd86850ab49a32de`.

Post-#11 changes have been source-inspected but **not yet hosted-execution verified**. Therefore:
- B remains CURRENT;
- the already verified B1/B2 slice remains valid;
- B3/B4 are pending the next hosted Product verification run;
- no overall Increment-3 Verification gate is claimed.


### Verification checkpoint — Product verification #12 FAILED, diagnosis resolved

Hosted Product verification run #12:
- run: https://github.com/motafegh/UpgradePilot/actions/runs/36588225308
- head: `dfc59a00339cfd0d3c76a70137c14e15b91f116a`
- focused investigation composition: success
- full deterministic product regression: **691 tests, 1 failure**

Single failing test:
`test_package_manager_process_environment_integration.PackageManagerProcessEnvironmentIntegrationTests.test_command_local_disabled_dry_run_moves_to_config_not_default`

Observed result:
`persistent_config_setting_unresolved`

Stale expected result:
`package_mutation_mode_needs_persistent_config_evidence`

Diagnosis:
- before B3, the integration path supplied no persistent-config evidence, so the generic semantic blocker "persistent-config evidence needed" was correct;
- after B3, the integration path now actively queries exact `PIP_CONFIG_FILE` process evidence and supplies a `PackageManagerConfigSettingEvidence`;
- when that exact process value is unresolved, the semantic layer correctly reports the stronger state: persistent-config evidence exists but the setting remains unresolved;
- the focused semantic tests already distinguish these two states correctly.

Therefore #12 exposed a stale integration assertion, not a product semantic regression.

Fix:
- `7c22f6e` — renamed the integration test to express the stronger contract and changed its assertion to `persistent_config_setting_unresolved`, while also checking that the detail preserves upstream reason `pip_config_file_process_environment_unresolved`.

Current verification status:
- Product verification #11 remains valid for B1/B2 through `24d28c0`;
- B3/B4 plus the corrected integration assertion now require a fresh hosted run on head `7c22f6e9cfde44972b62b0e32b7b4d5fbbdadcdb`;
- no Verification PASS is claimed yet;
- B remains CURRENT.


### B child verification — Product verification #13 GREEN

Hosted Product verification run #13:
- run: https://github.com/motafegh/UpgradePilot/actions/runs/36588887660
- event: `workflow_dispatch`
- head: `f48f9ac11c9fc4b4e4b4214ffe4d325814f38e74`
- conclusion: **success**
- installed-package / CLI checks: success
- focused investigation composition: **15 tests, OK**
- full deterministic product regression: **691 tests, OK**

The hosted logs explicitly include passing B3/B4 cases:
- `test_dev_null_config_file_disables_all_persistent_config`;
- `test_disabled_config_allows_manager_default_apply_changes`;
- `test_posix_explicit_path_is_established_without_path_lookup`;
- `test_successful_adjacent_setup_python_establishes_bare_python_relation`.

This verifies the #12 correction and the current B3/B4 implementation batch.

Supported claim:
> The bounded persistent-config/default path and the first explicit/setup-python executable-selection families execute successfully in the installed product environment without regressing the deterministic suite.

Still not established:
- arbitrary persistent pip config contents/precedence;
- general workflow/job/step env → exact-process closure;
- GITHUB_ENV/GITHUB_PATH propagation beyond the first admitted families;
- same-step venv activation identity;
- arbitrary/non-adjacent PATH mutation;
- bare pip provenance where executable identity is not closed;
- the complete first Route-A fixture across all four semantic facts;
- Increment-4 RequirementSatisfiedAtCommandCompletion.

Therefore Increment 3 remains **B CURRENT**. B1/B2/B3/B4 are now hosted-verified building blocks; the next B work should target the remaining proof-critical blockers required to satisfy the Increment-3 pass condition rather than broadening generically.


### Child responsibility B5 — first complete Route-A semantic fixture

After B1-B4 were hosted-green, the Increment-3 pass condition was evaluated directly instead of expanding environment modeling generically.

Selected controlled positive family:

```bash
PIP_DRY_RUN=0 \
PIP_CONFIG_FILE=/dev/null \
PIP_TARGET= \
PIP_PREFIX= \
PIP_ROOT= \
PIP_ONLY_DEPS=0 \
PIP_ONLY_DEPENDENCIES=0 \
/opt/bootstrap/bin/python -m pip \
  --python /opt/target/bin/python \
  install --no-user --no-deps -r requirements.txt
```

Why this is a useful controlled Route-A fixture:
- launcher executable path is explicit;
- manager environment is decisive through CLI `--python`;
- `--no-user` explicitly closes the user-site destination branch;
- target/prefix/root process variables are positively present as empty/non-overriding;
- `PIP_DRY_RUN=0` is positively non-overriding;
- both current pip only-deps environment aliases are positively disabled;
- `PIP_CONFIG_FILE=/dev/null` positively disables persistent pip config files;
- lower manager defaults therefore become admissible only after higher sources are closed.

Current upstream pip source evidence inspected:
- `Configuration.get_environ_vars()` accepts `PIP_*` variables and normalizes underscores to long-option hyphens;
- `ConfigOptionParser` applies environment/config values to matching long options and parses store-true/store-false values through pip boolean conversion;
- empty configuration/environment values are filtered from effective defaults;
- `PIP_CONFIG_FILE=os.devnull` skips loading all config files;
- pip install defaults `--target`, `--prefix`, and `--root` to no retargeting;
- `--only-deps/--only-dependencies` is a store-true option with default false.

Implemented on `main`:
- `9c67b61` — generalized disabled persistent-config evidence across dry-run, installation-destination, and only-deps settings;
- `8839e0e` — added bounded lower-source resolution for normal installation destination and direct requirement handling;
- `7510af6` — preserved the prior generic blocker reasons when lower-source evidence has not been supplied at all;
- `d44404d` — added focused tests for default destination, process-env destination override, explicit unresolved user-scope boundary, direct-handling default, process-env exclusion, and alias conflict;
- `f191de8` — verified `/dev/null` persistent-config disablement across all three supported settings;
- `b98a1d5` — added the first complete controlled Route-A semantic fixture.

New destination behavior:
```text
no CLI target/prefix/root/user
+ explicit --no-user
+ exact PIP_TARGET/PIP_PREFIX/PIP_ROOT empty
+ persistent config disabled
→ manager default
→ InstallationDestinationFact(manager_environment_scheme)
```

New direct-requirement behavior:
```text
no CLI only-deps exclusion
+ PIP_ONLY_DEPS=0
+ PIP_ONLY_DEPENDENCIES=0
+ persistent config disabled
→ manager default
→ DirectRequirementHandlingFact(handled)
```

The first positive fixture is expected to produce all four independent facts for one exact command identity:
- `ManagerEnvironmentSelectionFact` → `/opt/target/bin/python`;
- `InstallationDestinationFact` → `manager_environment_scheme`;
- `PackageMutationModeFact` → `apply_changes`;
- `DirectRequirementHandlingFact` → `handled`.

The paired ordinary-looking fixture `python -m pip install -r requirements.txt` intentionally remains unresolved at lower-source evidence rather than inheriting ambient defaults.

Important scope boundary:
- this does not create a new all-semantics bundle/composer in Increment 3;
- each fact remains independently owned and shares exact command identity;
- final RequirementSatisfiedAtCommandCompletion composition remains Increment 4;
- broader user/no-user environment composition, arbitrary persistent config content, GITHUB_ENV/GITHUB_PATH, venv activation, and general bare-executable resolution remain outside B5 unless later evidence proves they are required.

### B5 verification state

B5 source and tests are committed through `b98a1d51df7412dcf0126d4ba231ad24c2e6833c` but have **not yet received hosted execution proof**.

If the next Product verification is green and the new Route-A fixture executes as intended, reassess the Increment-3 pass condition before adding any further B work. Do not invent B6 unless a concrete remaining proof-critical blocker is exposed.


### Formal Verification / Evidence Gate — Product verification #14 GREEN

Hosted Product verification run #14:
- run: https://github.com/motafegh/UpgradePilot/actions/runs/36594702059
- event: `workflow_dispatch`
- exact head: `29247346d1c1e3ea7074ffd7daf9c53d8c3beeda`
- conclusion: **success**
- installed-package / CLI checks: success
- focused investigation composition: **15 tests, OK**
- full deterministic product regression: **699 tests, OK**

The hosted logs explicitly prove the new B5 acceptance cases:
- `test_controlled_positive_fixture_closes_all_four_semantic_facts` — PASS;
- `test_ordinary_looking_fixture_without_closure_evidence_remains_unresolved` — PASS;
- `test_default_destination_requires_explicit_lower_source_closure` — PASS;
- `test_disabled_only_deps_environment_and_config_allow_direct_handling_default` — PASS.

### Increment-3 pass-condition assessment

Controlling pass condition:

> the first selected Route-A fixture can obtain all required semantic facts from bounded evidence, while ordinary-looking cases with materially unknown ambient sources remain explicitly unresolved.

Observed proof:

```text
controlled Route-A fixture
→ ManagerEnvironmentSelectionFact
→ InstallationDestinationFact(manager_environment_scheme)
→ PackageMutationModeFact(apply_changes)
→ DirectRequirementHandlingFact(handled)
→ shared exact command identity

ordinary python -m pip install -r requirements.txt
without lower-source closure
→ remains unresolved
```

Therefore the Increment-3 Build responsibility has met its selected pass condition. No concrete proof-critical reason remains to invent another B child.

B is **DONE**.
Verification gate is **GREEN**.
D is now **CURRENT**.

Residual intentionally unsupported/unresolved surfaces remain explicit scope boundaries, not blockers to Increment-3 acceptance:
- arbitrary persistent pip config contents/precedence;
- generic workflow/job/step env → exact-process closure;
- arbitrary GITHUB_ENV/GITHUB_PATH propagation;
- same-step venv activation;
- general bare-pip/non-adjacent PATH provenance;
- universal runner environment reconstruction.

These may be revisited only if later product evidence makes them decision-critical.


## D — integrated post-work evidence-backed learning — CURRENT

### Teaching structure selected

D will teach Increment 3 as one evidence-resolution system rather than five isolated implementation changes:

```text
exact command identity
→ declarative environment observations
→ exact-process environment evidence
→ persistent package-manager config evidence
→ manager default only after higher sources close
→ independent semantic facts

parallel:
exact command executable
→ explicit path / bounded setup-python relationship
→ executable/interpreter selection evidence
```

Then connect those facts back to the product-evidence graph and Increment 4 rather than treating semantic facts as end-state conclusions.

### Real-case teaching anchors

**S002 — Kubernetes Dashboard Token API / HTTPX**
- Python workflow declares `actions/setup-python@v4` with Python 3.10 followed by `python -m pip install ...`, Ruff and pytest.
- But the workflow `paths:` excludes `requirements.txt`, so the dependency-only PR did not trigger that Python workflow.
- Docker workflow did run and install requirements/build the image, but did not execute TestClient/route behavior; historical exact resolved dependency graph is unavailable because logs expired.
- D lesson: Increment 3 can reason about executable/environment semantics only for an admitted command/evidence path; it cannot turn a skipped workflow into execution evidence or upgrade package installation into behavioral compatibility.

**S008 — CARLA / OpenCV Python-3.6 artifact fallback**
- Old OpenCV release had CPython-3.6 Linux wheels.
- New release has no CPython-3.6-compatible published wheel but does have an sdist and retains Python-3.6 source-build metadata.
- Target has real Python-3.6 relevance, but inspected CI does not establish that the requirements install ran under Python 3.6.
- D lesson: executable/interpreter identity can close the missing “which Python actually installed this?” edge. Even if it closes Python 3.6 identity, the next proposition “does the sdist build succeed?” remains separate and unresolved.

**S011 — Dictare MLX optional-extra coverage**
- affected NumPy pin is in optional `mlx` family;
- both inspected workflows install `.[dev]`, not `.[mlx]`;
- real runtime activation additionally needs Apple-Silicon/macOS/hardware-path conditions.
- D lesson: Increment 3 cannot repair the wrong dependency family being installed. Perfect PATH/env/config semantics for `.[dev]` still do not form the affected `mlx` environment.

### A2 expectation vs verified reality

A2 expected bounded 3A/3B/3C/3D evidence producers. Verified B1-B5 realized that responsibility proportionately:
- 3A: workflow/job/step env representation and step > job > workflow declaration precedence;
- 3C: exact-process positive evidence from literal Bash command-local assignments; declarative-only values deliberately remain below exact-process truth;
- 3D: setting-scoped pip persistent-config evidence using exact `PIP_CONFIG_FILE=/dev/null`, plus manager defaults only after higher sources close;
- 3B: explicit executable-path observation plus bounded runtime-backed setup-python PATH relation;
- B5: destination/direct-handling lower-source closure and one complete controlled four-fact Route-A fixture.

Expected but not needed for the selected pass condition and therefore not implemented:
- generic GITHUB_ENV/GITHUB_PATH propagation;
- arbitrary workflow env → exact-process promotion;
- same-step venv activation;
- arbitrary persistent config file acquisition/composition;
- general bare-pip/non-adjacent PATH provenance.

These remain explicit later expansion points, not hidden unfinished B work.

### D ownership gate

After integrated teaching, Ali should reason about:
1. declaration evidence vs exact-process evidence;
2. source precedence and when a manager default is legally usable;
3. launcher executable identity vs pip manager-target environment identity;
4. which proof layer owns a real-case gap;
5. what Increment 3 proves versus what remains for Increment 4 or later behavioral evidence.

D remains CURRENT until those reasoning checks are answered and any material gaps are characterized for E.
