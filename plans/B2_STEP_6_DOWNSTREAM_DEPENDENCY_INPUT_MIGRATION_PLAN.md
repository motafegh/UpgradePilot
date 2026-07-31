# B2 Step 6 — Downstream Dependency Input Migration Plan

**Status:** Approved and controlling for Step 6  
**Owner:** Ali Rajabi  
**Parent plan:** [`B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)  
**Architecture control:** [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)  
**Current validated boundary:** Steps 1–5 complete; Step 5 validated at repository state `0925b9e2bf146be920f50f584201f346094743f0`

## Purpose

Migrate downstream product code from the legacy exact-requirements-specific record:

```text
PinnedDependencyChange
```

to the shared PR-wide trusted record:

```text
DependencyVersionChange
```

without changing the meaning of existing S004 behavior, pretending that a dependency-evidence path proves CI installation, or prematurely integrating the full `uv.lock` command path.

This step prepares a stable downstream boundary so later dependency formats that establish the same bounded meaning can be added through source-specific adapters and one coordinator rather than through per-format branches across the CLI, package, upstream, target, and decision stages.

## Owning question

> Can every downstream identity consumer operate on one format-independent `DependencyVersionChange`, while the current direct-requirements CI rule receives its file-specific input explicitly rather than inferring installation from generic source evidence?

## Audit conclusion

The repository already contains the correct strategic architecture:

- ADR-0004 requires source-specific extraction followed by shared comparison;
- `DependencyVersionChange` is already the canonical trusted identity;
- direct per-format branching throughout downstream modules is explicitly rejected;
- `DependencyFileEvidence.path` is explicitly not proof of dependency role, installation, or CI consumption;
- constraints and `uv.lock` do not inherit requirements-file CI semantics;
- a dynamic plugin framework or registry is deliberately excluded at the current project depth.

The missing material was not another architecture decision. The missing material was an executable Step 6 contract: exact invariants, migration surface, compatibility boundary, tests, future-extension behavior, and stop line. This plan supplies that contract without superseding ADR-0004 or the parent plan.

## Current legacy coupling

The installed command currently follows:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
→ target Python
→ CI authority
→ PyPI package evidence
→ upstream evidence
→ CLI presentation
```

`PinnedDependencyChange` combines two different meanings:

```text
package/version identity
+
one direct-requirements CI assumption through source_file
```

That combination happened to fit S004:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
```

because the changed evidence file was also visibly installed by the admitted `pip -r <exact path>` CI rule.

It does not generalize to S001:

```text
uv.lock
soupsieve 2.6 → 2.8.4
```

because `uv.lock` identifies where the dependency transition was established but does not prove that a workflow consumed the lockfile or exercised the changed package.

## Target boundary

### Canonical downstream identity

All downstream identity consumers must receive:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

They must not require:

```text
PinnedDependencyChange
source_file
exact_requirement
uv_lock
another source-format discriminator
```

unless their own responsibility genuinely depends on source-specific evidence.

### Explicit CI consumption input

The current CI evaluator may continue using the existing `CIAuthorityResult` names and statuses during Step 6, but it must no longer obtain an install path from `PinnedDependencyChange` or choose a path from generic `source_evidence` by convenience.

Its Step 6 input boundary must distinguish:

```text
DependencyVersionChange
→ package/version identity

explicit direct-requirements install path
→ source-specific input for the existing pip -r rule
```

The explicit install-path input may be present only for the current admitted direct-requirements compatibility path. It must be absent for constraints, `uv.lock`, unknown formats, ambiguous paths, or any case in which the caller cannot establish the exact direct-requirements rule.

Step 7 will replace the legacy CI result vocabulary and finalize `DependencyCIExerciseResult` semantics. Step 6 must not perform that rename or claim `uv.lock` CI consumption.

## Required invariants

### Invariant 1 — One downstream identity type

```text
Target Python, package, upstream, and generic presentation consume
DependencyVersionChange, not PinnedDependencyChange.
```

### Invariant 2 — Source syntax stops before downstream identity work

```text
requirements syntax ─┐
constraints syntax  ─┼→ file-level results
uv.lock syntax      ─┘
                         ↓
          compare_extracted_dependency_changes
                         ↓
              DependencyVersionChange
```

No downstream package, upstream, or target module may branch on `file_format` merely to read package/version identity.

### Invariant 3 — Evidence path is not installation proof

```text
DependencyFileEvidence.path
≠
CI installation or consumption evidence
```

No code may automatically pass `source_evidence[0].path` into a requirements-install rule.

### Invariant 4 — Source-specific facts remain source evidence

Path, format, extraction method, base/head revision, blob, and byte identity remain inside `source_evidence[]`. They are not copied into canonical package/version fields.

### Invariant 5 — Generic presentation iterates evidence

The CLI presentation boundary must be capable of rendering zero, one, or several source-evidence records without a format-specific success branch for each source family.

### Invariant 6 — Same-meaning format additions remain localized

After Step 8 completes the command coordinator, a new source format that establishes the existing exactly-one-transition meaning should normally require only:

```text
recognizer
+ acquisition rule when needed
+ source-specific extractor
+ focused tests
+ one explicit coordinator registration/branch
```

It must not require redesigning package lookup, upstream resolution, target-Python acquisition, generic dependency presentation, or the canonical comparison contract.

### Invariant 7 — No premature plugin framework

The current project does not need dynamic discovery, entry points, reflection-based adapters, or a general plugin registry. Step 8 should use one explicit static coordinator whose supported formats are visible in ordinary source code and tests.

## Step 6 migration strategy

Step 6 is a downstream migration, not full source integration.

The current exact-requirements command path may remain the active ingress while its successful legacy result is converted at one compatibility boundary into:

```text
DependencyVersionChange
+
explicit direct-requirements install path
```

After that conversion, no downstream runtime code may receive `PinnedDependencyChange`.

A minimal tested compatibility adapter is acceptable during Step 6 when it:

- constructs `DependencyFileEvidence` with `file_format = exact_requirement`;
- uses `extraction_method = changed_file_patch`;
- preserves package, normalized package, and exact raw versions;
- supplies the legacy `source_file` separately as the explicit direct-requirements CI path;
- does not claim exact base/head blob evidence that the legacy patch path does not possess;
- contains no S004 repository, package, version, or expected-result condition.

The compatibility adapter is transitional. Step 8 will replace legacy command ingress with the real source-specific extraction and comparison coordinator, including `uv.lock` acquisition.

## Modification surface

### `src/upgradepilot/dependency_change.py`

Required:

- keep `DependencyVersionChange` as the canonical trusted record;
- add or expose one narrowly named tested compatibility conversion if needed;
- keep the existing legacy records and extractor only as an ingress compatibility boundary until command integration replaces them;
- document that no downstream module may depend on the legacy result after conversion.

Do not:

- add source-format branches to `DependencyVersionChange`;
- add CI install-path fields to the canonical record;
- perform PEP 440 interpretation;
- remove historical compatibility APIs before their callers and tests migrate.

### `src/upgradepilot/cli.py`

Required:

- narrow the legacy ingress result once;
- convert successful dependency identity to `DependencyVersionChange` immediately;
- use the canonical result for target, package, upstream, and presentation stages;
- pass the direct-requirements install path to CI explicitly and separately;
- render `Dependency evidence` by iterating `source_evidence[]`;
- preserve explicit stopping behavior when dependency identity is not established.

Step 6 does not yet:

- recognize and acquire `uv.lock` during normal command execution;
- run every source-specific extractor;
- call the PR-wide comparator across requirements and lockfiles;
- make `upgradepilot pydantic/pydantic 13432` the final S001 path.

Those are Step 8 responsibilities.

### `src/upgradepilot/ci_authority.py`

Required:

- replace the `PinnedDependencyChange` parameter with `DependencyVersionChange`;
- accept the current direct-requirements install path as a separate explicit input;
- use the canonical package and normalized package identity;
- preserve the current result names and validated S004 decision order until Step 7;
- refuse or remain unresolved when the explicit requirements-install input is absent rather than selecting a generic evidence path.

Do not:

- rename statuses to `proven`, `no_successful_ci`, and `unresolved` yet;
- implement `uv sync`, `uv run`, constraints consumption, or general workflow semantics;
- infer installability from a filename alone inside the generic evaluator.

### `src/upgradepilot/workflow_commands.py`

Expected:

- continue receiving an explicit source-specific requirements path and package identity;
- remain a command-inspection helper rather than a dependency-evidence interpreter.

Change only if required by the new explicit CI input shape. Do not make it inspect `DependencyFileEvidence` or choose a source record.

### `src/upgradepilot/__init__.py`

Required:

- keep the canonical shared contracts publicly available;
- export a compatibility conversion only if it is intentionally part of the supported transitional API;
- do not remove legacy exports until the repository no longer relies on them and the removal is explicitly selected.

### Tests

Primary affected tests:

```text
tests/test_cli.py
tests/test_ci_authority.py
tests/test_dependency_change.py
```

Possible focused compatibility coverage may use a new test file when that keeps responsibilities clearer.

Historical learning and working-memory files are not mass-renamed.

## Required Step 6 tests

### Canonical conversion

Prove that one generic legacy exact-requirements result converts to:

```text
DependencyVersionChange
+ one exact_requirement source-evidence record
+ one separate explicit direct-requirements install path
```

Prove no case or S004-specific identity is hardcoded.

### Downstream identity

Prove target, package, and upstream orchestration uses `DependencyVersionChange.package` and `.proposed_version` without accessing `source_file` or branching on format.

### Generic evidence presentation

Prove the CLI can render:

- one patch-based exact-requirement evidence record;
- one exact-base/head `uv_lock` evidence record supplied as a controlled canonical fixture;
- several equivalent evidence records;
- limitations when present.

The controlled `uv_lock` fixture in this test validates presentation only. It does not imply Step 8 command integration.

### Explicit CI input

Prove:

- the current S004-style explicit requirements path preserves sufficient CI authority;
- no explicit install path does not become sufficient merely because `source_evidence` contains a path;
- a `uv_lock` evidence path is never passed automatically to the `pip -r` rule;
- constraints evidence is not automatically treated as direct requirements installation evidence;
- package identity remains available even when CI exercise is unresolved.

### Legacy containment

Prove runtime and current tests no longer import or narrow `PinnedDependencyChange` outside:

```text
dependency_change.py compatibility boundary
exact_requirement_change.py legacy compatibility implementation
focused compatibility tests
```

The source tree may still contain the legacy record and historical documentation. The requirement is containment, not immediate deletion.

### Regression

Prove:

- existing S004 visible behavior remains materially intact;
- package and upstream failure paths preserve their current stopping behavior;
- unsupported dependency identity skips dependent stages;
- the complete deterministic suite remains green.

## Future-extension contract

### Category A — New syntax, same canonical meaning

Examples:

- another exact lockfile format;
- another bounded requirements syntax;
- another complete source that establishes one exact package transition.

Expected changes after Step 8:

```text
new adapter
+ tests
+ explicit coordinator branch
+ acquisition support when required
```

Expected unchanged:

```text
DependencyVersionChange
compare_extracted_dependency_changes
package lookup
upstream resolution
target-Python acquisition
generic dependency presentation
```

### Category B — New evidence semantics

Examples:

- `uv.lock` consumption through `uv sync` or `uv run`;
- constraints applied through `pip -c`;
- another package-manager installation command.

Expected changes:

```text
source-specific CI consumption rule
+ CI tests
+ workflow-command support when selected
```

Dependency extraction and package identity should remain unchanged.

### Category C — New product meaning

Examples:

- grouped multi-package updates;
- dependency graph roles;
- direct versus transitive dependency;
- environment-specific or platform-specific resolved transitions;
- changed duplicate resolver branches.

These meanings may legitimately require a new or extended canonical model and downstream changes. Step 6 must not create a vague universal abstraction to pretend otherwise.

## Build order

1. Freeze controlled tests for canonical conversion and explicit CI input.
2. Add the minimal compatibility conversion at the legacy ingress boundary.
3. Migrate `ci_authority.py` to canonical identity plus separate install-path input.
4. Migrate CLI target, package, upstream, and presentation stages to the canonical record.
5. Contain remaining legacy imports and update focused tests.
6. Run focused Step 6 tests.
7. Run all existing dependency, CLI, CI, package, target, and upstream regression tests.
8. Run the complete deterministic suite.
9. Run installed public S004 validation.
10. Record Step 6 validation and advance only to Step 7.

Do not combine Step 6 implementation with Step 7 result renaming or Step 8 multi-format command integration.

## Rejection and reframing conditions

Stop and reframe when:

- `DependencyVersionChange` cannot serve package, target, upstream, or presentation without adding source-format-specific identity fields;
- preserving S004 requires package- or repository-specific conditions;
- CI can remain sufficient only by choosing a generic evidence path automatically;
- the compatibility adapter begins duplicating source parsers or PR-wide comparison rules;
- Step 6 expands into full source coordination, `uv.lock` command integration, broad workflow interpretation, or dynamic plugin infrastructure;
- a new abstraction has no immediate Step 6 consumer or test.

## Step 6 stop line

Stop Step 6 when all of the following are true:

```text
all downstream identity consumers use DependencyVersionChange
+
PinnedDependencyChange is contained at the legacy ingress compatibility boundary
+
CI receives dependency identity and direct-requirements install path separately
+
no generic source-evidence path becomes installation proof
+
generic dependency-evidence presentation works for one or several records
+
S004 behavior remains intact
+
complete deterministic suite passes
```

Step 6 does not establish:

- one-line installed S001 behavior;
- normal CLI `uv.lock` recognition or exact-file acquisition;
- PR-wide comparison across all changed dependency formats during command execution;
- final CI result names or `uv.lock` consumption rules;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer action;
- a universal plugin system;
- user mastery.

## Exact continuation after approval

Begin implementation with read-only confirmation of the current blobs for:

```text
src/upgradepilot/dependency_change.py
src/upgradepilot/cli.py
src/upgradepilot/ci_authority.py
src/upgradepilot/workflow_commands.py
src/upgradepilot/__init__.py
tests/test_dependency_change.py
tests/test_cli.py
tests/test_ci_authority.py
```

Then add tests for the canonical conversion and explicit CI-input split before changing runtime source.
