# B2/X1 — Execution Proportionality Calibration

**Date:** 2026-08-28  
**Status:** PLAN CALIBRATED — hard evidence/security boundaries preserved; earlier development-only LLM smoke admitted after a smaller deterministic gate  
**Owning plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Accepted evaluation protocol:** `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

## 1. Trigger

Ali clarified a project-wide execution concern that is especially important for LLM/agent work:

```text
avoid too much investigation
avoid perfectionism
avoid treating every rule/check as equally strict
avoid over-engineering and under-engineering
avoid unnecessary ceremony
avoid spending days on pre-LLM preparation when a smaller safe prototype could teach more
```

The concern is not permission to discard safety/evidence discipline. It is a request to calibrate rigor to the actual consequence and to preserve learning breadth/forward progress.

## 2. Governance check

No root governance change was needed.

`OPERATING_GUIDE.md` already owns the relevant principles:

- context is a finite attention budget;
- **Ceremony is a tax** and should be paid only for tangible capability/material risk/real obligation;
- use the least ceremonial route;
- escalate to formal work only for consequential boundaries;
- de-escalate after the consequential issue is resolved;
- planning should select the simplest credible baseline;
- teaching/learning depth is proportional.

`AGENTS.md` already reinforces:

- smallest sufficient context;
- proportionate Learning-by-Doing depth;
- no manufactured ceremony;
- no framework/dependency/layer without demonstrated responsibility.

Therefore the problem was not missing project philosophy. It was the **local X1 execution sequence**.

## 3. Local problem found

The previous X1 plan required the complete Phase-3B protected baseline/replay/grading/manifest harness before the first local planner-model call.

That was defensible for protected scoring, but too strict for a **development-only smoke**. It created a risk that the project would spend several additional implementation slices on evaluation infrastructure before learning whether the available local model can even:

```text
follow the strict output schema
choose the one admitted action on a simple development case
produce a no-tool disposition
respect the bounded planner role
```

The accepted Phase-3 protocol already separates development/calibration from protected scoring and permits development calls under bounded rules, so the stricter all-harness-first ordering was a plan-level sequencing choice rather than an oracle/safety necessity.

## 4. Calibration applied

The owning X1 plan was rewritten into a smaller responsibility-focused execution plan.

The plan now explicitly separates:

```text
HARD / NON-NEGOTIABLE
→ exact identity
→ closed read-only action authority
→ deterministic admission
→ evidence/proof-strength boundary
→ no target mutation
→ protected-set contamination control

PROPORTIONAL PILOT PROCESS
→ documentation depth
→ generalized harness abstractions
→ exhaustive telemetry
→ optional checks
→ full protected infrastructure before development smoke
```

It also adds an anti-rabbit-hole trigger: if roughly two bounded engineering slices in a row add only pre-model preparation without new discriminating evidence, reassess whether the next preparation item is truly required before a development smoke.

## 5. New calibrated route

```text
Phase 3B-1
minimum model-ready deterministic slice
→ request/oracle isolation
→ Phase-2 schema/admission remains green
→ one development action case + one development no-tool case renderable
→ local loopback readiness

Phase 4A
early development-only local LLM smoke
→ normally 3–6 semantic calls
→ development/calibration cases only
→ inspect schema/action/no-tool behavior and obvious failure modes
→ no protected score / no adoption conclusion

Phase 3B-2
only if smoke shows basic viability
→ complete remaining protected cases
→ S001 replay
→ baseline/grading/manifest/shuffle/contamination machinery required for scoring

Phase 4B
protected 24-decision run under the already accepted protocol
```

This reaches real LLM planning earlier without changing the frozen protected oracle.

## 6. Why the accepted protocol was not modified

`B2_X1_PHASE3_EVALUATION_PROTOCOL.md` still correctly owns the final protected-case/oracle/replay/threshold/contamination contract.

Its existing development/calibration section already allows bounded development model calls before protected scoring, and its requirement that the complete deterministic harness pass with no model call means the harness proof itself must be runnable offline; it does not require withholding all development interaction until every scoring component exists.

Changing the accepted protocol would also rotate its accepted blob identity and force unrelated harness/provenance churn without changing the protected evaluation semantics. That would itself be ceremony.

Therefore the calibration was made at the **plan sequence owner**, not the oracle owner.

## 7. Current Slice-1 consequence

The current Phase-3B S001 request/oracle-isolation implementation remains useful and should still receive its focused WSL validation.

After that PASS, the next move is **not** to implement all remaining protected cases before touching the model.

The calibrated next preparation is only what is missing for Phase 3B-1:

```text
one development choose-action case
+ one contrasting development no-tool case
+ minimal local LM Studio transport/readiness boundary
```

Then enter Phase 4A development smoke.

## 8. External engineering cross-check

Current public agent-engineering guidance was checked only to validate the calibration direction, not to create a new research phase. The consistent themes were:

- start with simple prototypes and iterate;
- use early evals rather than requiring a huge eval system first;
- ground tasks in real-world use;
- use simple loops/tools before frameworks;
- add complexity when measurement shows it is needed.

This matches UpgradePilot's existing Ceremony Tax and simplest-credible-baseline rules.

## 9. Learning-by-Doing consequence

The Learning-by-Doing loop remains unchanged, but its depth stays proportional.

For the current route that means:

```text
finish Slice 1 evidence + learning closure
→ build the smallest missing model-ready pieces
→ engage the local LLM early
→ learn from actual planner behavior
→ only then deepen replay/scoring infrastructure where the evidence justifies it
```

This better supports the flagship project's learning goal: cover the important engineering concepts through real work rather than spending most of the LLM checkpoint on pre-model ceremony.
