# ADR-0004 — Dependency Version Change Evidence

**Status:** Accepted  
**Date:** 2026-07-30  
**Owner:** Ali Rajabi  
**Stage:** B2 — Public PR vertical slice  
**Controlling plan:** [`../../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](../../plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Naming control:** [`../specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)

## Context

UpgradePilot currently recognizes one dependency update only when a complete changed-file patch contains one same-file transition:

```text
-package==old_version
+package==new_version
```

That behavior is deterministic and has been validated through S004. It cannot establish the S001 change because S001 stores Soup Sieve versions in structured `uv.lock` package records.

Dependency identity feeds later CI, package, upstream, target, relevance, and decision work. Extending that responsibility through package-specific conditions, arbitrary-file scanning, or direct per-format branching in downstream code would make the evidence chain difficult to trust and difficult to extend.

The required design must:

- preserve the existing exact-requirement behavior;
- admit one materially different structured format;
- produce one file-format-independent dependency version change;
- stop explicitly on incomplete, ambiguous, multiple, or conflicting evidence;
- avoid claiming dependency role, CI consumption, compatibility, safety, or maintainer action;
- remain teachable during implementation.

## Decision

### 1. Shared dependency version change flow

Use source-specific deterministic extraction followed by one explicit comparison step:

```text
supported dependency file
→ clearly named extraction function
→ ExtractedDependencyVersionChange or DependencyChangeEvidenceProblem

all extracted changes and recognized file problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

The trusted downstream record is:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

It means only that admitted dependency-file evidence establishes one package transition from one exact old version string to one exact proposed version string.

### 2. Exactly one dependency version change in B2

B2 admits exactly one package version transition.

```text
one transition
→ trusted DependencyVersionChange

several transitions
→ multiple_dependency_version_changes
```

PR title, patch order, alphabetical order, known case identity, or convenience must not choose one package.

Equivalent extracted changes require:

```text
same normalized package
same exact raw old version
same exact raw proposed version
```

Equivalent changes combine all supporting file evidence. Different transitions produce `conflicting_dependency_version_changes`.

A recognized admitted dependency file that is malformed, unavailable, incomplete, or too large prevents a trusted result even when another file produces a convenient change.

### 3. Admitted dependency files

The first dependency-file families are:

1. conventional exact `package==version` requirements and constraints files;
2. modified same-path files whose basename is exactly `uv.lock`.

Requirements and constraints files are admitted when their lowercase final filename follows a conventional `requirements...txt/.in` or `constraints...txt/.in` form, or when a `.txt`/`.in` file is beneath an exact `requirements` or `constraints` directory component.

The rule applies at any repository depth and preserves the complete relative path.

Path eligibility establishes only that the file may supply package/version evidence. It does not establish runtime role, installation, CI consumption, compatibility, or safety.

### 4. Exact version text and later Python version semantics

Dependency-file extraction preserves exact raw old and proposed version strings.

Extraction validates only that each value:

- exists;
- is text;
- is non-empty;
- has no leading or trailing whitespace;
- differs from the other value.

Extraction does not perform PEP 440 validation or ordering.

The downstream package/upstream responsibility uses `packaging.version.Version` before official package release lookup and crossed-version ordering. It must preserve raw and parsed values separately and distinguish:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

A later version-semantics failure does not erase the observed `DependencyVersionChange`.

### 5. Exact PR file acquisition

Acquire complete structured dependency files through GitHub's repository Contents endpoint at only the exact immutable pull-request base SHA or head SHA.

Preserve:

- repository;
- complete relative path;
- requested revision;
- returned path;
- blob SHA;
- reported byte size;
- decoded byte size;
- UTF-8 text.

Keep the existing maximum of:

```text
1,000,000 decoded bytes
```

Require GitHub's reported size to be a non-negative integer. Reject before decoding when it exceeds the bound. After Base64 decoding, require the actual byte length to equal the reported size and apply the bound again.

An admitted file exceeding the bound produces:

```text
dependency_file_too_large
```

Do not add a Git Blob, raw-content, or large-file fallback in B2.

S001 measurements supporting this choice are:

```text
base revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
base blob:     b4a68ab725de337889d50d5374ac0f05db7fb484
base bytes:    606,307

head revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
head blob:     def33fe05d78ab851ce91a33db5bc55a439873a1
head bytes:    606,313
```

Both exact files fit the existing bound with substantial headroom. S001 therefore does not justify another acquisition mechanism or a larger limit.

### 6. First `uv.lock` schema boundary

Use Python 3.12 `tomllib`; add no TOML runtime dependency.

The first rule admits:

```text
lockfile version = 1
revision = non-negative integer
```

A different lock schema version produces:

```text
unsupported_uv_lock_schema
```

Missing, incorrectly typed, or structurally unusable schema controls produce `malformed_dependency_file` or `invalid_dependency_record`, according to the failing layer.

The first file-status boundary requires:

- GitHub status `modified`;
- basename exactly `uv.lock`;
- the same complete path at base and head;
- both exact files available.

Added, deleted, and renamed lockfiles remain unsupported.

### 7. `uv.lock` package record comparison

Group package records by normalized package name.

For one record at base and one at head:

- exact source structure and `resolution-markers` identify the resolution context;
- a source or resolution-context change is not silently paired as the same record;
- an exact version change may establish one extracted dependency transition;
- dependency and package metadata attached to that changed record may change as part of the version transition;
- `sdist` and `wheels` are artifact fields and do not create additional dependency transitions.

A same-version single record with another non-artifact structural change is outside the first exact-version-only rule and produces an explicit unsupported structural-change problem rather than being ignored.

For repeated normalized package names, prove that the group is unchanged by:

1. removing only top-level `sdist` and `wheels` artifact fields from each parsed package record;
2. retaining every other known or unknown field;
3. preserving internal list order;
4. comparing the resulting record collections as unordered multisets, so package-record order does not matter but duplicate counts do.

```text
unchanged duplicate group
→ does not block another unambiguous version transition

changed duplicate group
→ ambiguous_uv_lock_package_records
```

Do not pair repeated records by file position, select the first record, normalize marker meaning, or implement uv resolver semantics in B2.

### 8. CI dependency exercise

Use the future clear shared name:

```text
DependencyCIExerciseResult
```

with states:

```text
proven
no_successful_ci
unresolved
```

- `proven`: one completed successful exact-head CI path satisfies an explicitly admitted dependency-consumption and package-exercise rule;
- `no_successful_ci`: no completed successful exact-head job is available;
- `unresolved`: successful exact-head CI exists, but no admitted rule proves that the changed dependency was consumed and exercised.

The existing exact requirements rule may prove exercise through visible `pip -r <exact path>` installation plus direct changed-package invocation in one successful exact-head job.

Constraints and `uv.lock` do not inherit requirements-file installation semantics. They remain unresolved until separate bounded consumption rules are selected and tested.

Unresolved CI does not erase dependency identity or automatically block package, upstream, or target acquisition. It must not be presented as green evidence.

### 9. Selected source and public names

Use these implementation names unless tests expose a concrete contradiction:

```text
src/upgradepilot/dependency_change.py
    DependencyVersionChange
    ExtractedDependencyVersionChange
    DependencyFileEvidence
    DependencyChangeEvidenceProblem
    compare_extracted_dependency_changes

src/upgradepilot/exact_requirement_change.py
    is_exact_requirement_file
    extract_exact_requirement_changes

src/upgradepilot/uv_lock_change.py
    is_modified_uv_lock_file
    extract_uv_lock_changes

src/upgradepilot/github_repository.py
    ExactRepositoryTextFile
    UnavailableRepositoryFile
    get_pull_request_base_file
    get_pull_request_head_file

src/upgradepilot/ci_dependency_exercise.py
    WorkflowDependencyExerciseInput
    WorkflowDependencyExerciseResult
    DependencyCIExerciseResult
    evaluate_dependency_ci_exercise
