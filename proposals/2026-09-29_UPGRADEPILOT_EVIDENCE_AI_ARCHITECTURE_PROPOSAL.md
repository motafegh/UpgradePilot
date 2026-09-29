# UpgradePilot Evidence, AI, and Agent Architecture Proposal

**Version:** 0.1  
**Recorded:** 2026-09-29  
**Branch:** \`analysis/ai-agentic-capability-map-2026-09-28\`  
**Status:** Full non-controlling architecture proposal for discussion and future reconciliation  
**Authority:** None by itself. This proposal does not replace \`PROJECT_CHARTER.md\`, accepted specifications, ADRs, active plans, source/tests, \`MEMORY.md\`, or the current Increment-4 learning-by-doing cycle on \`main\`.  
**Scope:** mature product architecture, evidence model, AI/agent placement, repository intelligence, runtime observation, provenance/interoperability, evaluation, and experiment admission.  
**Research basis:** Track A project-conditioned analysis + independent/de-anchored Track B research + Track C adversarial reconciliation + whole-pipeline mapping + AI/agent reconciliation + Step-5 convergence decisions.

---

# 1. Executive proposal

UpgradePilot should mature as an **evidence-backed dependency-update decision-support system for public Python repositories**.

Its purpose is not to maximize AI autonomy, generate patches by default, or produce a single “safe/unsafe” score.

Its purpose is to help a maintainer answer:

> **What does this dependency update materially change for this exact repository, what evidence supports or limits that conclusion, what remains unresolved, what additional check is worth performing, and what maintainer action is justified?**

The proposed mature architecture therefore combines:

- deterministic identity, parsing, precedence, correlation, and policy where facts are mechanically computable;
- multiple provenance-preserving evidence producers;
- repository/code/build/CI/dependency intelligence where reusable structure is valuable;
- bounded semantic models for open-ended technical meaning;
- bounded adaptive investigation only when the next useful evidence action depends on current state;
- optional runtime observation when static inference cannot settle a decision-critical proposition;
- explicit unresolved/conflicted states;
- human maintainer decision authority;
- protected, mechanism-aware evaluation of both deterministic and AI components.

The proposed mature flow is:

\`\`\`text
PUBLIC DEPENDENCY-UPDATE PR
        │
        ▼
EXACT UPDATE IDENTITY
repo / PR / base / head / dependency / old→new
        │
        ▼
MULTI-SOURCE EVIDENCE ACQUISITION
repository / CI / package index / upstream / runtime / external intelligence
        │
        ▼
PROVENANCE-BACKED NORMALIZATION
typed evidence + problems + coverage + source identity
        │
        ▼
REPOSITORY / BUILD / WORKFLOW / DEPENDENCY INTELLIGENCE
multiple bounded structural views, not one universal graph
        │
        ▼
DETERMINISTIC EVIDENCE ANALYSIS
mechanical propositions and exact semantic facts
        │
        ▼
BROAD TECHNICAL IMPACT DISCOVERY
hybrid structured signals + source/API evidence + bounded semantic reasoning
        │
        ▼
CANDIDATE GROUNDING + APPLICABILITY
applicable / not applicable / unresolved / conflicted
        │
        ▼
MATERIAL EVIDENCE GAP?
       / \
     no   yes
     │     │
     │     ▼
     │   FIXED-FIRST INVESTIGATION
     │   → bounded planner if state-dependent action choice is justified
     │   → optional runtime execution/telemetry
     │   → rare sandboxed generalist escalation
     │
     └─────┘
        │
        ▼
CROSS-CANDIDATE + REPOSITORY-CONTEXT SYNTHESIS
        │
        ▼
ACTION-SPECIFIC SUFFICIENCY / PERMISSION
        │
        ▼
MAINTAINER DECISION REPORT
orientation → evidence → applicability → CI limits → uncertainty → next action
        │
        ▼
HUMAN MAINTAINER DECISION
        │
        ▼
REPLAY / EVALUATION / DIAGNOSIS
\`\`\`

The central architecture thesis is:

> **AI, agents, graphs, static analyzers, runtime telemetry, package intelligence, and supply-chain standards are methods and evidence producers inside UpgradePilot. None of them defines the product by itself.**

---

# 2. Product boundary

## 2.1 Primary user

A maintainer of a public Python repository receiving dependency-update pull requests, especially Dependabot-style updates.

## 2.2 Primary input

\`\`\`text
public repository
+ exact dependency-update PR
+ exact base/head revision
+ exact dependency transition
+ available public target/upstream/package/CI evidence
\`\`\`

## 2.3 Primary output

A maintainer-facing, traceable decision-support result containing:

- materially relevant technical impact candidates;
- source/provenance for each candidate;
- target-specific applicability evidence;
- what CI/runtime evidence does and does not establish;
- unresolved/conflicted propositions;
- candidate-discovery and evidence-coverage limitations;
- discriminating follow-up checks when justified;
- action-specific explanation;
- explicit claim limits.

## 2.4 Human authority

The human maintainer retains the final decision.

UpgradePilot should not be defined by automatic merging, repository mutation, or unattended remediation.

Those may become optional future workflows only if product evidence justifies them.

---

# 3. Why this architecture is needed

Dependency updates are not one problem.

A single PR can implicate:

- source/API compatibility;
- behavioral/default changes;
- Python/runtime/platform support;
- transitive dependency resolution;
- packaging/build/install semantics;
- CI/tooling behavior;
- configuration migration;
- optional extras;
- persisted-state compatibility;
- package behavior/security changes;
- artifact availability;
- framework/declarative integration;
- runtime-only behavior.

No one existing system or method covers this whole decision responsibly.

Existing ecosystems tend to specialize:

- dependency bots generate/update PRs;
- SCA products detect vulnerability/license risk;
- reachability tools establish bounded dependency/code paths;
- migration engines generate known transformations;
- program-analysis systems model code/workflow relationships;
- software agents navigate repositories and execute tools;
- provenance standards describe components, relationships, and build lineage.

UpgradePilot's opportunity is the **decision layer that composes these evidence families for one exact dependency-update PR while preserving uncertainty and source authority**.

---

# 4. Non-negotiable evidence doctrine

The following principles survived both internal project analysis and independent external challenge.

## 4.1 Exact identity before semantic use

Every material claim must bind to the exact object it describes:

- repository;
- revision;
- PR/base/head;
- package/version transition;
- workflow/run/attempt/job/step;
- source file/range;
- environment/build/artifact where relevant.

## 4.2 Declaration is not execution

\`\`\`text
workflow contains command
!= command executed
\`\`\`

## 4.3 Broader success is not exact inner success

\`\`\`text
job/step succeeded
!= every nested command executed and succeeded
\`\`\`

## 4.4 Successful execution is not automatically valid evidence

Evidence is proposition-relative.

A process launch may establish execution but not final package state.

A passing test may establish one exercised behavior but not global compatibility.

## 4.5 Missing evidence is not negative evidence

\`\`\`text
no path found
!= path impossible

no finding
!= no impact

component absent from graph
!= proven irrelevant
\`\`\`

unless analyzer/evidence coverage independently supports the stronger conclusion.

## 4.6 Candidate is not applicability

\`\`\`text
upstream change discovered
!= target affected
\`\`\`

## 4.7 Applicability is not action permission

\`\`\`text
candidate applicable
!= merge
!= block
!= defer
\`\`\`

## 4.8 Explicit uncertainty is a valid result

Accepted technical states should include:

- established;
- established not applicable;
- unresolved;
- conflicted;
- unsupported where needed.

A mature evaluation system must reward correct abstention rather than artificial decisiveness.

## 4.9 Provenance authenticity is not semantic truth

A signed or attested result can prove origin/integrity without proving the semantic claim correct.

---

# 5. Whole-pipeline responsibility architecture

## 5.1 Admission and exact update identity

**Primary owner:** deterministic code  
**Current status:** implemented in bounded production path  
**AI role:** none authoritative

Responsibilities:

- repository/PR identity;
- exact base/head;
- changed files;
- exact dependency transition;
- dependency source context.

This stage should remain mechanical and testable.

---

## 5.2 Multi-source evidence acquisition

Evidence should remain family-specific and provenance-preserving.

Potential evidence producers include:

### Target/repository

- exact source files;
- dependency declarations;
- lockfiles;
- build/test configuration;
- repository instructions/policy.

### CI/workflow

- workflow definitions;
- historical runs;
- jobs/steps;
- logs/debug evidence;
- future optional runtime telemetry.

### Package/ecosystem

- package metadata;
- artifacts;
- declared requirements;
- dependency graphs;
- package behavior metadata.

### Upstream

- release notes/changelog;
- exact release interval;
- source/API differences;
- migration guides;
- upstream tests/examples.

### External analysis

- CodeQL;
- actionlint;
- zizmor;
- Griffe;
- deps.dev;
- future graph/query systems;
- supply-chain evidence stores.

The architecture should not require every PR to activate every source.

Demand-driven acquisition is preferred.

---

# 6. Evidence normalization and provenance

UpgradePilot should maintain its own domain-specific internal reasoning model.

It should not force internal semantics into SPDX, CycloneDX, in-toto, GUAC, or any other external standard.

However, the internal model should preserve enough metadata to support future adapters.

A material evidence record should be able to answer:

\`\`\`text
WHAT proposition/evidence is represented?
WHICH exact repo/revision/environment?
WHO/WHAT produced it?
FROM WHICH source?
BY WHICH method?
WHEN?
WITH WHAT coverage/completeness limitation?
WAS it observed, inferred, emulated, symbolic, model-derived, or human-declared?
WAS it independently validated?
\`\`\`

This supports:

- audit;
- replay;
- conflict resolution;
- evidence-strength comparison;
- future standards export.

---

# 7. Multi-view repository intelligence

The research does not support one universal repository/evidence graph as the default architecture.

A stronger mature hypothesis is **multiple bounded views with stable identities and evidence-backed cross-links**.

Potential views:

\`\`\`text
RepositoryIdentity
     │
     ├── CodeStructureView
     │     symbols / imports / calls / inheritance
     │
     ├── BuildTestView
     │     modules / build targets / tests / coverage / runners
     │
     ├── WorkflowView
     │     jobs / steps / conditions / env/dataflow
     │
     ├── DependencyView
     │     declarations / resolution / package-manager operations
     │
     ├── SupplyChainView
     │     packages / artifacts / SBOM / provenance / attestations
     │
     └── DecisionEvidenceView
           candidates / propositions / evidence / conflicts / gaps
\`\`\`

These views should not be built all at once.

A stable repository-intelligence capability interface should be preferred over premature commitment to a graph database:

\`\`\`text
find_symbol
find_references
find_callers
find_importers
find_tests_for_component
find_build_owner
find_package_usage
find_ci_consumers
retrieve_exact_source
search_repository
get_project_instruction
\`\`\`

Possible backends may evolve:

- current parsers;
- CodeQL;
- bounded custom graph;
- RIG-like build/test extractor;
- Sourcegraph-like code intelligence;
- graph database only if proven necessary.

---

# 8. CI, workflow, and runtime evidence

UpgradePilot should preserve four different evidence classes:

\`\`\`text
STATIC STRUCTURAL EVIDENCE
what source/configuration permits

HISTORICAL RUNTIME OBSERVATION
what GitHub's actual run/logs establish

INSTRUMENTED RUNTIME TELEMETRY
what process/network/file monitoring observes

EMULATED / RECONSTRUCTED EXECUTION
what a modeled local environment such as act reproduces
\`\`\`

These must not be merged into one generic “execution evidence”.

A fifth distinct class may exist for bounded symbolic proof.

## 8.1 Current custom workflow logic

Current bounded exact-command execution and correlation work remains valid.

## 8.2 Future workflow expansion

Before substantially expanding generic GitHub Actions CFG/dataflow support, compare the current route against **CodeQL Actions**.

The architecture should allow CodeQL to become an evidence producer without requiring CodeQL to become the entire internal model.

## 8.3 Runtime telemetry

Runtime instrumentation should be an optional evidence producer for propositions that static evidence cannot settle.

It should not become mandatory infrastructure for all repositories.

---

# 9. Package-manager and runtime dependency-state architecture

The current R4 direction should remain deterministic.

Core mature chain:

\`\`\`text
exact package-manager operation
→ command declaration
→ independent semantic dimensions
→ effective value from CLI / process env / config / defaults
→ exact-command execution evidence
→ command-completion requirement-state witness
\`\`\`

Important boundaries:

\`\`\`text
requirement satisfied at command completion
!= fresh install causality
!= exact artifact/wheel identity
!= later persistence
!= later import/use
!= behavior compatible
!= CI coverage sufficient
!= maintainer action
\`\`\`

The future architecture should allow direct observed package-state evidence to coexist with command-derived inference without conflating their strength.

---

# 10. Broad technical impact-candidate discovery

This is the largest future AI-capable responsibility.

Question:

> **What materially plausible technical mechanisms should UpgradePilot evaluate for this dependency transition and this target repository?**

Candidate discovery should be hybrid.

## 10.1 Deterministic signals

Examples:

- explicit support metadata;
- dependency constraints;
- release/yank state;
- package artifact differences;
- old/new API signatures;
- package-manager metadata.

## 10.2 Upstream semantic evidence

Examples:

- release notes;
- migration guides;
- source/API diff;
- deprecation/removal notes;
- behavioral/default changes.

## 10.3 Target structural evidence

Examples:

- imports/references;
- wrappers/adapters;
- framework hooks;
- configuration;
- test/development use;
- build/install surfaces;
- package-role relationships.

## 10.4 Semantic model role

A bounded semantic model may:

- interpret open-ended change descriptions;
- connect upstream changes to target context;
- propose technical mechanism candidates;
- identify missing propositions.

It must not self-establish:

- applicability;
- candidate-discovery completeness;
- action permission.

## 10.5 Model context

The mature architecture should not permanently restrict broad discovery to tiny typed projections.

Instead use progressive disclosure:

\`\`\`text
compact typed evidence
→ structural query/retrieval
→ exact source range
→ broader raw source only when needed
\`\`\`

What the model may inspect remains separate from what becomes trusted state.

---

# 11. Candidate formulation and applicability

A candidate should be a challengeable technical object, not prose.

Candidate fields may include:

- candidate identity;
- mechanism;
- dependency transition;
- upstream/source evidence;
- target scope;
- possible exposure/relation;
- activation conditions;
- potential consequence;
- required propositions;
- provenance;
- lineage;
- coverage limitations.

Candidate applicability should resolve to:

- established applicable;
- established not applicable;
- unresolved;
- conflicted.

Keep separate:

\`\`\`text
evidence coverage
path-model coverage
candidate-discovery coverage
\`\`\`

The mature system must avoid claiming “no material impact” merely because all discovered candidates were eliminated unless candidate-discovery coverage independently supports that broader conclusion.

---

# 12. AI/LLM responsibility model

UpgradePilot should not have one generic AI owner.

AI responsibilities should remain explicit.

## 12.1 Semantic extractor

Question:

> What does this bounded evidence say?

Current adopted example:

- Python support-drop local LLM extractor.

Architecture:

\`\`\`text
trusted source window
→ structured model candidate
→ deterministic exact source recovery/validation
→ bounded candidate
\`\`\`

**Proposal:** keep this pattern.

---

## 12.2 Broad candidate-discovery reasoner

Question:

> What technical impact mechanisms might exist?

**Proposal:** future high-value AI capability, but only after protected evaluation and richer upstream/target evidence exist.

---

## 12.3 Evidence-gap planner

Question:

> Given a known unresolved proposition, what evidence should be acquired next?

Architecture:

\`\`\`text
trusted state
→ projected planning context
→ model action proposal
→ deterministic rebind/admission
→ read-only capability
→ deterministic interpretation
→ updated state
\`\`\`

**Proposal:** retain current pilot architecture; do not adopt generally until at least two real actions create a genuine state-dependent planning problem.

---

## 12.4 Cross-candidate synthesizer

Question:

> Given earned multi-candidate evidence, what matters most to the maintainer?

Possible role:

- prioritization;
- contradiction explanation;
- evidence relationship explanation;
- report structure.

**Proposal:** defer until mature cross-candidate state exists.

---

## 12.5 Generalist repository agent

Question:

> Can a broad sandboxed software agent solve long-tail investigations that bounded capabilities cannot?

**Proposal:** optional escalation/comparator only.

Do not use as default architecture.

---

# 13. Agent authority and tool model

Agent capability should be separated from authority.

A mature bounded investigation agent may select among registered capabilities:

\`\`\`text
query code/repository structure
retrieve exact source
inspect upstream evidence
query static analyzer
inspect CI/runtime evidence
execute admitted read-only check
query package intelligence
request maintainer input
\`\`\`

The model may select **which** action to propose.

Deterministic code should own:

- capability registry;
- parameter schemas;
- exact repo/revision/path binding;
- mutation class;
- preconditions;
- security policy;
- action admission;
- result interpretation where mechanically computable;
- trusted-state promotion.

Closed action catalogs are useful early scaffolds.

They should not be treated as a permanent mature limitation if richer registered capabilities are later justified.

---

# 14. Fixed pipeline vs adaptive agent

The default should be:

\`\`\`text
deterministic extraction
→ fixed structured reasoning
→ bounded semantic model
→ if material evidence gap remains:
     bounded adaptive planner
→ if bounded capabilities demonstrably fail on real long-tail cases:
     optional generalist sandboxed agent
\`\`\`

Why:

- Agentless/DepRepair-style systems show fixed pipelines can be highly competitive.
- Generalist agents introduce cost, security, trajectory variance, and evaluation difficulty.
- Adaptivity has value only when the best next action genuinely depends on intermediate evidence.

Therefore every agent proposal should compete against the strongest fixed baseline for the same responsibility.

---

# 15. Framework policy

Framework choice should follow product pressure.

## Direct LM Studio / HTTP

Keep for current adopted semantic extraction and bounded experiments while sufficient.

## LangGraph

Retain hands-on/architecture experiment evidence.

Do not adopt into product until real orchestration pressure appears, such as:

- checkpoint/resume;
- human pause/resume;
- durable workflow state;
- complex branching/recovery;
- multiple justified actors.

## LangChain

No current product need.

## OpenHands or equivalent

Future generalist-agent comparator only.

## Vector database / generic RAG

Do not adopt before retrieval evaluation demonstrates a real need.

---

# 16. Runtime and execution-assisted reasoning

Static analysis should remain first-class, but the mature architecture should allow observation where it is stronger.

Potential evidence ladder:

\`\`\`text
source/configuration
→ static semantic analysis
→ historical GitHub run evidence
→ instrumented runtime telemetry
→ targeted controlled execution
→ production-equivalent observation where available
\`\`\`

Each level answers different propositions.

Runtime success must not silently upgrade to compatibility proof.

Execution environments must record fidelity and scope.

---

# 17. Program-analysis integration

External analyzers should be treated as evidence producers, not automatic architecture owners.

Potential high-value integrations:

## CodeQL

For:

- GitHub Actions CFG/dataflow;
- cross-step environment flow;
- Python dataflow/control flow;
- security queries.

## actionlint

For:

- workflow schema/expression validation;
- shell/Python linting.

## zizmor

For:

- CI/CD security findings;
- template injection;
- permissions/action trust.

## Griffe

For:

- Python API representation;
- old/new API breakage candidates.

## Joern / CPG

For:

- broader code-property graph experiments if needed.

## CrossHair / symbolic methods

For:

- bounded pure predicate/path questions, not arbitrary repository execution.

The rule is:

> Do not reproduce a mature generic analyzer internally unless UpgradePilot's proposition semantics genuinely require a different model.

---

# 18. Provenance and standards interoperability

UpgradePilot should keep its own internal evidence/decision model.

But it should be capable of interoperating with mature standards where useful.

Potential adapters:

- CycloneDX;
- SPDX;
- in-toto;
- SLSA;
- Sigstore/GitHub attestations;
- GitHub dependency submission;
- GUAC.

Possible uses:

- component/dependency identity exchange;
- build provenance;
- evidence technique/tool metadata;
- no-assertion/completeness semantics;
- artifact/report attestation;
- external graph enrichment.

Do not confuse:

\`\`\`text
attested claim
with
correct claim
\`\`\`

---

# 19. Maintainer action architecture

The mature Charter action family is broader than current implementation.

Possible actions include:

- merge after normal review;
- run targeted checks;
- investigate/block;
- defer;
- abstain.

Current implementation correctly admits only \`abstain\`.

This proposal does not define the final action algorithm.

Instead it proposes:

1. each non-abstention action must have explicit positive prerequisites;
2. candidate applicability alone cannot authorize action;
3. unresolved/conflicted evidence must remain visible;
4. model synthesis cannot create permission;
5. action-permission architecture should be empirically compared once multiple actions become real.

The existing \`DecisionPermissionEnvelope\` proposal remains a strong experiment hypothesis, not an accepted mature architecture.

---

# 20. Maintainer-facing report architecture

The final report should support real review cognition.

Recommended structure:

## 20.1 Orientation

- dependency;
- old → new;
- repository/revision;
- why the update might matter.

## 20.2 Material findings

- applicable candidates;
- eliminated candidates where useful;
- conflicts;
- unresolved material candidates.

## 20.3 Evidence

For each material finding:

- source;
- producer/method;
- exact target relation;
- provenance;
- limitations.

## 20.4 CI/runtime interpretation

Explicitly state:

- what existing CI exercised;
- what runtime evidence established;
- what it did not prove.

## 20.5 Next discriminating check

Only when the check can materially change the decision.

## 20.6 Action explanation

Explain why an action is permitted/appropriate without implying certainty beyond evidence.

## 20.7 Claim limits

Make explicit what remains unproven.

The report should optimize for maintainer comprehension and decision quality—not for AI persuasiveness.

---

# 21. Evaluation architecture

Evaluation is part of the architecture.

## 21.1 Case/oracle quality

Every protected case should record:

- repository/version identity;
- dependency transition;
- mechanism labels;
- environment;
- oracle;
- oracle limitations;
- source provenance;
- freshness;
- contamination/leakage risk;
- human review state.

## 21.2 Deterministic evidence-producer evaluation

Measure:

- proposition precision;
- recall where ground truth exists;
- provenance correctness;
- unsupported-state correctness;
- negative-claim correctness;
- analyzer coverage.

Deterministic code is not trusted merely because it is deterministic.

## 21.3 Candidate-discovery evaluation

Measure:

- relevant mechanism recall;
- unsupported candidate rate;
- duplicate rate;
- grounding;
- discovery-coverage honesty.

## 21.4 Applicability evaluation

Measure correctness of:

- applicable;
- not applicable;
- unresolved;
- conflicted.

Pay special attention to false “not applicable” conclusions.

## 21.5 Agent evaluation

Use repeated runs.

Measure:

- useful next action;
- evidence gain/action;
- unnecessary actions;
- invalid/unauthorized choices;
- stopping correctness;
- cost;
- trajectory variance.

## 21.6 Semantic model evaluation

Measure:

- structured-output validity;
- source grounding;
- hallucination;
- abstention;
- accepted-claim precision;
- risk/coverage curves;
- OOD behavior.

Separate:

\`\`\`text
model confidence
evidence strength
empirical selective risk
\`\`\`

## 21.7 Maintainer outcome evaluation

Eventually measure:

- decision correctness;
- decision time;
- appropriate trust;
- external lookups;
- ability to detect system mistakes;
- cognitive load;
- usefulness;
- retained rationale.

Human agreement with the AI is not correctness.

---

# 22. Protected evaluation corpus proposal

A future high-value UpgradePilot asset is a reproducible Python dependency-update corpus.

Recommended structure:

\`\`\`text
exact repository snapshot
+ exact old→new dependency transition
+ reproducible environment/container
+ mechanism taxonomy
+ before/after evidence
+ executable or evidence-based oracle
+ oracle limitations
+ human audit
\`\`\`

Maintain three classes:

## Development corpus

Visible for building/debugging.

## Protected evaluation corpus

Not repeatedly inspected during implementation.

## Challenge corpus

Designed for:

- conflicting evidence;
- inadequate CI;
- unsupported syntax;
- unusual repository architecture;
- misleading release prose;
- OOD mechanisms;
- model hallucination pressure.

This corpus would support:

- deterministic analyzers;
- semantic models;
- agent planning;
- synthesis evaluation;
- calibration.

---

# 23. Optional remediation subsystem

Remediation should remain downstream from decision intelligence.

Potential future architecture:

\`\`\`text
established impact/evidence state
→ remediation strategy selection
→ deterministic recipe/codemod OR grounded model repair
→ validation
→ revised evidence state
→ maintainer decision
\`\`\`

For Python:

\`\`\`text
Griffe old/new API diff
+ target localization
+ migration evidence
→ known migration?
     LibCST codemod
→ novel but evidence-rich?
     bounded model repair
→ paradigm shift?
     interactive/generalist investigation
→ tests/build/static/runtime validation
\`\`\`

Do not adopt remediation merely to increase automation.

---

# 24. Security model

Security requirements increase as agent capability expands.

## 24.1 Read-only by default

Evidence acquisition and investigation should prefer read-only capabilities.

## 24.2 External policy boundary

When execution is required:

- filesystem scope;
- process execution;
- network;
- credentials;
- package-manager behavior;
- resource/budget limits;

should be externally enforced where practical.

## 24.3 Untrusted repository content

Repository source, issue text, release notes, CI output, and package metadata can contain adversarial instructions.

Models must not treat evidence content as system/tool authority.

## 24.4 Mutation

External repository mutation remains outside current Charter core.

Future remediation must have explicit authorization and validation.

---

# 25. Concrete experiment program

Experiments are responsibility-triggered.

## E1 — CodeQL Actions comparator

Trigger:
before broad custom workflow CFG/dataflow expansion.

Compare:
current model vs CodeQL Actions.

## E2 — Griffe/API/source-diff comparator

Trigger:
broad candidate discovery activation.

Compare:
changelog vs API/source diff vs combined.

## E3 — Runtime telemetry comparator

Trigger:
decision-critical runtime uncertainty unresolved by existing evidence.

Compare:
static inference vs direct telemetry.

## E4 — Multi-view repository intelligence

Trigger:
repeated structural queries across multiple responsibilities.

Build:
small bounded Python structural/build/test view first.

## E5 — Model context breadth

Trigger:
candidate-discovery model experiment.

Compare:
typed-only vs structural retrieval vs progressive raw-source retrieval.

## E6 — Fixed investigation vs bounded planner

Trigger:
at least two independently justified real investigation actions.

Required before EvidenceGapPlanner product adoption.

## E7 — Bounded planner vs generalist agent

Trigger:
real long-tail repositories where bounded planner/capabilities fail.

## E8 — Calibrated model-claim admission

Trigger:
protected semantic corpus + demonstrated coverage pressure.

## E9 — Standards mapping

Trigger:
interoperability/provenance need or bounded learning lab.

## E10 — Maintainer decision-quality study

Trigger:
stable report/action surface with multiple real action outcomes.

---

# 26. Technology and learning exposure strategy

UpgradePilot is also a learning-by-doing project.

Technology selection should therefore consider two axes:

\`\`\`text
A. product/architecture value
B. transferable engineering learning value
\`\`\`

But the two must remain separate.

A tool should not enter production merely for résumé value.

When product fit is weak but learning value is high, use a bounded lab.

## 26.1 Strong future hands-on candidates

When responsibility triggers exist:

- CodeQL / QL;
- Griffe;
- LibCST;
- GUAC / GraphQL;
- CycloneDX / SPDX;
- SLSA / in-toto / Sigstore;
- runtime CI telemetry;
- RIG-style graph modeling;
- OpenHands comparator;
- calibration / selective prediction;
- reproducible benchmark/evaluation harnesses.

## 26.2 Already earned hands-on experience

Current project evidence supports real experience with:

- LM Studio/local LLM inference;
- structured model output;
- deterministic source grounding;
- AI authority boundaries;
- bounded evidence-gap planner design;
- tool admission/rebinding;
- replayable state transitions;
- LangGraph StateGraph experiment;
- governance/skills/agent workflow design.

Maintain precise claims:

\`\`\`text
researched
!= hands-on experimented
!= project-integrated
!= validated/operated
\`\`\`

---

# 27. Current product sequencing

This proposal must not disrupt the current live route.

At proposal time, \`main\` is in Increment 4 A1.

Current R4 sequence remains:

\`\`\`text
Increment 1
reusable exact-command execution evidence
        ↓
Increment 2
shared package-manager operation + semantic facts
        ↓
Increment 3
bounded executable/process-env/config evidence
        ↓
Increment 4
command-derived requirement-state composer
        ↓
Increment 5
application integration
\`\`\`

No AI/agent/graph/runtime-telemetry experiment should be injected into Increment 4 or the initial Increment 5 responsibility without new contradictory evidence.

---

# 28. Explicit non-decisions

This proposal intentionally does **not** decide:

- CodeQL vs custom workflow modeling;
- final repository-intelligence backend;
- graph database choice;
- final broad-discovery model;
- permanent model-context width;
- calibrated AI trust admission;
- mature action-permission algorithm;
- final LLM synthesis architecture;
- generalist-agent adoption;
- standards export format;
- remediation engine.

These are experiment-gated decisions.

---

# 29. Explicit deferrals

Do not add now:

- LangChain;
- generalist agent as default;
- multi-agent architecture as default;
- generic vector DB/RAG stack;
- universal evidence graph;
- standards-native internal model;
- automatic remediation engine;
- production LangGraph runtime;
- LLM-as-judge product authority.

---

# 30. Relationship to current UpgradePilot artifacts

This proposal is a synthesis.

It should remain compatible with:

- \`PROJECT_CHARTER.md\`;
- Core Pipeline and Contract Specification;
- Product Decision Model Specification;
- accepted ADRs including bounded support-drop extraction and runtime dependency-state semantics;
- current R4 completion plan;
- current source/tests;
- current \`MEMORY.md\`.

It does not replace:

- the Mature System Horizon;
- bounded planner plan;
- LangGraph experiment plan;
- LLM synthesis proposal.

Future reconciliation may update those artifacts after a clean product-cycle boundary.

---

# 31. Branch and integration strategy

Keep this proposal and all research records on:

\`analysis/ai-agentic-capability-map-2026-09-28\`

while \`main\` progresses.

Do not merge this research branch wholesale.

The branch is detailed research provenance.

At a clean main-branch stop boundary, create a fresh branch from then-current \`main\` and selectively integrate a distilled architecture package.

Recommended durable integration set:

1. one concise architecture reconciliation artifact derived from this proposal;
2. Step-3 whole-pipeline map;
3. Step-4 AI/agent disposition summary;
4. Step-5 experiment/deferral register;
5. learning/exposure ledger where useful;
6. one bounded update to the Mature System Horizon.

Tier-1 reports may remain on the research branch as evidence provenance rather than becoming live project owners.

---

# 32. Success criteria for this proposal

This proposal should be considered useful if it provides a stable answer to:

- what UpgradePilot is;
- what it is not;
- how evidence should flow;
- where deterministic logic belongs;
- where AI belongs;
- where agents belong;
- where runtime observation belongs;
- how repository intelligence may evolve;
- how provenance/standards may integrate;
- what experiments are required before architecture admission;
- what current work should remain untouched;
- how learning exposure can be gained without corrupting product design.

It should **not** be considered accepted architecture merely because it is comprehensive.

Acceptance must remain responsibility-specific and evidence-gated.

---

# 33. Proposed mature architecture summary

\`\`\`text
PUBLIC DEPENDENCY-UPDATE PR
        │
        ▼
EXACT IDENTITY
        │
        ▼
MULTI-SOURCE EVIDENCE ACQUISITION
        │
        ▼
PROVENANCE-BACKED NORMALIZATION
        │
        ▼
MULTI-VIEW REPOSITORY / CI / DEPENDENCY INTELLIGENCE
        │
        ▼
DETERMINISTIC ANALYSIS
        │
        ▼
BOUNDED SEMANTIC DISCOVERY
        │
        ▼
TECHNICAL CANDIDATES
        │
        ▼
GROUNDING + APPLICABILITY + COVERAGE
        │
        ▼
MATERIAL GAP?
        │
        ├── no ──────────────────────────┐
        │                               │
        └── yes                         │
             ▼                          │
        FIXED-FIRST INVESTIGATION       │
             │                          │
             ├─ bounded planner         │
             ├─ runtime observation     │
             └─ rare generalist agent   │
             │                          │
             └──────────────────────────┘
        │
        ▼
VERIFIED CROSS-CANDIDATE SYNTHESIS
        │
        ▼
ACTION-SPECIFIC PERMISSION / SUFFICIENCY
        │
        ▼
MAINTAINER DECISION REPORT
        │
        ▼
HUMAN DECISION
        │
        ▼
REPLAY / EVALUATION / CONTINUOUS IMPROVEMENT
\`\`\`

---

# 34. Final proposal statement

The proposed mature UpgradePilot should be neither AI-first nor deterministic-only.

It should be **evidence-first**.

Deterministic methods should own facts that can be established mechanically.

Semantic models should be used where natural-language/code meaning is genuinely open-ended.

Agents should be introduced only where adaptive evidence selection creates measurable value.

Runtime observation should strengthen, not replace, static reasoning.

Repository intelligence should reduce repeated rediscovery without becoming one universal graph.

Provenance should make every important claim inspectable.

Uncertainty should remain visible when evidence is incomplete.

Evaluation should measure not only machine correctness but whether maintainers make better decisions with appropriate trust.

And every new technology should earn its place against the exact UpgradePilot responsibility it claims to improve.

---

# 35. Research provenance

This proposal synthesizes the following branch records:

- \`working-memory/2026-09-29_external-research-area-discovery.md\`
- \`working-memory/2026-09-29_tier1-01_closest-dependency-update-products-and-workflows.md\`
- \`working-memory/2026-09-29_tier1-02_dependency-risk-reachability-and-upgrade-impact-platforms.md\`
- \`working-memory/2026-09-29_tier1-03_remediation-and-migration-engines.md\`
- \`working-memory/2026-09-29_tier1-04_dependency-evidence-graphs-and-provenance-standards.md\`
- \`working-memory/2026-09-29_tier1-05_ci-runtime-evidence-and-program-analysis.md\`
- \`working-memory/2026-09-29_tier1-06_repository-intelligence-and-agent-architectures.md\`
- \`working-memory/2026-09-29_tier1-07_evaluation-maintainer-ux-and-decision-quality.md\`
- \`working-memory/2026-09-29_step2bx_independent-candidate-architecture-refresh.md\`
- \`working-memory/2026-09-29_step2c_adversarial-track-a-vs-track-b-comparison.md\`
- \`working-memory/2026-09-29_step3_whole-pipeline-architecture-map.md\`
- \`working-memory/2026-09-29_step4_existing-ai-agent-work-reconciliation.md\`
- \`working-memory/2026-09-29_step5_architecture-decisions-experiment-queue-and-integration-strategy.md\`
- \`working-memory/2026-09-29_research-technology-learning-exposure-ledger.md\`

External systems/research studied across those reports include:

- Dependabot / dependabot-core;
- Renovate / Merge Confidence;
- Updatecli;
- GitHub Dependency Review;
- Endor Labs;
- Semgrep Supply Chain;
- Snyk;
- Socket;
- OSV-Scanner;
- OpenRewrite / Moderne;
- DepRepair / DepBench;
- Griffe;
- LibCST;
- deps.dev;
- GUAC;
- OSS Review Toolkit;
- SPDX;
- CycloneDX;
- SLSA;
- in-toto;
- Sigstore;
- GitHub artifact attestations/dependency submission;
- actionlint;
- zizmor;
- CodeQL;
- StepSecurity;
- act;
- Joern;
- CrossHair;
- angr;
- RepoGraph;
- LocAgent;
- Repository Intelligence Graph;
- CodexGraph;
- Sourcegraph Code Graph;
- AutoCodeRover;
- SWE-agent;
- OpenHands;
- Agentless;
- CodeRAG research;
- calibration/selective-prediction research;
- maintainer/code-review human-factors research.

The detailed evidence, caveats, URLs, and per-system findings remain in the branch research reports rather than being duplicated here.
