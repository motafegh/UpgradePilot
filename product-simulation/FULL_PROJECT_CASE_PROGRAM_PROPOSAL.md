# UpgradePilot Product-Simulation Full-Project Case Program Proposal

**Status:** Proposal — unadmitted and non-controlling  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-29  
**Scope:** Future use of `product-simulation/` as a selective full-project discovery, evaluation, and failure-modeling workspace  
**Authority:** None. This document does not change the Project Charter, route, live project position, accepted specifications, architecture, implementation, or historical case conclusions.

## 1. Purpose

This proposal preserves a candidate direction for the next phase of work under
`product-simulation/`.

The proposal is based on a broader product horizon than one implementation increment. It treats
UpgradePilot as a complete end-to-end dependency-update decision system whose final evidence needs
include:

```text
public Dependabot PR input
→ exact proposal and dependency identity
→ multi-source evidence acquisition
→ repository-specific context
→ evidence quality, authority, contradiction, and sufficiency
→ bounded recommendation, targeted checks, defer, or abstention
→ human- and machine-readable output
→ persistence, replay, supersession, diagnosis, and evaluation
→ security, recovery, reproducibility, and ownership evidence
```

The proposal does not authorize implementation of that complete flow. It defines how carefully
chosen future simulation cases could generate evidence useful to present and later product work.

## 2. Central correction

A future simulation case should not be selected only because it serves the smallest presently
implemented product slice.

The implementation route remains relevant to prioritization, but the responsibility horizon for
this workspace may be the full production-oriented UpgradePilot product when Ali explicitly
selects that broader discovery scope.

The proposed selection principle is:

> Select cases that create the highest cumulative product value across the end-to-end route while
> avoiding duplicate evidence, speculative breadth, and case-count accumulation.

A useful case may therefore investigate a responsibility that will be implemented later when:

- the uncertainty is material to final product behavior;
- existing cases cannot answer it;
- the evidence can influence a later contract, evaluation, method, failure model, or acceptance
  gate;
- the case can be bounded without silently designing or implementing the future system;
- the result remains useful even when the preferred hypothesis fails.

## 3. Proposed durable role of `product-simulation/`

Under this proposal, `product-simulation/` would become a:

> **Full-project discovery, evaluation, decision-calibration, and failure-modeling laboratory using
> real dependency-update cases and controlled variants.**

Its responsibilities would include:

1. finding real cases that expose product-relevant uncertainties;
2. preserving exact identity, evidence, provenance, decision boundaries, and limitations;
3. comparing a transparent baseline with richer investigation;
4. discovering which evidence changes or does not change a maintainer action;
5. exposing failure, degraded, contradiction, abstention, replay, and supersession needs;
6. producing reusable evaluation and acceptance evidence for later implementation stages;
7. revealing when a proposed capability, method, or artifact does not justify its cost.

It would not become:

- a second implementation directory;
- a duplicate roadmap or live-state tracker;
- a source of permanent product schemas by default;
- a random gallery of interesting pull requests;
- an obligation to create a new scenario for every product concern;
- a mechanism for pre-implementing future architecture;
- evidence that UpgradePilot is safe, reliable, production-ready, or independently owned.

`MEMORY.md` would remain the sole owner of live project position and continuation.

## 4. Preservation of the completed cycle

S001–S005 and the accepted D1 synthesis remain completed historical discovery evidence.

This proposal does not:

- reopen or rewrite those cases;
- change their frozen identity or retrospective/prospective status;
- erase inaccessible, failed, superseded, contradicted, or unresolved evidence;
- claim that their conclusions prove automated product behavior;
- infer representative coverage from five contrasting cases;
- reactivate historical M2 work.

Future work would extend the case program only where a new uncertainty is materially different
from the completed evidence.

## 5. Case-value model

A candidate case should be judged through several dimensions rather than immediate implementation
usefulness alone.

A practical qualitative model is:

```text
case value =
  near-term implementation usefulness
+ future route leverage
+ production-risk coverage
+ decision novelty
+ evaluation reuse
+ reproducibility
+ learning and ownership value
− duplication
− acquisition and preservation cost
− speculative complexity
− ceremony burden
```

