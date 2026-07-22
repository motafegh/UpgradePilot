# 02 — Complete Runtime and Artifact Lifecycle

**Depth target:** Operational and implementation-adjacent understanding.  
**Primary question:** What state must exist from invocation through follow-up, and why cannot one polished case document represent it all?

## 1. Runtime versus narrative

A dependency-update investigation has two representations:

- `CASE.md` — the complete human-auditable story;
- `artifacts/` — the simulated runtime state.

The story explains why actions occurred and how the investigation changed. The runtime bundle preserves machine-addressable identity, operations, evidence, transformations, current findings, decisions, reports, transitions, and review state.

Neither replaces the other.

A narrative-only record can hide:

- what was known at invocation;
- when identity was frozen;
- failed acquisition attempts;
- raw-source preservation choices;
- which interpretation created a finding;
- superseded hypotheses;
- report-to-evidence traceability;
- what persists after the report;
- whether execution, factual review, and learner ownership differ.

## 2. Complete open-world flow

The current reference flow is:

```text
real dependency-update event
→ invocation received
→ exact case identity discovered and frozen
→ material operations and acquisition attempts
→ raw evidence captured or durably referenced
→ evidence items and evidence states
→ attributed claims and interpretations
→ relevance, corroboration, contradiction, or unresolved assessment
→ repository-specific findings
→ restricted transparent baseline
→ bounded decision
→ machine-readable report
→ maintainer-facing report
→ user action and follow-up state
→ rerun, replay, comparison, or supersession
→ factual review, Ali review, external evaluation, and ownership state
```

This is not a rigid pipeline. A real case may repeat, skip, split, or reorder responsibilities.

## 3. The default logical artifact family

### `RUN_MANIFEST.json`

Indexes the run, frozen identity, execution mode, artifact inventory, missing classes, baseline and decision identities, and validation state.

It answers:

> What belongs to this run, what exists, what is missing, and how should the bundle be interpreted?

### `INVOCATION.json`

Represents only what enters UpgradePilot at the start.

It must distinguish:

- caller-supplied values;
- event-supplied values;
- generated runtime metadata;
- contextual information visible to a person but not supplied;
- unknown, malformed, missing, or ambiguous input.

A final semantic answer must not be inserted here merely to bypass future investigation.

### `CASE_IDENTITY.json`

Represents the exact repository, change, base/head revision, dependency transition, and observation boundary discovered after invocation.

Its key invariant is:

> Evidence from different revisions must not be silently joined.

### `OPERATION_EVENTS.jsonl`

Preserves the material execution sequence.

An operation record should connect:

```text
question
→ method and reason
→ expected output and stop condition
→ exact action
→ result or failure
→ observation
→ interpretation effect
→ next action
```

It is not a click log. Routine mechanical navigation may be grouped.

### `EVIDENCE_ITEMS.jsonl`

Represents acquired observations, generated check results, explicit absence, and retention failures.

An evidence item says what was observed and what authority it has. It does not declare every source statement true.

### `CLAIMS_AND_INTERPRETATIONS.jsonl`

Preserves assigned meaning and transformation identity.

Examples:

- attributed upstream claim;
- parser-derived claim;
- deterministic source comparison;
- dependency-path interpretation;
- CI-authority interpretation;
- human or model interpretation;
- contradiction or relevance assessment.

### `FINDINGS.json`

Represents current case-level conclusions and limitations derived from evidence and transformations.

Findings may be supported, limited, unresolved, contradicted, superseded, or withdrawn.

### `BASELINE_RESULT.json`

Stores the result of the deliberately restricted comparator and its comparison with the full investigation.

This is required to test the project thesis rather than merely produce detailed reports.

### `DECISION.json`

Represents the bounded maintainer action, reasons, limitations, unresolved questions, targeted checks, and transitions.

It must explain why both stronger and weaker outcomes are unjustified.

### `MACHINE_REPORT.json`

An external machine-facing projection of the result. It contains what another system needs, not every internal operation.

### `HUMAN_REPORT.md`

The maintainer-facing explanation. It should be concise, understandable without the full case diary, and no stronger than the decision and evidence permit.

### `FOLLOW_UP_STATE.json`

Represents what happens next:

