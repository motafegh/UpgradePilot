# Semantic-comparison Phase D learning preparation

**Branch:** `learning/semantic-comparison-d-prep-2026-10-18`  
**Base main commit:** `243ab0c1cddaa6b074e0708eecef03be1308b789`  
**Base horizon:** reference-interface v2 qualification is complete for all 12 synthetic sequences and semantic admission is permitted; no real semantic assignment had started at this checkpoint.  
**Purpose:** prepare learner-owned understanding for the current Investigator semantic-comparison cycle while main continues B independently.  
**Authority:** branch-local learning working memory only. Root `MEMORY.md` remains the sole live project-position authority. Main B evidence/results remain authoritative for what actually happened.

## 1. Learning posture

Use this temporary branch to learn, trace, question, and record durable understanding without interrupting the parallel main-branch B execution. Keep learning decision-relevant and bounded by the companion guardrails in `working-memory/2026-10-18_semantic-comparison-phase-D-learning-guardrails.md`.

The default learning method is now **real-run first**:

`actual retained run/artifact -> inspect observable behavior -> derive the concept -> trace only the code needed to explain it -> learner checkpoint`

Prefer real published requests, visible model outputs, tool observations, evidence deliveries, citations, refusals, reports, receipts, costs and reviewer dispositions over invented examples whenever the real artifact exists.

Important boundary:
- observable retained model behavior is in scope;
- hidden chain-of-thought is not required and is intentionally not a learning target;
- published partial B results may be used to understand mechanisms and failure modes;
- partial results must **not** be promoted into the final Raw-vs-Structured scientific disposition before the frozen batch/review is complete.

When main B advances, add the new published horizon to the **B intake queue**. Do not rewrite history or pre-judge unfinished outcomes. Before eventual merge, reconcile this branch against completed main and retain only conclusions still supported by the final evidence horizon.

## 2. Phase D objective

Phase D targets enough learner ownership to:

1. explain the architecture, responsibilities and proof boundaries in our own words;
2. trace a real request/evidence/reference/result path through actual code and retained artifacts;
3. distinguish deterministic/interface proof, semantic validation and final decision authority;
4. explain the experiment's fairness, what it measures and what it cannot establish;
5. inspect real semantic outputs without confusing citation validity, entailment, stopping, usefulness or model ranking;
6. identify invalid inference, hidden authority promotion, unequal-information comparison and outcome-driven repair;
7. state the final evidence-backed conclusions and remaining uncertainty without treating the assistant as source of truth.

### Mastery check for each block

A block is sufficiently learner-owned when we can do most of the following:

- **Explain** the core mechanism/rationale in our own words.
- **Trace** one real representative run/data/code path.
- **Boundary** what is proven and what is not.
- **Diagnose** one real or representative failure/edge case.
- **Connect** the mechanism to the semantic comparison or next project decision.

Do not keep digging merely because more implementation detail exists.

## 3. Canonical real learning examples

These are preferred anchors, not exclusive cases.

### Canonical example A — first real Gemma12 HTTPX pair

Published on main after this branch's base horizon:
- `53a865a0...` — first real semantic boundary result/source review;
- `988dd812...` — first within-deployment pair review.

Use this pair repeatedly across D1-D7 because it exposes two different failure modes:

**Gemma12 HTTPX Raw**
- ends `limit_exhausted`;
- no report or notes;
- repeated malformed/redundant source-path reads consume the affordable completion reserve;
- correct source material existed;
- this is navigation/budget/stopping failure, not source exhaustion or successful semantic restraint.

**Gemma12 HTTPX Structured**
- completes and publishes a report;
- correctly supports the declaration transition `httpx 0.27.2 -> 0.28.1`;
- nevertheless overclaims basic usage / low breaking-risk without adequate support;
- review decomposes all report surfaces into atomic propositions, including supported, unsupported, narrower-scope-only and contradicted items;
- both Raw and Structured make zero native producer calls in this pair, so completion difference alone does not establish a native-treatment advantage.

This pair is ideal for learning the distinction between:
`mechanically valid output != semantically supported output != decision authorization`.

