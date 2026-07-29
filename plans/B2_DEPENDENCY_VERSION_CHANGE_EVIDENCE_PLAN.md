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
→ identify supported dependency files
→ extract possible package version changes
→ compare all extracted changes and recognized file problems
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

The correction is to support a bounded set of real dependency-file formats that all produce the same trusted package/version fact.

## Clear vocabulary

### `DependencyVersionChange`

The trusted record that one normalized Python package changed from one exact old version string to one exact proposed version string.

It does not state why the package exists, whether it is direct or transitive, whether CI consumed it, or whether the update is compatible or safe.

### `ExtractedDependencyVersionChange`

A possible package version change extracted from one supported dependency file. It is not trusted across the whole pull request until all relevant extracted changes and recognized file problems are compared.

### `DependencyChangeSourceEvidence`

The exact file, revision, blob, patch or complete-file method, and extraction rule that support an extracted change.

### `compare_extracted_dependency_changes`

The comparison step that determines whether extracted changes agree, conflict, or reveal several package changes. This plan avoids broader labels such as `reconciler` and `canonical contract` because the concrete action and result can be named directly.

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
- deterministic comparison of extracted changes and recognized file problems;
- exact evidence source, path, revision, and blob identity where acquired;
- explicit missing, unsupported, malformed, incomplete, ambiguous, multiple, and conflicting states;
- admitted exact `package==version` requirements and constraints files;
- modified same-path files whose basename is exactly `uv.lock`;
- controlled tests and public S004/S001 validation;
- no new runtime dependency for this responsibility.

## Excluded boundary

- grouped or multi-package Dependabot updates;
- choosing one package from several changes;
- requirement ranges, editable installs, extras, markers, URLs, VCS references, or local paths as trusted exact-version changes;
- arbitrary changed-file scanning for text that merely resembles a requirement;
- Poetry, PDM, Pipenv, Conda, or universal lockfile support;
- added, deleted, or renamed lockfiles in the first boundary;
- changed duplicate `uv.lock` package groups whose identity requires marker or resolution-branch matching;
- registry alias resolution;
- dependency graphs, direct/transitive classification, groups, extras, or runtime-role interpretation;
- repository usage analysis;
- broad CI interpretation for lock-based installs;
- package compatibility, Python-support relevance, safety, or maintainer action;
- LLM or model involvement in dependency-file parsing;
- target-repository mutation.

## Trusted dependency version change record

Downstream package, upstream, target, and decision modules should receive one file-format-independent record:

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

## Selected comparison rules

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

No dependency-file priority may silently choose one answer.

### Recognized malformed or incomplete evidence

A changed file recognized as an admitted dependency format must not be ignored merely because another file produced a convenient extracted change.

```text
one valid extracted change
+
one recognized malformed, unavailable, incomplete, or too-large dependency file
→ no trusted DependencyVersionChange
```

The recognized file could conceal another or conflicting change. A genuinely inapplicable file remains different from a recognized file that cannot be evaluated.

## Dependency file 1 — exact `package==version` requirements and constraints

Use a clearly named extraction function such as:

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

### Why file eligibility is required

An arbitrary README, tutorial, fixture, migration document, generated report, or example file can contain valid-looking `package==version` text. Syntax alone therefore cannot establish that a changed file is an admitted dependency source.

The system must first decide whether the path belongs to a bounded conventional requirements or constraints family, and only then inspect exact version lines.

### Admitted descriptive filenames

A normalized relative path is eligible when its final filename uses one of these lowercase conventional forms:

```text
requirements.txt
requirements.in
requirements-<description>.txt
requirements_<description>.txt
requirements.<description>.txt
requirements-<description>.in
requirements_<description>.in
requirements.<description>.in

constraints.txt
constraints.in
constraints-<description>.txt
constraints_<description>.txt
constraints.<description>.txt
constraints-<description>.in
constraints_<description>.in
constraints.<description>.in
```

The descriptive suffix must be non-empty and use ordinary filename characters admitted by the tested path rule. Examples include:

```text
requirements-dev.txt
requirements_test.in
requirements.docs.txt
constraints-ci.in
constraints_python310.txt
```

Names such as these are not admitted by this rule:

```text
my-requirements-example.md
requirements_notes.md
README.txt
dependency-list.txt
```

### Admitted dependency directories

A normalized relative `.txt` or `.in` file is also eligible when any directory component is named exactly:

```text
requirements
```

or:

```text
constraints
```

Examples include:

```text
requirements/base.txt
requirements/dev.in
config/requirements/test.txt
services/api/requirements/prod.in
constraints/python/py310.txt
```

### Nested paths and retained meaning

The rules apply at any repository depth. The complete relative path must be preserved as source evidence.

```text
backend/requirements.txt
services/api/requirements/dev.txt
docs/requirements.txt
```

may all establish an exact package version change.