- required user action;
- responsible actor;
- new evidence expected;
- pass/failure/unavailable/inconclusive transitions;
- rerun triggers;
- closure conditions;
- state that persists across runs.

### `REVIEW_AND_OWNERSHIP.json`

Separates:

- execution status;
- factual review;
- Ali review;
- external or behavioral confirmation;
- AI contribution;
- Ali direction, challenge, verification, and independent capability evidence.

### `raw/` and `checks/`

`raw/` preserves material source payloads or bounded captures. `checks/` preserves actually performed tests, comparisons, validation methods, and diagnostic outputs.

A proposed command belongs in a decision or follow-up record, not as a fake check result.

## 4. Why physical files are provisional

The logical responsibilities survived S001 and S002, but their exact fields and boundaries drifted.

Examples of drift include:

- status and method field names;
- record-ID conventions;
- timestamp representation;
- limitation structure;
- transition structure;
- compact versus pretty JSON;
- validation method representation.

This demonstrates why the package must distinguish:

```text
logical responsibility = repeated stable candidate
physical file/field layout = still provisional
```

## 5. One scenario, multiple identities

Do not collapse these:

- scenario ID — stable case identity across runs;
- run ID — one execution or evidence boundary;
- repository base/head identity — exact target snapshot;
- evidence source revision — source-specific identity;
- operation ID — one material action;
- decision version — current bounded decision state;
- report version — external representation version.

A new head SHA, materially different resolver output, changed workflow, or new decision-changing evidence may require a new run or explicit comparison rather than silent overwrite.

## 6. S002 example: why one file is insufficient

S002 needed separate records for:

- PR and dependency identity;
- target requirements and tests;
- direct declaration, adapter-mediated use, and production installation;
- HTTPX API removal;
- Starlette old/fixed source comparison;
- workflow trigger and command scope;
- HTTP 410 log failure;
- likely compatibility with unresolved historical environment;
- exact targeted checks;
- pass/failure/unavailable/rebase transitions;
- AI-controlled work and pending Ali review.

A single narrative could explain this, but a future system also needs queryable and replayable state.

## 7. Failure mode: artifact duplication

Separation does not justify repeating the same prose everywhere.

A healthy split is:

- raw capture stores the bounded source;
- evidence item stores observation, authority, state, and references;
- interpretation stores assigned meaning;
- finding stores case-level conclusion;
- decision stores permitted action effect;
- machine report projects the current result;
- human report explains the result concisely;
- `CASE.md` tells the complete chronological and reasoning story.

## 8. Read and inspect

Use these sources:

- `RUNTIME_ARTIFACT_SPECIFICATION.md` — each logical responsibility;
- `S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md` — artifact-by-artifact review and drift;
- S002 `RUN_MANIFEST.json` — full inventory example;
- S002 `OPERATION_EVENTS.jsonl` — progressive-chain representation;
- S002 `MACHINE_REPORT.json` and `HUMAN_REPORT.md` — external projections.

## 9. Classification exercise

Place each item in the most appropriate artifact:

1. “PR #20 changed only `requirements.txt`.”
2. “The frozen head SHA is `391508...`.”
3. “Inspect workflow path filters because green status may not cover the changed path.”
4. “Python tests did not trigger for the manifest-only PR.”
5. “Run `pytest --cov` under a captured resolution.”
6. “If the head changes, create a new run.”
7. “Ali has not independently verified the compatibility reasoning.”

Expected primary placements:

1. evidence item, with raw patch source;
2. case identity;
3. operation event;
4. interpretation/finding, supported by workflow evidence;
5. decision targeted check;
6. follow-up transition;
7. review and ownership.

## 10. Ownership checkpoint

Explain:

1. Why is invocation separate from case identity?
2. Why is an evidence item not a finding?
3. Why is `MACHINE_REPORT.json` not the internal truth store?
4. What should happen when a target head SHA changes?
5. Which artifacts should preserve an expired CI log?
6. What responsibility would disappear if follow-up were omitted?
7. Which logical responsibilities appear stable after two cases, and which physical details remain unresolved?

## 11. Current demonstrated depth

The default family has survived two retrospective cases and is a repeated stable candidate. Prospective persistence, real rerun behavior, scale, conflict handling, and final production schema fitness remain unproven.
