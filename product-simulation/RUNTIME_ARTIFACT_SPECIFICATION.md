# Product Simulation Runtime Artifact Specification

**Status:** Controlling local simulation specification  
**Scope:** Manual artifact bundles under `product-simulation/scenarios/`  
**Schema status:** Logical responsibilities are required; exact production schemas are not frozen

## 1. Purpose

A product-simulation scenario must preserve both:

1. a complete human-auditable narrative in `CASE.md`; and
2. a durable manual representation of the machine artifacts the future
   UpgradePilot runtime would conceptually produce.

This specification prevents one polished Markdown file from hiding:

- intermediate system state;
- acquisition attempts and failures;
- raw evidence preservation choices;
- evidence and transformation identities;
- partial-run behavior;
- decision inputs and state transitions;
- replay and supersession needs;
- differences among internal, persistent, machine-report, and human-report forms.

## 2. Non-binding implementation boundary

The files and example fields below are mandatory for current manual simulation
unless a scenario documents a better logical split. They are not automatically:

- production API schemas;
- database tables;
- Pydantic models;
- event contracts;
- service boundaries;
- final field names;
- permanent serialization formats.

Every artifact must identify:

```json
{
  "artifact_status": "manual_simulation",
  "schema_status": "illustrative_non_binding"
}
```

Equivalent metadata may be placed in a shared envelope or manifest when that is
clearer, but no artifact may be mistaken for implemented production output.

## 3. Default bundle

