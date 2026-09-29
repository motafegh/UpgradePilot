# AI / Agentic Architecture Independent Challenge and Comparison Plan

**Status:** ACTIVE supporting analysis plan on `analysis/ai-agentic-capability-map-2026-09-28`.
**Authority:** This plan governs only the parallel AI/agent architecture investigation on this branch. It does not replace `MEMORY.md`, the active runtime-dependency-state plan, accepted specifications, ADRs, or product continuation on `main`.
**Purpose:** prevent the AI/agent architecture investigation from becoming a restatement of UpgradePilot's existing design assumptions by requiring both project-conditioned reasoning and a separately derived external/first-principles challenge before any end-to-end architecture is proposed.

## 1. Why this plan exists

The first two analysis steps were useful but methodologically anchored:

```text
current UpgradePilot source
+ accepted specifications / ADRs
+ existing plans
+ prior LLM/agent experiments
+ product-simulation evidence
→ limitation inventory
→ mechanism classification
```

That is strong **internal architectural reconciliation**, but it is not independent validation of the architecture.

This plan adds a second derivation path:

```text
product problem + user boundary
+ current external research / real systems / empirical evidence
- UpgradePilot's chosen implementation and architecture assumptions
→ independently derived candidate architectures
```

Then the two are compared explicitly.

No research process is literally unbiased. The goal is **de-anchoring and adversarial independence**, not a false claim of perfect neutrality.

## 2. Track A — project-conditioned analysis

Track A intentionally uses UpgradePilot's existing owners and evidence.

Inputs include:

- current product source and tests;
- `PROJECT_CHARTER.md`;
- accepted specifications and ADRs;
- active and historical plans;
- existing LLM semantic extraction;
- EvidenceGapPlanner and LangGraph experiments;
- product-simulation scenarios and audits;
- current explicit unsupported/unresolved/deferred states.

Track A answers:

> Given the architecture UpgradePilot currently has, where do deterministic logic, LLM semantics, agentic investigation, hybrid composition, and explicit unresolved states fit best?

The Step-1 limitation inventory and Step-2 mechanism classification already constitute the first complete Track-A pass.

Track A remains valuable. It is not to be discarded merely because it is conditioned by current design.

## 3. Track B — independent / de-anchored architecture derivation

### 3.1 Research brief

Track B starts from only the product problem and externally necessary constraints:

```text
User:
maintainer of a public Python OSS repository receiving dependency-update PRs

Input:
public repository + dependency-update PR

Needed outcome:
trustworthy, explainable, uncertainty-aware evidence and decision support
about whether/how the dependency update affects the exact target repository

Core realities:
external evidence can be incomplete/conflicting
software meaning can be semantic and open-ended
runtime evidence may be expensive/unavailable
the system must remain secure and auditable
human maintainer retains decision authority
```

Do **not** treat UpgradePilot's current architecture choices as requirements during derivation.

In particular, Track B must not assume in advance that:

- deterministic code must own every trusted proposition;
- models may only consume typed projections;
- agents must always use a permanently closed tool catalog;
- impact discovery must use the current A→B→C structure;
- final synthesis must use a deterministic PermissionEnvelope;
- static analysis must precede model reasoning;
- LangGraph/LangChain should or should not be used;
- multi-agent designs are inappropriate;
- current evidence-state vocabulary is optimal;
- current package/CI responsibility decomposition is optimal.

Those are hypotheses to test later, not premises for Track B.

### 3.2 External research areas

Research current approaches and evidence across at least these families where materially relevant:

- automated dependency-update systems and software supply-chain analysis;
- software change-impact analysis;
- program analysis, abstract interpretation, symbolic execution, and bounded execution;
- CI/workflow semantics and runtime observability;
- code intelligence and repository-scale semantic search;
- LLM code reasoning and tool-use agents;
- agentic software engineering / debugging / investigation systems;
- retrieval-augmented code reasoning;
- verifier-guided LLM systems;
- LLM + execution/sandbox architectures;
- provenance/evidence graphs and knowledge-graph approaches;
- planning/search approaches for diagnostic investigation;
- multi-agent/debate/specialist architectures where evidence exists;
- human-in-the-loop decision-support systems;
- uncertainty/calibration/evaluation methods for model-assisted software reasoning.

