# UpgradePilot Current Memory

**Last updated:** 2026-07-31 20:31 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 6 plan:** [`plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md`](plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 5 validation:** [`working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md`](working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md)
- **Step 6 implementation:** [`working-memory/2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md`](working-memory/2026-07-31_1957_B2-step-6-downstream-dependency-input-implementation.md)
- **Step 6 validation:** [`working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md`](working-memory/2026-07-31_2031_B2-step-6-downstream-dependency-input-validation.md)
- **Behavior-validated Step 6 product/test revision:** `885d8aab5a3cfd187bf3fce179aabcbfccebeaac`.
- **Step 6 validation-record revision:** `02e0c5603d2945f37daef424b2cabcabdfb534a1`.

The user-supplied validation transcript showed branch `main` but did not include the exact local `HEAD`, clean-tree output, or Python version. Those omissions are preserved in the validation record and are not inferred.

## Current phase

Steps 1–6 are complete and behavior-validated.

Step 7 is now the next bounded plan step:

```text
migrate CI result names and semantics
```

Do not begin Step 8 multi-format command integration before Step 7 is behavior-validated.

## Step 6 validated boundary

### Deterministic execution

Observed complete-suite result:

```text
Ran 130 tests in 0.036s
OK
```

A separate focused 14-test summary was not supplied. The focused tests are part of the complete suite, but an independent focused invocation is not claimed.

### Installed anonymous S004 regression

Observed command:

```bash
unset GITHUB_TOKEN
upgradepilot googlefonts/glyphsLib 1145
```

Preserved material behavior:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
project_table_absent
2 exact-head workflow runs
CI authority sufficient
exact_head_dependency_exercised
pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

The `Regression Tests` workflow still established visible installation of `requirements-dev.txt` and direct invocation of `pytest`. The multi-job `Test + Deploy` workflow remained unresolved.

### Canonical dependency presentation

Observed:

```text
Dependency evidence records: 1
Dependency evidence: requirements-dev.txt
  Format: exact_requirement
  Extraction method: changed_file_patch
```

The old singular `Source file: requirements-dev.txt` presentation was absent.

## What Step 6 established

### Temporary legacy ingress containment

```text
ChangedFile[]
→ PinnedDependencyChange
→ LegacyDependencyIngress
   ├── dependency: DependencyVersionChange
   └── direct_requirements_install_path
```

`PinnedDependencyChange` remains only at the temporary exact-requirements ingress compatibility boundary.

### Canonical downstream identity

After ingress conversion, target, package, upstream, CI package identity, and CLI presentation consume:

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

### Explicit CI input split

`evaluate_ci_authority` receives:

```text
DependencyVersionChange
+ WorkflowAuthorityInput[]
+ direct_requirements_install_path: str | None
```

The direct-requirements path is keyword-only and independently supplied. Generic dependency evidence paths are never selected automatically as installation proof.

When the explicit path is absent and successful CI exists, the current evaluator remains unresolved with:

```text
direct_requirements_install_path_unavailable
```

### Future-extension boundary

A future source format that establishes the same exactly-one-transition meaning should normally require:

```text
recognizer
+ acquisition rule when needed
+ source-specific extractor
+ focused tests
+ one explicit static coordinator branch
```

It should not require redesigning package lookup, upstream resolution, target-Python acquisition, generic evidence presentation, or `DependencyVersionChange`.

No dynamic plugin framework is authorized at the current project depth.

## Step 7 responsibility

Step 7 must replace the legacy CI result vocabulary and contract with:

```text
DependencyCIExerciseResult
```

Required states:

```text
proven
no_successful_ci
unresolved
```

Required meanings:

- `proven`: one successful exact-head path satisfies an explicitly admitted dependency-consumption and package-exercise rule;
- `no_successful_ci`: no completed successful exact-head job is available;
- `unresolved`: successful exact-head CI exists, but no admitted rule proves dependency consumption and exercise.

Step 7 must preserve:

- the currently validated direct-requirements `pip -r <exact path>` plus direct package invocation rule;
- explicit source-specific CI input rather than generic evidence-path inference;
- visible unresolved states;
- S004 material behavior;
- package, upstream, and target identity independence from CI status.

Step 7 must not yet:

- integrate normal CLI `uv.lock` acquisition or comparison;
- claim `uv.lock` or constraints consumption;
- implement broad workflow or shell interpretation;
- add PEP 440 ordering, Python-support relevance, compatibility, safety, or recommendation logic.

## Exact continuation

Before Step 7 source changes:

1. inspect the current `CIAuthorityResult`, `WorkflowAuthorityAssessment`, evaluator, CLI presentation, package exports, and all associated tests;
2. compare their current meanings against ADR-0004 and the parent Step 7 entry;
3. determine whether a focused Step 7 execution plan is needed; create one when the parent entry is too terse to control exact migration mechanics;
4. freeze tests for new names, state mapping, decision order, unresolved visibility, and S004 preservation;
5. implement the migration without beginning Step 8.

## Not established

- Step 7 CI-result migration;
- one-line installed S001 behavior;
- normal CLI `uv.lock` recognition or exact-file acquisition;
- PR-wide multi-format command coordination;
- `uv.lock`, constraints, or other new CI-consumption rules;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 6 concepts introduced and reviewed:

- canonical domain model;
- compatibility boundary;
- package identity versus operational evidence;
- explicit dependency injection through a keyword-only argument;
- generic evidence rendering;
- localized extension versus legitimate canonical-model change.

Current depth:

```text
structured explanation completed
+ architecture approved
+ tests written before source
+ implementation completed
+ complete deterministic suite observed
+ installed S004 regression observed
but
no user-owned technical explanation recorded
no independent implementation practice recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
