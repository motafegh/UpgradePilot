# Artifact Serviceability Public Investigation Integration — Working Memory

**Date:** 2026-09-06  
**Session state:** ACTIVE execution/reasoning record. `../MEMORY.md` remains the sole owner of live project position.  
**Selected bounded plan:** [`../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md)

## Session objective

Continue UpgradePilot from the framework-experiment closure by completing the unfinished artifact-serviceability application-integration responsibility through the normal `PublicPullRequestInvestigation` path, using the repository Learning-by-Doing method and progressively preserving decisions/evidence as the work proceeds.

This session began with planning/design and has now entered the first bounded Build slice.

## Verified starting state

Re-entry inspection established:

1. `main` was at the framework-experiment closure boundary before this planning update; the framework package is intentionally deferred rather than the next product target.
2. The broad historical impact/applicability foundation plan already names the unfinished second-mechanism application-path responsibility, but its coordinate-heavy identity is no longer appropriate for live navigation and its scope is wider than the exact continuation now needed.
3. A new semantic bounded continuation plan now owns only the artifact-serviceability public-investigation integration responsibility.
4. `src/upgradepilot/impact/artifact_serviceability.py` already owns:
   - exact old/proposed wheel-inventory interpretation;
   - published-wheel-serviceability candidate formation;
   - explicit target wheel-compatibility evidence/problem contracts;
   - candidate applicability evaluation.
5. `src/upgradepilot/target/artifact_environment.py` already owns bounded exact-workflow interpretation into target artifact-environment facts while explicitly preserving static-configuration versus runtime-execution proof limits.
6. `src/upgradepilot/investigation.py` currently coordinates the Python-support mechanism but does not yet expose or orchestrate the artifact-serviceability / target-artifact-environment path.
7. `src/upgradepilot/cli.py` currently renders dependency, CI, package/upstream, Python-support, and target-Python state, but no artifact-serviceability section.
8. `tests/test_investigation.py` protects important orchestration invariants: conditional target acquisition, early-stop behavior, independent evidence preservation, exact target identity, and unresolved-state preservation.
9. `tests/test_artifact_serviceability.py` and `tests/test_target_artifact_environment.py` are existing focused proof owners for the two already-built mechanism components.
10. Package-root API expansion is not wanted; internal contracts remain with their owning modules.

## Why a new bounded plan was justified

The existing broad foundation plan is still useful historical/parent provenance, but it is not a good live execution surface for this session because:

- current naming governance requires semantic responsibility identities for selected active work;
- most of the broad foundation responsibility is already implemented/proven;
- the remaining work is a coherent multi-file integration spanning result contract, orchestration, presentation, tests, and final reconciliation;
- this boundary contains real design decisions that should be made progressively from source/test evidence rather than guessed all at once.

Therefore the session uses:

`plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md`

as the bounded continuation plan.

## Learning-by-Doing cadence for this session

For each substantive slice:

```text
orient on the exact mechanism / owner / proof boundary
→ perform one bounded real change
→ inspect actual tests/evidence
→ preserve material decisions/results here
→ explain what happened and what it teaches us
→ make the next ownership/reasoning decision together when useful
```

Do not silently jump from contract design to orchestration to CLI to full validation in one batch.

## Initial architectural model

The desired ownership relation is currently:

```text
PyPI release evidence
→ impact.artifact_serviceability candidate/evaluation owner

exact workflow file
→ github workflow-definition owner
→ target.artifact_environment interpretation owner

normal application coordination
→ investigation.py

human-facing rendering
→ cli.py
```

Important separation:

```text
published artifact transition fact
!= target exposure
!= exact target wheel compatibility
!= runtime installation outcome
!= final maintainer recommendation
```

`investigation.py` should coordinate these owners, not recreate their semantics.

## Decisions already established

### Decision 1 — continue with semantic plan identity

Use the new semantic continuation plan rather than selecting the old coordinate-heavy foundation filename as the live execution surface.

Reason: current navigation/naming governance plus the much narrower remaining responsibility.

### Decision 2 — integration is additive

The artifact-serviceability path must be added without weakening or replacing existing Python-support/CI/upstream behavior.

Reason: the existing mechanism is already independently proven and the second mechanism is meant to create heterogeneous technical state, not a replacement architecture.

### Decision 3 — serviceability state is technical evidence, not overall recommendation

The new path may expose candidate/applicability/proof-strength state, but must not silently decide the dependency update or maintainer action.

Reason: overall synthesis remains a separate product responsibility.

### Decision 4 — static target evidence remains bounded

Runner/Python/install declarations from workflow configuration must not be treated as runtime execution or exact wheel compatibility unless an admitted deterministic transformation genuinely establishes that proposition.

Reason: current Target and artifact-serviceability owners explicitly preserve this proof boundary.

## Slice 1 result-contract / evidence-flow decision

The first checkpoint inspected the concrete owners rather than designing from names alone:

- `tests/test_artifact_serviceability.py` proves candidate / no-candidate / evidence-problem distinctions and proves that missing or insufficient exact target compatibility remains unresolved.
- `tests/test_target_artifact_environment.py` proves that exact workflow interpretation deliberately leaves `exact_wheel_compatibility_state == "unresolved"`, including when literal runner/Python/install declarations are visible.
- `tests/test_investigation.py` proves conditional acquisition, independent CI preservation, target acquisition only after a grounded proposition, and explicit unresolved states.
- `src/upgradepilot/investigation.py` already transiently acquires exact workflow definitions for CI, but currently exposes only run/job evidence and acquires only the proposed PyPI release.
- `src/upgradepilot/pypi/release.py` already provides a provider-owned `PackageReleaseResult` for any exact package/version request; no new release-provider abstraction is needed.
- `DependencyChangeAnalysis.source_contexts` deliberately supports several exact dependency source contexts rather than projecting them onto one path.

### Decision 5 — preserve old package-release provider state explicitly

Add an application-level `old_package_result: PackageReleaseResult | None` beside the existing proposed `package_result`.

Why:

- artifact candidate formation requires exact old + proposed release inventories;
- `PackageReleaseResult` already distinguishes external evidence from provider problems;
- exposing the old result prevents a failed old-release acquisition from collapsing into the same apparent state as a successfully evaluated no-candidate transition;
- it reuses the existing PyPI owner instead of inventing an artifact-specific acquisition wrapper.

Intended activation semantics:

```text
dependency branch inactive
→ package_result = None
→ old_package_result = None

proposed package unavailable/problem
→ package_result = explicit provider problem
→ old_package_result = None
→ artifact candidate not attempted

proposed package established
→ acquire exact old release
→ old_package_result = evidence or explicit provider problem
```

### Decision 6 — expose candidate state and assessment state separately

The smallest truthful result contract needs both:

```text
artifact_serviceability_candidate_result
artifact_serviceability_impact_result
```

Candidate result uses the existing domain result space:

```text
ArtifactServiceabilityImpactCandidate
| ArtifactServiceabilityEvidenceProblem
| None
```

Its `None` means **no wheel-loss candidate after valid old/proposed release interpretation** only when the surrounding provider prerequisites are established. Inactive/provider-blocked states remain distinguishable from the accompanying `package_result` / `old_package_result` state.

`artifact_serviceability_impact_result` is `ArtifactServiceabilityImpactAssessment | None`:

- `None` when no candidate exists or candidate formation did not complete;
- an assessment when a real candidate exists;
- initially unresolved when exact target wheel compatibility has not been established;
- eligible for later re-evaluation only if admitted exact target compatibility evidence becomes available.

This avoids a new application-level mega-union while keeping candidate discovery separate from applicability.

### Decision 7 — target artifact-environment state is a collection, not one global target

One pull-request investigation can legitimately contain several exact workflow definitions and several dependency source contexts. A single target artifact-environment field would silently discard cardinality or force arbitrary selection.

The application layer now uses:

```text
DependencySourceArtifactEnvironmentResult
- dependency_source: DependencySourceContext
- target_environment: TargetArtifactEnvironmentResult
```

and the public investigation contract exposes:

```text
target_artifact_environment_results:
    tuple[DependencySourceArtifactEnvironmentResult, ...]
```

The target result still owns repository/revision/workflow/job semantics. The application association adds only the dependency-source relationship needed for later composition and explanation; it does not strengthen the evidence or claim runtime execution.

### Decision 8 — current static target environment does not become exact wheel compatibility

The current admitted target owner explicitly keeps exact wheel compatibility unresolved even when literal runner and Python declarations are available.

Therefore the first integration must **not** synthesize `TargetWheelCompatibilityEvidence` from:

```text
runs-on
+
setup-python python-version
+
static install declaration
```

It also should not create a semantic conversion merely so the assessment object looks more populated.

For the first integrated path:

```text
candidate exists
→ pre-target artifact-serviceability assessment can be created
→ exact workflow target-artifact-environment evidence may be collected where justified
→ target-artifact-environment results remain separately visible
→ artifact-serviceability applicability remains unresolved unless a real exact target-wheel-compatibility owner later supplies evidence
```

This is not incomplete reasoning; it is an explicit epistemic boundary.

### Decision 9 — old-release acquisition belongs in the artifact candidate branch, not the upstream semantic branch

The existing proposed `package_result` serves both package evidence and upstream repository resolution. Once the proposed release is established, old-release acquisition should occur independently for artifact-serviceability candidate formation rather than being nested under upstream repository/changelog success.

Reason:

```text
artifact-serviceability package transition
```

is independent from:

```text
upstream repository + tagged changelog + Python-support semantics
```

A later upstream failure must not erase already-earned old/proposed package artifact evidence or candidate state.

## Remaining design questions deferred to their owning slices

These do not block the first typed-contract edit:

1. Which exact workflow/source pairs should be interpreted in the target-environment slice so the application does not collect irrelevant target state merely because a workflow exists?
2. Should a future dedicated exact target wheel-compatibility transformation be admitted, and from what stronger evidence source?
3. What exact CLI labels/placement best distinguish candidate, partial static target evidence, unresolved compatibility, and established applicability?
4. Which optional context belongs in human-facing output versus remaining internal typed evidence?

## First Build slice — additive typed contract

The Build/Implement Skill and its Source Clarity application guidance were loaded before source mutation because this change introduces cross-file evidence associations and new typed states.

### Source change

Commit `602e6eecf399c75a21a922f423835a655154e676` (`feat: add artifact integration result contract`) changed only `src/upgradepilot/investigation.py`.

Added:

- `DependencySourceArtifactEnvironmentResult`, an application-owned association between one `DependencySourceContext` and one `TargetArtifactEnvironmentResult`;
- `old_package_result: PackageReleaseResult | None`;
- `artifact_serviceability_candidate_result: ArtifactServiceabilityCandidateResult`;
- `target_artifact_environment_results: tuple[DependencySourceArtifactEnvironmentResult, ...]`;
- `artifact_serviceability_impact_result: ArtifactServiceabilityImpactAssessment | None`.

All new fields currently use inactive defaults. No old-release acquisition, candidate construction, target-environment interpretation, or artifact applicability orchestration was added in this slice.

The association docstring explicitly states that composition does not imply workflow execution, preserving the static/runtime proof boundary at the application surface.

### Focused test change

Commit `8056695bf2329cace5a85f01a705d9edc154975b` (`test: protect inactive artifact integration state`) changed only `tests/test_investigation.py`.

The existing durable dependency-problem stop test now proves that when no trusted dependency transition exists:

```text
old_package_result is None
artifact_serviceability_candidate_result is None
target_artifact_environment_results == ()
artifact_serviceability_impact_result is None
```

This is a durable branch invariant rather than a temporary test that would require the artifact path to remain inactive after valid dependency analysis.

### Diff inspection

GitHub commit inspection confirmed:

- the source commit contains only the intended imports, association type, additive fields, and module export;
- the test commit contains only the four new dependency-problem assertions;
- no unrelated source/test cleanup was batched.

### Executable validation limitation

The repository currently has no `.github/workflows` directory, and the latest commit has no GitHub Actions runs or commit statuses. The available GitHub connector exposes repository mutation/inspection but no direct Python test runner or workflow-dispatch route.

A local network clone was also unavailable in the execution environment because external DNS/network access is blocked there.

Therefore **the focused test family has not actually executed yet in this slice**. Do not record it as passing.

Current proof status is:

```text
source/test diff inspected and structurally bounded
+
no remote CI exists for the pushed commit
+
no available local repository runner
→ executable proof still pending
```

This validation limitation blocks declaring the typed-contract slice fully proven, but it does not justify broadening scope or guessing a pass result.

## Next bounded action

Remain inside the typed-contract Build slice until executable proof is available through an admitted repository execution path. If the normal project execution environment becomes available, run `tests/test_investigation.py` first and record the exact result.

After that focused proof passes, the next product slice is artifact-serviceability candidate composition:

```text
established proposed PackageReleaseEvidence
→ acquire exact old PackageReleaseResult
→ when both are evidence, call build_artifact_serviceability_impact_candidate
→ preserve provider problem / no-candidate / evidence-problem / candidate distinctly
→ create unresolved impact assessment only when a real candidate exists
```

Do not yet wire target artifact-environment acquisition or CLI rendering.

## Validation / evidence ledger

### Planning re-entry

Inspected:

- `AGENTS.md`
- `MEMORY.md`
- `OPERATING_GUIDE.md`
- `.agents/skills/upgradepilot-planning-design/SKILL.md`
- `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`
- `.agents/skills/upgradepilot-working-memory/SKILL.md`
- `plans/README.md`
- `working-memory/README.md`
- historical impact/applicability foundation plan, including its unfinished second-mechanism application-path responsibility
- `src/upgradepilot/impact/artifact_serviceability.py`
- `src/upgradepilot/target/artifact_environment.py`
- `src/upgradepilot/investigation.py`
- `src/upgradepilot/cli.py`
- `tests/test_investigation.py`
- package-interface protection test

Planning conclusion:

```text
existing components are independently present
+
normal application path does not compose them
+
remaining responsibility is coherent and multi-file
→ semantic bounded continuation plan is justified
```

### Slice 1 design evidence

Inspected directly:

- `tests/test_artifact_serviceability.py`
- `tests/test_target_artifact_environment.py`
- `tests/test_investigation.py`
- `src/upgradepilot/investigation.py`
- `src/upgradepilot/pypi/release.py`
- `src/upgradepilot/impact/artifact_serviceability.py`
- `src/upgradepilot/target/artifact_environment.py`
- `src/upgradepilot/dependency/analysis.py`
- `src/upgradepilot/dependency/environment.py`
- `.agents/skills/upgradepilot-build-implement/SKILL.md`
- `.agents/skills/upgradepilot-build-implement/references/source-clarity-heuristics.md`
- `docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`

Result-contract conclusion:

```text
provider-owned exact old/proposed release results
+
domain-owned candidate result
+
application-owned dependency-source ↔ target-result association collection
+
domain-owned impact assessment
→ smallest current contract that preserves activation, cardinality, and proof boundaries
```

### Executable validation

Not yet executed. GitHub shows no workflow/status for the latest commit and no `.github/workflows` directory; the available local execution environment could not clone the repository because network access is unavailable.

## Progressive session log

- Result-contract/evidence-flow checkpoint completed from current source/tests.
- Current static Target artifact-environment evidence is confirmed insufficient for exact wheel compatibility; no static→exact compatibility transformation is admitted.
- First additive typed-contract source/test edit completed and diff-inspected.
- Executable proof for `tests/test_investigation.py` remains pending; do not advance the live responsibility past this proof boundary yet.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-build-implement`