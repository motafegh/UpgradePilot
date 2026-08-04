# Architecture Decisions

This directory contains UpgradePilot Architecture Decision Records (ADRs), including accepted and explicitly superseded consequential decisions.

## ADR responsibility

An ADR records one durable implementation or structural decision:

- context and owning responsibility;
- selected option;
- credible alternatives;
- rationale, consequences, risks, and reversal;
- bounded scope and undecided matters;
- reassessment triggers;
- links to requirements and evidence.

An ADR does not prove implementation, passing tests, installation, capability, current progress, or project continuation. Source, tests, commands, outputs, and current evidence prove implemented truth. `../../MEMORY.md` alone records live project position and exact continuation.

## Decision navigation

This section is navigation only. Each ADR's own `Status` field is the authority for whether that decision is accepted or superseded. This list must not be interpreted as a live-stage register or used to infer which ADR is currently active, completed, or next.

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md)
  — **Accepted.** Controls repository/distribution/import naming, `src/upgradepilot/`, `tests/`, and the non-speculative package boundary.
- [`ADR-0002-pydantic-runtime-contract-models.md`](ADR-0002-pydantic-runtime-contract-models.md)
  — **Superseded.** Historical M2 Pydantic choice; no longer an inherited B2 method.
- [`ADR-0003-clean-slate-b2-source-reset.md`](ADR-0003-clean-slate-b2-source-reset.md)
  — **Accepted.** Controls preservation of the M2 implementation in immutable history and the clean active source reset before B2.
- [`ADR-0004-dependency-version-change-evidence.md`](ADR-0004-dependency-version-change-evidence.md)
  — **Accepted.** Controls source-specific dependency-version extraction, trusted change comparison, bounded exact base/head `uv.lock` acquisition, duplicate-record abstention, and honest CI dependency-exercise states for the B2 evidence path.
- [`ADR-0005-packaging-version-and-python-line-method.md`](ADR-0005-packaging-version-and-python-line-method.md)
  — **Accepted.** Controls the bounded `packaging` runtime dependency, PEP 440 dependency-version ordering, crossed-release ordering, and exact stable Python-line specifier witness method.
- [`ADR-0006-bounded-local-support-drop-semantic-extractor.md`](ADR-0006-bounded-local-support-drop-semantic-extractor.md)
  — **Accepted.** Controls the bounded LM Studio / `gemma-4-e4b-it-ud` support-drop semantic extractor, contract-v2 representation, direct-HTTP baseline, mandatory deterministic grounding, and reassessment triggers.

Do not add labels such as **current ADR**, **active ADR**, **next ADR**, or similar live-state wording here. If project position changes, update `../../MEMORY.md` only.

## Specification versus ADR

- `docs/specifications/` states framework-independent behavior and invariants.
- `docs/architecture/` states accepted consequential methods and their status.
- source, tests, commands, outputs, and current evidence state what actually works.
- `../../MEMORY.md` states the current continuation.
- `archive/` identifies immutable historical implementation snapshots that have no current runtime authority.

Create an ADR only for a durable framework, source/package boundary, representation policy, persistence mechanism, service boundary, cross-cutting security rule, or comparable structural commitment. Do not create ADRs for routine implementation choices, exact next actions, transient results, or unactivated technologies.

## Proof and ownership

ADR acceptance authorizes a method only within its stated scope. It does not prove:

- dependency installation;
- import resolution;
- runtime behavior;
- passing tests;
- error diagnosis;
- integration;
- production fitness;
- Ali-owned capability.

Former implementations and proposals preserved in Git history or `archive/` are evidence, not active architecture or code baselines.