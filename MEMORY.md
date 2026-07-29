# UpgradePilot Current Memory

**Last updated:** 2026-07-30 01:27 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Downstream dependent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Naming control:** [`docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)
- **Latest decision evidence:** [`working-memory/2026-07-30_0127_B2-dependency-file-rules-cluster-2.md`](working-memory/2026-07-30_0127_B2-dependency-file-rules-cluster-2.md)
- **Previous decision evidence:** [`working-memory/2026-07-29_2213_B2-dependency-evidence-naming-and-cluster-1.md`](working-memory/2026-07-29_2213_B2-dependency-evidence-naming-and-cluster-1.md)
- **Planning evidence:** [`working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md`](working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md)
- **Latest relevant non-memory revision:** `9e4ffed0de5d2c41aa8ef45ac7b6e927ff8fcbe8`.

Use local `HHMM` after the date for additional same-day working-memory records. Existing files are not renamed merely to retrofit the convention.

## Why this plan is selected

S001 is the real Python-support relevance proof case:

```text
pydantic/pydantic PR 13432
Soup Sieve 2.6 → 2.8.4
upstream: Drop support for Python 3.8.
target: requires-python >=3.10
expected bounded relevance: outside_declared_python_range
```

The active dependency code accepts only complete same-file exact requirement changes:

```text
-package==old_version
+package==new_version
```

S001 changes a structured `uv.lock` package record. The current product therefore stops before it can establish S001's dependency identity.

Dependency version identity feeds CI, package, upstream, release-interval, target, and later decision work. The selected plan corrects that evidence responsibility before further Python-support relevance implementation.

## Behavior-validated product boundary

Target-declaration Step 1 remains behavior-validated at product revision:

```text
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15
```

Ali ran the complete deterministic suite:

```text
Ran 72 tests
OK
```

One installed public read-only S004 command preserved the existing evidence pipeline and produced the expected target state.

UpgradePilot behavior-validly reaches:

```text
public repository + Dependabot PR
→ exact PR identity and complete changed files
→ one supported same-file package==version transition
→ exact-head pyproject.toml target declaration evidence
→ exact-head workflow/job/step evidence
→ bounded CI-authority classification
→ exact PyPI package/version/file identity
→ PyPI-reported file source evidence
→ matching GitHub upstream repository
→ exact proposed-version release and tag reference
→ bounded release body
→ concise CLI evidence report
→ unresolved_claim
```

S004 target evidence remains:

```text
repository: googlefonts/glyphsLib
PR: 1145
revision: f3cda8a94600e58d27f1bc17c99b7693718b6350
path: pyproject.toml
blob: 38d6a9efc4b94e2b733d3bbb848156449814ec94
result: project_table_absent
```

No compatibility or safety claim followed.

## Naming clarity decision

The accepted naming rule is:

> Prefer the clearest concrete name that communicates the owned fact, action, or responsibility with minimal project-specific decoding.

Preferred dependency evidence vocabulary:

```text
DependencyVersionChange
→ trusted record that one package changed from one exact version to another

ExtractedDependencyVersionChange
→ possible change extracted from one supported dependency file

DependencyChangeSourceEvidence
→ exact file, revision, blob, and extraction method supporting the change

extract_exact_requirement_changes
→ read package==version patch changes

extract_uv_lock_changes
→ compare exact base/head uv.lock records

compare_extracted_dependency_changes
→ determine agreement, conflict, or several package changes
```

The existing source type `PinnedDependencyChange` remains implemented truth until a tested refactor replaces it. Historical records are not mass-rewritten solely for vocabulary modernization.

## Decision Cluster 1 — accepted architecture rules

### Trusted downstream record

Use one file-format-independent:

```text
DependencyVersionChange
```

It contains package identity, exact raw old/proposed versions, and supporting source evidence. It does not imply dependency role, target usage, CI consumption, compatibility, safety, or maintainer action.

### Source-specific extraction and comparison

```text
supported dependency file
→ clearly named extraction function
→ ExtractedDependencyVersionChange or source problem

all extracted changes and recognized source problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

Do not build a giant multi-format parser or case-specific CLI branches.

### Exactly one B2 dependency change

```text
one package version change
→ eligible for downstream evidence work

several package version changes
→ multiple_dependency_version_changes
```

Do not choose one package using title, patch order, known package identity, or convenience.

### Equivalent, conflicting, and malformed evidence

- same normalized package plus exact raw old/proposed versions → one trusted record with all source evidence;
- different package/version changes → `conflicting_dependency_version_changes`;
- one recognized malformed, unavailable, incomplete, or too-large dependency file prevents a trusted result even when another file produces a convenient change.

## Decision Cluster 2 — accepted dependency-file rules

### Exact requirements and constraints paths

Admit lowercase conventional descriptive filenames:

```text
requirements.txt / requirements.in
requirements-<description>.txt/.in
requirements_<description>.txt/.in
requirements.<description>.txt/.in

constraints.txt / constraints.in
constraints-<description>.txt/.in
constraints_<description>.txt/.in
constraints.<description>.txt/.in
```

Also admit `.txt` and `.in` descendants under a directory component named exactly `requirements` or `constraints`.

The rules apply at any repository depth and preserve the complete relative path. Repository-specific path allowlists are prohibited.

Path eligibility establishes only that the file may supply exact package/version evidence. It does not establish runtime/development/test/docs/fixture role, installation, CI consumption, compatibility, or safety.

### Requirements versus constraints

Both may establish an exact package version change. A constraints file may limit selection without requesting installation, so it must not become direct install evidence merely because it contains the changed version.

### `uv.lock` duplicate groups

```text
one record in base + one record in head
→ compare normally

repeated-name group unchanged under admitted identity comparison
→ does not block an unrelated clear change

repeated-name group differs between base and head
→ ambiguous_uv_lock_package_records
```

Do not select the first record, pair records by list position, or collapse different source, marker, or resolution contexts.

The exact fields used only to prove an unchanged duplicate group remain to be frozen in the ADR and tests. Artifact URLs, hashes, wheel lists, sizes, and upload times must not create false package-version changes.

### `uv.lock` path and status

First support requires:

```text
GitHub status: modified
basename: uv.lock
same complete relative path at base and head
both exact files available
```

Nested same-path lockfiles are eligible. Added, deleted, and renamed lockfiles remain outside the first rule.

Do not reopen Decision Clusters 1 or 2 unless implementation evidence exposes a concrete contradiction.

## Remaining decisions before ADR or code

1. exact raw-version validation and where later PEP 440 parsing and ordering begin;
2. CI result behavior when a supported dependency file's consumption is not established;
3. exact S001 base/head lockfile sizes, endpoint, and bounded acquisition maximum;
4. exact identity fields used only to prove an unchanged duplicate `uv.lock` group;
5. final clear source type, function, problem, module, and CLI names;
6. ADR alternatives, consequences, reversal, and reassessment triggers.

No product source or tests are authorized until these material boundaries are resolved and the architecture ADR is accepted.

## Downstream work retained but paused

The accepted Python range direction remains:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
```

No `packaging` dependency has yet been added. The exact stable Python-line overlap algorithm remains unresolved.

The eventual semantic order remains:

```text
trusted DependencyVersionChange
→ package and upstream identity
→ authoritative old-version-exclusive/proposed-version-inclusive upstream evidence
→ candidate support-drop extraction
→ deterministic claim validation
→ valid Python support-drop claim?
    ├── no  → target Python investigation not activated
    └── yes → exact-head pyproject.toml
              → requires-python evidence
              → packaging-based comparison
```

Instructor, Pydantic, OpenAI client, LM Studio, and a model remain unadopted. Local-LLM work remains paused.

Do not refactor target activation during the dependency version change evidence plan.

## Not established

- selected rules implemented in source or tests;
- `DependencyVersionChange` or other new records in runtime code;
- path eligibility enforcement;
- constraints-file product support;
- exact PR base/head generic file acquisition;
- bounded large-lockfile acquisition;
- `uv.lock` extraction;
- duplicate-group comparison;
- S001 dependency identity through the product;
- requirements, constraints, or uv CI consumption beyond existing exact-requirement behavior;
- PEP 440 dependency-version ordering boundary;
- architecture ADR;
- crossed-version upstream acquisition;
- reliable Python support-drop extraction;
- target/upstream relevance comparison;
- compatibility, safety, or maintainer action;
- production readiness or Ali-owned mastery.

## Exact continuation

Proceed with one coherent operational-boundary discussion:

1. explain why exact observed version strings and PEP 440 ordering are separate responsibilities;
2. decide whether dependency extraction validates only non-empty exact strings or also PEP 440 syntax;
3. decide where proposed-version ordering and old/proposed release interval validation begin;
4. define the honest CI result when requirements, constraints, or `uv.lock` consumption is not proven;
5. only after those decisions, measure the exact S001 base/head `uv.lock` sizes and select a bounded acquisition method;
6. freeze duplicate-group equality fields and final names;
7. create the ADR after all material rules are resolved.

Do not create the ADR or write product code during the next discussion.

## Relevant revisions

```text
Step 1 behavior-validated product:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Naming clarity specification:
06caa57eb91a228cd60d6cef2a2c34a0d4211bc7

Clearly named dependency evidence plan created:
a95caa35e7483fca3c566e66247d99a1226ee460

Decision Cluster 1 evidence:
b00f6477c481ef6f26a8fc2f0427b080f160df48

Dependency-file rules added to selected plan:
69dd9040fb5e8265163f2d491a8d14f6d419b6f1

Decision Cluster 2 evidence:
9e4ffed0de5d2c41aa8ef45ac7b6e927ff8fcbe8
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
