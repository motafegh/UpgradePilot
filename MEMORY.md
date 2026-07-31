# UpgradePilot Current Memory

**Last updated:** 2026-07-31 17:29 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable route definitions, specifications, ADRs, source, tests, plans, and dated evidence retain their own responsibilities. This file records only the current position needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Controlling route:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md)
- **B2 gate:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)
- **Selected plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Step 4 validation:** [`working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md`](working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md)
- **Validated repository `main` state:** `84fdd422152cd2b098fb88b6245e86b8750add29`.
- **Validated product-source revision:** `7bb542acf4ca24a89e384f9a9c590345939c8673`.
- **Step 4 validation-record revision:** `6d9e28cf9cb267c10c162040a545919611b26ac4`.

## Current phase

Steps 1, 2, 3, and 4 are complete and behavior-validated.

Step 5 is the next bounded plan step, but implementation has not started:

```text
extract uv.lock changes
```

The next activity is a focused educational inspection of controlled `uv.lock` structure, records, and comparison rules before modifying source.

## Current behavior-validated boundary

Observed deterministic result:

```text
Ran 101 tests in 0.023s
OK
```

Observed installed regression control:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

S004 preserved:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
exact-head CI authority sufficient
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

The supplied transcript did not repeat `git rev-parse HEAD`, `git status --short`, or `python --version`. The validation is bound to remote `main` as resolved immediately after execution; it does not independently establish the local exact commit, clean working tree, or interpreter version for that run.

## Step 4 behavior now validated

Validated record:

```text
ExactRepositoryTextFile
├── repository
├── path
├── returned_path
├── revision
├── blob_sha
├── reported_byte_count
├── decoded_byte_count
└── content
```

Validated methods:

```text
get_pull_request_base_file
get_pull_request_head_file
```

Validated strict acquisition sequence:

```text
normalized relative path
→ exact immutable PR base/head SHA
→ GitHub Contents API
→ regular-file response
→ requested/returned path agreement
→ non-empty blob SHA
→ required non-negative reported size
→ pre-decode 1,000,000-byte bound
→ strict Base64 decoding
→ actual decoded byte count
→ reported/decoded size agreement
→ decoded-byte bound
→ valid UTF-8
→ ExactRepositoryTextFile
```

Validated stopping distinctions include:

- ambiguous 404 becomes `UnavailableRepositoryFile` and does not become empty text;
- returned-path mismatch;
- missing, negative, or boolean reported size;
- reported oversize before decoding;
- malformed Base64;
- reported/decoded size disagreement;
- invalid UTF-8.

## Public S001 acquisition evidence

Public case:

```text
pydantic/pydantic #13432
uv.lock
```

Base evidence:

```text
revision: 652a61ce4f9d7d76eaada31535807a485ece0e21
blob SHA: b4a68ab725de337889d50d5374ac0f05db7fb484
reported bytes: 606307
decoded bytes: 606307
```

Head evidence:

```text
revision: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
blob SHA: def33fe05d78ab851ce91a33db5bc55a439873a1
reported bytes: 606313
decoded bytes: 606313
```

Both complete files were acquired below the authorized bound, and each reported byte count matched the actual decoded byte count.

This is the first newly implemented selected-plan capability exercised successfully against S001.

It does **not** yet establish:

```text
soupsieve 2.6 → 2.8.4
```

That identity belongs to Step 5 parsing and comparison.

## Compatibility boundary

Existing validated APIs remain present:

```text
get_exact_head_text_file
get_exact_head_workflow_file
RepositoryTextFile
```

The installed CLI still uses those APIs for target-Python and workflow evidence. It still follows the legacy dependency path:

```text
ChangedFile[]
→ extract_pinned_dependency_change
→ PinnedDependencyChange or UnsupportedDependencyChange
```

Step 4 did not migrate the CLI, parse `uv.lock`, or change CI semantics.

## Learning state

Step 4 introduced and reviewed:

- **commit SHA** — immutable repository-state identifier rather than a movable branch label;
- **base/head acquisition** — complete before/after reads of one path;
- **blob SHA** — identity of one exact GitHub content object;
- **reported byte count** — GitHub's declared size before decoding;
- **decoded byte count** — actual bytes produced by Base64 decoding;
- **size reconciliation** — both counts must agree;
- **pre-decode bound** — known oversized evidence stops before decoding;
- **defense-in-depth bound** — actual decoded bytes are bounded again;
- **Base64 versus UTF-8** — transport representation versus text encoding;
- **additive compatibility** — a stricter evidence contract was added without replacing existing workflow/target contracts.

Current depth:

```text
structured explanation completed
+ existing source and callers inspected
+ proof obligations defined
+ implementation reviewed
+ complete-suite execution observed
+ installed S004 regression observed
+ live S001 exact base/head acquisition observed
but
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## Exact continuation

Remain inside Step 5 of the selected dependency-version-change plan.

Before source modification, inspect and teach:

1. the admitted `uv.lock` path/status rule;
2. TOML and Python 3.12 `tomllib` parsing;
3. top-level `version = 1` and non-negative integer `revision` controls;
4. usable textual package `name` and `version` records;
5. normalized-name grouping;
6. one-record base/head comparison;
7. stable source and resolution-context requirements;
8. unchanged duplicate groups as unordered multisets after removing only `sdist` and `wheels`;
9. changed duplicate groups as `ambiguous_uv_lock_package_records`;
10. artifact-only differences versus unsupported structural differences;
11. exact base/head evidence preservation in `DependencyFileEvidence`.

Step 5 implementation names remain:

```text
src/upgradepilot/uv_lock_change.py
    is_modified_uv_lock_file
    extract_uv_lock_changes
```

Step 5 must prove with controlled fixtures:

- supported schema and revision;
- one unambiguous version transition;
- unchanged package;
- package addition or removal;
- several version changes;
- malformed TOML;
- invalid package records;
- source or resolution-context mismatch;
- same-version unsupported structural change;
- unchanged duplicate groups do not block another clear transition;
- changed duplicate groups remain ambiguous;
- artifact-only differences do not create transitions;
- exact source evidence is preserved;
- no S001 identifiers or expected answer are hardcoded.

Step 5 must not implement:

- CLI integration;
- downstream migration to `DependencyVersionChange`;
- CI dependency-exercise migration;
- PEP 440 parsing or ordering;
- Python-support relevance;
- compatibility, safety, recommendation, or maintainer-action logic.

## Not established

- `uv.lock` TOML parsing behavior;
- `uv.lock` schema/revision validation;
- package-record and duplicate-group comparison;
- Soup Sieve dependency identity from S001;
- PR-wide comparison using future `uv.lock` extraction results;
- CLI orchestration through the shared dependency flow;
- constraints or `uv.lock` CI-consumption semantics;
- downstream `DependencyVersionChange` migration;
- `DependencyCIExerciseResult` runtime behavior;
- PEP 440 runtime semantics;
- Python-support relevance;
- compatibility, safety, maintainer action, or production readiness;
- mastery of Steps 1–4 concepts.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
