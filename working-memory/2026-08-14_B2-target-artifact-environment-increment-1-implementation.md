# B2 Target Artifact Environment — Increment 1 Implementation

**Date:** 2026-08-14  
**Type:** Dated implementation / verification working memory  
**Live-state authority:** `../MEMORY.md` only

## Entry state

Artifact Serviceability Increment 2 is verified complete at its bounded downstream scope given exact `TargetWheelCompatibilityEvidence`.

The adopted next responsibility was the first real target-side acquisition/interpretation slice:

```text
exact repository/revision workflow evidence
→ one statically readable GitHub Actions job
→ partial provenance-carrying environment facts
→ exact wheel compatibility only when genuinely justified
```

This increment implements only the partial-fact side of that boundary. It does **not** derive exact wheel tags.

## Source implementation

Implementation entered `main` through:

- `8ae9441cea9bae00f7bc3814f1569461dc13e90f` — initial bounded target artifact-environment evidence and tests;
- `9ee9af0faf7ba0d6d066d28332ef824d3e2a4b10` — tighten setup-python fact provenance;
- `a206ea6d355e0d4a135945dfb85b2abbcc89b856` — permanent regression guard for that provenance correction.

New source:

- `src/upgradepilot/target/artifact_environment.py`

New focused regression file:

- `tests/test_target_artifact_environment.py`

## Implemented evidence contract

`TargetArtifactEnvironmentEvidence` preserves:

- exact repository;
- immutable revision;
- workflow path and blob SHA;
- one statically identified job;
- literal `runs-on` fact when deterministically visible;
- literal `actions/setup-python` `with.python-version` fact when deterministically visible;
- direct visible installation of the changed dependency source file;
- explicit limitations for facts that are missing or dynamic;
- `exact_wheel_compatibility_state="unresolved"`.

The first formation state is deliberately evidence-shaped:

```text
established
not_observed
```

`not_observed` is not a claim that the dependency environment does not exist. It means the bounded visible-command rule did not directly establish formation in that scoped job.

## Supported and guarded behavior

Permanent focused tests currently cover:

1. literal runner + literal setup-python + direct changed-dependency installation → partial environment evidence with formation established;
2. runner/Python context without changed-dependency installation → formation `not_observed`, not a fabricated negative claim;
3. dynamic setup-python version → preserve known runner/formation facts while Python remains unresolved;
4. a `python-version` key outside setup-python's `with:` block is not accepted as setup-python evidence;
5. multiple jobs → explicit unsupported/problem state;
6. matrix job → explicit unsupported/problem state.

The implementation also rejects insufficient strong `RepositoryTextFile` provenance and unsupported workflow paths rather than silently accepting weaker identity.

## Critical semantic guards preserved

```text
runner label + Python version != exact wheel tag set
CI/platform presence != affected dependency-environment formation
not directly observed != established absent
partial evidence != exact compatibility evidence
```

No `TargetWheelCompatibilityEvidence` is created by this increment.

## Validation evidence

An earlier reconstructed assistant-side focused harness using the actual new module logic and a minimal `RepositoryTextFile` contract ran the six focused behaviors successfully:

```text
Ran 6 tests
OK
```

That result remains only assistant-side reconstructed evidence.

On 2026-08-14, Ali then pulled current `main` and reported that both requested real-repository verification commands completed green in the normal UpgradePilot WSL environment:

```text
python -m unittest discover -s tests -p 'test_target_artifact_environment.py' -v
python -m unittest discover -s tests
```

No exact test count or timing is recorded because only the green result was reported in this conversation.

GitHub reports no configured commit status checks for the implementation commit, so no remote CI result is inferred.

## Verification state

```text
source implementation: PRESENT
permanent focused regression coverage: PRESENT
assistant reconstructed focused smoke: GREEN
real repository focused suite: GREEN (user-reported WSL run)
full active suite: GREEN (user-reported WSL run)
nearest regression suite: not separately recorded
increment: VERIFIED COMPLETE AT ITS BOUNDED SCOPE
```

The verification proves the admitted partial target-environment interpretation behavior and regression compatibility of the current active suite. It does **not** prove exact wheel-tag derivation, matrix/reusable/container workflow support, or universal environment reconstruction.

## Next product step

Do **not** immediately manufacture exact tags or generalize to matrix/reusable/container workflows.

First transfer-check this concrete slice against the already-admitted anchors, especially S008, S011, Buildtest/C203, S006, S007, and S001. Then identify the smallest next proposition that can genuinely move partial target facts toward exact `TargetWheelCompatibilityEvidence` or justify remaining unresolved.
