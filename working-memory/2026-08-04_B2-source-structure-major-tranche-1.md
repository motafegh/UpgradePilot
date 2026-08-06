# B2 Source-Structure Reconciliation — Major Tranche 1

**Date:** 2026-08-04  
**Purpose:** Preserve the first major structural migration after the 353-test / live-Step-7A pre-refactor baseline.

## Scope completed in this tranche

### Architecture admission

ADR-0007 accepted responsibility-based internal packages while retaining the `src/upgradepilot/` distribution boundary and rejecting speculative layer scaffolding.

### Shared primitives

Created active source-neutral owners:

```text
package_identity.py
repository_path.py
```

PEP 503 normalization is no longer implemented by `dependency_change.py`, and exact-requirements path recognition uses the shared repository-relative path grammar.

### Dependency architecture

Created real ownership under:

```text
upgradepilot/dependency/change.py
upgradepilot/dependency/requirements.py
upgradepilot/dependency/analysis.py
```

The exact-requirements extractor now produces the modern file-level result directly. The active modern path no longer routes through:

```text
PinnedDependencyChange
UnsupportedDependencyChange
DependencyChangeResult
extract_pinned_dependency_change(...)
_LEGACY_PROBLEM_CODES
_extract_legacy_pinned_dependency_change(...)
```

The old flat dependency files are temporary import shims only while remaining active callers/tests migrate.

### Root package API

`upgradepilot.__init__` no longer re-exports the internal client/evidence/problem graph. Its intentional public surface is now empty (`__all__ == ()`). Internal code and tests should import precise owners.

### Demonstrated provider/domain packages

Created explicit package boundaries:

```text
upgradepilot.github
upgradepilot.pypi
upgradepilot.dependency
upgradepilot.ci
upgradepilot.upstream
upgradepilot.target
```

New preferred owner paths include:

```text
upgradepilot.github.pull_request
upgradepilot.github.changelog
upgradepilot.pypi.release
upgradepilot.ci.dependency_exercise
upgradepilot.dependency.versioning
upgradepilot.target.python_specifier
upgradepilot.upstream.interval_evidence
upgradepilot.upstream.claim
```

Some large provider modules remain backed by temporary compatibility imports in this tranche; they are not yet considered physically migrated.

### Step 7A ownership

The actual Step 7A exact-commit changelog discovery implementation now lives in:

```text
upgradepilot.github.changelog
```

The old `upstream_changelog.py` path is a compatibility shim. The live S001 proof tool now imports the GitHub-owned path.

The move also centralized the Git commit/object-ID validator used by changelog discovery. During review, an initial overly narrow 40-lowercase-only validator was corrected before adoption because the validated pre-refactor behavior admitted 40- or 64-character hexadecimal object IDs.

### Upstream repository identity

Created:

```text
upgradepilot.upstream.repository
```

This boundary establishes only trusted GitHub repository identity from PyPI Source metadata plus PyPI publisher provenance. Its successful evidence contains no semantic `claim_state` and does not require a GitHub Release object.

The older `UpstreamSourceResolver` remains active only because the current CLI still uses the pre-Step-7 orchestration path. Removing it belongs to the later orchestration/upstream reconciliation tranche.

### Target evidence normalization

`TargetPythonDeclaration.state` now defaults to `available` rather than forcing callers to supply a constant. The keyword remains accepted during migration so existing trusted-input tests/fixtures do not break solely for construction syntax.

### Application boundary

Created:

```text
upgradepilot.investigation.investigate_public_pull_request(...)
```

with a typed `PublicPullRequestInvestigation` result. This establishes the application-owned orchestration location without changing current CLI execution order.

`cli.py` has not yet been switched to this entry point because its existing tests mock orchestration collaborators inside the CLI module. That activation will be done together with the corresponding CLI/investigation test migration rather than leaving an unreviewable mixed failure surface.

### Structural regression protection

Added `tests/test_source_topology.py` to protect:

- minimal root package API;
- dependency owner imports;
- GitHub provider owner imports;
- target specifier owner import;
- absence of semantic claim state from `UpstreamRepositoryEvidence`;
- concrete investigation entry point.

The legacy-focused `tests/test_dependency_change.py` was replaced with tests for the modern PR-wide comparison contract.

## Explicitly transitional after this tranche

These are not claimed complete yet:

1. large flat GitHub/PyPI/CI/upstream/target implementation modules still exist and several new package modules temporarily import them;
2. `uv_lock_change.py` still owns its old flat implementation and one duplicate path validator;
3. `packaging_method.py` still contains both implementations even though new domain-specific owner modules exist;
4. repository text evidence has not yet converged to one strong contract;
5. old `UpstreamSourceResolver` / `UpstreamReleaseEvidence.claim_state='unresolved_claim'` still exist for current CLI compatibility;
6. `cli.py` has not yet delegated to `investigation.py`;
7. active product tests have not yet been reorganized into domain subdirectories;
8. completed Step 6 experiment-harness tests still live under `tests/`;
9. final active docstring/comment stale-reference audit is not complete.

These are the intended scope of the second major tranche, not forgotten work.

## Feature boundary preserved

This tranche did not implement:

- Step 7B Markdown source windows;
- product LM Studio inference;
- conditional target-Python activation;
- compatibility/safety/merge/defer decisions;
- automatic retries or Instructor/Pydantic;
- target repository mutation.

## Validation state

The last user-observed pre-refactor baseline remains:

```text
Ran 353 tests in 0.077s
OK
LIVE STEP 7A PROOF: PASS
```

The code in this major tranche has not yet been executed in Ali's WSL checkout. The next proof should therefore be broad rather than per-file:

```text
focused source-topology/dependency/Step-7A tests
+ full deterministic suite
+ live Step 7A proof
+ package/CLI import smoke
```

Do not interpret this record as proof that those checks passed after the tranche.