Use current authoritative documentation, recent research, credible engineering reports, real tools/systems, and empirical evidence where available.

Do not search only for approaches that resemble UpgradePilot.

### 3.3 Alternative generation requirement

Track B must produce multiple materially different candidate architectures before comparing to UpgradePilot.

At minimum include credible versions of:

1. **deterministic-heavy / formal-analysis architecture**;
2. **LLM-first repository reasoner with deterministic/verifier guardrails**;
3. **tool-using agent architecture with execution/sandbox feedback**;
4. **hybrid evidence-graph / semantic-reasoning architecture**;
5. any materially stronger architecture discovered during research.

Do not include a candidate merely to satisfy a count. Collapse candidates that are not meaningfully different.

For each candidate record:

- core data/evidence model;
- reasoning owner(s);
- model/tool visibility;
- authority/trust model;
- execution model;
- uncertainty representation;
- provenance/grounding strategy;
- failure behavior;
- evaluation strategy;
- operational cost/complexity;
- security implications;
- likely strengths;
- likely failure modes;
- which UpgradePilot product problems it handles especially well or poorly.

### 3.4 Adversarial questions

Track B must actively test propositions opposite to current UpgradePilot instincts, including:

- Could a sufficiently evaluated model/verifier system own some propositions more economically than handcrafted deterministic logic?
- Are typed model projections too restrictive for repository-scale reasoning?
- Would allowing an agent controlled raw-source access improve discovery materially without unacceptable trust loss?
- Could symbolic execution or workflow simulation resolve more CI/runtime questions than our current bounded structural approach?
- Is the current static/runtime boundary too conservative?
- Could executable/sandbox feedback replace significant semantic reconstruction work?
- Would an evidence graph or graph-search architecture reduce duplicated proposition-specific logic?
- Could one general code agent plus verifier outperform many hand-built semantic adapters?
- Are closed action catalogs a temporary evaluation scaffold rather than the mature agent architecture?
- Could multiple specialist agents provide measurable value for discovery, challenge, or verification?
- Are some current “deterministic authority” responsibilities better modeled as probabilistic claims with calibrated confidence plus independent checks?
- Are there important architectures or research directions the current project has not considered at all?

The purpose is not to force these alternatives to win. It is to make them compete fairly.

## 4. Track C — explicit comparison and challenge

Only after Track B produces its architectures should UpgradePilot's current architecture be reintroduced.

Compare Track A and Track B responsibility by responsibility.

For every important current principle/classification, assign one of:

```text
INDEPENDENTLY SUPPORTED
SUPPORTED BUT TOO RESTRICTIVE
SUPPORTED BUT TOO PERMISSIVE
SUPPORTED BUT INCOMPLETE
PROJECT-SPECIFIC CHOICE
HISTORICAL / NO LONGER JUSTIFIED
CONTRADICTED BY STRONGER APPROACH
UNCERTAIN — EXPERIMENT REQUIRED
```

Comparison must include:

- correctness / false-positive risk;
- ability to preserve uncertainty;
- coverage / recall;
- interpretability / auditability;
- security / mutation risk;
- latency/cost;
- implementation complexity;
- maintainability;
- replay/evaluation feasibility;
- adaptability to new package/ecosystem semantics;
- usefulness to a real maintainer;
- learning/portfolio value only after product value is assessed.

Do not declare UpgradePilot's existing architecture the winner merely because it is already implemented.

Do not declare a newer AI-heavy method superior merely because it is more modern or flexible.

## 5. Bias-control protocol

Because the researcher has already seen UpgradePilot's architecture, perfect blindness is impossible. Use procedural controls instead.

### 5.1 Separate evidence notes

Keep Track-B findings in a separate research section/artifact from Track-A conclusions until candidate architectures are generated.

Do not continuously rewrite external findings into UpgradePilot terminology during research.

### 5.2 Source diversity

Do not rely only on:

- agent-framework vendor documentation;
- OpenAI/Anthropic-style agent examples;
- formal-methods literature;
- LLM benchmark papers;
- UpgradePilot-like dependency bots.

