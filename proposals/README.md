# Future Proposals

This directory preserves substantial UpgradePilot ideas that may strengthen the product,
evaluation, production orientation, or technical ambition but have not been admitted into
controlling scope.

For repository-wide documentation ownership and the durable decision-promotion lifecycle, see [`../docs/README.md`](../docs/README.md).

## Authority

Files here are **non-controlling proposals**.

They do not:

- authorize implementation, architecture, dependencies, experiments, infrastructure, or route changes;
- override the project charter, route, selected bounded plan, specifications, or accepted ADRs;
- establish accepted behavior or Ali-owned technical capability;
- become admitted merely because they are detailed, attractive, or technically plausible;
- state the live project position or continuation.

When a proposal conflicts with a controlling artifact or accepted architecture decision, the
controlling or accepted artifact governs unless a formal review changes it.

Statements in a proposal about a route, session, architecture, limitation, or implementation
are contextual snapshots from the proposal's recording date. They must not be read as present
state. `../MEMORY.md` is the sole owner of live position and continuation.

The Mature System Horizon is intentionally kept in this non-controlling area because it mixes accepted orientation, partially designed responsibilities, open design, and experimental possibilities. Accepted semantics referenced by that horizon belong to their canonical specification/Charter owner; consequential accepted implementation structures belong to ADRs.

## What belongs here

Use this directory for a substantial, reusable proposal such as:

- a product-capability enhancement;
- a new technical or analytical thesis;
- an ambitious end-to-end extension;
- a production-oriented system improvement;
- a candidate technology or architecture pattern;
- a future experiment family;
- a consolidated brainstorming or audit result worth preserving.

Do not create a proposal file for every casual idea, small clarification, or implementation
detail. Consolidate related ideas when one coherent document is easier to evaluate later.

## Relationship to other areas

- `docs/README.md` maps durable knowledge ownership and promotion.
- `plans/` defines admitted, position-neutral technical execution.
- `proposals/` preserves unadmitted candidate directions and non-controlling horizons.
- `docs/specifications/` records accepted framework-independent behavior/invariants and product decision semantics.
- `docs/architecture/` records accepted consequential implementation/structural decisions.
- `learning/` preserves reusable understanding.
- `working-memory/` records dated material work and reasoning history.
- `MEMORY.md` records the sole live project position and continuation.

A proposal may inform a future specification, plan, Charter change, or architecture decision, but it is none of those by itself.

## Proposal lifecycle

A proposal should state its own proposal status and authority explicitly. Useful lifecycle
states are:

- **Exploratory** — preserved for later analysis; no admission decision made.
- **Candidate** — considered relevant enough for formal comparison or review.
- **Partially admitted** — selected responsibilities entered controlling scope; the remainder stays non-controlling.
- **Admitted** — controlling artifacts adopt the relevant responsibility.
- **Rejected** — evaluated and not selected, with the reason preserved.
- **Deferred** — potentially useful but not admitted at the proposal's recorded time.
- **Superseded** — replaced by a later proposal or accepted decision.

These are proposal-local lifecycle labels, not project-stage status.

Admission requires the appropriate governing review. At minimum:

1. identify the user-visible, evaluation, or operational value;
2. identify the simpler baseline and observed limitation;
3. define the smallest responsibility or experiment;
4. state success, rejection, cost, safety, and ownership conditions;
5. reconcile the idea with the charter, route, relevant evidence, accepted specifications, and accepted architecture;
6. classify any accepted durable conclusion by responsibility and promote it to the canonical owner described in `../docs/README.md`;
7. record consequential implementation/structural decisions in the owning ADR when warranted;
8. create one position-neutral technical plan when execution is justified;
9. select that plan only through `MEMORY.md`.

Admitting part of a proposal does not make the remaining proposal authoritative. The canonical owner should state the accepted portion; the proposal remains the historical/open idea source for everything not adopted.

## Reading rule

Do not read every proposal during ordinary execution. Consult a proposal only when:

- reviewing future product direction;
- `MEMORY.md` or a selected plan points to it;
- evaluating whether a candidate idea should be admitted;
- investigating the origin or rationale of a future concept.

This keeps ambitious thinking available without allowing speculative or stale material to
redirect execution.
