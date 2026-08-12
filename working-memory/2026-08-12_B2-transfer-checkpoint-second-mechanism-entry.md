# B2 Transfer Checkpoint and Second-Mechanism Entry

**Date:** 2026-08-12  
**Type:** Dated implementation/architecture working memory  
**Live-state authority:** `../MEMORY.md` only  
**Selected responsibility:** `../plans/B2_IMPACT_APPLICABILITY_INVESTIGATION_FOUNDATION_PLAN.md`

## Purpose

Record the implementation-grounded transfer checkpoint after the first verified Python-support discriminating-investigation runtime loop, and define the smallest justified entry into the second materially different technical mechanism.

This is not a new broad architecture plan. It records evidence from the actual implementation plus the already-completed S006-S009 simulation cases and selects the next small learning/build increment.

## Evidence inspected

Active product/source evidence:

- `src/upgradepilot/impact/applicability.py`
- `src/upgradepilot/impact/python_support.py`
- `src/upgradepilot/investigation.py`
- `src/upgradepilot/pypi/release.py`
- `src/upgradepilot/ci/dependency_exercise.py`
- `src/upgradepilot/github/actions.py`
- `src/upgradepilot/target/`
- `pyproject.toml`

Transfer/adversarial evidence:

- `../product-simulation/S006_POST_CASE_SYNTHESIS.md`
- `../product-simulation/S007_POST_CASE_SYNTHESIS.md`
- `../product-simulation/S008_POST_CASE_SYNTHESIS.md`
- `../product-simulation/S009_POST_CASE_SYNTHESIS.md`
- S008 target-installation-context artifact where needed to understand the evidence shape.

Library-method check:

- current project dependency is `packaging>=26.2,<27`;
- `packaging.utils.parse_wheel_filename()` is the admitted library method for parsing wheel filenames into normalized identity/version/build/tags;
- wheel tags represent interpreter + ABI + platform compatibility;
- remote Linux compatibility must not be approximated from UpgradePilot's own runtime tags. The packaging API explicitly treats non-running Linux environment compatibility as specialized environment knowledge.

## Transfer findings

### 1. What is genuinely reusable now

The first mechanism plus S006-S009 support keeping these shared concepts:

```text
PropositionAssessment
→ ApplicabilityPathAssessment
→ CandidateApplicabilityAssessment
```

The current generic composition remains useful because materially different mechanisms can still preserve:

- established / refuted / unresolved / conflicted proposition state;
- evidence coverage separate from proposition truth;
- conjunctive path composition;
- candidate-level applicability separate from path-model coverage;
- missing evidence distinct from negative evidence.

The following lifecycle idea is also broader than Python support:

```text
current candidate/evidence state
→ determine whether a discriminating next observation is justified
→ select / stop / later prune
→ validate observation
→ reevaluate
```

This is a demonstrated responsibility pattern, but it is **not yet a demonstrated shared data type or generic planner**.

### 2. What remains Python-support-specific

Do not generalize these merely because the first loop works:

- `PythonSupportDropImpactCandidate`;
- Target-Python overlap semantics;
- `PythonSupportDropInvestigationSelection`;
- `pyproject.toml` as the discriminating target;
- the exact `not-yet-acquired target declaration` selector logic;
- Python-support mechanism fields currently carried by `PublicPullRequestInvestigation`.

A second implementation must first show which of these have a genuine analogue.

## Case pressure

### S006 — dynamic discriminating observation

S006 shows that a later mechanism may require a targeted dynamic observation when static evidence leaves an exact behavior path unresolved.

It also shows layered activation:

```text
dependency-version activation
+
target code-path activation
```

Do not create a generic differential-test executor now. Preserve this as pressure on future investigation contracts.

### S007 — investigation pruning and positive stopping

S007 shows the opposite outcome:

```text
a check looked useful
+
new authoritative static evidence resolves the proposition
→ prune the check
```

The current Python-support implementation selects and executes its read immediately inside one orchestration call, so there is not yet a real temporal gap in which a queued selection can become stale. Therefore do not invent a queue/cancellation framework. Preserve the rule that any future delayed/conditional investigation must be revalidated before execution.

`no further check justified` is a positive reasoning result, not the same as evidence unavailable.

### S008 — selected second technical mechanism

S008 is the strongest next implementation contrast because it changes the technical mechanism from support-range semantics to package artifact/environment-formation semantics while remaining largely static/read-only.

Required distinctions:

```text
package/interpreter admissibility
!= binary artifact availability
!= source fallback availability
!= source fallback success
```