Path eligibility does not establish whether the file is runtime, development, documentation, test, fixture, or example data. It also does not establish installation or CI consumption. Those meanings require separate evidence and later responsibility rules.

### Requirements versus constraints

A requirements file may request installation. A constraints file limits versions selected by another installation request and does not necessarily request installation by itself.

Both may establish an exact package/version change. Neither filename alone establishes:

- that the package was installed;
- how CI consumed the file;
- dependency role;
- repository usage;
- compatibility;
- safety.

## Dependency file 2 — exact base/head `uv.lock`

Use a clearly named extraction function such as:

```text
extract_uv_lock_changes
```

Do not infer structured package identity from patch proximity. Acquire the complete same-path file at both immutable PR revisions:

```text
<same relative path ending in uv.lock> at PullRequestIdentity.base_sha
<same relative path ending in uv.lock> at PullRequestIdentity.head_sha
```

Each available file must preserve:

- repository;
- complete relative path;
- requested revision;
- returned path;
- blob SHA;
- bounded decoded bytes;
- UTF-8 validity;
- TOML validity.

The existing repository reader provides exact-head text acquisition. This plan requires source-neutral exact-base and exact-head file acquisition with protection against branch-moving or arbitrary revisions.

### Why duplicate package names require a boundary

`uv.lock` is a universal lockfile. The same normalized package name can legitimately appear in more than one environment, source, marker, or resolution context. Matching changed duplicate records correctly can therefore require broader resolution semantics than B2 owns.

The first boundary must neither reject every realistic lockfile merely because an unrelated duplicate exists nor pretend that package name alone identifies a changed resolution branch.

### Selected duplicate-group rule

Group package records by normalized package name in each exact file.

```text
one record in base + one record in head
→ compare the package versions normally
```

For repeated-name groups:

```text
duplicate group is unchanged under the admitted identity comparison
→ it does not block an unrelated unambiguous package version change

duplicate group differs between base and head
→ ambiguous_uv_lock_package_records
```

Do not select the first record, pair records by position, or collapse different sources or marker contexts silently.

The exact set of fields used to prove that a duplicate group is unchanged must be frozen in the ADR and tests after inspecting the admitted `uv.lock` schema. It must use only package identity and resolution-discriminator fields needed for conservative equality; artifact URLs, hashes, wheel lists, sizes, and upload times must not create false package transitions.

### Selected file-status and path rule

The first `uv.lock` support requires:

- GitHub status `modified`;
- basename exactly `uv.lock`;
- the same complete relative path at base and head;
- both exact files available;
- no added, deleted, or renamed lockfile interpretation.

A nested path such as `services/api/uv.lock` is eligible when the same complete path exists at both exact revisions. The rule is based on file identity, not repository-specific allowlists.

### First transition rule

Require:

- both exact files are valid TOML;
- the lock schema contains a usable package list;
- admitted package records contain non-empty textual `name` and `version` fields;
- exactly one unambiguous normalized package has an exact version change;
- no unrelated package addition, removal, or version change makes the pull request a multi-change case;
- old and proposed version strings differ.

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

### File-size decision still required

The existing text reader accepts at most 1,000,000 decoded bytes. Real lockfiles can be larger.

Before implementation:

1. measure the exact S001 base and head `uv.lock` byte sizes;
2. compare the existing contents endpoint with exact-blob acquisition if needed;
3. select a justified bounded maximum;
4. preserve a clear `dependency_file_too_large` result;
5. do not remove limits merely to pass S001.

### Parsed structure

Use Python 3.12 `tomllib`; do not add another TOML dependency.

The first extraction rule may consume only the package identity structure needed by the admitted comparison, conceptually:

```toml
[[package]]
name = "distribution-name"
version = "exact-version"
source = { ... }
```

Artifact URLs, hashes, wheel lists, sizes, and upload times belong to package artifacts. They must not be misclassified as additional dependency version changes.

## Raw version identity and later ordering

This plan preserves exact raw old and proposed version strings while establishing dependency identity.

```text
observed old version string
→ preserved exactly

observed proposed version string
→ preserved exactly
```

Whether the proposed version is newer, how releases are ordered, and whether an interval is valid belong to later package/upstream work. The exact boundary at which PEP 440 validation and ordering begin remains to be frozen before implementation.

## Dependency evidence path versus CI consumption

Where the version change was found is not automatically how CI installed or consumed it.

```text
requirements-dev.txt
→ may be installed explicitly with pip -r requirements-dev.txt

constraints-ci.txt
→ may constrain versions without requesting installation

uv.lock
→ may be consumed through uv sync, uv run, or another uv command
```

Rules:

- dependency extraction records where the version change was established;
- CI authority separately proves how a workflow consumed that dependency file or package;
- the existing exact-requirement CI rule remains unchanged for its admitted command form;
- constraints files do not become direct install evidence merely because they contain the change;
- `uv.lock` CI consumption remains unresolved until a separate bounded uv command rule is selected and tested;
- a lockfile path must never be treated as directly installed merely because it contains the change.

