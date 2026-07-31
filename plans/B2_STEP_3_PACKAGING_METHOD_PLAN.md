# B2 Target Python Relevance Step 3 — Packaging Method Plan

**Owner:** Ali Rajabi  
**Parent plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Previous completed step:** [`B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md`](B2_STEP_2_SUPPORT_DROP_CLAIM_CONTRACT_PLAN.md)  
**Status:** Controlling implementation plan

## Purpose

Freeze the standards-based version and specifier method required by later target-Python relevance work.

This step owns two lower-level responsibilities:

```text
raw dependency release versions
→ validated PEP 440 ordering and crossed-release sequence

canonical Python line X.Y
+ textual requires-python declaration
→ deterministic stable-line overlap method
```

It does not yet map a grounded support-drop claim and target declaration into the final relevance states. That domain mapping remains parent Step 4.

## Runtime dependency decision

Add one runtime dependency:

```text
packaging>=26.2,<27
```

Rationale:

- `packaging.version.Version` supplies maintained PEP 440 parsing and comparison;
- `packaging.specifiers.SpecifierSet` supplies maintained specifier parsing;
- `SpecifierSet.is_unsatisfiable()` supplies a non-enumerative intersection test;
- version 26.1 introduced `is_unsatisfiable()`;
- 26.2 is the current stable release at this decision date and contains the documented API and subsequent fixes;
- `<27` prevents an unreviewed future calendar-version series from silently changing the admitted method.

Record the dependency and algorithm in an accepted ADR before product integration.

## Responsibility boundary

### Owned here

- exact dependency bound in `pyproject.toml`;
- PEP 440 parsing of raw old and proposed dependency versions;
- explicit invalid, equivalent, and non-forward interval results;
- ordering of already identified crossed-release version strings;
- exact raw and parsed version preservation;
- canonical Python `X.Y` line parsing;
- `requires-python` specifier parsing;
- accepted and unsupported specifier forms;
- stable-line overlap through specifier intersection and unsatisfiability;
- controlled tests and package exports.

### Not owned here

- GitHub or PyPI acquisition;
- release/tag enumeration;
- changelog path discovery;
- support-drop semantic extraction;
- target evidence acquisition;
- mapping to `declared_python_overlap`, `outside_declared_python_range`, or other relevance states;
- CLI orchestration;
- compatibility, safety, merge, or recommendation conclusions.

## Part A — Dependency release interval method

### Input

```text
DependencyReleaseInterval
├── package
├── normalized_package
├── old_version raw text
└── proposed_version raw text
```

### Parsed result

```text
ParsedDependencyReleaseInterval
├── interval
├── old_version: packaging.version.Version
└── proposed_version: packaging.version.Version
```

Preserve the raw interval and parsed objects separately.

### Required states

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

Rules:

1. parse both raw strings with `Version`;
2. invalid old or proposed text produces `invalid_python_package_version`;
3. PEP 440-equivalent bounds such as `1.0` and `1.0.0` produce `equivalent_python_package_versions`;
4. proposed less than old produces `dependency_version_not_forward`;
5. only strict forward intervals produce a parsed result.

Do not erase the original `DependencyReleaseInterval` when parsing fails.

## Part B — Crossed-release ordering method

### Input

```text
ParsedDependencyReleaseInterval
+ sequence of exact raw release version strings already selected as interval candidates
```

This method does not acquire or discover releases. The future acquisition stage must supply the candidate sequence.

### Successful result

```text
OrderedCrossedReleaseVersions
├── interval
├── ordered_raw_versions[]
└── ordered_versions[]
```

Rules:

- parse every candidate with `Version`;
- every candidate must satisfy old < candidate <= proposed;
- the exact raw proposed version must be present;
- no two raw candidates may be PEP 440-equivalent;
- sort by parsed `Version`;
- the exact proposed raw version must be final after sorting;
- preserve raw strings and parsed objects in corresponding positions.

### Problem states

```text
invalid_crossed_release_version
crossed_release_outside_interval
equivalent_crossed_release_versions
proposed_release_missing
```

