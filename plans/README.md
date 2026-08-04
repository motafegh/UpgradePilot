# Project-Local Plans

This directory is the canonical home for detailed UpgradePilot technical plans.

The project charter controls the stable product boundary. The 90-day plan controls stage
sequence and gates. `MEMORY.md` alone selects the live position and bounded plan.

## Ownership boundary

UpgradePilot normally owns:

- accepted project-level technical specifications under `docs/specifications/`;
- bounded implementation and investigation plans;
- experiment and comparison plans;
- test plans when a separate plan is justified;
- multi-step debugging plans;
- accepted architecture decisions under `docs/architecture/`.

Substantial ideas that have not been admitted belong under `proposals/`, not here. A proposal
may inform a later authorized plan, but it is not itself an execution plan.

## Position-neutral plan rule

A plan defines a responsibility, sequence, proof, and stop line. It must not state:

- which stage or increment is active, passed, pending, or next;
- the latest commit or validation result;
- an immediate blocker or handoff;
- the exact continuation for the project.

Those live facts belong only in `../MEMORY.md`. A plan may link to dated evidence without
turning that evidence into present project status.

## Specifications, decisions, plans, and source layout

Use the artifacts in this order when all are needed:

```text
project charter and route
→ accepted technical specification
→ architecture/method decision when consequential
→ bounded execution plan
→ source, tests, and observed evidence
```

- A specification defines what the system must represent and guarantee.
- An ADR records a selected consequential mechanism or structure.
- A plan coordinates how an authorized responsibility will be executed and proven.
- Source and tests establish the actual implemented organization and behavior.

A plan may name expected files as a bounded modification hint, but it does **not** permanently own directory hierarchy. A later accepted structural ADR may legitimately move the responsibility while preserving the plan's conceptual contract.

When `MEMORY.md` selects an older bounded plan for renewed execution:

1. compare its named source/test/tool paths with accepted architecture decisions and active source;
2. update the selected plan before implementation when those path hints are stale;
3. preserve the plan's responsibility, proof, and stop line unless a separate authorized change alters them;
4. do not recreate deleted compatibility paths merely to satisfy an old filename;
5. do not mass-rewrite unselected older plans or dated evidence solely to make their historical implementation names look current.

Root `../AGENTS.md` owns repository-wide artifact routing. ADR-0007 owns the responsibility-based Python source/test/experiment/tool structure. A plan cannot override either silently.

Do not use a plan to hide unresolved product contracts, or use a specification to
pre-implement future architecture.

## When a plan is justified

Create or update a plan when work:

- begins a new authorized responsibility;
- requires several coordinated steps, files, tests, or decisions;
- is likely to continue across conversations;
- needs an explicit pass condition, stop line, or comparison method;
- could materially change accepted behavior, architecture, dependencies, or evidence.

Do not create another plan for:

- a small explanation or clarification;
- a minor reversible edit already covered by a selected plan;
- one localized check or diagnosis that fits the selected responsibility;
- work whose steps and gate are already defined adequately;
- speculative future work that has not been admitted.

## Optional organization

Create subdirectories only when real plans require them. Suggested categories are:

- `implementation/`;
- `experiments/`;
- `debugging/`.

A `plans/experiments/` directory, if ever justified, would contain **experiment plans**, not executable experiment code; executable non-product evaluation machinery belongs under repository-root `experiments/` according to `../AGENTS.md`.

Do not pre-create empty directory trees or maintain a separate `completed/` hierarchy merely
for appearance. Git history and dated acceptance records preserve plan history.

## Plan standard

Use the smallest plan that makes execution unambiguous. A formal plan should normally
identify:

- authorized responsibility and user-visible outcome;
- applicable specification and accepted decisions;
- required entry evidence or prerequisites;
- unresolved decisions that must be closed before implementation;
- files or responsibility boundaries allowed to change;
- execution sequence;
- tests or proof;
- pass condition and stop line;
- prohibited scope;
- maintenance conditions.

`MEMORY.md` selects the plan and states the exact action. Reuse and update an adequate plan
before creating an overlapping one.
