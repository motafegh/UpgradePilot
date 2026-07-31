# ADR-0005 — Packaging Version and Python-Line Method

**Status:** Accepted  
**Date:** 2026-07-31  
**Owner:** Ali Rajabi  
**Stage:** B2 — Public PR vertical slice  
**Controlling plan:** [`../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`](../../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md)  
**Parent plan:** [`../../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)

## Context

UpgradePilot now preserves exact raw dependency-version transitions and can ground one upstream Python support-drop claim against exact crossed-interval authority.

The next responsibilities require two forms of standards-correct reasoning:

1. determine whether raw Python package versions form a valid forward PEP 440 interval and order crossed releases;
2. determine whether a target `requires-python` declaration admits any stable exact three-component version in one Python major/minor line.

A home-grown general PEP 440 parser or arbitrary patch enumeration would duplicate packaging standards incompletely and create hidden boundary errors.

The target method must:

- preserve raw version evidence;
- use maintained PEP 440 parsing and comparison;
- distinguish invalid, equivalent, and backwards dependency intervals;
- order crossed release versions deterministically;
- parse compound `requires-python` specifiers;
- support wildcard, exclusion, compatible-release, and patch-boundary cases;
- reject semantic forms outside the first stable-line model;
- prove exact `X.Y.Z` existence without an arbitrary patch ceiling;
- remain separate from target-relevance state mapping and CLI behavior.

## Decision

### 1. Add `packaging` as a bounded runtime dependency

Add:

```text
packaging>=26.2,<27
```

Reasons:

- `packaging.version.Version` implements maintained PEP 440 version parsing and ordering;
- `packaging.specifiers.SpecifierSet` implements maintained version-specifier parsing;
- `SpecifierSet.is_unsatisfiable()` identifies contradictory declarations;
- `SpecifierSet.contains(..., prereleases=False)` evaluates exact stable witness versions;
- `is_unsatisfiable()` was introduced in 26.1;
- 26.2 is the current stable release when this decision is recorded and includes the documented method plus subsequent fixes;
- `<27` requires explicit review before adopting a future calendar-version series.

The bound is intentionally neither unbounded nor exact-pinned:

```text
>=26.2
→ guarantees the selected documented methods

<27
→ allows compatible 26.x fixes
→ prevents silent adoption of an unreviewed 27.x method boundary
```

### 2. Preserve raw and parsed dependency versions separately

Create a parsed interval record containing:

```text
DependencyReleaseInterval
+ parsed old Version
+ parsed proposed Version
```

Raw strings remain authoritative evidence identities. Parsed `Version` objects supply standards-based semantic comparison.

Required failures:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

PEP 440-equivalent raw strings are not silently treated as a meaningful update.

### 3. Order only already selected crossed-release candidates

Step 3 does not discover releases.

A future acquisition stage supplies exact raw release version strings. The method:

- parses every candidate;
- requires old < candidate <= proposed;
- requires the exact raw proposed version;
- rejects PEP 440-equivalent duplicate raw identities;
- sorts by parsed `Version`;
- preserves corresponding raw and parsed tuples.

This produces deterministic ordering without assigning source authority.

### 4. Define the first Python-line question exactly

For canonical line `X.Y`, ask:

> Does the target declaration admit at least one stable public PEP 440 version with exactly three release components `X.Y.Z`, where `Z` is a non-negative integer?

This is declaration mathematics. It does not prove that the witness version was actually published by CPython, PyPy, or another implementation.

### 5. Use a boundary-complete witness method

Parse the target declaration with `SpecifierSet` and first reject contradictory declarations with `is_unsatisfiable()`.

Then derive a complete finite witness set from the admitted specifier boundaries:

```text
candidate patches = {0}

for each admitted boundary in the selected X.Y line:
    include Z - 1, Z, and Z + 1
    discard negative values
```

Construct only exact stable witnesses:

```text
Version("X.Y.Z")
```

Evaluate them through:

```python
target.contains(witness, prereleases=False)
```

The first admitted witness establishes method-level overlap. No admitted witness establishes method-level non-overlap.

### 6. Why the derived candidate set is complete

For the admitted grammar on a fixed exact `X.Y.Z` integer-patch domain, each specifier can change truth only:

- at its stable public boundary patch;
- immediately before or after that boundary;
- or nowhere inside the line for prefix-wide wildcard forms.

The truth of a conjunction can therefore change only at the union of those finite neighborhoods. Patch `0` samples the initial region, and `Z + 1` samples the region following each boundary. Exact exclusions are boundaries too, so a run of consecutive exclusions contributes the first patch after the run.

This is symbolic boundary analysis, not arbitrary enumeration. For `>=3.9.500000`, the method directly derives patch `500000`; it does not inspect patches `0` through `499999`.

### 7. Admit only specifier forms that map responsibly to exact `X.Y.Z`

Supported operators:

```text
< <= > >= == != ~=
```

Prefix wildcard equality and exclusion are admitted:

```text
==3.9.*
!=3.9.*
```

Reject for the first method:

- arbitrary equality `===`;
- epoch versions;
- local versions;
- prerelease versions;
- development releases;
- post releases;
- more than three public release components.

These are not declared invalid PEP 440. They are explicitly unsupported for the narrower exact stable interpreter-line meaning.

### 8. Separate malformed, unsupported, contradictory, and ordinary non-overlap

Required method problems:

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

A contradictory target declaration is not ordinary line exclusion. It is an unresolved declaration method problem.

### 9. Return a witness, not only a boolean

The method returns:

```text
PythonLineSpecifierEvaluation
├── exact input and normalized declaration
├── line bounds
├── candidate_versions_checked[]
├── witness_version: Version | None
└── contains_stable_release: bool
```

The witness makes the method auditable. It is not publication evidence.

Parent Step 4 later maps the result with a grounded support-drop claim and target evidence into:

```text
declared_python_overlap
outside_declared_python_range
or an explicit unresolved/unsupported relevance state
```

This ADR does not define compatibility, safety, merge, recommendation, or target acquisition behavior.

## Alternatives considered

### Home-grown general PEP 440 parser

Rejected. It would duplicate a complex interoperability standard, create long-term correctness risk, and provide no selected product advantage.

### Enumerate patch versions to a fixed ceiling

Rejected. No arbitrary ceiling proves an entire line. `>=3.9.500000` demonstrates the failure directly.

### Check only `X.Y.0`

Rejected. `>=3.9.7` overlaps Python 3.9 even though `3.9.0` does not satisfy it.

### Use raw `SpecifierSet.is_unsatisfiable()` on the broad line prefix

Rejected after implementation review. General PEP 440 satisfiability can be established by release tuples outside exact three-component `X.Y.Z`, so it is broader than the parent plan's product meaning.

### Sample several convenient versions

Rejected. Unprincipled sampling can miss high patch boundaries and runs of exact exclusions.

### Require a published interpreter-release catalog now

Rejected for Step 3. The current question concerns the mathematical declared range. Publication evidence would be a separate authority responsibility and is not needed to map the declaration conservatively.

### Permit every valid PEP 440 specifier immediately

Rejected. Epoch, local, prerelease, dev, post, overlong release, and arbitrary-equality semantics do not map cleanly to the first exact stable line question.

### Depend on `packaging>=26.1`

Rejected in favor of 26.2. Although 26.1 introduced `is_unsatisfiable()`, 26.2 is the current stable release at the decision boundary and includes subsequent fixes and documentation.

### Exact pin `packaging==26.2`

Rejected. Compatible 26.x fixes should remain installable without a governance change, while the `<27` upper bound preserves a review boundary.

### Unbounded `packaging>=26.2`

Rejected. Calendar-version changes should not silently alter the trusted method.

## Consequences

### Benefits

- standards-based version parsing and exact candidate evaluation;
- no arbitrary patch enumeration;
- exact three-component product meaning;
- an auditable witness when overlap exists;
- explicit unsupported semantics;
- raw evidence identity remains separate from parsed meaning;
- future Step 4 receives a small deterministic method result;
- one bounded runtime dependency replaces substantial custom parsing risk.

### Costs

- `packaging` becomes an installed runtime dependency;
- local editable environments must refresh dependencies after pulling the change;
- UpgradePilot owns a small boundary-candidate derivation algorithm;
- the initial grammar abstains on valid but unusual PEP 440 forms;
- the result does not prove actual interpreter release publication;
- the `<27` bound requires future review;
- `is_unsatisfiable()` is a recent public API and requires focused regression tests.

These costs are accepted because a narrow explicit standards dependency plus a bounded product-specific witness algorithm is preferable to either hidden broad semantics or incomplete enumeration.

## Reversibility

The decision is reversible by:

- keeping the method in one pure module;
- exposing small domain results instead of `packaging` behavior throughout the codebase;
- retaining raw version and specifier text;
- preserving checked candidates and witness evidence;
- keeping Step 4 mapping outside the method;
- removing the dependency and replacing the module only after equivalent controlled tests pass.

No persistence schema, external service, target mutation, or network behavior is introduced.

## Reassessment triggers

Reassess when:

- `packaging` 27.x changes the selected APIs or comparison behavior;
- a real case requires prerelease-only, epoch, local, dev, post, overlong release, or arbitrary-equality Python support semantics;
- a demonstrated admitted specifier changes truth somewhere outside the derived boundary neighborhoods;
- the product must prove actual published interpreter releases rather than mathematical declaration membership;
- target declarations use a valid excluded form often enough to block the product slice;
- release ordering requires non-PEP 440 identities;
- a standards body changes the meaning of `requires-python` or PEP 440 specifiers.

## Proof required

Controlled tests must prove:

- dependency metadata contains the exact selected bound;
- invalid, equivalent, and backwards dependency intervals remain distinct;
- crossed releases are ordered without losing exact raw identity;
- outside, invalid, equivalent, and missing-proposed candidates stop explicitly;
- all admitted specifier operators and wildcard cases behave as designed;
- patch boundaries are not reduced to `X.Y.0`;
- a high patch boundary is reached directly without a fixed ceiling;
- consecutive exact exclusions derive the first possible following witness;
- unsupported PEP 440 forms abstain explicitly;
- contradictory target declarations do not become ordinary non-overlap;
- the result preserves checked candidates and exact witness;
- importing `upgradepilot` remains network-free;
- the complete deterministic suite remains green.

## Learning note

This ADR introduces several terms that must be taught when reviewing implementation:

```text
PEP 440
Version
SpecifierSet
satisfiable / unsatisfiable
specifier boundary
symbolic candidate derivation
stable X.Y.Z witness
raw identity versus parsed semantic value
```

Approval of this ADR does not establish user mastery. Learning evidence requires later explanation, code tracing, and demonstrated reasoning.
