# Project-specific engineering guide — UpgradePilot fit analysis

**Status:** decision candidate, non-controlling research/learning evidence  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Related study:** `working-memory/2026-10-24_real-world-engineering-practices_project-fit_cycle.md`  
**Concrete pre-template:** `working-memory/evidence/2026-10-24-real-world-engineering-practices/engineering-guide-pretemplate.md`

## Question

Beyond AI-operation procedures under `.agents/skills/`, what project-specific human-facing guide should UpgradePilot have, regardless of whether the final label is handbook, playbook, technical guide, or another name?

## Current documentation reality

UpgradePilot already has several strong but intentionally different owners:

- `README.md` — external/product/reviewer entry point, quickstart, product boundary and operating examples.
- `docs/README.md` — durable documentation/decision navigation and owner-promotion map; explicitly optimized for findability and ownership rather than a coherent system tutorial.
- `PROJECT_CHARTER.md` — stable mission, user, product boundary, evidence doctrine and claim limits.
- `OPERATING_GUIDE.md` and `.agents/skills/` — how Ali/AI work in the repository and reusable operation procedures; these are not a technical model of UpgradePilot itself.
- `docs/specifications/` — controlling framework-independent behavior/semantic contracts.
- `docs/architecture/` — accepted consequential implementation/structural choices.
- `plans/` — bounded future or active responsibility execution/proof plans.
- `MEMORY.md` — sole live project position/continuation owner.
- `working-memory/` — dated engineering journey and provenance: investigations, alternatives, failures, corrections, experiments, proof transitions, implementation handoffs and reasoning that may later be promoted to a durable owner. It is historical evidence/reasoning, not the authority for current accepted semantics.
- `learning/` — reusable educational artifacts and commit-pinned snapshots; intentionally not a live/current system manual or project-status owner.

Therefore the repository has rich authoritative and historical material but lacks one obvious human-facing answer to:

> "I am an engineer joining or returning to UpgradePilot. What is the current system, how do its major parts fit together, what concepts must I understand, how did the important engineering decisions evolve, and where do I go deeper?"

## Recommended concept

Use a thin **Project Engineering Guide** (working name) as the primary current human mental-model layer for UpgradePilot.

This is closer to a **system/engineering guide** than to a playbook or runbook.

Its responsibility should be:

> Give a technically accurate, current, project-specific mental model of UpgradePilot to a human engineer, while linking to canonical owners rather than duplicating their contracts and selectively linking to working-memory when the engineering journey materially explains the present design.

## What it should contain

A useful first version would cover:

1. **Product and decision problem** — concise mission, supported user/action classes and explicit non-goals.
2. **System mental model** — the end-to-end evidence flow from PR locator through acquisition, domain evidence, interpretation/evaluation, Workspace/report/action boundaries and preserved output.
3. **Architecture map** — major source subsystems, their responsibilities and dependency/control relationships.
4. **Core project concepts** — evidence vs interpretation, provenance/authority, unresolved vs unsupported vs missing, applicability, coverage, exact identity, abstention, source retention, Workspace revision, report projection, etc.
5. **Major data/control flows** — representative normal investigation, saved-report/offline-source flow, Workspace/native flow and selected semantic/evaluation flow.
6. **State and persistence model** — what is volatile, what is durable, snapshots/checkpoints/revisions, saved reports, reconstruction/recovery/replay distinctions.
7. **Proof model** — unit/integration/product regression, controlled cases, live acquisition, installed-package proof, hosted proof, experiments and independent usefulness; what each establishes and does not establish.
8. **Engineering journey / design evolution** — selected major transitions from earlier assumptions or failures through experiments/corrections to the current design, with links to the exact working-memory/evidence records. This is selective rationale/history, not a chronological dump.
9. **How to change the system safely** — where new provider evidence, domain semantics, Workspace representations, report fields, action rules or experiments belong; link to specifications/ADRs/plans rather than restating them.
10. **Failure and uncertainty model** — major problem/unknown categories and why the product refuses to collapse them into false certainty.
11. **Navigation map** — direct pointers to current canonical owners for exact semantics, implementation truth, live state, historical reasoning/evidence, and reusable learning material.

