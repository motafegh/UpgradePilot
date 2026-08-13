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
- **Evidence-design checkpoint:** [`working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md`](working-memory/2026-08-13_B2-target-evidence-design-checkpoint.md).
- **Product-simulation review:** [`working-memory/2026-08-13_B2-product-simulation-review-summary.md`](working-memory/2026-08-13_B2-product-simulation-review-summary.md).
- **Detailed target-environment evidence findings:** [`working-memory/2026-08-13_B2-target-environment-evidence-review-addendum.md`](working-memory/2026-08-13_B2-target-environment-evidence-review-addendum.md).

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

A retained developer-verification area exists:

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

## Current evidence-design findings

Required target facts are derived in this direction:

```text
owned technical claim
→ wheel-serviceability semantics
→ required target facts
→ admissible evidence sources
```

The B2 proportionality rule is:

```text
BROAD EVIDENCE / DESIGN HORIZON
+
SMALLEST SUFFICIENT, DEFENSIBLE IMPLEMENTATION INCREMENT
```

The product-simulation review adds concrete pressure:

- environment evidence is proposition-specific;
- real repository evidence is often partial and scoped rather than a complete exact wheel-tag set;
- multiple legitimate repository environments are real and must preserve per-environment identity/correlation;
- different repository artifacts can describe different scopes or dependency identities without forming one simple contradiction;
- package index/build-family/container/CI/environment intent can all become material depending on the owned proposition;
- an environment pathway can be established while exact compatibility facts remain unresolved;
- broad CI/package exercise is not proof of the exact artifact-selection branch;
- static evidence may be sufficient and should then stop deeper investigation.

The current `TargetWheelCompatibilityEvidence` is therefore only a bounded downstream contract for one already-established environment. It must not be treated as proof that a repository has one canonical environment or that real acquisition can immediately manufacture a complete `Tag` set.

No universal environment reconstruction model is accepted.

## Immediate project action

Do **not** add more source yet.

Discuss the product-simulation findings and detailed evidence-design addendum against the current source boundaries. Decide the smallest explicit target-environment fact responsibility that preserves provenance, scope, partiality, and per-environment identity before deriving exact wheel compatibility.

Then select the smallest defensible implementation slice. A new simulation case is not currently justified merely to discover the broad evidence shapes already present in the corpus.

## Continuation-critical guards

- candidate formulation does not manufacture applicability;
- missing evidence is not negative evidence;
- package evidence and repository-environment evidence remain separate;
- exact repository/revision provenance must be preserved;
- UpgradePilot's own `sys_tags()` is not evidence for another repository environment;
- broad environment labels must not be silently converted into exact wheel tags;
- multi-environment evidence must not be flattened into a repository-wide union that loses environment identity;
- apparent evidence disagreement must be scoped before it is classified as conflict;
- wheel loss, source fallback availability, and source-build success remain separate;
- do not introduce universal planners, registries, environment reconstructors, plugin systems, or similar infrastructure without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

Current learning emphasis is target artifact-environment evidence design: derive required facts from the owned claim, preserve evidence scope and environment identity, distinguish partial evidence from exact compatibility, and use real-case pressure to choose the next bounded implementation.
