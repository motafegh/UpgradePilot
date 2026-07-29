# B2 Dependency Version Change Evidence Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Naming control:** [`../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)  
**Generality control:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Downstream plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Establish one trustworthy exact-version dependency change from supported Python dependency files without repository-, package-, version-, or case-specific logic.

```text
public Python Dependabot PR
→ exact PR, base, head, and changed-file identity
→ extract possible dependency version changes from supported file formats
→ compare the extracted changes
→ one trusted DependencyVersionChange
   or an explicit missing, unsupported, malformed, ambiguous, multiple, or conflicting result
→ downstream CI, package, upstream, target, and decision work
```

This plan broadens the accepted dependency-file formats while keeping the product bounded. It does not add universal package-manager support, dependency-graph analysis, compatibility evaluation, or automatic decisions.

## Owning question

> Given complete changed-file evidence and exact PR base/head revisions, can UpgradePilot establish exactly one supported Python package version change, preserve the exact evidence that supports it, and stop honestly when the available dependency files are unsupported, incomplete, ambiguous, multiple, or conflicting?

## Why this work is required

The behavior-validated implementation currently supports one exact requirement-line change:

```text
-package==old_version
+package==new_version
```

That rule is deterministic and is not hardcoded to S004, `pytest`, or one repository. Its accepted file grammar is nevertheless narrower than the product evidence exposed by S001–S005.

S004 uses:

```text
requirements-dev.txt
pytest==9.0.2
→ pytest==9.0.3
```

S001 uses:

```toml
[[package]]
name = "soupsieve"
version = "2.6"
```

becoming:

```toml
[[package]]
name = "soupsieve"
version = "2.8.4"
```

The active exact-requirement logic correctly rejects S001 because `uv.lock` does not contain complete `package==version` lines. Adding a Pydantic-, Soup Sieve-, or S001-specific patch rule would replace one narrow implementation with accumulating case logic.

The correction is to support a bounded set of dependency-file formats that all produce the same trusted package/version fact.

## Clear vocabulary for this plan

This plan uses these terms deliberately:

### `DependencyVersionChange`

The trusted record that one normalized Python package changed from one exact old version string to one exact proposed version string.

It does not state why the package exists, whether it is direct or transitive, whether CI consumed it, or whether the update is compatible or safe.

### `ExtractedDependencyVersionChange`

A possible dependency version change extracted from one supported dependency file. It is not trusted across the whole PR until all relevant extracted changes are compared.

### `DependencyChangeSourceEvidence`

The exact file, revision, blob, patch or complete-file method, and extraction rule that support an extracted change.

### `compare_extracted_dependency_changes`

The comparison step that determines whether the extracted changes agree, conflict, or reveal several dependency changes. This plan avoids the broader labels `reconciler` and `canonical contract` because the concrete action and result can be named directly.

## Relationship to B2 and B4

B2 must identify one supported Python dependency version change without repository-specific hardcoding. It does not require universal dependency support.

B4 later owns broader work including:

- more dependency declarations and lock formats;
- direct and transitive relationships;
- dependency groups, extras, and runtime roles;
- repository usage and dependency paths;
- richer CI consumption rules;
- version constraints and target activation;
- multi-package decision behavior.

This plan therefore does only enough to prevent B2 from depending permanently on one incidental file grammar:

1. preserve the validated exact `package==version` requirement path;
2. add one materially different structured dependency file: modified same-path `uv.lock`;
3. produce one shared trusted `DependencyVersionChange` record;
4. make later file formats additive rather than another downstream redesign;
5. defer graph, role, broad package-manager, and multi-update work to B4.

## Included boundary

- public GitHub-hosted Python repositories;
- Dependabot pull requests with exact base/head identity;
- complete changed-file records;
- exact base/head repository files when a supported format requires them;
- exactly one supported package version change;
- normalized Python distribution-name identity;
- exact raw old and proposed version strings;
- source-specific deterministic extraction functions;
- deterministic comparison of extracted changes;
- exact evidence source, path, revision, and blob identity where acquired;
- explicit missing, unsupported, malformed, incomplete, ambiguous, multiple, and conflicting states;
- exact `package==version` requirement changes;
- modified same-path `uv.lock` changes;
- controlled tests and public S004/S001 validation;
- no new runtime dependency for this responsibility.

