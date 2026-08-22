# Working Memory — B2 Source/Evidence and uv Reconciliation Session

**Date:** 2026-08-22  
**Status:** ACTIVE  
**Branch:** `main`  
**Mode:** learning by doing and building  
**Live-state owner:** `../MEMORY.md`

## Why this session exists

The project was in the middle of the dedicated learning route under:

```text
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
```

While learning the implemented B2 dependency-environment/CI path, Ali identified concrete design and implementation concerns: duplicated validation, potentially over-strong naming/propositions, repeated `uv.lock` structural interpretation, incomplete preservation of real uv workspace scope, and places where complexity may be compensating for weak internal contracts rather than product responsibility.

Those concerns were preserved in repository audits. A fresh review on 2026-08-22 validated that several findings are real enough to reconcile **before** ordinary Cluster-6 application integration or a new agentic product experiment.

This session therefore pauses the dedicated learning-folder progression and returns UpgradePilot to its normal project mode:

> **learning by doing and building**

Learning is not abandoned. Understanding, prediction, implementation, testing, and explanation are expected to happen inside each bounded engineering step under `OPERATING_GUIDE.md` and the source-clarity contract.

## Current session decision

Until this reconciliation closes:

1. the dedicated learning folder is paused;
2. the previously active B2 dependency-environment/CI continuation is deferred at the completed Cluster-5 boundary;
3. the bounded agentic-orchestration evaluation is deferred;
4. current engineering work is the fresh source/design reconciliation plan created in this session;
5. after that plan closes, older deferred plans must be re-reviewed against the modified source/architecture before any of them becomes active again.

No previous accepted implementation evidence is erased merely because its architecture is being refined. In particular, the accepted S001 positive explicit-root witness and Cluster-0–5 validation history remain historical evidence unless a new test/refactor actually refutes them.

## Selected plan

Current plan:

