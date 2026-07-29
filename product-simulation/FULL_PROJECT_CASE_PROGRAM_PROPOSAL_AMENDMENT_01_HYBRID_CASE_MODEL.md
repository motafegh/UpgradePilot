# Amendment 01 — Hybrid Real-and-Synthetic Case Model

**Parent proposal:** [`FULL_PROJECT_CASE_PROGRAM_PROPOSAL.md`](FULL_PROJECT_CASE_PROGRAM_PROPOSAL.md)  
**Status:** Proposal amendment — unadmitted and non-controlling  
**Owner:** Ali Rajabi  
**Recorded:** 2026-07-29  
**Scope:** How future `product-simulation/` work may combine real public cases, captured evidence, controlled variants, authored synthetic scenarios, and generated evaluation cases  
**Authority:** None. This amendment does not change project governance, the route, `MEMORY.md`, implementation, accepted specifications, historical case conclusions, or target-repository permissions.

## 1. Purpose

The parent proposal established that `product-simulation/` may be useful as a selective full-project discovery, evaluation, decision-calibration, and failure-modeling laboratory.

This amendment adds one essential principle:

> **The future case program should use a controlled hybrid of real and synthetic evidence. Real cases establish realism and product relevance; synthetic cases establish isolation, reproducibility, rare-condition coverage, and systematic validation. Neither is a substitute for the other.**

The case program should not wait indefinitely for a public pull request that happens to contain every desired condition. It should also not build confidence from artificial cases that merely reproduce assumptions written by the same people who designed the implementation.

The intended loop is:

```text
real case reveals a product uncertainty
→ a controlled or synthetic case isolates the uncertainty
→ implementation or method behavior is tested deterministically
→ another real case validates external behavior
→ new real irregularities become controlled regression variants
```

## 2. Terms and distinctions

### 2.1 Untouched real case

A public repository, real Dependabot pull request, real revisions, real dependency files, real workflow evidence, and real upstream/package evidence are investigated without altering the material case conditions.

Primary uses:

- product discovery;
- external behavior validation;
- maintainer-value assessment;
- real source and repository irregularity discovery;
- transparent-baseline comparison;
- evidence that a condition actually occurs.

### 2.2 Captured real fixture

A preserved response, source document, workflow file, package record, or normalized record derived from a real source and used for deterministic replay.

A fixture is an input artifact, not automatically a complete case. Captured evidence proves only the preserved observation and the behavior exercised against it; it does not prove that live acquisition still works.

### 2.3 Mock

A test replacement that returns controlled responses or records calls at a narrow interface.

Example:

```text
first GitHub request → HTTP 429
second request → successful response
```

Mocks are suitable for interaction boundaries and branch behavior. They do not prove that the real external service behaves identically.

### 2.4 Fake or emulator

A behavioral substitute that implements a meaningful subset of an external system rather than returning one fixed response.

A fake GitHub-like service may support:

- multiple PR revisions;
- pagination;
- workflow runs;
- changed remote state;
- rate limits;
- missing resources;
- retries and duplicate requests.

A fake can exercise orchestration more realistically than a narrow mock, but it remains authored behavior.

### 2.5 Real-derived controlled variant

A real case is retained as the host, while one or a small number of named variables are deliberately changed.

Example:

```text
real PR identity
+ real changed files
+ real target declaration
+ real workflow structure
+ synthetically unavailable upstream release endpoint
```

This is often the preferred synthetic form because it combines real structural complexity with controlled discrimination.

### 2.6 Fully synthetic authored case

A deliberately created repository, PR history, dependency update, evidence set, failure sequence, policy, and expected result designed to exercise a product responsibility that is difficult, unsafe, or impractical to find publicly.

### 2.7 Generated or property-based case

Inputs and state transitions are generated from declared invariants rather than authored one by one.

Examples:

- evidence ordering permutations;
- stale/fresh transitions;
- missing-evidence combinations;
- contradictory claims;
- valid and invalid identities;
- stricter and weaker policy variants;
- retry and interruption sequences.

Generated cases are especially useful for deterministic decision laws, state machines, and validation boundaries.

## 3. Why real cases alone are insufficient

### 3.1 Rare conditions are difficult to locate on demand

Useful conditions may exist but be difficult to discover at the right time:

- a PR head changes during analysis;
- a release is yanked after an initial decision;
- a source fails after partial acquisition;
- authoritative sources conflict;
- the second page of an API response fails;
- a process is interrupted after one evidence item is persisted;
- malicious instruction-like content appears in evidence;
- a retry would duplicate previously accepted evidence.

