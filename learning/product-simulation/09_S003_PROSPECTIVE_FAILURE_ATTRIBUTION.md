# 09 — S003 Prospective Failure Attribution

**Depth target:** Operational preparation and ownership practice.  
**Primary question:** How should the first prospective scenario distinguish a dependency-caused failure from other credible explanations while preserving the artifact lifecycle honestly?

## 1. Why S003 is different

S001 and S002 are retrospective reconstructions. S003 must be the first case whose artifacts are created during the actual investigation.

Its primary discovery responsibility is:

> Causal attribution of actual failing decision-relevant CI in a real dependency-update pull request.

The case is not useful merely because CI is red. It must expose a credible attribution problem and enough evidence to distinguish competing causes.

## 2. Primary questions

S003 must answer:

1. What exact workflow, run, job, step, command, and responsibility failed?
2. Which exact revision and environment produced the failure?
3. Is the failure caused by the dependency update?
4. Could it be pre-existing, flaky, environmental, unrelated, mixed, or unresolved?
5. What evidence supports or contradicts each explanation?
6. Does the dependency-update assessment differ from overall PR mergeability?
7. What is the smallest proportionate next action?
8. What state changes after rerun, base comparison, fix, rebase, or new environment evidence?
9. How does the restricted baseline compare with the full result?
10. Does the current artifact family adequately represent repeated executions and attribution?

## 3. Candidate eligibility

A strong S003 candidate needs:

- real public dependency-update event;
- exact repository and change locator;
- frozen base and head revisions;
- identifiable dependency and version transition;
- actual failing decision-relevant CI;
- accessible run/job/step/command/output evidence;
- environment information at useful depth;
- at least two credible causal alternatives;
- a useful base/main/rerun/reproduction comparison boundary;
- safe and manageable public scope.

Reject a candidate when logs and comparison evidence are already unavailable, identity cannot be frozen, or causal ambiguity cannot be investigated proportionately.

## 4. Candidate screening is not the selected run

Before selection:

- record criteria;
- preserve only material candidate and rejection evidence;
- do not create the final scenario run ID;
- do not present the selected case as inevitable;
- do not mix screening evidence into the selected run without explicit admission.

This prevents candidate search history from becoming hidden or falsely linear.

## 5. Prospective checkpoints

### Checkpoint 0 — candidate screening

Record candidate set, rejection reasons, evidence-retention feasibility, and selection boundary.

### Checkpoint 1 — selected and frozen

Immediately create:

- scenario `README.md`;
- initial live-state `CASE.md`;
- `RUN_MANIFEST.json`;
- `INVOCATION.json`;
- `CASE_IDENTITY.json`;
- initial `OPERATION_EVENTS.jsonl`;
- initial `REVIEW_AND_OWNERSHIP.json`;
- baseline input snapshot and result when permitted inputs are available;
- explicit not-yet-produced states for later artifacts.

### Checkpoint 2 — failure acquired

Preserve:

- workflow/run/job/step/attempt identity;
- exact command or responsibility;
- result and failure signature;
- environment and revision identity;
- bounded log or artifact;
- initial competing hypotheses;
- next discriminating action.

### Checkpoint 3 — attribution investigated

Preserve:

- base/head/main/rerun comparisons;
- comparability limits;
- supporting and disconfirming evidence;
- changed or superseded hypotheses;
- current causal classification;
- unresolved questions;
- evidence required for the next change.

### Checkpoint 4 — decision and reports

Complete findings, decision, reports, follow-up, baseline comparison, and transitions.

### Checkpoint 5 — validation and review

Run one declared validation profile, preserve the method and result, update the manifest, and separate factual, Ali, external, and ownership states.

## 6. Trial artifact: `CHECK_EXECUTIONS.jsonl`

The default evidence model can preserve one check, but S003 may contain multiple comparable executions.

A structured check-execution record should identify:

- execution ID;
- repository and revision;
- source: CI, rerun, local isolated reproduction, or external report;
- workflow/run/job/step/attempt identity;
- trigger and changed-path applicability;
- exact command or responsibility;
- environment identity;
- start, end, source-event, and observation times;
- result;
- normalized failure signature where useful;
- raw/check references;
- producing operation and evidence IDs;
- comparison relationship;
- retention and limitations.

This is a trial responsibility. S003 must determine whether it becomes universal, conditional, merged, renamed, or rejected.

## 7. Trial artifact: `FAILURE_ATTRIBUTION.json`

This artifact should preserve:

- attribution record and version;
- exact observed failure identities;
- candidate causes;
- supporting and contradicting evidence for each cause;
- comparison executions;
- causal mechanism where established;
- current classification;
- qualitative uncertainty with reasons;
- unresolved discriminating questions;
- next evidence or check required;
- effect on dependency assessment;
- effect on PR action;
- superseded attribution state.

The artifact must not hide ambiguity behind one confidence number.

## 8. Attribution vocabulary

### `update_caused`

Use when evidence supports a mechanism connecting the dependency change to the failure.

Strong patterns include:

- base passes and head fails under comparable execution;
- reverting only the dependency change removes the failure;
- the failure signature reaches changed dependency behavior;
- an upstream regression matches the exact path and environment;
- a corrected dependency version resolves the same failure.

### `pre_existing`

Use when the materially same failure occurs on base, main, or before the update under sufficiently comparable conditions.

### `flaky`

Use when unchanged revision and environment produce inconsistent results across reruns, with evidence of nondeterminism.

One pass and one fail may suggest flakiness, but comparison quality still matters.

### `environmental`

