# Product Simulation Learning Package

**Status:** D1 learning package complete; retained for B1 transfer and ownership practice  
**Project route:** [`../../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../../plans/UPGRADEPILOT_90_DAY_PLAN.md)  
**D1 acceptance:** [`../../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md`](../../plans/D1_ACCEPTANCE_AND_B1_ACTIVATION.md)  
**Current stage:** B1 — implementation responsibility freeze

## Purpose

This package preserves the reusable understanding produced by S001–S005:

- complete evidence-to-decision runtime;
- evidence identity, lineage, states, authority, and failures;
- retrospective versus prospective execution;
- CI dependency identity and command responsibility;
- causal attribution;
- baseline comparison;
- sufficiency, stopping, and cost;
- action-changing target evidence;
- universal versus conditional responsibilities;
- automation and human-control boundaries.

It is educational material, not project authority, production schema, or capability
proof.

## Completed case lessons

1. [`06_S001_CASE_LAB_CORRECTION_AND_CALIBRATION.md`](06_S001_CASE_LAB_CORRECTION_AND_CALIBRATION.md)
   — same action can have materially different authority and calibration.
2. [`07_S002_CASE_LAB_CI_AUTHORITY_AND_MISSING_ENVIRONMENT.md`](07_S002_CASE_LAB_CI_AUTHORITY_AND_MISSING_ENVIRONMENT.md)
   — direct dependency and green CI do not prove relevant behavior.
3. [`09_S003_PROSPECTIVE_FAILURE_ATTRIBUTION.md`](09_S003_PROSPECTIVE_FAILURE_ATTRIBUTION.md)
   — red CI requires causal attribution and comparable execution evidence.
4. [`11_S004_BASELINE_SUFFICIENCY_AND_STOPPING.md`](11_S004_BASELINE_SUFFICIENCY_AND_STOPPING.md)
   — a baseline may be sufficient after a narrow authority confirmation.
5. [`12_S005_ACTION_CHANGE_TARGET_RELEVANCE_AND_CI_IDENTITY.md`](12_S005_ACTION_CHANGE_TARGET_RELEVANCE_AND_CI_IDENTITY.md)
   — target-specific evidence can show the baseline chose the wrong broad action.

Foundational lessons remain available in files 01–05 and 08. The ownership workbook is
[`10_OWNERSHIP_WORKBOOK.md`](10_OWNERSHIP_WORKBOOK.md).

## Accepted mental model

```text
dependency-update event
→ invocation
→ exact identity
→ operations and acquisition attempts
→ evidence states and authority
→ claims and interpretations
→ findings and uncertainty
→ transparent baseline
→ authority confirmation or conditional activation
→ bounded decision or abstention
→ machine and human reports
→ follow-up, rerun, and supersession
→ review, stopping, validation, and ownership
```

A case may activate, skip, repeat, or stop responsibilities when evidence requires it.

## B1 transfer

The package's current purpose is to support B1 source/test reconciliation.

Ali should be able to use the case evidence to answer:

- Which runtime responsibilities must exist in every replay?
- Which responsibilities are conditional?
- Which current source components already implement part of the accepted runtime?
- Which old report-first components hide semantic answers or omit required state?
- What may a replay fixture contain as captured evidence or labeled interpretation?
- What must B2 execute and validate deterministically?
- What is the smallest reversible representation that can support same-action,
  action-change, early-stop, and degraded-evidence cases?
- Which test and code change will Ali own centrally?

## Current ownership exercises

During B1:

1. trace one current source path from input to output;
2. compare it with the accepted runtime model;
3. identify one retained behavior and one missing or superseded responsibility;
4. explain why simulation JSON files should not be copied directly as production
   schemas;
5. propose one B2 acceptance test for each of:
   - same-action result;
   - action change;
   - early stop;
   - missing or inaccessible evidence;
6. state which semantic interpretation remains prepared input and why;
7. challenge one proposed representation or interface for unnecessary ceremony.

## Depth state

Current demonstrated state:

- concepts and case mechanisms: AI-produced operational explanation;
- cross-case planning acceptance: completed by Ali;
- implementation transfer: active under B1;
- independent implementation ownership: not yet demonstrated.

D1 acceptance does not automatically raise the mastery level. B1 and B2 must produce
tracing, modification, testing, diagnosis, and explanation evidence.

## Boundaries

This package does not establish:

- final production schemas;
- persistence or service architecture;
- live acquisition behavior;
- automated semantic reliability;
- target-update safety;
- representative frequency;
- B2 implementation authorization;
- independently owned capability.
