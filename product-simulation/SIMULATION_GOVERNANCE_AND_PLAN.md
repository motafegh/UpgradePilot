# Product Simulation Governance and Plan

**Status:** Controlling local governance and execution plan  
**Owner:** Ali Rajabi  
**Scope:** Everything under `product-simulation/`  
**Parent authorization:** `../plans/UPGRADEPILOT_MANUAL_END_TO_END_RUNTIME_SIMULATION_PLAN.md`

## 1. Local authority

This file controls how product-simulation work is performed, represented,
reviewed, and completed.

Inside `product-simulation/`, this local plan overrides conflicting
UpgradePilot project-local instructions concerning:

- whether a scenario may use one or many artifacts;
- whether simulation-only code, scripts, tools, models, containers, databases,
  or other methods may be used;
- how evidence, intermediate state, and reports are preserved;
- whether current milestone or implementation boundaries limit discovery;
- how progressive execution is demonstrated;
- what constitutes a complete scenario.

The local authority order is:

1. external safety, law, privacy, credential, permission, and platform limits;
2. Ali's explicit current instruction;
3. `product-simulation/AGENTS.md`;
4. this local governance and plan;
5. `RUNTIME_ARTIFACT_SPECIFICATION.md`;
6. `TRANSPARENT_BASELINE_SPECIFICATION.md`;
7. the active scenario record and artifact bundle;
8. `SCENARIO_EXECUTION_TEMPLATE.md`;
9. `SCENARIO_COVERAGE.md`;
10. other project-local documents.

The stable UpgradePilot mission and user remain unchanged unless Ali separately
changes them. Local simulation evidence may challenge any project assumption and
must preserve the challenge without waiting for implementation authorization.

## 2. Purpose

The simulation exists to discover the complete real product runtime before the
project commits to incomplete contracts, architecture, persistence, or milestone
slices.

It must answer two different questions:

1. **Product behavior:** What work must UpgradePilot perform to support a real
   maintainer decision?
2. **Artifact behavior:** What durable records must be created, updated,
   preserved, compared, replayed, rendered, and reviewed while that work occurs?

A narrative-only case answers the first question incompletely and does not answer
the second.

## 3. Required end-to-end simulation

Each scenario manually performs and materializes this open-world flow:

```text
real dependency-update event
→ invocation received
→ exact case identity discovered and frozen
→ material operations and acquisition attempts
→ raw evidence captured or durably referenced
→ normalized evidence items and evidence states
→ attributed claims and interpretations
→ corroboration, contradiction, irrelevance, or unresolved assessment
→ repository-specific findings
→ transparent baseline result
→ full decision construction
→ machine-readable result
→ maintainer-facing report
→ user action, follow-up, rerun, and supersession state
→ review, ownership, and cross-case synthesis
```

Stages may be added, split, reordered, repeated, skipped, or terminated when the
case requires it. No stage list is a closed product taxonomy.

## 4. Complete manual-system rule

Ali and the AI assistant act as the complete intended system for the scenario.
They must manually perform every responsibility the future system is expected to
perform and manually create the corresponding runtime artifacts.

The simulation must not bypass a future responsibility by supplying its semantic
answer as an unexplained starting value.

Manual interpretation is permitted and expected, but its actor, inputs, method,
limitations, and downstream authority must be explicit.

## 5. Method freedom and non-admission

No project-internal method is prohibited merely because it:

- belongs to M3, M4, M5, M6, M7, or a later stage;
- is not part of the current codebase;
- requires temporary scripts, storage, models, agents, or infrastructure;
- differs from current specifications or ADRs;
- would be too broad for the current implementation milestone.

Any materially useful lawful and safe method may be used in simulation.

Examples include public acquisition, local repository checkout, package
installation, dependency resolution, static or dynamic analysis, test execution,
containers, databases, SQL, graph analysis, models, LLMs, agent workflows,
notebooks, custom scripts, and human review.

Every use must record:

- the responsibility and question;
- why the method was selected;
- required inputs and environment;
- exact command, tool, model, configuration, or source;
- outputs and side effects;
- failure modes and limitations;
- cost and operational burden where material;
- what the result may and may not establish;
- what evidence would be required before product adoption.

