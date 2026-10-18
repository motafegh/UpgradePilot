# Semantic-comparison Phase D learning preparation

**Branch:** `learning/semantic-comparison-d-prep-2026-10-18`  
**Base main commit:** `243ab0c1cddaa6b074e0708eecef03be1308b789`  
**Base horizon:** reference-interface v2 qualification is complete for all 12 synthetic sequences and semantic admission is permitted; no real semantic assignment had started at this checkpoint.  
**Purpose:** prepare learner-owned understanding for the current Investigator semantic-comparison cycle while main continues B independently.  
**Authority:** this is branch-local learning working memory, not a replacement for root `MEMORY.md`. Root `MEMORY.md` remains the sole live project-position authority. Main B evidence/results remain authoritative for what actually happened.

## 1. Why this branch exists

Use this temporary branch to learn, trace, question, and record durable understanding without interrupting the parallel main-branch B execution. The branch should contain only learning/audit material worth preserving later. Avoid product/experiment implementation changes unless a later learning task explicitly requires a small, promotable proof artifact.

When main B advances, reconcile its new published commits/evidence into the **B intake queue** below. Do not rewrite history or pre-judge unfinished semantic outputs. Once B is complete, append the final result/review material and finish the outcome-dependent D blocks. Before merging this branch to main, reconcile against current main and promote only statements still supported by the final evidence horizon.

## 2. Phase D objective

Phase D is not memorizing file names or repeating AI explanations. The target is learner ownership of the current system and experiment at enough depth to:

1. explain the architecture, responsibilities, and proof boundaries in our own words;
2. trace a concrete request/evidence/reference/result path through the actual code;
3. distinguish deterministic/interface proof from semantic evidence and from product/action authority;
4. explain why the experiment is fair, what it can measure, and what it cannot establish;
5. inspect the eventual semantic results without confusing citation validity, entailment, stopping, usefulness, or model ranking;
6. identify invalid inferences, hidden authority promotion, unequal-information comparisons, and outcome-driven repair;
7. state the final evidence-backed conclusions and remaining uncertainty without relying on the assistant as the source of truth.

### Mastery check for each learning block

A block is not learner-owned merely because it was explained. For each block we should be able to do most of the following:

- **Explain:** restate the mechanism and rationale in our own words.
- **Trace:** point to the actual files/functions/data records that implement or prove it.
- **Boundary:** say exactly what the proof establishes and what it does not.
- **Diagnose:** handle at least one concrete failure/edge case without guessing.
- **Connect:** explain why the mechanism matters to the semantic comparison and/or hybrid architecture.

Record uncertain answers as learning gaps, not mastered conclusions.

## 3. Learning journey path

### D0 — Re-orientation and evidence map

Goal: reconstruct the current cycle from retained evidence rather than narrative memory.

Cover:
- previous deployment/interface qualification versus budget-visible successor versus reference-interface v2;
- why each qualification horizon remains valid only for its exact contract/configuration;
- Gate P, deterministic proof, qualification gate, admission receipt, semantic execution, offline review;
- current B artifacts and which owner answers which question.

Output: one compact chronological/proof map and a list of still-unproven claims.

### D1 — Hybrid architecture and ownership

Goal: own the architecture `Evidence separation -> Interpretation -> Validation -> Decision` and the exact authority boundaries.

Cover:
- Workspace/product evidence and material-validity ownership;
- Investigator as attributed interpretation/proposal, not evidence owner or action authority;
- delivery, observation, typed reference, citation, proposition, validation, and decision as distinct objects;
- why product code does not import the experiment harness and what future productization would actually mean.

Code/evidence anchors:
- Workspace lifecycle/source/native access owners;
- `experiments/investigator_workspace_adapter.py`;
- controlling ADR/Core/plan sections referenced by the active cycle.

### D2 — One complete Investigator data-flow trace

Goal: trace one real-shaped interaction end-to-end.

Follow:
`Workspace evidence -> adapter registration -> AdapterEvent -> whole-event packing -> request-local typed pairs -> dynamic JSON grammar -> rendered stateless request -> model bytes -> strict adapter resolution -> note/report publication -> retained receipts`.

