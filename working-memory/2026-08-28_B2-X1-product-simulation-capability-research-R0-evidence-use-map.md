# B2/X1 Product-Simulation Capability Research — R0 Evidence-Use / Contamination Map

**Date:** 2026-08-28  
**Status:** R0 COMPLETE — research branch re-anchored; initial case-use ledger established; transfer evidence reclassified as capability-research pressure  
**Plan:** `../plans/B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md`  
**Main-side request:** `2026-08-28_B2-X1-product-simulation-capability-research-handoff.md`  
**Evaluated main revision at R0 start:** `14ba589de18aa72b0f9098d5154cc722c494c256`  
**Research branch:** `product-simulation/2026-08-28-main-support-lab`

## 1. R0 question

> Can the delegated capability research proceed from current main without losing branch-owned evidence or confusing historically/design-exposed cases with future holdout material?

R0 is a readiness/evidence-lineage slice. It does not promote any planner capability, screen new public cases, freeze v3, or change product/experiment behavior.

---

## 2. Current-main / branch reconciliation

Before R0, main had advanced through the evidence-first E1–E5 exploration and strict-design reconciliation.

The product-simulation branch was merged forward to that current main while preserving only branch-owned simulation/research assets. At R0 start the branch comparison was:

```text
base main: 14ba589de18aa72b0f9098d5154cc722c494c256
branch behind main: 0
branch-only content:
- prior product-simulation transfer evidence
- B2_X1_PRODUCT_SIMULATION_CAPABILITY_RESEARCH_PLAN.md
```

No stale branch copy of `MEMORY.md`, main-owned experiments, or product source was retained as a conflicting owner.

No target repository was mutated, commented on, rerun, approved, closed, or merged during R0.

---

## 3. Evidence-use rule discovered in R0

The phrase **"not used in E1–E5" does not mean "untouched."**

S001–S012 are all historical product-simulation cases with substantial preserved reasoning/evidence. Several additionally entered v2 or the later E1–E5 planner experiments.

Therefore R0 tracks two different exposure dimensions:

```text
HISTORICAL / DESIGN EXPOSURE
Was the case already deeply analyzed as simulation evidence or used to shape UpgradePilot reasoning/design?

PLANNER / EVALUATION EXPOSURE
Was the case additionally used in v2, E1–E5 model-result-driven work, or the current B2/X1 transfer evaluations?
```

For future v3 purposes these dimensions must not be collapsed.

A case can be:

```text
not used by the latest model experiment
AND
still not be an untouched holdout
```

This distinction is especially important for S002, S003, S009, and S010.

---

## 4. Initial S001–S012 case-use ledger

`historical_consumed` here means the case is already materially known/design-exposed and must not be described by this research as untouched final v3 protected evidence. It remains fully usable for capability discovery, mechanism comparison, deterministic-baseline analysis, and counterexamples.

