# UpgradePilot Current Memory

**Last updated:** 2026-07-31 19:10 +03:30  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, and exact continuation.

Stable plans, ADRs, source, tests, and dated evidence retain their own responsibilities. This file records only the current state needed to continue.

## Live position

- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md`](plans/B2_DEPENDENCY_VERSION_CHANGE_EVIDENCE_PLAN.md)
- **Step 6 controlling plan:** [`plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md`](plans/B2_STEP_6_DOWNSTREAM_DEPENDENCY_INPUT_MIGRATION_PLAN.md)
- **Accepted architecture:** [`docs/architecture/ADR-0004-dependency-version-change-evidence.md`](docs/architecture/ADR-0004-dependency-version-change-evidence.md)
- **Step 1 validation:** [`working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md`](working-memory/2026-07-30_2138_B2-step-1-dependency-contracts-validation.md)
- **Step 2 validation:** [`working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md`](working-memory/2026-07-31_1612_B2-step-2-exact-requirement-validation.md)
- **Step 3 validation:** [`working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md`](working-memory/2026-07-31_1635_B2-step-3-dependency-comparison-validation.md)
- **Step 4 validation:** [`working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md`](working-memory/2026-07-31_1729_B2-step-4-exact-pr-file-acquisition-validation.md)
- **Step 5 validation:** [`working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md`](working-memory/2026-07-31_1854_B2-step-5-uv-lock-extraction-validation.md)
- **Last behavior-validated repository state:** `0925b9e2bf146be920f50f584201f346094743f0`.
- **Behavior-validated Step 5 product/test revision:** `82237ee4b11b1df7182a58cf5913194d8b231eac`.
- **Step 6 plan revision:** `4ef166630b41251516757585a4c8f7246ad25b2b`.

Later planning and memory commits do not alter the behavior-validated Step 5 product/test revision.

## Current phase

Steps 1–5 are complete and behavior-validated.

Step 6 is approved and active:

```text
migrate downstream dependency input
```

Do not begin Step 7 CI-result migration or Step 8 multi-format command integration before Step 6 is behavior-validated.

## Validated Step 5 boundary

Deterministic execution:

```text
main @ 0925b9e2bf146be920f50f584201f346094743f0
clean working tree
Python 3.12.3
24 focused Step 5 tests passed
125 complete tests passed
```

Installed S004 remained intact:

```text
requirements-dev.txt
pytest 9.0.2 → 9.0.3
exact-head CI authority sufficient
published pytest==9.0.3
2 of 2 provenance
pytest-dev/pytest release tag 9.0.3
unresolved_claim
```

Live S001 file-level extraction established:

```text
pydantic/pydantic #13432
uv.lock
soupsieve 2.6 → 2.8.4
```

with exact Step 4 base/head revisions, blob SHAs, and byte counts.

## Finalized Step 6 architecture

The repository already had the correct strategic architecture in ADR-0004. The focused Step 6 plan now freezes the executable migration boundary.

### Canonical downstream identity

```text
DependencyVersionChange
├── package
├── normalized_package
├── old_version
├── proposed_version
├── source_evidence[]
└── limitations[]
```

Target, package, upstream, and generic presentation must consume this record rather than `PinnedDependencyChange`.

### Explicit CI input split

```text
DependencyVersionChange
→ package/version identity

explicit direct-requirements install path
→ input for the current pip -r CI rule
```

`DependencyFileEvidence.path` must never become installation evidence automatically.

### Future extension boundary

After Step 8, a new dependency source that establishes the same exactly-one-transition meaning should normally require:

```text
recognizer
+ acquisition rule when needed
+ source-specific extractor
+ focused tests
+ one explicit static coordinator branch
```

It must not require redesigning package lookup, upstream resolution, target-Python acquisition, generic evidence presentation, or the canonical comparison contract.

No dynamic plugin framework or registry is authorized at this stage.

### Legitimate future downstream changes

New syntax with the same canonical meaning should remain localized.

New CI-consumption semantics may require source-specific CI rules.

New product meanings—such as grouped updates, dependency graphs, direct/transitive role, or platform-specific transitions—may legitimately require a new canonical model. Step 6 must not create a vague universal abstraction to pretend otherwise.

## Step 6 modification surface

Primary runtime files:

```text
src/upgradepilot/dependency_change.py
src/upgradepilot/cli.py
src/upgradepilot/ci_authority.py
src/upgradepilot/workflow_commands.py
src/upgradepilot/__init__.py
```

Primary tests:

```text
tests/test_dependency_change.py
tests/test_cli.py
tests/test_ci_authority.py
```

The legacy `PinnedDependencyChange` may remain only at the exact-requirements ingress compatibility boundary until Step 8 replaces command ingress with the real multi-format coordinator.

## Exact continuation

Begin Step 6 implementation with tests before runtime source.

First re-fetch current blobs for:

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

Then add controlled tests proving:

1. legacy exact-requirements success converts to `DependencyVersionChange` plus one separate explicit direct-requirements install path;
2. target, package, and upstream stages use canonical package/version identity;
3. generic dependency-evidence presentation handles one or several source records;
4. no explicit install path cannot become sufficient CI merely because source evidence contains a path;
5. `uv_lock` and constraints evidence are not automatically passed to the `pip -r` rule;
6. `PinnedDependencyChange` is contained at the compatibility boundary;
7. S004 behavior remains materially intact.

Only after those tests are committed should runtime migration begin.

## Step 6 stop line

```text
all downstream identity consumers use DependencyVersionChange
+
PinnedDependencyChange is contained at legacy ingress
+
CI identity and direct-requirements path are separate inputs
+
source evidence path is not installation proof
+
generic evidence presentation works
+
S004 remains intact
+
complete deterministic suite passes
```

## Not established

- Step 6 implementation or validation;
- one-line installed S001 command behavior;
- normal CLI `uv.lock` recognition and exact-file acquisition;
- PR-wide multi-format comparison during command execution;
- final `DependencyCIExerciseResult` runtime behavior;
- `uv.lock` CI consumption;
- PEP 440 semantics;
- Python-support relevance;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery.

## Learning state

Step 5 concepts were introduced, implemented, corrected, and behavior-validated, including TOML parsing, lock schema and revision, normalized package grouping, duplicate groups, artifact versus structural metadata, versionless workspace records, and file-level versus PR-wide trust.

Current depth remains:

```text
introduced and reviewed
+ real failure diagnosed
+ corrected behavior validated
but
no independent implementation practice recorded
no user-owned technical explanation recorded
no formal assessment recorded
not mastered
```

Product behavior validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected plan, verified behavior, blocker, learning state, or exact continuation changes, update this file only. Change another file only when its stable responsibility or dated evidence changes.
