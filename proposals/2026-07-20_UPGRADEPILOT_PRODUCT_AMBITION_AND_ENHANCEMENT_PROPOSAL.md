# UpgradePilot Product Ambition and Enhancement Proposal

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-20  
**Status:** Exploratory future proposal — preserved, non-controlling, and not admitted  
**Origin:** Consolidated product, learning, production-readiness, and technical-ambition audit  
**Authority:** None. This proposal does not authorize implementation, architecture, dependencies, experiments, infrastructure, roadmap changes, or capability claims.  
**Current-work effect:** None. M2-S01 and its pre-code gate remain controlling and unchanged.

## 1. Purpose

This document preserves ambitious candidate ideas for making UpgradePilot:

- more powerful as a maintainer decision product;
- more valuable as a learning-by-building journey;
- more production-oriented end to end;
- more distinctive as a flagship portfolio project;
- more interesting and motivating to build;
- richer in Python, data, ML, AI, security, reliability, systems, and operations exposure.

The existing project agreements remain the baseline. This proposal does not reopen the agreed:

- primary user;
- public Python and Dependabot boundary;
- supported action classes;
- evidence and uncertainty doctrine;
- 90-day identity;
- learning-before-implementation method;
- current route and active M2-S01 responsibility.

The ideas below are candidates, not requirements. Each idea must later be admitted, narrowed, deferred, rejected, or superseded through the governing process.

## 2. Executive assessment

UpgradePilot already has a stronger intellectual foundation than most portfolio projects because it is centered on:

- one real maintainer decision;
- multiple imperfect evidence sources;
- explicit provenance;
- explicit missing, stale, inaccessible, invalid, rejected, and conflicting evidence states;
- abstention instead of synthetic certainty;
- a transparent baseline before ML, graphs, LLMs, or agents;
- temporal snapshots and replay;
- asymmetric decision costs;
- held-out evaluation and contamination control;
- negative-result acceptance;
- production-oriented reliability;
- increasing learner ownership;
- advanced-system experiments attached to a real workload.

The correct evolution is not merely to add more tools. It is to transform UpgradePilot from an evidence-backed report generator into an:

> **Evidence-driven dependency-update decision laboratory and maintainer investigation system.**

A stronger future working definition is:

> **UpgradePilot reconstructs a dependency update as it existed at decision time, verifies the identity and trustworthiness of its evidence, maps upstream changes to repository-specific usage and test coverage, determines whether current evidence is sufficient, selects the next most valuable investigation step, and produces a reproducible, policy-aware recommendation with a complete decision trace.**

This is a candidate refinement of the product thesis, not an accepted charter change.

## 3. Strategic product evolution

The current decision flow can be strengthened around five questions:

1. What changed?
2. Where can that change affect this repository?
3. Which evidence supports or weakens that possibility?
4. What should the maintainer do next?
5. What additional evidence would most efficiently change or confirm the decision?

The fifth question is especially important.

A passive report says:

> Here is the available evidence and my conclusion.

A stronger decision-intelligence product says:

> Here is the current conclusion, what remains uncertain, the most valuable next check, what that check could prove, and how each possible result would change the decision.

The strongest future product identity should be organized around three defining capabilities:

1. **Upgrade Impact Graph** — what could this update affect in this repository?
2. **Decision-Time Machine** — what could the maintainer actually know at the decision point?
3. **Targeted Check Planner** — what is the next most valuable action for reducing uncertainty?

The remaining ideas can connect to those three.

---

# Part I — Central product-capability proposals

## 4. Upgrade Impact Graph

### 4.1 Concept

Construct a graph connecting:

```text
dependency update
→ upstream release changes
→ changed, removed, deprecated, or behaviorally modified API symbols
→ target repository imports and references
→ configuration usage
→ tests touching the relevant paths
→ CI jobs executing those tests
→ supported environments
→ evidence gaps
→ recommended checks
```

A dependency graph says:

> Package A depends on package B.

An impact graph asks:

> Which changed behavior in B may matter to A, where is that behavior used, which tests or environments cover it, and what remains unresolved?

### 4.2 Example

```text
Changed symbol:
package.client.PackageClient.old_method

Downstream repository evidence:
- src/search/indexer.py imports PackageClient
- src/search/indexer.py calls old_method
- tests/search/test_indexer.py covers normal output
- no test covers empty-input serialization
- CI executes Python 3.10–3.12
- repository metadata still declares Python >=3.8

Impact assessment:
- direct API usage: observed
- removed symbol: observed
- Python 3.8 policy conflict: observed
- relevant behavioral coverage: partial
- production-path reachability: unresolved

Recommended action:
Investigate or block

Targeted checks:
1. run indexer tests against the proposed package;
2. add an empty-input serialization regression;
3. test or formally drop Python 3.8.
```

### 4.3 Candidate technical responsibilities

- upstream API surface extraction;
- old-versus-new API comparison;
- import and qualified-name analysis;
- repository symbol-usage mapping;
- configuration-key mapping;
- dependency-path construction;
- test-to-code association;
- CI-workflow and test-environment interpretation;
- graph traversal and explanation;
- static-versus-dynamic reachability boundaries.

### 4.4 Learning value

- Abstract Syntax Tree — AST analysis;
- Concrete Syntax Tree — CST analysis;
- imports and qualified names;
- static analysis;
- API compatibility;
- graph modeling and traversal;
- test coverage limitations;
- CI scope;
- evidence boundaries;
- changed-behavior reasoning.

### 4.5 Candidate tools

- Python `ast`;
- LibCST for source-preserving parsing and metadata;
- Griffe for static Python API representation and breaking-change comparison;
- NetworkX or a small explicit graph representation before a graph database;
- coverage and test metadata only when acquired safely and lawfully.

A tool is not admitted merely because it appears here.

## 5. Decision-Time Machine

### 5.1 Concept

Support two explicit analysis modes.

**Decision-time mode**

Use only evidence that was available when the maintainer decision was being made.