| Case | Frozen/public anchor | Historical/design exposure | Planner/eval exposure relevant to B2/X1 | R0 classification | Research use after R0 |
|---|---|---|---|---|---|
| **S001** | `pydantic/pydantic#13432`; accepted planner head `aa2dc024...`; Soup Sieve 2.6→2.8.4 simulation | deep D1 simulation + later product transfer | v2 protected action/replay; E2 state-origin; E3 minimally constrained planner; E4 action/schema/admission; transfer inventory | `historical_consumed` | use freely for action/precondition/replay patterns; never call fresh holdout |
| **S002** | `Aidan-Wallace/kubernetes-dashboard-token-api#20 @ 39150813...`; HTTPX 0.27.2→0.28.1 | deep retrospective simulation; adapter path + skipped relevant tests + targeted-check follow-up | not v2 protected; not E1–E5 planner-result tuning | `historical_consumed` | **high-value R1/R2 design research** because latest planner tuning did not consume it; not untouched v3 material |
| **S003** | `xayanide/event-handler-loader#341 @ f6d6daba...`; TypeScript 5.9.3→7.0.2 | deep prospective simulation; failing install + peer-conflict attribution | not v2 protected; not E1–E5 planner-result tuning | `historical_consumed` | useful contrast for failure attribution / installability / early deterministic closure; note non-Python/ecosystem boundary before planner promotion |
| **S004** | `googlefonts/glyphsLib#1145 @ f3cda8a9...`; pytest 9.0.2→9.0.3 | full stopping-control simulation | E5 `d-s004-stop` model probe; prior development fixture | `historical_consumed` | use as known STOP/baseline-sufficient pattern only |
| **S005** | `PennLINC/ModelArrayIO#85 @ b590cfe9...`; pytest 9.0.3→9.1.1 | deep action-changing simulation | v2 protected DEFER representation under current product boundary; no-tool transfer evaluation | `historical_consumed` | use for mediated consumption / current-product-vs-historical-proof boundary; not final protected material |
| **S006** | `eduardoklosowski/qldebugger#27 @ a454b47b...`; Pydantic V1/V2 validator behavior | real-derived controlled simulation with known withheld-test oracle; evaluator had oracle exposure | E5 `d-s006-defer`; no-tool transfer evaluation | `historical_consumed` | strong targeted-check / information-value research case; never use as blind-discovery proof |
| **S007** | `microsoft/BiomedParse#96 @ b8e53d52...`; Torch/CUDA family | deep real simulation; static evidence pruned planned resolver | v2 protected STOP; branch pre-execution staleness evaluation | `historical_consumed` | strong stale-plan / information-value / resolver-pruning design evidence |
| **S008** | `carla-simulator/scenario_runner#1111 @ f32ad2d2...`; OpenCV/Python-3.6 artifact fallback | deep real artifact-serviceability simulation | v2 protected STOP; no-tool transfer evaluation | `historical_consumed` | use for question ownership, static sufficiency, deeper-unresolved STOP pattern |
| **S009** | `jamisonhburks/cgm-chronobiological-features#12 @ 9065f883...`; pandas 2.2.2→3.0.5 | deep real repository-purpose/provenance simulation | not v2 protected; not E1–E5 planner-result tuning; referenced in branch transfer inventory as outside prior narrow X1 claim | `historical_consumed` | **high-value R1/R2 research** for context/provenance prioritization; do not treat context as technical compatibility proof |
| **S010** | `invaderDMG/podcast-script#36 @ 327196a5...`; NumPy requirement broadening | deep real multi-mechanism discovery simulation | not v2 protected; not E1–E5 planner-result tuning; referenced in branch transfer inventory as outside prior narrow X1 claim | `historical_consumed` | **high-value R1/R2 research** for discovery breadth / mechanism separation; may represent a separate semantic-discovery responsibility rather than planner action |
| **S011** | `dragfly/dictare#34 @ 62d65da8...`; NumPy in `mlx` optional extra | deep real optional-environment/CI-coverage simulation | v2 protected STOP; no-tool transfer evaluation | `historical_consumed` | use for mediated environment/CI consumption and adjacent-unresolved STOP pressure |
| **S012** | `freqtrade/freqtrade#12638 @ ca47882f...`; scikit-learn 1.7.2→1.8.0 | deep real persisted-artifact provenance simulation | v2 protected DEFER; no-tool transfer evaluation | `historical_consumed` | use for history-sensitive applicability / unavailable deployment provenance / DEFER pressure |

### R0 interpretation of S002 / S003 / S009 / S010

Main's handoff correctly identifies these four as **not consumed by v2 protected scoring or E1–E5 model-result tuning**.

That is valuable because they can pressure capability hypotheses without merely replaying the exact E3–E5 training path.

However, their own simulation artifacts already contain deep investigation, conclusions, and expected reasoning. Therefore this research will not call them `reserved_holdout_candidate` or untouched v3 evidence.

They are best treated as:

```text
historically known
+
not latest-planner-tuned
→ strong capability/design research material
```

---

## 5. Synthetic / development control ledger

These controls are calibration/evidence artifacts, not future holdouts.

| Control | Exposure | R0 classification / rule |
|---|---|---|
| `d-a1-smoke` | deliberately constructed positive A1 development fixture with known expected action | `historical_consumed`; calibration only |
| `d-s004-stop` | real S004-derived development STOP fixture; executed in E5 | `historical_consumed` |
| `d-s006-defer` | S006-derived development DEFER fixture; executed in E5 | `historical_consumed` |
| `d-conflict` | explicitly synthetic conflicted-state UNRESOLVED case; executed in E5 | `historical_consumed` |
| v2 synthetic unresolved / prompt-injection control | accepted protected v2 material with explicit oracle | `historical_consumed`; v2 protected set is consumed for reconciled candidate final scoring |
| E1 negation / future-drop / instruction-shaped support-drop probes | purpose-built semantic-extractor controls; live model outcomes observed | `historical_consumed` for semantic-boundary research; not planner holdouts |
| legacy repeat/budget development controls from v2 | deliberately designed around known semantics/oracles | development/calibration evidence only; never fresh holdout material |

---

