# Product Simulation Governance and Plan

**Status:** Controlling local governance and execution plan
**Owner:** Ali Rajabi
**Scope:** Everything under `product-simulation/`
**Project route:** [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)
**Historical authorization:** [`../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`](../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md)

## 1. Authority

This plan controls how product-simulation work is selected, performed, represented,
reviewed, synthesized, and completed.

Local authority order:

1. external safety, law, privacy, credential, permission, and platform limits;
2. Ali's explicit current instruction;
3. [`AGENTS.md`](AGENTS.md);
4. this plan;
5. [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md);
6. [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md);
7. current synthesis and active scenario bundle;
8. scenario template and coverage;
9. other project-local records.

The stable UpgradePilot mission and Python product boundary remain controlled by
the project charter. Cross-ecosystem cases may test transferable responsibilities;
they do not silently expand the supported core.

## 2. Purpose

Product simulation discovers the real operating and artifact model before the
project freezes implementation responsibility, schemas, persistence, architecture,
or automation methods.

It answers:

1. **Product behavior:** What work is required to support the maintainer decision?
2. **Artifact behavior:** What state must be created, preserved, compared, replayed,
   rendered, reviewed, and superseded?
3. **Stopping behavior:** When is existing evidence sufficient, and when does deeper
   investigation add useful value?
4. **Automation feasibility:** Which responsibilities appear deterministic,
   tool-assisted, model-dependent, human-controlled, or unsuitable?

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
→ review, ownership, cost, and synthesis
```

Stages may be added, split, reordered, skipped, repeated, or stopped when evidence
requires it.

## 4. Complete manual-system rule

Ali and the AI assistant act as the intended system during simulation.

Do not bypass a future product responsibility by supplying its semantic answer as
an unexplained starting value. Manual interpretation is allowed, but actor, inputs,
method, uncertainty, and downstream authority must remain explicit.

## 5. Method freedom and non-admission

Any lawful, safe, accessible, materially useful method may be used, including
public acquisition, local checkouts, package inspection, dependency resolution,
static or dynamic analysis, tests, containers, databases, scripts, notebooks,
models, LLMs, agents, graphs, and human review.

Record material method use:

- responsibility and question;
- selection reason;
- inputs, exact source/tool/configuration, and environment;
- outputs, failures, side effects, and cost where material;
- what the result establishes and does not establish;
- evidence required before supported-product adoption.

Simulation use is not architecture or method approval.

## 6. Scenario state

Default organization:

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

Logical responsibilities are required. Physical files and fields remain
illustrative and non-binding.

Conditional extensions activate only when needed:

- `CHECK_EXECUTIONS.jsonl` for repeated, comparative, rerun, matrix, or
  local-versus-CI execution evidence;
- `FAILURE_ATTRIBUTION.json` when failing evidence has competing causes;
- other comparison, environment, dependency, or diagnostic artifacts when they add
  non-duplicative value.

Separate dependency-update assessment and PR action remain a tested candidate
decision shape, not a universal schema.

## 7. Narrative versus state

`CASE.md` is the complete human-auditable story.

The artifact bundle is the simulated runtime state.

Neither substitutes for the other. Machine artifacts must identify themselves as
manual simulation and must not imply that their fields are accepted production
contracts.

## 8. Progressive materialization

### Candidate screening

Preserve selection criteria and material rejection reasons before assigning a run
identity.

### Selected and frozen

Create navigation/live state, manifest, invocation, exact identity, initial
operation/review state, and the restricted baseline.

### Investigation

Append operations and evidence after material acquisition, failure, method switch,
or new finding. Preserve raw/check outputs, superseded states, current question,
and next action.

### Decision and reports

Complete findings, decision, reports, follow-up, transitions, baseline comparison,
and review state.

### Validation and synthesis

Run the declared validation profile; preserve method, result, and proof limits;
update coverage and synthesis; record Ali review as complete or pending.

Natural durable checkpoints are required. One commit per operation is not.

## 9. Evidence, lineage, and honesty

Use the smallest preservation strategy that retains decision, audit, replay, and
diagnostic value:

- full bounded capture when lawful and materially necessary;
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

Evidence acquisition proves that an item was observed, not that every claim inside
it is true or relevant.

## 10. Baseline, cost, and stopping

Execute the current transparent baseline before admitting full-investigation
evidence.

Compare:

- action;
- reasons and authority;
- uncertainty;
- targeted next action;
- failure behavior;
- added acquisition and reasoning cost;
- user value;
- whether the baseline was wrong, weaker, sufficient, unresolved, or the full
  investigation overreached.

Do not modify the baseline during an active case or force a thesis class.

Stop evidence collection when additional work no longer changes the decision,
uncertainty, actionability, product model, or material evaluation result.

## 11. Review and ownership

Track separately:

- execution status;
- factual review;
- Ali review;
- external or behavioral confirmation;
- AI assistance;
- Ali-owned capability at an explicit depth.

AI-produced completeness and historical merge state are not correctness or
capability proof.

## 12. Cross-case classification

After each case, classify material observations as:

- repeated stable candidate;
- conditional responsibility;
- one-case observation;
- contradicted assumption;
- unresolved;
- outside product boundary.

Also classify automation feasibility as:

- deterministically automatable;
- tool-assisted with interpretation;
- model-dependent;
- human-review required;
- blocked by inaccessible evidence;
- not yet tested;
- unsuitable.

Coverage owns compact status; focused synthesis owns detailed reasoning.

## 13. Case selection

Select a case because it resolves a material planning uncertainty.

Do not select merely because it is easy, complex, available, similar, or likely to
support the thesis.

Case count is not a completion gate.

## 14. Completion

A scenario is complete only when:

- the real event and exact identity are clear;
- the runtime reaches a justified stop;
- narrative and required logical state exist or are explicitly unavailable/not
  applicable;
- JSON/JSONL parse and IDs/references resolve;
- provenance, evidence states, failures, supersession, and uncertainty remain
  visible;
- baseline/full comparison and cost are recorded;
- decisions and reports trace to evidence;
- follow-up, rerun, recovery, and new-boundary transitions exist;
- review and ownership states are explicit;
- coverage and synthesis are updated;
- no unsupported safety, correctness, automation, or capability claim is made.

Artifact and case counts are not quality metrics.

## 15. Current D1 sequence

Completed evidence:

- S001 — retrospective Python transitive docs/advisory case;
- S002 — retrospective Python adapter/partial-green-CI case;
- S003 — prospective failing-install/peer-conflict transfer case.

Current authorized sequence:

1. Select **S004** as a deliberately simple baseline-sufficient control.
2. Execute it prospectively and stop when adequate decision support exists.
3. Record investigation cost and any artifact/stopping implications.
4. Select **S005** as the strongest available:
   - baseline-wrong-action case; or
   - dependency-update-versus-PR-action divergence case.
5. Execute S005 prospectively.
6. Perform focused synthesis sufficient to support or reject the B1 minimum
   credible runtime responsibility.

Do not continue merely to reach a fixed number of cases.

## 16. Exit to implementation

Product simulation yields control back to the project route only when evidence and
Ali review support:

- a stable operating model at the useful current depth;
- universal and conditional runtime responsibilities;
- minimum durable state and report responsibilities;
- stop and cost behavior;
- smallest credible implementation responsibility;
- explicit unresolved questions and deferred contrasts.

The project route then controls B1. No automatic implementation resumption follows
from case count, elapsed time, or artifact volume.
