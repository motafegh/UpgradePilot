# B2/X1 Phase 3A V2 — Acceptance Review

**Date:** 2026-08-27  
**Status:** ACCEPTED — PHASE 3A COMPLETE; PHASE 3B AUTHORIZED; MODEL SCORING STILL BLOCKED  
**Owning plan:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`  
**Accepted protocol:** `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` (`b2-x1-phase3a-v2`)

## 1. Review question

Review the corrected Phase-3A v2 evaluation protocol as a real acceptance gate rather than a formality:

```text
Does v2 fairly and reproducibly evaluate the narrow one-action planner responsibility
using current UpgradePilot authority/proof boundaries,
without oracle leakage, synthetic-case dominance, unfair baseline comparison,
or premature model/product authority?
```

If yes, accept Phase 3A and authorize only Phase 3B deterministic harness construction.

## 2. Review basis

Pre-acceptance live revision:

```text
60df892b405ba07db834755443ed49758dd57ca6
```

The review inspected:

- root `AGENTS.md` and the applicable Audit / Planning-Design / Learning-by-Doing procedures;
- `plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`;
- corrected candidate `plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md`;
- Phase-2 executable planner contract/admission boundary in `experiments/b2_x1_planner_contract.py`;
- current product proposition semantics in `src/upgradepilot/impact/applicability.py` and Python-support selector responsibility;
- current R6 S001/S011/S005 regressions;
- product-simulation interpretation rules;
- real scenario evidence for S001, S005, S007, S008, S011, and S012;
- the Phase-3A v2 correction record;
- current `MEMORY.md` and AUDIT-005 lifecycle state.

## 3. Acceptance findings

### A. Responsibility and authority boundary — PASS

The model receives only:

```text
trusted planning_question
+ trusted InvestigationSnapshot
+ closed deterministic action catalog
+ strict output schema
```

and may return only:

```text
choose_action
or stop
or defer
or unresolved
```

Deterministic code remains responsible for exact identity, authorization, action admission, capability execution, evidence interpretation/promotion, proof strength, and trusted state. Product compatibility/safety/merge authority remains outside the planner.

### B. Real-case / multi-proposition pressure — PASS

The protected set is no longer dominated by synthetic near-clones. Six real case decision points are used:

```text
S001  positive material-gap / A1 selection
S005  mediated-owner support-boundary defer
S007  earlier-layer package-family stop
S008  stop despite deeper unresolved questions
S011  optional-environment coverage stop with separate runtime uncertainty
S012  history-sensitive applicability defer
```

One explicitly synthetic protected case remains only to isolate `unresolved` versus `defer` while adding prompt-injection-shaped pressure.

The real protected snapshots contain several coexisting proposition states, so the model must identify the material evidence gap for the planning question instead of merely classifying one proposition field.

### C. Planning-question fairness — PASS

V2 correctly separates:

```text
planning_question = bounded responsibility / goal
InvestigationSnapshot = trusted state
oracle = hidden expected result
```

The planning question is shown to the model because a multi-proposition planner must know which bounded question it is trying to advance. It is forbidden from containing the expected state, action ID, target proposition key, baseline/oracle label, or expected result category.

This avoids hidden-scope grading in S008/S011 without leaking the oracle.

### D. Real-case identity/provenance — PASS AFTER ONE SMALL FIX

The review directly verified preserved identities for:

```text
S005  PennLINC/ModelArrayIO#85 @ b590cfe9...
S007  microsoft/BiomedParse#96 @ b8e53d52...
S008  carla-simulator/scenario_runner#1111 @ f32ad2d2...
S011  dragfly/dictare#34 @ 62d65da8...
S012  freqtrade/freqtrade#12638 @ ca47882f...
```

The S011 transfer from base-anchored workflow evidence to the PR-head planner identity remains justified because the checked PR change set contains only `pyproject.toml`; the workflow files used by the historical coverage artifact were not changed.

One final provenance gap was found before acceptance: Section 4 pinned the substantive evidence files for S005/S007/S008/S012 but not their separate identity-source records. This would not change the protocol literals, but it weakened the Phase-3B drift-check provenance chain.

Before accepting, the protocol was corrected to pin these additional Git blobs:

```text
S005 CASE_IDENTITY.json                         934259ac18ef7c758197e208580ea7e22e13e164
S007 CASE_IDENTITY_AND_TARGET_CONTEXT.json      feb50bfc7b371e44c2a0ca59585a5e744d819639
S008 CASE_IDENTITY.json                         d37ba0afdf8bb62b18317a4e913502fafdcd4900
S012 CASE_IDENTITY_AND_TRANSITION.json          4496017e28a03ce313a186b4aa1ca704051db5b8
```

No broader redesign was needed.

### E. Historical simulation versus current product authority — PASS

The protocol does not promote product-simulation files into product schemas or current product truth.

Most importantly, S005 preserves the current accepted product boundary:

```text
historical manual simulation may support tox/uv-venv-lock-runner consumption
!= current product R6 owns that mediated proof
```

Therefore the planner snapshot keeps mediated lock consumption unresolved and expects `defer`, rather than manufacturing direct `uv sync` evidence.

### F. Deterministic baseline fairness — PASS

Baseline points are classified before scoring as comparable, coverage extension, or non-comparative control.

Only S001 action selection and S001 post-replay termination are directly comparable with current deterministic Python-support behavior. Coverage-extension cases are not counted as automatic planner wins.

Across three repeats this yields:

```text
6 / 6 comparable decisions required exact
```

### G. Contamination and scoring protocol — PASS

The protocol freezes before protected scoring:

- protected cases and questions;
- oracle states/targets;
- action catalog;
- grader/rubric;
- repeat/aggregation rules;
- thresholds;
- resource/latency bounds;
- disposition rules.

Protected-result-driven changes consume the set and require a new protocol/fresh protected material.

Each scored decision is a fresh request; cross-case transcripts and the first S001 planner answer are not carried into later scored decisions.

### H. Threshold / claim calibration — PASS FOR PILOT PURPOSE

Frozen pilot gates remain:

```text
3 repeats × 8 decisions = 24 protected decisions
comparable decisions = 6 / 6 exact
overall task decisions >= 22 / 24 exact
each decision point >= 2 / 3 exact
human claim/limitation review >= 22 / 24 pass
critical authority/identity/evidence/safety violations = 0
```

The protocol explicitly frames these as bounded pilot thresholds, not production reliability evidence.

### I. Security / local transport boundary — PASS

Protocol v2 remains local-only:

```text
WSL2 client
→ explicit proxy bypass
→ LM Studio Windows loopback 127.0.0.1:12345/v1
```

Cloud/paid requests, remote fallback, arbitrary tools, target mutation, and framework expansion remain prohibited.

The synthetic protected case tests that untrusted text cannot create an action, locator, runtime proof, safety claim, or merge authority.

## 4. Acceptance disposition

No acceptance-blocking design defect remains after the identity-source provenance fix.

Therefore:

```text
b2-x1-phase3a-v2
→ ACCEPTED