### Canonical example B — predecessor reference-interface failures

Use the earlier Gemma12 mangled-reference and E4B delivery-ID/source-reference failures to understand why reference-v2 exists and why repair must preserve strict authority rather than weaken validation.

### Canonical example C — reference-v2 qualification cohort

Use the actual 12/12, 60-call reference-v2 cohort to understand exact deployment identity, changed-contract requalification, usage/config/prompt/instance correspondence and admission gating.

As new B pairs are published, add them only when they demonstrate a genuinely new mechanism or help test whether our understanding generalizes. Do not read every run merely because it exists.

## 4. Learning journey path

### D0 — Re-orientation and proof map — **COMPLETE**

Goal: distinguish the proof horizons rather than treating all tests as one validation stage.

Learner-owned closure:
- older qualification remains evidence only for its exact old contract/configuration;
- deterministic reference-v2 proof establishes machinery/invariants, not model semantic correctness;
- 12/12 reference-v2 qualification establishes that the three exact deployments can operate through that exact interface point, not that their real conclusions are correct;
- final Raw-vs-Structured conclusions require real semantic assignments plus offline source-to-claim review/comparison.

Closure record: `working-memory/2026-10-18_semantic-comparison-D0-learning-closure.md`.

### D1 — Hybrid architecture and authority — **ACTIVE**

Goal: own `Evidence separation -> Interpretation -> Validation -> Decision` through the first real Gemma12 HTTPX pair.

Real-run-first route:
1. inspect what actual source evidence was retained/delivered;
2. inspect what the Structured model actually claimed/recommended;
3. compare the valid declaration citations with the unsupported basic-usage/low-risk propositions;
4. inspect why the reviewer can reject semantic support without altering the original model report;
5. use the Raw no-report outcome to distinguish absence of claims from successful/truthful investigation.

Must understand:
- Workspace/product evidence and material-validity ownership;
- Investigator as attributed interpretation/proposal, not evidence owner/action authority;
- source material, delivery, observation, typed reference, citation, proposition, validation and decision as distinct objects;
- mechanical/interface validation versus semantic validation;
- why product code does not import the experiment harness and what later productization would mean.

Primary anchors:
- first Gemma12 HTTPX Raw/Structured reviews on main;
- `experiments/investigator_workspace_adapter.py`;
- relevant Workspace lifecycle/source/native owners only as needed.

Stop line: once we can explain why a valid requirements citation supports the version transition but not the low-risk recommendation, and why no-report Raw is not semantic success, move on.

### D2 — One complete **real** Investigator data-flow/code trace

Goal: follow one retained interaction from the Gemma12 HTTPX Structured run end-to-end.

Trace:
`frozen assignment -> visible source/tool request -> Workspace delivery -> adapter reference registration -> AdapterEvent -> whole-event packing -> request-local typed pairs -> dynamic JSON grammar -> rendered stateless request -> visible model bytes -> strict reference resolution -> finish/report publication -> retained proposal/citations/receipts -> offline proposition review`.

Understand at each hop:
- what is trusted;
- what is model-authored/untrusted;
- what omission/repacking changes;
- where material validity is rechecked;
- where grammar assists generation but does not become evidence authority;
- where semantic validation begins outside the mechanical publishing path.

Primary files:
- `experiments/investigator_workspace_adapter.py`
- `experiments/investigator_workspace_trial.py`
- `experiments/investigator_model_interface.py`

Stop line: one representative complete trace is enough; do not read every function/event.

### D3 — Reference-interface v2 and failure-driven design

Goal: derive v2 from the actual predecessor failures rather than from abstract schema theory.

Use:
- Gemma12 mangled exact source reference;
- E4B delivery-ID/source-reference authority confusion;
- corresponding deterministic v2 fixtures;
- successful reference-v2 qualification behavior.

Cover:
- `(kind,id)` registration and request-local visibility;
- closed exact-pair grammar rather than arbitrary ID or kind×ID Cartesian product;
- `typed_citation_available` and uncitable problem observations;
- omission/repacking authority loss;
- correction/refusal behavior;
- why aliases/fuzzy repair/kind coercion/failure-reference invention were rejected or deferred;
- why we cannot claim budget visibility or output allowance caused the predecessor failures.