The formula is not a numerical product rule. It is a disciplined comparison aid.

### 5.1 Near-term implementation usefulness

Does the case clarify an evidence source, contract, comparison, orchestration rule, failure state,
or output already close to implementation?

### 5.2 Future route leverage

Can the same case later support acquisition robustness, repository context, persistence, replay,
evaluation, method comparison, security, hardening, or ownership proof?

### 5.3 Production-risk coverage

Does the case expose a failure that could produce a wrong action, stale result, unsupported claim,
lost evidence, unsafe operation, unrecoverable run, or misleading report?

### 5.4 Decision novelty

Does the case add a genuinely missing decision transition, such as:

- merge to targeted checks;
- targeted checks to block;
- recommendation to defer;
- recommendation to abstain;
- dependency conclusion separated from PR action;
- unchanged action with materially different authority or explanation?

### 5.5 Evaluation reuse

Can the case become a deterministic fixture, replay case, temporal comparison, baseline arena item,
adversarial variant host, property test seed, or held-out evaluation example?

### 5.6 Evidence feasibility

Can public evidence be preserved lawfully, safely, minimally, and with sufficient exact identity?

### 5.7 Negative-result value

Would the case still teach something useful if no decision change, API impact, source conflict, or
method advantage is found?

## 6. Existing coverage assessment

The following assessment concerns manual discovery evidence, not implemented capability.

| End-to-end responsibility | Existing evidence | Coverage assessment |
|---|---|---|
| Exact PR, revision, dependency, and run identity | Repeated across S001–S005 | Strong |
| Observation, interpretation, finding, and decision separation | Repeated manual bundles | Strong |
| Transparent-baseline comparison | Same-action, baseline-sufficient, and baseline-wrong cases | Strong |
| CI authority | Relevant green, skipped relevant CI, actual failure, and matrix evidence | Strong |
| Dependency role and repository relevance | Transitive, direct, adapter, lock, and test paths | Moderate to strong |
| Stopping and non-activation | S004 directly exercises early stopping | Strong |
| Decision-changing repository context | S005 changes the baseline action | Strong |
| Upstream authority and provenance | Package, release, advisory, and artifact evidence appear | Moderate |
| Honest defer or abstain outcome | No central completed case | Absent |
| Changed PR head and stale-evidence invalidation | Supersession appears, but no complete lifecycle | Weak |
| Partial acquisition, retry, and recovery | Isolated failures exist, but no complete recovery model | Weak |
| Contradictory authoritative sources | Not directly exercised | Absent |
| Persistent runs, idempotency, and query behavior | Not exercised | Absent |
| Deterministic replay after source disappearance | Not exercised end to end | Absent |
| Decision-time versus retrospective evidence | Historical correction exists, but no designed comparison | Weak |
| Adversarial evidence and prompt injection | Not exercised | Absent |
| Native wheels, platforms, and compiled dependencies | Not exercised | Absent |
| External ecosystem baseline comparison | Internal transparent baseline only | Weak |
| Representative corpus and adjudication | Cases are contrasting, not representative | Weak |
| Independent diagnosis and owner capability | Some review evidence, limited central proof | Weak |

This coverage suggests that additional cases can be justified, but only through selective admission.

## 7. Full-project responsibility map

Future case selection should consider the complete route without claiming that all responsibilities
are already admitted.

### 7.1 Public vertical slice

Potential evidence needs:

- real public locator behavior;
- exact PR and revision identity;
- complete changed-file acquisition;
- dependency identity;
- exact-head CI authority;
- official package and upstream evidence;
- bounded recommendation or abstention;
- concise human and machine outputs.

### 7.2 Acquisition and replay robustness

Potential evidence needs:

- source unavailable and source changed states;
- timeout, rate limit, malformed response, pagination, and partial-success behavior;
- credential and anonymous-access differences;
- retries, idempotency, and duplicate prevention;
- raw preservation and deterministic replay;
- recovery after interrupted acquisition;
- stale evidence and changed-head handling.

