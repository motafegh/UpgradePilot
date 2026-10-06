# Deferred Phase D — post-design evidence integration for D3/D4

**Date:** 2026-10-06  
**Branch:** `learning/deferred-api-interpretation-phase-d-2026-10-05`  
**Status:** Supporting learning adaptation only; D3/D4 remain pending.  
**Historical owner:** `working-memory/2026-10-05_1617_api-change-interpretation-preparation_lbd-cycle.md` remains the deferred-D cycle-status owner until D5 reconciliation.  
**Mutation boundary:** learning documentation only. No product/experiment source, active implementation-cycle state, `MEMORY.md`, specification, ADR, semantic-role acceptance, or product authority change.

## Why this addendum exists

After D1 and D2 were completed on the learning branch, `main` advanced through the implementation, real-model evaluation, output-budget diagnosis, contract repair, and Gemma-vs-MiMo comparison responsibilities for the same source-only API interpretation problem.

The learning branch was synchronized with `main` at `49fe959f3a263576d6f1baf047233bf90cbca2da` while preserving the four branch-local learning/research artifacts. These newer results are **post-design evidence**. They may strengthen and concretize the remaining deferred Phase D, but they must not be rewritten as evidence that existed when the original preparation design was frozen.

Use this distinction:

```text
original preparation design
→ what responsibilities/failure classes were intended

later implementation/model evidence
→ which of those boundaries became observable in real execution
```

## D3 integration — evaluation, coverage, uncertainty, and failure classes

D3 should keep the original prepared concepts, but teach them with these actual later results where useful:

1. **Capacity/input fit versus completion-budget failure**
   - Initial Gemma pass measured the exact rendered requests and established that all 18 nonempty inputs fit the loaded 4,096-token context under the conservative accounting.
   - Full HTTPX and partial HTTPX nevertheless hit the fixed 1,536-token completion ceiling.
   - Therefore `input fits context` and `output budget is adequate` are separate propositions.

2. **Budget failure versus semantic failure**
   - Reloading the same Gemma deployment at 16,384 context and using an 8,192-token completion reserve removed truncation on all 18 requests.
   - The previously completed replies were byte-identical and the critical semantic cleanup/removal error persisted.
   - Therefore fixing capacity/truncation cannot be credited as fixing meaning.

3. **Contract/schema, grounding, and semantic failure remain distinct in real runs**
   - v1 produced conditional contract failures such as null subjects without required explanations and a bad line-reference case.
   - Other outputs passed structure/reference admission yet remained semantically wrong.
   - No partial semantic proposal was salvaged from rejected/truncated outputs.

4. **Source coverage versus interpretation coverage**
   - Full-window and partial-window cases preserved different acquisition scope.
   - Even after capacity repair, model outputs omitted or collapsed required propositions.
   - Later MiMo results particularly demonstrate that a response can stop cleanly with spare budget and still omit important supplied changes.
   - Therefore acquisition/source completeness and model semantic completeness remain independently owned.

5. **`unassessed` / abstention quality versus empty-safe output**
   - Real runs show both useful preservation of ambiguity and problematic omission/blanket limitation behavior.
   - D3 should distinguish justified `unassessed` material from evasion that avoids false positives while failing coverage obligations.

6. **Frozen evaluator separation in practice**
   - v1 expectations remained separate from model inputs.
   - v2 kept the original 19 inputs/expectations byte-identical and froze a new Requests case/expectation before either v2 model output.
   - This supplies concrete evidence for why expected/forbidden propositions and omission checks must stay outside producer/model inputs.

7. **Development evidence versus admission**
   - Gemma v1, Gemma v2, and MiMo v2 all produced useful individual cases, but every semantic disposition remained `FAILED / REVISE`.
   - Neither model comparison nor isolated wins establish protected independent semantic accuracy, a second ordinary target-PR case, target applicability, maintainer usefulness, or product admission.

## D4 integration — changed-case ownership using actual failures

D4 should now prefer these real post-design cases over purely hypothetical variants when testing transfer:

- **Correct citation + wrong meaning:** Gemma's ambiguous cleanup passage became an affirmed current removal even with valid evidence linkage.
- **Correct/available meaning + typed-representation loss:** MiMo mentioned future removal inside a current-deprecation record instead of preserving the separate planned-removal proposition.
- **Clean provider completion + semantic omission:** MiMo's partial-window output omitted the required `app`/`proxies` removals and most other changes despite no truncation/contract/grounding failure.
- **Capacity repair that does not repair semantics:** compare Gemma v1 truncated full window with the extended-budget run; removal of truncation did not fix the separate semantic defects.
- **Mechanical contract improvement without semantic admission:** Gemma v2 improved decoder admission and subject population but still failed the semantic role.
- **Model comparison without winner authority:** MiMo repairs some Gemma failures and introduces different omissions/encoding problems; neither earns role or product authority merely by outperforming the other on selected cases.
- **Policy ambiguity:** Requests ongoing-deprecation timing exposes a genuine evaluator/design-policy question. A disputed criterion must not be silently rewritten after output or used alone to manufacture a unique model error.

These cases directly support the D4 shortcut critiques:

```text
more tokens != better semantics
valid explanation != correct category
valid citation != correct meaning
clean stop != complete coverage
better model on one case != admitted role
more structured fields != evidence of target impact
```

## What should NOT be folded into the deferred preparation D

Keep the following owned by the later implementation/repair cycles rather than pretending the historical preparation D originally included them:

- exact implementation syntax/module structure;
- LM Studio SDK/native loading mechanics;
- exact request/token-count APIs;
- model-specific latency or token totals as facts to memorize;
- v2 prompt/schema implementation details beyond the conceptual lessons they expose;
- current runtime loaded/unloaded state;
- engineering regression counts as proof of learner mastery;
- semantic admission or product promotion, which remain explicitly unestablished.

## Revised remaining learning route

The original deferred-D sequence remains valid, with stronger teaching evidence:

```text
D1 architecture/responsibility ownership    COMPLETE
D2 contract/real source trace               COMPLETE
D3 evaluation/coverage/failure ownership    NEXT — use original design + real v1/v2 evidence
D4 changed-case engineering reasoning       PENDING — prefer real observed failures/comparisons
D5 gap repair/final reconciliation          PENDING
```

D5 must still reconcile learning completion separately from engineering proof. Understanding why the real models failed does not establish that the interpreter is semantically accepted, that either model is suitable as a product default, or that target exposure/compatibility/action is proved.
