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

## Ali's controlling correction

After reviewing the reconciliation, Ali directed the project not to assume or evolve the
previous source. His reason was that inherited AI-generated modules and tests could confuse
his learning and silently constrain the new product boundary.

That instruction supersedes the preliminary recommendation to evolve selected old modules.

The accepted consequence is:

> Learn and build the B2 runtime from its current responsibility, writing contracts,
> behavior, and tests fresh. Consult archived implementation only for a named comparison,
> never as an automatic code baseline.

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
- No database, service, queue, model, agent, graph, acquisition, or deployment method is
  selected.

## Validation state

The reset was performed through GitHub file operations and structural inspection.

A fresh local installation/import/test command has not been run because the available
execution environment could not resolve `github.com`. Therefore:

- the active tree structure is verified through the connector;
- no clean-checkout or editable-install proof is claimed yet;
- B2 must establish fresh installation, import, and test proof from the new source.

## Current B1 consequence

B1 no longer needs to classify old modules for reuse. It must now freeze the new runtime
responsibility without source inheritance.

The next deliverable must define:

1. the minimum complete replay-to-decision responsibility;
2. what the replay fixture may provide as captured evidence or labeled interpretation;
3. what the active runtime must execute deterministically;
4. the smallest dependency and representation baseline;
5. the bounded application interface;
6. universal and conditional responsibilities;
7. B2 acceptance tests;
8. Ali-owned implementation, test, diagnosis, and explanation work.

## Non-reuse gate

Before any new source is created, the B2 plan must state that:

- archived modules are not imported;
- archived tests are not copied or counted;
- previous class names and file boundaries have no presumption of survival;
- every dependency must be justified again;
- similarities to archived behavior must come from current requirements, not convenience;
- Ali receives the minimum complete concept before implementing or modifying each central
  responsibility.

## Exact next action

Freeze the clean-slate B2 executable responsibility and prepared-input versus
deterministic-runtime boundary. Do not write B2 product code until that freeze and one
bounded implementation plan are accepted.