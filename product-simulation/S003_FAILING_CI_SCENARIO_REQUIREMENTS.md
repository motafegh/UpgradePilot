# S003 Failing-CI Scenario Requirements

**Status:** Active preparation and entry requirements; case not yet selected  
**Purpose:** Define what S003 must test, preserve, and prove before candidate
selection begins  
**Authority:** Subordinate to `AGENTS.md`, `SIMULATION_GOVERNANCE_AND_PLAN.md`,
`RUNTIME_ARTIFACT_SPECIFICATION.md`, and the current transparent baseline  
**Cross-case basis:** [`S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md`](S001_S002_CROSS_CASE_ARTIFACT_REVIEW.md)

S003 is the first prospective product-simulation case. Its primary discovery
responsibility is **causal attribution of actual failing CI in a real dependency-
update PR**.

S003 is not selected merely because a PR is red. It must expose a credible
attribution problem and enough evidence to distinguish competing causes.

## 1. Primary questions

S003 must answer:

1. What exact check, job, step, command, and responsibility failed?
2. Which exact revision and environment produced the failure?
3. Is the failure caused by the dependency update?
4. Could it be pre-existing, flaky, environmental, unrelated, mixed, or
   unresolved?
5. What evidence distinguishes those explanations?
6. Does the dependency-update assessment differ from current PR mergeability?
7. What is the smallest proportionate next action?
8. How should the decision change after rerun, base comparison, fix, rebase, or
   new environment evidence?
9. Does the restricted baseline choose the same action, a wrong action, or an
   unresolved action?
10. Does the current artifact family adequately represent real failure analysis?

## 2. Mandatory candidate-selection criteria

A candidate is eligible only when all mandatory criteria are satisfied.

### 2.1 Real dependency-update event

The candidate must be a real public dependency-update PR or equivalent public
change with:

- identifiable update producer;
- exact repository and change locator;
- exact base and proposed head revisions;
- identifiable dependency/ecosystem/version transition;
- retained change patch or equivalent mutation record.

### 2.2 Actual failing decision-relevant CI

At least one check associated with the proposed head must be failing, and the
failure must be potentially relevant to the dependency update or its integration
surface.

A red status without accessible job, step, command, or diagnostic information is
not sufficient.

### 2.3 Preservable failure evidence

Before final selection, confirm that enough evidence can be durably captured:

- workflow definition or equivalent check configuration;
- run, job, and step identity;
- failing command or responsibility;
- failure output, bounded log excerpt, or stable artifact;
- runner/environment identity at the available depth;
- base, prior, main-branch, rerun, or equivalent comparison evidence.

If failure logs are already expired or inaccessible and no alternative evidence
can support attribution, reject the candidate rather than repeating S002's
retention limitation.

### 2.4 Genuine causal ambiguity

The case must permit at least two credible candidate explanations among:

- update-caused;
- pre-existing;
- flaky;
- environmental/infrastructure;
- unrelated;
- mixed;
- unresolved.

An obviously deterministic and already-explained failure may be useful later as a
control, but it is not the preferred S003 case.

### 2.5 Useful comparison boundary

At least one of the following must be available or plausibly reproducible:

- comparable check on the base revision;
- comparable recent main-branch run;
- prior successful/failed attempt under similar conditions;
- rerun on unchanged revision;
- isolated reproduction under a recorded environment;
- upstream known-failure/fix evidence tied to the exact path.

### 2.6 Manageable and safe scope

The case must be bounded enough to inspect without:

- mutating the target repository;
- requiring private credentials or restricted data;
- executing unsafe third-party code without isolation;
- reproducing a large production deployment unnecessarily;
- relying on inaccessible proprietary infrastructure;
- turning S003 into an unbounded repository audit.

## 3. Candidate rejection criteria

Reject or defer a candidate when:

- exact base/head identity cannot be frozen;
- the failing run cannot be tied to the proposed head;
- failure details are unavailable and unrecoverable;
- the failure is only a cancelled/skipped/neutral status without causal content;
- the failing responsibility is clearly outside the update and no meaningful
  decision ambiguity remains;
- the repository is so large or dynamic that the case cannot be bounded to a
  decision-support question;
- the PR changes many unrelated dependencies or source areas and causal isolation
  is impractical for this scenario;
- a moving PR cannot be snapshotted before material analysis;
- safe investigation requires unauthorized mutation, credentials, or production
  access;
- candidate selection would duplicate S001 or S002 rather than add failure-
  attribution evidence.

Rejected candidates and reasons belong in a bounded screening record. They must
not be rewritten as though the selected case was known from the beginning.

## 4. Required prospective checkpoints