## Excluded boundary

- grouped or multi-package Dependabot updates;
- choosing one package from several changes;
- requirement ranges, editable installs, extras, markers, URLs, VCS references, or local paths as trusted exact-version changes;
- Poetry, PDM, Pipenv, Conda, or universal lockfile support;
- added, deleted, or renamed lockfiles in the first boundary;
- registry alias resolution;
- dependency graphs, direct/transitive classification, groups, extras, or runtime-role interpretation;
- repository usage analysis;
- broad CI interpretation for lock-based installs;
- package compatibility, Python-support relevance, safety, or maintainer action;
- LLM or model involvement in dependency-file parsing;
- target-repository mutation.

## Trusted dependency version change record

Downstream package, upstream, target, and decision modules should receive one representation-independent record:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
│   ├── dependency_file_format
│   ├── path
│   ├── base revision/blob when applicable
│   ├── head revision/blob when applicable
│   └── extraction_method
└── limitations[]
```

The record means only:

> Evidence from the admitted dependency files establishes that one Python distribution changed from one exact version string to another.

It must not imply:

- why the package is present;
- direct or transitive role;
- runtime or development use;
- CI installation or execution;
- compatibility;
- safety;
- a maintainer action.

The existing name `PinnedDependencyChange` describes the current exact-requirement grammar. It should not remain the shared downstream name after the broader evidence path is implemented.

## Approved comparison rules

### Exactly one change

B2 supports exactly one trusted dependency version change.

```text
one package version change
→ eligible for downstream evidence work

