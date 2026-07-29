# B2 Dependency Change Interpretation Foundation Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Controlling generality specification:** [`../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)  
**Downstream dependent plan:** [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Define the smallest professional dependency-change interpretation foundation that can establish one exact Python dependency-version transition from materially different admitted representations without repository-, package-, version-, or fixture-specific logic.

```text
public Python Dependabot PR
→ exact PR/base/head/changed-file identity
→ representation-aware deterministic interpretation
→ one canonical dependency-version change
   or explicit unsupported, ambiguous, incomplete, or conflicting result
→ downstream CI, package, upstream, target-relevance, and decision work
```

This plan broadens the dependency-change **representation foundation**. It does not broaden the product into universal package-manager support, dependency-graph analysis, compatibility evaluation, or automatic decision policy.

## Owning question

> Given complete changed-file evidence and exact PR base/head revisions, can UpgradePilot establish exactly one supported Python distribution version transition through an admitted dependency representation, preserve how that transition was proven, and refuse to guess when representations are unsupported, incomplete, ambiguous, multiple, or conflicting?

## Why this plan exists

The first behavior-validated dependency interpreter proves one same-file exact requirement transition:

```text
package==old_version
→ package==new_version
```

That rule is deterministic and general inside its grammar. It is not hardcoded to S004, `pytest`, or one repository. However, the accepted grammar is narrower than the product responsibility discovered across S001–S005.

S004 uses a line-oriented exact-pin representation:

```text
requirements-dev.txt
pytest==9.0.2
→ pytest==9.0.3
```

S001 uses a structured lock representation:

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

The existing exact-pin interpreter correctly returns unsupported for S001 because `uv.lock` does not contain full `package==version` lines. Adding a Soup Sieve-, Pydantic-, or S001-specific patch rule would violate minimum useful generality. Continuing downstream relevance work without correcting the foundation would leave package identity, release intervals, CI evidence, and target comparison dependent on one incidental representation.

The project-wide requirement remains:

> Bound the supported domain, not the known fixture.

This does not require every Python packaging format. It requires a representation-neutral product contract and a credible extension mechanism within a deliberately admitted domain.

## Relationship to B2 and B4

The controlling route requires B2 to identify one supported Python dependency-version change without repository-specific hardcoding. It does not require universal dependency support.

B4 later owns broader expansion across:

- dependency declarations and locks;
- direct and transitive relationships;
- role and path evidence;
- repository usage;
- richer CI responsibility;
- version and constraint comparisons;
- target activation and action changes.

This plan therefore admits only enough architectural breadth to prevent B2 from being representation-specific:

1. preserve the validated exact-pin path;
2. admit one materially different structured Python lock representation;
3. produce one common downstream contract;
4. make later representations additive rather than another redesign;
5. defer graph, role, broad package-manager, and multi-update behavior to B4.

## First bounded scope

### Included

- public GitHub-hosted Python repositories;
- Dependabot pull requests with exact base/head identity;
- complete changed-file evidence;
- exactly one supported dependency-version transition;
- normalized Python distribution-name identity;
- exact raw old and proposed version strings;
- source-specific deterministic interpreters;
- deterministic reconciliation of interpreter results;
- exact provenance, including changed path, revision, and blob identity where acquired;
- explicit unsupported, malformed, incomplete, ambiguous, multiple, and conflicting states;
- existing exact-pin requirement transitions;
- modified same-path `uv.lock` base/head transitions;
- controlled tests and safe public S004/S001 validation;
- no new runtime dependency for this foundation.

### Excluded

- grouped or multi-package Dependabot updates;
- arbitrary selection from several changed dependencies;
- requirement ranges, editable installs, extras, markers, URLs, VCS references, or local paths as trusted version transitions;
- `poetry.lock`, `pdm.lock`, Pipenv, Conda, or universal lockfile support;
- added, deleted, or renamed lockfiles in the first boundary;
- package-source alias resolution across registries;
- dependency graph, direct/transitive, group, extra, or runtime-role interpretation;
- repository usage analysis;
- broad CI interpretation for lock-based installs;
- package compatibility, target relevance, safety, or maintainer action;
- LLM or model involvement in dependency representation parsing;
- target-repository mutation.

## Recommended durable architecture

This architecture is consequential and cross-cutting. It should be accepted through an ADR before implementation after Ali reviews the unresolved decisions in this plan.

### 1. Source-neutral canonical contract

Downstream modules should consume one representation-neutral semantic result, conceptually:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── evidence_sources[]
│   ├── representation_kind
│   ├── path
│   ├── base revision/blob when applicable
│   ├── head revision/blob when applicable
│   └── interpretation identity
└── limitations[]
```

The canonical contract represents only:

> One Python distribution was established to change from one exact version string to another.

It must not imply:

- why the package is present;
- whether it is direct or transitive;
- which environment installs it;
- which CI command exercised it;
- whether the update is compatible or safe.

The existing name `PinnedDependencyChange` reflects one source grammar. The recommended representation-neutral name is:

```text
DependencyVersionChange
```

### 2. Source-specific interpreters

Each admitted representation owns its own structure, authority, applicability, and failure semantics.

```text
exact-pin patch interpreter
→ candidate dependency transition or source-specific problem

uv.lock base/head interpreter
→ candidate dependency transition or source-specific problem
```

A source-specific interpreter must not become a repository-specific interpreter. It may recognize a defined file/grammar family; it must not recognize Pydantic, Soup Sieve, glyphsLib, pytest, known SHAs, or expected answers.

### 3. Candidate versus trusted change

An interpreter result is not automatically the final product identity. Conceptually:

```text
DependencyTransitionCandidate
→ source-specific evidence interpretation

DependencyVersionChange
→ reconciled trusted downstream input
```

This separation is useful because two representations may:

- identify the same transition;
- identify different transitions;
- contain several transitions;
- be malformed or incomplete;
- be inapplicable.

### 4. Deterministic reconciliation

The reconciler should apply these rules:

```text
no applicable supported candidate
→ unsupported dependency change

one supported candidate
→ trusted canonical change

multiple candidates with identical normalized package, old version, and proposed version
→ one trusted canonical change with combined provenance

multiple candidates with different semantic transitions
→ conflicting dependency evidence

one recognized representation is malformed or incomplete
→ preserve the problem; do not ignore it merely because another adapter produced a convenient answer

multiple dependency transitions inside the admitted evidence
→ explicit multiple_dependency_changes; do not select one heuristically
```

`not_applicable` must remain distinct from `malformed`, `unavailable`, `incomplete`, or `conflicting`.

## Representation 1 — exact-pin requirement patch

The existing deterministic behavior should be preserved as the first adapter:

```text
-package==old_version
+package==new_version
```

### Preserved invariants

- complete changed-file patch evidence;
- visible additions/deletions reconcile with GitHub metadata;
- one removed and one added exact pin;
- same modified file;
- normalized package identity matches;
- version changes;
- richer syntax remains unsupported;
- ambiguity is not guessed.

### Eligibility decision that must be frozen

The existing implementation scans all changed files for full exact-pin lines. That is simple, but an arbitrary documentation or example file could contain the same text.

Recommended first policy:

> Invoke the exact-pin interpreter only for a bounded requirements/constraints file family whose path semantics are frozen and tested.

Candidate filename rules to compare before implementation:

1. `requirements*.txt` and `requirements*.in`;
2. `constraints*.txt` and `constraints*.in`;
3. explicitly configured Dependabot `pip` manifest paths when that public metadata is reliably available;
4. the existing any-file scan as a compatibility baseline, not the preferred final policy.

The selected rule must avoid both known-fixture allowlisting and arbitrary text-file false positives.

## Representation 2 — `uv.lock` exact base/head interpretation

### Acquisition boundary

Do not interpret a structured lock transition from patch proximity alone. Acquire the complete same-path file at both immutable PR revisions:

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
- UTF-8 and TOML validity.

The existing repository client provides exact-head text acquisition. This plan requires source-neutral exact-base and exact-head acquisition mechanics, while validation must prevent arbitrary or branch-moving refs from entering the evidence chain.

### File-size decision

The existing repository text reader accepts at most 1,000,000 decoded bytes. Real lockfiles can be materially larger.

Before implementation:

1. measure S001 base/head `uv.lock` byte sizes;
2. compare the existing contents-API path with an exact-blob path if required;
3. select a justified bounded maximum;
4. preserve explicit `file_too_large` or equivalent evidence;
5. do not remove bounds merely to make one case pass.

### Parsed structure

Use Python 3.12 `tomllib`; do not add a TOML dependency.

The first adapter may consume only:

```toml
[[package]]
name = "distribution-name"
version = "exact-version"
source = { ... }  # preserved only as bounded identity context where usable
```

Artifact URLs, hashes, wheel lists, and upload times may change with the package version. They are evidence attached to the same package record; they must not be misclassified as separate dependency transitions.

### Package identity recommendation

A `uv.lock` file may contain repeated normalized names under different sources, markers, or resolution contexts. Building a universal lock identity model is outside this plan.

Recommended first rule:

> A normalized package name is admissible only when it identifies one unambiguous version-bearing package record in each exact file for the compared transition.

If duplicate normalized names prevent one-to-one comparison, return:

```text
ambiguous_lock_package_identity
```

Do not select the first record or collapse different sources silently.

### Transition rule

The first `uv.lock` adapter should require:

- same modified path `uv.lock` at base and head;
- both files available and valid TOML;
- valid package lists;
- textual non-empty `name` and `version` for admitted records;
- exactly one unambiguous normalized package whose exact version value changes;
- no unrelated package addition/removal/version change that would make the PR a multi-change case;
- old and proposed versions differ.

Expected S001 semantic candidate:

```text
package: soupsieve
normalized_package: soupsieve
old_version: 2.6
proposed_version: 2.8.4
representation: uv_lock
base path/revision/blob: preserved
head path/revision/blob: preserved
```

Version strings remain raw identity values at this stage. PEP 440 ordering belongs to later package/release-interval work and must not be smuggled into dependency-change recognition.

## Evidence path versus CI consumption

The existing exact-pin result exposes `source_file`, and the CI-authority rule can treat that file as an explicitly installed requirements file.

That meaning does not generalize automatically:

```text
requirements-dev.txt
→ may be explicitly installed with pip -r requirements-dev.txt

uv.lock
→ may be consumed implicitly by uv sync or another tool command
```

The canonical contract must therefore distinguish:

```text
change evidence path
≠
proven CI install input
```

Recommended rule:

- dependency interpretation records where the transition was established;
- CI authority separately proves how a workflow consumed that representation;
- the exact-pin CI rule remains unchanged for its admitted command form;
- `uv.lock` must produce an explicit unresolved/unsupported CI-authority reason until a separately bounded `uv` consumption rule is selected and tested;
- a lockfile path must never be treated as directly installed merely because it contains the change.

This plan may perform the minimum type/interface correction required to prevent false authority. It must not broaden into full `uv` command, workspace, group, or environment interpretation.

## Problem and abstention model

The exact final enum/type names should be frozen before code, but the foundation must preserve at least these meanings:

```text
no_supported_representation
missing_patch_evidence
incomplete_patch_evidence
unsupported_requirement_syntax
unsupported_file_status
source_file_unavailable
source_file_too_large
malformed_structured_source
invalid_package_record
ambiguous_package_identity
unchanged_version
multiple_dependency_changes
conflicting_dependency_evidence
```

Where an existing reason already has the same meaning, preserve it or provide a deliberate migration rather than changing user-visible diagnostics casually.

A valid unsupported representation is not malformed. A malformed recognized source is not merely inapplicable. A multi-change PR is not the same as conflicting representations.

## Dependency and module boundary

No new runtime dependency is required:

- `tomllib` parses `uv.lock`;
- existing GitHub and standard-library mechanics remain sufficient;
- package-name normalization may retain the existing PEP 503-compatible deterministic rule until a separately admitted dependency replaces it.

ADR-0001 requires cohesive modules directly under `src/upgradepilot/` until implemented responsibility demonstrates a subpackage boundary.

Recommended initial physical structure:

```text
src/upgradepilot/dependency_change.py
→ canonical contracts and reconciliation

src/upgradepilot/exact_pin_dependency.py
→ exact-pin patch interpretation

src/upgradepilot/uv_lock_dependency.py
→ uv.lock base/head interpretation

src/upgradepilot/github_repository.py
→ source-neutral exact PR base/head text acquisition
```

Do not create a package-manager framework, plugin registry, dynamic discovery system, or dependency subpackage merely to anticipate future adapters.

## Decision gate before source implementation

Ali should approve or revise these durable choices before code begins:

1. **Canonical contract:** use one representation-neutral `DependencyVersionChange` downstream.
2. **Adapter architecture:** source-specific deterministic interpreters produce candidates; a deterministic reconciler produces the trusted result.
3. **First admitted representations:** exact-pin requirements/constraints plus modified same-path `uv.lock`.
4. **Exactly-one boundary:** multiple package transitions remain explicit and unsupported in B2.
5. **Consistent evidence:** semantically identical candidates combine provenance.
6. **Conflicting evidence:** different candidates produce conflict; no priority-based guess.
7. **Duplicate lock identities:** abstain when normalized names are not uniquely comparable.
8. **CI separation:** change evidence path does not imply CI consumption.
9. **File eligibility:** replace arbitrary-file exact-pin scanning with a bounded source-family rule.
10. **File-size bound:** measure and select a justified bounded acquisition method for real lockfiles.
11. **ADR requirement:** record the accepted representation policy as a durable cross-cutting ADR before implementation.

## Work sequence

### Step 1 — Record the architecture decision

After Ali approves or revises the decision gate:

- create the representation-policy ADR;
- compare the existing monolithic exact-pin function, a giant multi-format parser, and the selected adapter/reconciler architecture;
- record consequences, failure modes, reversibility, and reassessment triggers;
- update the architecture register.

Do not claim implementation from ADR acceptance.

### Step 2 — Freeze canonical contracts and diagnostics

Define and test the representation-neutral result, candidate, evidence-source, and problem contracts.

Requirements:

- downstream package/version fields remain straightforward;
- evidence provenance is representation-aware;
- exact-pin user-visible behavior is preserved where meaning is unchanged;
- change-evidence paths are not mislabeled as CI install evidence;
- no repository/package/version fixtures enter production types.

### Step 3 — Extract the exact-pin interpreter

Move the validated exact-pin behavior behind the source-specific interface without changing its semantic result.

Prove:

- S004 controlled tests still pass;
- complete-patch and ambiguity protections remain;
- file eligibility is bounded to the selected source family;
- downstream package, CI, PyPI, and upstream behavior remains unchanged for the supported exact-pin case.

### Step 4 — Add deterministic reconciliation

Implement candidate collection and reconciliation independently of `uv.lock`.

Controlled tests must prove:

- zero candidates;
- one candidate;
- two equivalent candidates with combined provenance;
- two conflicting candidates;
- recognized malformed evidence is not silently ignored;
- multiple transitions do not collapse to one.

### Step 5 — Add exact base/head repository-file acquisition

Extend source-neutral repository acquisition to the exact PR base and head revisions.

Prove:

- only the frozen PR base/head SHAs are admitted;
- path and returned identity reconcile;
- blob SHAs and revision are preserved;
- missing/inaccessible base and head remain distinct evidence;
- byte bounds, base64, UTF-8, and response-shape errors remain explicit;
- workflow and target exact-head acquisition regressions remain green.

Measure the exact S001 lockfile sizes before selecting the final byte limit or blob path.

### Step 6 — Implement the bounded `uv.lock` interpreter

Use controlled complete-file fixtures first.

Prove:

- one exact version transition;
- unchanged package;
- package addition/removal;
- several version transitions;
- malformed TOML;
- missing or invalid package records;
- duplicate normalized package names;
- differing sources or ambiguous identities;
- base/head provenance;
- artifact metadata changes do not create extra dependency transitions;
- no S001 identifiers are hardcoded.

### Step 7 — Integrate the canonical result into CLI orchestration

Preserve the public command and exact PR acquisition.

Expected bounded outcomes:

```text
S004
→ exact-pin candidate
→ canonical DependencyVersionChange
→ existing target/CI/package/upstream behavior preserved

S001
→ uv.lock candidate
→ canonical DependencyVersionChange
→ target declaration and package/upstream stages may proceed
→ CI authority remains explicit and may be unresolved for unsupported lock-consumption semantics
```

Do not implement Python support-drop comparison, upstream interval acquisition, or LLM extraction in this step.

### Step 8 — Validate controlled and public behavior

Run:

1. narrow adapter and reconciliation tests;
2. repository acquisition tests;
3. dependency/CLI integration tests;
4. the complete deterministic suite;
5. installed S004 public read-only command;
6. installed S001 public read-only command.

The public proof must state exactly what advanced and where the product still abstains.

### Step 9 — Return to target Python relevance

Only after the foundation is behavior-validated:

- restore [`B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md) as the selected bounded plan through `MEMORY.md`;
- continue upstream interval/source, trusted claim, `packaging`, relevance, and conditional activation work;
- use S001 as the end-to-end relevance case without reopening historical product simulation.

