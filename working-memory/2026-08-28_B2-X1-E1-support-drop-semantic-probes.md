# B2/X1 E1 — Support-Drop Semantic Probe Execution Record

**Date:** 2026-08-28  
**Status:** ACTIVE  
**Parent exploration:** `working-memory/2026-08-28_B2-X1-evidence-first-llm-risk-and-design-exploration.md`

## Purpose

Run small live probes through the already-adopted product semantic boundary:

```text
exact tagged changelog / crossed-release window
→ LocalSupportDropExtractor
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ grounded support-drop claim OR explicit problem
```

The goal is to distinguish:

```text
model semantic correctness
from
deterministic source/identity grounding
```

and to learn from actual UpgradePilot behavior before deciding whether additional LLM controls are justified.

## E1.1 — explicit negation / continued support

### Input semantics

Purpose-built exact release text contains:

```text
Python 3.8 support was not dropped; Python 3.8 remains supported.
```

Expected semantic result:

```text
no current Python 3.8 support-drop candidate
```

### Live execution evidence

User-executed on the normal local UpgradePilot/LM Studio system:

```text
case: e1-negated-python-support-drop
candidate_state: no_relevant_claim
candidate_count: 0
grounded_result: UpstreamSupportDropClaimProblem
classification: correct_no_support_drop
output: /tmp/upgradepilot-b2-x1-e1-negated-support-drop.json
```

### Interpretation

Observed model behavior was correct for this case:

```text
explicit negation / continued-support prose
→ no candidate selected
→ deterministic validator returns no-support-drop problem
```

This is evidence that the adopted model + current product prompt/contract handle this one simple explicit-negation case correctly.

It does **not** establish general robustness against semantic ambiguity, future/planned support changes, historical statements, nearby conflicting version statements, or instruction-shaped text. It also does not change the separate offline boundary proposition: if a semantically wrong candidate is produced but is exactly attributable to admitted source text, current grounding primarily proves attribution/identity rather than independently re-solving the English semantics.

### Current disposition

```text
E1.1 live semantic result: PASS
H1 overall: still OPEN
```

Do not add a product guard because E1.1 passed. Continue to the next discriminating semantic case.

## Next probe

E1.2 should test future/planned support-drop wording where the current release explicitly retains support, for example:

```text
Python 3.8 remains supported in this release; support will be dropped in the next major release.
```

Expected result: no current support-drop candidate.