### 7.3 Repository-specific context and decision support

Potential evidence needs:

- direct, transitive, development, optional, and tool dependencies;
- version constraints and lock resolution;
- repository imports, calls, configuration, and generated artifacts;
- API and behavior changes;
- CI, test, platform, and runtime relevance;
- policy-sensitive actions;
- targeted checks;
- stopping, defer, and abstention.

### 7.4 Persistence, diagnosis, and evaluation

Potential evidence needs:

- immutable run and evidence identity;
- supersession without overwriting history;
- query and report reconstruction;
- source and transformation lineage;
- deterministic replay comparisons;
- corpus versioning and adjudication;
- baseline and method comparison;
- latency, cost, error, abstention, and unsupported-claim measurement.

### 7.5 Evidence-gated experiments

Potential evidence needs:

- graph methods versus simpler context methods;
- deterministic rules versus policy engines;
- learned ranking or selective prediction;
- grounded LLM extraction and synthesis;
- single-agent versus multi-agent investigation;
- queue, workflow, service, or deployment experiments;
- measured value compared with complexity and replacement cost.

### 7.6 Hardening and closure

Potential evidence needs:

- representative normal, failure, changed, early-stop, and recovery cases;
- secure configuration and credential behavior;
- reproducible installation and operation;
- failure diagnosis and recovery instructions;
- report truthfulness and limitation disclosure;
- Ali-controlled modification, test, diagnosis, and explanation.

## 8. Proposed case forms

Not every future product concern should become a complete S006-style narrative bundle.

### 8.1 Full real PR scenario

Use when repository-specific evidence, source authority, context, or maintainer action is central.

Typical outputs may include a complete scenario bundle, frozen baseline, material checkpoints,
findings, decision, reports, and review state.

### 8.2 Multi-snapshot scenario

Use when the same logical case must be compared across time or revision.

Examples:

- PR head A versus head B;
- original proposal versus Dependabot supersession;
- decision-time evidence versus later retrospective evidence;
- source available versus later removed or corrected;
- policy version A versus policy version B.

A multi-snapshot case must preserve separate run and evidence identity. It must not overwrite the
older state.

### 8.3 Controlled case variant

Use when a deterministic failure or recovery behavior can be attached to a real host case without
requiring a new full scenario.

Examples:

- timeout;
- rate limit;
- malformed JSON;
- truncated pagination;
- missing tag;
- conflicting package identity;
- interrupted acquisition;
- duplicated retry result;
- broken report reference.

### 8.4 Adversarial or evaluation caselet

Use for narrow security, invariant, method-comparison, or property-testing questions.

Examples:

- prompt injection inside release notes;
- instruction-like PR text;
- malicious branch names;
- misleading logs;
- reordered evidence;
- stale evidence reclassification;
- contradictory claims;
- malformed model output;
- unsupported report citations;
- irrelevant evidence intended to change a decision.

### 8.5 Form-selection rule

Use the smallest case form that preserves the material evidence lifecycle.

A full case is excessive when a controlled variant answers the question. A tiny caselet is
insufficient when the uncertainty depends on repository-specific context, source authority,
temporal history, or a real maintainer action.

## 9. Ranked full-case families

The following ranking is a proposal for comparison, not a committed sequence.

Scores are planning estimates out of 100 combining route leverage, production-risk relevance,
decision novelty, evaluation reuse, near-term usefulness, public reproducibility, and
non-duplication.

| Rank | Full-case family | Indicative score | Principal value |
|---:|---|---:|---|
| 1 | Conflicting or degraded source authority producing defer or abstention | 95 | Missing action class; source authority, contradiction, sufficiency, and honest stopping |
| 2 | Changed head, rebase, or supersession with rerun | 94 | Stale evidence, immutable identity, replay, persistence, idempotency, and report lineage |
| 3 | Direct runtime API or behavioral break with target usage | 88 | Upstream change connected to repository code, tests, CI, and a targeted check |
| 4 | Decision-time versus retrospective evidence | 86 | Temporal leakage, hindsight bias, source availability, and evaluation validity |
| 5 | Artifact-provenance regression, yanked release, or source mismatch | 83 | Supply-chain identity, degraded verifiability, and security-sensitive action |
| 6 | Python, platform, native-wheel, or compiled-extension support gap | 79 | Operating-system, architecture, ABI, and environment-specific evidence |
| 7 | Dynamic, plugin, reflection, or generated-code usage | 77 | Static-analysis limitations and disciplined unresolved output |
| 8 | Multiple dependency changes or ambiguous requirement forms | 74 | Supported-boundary behavior and refusal to guess |