## Proof obligations

The implementation must prove:

1. production logic contains no S001, S004, repository, package, version, SHA, or expected-result hardcoding;
2. the supported domain is expressed by representation rules, not known fixtures;
3. S004 and equivalent exact-pin variations normalize to the same canonical contract;
4. S001 and equivalent `uv.lock` variations normalize to the same canonical contract;
5. changed package spelling normalizes under the accepted distribution-name rule;
6. raw old/proposed versions are preserved exactly;
7. exact base/head/path/blob evidence is attached where structured comparison requires it;
8. malformed, unavailable, too-large, incomplete, unsupported, multiple, ambiguous, and conflicting states remain distinguishable;
9. multiple packages are never reduced to one by heuristic selection;
10. consistent multi-source evidence combines provenance without inventing stronger meaning;
11. conflicting evidence cannot reach downstream package/upstream analysis as trusted identity;
12. change evidence path is not treated as proof of CI consumption;
13. the existing exact-pin CI-authority behavior remains unchanged for its admitted form;
14. `uv.lock` CI authority remains unresolved unless separately proven;
15. no new runtime dependency is introduced;
16. the complete deterministic suite remains green;
17. the installed S004 command preserves its prior behavior-valid evidence chain;
18. the installed S001 command establishes the dependency transition and reaches only downstream stages supported by their own evidence rules;
19. plans, ADRs, tests, and live output do not claim compatibility, safety, recommendation correctness, production readiness, or Ali-owned mastery beyond evidence.