Seek competing schools of solution.

### 5.3 Architecture-before-comparison

Write the independent candidate architectures **before** checking how neatly they map onto existing UpgradePilot modules/ADRs.

### 5.4 Counterevidence first

For major UpgradePilot principles, actively seek evidence that would falsify or weaken them.

### 5.5 No prestige proxy

Framework popularity, benchmark marketing, paper citation count, or model size is not sufficient evidence of suitability.

### 5.6 Separate capability from authority

A method may be capable of producing a correct answer without being appropriate as trusted authority. Compare both independently.

### 5.7 Separate current feasibility from mature architecture

Record when an architecture is conceptually better but currently too expensive/risky, and when a simpler current architecture is appropriate only as an interim step.

## 6. Revised analysis sequence

The parallel AI/agent architecture workstream now follows:

### Step 1 — project-conditioned limitation inventory
**Status: COMPLETE initial pass.**

### Step 2A — project-conditioned mechanism classification
**Status: COMPLETE initial pass.**

This is the existing deterministic / LLM / agentic / hybrid / unresolved classification.

### Step 2B — independent external research and architecture derivation
**Status: NOT STARTED.**

Use the de-anchored Track-B protocol above.

Outputs:

- external research evidence;
- materially different candidate architectures;
- explicit strengths/failure modes;
- findings that current UpgradePilot design has not considered.

### Step 2C — adversarial comparison and reconciliation
**Status: BLOCKED BY 2B.**

Compare Track-A and Track-B results.

Outputs:

- principle-by-principle challenge matrix;
- architecture gaps;
- over-conservative current choices;
- under-constrained current choices;
- independently supported current choices;
- experiments needed to decide unresolved competitions.

### Step 3 — end-to-end whole-pipeline architecture map
**Status: BLOCKED BY 2B + 2C.**

Only now construct the full Dependabot-PR → maintainer-output architecture.

The map must distinguish:

- current implemented reality;
- independently validated architecture direction;
- project-specific choices;
- experimental methods;
- unresolved architecture competitions;
- future possibilities.

### Step 4 — reconcile with existing AI/agent experiments

Determine which independently identified needs are already served by:

- support-drop semantic extraction;
- EvidenceGapPlanner;
- ordinary-Python orchestration;
- LangGraph;
- proposed DecisionSynthesizer;
- existing evaluation machinery.

This step now happens **after external challenge**, not before it.

### Step 5 — select actual architecture/design gaps

Only after the above decide whether any result deserves:

- specification change;
- ADR;
- bounded experiment;
- implementation plan;
- product Build;
- explicit deferral;
- or no action.

## 7. Stop lines

Do not:

- change product architecture merely because Track B finds an interesting method;
- alter `main` during this branch analysis;
- retrofit external findings to make current design look correct;
- throw away current deterministic work merely because an LLM-heavy architecture is plausible;
- run a framework experiment before the comparison identifies a real discriminating question;
- use product-simulation cases as both hidden oracle and supposedly independent evaluation without disclosure;
- claim “unbiased research”; use “independent/de-anchored challenge” accurately.

## 8. Completion condition

This plan is complete enough for Step 3 only when:

1. Track-A current analysis is preserved unchanged as the project-conditioned baseline;
2. Track-B has current external evidence and multiple materially different candidate architectures;
3. Track-C explicitly challenges current UpgradePilot principles rather than merely mapping external ideas onto them;
4. disagreements are preserved rather than prematurely reconciled;
5. unresolved architecture competitions identify a discriminating experiment or evidence need;
6. the resulting whole-pipeline map can state which choices are internally inherited versus independently supported.



## 9. Expanded external-research program — pre-research discovery

Ali broadened the investigation beyond AI/agent architecture alone. Before Track C, perform staged deeper research across the wider dependency-update decision-support ecosystem. The purpose is to discover product capabilities, architecture patterns, evidence sources, UX/policy mechanisms, standards, and evaluation methods that UpgradePilot may otherwise miss.

### 9.1 Research families and representative systems

