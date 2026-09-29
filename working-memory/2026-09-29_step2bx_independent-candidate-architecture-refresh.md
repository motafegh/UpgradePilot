# Step 2B-X — Independent Candidate-Architecture Refresh

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial refresh  
**Authority:** independent/de-anchored research synthesis only; does not alter accepted UpgradePilot architecture, specifications, ADRs, product plans, or `main`.  
**Inputs:** Tier-1 Reports 01–07 plus the original Track-B candidate architectures.

---

## 1. Why a refresh was necessary

The original Track-B candidate set was intentionally broad, but Tier-1 research exposed a methodological problem:

> several original “architectures” were actually **cross-cutting mechanisms**, not whole-system architectures.

Examples:

- calibrated selective prediction is a **trust/output policy** that can sit on top of several system designs;
- challenger/verifier agents are an **escalation/evaluation topology**, not a complete product architecture;
- an evidence graph is a **world-model substrate**, not necessarily the decision engine;
- sandboxing is an **execution/authority boundary**, not a reasoning architecture.

Tier-1 also materially narrowed the product space.

Therefore this refresh separates:

1. **product boundary**;
2. **shared infrastructure/substrate choices**;
3. **competing reasoning/execution architectures**;
4. **cross-cutting trust/UX/evaluation mechanisms**;
5. **optional future remediation architecture**.

---

## 2. Refined independent product boundary

Tier-1 evidence strongly suggests UpgradePilot should not primarily compete with:

- Dependabot/Renovate on update discovery/generation;
- GitHub Dependency Review on vulnerability/license policy;
- Endor/Semgrep/Snyk/Socket on security-only reachability/remediation;
- OpenRewrite on large-scale codemods;
- OpenHands on general-purpose repository modification;
- GUAC on generic supply-chain graph aggregation.

The independently plausible product boundary is narrower:

> **post-PR, target-specific dependency-update decision intelligence across multiple impact mechanisms and evidence classes, with explicit uncertainty, inspectable provenance, adaptive evidence acquisition where needed, and maintainer-centered decision support.**

Input:

```text
public repository
+ exact dependency-update PR / version transition
+ available upstream/package/CI/runtime evidence
```

Output:

```text
decision-relevant impact hypotheses
+ applicability evidence
+ explicit uncertainty / conflicts
+ what existing CI/runtime does or does not establish
+ next discriminating evidence action when needed
+ inspectable maintainer-facing decision support
```

This remains a hypothesis until Track C compares it to current UpgradePilot and later product-positioning work.

---

## 3. Architecture layers that Tier-1 showed must be separated

A mature design should not reduce the problem to “deterministic vs LLM vs agent.”

At least these layers exist independently:

### 3.1 Identity / revision layer

- repository;
- exact revision;
- PR/base/head;
- package/version transition;
- workflow/run/attempt/job/step identity;
- artifact/build identity.

### 3.2 Evidence-producer layer

Potential producers include:

- package/registry metadata;
- deps.dev;
- package-manager/build tools;
- GitHub APIs/logs;
- runtime telemetry;
- actionlint/zizmor;
- CodeQL;
- Griffe/API diff;
- code/build/test graph extractors;
- SBOM/provenance/attestation sources;
- model semantic extractors;
- human/maintainer declarations.

### 3.3 Repository-intelligence layer

Multiple views may coexist:

```text
CodeStructureView
BuildTestView
WorkflowView
DependencyView
SupplyChainView
DecisionEvidenceView
```

These should share stable identities where justified but need not collapse into one ontology.

### 3.4 Evidence normalization / provenance layer

Every imported fact should preserve enough metadata to answer:

- who/what produced it;
- from which revision/source;
- with which method;
- whether it is observed, inferred, emulated, symbolic, model-derived, human-declared, or externally attested;
- known completeness/coverage;
- whether it was independently validated.

Standards such as CycloneDX/SPDX/in-toto/SLSA may supply interoperability at this layer.