`../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

Sequence:

```text
R0  re-anchor contracts + freeze behavior
R1  strengthen exact repository-file evidence ownership
R2  one bounded uv-specific structural lock model
R3  preserve minimum real uv command/workspace scope
R4  narrow uv membership to explicit selected-root reachability
R5  rebind CI consumption to reconciled evidence
R6  pressure S001 / S011 / S005 + changed-case workspace transfer
R7  acceptance + audit disposition + deferred-plan re-review
```

No product-source change has started yet. Ali requested that the plan be written and onboarded first, then implementation starts only after Ali explicitly selects the first part.

## Audit lifecycle created in this session

Lifecycle indexes now exist at:

```text
../audits/active/README.md
../audits/deferred/README.md
../audits/absorbed/README.md
```

Policy:

- `../audits/README.md`
- `../audits/LIFECYCLE.md`

Canonical audit records remain directly under `../audits/` because the existing records contain repository-relative references written from that location. An initial physical-move attempt was corrected in this same session before handoff because nesting those files unchanged would have silently broken links such as `../docs/...`, `../src/...`, and `../plans/...`.

The lifecycle folders therefore own the **current status/title index**, while audit IDs/files retain stable canonical paths.

### Active

- `../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`
- `../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md`
- `../audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md`

### Deferred

- `../audits/2026-08-16_AUDIT-004_uv-lock-resolution-satisfiability-evidence-boundary.md`
- `../audits/2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md`

### Absorbed

- `../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md`
- `../audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`

Lifecycle titles are visible in the indexes, for example `ACTIVE — AUDIT-007`. Reclassification updates the indexes instead of renaming the stable audit ID/file every time.

## Active audit pressure

### AUDIT-001

Exact-file acquisition remains justified, but some fields are likely validation/transport details rather than necessary long-lived domain evidence. This should be reconsidered only while preserving strong GitHub/path/size/encoding/content validation.

### AUDIT-006

`RepositoryTextFile` does not structurally express all guarantees established by the normal provider path. Downstream consumers therefore repeat some checks that may be removable only after a stronger owning contract exists. Relational/rebinding and semantic checks must remain distinct from redundant internal-invariant checks.

### AUDIT-007

Current uv design pressure includes:

- whole-environment-sounding membership naming versus actual explicit-root reachability;
- dropped S001 `--all-packages` workspace scope;
- asymmetric proof needs for positive witness versus `not_established`;
- overlapping `uv.lock` structural parsers with demonstrated rule drift;
- mandatory `pyproject.toml` participation that must be justified by the exact proposition rather than existing implementation shape.

## Controlling/accepted references

This session must remain compatible with:

- `../AGENTS.md`
- `../PROJECT_CHARTER.md`
- `../OPERATING_GUIDE.md`
- `../SECURITY.md`
- `../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`
- `../docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`
- `../docs/architecture/ADR-0004-dependency-version-change-evidence.md`
- `../docs/architecture/ADR-0007-responsibility-based-source-subpackages.md`
- `../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition-ir.md`
- `../docs/MATURE_SYSTEM_HORIZON.md`
- current product source/tests.

Stable product rules that must survive the reconciliation include:

```text
exact dependency transition
!= environment/root reachability
!= static CI consumption
!= runtime execution/success
!= exact-version runtime witness
!= behavioral compatibility/safety/action
```

and:

```text
observation != interpretation != evidence quality != decision
```

## Current likely engineering direction

The selected plan seeks the smallest architecture that:

1. expresses strong exact repository-file guarantees at the correct owning boundary so downstream consumers do not repeatedly defend against already-established internal invariants;
2. preserves semantic and relational/rebinding validation where it genuinely belongs;
3. centralizes only the genuinely shared structural truth of the external `uv.lock` format in one uv-specific parser/model;
4. keeps dependency-transition comparison and explicit-root reachability as separate semantic consumers;
5. narrows uv membership language toward **explicit selected-root reachability** rather than building a complete uv environment interpreter;
6. preserves enough real command/workspace scope (starting with S001 `--all-packages`) that negative-ish `not_established` results are never stronger than the modeled scope;
7. uses `pyproject.toml` only for propositions/facts it actually establishes;
8. avoids generic trust wrappers, generic dependency graphs, universal package-manager abstractions, or runtime execution of target repositories merely to simplify code.

## Pressure cases / proof anchors

- **S001** — Pydantic / Soup Sieve: preserve the positive docs-root transitive witness, now with honest workspace-scope semantics.
- **S011** — optional-extra `mlx` versus selected `dev`: keep project-source environment membership separate from uv lock reachability.
- **S005** — tox/uv-mediated lock consumption: ensure lock reachability is not coupled to one direct `uv sync` interpreter.

Required validation will include focused tests, nearest integration tests, and the full deterministic suite before this reconciliation is accepted.

## Latest product validation retained

The latest product-runtime validation point remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
HEAD == origin/main
clean worktree at that validation point
```

The audit/lifecycle/plan/memory commits in this session are governance/document changes, not a newer product-runtime validation point.

## Session progression log

### 2026-08-22 — Session opened

- Ali explicitly paused the dedicated learning-folder route and selected normal learning-by-building mode.
- Ali requested audit lifecycle organization and a fully fresh implementation plan.
- Current source/audit review supports treating AUDIT-001, AUDIT-006, and AUDIT-007 as the immediate reconciliation pressure.
- No product-source code changed.

### 2026-08-22 — Governance/session setup completed

- Created this progressive working-memory record before implementation work.
- Created audit lifecycle indexes and policy.
- Classified AUDIT-001/006/007 as active.
- Classified AUDIT-004/005 as deferred.
- Classified AUDIT-002/003 as absorbed.
- Corrected the first physical-move approach after detecting that it would break existing relative references; canonical audit paths are stable and lifecycle folders now own status navigation.
- Created `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`.
- Updated root `MEMORY.md` so that plan is the sole active implementation route.
- Paused the dedicated learning package at its existing recorded position.
- Deferred old Cluster-6 continuation and the agentic evaluation until R7 re-review.
- No product source/tests have been modified yet.

## Exact next action

Wait for Ali to explicitly start **R0 — re-anchor contracts and freeze behavior**.

R0 is inspect/classify/freeze only. It should establish the precise source/test change surface and ownership taxonomy before the first implementation modification in R1.
