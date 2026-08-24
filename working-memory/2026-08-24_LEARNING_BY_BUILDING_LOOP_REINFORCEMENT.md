# Learning-by-Building Loop Reinforcement — 2026-08-24

## Context

During B2 R2, the assistant completed a substantive Audit/Design + Build slice, recorded the implementation state, and then moved directly toward runtime validation. A pre-implementation orientation had been given, but the completed implementation slice did not receive a deliberate post-action learning/onboarding closure before the next engineering gate.

Ali clarified the intended project working loop:

```text
pre-action explanation/onboarding
→ real bounded project work
→ inspect actual evidence
→ preserve material state
→ post-action explanation/onboarding
→ proportional learner reasoning/ownership
→ next bounded slice
→ repeat
```

The learning depth must remain adaptive. Small/familiar work may need a short closure; a new architectural, semantic, proof, debugging, or implementation mechanism may require a larger walkthrough. The assistant must not wait for Ali to explicitly request teaching after substantive work.

## Governance change

Root `AGENTS.md` now begins with a high-salience **Mandatory Learning-by-Building execution loop** that reinforces the existing canonical Learning-by-Doing method in `OPERATING_GUIDE.md` and the reusable procedure in `.agents/skills/upgradepilot-learning-by-doing/SKILL.md`.

The reinforcement explicitly requires:

1. smallest real responsibility/question/failure + primary operation;
2. pre-action orientation sufficient for the coming action;
3. real bounded work;
4. actual evidence inspection and model correction;
5. material state preservation in the correct owner;
6. post-action learning closure based on what actually happened;
7. proportional learner reasoning/ownership;
8. repeat for the next bounded slice.

It also records two important failure-prevention rules:

- pre-action orientation does **not** replace post-action learning closure;
- if later validation depends on Ali's local environment, the assistant must still close the learning loop for the completed work, record validation as pending, then treat validation/result interpretation as the next bounded slice.

## Scope and ownership

This is a governance/working-method reinforcement only.

It does **not** change:

- R2 product behavior;
- the accepted B2 reconciliation plan boundaries;
- action authorization rules;
- R2/R3/R4/R5 sequencing;
- evidence/proof requirements;
- the canonical responsibility allocation in `OPERATING_GUIDE.md` or the Learning-by-Doing Skill.

No product source or test file was changed by this governance slice.

## Immediate continuation implication

Before asking Ali to perform the pending R2 local runtime validation, close the missed post-action learning/onboarding step for the already-implemented R2 shared `uv.lock` structural-owner slice. Then treat focused local validation as the next bounded Learning-by-Building slice and repeat the loop from evidence through post-action interpretation.
