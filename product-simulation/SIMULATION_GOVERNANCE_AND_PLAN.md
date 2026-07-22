# Product Simulation Governance and Plan

**Status:** Controlling local governance and execution plan  
**Owner:** Ali Rajabi  
**Scope:** Everything under `product-simulation/`  
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)

## 1. Authority

This plan controls how product-simulation work is selected, performed, represented,
stopped, reviewed, synthesized, and completed.

Local authority order:

1. external safety, law, privacy, credential, permission, and platform limits;
2. Ali's explicit current instruction;
3. [`AGENTS.md`](AGENTS.md);
4. this plan;
5. [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md);
6. [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md);
7. current synthesis, active requirements, coverage, and scenario bundle;
8. scenario template and other project-local records.

The stable mission and public-Python product boundary remain controlled by the
project charter. Cross-ecosystem cases may test transferable responsibilities; they
do not expand supported scope.

## 2. Purpose

Product simulation discovers the operating, artifact, stopping, and automation model
before implementation responsibility, schemas, persistence, architecture, or methods
are frozen.

It answers:

1. What work must UpgradePilot perform to support a bounded maintainer decision?
2. What durable state must be created, preserved, compared, replayed, rendered,
   reviewed, stopped, and superseded?
3. When is current evidence sufficient, and when does deeper investigation add
   material value?
4. Which responsibilities appear deterministic, tool-assisted, model-dependent,
   human-controlled, or unsuitable?

Narrative-only cases are insufficient.

## 3. Open runtime

Each case challenges an open-world flow:

```text
real dependency-update event
→ invocation
→ exact identity discovery and freeze
→ material operations and acquisition attempts
→ raw evidence capture or durable reference
→ evidence records and states
→ claims and interpretations
→ findings, contradictions, and unresolved questions
→ transparent baseline
→ bounded decision
→ machine and human reports
→ action, follow-up, rerun, and supersession
→ review, ownership, cost, stopping, and synthesis
```

Stages may be added, split, reordered, skipped, repeated, activated conditionally,
or stopped when evidence requires it.

## 4. Complete manual-system rule

Ali and the AI assistant act as the intended system during simulation.

Do not bypass a future responsibility by supplying its semantic answer as an
unexplained starting value. Manual interpretation is allowed, but actor, input,
method, uncertainty, and downstream authority must remain explicit.

## 5. Method freedom and non-admission

Any lawful, safe, accessible, materially useful method may be used, including public
acquisition, package/repository inspection, local checkouts, dependency resolution,
static or dynamic analysis, tests, containers, temporary data stores, scripts,
notebooks, models, LLMs, agents, graphs, and human review.

Record material method use:

- responsibility and question;
- selection reason;
- inputs, source/tool/configuration, and environment;
- outputs, failures, side effects, and cost where material;
- what the result establishes and does not establish;
- evidence required before supported-product adoption.

Simulation use is not architecture or method approval.

## 6. Scenario state

Default logical organization:

```text
scenarios/<scenario-id>/
├── README.md
├── CASE.md
└── artifacts/
    ├── RUN_MANIFEST.json
    ├── INVOCATION.json
    ├── CASE_IDENTITY.json
    ├── OPERATION_EVENTS.jsonl
    ├── EVIDENCE_ITEMS.jsonl
    ├── CLAIMS_AND_INTERPRETATIONS.jsonl
    ├── FINDINGS.json
    ├── BASELINE_RESULT.json
    ├── DECISION.json
    ├── MACHINE_REPORT.json
    ├── HUMAN_REPORT.md
    ├── FOLLOW_UP_STATE.json
    ├── REVIEW_AND_OWNERSHIP.json
    ├── raw/
    └── checks/
```

Logical responsibilities are required. Physical files and fields remain illustrative
and non-binding.

Conditional extensions activate only when needed:

- `CHECK_EXECUTIONS.jsonl` for repeated, comparative, rerun, matrix, or
  local-versus-CI execution evidence;
- `FAILURE_ATTRIBUTION.json` when failing evidence has competing causes;
- `STOPPING_EVALUATION.json` when sufficiency, stage activation, overreach, or
  investigation cost is a material question;
- other comparison, environment, dependency, or diagnostic artifacts only when they
  add non-duplicative value.

Separate dependency-update assessment and PR action remain a candidate decision
shape. Activate the split only when evidence supports distinct answers.

## 7. Narrative versus state

`CASE.md` is the complete human-auditable story. The artifact bundle is simulated
runtime state. Neither substitutes for the other.

Machine artifacts must identify themselves as manual simulation and must not imply
that exact fields are accepted production contracts.

## 8. Progressive materialization

### Candidate screening

Preserve selection criteria, screened candidates, and material rejection reasons
before assigning a run identity.

### Selected, frozen, and baseline executed

Create navigation/live state, manifest, invocation, exact identity, initial
operations/review state, explicit questions and stop/switch conditions, and the
restricted baseline.

### Investigation

Append operations and evidence after material acquisition, failure, method switch,
new interpretation, or finding. Preserve raw/check outputs, superseded states,
current question, and next action.

### Action-change, divergence, or stopping assessment

State which evidence changes or confirms the baseline, whether dependency and PR
decisions differ, which conditional stages activated or remained inactive, and why
the investigation continues or stops.