The ranking should change when candidate evidence quality, duplication, or cost changes.

## 10. Ranked controlled caselet families

| Rank | Controlled family | Best host |
|---:|---|---|
| 1 | Prompt injection and instruction-like external content | Semantic extraction or synthesis case |
| 2 | Timeout, rate limit, malformed JSON, truncated pagination, partial success | Acquisition-rich case |
| 3 | Worker interruption, retry, duplicated event, idempotent recovery | Multi-source case after run-state behavior exists |
| 4 | Evidence deletion, stale marking, reordered records, replay mismatch | Persisted and replayable case |
| 5 | Broken evidence references, human/machine report disagreement, lineage corruption | Completed report case |
| 6 | Property-based evidence and policy mutation | Cross-case deterministic corpus |

These caselets should preserve untrusted-content boundaries and must not execute target repository
code merely for investigation.

## 11. Recommended first wave

The proposed first wave is three full cases with attached controlled variants.

### 11.1 Case A — Authority degradation and honest abstention

#### Candidate characteristics

Find a public Python Dependabot PR where one or more of these conditions can be established:

- upstream source identity cannot be resolved cleanly;
- package metadata and publisher provenance disagree;
- an expected release or tag is absent, ambiguous, or mismatched;
- official source claims conflict;
- evidence required for a defensible action is inaccessible or insufficient;
- a copied Dependabot summary cannot be elevated to independent authority.

#### Product path exercised

```text
valid PR and dependency identity
+ degraded, conflicting, or insufficient upstream authority
→ explicit uncertainty and evidence state
→ defer or abstain
→ exact recovery request, missing evidence, or stop reason
```

#### Cross-stage value

- near-term upstream evidence and claim authority;
- acquisition failure and recovery;
- contradiction preservation;
- evidence sufficiency;
- defer and abstain semantics;
- report limitations;
- evaluation of unsupported confidence.

#### Useful negative result

If no contradiction exists, the case can still establish the minimum source set and what source
combination is actually sufficient.

### 11.2 Case B — Changed-head and supersession lifecycle

#### Candidate characteristics

Use a PR with multiple meaningful head revisions, a rebase that changes evidence, or one Dependabot
proposal superseded by another.

#### Product path exercised

```text
run at head A
→ evidence and recommendation A
→ head changes or proposal is superseded
→ evidence from A becomes stale for B
→ new run or explicit comparison
→ recommendation B
→ preserved relationship, difference, and supersession lineage
```

#### Cross-stage value

- exact snapshot identity;
- stale evidence invalidation;
- immutable history;
- new-run boundaries;
- idempotency;
- persistence and replay;
- report diffs;
- decision-time reconstruction;
- recovery after changed evidence.

#### Useful negative result

An unchanged action is still valuable when the explanation, authority, or missing evidence changes.

### 11.3 Case C — Direct behavior impact and targeted checks

#### Candidate characteristics

Find a Python dependency update where:

- upstream removes, changes, deprecates, or behaviorally modifies an API;
- the target repository imports, invokes, configures, or otherwise reaches the affected behavior;
- existing tests or CI cover only part of the relevant path or environment;
- one focused check could materially change the decision.

#### Product path exercised

```text
upstream behavioral change
→ observed target usage
→ mapped tests and CI authority
→ unresolved behavioral or environment gap
→ concrete targeted check
→ explicit pass/failure decision transition
```

#### Cross-stage value

