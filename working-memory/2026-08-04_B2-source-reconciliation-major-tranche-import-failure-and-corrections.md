# B2 Source Reconciliation — Major-Tranche Failure, Diagnosis, and Corrections

**Date:** 2026-08-04  
**Scope:** Source-structure reconciliation only. No Step 7B/model-runtime/target-activation capability was introduced.

## Why this record exists

The first broad post-migration validation did not pass. The failure was useful: it exposed a symbol-wiring defect created during the responsibility migration while also showing that most loaded behavior and the live Step 7A GitHub/changelog path remained intact.

This record preserves the observed symptom, root cause, diagnosis, corrections, and reusable lessons instead of retaining only the eventual green state.

## User-observed validation result

Focused architecture/dependency/Step-7A tests attempted 47 tests. Three modules failed to import:

```text
test_source_topology
test_exact_requirement_change
test_dependency_analysis
```

The common error was:

```text
ImportError: cannot import name 'repository_relative_path_parts'
from 'upgradepilot.repository_path'
```

The full suite then reported:

```text
Ran 320 tests in 0.059s
FAILED (errors=5)
```

The five collection/import errors were:

```text
test_cli
test_dependency_analysis
test_exact_requirement_change
test_source_topology
test_step8_source_recognition
```

`python -m upgradepilot --help` failed through the same import chain, and Python's diagnostic correctly suggested the existing symbol:

```text
repository_relative_parts
```

Every test that loaded past this import chain passed in that run.

## Why Step 7A still passed

The live Step 7A proof was independent of the broken dependency import path:

```text
GitHub exact-commit changelog discovery
→ upgradepilot.github.changelog
```

It did not import `dependency.analysis` or `dependency.requirements`, so the generic exact-commit discovery rule still recovered:

```text
docs/src/markdown/about/changelog.md
```

This distinction mattered diagnostically. The repository did not have one undifferentiated "refactor failure"; it had a dependency-module symbol-wiring failure while the migrated GitHub/changelog behavior remained live-valid.

## Root cause

The new shared primitive had already been established as:

```python
repository_relative_parts(...)
```

During the major migration, two new dependency implementation owners imported a different name:

```python
repository_relative_path_parts
```

The architectural ownership decision was correct, but the consumer symbol was typed from memory instead of being copied from the exact exported contract.

Because `dependency.analysis` sits on the CLI import path, one missing symbol propagated into several apparently unrelated test modules and the package entry point.

## Correction

Both active dependency owners now import and call the exact shared primitive name:

```text
src/upgradepilot/dependency/requirements.py
src/upgradepilot/dependency/analysis.py
```

The consumers were also moved further toward the final topology while being corrected:

```text
dependency requirements → github.pull_request
dependency analysis     → github.pull_request + github.repository + dependency.uv_lock
```

The fix did not weaken path validation or add a second alias merely to hide the typo. There remains one source-neutral repository-path owner.

## Additional migration defect prevented before validation

The target-Python success record was being normalized so callers no longer had to supply the constant state:

```text
state = "available"
```

An initial implementation used `init=False`. That would have broken existing explicit test/fixture construction that still passed `state="available"` during the migration.

The corrected contract uses a normal defaulted field instead:

```python
state: Literal["available"] = "available"
```

Therefore:

- new callers do not need to repeat the constant;
- transitional explicit fixtures still remain valid;
- no second target-evidence model is introduced.

This was caught before a user validation run.

## Git object-ID compatibility check

The first draft of the centralized GitHub commit validator admitted only 40-character lowercase SHA-1 strings. Existing exact-file and changelog behavior had already proven a broader invariant:

```text
40- or 64-character hexadecimal immutable Git object ID
uppercase accepted and normalized
movable refs rejected
```

The shared `github.identity.validate_commit_sha(...)` was corrected to preserve the proven grammar before provider modules were migrated to it. This avoided silently narrowing runtime behavior during a nominal refactor.

## Structural work completed after diagnosis

After isolating the import defect, the migration continued forward rather than backing out the demonstrated package boundaries:

```text
GitHub API/identity/PR/Actions/repository/release/tag/changelog
→ provider-owned implementations

PyPI API/release/provenance
→ provider-owned implementations

dependency change/requirements/analysis/uv_lock/versioning
→ domain-owned implementations

CI workflow commands/dependency exercise
→ domain-owned implementations

target Python/specifier/relevance
→ domain-owned implementations

upstream repository/interval/interval-evidence/claim
→ domain-owned implementations
```

The package root remains intentionally minimal.

## Exact repository-file convergence

The reconciliation also removed two active repository-text evidence generations.

Runtime acquisition now returns one `RepositoryTextFile` shape capable of retaining:

```text
repository
requested path
returned path
immutable revision
blob SHA
reported byte count
decoded byte count
UTF-8 content
retrieval time
```

The historical `ExactRepositoryTextFile` name is temporarily an alias to this one active type for migration compatibility. Exact runtime readers populate the strong fields; downstream boundaries that require them validate them explicitly.

The workflow exact-head reader was strengthened to use the same byte-agreement/retrieval evidence path as dependency and changelog readers.

## Old upstream semantic generation retired

The application no longer uses:

```text
UpstreamSourceResolver
→ UpstreamReleaseEvidence
→ claim_state = "unresolved_claim"
```

Trusted upstream repository identity now ends at:

```text
PyPI Source metadata
+ PyPI publisher provenance
→ UpstreamRepositoryEvidence
```

GitHub releases, interval authority, semantic claim candidates, and deterministic claim grounding remain separate later boundaries.

This removes a fake semantic state instead of renaming it.

## CLI/orchestration correction

`investigation.py` now owns application sequencing. `cli.py` owns:

```text
arguments
environment token input
presentation
exit-status policy
```

The CLI no longer constructs every provider/domain client itself, and its output no longer presents `Claim state: unresolved_claim`.

## Reusable lessons

### 1. Architecture and wiring are different proof obligations

A correct module boundary does not prove that import names, exported symbols, and call sites were wired correctly.

### 2. One import defect can fan out through an application root

A collection failure in five tests did not mean five independent bugs. Trace the first shared import chain before editing downstream callers.

### 3. Preserve exact proven grammars during refactors

Moving a validator is not permission to narrow its accepted values. Existing tests/proofs define the behavior unless an intentional contract change is separately admitted.

### 4. Compatibility during migration should not create duplicate owners

Where temporary compatibility is useful, old paths point to the new owner. The new owner must not import the old implementation.

### 5. Do not fabricate stronger evidence

When converging evidence contracts, do not synthesize reported byte counts or retrieval facts that the source did not provide. Strengthen acquisition so the facts are actually earned.

### 6. Live proofs help localize structural regressions

The Step 7A live PASS during the dependency import failure showed that the GitHub/changelog migration survived independently. That reduced the diagnostic search space.

## Status at the end of this record

The original symbol mismatch has been corrected. The larger responsibility migration has continued and now requires one broad deterministic/import/entry-point/live regression run before compatibility shims and historical experiment-test placement can be finalized.