This plan may make the minimum type or interface correction needed to prevent false CI authority. It must not implement complete uv workspace, group, environment, or command interpretation.

## Required problem meanings

Exact final code names must be reviewed before implementation, but the product must distinguish at least:

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
ambiguous_uv_lock_package_records
version_unchanged
multiple_dependency_version_changes
conflicting_dependency_version_changes
```

A supported but malformed file is different from an unsupported format. Several package changes are different from two files contradicting each other.

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
→ identify admitted requirements/constraints paths
→ extract_exact_requirement_changes

src/upgradepilot/uv_lock_change.py
→ identify modified same-path uv.lock evidence
→ extract_uv_lock_changes

src/upgradepilot/github_repository.py
→ acquire exact PR base/head repository files
```

These are recommended responsibility names, not mandatory file counts. Do not create a plugin framework, dynamic registry, package-manager framework, or speculative dependency subpackage.

## Remaining decisions before the ADR and code

The following decisions remain to be learned and resolved:

1. exact raw-version validation and where later PEP 440 parsing and ordering begin;
2. CI result behavior when a supported dependency file's consumption is not established;
3. exact S001 base/head lockfile sizes, endpoint, and bounded acquisition maximum;
4. exact identity fields used only to prove an unchanged duplicate `uv.lock` group;
5. final clear source type, function, problem, module, and CLI names;
6. ADR alternatives, consequences, reversal, and reassessment triggers.

The selected comparison and dependency-file rules in this plan must not be reopened casually. Implementation evidence may expose a concrete contradiction that requires explicit review.

## Work sequence

### Step 1 — Complete the remaining design discussions

Teach and decide the remaining version, CI, acquisition, duplicate-equality, and naming boundaries in coherent groups.

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
- filename eligibility follows the selected path rules;
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
- unchanged duplicate groups do not block an unrelated clear change;
- changed duplicate groups remain ambiguous;
- differing sources or resolution identities are not collapsed;
- exact base/head source evidence is preserved;
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

1. narrow path-eligibility, extraction, and comparison tests;
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
2. supported behavior is defined by dependency-file and path rules, not known cases;
3. arbitrary documentation or example files containing `package==version` text are not admitted;
4. conventional root and nested requirements/constraints paths are admitted consistently;
5. requirements and constraints evidence does not silently become dependency-role or CI-install evidence;
6. S004 and equivalent exact-requirement variations produce the same trusted record shape;
7. S001 and equivalent `uv.lock` variations produce the same trusted record shape;
8. package spelling normalizes under the accepted distribution-name rule;
9. exact raw old/proposed versions are preserved;
10. exact base/head/path/blob evidence is attached where complete-file comparison is required;
11. unavailable, too-large, malformed, incomplete, unsupported, ambiguous, multiple, and conflicting results remain distinct;
12. several package changes are never reduced to one heuristically;
13. equivalent file evidence combines sources without inventing stronger meaning;
14. conflicting evidence cannot reach downstream package or upstream work as trusted identity;
15. recognized malformed or unavailable dependency files are not ignored;
16. unchanged duplicate `uv.lock` groups do not block an unrelated clear change;
17. changed duplicate groups cannot be paired or collapsed heuristically;
18. added, deleted, and renamed `uv.lock` files remain outside the first rule;
19. an evidence path is not treated as proof of CI consumption;
20. existing exact-requirement CI behavior remains unchanged for its admitted command form;
21. constraints and `uv.lock` CI authority remain unresolved unless separately proven;
22. no new runtime dependency is introduced;
23. the complete deterministic suite remains green;
24. the installed S004 command preserves its prior behavior-valid chain;
25. the installed S001 command establishes the dependency version change and reaches only downstream stages supported by their own evidence rules;
26. names and output labels satisfy the naming clarity specification;
27. no compatibility, safety, recommendation correctness, production readiness, or ownership claim exceeds the evidence.

## Rejection and reframing conditions

Reframe or stop if:

- the trusted change record cannot serve downstream consumers without hiding file-specific meaning;
- conventional path rules create unacceptable false positives that cannot be separated from real dependency evidence inside B2;
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
conventional exact package==version requirements/constraints extraction
+
modified same-path uv.lock extraction
+
comparison that preserves equivalent, conflicting, malformed, ambiguous, and multiple states
+
exact dependency-file source identity
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

Change this plan only when its dependency-version-change responsibility, supported file/path rules, trusted record, extracted-change comparison rules, exact-file acquisition boundary, proof obligations, rejection conditions, or stop line changes.

Do not record live approval status, current blockers, completed steps, latest commits, or immediate continuation here. `MEMORY.md` owns those facts.