S003 must demonstrate the future artifact lifecycle through natural durable
checkpoints.

### Checkpoint 0 — Candidate screening

Before the selected run exists:

- record screening criteria;
- preserve only material candidate/rejection evidence;
- keep screening separate from selected-case runtime evidence;
- do not assign a run identity prematurely.

### Checkpoint 1 — Selected and frozen

Immediately after selection, create and commit:

- scenario directory and `README.md`;
- initial live-state `CASE.md`;
- `RUN_MANIFEST.json`;
- `INVOCATION.json`;
- `CASE_IDENTITY.json`;
- initial `OPERATION_EVENTS.jsonl`;
- initial `REVIEW_AND_OWNERSHIP.json`;
- restricted baseline input snapshot and execution, when all allowed inputs are
  available;
- placeholder states for artifacts not yet produced.

No repository-specific finding may be treated as invocation input.

### Checkpoint 2 — Failure acquired

After preserving the first failing run:

- append operation events;
- create evidence items for workflow/run/job/step/command/output;
- preserve bounded raw logs or artifacts;
- create `CHECK_EXECUTIONS.jsonl` records;
- state the initial causal hypotheses without choosing one prematurely;
- update live case state and next discriminating action.

### Checkpoint 3 — Attribution investigated

After base/head/rerun/environment/upstream comparisons:

- append comparison operations and evidence;
- preserve alternative explanations and disconfirming evidence;
- create or update claims and interpretations;
- create versioned findings;
- create `FAILURE_ATTRIBUTION.json`;
- preserve superseded hypotheses;
- record whether the current evidence resolves or merely narrows causality.

### Checkpoint 4 — Decision and reports

After reaching the justified stop point:

- complete `FINDINGS.json`;
- complete `DECISION.json`;
- render `MACHINE_REPORT.json` and `HUMAN_REPORT.md`;
- create `FOLLOW_UP_STATE.json`;
- update review and ownership;
- compare baseline and full investigation;
- preserve exact state transitions.

### Checkpoint 5 — Validation and review

Before scenario completion:

- run the common bundle-validation profile;
- preserve validation method and result;
- update manifest hashes/inventory;
- update coverage and cross-case synthesis;
- record factual, Ali, external, and capability-review states separately.

One commit per click is unnecessary. One final commit containing an invented
progressive history is prohibited.

## 5. Required default artifacts

S003 keeps the current default bundle:

```text
scenarios/<S003-case>/
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

## 6. S003 trial artifacts

### 6.1 `CHECK_EXECUTIONS.jsonl`

Purpose: represent repeated CI/local check executions as comparable structured
records rather than only raw logs and generic evidence.

Each material record should include:

- `check_execution_id`;
- scenario and run identity;
- repository and revision;
- execution source: CI, rerun, local isolated reproduction, or external report;
- workflow/run/job/step/attempt identity where applicable;
- trigger and changed-path applicability;
- exact command or responsibility;
- environment identity or environment reference;
- start/end/observation times;
- result: pass, fail, cancelled, skipped, timed out, infrastructure error, or
  unknown;
- normalized failure signature where useful;
- raw/check artifact references;
- producing operation and evidence IDs;
- comparability relationship to another execution;
- limitations and retention state.

This artifact is a trial candidate. After S003, determine whether it becomes
universal, conditional, merged, renamed, or rejected.

### 6.2 `FAILURE_ATTRIBUTION.json`

Purpose: preserve the current causal assessment and competing hypotheses without
hiding uncertainty.

It should include:

- attribution record/version;
- exact failure observation identities;
- candidate causes;
- supporting and contradicting evidence per cause;
- comparison executions used;
- causal mechanism where established;
- current classification;
- confidence/uncertainty stated qualitatively and with reasons;
- unresolved discriminating questions;
- next check or evidence required;
- effect on dependency assessment;
- effect on PR/repository action;
- superseded attribution state and reason.

This artifact is also a trial candidate rather than an accepted universal
contract.

## 7. Common machine-artifact envelope for S003

Every JSON artifact and every JSONL record must be attributable through these
fields or an explicitly referenced shared envelope:

```json
{
  "artifact_status": "manual_simulation",
  "schema_status": "illustrative_non_binding",
  "scenario_id": "S003",
  "run_id": "s003-<UTC-basic-timestamp>-r1",
  "execution_mode": "prospective_manual_simulation",
  "artifact_type": "<type>",
  "artifact_version": 1,
  "created_at": "<RFC3339 UTC>",
  "updated_at": "<RFC3339 UTC>"
}
```

For append-only records, `observed_at`, `source_event_at`, and `recorded_at` may
be more appropriate than `updated_at`. Do not fabricate unavailable source times.

## 8. S003 record-ID convention

Use stable lowercase prefixes:

```text
op-001-...   operation
ev-001-...   evidence
cl-001-...   attributed claim
in-001-...   interpretation
fn-001-...   finding
dr-001-...   decision reason
ck-001-...   planned check
ce-001-...   check execution
fa-001-...   failure attribution revision
rv-001-...   review event
```

IDs are unique within one run and immutable after publication. A renamed label
must not change an established ID.

## 9. Serialization and diff discipline

For S003:

- JSON uses two-space indentation and a terminal newline;
- JSONL uses one complete object per line;
- generated ordering should be stable where practical;
- arrays preserve meaningful order only when order is semantically relevant;
- formatting-only changes must not be presented as evidence changes;
- large raw logs remain bounded files under `raw/` or `checks/`, not embedded in
  state artifacts.

## 10. Failure-attribution vocabulary

Use the following open classification set when it fits the evidence.

### `update_caused`

Use only when evidence supports a causal mechanism connecting the dependency
change to the failure. Strong evidence normally includes comparable base/head
behavior or an equivalent controlled comparison.

### `pre_existing`

Use when the materially same failure exists on the base revision, main branch, or
before the dependency change under a sufficiently comparable environment.

### `flaky`

Use when materially identical reruns on the same revision/environment produce
inconsistent results and there is evidence of nondeterminism. One transient pass
or failure alone does not prove flakiness.

### `environmental`

Use when runner, operating system, architecture, toolchain, network, cache,
service, credential, rate-limit, resource, or infrastructure differences best
explain the failure.

### `unrelated`

Use when the failure is attributable to a responsibility outside the changed
dependency path and that attribution is supported independently. Mere distance
from the changed file is insufficient.

### `mixed`

Use when more than one material cause contributes and cannot honestly be reduced
to one label.

### `unresolved`

Use when evidence is insufficient, inaccessible, contradictory, or incomparable.
An unresolved attribution must identify the next discriminating evidence rather
than collapse into generic low confidence.

The vocabulary remains open. A case may require another classification with a
clear definition and evidence rule.

## 11. Minimum causal evidence rules

S003 must not infer causality from correlation alone.

### Evidence supporting update causality

Examples include:

- base passes and head fails under comparable execution;
- reverting only the dependency change removes the failure;
- failure stack/signature reaches the changed dependency behavior;
- upstream known regression matches the exact environment and path;
- a fixed dependency release resolves the same failure under comparison.

### Evidence supporting non-update causality

Examples include:

- base or recent main fails identically;
- failure predates the PR;
- unchanged-head reruns alternate pass/fail;
- infrastructure diagnostics explain the failure;
- the failed responsibility cannot reach the changed dependency and another
  concrete cause is established.

### Evidence that is insufficient alone

- red/green color;
- eventual merge or closure;
- failure proximity in time;
- dependency directness;
- release-note keywords;
- changed-file distance;
- one model-generated explanation;
- one uncorroborated maintainer comment;
- a fresh local reproduction under a materially different environment.

## 12. Required comparison design

S003 should seek the smallest credible comparison set, not execute every possible
combination.

Preferred order:

1. inspect existing base/main/pr-head CI evidence;
2. compare exact commands, environments, and failure signatures;
3. use retained reruns or prior attempts;
4. inspect changed dependency path and upstream evidence;
5. perform an isolated local/container reproduction only when needed and safe;
6. request maintainer-owned evidence only when public comparison cannot resolve
   the material decision.

Every comparison must state what is and is not comparable.

## 13. CI authority requirements

For every material CI result, preserve:

- exact repository and revision;
- event and trigger type;
- changed-path applicability;
- workflow identity and version;
- job, matrix, runner, and attempt identity;
- exact step/command or reusable-workflow responsibility;
- environment identity at available depth;
- result and failure signature;
- log/artifact retention state;
- what responsibility the result exercised;
- what it cannot establish.

A failing status has no global causal authority merely because it is red.

## 14. Baseline execution and thesis comparison

Run `simulation-transparent-baseline-v0.1` using only its permitted inputs.

For a failing-CI candidate, the baseline will likely produce
`investigate_or_block`, but S003 must not predetermine the final comparison.

Possible evidence-derived results include:

- same action, stronger causal explanation;
- baseline blocks but full investigation identifies a pre-existing/unrelated
  failure and changes the dependency-specific action;
- baseline blocks but full evidence remains unresolved;
- full investigation adds little because failure causality is already explicit;
- full investigation costs more than its useful decision improvement.

Record:

- baseline input cutoff and execution time;
- baseline outcome and reason codes;
- full outcome and reasons;
- dependency-specific action difference;
- PR/repository-action difference;
- uncertainty and evidence-authority difference;
- check specificity and transition difference;
- additional investigation cost;
- whether the baseline was wrong, weaker, sufficient, or unresolved.

Do not select a candidate or interpret evidence merely to force a thesis result.

## 15. Decision-model question to test

S003 must explicitly test whether one outcome is sufficient.

Potential distinction:

```text
dependency_update_assessment:
  acceptable | targeted_check | update_caused_block | unresolved