Waiting for an ideal public example can block product learning and contract validation.

### 3.2 Real cases often combine too many variables

A real pull request may simultaneously contain incomplete CI, unusual requirements, several revisions, missing release notes, and ambiguous target usage. A controlled case can change one material variable while holding the rest stable.

### 3.3 Some failures should not be induced against real systems

The program must not deliberately exhaust quotas, mutate target repositories, corrupt real package metadata, trigger other projects' workflows, or publish adversarial content to reproduce a test condition.

### 3.4 Live evidence may disappear or drift

Logs expire, tags and releases can be edited, repositories can be archived, and pull requests can be rebased or superseded. Captured and synthetic cases allow deterministic replay after live evidence changes.

## 4. Why synthetic cases alone are insufficient

### 4.1 Synthetic cases can encode the designer's assumptions

A circular proof can occur:

```text
we invent the world
→ we invent the expected answer
→ we implement the behavior
→ our authored case passes
```

This establishes internal agreement, not external validity.

### 4.2 Artificial data is usually cleaner than public repositories

Real projects contain inconsistent metadata, historical residue, mixed dependency forms, indirect scripts, path filters, unusual naming, incomplete records, and ambiguous maintenance behavior. Synthetic cases omit these unless they are deliberately modeled from observed evidence.

### 4.3 Synthetic decisions can become policy hardcodes

An authored expected recommendation may reflect preference rather than a defensible maintainer decision. Synthetic cases are strongest for invariant, failure, recovery, security, state, and report behavior; they are weaker as sole evidence of recommendation usefulness.

### 4.4 External integrations still require live proof

A fake GitHub or PyPI service cannot establish that authentication, pagination, source schemas, network behavior, and identity reconciliation work against the real service.

## 5. Hybrid evidence ladder

Future case work should distinguish four evidence levels.

### Level 1 — Untouched real public cases

Best for:

- discovering unknown responsibilities;
- validating real integrations;
- testing repository-specific reasoning;
- assessing baseline and maintainer-action value;
- challenging authored assumptions.

### Level 2 — Real-derived controlled variants

Best for:

- isolating one failure or decision variable;
- creating deterministic regressions from real irregularities;
- testing counterfactuals;
- preserving realistic source and repository structure.

This should normally be the preferred synthetic level.

### Level 3 — Fully synthetic scenario systems

Best for:

- multi-revision repositories;
- source-conflict designs;
- temporal sequences;
- recovery and interruption;
- adversarial evidence;
- repository-code, test, CI, and policy relationships that must be deliberately controlled.

### Level 4 — Generated and property-based evaluation

Best for:

- invariant coverage;
- combination exploration;
- state-machine testing;
- shrinking defects to minimal examples;
- detecting behavior that hand-authored cases did not anticipate.

These levels are complementary. Passing a higher-numbered artificial level does not replace Level 1 external validation.

## 6. Simulation fidelity layers

Synthetic work should state which layer it simulates.

### 6.1 Data-level simulation

Controlled JSON, YAML, TOML, Markdown, logs, API bodies, and model outputs.

Suitable for:

- parsing and validation;
- malformed data;
- semantic extraction;
- schema shifts;
- misleading and adversarial content.

### 6.2 Service-level simulation

A mock or fake external source responds across multiple requests.

Suitable for:

- pagination;
- rate limits;
- timeouts;
- partial success;
- retries;
- changing remote state;
- authentication differences.

### 6.3 Repository-level simulation

A local Git repository contains commits, branches, tags, dependency declarations, code, tests, and workflow definitions.

Suitable for:

- base/head identity;
- rebases and supersession;
- target usage;
- changed files;
- test-to-code relationships;
- policy and runtime declarations.

### 6.4 Workflow-level simulation

A complete analysis progresses through acquisition, normalization, context, decision, reporting, and persistence while controlled failures are inserted between stages.

Suitable for:

- explicit run states;
- interruption and recovery;
- idempotency;
- duplicate prevention;
- partial progress;
- report consistency.

### 6.5 Temporal simulation

Evidence changes through a controlled timeline.

Example:

```text
T1 — PR head A and release evidence are available
T2 — PR rebases to head B
T3 — proposed artifact is yanked
T4 — advisory is published
T5 — maintainer adds a failing platform job
```

Suitable for:

- decision-time versus retrospective analysis;
- stale evidence;
- supersession;
- source drift;
- temporal leakage;
- reevaluation.

## 7. Permitted claims

### 7.1 A synthetic case may establish

