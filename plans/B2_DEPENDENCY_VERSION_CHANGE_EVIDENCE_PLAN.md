# B2 Dependency Version Change Evidence Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Architecture control:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Naming control:** [`../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Downstream package plan:** [`B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)  
**Downstream relevance plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)

## Purpose

Implement and prove one trustworthy exact-version dependency change from a bounded set of real Python dependency-file formats.

```text
public Python Dependabot PR
→ exact PR, base, head, and complete changed-file identity
→ identify admitted dependency files
→ extract possible exact version changes
→ compare all extracted changes and recognized file problems
→ one trusted DependencyVersionChange
   or an explicit unsupported, unavailable, malformed, incomplete,
   ambiguous, multiple, or conflicting result
→ bounded CI, package, upstream, target, and later decision work
```

This plan does not implement universal dependency management, dependency graphs, broad CI interpretation, compatibility evaluation, or automatic maintainer decisions.

## Owning question

> Can UpgradePilot establish exactly one supported Python package version change from complete exact-revision dependency evidence, preserve the exact evidence supporting it, and stop honestly when the evidence is outside the admitted boundary?

## Starting product truth

The behavior-validated implementation currently supports one complete same-file exact requirement transition:

```text
-package==old_version
+package==new_version
```

S004 proves that path with:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
```

S001 uses:

```text
uv.lock
soupsieve 2.6 → 2.8.4
```

The current code cannot establish S001 because it does not compare structured exact base/head lockfiles.

## Included boundary

- public GitHub-hosted Python repositories;
- Dependabot pull requests with immutable base/head SHAs;
- complete changed-file records;
- exactly one supported package version transition;
- normalized Python distribution-name identity;
- exact raw old and proposed version strings;
- conventional exact `package==version` requirements and constraints files;
- modified same-path files whose basename is exactly `uv.lock`;
- exact base/head repository-file acquisition when structured comparison requires it;
- deterministic source-specific extraction;
- deterministic comparison of all extracted changes and recognized file problems;
- exact path, revision, blob, and byte-count evidence;
- bounded CI dependency-exercise states;
- controlled tests and public S004/S001 read-only validation;
- no new runtime dependency for dependency-file extraction.

## Excluded boundary

- grouped or multi-package Dependabot updates;
- selecting one package from several changes;
- requirement ranges, extras, markers, editable installs, URLs, VCS references, or local paths as trusted exact-version changes;
- arbitrary changed-file scanning for requirement-like text;
- Poetry, PDM, Pipenv, Conda, and other lock formats;
- added, deleted, or renamed lockfiles;
- changed duplicate `uv.lock` groups requiring resolver-aware pairing;
- broad uv workspace, group, environment, or command interpretation;
- dependency graph, direct/transitive, group, extra, or runtime-role analysis;
- repository usage analysis;
- complete constraints-file installation tracing;
- package compatibility, Python-support relevance, safety, or maintainer action;
- LLM or model involvement in dependency-file parsing;
- target-repository mutation.

## Accepted architecture summary

ADR-0004 controls the detailed method. The build must preserve these boundaries.

### Shared trusted result

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

The record states only that admitted dependency-file evidence establishes one exact textual package version transition.

### Extraction and comparison

```text
admitted source file
→ ExtractedDependencyVersionChange or DependencyChangeEvidenceProblem

all extracted changes and recognized file problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

B2 supports exactly one transition.

Equivalent extracted changes require the same normalized package and exact raw old/proposed strings. Equivalent evidence combines source records. Different transitions conflict. Recognized malformed, unavailable, incomplete, or oversized admitted evidence blocks a trusted result.

### Requirements and constraints files

Admit conventional lowercase `requirements...txt/.in` and `constraints...txt/.in` filenames and `.txt/.in` descendants beneath exact `requirements` or `constraints` directory components at any depth.

Path eligibility does not establish dependency role, installation, CI consumption, compatibility, or safety.

### `uv.lock`

The first structured boundary requires:

- GitHub status `modified`;
- basename exactly `uv.lock`;
- the same complete relative path at base and head;
- both exact files available;
- schema `version = 1`;
- non-negative integer `revision`;
- valid TOML parsed with Python 3.12 `tomllib`;
- usable textual package `name` and `version` fields.

Acquire through the GitHub Contents endpoint at only the exact PR base or head SHA.

Keep the maximum:

```text
1,000,000 decoded bytes
```

Validate GitHub-reported size before decoding and require decoded byte length to match it. Preserve repository, path, revision, blob SHA, and byte count.

S001 exact measurements are:

```text
base: 606,307 bytes
head: 606,313 bytes
```

No blob/raw fallback or larger bound is authorized.

Group package records by normalized name.