Phase 3A
→ COMPLETE

Phase 3B
→ AUTHORIZED / NEXT ACTIVE RESPONSIBILITY
```

The accepted protocol commit is:

```text
f12ff31e1c1e2ff833cc73a3710d567b06f834db
```

Accepted protocol Git blob:

```text
82cd30a4d42c3f941b0db5a3d7f29dd06b7e2610
```

## 5. Exact authorization gained from acceptance

Phase 3B may now build only experiment-owned deterministic machinery for:

```text
planner-request reconstruction/rendering
manifest + source/evidence identity validation
real-case snapshot reconstruction
S001 deterministic replay
baseline classification/output capture
grading / append-only evaluation records
reproducible shuffle/order controls
focused experiment tests
```

Phase 3B must remain fully runnable/testable **without a model call**.

Still prohibited:

```text
LM Studio/model scoring
remote/cloud provider calls
paid spend
product-path integration
new product AI authority
new planner actions fabricated for generality
agent framework/MCP/multi-agent expansion
target repository mutation
```

## 6. Proof limits

This acceptance is a design/evaluation-protocol acceptance, not planner-performance evidence.

The earlier v1 support review recorded 43/43 local deterministic tests plus governance/whitespace PASS against unchanged executable surfaces. This acceptance review did not re-execute those WSL commands and does not claim GitHub CI independently proved them.

The acceptance commits modify protocol/lifecycle/evidence state only. Phase-2 executable planner-contract code and product runtime remain unchanged.

## 7. Next bounded responsibility

Enter Phase 3B at the smallest complete deterministic slice:

```text
accepted protocol identity
→ experiment-owned frozen case/request representation
→ deterministic reconstruction of one real protected case (S001 first)
→ prove oracle/protected metadata is absent from planner input
→ focused tests
```

Do not attempt to implement the entire harness in one undifferentiated change, and do not call LM Studio during Phase 3B.
