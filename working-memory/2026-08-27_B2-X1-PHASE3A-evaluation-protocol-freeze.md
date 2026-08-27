# B2/X1 Phase 3A Evaluation-Protocol Freeze

**Date:** 2026-08-27
**Status:** PHASE-3A DESIGN FROZEN — READY FOR ALI ACCEPTANCE; PHASE 3B BLOCKED
**Owning checkpoint:** `../plans/B2_AGENTIC_INVESTIGATION_ORCHESTRATION_EVALUATION_PLAN.md`
**Frozen protocol candidate:** `../plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md`

## 1. Responsibility completed

Phase 3A converted the corrected evaluation requirements into one exact, reviewable protocol
candidate before harness implementation or model/provider scoring.

The work inspected the Phase-2 experiment contract/tests, the current Python-support selector,
the Phase-1 capability inventory, the current S001/S011/S005 regressions, and the preserved
historical case evidence. No product or experiment executable file changed and no provider or
model was called.

## 2. Material decisions

### Narrow claim branch

Only `acquire_exact_target_python_declaration` is an independently justified executable
planner action. Existing CI/upstream chains remain fixed orchestration clusters. The protocol
therefore evaluates action-vs-stop/defer/unresolved behavior and makes general
adaptive-planner `ADOPT` unavailable.

### Seven families and one replay turn

The protocol freezes:

1. S001 positive membership/CI;
2. S011 affected optional environment not selected;
3. S005 mediated lock-consumption support gap;
4. Python-support action selection;
5. correct stop after attempt/budget exhaustion;
6. prompt-injection-shaped untrusted evidence;
7. explicit unresolved/abstention control;
8. a second protected turn after deterministic action-problem replay.

Each family has a development instance and a distinct protected instance or variation. The
protected set has eight scored decisions repeated three times, for 24 protected calls.

### Honest baseline comparison

Only the current Python-support selector/action and stop/non-reselection decision points are
directly comparable. S001/S011/S005 generic planner dispositions, prompt-injection exposure,
and generic unresolved abstention are coverage-extension results. Baseline absence cannot be
counted as a win.

### Precommitted scoring and cost

The protocol freezes zero-tolerance authority/identity/evidence/safety gates, 9/9 exact
comparable decisions, at least 22/24 exact protected decisions, at least 22/24 human
claim-rubric passes, per-family minimums, three repeats, and token/latency/request ceilings.

### Contamination rule

Any protected-result-driven prompt/model/schema/catalog/renderer/grader/threshold change
consumes the whole protected set. No replacement set exists in v1, so the checkpoint must
defer until a new version freezes fresh protected instances.

## 3. Why the protocol is proportionate

The protocol is stricter than an ordinary smoke test because it may later influence a
security-sensitive product-adoption decision. It remains bounded:

- fourteen initial snapshots, not a broad benchmark;
- seven development instances and seven protected instances;
- one real action, one replayed result family, and explicit no-tool states;
- deterministic schema/admission/replay controls plus bounded human semantic review;
- no framework, multi-agent system, generic tool layer, or product integration.

## 4. Proof and limitations

Validation after the protocol freeze:

```text
Phase-2 planner contract/admission tests                  23 / 23 PASS
Python-support selector/state tests                       11 / 11 PASS
R6 S001/S011/S005 source-to-workflow regressions           9 / 9 PASS
combined focused deterministic suite                      43 / 43 PASS
agent-governance doctor                                   PASS
tracked + new-file whitespace checks                      PASS
executable files changed                                  NONE
provider/model calls                                      NONE
```

The focused suite establishes that the current contract, exact target-action selector,
no-reselection behavior, S001 positive witness, S011 non-selection, and S005 mediated-support
boundary still behave as the protocol assumes. It does not execute the planned manifest,
replay, renderer, grader, protected repetitions, or a model.

This Phase-3A slice proves only that a complete candidate protocol/oracle now exists with no
result-dependent rule intentionally left open. It does not prove:

- Ali has accepted the consequential thresholds/claim branch;
- Phase 3B can implement the design cleanly;
- any provider/model can satisfy the protocol;
- any exact LM Studio model/configuration is selected or proven suitable;
- the planner is valuable, reliable, safe, or adoptable;
- the purpose-built protected variations represent production prevalence.

## 5. Post-freeze local-only direction

Ali selected LM Studio and locally hosted LLMs for this checkpoint. Protocol v1 was therefore
narrowed before acceptance to:

```text
LM Studio on the accepted 127.0.0.1:12345 loopback boundary only
external/cloud provider requests = 0
paid-provider ceiling = USD 0.00
no ambient-proxy or remote fallback
```

This selects the transport class, not the exact planner model. Exact model identity,
quantization/deployment, prompt, sampling configuration, and current LM Studio availability
remain later evidence-backed choices. The existing ADR-0006 model is a candidate/control, not
automatically accepted for planning.

## 6. Prior LM Studio evidence reconciliation

The earlier LM Studio records and the stable runtime owner were reconciled after the local-only
direction:

- `ENVIRONMENT.md` still owns the accepted WSL2-to-Windows loopback topology, port 12345,
  OpenAI-compatible `/v1` base, and explicit proxy-bypass requirement;
- ADR-0006 and its live proof establish `gemma-4-e4b-it-ud` Q4_K_XL at 4096 context and
  parallelism 1 as a real bounded semantic-extraction deployment, including temperature 0,
  seed 0, disabled semantic retries, and strict structured output;
- the proxy-contamination diagnosis proves that ambient `HTTP_PROXY`/`HTTPS_PROXY` state can
  intercept loopback despite permissive `NO_PROXY`, so Phase 4 must use an explicit no-proxy
  client boundary rather than infer locality from the URL alone;
- the 2026-07-28 inventory and historical GPU/load measurements are not current availability
  proof. Phase 4 must refresh LM Studio version, installed and loaded models, exact deployment
  identity, configuration, and pre/post-load GPU state before the first model call;
- no model download, update, JIT substitution, or cloud fallback is admitted by this protocol.

Consequently, the prior Gemma deployment becomes the first planning **candidate/control** only
if still locally available. It does not become the selected planner until it passes the new
planning-specific development smoke and the complete configuration is frozen.

## 7. Acceptance and continuation

Phase 3B remains blocked until Ali explicitly accepts
`plans/B2_X1_PHASE3_EVALUATION_PROTOCOL.md` with the understanding summarized in its Section
11. Acceptance authorizes only the deterministic experiment harness/replay/grading build and
focused tests. It does not authorize model/provider scoring, paid spend, product integration,
or target mutation.