more than one package version change
→ multiple_dependency_version_changes
```

PR title, patch order, alphabetical order, known package identity, or convenience must not select one package heuristically.

### Equivalent extracted changes

Extracted changes are equivalent only when they have:

```text
same normalized package
same exact raw old version
same exact raw proposed version
```

Equivalent extracted changes produce one trusted record with all supporting source evidence attached.

Agreement between two files proves agreement on the version change. It does not automatically prove dependency role, lock correctness, CI consumption, compatibility, or safety.

### Conflicting extracted changes

Different package identities or different old/proposed version strings produce:

```text
conflicting_dependency_version_changes
```

No file-format priority may silently choose one answer.

### Recognized malformed or incomplete evidence

A changed file recognized as an admitted dependency format must not be ignored merely because another file produced a convenient extracted change.

For example:

```text
requirements file produces a valid change
+
changed uv.lock is malformed or unavailable
→ no trusted DependencyVersionChange
```

The recognized malformed or unavailable file could conceal another or conflicting change. The result must remain explicit until the evidence can be evaluated responsibly.

A file that is genuinely not applicable is different from a recognized supported file that is malformed, unavailable, incomplete, or too large.

## Dependency file 1 — exact `package==version` requirements

The existing deterministic behavior should be preserved behind a clearly named extraction function such as:

```text
extract_exact_requirement_changes
```

It reads complete patch evidence shaped like:

```text
-package==old_version
+package==new_version
```

Preserve these protections:

- complete patch evidence exists;
- visible addition/deletion counts match GitHub metadata;
- one removed and one added exact version line;
- both lines belong to the same modified file;
- normalized package identity matches;
- the version changed;
- richer syntax remains unsupported;
- ambiguity is not guessed.

### Remaining filename decision

The current implementation scans every changed file for complete exact requirement lines. An arbitrary documentation or example file could contain the same text.

The first accepted path family should be chosen from:

1. `requirements*.txt` and `requirements*.in`;
2. `constraints*.txt` and `constraints*.in`;
3. a similarly bounded nested-path form;
4. the existing all-file scan only as a compatibility baseline, not the preferred final rule.

The selected path rule must avoid known-file allowlists and arbitrary text-file false positives.

## Dependency file 2 — exact base/head `uv.lock`

Use a clearly named extraction function such as:

```text
extract_uv_lock_changes
```

Do not infer structured package identity from patch proximity. Acquire the complete same-path file at both immutable PR revisions:

```text
uv.lock at PullRequestIdentity.base_sha
uv.lock at PullRequestIdentity.head_sha
```

Each available file must preserve:

- repository;
- path;
- requested revision;
- returned path;
- blob SHA;
- bounded decoded bytes;
- UTF-8 validity;
- TOML validity.

The existing repository reader provides exact-head text acquisition. This plan requires source-neutral exact-base and exact-head file acquisition with protection against branch-moving or arbitrary revisions.

### Remaining file-size decision

The existing text reader accepts at most 1,000,000 decoded bytes. Real lockfiles can be larger.

Before implementation:

1. measure the exact S001 base and head `uv.lock` byte sizes;
2. compare the existing contents endpoint with exact-blob acquisition if needed;
3. select a justified bounded maximum;
4. preserve a clear `dependency_file_too_large` result;
5. do not remove limits merely to pass S001.

### Parsed structure

Use Python 3.12 `tomllib`; do not add another TOML dependency.

The first extraction rule may consume only:

```toml
[[package]]
name = "distribution-name"
version = "exact-version"
source = { ... }
```

Artifact URLs, hashes, wheel lists, and upload times may change when the package version changes. They belong to the same package record and must not be misclassified as additional dependency changes.

### Remaining duplicate-name decision

A `uv.lock` file may contain repeated normalized package names under different sources, markers, or resolution contexts. A universal uv resolution identity model is outside B2.

Recommended first rule:

> A normalized package name is usable only when it identifies one unambiguous version-bearing package record in each exact file for the compared change.

If duplicate names prevent one-to-one comparison, return:

```text
ambiguous_uv_lock_package_identity
```

Do not select the first record or silently collapse different sources.

### First transition rule

Require:

- the same modified path `uv.lock` at base and head;
- both exact files available and valid TOML;
- a valid package list;
- non-empty textual `name` and `version` fields;
- exactly one unambiguous normalized package whose exact version changes;
- no unrelated package addition, removal, or version change;
- different old and proposed versions.

Expected S001 extracted change:

```text
package: soupsieve
normalized_package: soupsieve
old_version: 2.6
proposed_version: 2.8.4
dependency_file_format: uv_lock
base path/revision/blob: preserved
head path/revision/blob: preserved
```

Preserve raw version strings at this stage. PEP 440 ordering belongs to later package release-interval work.

## Dependency evidence path versus CI consumption

Where the version change was found is not automatically how CI installed or consumed it.

```text
requirements-dev.txt
→ may be installed explicitly with pip -r requirements-dev.txt

uv.lock
→ may be consumed through uv sync or another uv command
```

The trusted dependency version change record must therefore distinguish:

```text
source evidence path
≠
proven CI install input
```

Rules:

- dependency extraction records where the version change was established;
- CI authority separately proves how a workflow consumed that dependency file or package;
- the existing exact-requirement CI rule remains unchanged for its admitted command form;
- `uv.lock` CI consumption remains unresolved until a separate bounded uv command rule is selected and tested;
- a lockfile path must never be treated as directly installed merely because it contains the change.

This plan may make the minimum type or interface correction needed to prevent false CI authority. It must not implement complete uv workspace, group, environment, or command interpretation.

## Required problem meanings

Exact final code names should be reviewed before implementation, but the product must distinguish at least:

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
ambiguous_package_identity
version_unchanged
multiple_dependency_version_changes
conflicting_dependency_version_changes
```

A supported but malformed file is different from an unsupported format. Multiple package changes are different from two files contradicting each other.

Where an existing user-visible reason has the same meaning, preserve it or migrate it deliberately rather than changing diagnostics casually.

## Recommended source layout

No new runtime dependency is required.

Prefer concrete function and data names over broad architecture labels. A likely initial source arrangement is:

```text
src/upgradepilot/dependency_change.py
→ DependencyVersionChange, ExtractedDependencyVersionChange,
  DependencyChangeSourceEvidence, DependencyChangeProblem,
  compare_extracted_dependency_changes

src/upgradepilot/exact_requirement_change.py
→ extract_exact_requirement_changes

src/upgradepilot/uv_lock_change.py
→ extract_uv_lock_changes

src/upgradepilot/github_repository.py
→ acquire exact PR base/head repository files
```

