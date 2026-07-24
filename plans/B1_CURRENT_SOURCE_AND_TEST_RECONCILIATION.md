# B1 Current Source and Test Reconciliation

**Status:** Completed inspection; active-source disposition superseded by accepted clean reset  
**Date:** 2026-07-23  
**Stage:** B1 — Implementation responsibility freeze  
**Reset decision:** [`../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md`](../docs/architecture/ADR-0003-clean-slate-b2-source-reset.md)  
**Archive:** [`../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md`](../archive/2026-07-23_PRE_B2_M2_IMPLEMENTATION.md)

## Purpose

Preserve what B1 learned from inspecting the pre-reset implementation while making clear
that none of that source now controls or constrains B2.

This is not a B2 implementation plan.

## Inspection result before reset

Connector-backed inspection found an M2-era path:

```text
manual case mapping
→ strict case identity
→ manually assembled evidence
→ optional local-LLM extraction and input-risk experiments
→ mechanical grounding
→ one Python-support decision rule
→ targeted checks or abstention
```

The implementation contained useful concepts—strict identity, immutable contracts,
explicit missing evidence, traceable reasons, limitations, abstention, and separation of
untrusted model output—but it did not implement the accepted S001–S005 runtime.

It lacked, among other responsibilities:

- a real public PR locator and acquisition path;
- replay invocation and stable run identity;
- operation history;
- complete provenance and degraded evidence states;
- distinct observations, interpretations, and findings;
- transparent baseline versus full decision;
- conditional activation and non-activation;
- same-action, action-change, early-stop, and degraded-evidence flows;
- synchronized machine and human reports;
- follow-up, rerun, supersession, and changed-boundary transitions;
- review, ownership, and whole-run validation.

The detailed original reconciliation remains available at pre-reset commit:

```text
e7425dcfc20f093ac10c9a903f1c4ae50a8b2638
```

## Ali's controlling corrections

After reviewing the reconciliation, Ali directed the project not to assume or evolve the
previous source. His reason was that inherited AI-generated modules and tests could confuse
his learning and silently constrain the new product boundary.

That instruction superseded the preliminary recommendation to evolve selected old modules.

During the subsequent B1 explanation, Ali also rejected a replay-first implementation and
teaching sequence because it began from prepared fixtures and internal lifecycle terminology
rather than what the real product will do.

The accepted consequence is:

> Learn and build B2 from a thin real public PR-to-decision vertical slice. Begin with a
> public repository and Dependabot PR locator, acquire the minimum required public evidence
> read-only, freeze the exact proposal, evaluate it, and produce a bounded recommendation or
> abstention. Capture acquired responses for deterministic tests and later replay, but do
> not make replay the primary product interface or learning path.

Archived implementation may be consulted only for a named comparison, never as an automatic
code baseline.

## Current implemented truth

The active package now contains only:

```text
pyproject.toml                    # minimal package metadata; no runtime dependencies
src/upgradepilot/__init__.py      # fresh package marker only
tests/README.md                   # records that no active product tests exist yet
```

The following are absent from the active tree:

- M2 identity, evidence, decision, extraction, and input-risk modules;
- M2 unit and integration tests;
- local-model clients and evaluators;
- generated root-level model outputs;
- inherited Pydantic and OpenAI runtime dependencies.

No active product behavior is currently claimed beyond the minimal package boundary.

## Historical preservation

The exact old code, tests, scripts, outputs, and package metadata are preserved at the
immutable pre-reset commit and enumerated in the archive manifest.

Historical records under `plans/`, `working-memory/`, and `learning/m2-s02/` remain for
context. They do not control active source or current learning sequence.

## Active architectural state

- ADR-0001 remains accepted for the `src/upgradepilot/` and `tests/` layout.
- ADR-0002 is superseded; Pydantic is not inherited or rejected.
- ADR-0003 controls the clean source reset and non-reuse rule.
- No HTTP client, validation framework, database, service, queue, model, agent, graph, or
  deployment method is selected.
- Minimum live read-only public acquisition is now part of the intended B2 responsibility,
  but its exact interface and method remain for B1 to freeze.

## Validation state

The reset was performed through GitHub file operations and structural inspection.

The active `pyproject.toml` was parsed, the package marker compiled, and an isolated
source-path import succeeded. Therefore:

- the active tree structure is verified through the connector;
- basic TOML, compilation, and isolated import checks passed;
- no clean-checkout or editable-install proof is claimed yet;
- no live GitHub acquisition path or active product test exists yet;
- B2 must establish fresh installation, import, deterministic tests, and an explicitly
  identified live public smoke path.

## Current B1 consequence

B1 no longer needs to classify old modules for reuse or design a replay-only kernel. It must
freeze the first real vertical slice without source inheritance.

The next deliverable must define:

1. the public repository and Dependabot PR input;
2. minimum read-only GitHub and required upstream/package acquisition;
3. exact base/head, changed-file, dependency, and version identity;
4. the first supported dependency-change shape;
5. the bounded evidence-authority evaluation and abstention behavior;
6. the smallest dependency and representation baseline;
7. one bounded user-facing interface;
8. captured-response testing and later replay support;
9. B2 live-smoke, deterministic, failure, and output-consistency tests;
10. Ali-owned implementation, test, diagnosis, and explanation work.

## Non-reuse and non-hardcoding gate

Before any new source is created, the B2 plan must state that:

- archived modules are not imported;
- archived tests are not copied or counted;
- previous class names and file boundaries have no presumption of survival;
- every dependency must be justified again;
- the product accepts a real public PR locator rather than only a prepared fixture;
- S004 or another known PR is not hardcoded;
- captured expected decisions are not consumed by product logic;
- similarities to archived behavior come from current requirements, not convenience;
- Ali receives the minimum complete concept while working on the real responsibility that
  requires it.

## Exact next action

Freeze the clean-slate minimum public PR-to-decision vertical slice. Do not write B2 product
code until that slice, its acquisition and evaluation boundaries, tests, Ali-owned work,
and one bounded implementation plan are accepted.