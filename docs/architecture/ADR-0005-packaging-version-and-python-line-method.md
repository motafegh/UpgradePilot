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
2. determine whether a target `requires-python` declaration admits any stable release in one Python major/minor line.

A home-grown parser or finite patch enumeration would duplicate packaging standards incompletely and create hidden boundary errors.

The target method must:

- preserve raw version evidence;
- use maintained PEP 440 parsing and comparison;
- distinguish invalid, equivalent, and backwards dependency intervals;
- order crossed release versions deterministically;
- parse compound `requires-python` specifiers;
- support wildcard, exclusion, compatible-release, and patch-boundary cases;
- reject semantic forms outside the first stable-line model;
- avoid arbitrary finite patch enumeration;
- remain separate from target-relevance state mapping and CLI behavior.

## Decision

### 1. Add `packaging` as a bounded runtime dependency

Add:

```text
packaging>=26.2,<27
```

Reasons:

- `packaging.version.Version` implements maintained PEP 440 version parsing and ordering;
- `packaging.specifiers.SpecifierSet` implements maintained version-specifier parsing and intersection;
- `SpecifierSet.is_unsatisfiable()` supplies the complete range-satisfiability operation needed by the selected non-enumerative line method;
- `is_unsatisfiable()` was introduced in 26.1;
- 26.2 is the current stable release when this decision is recorded and includes the documented method plus subsequent fixes;
- `<27` requires an explicit review before adopting a future calendar-version series.

The bound is intentionally neither unbounded nor exact-pinned:

```text
>=26.2
→ guarantees the selected documented method

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

### 4. Define a Python support line as a stable major/minor interval

For canonical line `X.Y`, define:

```text
>=X.Y,<X.(Y+1)
```

This is a product meaning owned by UpgradePilot. `packaging` owns parsing, comparison, intersection, and satisfiability.

The method asks:

> Is the intersection of the target declaration and the stable Python-line interval satisfiable under the admitted specifier forms?

### 5. Use intersection plus `is_unsatisfiable()`

The selected algorithm is:

```python
line = SpecifierSet(">=X.Y,<X.(Y+1)")
target = SpecifierSet(requires_python)
intersection = target & line
contains_stable_release = not intersection.is_unsatisfiable()
```

This does not enumerate `X.Y.0`, `X.Y.1`, or any finite patch set.

### 6. Admit only specifier forms that map responsibly to a stable line

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
- post releases.

These are not declared invalid PEP 440. They are explicitly unsupported for the narrower stable interpreter-line meaning.

### 7. Separate malformed, unsupported, contradictory, and ordinary non-overlap

Required method problems:

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

A contradictory target declaration is not ordinary line exclusion. It is an unresolved declaration method problem.

### 8. Keep relevance mapping outside this ADR

The method returns:

```text
contains_stable_release = true | false
```

Parent Step 4 later maps that result with a grounded support-drop claim and target evidence into:

```text
declared_python_overlap
outside_declared_python_range
or an explicit unresolved/unsupported relevance state
```

This ADR does not define compatibility, safety, merge, recommendation, or target acquisition behavior.

## Why satisfiability implies a stable release in the admitted scope

The line interval itself uses stable public boundaries.

Before intersection, UpgradePilot rejects target specifiers containing prerelease, dev, post, local, epoch, or arbitrary-equality forms. The remaining admitted operators describe stable public version ranges, exact stable versions, compatible-release ranges, and finite or prefix exclusions.

Under this bounded grammar, a satisfiable intersection with `>=X.Y,<X.(Y+1)` cannot rely solely on an excluded non-stable version class. Therefore the boolean is used as the method-level stable-line answer.

If future cases require prerelease-only interpreter support or other excluded semantics, the ADR must be reassessed rather than extending the meaning implicitly.

## Alternatives considered

### Home-grown PEP 440 parser

Rejected. It would duplicate a complex interoperability standard, create long-term correctness risk, and provide no selected product advantage.

### Enumerate patch versions

Rejected. No finite patch ceiling proves that an entire Python line is included or excluded. A declaration such as `>=3.9.500` would defeat an arbitrary enumeration bound.

### Check only `X.Y.0`

Rejected. `>=3.9.7` overlaps Python 3.9 even though `3.9.0` does not satisfy it.

### Use `SpecifierSet.contains()` on several sample versions

Rejected. Sampling is incomplete and can misclassify exclusions and patch boundaries.

### Permit every valid PEP 440 specifier immediately

Rejected. Epoch, local, prerelease, dev, post, and arbitrary-equality semantics do not map cleanly to the first stable Python support-line question.

### Depend on `packaging>=26.1`

Rejected in favor of 26.2. Although 26.1 introduced `is_unsatisfiable()`, 26.2 is the current stable release at the decision boundary and includes subsequent fixes and documentation.

### Exact pin `packaging==26.2`

Rejected. Compatible 26.x fixes should remain installable without a governance change, while the `<27` upper bound preserves a review boundary.

### Unbounded `packaging>=26.2`

Rejected. Calendar-version major changes should not silently alter the trusted method.

## Consequences

### Benefits

- standards-based version parsing and ordering;
- no finite patch enumeration;
- complete handling of compound admitted specifiers through one maintained range method;
- explicit unsupported semantics;
- raw evidence identity remains separate from parsed meaning;
- future Step 4 receives a small deterministic method result;
- one bounded runtime dependency replaces substantial custom parsing risk.

### Costs

- `packaging` becomes an installed runtime dependency;
- local editable environments must refresh dependencies after pulling the change;
- the initial stable-line grammar abstains on valid but unusual PEP 440 forms;
- the `<27` bound requires future review;
- `is_unsatisfiable()` is a relatively recent public API and therefore requires focused regression tests.

These costs are accepted because a narrow explicit standards dependency is preferable to hidden custom semantics.

## Reversibility

The decision is reversible by:

- keeping the method in one pure module;
- exposing small domain results instead of `packaging` behavior throughout the codebase;
- retaining raw version and specifier text;
- keeping Step 4 mapping outside the method;
- removing the dependency and replacing the module only after equivalent controlled tests pass.

No persistence schema, external service, target mutation, or network behavior is introduced.

## Reassessment triggers

Reassess when:

- `packaging` 27.x changes the selected APIs or satisfiability behavior;
- a real case requires prerelease-only, epoch, local, dev, post, or arbitrary-equality Python support semantics;
- `SpecifierSet.is_unsatisfiable()` produces a demonstrated false answer for an admitted form;
- target declarations use a valid specifier form excluded by this ADR often enough to block the product slice;
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
- no finite patch enumeration appears in the implementation;
- unsupported PEP 440 forms abstain explicitly;
- contradictory target declarations do not become ordinary non-overlap;
- importing `upgradepilot` remains network-free;
- the complete deterministic suite remains green.

## Learning note

This ADR introduces several terms that must be taught when reviewing implementation:

```text
PEP 440
Version
SpecifierSet
specifier intersection
satisfiable / unsatisfiable
stable Python line
raw identity versus parsed semantic value
```

Approval of this ADR does not establish user mastery. Learning evidence requires later explanation, code tracing, and demonstrated reasoning.
