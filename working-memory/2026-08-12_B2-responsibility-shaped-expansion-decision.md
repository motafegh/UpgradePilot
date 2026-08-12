# B2 Responsibility-Shaped Expansion Decision

**Date:** 2026-08-12  
**Type:** Dated planning/design decision record  
**Live-state authority:** `../MEMORY.md` only

## Decision

UpgradePilot keeps incremental learning-by-building, evidence gates, explicit claim limits, and anti-overengineering controls, but changes the interpretation of **bounded implementation** for the remainder of B2.

The design and method horizon is now the **complete owning product responsibility inside the admitted B2 domain**, while implementation still proceeds through small testable increments.

```text
BOUND THE SUPPORTED DOMAIN
NOT THE KNOWN FIXTURE

broad responsibility horizon
+
small implementation increments
+
materially different real-case pressure
+
evidence-earned abstraction
+
continued end-to-end convergence
```

A first case or mechanism is an implementation/proof slice. It must not silently become the architecture horizon.

## Why this correction is needed

Earlier B2 planning deliberately used narrow slices to prevent speculative architecture, premature graphs/planners/frameworks, and case-count-driven scope expansion. That discipline was useful and remains necessary.

The failure mode now visible is different: repeated language such as `smallest slice`, `one bounded case`, and `stop after this proof` can create local optimization around the first implemented mechanism. The current impact/applicability implementation is intentionally anchored on the S001-style Python-support-drop path. Continuing to deepen only that path would provide weak pressure on heterogeneous result contracts, orchestration, mechanism ownership, investigation selection, and later synthesis.

The controlling Minimum Useful Generality specification already gives the correct rule:

> Bound the supported domain, not the known fixture.

It also states that the method-selection horizon is the complete owning responsibility rather than the next fixture or proof case. This decision applies that rule more explicitly to B2 planning and execution.

## What changes

### 1. Small increments remain; small architecture horizons do not

A coding session may still change one function, contract, test, or orchestration seam at a time. But consequential design choices must be evaluated against the broader responsibility they are expected to serve.

Before accepting an abstraction or permanent mechanism shape, ask:

1. What complete product responsibility owns this code?
2. What material variation exists inside the admitted B2 domain?
3. Does the design survive at least one structurally different case without becoming a fixture-specific branch tree?
4. What should remain mechanism-specific rather than being generalized?
5. Is the proposed abstraction supported by two or more real implementations/pressures, or is it speculative?

### 2. Product simulation becomes continuous design pressure, not a feature backlog

The product-simulation workspace remains non-controlling discovery/evaluation evidence.

Do **not** implement S001-S009 sequentially or treat scenario count as progress.

Instead, select the smallest materially diverse pressure set needed for the responsibility being designed.

For the current decision foundation:

- **S001 / Python support drop** — existing concrete implementation anchor.
- **S006 / targeted behavior check** — pressure for a case where static evidence is insufficient and a discriminating dynamic observation has value.
- **S007 / package-family contradiction** — opposite pressure: authoritative static evidence can resolve a proposition and prune execution; a previously selected check may become stale before execution.
- **S008 / artifact serviceability** — preferred second technical mechanism family because it is materially different from Python-support range reasoning while remaining compatible with safe read-only/static evidence acquisition for its first useful form.
- **S009 / reproducibility/provenance context** — boundary pressure showing that decision-relevant repository context must not be forced into technical applicability.

These cases pressure contracts and architecture. They do not authorize universal support for their ecosystems or every investigation used in simulation.

### 3. The second technical mechanism becomes an intentional architecture checkpoint

After the first real discriminating-investigation runtime loop is implemented and verified, B2 should not simply stop the decision-foundation effort because the first mechanism works.

The next expansion is one materially different technical mechanism family. The current preferred candidate is the S008-style **artifact-serviceability / installation-mode transition**, because it pressures:

- package/interpreter admissibility versus artifact availability;
- binary path versus source fallback;
- exact target environment relevance;
- proposition-specific evidence and stopping;
- heterogeneous impact-candidate/result handling;
- application orchestration beyond one `python_support_drop_impact_result` branch;
- static evidence sufficiency without requiring arbitrary target execution.

This does not authorize a universal wheel resolver, environment reconstruction framework, or OpenCV-specific production branch.

### 4. Abstractions must be earned across contrasting mechanisms

The first Python-support implementation appropriately keeps generic proposition/path composition separate from `PythonSupportDropImpactCandidate`.

That pattern should continue:

```text
shared responsibility contract where real sameness exists
+
mechanism-specific evidence/candidate/evaluator where semantics differ
```

Do not respond to broader scope by introducing a `UniversalImpactEngine`, generic `planner`, generic rule tree, generic dependency graph, or a single opaque score.

The second mechanism is specifically an opportunity to discover which interfaces are genuinely shared and which code should remain duplicated or mechanism-specific.

### 5. End-to-end convergence gets higher priority

The project must continue moving vertically toward the B2 user-visible flow rather than indefinitely deepening the pre-action decision foundation.

Expected direction:

```text
complete first candidate → applicability → investigation → observation → reevaluation loop
↓
pressure architecture against materially different simulation evidence
↓
implement one second technical mechanism family
↓
extract only abstractions earned by the two implementations
↓
reconnect heterogeneous technical/context evidence to the minimum overall-sufficiency / maintainer-output question that concretely blocks B2
↓
continue toward public PR → evidence-backed recommendation/abstention → traceable output
```

The later overall-sufficiency/repository-policy/maintainer-synthesis responsibility is still separate and must not be invented prematurely, but it is no longer treated as something to defer simply because the current foundation plan can stop earlier. It should open when the broadened implementation exposes the concrete synthesis dependency.

## What does not change

- Project Charter mission, user, supported decision family, evidence doctrine, and claim limits.
- Public Python / Dependabot product boundary.
- Read-only/non-mutation and security boundaries.
- Distinction among observation, interpretation, evidence quality, uncertainty, and decision.
- Missing evidence is not negative evidence.
- Evidence coverage, path-model coverage, and candidate-discovery coverage remain distinct.
- Candidate generation does not self-authorize applicability or truth.
- Investigation value, UpgradePilot execution admissibility, and later maintainer-facing recommendability remain distinct.
- A failed/unavailable investigation is not automatically retried without a concrete justification.
- Selected investigations must be revalidated against the evidence/proposition state before execution when state can change.
- No target repository code execution merely because a simulation used execution.
- No speculative infrastructure, services, queues, generic graphs, generic planners, or numeric utility framework.
- B3/B4/B5/X1 remain separate route gates; B2 does not need mature-system breadth.

## Planning consequences

The following active owners should reflect this decision:

1. `plans/UPGRADEPILOT_90_DAY_PLAN.md` — stable route principle: complete responsibility horizon + small increments + representative contrast.
2. `plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md` — B2 gate/proof should require representative pressure for central variable-input reasoning rather than accepting one specimen as the method horizon.
3. `plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md` — completion should include the first real investigation loop, a deliberate transfer/architecture checkpoint, one second materially different mechanism family, and an explicit handoff toward the concrete B2 synthesis dependency.
4. `working-memory/2026-08-12_B2-learning-by-building-first-c-session.md` — immediate session sequencing should retain small learning/build steps but remove the implication that breadth itself is forbidden after the first runtime investigation.
5. `MEMORY.md` — live continuation should record the revised sequence and current proof without claiming that any new runtime behavior has already been implemented.

No new product source behavior is established by this planning decision. Source/tests remain the implementation truth.