### 3.5 Discovery / reasoning layer

Possible mechanisms:

- deterministic queries;
- fixed semantic pipeline;
- bounded LLM reasoning;
- adaptive evidence planner;
- generalist agent;
- specialist/challenger ensemble.

### 3.6 Verification / admission layer

Separate from generation/reasoning:

- source binding;
- static analyzer;
- execution/test oracle;
- runtime telemetry;
- independent challenger;
- deterministic schema/policy checks;
- calibrated selective-risk policy.

### 3.7 Decision / UX layer

- orientation;
- key evidence;
- evidence-to-target connection;
- CI/runtime interpretation;
- uncertainty/conflicts;
- next discriminating check;
- final maintainer decision support.

### 3.8 Evaluation layer

Evaluation is architecture, not an afterthought:

- protected corpus;
- oracle quality;
- per-proposition accuracy;
- coverage;
- abstention;
- repeated agent runs;
- maintainer decision quality;
- cost/security/reproducibility.

---

## 4. Shared substrate pattern emerging from Tier-1

This is not yet an adopted architecture, but multiple independent systems converge on a reusable pattern:

```text
EXACT REVISION / UPDATE IDENTITY
        │
        ▼
EVIDENCE PRODUCERS
(static analyzers, package tools, upstream diff, runtime, external data)
        │
        ▼
NORMALIZED EVIDENCE + PROVENANCE
        │
        ├── repository structural views
        ├── build/test/workflow views
        ├── dependency/supply-chain views
        └── domain propositions / unresolved gaps
        │
        ▼
CONTEXT / QUERY INTERFACE
(progressive disclosure + on-demand raw source)
        │
        ▼
REASONING / INVESTIGATION
        │
        ▼
VERIFICATION / ADMISSION
        │
        ▼
MAINTAINER DECISION SUPPORT
        │
        ▼
EVALUATION / REPLAY / AUDIT
```

The main architectural competition now concerns **who owns reasoning and investigation at the middle of this stack**, not whether the stack needs evidence provenance at all.

---

# 5. Refreshed candidate architectures

## Candidate A — Deterministic Evidence Compiler

### Core idea

Treat UpgradePilot like a domain compiler/static-analysis pipeline.

```text
PR / repository / upstream evidence
→ deterministic extractors/analyzers
→ normalized evidence IR
→ deterministic proposition composition
→ explicit unresolved states
→ maintainer report
```

### World model

Typed records + optional multi-view graphs.

External tools may include:

- CodeQL;
- actionlint/zizmor;
- Griffe;
- package-manager/build tools;
- deps.dev;
- runtime telemetry parsers.

### LLM role

Minimal/optional:

- unstructured release-note extraction;
- explanation drafting;
- query assistance.

### Strengths

- strongest auditability/replay;
- bounded authority;
- easy proposition-level testing;
- predictable cost;
- clear failure states;
- good fit for stable recurring mechanisms.

### Weaknesses

- high engineering cost for long-tail semantics;
- risk of growing many narrow adapters;
- poor handling of novel repository conventions;
- may under-discover mechanisms not anticipated by designers.

### Best fit

Known, repeated, structurally analyzable dependency-update mechanisms.

### Tier-1 effect

Original Candidate A **survives**, but now includes mature external analyzers and standards adapters rather than assuming all analysis is handwritten.

---

## Candidate B — Structured Hybrid Impact Reasoner

### Core idea

Use deterministic evidence/structure to create a compact, high-quality cross-repository reasoning packet, then let an LLM own bounded semantic inference.

```text
upstream old/new evidence
+ target structural usage
+ CI/runtime/environment evidence
+ repository-purpose context
+ explicit gaps

→ evidence distillation

→ bounded semantic model

→ structured impact/applicability hypotheses

→ deterministic/static/executable validation where available

→ maintainer report
```

### World model

Multi-view structural/evidence substrate + compact semantic projection.

