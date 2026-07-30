# B2 Dependency Evidence Design Closure

**Local timestamp:** 2026-07-30 16:31 +03:30  
**Route:** B2 — Public PR vertical slice  
**Selected plan:** [`../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Accepted architecture:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Operation:** Close the remaining dependency-evidence architecture decisions and prepare the selected plan for implementation  
**Result:** Design closed; implementation Step 1 authorized; no product source, tests, dependency, or CLI behavior changed

## User direction and understanding boundary

Ali stated that he did not understand the final lockfile acquisition and duplicate-record explanation, approved the recommended direction, delegated any remaining engineering decisions, and asked to close this part properly so the concepts could be learned during building.

This is recorded precisely:

- Ali authorized the project to proceed with the AI-recommended bounded architecture;
- the authorization is not evidence that Ali understood the complete design;
- no progress or mastery tracker may treat this approval as demonstrated technical knowledge;
- implementation sessions must teach each concept when its record, function, algorithm, or test becomes concrete.

## Decisions closed by delegation

### Exact structured-file acquisition

Selected:

```text
GitHub Contents endpoint
+ exact PR base/head commit SHA only
+ exact relative path
+ GitHub-reported size validation
+ Base64 decoding
+ reported/decoded byte agreement
+ 1,000,000 decoded-byte maximum
+ UTF-8 validation
+ exact path/revision/blob/byte evidence
```

Do not add a Git Blob, raw-content, or large-file fallback in B2.

An admitted file above the bound produces:

```text
dependency_file_too_large
```

### Exact S001 measurements

Pull request:

```text
pydantic/pydantic #13432
```

Base:

```text
revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
blob:     b4a68ab725de337889d50d5374ac0f05db7fb484
bytes:    606,307
```

Head:

```text
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
blob:     def33fe05d78ab851ce91a33db5bc55a439873a1
bytes:    606,313
```

The exact sizes were calculated from GitHub's complete line-wrapped Base64 responses. Both files fit the existing one-million-byte boundary. The head is six bytes larger than the base.

### First `uv.lock` schema

Selected:

```text
version = 1
revision = non-negative integer
Python 3.12 tomllib
```

A different schema version produces `unsupported_uv_lock_schema`. Missing, incorrectly typed, or unusable controls remain malformed or invalid dependency records.

### Single package record behavior

For one record at base and one at head:

- normalized name groups the package;
- exact source structure and `resolution-markers` preserve resolution context;
- source or context changes are not silently paired;
- an exact version change may establish one extracted transition;
- dependency and metadata changes attached to that changed record may accompany the transition;
- top-level `sdist` and `wheels` are artifact fields and do not create extra dependency transitions;
- a same-version non-artifact structural change remains outside the first exact-version-only rule.

### Duplicate package groups

For repeated normalized package names:

1. remove only top-level `sdist` and `wheels` from each parsed package record;
2. retain every other known or unknown field;
3. preserve internal list order;
4. compare the resulting package records as unordered multisets.

```text
unchanged group
→ does not block another clear transition

changed group
→ ambiguous_uv_lock_package_records
```

Do not pair by record position or implement uv resolver semantics.

### Final clear implementation names

Selected:

```text
DependencyVersionChange
ExtractedDependencyVersionChange
DependencyFileEvidence
DependencyChangeEvidenceProblem
compare_extracted_dependency_changes

is_exact_requirement_file
extract_exact_requirement_changes

is_modified_uv_lock_file
extract_uv_lock_changes

ExactRepositoryTextFile
get_pull_request_base_file
get_pull_request_head_file

DependencyCIExerciseResult
evaluate_dependency_ci_exercise
```

Selected public labels:

```text
Dependency change
Dependency evidence
CI dependency exercise
```

Existing runtime names remain current truth until a tested migration replaces them.

## Architecture alternatives closed

Rejected as the selected B2 method:

- retaining exact requirements as the permanent only format;
- one giant multi-format parser;
- direct source-format branches throughout downstream and CLI code;
- `uv.lock` interpretation from patch proximity;
- rejecting every lockfile with duplicate package names;
- fully pairing changed duplicate resolution branches;
- comparing package artifact fields as dependency identity;
- increasing the file-size limit or adding another endpoint without a selected real need.

The safe reversal remains preserving the existing S004 path and returning S001 to explicit unsupported status.

## Files changed

Created:

```text
docs/architecture/ADR-0004-dependency-version-change-evidence.md
```

Commit:

```text
a305753462cbf4bb0f30739ea9a91567cb2ec931
```

Updated the selected plan to remove unresolved design gates and begin at implementation records/tests.

Commit:

```text
3c6df2e1a62c125030a29ff016eb88259fa960d8
```

Updated the architecture decision register.

Commit:

```text
4dfd0208b774744d51c4bde245d17a181556fd2a
```

## Implementation authorization

The next authorized product work is only Step 1 of the selected plan:

```text
freeze and test the shared dependency-change records and problem states
```

The first implementation session must teach:

- what a data record is;
- why extracted evidence differs from a trusted PR-wide result;
- why immutable records are used;
- how explicit problem results prevent guessed control flow;
- the smallest tests proving those contracts.

Do not begin `uv.lock` parsing, CI migration, PEP 440 work, or public S001 execution before the earlier build steps and tests authorize them.

## Not established

- any new source type or function exists in runtime code;
- path eligibility is implemented;
- constraints-file behavior is implemented;
- exact base/head generic acquisition is implemented;
- `uv.lock` parsing is implemented;
- duplicate-group comparison is implemented;
- S001 reaches dependency identity through the product;
- CI result migration is implemented;
- tests pass for the selected architecture;
- Ali understands or can reproduce the architecture;
- compatibility, safety, maintainer action, or production readiness.