- a defined condition can be represented;
- a contract or invariant is enforced under controlled input;
- a state transition is deterministic;
- a failure remains distinguishable from degradation or abstention;
- recovery avoids duplicate or lost trusted evidence;
- human and machine reports remain consistent;
- adversarial content does not cross a declared trust boundary;
- a method distinguishes authored semantic variations;
- a counterfactual input produces an expected rule transition.

### 7.2 A synthetic case cannot independently establish

- that the condition is frequent in public repositories;
- that real GitHub, PyPI, or package-manager behavior matches the fake;
- that maintainers find the recommendation useful;
- that a policy generalizes across repositories;
- that the corpus is representative;
- that production reliability is established;
- that a recommendation is objectively correct;
- that the complete public request-to-report flow works live.

### 7.3 A real case also has limits

A real case proves that one observed situation occurred and that the preserved investigation reached a bounded conclusion. One real case does not establish prevalence, universal behavior, objective safety, or representative product accuracy.

## 8. Pedigree and contamination control

Synthetic evidence must never be represented as observed public evidence.

Each future case or variant should identify at least:

```text
case_origin:
  real_public
  real_derived
  synthetic_authored
  generated

evidence_origin:
  live_observed
  captured_real
  mutated_real
  authored
  generated

evaluation_role:
  product_discovery
  integration_validation
  contract_validation
  failure_validation
  recovery_validation
  security_validation
  method_comparison
  regression
```

The exact runtime schema is not defined here. These are conceptual distinctions for simulation evidence.

Each synthetic case should also state:

- which facts came from a real host;
- which facts were authored or changed;
- the exact mutation;
- why the mutation is credible;
- the fidelity layer;
- the permitted claim;
- the external validation still required;
- whether expected behavior came from a stable invariant, an accepted policy, or a human hypothesis.

## 9. Case-selection preference

The proposed default order is:

```text
1. untouched real case when feasible and discriminating
2. real-derived controlled variant
3. fully synthetic case when isolation, safety, timing, or rarity requires it
4. generated variants for systematic contract coverage
```

The governing rule is:

> **Use the least artificial case that provides discriminating evidence safely, reproducibly, and proportionally.**

A real case should not be pursued at excessive cost merely to avoid simulation. A synthetic case should not be selected merely because it is easier to make pass.

## 10. Three complementary case tracks

### 10.1 Discovery track

Primarily untouched public cases.

Purpose:

- reveal unknown product responsibilities;
- evaluate real source and repository behavior;
- test product usefulness;
- challenge the transparent baseline;
- identify high-value simulation seeds.

### 10.2 Controlled simulation track

Real-derived or fully synthetic cases.

Purpose:

- isolate known uncertainties;
- reproduce rare conditions;
- test failures, recovery, state, and counterfactuals;
- validate trust boundaries;
- create stable regressions.

### 10.3 Evaluation track

Curated and generated variants.

Purpose:

- regression coverage;
- property and state-machine testing;
- adversarial evaluation;
- method comparison;
- coverage measurement;
- held-out evaluation where defensible.

Results from these tracks must not be pooled as though they carry equal evidential authority.

## 11. High-value hybrid scenarios

### 11.1 Changed head and stale evidence

Preferred form:

- synthetic multi-revision repository for deterministic lifecycle coverage;
- later validation against one or more real rebased or superseded Dependabot PRs.

Expected path:

```text
head A acquired
→ evidence accepted for A
→ head changes to B
→ A evidence cannot silently justify B
→ new run or explicit comparison
→ prior history preserved
```

### 11.2 Conflicting upstream authority

Preferred form:

- real package/PR host when a genuine authority problem exists;
- controlled variants for missing tag, mismatched repository, conflicting changelog, or unavailable provenance.

Expected behavior:

- preserve each source claim and identity;
- avoid guessing a preferred source;
- degrade, defer, or abstain according to the admitted policy;
- state the exact evidence required to continue.

### 11.3 Partial acquisition

Preferred form:

- real host case plus service-level variants.

Variant examples:

- first page succeeds and second page fails;
- PR and changed files succeed but workflow definition is unavailable;
- PyPI succeeds but upstream release times out;
- authenticated request fails while anonymous public access succeeds;
- retry returns previously observed evidence.

### 11.4 Prompt-injection and instruction-like evidence

Preferred form:

- authored adversarial evidence attached to a real-derived semantic case.

Expected behavior:

- preserve the source content as untrusted evidence;
- do not execute or obey its instructions;
- do not erase the evidence merely because it is adversarial;
- apply deterministic authority and permitted-effect controls.