- one base record plus one head record: require stable source and resolution context, then compare exact version strings;
- unchanged repeated-name group: remove only `sdist` and `wheels`, retain all other parsed fields, and compare records as an unordered multiset;
- changed repeated-name group: `ambiguous_uv_lock_package_records`;
- same-version non-artifact structural change outside the exact-version rule: explicit unsupported structural-change result;
- artifact-only differences do not create dependency transitions.

### Version semantics

Dependency extraction preserves exact raw strings and validates only textual structure and inequality.

PEP 440 parsing and ordering begin in the downstream package/upstream responsibility using `packaging.version.Version`. Invalid or non-forward Python package semantics do not erase the observed dependency change.

### CI dependency exercise

Future shared result:

```text
DependencyCIExerciseResult
```

States:

```text
proven
no_successful_ci
unresolved
```

The existing direct requirements rule may prove one successful exact-head path through visible `pip -r <exact path>` installation plus direct changed-package invocation.

Constraints and `uv.lock` do not inherit requirements-file semantics. Until separate bounded consumption rules exist, successful CI remains unresolved for those evidence-only paths.

## Selected implementation names

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

Public CLI labels:

```text
Dependency change
Dependency evidence
CI dependency exercise
```

Existing names remain implemented truth until replaced through tests. Historical records are not mass-renamed.

## Required problem meanings

Dependency evidence must distinguish at least:

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

## Learning and implementation method

Approval of the architecture does not establish user understanding.

Each implementation unit must be taught when it becomes concrete:

```text
new record, function, or rule
→ full technical term
→ practical meaning
→ why the name fits
→ input and output
→ smallest mechanism explanation
→ test proving the boundary
→ user review at the depth reached
```

Do not require the user to understand the complete architecture before implementation begins. Do not mark a concept mastered because its code was generated or a decision was approved.

## Build sequence

### Step 1 — Freeze shared records and problem states

Implement and test:

- `DependencyFileEvidence`;
- `ExtractedDependencyVersionChange`;
- `DependencyVersionChange`;
- `DependencyChangeEvidenceProblem`;
- exact problem vocabulary;
- immutable evidence behavior.

Teach data classes, immutable records, union-style result handling, and why extracted evidence is not yet trusted across the PR.

### Step 2 — Move the existing exact-requirement behavior

Create `exact_requirement_change.py` and move the validated parser behind:

```text
is_exact_requirement_file
extract_exact_requirement_changes
```

Preserve:

- complete-patch checks;
- GitHub addition/deletion reconciliation;
- same-file modified status;
- exact `package==version` grammar;
- package-name normalization;
- ambiguity abstention;
- S004 behavior.

Add path-eligibility tests for conventional root and nested requirements/constraints files and rejection of documentation/example paths.

### Step 3 — Compare extracted changes

Implement `compare_extracted_dependency_changes` independently of `uv.lock`.

Prove:

- no extracted changes;
- one extracted change;
- equivalent evidence with combined source records;
- conflicting changes;
- several package changes;
- recognized malformed evidence cannot be ignored.

### Step 4 — Generalize exact PR file acquisition

Extend `github_repository.py` with explicit base/head file functions.

Prove:

- only the PR's immutable base or head SHA is accepted;
- requested and returned paths match;
- blob SHA and revision are preserved;
- reported size is validated before decoding;
- reported and decoded size must agree;
- the one-million-byte limit is enforced;
- missing, inaccessible, oversized, malformed Base64, and invalid UTF-8 remain distinct;
- existing workflow and target exact-head acquisition remains green.

### Step 5 — Extract `uv.lock` changes

Use controlled complete-file fixtures before public validation.

Prove:

- supported schema and revision controls;
- one unambiguous exact version transition;
- unchanged package;
- package addition or removal;
- several version changes;
- malformed TOML;
- invalid package records;
- source or resolution-context mismatch;
- same-version unsupported structural change;
- unchanged duplicate groups do not block another clear transition;
- changed duplicate groups remain ambiguous;
- artifact-only differences do not create extra transitions;
- exact base/head source evidence is preserved;
- no S001 identifiers are hardcoded.

### Step 6 — Migrate downstream dependency input

Replace downstream dependence on `PinnedDependencyChange` with the trusted shared record while preserving current exact-requirement behavior.

Prevent file evidence paths from being treated automatically as installation evidence.

### Step 7 — Migrate CI result names and semantics

Introduce `DependencyCIExerciseResult` and preserve the current direct requirements rule.

Prove:

- one admitted successful exact-head path produces `proven`;
- no completed successful exact-head job produces `no_successful_ci`;
- successful CI without an admitted consumption/exercise rule produces `unresolved`;
- constraints and `uv.lock` do not inherit requirements-file install semantics;
- unresolved CI remains visible and is not presented as green evidence.

### Step 8 — Integrate the command path

Expected bounded outcomes:

```text
S004
→ exact requirements change extracted
→ trusted DependencyVersionChange
→ existing direct requirements CI rule may produce proven
→ existing target, package, and upstream behavior preserved

S001
→ exact base/head uv.lock comparison
→ Soup Sieve 2.6 → 2.8.4 established
→ trusted DependencyVersionChange
→ package/upstream and target stages may proceed when independently supported
→ CI dependency exercise remains unresolved until uv consumption is separately proven
```

Do not implement Python support-drop comparison, crossed-release acquisition, or LLM extraction here.

### Step 9 — Validate

Run:

1. focused record and problem tests;
2. exact-requirement path and extraction tests;
3. extracted-change comparison tests;
4. repository-file acquisition tests;
5. `uv.lock` fixture tests;
6. CI dependency-exercise tests;
7. CLI integration tests;
8. the complete deterministic suite;
9. installed public read-only S004 validation;
10. installed public read-only S001 validation.

Record exactly what advanced and where the product still stops.

### Step 10 — Return to Python-support relevance

Only after this plan reaches its stop line:

- select [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md) again through `MEMORY.md`;
- continue PEP 440 admission, crossed-version upstream evidence, trusted support-drop claims, and target relevance;
- use S001 without rewriting historical product-simulation evidence.

## Proof obligations

Implementation must prove:

1. no case, repository, package, version, SHA, or expected-result hardcoding;
2. supported behavior follows admitted file and evidence rules;
3. arbitrary documentation or example files are not admitted;
4. conventional root and nested requirements/constraints paths are admitted consistently;
5. requirements and constraints evidence does not become role or installation proof;
6. S004 preserves its validated behavior;
7. S001 and equivalent lock variations produce the shared trusted record shape;
8. package names normalize under the admitted distribution-name rule;
9. exact raw old/proposed versions remain preserved;
10. extraction performs no PEP 440 ordering;
11. exact path/revision/blob/byte evidence is preserved;
12. reported and decoded file sizes must agree;
13. unavailable, oversized, malformed, incomplete, unsupported, ambiguous, multiple, and conflicting states remain distinct;
14. several package changes never collapse to one;
15. equivalent evidence combines source records without inventing stronger meaning;
16. conflicting evidence cannot reach downstream work as trusted identity;
17. recognized malformed or unavailable admitted files are not ignored;
18. unsupported lock schema remains explicit;
19. unchanged duplicate groups do not block S001;
20. changed duplicate groups are not paired heuristically;
21. artifact-only changes do not create extra transitions;
22. source and resolution-context differences are not collapsed;
23. added, deleted, and renamed lockfiles remain unsupported;
24. an evidence path is not proof of CI consumption;
25. CI states preserve proven, no-successful-CI, and unresolved meanings;
26. constraints and `uv.lock` do not inherit requirements-file CI semantics;
27. unresolved CI does not erase dependency identity or become green evidence;
28. no new runtime dependency enters dependency-file extraction;
29. the complete deterministic suite remains green;
30. public S004 and S001 behavior matches the bounded stop line;
31. names and output labels satisfy the naming specification;
32. no compatibility, safety, recommendation, production-readiness, mastery, or ownership claim exceeds the evidence.

## Rejection and reframing conditions

Reframe or stop if:

- the trusted record cannot serve downstream modules without hiding required file-specific meaning;
- conventional path rules create material false positives;
- structured lock interpretation requires broad resolver or graph semantics;
- selected real files require effectively unbounded acquisition;
- duplicate/source/marker behavior cannot remain honest through conservative abstention;
- source-specific extraction plus comparison costs more than the supported breadth justifies;
- S004 cannot be preserved without case-specific exceptions;
- CI code cannot separate source evidence from exercise proof;
- work expands into universal package managers, dependency graphs, role analysis, or universal CI interpretation;
- selected public cases no longer expose the intended responsibility at their exact revisions.

The safe fallback is to preserve the exact-requirement path and keep S001 explicitly unsupported. Never manufacture support through patch proximity or case-specific rules.

## Stop line

Stop this plan when UpgradePilot demonstrates:

```text
one trusted DependencyVersionChange
+
conventional exact requirements/constraints extraction
+
modified same-path uv.lock extraction
+
comparison preserving equivalent, conflicting, malformed,
ambiguous, multiple, and recognized-incomplete states
+
exact dependency-file source identity and byte bounds
+
honest DependencyCIExerciseResult behavior
→
S004 preserved
and
S001 Soup Sieve 2.6 → 2.8.4 established
```

This stop line does not establish:

- broad Python dependency-file support;
- direct/transitive or role/path analysis;
- constraints or uv CI consumption beyond admitted rules;
- package compatibility;
- crossed-release upstream acquisition;
- upstream semantic extraction;
- Python support-drop relevance;
- safety or maintainer action.

## Maintenance

Change this plan only when its responsibility, supported formats, trusted record, extraction/comparison rules, exact-file acquisition boundary, CI states, build sequence, proof obligations, rejection conditions, or stop line changes.

`MEMORY.md` alone owns live progress, current blockers, latest revisions, and exact continuation.