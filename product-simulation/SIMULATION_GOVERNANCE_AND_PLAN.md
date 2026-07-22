# Product Simulation Governance and Plan

**Status:** Controlling local governance and execution plan  
**Owner:** Ali Rajabi  
**Scope:** Everything under `product-simulation/`  
**Parent authorization:** `../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`

## 1. Authority

This plan controls how product-simulation work is performed, represented,
reviewed, synthesized, and completed.

Local authority order:

1. external safety, law, privacy, credential, permission, and platform limits;
2. Ali's explicit current instruction;
3. [`AGENTS.md`](AGENTS.md);
4. this plan;
5. [`RUNTIME_ARTIFACT_SPECIFICATION.md`](RUNTIME_ARTIFACT_SPECIFICATION.md);
6. [`TRANSPARENT_BASELINE_SPECIFICATION.md`](TRANSPARENT_BASELINE_SPECIFICATION.md);
7. current cross-case synthesis and active scenario bundle;
8. scenario template and coverage;
9. other project-local documents.

The stable UpgradePilot mission and user remain unchanged unless Ali separately
changes them. Simulation evidence may challenge project assumptions and must
preserve the challenge without waiting for implementation authorization.

## 2. Purpose

The simulation discovers the real product runtime before the project commits to
incomplete contracts, architecture, persistence, or milestone slices.

It answers two separate questions:

1. **Product behavior:** What work must UpgradePilot perform to support a real
   maintainer decision?
2. **Artifact behavior:** What durable records must be created, updated, preserved,
   compared, replayed, rendered, and reviewed while that work occurs?

Narrative-only cases are insufficient.

## 3. Open end-to-end runtime

Each scenario manually performs and materializes an open-world flow:

```text
real dependency-update event
→ invocation
→ exact identity discovery and freeze
→ material operations/acquisition attempts
→ raw evidence capture or durable reference
→ evidence records and states
→ attributed claims and interpretations
→ corroboration/contradiction/irrelevance/unresolved assessment
→ repository-specific findings
→ transparent baseline
→ full decision
→ machine and human reports
→ action, follow-up, rerun, and supersession state
→ review, ownership, and cross-case synthesis
```

Stages may be added, split, reordered, repeated, skipped, stopped, or terminated
when the case requires it. No stage list is a closed product taxonomy.

## 4. Complete manual-system rule

Ali and the AI assistant act as the intended system during simulation. Every future
responsibility must be performed manually and represented through its artifacts.

Do not bypass a responsibility by supplying its semantic answer as an unexplained
starting value. Manual interpretation is permitted, but actor, inputs, method,
limits, and downstream authority must be explicit.

## 5. Method freedom and non-admission

Any lawful, safe, materially useful method may be used even when it belongs to a
later milestone or is absent from the current codebase.

Examples include public acquisition, local checkouts, package installation,
dependency resolution, static/dynamic analysis, tests, containers, databases,
SQL, graph analysis, models, LLMs, agent workflows, notebooks, scripts, and human
review.

Every material use records:

- responsibility and question;
- selection reason;
- inputs and environment;
- exact tool/command/model/configuration/source;
- outputs and side effects;
- failures and limitations;
- cost/burden where material;
- what it does and does not establish;
- evidence required before product adoption.

Simulation use never constitutes architecture or method approval.

## 6. Scenario artifacts

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
    ├── FOLLOW_UP_STATE.json
    ├── REVIEW_AND_OWNERSHIP.json
    ├── HUMAN_REPORT.md
    ├── raw/
    └── checks/
