# Investigator real-case Raw-vs-Structured semantic comparison — LbD cycle

**Date/horizon:** October 17, 2026, +03:30; A0 reconciled from `main@ce96280c4d271e63ad0b60db9dd1c1f8e635f71b`.
**Session status:** ACTIVE — A0 complete; A1 continuity/onboarding current at its normal stop gate.
**Responsibility:** freeze and verify the paired real-case Raw-vs-Structured semantic comparison over two exposed development cases and three selected deployments, then only after the pre-inference gates are satisfied attempt the admitted assignments, preserve immutable outcomes/failures/costs, perform source-to-claim semantic review and reach a bounded retain/reject/inconclusive disposition.
**Live owner:** [MEMORY.md](../MEMORY.md) alone owns current continuation.
**Controlling owners:** [Investigator integration/comparison plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md), explicitly amended by the [three-deployment semantic-comparison decision](../plans/INVESTIGATOR_SEMANTIC_COMPARISON_THREE_DEPLOYMENT_AMENDMENT_2026-10-17.md).
**Previous:** [deployment/model-interface D/E closure](2026-10-17_deployment-interface-D-reconciliation-and-E-entry.md).
**Procedural provenance:** `UP-SKILL:upgradepilot-learning-by-doing`; `UP-SKILL:upgradepilot-working-memory`.

## Phase status

| Phase | Status | Current meaning |
| --- | --- | --- |
| A0 | **DONE** | Reconciled live owners, previous closure, amendment, final deployment/interface evidence, durable common-input snapshot, current experiment contracts and semantic-review owner; initialized this one cycle record. |
| A1 | **CURRENT — STOP GATE** | Bring Ali from the closed deployment/interface responsibility to the exact successor entry state; preserve questions/challenges before A2. |
| A2 | PENDING | Orient the 12-assignment freeze/execution/review responsibility, important data/control/evidence flow, proof boundary, failure states and non-goals. |
| B | PENDING | Prepare/verify the successor freeze first; semantic inference remains forbidden until that freeze is complete and justified. Later execution is separately gated by the verified freeze. |
| Verification gate | PENDING | Must verify exact inputs/configuration/order/contracts/fit/review/accounting/retention and later the attempted comparison evidence. |
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

**Important successor configuration consequence:** Gemma12 and Qwen27 qualified with a 2048 synthetic generation cap, while the comparison plan/amendment carries an 8192 real-case allowance. Capacity-fit evidence showed the relevant synthetic/preflight shapes can fit an 8192 reserve inside 32768, but that is not the same as an observed 8192 real-case deployment/prediction configuration. The successor freeze must therefore make the intended 8192 case configuration explicit and obtain the required pre-inference fit/runtime correspondence evidence before semantic assignments. It may not silently call the old 2048 point and the new 8192 point “the same configuration.” E4B already used 8192 during qualification, but its actual real-case request shapes still require successor fit/correspondence checks.

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
- Gemma12/Qwen27 require an explicit 8192 case-allowance configuration/fit/correspondence disposition because their qualified synthetic calls used 2048;
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
- The specific 2048-versus-8192 consequence for Gemma12/Qwen27.

### A2 upcoming-responsibility topics

- Common case freeze → fresh assignment host/lineage → Raw/Structured capability boundary → complete stateless model request → strict tool/reference/report admission → immutable output/accounting → offline source-to-claim review → bounded disposition.
- How to choose/freeze all 12 IDs and a balanced serial order without outcome-dependent scheduling.
- Exact budget/accounting model: per-assignment ceilings versus aggregate ceilings, prior qualification spend kept separate, ceilings not targets.
- Real-case token/context/output fit and requested-versus-observed runtime correspondence.
- Semantic-review masking/source obligations and how reviewer evidence stays outside model input.
- Failure/refusal/no-rerun/withholding semantics and the line between experiment evidence and product authority.

### Expected result / proof boundary

Expected cycle output is one truthful frozen 12-assignment protocol followed, only after admission, by attempted results and semantic review sufficient for a **retain / reject / inconclusive development-pilot disposition**. One sample per case/treatment/deployment cannot establish stochastic reliability, intrinsic model ranking, general semantic superiority, maintainer usefulness, production adoption or action permission.

### Stop conditions / non-goals

Stop/reconcile before affected inference on input drift/unavailability, identity/configuration mismatch, unverified 8192 fit/correspondence, placeholder manifest fields, unequal evidence universes, protocol/order/budget changes, protected-review leakage or a required product-authority change. No cloud fallback, target execution/mutation, hidden-reasoning retention, extra model arm, multi-agent/critic topology, outcome-driven tuning or premature productization is admitted.

## A1 continuity packet — current gate

The successor begins from a **qualified delivery/interface mechanism, not a qualified semantic Investigator**. The real scientific question is now whether Structured native evidence improves evidence use/interpretation/uncertainty/stopping/recommendation quality relative to Raw navigation over the same evidence universe, with E4B adding the bounded smaller-deployment/resource question.

The immediate work is therefore not “run the models.” It is to make the comparison scientifically and operationally determinate before the first outcome exists: exact shared cases, exact three deployments, exact 12 assignments/order, exact contracts/budgets, actual real-case fit/configuration correspondence, review protocol, retention/accounting and no-rerun rules.

**A1 gate is intentionally open.** A2/B have not been started and no inference has been performed. Ali has the normal opportunity to challenge/correct this reconstructed current-state model before we orient the detailed freeze/execution flow.