1. **Closest dependency-update products and workflows**
   - Dependabot / dependabot-core
   - Renovate / Mend Merge Confidence
   - GitHub Dependency Review
   - Updatecli
   - Compare: update discovery, grouping, schedules/cooldowns, dashboards/approval, confidence/risk signals, CI use, human control, supported ecosystems, architecture/extensibility, and known limitations.

2. **Dependency risk, reachability, and upgrade-impact platforms**
   - Endor Labs Upgrade Impact Analysis + reachability
   - Semgrep Supply Chain reachability
   - Snyk Open Source
   - Socket
   - Compare: dependency graph construction, reachability/exploitability, behavioral/package risk, target-specific impact, prioritization, and evidence/claim strength.

3. **Remediation and migration engines**
   - OSV-Scanner guided remediation
   - OpenRewrite / Moderne
   - DepRepair and related dependency-repair research
   - API compatibility tools such as Griffe and japicmp
   - Study: graph-aware remediation, minimal-change strategies, codemods/recipes, API-diff detection, source migration, execution requirements, and rollback/failure handling.

4. **Dependency/package intelligence and graph foundations**
   - deps.dev / Open Source Insights
   - GUAC
   - OSS Review Toolkit
   - Trivy dependency/SBOM views
   - Study: graph models, historical package/version data, transitive relationships, advisory joins, package/project identity, query interfaces, and reusable evidence stores.

5. **Provenance, attestations, and software-supply-chain standards**
   - in-toto
   - SLSA build/dependency provenance
   - GitHub artifact attestations / Sigstore
   - SPDX, CycloneDX, VEX/OpenVEX
   - Study which existing standards could represent UpgradePilot evidence rather than inventing project-only schemas.

6. **CI/workflow semantics, observability, and runtime security**
   - actionlint
   - zizmor
   - StepSecurity Harden-Runner
   - act / workflow emulation
   - GitHub Actions runtime/attestation capabilities
   - Study static-versus-runtime evidence, workflow security, per-step process/network/file observations, environment fidelity, and whether runtime telemetry can close current evidence gaps.

7. **Program analysis and target-impact techniques**
   - CodeQL
   - Joern / Code Property Graphs
   - symbolic execution tools such as angr/CrossHair
   - API-diff and call/data-flow tools
   - Study whether general structural analysis can replace or complement proposition-specific rules.

8. **Repository intelligence and code-context architectures**
   - RepoGraph
   - LocAgent
   - Repository Intelligence Graph
   - AutoCodeRover and related repository localization systems
   - Study graph/IR world models, retrieval, context selection, localization, and cross-file/cross-component reasoning.

9. **AI code review and software-engineering agents**
   - GitHub Copilot code review / cloud agent
   - OpenHands
   - SWE-agent
   - Agentless
   - relevant review/agent systems discovered later
   - Study context access, instructions/skills/MCP, tool execution, autonomy, review authority, re-review, traceability, and human handoff.

10. **Risk/confidence/reputation signals**
    - Dependabot compatibility score
    - Renovate Merge Confidence
    - OpenSSF Scorecard
    - release age/adoption/cooldown signals
    - package behavior/reputation signals from Socket and similar systems
    - Study which population each signal represents, calibration, failure modes, and whether crowd evidence can legitimately affect a target-specific decision.

11. **Maintainer UX, policy, and workflow design**
    - Renovate Dependency Dashboard + approval/packageRules
    - Dependabot grouping/cooldown/scheduling
    - GitHub rulesets / dependency review
    - AI review workflows
    - Study prioritization, batching, approval, escalation, explanation, user control, and how to reduce review load without hiding uncertainty.

12. **Evaluation corpora, benchmarks, and uncertainty**
    - BUMP
    - DepBench / DepRepair
    - SWE-bench-style software-agent evaluation
    - calibration/selective-prediction research
    - product-simulation / replay methodologies
    - Study realistic ground truth, executable oracles, protected evaluation sets, error taxonomies, coverage-vs-risk, and human decision-quality metrics.

13. **Security boundaries for agentic execution**
    - sandbox/policy runtimes such as OpenShell
    - untrusted-repository and prompt-injection research
    - credentials/network/filesystem/mutation controls
    - Study whether broad agent autonomy can coexist with externally enforced authority and reproducible audit logs.

