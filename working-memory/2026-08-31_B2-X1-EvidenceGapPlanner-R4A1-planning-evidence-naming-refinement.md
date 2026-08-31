# B2/X1 EvidenceGapPlanner R4-A1 — Planning-Evidence Naming Refinement

**Date:** 2026-08-31  
**Status:** COMPLETE — active R4-A1 implementation vocabulary refined; behavior unchanged  
**Primary operation:** Build / Implement + Learning-by-Doing

## Trigger

Implementation made the earlier design names visibly cumbersome:

```text
EvidenceGapPlanningEvidence
EvidenceGapPlanningEvidenceFact
```

The first `Evidence` belonged to the `EvidenceGapPlanner` domain while the second named the actual evidence object. The names were semantically explainable but unnecessarily repetitive in source and imports.

## Decision

Active experiment vocabulary is now:

```text
PlanningEvidence
PlanningEvidenceFact
```

inside:

```text
EvidenceGapPlannerContext.planning_evidence
```

The enclosing module/context/field already establishes that these objects are evidence supplied for evidence-gap planning, so repeating the full `EvidenceGap` prefix on both child types added cognitive load without adding responsibility information.

`PlanningEvidenceValue` already used the shorter local vocabulary and remains unchanged.

## Migration

Updated active executable files:

- `experiments/b2_x1_evidence_gap_planner.py`
- `experiments/tests/test_b2_x1_evidence_gap_planner.py`

Commits:

```text
source rename
b7cbda1be6e0f74cc806f88f5d054e82a361ba47

test rename
6e956005575c2e5cd133b5f52ac642a287ca2d1a
```

No wire field changed. The model request still uses:

```text
planning_evidence
```

with the same `evidence_kind`, `summary`, and `facts` payload.

## Historical-name policy

Completed R2 design/projection records may retain `EvidenceGapPlanningEvidence` because they are historical provenance for how the concept was developed. They are not active source naming authority.

The selected plan's completed R2 discussion may therefore still contain the former design label until a future substantive plan edit naturally touches that section; current live vocabulary is owned by `MEMORY.md` and executable R4 source.

This follows the Naming Clarity rule to correct active implementation while avoiding repository-wide historical rewrites solely for vocabulary uniformity.

## Proof / limitation

This is a naming-only migration. It does not establish new runtime behavior and does not resolve the already-pending R4-A1 focused runtime validation.

## Continuation

Resume R4-A2 deterministic action rebinding/admission after this naming correction.
