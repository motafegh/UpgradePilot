# UpgradePilot Current Memory

**Last updated:** 2026-08-12  
**Authority:** Sole repository owner of live project position, latest material verification, blockers affecting continuation, selected continuation, and current learning depth.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Controlling route plan:** [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](plans/UPGRADEPILOT_90_DAY_PLAN.md).
- **B2 parent plan:** [`plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md).
- **Selected B2 responsibility:** [`plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`](plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md), revised for responsibility-shaped generality and continued end-to-end convergence.
- **Planning correction:** [`working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md`](working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md).
- **Verified first runtime-loop record:** [`working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md`](working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md), recorded at `89c13a85031478f571938b951719147d59e48328`.
- **Transfer checkpoint / second-mechanism entry:** [`working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md`](working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md), recorded at `3ee7fe00554155c337d2e89a1d92d3209eac3d11`.
- **Current artifact-serviceability increment record:** [`working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md`](working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md), recorded at `18fedb4fd5f217473b8a74f9a35be9b2734e5a32`.
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).

## Current implementation truth

### First technical mechanism — Python support drop

The first Python-support **technical impact candidate → candidate-specific applicability → discriminating investigation → observation feedback → reevaluation** runtime loop is implemented and fresh local verification is green.

Verified runtime shape:

```text
grounded Python-support-drop claim
→ build PythonSupportDropImpactCandidate
→ evaluate before target evidence
→ applicability unresolved because exact target declaration is not yet acquired
→ select exact target-declaration acquisition
→ execute existing read-only exact-head repository read
→ interpret target declaration
→ evaluate Target-Python relevance
→ reevaluate the same candidate
→ preserve post-observation applicability
```

The runtime preserves pre-investigation assessment, selected investigation, and post-observation assessment separately. The selector remains Python-support-specific and does not blindly repeat the same target acquisition after target evidence/problem state exists.

### Transfer checkpoint — complete

The implementation-grounded checkpoint against S006/S007/S008/S009 is complete.

Accepted conclusions at this point:

- generic proposition/path/candidate applicability composition transfers beyond Python support;
- the broader lifecycle `current state → justified investigation/stop → observation → reevaluation` is a demonstrated responsibility pattern, but not yet a demonstrated generic planner/data type;
- Python-support candidate semantics, Target-Python overlap, and its exact target-declaration selector remain mechanism-specific;
- S006 preserves pressure for targeted dynamic investigation when static evidence is insufficient;
- S007 preserves positive stopping and future revalidation/pruning pressure when new static evidence makes an investigation unnecessary;
- S009 confirms repository purpose/provenance context must remain separate from technical applicability and feed later overall synthesis;
- `PublicPullRequestInvestigation` now shows real field-per-mechanism pressure, but no refactor is authorized until the second mechanism is integrated enough to reveal actual shared structure.

No generic planner, registry, plugin system, universal impact result, or orchestration framework has been introduced.

### Second technical mechanism — artifact serviceability / installation mode

Phase 3 has started with an S008-style artifact-serviceability mechanism.

Increment 1 source/tests are present:

- `b25529c74c3025666fae74f36eac95611d72a99d` — focused `tests/test_artifact_serviceability.py`;
- `c6d1c4bde7b9d972ba86927269e0e6071f16f1ed` — `src/upgradepilot/impact/artifact_serviceability.py`.

The new target-agnostic builder consumes:

```text
exact PullRequestIdentity
+ exact DependencyVersionChange
+ exact old PackageReleaseEvidence
+ exact proposed PackageReleaseEvidence
→ published artifact-inventory transition interpretation
```

Implemented behavior:

- validates exact package + old/proposed release identity;
- interprets published wheel filenames with `packaging.utils.parse_wheel_filename()` rather than handwritten parsing;
- preserves exact parsed wheel compatibility tags;
- computes published wheel tags removed/added across the exact release transition;
- preserves old/proposed source-distribution presence separately;
- creates an `ArtifactServiceabilityImpactCandidate` only when an exact published wheel compatibility tag disappears;
- keeps target exposure `to_evaluate` and consequence only `possible`;
- returns `None` when the bounded artifact-loss mechanism is not observed rather than manufacturing a candidate;
- preserves malformed/conflicting wheel evidence as an explicit evidence problem;
- does not claim source-build success from sdist presence.

Critical semantic boundary:

```text
removed published wheel tag(s)
!= exact target loses a compatible wheel

proposed sdist exists
!= source fallback succeeds
```

Target interpreter/ABI/platform applicability is deliberately not implemented yet.

## Latest material verification

### Verified first mechanism

Fresh 2026-08-12 local verification reported:

```text
focused runtime-investigation tests: GREEN
nearest relevant regressions: GREEN
full active test suite: GREEN
```

No exact fresh count/timing transcript was captured, so do not invent one.

### Second mechanism Increment 1

Current evidence status:

```text
source implementation: PRESENT
focused tests: PRESENT
GitHub static consistency review: PASSED
fresh executable test run in normal UpgradePilot environment: PENDING
```

Do not claim Increment 1 runtime verification until it is executed in the normal repo environment.

## Planning/execution rule now in force

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE

broad responsibility horizon
+
small implementation/learning increments
+
materially different real-case pressure
+
evidence-earned abstraction
+
continued end-to-end convergence
```

The second mechanism exists to pressure the architecture with genuinely different packaging/environment-formation semantics, not to hardcode S008/CARLA/OpenCV.

## Immediate project action

The current gate is **fresh executable verification of artifact-serviceability Increment 1**.

Run the focused test first in the normal UpgradePilot environment:

```bash
.venv/bin/python -m unittest tests.test_artifact_serviceability -v
```

If green, run the nearest package-evidence regression and then the active full suite before advancing source breadth.

If any failure appears, diagnose the current increment before adding target-environment applicability.

## Next implementation increment after green verification

Increment 2 will add the smallest justified **target artifact-environment evidence + candidate-specific applicability** responsibility.

Owned question:

> What exact admitted target-environment evidence is sufficient to establish, refute, or leave unresolved whether the target had a compatible old published wheel path that the proposed release no longer provides?

Important constraints:

- wheel compatibility is interpreter + ABI (Application Binary Interface) + platform, not just a Python version string;
- do not use UpgradePilot's own local `sys_tags()` as a proxy for a remote target environment;
- keep target environment evidence separate from package artifact inventory evidence;
- reuse the generic applicability composition only where the proposition semantics genuinely fit;
- do not collapse package/interpreter admissibility, binary wheel availability, source-distribution fallback availability, and source-build success;
- do not authorize native/source builds merely because source-build success remains unresolved.

After target applicability exists, the next step is bounded investigation/positive stopping, then real `PublicPullRequestInvestigation` integration. Only after the second mechanism is integrated should the project decide whether the current field-per-mechanism orchestration shape earns a shared result collection/tagged union/protocol.

## Continuation-critical guards

- candidate formulation does not manufacture target exposure/activation/completeness/consequence truth;
- missing evidence is not negative evidence;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- identical failed/unavailable investigation is not blindly retried;
- selected investigations may need revalidation/pruning when later evidence removes their discriminating value;
- `no further justified investigation` is a positive technical outcome distinct from unresolved evidence;
- successful execution is not automatically valid evidence;
- investigation stopping is not overall evidence sufficiency or final maintainer action;
- technical applicability remains separate from repository purpose/policy/provenance context;
- do not introduce a universal impact engine, generic planner, generic rules framework, arbitrary dependency graph, plugin system, opaque scalar score, persistence/service/queue infrastructure, or target mutation without demonstrated need.

## Learning state

Current learning focus is practical architecture through a second genuinely different mechanism.

Immediate concepts being practiced:

- wheel filename compatibility tags as interpreter + ABI + platform;
- authoritative library parsing rather than handwritten packaging syntax;
- package artifact capability change versus exact target applicability;
- why a source distribution is an available fallback artifact but not proof of successful installation;
- when duplicated mechanism-specific contracts are healthier than premature abstraction;
- how a second real implementation provides evidence for or against future shared orchestration/result contracts.