Stop line: understand the two actual failure classes, the bounded repair responsibility and why strict resolver authority remains unchanged.

### D4 — Budgets, packing, statelessness and resource ownership

Goal: understand the control plane through actual runs.

Use the Raw HTTPX failure as the primary budget/stopping example:
- observe operation units before late calls;
- see that finish/report remained affordable earlier;
- see repeated reads consume capacity until another read is refused;
- distinguish external budget cutoff from justified stopping/source exhaustion.

Also cover:
- trial-driver budget owner versus model-binding budget owner;
- invocation/operation/observation/correction/time versus model-call/token/context allowance;
- finish/report/termination cost;
- stable snapshots during repacking;
- unknown usage versus zero;
- whole-event omission versus text truncation;
- explicit stateless requests/fresh assignment state;
- backend prefix caching does not grant hidden conversational authority.

Stop line: explain the Raw failure from actual budget/operation observations without speculating about hidden reasoning.

### D5 — Qualification, freezes and semantic admission

Goal: explain what the real 12/12 qualification means and why it was required.

Use the reference-v2 cohort and admission evidence, not hypothetical deployment examples.

Cover:
- candidate/deployment/preflight/qualification/semantic-assignment distinctions;
- exact deployment identity: asset, runtime, template/tokenizer, context, generation reserve, sampling/thinking/load configuration;
- context/rendered fit versus requested/applied correspondence versus interface behavior;
- changed model-facing contract -> fresh qualification requirement;
- why Qwen27 also required fresh qualification despite predecessor success;
- known usage/config/prompt/instance checks;
- no selective retry/successful-subset semantic run;
- append-only semantic-admission receipt and immutable pre-run freezes.

Primary anchors:
- `experiments/qualify_investigator_model_interface.py`
- `experiments/INVESTIGATOR_MODEL_INTERFACE_QUALIFICATION.md`
- reference-v2 freeze/results/admission artifacts.

### D6 — Experimental fairness and semantic runner

Goal: understand the actual frozen scientific design independently of whether individual models succeed.

Cover with the real schedule/freeze:
- `2 cases × 2 treatments × 3 deployments = 12 assignments`;
- same evidence universe, different Raw/Structured capabilities;
- global 3/3 alone was insufficient;
- per-case inverse `1:2 / 2:1` treatment-first balance and per-deployment inversion;
- fresh Workspace/model assignment state;
- serial immutable execution and no failure-selective rerun;
- why Raw failure does not authorize rerunning it or changing Structured;
- runner enforces execution/protocol boundaries but does not semantically grade outputs.

Primary file: `experiments/run_investigator_semantic_comparison.py`.

### D7 — Semantic review methodology through real reports

Goal: learn to review an actual mechanically valid report.

Primary anchor: Gemma12 HTTPX Structured review.

Walk through a small decisive subset of actual propositions:
- supported version-transition propositions;
- unsupported `basic requests` proposition;
- unsupported `low breaking risk` proposition;
- narrower-scope `no specific usage identified` / `no breaking changes identified` statements;
- contradicted unavailable-changelog proposition.

Master dimensions:
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
- source obligations/evidence-use traces;
- citation validity versus entailment;
- observed empty versus scoped negative versus problem/unavailable;
- procedural finish versus adequate stopping;
- recommendation usefulness versus action permission;
- original model output remains immutable while reviewer disposition is separate.

Published partial pair reviews may be used here to learn the method. Do not use them to declare the final treatment winner.

### D8 — Final B result intake and comparative interpretation

**Final disposition remains blocked until B publishes the complete semantic batch and review.**

When available:
- inspect assignment-by-assignment Raw/Structured outcomes;
- compare within deployment first;
- inspect case-specific differences;
- evaluate E4B trade-offs without turning this into a generic model leaderboard;
- include failed/incomplete runs and triage effort, not only successful reports;
- compare resource/cost behavior;
- distinguish actual supported gains/losses from one-sample noise;
- state what remains inconclusive from exposed development cases.