14. **Extensibility and ecosystem-generalization architecture**
    - Dependabot-core ecosystem adapters
    - Renovate managers/datasources/versioning modules
    - ORT analyzer/provider abstractions
    - OpenRewrite recipe ecosystem
    - Study how mature tools add ecosystems without central logic becoming brittle, and what should remain Python-first in UpgradePilot.

15. **Product positioning and maintainer-value research**
    - Compare the above systems by the actual maintainer question they answer.
    - Identify underserved space between “open an update PR”, “scan vulnerability/risk”, “migrate code”, “review PR”, and “provide trustworthy target-specific update decision support”.
    - Research maintainer pain, review burden, useful output shape, adoption friction, and differentiation before treating architecture sophistication as product value.

### 9.2 Pre-research findings that justify this expansion

The initial scan already found materially relevant patterns:

- Dependabot now exposes scheduling, cooldown and grouping, while its compatibility score is based on CI outcomes from other public repositories.
- Renovate provides a Dependency Dashboard/approval workflow, powerful package rules, and Merge Confidence based on release age, adoption, passing tests, and confidence.
- GitHub Dependency Review combines dependency diffs with vulnerability, license and scope policy.
- Endor Labs explicitly offers both reachability analysis and direct-dependency Upgrade Impact Analysis.
- Socket analyzes dependency behavioral changes such as install scripts, obfuscation, native code and privileged API use.
- OSV-Scanner guided remediation resolves the transitive graph and presents alternative remediation strategies with different change/risk trade-offs.
- OpenRewrite/Moderne show a recipe/codemod model where dependency upgrades can include source and build-file migration rather than only version replacement.
- deps.dev and GUAC demonstrate reusable dependency/supply-chain graph foundations.
- in-toto/SLSA/GitHub attestations demonstrate portable provenance claims rather than application-specific evidence only.
- StepSecurity demonstrates per-workflow-step runtime network/process/file evidence; zizmor demonstrates the complementary static-analysis boundary.
- Griffe demonstrates Python-specific deterministic API-break detection.
- GitHub Copilot code review demonstrates a modern PR-review UX combining repository instructions, skills/MCP context, agentic operations, re-review, and bounded approval configuration.

These are discovery signals only; each requires its own deeper report before being used as architecture evidence.

### 9.3 Deep-report protocol

When a research family's turn arrives, create a dated report instead of continuously expanding this plan.

Each report should record:

- research question and relevance to UpgradePilot;
- representative systems/projects and current versions/state where material;
- user workflow and product boundary;
- inputs/evidence acquired;
- internal representation/data model where observable;
- algorithms/models/analyzers/tools used;
- authority and trust boundaries;
- automation/actions/mutations;
- output/UX and policy controls;
- supported ecosystems and extensibility strategy;
- failure/uncertainty behavior;
- security and privacy model;
- evaluation/empirical evidence;
- strengths and limitations;
- transferable ideas;
- ideas that should **not** be copied;
- concrete hypotheses or experiments for later Track C;
- sources and date checked.

Do not convert a feature list into an UpgradePilot requirement during the report.

### 9.4 Priority / sequencing

Before Track C, perform deeper reports for the highest-leverage families:

**Tier 1**
1. closest dependency-update products/workflows;
2. risk/reachability/upgrade-impact platforms;
3. remediation/migration engines;
4. dependency/evidence graph foundations + provenance standards;
5. CI/runtime evidence and program-analysis techniques;
6. repository-intelligence/agent architectures;
7. evaluation + maintainer UX.

**Tier 2**
8. confidence/reputation signals;
9. agent execution security;
10. ecosystem extensibility;
11. product positioning / maintainer-value research.

**Tier 3 / trigger-driven**
12. multi-agent specialization;
13. probabilistic/calibrated claim authority;
14. hosted/local model routing and cost optimization;
15. other areas surfaced by Tier-1/2 reports.

### 9.5 Sequence correction

The previous “Step 2B complete enough for Track C” statement is superseded.

The new route is:

```text
Step 2B-0  broad pre-research discovery                  COMPLETE
Step 2B-1+ staged deep reports by research family        CURRENT / PENDING
Step 2B-X   independent candidate-architecture refresh   after sufficient Tier-1 reports
Step 2C     adversarial comparison with Track A          blocked by 2B-X
Step 3      whole-pipeline architecture map              blocked by 2C
```

The research program should remain finite: a deep report is justified when it can materially change product scope, architecture, evidence design, evaluation, security, or maintainer UX. Stop investigating a family when additional detail cannot change those decisions.


### 9.6 Deep-report progress

- **Tier-1 Report 01 — Closest dependency-update products/workflows:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-01_closest-dependency-update-products-and-workflows.md`
  - Systems: Dependabot/dependabot-core, Renovate/Mend Merge Confidence, GitHub Dependency Review, Updatecli.
  - Main provisional finding: the mature adjacent systems are strongest at update discovery/generation, orchestration, policy, security/license gating, CI/status integration, and maintainer queue control; the reviewed public product models do not document complete target-specific technical-impact reasoning as their core responsibility.
  - This finding remains provisional pending the risk/reachability/upgrade-impact platforms report.

- **Tier-1 Report 02 — Dependency risk, reachability, and upgrade-impact platforms:** NEXT.


- **Tier-1 Report 02 — Dependency risk, reachability, and upgrade-impact platforms:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-02_dependency-risk-reachability-and-upgrade-impact-platforms.md`
  - Systems: Endor Labs, Semgrep Supply Chain, Snyk Open Source, Socket.
  - Main correction: target-specific dependency impact analysis is already a real commercial capability. Endor and Semgrep explicitly connect dependency-version changes to target usage; Snyk and Socket expose application-level reachability with nuanced evidence states.
  - Revised provisional differentiation: UpgradePilot must be broader than vulnerability-remediation impact analysis and compete on cross-mechanism evidence composition, CI/runtime/environment proof, repository-purpose context, explicit uncertainty, adaptive investigation, and maintainer-facing decision traceability.
  - New architecture hypotheses: graph/IR substrate, upstream old→new source/API diff evidence, package-behavior delta analysis, graded producer authority, and asymmetric positive/negative reachability semantics.

- **Tier-1 Report 03 — Remediation and migration engines:** NEXT.


- **Tier-1 Report 03 — Remediation and migration engines:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-03_remediation-and-migration-engines.md`
  - Systems: OSV-Scanner Guided Remediation, OpenRewrite/Moderne, DepRepair/DepBench, Griffe, LibCST.
  - Main finding: remediation is not one responsibility; strategy selection, target-site localization, transformation execution, ecosystem graph/lock recomputation, and validation should remain separable.
  - External patterns: graph-level risk/reward remediation planning; deterministic semantic recipes; evidence-grounded single-call LLM repair; Python API-diff and codemod substrates; explicit partial/no-fix/unsupported outcomes.
  - New hypotheses: a Python-first remediation stack using upstream API diff + target localization + deterministic recipe or bounded model repair + LibCST transform + executable validation; repeated validated model repairs may potentially become deterministic reusable recipes.

- **Tier-1 Report 04 — Dependency/evidence graph foundations + provenance standards:** NEXT.


## 10. Dual-value research rule — product value + learning/exposure value

The external research program must evaluate tools, libraries, methods, standards, and frameworks on **two separate axes**.

### 10.1 Axis A — UpgradePilot product/architecture value

Ask:

- does this solve a real current/future UpgradePilot responsibility?
- does it improve correctness, coverage, evidence quality, security, UX, cost, or maintainability?
- is it better than a simpler existing approach?
- what concrete product pressure would justify adopting it?

### 10.2 Axis B — engineering learning / career exposure value

Also ask:

- would hands-on exposure teach a transferable engineering concept or toolchain?
- is the technology current, credible, and used in relevant software/AI/security/platform work?
- would implementing a bounded real use case build demonstrable capability?
- would it expose useful concepts that UpgradePilot otherwise would not teach?
- can the learning be evidenced by code, tests, evaluation, design notes, or an experiment?

Examples of potentially valuable exposure include:

- program-analysis frameworks;
- graph/query systems;
- AST/CST transformation;
- SBOM/provenance standards;
- policy engines;
- sandbox/runtime security;
- agent orchestration;
- static-analysis/query languages;
- package-manager/resolver integration;
- supply-chain security tooling;
- benchmark/evaluation infrastructure.

### 10.3 Keep the two axes independent

A technology may be:

```text
high product value + high learning value
→ strong adoption/experiment candidate