**Present-time retrospective mode**

Use currently available evidence while clearly identifying information that appeared later.

### 5.2 Why it matters

Historical evaluation can leak future information:

- a vulnerability may be published later;
- release notes may be corrected later;
- a repository may add tests later;
- a release may be yanked later;
- maintainers may describe a regression after the original review;
- a later patch release may reveal the original problem;
- present-day package metadata may differ from the original state.

Without decision-time reconstruction, a system can appear intelligent because it knows the future.

### 5.3 Candidate temporal contract

For material facts, preserve:

- `source_valid_time`;
- `observed_at`;
- `available_at`;
- `superseded_at`;
- repository revision;
- package or artifact version;
- retrieval snapshot;
- content hash;
- retrospective-only indicator.

This introduces practical bitemporal reasoning:

- **valid time** — when the source says the fact applied;
- **system or observation time** — when UpgradePilot observed or stored it.

### 5.4 Example output

```text
Decision reconstructed as of:
2026-03-02 14:30 UTC

Excluded retrospective evidence:
- advisory published 12 days later
- maintainer regression comment posted 2 days later
- new CI workflow added 3 weeks later

Decision-time action:
Run targeted checks

Retrospective action:
Investigate or block

Why the decision changed:
Later vulnerability and regression evidence were unavailable during review.
```

### 5.5 Learning value

- temporal data modeling;
- hindsight bias;
- data leakage;
- bitemporal databases;
- snapshots and event history;
- retrospective evaluation;
- reproducibility;
- historical source drift.

## 6. Targeted Check Planner

### 6.1 Concept

Expand “suggest targeted checks” into a real planning subsystem.

```text
unresolved evidence
→ enumerate candidate checks
→ identify which uncertainty each check addresses
→ estimate effort, latency, environment, and risk
→ estimate expected information value
→ rank checks
→ show how each possible result changes the decision
```

### 6.2 Example

| Rank | Check | Resolves | Estimated effort | Possible decision effect |
|---:|---|---|---:|---|
| 1 | Run existing search-record regression tests against the new dependency | Behavioral compatibility | 3 min | Pass may permit normal review; failure blocks |
| 2 | Add generated-record schema assertion | Silent-output risk | 10 min | Detects malformed records missed by existing tests |
| 3 | Run the full test suite | Broad unknown failures | 18 min | Useful but less targeted |
| 4 | Inspect every upstream commit manually | General change uncertainty | 45 min | High cost and uncertain information gain |

### 6.3 Value of Information

The planner can introduce **Value of Information — VOI**:

```text
check priority =
expected decision improvement
× consequence weight
× evidence relevance
÷ investigation cost
```

The first version can be deterministic and inspectable. It does not require a probabilistic model.

### 6.4 Candidate check contract

Each proposed check should state:

- check identifier;
- exact command or review action when known;
- uncertainty addressed;
- expected output categories;
- execution environment;
- estimated time or cost;
- evidence produced;
- result-to-decision mapping;
- limitations and false-reassurance risk.

### 6.5 Strategic value

Targeted-check ranking may become a more defensible learned target than a universally correct five-class recommendation because maintainers may disagree on the final action while still agreeing about which evidence would be useful next.

### 6.6 Learning value

- decision theory;
- information gain;
- active learning;
- ranking;
- test selection;
- asymmetric costs;
- workflow design;
- uncertainty reduction.

## 7. Maintainer Policy Profiles

### 7.1 Concept

Represent repository policy explicitly rather than hiding it inside general rules.

The same evidence may justify different actions when repositories differ in:

- supported Python versions;
- required platforms;
- release freeze;
- dependency scope;
- license policy;
- security policy;
- test requirements;
- update policy;
- artifact-provenance expectations;
- tolerance for development-only dependency risk.

### 7.2 Candidate policy example

```yaml
repository_policy:
  supported_python:
    - "3.10"
    - "3.11"
    - "3.12"

  required_platforms:
    - linux
    - windows

  dependency_scopes:
    runtime:
      minimum_ci_coverage: required
    development:
      minimum_ci_coverage: preferred

  prohibited_licenses:
    - AGPL-3.0-only

  update_policy:
    major: investigate
    minor: contextual
    patch: normal_review_unless_signals

  provenance:
    verified_publish_attestation: preferred

  release_freeze:
    active: false
```

### 7.3 Policy-diff experience

```text
With default policy:
Run targeted checks

With strict runtime policy:
Investigate or block

Decision-changing policy:
Python 3.8 support is mandatory, but upstream dropped it.
```

### 7.4 Candidate implementation sequence

1. typed Python structures;
2. versioned YAML or JSON;
3. transparent decision table;
4. policy-diff tests;
5. optional comparison with policy-as-code technology such as Open Policy Agent — OPA.

OPA is a later comparison candidate, not an automatic architecture choice.

### 7.5 Learning value

- policy-as-code;
- configuration versus behavior;
- separation of evidence and policy;
- versioned decision rules;
- testable governance;
- explainable rule evaluation.

## 8. Multidimensional Uncertainty Profile

### 8.1 Concept

Avoid collapsing uncertainty into a single percentage.

Candidate uncertainty dimensions:

| Dimension | Meaning |
|---|---|
| Identity uncertainty | Are package, PR, versions, and revisions correctly identified? |
| Source-availability uncertainty | Are material sources missing or inaccessible? |
| Source-trust uncertainty | Is the source authentic and credible? |
| Applicability uncertainty | Does the upstream change affect repository usage? |
| Coverage uncertainty | Do tests and CI cover the relevant behavior and environments? |
| Temporal uncertainty | Was the evidence available at decision time? |
| Policy uncertainty | Is repository policy known? |
| Label uncertainty | Would reasonable adjudicators agree? |
| Model uncertainty | How stable is a learned prediction? |
| Synthesis uncertainty | Did an LLM omit, contradict, or invent a claim? |

### 8.2 Example

