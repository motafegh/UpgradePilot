# UpgradePilot Current Memory

**Last updated:** 2026-07-30 15:50 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Downstream package/upstream owner:** [`plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md`](plans/B2_MINIMUM_PACKAGE_AND_UPSTREAM_EVIDENCE_PLAN.md)
- **Downstream Python relevance plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Naming control:** [`docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)
- **Latest decision evidence:** [`working-memory/2026-07-30_1550_B2-version-and-ci-evidence-cluster-3.md`](working-memory/2026-07-30_1550_B2-version-and-ci-evidence-cluster-3.md)
- **Previous decision evidence:** [`working-memory/2026-07-30_0127_B2-dependency-file-rules-cluster-2.md`](working-memory/2026-07-30_0127_B2-dependency-file-rules-cluster-2.md)
- **Latest relevant non-memory revision:** `f07a35644cc5f355453725a3d0f81f553301b388`.

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
→ current bounded CI classification
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

The accepted rule is:

> Prefer the clearest concrete name that communicates the owned fact, action, or responsibility with minimal project-specific decoding.

Preferred selected-design vocabulary:

```text
DependencyVersionChange
→ trusted record that one package changed from one exact version string to another

ExtractedDependencyVersionChange
→ possible change extracted from one supported dependency file

DependencyChangeSourceEvidence
→ exact file, revision, blob, and extraction method supporting the change

compare_extracted_dependency_changes
→ determine agreement, conflict, or several package changes

DependencyCIExerciseResult
→ what exact-head CI evidence proves about consumption and exercise of the changed dependency
```

Existing source types such as `PinnedDependencyChange` and `CIAuthorityResult` remain implemented truth until a tested migration replaces them. Historical records are not mass-rewritten solely for vocabulary modernization.

## Decision Cluster 1 — accepted change-record architecture

```text
supported dependency file
→ clearly named extraction function
→ ExtractedDependencyVersionChange or source problem

all extracted changes and recognized source problems
→ compare_extracted_dependency_changes
→ DependencyVersionChange or explicit problem
```

Rules:

- B2 supports exactly one package version change;
- several changes produce `multiple_dependency_version_changes`;
- same normalized package plus exact raw old/proposed strings combines source evidence;
- different package/version changes produce `conflicting_dependency_version_changes`;
- a recognized malformed, unavailable, incomplete, or too-large dependency file prevents a trusted result even when another file produces a convenient change;
- do not build a giant multi-format parser or case-specific CLI branches.

## Decision Cluster 2 — accepted dependency-file rules

### Requirements and constraints paths

Admit conventional lowercase filenames:

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

Also admit `.txt` and `.in` descendants beneath a directory component named exactly `requirements` or `constraints`.

The rules apply at any repository depth and preserve the complete relative path. Path eligibility does not establish dependency role, installation, CI consumption, compatibility, or safety.

### `uv.lock` duplicate groups

```text
one record in base + one record in head
→ compare normally

repeated-name group unchanged under admitted identity comparison
→ does not block an unrelated clear change

repeated-name group differs between base and head
→ ambiguous_uv_lock_package_records
```

Do not select the first record, pair by list position, or collapse different source, marker, or resolution contexts.

### `uv.lock` path and status

First support requires:

```text
GitHub status: modified
basename: uv.lock
same complete relative path at base and head
both exact files available
```

Nested same-path lockfiles are eligible. Added, deleted, and renamed lockfiles remain outside the first rule.

## Decision Cluster 3 — accepted version and CI rules

### Exact version observation

Dependency-file extraction preserves exact raw old and proposed version strings.

It validates only:

- value exists;
- value is textual and non-empty;
- no leading or trailing whitespace;
- old and proposed strings differ.

Extraction does not perform PEP 440 validation, version ordering, package existence checks, or release-interval logic.

### PEP 440 boundary

PEP 440 validation begins in package/upstream work before official package release lookup and crossed-version ordering.

Selected method:

```text
packaging.version.Version
```

Raw and parsed values remain distinguishable.

Required later results include:

```text
invalid_python_package_version
equivalent_python_package_versions
dependency_version_not_forward
```

Invalid or non-forward Python package semantics block package release interval work. They do not erase the observed `DependencyVersionChange`.

`packaging` is not yet installed or admitted. Exact dependency bounds and behavior proof remain required.

### CI exercise result

Future clear result name:

```text
DependencyCIExerciseResult
```

Selected states:

```text
proven
no_successful_ci
unresolved
```

- `proven` — one completed successful exact-head CI path satisfies an admitted dependency-consumption and package-exercise rule;
- `no_successful_ci` — no completed successful exact-head job exists;
- `unresolved` — successful exact-head CI exists, but no admitted rule proves consumption and exercise of the changed dependency.

File-specific behavior:

- exact requirements files may use the existing direct `pip -r` plus direct package-invocation rule;
- constraints files do not inherit requirements-file install semantics;
- `uv.lock` does not inherit requirements-file install semantics;
- constraints-only or `uv.lock`-only evidence remains `unresolved` when successful CI exists until a separate bounded consumption rule is admitted;
- one admitted path may prove the narrow existential CI rule when several files support the same dependency change;
- unresolved CI does not erase dependency identity or automatically block package/upstream/target acquisition;
- unresolved CI must not be presented as green evidence.

Do not reopen Decision Clusters 1–3 unless implementation evidence exposes a concrete contradiction.

## Remaining decisions before ADR or code

1. measure exact S001 base/head `uv.lock` byte sizes;
2. compare contents-endpoint and exact-blob acquisition behavior;
3. select a justified bounded maximum file size;
4. freeze the exact minimal fields used only to prove an unchanged duplicate `uv.lock` group;
5. finalize clear source type, function, problem, module, and CLI names;
6. define ADR alternatives, consequences, reversal, and reassessment triggers.

No product source or tests are authorized until these boundaries are resolved and the architecture ADR is accepted.

## Downstream work retained but paused

The eventual semantic order remains:

```text
trusted DependencyVersionChange
→ valid forward PEP 440 old/proposed versions
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

No `packaging` dependency has yet been added. The exact stable Python-line overlap algorithm remains unresolved.

Instructor, Pydantic, OpenAI client, LM Studio, and a model remain unadopted. Local-LLM work remains paused.

Do not refactor target activation during the dependency version change evidence plan.

## Not established

- selected dependency evidence rules implemented in source or tests;
- `DependencyVersionChange` or `DependencyCIExerciseResult` in runtime code;
- path eligibility enforcement;
- constraints-file product support;
- exact PR base/head generic file acquisition;
- bounded large-lockfile acquisition;
- `uv.lock` extraction;
- duplicate-group equality fields;
- S001 dependency identity through the product;
- constraints or `uv.lock` CI consumption;
- `packaging` admission or PEP 440 runtime validation;
- architecture ADR;
- crossed-version upstream acquisition;
- reliable Python support-drop extraction;
- target/upstream relevance comparison;
- compatibility, safety, or maintainer action;
- production readiness or Ali-owned mastery.

## Exact continuation

Proceed with one evidence-driven acquisition and equality session:

1. acquire or calculate exact S001 base and head `uv.lock` byte sizes without executing target code;
2. determine whether the existing GitHub contents path can retrieve both exact files within its limits;
3. compare exact-contents and exact-blob acquisition only if the measured evidence requires it;
4. select a bounded maximum with an explicit `dependency_file_too_large` result;
5. inspect the admitted `uv.lock` package fields needed to prove an unchanged duplicate group;
6. freeze final clear names;
7. present the complete ADR decision for Ali approval;
8. do not write product source before ADR acceptance.

## Relevant revisions

```text
Step 1 behavior-validated product:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Naming clarity specification:
06caa57eb91a228cd60d6cef2a2c34a0d4211bc7

Decision Cluster 1 evidence:
b00f6477c481ef6f26a8fc2f0427b080f160df48

Decision Cluster 2 selected plan update:
69dd9040fb5e8265163f2d491a8d14f6d419b6f1

Decision Cluster 2 evidence:
9e4ffed0de5d2c41aa8ef45ac7b6e927ff8fcbe8

Decision Cluster 3 selected plan update:
8bbce1187427826fd49b47a20c915067da28ac19

Package/upstream PEP 440 boundary update:
3a61e9aa64dbaf99e9ed37b03eeb3f35038d942d

Decision Cluster 3 evidence:
f07a35644cc5f355453725a3d0f81f553301b388
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.