high product value + low novelty
→ still use it if it is the right engineering solution

low product value + high learning value
→ possible bounded learning experiment, but do not burden product architecture

low product value + low learning value
→ normally skip
```

Do not add technology to production merely for résumé value.

But also do not reject a technically reasonable option only because another simpler option exists when the alternative provides materially higher transferable learning value at proportionate cost.

This refines the project's “smartest instead of smallest” principle:

> choose proportionately strong solutions while accounting for both product quality and deliberate engineering skill acquisition.

### 10.4 Experience-evidence ladder

Use precise language for future portfolio/CV claims:

```text
RESEARCHED
read/evaluated/documented the tool
!= worked with it

HANDS-ON EXPERIMENTED
installed/configured/executed it on a bounded real case
→ may say experimented with / hands-on exposure

PROJECT-INTEGRATED
implemented it in UpgradePilot with source/tests/design evidence
→ may say worked with / integrated

VALIDATED / OPERATED
used it repeatedly against representative cases with evaluation/diagnostics
→ stronger practical experience claim
```

Never turn reading documentation into a “worked with” claim.

### 10.5 Required field in future deep reports

Every deep report must now include:

**Learning / exposure opportunities**

For each interesting tool/method:

- what it teaches;
- relevance to target career capability;
- hands-on experiment that would count as real exposure;
- estimated implementation/learning cost;
- whether product need independently justifies it;
- recommended exposure level: `research only / lab experiment / project experiment / product candidate / defer`.

A separate exposure ledger tracks these across reports.

### 10.6 Selection rule

When two technically acceptable approaches are close in product value, prefer the one that gives broader transferable engineering learning **if** it does not materially worsen correctness, maintainability, security, or schedule.

When learning value is the primary reason for trying a technology, keep it explicitly bounded as an experiment and evaluate it against the simpler baseline.


- **Tier-1 Report 04 — Dependency/evidence graph foundations + provenance standards:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-04_dependency-evidence-graphs-and-provenance-standards.md`
  - Systems/standards: deps.dev, GUAC, ORT, SPDX 3.0.1, CycloneDX 1.7, SLSA 1.2, in-toto v1.2, Sigstore/Cosign, GitHub artifact attestations/dependency submission.
  - Main finding: mature standards already cover package/dependency graphs, build provenance, explicit no-assertion/completeness semantics, evidence techniques/confidence, claims/counterclaims, assessors, call stacks, citations, and attestation binding. They do not replace UpgradePilot's target-specific decision semantics.
  - Strongest current hypothesis: keep a domain-specific internal reasoning model but seriously evaluate standards adapters/import/export/attestation rather than inventing isolated provenance vocabulary.
  - Learning candidates: GUAC/GraphQL, CycloneDX, SPDX, SLSA/in-toto/Sigstore, deps.dev; ORT as a heavier pipeline comparator.

- **Tier-1 Report 05 — CI/runtime evidence + program-analysis techniques:** NEXT.