## 6. Holdout policy after R0

R0 intentionally assigns **no** `reserved_holdout_candidate`.

Reason:

```text
capability hypotheses are not yet narrowed
→ random holdout selection now could reserve cases irrelevant to the eventual planner claim
→ or force later design around the cases we happened to reserve
```

Holdout candidates should first appear during targeted R3 discovery, after R1/R2 identify what capability/planner-value uncertainty fresh cases must discriminate.

When R3 finds a plausible holdout:

1. record only identity/basic suitability needed for screening;
2. record exactly what was viewed;
3. stop before material mechanism/oracle analysis;
4. mark `reserved_holdout_candidate` only as a research-side preservation status;
5. leave actual protected admission/freeze to main's later v3 owner.

If deeper investigation becomes necessary for capability design, reclassify it to `design_research_used` **before** using the result.

---

## 7. Existing branch transfer evidence — new role

The branch-owned transfer assets remain valid historical discovery evidence:

- `product-simulation/B2_X1_MODEL_READY_TRANSFER_PRESSURE_INVENTORY_2026-08-28.md`
- `product-simulation/b2-x1-no-tool-disposition-transfer/README.md`
- `product-simulation/b2-x1-pre-execution-action-staleness/README.md`
- `product-simulation/b2-x1-action-failure-retry-boundary/README.md`
- `product-simulation/B2_X1_TRANSFER_EVALUATIONS_INDEX_2026-08-28.md`

Their role is now:

```text
NOT an ordered queue of next implementation/evaluation tasks

INSTEAD
cross-cutting pressure dimensions for richer capability candidates
```

Examples:

```text
candidate has several actions
→ can one become stale before execution?

one attempted action fails
→ was it a typed domain result or transient acquisition failure?

adjacent uncertainty remains
→ should planner still STOP for the bounded question?

useful outside capability exists
→ should planner DEFER rather than fabricate an action?
```

No existing transfer file is deleted or rewritten to pretend it was originally created for the new capability-growth route.

---

## 8. R0 findings

### R0-F1 — all numbered historical cases are design-exposed

**CONFIRMED.**

S001–S012 all have substantial preserved simulation analysis. This research must not label any of them an untouched holdout merely because some were absent from v2/E1–E5.

### R0-F2 — latest planner-tuning exposure is uneven

**CONFIRMED.**

The strongest non-E1–E5/v2 cases for immediate capability research are S002, S003, S009, and S010.

This does not automatically make them good planner cases; R1/R2 must still test real capability responsibility and deterministic-baseline sufficiency.

### R0-F3 — future protected evidence should normally come from new targeted discovery

**SUPPORTED RECOMMENDATION.**

Given the historical exposure of S001–S012 and consumed v2/E1–E5 material, the cleanest path to a genuinely fresh v3 protected set is likely new real cases discovered after the planner responsibility is narrowed.

This is not a v3 freeze decision.

### R0-F4 — existing transfer work remains useful but should not control sequence

**CONFIRMED.**

No-tool semantics, stale-plan revalidation, and failure/retry ownership are now evaluation lenses to apply to real richer action/state candidates, not reasons to keep extending the earlier one-action planner in isolation.

### R0-F5 — no R0 environment/tool blocker

**CONFIRMED for this repository-inspection slice.**

R0 required only GitHub/repository evidence. No local WSL/LM Studio execution was needed and no new runtime claim was made.

---

## 9. R0 pass / proof limits

R0 pass conditions are satisfied at the dated evidence level:

- branch began the substantive slice 0 commits behind current main;
- delegated capability-research responsibility is explicit;
- product-simulation governance permits this discovery work;
- S001–S012 and synthetic-control exposure is mapped;
- historical exposure is separated from latest planner/evaluation exposure;
- existing transfer assets are preserved and reinterpreted without historical rewriting;
- no holdout is prematurely frozen;
- no product source, experiment contract, v2 protocol, or target repository was modified.

R0 does **not** prove:

- any second action/capability is justified;
- any historical case should become v3 evidence;
- S002/S003/S009/S010 are suitable planner cases;
- a fresh holdout exists;
- the model can handle multi-action planning;
- product integration is justified.

Those belong to later research stages.

---

## 10. Dated handoff implication

If `MEMORY.md` continues to select the delegated capability-research route, this R0 evidence permits the plan to enter **R1 capability-responsibility inventory** without repeating case-contamination analysis.

R1 should begin from recurring investigation responsibilities and current owners—not from a requirement to promote S002/S003/S009/S010 or to invent a second planner action.
