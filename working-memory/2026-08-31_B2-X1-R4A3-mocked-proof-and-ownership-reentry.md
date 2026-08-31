# B2/X1 R4-A3 — mocked proof and ownership re-entry

**Date:** 2026-08-31  
**Mode:** Learning-by-Doing / Build with ownership repair  
**Scope:** A1+A2+A3 ordinary-Python experiment seam

## Observed focused proof

Ali ran:

```bash
python -m unittest discover \
  -s experiments/tests \
  -p 'test_b2_x1_evidence_gap_*.py' \
  -v
```

Observed result:

```text
Ran 36 tests in 0.006s
OK
```

Breakdown:

```text
R4-A1 planner boundary
→ 10/10 PASS

R4-A2 deterministic admission
→ 13/13 PASS

R4-A3 mocked model/provider seam
→ 13/13 PASS

combined focused suite
→ 36/36 PASS
```

This establishes the focused mocked/source boundary behavior for A1+A2+A3. It does **not** establish live LM Studio behavior, planner semantic quality, capability execution/update, production reliability, or product/framework adoption value.

## Learning/ownership re-entry trigger

After the green run, Ali explicitly reported that the new source had materially outrun his current understanding: the source files appeared too large/complex and he could not yet explain what he should learn from them.

This fires the active R4 learning-depth map's cross-stage re-entry rule:

```text
implementation proof green
+
learner cannot accurately explain the mechanism needed for the next material decision
→ pause further implementation/live inference briefly
→ restore the minimum-complete mental model against the real source
→ resume only when the next step is meaningful
```

This is not a switch to a detached Python course. The learning target is the actual ordinary-Python planner flow:

```text
EvidenceGapPlannerContext
→ explicit model projection
→ LocalEvidenceGapPlanner / LM Studio request-response
→ EvidenceGapDecision
→ fresh deterministic admission
→ AdmittedInvestigationAction OR typed problem
```

## Learning order

Use runtime responsibility order rather than file creation order:

1. `experiments/b2_x1_evidence_gap_planner.py` — model-visible state and decision contract;
2. `experiments/b2_x1_evidence_gap_model.py` — local provider/model invocation boundary;
3. `experiments/b2_x1_evidence_gap_admission.py` — trusted rebinding and execution authorization.

Tests are learned after each owning mechanism, not as 36 independent cases.

## Required practical concepts before live inference

Understand at practical ownership depth:

```text
dataclass / frozen / slots
basic annotations, X | None, tuple[X, ...], Literal
__post_init__ invariants
explicit projection
JSON Schema vs Python parser
Mapping[str, Any] as broad untrusted response view
JSON dumps vs loads
requests Session / POST / timeout at practical level
try/except and typed invocation problems
provider envelope vs model message content
runtime narrowing with isinstance
early-return guards
stable action-ID rebinding
TOCTOU
proposal != authorization
```

Keep deeper dataclass/typing internals, requests internals, advanced JSON Schema, generic provider abstractions, retry frameworks, async/concurrency, LangGraph and LangChain mechanics deferred behind their existing triggers.

## Next continuation

Do not run the live LM Studio planner smoke yet. First complete a bounded A1→A3→A2 source walkthrough using the real code and reach enough ownership to explain the end-to-end responsibility and the major syntax/control-flow mechanisms. Then resume R4-A3 live inference.
