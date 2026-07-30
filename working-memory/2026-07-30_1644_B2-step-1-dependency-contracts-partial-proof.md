# B2 Step 1 — Dependency Change Contracts, Partial Proof

**Local timestamp:** 2026-07-30 16:44 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Begin Step 1 only: inspect the current dependency contract, teach its coupling, add the shared immutable evidence records and problem vocabulary, and preserve existing runtime behavior  
**Result:** Additive contract implementation committed; local contract smoke passed; repository-focused and complete deterministic suites remain unexecuted in the available environment

## Existing implementation inspected

The current runtime path remains:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

`PinnedDependencyChange.source_file` currently has two coupled meanings:

1. the file where the exact `package==version` transition was observed;
2. the requirements file that the current CI rule expects to install directly.

Direct callers inspected:

- `src/upgradepilot/cli.py` gates every later stage on `PinnedDependencyChange`;
- `src/upgradepilot/ci_authority.py` accepts `PinnedDependencyChange` and reads `source_file` and `package`;
- `src/upgradepilot/workflow_commands.py` searches for `pip -r <source_file>` and direct package invocation;
- `tests/test_dependency_change.py` protects the supported exact-pin path and current abstention reasons;
- `src/upgradepilot/__init__.py` exposes the current package-level contract.

The legacy parser, CLI gating, CI evaluator, workflow-command reader, and their current result meanings were not migrated in this operation.

## Shared contract added

Added to `src/upgradepilot/dependency_change.py`:

```text
DependencyFileEvidence
ExtractedDependencyVersionChange
DependencyVersionChange
DependencyChangeEvidenceProblem

DependencyChangeExtractionResult
DependencyChangeComparisonResult
```

### `DependencyFileEvidence`

Preserves:

```text
complete relative path
file format
extraction method
optional exact base revision/blob/byte count
optional exact head revision/blob/byte count
```

The optional exact-file fields allow the same record to support both patch extraction and later exact base/head `uv.lock` extraction without pretending that patch evidence already has blob-level identity.

### `ExtractedDependencyVersionChange`

Means:

> One admitted dependency file supplied one possible exact package version transition.

It is not trusted across the complete pull request.

### `DependencyVersionChange`

Means:

> All admitted dependency evidence was considered and exactly one trusted package transition remains.

It preserves all supporting file evidence and explicit limitations as tuples.

### `DependencyChangeEvidenceProblem`

Preserves one stable machine-readable reason, human detail, and any source evidence already identified before the stopping condition.

## Initial problem vocabulary

The runtime vocabulary is an immutable ordered tuple and a corresponding `Literal` type:

```text
no_supported_dependency_file
missing_dependency_patch
incomplete_dependency_patch
unsupported_requirement_format
unsupported_dependency_file_status
dependency_file_unavailable
dependency_file_too_large
malformed_dependency_file
invalid_dependency_record
unsupported_uv_lock_schema
unsupported_uv_lock_structural_change
ambiguous_uv_lock_package_records
version_unchanged
multiple_dependency_version_changes
conflicting_dependency_version_changes
```

No file parser uses this new vocabulary yet. Existing legacy reasons remain runtime truth until later tested migration.

## Focused tests added

Created:

```text
tests/test_dependency_change_contracts.py
```

The tests cover:

1. path, format, method, revision, blob, and byte-count preservation;
2. one-file extracted evidence versus PR-wide trusted evidence;
3. frozen dataclass behavior;
4. immutable tuple collections;
5. the exact problem vocabulary;
6. a problem retaining its source evidence.

The tests use synthetic revisions, blobs, and byte counts. S001 identifiers are not used in the generic contract tests.

## Package-level exports

`src/upgradepilot/__init__.py` now re-exports the shared records, aliases, and problem vocabulary while preserving every existing export.

## Revisions

```text
Add shared records and vocabulary:
81717384f7351dd018c2ba7c3a2bfc7db970dc63

Add focused contract tests:
d9bf3c6c9317ecaee9a03c842e92d75a902d0394

Expose shared package-level contracts:
e8447a9c8330e67df5bbcdd3ba832ad53a5cf745

Make generic contract tests case-neutral:
121d70530c97a80cca83c648670c71d874a66930
```

## Proof completed

A local Python 3.13 smoke check reproduced the committed contract shapes and proved:

```text
frozen field reassignment
→ FrozenInstanceError

tuple collection mutation
→ AttributeError

source values and problem vocabulary
→ preserved as expected
```

The repository comparison confirms that this operation changed only:

```text
src/upgradepilot/dependency_change.py
src/upgradepilot/__init__.py
tests/test_dependency_change_contracts.py
```

The current commit has no associated GitHub Actions workflow run.

## Proof not completed

The available execution environment has:

- no local UpgradePilot checkout;
- no network access from the execution container to clone GitHub;
- Python 3.13, but no Python 3.12 executable;
- no GitHub Actions workflow run for the current commit.

Therefore these required proofs remain outstanding:

```text
python -m unittest tests.test_dependency_change_contracts
python -m unittest tests.test_dependency_change
python -m unittest discover -s tests -v
```

The smoke check is not equivalent to running the committed repository tests.

## Current status

Step 1 is **implemented but not behavior-validated**.

Do not begin Step 2 until the focused contract tests, existing dependency-change tests, and complete deterministic suite pass in a real repository checkout using an admitted Python version.

## Learning status

Introduced:

- frozen dataclass;
- slots;
- tuple immutability;
- union-style result handling;
- extracted file evidence versus trusted PR-wide evidence;
- stable machine-readable problem vocabulary.

Not established:

- Ali can independently define or implement these records;
- Ali understands every optional source-identity field;
- tests have been studied line by line;
- Step 1 is complete.