```text
Overall action: Run targeted checks

Uncertainty profile:
Identity             low
Source availability  medium
Artifact provenance  high
Repository usage     low
Behavior coverage    high
Policy               low
Label disagreement   medium
```

### 8.3 Uses

- abstention;
- evidence-sufficiency evaluation;
- check ranking;
- error analysis;
- calibration;
- dashboards;
- ML features;
- human review.

## 9. Evidence Sufficiency Engine

### 9.1 Concept

Assess whether the combination of evidence is sufficient for a particular action.

Example candidate condition for `merge_after_normal_review`:

```text
identity_valid
AND no_material_conflicts
AND required_repository_policy_known
AND no_observed_block_signal
AND relevant_ci_evidence_available
AND repository_usage_context_sufficient
AND no_high-impact_uncovered_api_change
```

Candidate condition for `run_targeted_checks`:

```text
identity_valid
AND uncertainty_is_resolvable
AND at_least_one_actionable_check
```

Candidate condition for `abstain`:

```text
identity_invalid
OR material_conflict_unresolvable
OR minimum_source_set_unavailable
OR policy_unknown_and_decision_sensitive
```

### 9.2 Example output

```text
Evidence sufficiency:
Actionability: sufficient
Compatibility support: insufficient
Security support: partial
Repository context: partial
Policy context: sufficient

Strongest defensible output:
Run targeted checks
```

### 9.3 Key distinction

- evidence quantity;
- evidence quality;
- evidence coverage;
- evidence sufficiency for a specific claim.

These are not interchangeable.

## 10. Counterfactual Explanations

### 10.1 Concept

Every recommendation should explain what would have to change for the decision to change.

### 10.2 Example

```text
Current action:
Run targeted checks

Why:
Relevant generated-output behavior is not covered by observed tests.

Decision would change to merge after normal review if:
- the named regression check passes;
- no API break affects used symbols;
- repository policy does not require Python 3.8.

Decision would change to investigate or block if:
- the generated schema differs;
- upstream removed an invoked API;
- the package dropped a required runtime.
```

### 10.3 Product value

- makes decisions actionable;
- improves reviewability;
- exposes policy sensitivity;
- supports test generation;
- supports debugging;
- makes ML and LLM output easier to evaluate.

## 11. Enhanced Output Contract

A future decision report can extend the current contract with the following sections.

### 11.1 Identity

- repository;
- PR;
- old and new dependency versions;
- base and head revisions;
- decision-time timestamp;
- run identifier.

### 11.2 Decision

- selected action or abstention;
- policy profile;
- rule or model version;
- triggering evidence;
- counterfactual conditions.

### 11.3 Uncertainty

- uncertainty vector;
- evidence sufficiency;
- degraded states;
- abstention rationale.

### 11.4 Change impact

- upstream release delta;
- API surface delta;
- dependency-path changes;
- repository usage matches;
- relevant tests and CI coverage;
- unresolved dynamic paths.

### 11.5 Trust and supply chain

- distribution hashes;
- source association;
- attestations;
- yanked status;
- advisories;
- licenses;
- limited project-health signals.

### 11.6 Investigation plan

- ranked targeted checks;
- cost or effort;
- expected evidence;
- possible decision changes;
- required environment.

### 11.7 Provenance

- material claims;
- exact evidence references;
- transformation lineage;
- retrieval time;
- snapshot identifiers;
- source and method versions.

### 11.8 Reproducibility

- input hash;
- policy hash;
- code commit;
- environment identity;
- rerun command;
- expected deterministic and nondeterministic boundaries.

---

# Part II — Supply-chain, security, and interoperability proposals

## 12. Artifact Authenticity and Supply-Chain Provenance

### 12.1 Central question

> Can UpgradePilot verify where a released artifact came from and how it was produced?

### 12.2 Candidate evidence

For previous and proposed releases:

- distribution hashes;
- yanked state;
- source repository association;
- release artifact identities;
- PyPI publish attestations;
- SLSA provenance;
- signing identity;
- build workflow;
- source commit;
- verified and unverified attestation states;
- unexpected artifact differences;
- wheel and platform coverage changes.

### 12.3 Example

```text
Release 2.7.1:
- PyPI publish attestation: verified
- trusted publisher: GitHub Actions
- source repository: upstream/project
- source commit: abc123...
- wheel hash: verified

Release 2.7.2:
- no publish attestation found
- source association unresolved
- new Windows wheel added
- sdist hash recorded

Effect:
Artifact provenance degraded relative to the previous release.

Boundary:
This does not prove compromise. It identifies reduced verifiability and may justify an additional check.
```

### 12.4 Candidate technologies and standards

- PyPI digital attestations;
- PEP 740;
- SLSA provenance;
- Sigstore;
- GitHub artifact attestations;
- OpenID Connect — OIDC;
- Trusted Publishing;
- Rekor or transparency-log concepts;
- cryptographic hashes.

### 12.5 Learning value

- artifact identity;
- cryptographic verification;
- signing versus safety;
- build provenance;
- software supply-chain security;
- identity federation;
- trusted build systems.

## 13. SBOM and VEX Interoperability

### 13.1 Software Bill of Materials — SBOM

Use a machine-readable component inventory to:

- compare old and new dependency sets;
- identify changed transitive paths;
- record package identifiers and versions;
- exchange dependency context with external tools.

CycloneDX is a candidate standard.

### 13.2 Vulnerability Exploitability eXchange — VEX

Use a VEX-like contextual state to distinguish:

- vulnerability known;
- dependency present;
- relevant path observed;
- runtime applicability unresolved;
- not affected under declared evidence;
- affected;
- investigation required.

### 13.3 Claim discipline

UpgradePilot must not say a vulnerability is not exploitable merely because static imports were absent.

A safer output:

```text
Known vulnerability:
OSV-...

Observed repository context:
No static import or direct call found.

Unresolved:
Plugin loading, reflection, generated code, and deployment-specific paths.

Contextual state:
Not observed in inspected static paths; exploitability unresolved.
```

