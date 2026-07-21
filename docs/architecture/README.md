# Architecture Decisions

This directory contains accepted UpgradePilot architecture decisions and the minimum context needed to interpret them.

## Authority

A file here is authoritative only when it states an accepted status and is consistent with the controlling Career plan, tracker, current project memory, and applicable accepted technical specification.

This directory is not a proposal archive or a general requirements area. Unadmitted ideas belong under `proposals/`; project-level conceptual contracts belong under `docs/specifications/`.

## Specification versus ADR

Use:

- `docs/specifications/` to define what the system must represent and guarantee, including conceptual pipeline, information boundaries, invariants, states, and provisional assumptions;
- `docs/architecture/` to record a consequential selected mechanism or structural choice, alternatives, trade-offs, proof, and reassessment triggers.

The specification should normally precede a framework or representation ADR. An ADR must satisfy the applicable specification and state any intentional deviation explicitly.

## Decision standard

An accepted architecture decision should state:

- the concrete problem or boundary being decided;
- the selected option;
- the alternatives considered;
- the rationale and trade-offs;
- the exact scope accepted now;
- what remains deliberately undecided;
- validation or proof required during implementation;
- reassessment triggers;
- assistance and ownership evidence.

Do not create architecture records for hypothetical layers, technologies, or directory trees that no implemented or immediately activated responsibility requires.

## Current accepted decisions

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md) — repository, distribution/import-package naming, `src` source boundary, tests, and minimum project metadata.
- [`ADR-0002-pydantic-runtime-contract-models.md`](ADR-0002-pydantic-runtime-contract-models.md) — Pydantic v2 for strict runtime application contracts, explicit adapters, raw/trusted separation, mutation-resistant trusted models, and persistence/report separation.

## Current implementation status

ADR-0002 closes the M2 representation-method decision and authorizes Pydantic as a runtime dependency for the activated contract implementation. It does not prove installation, model behavior, tests, diagnosis, or Ali ownership.

The exact continuation is controlled by `MEMORY.md`, the Career tracker and amendment, and the active working record.

## Historical correction

The former AI-generated `ARCHITECTURE.md` and `DECISIONS.md` files were removed from the active tree after their audit and after fresh decisions replaced the only boundaries currently required. Their historical content and correction remain available through Git history and the M2-entry audit record; they have no implementation authority.