repository_or_pr_action:
  merge_after_normal_review | blocked_by_current_ci | investigate | defer
```

These labels are illustrative only. Do not add them to the universal
specification unless the case demonstrates that one existing outcome cannot
represent the maintainer decision without ambiguity.

## 16. Required decision transitions

At minimum, model transitions for:

- confirmed update-caused failure;
- base/pre-existing failure;
- unrelated failure;
- flaky rerun result;
- environmental/infrastructure failure;
- mixed or unresolved attribution;
- fixed dependency version;
- new head or rebase;
- changed workflow or environment;
- missing/expired logs;
- maintainer action.

A new run, decision version, comparison, or supersession record must be created
when the frozen evidence boundary changes materially.

## 17. Stop and switch conditions

### Switch candidate before freeze when

- logs or exact identity cannot be preserved;
- no credible causal ambiguity exists;
- base/head comparison is impossible and no alternative discriminator exists;
- safe scope cannot be bounded;
- the candidate duplicates prior coverage.

### Stop investigation with resolved attribution when

- one classification has sufficient direct and comparative support;
- material alternatives have been tested or bounded;
- the decision and transitions are justified;
- further work would not change the maintainer action materially.

### Stop with unresolved attribution when

- required evidence is inaccessible or non-comparable;
- additional execution would require unauthorized action;
- evidence conflicts cannot be resolved proportionately;
- the next action can be specified without inventing causality.

Unresolved is an acceptable result when honestly earned.

## 18. Validation profile

Before completion, validate:

1. every JSON file parses;
2. every JSONL line parses independently;
3. IDs are unique within the run;
4. all internal references resolve;
5. scenario/run/base/head identity is consistent;
6. operation and check-execution ordering is coherent;
7. each evidence item has an operation and raw/reference origin;
8. each claim/interpretation traces to evidence;
9. each finding traces to evidence and transformations;
10. each attribution cause traces to evidence and comparison executions;
11. each decision reason traces to findings or explicit limitations;
12. reports match the current decision and attribution;
13. superseded hypotheses/findings/decisions remain discoverable;
14. missing data is represented rather than invented;
15. manifest inventory matches files and states;
16. baseline inputs remain within the baseline boundary;
17. review and ownership dimensions are explicit;
18. prospective checkpoints are visible in repository history.

Preserve the exact validator method, version, result, and proof limits.

## 19. Completion criteria

S003 is complete only when:

- one real failing-CI dependency update is frozen;
- the failure is represented at run/job/step/command/responsibility depth;
- actual logs or equivalent bounded output are preserved;
- competing causal hypotheses are explicit;
- comparison evidence supports a classification or justified unresolved state;
- dependency assessment and PR action are not silently conflated;
- baseline and full results are compared;
- decision, reports, follow-up, and transitions are complete;
- the trial artifacts are reviewed for value and duplication;
- structural validation passes or defects are preserved and corrected;
- coverage and cross-case synthesis are updated;
- factual, Ali, external, and capability states remain separate;
- no target mutation or unsupported safety/correctness claim occurs.

## 20. S003 outputs for later planning

S003 must produce evidence for these planning decisions:

- whether structured check executions are a stable product responsibility;
- whether causal attribution needs a dedicated artifact;
- whether environment identity requires a separate artifact or can remain a
  check-execution reference;
- whether dependency assessment and PR mergeability require separate decision
  dimensions;
- which failure-attribution steps are deterministic, tool-assisted, model-
  dependent, or human-owned;
- which comparisons are sufficient and which are excessive;
- how prospective persistence and replay should work;
- whether the current artifact family remains adequate;
- what corrected implementation responsibility should eventually follow.

## 21. Review and authorization state

- **Requirements authoring:** AI assistant under Ali's direction.
- **Ali acceptance of these requirements:** pending.
- **S003 candidate selected:** no.
- **S003 execution authorized by this file alone:** no; selection follows Ali review
  and must comply with current local governance.
- **Implementation resumption:** not authorized.
- **Capability claim:** none.