Do not silently select one of two equivalent raw identities.

## Part C — Stable Python-line specifier method

### Canonical line

Only exact non-negative major/minor text is admitted:

```text
X.Y
```

Examples:

```text
3.8   admitted
3.10  admitted
03.8  invalid
3.8.1 invalid
```

### Exact line interval

For line `X.Y`, construct:

```text
>=X.Y,<X.(Y+1)
```

This interval represents all public stable releases in that Python major/minor line under the admitted method.

### Target declaration parsing

Parse the exact `requires-python` text with:

```text
packaging.specifiers.SpecifierSet
```

The text must be non-empty and syntactically valid.

### Supported specifier operators

```text
<
<=
>
>=
==
!=
~=
```

`==` and `!=` prefix wildcards such as `3.9.*` are admitted.

### Explicit unsupported forms

Return `unsupported_requires_python_specifier` when any individual specifier uses:

- arbitrary equality `===`;
- an epoch;
- a local version;
- a prerelease;
- a development release;
- a post release.

These forms are valid PEP 440 in some contexts, but the first stable Python-line method does not map them to a support line responsibly.

### Contradictory declaration

A syntactically valid target specifier that is itself unsatisfiable returns:

```text
unsatisfiable_requires_python_specifier
```

It must not be reported as ordinary non-overlap.

### Non-enumerative overlap algorithm

```text
target = SpecifierSet(requires_python)
line = SpecifierSet(">=X.Y,<X.(Y+1)")
intersection = target & line

contains_stable_release = not intersection.is_unsatisfiable()
```

No finite list of patch releases may be generated.

The stable-release inference is bounded by the admitted forms: all prerelease, dev, post, local, epoch, and arbitrary-equality forms are rejected before intersection. Therefore a satisfiable intersection cannot depend solely on one of those excluded version classes.

### Result

```text
PythonLineSpecifierEvaluation
├── python_line
├── requires_python raw text
├── normalized_requires_python
├── line_lower_bound
├── line_upper_bound
└── contains_stable_release: bool
```

### Problem states

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

Step 3 exposes the boolean method result only. Parent Step 4 owns its relevance-state meaning.

## Controlled tests

Tests must prove at least:

### Dependency interval

- valid forward versions;
- invalid old and proposed versions;
- equivalent raw forms;
- backwards update;
- prerelease-to-final ordering remains PEP 440-valid.

### Crossed-release ordering

- unsorted candidates become deterministic order;
- old bound excluded;
- proposed bound included and final;
- before-old and after-proposed candidates rejected;
- invalid candidates rejected;
- equivalent raw candidate identities rejected;
- missing exact proposed release rejected.

### Python-line overlap

- `>=3.9` overlaps 3.9;
- `>=3.9.7` overlaps 3.9;
- `>=3.10` excludes 3.9;
- `!=3.9.*` excludes the entire 3.9 line;
- `>=3.8,<3.10` overlaps 3.9;
- wildcard equality and exclusion;
- compatible-release operators;
- exact patch inclusions and exclusions;
- compound contradictory intersection;
- invalid syntax;
- empty text;
- arbitrary equality;
- prerelease, dev, post, local, and epoch forms;
- contradictory target declaration;
- invalid Python-line text.

Tests must prove the implementation calls the maintained range method rather than enumerating patch releases.

## Required files

```text
docs/architecture/ADR-0005-packaging-version-and-python-line-method.md
src/upgradepilot/packaging_method.py
tests/test_packaging_version_method.py
tests/test_python_line_specifier_method.py
```

Update:

```text
pyproject.toml
src/upgradepilot/__init__.py
tests/test_package_interface.py
```

## Stop line

Stop Step 3 when:

```text
raw release versions
→ validated PEP 440 interval/order or explicit problem

canonical Python line + requires-python
→ stable-line overlap boolean or explicit problem
```

and focused plus complete deterministic suites pass.

Do not proceed during this step into:

- final target relevance result types;
- model or Instructor integration;
- upstream network acquisition;
- conditional target acquisition;
- CLI output changes;
- compatibility, safety, or action logic.