- **Tier-1 Report 05 — CI/runtime evidence + program-analysis techniques:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-05_ci-runtime-evidence-and-program-analysis.md`
  - Systems/methods: actionlint, zizmor, GitHub Actions native logs/runtime model, StepSecurity Harden-Runner, act, CodeQL Actions/Python, Joern, CrossHair, angr.
  - Main finding: UpgradePilot's CI problem spans distinct layers—Actions semantics, shell semantics, package-manager semantics, runtime observation, and target decision logic—and mature tools already cover significant portions of the first and fourth layers.
  - Most important comparator: CodeQL's dedicated GitHub Actions AST/CFG/inter-step dataflow model. Before expanding bespoke workflow-graph/env-propagation logic, run a bounded CodeQL comparison against one real UpgradePilot case.
  - Runtime finding: instrumented process/network/file telemetry can convert some static execution inference into direct observation, but observed process execution still does not establish package-manager semantic success/state.
  - Learning candidates: CodeQL, actionlint, zizmor, StepSecurity, act, Joern, CrossHair; angr as a separate security/formal-method lab.

- **Tier-1 Report 06 — Repository-intelligence and agent architectures:** NEXT.


- **Tier-1 Report 06 — Repository-intelligence and agent architectures:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-06_repository-intelligence-and-agent-architectures.md`
  - Systems/research: RepoGraph, LocAgent, RIG, CodexGraph, CodeRAG-Bench, Sourcegraph Code Graph/Cody, AutoCodeRover, SWE-agent, OpenHands, Agentless, current GitHub Copilot repository instructions/skills/MCP patterns.
  - Main finding: repository intelligence decomposes into world-model representation, retrieval/localization, repository knowledge/instructions, agent-computer interface, execution feedback, and reasoning topology. Treating all of this as generic “context” hides critical architecture choices.
  - Strongest current hypothesis: use multiple evidence-backed repository views with stable identities, progressive disclosure, on-demand raw-source access, and a stable repository-intelligence capability interface; keep fixed pipelines as the baseline and introduce adaptive agents only where state-dependent evidence selection earns its cost.
  - New architecture challenge: the code graph, build/test graph, supply-chain/evidence graph, and decision/proposition graph may need to remain distinct but linkable rather than becoming one universal graph.
  - Learning candidates: small Python code graph, RIG-like build/test graph, Neo4j/Cypher lab, retrieval comparison, OpenHands comparator, and UpgradePilot-specific ACI/tool-interface experiment.

- **Tier-1 Report 07 — Evaluation, maintainer UX, and decision-quality measurement:** NEXT.


- **Tier-1 Report 07 — Evaluation, maintainer UX, and decision-quality measurement:** COMPLETE.
  - Record: `working-memory/2026-09-29_tier1-07_evaluation-maintainer-ux-and-decision-quality.md`
  - Evidence: BUMP, DepBench/DepRepair, SWE-bench/Verified/later benchmark audits, SWE-rebench, agent trajectory/framework studies, code-model calibration/selective prediction, Dependabot maintainer study, code-review decision-making/XAI research, HiLDe.
  - Main finding: UpgradePilot needs a layered evaluation stack spanning case/oracle quality, fact/evidence correctness, discovery coverage, applicability, investigation efficiency, calibration/abstention, report fidelity, maintainer decision quality, and operational cost/security.
  - Critical principle: unresolved/abstain can be the correct outcome and must be scored as such; decisiveness is not equivalent to quality.
  - Benchmark lesson: evaluation datasets themselves need quality/freshness/contamination/oracle audits. Popular benchmark scores are insufficient evidence.
  - Product metric direction: measure whether maintainers reach better evidence-informed decisions with less effort and appropriate trust—not autonomous action rate or persuasive agreement.
  - Learning candidates: SWE-bench-style containerized eval harness, Python BUMP/DepBench-style corpus, calibration/risk-coverage analysis, agent trajectory analytics, and later maintainer user-study design.

### 9.7 Tier-1 completion checkpoint

All planned Tier-1 deep reports are COMPLETE:

1. closest dependency-update products/workflows;
2. risk/reachability/upgrade-impact platforms;
3. remediation/migration engines;
4. dependency/evidence graph foundations + provenance standards;
5. CI/runtime evidence + program-analysis techniques;
6. repository-intelligence and agent architectures;
7. evaluation, maintainer UX, and decision-quality measurement.

**Next:** Step 2B-X — refresh the independently derived candidate architectures using the complete Tier-1 evidence before Track C.

The refresh must:
- revisit the original candidate architectures without privileging them;
- incorporate product-scope corrections discovered in Tier 1;
- identify new hybrid patterns that did not exist in the original six;
- explicitly include evaluation/UX architecture, not only reasoning architecture;
- identify which architecture competitions need hands-on experiments;
- identify whether any Tier-2 family must be promoted before Track C because Tier-1 evidence exposed a material missing dimension.