Use when runner, platform, toolchain, network, cache, service, credentials, resource limits, or infrastructure best explain the result.

### `unrelated`

Use when another responsibility outside the dependency path is independently shown to cause the failure.

Changed-file distance alone is insufficient.

### `mixed`

Use when more than one material cause contributes.

### `unresolved`

Use when evidence is missing, inaccessible, contradictory, or not sufficiently comparable.

An unresolved result must still name the next discriminating evidence.

## 9. Correlation is not causation

Insufficient evidence alone includes:

- red or green color;
- temporal proximity;
- direct dependency status;
- release-note keywords;
- eventual merge or closure;
- one model explanation;
- one uncorroborated comment;
- fresh local behavior under a materially different environment.

The update and failure occurring together establish association, not causal mechanism.

## 10. Comparison design

Use the smallest credible comparison set.

Preferred order:

1. inspect existing base, main, head, and prior CI evidence;
2. compare exact commands, environments, and failure signatures;
3. inspect reruns or prior attempts;
4. inspect dependency path and upstream behavior;
5. use isolated local or container reproduction only when needed and safe;
6. request maintainer-owned evidence only when public comparison cannot resolve the material decision.

Every comparison must state:

- what is held constant;
- what differs;
- whether the commands are equivalent;
- whether environments are sufficiently comparable;
- whether timing or external dependencies could matter;
- what conclusion is permitted.

## 11. CI authority for a failure

For each failing result, preserve:

```text
exact revision
+ event and trigger
+ path applicability
+ workflow version
+ job/matrix/runner/attempt
+ step and command
+ environment
+ result and failure signature
+ retention state
+ responsibility exercised
+ proof limit
```

A red status has no global causal authority.

## 12. Dependency assessment versus PR action

S003 must test whether one action label is enough.

Possible situation:

```text
base and head fail identically
→ dependency update not shown to cause failure
→ dependency assessment may be acceptable or unresolved
→ PR still blocked by current repository CI policy
```

This may require separate dimensions for:

- dependency-update assessment;
- current PR/repository action.

The labels and schema remain illustrative until the case proves the need.

## 13. Baseline behavior under failing CI

The transparent baseline will likely use its first rule and select `investigate_or_block` when overall CI is failing or mixed.

The full investigation may find:

- same action with stronger causal explanation;
- pre-existing or unrelated failure, changing dependency-specific assessment;
- unresolved causality;
- already-explicit causality where deeper work adds little;
- excessive investigation cost relative to decision improvement.

S003 must not be forced into a wrong-action or pro-thesis result.

## 14. Required transitions

Model at least:

- confirmed update-caused failure;
- base/pre-existing failure;
- unrelated failure;
- flaky rerun;
- environmental failure;
- mixed or unresolved attribution;
- corrected dependency release;
- new head or rebase;
- changed workflow or environment;
- missing or expired logs;
- maintainer action.

A materially changed frozen boundary requires a new run, decision version, comparison, or supersession record.

## 15. Stop conditions

Stop with resolved attribution when:

- one classification has sufficient direct and comparative support;
- material alternatives are tested or bounded;
- the decision and transitions are justified;
- further work would not materially change the action.

Stop unresolved when:

- required evidence is inaccessible or non-comparable;
- safe investigation would require unauthorized action;
- conflicts cannot be resolved proportionately;
- a specific next action can be stated without inventing causality.

Unresolved is a valid result.

## 16. Validation profile

Before completion, validate:

- JSON and JSONL parsing;
- unique IDs;
- scenario/run/base/head consistency;
- operation and execution order;
- raw/evidence/claim/finding/attribution/decision/report lineage;
- current and superseded discoverability;
- explicit missing data;
- manifest inventory;
- baseline boundary;
- review and ownership dimensions;
- prospective checkpoints visible in history.

Preserve the exact validator method and proof limits.

## 17. Preparation exercises

### Exercise A — candidate test

Given a red dependency PR, decide whether it meets all S003 eligibility conditions. Identify missing evidence before selection.

### Exercise B — hypothesis table

Create rows for update-caused, pre-existing, flaky, environmental, unrelated, mixed, and unresolved. For each, list:

- supporting observation;
- contradicting observation;
- best discriminating comparison;
- decision effect.

### Exercise C — comparability review

Compare a base CI run and head local reproduction. Identify every environmental difference that limits causal inference.

### Exercise D — decision-axis test

Construct a case where the dependency appears acceptable but the PR remains blocked. Explain why one outcome label becomes ambiguous.

### Exercise E — checkpoint plan

Draft only Checkpoint 1 artifacts for a hypothetical selected case. Do not include any repository-specific finding that would only be discovered later.

## 18. Ownership checkpoint

Before S003 candidate selection, Ali should be able to explain:

1. Why a red PR is not enough for selection.
2. What makes two executions causally comparable.
3. The difference among update-caused, pre-existing, flaky, environmental, and unrelated failure.
4. Why a fresh local reproduction may not represent historical CI.
5. Why candidate screening is separate from the run.
6. What must exist at the selected-and-frozen checkpoint.
7. Why `CHECK_EXECUTIONS.jsonl` and `FAILURE_ATTRIBUTION.json` are trials.
8. How dependency assessment and PR action may diverge.
9. When to stop unresolved.
10. What structural validation cannot prove.

## 19. Current demonstrated depth

S003 requirements are prepared, but no candidate is selected and no prospective execution exists. This lesson supports preparation; ownership evidence begins when Ali participates in selection, checkpoint creation, hypothesis challenge, evidence comparison, and attribution review.
