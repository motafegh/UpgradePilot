# 04 — Progressive Execution, Failures, and Honest History

**Depth target:** Operational and implementation-adjacent understanding.  
**Primary question:** How should the repository preserve what actually happened without inventing a clean history after the answer is known?

## 1. Why progressive execution matters

A future runtime is not only a final report generator. It must survive partial work, failed acquisition, changing hypotheses, unavailable evidence, reruns, and review.

If artifacts are created only after the final decision, several important behaviors disappear:

- what was known before each action;
- why a method was selected;
- what result was expected;
- which alternatives were considered;
- when a hypothesis changed;
- which failure caused a method switch;
- what state another investigator could resume from;
- whether the apparent reasoning path was reconstructed after the fact.

## 2. Material operation versus mechanical activity

A material operation changes or tests at least one of:

- current question;
- evidence set;
- hypothesis;
- finding or authority;
- recommendation;
- artifact model;
- method assessment;
- uncertainty or limitation;
- next branch.

Examples of material operations:

- freezing exact PR identity;
- acquiring a failing CI log;
- comparing base and head behavior;
- discovering a workflow path filter;
- failing to retrieve expired logs;
- correcting an advisory date;
- superseding a causal hypothesis;
- running the transparent baseline;
- validating the artifact bundle.

Routine page navigation or repeated safe lookups may be grouped.

## 3. Required operation chain

A useful material record preserves:

```text
state and question before action
→ method selection and reason
→ alternatives not selected
→ expected output
→ what success would and would not establish
→ stop, switch, or escalation condition
→ exact execution and attribution
→ raw output or explicit failure
→ direct observation
→ interpretation and alternatives
→ records changed
→ next action and reason
```

This structure prevents hindsight from rewriting method choice.

## 4. Prospective execution

A prospective case creates and updates state during the actual investigation.

Minimum durable progression:

```text
candidate screening
→ selected and frozen
→ material evidence acquired
→ hypotheses investigated
→ decision and reports completed
→ validation and review
```

Repository history should show natural checkpoints. It does not require one commit per operation.

S003 is intended to become the first prospective product-simulation case.

## 5. Retrospective reconstruction

A retrospective reconstruction creates the artifact bundle after the original investigation.

This can still be valuable when it honestly distinguishes:

- retained exact operations;
- retained exact results;
- grouped history;
- reacquired current evidence;
- reconstructed rationale;
- unknown original timestamps;
- unrecoverable payloads;
- artifacts that did not exist originally.

S001 and S002 are complete as retrospective reconstructions. They do not demonstrate prospective persistence.

## 6. What must never be invented

Do not fabricate:

- historical timestamps;
- commands that were only proposed;
- successful checks that were not executed;
- missing raw connector payloads;
- candidate rejection reasons not recorded at the time;
- exact historical dependency resolution;
- external confirmation;
- an Ali explanation or independent execution that did not happen.

Use explicit states instead:

- `historical_time_unknown`;
- `not_recoverable`;
- `not_preserved`;
- `inaccessible`;
- `expired`;
- `not_run`;
- `pending_review`.

## 7. Failure is part of the runtime

A failed method should preserve:

- the attempted question;
- selected method;
- exact target and time/revision boundary;
- error or returned state;
- whether the failure is evidence itself;
- what alternatives remain;
- whether the investigation stops, switches, or continues;
- decision and report consequences.

### S002 example: HTTP 410

The historical Docker job log request returned HTTP 410.

Correct outcome:

```text
log retrieval attempt
→ expired/inaccessible evidence item
→ exact historical resolver state remains unavailable
→ likely compatibility cannot become behavioral proof
→ targeted exact-head rerun remains necessary
```

Incorrect outcomes would include:

- assuming the old environment from a fresh resolver;
- treating log absence as a failed job;
- omitting the failed attempt from the case;
- claiming the environment was reproduced.

## 8. Supersession rather than cleanup

Earlier hypotheses may be wrong or too broad. They should remain discoverable.

