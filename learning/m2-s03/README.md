# M2-S03 Learning Orientation — Historical Report-First Slice

**Status:** Superseded learning orientation; retained for B1 comparison
**Current route:** [`../../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../../plans/UPGRADEPILOT_90_DAY_PLAN.md)
**Historical plan:** [`../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](../../plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md)

## Why this package remains

The former M2-S03 plan contained useful concepts:

- application composition;
- strict case and evidence contracts;
- deterministic decision authority;
- application, machine, and human representation separation;
- provenance-backed report statements;
- explicit degraded evidence;
- no-model operation;
- changed, missing, invalid, and security-boundary tests.

Those ideas remain candidate building blocks and some may already exist in source
and tests.

## Why it is not the current learning path

S001–S003 showed that the report-first slice omitted or deferred material runtime
responsibilities:

- invocation and discovered/frozen identity;
- operation and acquisition history;
- raw/reference preservation;
- complete evidence-state and authority behavior;
- findings and supersession;
- baseline comparison;
- decision transitions;
- follow-up, rerun, replay, and new-run boundaries;
- review, external confirmation, and ownership state;
- conditional investigation stages.

The old package therefore cannot be resumed as a milestone course.

## How to use it later

During B1:

1. inspect current source and tests;
2. compare each retained concept with S001–S005 evidence;
3. re-admit only correctly scoped requirements;
4. reject or rewrite report-first assumptions that no longer fit;
5. organize new learning around the accepted B2 runtime responsibility.

Until B1, use
[`../product-simulation/README.md`](../product-simulation/README.md) as the current
learning entry point.

This package records historical orientation, not implemented behavior, current
scope, or Ali-owned capability.