### Decision and reports

Complete findings, decision, reports, follow-up, transitions, baseline comparison,
and review state.

### Validation and synthesis

Run a declared validation profile; preserve method, result, degradation, and proof
limits; update coverage and synthesis; record Ali review as complete or pending.

Natural durable checkpoints are required. One commit per operation is not.

## 9. Evidence, lineage, and honesty

Use the smallest preservation strategy retaining decision, audit, replay, and
diagnostic value:

- full bounded capture when lawful and necessary;
- bounded excerpt without changing meaning;
- immutable/recoverable exact reference;
- explicit non-preservation for inaccessible, expired, private, secret, excessive,
  or unrecoverable data.

Never invent missing output or diagnostic details.

Backward traversal should remain possible:

```text
report statement
→ decision reason
→ finding or limitation
→ claim or interpretation
→ evidence
→ operation
→ raw/reference source
→ frozen identity
```

Observation does not grant truth, relevance, or decision authority automatically.

## 10. Baseline, authority, cost, and stopping

Execute the current transparent baseline before admitting full-investigation
evidence.

Compare:

- action;
- reasons and authority;
- uncertainty;
- targeted next action;
- failure behavior;
- acquisition/reasoning cost;
- user value;
- whether the baseline was wrong, weaker, sufficient, unresolved, or the full
  investigation overreached.

Do not modify the baseline during an active case or force a thesis class.

After the baseline, identify its authority-critical assumptions and the smallest
question that could validate or reject them. Define stop/switch conditions before
deep investigation where practical.

Stop when additional work no longer changes the decision, material uncertainty,
actionability, product model, or evaluation conclusion. Inactive conditional stages
and the reason for non-activation are valid runtime state.

## 11. Failure and decision divergence

When a PR has failing evidence, distinguish:

- `update_caused`;
- `pre_existing`;
- `unrelated`;
- `flaky`;
- `environmental`;
- `mixed`;
- `unresolved`.

A red status alone is not causal evidence.

When supported, answer separately:

```text
dependency_update_assessment
repository_or_pr_action
```

The dependency may be acceptable while the PR remains blocked, or the PR may be
green while the dependency requires a stronger action because relevant checks were
not exercised.

## 12. Review and ownership

Track separately:

- execution status;
- factual review;
- Ali review;
- external or behavioral confirmation;
- AI assistance;
- Ali-owned capability at an explicit depth.

AI-produced completeness and historical merge state are not correctness or
capability proof.

## 13. Cross-case classification

After each case, classify material observations as:

- repeated stable candidate;
- conditional responsibility;
- one-case observation;
- contradicted assumption;
- unresolved;
- outside product boundary.

Classify automation feasibility as:

- deterministically automatable;
- tool-assisted with interpretation;
- model-dependent;
- human-review required;
- blocked by inaccessible evidence;
- not yet tested;
- unsuitable.

Coverage owns compact status; focused synthesis owns detailed reasoning.

## 14. Case selection

Select a case because it resolves a material planning uncertainty.

Do not select merely because it is easy, complex, available, similar, or likely to
support the thesis. Case count is not a completion gate.

Prefer supported-boundary Python Dependabot cases when the same uncertainty can be
tested there.

## 15. Completion

A scenario is complete only when:

- the real event and exact identity are clear;
- the runtime reaches a justified stop;
- narrative and required logical state exist or are explicitly unavailable/not
  applicable;
- JSON/JSONL parse and IDs/references resolve;
- provenance, evidence states, failures, supersession, contradiction, and
  uncertainty remain visible;
- baseline/full comparison and material cost are recorded;
- decisions and reports trace to evidence;
- follow-up, rerun, recovery, and new-boundary transitions exist;
- review and ownership states are explicit;
- coverage and synthesis are updated;
- no unsupported safety, correctness, automation, or capability claim is made.

Artifact and case counts are not quality metrics.

## 16. Current D1 sequence after S004

Completed evidence:

- S001 — retrospective Python transitive docs/advisory case;
- S002 — retrospective Python adapter/partial-green-CI case;
- S003 — prospective failing-install/peer-conflict transfer case;
- S004 — prospective Python baseline-sufficient early-stop control.

Current authorized sequence:

1. Screen and select S005 under
   [`S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md`](S005_ACTION_CHANGE_OR_DIVERGENCE_REQUIREMENTS.md).
2. Prefer a public Python Dependabot case where:
   - the baseline broad action is changed by full evidence; or
   - dependency assessment and PR action genuinely diverge.
3. Execute S005 prospectively and preserve an unresolved result rather than force a
   preferred class.
4. Perform focused S001–S005 synthesis.
5. Decide whether D1 has enough evidence to yield control to B1.
6. Add another case only if a named material uncertainty still blocks the minimum
   credible runtime responsibility.

Do not continue merely to reach a fixed number of cases.

## 17. Exit to implementation

Product simulation yields control back to the project route only when evidence and
Ali review support:

- a stable operating model at the useful current depth;
- universal and conditional runtime responsibilities;
- minimum durable state and report responsibilities;
- activation, stopping, cost, and divergence behavior;
- the smallest credible implementation responsibility;
- explicit unresolved questions and deferred contrasts.

The project route then controls B1. No automatic implementation resumption follows
from case count, elapsed time, or artifact volume.