Raw source remains retrievable on demand for discovery, but trusted conclusions retain source/provenance binding.

### Model authority

Higher than Candidate A.

The model may infer:

- semantic relevance;
- likely impact mechanism;
- repository-purpose implications;
- missing evidence;
- candidate next checks.

Claims may be:

- verifier-confirmed;
- grounded but unverified;
- calibrated/accepted under selective-risk policy;
- unresolved.

### Strengths

- strong fit for cross-repository semantic changes;
- supported by Semgrep Upgrade Guidance and DepRepair-style results;
- lower orchestration overhead than a general agent;
- easier evaluation than open-ended agent trajectories.

### Weaknesses

- evidence preselection can omit decisive context;
- semantic inference remains probabilistic;
- fixed pipeline may fail when next evidence need depends strongly on intermediate results.

### Best fit

Most ordinary but semantically non-trivial dependency updates.

### Tier-1 effect

Original Candidate B **survives and becomes substantially stronger**.

It is now one of the most credible default mature architectures.

---

## Candidate C — Fixed-First Adaptive Investigation System

### Core idea

Use Candidate A/B as the normal path, then escalate to an adaptive planner only when material evidence gaps remain and several meaningful actions exist.

```text
fixed evidence pipeline
→ remaining decision-relevant gaps?

NO
→ conclude/report

YES
→ bounded investigation planner
→ choose evidence-acquisition action
→ deterministic admission
→ read/execute/query capability
→ state update
→ repeat / stop
```

### Available actions may include

- query repository structure;
- retrieve exact raw source;
- inspect upstream source/API diff;
- query CodeQL;
- inspect CI logs;
- inspect runtime telemetry;
- execute safe package-manager/build/test check;
- query external package intelligence;
- request maintainer input.

### Key property

The agent controls **sequence**, not evidence truth.

The tool interface and observation format are frozen/evaluated as part of the system.

### Strengths

- adaptivity only when useful;
- lower cost/risk than a generalist agent;
- naturally integrates explicit evidence gaps;
- highly replayable compared with unrestricted shell agents;
- compatible with fixed-pipeline baselines.

### Weaknesses

- tool/action catalog requires design;
- can still over-investigate;
- may fail on truly novel repository behavior outside the catalog;
- planner quality depends heavily on interface design.

### Best fit

Cases where the useful next action is state-dependent but the problem remains inside known evidence families.

### Tier-1 effect

This is the strongest refresh of the original bounded-agent idea.

Original Candidate C **splits**:
- bounded adaptive investigation becomes this Candidate C;
- broad generalist agent moves to Candidate E.

---

## Candidate D — Runtime / Execution-Assisted Evidence System

### Core idea

Resolve as many uncertain propositions as practical through controlled execution or direct runtime observation rather than increasingly complex static reconstruction.

```text
static source / workflow evidence
→ identify proposition

→ controlled execution OR historical/instrumented runtime telemetry

→ correlate runtime observation to exact source/revision/step

→ derive stronger evidence

→ compose with static/semantic reasoning
```

### Possible evidence sources

- GitHub native logs/debug logs;
- StepSecurity-like process/network/file telemetry;
- real package-manager resolution/build execution;
- targeted tests;
- isolated reproduction;
- `act` only as emulated experimental evidence;
- symbolic execution for bounded pure predicates.

### Strengths

- converts inference into observation for some hard cases;
- may reduce need to model every shell/workflow combination statically;
- strong validation for repairs and environment claims;
- high value for CI/runtime semantics.

### Weaknesses

- environment fidelity;
- untrusted-code execution risk;
- cost/latency;
- missing historical instrumentation;
- test inadequacy;
- runtime event ≠ semantic success automatically.

### Best fit

Repositories where execution is reproducible/available and the proposition is operational rather than purely semantic.

### Tier-1 effect

This is a **new full candidate** that was underrepresented in the original six.

Tier-1 repeatedly showed execution/runtime evidence as strong enough to deserve architectural status.

---

