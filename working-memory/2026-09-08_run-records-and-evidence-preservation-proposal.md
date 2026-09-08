# Run records and evidence preservation proposal

**Date:** 2026-09-08
**Status:** Proposal prepared; implementation not admitted.
**Source snapshot:** `410e106d6a649712ff733e7e083a791eb82a1a17`, synchronized with origin at inspection.

## Request and assessment

Ali requested an analysis of current implementation and plans followed by a new proposal for report export, evidence preservation, deterministic replay and execution recovery, including database choices and surrounding responsibilities. This is supporting work alongside ongoing product integration.

Traced CLI/application return and presentation, GitHub/PyPI acquisition, CI and target-environment composition, semantic extraction and grounding, and experiment save/replay boundaries. Reconciled charter, core invariants, delivery route, vertical-slice plan and artifact integration plan. This was a focused system-boundary audit, not an exhaustive parser review or runtime validation.

The normal CLI prints findings without a durable run contract. The returned application object contains substantial typed evidence but omits some transient acquisition/composition and model-call material. Existing simulation/evaluation/temporary experiment artifacts establish useful precedents, not automatic product capture. Storage absence reflects both explicit staged admission and unfinished capability.

## Deliverable and direction

Created the [focused proposal](../proposals/2026-09-08_RUN_RECORDS_EVIDENCE_PRESERVATION_REPLAY_AND_RECOVERY_PROPOSAL.md) and linked it from the existing end-to-end proposal. It provides a source map, four separate capability promises, proposed records/formats and capture points, file/SQLite alternatives, priorities and dependencies, replay/recovery boundaries, failure cases, privacy/retention and acceptance gates.

Recommend inspectable run bundles first unless the first admitted task requires relational history queries, in which case SQLite should be evaluated directly. Capture must happen before transient inputs are discarded. Neither a database nor a saved experiment trace establishes deterministic replay or execution recovery. Product semantics remain owned by domain contracts; static target facts must not become exact compatibility on reload.

No product source, tests, dependencies, CLI, database, simulation or live MEMORY.md changed. The source snapshot records deferred executable proof and later presentation work in the main integration; this proposal does not close those obligations.

## Validation and limits

Check relative Markdown links, balanced fences, whitespace and governance doctor before publication. Official SQLite documentation supports the local-storage, WAL and backup distinctions in the proposal. No product tests, model calls, live acquisition or workflow dispatch are needed for these documentation-only changes; no new runtime proof is claimed. Inspect only intended staged paths before commit and verify local/origin/remote alignment after push.

## Learning cycle

A — DONE: oriented the four distinct promises against current producers, consumers and plans.
B — DONE: drafted one focused, non-controlling proposal with concrete admission/proof criteria.
C — DONE: preserved source snapshot, findings, scope and limitations here; live continuation remains elsewhere.
D — explanation supplied; learner ownership response pending. Review prompt: why can a saved final result reproduce a report but still be insufficient to replay the reasoning?
E — pending learner response and selection of the first storage task; reconcile the then-current application contract before implementation.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-working-memory`.
