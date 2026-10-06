# Deferred Phase D — active learning tracker with post-design evidence

**Date:** 2026-10-06  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Status:** ACTIVE deferred-D operational learning tracker.  
**Historical cycle owner:** `working-memory/2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md` remains the historical preparation-cycle/status record and will receive final reconciliation at D5.  
**Current tracking rule:** use this file as the live D1–D5 checklist from this point forward; check items only after demonstrated ownership, not after presentation/agreement.  
**Mutation boundary:** learning documentation only. No product/experiment source, active implementation-cycle state, `MEMORY.md`, specification, ADR, semantic-role acceptance, or product authority change.

## Why this tracker exists

After D1 and D2 were completed on the learning branch, `main` advanced through the implementation, real-model evaluation, output-budget diagnosis, contract repair, and Gemma-vs-MiMo comparison responsibilities for the same source-only API interpretation problem.

The learning branch was synchronized with `main` at `49fe959f3a263576d6f1baf047233bf90cbca2da` while preserving the branch-local learning/research artifacts. These newer results are **post-design evidence**. They strengthen and concretize the remaining deferred Phase D, but they must not be rewritten as evidence that existed when the original preparation design was frozen.

Use this distinction:

```text
original preparation design
→ what responsibilities/failure classes were intended

later implementation/model evidence
→ which of those boundaries became observable in real execution
```

## Current Phase-D progress

```text
D1 architecture/responsibility ownership    COMPLETE
D2 contract/real source trace               COMPLETE
D3 evaluation/coverage/failure ownership    NEXT
D4 changed-case engineering reasoning       PENDING
D5 gap repair/final reconciliation          PENDING
```

Supporting ownership evidence:

- D1: `working-memory/2026-10-05_deferred-D_D1_agenticity-authority-supporting-note.md`
- D2: `working-memory/2026-10-06_deferred-D_D2_contract-evidence-trace.md`

## D1 — whole architecture and responsibility map — COMPLETE

- [x] Trace acquired upstream release evidence → source-only interpretation proposal → deterministic validation/evaluation → later target-exposure composition.
- [x] Explain why the broader role is experiment-local at this stage instead of silently broadening admitted product semantics.
- [x] Distinguish reusable support-drop infrastructure from non-reusable semantic authority.
- [x] Identify producer/model/evaluator/downstream ownership boundaries and the stronger claims each must not make.
- [x] Transfer the reasoning to a changed Starlette/HTTPX target-exposure case with a missing resolved-version premise.
- [x] Distinguish AI/agent capability from evidentiary authority.

**D1 checkpoint:** passed at intended architecture/responsibility depth.

## D2 — actual interpretation contract and real evidence trace — COMPLETE

- [x] Read the real v1 prompt/schema as an engineering contract rather than syntax trivia.
- [x] Trace authentic HTTPX source evidence and producer IDs into a proposed observation.
- [x] Understand `kind`, `subject`, `assertion`, `timing`, `effective_version`, `source_spans`, `reason`, and `unassessed` at the evidence-model level.
- [x] Demonstrate `schema-valid ≠ grounded ≠ semantically correct` with the real deprecation/removal control.
- [x] Explain why producer-owned IDs/reconstruction are stronger than model-authored authoritative quotes/source identity.
- [x] Diagnose the inverse case: semantically correct idea + nonexistent citation → grounding failure; correct meaning does not rescue an ungrounded result.
- [x] Preserve deterministic source evidence when the model interpretation fails instead of conflating source failure with semantic failure.

**D2 checkpoint:** passed at intended contract/evidence depth.

## D3 — evaluation, coverage, uncertainty and failure model — NEXT

### Original design responsibilities

- [ ] Explain why expected/forbidden propositions and omission checks are frozen outside producer/model inputs.
- [ ] Distinguish known-development/calibration review from protected/independent semantic admission and maintainer usefulness.
- [ ] Separate acquisition/source coverage from interpretation/semantic coverage.
- [ ] Explain the purpose and limit of `unassessed`: justified abstention is not a no-change/no-impact claim and is not automatically complete coverage.
- [ ] Trace incomplete/ambiguous source cases without promoting partial evidence into complete-window truth.
- [ ] Classify provider, capacity/token-fit, completion-budget/truncation, contract/schema, grounding/reference, semantic, and omission/coverage failures.
- [ ] State what evidence remains valid and what proof becomes unavailable for each failure class.
- [ ] Explain why all-unknown/all-unassessed output cannot pass merely because it avoids false positives.

### Actual post-design evidence that D3 must cover

- [ ] **Input-context fit vs output-budget adequacy:** understand why Gemma v1 could fit all measured inputs while full/partial HTTPX still hit the 1,536-token completion ceiling.
- [ ] **Capacity failure vs semantic failure:** understand why moving Gemma to 16,384 context / 8,192 completion removed truncation but did not repair the critical wrong-meaning cases.
- [ ] **Contract vs grounding vs semantics in real execution:** classify null-subject/missing-reason failures, invalid line references, and structurally/groundedly admitted but semantically wrong proposals separately.
- [ ] **Clean stop vs semantic coverage:** explain why MiMo can finish normally with no truncation/contract/grounding problem and still omit required supplied changes.
- [ ] **Source completeness vs interpretation completeness:** compare complete-window and partial-window evidence without treating model omission as acquisition absence.
- [ ] **Abstention quality:** distinguish useful preservation of ambiguity from blanket/unhelpful `unassessed` output that evades coverage obligations.
- [ ] **Evaluator separation in practice:** understand that original v1 expectations stayed outside model input, and the new Requests case/expectations were frozen before v2 model outputs.
- [ ] **Development wins do not equal admission:** explain why Gemma v1, Gemma v2, and MiMo v2 all had useful individual outcomes yet all remained `FAILED / REVISE` and did not establish protected accuracy/product authority.