## Candidate E — Sandboxed Generalist Repository Agent

### Core idea

Use a capable software-engineering agent with broad repository/search/tool access, but place operational authority outside the agent in a sandbox/policy runtime.

```text
update goal
→ generalist agent
→ inspect code/upstream/docs
→ query graphs/search
→ run analyzers
→ execute tests/build/package tools
→ revise hypothesis
→ stop under budget/policy
→ evidence-backed report
```

### World model

Broad repository visibility with progressive search/retrieval.

The agent can use:

- raw source;
- repository graphs;
- CI/runtime tools;
- web/upstream evidence;
- shell/test execution.

### Authority model

Operational effects constrained externally.

Semantic conclusions still require evidence/provenance and possibly independent validation.

### Strengths

- maximum long-tail flexibility;
- minimal need to pre-enumerate every repository structure;
- strong fit for unusual/custom build systems;
- useful escalation/comparator architecture.

### Weaknesses

- cost;
- long/variable trajectories;
- prompt injection/untrusted repository surface;
- harder replay/evaluation;
- unnecessary exploration;
- potential to conflate successful action with correct evidence.

### Best fit

Rare atypical repositories/cases where bounded capabilities cannot express a useful investigation.

### Tier-1 effect

Original Candidate C **survives only as an escalation/comparator**, not as the strongest default architecture.

---

## Candidate F — Evidence-Centric Multi-View Knowledge Platform

### Core idea

Make the core system a provenance-backed, queryable set of linked repository/evidence views, with different reasoners layered on top.

```text
code graph
build/test graph
workflow graph
dependency graph
supply-chain graph
decision/evidence graph
maintainer knowledge

→ stable identities + provenance links

→ query service / repository intelligence API

→ deterministic queries, LLM reasoner, or agent
```

### Key difference from original graph candidate

This is **not one universal graph ontology**.

It is:

> multiple bounded views with shared identity and evidence-backed cross-links.

### Strengths

- reusable substrate for many reasoning strategies;
- reduces rediscovery;
- supports progressive context;
- strong auditability if edges preserve producer/coverage;
- compatible with GUAC/CodeQL/RIG/RepoGraph lessons.

### Weaknesses

- substantial schema/infrastructure work;
- easy to over-engineer;
- cross-view identity and freshness are hard;
- value must be proven with concrete queries.

### Best fit

A mature multi-evidence system with repeated cross-domain queries.

### Tier-1 effect

Original Candidate D **survives but is corrected**:
- universal graph is weakened;
- multi-view/federated graph becomes the stronger form.

This candidate may ultimately be a **substrate beneath A/B/C**, not a mutually exclusive product architecture.

---

## Candidate G — Selective Human Decision-Support Architecture

### Core idea

Optimize the entire system for high-quality human decisions under uncertainty rather than autonomous verdicts.

```text
evidence / analysis
→ findings + alternatives + uncertainty
→ calibrated selective acceptance / abstention
→ interactive next-check choices
→ maintainer orientation + analytical support
→ human decision
```

### Evaluation is built into architecture

A claim may be admitted because:

- deterministically established;
- independently verified;
- executable/runtime confirmed;
- or model-derived under an empirically validated selective-risk policy.

The report preserves which class applies.

### UX structure

```text
orient
→ show decisive evidence
→ explain applicability
→ explain CI/runtime proof limits
→ show unresolved conflict
→ offer next discriminating action
→ support final decision
```

### Strengths

- aligned with actual maintainer workflow;
- allows correct abstention;
- avoids false goal of maximizing automation;
- integrates calibration and explainability honestly.

### Weaknesses

- requires human-factor evaluation;
- more difficult to measure than benchmark pass rate;
- can become verbose/noisy if prioritization is weak.

### Best fit

Potentially **all** mature architectures as the product-facing layer.

### Tier-1 effect

Original Candidate F is **reclassified**:
it is primarily a cross-cutting product/trust layer, not a separate reasoning engine.

