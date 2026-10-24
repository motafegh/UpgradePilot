# Project-specific engineering guide — UpgradePilot fit analysis

**Status:** decision candidate, non-controlling research/learning evidence  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Related study:** `working-memory/2026-10-24_real-world-engineering-practices_project-fit_cycle.md`

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
- `learning/` — reusable educational artifacts and commit-pinned snapshots; intentionally not a live/current system manual or project-status owner.

Therefore the repository has rich authoritative material but lacks one obvious human-facing answer to:

> "I am an engineer joining or returning to UpgradePilot. What is the current system, how do its major parts fit together, what concepts must I understand, and where do I go deeper?"

## Recommended concept

Use a thin **Project Engineering Guide** (working name) as the primary current human mental-model layer for UpgradePilot.

This is closer to a **system/engineering guide** than to a playbook or runbook.

Its responsibility should be:

> Give a technically accurate, current, project-specific mental model of UpgradePilot to a human engineer, while linking to canonical owners rather than duplicating their contracts.

## What it should contain

A useful first version would cover:

1. **Product and decision problem** — concise mission, supported user/action classes and explicit non-goals.
2. **System mental model** — the end-to-end evidence flow from PR locator through acquisition, domain evidence, interpretation/evaluation, Workspace/report/action boundaries and preserved output.
3. **Architecture map** — major source subsystems, their responsibilities and dependency/control relationships.
4. **Core project concepts** — evidence vs interpretation, provenance/authority, unresolved vs unsupported vs missing, applicability, coverage, exact identity, abstention, source retention, Workspace revision, report projection, etc.
5. **Major data/control flows** — representative normal investigation, saved-report/offline-source flow, Workspace/native flow and selected semantic/evaluation flow.
6. **State and persistence model** — what is volatile, what is durable, snapshots/checkpoints/revisions, saved reports, reconstruction/recovery/replay distinctions.
7. **Proof model** — unit/integration/product regression, controlled cases, live acquisition, installed-package proof, hosted proof, experiments and independent usefulness; what each establishes and does not establish.
8. **How to change the system safely** — where new provider evidence, domain semantics, Workspace representations, report fields, action rules or experiments belong; link to specifications/ADRs/plans rather than restating them.
9. **Failure and uncertainty model** — major problem/unknown categories and why the product refuses to collapse them into false certainty.
10. **Navigation map** — direct pointers to current canonical owners for exact semantics, implementation truth, live state, history and learning material.

## What it should NOT become

Do not make it:

- a second `MEMORY.md` or current-task tracker;
- a copy of specifications/ADRs/plans;
- a giant historical narrative;
- an AI-agent instruction file;
- a replacement for README quickstart;
- a collection of exact operational command sequences that belong in runbooks;
- a set of scenario procedures that belong in playbooks;
- a frozen learning snapshot tied to one historical commit.

The guide should describe the **current durable mental model**, and link out for details that have stronger owners.

## Relationship to playbooks/runbooks

Recommended documentation stack:

```text
README.md
  external/product entry + quickstart
        ↓
Project Engineering Guide
  coherent current human mental model of UpgradePilot
        ↓
canonical owners
  Charter / specifications / ADRs / source / tests / MEMORY
        ↓
scenario procedures when justified
  playbooks
        ↓
exact operational procedures when justified
  runbooks
```

A playbook answers "what should we do when situation X happens?" A runbook answers "what exact steps/commands perform operation X?" Neither replaces the engineering guide.

## Why this is useful for UpgradePilot specifically

The project now has enough subsystem depth, evidence semantics, staged migration boundaries and proof distinctions that a new or returning engineer must synthesize many files to recover the whole system. `docs/README.md` solves ownership/findability but intentionally does not teach the whole technical model. `learning/` has valuable detailed snapshots but intentionally remains historical/educational rather than a single current system guide.

A thin engineering guide can therefore reduce orientation cost without creating a second source of truth, provided it obeys a strict "summarize and link, do not re-own" rule.

It also has career/portfolio value: a reviewer can see that Ali understands not only individual code paths but the system architecture, responsibility boundaries, proof model and change discipline in transferable engineering terms.

## Naming candidate

Current preferred name: **UpgradePilot Engineering Guide**.

Possible file location if later adopted:

- `docs/ENGINEERING_GUIDE.md`, or
- `docs/engineering/README.md` only if multiple durable human-engineering guides actually emerge.

Do not create a directory merely for taxonomy. A single file is sufficient until a real second responsibility appears.

## Disposition candidate

**`ADOPT_LATER_IF_EARNED` with a strong positive recommendation.**

This appears materially more useful than a generic engineering handbook because it fills a concrete documentation gap: current project-specific human system understanding. It should be promoted only after this research branch finishes and is reconciled against then-current `main`, because main is actively changing and the guide would be a durable accepted artifact.

## Follow-on playbook trigger

After the Engineering Guide exists, introduce project-specific playbooks only when a recurring scenario requires repeatable judgment that is not already adequately owned by an existing specification, plan, tool or AI procedure. Good candidates may later include evidence-acquisition diagnosis, Workspace recovery, semantic-claim validation or report/projection diagnosis, but none is automatically selected by this recommendation.