These are recommended responsibility names, not mandatory file counts. Do not create a plugin framework, dynamic registry, package-manager framework, or speculative dependency subpackage.

## Remaining decisions before the ADR and code

The following decisions remain to be learned and resolved:

1. exact requirement and constraint filename/path eligibility;
2. first `uv.lock` duplicate-name identity rule;
3. modified-only `uv.lock` status boundary;
4. raw version identity and where later PEP 440 ordering begins;
5. CI behavior for dependency files whose consumption is not yet understood;
6. lockfile acquisition size and exact endpoint;
7. final clear source type, function, error, module, and CLI names;
8. the resulting ADR scope and reassessment triggers.

The already accepted comparison rules in this plan must not be reopened casually, but implementation evidence may expose a concrete contradiction that requires explicit review.

## Work sequence

### Step 1 — Complete the remaining design discussions

Teach and decide the remaining file-format, identity, CI, acquisition, and naming boundaries in coherent groups.

Do not create the architecture ADR or product source while material names or rules remain unresolved.

### Step 2 — Record the accepted architecture

After the remaining decisions are resolved:

- create an ADR using clear concrete vocabulary;
- compare the existing one-format function, a giant multi-format parser, and the selected source-specific extraction plus comparison design;
- record consequences, failure modes, reversibility, and reassessment triggers;
- update the architecture register.

ADR acceptance authorizes the design but does not prove implementation.

### Step 3 — Freeze data records and problem states

Define and test:

- `DependencyVersionChange`;
- `ExtractedDependencyVersionChange`;
- `DependencyChangeSourceEvidence`;
- `DependencyChangeProblem`;
- `compare_extracted_dependency_changes` behavior;
- clear user-visible diagnostics.

Requirements:

- package/version fields remain straightforward;
- source evidence preserves exact identity;
- exact-requirement behavior remains recognizable;
- source evidence paths are not mislabeled as CI install evidence;
- no case identifiers enter production records.

### Step 4 — Extract the existing exact-requirement logic

Move the validated behavior behind the clearly named exact-requirement extraction function without changing its meaning.

Prove:

- existing S004 controlled tests remain green;
- complete-patch and ambiguity protections remain;
- filename eligibility follows the selected rule;
- downstream package, CI, PyPI, and upstream behavior remains unchanged for the admitted exact-requirement case.

### Step 5 — Compare extracted changes

Implement `compare_extracted_dependency_changes` independently of `uv.lock`.

Controlled tests must prove:

- zero extracted changes;
- one extracted change;
- two equivalent extracted changes with combined source evidence;
- two conflicting extracted changes;
- recognized malformed evidence is not ignored;
- several package changes never collapse to one.

### Step 6 — Add exact PR base/head file acquisition

Extend source-neutral repository acquisition to the exact PR base and head revisions.

Prove:

- only the frozen PR base/head SHAs are accepted;
- requested and returned paths match;
- blob SHAs and revisions are preserved;
- missing base and head files remain distinct;
- byte limits, base64, UTF-8, and response-shape errors remain explicit;
- existing workflow and target exact-head behavior remains green.

Measure S001 lockfile sizes before selecting the final limit or exact-blob path.

### Step 7 — Implement `uv.lock` change extraction

Use controlled complete-file fixtures first.

Prove:

- one exact version change;
- unchanged package;
- package addition or removal;
- several version changes;
- malformed TOML;
- missing or invalid package records;
- duplicate normalized package names;
- differing sources or ambiguous identities;
- exact base/head source evidence;
- artifact metadata changes do not create extra package changes;
- no S001 identifiers are hardcoded.

### Step 8 — Integrate the trusted change record

Preserve the public command and exact PR acquisition.

Expected bounded outcomes:

```text
S004
→ exact requirement change extracted
→ trusted DependencyVersionChange
→ existing target, CI, package, and upstream behavior preserved

S001
→ uv.lock change extracted
→ trusted DependencyVersionChange
→ target and package/upstream stages may proceed
→ CI authority remains explicit and may be unresolved for unsupported uv consumption
```