---

# 6. Cross-cutting patterns that are no longer standalone architectures

## 6.1 Challenger / verifier

Original Candidate E becomes a selective mechanism:

```text
primary reasoner
→ material ambiguity / high consequence
→ independent challenger
→ static/runtime verifier
→ preserve disagreement
```

Use only where measured benefit exceeds cost.

Possible roles:

- omitted-mechanism discovery;
- counterexample search;
- source-grounding check;
- independent model sample;
- static analyzer vs model disagreement.

## 6.2 Calibrated selective prediction

Not a standalone engine.

It can govern model-derived claim admission in Candidates B/C/E/G.

## 6.3 Standards/provenance

SPDX/CycloneDX/in-toto/SLSA/Sigstore are interoperability/authentication layers, not dependency-update reasoning engines.

## 6.4 Remediation

Patch generation is now treated as an optional downstream subsystem, not part of the core decision engine.

---

# 7. Optional future remediation architecture

Tier-1 Report 03 suggests a clean downstream boundary:

```text
DECISION SYSTEM
→ establishes impact / evidence / unresolved state

optional:

REMEDIATION PLANNER
→ choose strategy / trade-off

PATCH ENGINE
→ deterministic recipe/codemod
   OR evidence-grounded model repair

VALIDATOR
→ tests/build/static/runtime evidence

→ revised decision state
```

Potential Python stack to test later:

```text
Griffe old/new API diff
+ target usage localization
+ migration evidence

→ known rule?
   LibCST deterministic codemod

→ novel evidence-rich change?
   bounded LLM repair → LibCST/edit patch

→ paradigm shift?
   interactive/generalist investigation

→ executable/static validation
```

This should not be pulled into the core product before decision-support value is established.

---

# 8. Original six candidates — refresh disposition

| Original candidate | Refresh disposition | Why |
| --- | --- | --- |
| A Formal / structural evidence engine | **SURVIVES → Candidate A** | strengthened by CodeQL/actionlint/Griffe/deps.dev/runtime analyzers |
| B Structured cross-repository semantic reasoner | **SURVIVES → Candidate B** | strongly supported by Semgrep + DepRepair patterns |
| C Sandboxed generalist investigation agent | **SPLITS** | bounded adaptive planner becomes Candidate C; generalist remains Candidate E escalation |
| D Evidence/repository graph + semantic agent | **SURVIVES BUT REFRAMED → Candidate F** | multi-view/federated repository intelligence stronger than one universal graph |
| E Parallel challenger/verifier | **RECLASSIFIED CROSS-CUTTING** | useful escalation/evaluation pattern, not full architecture |
| F Calibrated selective decision support | **RECLASSIFIED CROSS-CUTTING / PRODUCT LAYER → Candidate G** | calibration/abstention/UX applies across reasoning engines |

New major architecture:

- **Candidate D — Runtime / Execution-Assisted Evidence System**.

New optional subsystem:

- **Remediation Planner + Patch Engine + Validator**.

---

# 9. Which architectures look strongest after independent research?

This is **not Track C** and does not compare against current UpgradePilot.

Within Track B alone, the external evidence currently favors a **composite mature architecture family** rather than one pure candidate:

```text
MULTI-VIEW EVIDENCE / REPOSITORY INTELLIGENCE
(Candidate F as substrate)

          ↓

DETERMINISTIC EVIDENCE COMPILER
(Candidate A)
for mechanical/known propositions

          ↓

STRUCTURED HYBRID SEMANTIC REASONER
(Candidate B)
for open-ended semantic interpretation

          ↓ only when material gaps remain

FIXED-FIRST ADAPTIVE INVESTIGATION
(Candidate C)

          ↓ optional proposition-specific strengthening

RUNTIME / EXECUTION EVIDENCE
(Candidate D)

          ↓ rare long-tail escalation

GENERALIST SANDBOXED AGENT
(Candidate E)

          ↓

SELECTIVE HUMAN DECISION SUPPORT
(Candidate G)

          ↓

PROTECTED EVALUATION / REPLAY / HUMAN METRICS
```

