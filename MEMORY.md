# UpgradePilot Current Memory

**Last updated:** 2026-07-29 22:13 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the live position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected bounded plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Downstream dependent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Naming control:** [`docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md)
- **Latest decision evidence:** [`working-memory/2026-07-29_2213_B2-dependency-evidence-naming-and-cluster-1.md`](working-memory/2026-07-29_2213_B2-dependency-evidence-naming-and-cluster-1.md)
- **Planning evidence:** [`working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md`](working-memory/2026-07-29_2122_B2-dependency-change-foundation-planning.md)
- **Latest relevant non-memory revision:** `b00f6477c481ef6f26a8fc2f0427b080f160df48`.

Additional working-memory records created on 2026-07-29 use local `HHMM` after the date. Existing files are not renamed merely to retrofit that convention.

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

Dependency version identity feeds CI, package, upstream, release-interval, target, and later decision work. The selected plan corrects that foundational evidence responsibility before further Python-support relevance implementation.

## Behavior-validated product boundary

Target-declaration Step 1 remains fully behavior-validated at product revision:

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

Ali identified that broad terms such as:

```text
canonical contract
provenance
interpreter
reconciler
foundation
```

required unnecessary project-specific explanation and were difficult to recall from their names alone.

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

The existing source type `PinnedDependencyChange` remains implemented truth until a tested refactor replaces it. It must not be confused with the future shared trusted record.

Historical records are not mass-rewritten only for vocabulary modernization. Apply the naming rule to selected plans, future ADRs, new or changed source/tests, CLI labels, and active controlling documents when touched.

## Decision Cluster 1 — approved

Ali approved these connected architecture rules:

### Trusted downstream record

Use one representation-independent:

```text
DependencyVersionChange
```

It contains package identity, exact raw old/proposed versions, and supporting source evidence.

It does not imply dependency role, target usage, CI consumption, compatibility, safety, or maintainer action.

### Source-specific extraction and comparison

Use:

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

### Equivalent evidence

Same normalized package, exact raw old version, and exact raw proposed version:

```text
→ one DependencyVersionChange
→ all supporting source evidence attached
```

### Conflicting evidence

Different package/version changes produce:

```text
conflicting_dependency_version_changes
```

No dependency-file priority silently chooses an answer.

### Recognized malformed or incomplete dependency evidence

A changed file recognized as a supported dependency format cannot be ignored merely because another file provides a convenient extracted change.

```text
one valid extracted change
+
one recognized malformed, unavailable, incomplete, or too-large supported dependency file
→ no trusted DependencyVersionChange
```

Do not reopen these approved rules unless implementation evidence exposes a concrete contradiction.

## Remaining decisions before ADR or code

1. exact requirement and constraint filename/path eligibility;
2. handling of nested conventional requirements/constraints paths;
3. first `uv.lock` duplicate-package identity rule;
4. modified-only `uv.lock` status boundary;
5. raw version identity and where later PEP 440 ordering begins;
6. CI behavior when a dependency file's consumption is not established;
7. exact S001 base/head lockfile sizes and bounded acquisition method;
8. final source type, function, module, problem, and CLI names under the naming specification;
9. ADR scope, alternatives, consequences, and reassessment triggers.

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

## Exact continuation

Proceed with one coherent representation-rules discussion:

1. explain why scanning arbitrary changed files for `package==version` can create false dependency evidence;
2. compare conventional `requirements` and `constraints` filename/path rules;
3. decide how nested paths are admitted without repository allowlists;
4. explain `uv.lock` duplicate package records, sources, markers, and resolution contexts at the minimum depth needed now;
5. decide the first duplicate-name and modified-file boundaries;
6. record the resulting decisions with clear names;
7. continue to version identity, CI consumption, and bounded file acquisition only after this group is understood.

Do not create the ADR or write product code during this next discussion.

## Relevant revisions

```text
Step 1 behavior-validated product:
75e1b5c55844c2e7b6f9f64d6ae1bd76c2dabd15

Naming clarity specification:
06caa57eb91a228cd60d6cef2a2c34a0d4211bc7

Clearly named dependency evidence plan:
a95caa35e7483fca3c566e66247d99a1226ee460

Former plan path converted to pointer:
1ac9d66d1209ce9faa746b8f44221672c9118f25

Naming and Decision Cluster 1 evidence:
b00f6477c481ef6f26a8fc2f0427b080f160df48
```

## State-maintenance rule

When route, selected plan, verified behavior, blocker, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.