Example from S002:

```text
initial concern: HTTPX 0.28 may hard-break TestClient
→ inspect Starlette 0.36.3 and 0.37.2
→ inspect FastAPI constraint
→ narrow to: compatible branch existed, exact historical resolution unavailable
```

The earlier concern is preserved as superseded rather than deleted.

## 9. Correction without decision manipulation

S001 corrected:

- advisory publication date;
- timing relative to the PR;
- strength of the security-trigger inference.

The correction process should ask:

1. Which source or interpretation was wrong?
2. What new evidence corrects it?
3. Which findings and report statements change?
4. Does the bounded decision change?
5. If not, why not?

The decision remained the same because remediation, target compatibility, dependency scope, package identity, and relevant CI still supported normal review.

## 10. Validation evidence must also be audited

A validation artifact is itself evidence with a method and proof boundary.

A “passed” result should answer:

- what validator was used;
- whether the method is preserved;
- which files and run boundary it validated;
- which checks it performed;
- whether the current repository still matches the validated inventory;
- what it explicitly does not prove.

Structural validation does not prove:

- external truth;
- decision correctness;
- target safety;
- production schema fitness;
- Ali-owned capability.

The cross-case review found that S001 and S002 used different validation practices. S003 must preserve one declared validation profile and the exact method used.

## 11. Natural checkpoint design for S003

### Checkpoint 0 — candidate screening

Preserve criteria and material rejection reasons. Do not create the selected run prematurely.

### Checkpoint 1 — selected and frozen

Create initial navigation, live case state, manifest, invocation, identity, operations, ownership record, and baseline snapshot where available.

### Checkpoint 2 — failure acquired

Preserve exact workflow/run/job/step/command/output and initial competing hypotheses.

### Checkpoint 3 — attribution investigated

Preserve comparisons, disconfirming evidence, versioned findings, and current attribution state.

### Checkpoint 4 — decision and reports

Complete current findings, decision, reports, follow-up transitions, and baseline comparison.

### Checkpoint 5 — validation and review

Run the validator, update manifest and coverage, and separate execution, factual review, Ali review, external confirmation, and ownership.

## 12. Failure modes

### Final-state reconstruction presented as progressive

Correction: label the execution mode and preserve the actual retrofit boundary.

### One commit per click

This creates ceremony without useful state transitions.

Correction: commit natural checkpoints.

### Only successful paths preserved

This hides why the final method and decision are justified.

Correction: preserve material failed, abandoned, replaced, and superseded paths.

### Proposed check stored as check output

Correction: planned actions belong in decision/follow-up; actual outputs belong in `checks/` and evidence records.

### Historical merge used as confirmation

Correction: preserve it as user action history, not correctness evidence.

## 13. Read and inspect

- `SIMULATION_GOVERNANCE_AND_PLAN.md` — progressive materialization;
- `SCENARIO_EXECUTION_TEMPLATE.md` — material-step structure;
- S001 reconstruction and honesty boundary;
- S002 `OPERATION_EVENTS.jsonl` and HTTP 410 evidence;
- `S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md` — prospective progression and validation drift;
- `S003_FAILING_CI_SCENARIO_REQUIREMENTS.md` — required checkpoints.

## 14. Ownership checkpoint

1. Define a material operation without using the word “important.”
2. Explain why expected output should be recorded before execution.
3. Distinguish prospective execution from retrospective reconstruction.
4. Explain how an HTTP 410 response affects the evidence and decision chain.
5. Give one example of a superseded hypothesis from S001 or S002.
6. Explain what a structural validator proves and does not prove.
7. Design one natural checkpoint for a hypothetical failing-CI case.
8. Identify one situation where stopping unresolved is more honest than continuing.

## 15. Current demonstrated depth

The repository now contains two honest retrospective reconstructions and detailed prospective requirements. It has not yet demonstrated a complete prospective run, real rerun comparison, multi-session recovery, or Ali-independent progressive execution.