This should be understood as an **independent external architecture hypothesis**, not a recommendation to retrofit UpgradePilot immediately.

---

# 10. Why this composite is stronger than the original framing

It resolves several false binaries:

### 10.1 deterministic vs AI

Use deterministic methods where the proposition is computable and semantic models where interpretation/generalization is required.

### 10.2 typed projection vs raw source

Use typed evidence for trusted reasoning state, while allowing controlled on-demand raw source for discovery.

### 10.3 fixed pipeline vs agent

Use fixed pipelines by default; escalate to agents only when next-action selection is genuinely state-dependent.

### 10.4 static vs runtime

Static analysis and runtime observation answer different propositions and can strengthen one another.

### 10.5 one graph vs no graph

Use multiple bounded structural views with provenance rather than one universal ontology.

### 10.6 confidence vs proof

Separate deterministic proof, runtime observation, model-derived claims, empirical calibration, and human judgment.

### 10.7 analysis vs remediation

Decision intelligence can exist independently of patch generation.

---

# 11. Architecture competitions still unresolved

These should enter Track C as explicit `UNCERTAIN — EXPERIMENT REQUIRED` candidates unless project evidence already resolves them.

## Competition 1 — custom workflow modeling vs CodeQL Actions

Question:

> should generic GitHub Actions CFG/dataflow remain bespoke or use/import CodeQL?

Discriminating experiment:
one real env-propagation/conditional package-manager case.

## Competition 2 — typed records vs multi-view graph substrate

Question:

> when do repeated cross-evidence queries justify a persistent graph/view layer?

Experiment:
build a small bounded graph for one real case and compare query complexity/reuse.

## Competition 3 — narrow typed model context vs progressive raw-source access

Question:

> does controlled raw-source/graph retrieval materially increase discovery recall without unacceptable noise?

Experiment:
same frozen impact cases, compare context modes.

## Competition 4 — fixed semantic pipeline vs adaptive investigation planner

Question:

> do state-dependent evidence actions improve resolution enough to justify agent complexity?

Experiment:
same evidence-gap corpus, fixed action plan vs bounded planner.

## Competition 5 — bounded planner vs generalist OpenHands-style agent

Question:

> on truly unusual repositories, does generalist flexibility outperform typed capabilities at acceptable cost/security?

Experiment:
small long-tail case set.

## Competition 6 — static inference vs runtime telemetry

Question:

> which unresolved CI/package-manager propositions become decisively observable with instrumentation?

Experiment:
instrument one workflow and compare inference/telemetry.

## Competition 7 — changelog extraction vs upstream API/source diff

Question:

> for Python updates, does Griffe/source-diff evidence materially improve impact discovery over release-text evidence?

Experiment:
real update corpus.

## Competition 8 — binary trusted/untrusted model output vs graded/selective authority

Question:

> can model-derived claims be admitted safely under empirical selective-risk thresholds?

Experiment:
protected semantic corpus + risk/coverage evaluation.

## Competition 9 — internal-only schema vs standards adapters

Question:

> how much of real UpgradePilot evidence maps cleanly to CycloneDX/SPDX/in-toto without semantic distortion?

Experiment:
one current evidence case → standards mapping.

## Competition 10 — machine output quality vs maintainer decision quality

Question:

> do richer UpgradePilot reports actually improve human decisions and reduce effort?

Experiment:
later controlled maintainer study.

---

# 12. Tier-2 promotion decision before Track C

Tier-1 exposed several interesting Tier-2 topics, but **none currently requires a full Tier-2 deep report before Track C**.

Reason:

- confidence/reputation signals were already sufficiently sampled through Dependabot/Merge Confidence;
- agent execution security was materially covered through OpenHands/OpenShell/StepSecurity/runtime-policy research;
- ecosystem extensibility was covered through Dependabot/Renovate/ORT/OpenRewrite adapter models;
- product positioning was narrowed through Tier-1 #01/#02 and maintainer UX research;
- multi-agent and calibrated-authority topics now have precise experiment questions.

