# Project-Local Plans

This directory is the canonical home for future detailed UpgradePilot technical plans.

Career controls the program horizon and authorization. UpgradePilot controls the technical execution details for the bounded project responsibility that Career authorizes.

## Ownership boundary

Career owns:

- the 90-day route;
- monthly and weekly priorities;
- daily capacity and operating rules;
- milestone entry and exit gates;
- cross-project allocation;
- capability and evidence tracking.

UpgradePilot owns:

- bounded technical session plans;
- implementation plans;
- experiment and comparison plans;
- test plans when a separate plan is justified;
- multi-step debugging and investigation plans.

## Current transition

`docs/program/career/plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` remains the approved and controlling M2-S01 plan. Do not move, rewrite, or duplicate it while M2-S01 is active.

After M2-S01, Career should authorize the bounded objective and gate, then link to one canonical detailed plan here. Career records the resulting status and capability evidence rather than maintaining a second editable full copy.

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
- starting state and relevant evidence;
- required concepts or prerequisites;
- files or boundaries allowed to change;
- execution sequence;
- tests or proof;
- ownership evidence;
- pass condition and stop line;
- prohibited scope;
- exact continuation.

Reuse and update the active plan instead of creating overlapping plans. A plan coordinates work; it does not replace teaching, execution, tests, or evidence.