Understand:
- what data is trusted at each hop;
- what is model-authored and therefore untrusted;
- what omission/repacking changes;
- where material validity is rechecked;
- why grammar assistance never becomes citation/evidence authority.

Primary files:
- `experiments/investigator_workspace_adapter.py`
- `experiments/investigator_workspace_trial.py`
- `experiments/investigator_model_interface.py`

### D3 — Reference-interface v2 and failure-driven design

Goal: understand the two predecessor failure classes and why v2 is a bounded interface repair rather than validator weakening or answer tuning.

Cover:
- Gemma12 mangled long reference versus E4B delivery-ID/source-reference authority confusion;
- why causal attribution to budget visibility/generation allowance was not established;
- `(kind,id)` registration and request-local visibility;
- `typed_citation_available` and uncitable problem observations;
- exact pair correlation rather than kind×ID Cartesian products;
- empty-reference catalogs;
- correction/refusal behavior;
- why aliases, fuzzy matching, prefix repair, or minted failure citations were rejected/deferred.

Proof anchors:
- reference-v2 deterministic proof;
- driver/model fixture tests;
- predecessor negative-result analysis.

### D4 — Budget visibility, packing, statelessness, and resource ownership

Goal: understand the control plane around the Investigator rather than treating budget fields as evidence.

Cover:
- trial-driver budget owner versus model-binding budget owner;
- invocation/operation/observation/correction/time versus model-call/token/context allowances;
- finish/report/termination costs;
- stable snapshot during repacking;
- unknown usage versus zero;
- whole-event omission instead of text truncation;
- why explicit stateless requests and fresh assignment state matter;
- what backend prefix caching does *not* mean.

### D5 — Qualification and admission mechanics

Goal: explain exactly what 4/4 qualification means and does not mean.

Cover:
- candidate/deployment/preflight/canary/qualification/semantic-assignment distinctions;
- exact deployment identity: model asset, runtime, template/tokenizer, context, generation reserve, sampling/thinking/load configuration;
- rendered-token/context fit versus requested/applied correspondence versus interface behavior;
- why a request-contract change requires new source-bound qualification;
- why all three selected deployments required reference-v2 qualification;
- known usage/configuration/prompt/instance checks;
- no selective retry, no successful-subset semantic comparison;
- append-only semantic-admission receipt and why frozen manifests are not rewritten after outcomes.

Primary files:
- `experiments/qualify_investigator_model_interface.py`
- `experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md`
- reference-v2 qualification freeze/results/admission evidence.

### D6 — Experimental fairness and semantic runner

Goal: understand the scientific design independently of model outputs.

Cover:
- 2 development cases × 2 treatments × 3 deployments = 12 assignments;
- Raw and Structured share the same underlying evidence universe but expose different access/representation capabilities;
- exact treatment-first balance and why global 3/3 alone was insufficient;
- per-case inverse 1:2 / 2:1 balance and per-deployment inversion;
- fresh Workspace/model instance per semantic assignment;
- serial order, immutable outputs, no failure-selective reruns;
- why the runner gates execution but does not semantically grade its own outputs.

Primary file:
- `experiments/run_investigator_semantic_comparison.py`

### D7 — Semantic review methodology

Goal: become able to review the real outputs rather than accept a mechanically valid report.

Master the separate review dimensions:
- relevant evidence coverage;
- interpretation correctness;
- unsupported/contradicted claims;
- scoped negative evidence;
- unresolved quality;
- stopping quality;
- recommendation usefulness;
- reviewer effort;
- resource cost.

Also cover:
- source obligations and evidence-use traces;
- material propositions and support dispositions;
- citation validity versus entailment;
- observed empty versus scoped negative versus problem/unavailable;
- procedural finish versus adequate stopping;
- recommendation usefulness versus action permission;
- reviewer corrections never modifying original output;
- formative exposed development evidence versus protected/generalization evidence.

Do **not** consume unfinished/unpublished semantic outcomes or hidden reviewer material merely to get ahead of main. Outcome-specific work starts from the final retained B evidence.

### D8 — Final B result intake and comparative interpretation

