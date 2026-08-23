# B2 R2 — uv.lock structural model initial slice

**Date:** 2026-08-24  
**Branch:** `agent/r2-uv-lock-structural-model`  
**Base:** `d92e8d263e856c3dde3e6dc5ddcd99ce1f7d0288`  
**State:** R2 IN PROGRESS — initial structural-owner implementation complete; runtime validation pending  
**Authority:** working evidence only; `MEMORY.md` remains the sole live-state owner.

## Bounded question

R2 asks for the smallest uv-specific owner that establishes external `uv.lock` structural truth once while preserving two separate semantic responsibilities:

```text
exact base/head uv.lock
→ dependency-transition semantics

exact head uv.lock + explicit selector/project evidence
→ explicit-root reachability semantics
```

It must not introduce a generic dependency graph/package-manager layer, workspace-scope semantics, a complete uv interpreter, resolver/currentness evidence, or R4 reachability-contract redesign.

## Evaluative trace

Current source before R2 contained two independent lock parsers.

`dependency/uv_lock.py` interpreted:

```text
TOML
schema version
lock revision
package records
package names
package versions
versionless editable/virtual source admission
normalized-name groups / repeated records
```

and then separately owned base/head transition comparison.

`dependency/uv_membership.py` independently interpreted:

```text
TOML
schema version
lock revision
package records
package names
package versions
package sources
resolution markers
dependency edges
optional/dev root tables
edge markers/extras
```

and then owned project binding, selected roots, deterministic edge resolution, and bounded traversal.

The duplicated core structural admission had already drifted:

```text
uv_lock.py
missing package version
→ admitted only for exact one-key editable/virtual local source

uv_membership.py
missing package version
→ admitted regardless of source
```

A second source-level inconsistency was found during R2 inspection: membership used `document.get("version") != 1`, so TOML `version = true` could compare equal to integer `1` in Python.

## Rationale / JUST disposition

The earliest sufficient shared owner is the uv lock format boundary, not either semantic consumer.

Under `JUST-001` through `JUST-005`:

- existing duplicate parsers are not retained merely because tests/callers already exercise them;
- schema/package admission is one proposition and therefore should not be independently re-proved by both consumers;
- transition comparison remains independently necessary because it answers a base/head change proposition;
- reachability edge/root projection and traversal remain independently necessary because they answer a selected-root reachability proposition;
- R3 workspace scope and R4 proposition/naming changes are not pulled into R2.

The initial design deliberately centralizes only genuinely shared structural facts. Reachability-only dependency-edge/root interpretation remains in `uv_membership.py`; moving it merely because it is lock-shaped would enlarge the shared owner without eliminating duplication.

## Implemented structure

Added:

```text
src/upgradepilot/dependency/uv_lock_structure.py
```

Shared model:

```text
UvLockStructure
├── schema_version
├── revision
├── packages
└── by_name

UvLockPackageRecord
├── index
├── package
├── normalized_package
├── version
├── source
└── record_data
```

Shared structural problems remain uv-specific and consumer-neutral:

```text
malformed_uv_lock
unsupported_uv_lock_schema
invalid_uv_lock_package_record
```

The shared parser now owns:

```text
TOML admission
exact-int schema-version admission
schema version 1 boundary
non-negative exact-int lock revision
package array/table admission
distribution-name admission
package textual-version admission
versionless editable/virtual local-source exception
normalized package grouping
preservation of repeated records and raw package structure
```

It does **not** own:

```text
base/head package pairing
artifact-only comparison rules
transition extraction
selected group/extra semantics
project binding
edge resolution/traversal
workspace scope
lock currentness/resolution/runtime behavior
```

## Consumer migration

### Transition consumer

`dependency/uv_lock.py` now:

```text
exact base/head RepositoryTextFile
→ parse_uv_lock_structure() for each side
→ map structural failure to existing dependency problem vocabulary
→ compare admitted package groups
→ preserve current transition/repeated-record/canonical comparison semantics
```

The old duplicate TOML/schema/package/version/versionless parser was removed.

### Reachability consumer

`dependency/uv_membership.py` now:

```text
exact head RepositoryTextFile
→ parse_uv_lock_structure()
→ reachability-specific projection of markers/edges/optional/dev roots
→ existing project binding + selected-root traversal
```

Package name/version/source admission is no longer reimplemented there. Existing cross-object composition checks remain because they bind independently produced dependency/workflow/project/lock evidence rather than repeating intrinsic lock parsing.

## Focused regression added

Added:

```text
tests/test_uv_lock_structure.py
```

It protects:

- valid versionless editable workspace admission;
- repeated normalized-name record preservation;
- one shared rejection for a versionless registry record;
- transition consumer mapping of that rejection to `invalid_dependency_record`;
- membership consumer mapping of the same rejection to `uv_membership_lock_structure_unresolved`;
- TOML boolean schema value not being admitted as integer schema 1;
- unsupported integer schema version remaining distinct;
- untrimmed package version remaining invalid structural evidence.

## Current Git evidence

After the focused implementation/test commits, branch comparison against the R2 base reported:

```text
status: ahead
behind_by: 0
files:
  src/upgradepilot/dependency/uv_lock.py
  src/upgradepilot/dependency/uv_lock_structure.py
  src/upgradepilot/dependency/uv_membership.py
  tests/test_uv_lock_structure.py
```

Initial implementation/test head before this working-memory commit:

```text
77575e3558c6425066047b5e3201e61f8665d0d9
```

## Validation state / next action

No runtime acceptance is claimed yet. The next required evidence is narrow-to-broad local execution in the established project environment:

```text
new shared-structure regression
+ existing uv transition/versionless suites
+ existing uv reachability/universal-lock suites
→ then standard suite
→ then compileall as justified by the active plan
```

If focused runtime exposes a regression, diagnose/fix inside R2 before broadening. R2 must not be marked complete until runtime evidence is green and the final ownership/diff review finds no unexplained structural drift or accidental R3/R4 scope.
