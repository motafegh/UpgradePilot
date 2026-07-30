# B2 Step 1 — Dependency Change Contracts Validation

**Local timestamp:** 2026-07-30 21:38 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Validate the committed Step 1 shared dependency-change contracts, preserve legacy dependency behavior, run the complete deterministic suite, and execute the installed public S004 control  
**Result:** Step 1 behavior validation passed; existing runtime behavior was preserved; Step 2 may be discussed as the next bounded implementation step

## Validated source position

The local shell showed the UpgradePilot checkout on `main`. At the time this evidence was recorded, repository `main` resolved to:

```text
60837a65883e1d21229e383ee47225839d49e951
Correct Step 1 learning state
```

The local command transcript did not separately capture `git rev-parse HEAD` or `git status --short`. Therefore the validated revision is recorded from the repository's current `main` position immediately after the supplied run, not from a separately printed local SHA.

No product source or test file changed during this validation operation.

## Interpreter and commands

The real repository checkout used the admitted project interpreter:

```text
Python 3.12.3
```

Commands executed:

```bash
python --version
python -m unittest tests.test_dependency_change_contracts -v
python -m unittest tests.test_dependency_change -v
python -m unittest discover -s tests -v
```

## Focused contract validation

Exact result:

```text
Ran 4 tests in 0.000s

OK
```

The passing focused tests established the currently implemented contract mechanics:

1. `DependencyFileEvidence` preserves path, format, acquisition method, revisions, blobs, and byte counts supplied to it;
2. `ExtractedDependencyVersionChange` preserves one file-level source record;
3. `DependencyVersionChange` preserves multiple supporting source records and limitations as tuples;
4. frozen field reassignment raises `FrozenInstanceError`;
5. tuple extension through `append` raises `AttributeError`;
6. the architecture-approved dependency problem vocabulary remains exact and ordered;
7. `DependencyChangeEvidenceProblem` preserves identified source evidence.

These tests validate record shape and mechanics. They do not establish parser, comparison, GitHub acquisition, or `uv.lock` behavior.

## Legacy dependency regression validation

Exact result:

```text
Ran 6 tests in 0.001s

OK
```

The existing dependency-change tests continued to pass for:

- one supported same-file exact `package==version` replacement;
- package-name normalization and identity agreement;
- explicit missing-patch abstention;
- incomplete-patch detection through GitHub edit-count disagreement;
- rejection of version-range changes;
- abstention when several pinned changes are present.

This proves that adding the Step 1 contracts did not change the current legacy parser behavior protected by these tests.

## Complete deterministic-suite validation

Exact result:

```text
Ran 76 tests in 0.022s

OK
```

The 76-test result is the complete suite count. The four focused and six legacy dependency tests are included in those 76 tests; they are not additional unique tests.

The full passing suite preserved the existing deterministic areas, including:

- public pull-request and changed-file acquisition contracts;
- exact-head GitHub Actions run, job, and workflow-definition evidence;
- bounded CI-authority classification;
- CLI orchestration and unsupported-stage stopping;
- exact-head target Python declaration evidence;
- PyPI package, release-file, and provenance contracts;
- upstream source and release resolution;
- shared JSON response contracts;
- workflow-command interpretation.

No failure, error, or skip was reported.

## Installed public S004 control

Authentication was explicitly removed before the command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The installed command completed successfully and returned exit status `0`.

Observed public identity:

```text
Repository: googlefonts/glyphsLib
PR: 1145
Title: Bump pytest from 9.0.2 to 9.0.3
Author: dependabot[bot]
State: closed
Merged: true
Base: main @ 044f19e4b1437bfc4343592486f4e3c6040306d9
Head: dependabot/pip/pytest-9.0.3 @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Changed-file records: 1
Changed file: requirements-dev.txt (modified)
```

Observed dependency identity:

```text
Dependency change: supported
Source file: requirements-dev.txt
Package: pytest
Old version: 9.0.2
Proposed version: 9.0.3
```

Observed exact-head target declaration evidence:

```text
Target Python declaration: project_table_absent
Target Python source: pyproject.toml @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Target Python blob SHA: 38d6a9efc4b94e2b733d3bbb848156449814ec94
Target Python detail: pyproject.toml did not contain a [project] table.
```

Observed exact-head CI evidence:

```text
Exact-head workflow runs: 2

Regression Tests
→ completed / success
→ one job
→ authority sufficient
→ requirements-dev.txt installed
→ pytest directly invoked

Test + Deploy
→ completed / success
→ six jobs
→ authority unresolved
→ multiple_or_zero_workflow_jobs
```

Overall CI result:

```text
CI authority: sufficient
CI authority reason: exact_head_dependency_exercised
```

Observed package and upstream evidence:

```text
Package evidence: available
Published package: pytest==9.0.3
Distribution files: 2

Upstream source: available
Upstream repository: pytest-dev/pytest
Provenance coverage: 2 of 2 files
Provenance unavailable files: none
Accepted tag: 9.0.3
Tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
Claim state: unresolved_claim
```

The anonymous run proves this public control succeeded without a token in this execution. It does not remove GitHub's anonymous rate limits or establish that all future unauthenticated runs will succeed.

## Behavior now established

For the validated source position, Step 1 establishes:

```text
shared dependency-evidence records and result aliases exist
+ focused record mechanics pass on Python 3.12.3
+ legacy exact-requirement behavior remains green
+ the complete deterministic suite remains green
+ the installed S004 public evidence chain remains intact
```

The current runtime remains:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

No new parser produces the Step 1 shared records yet.

## Learning state

A structured introductory teaching and guided source/test walkthrough occurred before validation. It covered:

- record and value-object meaning;
- `@dataclass` generated construction, representation, and equality;
- `frozen=True` and its shallow-immutability boundary;
- `slots=True` and fixed declared instance shape;
- list versus tuple behavior;
- `Literal` as static vocabulary rather than automatic runtime validation;
- success-or-problem union results and caller type narrowing;
- file-level extracted evidence versus PR-wide trusted evidence;
- the purpose and limits of the focused contract tests.

Current depth must be recorded as:

```text
structured introductory explanation completed
+ actual source and focused tests reviewed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

The user requested continuation without comprehension-check questions. Product behavior validation and learning mastery remain separate claims.

## Not established

This validation does not establish:

- an exact-requirement extractor returning `ExtractedDependencyVersionChange`;
- `compare_extracted_dependency_changes`;
- path-eligibility enforcement;
- generic exact base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` parsing or duplicate-group comparison;
- S001 dependency identity through the product;
- migration of CLI, CI, workflow-command, or output contracts;
- `packaging` admission or PEP 440 runtime validation;
- Python-support relevance;
- compatibility, objective safety, or maintainer action;
- production readiness;
- mastery of the Step 1 Python concepts.

## Step 1 closure and exact continuation

Step 1 is now **behavior-validated** for the current committed contract layer and preserved legacy runtime.

The next bounded step from the selected plan is Step 2:

```text
move the existing exact-requirement extraction behavior
into a dedicated exact_requirement_change.py module
without changing validated behavior
```

Before implementation, Step 2 should be discussed through a focused source and caller review. The review must identify:

1. the exact functions and private helpers currently owned by `dependency_change.py`;
2. package exports and direct imports that must remain compatible;
3. the six existing dependency tests that define the behavior-preservation boundary;
4. which new shared result type Step 2 will return and which migration is intentionally deferred;
5. the stop line separating module extraction from path eligibility, PR-wide comparison, base/head acquisition, and `uv.lock` work.

Do not begin those later features during Step 2.