**Blocked until B publishes the complete semantic batch and review/disposition.**

When available, append the final B artifacts and learn them systematically:
- assignment-by-assignment Raw/Structured behavior;
- within-deployment comparisons first;
- case-specific differences;
- smaller E4B trade-offs versus larger deployments without turning the experiment into a generic model leaderboard;
- failures/incompleteness and their triage costs;
- resource/cost differences;
- which observed gains/losses are actually supported;
- what remains inconclusive from one sample per condition and exposed development cases.

Output: our own evidence-backed explanation of the semantic comparison and its limits.

### D9 — Learner synthesis and promotion

Goal: convert AI-assisted study into learner-owned conclusions.

Required before D closure/promotion:
- answer the important questions below in our own words;
- trace at least one complete code/data path without relying on a prepared summary;
- diagnose representative reference, omission, scoped-negative, stopping, and qualification scenarios;
- explain the final semantic findings and non-findings from retained evidence;
- explicitly name remaining uncertainties/deferred responsibilities.

Only durable, evidence-backed conclusions should be promoted/merged to main. Intermediate misunderstandings remain historical branch material, not current project truth.

## 4. Important questions Phase D must answer

### Architecture and authority

1. What exactly does each layer in `Evidence -> Interpretation -> Validation -> Decision` own, and what is it forbidden to promote on its own?
2. What are the differences between source material, delivery, observation, typed reference, citation, claim/proposition, interpretation, validation, and decision?
3. Why is an Investigator report attributed proposal material rather than evidence or action permission?
4. Where and how is material validity checked, and why can a once-visible reference later still fail admission?
5. Why must experiment code remain outside product-source ownership until a responsibility earns adoption?

### Raw/Structured comparison

6. What is held constant between Raw and Structured, and what is deliberately different?
7. Why would unequal evidence universes make the comparison invalid?
8. What extra native representation can Structured expose, and what authority does that representation *not* gain merely by being structured?
9. Why are within-deployment Raw/Structured comparisons primary before cross-model comparisons?

### Reference-interface v2

10. How is a typed `(kind,id)` reference created from an actual producer and carried into a packed request?
11. Why was the old general-string grammar insufficient even though the strict resolver was correct?
12. Why is a closed request-local grammar assistance rather than evidence authority?
13. What happens when the sole event carrying a reference is omitted by repacking?
14. Why can a delivery ID or native/internal/catalog ID not become a citation just because the model saw it?
15. What does `typed_citation_available=false` mean, and how should an uncitable problem be represented in a report?
16. Why are observed empty, scoped-negative, unavailable/problem, refusal, and unsupported-native outcomes different?
17. Why were fuzzy matching, prefix completion, nearest-ID repair, kind coercion, and automatic alias fallback rejected?
18. How did the v2 fixture suite prove the deterministic boundary without proving semantic correctness?

### Stateless request and budgets

19. What state exists across calls, and what state is deliberately *not* implicit?
20. Why is a prior model-authored request intent rather than evidence?
21. What budget facts are owned by the trial driver versus the model binding?
22. Why is budget metadata control information rather than source evidence?
23. Why are finish/report costs important when evaluating stopping behavior?
24. What does unknown usage do to later prediction admission, and why must it never become zero by default?
25. Why does packing omit whole events rather than silently truncate observation text?

### Qualification, freezes, and gates

26. What is the difference between rendered/context fit, requested/applied runtime correspondence, interface qualification, and semantic correctness?
27. Why did previous 4/4 results remain historically valid yet fail to authorize a changed contract?
28. Why did reference-v2 require a fresh qualification cohort for Qwen27 even though Qwen27 had passed the predecessor contract?
29. What exactly does `4/4 qualified` establish for a deployment?
30. Why must all selected points qualify before this frozen semantic comparison rather than running only the successful subset?
31. What is Gate P, and why must it happen before prediction?
32. Why is the semantic admission receipt append-only rather than inserted into/replacing the pre-run freeze?
33. What failure classes stop one sequence versus the whole cohort?
34. Why are retries/repairs versioned rather than silently rerunning until green?

### Fairness and execution