```

Use clear CLI labels:

```text
Dependency change
Dependency evidence
CI dependency exercise
```

Existing names such as `PinnedDependencyChange` and `CIAuthorityResult` remain implemented truth until a tested migration replaces them. Do not rename historical records solely for vocabulary consistency.

## Required problem meanings

The product must distinguish at least:

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

Downstream Python package semantics additionally distinguish:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

## Alternatives considered

### Keep only the existing exact-requirement function

Rejected as the B2 destination because it permanently excludes the selected S001 evidence form and forces later package/upstream work to depend on one incidental file grammar.

It remains the fallback if structured lock interpretation cannot stay bounded and trustworthy.

### One giant multi-format parser

Rejected because requirements patches and structured base/head lockfiles have different evidence semantics. One parser would accumulate format branches and make malformed-source behavior harder to isolate.

### Direct per-format branching throughout the CLI and downstream modules

Rejected because file representation would leak into CI, package, upstream, target, and decision code. Adding each format would require another downstream redesign.

### Infer `uv.lock` changes from patch proximity

Rejected because artifact metadata and adjacent package records can produce misleading patch fragments. Complete exact base/head TOML files are required.

### Reject every lockfile containing duplicate package names

Rejected because S001 itself contains legitimate repeated-name groups for different resolution markers. Unchanged duplicate groups can be handled conservatively without full resolver semantics.

### Fully pair changed duplicate resolution branches

Rejected for B2 because correct pairing can require uv marker, source, workspace, and resolver semantics assigned to later breadth work.

### Compare complete package records including artifacts

Rejected because wheel URLs, hashes, sizes, and upload times are package artifacts and would create false dependency-transition ambiguity.

### Switch to blob/raw acquisition or raise the file-size bound

Rejected because S001 fits the existing bound and the Contents endpoint already preserves path, revision, blob, and content identity. Another transport path adds complexity without a selected need.

## Consequences

### Benefits

- S004 remains supported through its existing evidence form.
- S001 can establish Soup Sieve `2.6 → 2.8.4` without case-specific code.
- Downstream modules receive one clear dependency version change shape.
- File-format additions remain localized to extraction functions.
- Malformed, ambiguous, multiple, conflicting, and oversized evidence remains explicit.
- Source evidence is separated from CI consumption proof.
- Real duplicate-name lockfile groups can remain present when unchanged.
- The design remains deterministic and testable without an LLM.

### Costs

- More data records and explicit problem states are required than the current one-function implementation.
- Exact base/head structured-file acquisition adds network and fixture work.
- Conservative duplicate handling may abstain on semantically harmless reordering or changed resolution branches.
- The first lockfile rule supports only one schema and one narrow file-status shape.
- CI may remain unresolved for valid constraints or uv-based workflows.
- Current source names require a tested migration.

These costs are accepted because explicit non-proof and bounded abstention are preferable to guessed dependency identity.

## Reversibility

The design is reversible by:

- preserving the existing exact-requirement tests before refactoring;
- keeping each source extraction function independent;
- keeping comparison independent of `uv.lock` parsing;
- avoiding a dynamic plugin framework or registry;
- returning S001 to explicit unsupported status if bounded lock interpretation fails;
- retaining source evidence so later implementations can reinterpret it without changing downstream meaning.

No database, external service, persisted schema, or target-repository mutation is introduced by this decision.

## Reassessment triggers

Reassess this ADR when:

- a selected real case requires a dependency file above 1,000,000 bytes;
- GitHub changes the Contents endpoint behavior used by the evidence contract;
- uv changes the admitted schema incompatibly;
- common lockfiles produce frequent unsupported structural-change results;
- changed duplicate groups can be supported only through a clearly bounded, tested identity rule;
- downstream consumers require file-specific meaning absent from `DependencyVersionChange`;
- conventional filename rules create material false positives;
- requirements, constraints, or uv CI consumption becomes a selected B2/B4 responsibility;
- implementation evidence shows the selected names obscure rather than clarify responsibility.

Convenience, a known case title, or the existence of a larger parser library is not by itself a reassessment trigger.

## Proof required

Implementation must prove through controlled tests and public read-only validation that:

- no S001, S004, repository, package, version, SHA, or expected result is hardcoded;
- conventional root and nested exact requirements/constraints paths are admitted;
- arbitrary documentation and example files are not admitted;
- exact raw versions and complete source evidence are preserved;
- equivalent, conflicting, malformed, multiple, and recognized-incomplete cases remain distinct;
- exact base/head file acquisition enforces path, revision, blob, reported size, decoded size, UTF-8, and the one-million-byte bound;
- supported `uv.lock` schema and file-status rules are enforced;
- unchanged duplicate groups do not block S001;
- changed duplicate groups remain ambiguous;
- artifact-only changes do not create extra dependency transitions;
- source and resolution-context differences are not silently collapsed;
- S004 preserves its validated behavior;
- S001 establishes Soup Sieve `2.6 → 2.8.4` and no stronger unsupported claim;
- CI states preserve proven, no-successful-CI, and unresolved meanings;
- the complete deterministic suite remains green.

## Ownership and learning note

Ali approved Decision Clusters 1–3 after progressive discussion. For the final acquisition, lockfile-equality, schema, naming, and ADR details, Ali explicitly stated that he did not understand the explanation and delegated the remaining engineering decisions so the project could close design and proceed to building.

This ADR therefore records an AI-recommended and Ali-authorized implementation method. It does **not** establish Ali's understanding, mastery, or independent ability to reproduce the design.

Implementation must teach the relevant concepts at the point they become concrete:

```text
record or function being introduced
→ practical responsibility
→ input and output
→ reason for the boundary
→ smallest test proving it
→ user review before proceeding to the next conceptual unit
```

The user is not required to understand the complete architecture in advance. Learning evidence must come from the implementation sessions, explanations, tests, and the user's demonstrated reasoning—not from approval of this ADR.