The current PyPI provider already preserves exact release distribution filenames, package types, URLs, and digests. This is enough raw evidence to begin interpreting wheel/sdist inventories.

Important current gaps:

1. current application orchestration acquires the **proposed** release but not the exact old release for the same dependency transition;
2. the target package currently models target Python declaration/relevance, not a general exact wheel-compatibility environment;
3. current CI interpretation proves only a narrow dependency-exercise claim and does not model remote interpreter/ABI/platform compatibility;
4. therefore target artifact compatibility must remain a separate later evidence/applicability step rather than being guessed during artifact inventory interpretation.

### S009 — later synthesis boundary

S009 confirms:

```text
technical impact/applicability
!= repository purpose/policy/provenance context
```

Do not force reproducibility/provenance context into the technical applicability model. Preserve it for the later overall evidence-sufficiency / maintainer-facing synthesis responsibility.

## Architecture pressure observed

`PublicPullRequestInvestigation` now has three Python-support-specific fields around pre-state / selected investigation / post-state.

A second mechanism will create real pressure against continuing one dedicated field group and branch per mechanism. That pressure is now visible, but **do not refactor yet**.

Required order:

```text
implement second mechanism enough to integrate
→ observe actual common result/orchestration shape
→ then decide whether a shared collection/tagged union/protocol is earned
```

Do not introduce a registry, plugin system, generic planner, or universal impact result before that evidence exists.

## Selected second-mechanism implementation path

### Increment 1 — target-agnostic artifact transition candidate

Use exact old/proposed `PackageReleaseEvidence` plus the exact `DependencyVersionChange` to interpret published artifact inventories.

Use `packaging.utils.parse_wheel_filename()` rather than handwritten wheel parsing.

Preserve at minimum:

- exact dependency identity;
- exact old/proposed release identity;
- parsed old wheel filenames/tags;
- parsed proposed wheel filenames/tags;
- whether old/proposed source distributions exist;
- exact wheel-tag compatibility combinations no longer published by the proposed release;
- possible consequence only, not target applicability.

Important semantic boundary:

```text
removed published wheel tag(s)
!= target loses a compatible wheel
```

Target loss can be established only after target-environment compatibility evidence exists.

If no published wheel-tag capability is lost, do not manufacture an artifact-loss candidate.

### Increment 2 — target artifact-environment evidence + applicability

After Increment 1 is tested, determine the smallest admitted exact target environment evidence that can establish or leave unresolved whether the target is compatible with old/proposed wheel inventories.

Do not derive remote Linux compatibility from local `sys_tags()`.

The likely model should preserve target environment evidence separately from wheel inventory evidence and then reuse generic proposition/path composition only where the semantics fit.

### Increment 3 — investigation/stop behavior

Once applicability can be unresolved for a concrete missing environment fact, select a bounded read-only investigation only when it can discriminate that proposition.

If exact static package/target evidence already resolves the owned artifact transition, stop without source-build execution.

Source-build success remains a different downstream proposition and must not be auto-activated.

### Increment 4 — real application integration

Integrate through `PublicPullRequestInvestigation` using real old/proposed package evidence and real target evidence. Only then evaluate the field-per-mechanism orchestration pressure and decide whether a shared result shape is earned.

## Immediate learning/build step

Proceed test-first with Increment 1.

The learning target is small and operational:

1. understand what a wheel compatibility tag represents: interpreter + ABI + platform;
2. use `parse_wheel_filename()` to obtain exact tags from real-style wheel filenames;
3. compare old/proposed published tag sets without confusing that comparison with target compatibility;
4. model source-distribution presence separately;
5. build the first artifact-transition candidate only when exact published artifact evidence justifies it.

## Guardrails

Do not:

- hardcode OpenCV, CARLA, Python 3.6, or the S008 answer;
- hand-parse wheel tag syntax;
- use UpgradePilot's current Linux runtime as a proxy for the target repository environment;
- equate no wheel with impossible installation;
- equate an sdist with successful source installation;
- run arbitrary target code or native builds;
- refactor `PublicPullRequestInvestigation` before the second mechanism creates concrete integration evidence;
- introduce a generic investigation planner/registry/plugin system.

## Checkpoint result

```text
Phase 1 verified Python-support runtime loop
→ COMPLETE

Phase 2 implementation-grounded transfer checkpoint
→ COMPLETE

Phase 3 second technical mechanism
→ ENTERED
→ first increment = target-agnostic exact artifact-inventory transition candidate
```
