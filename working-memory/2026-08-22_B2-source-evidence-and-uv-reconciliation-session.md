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
2. the previously active B2 continuation is deferred;
3. the bounded agentic-orchestration evaluation is deferred;
4. current engineering work is a fresh source/design reconciliation centered on the validated audit findings;
5. after the new implementation plan closes, older deferred plans must be re-reviewed against the modified source/architecture before any of them becomes active again.

No previous accepted implementation evidence is erased merely because its architecture is being refined. In particular, the accepted S001 positive explicit-root witness and Cluster-0–5 validation history remain historical evidence unless a new test/refactor actually refutes them.

## Primary audit inputs

Current actionable audit pressure:

- `../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md`
  - exact-file record contains some validation/transport facts whose long-lived ownership should be reconsidered;
- `../audits/2026-08-21_AUDIT-006_internal-evidence-type-strength-and-revalidation-boundaries.md`
  - `RepositoryTextFile` does not structurally express all guarantees established by the real provider path, causing repeated downstream defensive validation;
- `../audits/2026-08-22_AUDIT-007_uv-membership-proposition-and-lock-model-boundaries.md`
  - current uv membership naming is broader than the implemented explicit-root reachability proposition;
  - real `--all-packages` workspace scope is dropped;
  - `uv_lock.py` and `uv_membership.py` duplicate overlapping external lock-format truth and have already drifted;
  - mandatory `pyproject.toml` participation in narrow lock-backed reachability must be justified by the exact proposition rather than by existing code shape.

Other audits remain useful evidence but are not all immediate implementation work. This session will organize them by lifecycle so active engineering questions are distinguishable from absorbed or deferred review records.

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

## Current likely engineering direction — not yet implementation detail

The validated direction is to seek the smallest architecture that:

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

## Session progression log

### 2026-08-22 — Session opened

- Ali explicitly paused the dedicated learning-folder route and selected normal learning-by-building mode.
- Ali requested audit lifecycle organization and a fully fresh implementation plan.
- Current source/audit review supports treating AUDIT-001, AUDIT-006, and AUDIT-007 as the immediate reconciliation pressure.
- No product-source code has been changed yet.
- Next repository actions in this session:
  1. reconcile live `MEMORY.md`;
  2. organize audit lifecycle without losing audit identity/history;
  3. create and select the fresh reconciliation implementation plan;
  4. update this working memory with the exact resulting paths/state.
