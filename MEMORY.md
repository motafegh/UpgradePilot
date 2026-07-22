# UpgradePilot Current Memory

**Last updated:** 2026-07-22  
**Purpose:** Concise project-local continuation. Source, tests, commands, outputs,
and the current environment remain the authority for actual behavior.

## Current responsibility

Manual end-to-end runtime simulation under
[`plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md),
using the dedicated [`product-simulation/`](product-simulation/) workspace.

The current responsibility is to manually perform and document the complete
intended UpgradePilot runtime on materially different real public dependency-
update cases before further product implementation.

M2-S03 is paused, not rejected. Its retained implementation plan is
[`plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md`](plans/M2_S03_EVIDENCE_REPORT_VERTICAL_SLICE_PLAN.md).
It may resume only after the simulation synthesis is reviewed and any required
corrections are explicitly approved.

M2-S02 is closed with a negative local-model extraction disposition. Its detailed
record is
[`working-memory/2026-07-22_M2-S02_llm-extraction-session.md`](working-memory/2026-07-22_M2-S02_llm-extraction-session.md).

## Verified current implementation

The repository currently provides:

- strict case identity and evidence contracts;
- attributed Python-support claim contracts with application-assigned
  `model_derived` authority and transformation identity;
- mechanical evidence grounding that checks evidence eligibility, exact unique
  quotation, version presence, and duplicate candidates;
- deterministic decision outcomes limited to `run_targeted_checks` or `abstain`;
- an LM Studio structured-output extractor retained for experiments;
- an input-risk detector and evaluator retained for experimental evidence;
- live semantic and decision-effect evaluators with preserved JSON artifacts.

The normal extraction orchestration is now:

```text
accepted release-note EvidenceItem
→ untrusted schema-constrained candidate attributed claims
→ mechanical source grounding
→ model-derived attributed claims
→ deterministic bounded decision
```

The normal service no longer requires the second-model risk detector. Mechanical
grounding no longer uses instruction phrases or Python-support semantic regexes
to manufacture model-evaluation passes. Contradictory source claims remain
visible for later conflict handling.

No current model has shell, filesystem, GitHub, credential, tool, mutation, or
merge authority. JSON Schema constrains output shape; it does not establish
semantic truth.

## M2-S02 final evidence

Complete live run, 14 cases per deployment:

| Local deployment | Correct candidate/grounded claims | Correct decision effects | Disposition |
|---|---:|---:|---|
| `gemma-4-e2b-it` | 9/14 | 11/14 | Rejected for normal extraction |
| `qwen3-4b-instruct-2507` | 8/14 | 10/14 | Rejected for normal extraction |

Focused repetition on six discriminating cases produced:

| Local deployment | Clean repetitions | Correct decision effects | Material result |
|---|---:|---:|---|
| `gemma-4-e2b-it` | 3/12 | 6/12 | Repeated false dropped claims changed abstention to targeted checks |
| `qwen3-4b-instruct-2507` | 0/12 | 4/12 | Repeated deprecation and instruction-shaped failures changed decisions |

Artifacts:

- `m2-s02-attributed-claim-decision-effects.json` — complete claim and
  decision-effect run;
- `m2-s02-attributed-claim-repeated-failures.json` — focused repeated failures;
- `m2-s02-input-risk-expanded-results.json` — expanded detector matrix;
- `m2-s02-input-risk-qwen-failures.json` — focused detector failures.

The non-zero evaluator exits are expected because scored cases failed. The
artifacts parsed successfully and are evidence of rejection, not failed test
execution.

## Adopted and rejected controls

Keep in the supported contracts:

- raw evidence preservation and strict schemas;
- exact source quotation and evidence identity;
- source attribution and transformation provenance;
- explicit model-derived authority;
- deterministic limits on permitted decision effects;
- explicit unresolved and degraded states.

Reject from normal M2 runtime:

- both tested local model deployments as the semantic extractor;
- the mandatory second-model input-risk gate;
- instruction/output phrase regexes in grounding;
- deprecation/future/continued-support regexes in grounding.

Retain the rejected implementations, cases, and outputs as experiment evidence.
Do not delete negative results or tune only to known failed wording.

## Evidence and truth boundary

```text
source observation
→ attributed source claim
→ later corroborated / contradicted / irrelevant / unresolved
→ bounded decision
```

Accepted release-note evidence means the source was recorded and is eligible for
processing. It does not make every source statement true. Grounding proves that
an extracted claim corresponds to cited source content; it does not independently
corroborate that claim. Package, repository, dependency-path, and CI evidence can
perform later corroboration when those sources are activated.

A false favorable model claim cannot currently justify a less cautious result.
A false dropped-support claim can create unnecessary targeted work, which is why
decision-effect tests—not JSON validity or candidate accuracy alone—drove model
rejection.

## Immediate continuation

1. select the first foundational real public dependency-update case;
2. create one complete scenario record from
   [`product-simulation/SCENARIO_EXECUTION_TEMPLATE.md`](product-simulation/SCENARIO_EXECUTION_TEMPLATE.md);
3. manually perform the whole intended UpgradePilot runtime from trigger and
   invocation through evidence investigation, decision support, report, user
   interaction, and retrospective;
4. update
   [`product-simulation/SCENARIO_COVERAGE.md`](product-simulation/SCENARIO_COVERAGE.md)
   only from actual case evidence;
5. progressively synthesize the operating model, inputs, evidence origins,
   purposes, data flow, user flow, failure behavior, outputs, and candidate
   methods;
6. use at least ten materially different real cases and continue beyond them
   when major uncertainty remains;
7. after synthesis, decide the smallest corrected implementation responsibility
   and whether M2-S03 should resume unchanged, be revised, or be replaced.

Do not implement product code, select permanent architecture, or resume M2-S03
while the manual simulation plan is current.

All lists in the simulation workspace are non-exhaustive starting prompts. Real
case evidence may add, split, reorder, remove, or redefine actors, inputs,
evidence, stages, methods, outputs, states, and diagrams.

## Ownership and assistance

- Ali identified that manually supplied semantics did not satisfy automated
  extraction and required real local-model testing.
- Ali required both Qwen and Gemma evaluation and challenged conclusions based on
  output shape, token counts, and adversarial wording.
- Ali identified the decisive difference between a source claim and corroborated
  truth, causing the runtime architecture and threat model to be corrected.
- Ali rejected narrow phrase/grammar fixes and required responsibility-level,
  whole-project planning.
- Ali identified that incremental implementation without a concrete complete
  runtime model was causing local rabbit holes and authorized the manual product
  simulation responsibility.
- The implementation, tests, evaluators, and records are substantially
  AI-generated under Ali's direction; independent ownership has not been claimed.

## Career boundary

Do not update Career for ordinary project progress. Ali explicitly initiates a
Career review for capability, workload, strategy, or durable program changes.

## Detailed evidence

Use current source/tests, the closed M2-S02 plan and working record, the paused
M2-S03 plan, the current manual simulation plan and scenario workspace,
evaluation artifacts, specifications, Git history, and actual command outputs.
Do not copy this continuation into stable entrypoints or Career.