- repository-specific impact analysis;
- API or behavior delta;
- static usage evidence;
- test and CI association;
- evidence sufficiency;
- counterfactual explanation;
- targeted-check planning;
- later graph, LLM, or learned-method evaluation.

#### Useful negative result

If the target does not reach the changed behavior, the case can prove a justified non-activation
path and stopping boundary.

## 12. Valuable later case families

The following remain valuable but should normally follow the first wave unless exceptionally strong
candidate evidence appears.

### 12.1 Decision-time versus retrospective evidence

Compare what was knowable at review time with evidence published later. This supports temporal
modeling, leakage control, retrospective evaluation, and honest historical claims.

### 12.2 Artifact provenance and yanked releases

Compare old and proposed artifacts through package hashes, source association, publish attestation,
yanked state, and release identity. Degraded provenance must not be described as compromise without
additional evidence.

### 12.3 Native and platform support

Exercise wheels, source distributions, operating systems, CPU architectures, Python ABI support,
compiled extensions, and CI platform gaps.

### 12.4 Dynamic usage

Exercise plugins, reflection, entry points, imports by string, generated code, optional extras, and
configuration-driven activation. Static non-observation must remain different from proof of absence.

### 12.5 Separate dependency conclusion and PR action

Test cases where the proposed dependency version is acceptable but the specific PR should not be
merged as-is, or where the dependency has a concern but the PR action is still a bounded targeted
check rather than immediate block.

### 12.6 Multiple or ambiguous changes

Exercise multiple package updates, range changes, lockfile-only updates, environment markers,
extras, editable sources, direct URLs, and unsupported requirement syntax without guessing.

## 13. Case-admission gate

Every candidate should answer the following before becoming a selected case.

| Gate | Required answer |
|---|---|
| Specific uncertainty | What exact product, evaluation, or failure-model question does the case test? |
| Material consequence | Which behavior, contract, decision, method, acceptance gate, or architecture choice could change? |
| Existing-case gap | Why can S001–S005 and accepted synthesis not answer it? |
| Cross-stage leverage | Which route responsibilities can reuse the result? |
| Evidence feasibility | Can exact public identity and sufficient durable evidence be preserved? |
| Baseline contrast | What would the transparent baseline see and miss? |
| Decision transition | What action, uncertainty, authority, or explanation could change? |
| Negative-result value | What useful result remains if the preferred hypothesis fails? |
| Security boundary | What untrusted content, credential, execution, privacy, or mutation risk exists? |
| Stop boundary | When does further investigation stop adding material value? |
| Correct form | Full scenario, multi-snapshot case, controlled variant, or evaluation caselet? |
| Cost proportionality | Is this the simplest adequate evidence mechanism? |

A candidate that cannot answer these questions should remain a note or be rejected rather than
becoming a case.

## 14. Proposed candidate-selection workflow

### Step 1 — Maintain an uncertainty inventory

List the small number of material uncertainties not covered by existing cases. Do not list every
future feature.

### Step 2 — Search for evidence-bearing candidates

Prefer public Python Dependabot PRs inside the supported product boundary. Candidate search should
look for evidence patterns, not merely repository popularity.

### Step 3 — Perform lightweight screening

For each candidate, record only enough to judge:

- exact repository and PR;
- dependency and proposal;
- material difference from existing cases;
- likely evidence sources;
- prospective status feasibility;
- expected decision or evaluation contrast;
- major acquisition or preservation risks.

### Step 4 — Compare candidates through the admission gate

Use a compact matrix rather than long preliminary narratives.

### Step 5 — Select one case form

Choose the smallest form that preserves the material lifecycle.

### Step 6 — Freeze the prospective baseline

Before deep investigation, record what the transparent baseline sees, its action, reasons,
uncertainty, and stopping rule.

### Step 7 — Investigate through material checkpoints

Record decisions and failures prospectively. Preserve inaccessible, contradictory, superseded, and
negative evidence.

### Step 8 — Stop on sufficiency

Do not investigate every possible source. Stop when the case question is answered, the result is
unresolvable within the safe boundary, or the next step would not change a material product
conclusion.

### Step 9 — Update synthesis selectively

