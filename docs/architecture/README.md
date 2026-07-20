# Architecture Decisions

This directory contains accepted UpgradePilot architecture decisions and the minimum context needed to interpret them.

## Authority

A file here is authoritative only when it states an accepted status and is consistent with the controlling Career plan, tracker, and current project memory.

This directory is not a proposal archive. Unadmitted ideas belong under `proposals/`.

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

Do not create architecture records for hypothetical layers, technologies, or directory trees that no implemented responsibility requires.

## Current accepted decisions

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md) — repository, distribution/import-package naming, `src` source boundary, tests, and minimum project metadata.

## Historical correction

The former AI-generated `ARCHITECTURE.md` and `DECISIONS.md` files were removed from the active tree after their audit and after a fresh source-layout decision was derived and accepted. Their historical content and correction remain available through Git history and the M2-entry audit record; they have no implementation authority.