### 13.4 Learning value

- SBOM formats;
- package identifiers;
- vulnerability aliases;
- exploitability versus presence;
- interoperability;
- security claim boundaries.

## 14. Adversarial Evidence and Red-Team Corpus

### 14.1 Purpose

UpgradePilot processes untrusted public information:

- PR titles and descriptions;
- branch names;
- release notes;
- changelogs;
- repository files;
- workflow definitions;
- package metadata;
- CI logs;
- LLM-visible evidence.

Create a deliberate adversarial corpus.

### 14.2 Data and parser attacks

- oversized payloads;
- deeply nested JSON;
- malformed Unicode;
- duplicate keys;
- path traversal strings;
- archive bombs;
- invalid timestamps;
- contradictory package names;
- malicious URLs;
- source schema shifts.

### 14.3 Evidence manipulation

- release notes claim compatibility while code removes an API;
- misleading Semantic Versioning;
- renamed, transferred, or typosquatted package;
- yanked release;
- stale changelog;
- altered repository link;
- conflicting advisory aliases;
- dependency confusion indicators.

### 14.4 CI and automation attacks

- shell syntax inside PR titles;
- malicious branch names;
- workflow expressions containing untrusted strings;
- logs designed to resemble trusted output;
- attacker-controlled values reaching shell commands.

### 14.5 LLM attacks

- prompt injection in release notes;
- fake citations;
- malicious tool-use instructions;
- evidence text attempting to redefine policy;
- long irrelevant content hiding a material change;
- conflicting evidence designed to force confident synthesis.

### 14.6 Candidate suite organization

```text
identity attacks
parser attacks
provenance attacks
temporal attacks
policy attacks
prompt-injection attacks
resource-exhaustion attacks
silent-degradation attacks
```

### 14.7 Learning value

- secure parsing;
- input validation;
- injection defense;
- trust boundaries;
- fuzzing;
- resource limits;
- fail-closed versus degraded behavior;
- adversarial AI evaluation.

## 15. Self-Application to UpgradePilot

Eventually apply UpgradePilot’s own supply-chain principles to UpgradePilot:

- generate an SBOM;
- inspect dependency updates;
- pin CI actions appropriately;
- run dependency and security checks;
- evaluate OpenSSF Scorecard findings;
- generate build provenance;
- sign or attest released artifacts;
- verify attestations during release validation;
- preserve a reproducible release manifest.

This creates a recursive portfolio story:

> UpgradePilot evaluates dependency-update evidence, and its own build and release process emits the evidence it expects from dependencies.

---

# Part III — Evaluation and method-comparison proposals

## 16. External Baseline Arena

### 16.1 Purpose

Compare UpgradePilot with existing ecosystem signals rather than evaluating only internal variants.

### 16.2 Candidate baselines

- GitHub Dependency Review;
- OSV and OSV-Scanner;
- deps.dev or Open Source Insights;
- OpenSSF Scorecard;
- Griffe API comparison;
- package metadata and release-note-only baselines;
- CI-result-only baseline;
- version-category baseline.

### 16.3 Example comparison

```text
Case: repository#PR

GitHub Dependency Review:
No known vulnerability; dependency updated.

OSV:
No advisory affecting the proposed version.

Griffe:
One public method removed; one required parameter added.

UpgradePilot repository context:
Removed method is imported and called in a production path.
Relevant test coverage is absent.

UpgradePilot action:
Investigate or block.

Added value:
Repository-specific API impact and missing behavioral coverage.
```

### 16.4 Evaluation questions

- Which evidence categories does each baseline expose?
- Which repository-specific facts does UpgradePilot add?
- Which high-cost errors does each method make?
- Which cases remain unresolved for all methods?
- What extra latency and maintenance burden does UpgradePilot introduce?
- Does the extra context change the maintainer action?
- Is a longer report actually more useful?

### 16.5 Portfolio value

> I evaluated marginal utility against existing ecosystem tools rather than evaluating my system in isolation.

## 17. Decision Laws and Property-Based Testing

### 17.1 Candidate decision laws

1. Adding a verified blocking signal must not produce a less cautious action.
2. Removing evidence must not increase evidence sufficiency.
3. Reclassifying fresh evidence as stale must not increase confidence.
4. A malformed identity must never produce a decision report.
5. Replaying identical inputs and versions must reproduce the deterministic output.
6. Reordering evidence items must not change the decision.
7. Raw input must remain unchanged.
8. A stricter repository requirement must not produce a weaker action.
9. An inaccessible source must not be represented as observed.
10. A report claim must not reference a missing evidence identifier.
11. Adding irrelevant evidence must not change the action.
12. Changing a decision-causing field must change either the action or the explicit explanation of why it did not.

### 17.2 Property-based testing

Hypothesis is a candidate tool for:

- generating valid and invalid evidence records;
- discovering edge combinations;
- shrinking failures to minimal counterexamples;
- testing invariants beyond hand-written examples.

### 17.3 Stateful model testing

Candidate sequence:

```text
create case
→ add evidence
→ mark source stale
→ replay
→ change policy
→ remove source
→ rerun
→ verify invariants
```

### 17.4 Learning value

- invariants;
- property-based testing;
- state-machine testing;
- model-based testing;
- edge-case generation;
- minimal counterexamples;
- formal reasoning through executable tests.

## 18. Baseline-versus-Method Battle Board

### 18.1 Per-case comparison

| Method | Action | Unsupported claims | Evidence coverage | Cost | Latency |
|---|---|---:|---:|---:|---:|
| Version/CI baseline | Merge normally | 0 | 35% | negligible | 5 ms |
| Context baseline | Targeted checks | 0 | 71% | low | 2.8 s |
| Impact graph | Investigate | 0 | 83% | medium | 5.1 s |
| Learned ranker | Targeted checks | — | same evidence | low | 30 ms |
| LLM synthesis | Investigate | 1 | 83% | medium | 7.4 s |
| Multi-agent | Investigate | 0 | 88% | high | 46 s |

