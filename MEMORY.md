# UpgradePilot Current Memory

**Last updated:** 2026-08-13  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md).
- **First runtime loop verification:** [`working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md`](working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md).
- **Second-mechanism entry:** [`working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md`](working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md).
- **Artifact Increment 1:** [`working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md`](working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md).
- **Artifact Increment 2 implementation record:** [`working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md`](working-memory/2026-08-13_B2-artifact-serviceability-increment-2-target-applicability.md).
- **Current evidence-design checkpoint:** [`working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md`](working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md).

## Current implementation truth

### First mechanism — Python support

The first Python-support candidate → applicability → discriminating observation → reevaluation loop is implemented and verified green.

Generic proposition/path/candidate applicability composition remains accepted. Python-support semantics and its selector remain mechanism-specific.

### Second mechanism — Artifact serviceability

Increment 1 is implemented and fresh local verification is green.

It compares exact old/proposed PyPI release artifact inventories, parses wheel compatibility tags, preserves sdist availability, and creates a target-agnostic artifact candidate when published wheel capabilities disappear.

Critical guards remain:

```text
removed published wheel tag
!= exact repository loses a compatible wheel

sdist exists
!= source build succeeds
```

Increment 2 source is present in commit `a37edf3b8941d085427c276a68496da2b3282555`.

It adds:

- `TargetWheelCompatibilityEvidence`;
- `TargetWheelCompatibilityProblem`;
- `ArtifactServiceabilityImpactAssessment`;
- `evaluate_artifact_serviceability_impact(...)`.

The evaluator compares complete old/proposed published wheel-tag inventories against an already-established target-supported tag set. A removed old tag alone is not enough because another proposed tag may still serve the same repository environment.

Increment 2 does **not** yet acquire or derive target-environment evidence from a real repository.

## Verification truth

A retained developer-verification area now exists:

- [`tools/verification/README.md`](tools/verification/README.md);
- [`tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py`](tools/verification/2026-08-13_b2_artifact_serviceability_increment2_smoke.py).

Responsibility split:

```text
permanent product regression → tests/
retained developer verification procedure → tools/verification/
observed run evidence → working-memory/
```

Current proof state:

```text
Artifact Increment 1: GREEN
Artifact Increment 2 source: PRESENT
Artifact Increment 2 retained verification procedure: PRESENT
Artifact Increment 2 retained verification execution: NOT YET RUN
Artifact Increment 2 permanent focused regression coverage: NOT YET PRESENT
Artifact Increment 2 fresh executable proof: PENDING
```

Do not classify Increment 2 complete yet.

## Current design question

The hardest current problem is how UpgradePilot may earn target artifact-environment facts from exact repository-owned evidence without guessing missing compatibility properties.

Required target facts are derived in this direction:

```text
owned technical claim
→ wheel-serviceability semantics
→ required target facts
→ admissible evidence sources
```

The B2 proportionality rule is interpreted here as:

```text
BROAD EVIDENCE / DESIGN HORIZON
+
SMALLEST SUFFICIENT, DEFENSIBLE IMPLEMENTATION INCREMENT
```

Therefore `smallest admitted evidence` does not mean choosing one convenient source and ignoring realistic evidence forms.

The upcoming decision must consider real pressure from partial evidence, provenance, multiple repository environments, evidence composition, evidence conflict, and the difference between broad CI exercise and the exact artifact-selection branch. No universal environment reconstruction architecture is accepted.

## Immediate project action

Before further source changes or choosing the first target-environment acquisition method:

1. inspect the existing real `product-simulation/` cases specifically for target-environment evidence shapes;
2. determine which cases inform evidence authority, partial/multiple/conflicting environments, compatibility derivation, and justified stopping;
3. discuss the findings;
4. then decide the first defensible implementation slice.

Product-simulation cases are transfer/adversarial evidence, not a sequential feature backlog.

## Continuation-critical guards

- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance must be preserved;
- UpgradePilot's own `sys_tags()` is not evidence for another repository environment;
- broad environment labels must not be silently converted into exact wheel tags;
- wheel loss, source fallback availability, and source-build success remain separate;
- do not introduce universal planners, registries, environment reconstructors, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is target artifact-environment evidence design: derive required facts from the owned claim, distinguish evidence availability from inference permission, and use real cases to decide the smallest defensible next implementation while keeping the method horizon broad.