**D3 ownership checkpoint:** Ali can classify changed real failure scenarios, identify the owning layer, and state exactly which evidence/proof remains valid versus invalid without conflating mechanical success, semantic correctness, or coverage.

## D4 — engineering ownership through changed-case reasoning — PENDING

### Original transfer targets

- [ ] Reason through a correctly cited deprecation misclassified as removal.
- [ ] Reason through an incomplete source window containing one useful exact section.
- [ ] Reason through a semantically plausible result when exact runtime/capacity proof is unavailable or completion truncates.
- [ ] Identify which component may and may not claim that the target repository is actually exposed to an interpreted upstream change.
- [ ] Critique tempting shortcuts such as model-owned `complete=true`, answer-selected excerpts, silent retry/truncation rescue, or treating the support-drop semantic role as generic API authority.

### Prefer these real observed transfer cases

- [ ] **Correct citation + wrong meaning:** Gemma's ambiguous cleanup passage becomes an affirmed current removal despite valid evidence linkage.
- [ ] **Meaning present in prose + typed representation loss:** MiMo mentions future removal inside a current-deprecation record but fails to preserve the separate planned-removal proposition.
- [ ] **Clean provider completion + semantic omission:** MiMo partial-window output omits required `app`/`proxies` removals and most other changes despite no truncation/contract/grounding failure.
- [ ] **Capacity repair does not repair semantics:** compare the truncated Gemma v1 full-window result with the extended-budget run and separate what the intervention did and did not establish.
- [ ] **Mechanical contract improvement without semantic admission:** Gemma v2 improves decoder admission/subject population while the semantic role remains failed.
- [ ] **Model comparison without winner authority:** MiMo repairs some Gemma failures but introduces different omissions/encodings; explain why relative improvement does not automatically earn role/product authority.
- [ ] **Evaluator/design-policy ambiguity:** reason about the Requests ongoing-deprecation timing dispute without silently rewriting expectations after outputs or manufacturing a unique model error from a genuinely ambiguous policy question.

Shortcut principles D4 must be able to defend:

```text
more tokens != better semantics
valid explanation != correct category
valid citation != correct meaning
clean stop != complete coverage
better model on one case != admitted role
more structured fields != evidence of target impact
```

**D4 ownership checkpoint:** Ali transfers the architecture/evidence logic to changed real cases rather than repeating prepared HTTPX facts.

## D5 — gap repair and deferred-D completion assessment — PENDING

- [ ] Classify every material D1–D4 topic as `understood`, `partially understood`, `important gap to repair`, or `safe to defer`.
- [ ] Repair important gaps at the minimum useful depth and preserve non-central deferrals explicitly.
- [ ] Record concise evidence of D1–D4 ownership without turning working memory into a transcript.
- [ ] Reconcile the historical preparation-cycle learning statement only if the ownership evidence supports whole-design understanding.
- [ ] Reconcile this active tracker back into `working-memory/2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md` as the final historical learning result.
- [ ] Fetch/reconcile the then-current `main` before final merge-back so later engineering state is preserved.
- [ ] Keep preparation-design ownership learned here separate from later implementation behavior/proof.
- [ ] Keep learning completion separate from engineering proof: it does not establish interpreter semantic acceptance, either model as product default, target exposure, compatibility, usefulness, or maintainer action authority.

## What should NOT become required memorization in this deferred D

Keep these owned by later implementation/repair cycles unless needed to explain a conceptual boundary:

- exact implementation syntax/module structure;
- LM Studio SDK/native loading mechanics;
- exact request/token-count API calls;
- model-specific latency/token totals as facts to memorize;
- v2 prompt/schema implementation details beyond the conceptual lessons they expose;
- current runtime loaded/unloaded state;
- regression counts as learner-mastery evidence;
- semantic admission or product promotion, which remain explicitly unestablished.

## Working progress record

| Area | State | Evidence of ownership | Remaining gap |
| --- | --- | --- | --- |
| D1 architecture/responsibilities | COMPLETE | D1 supporting note + changed Starlette/HTTPX transfer reasoning | none at intended depth |
| D2 contract/real trace | COMPLETE | D2 supporting note + semantic-vs-grounding inverse cases | none at intended depth |
| D3 evaluation/coverage/failures | NEXT | not yet assessed after post-design sync | original concepts + real v1/v2/Gemma/MiMo failure classification |
| D4 changed-case engineering reasoning | PENDING | not yet assessed | transfer across real observed model/coverage/policy cases |
| D5 gap repair/completion | PENDING | waits on D3/D4 | final classification, historical reconciliation, merge-back |

Update this table and the checkboxes only at meaningful learning checkpoints. Presentation, agreement, implementation success, test counts, or model-output fluency alone do not establish ownership.
