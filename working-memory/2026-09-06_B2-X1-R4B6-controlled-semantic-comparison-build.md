# B2/X1 R4-B6 — Controlled R4-A vs R4-B Semantic Comparison Build

**Date:** 2026-09-06  
**Status:** COMPLETE — controlled semantic comparison 4/4 PASS in normal WSL control plane  
**Primary mode:** Learning-by-Doing + Build/Implement  
**Product runtime integration:** not authorized

## 1. Entry evidence

The corrected first native R4-B LangGraph slice has executable proof in the normal UpgradePilot WSL environment:

```text
7/7 PASS
```

That proof established LangGraph import/compile/invoke, no-action routing, fresh-T2 rejection, semantic success, operational-failure handling, and R4-A→R4-B planner adapter mappings for the current focused slice.

R4-B6 then compared R4-A ordinary Python and R4-B LangGraph through a common framework-neutral semantic surface rather than internal implementation equality.

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

## 3. Comparison projection

Added:

`experiments/b2_x1_r4_semantic_comparison.py`

The `EvidenceGapSemanticProjection` compares:

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

The four discriminating scenarios are:

1. **No-action** — `QUESTION_SETTLED`; no external effect; lifecycle/continuation consequence must match.
2. **Fresh-T2 consumed-action rejection** — both implementations reject the stale proposal and preserve the current T2 baseline without repository execution.
3. **Authorized semantic success** — both read the same controlled `pyproject.toml` evidence (`requires-python = ">=3.10"`) and must agree on target evidence, relevance, applicability, budget, and action consumption.
4. **Expected repository failure** — both receive the same controlled timeout and must agree on operational-failure classification, budget spend, no action consumption, and unchanged domain assessment.

Provider-problem translation is not duplicated here because the dedicated adapter family already proves R4-A provider result → R4-B provider outcome mapping. It can be added to the common comparison only if a later proof gap requires it.

## 5. WSL execution proof

User executed after fast-forwarding `main` in the normal UpgradePilot `.venv`:

```bash
python -m unittest \
  experiments.tests.test_b2_x1_r4_semantic_comparison \
  -v
```

Observed result:

```text
test_authorized_semantic_success_semantics_match ... ok
test_expected_repository_failure_semantics_match ... ok
test_fresh_t2_consumed_action_rejection_semantics_match ... ok
test_no_action_semantics_match ... ok

Ran 4 tests in 0.017s

OK
```

Therefore R4-B6 controlled semantic equivalence is green for the bounded comparison surface represented by these four cases.

## 6. Established / not established

Established:

- the comparison module imports and executes successfully in the normal WSL control plane;
- R4-A and R4-B do not need shared internal architecture to be compared fairly;
- both sides normalize into one small accepted semantic surface;
- no-action semantics match;
- fresh-T2 rejection semantics match;
- authorized semantic-success semantics match;
- expected repository operational-failure semantics match;
- budget, consumed-action history, continuation, domain/relevance/applicability consequences represented by the projection match for those cases.

Not established:

- every theoretically possible branch of both implementations is equivalent;
- real LM Studio/provider behavior through R4-B is proven;
- real S001 LangGraph execution is green;
- LangGraph framework value/adoption is established;
- product runtime integration is authorized.

## 7. Learning takeaway

The main comparison lesson is:

```text
semantic equivalence
!=
implementation equality
```

R4-A may use ordinary-Python transitions/traces while R4-B uses LangGraph State/nodes/routing. A fair framework comparison projects both into the same externally meaningful behavioral contract and compares that contract.

This also protects the earlier architecture-coupling correction: comparison must not force R4-B to inherit R4-A representations merely to make equality easy.

## 8. Handoff

R4-B6 is complete for its current bounded proof responsibility.

Next:

```text
R4-B7
→ prepare and execute the bounded real S001 LangGraph smoke
→ real UpgradePilot investigation evidence
→ real controlled planner/model boundary
→ fresh deterministic authority
→ exact real GitHub read
→ deterministic conclusion
```

If that smoke is green, preserve exact execution evidence and then evaluate what LangGraph actually added or cost relative to R4-A before broader R4 disposition work.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`  
`UP-SKILL:upgradepilot-build-implement`
