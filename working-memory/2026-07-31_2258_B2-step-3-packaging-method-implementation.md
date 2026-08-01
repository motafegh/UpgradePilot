# B2 Target Python Relevance Step 3 — Packaging method implementation

**Recorded:** 2026-07-31 22:58 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](../plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Focused Step 3 plan:** [`../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md`](../plans/B2_STEP_3_PACKAGING_METHOD_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md`](../docs/architecture/ADR-0005-packaging-version-and-python-line-method.md)  
**Status:** Implemented; deterministic repository validation required

## Previous validated boundary

Step 2 support-drop claim grounding is complete and behavior-validated.

Validation record:

```text
working-memory/2026-07-31_2258_B2-step-2-support-drop-claim-contract-validation.md
```

Validated upstream semantic input:

```text
GroundedPythonSupportDropClaim
```

## Latest Step 3 product/test revision

```text
52d56773342f5dfe31c41fb0e39e58cc745ef5bf
Test installed packaging runtime version
```

Later implementation-record and memory commits do not alter this source/test boundary.

The GitHub connector reported no combined commit statuses for this revision. No Step 3 test pass is claimed here.

## Runtime dependency decision

Added to `pyproject.toml`:

```text
packaging>=26.2,<27
```

The bound follows ADR-0005:

- `Version` owns PEP 440 version parsing and ordering;
- `SpecifierSet` owns specifier parsing and exact candidate evaluation;
- `is_unsatisfiable()` identifies contradictory target declarations;
- 26.2 is the current stable release at the decision boundary;
- `<27` preserves an explicit future review boundary.

## Added module

```text
src/upgradepilot/packaging_method.py
```

The module is pure. It performs no network request and does not map results to final target-relevance states.

## Dependency interval parsing

Created:

```text
ParsedDependencyReleaseInterval
├── interval: exact raw DependencyReleaseInterval
├── old_version: packaging.version.Version
└── proposed_version: packaging.version.Version
```

Created:

```text
parse_dependency_release_interval
```

Problems:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

Raw version strings remain preserved even when semantic parsing fails.

## Crossed-release ordering

Created:

```text
OrderedCrossedReleaseVersions
├── interval
├── ordered_raw_versions[]
└── ordered_versions[]
```

Created:

```text
order_crossed_release_versions
```

The method:

- accepts only already selected candidate releases;
- parses every exact raw identity with `Version`;
- requires old < release <= proposed;
- rejects PEP 440-equivalent duplicate raw identities;
- requires the exact raw proposed version;
- sorts by parsed meaning;
- preserves raw and parsed tuples in corresponding order.

Problems:

```text
invalid_crossed_release_version
crossed_release_outside_interval
equivalent_crossed_release_versions
proposed_release_missing
```

## Exact stable Python-line method

Created:

```text
PythonLineSpecifierEvaluation
├── python_line
├── requires_python
├── normalized_requires_python
├── line_lower_bound
├── line_upper_bound
├── candidate_versions_checked[]
├── witness_version
└── contains_stable_release
```

Created:

```text
evaluate_python_line_specifier
```

The method asks whether one exact stable public three-component PEP 440 version exists:

```text
X.Y.Z
Z >= 0
```

It does not claim that the witness was published by a Python implementation.

## Boundary-complete witness derivation

The first implementation used broad `SpecifierSet` intersection satisfiability. Review rejected that as wider than exact `X.Y.Z`, because general PEP 440 satisfiability may use longer release tuples.

The corrected method:

1. parses the target `SpecifierSet`;
2. rejects unsupported forms;
3. reports a globally contradictory declaration through `is_unsatisfiable()`;
4. starts with patch candidate `0`;
5. derives `Z - 1`, `Z`, and `Z + 1` from every admitted boundary inside the selected line;
6. constructs only exact `Version("X.Y.Z")` witnesses;
7. tests each with `target.contains(..., prereleases=False)`;
8. returns the first witness or explicit method-level non-overlap.

The candidate set has no fixed ceiling. A boundary such as `>=3.9.500000` directly derives patch `500000` rather than scanning preceding patches.

## Admitted and unsupported specifiers

Supported operators:

```text
< <= > >= == != ~=
```

Supported wildcard prefix forms:

```text
==X.Y.*
!=X.Y.*
```

Explicitly unsupported:

```text
=== arbitrary equality
epoch
local version
prerelease
development release
post release
more than three public release components
```

Problems:

```text
invalid_python_line
invalid_requires_python_specifier
unsupported_requires_python_specifier
unsatisfiable_requires_python_specifier
```

## Public package interface

Exported:

```text
OrderedCrossedReleaseVersions
PackagingVersionProblem
ParsedDependencyReleaseInterval
PythonLineSpecifierEvaluation
PythonLineSpecifierProblem
order_crossed_release_versions
parse_dependency_release_interval
evaluate_python_line_specifier
```

Importing `upgradepilot` remains network-free.

## Controlled tests

Added:

```text
tests/test_packaging_version_method.py: 13 tests
tests/test_python_line_specifier_method.py: 34 tests
tests/test_runtime_dependency_contract.py: 2 tests
```

Updated:

```text
tests/test_package_interface.py: 1 new Step 3 test
```

Expected complete deterministic total:

```text
250 tests
```

Expected focused invocation includes all five package-interface tests:

```text
54 tests
```

These are derived counts, not observed passing results.

## Validation environment requirement

The editable environment must refresh project dependencies before testing:

```bash
python -m pip install -e .
```

The runtime dependency contract checks both:

```text
pyproject.toml contains packaging>=26.2,<27
installed packaging version is >=26.2 and <27
```

This avoids a confusing later failure from an old editable environment still using `packaging` 25.x.

## Explicit exclusions preserved

Step 3 does not:

- map the boolean/witness into final relevance states;
- combine a grounded claim with target evidence;
- acquire release indexes, tags, changelog files, or metadata;
- run an LLM or Instructor;
- modify the CLI;
- reorder target acquisition;
- establish interpreter release publication;
- infer compatibility, safety, merge, or recommendation outcomes.

No S001 or S004 repetition is required because their active command paths were unchanged.

## Validation required

Run from the real checkout:

```bash
git switch main
git pull --ff-only
python -m pip install -e .

python -m unittest \
  tests.test_packaging_version_method \
  tests.test_python_line_specifier_method \
  tests.test_runtime_dependency_contract \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v
```

Expected:

```text
focused: Ran 54 tests / OK
complete: Ran 250 tests / OK
```

## Stop line

Step 3 remains open until both suites pass.

After validation, proceed to parent Step 4:

```text
GroundedPythonSupportDropClaim
+ TargetPythonDeclaration
→ deterministic relevance result
```

Do not begin model integration, upstream network acquisition, conditional CLI orchestration, or end-to-end S001 work during Step 3 closure.

## Learning state

Concepts introduced and implemented:

- PEP 440 raw versus parsed identity;
- equivalent and non-forward version intervals;
- deterministic crossed-release ordering;
- `SpecifierSet` syntax versus product support semantics;
- contradictory declarations;
- exact stable `X.Y.Z` product meaning;
- symbolic boundary candidate derivation;
- witness evidence versus publication evidence.

Current depth:

```text
structured explanation completed
+ focused plan and ADR created
+ tests written before implementation
+ implementation completed
+ broad satisfiability design reviewed and corrected
but
repository execution not yet observed
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.
