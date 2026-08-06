# B2 Step 7F — Normal-Path Live S001 Proof

**Date:** 2026-08-05  
**Status:** Passed  
**Responsibility:** Final live proof for Step 7 bounded extractor/runtime integration and the parent Target Python Support Relevance slice.

## Reported deterministic gate

Ali reported the focused Step 7F/integration regressions and the complete active product regression green in WSL after the Homepage/provenance repository-association correction and the separate `PyPIReleaseIndexClient` orchestration correction.

Exact test counts were not supplied here, so this record does not invent them.

## Live command

```bash
time env -u GITHUB_TOKEN python -m upgradepilot pydantic/pydantic 13432 \
  | tee /tmp/upgradepilot-s001.txt
```

The command used the normal public CLI/application path. It did not use the scenario-specific Step 5 or Step 7C proof tools.

## Reacquired normal-path result

UpgradePilot established:

```text
target repository: pydantic/pydantic
PR: 13432
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
changed file: uv.lock
trusted dependency change: soupsieve 2.6 -> 2.8.4
```

Dependency evidence was derived from exact base/head `uv.lock` files.

### Independent CI branch

The exact-head CI branch acquired three workflow runs. The bounded dependency-exercise result remained:

```text
state: unresolved
reason: dependency_exercise_not_proven
```

Successful CI existed, but no admitted rule proved that those successful paths consumed and exercised the changed Soup Sieve dependency. This unresolved result did not block the separate upstream/target relevance branch and was not promoted into a safety or compatibility claim.

### Package and upstream repository authority

The normal product path established:

```text
published package: soupsieve==2.8.4
distribution files: 2
trusted upstream repository: facelessuser/soupsieve
provenance coverage: 2 of 2 files
provenance unavailable files: none
```

This validates the narrow repository-association correction learned during Step 7F: Soup Sieve's canonical GitHub repository is exposed by PyPI under `Homepage`, but product trust still requires canonical GitHub URL parsing plus exact-file PyPI publisher provenance and repository agreement.

### Crossed-release authority

The normal product path then established:

```text
upstream interval authority: available
authority basis: tagged_changelog
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
```

The package-wide release index was acquired through the dedicated `PyPIReleaseIndexClient`; this confirms the Step 7F wiring correction that separated exact-release acquisition from package-wide release-index acquisition.

### Live local semantic extraction and deterministic grounding

The active product path reached the adopted local LM Studio/Gemma semantic extractor and returned:

```text
upstream support-drop result: grounded
dropped Python line: 3.8
introduced in upstream release: 2.8
grounded source records: 1
```

The trusted result therefore remained the accepted chain:

```text
bounded authoritative crossed-release source window
→ local Gemma candidate extraction
→ deterministic exact-source reconstruction
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
```

The model did not own package/repository identity, release ordering, source authority, exact source coordinates, target relevance, compatibility, safety, or maintainer action.

### Conditional exact-head target activation

Only after the grounded upstream support-drop claim, the application acquired target Python metadata at the exact PR head:

```text
source: pyproject.toml @ aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
blob SHA: 8271997ab85caa1af522954812a2749784432dc7
requires-python: >=3.10
```

The deterministic relevance result was:

```text
outside_declared_python_range
```

with the bounded explanation that the target declaration admits no stable Python `3.8.Z` version under the accepted method.

## Live duration

Observed wall-clock duration reported by `time`:

```text
36.546 seconds
```

This duration includes the complete normal public CLI path, not only local model inference.

## What this proof establishes

The selected public proof now demonstrates through the active read-only product path:

```text
trusted dependency change
→ exact package/upstream repository authority
→ complete old-exclusive/proposed-inclusive crossed-release interval
→ exact tagged changelog authority
→ bounded local semantic candidate extraction
→ deterministic grounded Python support-drop claim
→ conditional exact-head target declaration acquisition
→ deterministic target-Python relevance
```

For S001 the bounded conclusion is:

> Soup Sieve's Python 3.8 support drop, introduced in 2.8, is outside Pydantic's declared `requires-python >=3.10` range at the exact PR head.

## What this proof does not establish

It does **not** establish that:

- the dependency update is objectively safe or universally compatible;
- CI coverage is sufficient for the dependency;
- no other upstream changes matter;
- the PR should be merged, deferred, or blocked;
- the model may authorize source selection, target relevance, or maintainer actions.

Those remain separate responsibilities.

## Closure classification

**Step 7F: passed.**

Because Steps 7A–7E already passed their bounded gates, Step 7 bounded extractor/runtime integration is complete.

The parent `B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md` completion condition is also satisfied for its admitted responsibility: the active read-only product path connects a trusted dependency change to authoritative crossed-release evidence, admits or rejects a bounded support-drop claim, conditionally inspects the exact target declaration, and returns an honest relevance/unresolved state with deterministic regression and selected live proof.

The next B2 responsibility is the position-neutral `B2_TRANSPARENT_DECISION_METHOD_PLAN.md`. No recommendation policy is activated by this closure record.
