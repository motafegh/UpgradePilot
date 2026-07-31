# B2 Step 3 — Dependency Comparison Validation

**Local timestamp:** 2026-07-31 16:35 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Validate Step 3 PR-wide dependency-change comparison, all prior dependency boundaries, the complete deterministic suite, and the installed S004 public regression control  
**Result:** Step 3 behavior validation passed; Step 4 may be discussed as the next bounded implementation step

## Validated source position

Immediately after the supplied local run, repository `main` resolved to:

```text
0b1e045ad18915fed59c34318cf482f0132d9112
Record Step 3 comparison implementation
```

The last product-source or test revision inside that `main` state was:

```text
fe3b1f7a07aeb2acbc0b76105ddc3cb09e131497
Test dependency change comparison
```

The later `0b1e045...` commit changed only `MEMORY.md`; it did not modify product source or tests.

The supplied transcript showed the local checkout on branch `main`, but did not separately include:

```text
git rev-parse HEAD
git status --short
python --version
```

Therefore this record binds the observed validation to repository `main` as resolved immediately after the run. The active `.venv` had previously reported Python 3.12.3 during Step 1 validation, but the exact interpreter output was not repeated in this transcript.

No product source or test file changed during this validation operation.

## Complete deterministic-suite validation

Observed result:

```text
Ran 92 tests in 0.021s

OK
```

The complete suite includes:

- 6 Step 3 dependency-comparison tests;
- 10 Step 2 exact-requirement tests;
- 6 legacy dependency-change tests;
- 4 Step 1 shared-contract tests;
- all existing GitHub, CI, CLI, target-Python, PyPI, provenance, upstream, JSON-contract, and workflow-command tests.

No failure, error, or skip was reported.

The passing suite establishes that the Step 3 comparator and export did not regress the deterministic behavior covered by the repository tests.

## Step 3 behavior now established

The public comparator is behavior-validated:

```text
compare_extracted_dependency_changes
```

Input:

```text
Sequence[DependencyChangeExtractionResult]
```

Output:

```text
DependencyVersionChange
or
DependencyChangeEvidenceProblem
```

Validated decision order:

```text
1. any explicit evidence problem blocks PR-wide trust
2. no extracted changes
   → no_supported_dependency_file
3. several normalized package identities
   → multiple_dependency_version_changes
4. one normalized package with different exact old/proposed transitions
   → conflicting_dependency_version_changes
5. equivalent extracted changes
   → one DependencyVersionChange with combined source evidence
```

Equivalent extracted changes require:

```text
same normalized package
+ same exact raw old-version string
+ same exact raw proposed-version string
```

The comparison layer preserves every unique `DependencyFileEvidence` record once in caller-provided order. It does not reparse files, acquire GitHub content, interpret `uv.lock`, perform PEP 440 validation, inspect CI, or decide compatibility or safety.

## Installed public S004 regression control

Observed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The command completed and preserved the established public evidence chain.

Pull-request identity:

```text
repository: googlefonts/glyphsLib
pull request: 1145
title: Bump pytest from 9.0.2 to 9.0.3
author: dependabot[bot]
state: closed
merged: true
base: main @ 044f19e4b1437bfc4343592486f4e3c6040306d9
head: dependabot/pip/pytest-9.0.3 @ f3cda8a94600e58d27f1bc17c99b7693718b6350
changed-file records: 1
```

Dependency evidence:

```text
source file: requirements-dev.txt
status: modified
package: pytest
old version: 9.0.2
proposed version: 9.0.3
```

Target-Python evidence:

```text
declaration: project_table_absent
source: pyproject.toml @ f3cda8a94600e58d27f1bc17c99b7693718b6350
blob SHA: 38d6a9efc4b94e2b733d3bbb848156449814ec94
```

Exact-head CI evidence:

```text
workflow runs: 2
Regression Tests: completed / success / 1 job
Test + Deploy: completed / success / 6 jobs
CI authority: sufficient
reason: exact_head_dependency_exercised
```

The sufficient path preserved visible installation of `requirements-dev.txt` and direct invocation of `pytest`. The second workflow remained unresolved because it contained multiple statically identified jobs.

Package and upstream evidence:

```text
published package: pytest==9.0.3
distribution files: 2
upstream repository: pytest-dev/pytest
provenance coverage: 2 of 2
provenance unavailable files: none
accepted tag: 9.0.3
tag object SHA: 24ec4b54c06a74721a285dcc317825b1735f4717
claim state: unresolved_claim
```

The anonymous command succeeded for this execution. GitHub anonymous rate limits still exist.

## What this validation proves

Established:

- the Step 3 comparator behaves according to its six focused proof obligations;
- one unopposed extracted change becomes one trusted PR-wide record;
- equivalent evidence combines source records;
- conflicting exact transitions remain explicit;
- several package changes remain explicit;
- recognized evidence problems cannot be hidden by convenient successful extraction;
- package-level import of `compare_extracted_dependency_changes` works in the complete suite;
- all prior deterministic repository tests remain green;
- the installed legacy S004 end-to-end product path remains unchanged.

Not established by this validation:

- CLI orchestration through the new file-level extraction and comparison flow;
- generic exact PR base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` extraction;
- duplicate `uv.lock` package-group comparison;
- S001 dependency identity through the installed product;
- constraints-file CI consumption semantics;
- migration to `DependencyVersionChange` in CLI and CI layers;
- PEP 440 runtime validation or ordering;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness.

## Learning depth recorded

This implementation and validation session introduced and reviewed:

- comparison layer versus extraction layer;
- comparison key;
- evidence aggregation;
- decision precedence;
- multiple-package versus conflicting-transition classification;
- representative readable package spelling versus normalized identity.

Current depth:

```text
structured explanation completed
+ source ownership and decision order reviewed
+ focused tests defined
+ complete-suite and installed-control execution observed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Step 3 closure

Step 3 is complete and behavior-validated.

The next selected-plan step is Step 4:

```text
generalize exact pull-request dependency-file acquisition
```

The next session should first discuss and inspect the existing repository-file acquisition code and its tests before modifying source.

Step 4 must remain limited to exact immutable base/head file acquisition and its evidence validation. Do not begin `uv.lock` parsing, CLI migration, PEP 440 work, Python-support relevance, or recommendation logic during Step 4.
