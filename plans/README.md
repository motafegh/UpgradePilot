# Project-Local Plans

This directory is the canonical home for future detailed UpgradePilot technical plans.

UpgradePilot's charter and 90-day plan control the project horizon and technical execution. Career is consulted only when Ali explicitly requests a career/program review or changes a durable career commitment.

## Ownership boundary

UpgradePilot's charter, operating guide, 90-day plan, current plan, and evidence
own ordinary project execution. Career owns only formal capability assessment,
cross-project workload/capacity, career strategy, and durable program commitments
during an explicit Career review.

UpgradePilot normally owns:

- accepted project-level technical specifications under `docs/specifications/`;
- bounded technical session plans;
- implementation plans;
- experiment and comparison plans;
- test plans when a separate plan is justified;
- multi-step debugging and investigation plans;
- accepted architecture decisions under `docs/architecture/`.

Substantial future ideas that have not been admitted belong under `proposals/`, not here. A proposal may inform a later authorized plan, but it is not itself an execution plan.

## Specifications, decisions, and plans

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

Do not use a plan to hide unresolved product contracts, or use a specification to pre-implement future architecture.

## Current transition

M2-S01 established the trusted case contract. M2-S02 closed with a negative
local-model extraction disposition. The current complete M2 continuation is
`M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`. `MEMORY.md` remains the concise
continuation pointer; source, tests, commands, and outputs remain implementation
truth.

## When a project plan is justified

Create or update a plan when work:

- begins a new authorized responsibility or formal session;
- requires several coordinated steps, files, tests, or decisions;
- is likely to continue across conversations;
- needs an explicit pass condition, stop line, or comparison method;
- could materially change accepted behavior, architecture, dependencies, or evidence.

Do not create another plan for:

- a small explanation or clarification;
- a minor reversible edit already covered by an active plan;
- one localized check or diagnosis that fits the active record;
- work whose steps and gate are already defined adequately;
- speculative future work that has not been authorized.

## Optional organization

Create subdirectories only when real plans require them. Suggested categories are:

- `sessions/`;
- `implementation/`;
- `experiments/`;
- `debugging/`.

Do not pre-create empty directory trees or maintain a separate `completed/` hierarchy merely for appearance. A plan's status and Git history are sufficient unless volume later proves otherwise.

## Plan standard

Use the smallest plan that makes execution unambiguous. A formal plan should normally identify:

- authorized responsibility and user-visible outcome;
- applicable specification and accepted decisions;
- starting state and relevant evidence;
- required concepts or prerequisites;
- files or boundaries allowed to change;
- execution sequence;
- tests or proof;
- ownership evidence;
- pass condition and stop line;
- prohibited scope;
- exact continuation.

Reuse and update the active plan before creating overlapping plans. A plan coordinates work; it does not replace teaching, technical specification, execution, tests, or evidence.