```text
artifacts/
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

The bundle may add files such as dependency graphs, environment snapshots,
comparison outputs, diagrams, SQL exports, model results, or replay records when
the case requires them.

Do not create empty decorative files. A required logical artifact that has no
available data must still exist where needed to preserve the state, with an
explicit state such as `not_available`, `not_applicable`, `not_recoverable`, or
`not_yet_produced` and a reason.

## 4. Common identity and reference rules

### 4.1 Run identity

Every scenario execution must have a stable `run_id` distinct from the scenario
ID. A rerun, changed head revision, new evidence set, or later decision revision
may require a new run or comparison record rather than silent replacement.

### 4.2 Scenario identity

Every artifact belongs to exactly one scenario ID.

### 4.3 Frozen repository identity

Material evidence and findings must identify the repository and revision, release,
workflow run, artifact, or observation-time boundary to which they apply.

### 4.4 Record IDs

Use stable unique IDs for material records, normally with readable prefixes:

- `op-...` — operation event;
- `ev-...` — evidence item;
- `cl-...` — attributed claim;
- `in-...` — interpretation;
- `fn-...` — finding;
- `dr-...` — decision reason;
- `ck-...` — targeted check or verification action;
- `rv-...` — review event.

Exact prefixes are provisional. Uniqueness and resolvable references are
mandatory.

### 4.5 Time

Record timestamps when actually known or generated. Do not fabricate historical
operation timestamps. For retrospective work, record:

- observed/retrieved time;
- source publication or event time if authoritative;
- `historical_time_unknown` where exact operation time cannot be recovered.

## 5. `RUN_MANIFEST.json`

### Responsibility

Index and describe one complete simulated run and its artifacts.

### Create

At the selected-and-frozen checkpoint. Update after material bundle changes and at
completion.

### Minimum content

- scenario ID;
- run ID;
- run status;
- repository and PR/change locator;
- frozen base/head or equivalent identity when available;
- started and completed times where known;
- execution mode: progressive, retrospective retrofit, replay, or rerun;
- investigators and assistance status;
- artifact inventory with path, type, state, and purpose;
- raw/check directories and their preservation policy;
- baseline version;
- decision version or manual method identity;
- schema status;
- known missing or unrecoverable artifact classes;
- superseded run or prior run relationship where applicable.

### Completion behavior

The manifest must identify every required logical artifact as:

- present;
- merged into another named artifact;
- not applicable;
- unavailable;
- unrecoverable;
- deferred because the run is still active.

## 6. `INVOCATION.json`

### Responsibility

Represent only what enters UpgradePilot at the beginning of the run.

### Must distinguish

- caller-supplied values;
- event-supplied values;
- generated runtime metadata;
- contextual values visible to a person but not actually supplied;
- required, conditional, and optional inputs;
- malformed, missing, or ambiguous input;
- policy or authorization context.

### Must not contain as starting input

- identities discovered later;
- upstream release evidence;
- target source analysis;
- CI evidence;
- final decision;
- semantic conclusions supplied merely to bypass future work.

### Useful fields

- invocation type;
- caller/actor type;
- repository locator;
- PR/change locator;
- event or request ID;
- requested responsibility;
- supplied policy constraints;
- authentication/access context without secrets;
- received time;
- unknowns at invocation;
- validation result.

## 7. `CASE_IDENTITY.json`

### Responsibility

Represent the exact case identity discovered and frozen after invocation.

### Useful content

- repository;
- PR or change reference;
- base branch and SHA;
- head branch and SHA;
- merge or closure identity as historical context;
- dependency/ecosystem;
- old and new versions or constraints;
- changed files;
- update producer;
- relevant event times;
- observation time;
- identity authorities;
- identity elements that remain unresolved;
- superseded proposal relationships.

### Invariants

- later repository state must not be silently merged into the frozen identity;
- shortened or guessed identifiers must remain unresolved;
- source-supplied strings must not be rewritten into unsupported semantics;
- changed files remain evidence associated with the snapshot, not the minimal
  identity itself.

## 8. `OPERATION_EVENTS.jsonl`

### Responsibility

Preserve the progressive material execution sequence.

### Append behavior

Append one record for each material operation or grouped operation. Do not rewrite
old records to make the investigation appear cleaner.

### Required information per material record

- operation ID;
- scenario and run ID;
- sequence number;
- event time or honest unknown-time marker;
- current question;
- why the question matters;
- current hypothesis or state;
- selected method;
- method-selection reason;
- alternatives not selected and reason;
- expected output;
- what success would and would not establish;
- stop, switch, or escalation condition;
- actor who proposed, approved, and performed the work;
- exact tool, API, command, model, source, configuration, or manual method;
- target identity and revision/time boundary;
- reads, writes, network access, code execution, and side effects;
- actual result state;
- raw/check artifact references;
- direct observation;
- interpretation summary;
- output;
- outcome;
- created/updated evidence, claim, interpretation, or finding IDs;
- next action and reason;
- approach status: complete, repeat, stopped, deferred, failed, or replaced;
- replacement operation ID where applicable.

### Routine grouping

Repeated safe lookups or mechanical navigation may be grouped. Grouping must not
hide a material failure, source change, method switch, or decision-changing
result.

## 9. `EVIDENCE_ITEMS.jsonl`

### Responsibility

Represent material external observations, preserved source material, generated
check results, and explicit evidence absence or failure.

### Evidence is not truth

An accepted evidence item establishes that the item was acquired or recorded and
is eligible for the stated use. It does not make every statement inside it true.

### Useful evidence record content

- evidence ID;
- scenario/run ID;
- producing operation ID;
- evidence kind;
- source/producer;
- acquisition path;
- exact source identity, revision, release, run, job, or timestamp;
- raw artifact or stable reference;
- bounded excerpt or structured observation;
- direct observation;
- evidence state;
- authority and allowed claims;
- what it cannot establish;
- integrity/hash information where useful;
- freshness and retention state;
- limitations;
- replacement or corroborating evidence IDs;
- downstream claim, finding, decision, and report references;
- superseded-by relationship where applicable.

### Open evidence-state vocabulary

Use real states, including when applicable:

- accepted;
- missing;
- inaccessible;
- stale;
- invalid;
- malformed;
- conflicting;
- rejected;
- unsupported;
- ambiguous;
- not applicable;
- expired;
- superseded;
- partially preserved;
- not independently corroborated.

Do not collapse distinct failure states merely to fit the existing M2 contract.

## 10. `CLAIMS_AND_INTERPRETATIONS.jsonl`

### Responsibility

Preserve meaning assigned to evidence without disguising transformations as raw
facts.

### Record types

A record may represent:

- an attributed source claim;
- a parser-derived claim;
- a model-derived claim;
- a human interpretation;
- a deterministic comparison;
- a contradiction assessment;
- a relevance assessment;
- a dependency-path interpretation;
- a CI-authority interpretation;
- another case-specific transformation.

### Useful content

- claim or interpretation ID;
- record type;
- source evidence IDs;
- operation/transformation ID;
- transformation actor and method;
- exact source statement where relevant;
- normalized meaning;
- authority level;
- grounding state;
- corroboration state;
- repository relevance;
- uncertainty;
- alternative explanations;
- limitations;
- downstream finding IDs;
- prior record and supersession reason.

### Mandatory distinctions

```text
source contains statement
≠ statement accurately extracted
≠ statement independently corroborated
≠ statement relevant to target
≠ statement permitted to affect decision
```

## 11. `FINDINGS.json`

### Responsibility

Represent case-level conclusions and limitations produced from evidence and
interpretations.

### Useful structure

- finding ID;
- statement;
- state;
- supporting evidence IDs;
- supporting claim/interpretation IDs;
- contradicting evidence or explanation IDs;
- repository and revision scope;
- direct or conditional nature;
- uncertainty and limitations;
- permitted decision effect;
- created/updated operation ID;
- prior finding state;
- supersession, narrowing, withdrawal, or contradiction reason.

### Finding states

Use open, case-driven states such as:

- corroborated;
- supported with limitation;
- unresolved;
- contradicted;
- irrelevant to the case;
- not yet corroborated;
- superseded;
- withdrawn;
- not applicable.

## 12. `BASELINE_RESULT.json`

### Responsibility

Preserve the transparent baseline result and compare it with the complete
investigation.

### Required content

- baseline version;
- allowed baseline inputs and their source;
- baseline feature values;
- baseline outcome;
- baseline reason codes and explanation;
- unknown or missing baseline inputs;
- full-investigation outcome;
- full-investigation reason/finding references;
- outcome changed: yes/no/unresolved;
- uncertainty changed;
- targeted action changed;
- limitation changed;
- explanation changed;
- cost/complexity difference;
- comparative assessment;
- reviewer status.

The baseline must not consume evidence outside the baseline specification.

## 13. `DECISION.json`

### Responsibility

Represent the current bounded maintainer decision and its state transitions.

### Useful content

- decision ID and version;
- scenario/run/frozen identity;
- decision method or policy identity;
- outcome;
- reason records with finding/evidence references;
- material limitations;
- unresolved questions;
- targeted checks;
- check IDs and exact purpose;
- why stronger and weaker outcomes are unjustified;
- human judgment required;
- transition on new evidence;
- prior decision and supersession relationship;
- decision status: provisional, current, superseded, disputed, or withdrawn;
- decision actor and reviewer.

### Outcome vocabulary

Use the clearest bounded action supported by the case. Current charter outcomes
include:

- merge after normal review;
- run targeted checks;
- investigate or block;
- defer;
- abstain.

Record a new candidate outcome only when the case genuinely requires it.

## 14. `MACHINE_REPORT.json`

### Responsibility

Represent what another system or API consumer would need from the completed run.

### It may include

- report identity and representation version;
- exact case identity;
- concise update summary;
- evidence references and states;
- material findings;
- decision and reasons;
- targeted checks;
- limitations and unresolved questions;
- provenance and transformation references;
- user action and follow-up state;
- review status;
- artifact links.

### Distinction

This is an external representation. It need not expose every internal operation
or every intermediate interpretation.

## 15. `HUMAN_REPORT.md`

### Responsibility

Contain only the maintainer-facing report that the future product should deliver.

### Required qualities

- exact case and revision;
- concise explanation of what changed;
- repository-specific relevance;
- evidence-supported findings;
- important missing or contradictory evidence;
- bounded recommendation;
- reasons;
- targeted next action;
- limitations;
- useful provenance references;
- no claim of objective safety.

`HUMAN_REPORT.md` is not the full scenario diary and must be understandable
without reading `CASE.md`.

## 16. `FOLLOW_UP_STATE.json`

### Responsibility

Represent what happens after the report and what should persist across reruns.

### Useful content

- current follow-up state;
- required or optional user action;
- responsible actor;
- action/check IDs;
- authorization needed;
- expected new evidence;
- transition on pass, failure, unavailable, inconclusive, rebase, or changed
  dependency resolution;
- rerun/replay trigger;
- prior/new run relationship;
- user action history;
- closure condition;
- state that remains unresolved.

## 17. `REVIEW_AND_OWNERSHIP.json`

### Responsibility

Keep execution completion, factual review, user acceptance, external confirmation,
and learner ownership distinct.

### Required dimensions

- execution status;
- factual review status;
- Ali review status;
- external/behavioral evaluation status;
- reviewers and review times;
- corrections and disputed items;
- AI contribution;
- Ali direction;
- Ali challenge or verification;
- independently performed work;
- capability evidence and stated depth;
- remaining AI dependence;
- approval or rejection of scenario conclusions.

### Prohibition

Do not infer Ali-owned capability from project ownership, approval, or an
AI-generated artifact.

## 18. `raw/`

### Responsibility

Preserve material source payloads or bounded captures needed for audit, replay,
or disappearance-risk control.

### Examples

- PR metadata subset;
- patch/diff;
- workflow definition;
- workflow job summary;
- downloaded log or error response;
- upstream changelog excerpt;
- package metadata;
- advisory record;
- resolver output;
- model response;
- API response subset.

### Naming

Use names that include evidence or operation IDs and a practical source label.
Record every raw file in the manifest and evidence item.

### Secrets and copyright

Do not preserve secrets, private data, restricted content, or excessive
copyrighted material. Use bounded excerpts and references when full preservation
is inappropriate.

## 19. `checks/`

### Responsibility

Preserve material commands, test outputs, comparison results, environment
snapshots, and diagnostic artifacts.

### Examples

- exact command record;
- dependency resolution or `pip freeze` output;
- unit/integration test output;
- static-analysis result;
- container build/run result;
- platform matrix;
- environment metadata;
- reproduction notes;
- failure log;
- comparison table or script output.

A command proposed but not executed must not have a fabricated check output. It
belongs in decision/follow-up state as a required future action.

## 20. Validation requirements

Before scenario completion:

1. parse every JSON file;
2. parse every non-empty JSONL line independently;
3. verify unique IDs within each run;
4. verify all cross-artifact references resolve or are explicitly external;
5. verify run/scenario/frozen identity consistency;
6. verify operation ordering is coherent;
7. verify every material evidence item has a producing operation or explicit
   imported/manual origin;
8. verify every material finding references evidence and interpretation;
9. verify every decision reason references findings or explicit limitations;
10. verify reports match the current decision and limitations;
11. verify superseded records remain discoverable;
12. verify missing/unavailable data was not invented;
13. verify artifact inventory matches actual files;
14. verify factual and ownership review states are explicit.

Record the validation method and result in the final operation event and
`RUN_MANIFEST.json`.

## 21. Progressive durability requirements

For a new scenario, repository history should demonstrate at least:

1. initial selected/frozen bundle;
2. one or more material investigation updates before final decision;
3. decision/report completion;
4. review/correction update where applicable.

This is a minimum natural progression, not a commit quota.

## 22. Retrofit rules for historical scenarios

S001 and S002 may be retrofitted, but the retrofit must not claim a historical
artifact existed when it did not.

### Required retrofit metadata

- execution mode: `retrospective_artifact_reconstruction`;
- reconstruction date;
- sources used to reconstruct;
- exact elements retained from original work;
- elements summarized from `CASE.md`;
- raw outputs not recoverable;
- timestamps not recoverable;
- confidence or completeness of each artifact;
- corrections and superseded statements.

### S001

Preserve:

- the original incorrect advisory-timing interpretation as superseded history;
- the corrected official dates;
- the fact that operation order was reconstructed;
- unrecoverable raw responses and exact operation times;
- the current recommendation and why it did not change.

### S002

Preserve:

- candidate screening before formal identity freeze;
- the HTTP 410 log-retrieval failure;
- exact operation/evidence IDs already represented;
- missing historical environment;
- likely-compatible but unproven finding;
- targeted-check transition state;
- any gap between narrative progressive structure and durable commit timing.

## 23. Discovery feedback

When a case shows that this artifact family is wrong or incomplete:

1. preserve the scenario evidence;
2. identify the missing or misleading logical boundary;
3. change this local specification before the next case where practical;
4. do not force old cases into a new shape without labeling the retrofit;
5. classify the change as stable candidate, conditional, or unresolved in
   `SCENARIO_COVERAGE.md`.

The bundle is a discovery instrument. Its purpose is to expose the future
system's real information lifecycle, not to make current documents look complete.