Output: our own evidence-backed explanation of the semantic comparison and its limits.

### D9 — Learner synthesis and promotion

Goal: convert AI-assisted study into learner-owned conclusions.

Required before closure/promotion:
- answer the important questions below in our own words;
- trace one complete real code/data path without a prepared summary;
- diagnose representative reference, omission, scoped-negative, stopping and qualification scenarios;
- explain final semantic findings/non-findings from retained evidence;
- explicitly name remaining uncertainty/deferred responsibilities.

Only durable evidence-backed conclusions should be promoted to main.

## 5. Important questions Phase D must answer

These are grouped checkpoints, **not 53 separate lessons**.

### Architecture and authority
1. What does each layer in `Evidence -> Interpretation -> Validation -> Decision` own, and what can it not promote itself?
2. What are source material, delivery, observation, typed reference, citation, proposition, interpretation, validation and decision?
3. Why is an Investigator report attributed proposal material rather than evidence/action permission?
4. Where is material validity checked, and why can previously visible evidence still become stale?
5. In the real Gemma12 Structured report, why do valid requirements citations support the version transition but not `basic requests` or `low risk`?
6. Why is Raw's absence of a report not evidence that it avoided unsupported claims successfully?

### Raw/Structured comparison
7. What is held constant and what differs between Raw and Structured?
8. Why would unequal evidence universes invalidate treatment comparison?
9. What native representation may Structured expose, and what authority does it not gain merely by being structured?
10. Why are within-deployment treatment comparisons primary?
11. Why does the first pair's completion difference not establish native-treatment advantage when neither side used native producers?

### Reference-interface v2
12. How does a real typed `(kind,id)` reference travel from producer registration to a packed model request?
13. Why was arbitrary-string reference generation insufficient despite a correct strict resolver?
14. Why is closed request-local grammar generation assistance rather than evidence authority?
15. What happens when repacking omits the event carrying a reference?
16. Why can delivery/native/catalog IDs not become citations merely because the model saw them?
17. What does `typed_citation_available=false` mean for a real problem observation?
18. Why are empty, scoped-negative, unavailable/problem, refusal and unsupported-native distinct?
19. Why were fuzzy matching, prefix completion, nearest-ID repair, kind coercion and automatic aliases rejected?
20. What did deterministic v2 fixtures prove that model qualification still had to test separately?

### Stateless requests and budgets
21. What state exists across calls, and what state is deliberately not implicit?
22. Why is prior model-authored request text intent rather than independent evidence?
23. Which budget facts belong to the trial driver versus model binding?
24. Why is budget metadata control information, not evidence?
25. Using Gemma12 HTTPX Raw, how did feasible completion capacity become consumed by repeated source reads?
26. Why is the final operation refusal not justified stopping/source exhaustion?
27. What does unknown usage do to later admission, and why is it not zero?
28. Why are whole events omitted instead of silently truncating evidence text?

### Qualification, freezes and gates
29. What differs among rendered/context fit, requested/applied correspondence, interface qualification and semantic correctness?
30. Why do old qualifications stay historically valid but not authorize a changed contract?
31. Why did all three selected deployments, including prior-successful Qwen27, require reference-v2 qualification?
32. What exactly does the real `12/12 qualified` result establish?
33. Why must all selected points qualify before this frozen semantic comparison?
34. What is Gate P and why must it precede prediction?
35. Why is semantic admission append-only rather than rewriting the freeze?
36. Why are repair/rerun/version changes explicit rather than tuning-until-green?

### Fairness and execution
37. Why are there exactly 12 semantic assignments?
38. What does per-case inverse `1:2 / 2:1` solve beyond global 3/3?
39. Why do fresh Workspace/model states matter?
40. Why are assignments serial, immutable and non-rerun by default?
41. What does the runner enforce, and what intentionally remains outside it?

