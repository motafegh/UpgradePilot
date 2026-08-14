# 2026-08-14 Main Sync and Learning Orientation

**Learning branch:** `learning/real-case-code-flows-2026-08-12`  
**Previous product baseline:** `main@7a177a585fb8dcf0ed4c6af295ca93d975b11c85`  
**Current synchronized product baseline:** `main@8c1415e61aab4b16e80bb3f09ba7fb9a77b54ae1`  
**Learning-branch sync merge:** `64971024740f8943533410c7d222606b7b4a97d5`

## Why this checkpoint exists

The learning branch was created while `main` continued implementation in parallel. Before beginning substantive learning work, `main` had advanced materially. This checkpoint preserves the exact pre-sync learning state, records the implementation changes that matter for learning, and establishes the current orientation without turning the learning workspace into a second live project tracker.

`MEMORY.md` on synchronized `main` remains the live-state authority.

## Preserved pre-sync learning state

Before this synchronization:

- the dedicated learning branch/workspace existed;
- `LEARNING_PLAN.md` and `LEARNING_TODO.md` existed;
- the broad learning-order override / prerequisite-recovery rule had been added;
- no substantive code-flow lesson had started yet;
- the previous nominal `CURRENT` item was the runtime-map orientation, but it had **not** been completed or partially claimed as learned.

Therefore there is no unfinished technical lesson to reconstruct. Earlier learning tasks remain open and may be postponed or pulled in just-in-time as prerequisites.

## Synchronization result

Before synchronization, the learning branch had six learning-only commits while `main` had advanced by 65 commits from the common baseline.

The sync was performed as a real merge preserving both histories:

```text
learning history
        \
         64971024740f8943533410c7d222606b7b4a97d5
        /
main@8c1415e61aab4b16e80bb3f09ba7fb9a77b54ae1
```

The merged tree uses current `main` for product/source/test/governance state and preserves only the three learning-workspace files that were unique to the learning branch at that moment.

After synchronization the learning branch is behind `main` by zero commits.

## Material implementation changes now available to learn

### 1. Artifact Serviceability Increment 2

The downstream target-applicability step is now implemented and verified at its bounded scope.

Current shape:

```text
ArtifactServiceabilityImpactCandidate
+ exact TargetWheelCompatibilityEvidence
→ compare old published tags with target-supported tags
→ compare proposed published tags with target-supported tags
→ compose bounded candidate applicability
```

Important current concepts include:

- `TargetWheelCompatibilityEvidence`;
- `TargetWheelCompatibilityProblem`;
- `ArtifactServiceabilityImpactAssessment`;
- `evaluate_artifact_serviceability_impact(...)`;
- old published tags ∩ target-supported tags;
- proposed published tags ∩ target-supported tags;
- candidate applicability via the existing generic proposition/path/candidate composer.

A removed tag alone is not enough to establish target loss because a different proposed wheel may still serve the same target environment.

### 2. First real target artifact-environment interpretation slice

`src/upgradepilot/target/artifact_environment.py` is now implemented and verified at its bounded scope.

Current positive flow:

```text
strongly provenanced RepositoryTextFile
representing one GitHub Actions workflow
+ changed dependency source-file path
→ interpret_target_artifact_environment(...)
→ one statically readable job
→ literal runner fact when visible
→ literal actions/setup-python python-version fact when visible
→ direct visible changed-dependency installation evidence
→ TargetArtifactEnvironmentEvidence
```

The result preserves exact repository/revision/workflow/blob/job scope plus explicit limitations.

Its dependency-environment formation state is intentionally evidence-shaped:

```text
established
not_observed
```

`not_observed` means the bounded visible-command rule did not directly establish formation. It does **not** mean the dependency environment is proven absent.

The implementation deliberately leaves:

```text
exact_wheel_compatibility_state = "unresolved"
```

It does not yet derive exact `packaging.tags.Tag` sets and does not create `TargetWheelCompatibilityEvidence`.

### 3. Evidence-boundary pressure has become more concrete

The current supported responsibility before exact target wheel compatibility is:

```text
exact repository + immutable revision
→ one identified environment/job scope
→ proposition-specific repository evidence
→ partial provenance-carrying environment facts
→ exact wheel compatibility only when genuinely justified
→ otherwise explicit insufficient / unresolved
```

Important guards now visible in real code include:

```text
runner label + Python version != exact wheel tag set
CI/platform presence != affected dependency-environment formation
not directly observed != established absent
partial environment evidence != exact compatibility evidence
UpgradePilot local sys_tags() != remote target evidence
```

The first slice deliberately rejects or preserves explicit problem state for weak provenance, unsupported workflow paths, multiple/zero jobs, matrix jobs, reusable-workflow jobs, container jobs, and other ambiguous admitted shapes rather than guessing.

### 4. Product-simulation Cycle 02 additions

Cycle 02 material through S012 is now on `main`. These remain pressure/example evidence, **not our curriculum**. We will use S008/S011/S006/S007/S001 or newer cases only when they help discriminate a concept in current code.

## Current project learning emphasis from `MEMORY.md`

The current product-side learning checkpoint is the concrete positive target-environment flow:

```text
RepositoryTextFile
→ interpret_target_artifact_environment(...)
→ TargetArtifactEnvironmentEvidence
```

Then transfer-check the semantics, especially:

- `not_observed`;
- partial-fact preservation;
- exact provenance scope;
- unsupported/ambiguous shapes;
- why partial environment facts remain weaker than exact wheel compatibility.

Only after that should the next smallest proposition/evidence step toward `TargetWheelCompatibilityEvidence` be identified.

## Learning-plan impact

The broad `LEARNING_PLAN.md` remains valid as the method/guardrail document. Its own rules already state that:

- the sequence is navigation rather than a mandatory gate;
- current learning needs may jump ahead;
- state is preserved before jumps;
- prerequisites are recovered just in time;
- current source/tests and `MEMORY.md` outrank a frozen learning sequence.

Therefore the broad plan does not need to become a live-state document.

The operational `LEARNING_TODO.md` **does** need realignment because it previously treated Artifact Serviceability Increment 2 as future work. It is updated separately to reflect the synchronized current implementation.

## Recommended learning orientation after this sync

Unless Ali chooses another target, the highest-value current starting point is:

```text
Target Artifact Environment — positive concrete flow
```

This gives us the newest implemented code while naturally pulling in only the prerequisites actually needed:

- `RepositoryTextFile` provenance;
- GitHub Actions workflow/job structure;
- `actions/setup-python` literal evidence;
- direct dependency-environment formation evidence;
- observation vs inference vs absence;
- explicit limitation/problem states.

Earlier PR/dependency/CI/PyPI/Python-support lessons remain available and unchecked. They can be learned later or taught/re-taught just in time when required by the current flow.
