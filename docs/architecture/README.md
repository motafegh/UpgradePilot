# Architecture Decisions

This directory contains accepted UpgradePilot Architecture Decision Records (ADRs).

## ADR responsibility

An ADR records one durable consequential implementation or structural decision:

- context and responsibility;
- selected option;
- key credible alternatives;
- rationale, consequences, and risks;
- bounded scope and undecided matters;
- reassessment triggers;
- links to applicable requirements and evidence.

An ADR does not contain current progress, exact next actions, complete test plans, detailed capability assessment, or proof that implementation works.

## Specification versus ADR

- `docs/specifications/` states framework-independent required behavior and invariants.
- `docs/architecture/` states the selected consequential implementation method and why it was selected.
- source, tests, commands, outputs, and current evidence show what actually works.
- `MEMORY.md` states concise project continuation.

Create an ADR only when a choice establishes a durable framework, source/package boundary, representation policy, persistence mechanism, service boundary, cross-cutting security rule, or comparable structural commitment.

Do not create ADRs for routine implementation choices, exact next actions, transient test results, hypothetical future layers, or technologies not required by an activated responsibility.

## Accepted decisions

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md) — repository, distribution/import-package naming, `src` source boundary, tests, and minimum metadata boundary.
- [`ADR-0002-pydantic-runtime-contract-models.md`](ADR-0002-pydantic-runtime-contract-models.md) — bounded Pydantic v2 adoption for strict boundary and trusted application contracts.

## Proof and ownership

ADR acceptance authorizes a method inside its scope. It does not prove:

- dependency installation;
- import resolution;
- model behavior;
- passing tests;
- error diagnosis;
- integration;
- Ali-owned capability.

Use source/tests/outputs and working evidence for implementation proof. Use a formal Career review only when Ali asks to update career-level capability assessment.

Former architecture proposals removed from the active tree remain historical evidence in Git history and have no current authority.
