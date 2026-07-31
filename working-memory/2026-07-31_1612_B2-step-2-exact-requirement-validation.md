# B2 Step 2 — Exact Requirement Extraction Validation

**Local timestamp:** 2026-07-31 16:12 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Validate Step 2 exact-requirement module extraction, path eligibility, shared file-level results, legacy compatibility, the complete deterministic suite, and the installed S004 public control  
**Result:** Step 2 behavior validation passed; Step 3 may be discussed as the next bounded implementation step

## Validated source position

At the time this evidence was recorded, repository `main` resolved to:

```text
734c78e1b7754b14f2a8456fa415d3b714d24032
Record Step 2 implementation on main
```

The supplied local transcript showed the checkout on branch `main` but did not separately include:

```text
git rev-parse HEAD
git status --short
python --version
```

Therefore the validated revision is bound to repository `main` as resolved immediately after the supplied run. The exact interpreter version was not repeated in this Step 2 transcript; the same active `.venv` had previously reported Python 3.12.3 during Step 1 validation.

No product source or test file changed during this validation operation.

## Complete deterministic-suite validation

Observed result:

```text
Ran 86 tests in 0.021s

OK
```

The complete suite includes:

- 10 Step 2 exact-requirement tests;
- 6 legacy dependency-change tests;
- 4 Step 1 shared-contract tests;
- all existing GitHub, CI, CLI, target-Python, PyPI, provenance, upstream, JSON-contract, and workflow-command tests.

No failure, error, or skip was reported.

The passing suite establishes that the Step 2 source move and new APIs did not regress the deterministic product behavior covered by the repository tests.

## Step 2 behavior now established

The dedicated module exists:

```text
src/upgradepilot/exact_requirement_change.py
```

The public path predicate is behavior-validated through the complete suite:

```text
is_exact_requirement_file
```

It admits the selected conventional requirements and constraints path families and rejects arbitrary or invalid paths according to the Step 2 tests.

The public file-level extractor is behavior-validated through the complete suite:

```text
extract_exact_requirement_changes
```

It returns:

```text
ExtractedDependencyVersionChange
or
DependencyChangeEvidenceProblem
```

for one admitted `ChangedFile`, preserving exact package/version strings, normalized package identity, file evidence, complete-patch checks, file-status checks, and shared problem meanings.

The current legacy runtime API remains available:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

The compatibility wrapper delegates to the moved exact-requirement implementation without migrating current CLI or CI callers.

## Installed public S004 control

Authentication was explicitly removed before execution:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

The installed command completed successfully.

Observed pull-request identity:

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

Observed target declaration evidence:

```text
Target Python declaration: project_table_absent
Target Python source: pyproject.toml @ f3cda8a94600e58d27f1bc17c99b7693718b6350
Target Python blob SHA: 38d6a9efc4b94e2b733d3bbb848156449814ec94
```

Observed exact-head CI evidence:

```text
Exact-head workflow runs: 2
Regression Tests → completed / success / authority sufficient
Test + Deploy → completed / success / authority unresolved

CI authority: sufficient
CI authority reason: exact_head_dependency_exercised
```

The sufficient workflow visibly installed `requirements-dev.txt` and directly invoked `pytest` in one successful exact-head job.

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

The anonymous success applies only to this execution. GitHub anonymous rate limits still exist.

## Regression conclusion

The installed S004 evidence chain remained unchanged after Step 2:

```text
public PR identity
→ complete changed-file evidence
→ requirements-dev.txt
→ pytest 9.0.2 → 9.0.3
→ target declaration: project_table_absent
→ exact-head CI authority: sufficient
→ exact package and upstream evidence
→ unresolved_claim
```

This validates the Step 2 compatibility objective: the exact-requirement implementation moved and gained the new file-level API without changing the established runtime behavior.

## Learning state

Step 2 concepts have been introduced through source review and implementation narration:

- source-specific module ownership;
- path eligibility before syntax interpretation;
- file-level extracted evidence versus PR-wide trusted evidence;
- compatibility wrapper;
- lazy import for cycle avoidance;
- explicit legacy-to-shared problem translation.

Current depth remains:

```text
introduced and explained through concrete source
+ validation observed
but
no independent implementation practice recorded
no user-owned explanation recorded
no formal assessment recorded
not mastered
```

Test execution and successful runtime behavior are product evidence, not mastery evidence.

## Not established

Step 2 validation does not establish:

- `compare_extracted_dependency_changes`;
- PR-wide trusted `DependencyVersionChange` production;
- constraints-file CI consumption semantics;
- generic exact base/head dependency-file acquisition;
- reported-versus-decoded byte-size validation;
- `uv.lock` parsing;
- duplicate-package-group comparison;
- S001 dependency identity through the product;
- CLI or CI migration to the shared trusted result;
- PEP 440 runtime validation;
- Python-support relevance;
- compatibility, objective safety, or maintainer action;
- production readiness;
- mastery of Step 1 or Step 2 concepts.

## Step 2 closure and exact continuation

Step 2 is now **behavior-validated** for the dedicated exact-requirement module, selected path eligibility, shared file-level results, and preserved legacy runtime.

The next bounded plan step is Step 3:

```text
compare_extracted_dependency_changes
```

Before implementation, Step 3 should be discussed through concrete input/output cases and stop conditions:

1. no extracted changes;
2. one extracted change;
3. equivalent changes with combined source evidence;
4. conflicting changes;
5. several package transitions;
6. recognized file problems that must block trust.

Do not begin generic exact-file acquisition, `uv.lock` parsing, CI migration, PEP 440 work, or recommendation logic during Step 3.
