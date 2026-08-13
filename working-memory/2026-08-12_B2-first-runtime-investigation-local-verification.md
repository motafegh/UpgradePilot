# B2 First Runtime Investigation Local Verification

**Date:** 2026-08-12  
**Type:** Dated local execution evidence  
**Live-state authority:** `../MEMORY.md` only

## Scope

Verify the first Python-support discriminating-investigation runtime loop after the source/test changes through commit `1c7f7a79f7f2b56a572e6c460cdb7f11b7f654d4`.

The verified behavior is intended to preserve this runtime sequence:

```text
grounded Python-support-drop claim
→ build candidate
→ pre-acquisition applicability = unresolved
→ select exact target-declaration acquisition
→ execute existing exact-head read-only acquisition
→ interpret target declaration
→ evaluate Target-Python relevance
→ reevaluate the same candidate
→ preserve post-observation applicability
```

It also preserves the materially different state in which target acquisition/evidence has already been attempted: the same exact acquisition is not blindly reselected merely because applicability remains unresolved.

## Local verification result

Ali pulled the latest `main` changes into the normal UpgradePilot local environment and executed the focused and broader/full test commands requested for this increment.

Reported result:

```text
focused runtime-investigation tests: GREEN
nearest relevant regression tests: GREEN
full active test suite: GREEN
```

No exact test-count/output transcript was captured in this record, so this record does not invent counts or timings. The material verification claim is limited to the reported green local execution of the requested test layers after pulling the implementation.

## What this verifies

Within the exercised deterministic suite, the fresh local run supports that:

- the pre-acquisition Python-support candidate state is represented as unresolved;
- that specific unresolved state selects the exact target Python declaration as the discriminating investigation;
- the selection preserves exact repository/revision/path/reason identity;
- the selected investigation executes through the existing read-only exact-head acquisition boundary;
- the resulting target evidence feeds Target-Python relevance evaluation;
- the same candidate is reevaluated after observation;
- pre-investigation, selected-investigation, and post-observation states remain separately observable in `PublicPullRequestInvestigation`;
- an already-attempted target-evidence/problem state does not automatically select the identical acquisition again;
- the broader active suite remained green for the implementation as tested locally.

## Proof boundary

This verification does **not** establish:

- a generic investigation planner or general investigation abstraction;
- correctness for mechanisms other than the implemented Python-support path;
- universal candidate discovery or applicability coverage;
- runtime revalidation/pruning for every possible stale selected investigation;
- final overall evidence sufficiency;
- maintainer-facing recommendation correctness or merge safety.

## Continuation

The fresh verification gate for the first runtime investigation loop is cleared.

The next responsibility is the implementation-grounded transfer/architecture checkpoint against materially different evidence shapes, especially S006, S007, S008, and S009. The purpose is to determine what the current candidate/applicability/investigation/result/orchestration shape genuinely generalizes, what remains Python-support-specific, and what pressure a second technical mechanism creates.

Unless that checkpoint identifies a stronger lower-cost contrast, the next implementation breadth target remains an S008-style artifact-serviceability / installation-mode mechanism.