Therefore:

> **do not delay Track C for more broad literature research.**

If Track C exposes one unresolved architecture choice that cannot be classified from current evidence, perform targeted research/experiment only for that competition.

---

# 13. Learning / exposure architecture

The research also now supports a deliberate learning path separate from product adoption.

Highest combined product + learning experiments:

1. **CodeQL Actions comparator**
   - workflow CFG/dataflow;
   - QL;
   - security/program analysis.

2. **Griffe + LibCST Python migration lab**
   - API diff;
   - structural transformations;
   - validation.

3. **Small RIG / repository graph experiment**
   - multi-view graphs;
   - build/test/CI architecture;
   - agent context.

4. **GUAC + CycloneDX/SPDX + deps.dev lab**
   - GraphQL;
   - SBOM;
   - evidence normalization;
   - supply-chain graphs.

5. **SLSA/in-toto/Sigstore artifact-attestation experiment**
   - provenance;
   - signing;
   - GitHub Actions supply-chain security.

6. **EvidenceGapPlanner trajectory evaluator**
   - agent metrics;
   - stopping;
   - evidence gain;
   - repeated-run evaluation.

7. **OpenHands generalist-agent comparator**
   - sandbox;
   - MCP/tool loop;
   - broad agent architecture.

8. **Python dependency-update protected evaluation corpus**
   - Docker;
   - benchmark engineering;
   - reproducibility;
   - calibration/evaluation.

These should be selected based on discriminating architecture questions, not executed all at once.

---

# 14. Independent mature architecture hypothesis

The strongest Track-B mature hypothesis after Tier-1 is:

```text
DEPENDENCY UPDATE PR
        │
        ▼
IDENTITY + ACQUISITION
exact repo/base/head/update/upstream/run identity
        │
        ▼
MULTI-PRODUCER EVIDENCE INGESTION
package metadata
source/API diff
repository structure
CI/workflow
runtime
package-manager/build tools
external standards/intelligence
maintainer knowledge
        │
        ▼
NORMALIZED PROVENANCE-BACKED EVIDENCE
+ multiple bounded repository views
+ explicit coverage / unresolved state
        │
        ▼
FIXED DETERMINISTIC ANALYSIS
for mechanical propositions
        │
        ▼
STRUCTURED SEMANTIC REASONING
for open-ended meaning/relevance
        │
        ▼
GAP?
  no ───────────────┐
  yes               │
   ▼                │
BOUNDED ADAPTIVE INVESTIGATION
   │                │
   ├─ optional runtime/execution evidence
   ├─ graph/source/upstream query
   └─ rare generalist-agent escalation
   │                │
   └────────────────┘
        ▼
VERIFICATION / ADMISSION
source/static/runtime/test/selective-risk
        │
        ▼
UNCERTAINTY-AWARE MAINTAINER DECISION SUPPORT
        │
        ▼
OPTIONAL REMEDIATION SUBSYSTEM
only when authorized/useful
        │
        ▼
PROTECTED EVALUATION + REPLAY + HUMAN OUTCOME METRICS
```

This is **Track B's strongest independent hypothesis**, not the final UpgradePilot architecture.

Track C must now challenge it against the actual current project architecture and evidence.

---

## 15. Step status

```text
Track A
  Step 1   limitation inventory                 COMPLETE
  Step 2A  project-conditioned classification  COMPLETE

Track B
  Step 2B-0 broad discovery                     COMPLETE
  Tier-1 #01–#07                                COMPLETE
  Step 2B-X candidate architecture refresh      COMPLETE

Track C
  Step 2C adversarial comparison                NEXT

Step 3
  whole-pipeline architecture map               BLOCKED BY 2C
```

No further broad research is required before starting Track C.