Do not implement Python support-drop comparison, upstream release-interval acquisition, or LLM extraction in this step.

### Step 9 — Validate controlled and public behavior

Run:

1. narrow extraction and comparison tests;
2. repository acquisition tests;
3. dependency and CLI integration tests;
4. the complete deterministic suite;
5. the installed S004 public read-only command;
6. the installed S001 public read-only command.

State exactly what advanced and where the product still stops.

### Step 10 — Return to Python-support relevance

Only after this plan reaches its stop line:

- select [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md) again through `MEMORY.md`;
- continue upstream interval, trusted support-drop claim, `packaging`, relevance, and conditional target activation work;
- use S001 as the end-to-end relevance case without rewriting historical product simulation.

## Proof obligations

The implementation must prove:

1. production logic contains no S001, S004, repository, package, version, SHA, or expected-result hardcoding;
2. supported behavior is defined by dependency-file rules, not known cases;
3. S004 and equivalent exact-requirement variations produce the same trusted record shape;
4. S001 and equivalent `uv.lock` variations produce the same trusted record shape;
5. package spelling normalizes under the accepted distribution-name rule;
6. exact raw old/proposed versions are preserved;
7. exact base/head/path/blob evidence is attached where complete-file comparison is required;
8. unavailable, too-large, malformed, incomplete, unsupported, ambiguous, multiple, and conflicting results remain distinct;
9. several package changes are never reduced to one heuristically;
10. equivalent file evidence combines sources without inventing stronger meaning;
11. conflicting evidence cannot reach downstream package or upstream work as trusted identity;
12. an evidence path is not treated as proof of CI consumption;
13. existing exact-requirement CI behavior remains unchanged for its admitted command form;
14. `uv.lock` CI authority remains unresolved unless separately proven;
15. no new runtime dependency is introduced;
16. the complete deterministic suite remains green;
17. the installed S004 command preserves its prior behavior-valid chain;
18. the installed S001 command establishes the dependency version change and reaches only downstream stages supported by their own evidence rules;
19. names and output labels satisfy the naming clarity specification;
20. no compatibility, safety, recommendation correctness, production readiness, or ownership claim exceeds the evidence.

## Rejection and reframing conditions

Reframe or stop if:

- the trusted change record cannot serve downstream consumers without hiding file-specific meaning;
- `uv.lock` identity requires broad graph or resolution semantics before one exact change can be established;
- real lockfile size requires effectively unbounded acquisition;
- duplicate, marker, or source behavior cannot remain honest through conservative abstention;
- source-specific extraction plus comparison adds more complexity than the second file format justifies;
- preserving exact-requirement behavior requires case-specific exceptions;
- CI code cannot be prevented from confusing evidence paths with install authority without broad B4 work;
- work begins implementing general package-manager support, dependency graphs, or role analysis;
- selected public cases no longer expose the intended responsibility at their exact revisions.

A rejected approach may leave the exact-requirement path intact and record S001 as unsupported. It must not manufacture support through patch proximity or package-specific rules.

## Stop line

Stop this plan when UpgradePilot demonstrates:

```text
one trusted DependencyVersionChange record
+
exact package==version requirement extraction
+
modified same-path uv.lock extraction
+
comparison that preserves equivalent, conflicting, malformed, and multiple states
+
exact evidence source identity
→
S004 preserved
and
S001 dependency version change established
```

At this stop line, the plan does not establish:

- broad Python dependency-file support;
- direct/transitive or role/path analysis;
- uv CI consumption authority;
- package compatibility;
- crossed-release upstream acquisition;
- upstream semantic extraction;
- Python support-drop relevance;
- safety or maintainer action.

Those responsibilities remain with later plans and B4.

## Maintenance

Change this plan only when its dependency-version-change responsibility, supported file formats, trusted record, extracted-record comparison rules, exact-file acquisition boundary, proof obligations, rejection conditions, or stop line changes.

Do not record live approval status, current blockers, completed steps, latest commits, or immediate continuation here. `MEMORY.md` owns those facts.