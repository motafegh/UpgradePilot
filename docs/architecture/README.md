# Architecture Decisions

This directory contains accepted UpgradePilot Architecture Decision Records (ADRs).

## Responsibility

An ADR records one consequential selected implementation mechanism or structural choice, including:

- the concrete responsibility or boundary being decided;
- the selected option;
- credible alternatives;
- rationale and trade-offs;
- exact accepted scope;
- what remains undecided;
- implementation proof required;
- reassessment triggers;
- assistance and ownership evidence.

This directory is not:

- a live project-state dashboard;
- a requirements catalogue;
- a proposal archive;
- proof that implementation works;
- proof of learner ownership.

Unadmitted ideas belong under `proposals/`. Framework-independent required behavior belongs under `docs/specifications/`.

## Specification versus ADR

Use:

- `docs/specifications/` for what the system **MUST** represent, guarantee, reject, preserve, or prove;
- `docs/architecture/` for **how** a consequential responsibility is implemented and why that method was selected.

The specification should normally define the responsibility and proof obligations before a framework/method ADR is accepted.

An ADR must satisfy the applicable requirement IDs or state an intentional deviation explicitly.

Framework-specific mechanisms should primarily remain in the ADR rather than being duplicated throughout the specification.

## Decision standard

Create an ADR when a choice establishes a durable framework, source/package boundary, representation policy, persistence mechanism, service boundary, cross-cutting security rule, or other structural commitment whose alternatives/trade-offs should remain reviewable.

Do not create ADRs for:

- routine small implementation choices;
- exact next actions;
- transient test results;
- hypothetical future layers;
- technologies not required by an implemented or immediately activated responsibility.

## Accepted decisions

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md) — repository, distribution/import-package naming, `src` source boundary, tests, and minimum project metadata.
- [`ADR-0002-pydantic-runtime-contract-models.md`](ADR-0002-pydantic-runtime-contract-models.md) — Pydantic v2 for strict runtime application contracts, explicit adapters, raw/trusted separation, mutation-resistant trusted models, and persistence/report separation.

## Decision and proof separation

An accepted ADR authorizes the selected mechanism inside its approved scope. It does not prove:

- dependency installation;
- import resolution;
- model behavior;
- passing tests;
- error diagnosis;
- end-to-end integration;
- Ali-owned capability.

Actual proof belongs in source, tests, commands, outputs, working evidence, and the canonical tracker.

## State routing

For current milestone, gate, blocker, capability, or next controlled responsibility, use the canonical Career tracker after checking snapshot provenance in `../program/SOURCE.md`.

For concise project-local continuation, use `../../MEMORY.md`.

Do not add exact session-level continuation or implementation status to this index.

## Historical correction

Former AI-generated architecture proposal files removed from the active tree remain historical evidence in Git history and the M2-entry audit. They have no implementation authority.