## Working-memory's specific role

`working-memory/` should be treated as a first-class **engineering-history/provenance layer** for the guide.

The guide should use it when history materially improves current understanding, especially for:

- why a current architecture/semantic boundary exists;
- which earlier approach failed or proved insufficient;
- how an experiment changed a design decision;
- what regression/failure exposed a missing responsibility;
- how a staged migration evolved;
- why some apparently attractive capability remains rejected/deferred;
- what proof was obtained and what remained unproved at a consequential transition.

A useful pattern is:

```text
current mechanism / decision
→ concise explanation of the pressure or correction that produced it
→ link to current canonical owner for exact accepted rule
→ link to selected working-memory/evidence record for the engineering journey
```

The guide should **not** read like a full project diary. Old working-memory is historical evidence, so it must be reconciled against current source/owners before being presented as present fact.

## What it should NOT become

Do not make it:

- a second `MEMORY.md` or current-task tracker;
- a copy of specifications/ADRs/plans;
- a giant historical narrative or transcript of `working-memory/`;
- an AI-agent instruction file;
- a replacement for README quickstart;
- a collection of exact operational command sequences that belong in runbooks;
- a set of scenario procedures that belong in playbooks;
- a frozen learning snapshot tied to one historical commit.

The guide should describe the **current durable mental model**, and link out for details that have stronger owners.

## Relationship to playbooks/runbooks and history

Recommended documentation stack:

```text
README.md
  external/product entry + quickstart
        ↓
Project Engineering Guide
  coherent current human mental model
  + selective engineering-journey context
        ↓
canonical owners
  Charter / specifications / ADRs / source / tests / MEMORY
        ↘
historical reasoning/evidence
  working-memory / audits / simulations / experiment evidence
        ↓
scenario procedures when justified
  playbooks
        ↓
exact operational procedures when justified
  runbooks
```

A playbook answers "what should we do when situation X happens?" A runbook answers "what exact steps/commands perform operation X?" Working-memory answers "how and why did this engineering state emerge?" None replaces the engineering guide.

## Why this is useful for UpgradePilot specifically

The project now has enough subsystem depth, evidence semantics, staged migration boundaries and proof distinctions that a new or returning engineer must synthesize many files to recover the whole system. `docs/README.md` solves ownership/findability but intentionally does not teach the whole technical model. `working-memory/` preserves a rich engineering journey but is intentionally historical and distributed. `learning/` has valuable detailed snapshots but intentionally remains educational rather than a single current system guide.

A thin engineering guide can therefore reduce orientation cost without creating a second source of truth. It can also make the project's recorded journey useful: instead of forcing a reader to discover hundreds of dated records, it can point to the few historical records that explain the most consequential current mechanisms and corrections.

It also has career/portfolio value: a reviewer can see that Ali understands not only individual code paths but the system architecture, responsibility boundaries, proof model, engineering evolution and change discipline in transferable engineering terms.

## Naming candidate

Current preferred name: **UpgradePilot Engineering Guide**.

Possible file location if later adopted:

- `docs/ENGINEERING_GUIDE.md`, or
- `docs/engineering/README.md` only if multiple durable human-engineering guides actually emerge.

Do not create a directory merely for taxonomy. A single file is sufficient until a real second responsibility appears.

## Disposition candidate

**`ADOPT_LATER_IF_EARNED` with a strong positive recommendation.**

This appears materially more useful than a generic engineering handbook because it fills a concrete documentation gap: current project-specific human system understanding while providing a curated entry into the already-preserved engineering journey. It should be promoted only after this research branch finishes and is reconciled against then-current `main`, because main is actively changing and the guide would be a durable accepted artifact.

## Follow-on playbook trigger

After the Engineering Guide exists, introduce project-specific playbooks only when a recurring scenario requires repeatable judgment that is not already adequately owned by an existing specification, plan, tool or AI procedure. Good candidates may later include evidence-acquisition diagnosis, Workspace recovery, semantic-claim validation or report/projection diagnosis, but none is automatically selected by this recommendation.