### Semantic review and scientific interpretation
42. Why can a valid citation fail entailment in an actual report?
43. How do we scope a negative/non-identification claim correctly?
44. What is procedural finish versus justified stopping?
45. How should remaining feasible discriminators and budget affect stopping review?
46. What makes a recommendation useful without granting action permission?
47. Why review summary/recommendation/stopping/missing-observation surfaces, not only `claims`?
48. How should reviewer effort and failed-run triage cost enter treatment comparison?
49. What can one sample per condition establish, and what can it not establish about reliability/generalization/model ranking?
50. Why are HTTPX/glyphsLib development evidence rather than production-generalization proof?
51. Given the final B results, what supports retain, reject or inconclusive for Structured Investigator responsibilities?

### Code ownership
52. Which responsibilities belong to adapter, trial driver, model interface, qualification runner and semantic runner?
53. Can we trace one real report citation from source producer to registration, packing, grammar, model output, strict resolution, publication and semantic review?
54. Can we trace one real semantic assignment's freeze/profile/case/treatment/budget/retention records?

## 6. Minimal roadmap / TODO

- [x] **D0:** proof/timeline map and qualification-horizon boundary.
- [ ] **D1:** use the real Gemma12 HTTPX pair to own architecture/authority and mechanical-vs-semantic validation.
- [ ] **D2:** trace one real Structured interaction end-to-end through retained artifacts and code.
- [ ] **D3:** predecessor failures -> reference-v2 design -> deterministic proof/qualification.
- [ ] **D4:** use Raw HTTPX to learn budgets, stateless packing and stopping failure.
- [ ] **D5:** real qualification cohort, exact deployment identity, freezes and admission.
- [ ] **D6:** actual frozen Raw/Structured fairness/schedule/runner rules.
- [ ] **D7:** review selected actual propositions from published semantic reports.
- [ ] **B intake:** periodically record newly published main B evidence; use it for mechanism learning without prematurely deciding the final comparison.
- [ ] **D8:** after complete B publication, perform comparative interpretation.
- [ ] **D9:** learner synthesis, scenario checks, remaining gaps and durable conclusions for merge/promotion.

Expected compressed journey:
`real pair + architecture -> one real code trace -> v2/budget/qualification -> fairness + real review method -> final B comparison -> synthesis`.

## 7. B intake queue

### Branch-creation horizon
- main base: `243ab0c1...`;
- reference-v2 deterministic proof: complete;
- pre-inference freeze: complete;
- qualification cohort: **12/12 qualified, 60 charged calls**;
- semantic admission: permitted;
- real semantic assignments at branch-base checkpoint: **0 attempted**.

### Intake after branch creation — published first real pair
Main later published:
- `53a865a0...` — Gemma12 HTTPX Raw first real boundary result/source review;
- `988dd812...` — Gemma12 HTTPX Structured review and first within-deployment pair review.

Learning impact:
- **D1:** provides real evidence/interpretation/validation boundary;
- **D2:** provides the preferred real interaction to trace;
- **D4:** Raw provides a concrete budget/stopping/navigation failure;
- **D7:** Structured provides real supported/unsupported/narrower/contradicted propositions;
- **D8:** no final treatment conclusion yet; remaining batch is still required.

For every later main intake append:
- main commit/horizon;
- new B artifact(s);
- whether they change architecture/protocol/proof boundary or only add outcome evidence;
- which D blocks/questions need amendment;
- whether the artifact is useful as a new canonical example or merely another sample;
- no final comparative conclusion until the completed B disposition exists.

## 8. Branch discipline and eventual merge

- Do not edit root `MEMORY.md` on this branch to claim live main progress.
- Do not overwrite main B evidence or model outputs.
- Do not copy owner-only/raw runtime artifacts into the repository merely for learning unless governance explicitly permits it; use retained/public-safe evidence and exact locators where appropriate.
- Never invent or reconstruct hidden chain-of-thought; learn from observable requests, responses, observations, reports and receipts.
- Prefer one decisive real example over many redundant cases.
- If main changes code we are studying, reconcile before making code-specific learner claims.
- Final merge only after completed B horizon is reconciled and stale statements are repaired.
- Promote learner-owned conclusions only after demonstrated understanding; AI explanations alone remain preparation, not mastery.
