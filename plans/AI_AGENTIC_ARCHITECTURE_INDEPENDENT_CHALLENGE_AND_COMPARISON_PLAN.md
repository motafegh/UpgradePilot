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