### 18.2 Per-case analysis

```text
Context method won because:
It linked a removed upstream symbol to an active repository call.

LLM lost because:
It described a transitive dependency as directly imported.

Multi-agent added:
One missing platform-support observation.

Multi-agent cost:
6.4× latency and 8.1× token cost.
```

### 18.3 Required discipline

A method is not better because it is:

- more complex;
- longer;
- agentic;
- learned;
- graph-based;
- more expensive;
- visually impressive.

It must create measured decision, evidence, review, reliability, or operational value.

## 19. ML Targets

### 19.1 Preferred candidate targets

1. **Investigation-priority ranking**  
   Rank dependency updates by which deserve maintainer attention first.

2. **Targeted-check ranking**  
   Rank checks by expected value and cost.

3. **Evidence-sufficiency prediction**  
   Predict whether evidence is sufficient for a specific action.

4. **Selective recommendation**  
   Predict only when evidence and confidence pass a threshold; otherwise abstain.

5. **Failure-type classification**  
   Predict the likely unresolved risk category without pretending to know the final action.

### 19.2 Why ranking may be stronger than forced classification

Maintainers may disagree about the final action but agree that:

- a case needs investigation;
- one check is more valuable than another;
- evidence is insufficient;
- a case should be reviewed before low-risk updates.

### 19.3 Candidate MLOps responsibilities

When a defensible experiment exists:

- corpus version;
- temporal split;
- adjudication-rubric version;
- feature version;
- model version;
- decision-cost matrix;
- abstention threshold;
- metrics;
- error cases;
- permitted claim;
- rejection or replacement decision.

MLflow is a candidate lifecycle tool, not an automatic requirement.

## 20. Grounded LLM Track

### 20.1 Candidate experiments

**Evidence compression**

Can an LLM shorten a large evidence package without omitting material uncertainty?

**Claim generation**

Can it produce report claims with exact evidence identifiers?

**Contradiction detection**

Can it detect disagreement between release notes, metadata, source changes, and CI?

**Targeted-check proposal**

Can it suggest checks that are relevant, executable, proportionate, and grounded?

**Counterfactual explanation**

Can it correctly state what evidence would change the recommendation?

**Adversarial grounding**

Can it resist instructions embedded in PR text, release notes, source files, and logs?

### 20.2 Candidate structured output

```json
{
  "claims": [
    {
      "text": "...",
      "evidence_ids": ["E12", "E19"],
      "claim_type": "observed",
      "materiality": "high"
    }
  ],
  "missing_material_evidence": ["..."],
  "contradictions": ["..."],
  "proposed_checks": ["..."],
  "abstain": false
}
```

### 20.3 Deterministic validation

- every evidence identifier exists;
- observed claims are supported;
- inaccessible sources are not described as observed;
- schema is valid;
- untrusted evidence cannot redefine system policy;
- material uncertainty is represented;
- unsupported claims are rejected or degraded.

### 20.4 Comparison baselines

- deterministic template;
- one LLM call;
- retrieval plus one LLM call;
- multi-stage grounded synthesis;
- multi-agent synthesis.

## 21. Multi-Agent Investigation Track

### 21.1 Candidate roles

- acquisition agent;
- repository-context agent;
- upstream-change agent;
- skeptic or falsification agent;
- evidence auditor;
- decision agent;
- deterministic arbiter.

### 21.2 Central experiment

> Does specialization plus adversarial review improve quality over one agent and a deterministic pipeline?

### 21.3 Failure modes to test

- repeated work;
- false consensus;
- unsupported claims;
- shared-state contamination;
- recursive investigation;
- cost explosion;
- failure to terminate;
- unresolved disagreement;
- prompt injection propagated between agents;
- authorization or tool-boundary violation.

### 21.4 Required trace

Preserve:

- each agent’s inputs;
- evidence references;
- claims;
- disagreements;
- tool actions;
- failures;
- termination reason;
- final arbitration.

---

# Part IV — Production-oriented system proposals

## 22. Analysis Run State Machine

### 22.1 Candidate states

```text
created
→ identity_validated
→ acquisition_started
→ partially_acquired
→ evidence_normalized
→ context_constructed
→ policy_evaluated
→ report_generated
→ persisted
→ evaluated
```

Failure and degraded states:

```text
identity_rejected
source_degraded
acquisition_interrupted
normalization_failed
policy_abstained
report_failed
```

### 22.2 Product value

- resumability;
- explicit partial progress;
- idempotency;
- retry boundaries;
- recovery;
- auditability;
- clearer failure diagnosis.

### 22.3 Later comparison

After a local state machine is proven, compare:

- synchronous Python orchestration;
- queue-backed jobs;
- a durable workflow engine such as Temporal.

The comparison question is:

> Does durable execution improve recovery for rate-limited, multi-source analysis enough to justify its operational burden?

## 23. Observability as a Product Responsibility

### 23.1 Analysis trace

```text
run 8f31...
├── identify_case                 12 ms
├── acquire_github_pr            311 ms
├── acquire_changed_files        582 ms
├── acquire_pypi_release         144 ms
├── verify_attestation           271 ms
├── compare_api_surfaces         1.8 s
├── analyze_repository_usage     2.7 s
├── compute_evidence_sufficiency 18 ms
├── select_targeted_checks       24 ms
└── render_report                37 ms
```

### 23.2 Candidate span attributes

- source;
- snapshot;
- cache hit;
- retry count;
- rate-limit state;
- evidence identifiers produced;
- degraded result;
- exception class;
- method version;
- case and run identifiers.

### 23.3 Candidate metrics

- analysis success rate;
- degraded-run rate;
- source availability;
- source latency;
- cache-hit rate;
- retry rate;
- report-generation latency;
- unsupported-claim count;
- provenance coverage;
- abstention rate;
- high-confidence error count;
- replay mismatch count.

### 23.4 Candidate technology