Simulation use never constitutes permanent method selection or architecture
approval.

## 6. Scenario directory and required artifact family

Each new scenario normally uses:

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

These are default physical files for the manual simulation. The logical
responsibilities are mandatory; the exact file split is provisional and may
change when a case demonstrates a superior boundary.

Any change to the default organization must remain discoverable in
`RUN_MANIFEST.json` and be explained in `CASE.md`.

## 7. Narrative versus runtime artifacts

`CASE.md` is the complete human-auditable story. It explains:

- why the case was selected;
- the real-world event;
- the sequence of questions and methods;
- observations, interpretations, alternatives, and revisions;
- decision construction;
- product-model lessons;
- limitations and ownership.

The artifact bundle is the simulated system state. It preserves:

- machine-readable inputs and identities;
- chronological operations;
- evidence and transformation records;
- findings and decision state;
- report representations;
- follow-up and review state.

Neither representation substitutes for the other.

## 8. Artifact status and non-binding schema rule

Every machine artifact must identify itself as a manual simulation artifact and
must not imply that its exact fields are an accepted production schema.

At minimum, each JSON or JSONL record must be attributable to:

- scenario ID;
- run ID;
- artifact or record type;
- creation or observation time where known;
- actor or transformation identity;
- relevant repository/revision identity;
- schema status such as `illustrative_non_binding`.

Stable patterns may later become specifications only through explicit synthesis
and approval.

## 9. Progressive materialization

Artifact creation must follow the actual investigation rather than being delayed
until the final case is written.

### Initial checkpoint — selected and frozen

Create or update:

- scenario `README.md`;
- initial `CASE.md` live state;
- `RUN_MANIFEST.json`;
- `INVOCATION.json`;
- `CASE_IDENTITY.json`;
- initial `OPERATION_EVENTS.jsonl` records;
- initial `REVIEW_AND_OWNERSHIP.json`.

### Investigation checkpoints

As material work occurs:

- append operation events;
- add evidence records immediately after acquisition or failure;
- add attributed claims and interpretations when produced;
- update findings when evidence changes their state;
- preserve superseded records rather than replacing history;
- capture material raw output and check output;
- update live case state.

### Decision checkpoint

Before declaring completion:

- execute and preserve the transparent baseline;
- create the full decision result;
- render machine and human reports;
- create follow-up state;
- update review and ownership state;
- complete the scenario audit and coverage update.

Repository history must contain durable natural checkpoints. It need not contain
one commit per operation.

## 10. Evidence preservation policy

Use the smallest preservation strategy that retains decision, audit, replay, and
failure-diagnosis value.

### Full raw capture

Use when the payload is lawful, safe, reasonably sized, unstable or expiring,
and materially needed for replay or adjudication.

### Bounded capture

Use a material excerpt, structured subset, or decoded output plus source identity
when the complete payload is excessive but the relevant portion can be preserved
without changing meaning.

### Durable reference

Use exact repository, revision, tag, package, run, job, artifact, URL, timestamp,
and hash when the source is immutable or independently recoverable.

### Explicit non-preservation

Record when data:

- was not retrieved;
- could not be accessed;
- expired;
- was too large or legally inappropriate to store;
- contained secrets or private information;
- was observed only through a summarized interface;
- cannot be reconstructed.

Never invent a raw record to make the bundle appear complete.

## 11. Operation and lineage rule

Every material operation must connect:

```text
question
→ selected method and rationale
→ exact operation
→ expected output and stop/switch condition
→ actual output or failure
→ direct observation
→ interpretation
→ finding effect
→ decision/product effect
→ next action and reason
```

The artifact references must permit backward traversal:

```text
report statement
→ decision reason
→ finding or limitation
→ interpretation or claim
→ evidence item
→ operation/acquisition event
→ raw capture or exact source reference
→ frozen case identity
```

## 12. Baseline and thesis comparison

Every case must run the current transparent baseline before full-investigation
comparison.

