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

Increment 1 is implemented and fresh local verification is green.

Implemented in:

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

The candidate therefore establishes a package-release artifact transition without self-authorizing exact target applicability.

### Artifact parsing failure/correction now verified

The first local run exposed an overly strict evidence-admission rule:

```text
parse_wheel_filename(..., validate_order=True)
```

rejected a real-world-style compressed platform tag because its compressed components were not in canonical sorted order.

That was diagnosed as the wrong responsibility boundary: UpgradePilot needs to interpret parseable published artifact compatibility evidence, not lint canonical compressed-tag ordering.

Correction:

- `69dc1f1252997bc845a8b3c2b51bdcfc93bd7e9c` — use normal `parse_wheel_filename()` parsing while retaining normal wheel syntax and explicit package/version identity validation;
- the failing test remained unchanged and now protects this behavior.

Fresh post-correction verification reported by Ali:

```text
focused artifact-serviceability tests: GREEN
nearest PyPI/package regressions: GREEN
full active suite: GREEN
```

No exact fresh full-suite count/timing transcript was captured, so none is inferred.

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

Artifact Serviceability Increment 1 verification is **cleared**.

Before adding more source, use the current implementation as a learning checkpoint so Ali can consolidate the concepts now present in real code:

- candidate vs established applicability;
- proposition/path/candidate composition;
- evidence coverage vs negative evidence;
- discriminating investigation and no-blind-repeat;
- package metadata vs artifact inventory vs target environment;
- wheel interpreter/ABI/platform tags;
- wheel parsing vs formatting lint;
- wheel loss vs source fallback vs source-build success;
- evidence-earned abstraction across the first two mechanisms.

After that learning checkpoint, begin **Artifact Serviceability Increment 2 — exact target artifact-environment evidence + candidate applicability**.

Increment 2 must answer:

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

The current learning emphasis is consolidation of the actual implemented mental model before Artifact Serviceability Increment 2: understand how grounded evidence becomes a bounded candidate, how applicability remains separate, how investigations are selected by unresolved propositions, and how packaging artifact facts differ from target-environment claims.