35. Why are there exactly 12 semantic assignments?
36. What problem does the per-case inverse 1:2/2:1 treatment-first rule solve that global 3/3 did not?
37. Why do fresh Workspace and model instances matter for assignment isolation?
38. Why are assignments serial, immutable, and non-rerun by default?
39. What does the semantic runner enforce, and what intentionally remains outside the runner?

### Semantic review and scientific interpretation

40. Why can a perfectly valid citation still fail semantic support/entailment?
41. How do we decide whether a negative claim is properly scoped?
42. What is the difference between procedural finish and justified stopping?
43. How do remaining feasible discriminators and visible remaining budget affect stopping review?
44. What makes a recommendation useful without granting action permission?
45. How are source obligations, evidence-use traces, propositions, and support dispositions related?
46. Why must summary/recommendation surfaces be reviewed, not only a formal `claims` array?
47. How should reviewer effort and failed-run triage cost enter the comparison?
48. What can one sample per case/treatment/deployment establish, and what cannot it establish about reliability, generalization, or intrinsic model ranking?
49. Why are HTTPX/glyphsLib formative development cases rather than production/generalization proof?
50. Given the final B results, what evidence would justify retain, reject, or inconclusive for the Structured Investigator direction?

### Code ownership

51. Which responsibilities live in `investigator_workspace_adapter.py`, `investigator_workspace_trial.py`, `investigator_model_interface.py`, `qualify_investigator_model_interface.py`, and `run_investigator_semantic_comparison.py`?
52. For one report citation, can we trace the exact functions/records from producer registration through packing, grammar, generated bytes, resolution, and publication?
53. For one semantic assignment, can we trace the exact freeze/profile/case/treatment/budget/retention records that make it comparable to its pair?

## 5. Minimal roadmap / TODO

- [ ] **D0:** reconcile latest main B horizon and build one proof/timeline map.
- [ ] **D1:** architecture/authority terminology and ownership.
- [ ] **D2:** trace one complete reference/request/publication path in code.
- [ ] **D3:** predecessor failures -> reference-v2 design -> deterministic fixtures/proof.
- [ ] **D4:** budgets, whole-event packing, statelessness, and resource accounting.
- [ ] **D5:** qualification, exact deployment identity, freezes, and admission receipt.
- [ ] **D6:** Raw/Structured fairness, schedule logic, semantic runner, isolation/no-rerun rules.
- [ ] **D7:** semantic-review methodology and proof boundaries.
- [ ] **B intake:** periodically append newly published main B evidence without interpreting incomplete outcomes as final.
- [ ] **D8:** after complete B publication, inspect actual semantic assignments/reviews/costs and produce our comparative interpretation.
- [ ] **D9:** learner-owned synthesis, scenario checks, remaining gaps, and durable conclusions for merge/promotion.

The roadmap is intentionally short. New B mechanisms/results should be appended to the relevant block rather than spawning redundant learning phases unless they introduce a genuinely new responsibility.

## 6. B intake queue

Starting horizon at branch creation:

- reference-interface v2 deterministic proof: complete;
- reference-v2 pre-inference freeze: complete;
- reference-v2 qualification cohort: **12/12 qualified, 60 charged calls**;
- semantic admission: permitted / append-only admission receipt is the next main-side boundary;
- real semantic assignments: **0 attempted at the branch-base checkpoint**;
- D/E on main: pending.

For every later main sync, append:
- main commit/horizon;
- new B artifact(s);
- whether they change architecture, experiment protocol, proof boundary, or only add outcome evidence;
- which D block/questions need amendment;
- no learner conclusion until we inspect the retained evidence.

## 7. Branch discipline and eventual merge

- Do not edit root `MEMORY.md` from this learning branch to claim live main progress.
- Do not overwrite main B evidence or experimental outputs.
- Prefer durable learning records over scratch notes so the branch can later be merged cleanly.
- If main changes code we are studying, reconcile before making code-specific learner claims.
- Final merge should occur only after rebasing/merging the completed B horizon and resolving any stale statements.
- Promote learner-owned conclusions only after demonstrated understanding; AI-authored explanations alone are preparation evidence, not mastery.