## Rejection and reframing conditions

Reframe or stop this plan if:

- a canonical transition cannot serve existing package/upstream consumers without hiding representation-specific meaning;
- `uv.lock` identity requires broad graph/resolution semantics before one exact transition can be established;
- real lockfile size requires effectively unbounded acquisition;
- duplicate/marker/source behavior cannot be kept honest through conservative abstention;
- the adapter/reconciler architecture adds more complexity than the second representation justifies;
- preserving existing exact-pin behavior requires repository-specific exceptions;
- downstream CI code cannot be prevented from confusing evidence paths with install authority without broad B4 work;
- the work begins implementing general package-manager support, dependency graphs, or role analysis;
- the selected proof cases no longer expose the intended responsibility at their exact revisions.

A rejection may leave the exact-pin path intact and record S001 as unsupported. It must not manufacture support through patch heuristics.

## Stop line

Stop this plan when UpgradePilot can demonstrate:

```text
one canonical dependency-version change contract
+
exact-pin requirement interpretation
+
modified same-path uv.lock interpretation
+
deterministic reconciliation and explicit conflict/multiple states
+
exact evidence provenance
→
S004 preserved
and
S001 dependency transition established
```

At this stop line, the plan does **not** establish:

- broad Python dependency declaration/lock support;
- direct/transitive or role/path analysis;
- `uv` CI consumption authority;
- package compatibility;
- authoritative crossed-release acquisition;
- upstream semantic extraction;
- Python support-drop relevance;
- safety or maintainer action.

Those responsibilities remain with later selected plans and B4.

## Maintenance

Change this plan only when its owning dependency-change responsibility, admitted representations, canonical contract, reconciliation policy, source acquisition boundary, proof obligations, rejection conditions, or stop line changes.

Do not record active status, latest commit, current blocker, completed step, or immediate continuation here. Those facts belong only in [`../MEMORY.md`](../MEMORY.md).
