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
- **Verified first runtime loop record:** [`working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md`](working-memory/2026-08-12_B2-first-runtime-investigation-local-verification.md).
- **Transfer checkpoint / second-mechanism entry:** [`working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md`](working-memory/2026-08-12_B2-transfer-checkpoint-second-mechanism-entry.md).
- **Current second-mechanism increment:** [`working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md`](working-memory/2026-08-12_B2-artifact-serviceability-increment-1.md).
- **Accepted source organization:** [`docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`](docs/architecture/ADR-0007-responsibility-based-python-subpackages.md).

## Current implementation truth

### First mechanism — Python-support reasoning loop

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

`PublicPullRequestInvestigation` preserves separately the pre-investigation assessment, selected investigation, and post-observation result. The selector remains Python-support-specific and does not blindly repeat the same target acquisition once target evidence/problem state exists.

### Architecture/transfer checkpoint

The implementation-grounded S006-S009 checkpoint is complete.

Current conclusion:

- generic proposition/path/candidate applicability composition remains useful across materially different mechanism pressure;
- the lifecycle idea `current state → justified investigation/stop → observation → reevaluation` appears reusable as a responsibility pattern;
- Python-support candidate semantics, Target-Python overlap, and its exact-target-declaration selector remain mechanism-specific;
- `PublicPullRequestInvestigation` shows emerging field-per-mechanism pressure, but no shared mechanism/result abstraction is accepted yet;
- S008-style artifact serviceability remains the selected second technical mechanism;
- S009 repository purpose/provenance context remains outside technical applicability and belongs to later overall synthesis.

### Second mechanism — Artifact Serviceability Increment 1

Increment 1 is now implemented in:

- `src/upgradepilot/impact/artifact_serviceability.py`;
- `tests/test_artifact_serviceability.py`.

Implemented responsibility:

```text
exact dependency transition
+ exact old PyPI release inventory
+ exact proposed PyPI release inventory
→ parse published wheel compatibility tags
→ compare old/proposed tag sets
→ preserve removed/added published tags
→ preserve old/proposed sdist presence
→ formulate target-agnostic artifact-serviceability candidate when evidence justifies it
```

Critical semantic guards:

```text
removed published wheel tag
!= exact target loses a compatible wheel

proposed sdist exists
!= source fallback succeeds
```

Target environment compatibility remains intentionally unimplemented until Increment 2.

## Latest second-mechanism verification / diagnosis

Fresh local execution of:

```text
.venv/bin/python -m unittest tests.test_artifact_serviceability -v
```

produced:

```text
4 tests run
3 passed
1 failed
```

The failure was the main real-world-style removed-wheel-tag candidate test. The implementation returned `wheel_filename_uninterpretable` for:

```text
demo-2.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

Diagnosis:

- source used `packaging.utils.parse_wheel_filename(..., validate_order=True)`;
- `validate_order=True` adds canonical compressed-tag ordering validation;
- that strict lint is stronger than this product responsibility needs because UpgradePilot must interpret published artifact tag evidence rather than reject a parseable published wheel solely for compressed-component ordering;
- normal `parse_wheel_filename()` parsing still validates wheel syntax/identity while returning the compatibility `Tag` set needed here.

Correction:

- `69dc1f1252997bc845a8b3c2b51bdcfc93bd7e9c` — removed strict order lint from published-wheel evidence interpretation while retaining normal wheel parsing and explicit package/version identity validation;
- the failing test remains unchanged and now serves as a regression test for this real evidence shape;
- working-memory diagnosis recorded at `316bc7de6dce5ab9c7893e4f8e5052c6d296e0f6`.

Current proof classification:

```text
Increment 1 source: PRESENT
Increment 1 focused tests: PRESENT
first local execution: FAILED usefully and diagnosed
source correction: PRESENT
post-correction focused execution: PENDING
```

Do not claim Increment 1 green until the corrected tests are rerun locally.

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

Product-simulation cases remain transfer/adversarial evidence, not a sequential implementation backlog.

## Immediate project action

1. pull `main` through the artifact parsing correction;
2. rerun `tests.test_artifact_serviceability`;
3. if green, run the nearest PyPI/package regressions and then the full active suite;
4. record fresh green verification;
5. then begin **Artifact Serviceability Increment 2 — exact target artifact-environment evidence + candidate applicability**.

Increment 2 must answer the concrete question:

> What exact admitted target-environment evidence is sufficient to establish, refute, or leave unresolved whether the target had an old compatible wheel path that is absent in the proposed release?

Do not use UpgradePilot's own `sys_tags()` as a proxy for a remote target environment.

## Continuation-critical guards

- candidate formulation does not manufacture exposure/activation/completeness/consequence truth;
- missing evidence is not negative evidence;
- evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct;
- identical failed/unavailable investigation is not blindly retried;
- a selected investigation may need revalidation/pruning if new evidence removes its discriminating value;
- successful execution is not automatically valid evidence;
- investigation stopping is not overall evidence sufficiency or final maintainer action;
- package/interpreter admissibility, binary artifact availability, source fallback availability, and source fallback success remain distinct;
- do not introduce a universal impact engine, generic planner, generic rules framework, arbitrary dependency graph, plugin system, opaque scalar score, persistence/service/queue infrastructure, or target mutation without demonstrated need.

## Learning state

Current demonstrated depth remains **substantial guided implementation exposure with repeated evidence-driven reasoning/debugging; no formal mastery assessment**.

The current learning emphasis is practical packaging evidence and architecture through contrast: interpret wheel compatibility tags correctly, distinguish package artifact facts from target-environment applicability, and use real test failures to tighten evidence-admission rules rather than weakening claim boundaries.