```

Logical responsibilities are mandatory. Physical files and fields are provisional.
Any deviation must remain discoverable in the manifest and narrative.

Conditional extensions may be activated. After S003:

- `CHECK_EXECUTIONS.jsonl` is a conditional stable candidate for repeated or
  comparative executions;
- `FAILURE_ATTRIBUTION.json` is a conditional stable candidate for competing
  causal explanations;
- separate dependency-assessment and PR-action dimensions remain a one-case
  observation rather than a universal contract.

## 7. Narrative versus state

`CASE.md` is the complete human-auditable story: selection, event, question/method
sequence, observations, interpretations, revisions, decision, product lessons,
limits, and ownership.

The artifact bundle is simulated runtime state: inputs, identities, operations,
evidence, transformations, findings, decision, reports, follow-up, and review.

Neither substitutes for the other.

## 8. Non-binding representation

Every machine artifact identifies itself as manual simulation and must not imply
that its exact fields are accepted production schema.

At minimum, records remain attributable to scenario, run, artifact/record type,
time where known, actor/transformation, relevant revision identity, and schema
status.

Stable patterns become specifications only through explicit synthesis and approval.

## 9. Progressive materialization

### Candidate screening

Preserve screening criteria and material rejection reasons before assigning a run
identity. Do not rewrite selection as obvious from the beginning.

### Selected and frozen checkpoint

Create scenario navigation/live state, manifest, invocation, identity, initial
operations, review state, and baseline input/result when available.

### Investigation checkpoints

Append operations and evidence immediately after acquisition/failure; add
transformations and findings as they arise; preserve supersession and raw/check
outputs; update live state and next action.

### Decision checkpoint

Complete findings, decision, machine/human reports, follow-up, review state,
baseline comparison, and transitions.

### Validation checkpoint

Run a declared validation profile, preserve method/result/proof limits, update
manifest/coverage/synthesis, and record review status.

Natural repository checkpoints are required; one commit per operation is not.

## 10. Evidence preservation

Use the smallest strategy retaining decision, audit, replay, and diagnostic value:

- full raw capture when lawful, safe, bounded, unstable/expiring, and needed;
- bounded capture when relevant material can be preserved without changing meaning;
- durable exact reference for immutable/recoverable sources;
- explicit non-preservation for inaccessible, expired, private, secret, excessive,
  summarized-only, or unrecoverable data.

Never invent a missing record or diagnostic.

## 11. Operation and lineage

Every material operation should connect question, method/rationale,
expected output/stop condition, exact execution, result/failure, observation,
interpretation/alternatives, finding/decision effect, and next action.

Backward traversal must be possible:

```text
report statement
→ decision reason
→ finding/limitation
→ interpretation/claim
→ evidence
→ operation
→ raw/reference source
→ frozen identity
```

## 12. Baseline and thesis comparison

Every case runs the current transparent baseline before full evidence is used for
comparison.

The comparison records baseline visibility/outcome/reasons, full evidence and
outcome, changed action/uncertainty/checks/authority/explanation/cost, and whether
the baseline was wrong, weaker, sufficient, unresolved, or the full process added
no useful value.

Do not force a thesis class through candidate selection or interpretation.

Current evidence after S003 contains three examples of the same broad-action,
stronger-decision-support class. Required contrasts remain baseline sufficient,
wrong action, unresolved, and overreach/excessive cost.

## 13. Review, evaluation, and capability

Track independently:

- execution status;
- factual review status;
- Ali review status;
- external/behavioral confirmation;
- assistance and capability state.

A scenario may be execution-complete while review remains pending. AI-controlled
work does not establish Ali-owned capability. Historical merge is not ground truth.

## 14. Cross-case classification

After each case, classify observations as:

- repeated stable candidate;
- one-case observation;
- conditional responsibility;
- contradicted assumption;
- unresolved;
- outside product boundary.

[`SCENARIO_COVERAGE.md`](SCENARIO_COVERAGE.md) owns compact status. Detailed
synthesis belongs in focused cross-case documents.

## 15. Automation-feasibility classification

For each material responsibility, record whether it appears:

- manually feasible;
- deterministically automatable;
- tool-assisted with interpretation;
- model-dependent;
- human-review required;
- blocked by inaccessible evidence;
- not yet tested;
- unsuitable for automation.

This is discovery status, not architecture selection.

## 16. Case selection

Select a case because it tests a material uncertainty, not because it is easy or
similar.

Useful contrasts include actual failing CI, missing/contradictory evidence,
native/platform-specific artifacts, moving PRs, direct runtime use, block/defer/
abstain, private-evidence pressure, baseline-sufficient control, dynamic execution,
replay/supersession, and divergent dependency-versus-PR action.

The case-count minimum remains a discovery floor, not proof of completeness.

## 17. Completion

A scenario is complete only when:

- real event and frozen identity are clear;
- runtime reaches a justified stop point;
- narrative is complete and honest;
- required logical artifacts are present or explicitly unavailable/not applicable;
- JSON/JSONL parse and IDs/references resolve;
- provenance and raw/check policy are adequate;
- failures, supersession, inaccessible evidence, and uncertainty remain visible;
- baseline/full results are compared;
- decision/reports trace to evidence;
- follow-up/rerun/new-boundary transitions exist;
- review/ownership states are explicit;
- coverage/synthesis are updated;
- no unsupported safety/correctness claim is made.

## 18. Current execution sequence after S003

Completed evidence:

- S001: retrospective transitive docs/advisory case;
- S002: retrospective adapter/partial-green-CI case;
- S003: prospective update-caused failing-install/peer-conflict case.

Current authorized sequence:

1. Ali reviews S003 and [`S003_POST_CASE_SYNTHESIS.md`](S003_POST_CASE_SYNTHESIS.md).
2. Correct only a real evidence-backed local-model defect.
3. Select S004 as a deliberately simple baseline-sufficient control.
4. Execute S004 prospectively and stop early when adequate decision support is
   already present.
5. After S004, prioritize a baseline wrong-action case or a failure case where
   dependency assessment and PR action genuinely diverge.
6. Continue other high-value contrasts only while they resolve planning
   uncertainties.
7. Keep M2-S03 paused until synthesis supports an explicit corrected minimum
   implementation responsibility.

Do not restart S003, universalize its conditional trial artifacts, or resume
implementation from case count alone.

## 19. Exit from product simulation

Product simulation ends only after sufficient contrasts and Ali-approved synthesis
support decisions about:

- stable operating model;
- minimum durable artifact family;
- evidence/state model;
- decision/report responsibilities;
- smallest corrected implementation responsibility;
- which plans/specifications remain valid, need revision, or should be replaced.

No automatic implementation resumption follows from a case count.