OpenTelemetry for traces, metrics, and logs after local structured observability needs are understood.

### 23.5 Learning value

- logs versus metrics versus traces;
- correlation identifiers;
- distributed tracing;
- service-level indicators;
- performance diagnosis;
- observability-driven design.

## 24. Transformation and Claim Lineage

### 24.1 Concept

Formalize:

```text
raw GitHub response
→ parsed PR identity
→ normalized case
→ dependency relationship
→ evidence item
→ policy rule
→ report claim
```

### 24.2 Candidate lineage record

- input entity;
- transformation;
- output entity;
- code version;
- transformation version;
- timestamp;
- status;
- hash;
- parent lineage;
- error or degraded state.

### 24.3 Later interoperability

Compare the internal lineage model with OpenLineage when real cross-job lineage needs exist.

### 24.4 Learning value

- data lineage;
- impact analysis;
- root-cause analysis;
- transformation contracts;
- event metadata;
- provenance versus lineage.

## 25. Shadow Mode

### 25.1 Concept

Operate a read-only monitoring mode:

```text
discover eligible public Dependabot PR
→ analyze without posting or mutating
→ preserve decision-time evidence
→ record recommendation
→ observe later public outcome
→ compare retrospective evidence
```

### 25.2 Example

```text
At PR opening:
Run targeted checks

Three days later:
Maintainer added a Python 3.9 job; it failed.

Seven days later:
Upstream released 4.2.1 fixing the issue.

Retrospective assessment:
The original targeted-check recommendation was appropriate.
```

### 25.3 Value

- fresh cases;
- temporal evaluation;
- distribution-shift evidence;
- realistic source failures;
- naturally occurring changed evidence;
- continuous motivation;
- ongoing portfolio evidence.

### 25.4 Boundary

Shadow mode remains read-only. It does not comment, approve, merge, close, or mutate external repositories.

## 26. Maintainer Decision Cockpit

### 26.1 Purpose

Create one functional visual experience, not a decorative dashboard.

### 26.2 Candidate views

**Case summary**

- repository;
- PR;
- dependency update;
- action;
- uncertainty profile;
- degraded-state indicator.

**Evidence matrix**

| Source | State | Freshness | Provenance | Decision effect |
|---|---|---:|---|---|
| PR diff | observed | current | commit-bound | neutral |
| release notes | observed | current | upstream URL | targeted check |
| CI logs | inaccessible | unknown | — | uncertainty |
| API diff | observed | current | version-bound | block |

**Impact graph**

Visual path from upstream change to repository code, tests, CI, and decision.

**Decision trace**

```text
Policy v4
Rule 12 matched
Evidence E17 + E21
Repository policy P3
Action: run_targeted_checks
```

**Counterfactual simulator**

Change evidence or policy and see why the action changes.

**Targeted-check planner**

Ranked checks with cost, expected evidence, and decision effect.

**Method arena**

Compare deterministic, context, graph, learned, LLM, and agent methods.

### 26.3 Interface progression

1. CLI and machine-readable report;
2. deterministic local HTML report;
3. lightweight local web application;
4. API only when a real interface need exists.

## 27. Case Gallery and Archetypes

Curate memorable cases that teach different lessons:

1. green CI with uncovered behavior;
2. transitive dependency surprise;
3. dropped Python version;
4. API break hidden in a minor release;
5. yanked or superseded release;
6. advisory with unresolved applicability;
7. unsigned-to-attested release transition;
8. attestation regression;
9. conflicting upstream evidence;
10. dynamic or plugin usage;
11. license-policy conflict;
12. CI platform gap;
13. dependency fan-out;
14. generated artifact drift;
15. malicious evidence text.

Each case should record:

- why it is interesting;
- what the weak baseline sees;
- what additional context reveals;
- decision-time evidence;
- targeted checks;
- actual or retrospective outcome;
- what the case teaches;
- what remains unresolved.

---

# Part V — Advanced-system proposals tied to real workloads

## 28. Queue and Durable-Workflow Experiments

### 28.1 Representative workload

- rate-limited acquisition;
- multi-source evidence collection;
- long-running API comparison;
- repository-context analysis;
- report generation;
- evaluation across a corpus.

### 28.2 Comparison

- synchronous local call;
- local worker queue;
- distributed queue;
- durable workflow engine.

### 28.3 Required measurements

- retry behavior;
- duplication;
- idempotency;
- backpressure;
- partial failure;
- recovery;
- state visibility;
- latency;
- operating burden;
- cleanup.

### 28.4 Wow experiment

Terminate a worker in the middle of an analysis and verify that execution resumes without losing state or duplicating evidence.

## 29. Microservice Experiment

Extract one proven responsibility, such as:

- evidence acquisition;
- API-surface comparison;
- LLM report synthesis;
- corpus evaluation.

Compare with the modular-monolith baseline on:

- lifecycle isolation;
- failure isolation;
- deployment independence;
- network complexity;
- observability;
- testing;
- latency;
- operations;
- developer effort.

A service is adopted only when measured value justifies it.

## 30. Kubernetes Experiment

Deploy a representative workload only after a containerized baseline exists.

Candidate learning:

- pods;
- deployments;
- jobs;
- services;
- configuration;
- secrets;
- readiness;
- rollout;
- failure;
- logs;
- resource limits;
- cleanup.

Candidate workload:

- decision cockpit;
- analysis API;
- background worker;
- scheduled shadow-mode job.

## 31. Multi-Cloud Portability Experiment

Run the same bounded, signed workload in two environments.

Compare:

- identity and credentials;
- container behavior;
- storage;
- networking;
- observability;
- cost;
- deployment steps;
- portability limitations;
- cleanup.

Permanent multi-cloud operation is not required.

## 32. MLOps Lifecycle Experiment

When a defensible model exists:

- version data;
- version features;
- track experiments;
- register the model;
- evaluate against gates;
- package inference;
- monitor or compare drift;
- replace, roll back, or reject.

When labels are insufficient:

- preserve the negative result;
- run a bounded lifecycle experiment without manufacturing a recommendation-quality claim;
- decide whether MLOps remains relevant.

## 33. Policy-Engine Experiment

Compare native typed decision rules with OPA or another policy-as-code system.

Measure:

- explainability;
- testability;
- decision logs;
- policy versioning;
- deployment separation;
- integration complexity;
- performance;
- debugging burden.

---

# Part VI — Proposed conceptual architecture

## 34. Capability map

```text
Case Interface
    ↓
Identity and Snapshot Boundary
    ↓
Evidence Acquisition
    ├── GitHub / PR / CI
    ├── PyPI / releases
    ├── advisories
    ├── attestations
    ├── dependency graph
    └── repository files
    ↓
Immutable Evidence Ledger
    ├── raw snapshots
    ├── hashes
    ├── timestamps
    ├── provenance
    └── temporal availability
    ↓
Normalization and Quality States
    ↓
Context and Impact Layer
    ├── dependency-path diff
    ├── API surface diff
    ├── repository symbol usage
    ├── tests and CI mapping
    ├── platform/runtime policy
    └── artifact authenticity
    ↓
Evidence Sufficiency Engine
    ↓
Decision and Policy Engine
    ├── deterministic baseline
    ├── repository policy profile
    ├── abstention
    └── counterfactual explanation
    ↓
Investigation Planner
    ├── candidate checks
    ├── expected information
    ├── cost
    └── decision effects
    ↓
Optional Methods
    ├── graph method
    ├── learned ranker
    ├── grounded LLM
    └── bounded multi-agent workflow
    ↓
Decision Cockpit / CLI / API
    ↓
Evaluation, Telemetry, Replay, and Shadow Mode
```

This diagram is a future capability map, not an accepted architecture.

---

# Part VII — Candidate roadmap integration

## 35. M2-S01 protection

The current M2-S01 identity-normalization responsibility remains unchanged.

No proposal in this document authorizes:

- source or test creation before the pre-code gate;
- a package layout;
- a policy engine;
- live acquisition;
- persistence;
- graphs;
- ML;
- LLMs;
- agents;
- queues;
- services;
- cloud;
- architecture adoption.

M2-S01 remains foundational because reliable decision intelligence requires exact case identity and immutable raw input.

## 36. R2 — First automated vertical slice

Candidate additions after current authorization permits them:

- explicit rule trace;
- evidence-sufficiency fields;
- counterfactual changed-case output;
- deterministic run identity;
- policy-version identity;
- report diff.

**Candidate wow moment**

Change one evidence field and observe a deterministic action and explanation change.

## 37. R3 — Reliable evidence system

Candidate additions:

- immutable evidence ledger;
- temporal availability;
- decision-time and retrospective modes;
- transformation lineage;
- analysis-run state machine;
- initial observability;
- package hashes and attestations;
- source-drift detection.

**Candidate wow moment**

Replay a historical case and explain every changed output.

## 38. R4 — Repository-specific context

Candidate additions:

- API surface diff;
- downstream symbol-usage mapping;
- test and CI coverage mapping;
- impact graph;
- runtime and platform support matrix;
- SBOM diff;
- artifact-provenance context.

**Candidate wow moment**

Select an upstream API change and trace it to a repository call site, related test, CI job, and unresolved gap.

## 39. R5 — Deterministic baseline and evaluation

Candidate additions:

- maintainer policy profiles;
- counterfactual explanations;
- decision laws;
- property-based testing;
- external baseline arena;
- targeted-check planner baseline;
- temporal leakage audit;
- adversarial corpus.

**Candidate wow moment**

Compare GitHub dependency signals, OSV, API diff, and UpgradePilot on the same PR and show UpgradePilot’s added value.

## 40. R6 — Contextual, ML, graph, and AI experiments

Candidate priorities:

- investigation-priority ranking;
- targeted-check ranking;
- selective prediction;
- evidence-sufficiency modeling;
- graph-feature evaluation;
- grounded claim synthesis;
- contradiction detection;
- prompt-injection evaluation;
- MLOps tracking.

**Candidate wow moment**

Compare multiple methods on one case and inspect exactly why a complex method won or lost.

## 41. R7 — Advanced systems

Candidate workloads:

- queue for parallel and rate-limited acquisition;
- durable workflow for resumable analysis;
- microservice extraction comparison;
- Kubernetes deployment of cockpit and worker;
- multi-cloud portability;
- specialized multi-agent investigation;
- MLOps lifecycle.

**Candidate wow moment**

Terminate a worker and recover without duplicated evidence or a lost decision trace.

## 42. R8 — Closure

Candidate final assets:

- case gallery;
- decision cockpit;
- shadow-mode results;
- external-baseline comparisons;
- attested UpgradePilot release;
- limitations and rejected-technology register;
- concise technical demonstration;
- final architecture derived from implemented behavior.

**Candidate wow moment**

A reviewer supplies a public Dependabot PR and receives an impact map, policy-aware action, ranked checks, uncertainty profile, and reproducible trace.

---

# Part VIII — Priority classification

## 43. Tier 1 — candidate central product identity

1. Upgrade Impact Graph
2. Decision-Time Machine
3. Targeted Check Planner
4. Maintainer Policy Profiles
5. Evidence Sufficiency Engine
6. Counterfactual explanations
7. Decision laws and property-based testing

These ideas most directly strengthen usefulness and distinctiveness.

## 44. Tier 2 — candidate production and portfolio enhancements

8. artifact provenance and attestation verification
9. External Baseline Arena
10. Adversarial Evidence Suite
11. analysis-run state machine
12. OpenTelemetry-style traces and metrics
13. Maintainer Decision Cockpit
14. Shadow Mode
15. SBOM and VEX interoperability
16. transformation lineage
17. case gallery

These ideas strengthen end-to-end production orientation and demonstration quality.

## 45. Tier 3 — candidate experimental technologies

