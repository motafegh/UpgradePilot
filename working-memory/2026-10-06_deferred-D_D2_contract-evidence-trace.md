# Deferred Phase D — D2 supporting note: interpretation contract and real evidence trace

**Date:** 2026-10-06  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Status:** D2 ownership checkpoint COMPLETE; supporting learning evidence pending final D5 reconciliation into the sole cycle-status record.  
**Cycle-status owner:** `working-memory/2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md`.  
**Mutation boundary:** learning documentation only; no product/experiment source, tests, active implementation-cycle record, `MEMORY.md`, specification or ADR change.

## Real contract and trace used

D2 used the frozen preparation artifacts directly:

- `working-memory/evidence/2026-10-05-api-interpretation-preparation/prompt-template-v1.md`;
- `working-memory/evidence/2026-10-05-api-interpretation-preparation/output-schema-v1.json`;
- `working-memory/evidence/2026-10-05-api-interpretation-preparation/source-inputs-v1.json`;
- `working-memory/evidence/2026-10-05-api-interpretation-preparation/evaluation-cases-v1.json`;
- `working-memory/evidence/2026-10-05-api-interpretation-preparation/schema-review-examples.json`.

The primary authentic trace was HTTPX 0.28.0 input `I002`, where producer-controlled source identity and line mapping establish the exact changelog excerpt containing the `app` argument removal. The model role is limited to proposing semantic meaning from supplied source, not source authority, target impact, compatibility, safety or maintainer action.

## Contract ownership understood

Ali was taught and then assessed on the distinction among:

```text
producer-controlled exact source evidence
→ model semantic proposal
→ schema/structural validation
→ grounding/reference validation
→ semantic evaluation
```

Relevant schema fields were treated as an evidence contract rather than syntax trivia:

- `kind`: proposed change category;
- `subject`: source-supported affected thing;
- `summary`: bounded semantic description;
- `assertion`: affirmed / negated / uncertain;
- `timing`: current / planned / historical / unspecified;
- `effective_version`: source-supported effective version, separate from enclosing release context;
- `source_spans`: producer-controlled evidence IDs cited by the model;
- `reason`: explanation for uncertainty/unspecified cases where required;
- `unassessed`: supplied material the model is not claiming to have interpreted.

The prompt/schema boundary was understood to restrict not only shape but semantic authority: a model output cannot add compatibility, safety, target-impact or maintainer-action fields merely because it can produce valid JSON.

## Ownership checkpoint evidence

Ali correctly diagnosed the prepared deprecation-vs-removal control:

- a proposal that classifies string-valued `verify` usage as a current removal while citing the real deprecation line can pass schema validation;
- the source reference is real, so grounding/reference validation can pass;
- semantic evaluation must fail because the source says deprecation, not removal;
- the deterministic source evidence remains valid and should be preserved; the failed semantic proposal must not be promoted into trusted downstream state.

Ali then correctly diagnosed the inverse failure:

- a semantically correct `app`-removal proposal that cites nonexistent `S9:L99` fails at the grounding/reference layer;
- the fact that its semantic idea happens to be correct does not rescue the result, because UpgradePilot would otherwise admit an ungrounded claim.

This demonstrates the intended distinction:

```text
schema-valid
!= grounded
!= semantically correct
```

and also:

```text
bad interpretation != bad source evidence
correct semantic guess != acceptable ungrounded result
```

## D2 assessment

**D2 — COMPLETE at the intended contract/evidence ownership depth.**

Established learning evidence:

- real HTTPX source-to-proposal trace understood;
- prompt role and schema authority surface understood;
- producer IDs versus model-generated quotation/source authority understood;
- schema, grounding and semantic evaluation separated correctly;
- failed interpretation preserves deterministic source evidence;
- semantically correct but ungrounded output is still inadmissible;
- target impact remains outside this source-only role.

This does not establish D3 evaluation/coverage/failure ownership, D4 broader transfer ownership, interpreter implementation, real-model accuracy, target exposure, usefulness or product adoption.

**Next deferred-D responsibility: D3 — evaluation, coverage, uncertainty and failure model.**
