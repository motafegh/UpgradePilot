# B2/X1 R4-B6 — Controlled R4-A vs R4-B Semantic Comparison Build

**Date:** 2026-09-06  
**Status:** ACTIVE — comparison source/tests written; WSL execution pending  
**Primary mode:** Learning-by-Doing + Build/Implement  
**Product runtime integration:** not authorized

## 1. Entry evidence

The corrected first native R4-B LangGraph slice has executable proof in the normal UpgradePilot WSL environment:

```text
7/7 PASS
```

That proof established LangGraph import/compile/invoke, no-action routing, fresh-T2 rejection, semantic success, operational-failure handling, and R4-A→R4-B planner adapter mappings for the current focused slice.

The next plan responsibility is R4-B6: compare R4-A ordinary Python and R4-B LangGraph through a common framework-neutral semantic surface rather than internal implementation equality.

## 2. Comparison rule

```text
same bounded scenario
→ R4-A ordinary Python
→ normalize accepted observable semantics

same bounded scenario
→ R4-B LangGraph
→ normalize accepted observable semantics

compare normalized projections
```

Do not compare:

- R4-A A-number decomposition;
- R4-A trace class identity;
- LangGraph State fields as implementation objects;
- node count or topology as semantic equality;
- explanation text as semantic truth.

Compare only framework-neutral behavior that matters to the accepted responsibility.

## 3. New comparison projection

Added:

`experiments/b2_x1_r4_semantic_comparison.py`

The `EvidenceGapSemanticProjection` currently compares:

- planner semantic outcome;
- selected action id when applicable;
- authority status and rejection reason;
- whether the external effect was attempted;
- final outcome family;
- remaining investigation budget;
- consumed-action history;
- continuation status;
- interpreted target semantic state;
- target relevance state;
- final applicability state;
- expected repository operational-failure type/reason.

This module intentionally imports both R4-A and R4-B result forms because it is an evaluation bridge, not either implementation's architecture owner.

A small correction was made immediately during construction: provider/model problems were not allowed to reuse repository operational-failure fields. Those failure classes remain semantically separate.

Commits:

- `53eb9a077da62d77512836f0b1f24ab923687d78` — initial framework-neutral projection
- `632fd3378be64cc5be4c878bbd4ab7a27d41b4c7` — preserve provider vs repository failure distinction

## 4. Controlled comparison tests

Added:

`experiments/tests/test_b2_x1_r4_semantic_comparison.py`

Commit:

`aa6be7bd4652180d4471db65c00d4e2999875d04` — `Add controlled R4-A versus R4-B semantic comparison proof`

The first four discriminating scenarios are:

1. **No-action** — `QUESTION_SETTLED`; no external effect; lifecycle/continuation consequence must match.
2. **Fresh-T2 consumed-action rejection** — both implementations reject the stale proposal and preserve the current T2 baseline without repository execution.
3. **Authorized semantic success** — both read the same controlled `pyproject.toml` evidence (`requires-python = ">=3.10"`) and must agree on target evidence, relevance, applicability, budget, and action consumption.
4. **Expected repository failure** — both receive the same controlled timeout and must agree on operational-failure classification, budget spend, no action consumption, and unchanged domain assessment.

Provider-problem translation is not duplicated here because the dedicated adapter family already proves R4-A provider result → R4-B provider outcome mapping. It can be added to the common comparison only if a later proof gap requires it.

## 5. Current proof boundary

Established by source inspection:

- comparison does not require shared internal architecture;
- both sides are projected into one small semantic surface;
- the four scenarios cover the highest-value current branches;
- R4-A admission/transition and R4-B graph are both exercised rather than comparing hand-written expected dictionaries only.

Not yet established:

- the new comparison module imports successfully in WSL;
- the four comparison tests pass;
- R4-B6 semantic equivalence is green;
- real S001 LangGraph smoke is green;
- LangGraph framework value/adoption is established.

## 6. Immediate handoff

Run in the normal active UpgradePilot `.venv` after pulling main:

```bash
python -m unittest \
  experiments.tests.test_b2_x1_r4_semantic_comparison \
  -v
```

If green, preserve exact proof and advance to R4-B7 real S001 LangGraph smoke preparation/execution. If a case fails, inspect the normalized projection difference first; do not weaken the comparison merely to make it pass.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