18. OPA policy-as-code comparison
19. OpenLineage interoperability
20. MLflow lifecycle
21. durable workflow engine
22. queue-backed acquisition
23. microservice extraction
24. Kubernetes
25. multi-cloud portability
26. grounded LLM synthesis
27. bounded multi-agent investigation

These should operate on the strengthened core rather than become disconnected demonstrations.

---

# Part IX — Desired learning and motivation outcomes

## 46. Candidate “wow” experiences

The enhanced journey should make it possible to say:

- I reconstructed what information was actually available at decision time.
- I connected an upstream API break to a downstream call site, its tests, and its CI coverage.
- I learned why dependency presence is not the same as runtime applicability.
- I verified cryptographic provenance for a Python release.
- I built a policy engine whose decisions can be replayed and audited.
- I used property-based testing to discover combinations I had not manually imagined.
- I ranked tests by how much uncertainty they could resolve.
- I compared UpgradePilot against existing ecosystem tools and measured its marginal value.
- I measured where an LLM added value and where it invented or omitted claims.
- I killed a worker mid-run and recovered without duplicated evidence.
- I built an interface where every material claim traces to its source.
- I trained a model only after proving that the labels and evaluation were defensible.
- I rejected technologies when measured benefit did not justify their burden.
- I can explain the complete path from a public pull request to an evidence-backed maintainer action.

## 47. Candidate capability exposure

This proposal can create meaningful exposure to:

- Python application engineering;
- packaging and dependency semantics;
- HTTP and public APIs;
- data validation;
- relational modeling and SQL;
- temporal data;
- provenance and lineage;
- static analysis;
- graphs;
- testing and property-based testing;
- security and supply-chain verification;
- decision theory;
- ranking and selective prediction;
- ML evaluation;
- grounded LLM systems;
- agent evaluation;
- observability;
- queues and durable workflows;
- containers and Kubernetes;
- cloud portability;
- MLOps;
- product explanation and technical demonstration.

The exposure remains valuable only when tied to working UpgradePilot responsibilities and honest ownership evidence.

---

# Part X — Candidate thesis refinement

## 48. Current thesis direction

Repository-specific contextual evidence may improve dependency-update recommendations over generic version, CI, directness, and release-note signals.

## 49. Candidate stronger thesis

> **Repository-specific impact, temporal evidence integrity, explicit maintainer policy, and active investigation planning produce more useful dependency-update decisions than generic dependency signals or passive reports.**

## 50. Candidate project essence

> UpgradePilot does not merely analyze dependency updates. It models the complete reasoning process by which a responsible maintainer determines what changed, where it may matter, whether current evidence is sufficient, which check has the highest value, and what defensible action should happen next.

This thesis is preserved for future review. It is not controlling until formally admitted.

---

# Part XI — Proposal admission guidance

## 51. Recommended first admission review

When the current route reaches the appropriate review point, evaluate the Tier 1 ideas in this order:

1. Upgrade Impact Graph;
2. Decision-Time Machine;
3. Targeted Check Planner;
4. Evidence Sufficiency Engine;
5. Maintainer Policy Profiles;
6. Counterfactual explanations;
7. property-based decision laws.

For each, ask:

- What real limitation has appeared?
- What is the smallest useful responsibility?
- Which current route or milestone owns it?
- What prerequisite depth is required?
- What simpler baseline exists?
- What would success prove?
- What would success not prove?
- What is the rejection or defer condition?
- What new maintenance or failure burden appears?
- What Ali-owned action is required?

## 52. Non-admission rule

This document must not be used as a checklist that requires every idea.

A proposal can remain valuable when it is:

- partially admitted;
- deferred;
- rejected with evidence;
- replaced by a simpler idea;
- retained only as a future direction.

The project remains successful when its accepted core is coherent, reproducible, evaluated, and owned—even when ambitious experiments are rejected.

---

# Part XII — Technical reference candidates

These links are preserved as future primary references. They do not establish technology adoption.

- Python `ast`: https://docs.python.org/3/library/ast.html
- LibCST: https://libcst.readthedocs.io/
- Griffe: https://mkdocstrings.github.io/griffe/
- Hypothesis: https://hypothesis.readthedocs.io/
- GitHub Dependency Review: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-dependency-changes-in-a-pull-request
- OSV-Scanner: https://google.github.io/osv-scanner/
- deps.dev API: https://docs.deps.dev/api/v3/
- OpenSSF Scorecard: https://scorecard.dev/
- PyPI digital attestations: https://docs.pypi.org/attestations/
- SLSA provenance: https://slsa.dev/spec/
- Sigstore Python: https://sigstore.github.io/sigstore-python/
- GitHub artifact attestations: https://docs.github.com/en/actions/concepts/security/artifact-attestations
- CycloneDX SBOM: https://cyclonedx.org/capabilities/sbom/
- CycloneDX VEX: https://cyclonedx.org/capabilities/vex/
- Open Policy Agent: https://www.openpolicyagent.org/docs/
- OpenTelemetry Python: https://opentelemetry.io/docs/languages/python/
- OpenLineage: https://openlineage.io/
- Temporal: https://docs.temporal.io/
- MLflow: https://mlflow.org/docs/latest/
- GitHub Actions script-injection guidance: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions

## 53. Final preserved recommendation

The three candidate defining capabilities are:

1. **Impact Graph** — what can this update affect here?
2. **Decision-Time Machine** — what could the maintainer actually know then?
3. **Targeted Check Planner** — what is the next most valuable action to reduce uncertainty?

Supply-chain verification, SBOM/VEX, property-based tests, external baselines, ML, graphs, LLMs, agents, queues, observability, durable workflows, Kubernetes, multi-cloud, and MLOps can attach coherently to these capabilities.

The intended future identity is:

> **A reproducible dependency-update decision and investigation system that connects upstream change to repository-specific impact, preserves decision-time evidence, evaluates sufficiency and policy, ranks the next checks, and produces an auditable recommendation or abstention.**