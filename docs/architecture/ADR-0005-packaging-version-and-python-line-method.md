# ADR-0005 — Packaging Version and Python-Line Method

**Status:** Accepted  
**Date:** 2026-07-31  
**Owner:** Ali Rajabi  
**Scope:** PEP 440 dependency-version ordering and exact stable Python-line membership method  
**Controlling plan:** [`../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`](../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md)  
**Parent plan:** [`../../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)

## Context

The selected responsibilities need two standards-correct operations:

1. establish valid forward Python-package version intervals and deterministic crossed-release ordering;
2. determine whether a target `requires-python` specifier admits any stable exact `X.Y.Z` version in one Python major/minor line.

A home-grown general PEP 440 parser would duplicate a complex interoperability standard. A fixed patch-number search would not prove line membership.

## Decision

### 1. Use `packaging` as the bounded standards dependency

Admit:

```text
packaging>=26.2,<27
```

The selected public methods are:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
SpecifierSet.is_unsatisfiable()
SpecifierSet.contains(..., prereleases=False)
```

The lower bound guarantees the selected API; the upper bound prevents silent adoption of a later major/calendar-version boundary without review.

### 2. Preserve raw and parsed dependency-version identity separately

Raw version strings remain source evidence. Parsed `Version` objects provide standards-based semantic comparison.

The method must distinguish at least:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

PEP 440-equivalent raw strings are not silently treated as a meaningful forward update.

### 3. Order only already selected crossed-release candidates

Release discovery/authority is outside this ADR.

Given candidate release identities, parse them with `Version`, require the admitted interval `old < candidate <= proposed`, require the exact raw proposed identity, reject PEP 440-equivalent duplicate raw identities, and sort deterministically by parsed value while preserving raw identity.

### 4. Define the Python-line question narrowly

For canonical line `X.Y`, ask:

> Does the target declaration admit at least one stable public PEP 440 version with exactly three release components `X.Y.Z`, where `Z` is a non-negative integer?

This is declaration mathematics. It does not prove publication by a Python implementation or actual CI/runtime use.

### 5. Use boundary-complete witness derivation, not arbitrary enumeration

Parse the declaration with `SpecifierSet` and reject contradictory sets with `is_unsatisfiable()`.

For supported specifier forms on a fixed `X.Y.Z` integer-patch domain, derive a finite candidate witness set:

```text
candidate patches = {0}

for each admitted stable boundary in line X.Y:
    include Z - 1, Z, Z + 1
    discard negative values
```

Evaluate exact stable witnesses through:

```python
target.contains(Version("X.Y.Z"), prereleases=False)
```

The reason this is complete for the admitted grammar is that truth can change only at or around the finite set of stable public boundaries/exclusions represented by those specifiers. Patch `0` covers the initial region; boundary neighborhoods cover subsequent regions. High patch values are reached directly rather than by iterating to a ceiling.

Return the checked candidate set and an exact witness when one exists so the result is auditable.

### 6. Supported and unsupported specifier forms

Supported operators:

```text
< <= > >= == != ~=
```

Prefix wildcard equality/exclusion such as `==3.9.*` and `!=3.9.*` are admitted.

The first exact stable-line method explicitly abstains on forms whose semantics do not map cleanly to this question, including:

- arbitrary equality `===`;
- epochs;
- local versions;
- prerelease/dev/post-release versions;
- more than three public release components.

These forms are not declared invalid PEP 440; they are unsupported for this narrower product meaning.

Malformed, unsupported, contradictory, and ordinary non-overlap remain different outcomes.

## Alternatives considered

### Home-grown PEP 440 parser

Rejected because it duplicates a maintained interoperability standard without product advantage.

### Fixed patch enumeration

Rejected because no arbitrary ceiling proves an entire Python line.

### Check only `X.Y.0`

Rejected because declarations such as `>=3.9.7` still overlap the 3.9 line.

### Use broad satisfiability as the whole line answer

Rejected because general PEP 440 satisfiability can be established by values outside the exact stable three-component `X.Y.Z` meaning selected here.

### Sample convenient versions

Rejected because unprincipled samples can miss high boundaries and exact-exclusion runs.

### Require an interpreter publication catalog now

Rejected because publication authority is a separate responsibility from declaration mathematics.

### Admit every valid PEP 440 form immediately

Rejected because unusual valid forms do not all map responsibly to the first exact stable-line question.

### Exact pin or unbounded dependency range

Rejected. Compatible 26.x fixes should remain installable, while a future major/calendar series requires explicit review.

## Consequences

### Benefits

- standards-based parsing/comparison;
- no arbitrary patch ceiling;
- narrow auditable product meaning;
- explicit witness evidence;
- raw identity stays separate from parsed semantics;
- unsupported semantics abstain instead of being guessed;
- one bounded maintained dependency replaces substantial custom parsing risk.

### Costs

- `packaging` becomes a runtime dependency;
- UpgradePilot owns a small product-specific boundary-candidate algorithm;
- valid but unusual PEP 440 forms may remain unsupported;
- the result does not prove actual interpreter publication;
- the `<27` bound requires future review.

## Reversibility

Keep the method behind small domain results, preserve raw inputs and checked witnesses, and keep target-relevance mapping outside this method. A replacement may remove `packaging` only after equivalent controlled behavior is proven.

## Reassessment triggers

Reassess when:

- a later `packaging` series changes selected APIs/semantics;
- a real supported case requires an excluded PEP 440 form;
- evidence demonstrates a truth change outside the derived boundary neighborhoods for an admitted form;
- the product must prove actual published interpreter releases;
- release ordering requires non-PEP-440 identities;
- the governing interoperability semantics materially change.

## Proof boundary

The controlling plan and tests own the detailed proof matrix. Evidence must at minimum discriminate invalid/equivalent/backward package intervals, exact raw identity preservation, supported/unsupported specifier forms, contradiction versus non-overlap, high patch boundaries without enumeration, wildcard/exclusion behavior, and auditable witness results.

Acceptance of this ADR authorizes the method. It does not prove implementation or learner mastery.