Change cross-case synthesis only when a new finding materially changes the product model,
responsibility classification, artifact need, or evaluation design.

## 15. Proposed candidate-comparison matrix

A reusable screening matrix may use these columns:

| Field | Purpose |
|---|---|
| Candidate ID | Temporary screening identity |
| Repository and PR | Exact public locator |
| Dependency update | Package, old version, proposed version |
| Named uncertainty | Product question being tested |
| Why existing cases are insufficient | Non-duplication proof |
| Case form | Full, multi-snapshot, controlled variant, or caselet |
| Near-term usefulness | Relationship to close implementation responsibilities |
| Future-route leverage | Later responsibilities supported |
| Decision novelty | Missing action or explanation transition |
| Evidence sources | Expected authoritative and corroborating sources |
| Prospective feasibility | Whether investigation can begin before outcome knowledge |
| Baseline contrast | Expected simple-method result |
| Negative-result value | Useful outcome if hypothesis fails |
| Security and privacy risks | Untrusted content, credentials, execution, and data limits |
| Evidence durability | Ability to preserve exact references or lawful snapshots |
| Investigation cost | Expected effort and source complexity |
| Stop condition | Explicit stopping rule |
| Admission recommendation | Admit, reserve, reject, or needs more screening |

Scores may assist ranking, but written reasons should control the selection.

## 16. Artifact strategy

The existing scenario artifact ideas remain useful but should be proportional.

### 16.1 Full scenario bundle

A complete case may need:

- scenario overview;
- run manifest;
- invocation;
- case identity;
- operation events;
- evidence items;
- claims and interpretations;
- findings;
- transparent baseline result;
- decision;
- human report;
- machine report;
- follow-up and supersession state;
- review and ownership state;
- raw or durable evidence references;
- check executions, failure attribution, or stopping evaluation when activated.

### 16.2 No empty decorative artifacts

Do not create every possible file before the case demonstrates the need. A smaller case may combine
records when distinctions remain clear and validation is possible.

### 16.3 Conceptual, not permanent product schemas

Simulation records may reveal future product concepts, but they do not automatically become runtime,
persistence, API, or report contracts.

### 16.4 Raw preservation

Preserve raw evidence or durable source identity separately from normalized interpretations. Do not
rewrite source material to match the final conclusion.

## 17. Security and safety requirements

Future cases must treat all public evidence as untrusted data, including:

- PR titles and bodies;
- comments and branch names;
- diffs and repository files;
- workflow definitions and logs;
- release notes and changelogs;
- package metadata and artifact names;
- advisory text;
- generated AI content.

Future work must not:

- execute target repository code merely for inspection;
- install investigated dependencies without an explicitly approved isolated test;
- allow source text to become shell commands, file paths, policy, prompts, or tool authorization;
- expose access tokens or unrelated personal data;
- mutate, rerun, comment on, approve, close, or merge target repositories without exact current
  authorization;
- present source agreement, green CI, SemVer, package provenance, or model output as proof of safety.

Adversarial variants should be added only when they test a real admitted or candidate trust boundary.

## 18. Evaluation and reuse strategy

A well-selected case should support more than one narrative conclusion.

Potential reuse includes:

- deterministic regression fixtures;
- acquisition and recovery tests;
- replay and supersession tests;
- decision laws and property-based test seeds;
- evidence-sufficiency evaluation;
- report traceability evaluation;
- temporal leakage checks;
- external baseline comparison;
- graph, LLM, ML, and agent method comparison;
- cost and latency measurement;
- ownership and diagnosis exercises;
- public case gallery entries after evidence and claim review.

A complex method should be compared against the simplest credible baseline and retained only when it
creates measured decision, evidence, reliability, review, or operational value.

## 19. Governance realignment candidate

The repository presently describes `product-simulation/` primarily as completed historical
discovery evidence. Ali's broader intended use may justify a later minimal governance realignment.

That change is not performed by this proposal.

A future approved realignment could:

1. preserve S001–S005 and D1 synthesis as closed historical evidence;
2. authorize an ongoing but selectively admitted full-project case program;
3. define the four case forms;
4. permit cases to investigate later route responsibilities without activating implementation;
5. retain the material-uncertainty and non-duplication admission gate;
6. prohibit case-count accumulation, speculative architecture, and implementation control;
7. retain `MEMORY.md` as the sole live-state owner;
8. clarify when synthesis and coverage records should change;
9. preserve exact target-repository mutation and security boundaries.

Potential files for a later minimal change may include:

- `product-simulation/AGENTS.md`;
- `product-simulation/SIMULATION_GOVERNANCE_AND_PLAN.md`;
- `product-simulation/README.md`;
- `product-simulation/SCENARIO_COVERAGE.md`;
- one root orientation sentence if required for accurate navigation.

No governance file should be changed until Ali explicitly approves the exact realignment.

## 20. Branch strategy proposal

Parallel product implementation can change `main` frequently. Simulation proposal and case work
should avoid disrupting or being disrupted by those commits.

### 20.1 Proposal or governance work

Use one short-lived branch based on an exact inspected `main` commit.

Example:

```text
agent/product-simulation-case-program-proposal
```

### 20.2 Admitted full cases

Prefer one short-lived branch per case:

```text
agent/product-simulation-s006-<case-slug>
agent/product-simulation-s007-<case-slug>
```

### 20.3 Controlled variants

Variants may stay on the host case branch when they are part of the same evidence question.

### 20.4 Reconciliation rule

Before merging or applying a simulation change:

- compare against the latest `main`;
- preserve concurrent implementation work;
- reassess references to route, specifications, and source behavior;
- avoid copying live-state details into the simulation subtree;
- resolve only relevant conflicts;
- do not force-push or rewrite history.

A single long-lived simulation branch should be avoided because it would accumulate drift and make
later integration harder.

## 21. Non-goals

This proposal does not authorize:

- selecting S006;
- researching or mutating a target repository;
- changing the simulation governance;
- changing the project route or charter;
- changing `MEMORY.md`;
- implementing persistence, graphs, LLMs, ML, agents, queues, services, or deployment;
- creating complete future schemas;
- claiming representative evaluation;
- claiming production readiness;
- changing historical case conclusions.

## 22. Proposed decision sequence

A disciplined next sequence would be:

```text
preserve this proposal
→ review and revise the intended role of product-simulation
→ decide whether minimal governance realignment is needed
→ build an uncertainty and candidate-admission matrix
→ screen actual public PR candidates
→ compare candidates for Case A and Case B first
→ admit only one bounded case
→ freeze its baseline and prospective identity
→ investigate through material checkpoints
→ reuse the result across later implementation and evaluation work
```

## 23. Decisions reserved for Ali

Before work proceeds beyond this proposal, Ali should decide:

1. whether `product-simulation/` should formally become an ongoing full-project case laboratory;
2. whether the first change should be governance realignment or candidate screening;
3. whether Case A, Case B, and Case C remain the first-wave priorities;
4. whether one case should be admitted at a time;
5. whether controlled caselets live inside host scenarios or under a shared evaluation area;
6. when a proposal branch is ready to merge into `main`;
7. whether later case work should use pull requests or remain direct branch-to-main work after review.

## 24. Proposed summary

The proposed direction is:

```text
preserve S001–S005
→ broaden the selection horizon to the full production-oriented product
→ use the implementation route as one priority factor, not the workspace boundary
→ admit cases through material uncertainty, non-duplication, evidence feasibility, and cross-stage value
→ distinguish full scenarios, multi-snapshot cases, controlled variants, and adversarial caselets
→ prioritize:
   1. degraded or conflicting authority with defer/abstention
   2. changed-head or supersession lifecycle
   3. direct behavior impact with targeted-check planning
→ attach failure and adversarial variants proportionally
→ preserve security, stopping, provenance, replay, and claim boundaries
→ defer governance and implementation changes until explicitly approved
```

This document exists so the complete proposal can be reviewed, challenged, narrowed, and either
accepted, revised, or rejected without losing the reasoning that produced it.