### 11.5 Idempotent recovery

Preferred form:

- workflow-level synthetic case after persistence and run-state responsibilities are admitted.

Expected path:

```text
evidence E1 persisted
→ process interrupted
→ run resumes
→ same source is reacquired
→ no duplicate trusted evidence
→ provenance and recovery state remain visible
```

### 11.6 Targeted-check counterfactual

Preferred form:

- real repository context with authored pass/fail check outcomes.

Expected path:

```text
current evidence → run targeted checks
synthetic result A passes → less cautious action may become supportable
synthetic result B fails → investigate or block
```

The synthetic result validates decision-transition logic; it does not claim that the real check passed or failed.

## 12. Effect on the proposed first wave

### Case A — Authority degradation and honest abstention

Recommended hybrid:

- search first for a real public authority-degradation case;
- use real-derived variants to cover unavailable, ambiguous, mismatched, and contradictory source states;
- reserve a fully synthetic source-conflict case if no public case provides enough controlled evidence.

### Case B — Changed-head and supersession lifecycle

Recommended hybrid:

- use a synthetic repository and temporal sequence for deterministic first coverage;
- preserve one or more real rebased/superseded PRs as external validation candidates;
- do not wait for a perfectly timed live head change before learning the lifecycle.

### Case C — Direct behavior impact and targeted checks

Recommended hybrid:

- use a real public PR and repository for upstream-to-target relevance;
- attach authored check-result counterfactuals;
- later use generated variations for coverage and policy sensitivity.

## 13. Admission additions for synthetic cases

In addition to the parent proposal's case-admission gate, synthetic work should answer:

| Gate | Required answer |
|---|---|
| Why simulation is needed | What timing, safety, isolation, rarity, or reproducibility problem prevents an adequate untouched real case? |
| Realism basis | Which observed behavior, official contract, or real case makes the authored condition credible? |
| Controlled variables | What exactly is changed, and what remains fixed? |
| Fidelity layer | Data, service, repository, workflow, or temporal? |
| Oracle authority | Is expected behavior derived from an invariant, accepted policy, source contract, or hypothesis? |
| Permitted claim | What may this case establish? |
| External validation debt | What still requires a live or untouched real case? |
| Contamination control | How will authored evidence remain distinguishable from observed evidence? |
| Simplest adequate mechanism | Is a fixture or variant sufficient, or is a full synthetic system justified? |

## 14. Security boundaries

Synthetic capability does not authorize unsafe execution.

Future work must not:

- clone and execute arbitrary target code merely to make a scenario realistic;
- install investigated packages outside an explicitly approved isolated test;
- include real credentials or private data in fixtures;
- reproduce secrets from public logs;
- publish malicious content to an external project;
- let authored evidence become shell commands, file paths, prompts, policy, or tool authorization;
- treat a fake service as proof of real authentication or permission behavior.

Security-oriented cases should use the minimum artificial content necessary to test the boundary.

## 15. Research and selection companions

This amendment should be read with:

- [`REAL_WORLD_SCENARIO_PREVALENCE_CATALOG.md`](REAL_WORLD_SCENARIO_PREVALENCE_CATALOG.md) — evidence-informed occurrence bands and scenario inventory;
- [`CASE_SELECTION_AND_COVERAGE_MATRIX.md`](CASE_SELECTION_AND_COVERAGE_MATRIX.md) — admission, scoring, case-form, and cross-stage comparison method.

These companion documents remain proposal-support artifacts, not governance or implementation authority.

## 16. Decisions reserved for Ali

Before synthetic work becomes an active case program, Ali should decide:

1. whether this hybrid model is accepted as the intended proposal direction;
2. whether a future governance realignment should recognize the three case tracks;
3. whether controlled variants live inside host scenarios or under a shared evaluation area;
4. whether synthetic repositories are committed as source-like fixtures, generated during tests, or preserved separately;
5. what minimum real-world validation is required before a synthetic result influences a product claim;
6. whether the first admitted work should be a real candidate screen or the synthetic changed-head lifecycle.

## 17. Proposed summary

```text
real cases establish realism and product value
+ captured evidence establishes replay
+ controlled variants establish isolated failure behavior
+ synthetic systems establish rare and temporal coverage
+ generated cases establish invariant breadth
→ explicit pedigree and claim limits
→ real validation remains required
```

The hybrid model allows UpgradePilot to investigate difficult production conditions without waiting for perfect public cases, while preventing authored evidence from masquerading as real-world proof.