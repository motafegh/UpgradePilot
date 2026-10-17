# Investigator real-case Raw-vs-Structured semantic comparison — LbD cycle

**Date/horizon:** October 17, 2026, +03:30; A0 reconciled from `main@ce96280c4d271e63ad0b60db9dd1c1f8e635f71b`.
**Session status:** ACTIVE — Ali explicitly directed “go for B fully” on October 18; B is in progress. The preceding A2 gate text retains its historical horizon; the activation below controls this cycle's progression.
**Responsibility:** freeze and verify the paired real-case Raw-vs-Structured semantic comparison over two exposed development cases and three selected deployments, then only after the pre-inference gates are satisfied attempt the admitted assignments, preserve immutable outcomes/failures/costs, perform source-to-claim semantic review and reach a bounded retain/reject/inconclusive disposition.
**Live owner:** [MEMORY.md](../MEMORY.md) alone owns current continuation.
**Controlling owners:** [Investigator integration/comparison plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md), explicitly amended by the [three-deployment semantic-comparison decision](../plans/INVESTIGATOR_SEMANTIC_COMPARISON_THREE_DEPLOYMENT_AMENDMENT_2026-10-17.md).
**Previous:** [deployment/model-interface D/E closure](2026-10-17_deployment-interface-D-reconciliation-and-E-entry.md).
**Procedural provenance:** `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.

## Phase status

| Phase | Status | Current meaning |
| --- | --- | --- |
| A0 | **DONE** | Reconciled live owners, previous closure, amendment, final deployment/interface evidence, durable common-input snapshot, current experiment contracts and semantic-review owner; initialized this one cycle record. |
| A1 | **DONE** | Ali explicitly agreed with the reconstructed state and cleared the continuity gate. His configuration-proof correction is incorporated below rather than treated as a contradiction. |
| A2 | **DONE — progression explicitly directed** | Orientation and the budget/proof consequence were presented; Ali explicitly selected B fully. The budget-allocation reasoning answer remains unassessed and is preserved for D, not recorded as mastered. |
| B | **CURRENT** | Implement model-visible budget metadata and focused proof, then complete the successor freeze before any prediction. Required synthetic requalification has a separate frozen budget before semantic admission. |
| Verification gate | PENDING — scoped implementation GREEN | 40 focused experiment tests and 65 nearest Workspace controls pass. Complete freeze, actual interface requalification and conditional semantic result/review remain required. |
| D | PENDING | Evidence-backed learning from the actual comparison/review result. |
| E | PENDING | Repair/defer D gaps, disposition the experiment and hand off the next responsibility. |
| C | **CONTINUOUS** | Preserve meaningful progression, failures/corrections, proof/non-proof and learner gaps in this record. |

## A0 — current-state reconciliation

### 1. Live state and selected successor

`MEMORY.md` and the D/E closure agree: the canonical Workspace foundation, adapter/mechanical integration and deployment/model-interface qualification are closed through their required gates. The selected successor is the real semantic comparison, with no automatic inference authorization.

The October 17 amendment explicitly supersedes the old two-deployment/eight-assignment future baseline for this successor:

`2 cases × 2 treatments × 3 deployments = 12 assignments`.

Selected deployments are Gemma 4 12B, Qwen3.8-27B UD-Q4_K_M and Gemma 4 E4B. Qwen3.5-9B remains qualified but unselected; Gemma E2B and MiMo remain withheld at their current points.

### 2. Engineering horizon did not silently move

The final bounded deployment/interface engineering horizon is `c414a6e9bacd572d2d04c38ca54b313f73e83846`. Comparing that horizon to A0 `main@ce96280c4d271e63ad0b60db9dd1c1f8e635f71b` shows five later commits affecting only:

- `MEMORY.md`;
- the three-deployment amendment;
- the D/E reconciliation record;
- the promoted D learning closure.

No experiment/product/test executable changed in that delta. The final qualification evidence therefore remains the relevant executable horizon, while the newer amendment controls successor assignment count/question.

### 3. Historical-baseline statements are superseded, not rewritten

The r8 final analysis/catalog/freeze and plan sections written before Ali selected E4B still say the later comparison has two deployments/eight assignments. Those statements accurately describe their own historical horizon and must not be edited into retroactive agreement. For this successor they are **superseded by the October 17 amendment and current MEMORY**. Treating them as current would be a protocol error; preserving them as historical evidence is not a contradiction.

### 4. Common real-case evidence basis recovered from its durable owner

The current common snapshot owner is `common-freeze-2026-10-16-2025`, not the older expired `/tmp` preparation. Its dated qualification records a durable owner-only original plus validated same-machine backup:

- original: `/home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025`;
- backup: `/home/motafeq/.local/share/upgradepilot/investigator-inputs/common-freeze-2026-10-16-2025/validated-backup`;
- preparation manifest SHA256: `e5b296dba68f7b6bb0c755e00681ec0db1ad8727ed9af51d417e5751a25bd4ac`.

Exact case identities at that horizon:

1. `development-httpx-framework-ci` — `Aidan-Wallace/kubernetes-dashboard-token-api` PR 20, base `b065646e4b7b894964567950f9ad770b02c136c2`, head `391508134b083b8f54461c0b576e8f7985c6ecb4`, `httpx 0.27.2 -> 0.28.1`, catalog `288c3c88a12ed32706641b977f5a29b09d4727b6e9fa3de7ff2df23e28ba1bf3`, checkpoint digest `991b5eb0cf2ca6d86319ef80f07f6939702f27e134f4a3954ca2e0bb619c7e5f`.
2. `development-glyphslib-pytest-stopping` — `googlefonts/glyphsLib` PR 1145, base `044f19e4b1437bfc4343592486f4e3c6040306d9`, head `f3cda8a94600e58d27f1bc17c99b7693718b6350`, `pytest 9.0.2 -> 9.0.3`, catalog `37f51311401773b05a7934945a2cc9d7904af044d328ec9fb1dae855062626ce`, checkpoint digest `202f04de13ff2223d1ace35b36aafc0a98b5fde2a2abe2e26c8a6e568dce974e`.

That snapshot was mechanically/offline qualified on October 16. **Successor inference cannot inherit “available now” from a dated check:** the pre-inference freeze must revalidate the exact retained files/store/source-profile identities and supported offline reads at the current horizon without acquisition/model/evaluator calls. New acquisition would create a new evidence freeze, not reproduce this one.

### 5. Exact selected deployment evidence entering successor planning

Final current-runtime evidence records CUDA llama.cpp 2.60.0 (`b11698/2a667032d` display identity) and existing isolated `lmstudio==1.5.0`. All selected deployments are 4/4 synthetic interface-qualified at their exact observed points, with requested/applied prediction/load/prompt-count correspondence checked in the completed cohort.

- **Gemma 4 12B** — weight SHA256 `c088a44859de42a1966851b552ba628c0ff4419b87c4622539d69430f40024ed`; context 32768; requested GPU ratio 0.45 / observed backend `n-gpu-layers=22`; CPU unified q8_0 K/V; batch 256; thinking off; T0.2/K40/P0.95; canary generation cap 2048.
- **Qwen3.8-27B UD-Q4_K_M** — weight SHA256 `322e194ff79741c7baa497c240f677f54b201b0efab44ca8e50f122b39123482`; context 32768; requested GPU ratio 0.20 / observed backend `n-gpu-layers=13`; CPU unified q8_0 K/V; batch 256; MTP exposed applied; thinking off; T0.2/K40/P0.95; canary generation cap 2048.
- **Gemma 4 E4B** — weight SHA256 `e8cd1a4c5162dfa355c567b4099206793b5548951f077f376a0076dc0a058`; context 32768; requested full offload / observed all-layer sentinel; CPU unified q8_0 K/V; batch 256; native thinking on; T1/K64/P0.95; generation allowance 8192.

Interface qualification does not establish semantic correctness, autonomous discovery/stopping, usefulness, action permission or generalization.

**Important successor configuration consequence:** Gemma12 and Qwen27 qualified with a 2048 synthetic generation cap, while the comparison plan/amendment carries an 8192 real-case allowance. Ali explicitly corrected the proof model at A1: 2048 → 8192 is a **material prediction-configuration change from the exact qualified point**, not merely a context-capacity question. The successor therefore keeps three independent proofs separate:

1. **Rendered/context capacity fit** — actual fully rendered real-case/late-history/final-report input plus 8192 generated-token reserve plus justified margin must fit the selected context without silent loss/truncation.
2. **Requested-versus-applied correspondence** — the intended load/prediction configuration, including the 8192 generation allowance and all other material controls, must match the actually observed runtime/applied state.
3. **Bounded interface requalification at the changed point** — because Gemma12/Qwen27 would no longer be at their exact 2048-qualified point, the changed 8192 points must receive the versioned bounded correspondence/qualification proof required by the controlling plan/amendment before their semantic assignments are admitted.

Capacity-fit evidence cannot transfer the prior 4/4 qualification by itself. The old 4/4 result remains evidence about the old 2048 operating point. E4B already qualified with 8192, so no output-limit change is inferred for it, but its exact real-case shapes/configuration and current correspondence still must be frozen and verified; any material drift would likewise trigger versioned requalification rather than inheritance.

### 6. Existing experiment contract entering the freeze

Current experiment sources preserve the model-free Workspace contract plus the complete-stateless model boundary. The final r8 freeze content-hashed the active code at:

- `experiments/investigator_workspace_adapter.py` — `b9ed4a2533fc671a3026d066154cfb14910ced5551dd13664b0c3e562ba08321`;
- `experiments/investigator_workspace_trial.py` — `7a883f318a244612edbe5ec4691ae967b4f7722a1db4dfbc7a1d20a34137ec30`;
- `experiments/investigator_model_interface.py` — `f42a9e28779bb6a545982352332a1ec28c3a4eac117209e93bfa0fc32ab59031`;
- `experiments/qualify_investigator_model_interface.py` — `50dfaf8b0d0bc71b0e67c9e935a6a3642ad0e660f87a922a49fd2d816d70996e`.

No executable change occurred after that horizon.

The inherited protocol provides:

- contract `investigator-contract2-workspace/1`;
- a fixed evidence-discipline system prompt and generic dependency-investigation task;
- Raw source navigation versus Structured source + native view/page access over the same underlying case evidence;
- exact tool argument schemas and strict no-extra-field validation;
- Contract-2 report schema with asserted/inferred/unresolved statuses;
- current-request-only typed-reference authority for stateless inference;
- whole-event packing/omission with no text truncation;
- conservative operation/observation/correction/deadline accounting;
- fresh assignment host/lineage and no product action authority;
- immutable original model output separated from later semantic review/corrections.

These contracts are an inheritance candidate, not yet the successor run freeze. The successor must explicitly bind their exact content identity plus any semantic-case runner/packing differences rather than relying on names alone.

### 7. Semantic review owner entering the freeze

The controlling plan carries forward `claim-evidence-review-v2` with nine dimensions and no weighted winner score:

1. relevant evidence coverage;
2. interpretation correctness;
3. unsupported claims;
4. scoped negative evidence;
5. unresolved quality;
6. stopping quality;
7. recommendation usefulness;
8. reviewer effort;
9. resource cost.

Case-specific source obligations must be preregistered before outputs and hidden from the Investigator. Every material assertion, including summary/recommendation surfaces, needs source-to-claim support review; citation validity alone is insufficient. Immutable model outputs remain separate from reviewer corrections. AI-assisted known-case review is formative, not independent acceptance.

### 8. A0 blocker/inconsistency assessment

No contradiction or hidden executable regression requires redesigning the selected successor.

There are, however, **real pre-inference blockers by design**—normal prerequisites rather than defects:

- current offline availability/hash/store validation of the common snapshot and validated backup has not yet been re-established for this successor;
- the three intended deployments must be re-observed at the exact successor configuration/runtime horizon rather than assumed from dated qualification receipts;
- Gemma12/Qwen27 require explicit versioned 8192 operating points with capacity-fit, applied-correspondence **and bounded interface-requalification** proof because their qualified synthetic calls used 2048;
- exact real-case rendered request shapes/tokens, late-history packing and final-report fit are not yet successor evidence;
- the 12 assignment IDs and balanced serial order are not yet frozen;
- exact prompt/tool/reference/packing/report identities for the semantic batch are not yet published as one successor manifest;
- case-specific semantic source obligations, masking/order/assistance/timer/source-check protocol are not yet frozen;
- the successor accounting ledger, prior-spend boundary, owner-only output root and public-safe evidence path are not yet published/validated.

No model load or inference is justified before those items are resolved in the pre-inference freeze. An unresolvable input/deployment/configuration problem withholds the affected assignment(s) or forces a versioned pre-run revision; it never authorizes a silent substitute/rerun.

## Living A-phase orientation/learning map

### A1 continuity topics

- What the closed deployment/interface cycle actually established versus what it explicitly did not.
- Why E4B changes the semantic experiment design rather than merely adding four casual calls.
- Why old `2 deployments / 8 assignments` statements remain historical evidence while the amendment controls this successor.
- Why qualified interface points still need successor-specific case/input/configuration/fit/review freeze.
- The specific 2048-versus-8192 consequence for Gemma12/Qwen27, including the distinction between capacity fit, applied correspondence and requalification.

### A2 upcoming-responsibility topics

- Common case freeze → fresh assignment host/lineage → Raw/Structured capability boundary → complete stateless model request → strict tool/reference/report admission → immutable output/accounting → offline source-to-claim review → bounded disposition.
- How to choose/freeze all 12 IDs and a balanced serial order without outcome-dependent scheduling.
- Exact budget/accounting model: per-assignment ceilings versus aggregate ceilings, prior qualification/requalification spend kept separate, ceilings not targets.
- Real-case token/context/output fit, requested-versus-observed runtime correspondence and changed-point interface requalification as separate gates.
- Semantic-review masking/source obligations and how reviewer evidence stays outside model input.
- Failure/refusal/no-rerun/withholding semantics and the line between experiment evidence and product authority.

### Expected result / proof boundary

Expected cycle output is one truthful frozen 12-assignment protocol followed, only after admission, by attempted results and semantic review sufficient for a **retain / reject / inconclusive development-pilot disposition**. One sample per case/treatment/deployment cannot establish stochastic reliability, intrinsic model ranking, general semantic superiority, maintainer usefulness, production adoption or action permission.

### Stop conditions / non-goals

Stop/reconcile before affected inference on input drift/unavailability, identity/configuration mismatch, unverified 8192 fit/correspondence/requalification, placeholder manifest fields, unequal evidence universes, protocol/order/budget changes, protected-review leakage or a required product-authority change. No cloud fallback, target execution/mutation, hidden-reasoning retention, extra model arm, multi-agent/critic topology, outcome-driven tuning or premature productization is admitted.

## A1 continuity packet and gate closure

The successor begins from a **qualified delivery/interface mechanism, not a qualified semantic Investigator**. The real scientific question is whether Structured native evidence improves evidence use/interpretation/uncertainty/stopping/recommendation quality relative to Raw navigation over the same evidence universe, with E4B adding the bounded smaller-deployment/resource question.

Ali explicitly agreed with the A1 reconstruction and cleared the continuity gate. He added one material proof clarification: Gemma12/Qwen27 2048 → 8192 is a prediction-configuration change, so capacity fit must not be treated as qualification transfer. This clarification is consistent with the controlling amendment's rule that any material change from a qualified point is versioned and receives bounded correspondence/qualification proof before semantic admission.

A1 is therefore **DONE**. No B work or model inference occurred during this transition.

## A2 — upcoming responsibility orientation

### 1. What this cycle is actually testing

The primary experiment is not “which model answers best.” It is a controlled **representation/access comparison** over the same retained evidence universe:

`same case evidence + same task/authority/budgets + fresh assignment state`

→ Raw treatment: bounded source navigation

versus

→ Structured treatment: the same source navigation **plus** admitted native records/pages.

The primary question is whether Structured access produces better evidence coverage, interpretation, uncertainty handling, stopping and recommendations. The three deployments let us see whether that treatment effect appears similarly or differently across the two larger baselines and the smaller E4B point. Cross-model observations remain deployment-specific; this design does not estimate intrinsic model ranking or stochastic reliability.

### 2. The end-to-end evidence/control flow

For each eventual semantic assignment the intended flow is:

`exact retained case snapshot`
→ `fresh product Workspace host + lineage`
→ `treatment-specific capability menu`
→ `complete explicit stateless request using the frozen prompt/tool/report contract`
→ `exact qualified deployment point`
→ `strict tool/reference/report admission`
→ `immutable original output + complete accounting`
→ `offline source-to-claim semantic review`
→ `paired development disposition`.

The product Workspace remains authoritative for evidence identity/material validity. The Investigator produces attributed interpretation/report material. Offline review validates claims; it does not retroactively change the model output or become runtime feedback. Final product/action decisions remain outside this experiment.

### 3. Two pre-semantic admission gates

A2 makes the ordering explicit so qualification work cannot be confused with semantic work.

#### Gate P — complete pre-inference freeze before any new model prediction

Before **any** new model inference, B must publish and verify a complete successor freeze that fixes:

- exact HTTPX/glyphsLib retained input identities and current offline availability checks;
- exact intended three deployment configurations, including the intended 8192 case allowance;
- exact 12 semantic assignment IDs and balanced serial order;
- exact prompt/system/task/tool/reference/packing/omission/report contracts and code identities;
- semantic per-assignment and aggregate ceilings;
- a **separate bounded requalification budget/order/protocol** for every changed deployment point that requires model-interface proof;
- real-case rendering/token-fit measurement procedure;
- review source obligations, masking/order/assistance/timing/source-check procedure;
- accounting/retention/public-safe evidence paths;
- failure/refusal/no-rerun/versioned-repair rules.

This freeze must contain no unknown placeholder that will later be filled opportunistically from outputs. A deployment may be explicitly marked `WITHHELD_PENDING_REQUALIFICATION`; that is a real state, not a placeholder.

Only after Gate P is verified may any frozen non-semantic qualification prediction occur.

#### Gate Q — exact deployment-point/interface admission before semantic assignments

The 12 real-case assignments remain withheld until their deployment points satisfy the required interface proof.

For **Gemma12 and Qwen27**, 8192 changes `maxPredictedTokens` from the exact 2048 current-runtime qualified point. Their admission therefore needs all three:

`real rendered-shape capacity fit`
+
`requested/applied configuration correspondence at the 8192 point`
+
`bounded outcome-blind interface requalification at that changed point`.

The controlling plan's normal proof shape covers both treatments and both short and near-envelope/late-final behavior, including complete visible structured responses, tool/reference behavior, honest omissions and final report production. The strong default for B is therefore to freeze the full representative Raw/Structured × short/near-envelope synthetic matrix at the 8192 point rather than weaken proof merely because the old 2048 point passed. These are **synthetic interface canaries**, not HTTPX/glyphsLib semantic runs.

For **E4B**, the previously qualified point already used 8192. B still must verify exact real-case rendering/fit and current configuration identity/correspondence. If current inspection shows no material configuration/runtime drift, the existing 4/4 qualification remains evidence for that same exact point; if a material point changes, E4B enters the same versioned requalification rule rather than silently inheriting its prior pass.

Complete all required deployment-point qualification/dispositions **before starting any of the 12 semantic assignments**. This prevents semantic outcomes from influencing later configuration tuning. A failed changed point is retained as a negative qualification result. Reducing the experiment to fewer deployments, changing configuration, or substituting another model would require a new explicit pre-semantic protocol revision before any semantic outcome, not an automatic fallback.

### 4. What “balanced 12 assignments” means

There are six case×deployment pairs; each pair contains Raw and Structured. Three deployments make perfect per-case treatment-order symmetry impossible, but we can still balance deliberately.

The intended balancing rule for B to instantiate exactly is:

- within **each deployment**, one case is Raw-first and the other Structured-first;
- across all six case×deployment pairs, exactly **three are Raw-first and three Structured-first**;
- because each case has three deployments, one case will necessarily be 2:1 in one first-treatment direction and the other case will use the inverse 1:2 split;
- rotate case/deployment serial positions so one treatment or one case is not systematically early or late;
- every assignment gets fresh Workspace/context state; execution remains serial;
- the exact 12 IDs/order are frozen before outputs and never rearranged because a previous assignment was slow, failed or surprising.

B will choose the concrete IDs/order using that rule and verify the mapping mechanically. The rule is fixed now; the exact schedule is intentionally left to the freeze rather than invented during A2.

### 5. Budget and accounting model

The amendment carries semantic per-assignment ceilings of:

- 16 model calls;
- 524,288 input tokens;
- 131,072 generated tokens including reported reasoning where applicable;
- 48 charged operations;
- 8 MiB delivered observations;
- 14,400 seconds;
- 8192 generated-token per-call/final reserve target subject to exact qualification.

Across 12 assignments, the conservative semantic maxima are 192 calls, 6,291,456 input tokens, 1,572,864 generated tokens, 576 charged operations, 96 MiB observations and 172,800 seconds. They are ceilings, not targets.

Any new synthetic requalification needed to admit changed 8192 deployment points has a **separate explicitly frozen budget and ledger**. It is neither silently deducted from the semantic 192-call ceiling nor treated as free. Final resource reporting distinguishes preparation/requalification cost from within-assignment semantic cost while still retaining the total operational cost of reaching the comparison result. Earlier deployment/interface spend remains historical prior spend, not a semantic assignment result.

### 6. Prompt/tool/reference/packing fairness

Both treatments share the same system/task authority, target transition, source universe, report schema, stateless-history rule, correction rules and source-navigation capabilities. Structured differs only by the declared native record/page capabilities.

Important fairness constraints:

- no solved path, expected answer, case-specific obligation, reviewer label or outcome-derived hint enters model input;
- Raw being unable to call a native tool means the view is **withheld by treatment**, not nonexistent evidence;
- whole-event packing/omission policy is common and frozen; no arm receives selective history enrichment;
- current-request-only reference eligibility remains authoritative for stateless inference;
- reviewer/source obligations are outside the model context;
- any transport/interface difference forced by a deployment is declared and qualified before outcomes, not patched afterward.

### 7. Semantic review protocol

Before model outputs exist, B must preregister case-specific source obligations for HTTPX and glyphsLib against the frozen common evidence. Those obligations stay hidden from the Investigator and form the original coverage denominator; genuinely new obligations discovered during review are supplemental rather than silently changing that denominator.

The review sequence should preserve masking as far as practical:

1. first-pass semantic review uses treatment/deployment masking where feasible and records any identity leakage/unmasking;
2. every material proposition in claims, summary, conditions and recommendation is checked against the actual cited/source evidence for support, scope, polarity, version/time and applicability;
3. stopping is checked against remaining feasible discriminators at the actual capability/budget boundary, not merely the presence of a finish event;
4. reviewer assistance and active review time are recorded; unknown effort remains unknown;
5. treatment/deployment identities are then revealed for paired interpretation and resource/cost comparison.

The nine dimensions remain separate profiles; there is no weighted winner score. AI-assisted review of these exposed development cases is useful formative evidence but cannot establish independent maintainer acceptance or protected-case generalization.

### 8. Failure, refusal and no-rerun semantics

The experiment must make failure informative rather than disappear it.

- Each semantic assignment is one frozen sample. No failure-selective rerun or output salvage.
- Allowed visible corrections happen only inside the same assignment under the already frozen correction/call/operation ceilings; rejected originals and costs remain retained.
- Timeout, empty output, malformed output, reference refusal, generation exhaustion, runtime/configuration mismatch and semantic incompleteness remain distinct outcomes.
- Unknown usage is unknown, never zero; conservative reservation may bound it without relabeling it measured usage.
- A pre-semantic qualification failure withholds the affected deployment point. A discriminating repair, if justified, requires a versioned pre-semantic revision and fresh bounded proof before semantic outcomes; it is not tuning-until-pass.
- Once semantic outcomes begin, no configuration/prompt/packing/order/budget change may be tuned and then pooled into the same comparison.
- Withheld/failed/incomplete assignments remain in the disposition; the final outcome may legitimately be inconclusive.

### 9. What B will and will not do

If the A2 gate clears, B begins with **freeze construction and verification**, not model calls. It will first establish current retained-input availability, exact identities/contracts/order/budgets/review/retention and real rendered-fit evidence, and freeze any required synthetic requalification protocol.

Only after Gate P is complete may the separately frozen interface requalification inference occur. Only after Gate Q is satisfied may the 12 real-case semantic assignments begin.

B remains experiment-owned. Product code may be used through its supported Workspace interfaces, but product source must not depend on experiment code. If B discovers a genuinely missing product seam or authority requirement, it stops and returns to that owner rather than emulating authority or prematurely productizing the harness.

### 10. Acceptance and non-proof boundary

A successful cycle can establish a bounded development conclusion about whether Structured native access improves evidence use over Raw navigation for these two exposed cases under the exact three frozen deployments and measured costs.

It **cannot** establish:

- stochastic reliability from one sample per condition;
- intrinsic model superiority;
- general semantic competence;
- protected-case generalization;
- independent maintainer usefulness;
- product action permission;
- production adoption;
- a reason to copy the experiment harness into product code.

A result can therefore be technically successful even when the correct disposition is **reject** or **inconclusive**, provided the evidence and failure states are preserved truthfully.

## A2 pre-B understanding gate — CURRENT

The main new ownership distinction is:

`fits in context` **does not mean** `runtime applied the intended configuration`, and neither means `the changed deployment point is interface-qualified`.

For Gemma12/Qwen27, the intended 8192 point must independently satisfy all three before semantic admission. The prior 4/4 canary result remains attached to the exact 2048 point and is not silently transferred.

No B work, model load or model inference has been performed in A2. The normal pre-B understanding gate remains open.

## October 18 takeover review — before continuing A2

**Inspection horizon:** `main@da467974a7800b891b360f9c8a44d301fd6fde80`, approximately 02:05 Asia/Tehran. Ali requested pulling main, analyzing recent work/working memory and independent recommendations before deciding how to continue. Fast-forwarded from `c414a6e9`; the unrelated untracked October 3 audit was preserved.

This is a dated review/reconciliation appendix within the existing cycle, not another phase-status owner. A0/A1 retain their recorded completion; A2 remains at its understanding gate; successor B and inference remain pending. Read-only audit probes below are not successor freeze construction or interface/semantic execution. No product, experiment, plan, accepted semantic owner or live-position change is made by this review.

**Proportionate route:** the normal route for a separately selected substantive audit would create its own cycle and orientation gates. Here the requested review serves takeover/onboarding of this already initialized successor, before Ali decides continuation. Preserve its evidence in this record's continuous C instead of creating a competing audit cycle or declaring the successor advanced. Findings are proposals for discussion, not accepted protocol changes or new live blockers. No learning ownership is inferred from this AI review.

### Fresh evidence

- Both new experiment families pass: **35 tests**, using `PYTHONPATH=src:. .venv/bin/python -m unittest experiments.tests.test_investigator_workspace_trial experiments.tests.test_investigator_model_interface -q`.
- Nearest Workspace controls pass: **65 tests**, using `PYTHONPATH=src:tests:. .venv/bin/python -m unittest test_workspace_consumer_access test_workspace_lifecycle_publication test_workspace_host_integration -q` (25.072 seconds). The earlier asynchronous test handle became unavailable across a user turn; this completed rerun supplies the result.
- The older planner entry family still has **23 passes / four fixture errors** across 27 tests. The same removed `segment_index` constructor argument at `experiments/tests/test_evidence_gap_product_planner_composition.py:270` fails before projection; this is neither newly caused drift nor a planner semantic failure. No fixture repair was performed.
- `verify_retained_inputs` revalidates **17 input files** and **96 current product-source hashes** against the common snapshot. Original and backup directories exist. Fresh guarded cold reads of both cases from both roots succeed: 16 revisions per case, matching original/backup projection hashes, unchanged databases and nine guards per child. This supports current offline availability at the checked scope, not a complete successor admission freeze.
- All four r8 frozen executable-source hashes match current source. The local r8 retention index matches published SHA256 `ba54645fd808ca44023ccc306b15afe21ce55cfbce652b42d54484d313dd9613`; all **600 indexed files / 22,798,015 bytes** revalidate by size/hash and 0600 mode. No live model/runtime identity or off-machine-backup claim is added.
- r7/r8 assignment dispositions agree with the final catalog: four exact points qualify 4/4; E2B and MiMo remain 2/4 withheld. Two original visible reports were sampled independently. Qwen9 Raw-long recommends proceeding with the dependency update from the synthetic marker; Gemma12 Structured-long describes the system as confirmed interface-ready from that marker. These support the already recorded distinction between interface passing and unsupported semantic conclusions; originals/grades remain unchanged.

### New source-interface observation: budget visibility

The current `protocol_definition` retains limits and tool/report charging, but `pack_input` serializes only contract/system/task/phase/tools/report schema/events/omissions. `run_model_trial` passes this packing path to the model; `present_request_body` cannot restore fields that were never packed. A model-free probe of the normal protocol confirms that the delivered body contains neither static budget/charging fields nor explicit remaining call/operation allowances. Driver/model guards still enforce the limits.

**Assessment:** this is a decision-relevant visibility gap for interpreting budget-aware stopping, not proof that historical canaries failed or an already specified invariant was violated. An external cutoff cannot be described as a model's informed allocation decision when the relevant allowance was not delivered. Static maximum, current remaining allowance and final-report/termination reserve are also different facts.

**Recommendation before freeze:** decide and document the budget information the Investigator receives and the claim the review will assess. Prefer minimal factual, symmetrically delivered budget/remaining-capacity information, owned by runner accounting, if informed allocation/stopping is part of the selected responsibility. Such an input-contract change needs the ordinary bounded implementation and applicable source-bound requalification before inference. Alternatively retain the current contract explicitly and review external exhaustion separately from voluntary stopping, with the narrower interpretation recorded. This review selects neither implementation automatically nor a weaker stopping claim silently.

### Other takeover recommendations

1. Preserve the existing scientific boundary: Structured bundles native analysis/access with source navigation; a gain cannot be attributed to JSON serialization alone. Compare treatments within each exact deployment first. E4B's thinking-on recipe differs from the larger off-mode recipes, so cross-deployment results are operating-point observations, not intrinsic size/model effects.
2. Make the nine-dimension review executable before outputs: exact source obligations, material-proposition support/contradiction/unknown records, a source-check trace, reviewer assistance/time and honest masking limits. Keep available, delivered, used, cited and supported evidence distinct, especially when final-request packing omits earlier material. Do not infer evidence exhaustion from the report-phase empty tool menu.
3. Keep the intended 8192 point and its separate bounded requalification decision explicit. Do not start another model/runtime optimization sweep merely because more tuning is possible. The existing 338-attempt historical cost and measured large-model latency make total preparation plus within-assignment cost relevant to disposition; existing ceilings remain maxima rather than spending targets.
4. Keep planner fixture repair and normal-report/task/reviewer usefulness readiness as separate owned responsibilities with concrete re-entry conditions. Neither blocks this comparison by default, and comparison success cannot discharge either obligation.

**Review limits/handoff:** no full product/installed/hosted suite, model load/inference, fresh runtime qualification, target execution/acquisition, hidden reasoning inspection or independent semantic/usefulness acceptance occurred. No source defect requiring reopening completed interface qualification was established in this bounded sample. Resume by discussing these findings at the existing A2 gate, resolving any selected input/review-contract change with its proper owner, then deciding B scope. This review does not satisfy the gate on Ali's behalf.

Procedural provenance: `UP-SKILL:upgradepilot-repository-audit`; `UP-SKILL:upgradepilot-workstream-supervision`; continuous preservation uses the existing `UP-SKILL:upgradepilot-working-memory` route.

## October 18 planning follow-up — budget visibility and concrete review

Ali directed continuation with “go on for it” after the takeover recommendations. Continued the existing A2 responsibility through bounded Planning/Design; no new cycle or executable mutation. Read the plan owner, inspected the driver/model ledger and packing seams, and used the applicable Operating Guide rationale/decision-readiness sections. The controlling integration plan now owns the reusable contract/proof requirements; this record preserves their reasoning and time-scoped handoff.

### Design and responsibility placement

- Keep enforcement in the existing trial/model guards. Add a factual model-visible budget observation from those same authoritative ledgers, not counters inferred from model notes/history. Static maximum, remainder before the next invocation and final completion cost are different facts.
- The trial driver owns turns, operation units, observations, corrections and its deadline. The model binding owns model calls, validated token spend, context/output allowance and its deadline. Joining them in experiment request composition needs no new product service, dependency, evaluator or durable architecture decision.
- Snapshot driver state before packing; enrich from model state before rendering. Keep the snapshot stable while repacking that invocation. The upcoming invocation is included in the displayed remaining count; the upcoming rendered input is not already deducted from prior-spend token remainder. Existing actual token/configuration admission remains authoritative.
- Expose exact operation costs and the finish/report/termination obligations, without claiming that the current driver reserves completion capacity it does not reserve. A finish consumes one model invocation and three operation units; a report consumes another invocation and four plus unique citations; termination reserves one operation unit. More calls alone do not imply enough operations for another read plus completion. Time values are sampled allowances, not guaranteed future capacity.
- The credible alternative is retaining invisible budgets and narrowing stopping interpretation to external cutoffs versus voluntary finish. Prefer factual visibility because the selected scientific question includes allocation/stopping under bounded capacity. This supports the full responsibility without adding automatic stopping policy, optimal scheduling or semantic adequacy claims.

### Review protocol made concrete

The existing plan's nine dimensions now have explicit record requirements for source obligations, evidence-use trace, each material proposition/support reason, stopping cause/state/discriminator and reviewer effort/masking. Review all report surfaces, keep available/delivered/used/cited/supported distinct, preserve immutable outputs and separate unsupported from contradicted or unresolved. Treat the HTTPX capture-scoped CI absence and glyphsLib declaration-versus-runtime boundary as real calibration examples; exact case passages/obligations still require source-check/freeze during B, outside model inputs. No automated semantic grader or protected-case acceptance is introduced.

### Proof consequence and bounded implementation handoff

The proposed budget observation changes the common request contract for **all three** deployments. Therefore the earlier A2 statement that unchanged E4B configuration could inherit its 8192 canaries no longer suffices for the revised input contract. Old qualifications remain unchanged historical evidence. After implementation/model-free proof and the complete pre-inference freeze, requalify the revised contract for all selected points; combine Gemma12/Qwen27's 8192 allowance with that same revision. Freeze the exact bounded matrix/order/call ceiling before inference rather than start another tuning sweep or redundant qualification revisions.

Expected B edit scope is the existing experiment driver/model packing path, synthetic representative-shape preparation, focused tests and contract guides. Test authoritative/decreasing counters across accepted/refused calls, completion costs, unchanged enforcement, assignment isolation, budget visibility through omissions/report phase, exact rendering and unknown-usage refusal. Product code, model roster, case universe, tool authority and semantic ceilings are not expanded by this design.

Validation passed for all three changed documents: 41 local links, two anchors, balanced fences, final newlines and `git diff --check`. Only the plan/live-memory/cycle record changed; all four r8 frozen executable hashes still match. Runtime tests were not repeated for this documentation-only increment. No model-free implementation proof, actual freeze, model load/inference or semantic review execution is claimed. A2 ownership remains open: explain why spare model calls can coexist with insufficient operation units to read again and still finish/report, and why a budget-driven stop does not establish adequacy. Resume at that understanding boundary before B. These questions are learning/ownership checks, not approval requests for a hidden implementation.

Procedural provenance: `UP-SKILL:upgradepilot-planning-design`; existing Learning-by-Doing and Working-Memory routes continue to apply.

## October 18 Build activation and early implementation

Ali explicitly directed “go for B fully.” This authorizes the coherent successor B responsibility through implementation, verification, full pre-inference freeze, required bounded qualification and conditional semantic execution. It does not waive a failed freeze/qualification, authorize another model/configuration sweep or establish learner mastery from the unanswered A2 question. Under the Smart Situational Override Rule, preserve that narrow ownership check for D rather than repeat an approval request after explicit B direction. No scientific/proof/security gate is waived.

Applied `UP-SKILL:upgradepilot-build-implement` with the continuing Learning-by-Doing/Working-Memory routes. The loopback inventory is reachable and selected assets are registered with no loaded selected instances; this is inventory evidence, not runtime qualification.

Implemented a versioned budget observation in complete packed requests. Driver counters are sampled before the next invocation; model limits/validated spend are joined before rendering with a stable snapshot across repacking. Frozen task overrides cannot replace current accounting. Completion costs are visible without adding automatic stopping or claiming a finish/report reserve. Unknown token usage stays null and existing guards still refuse further prediction. Representative preflight now includes the full budget representation. First focused result: 37 tests pass, including actual driver/model composition across a refused call, ledger decrements, retained final metadata, assignment isolation, omission survival and the independent call/operation limit failure.

The implementation increment adds the existing experiment's semantic execution entry: exact code/input/protocol/review bindings, complete balanced 12-assignment schedule, all-selected-profile qualification before semantic loading, fresh host/model-instance state, immutable original results and charged failures. Additional controls reject duplicate/biased schedules, a failed qualification matrix and a different profile despite the same model name. Token-repacking proof verifies one sampled budget survives repeated rendering while omitted evidence loses citation authority. **40 focused tests pass**, **65 nearest Workspace controls pass** (21.173 seconds), Ruff checks/format and whitespace pass. Product source/tests remain unchanged; no full/installed/hosted suite is claimed.

All three zero-generation synthetic preparations pass 12 shapes each at the intended 8192 points: maximum inputs Gemma12 22920, Qwen27 22658, E4B 22937, plus 8192 output reserve/256 margin within 32768. Retained six source-grounded reviewer obligations per case outside model input; exact actual source-file identities and capture limits are included. This is preparation, not interface qualification or semantic acceptance.

Real-case preparation attempt 1 correctly refused before prediction because its temporary load identifier differed from the profile-bound identifier. Preserved the failure and unloaded the owned instance. Corrected the runner/preparation to reuse the frozen identifier with a newly loaded instanceReference; strict identity validation and settings are unchanged. The correction is ordinary runner binding, not a model configuration retry or semantic-outcome tuning. Real-case preparation attempt 2 has a new retained directory and is in progress. Exact private artifacts reside under `/home/motafeq/.local/share/upgradepilot/investigator-runs/semantic-comparison-2026-10-18-budget-v1`; no new prediction has occurred at this implementation publication horizon.