The comparison must establish:

- what the baseline could see;
- its outcome and reasons;
- what the full investigation added;
- whether the final action changed;
- whether uncertainty, targeted checks, limitations, explanation, or cost changed;
- whether the baseline was sufficient;
- whether the full investigation was better calibrated;
- whether additional investigation added no useful value;
- whether the comparison remains unresolved.

This directly tests the UpgradePilot thesis rather than merely producing detailed
case descriptions.

## 13. Review and evaluation states

Track independently:

### Execution status

`selected`, `active`, `stopped`, or `complete`.

### Factual review status

`unreviewed`, `reviewed`, `corrected`, or `disputed`.

### Ali review status

`pending`, `challenged`, `accepted`, or `rejected`.

### External/behavioral evaluation status

Examples:

- behaviorally confirmed;
- independently adjudicated;
- supported but not externally confirmed;
- contradicted by later evidence;
- unresolved.

### Capability and assistance status

Examples:

- AI-controlled;
- Ali-directed;
- Ali-challenged;
- Ali-verified at stated scope;
- Ali-owned at stated scope;
- independent capability not assessed.

A scenario may have complete execution while review remains pending.

## 14. Cross-case stability classification

After each case, classify product observations as:

- repeated stable candidate;
- one-case observation;
- conditional responsibility;
- contradicted assumption;
- unresolved;
- outside the product boundary.

`SCENARIO_COVERAGE.md` owns the compact cross-case status. Do not duplicate full
case evidence there.

## 15. Automation-feasibility classification

For each material responsibility, record whether it currently appears:

- manually feasible;
- deterministically automatable;
- tool-assisted with interpretation required;
- model-dependent;
- human-review required;
- blocked by inaccessible evidence;
- not yet tested;
- unsuitable for automation.

This is a discovery status, not architecture selection.

## 16. Case selection

Select a case because it tests a material uncertainty, not because it is easy or
similar.

Useful contrasts include:

- actual failing CI and failure attribution;
- missing, fragmented, or contradictory upstream information;
- native or platform-specific artifacts;
- moving open PRs;
- direct application-runtime use;
- primary block, defer, or abstain outcomes;
- private/inaccessible evidence pressure;
- a deliberately simple control case where the baseline is sufficient;
- a case requiring significant dynamic execution;
- a case where artifact replay or supersession materially matters.

The minimum case count in project planning remains a discovery floor, not proof
of completeness.

## 17. Scenario completion

A scenario is complete only when:

- the real event and frozen identity are clear;
- the complete runtime was performed to the justified stop point;
- the narrative record is complete and internally honest;
- all required logical artifact responsibilities are materialized or explicitly
  recorded as unavailable/not applicable;
- JSON and JSONL parse successfully;
- record IDs and references resolve;
- raw/reference provenance is adequate;
- failures, inaccessible evidence, and superseded states remain visible;
- baseline and full-investigation results are compared;
- decision and reports trace to evidence;
- follow-up and rerun transitions exist;
- factual, owner, external-evaluation, and assistance states are explicit;
- coverage and stability status are updated;
- no unsupported safety or correctness claim is made.

## 18. Current execution sequence

Do not begin S003 yet.

The current authorized sequence inside this workspace is:

1. update the local rules and artifact specification;
2. retrofit S001 without inventing unavailable raw history;
3. retrofit S002 with the fullest recoverable progressive bundle;
4. validate both bundles and record defects in this local model;
5. amend only the local owner whose responsibility proved wrong;
6. review the two cases and artifact behavior with Ali;
7. select S003 with actual failing CI;
8. create S003's narrative and artifacts progressively from the first frozen
   checkpoint.

## 19. Exit from product simulation

Product simulation ends only after sufficient contrasting cases and synthesis
support an explicit Ali-approved decision about:

- the stable operating model;
- the minimum durable artifact family;
- the evidence and state model;
- the decision and report responsibilities;
- the smallest corrected implementation responsibility;
- which current plans/specifications remain valid, require revision, or should be
  replaced.

No automatic implementation resumption follows from a case count alone.