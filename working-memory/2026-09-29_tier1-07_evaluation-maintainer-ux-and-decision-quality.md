# Tier 1 Report 07 — Evaluation, Maintainer UX, and Decision-Quality Measurement

**Recorded:** 2026-09-29  
**Branch:** `analysis/ai-agentic-capability-map-2026-09-28`  
**Status:** COMPLETE initial deep report  
**Research family:** Evaluation, benchmark quality, calibration/abstention, maintainer UX, human decision support  
**Primary evidence examined:** BUMP, DepBench/DepRepair, SWE-bench / SWE-bench Verified / later benchmark audits, SWE-rebench, coding-agent trajectory studies, calibration/selective-prediction research, Dependabot maintainer studies, code-review decision-making/XAI studies, HiLDe  
**Purpose:** define how UpgradePilot should evaluate deterministic evidence, LLM components, agentic investigation, final maintainer reports, and the product as a whole without optimizing only for benchmark pass rate, persuasive prose, or autonomous action rate.

This report records external research evidence only. It does not set final product KPIs or authorize any model/agent deployment.

---

## 1. Core question

How should UpgradePilot prove that it helps a maintainer make **better dependency-update decisions**?

That is different from proving:

- a model produced a plausible explanation;
- an agent completed a trajectory;
- a test suite passed;
- a benchmark case was “solved”;
- the system generated fewer unresolved states;
- the maintainer agreed with the system;
- the system acted autonomously.

The evaluation target must match the product responsibility.

---

## 2. Executive result

A single top-line metric is inadequate.

The research supports a **multi-layer evaluation stack**:

```text
LAYER 1 — DATASET / ORACLE QUALITY
Is the case itself valid, reproducible, sufficiently specified, fresh, and uncontaminated?

LAYER 2 — FACT / EVIDENCE QUALITY
Did each analyzer/evidence producer establish the claimed proposition correctly?

LAYER 3 — DISCOVERY / COVERAGE
Did the system find the relevant impact mechanisms, target locations, and missing evidence?

LAYER 4 — INVESTIGATION QUALITY
Did it choose useful next actions, avoid waste, stop appropriately, and preserve uncertainty?

LAYER 5 — SYNTHESIS / CALIBRATION
Are accepted claims correct, uncertainty calibrated, required caveats preserved, and abstention appropriate?

LAYER 6 — MAINTAINER DECISION QUALITY
Does the output help a maintainer orient, understand, verify, choose next actions, and decide faster/better?

LAYER 7 — OPERATIONAL QUALITY
Latency, token/tool cost, reproducibility, security, failure recovery, and maintenance burden.
```

The strongest product metric is therefore unlikely to be:

```text
% PRs automatically approved
```

or:

```text
% benchmark cases “solved”
```

A more defensible product objective is:

> **increase the proportion of dependency-update decisions that are correctly informed by decision-relevant evidence, while reducing maintainer effort and preserving appropriate uncertainty.**

---

## 3. BUMP — reproducibility is part of ground truth

BUMP contains 571 reproducible breaking dependency updates from 153 Java/Maven projects.

Its important methodological contribution is not merely the number of cases.

For each accepted breaking update:

```text
pre-update state
→ build/test succeeds

dependency-only update
→ reproducible failure

containerized environment
→ failure preserved over time
```

Failure categories include compilation, tests, dependency resolution, enforcer rules, lock failures, warning-as-error behavior, and others.

### Evaluation lesson

A useful dependency-update benchmark should preserve:

- exact repository revisions;
- exact dependency transition;
- exact environment/toolchain;
- before/after outcome;
- failure category;
- reproduction command;
- artifacts needed to rerun later.

A textual “this PR broke” label is much weaker than an executable reproduction.

### Limitation

BUMP focuses on observable build/test failures.

It does not represent the much harder classes UpgradePilot cares about where:

- CI remains green;
- impact is behavioral or deployment-specific;
- evidence is missing;
- a change is relevant but not automatically test-covered.

So BUMP is useful but insufficient as the whole evaluation corpus.

Sources:
- https://arxiv.org/abs/2401.09906
- https://github.com/chains-project/bump/

---

## 4. DepBench / DepRepair — executable repair oracle + cross-repository evidence

DepBench contains 95 dependency-update repair cases across multiple ecosystems, including PyPI.

Each case includes a Docker-based executable oracle using the consumer's own tests.

This provides a strong pattern:

```text
known update breakage
+ upstream evidence
+ consumer repository
→ proposed repair
→ execute consumer oracle
→ pass / fail
```

DepRepair also provides useful subcategories:

- direct rename;
- compound API migration;
- import migration;
- paradigm shift.

### Evaluation lesson

UpgradePilot should eventually evaluate by mechanism class, not only aggregate accuracy.

A system can appear strong overall while failing systematically on:

- paradigm shifts;
- packaging changes;
- CI/environment issues;
- indirect/plugin activation;
- runtime-only mechanisms.

### Important limitation

Passing the executable oracle proves only what the oracle exercises.

Therefore:

```text
tests pass
!=
global compatibility proven
```

A repair benchmark needs both executable correctness and explicit oracle/coverage limitations.

Source:
- https://arxiv.org/abs/2607.17957

---

## 5. SWE-bench history — benchmark quality must itself be evaluated

SWE-bench became a major coding-agent benchmark because it uses real GitHub issues and executable tests.

SWE-bench Verified was later created because the original benchmark contained tasks with:

- underspecified issue descriptions;
- tests that rejected valid solutions;
- other unsound evaluation conditions.

Professional software developers manually reviewed cases to create a 500-case verified subset.

By 2026, OpenAI stopped treating SWE-bench Verified as a meaningful frontier signal because benchmark contamination had become substantial.

A later 2026 audit of SWE-Bench Pro estimated roughly 30% of tasks were broken, including:

- overly strict tests;
- underspecified prompts;
- low-coverage tests that allowed incomplete solutions;
- misleading problem descriptions.

Meanwhile newer efforts such as SWE-rebench attempt to continually collect fresh executable tasks to reduce contamination and improve diversity.

### UpgradePilot lesson

The benchmark is itself an engineered product.

Every protected UpgradePilot case should carry a **case-quality record**:

```text
case identity
source provenance
repository revision
dependency transition
known ground truth
oracle type
oracle limitations
environment reproducibility
human review state
contamination/leakage risk
difficulty/mechanism labels
date admitted
```

A failing model/system should not automatically be blamed until the case and oracle are audited.

### Strong evaluation rule

> **Never use the same opaque artifact as both evidence input and hidden oracle unless the leakage is explicitly intended and measured.**

Sources:
- https://openai.com/index/introducing-swe-bench-verified/
- https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- https://arxiv.org/abs/2505.20411
- https://arxiv.org/abs/2602.23866

---

## 6. Evaluation must separate model capability from scaffold/tool capability

Current SWE-bench leaderboards explicitly separate arbitrary agent systems from “bash-only” configurations using the same minimal agent environment.

That reflects an important problem:

```text
model
+ prompt
+ retrieval
+ tools
+ agent interface
+ execution budget
+ retry policy
= observed system performance
```

A model score cannot be interpreted independently of its scaffold.

### UpgradePilot implication

When evaluating LLM/agent components, freeze and record:

- model/version;
- temperature/sampling settings;
- context projection;
- repository tools;
- action catalog;
- exact prompts/instructions;
- budget;
- retry count;
- stopping rules;
- external analyzers available;
- validation/rebinding behavior.

Otherwise a comparison such as:

```text
Model A > Model B
```

may actually mean:

```text
Tool/interface/configuration A > B
```

---

## 7. Repeated runs and trajectory evaluation

Software-engineering agents are stochastic systems.

Empirical studies of agent frameworks and trajectories show that:

- frameworks trade effectiveness, execution efficiency, and token/cost overhead differently;
- failed trajectories may be longer/more variable;
- context gathering and validation behavior are often associated with success;
- model capability may dominate framework choice as models improve;
- raw trajectory length alone is a confounded quality metric.

### UpgradePilot implication

Agent evaluation should report distributions, not one lucky run.

For each case/model/configuration:

```text
N repeated runs
→ success / correct-stop rate
→ action count
→ tool-call count
→ token/cost
→ wall time
→ evidence acquired
→ invalid actions
→ authority violations
→ unnecessary actions
→ stopping quality
→ trajectory variance
```

A planner that succeeds once after 35 unnecessary actions is not equivalent to one that reliably reaches the right evidence in 4 actions.

Sources:
- https://arxiv.org/abs/2511.00872
- https://arxiv.org/abs/2511.00197
- https://arxiv.org/abs/2604.02547

---

## 8. Calibration and selective prediction

Code-generation calibration research finds that model confidence is generally poorly calibrated by default.

Other research shows that uncertainty estimates can correlate with correctness and can support abstention policies.

Selective Code Generation goes further by combining generated tests/dynamic analysis with selective prediction to control the error rate among non-abstaining outputs.

### Key distinction

UpgradePilot should separate:

```text
MODEL CONFIDENCE
how sure the model says/is estimated to be

from

EVIDENCE STRENGTH
what observations/proofs support the proposition

from

EMPIRICAL SELECTIVE RISK
historically measured error among accepted outputs under a fixed policy
```

These are not interchangeable.

### Potential metric family

For a model-derived proposition:

- coverage: fraction of cases where the model/system accepts a claim rather than abstains;
- accepted-claim precision;
- false-positive rate;
- false-negative rate;
- calibration error;
- risk vs coverage curve;
- out-of-distribution behavior;
- performance by mechanism class.

This is a stronger evaluation than asking the model to emit “confidence: 0.91”.

Sources:
- https://arxiv.org/abs/2402.02047
- https://arxiv.org/abs/2502.11620
- https://arxiv.org/abs/2505.13553

---

## 9. Maintainer UX: code review is a decision-making activity

A 2026 empirical study observed 34 real code reviews by 10 developers and modeled review as a two-phase decision process:

```text
ORIENTATION
understand context, rationale, expectations, scope

→

ANALYTICAL LOOP
understand implementation
assess consequences
seek missing information
choose next action
eventually vote/decide
```

The study also emphasizes that reviewers routinely leave the code-review tool to gather information from:

- issue trackers;
- documentation;
- CI;
- local execution;
- team knowledge;
- other systems.

### UpgradePilot implication

A good maintainer report should not merely dump findings.

It should support the same cognitive sequence:

```text
1. ORIENT ME
What changed? Why might it matter here?

2. SHOW DECISION-RELEVANT EVIDENCE
What is established, unresolved, conflicting?

3. SHOW THE CONNECTION
Why does this evidence apply to this repository/environment?

4. TELL ME WHAT EXISTING CI DOES/DOES NOT ESTABLISH

5. SHOW THE NEXT DISCRIMINATING ACTION
What should be checked next, if anything?

6. SUPPORT MY FINAL DECISION
without replacing it
```

This is much closer to UpgradePilot's product goal than a generic “AI code review comment.”

Source:
- https://link.springer.com/article/10.1007/s10664-025-10791-2

---

## 10. Explanation quality should not be measured by agreement alone

A 2026 study on explainable AI in code review compared AI review systems with different explanation levels.

It found that richer explanations increased perceived trust, while the condition with moderate explanation achieved the highest agreement with AI recommendations. More explanation did not simply maximize agreement.

### Important lesson

```text
user agrees with AI
!=
AI was correct
```

and:

```text
user trusts AI more
!=
decision quality improved
```

A good explanation may cause a maintainer to **disagree more appropriately** because the reasoning is inspectable.

### UpgradePilot UX metrics should therefore distinguish

- factual comprehension;
- appropriate trust;
- ability to identify a deliberately wrong system conclusion;
- decision accuracy;
- decision time;
- number of external lookups needed;
- confidence calibration of the human;
- perceived usefulness;
- explanation clarity.

Source:
- https://arxiv.org/abs/2607.24601

---

## 11. Human-in-the-loop interaction can improve outcomes

HiLDe's human-in-the-loop code-generation study exposed consequential model choices and let users intervene.

In a study with 18 participants on security-related tasks, participants generated fewer vulnerabilities and aligned output better with their goals than with conventional code completion.

### UpgradePilot implication

Human control should not be reduced to:

```text
AI recommendation
→ approve / reject
```

There may be value in exposing key decision points:

- which impact mechanism should be investigated;
- which repository context is authoritative;
- whether a low-authority AI-derived claim may be considered;
- which expensive/runtime check is worth running;
- whether to accept a remediation strategy.

This supports **interactive decision support**, not just final human approval.

Source:
- https://arxiv.org/abs/2505.22906

---

## 12. Dependency-bot UX: notification fatigue and transparency are real product metrics

An empirical Dependabot study found mixed outcomes:

- adoption reduced technical lag;
- developers were receptive to many Dependabot PRs;
- compatibility scores were often too sparse to reduce update suspicion effectively;
- developers configured bots to reduce notification volume;
- notification fatigue and update suspicion were material concerns.

The study derived four desirable dimensions:

- configurability;
- autonomy;
- transparency;
- self-adaptability.

### UpgradePilot implication

A technically correct system can still fail as a product if it creates:

- too many findings;
- too many “possible issues” with low decision value;
- repeated unresolved warnings;
- too many follow-up actions;
- long reports for trivial updates.

Therefore evaluation needs **attention efficiency**.

Possible metrics:

- high-priority findings per PR;
- low-value finding rate;
- maintainer actions requested per PR;
- report reading time;
- investigation actions avoided;
- duplicate finding rate;
- notification/escalation frequency;
- proportion of cases closed without human deep dive.

Source:
- https://arxiv.org/abs/2206.07230

---

## 13. Proposed UpgradePilot evaluation matrix

No final KPI is adopted here. This is the independent research candidate to take into Track C.

### 13.1 Dataset quality

For every evaluation case:

- executable/replayable where possible;
- exact revisions;
- exact dependency transition;
- known mechanism labels;
- oracle reviewed;
- oracle limitation recorded;
- source/provenance recorded;
- freshness recorded;
- contamination/leakage risk recorded;
- difficulty recorded;
- protected test split separate from development examples.

### 13.2 Fact/evidence producer metrics

For each deterministic or external analyzer:

- proposition precision;
- proposition recall where ground truth exists;
- unsupported-state correctness;
- provenance correctness;
- revision identity correctness;
- false promotion rate;
- negative-claim correctness;
- analyzer coverage.

### 13.3 Candidate-discovery metrics

For each real update:

- relevant mechanism recall;
- unsupported candidate rate;
- duplicate candidate rate;
- candidate granularity;
- source grounding rate;
- discovery coverage honesty;
- novel-mechanism recall.

### 13.4 Applicability metrics

- applicable correctly established;
- not-applicable correctly established;
- unresolved correctly preserved;
- conflicted correctly preserved;
- false “not applicable” rate;
- false “applicable” rate.

The false negative here may be substantially more dangerous than an unresolved result.

### 13.5 Investigation planner metrics

- useful action chosen;
- unnecessary action count;
- action admission violations;
- stale-action attempts;
- evidence gain per action;
- cost/time per resolved proposition;
- stop correctness;
- over-investigation rate;
- under-investigation rate;
- repeated-run stability.

### 13.6 LLM semantic-component metrics

- structured output validity;
- source-grounding correctness;
- unsupported-claim rate;
- hallucination rate;
- paraphrase robustness;
- mechanism-variation robustness;
- accepted-claim precision;
- abstention/coverage;
- calibration/selective-risk curves;
- OOD performance.

### 13.7 Final synthesis/report metrics

- mandatory uncertainty preserved;
- contradictions preserved;
- evidence citations correct;
- no prohibited claim/action;
- action explanation supported;
- concise enough for actual use;
- conclusion stable under irrelevant-context perturbation;
- no misleading confidence.

### 13.8 Maintainer decision metrics

Using controlled user studies or structured maintainer simulation:

- correct decision rate;
- time-to-decision;
- time-to-orientation;
- number of external lookups;
- amount of evidence inspected;
- correct identification of system mistakes;
- appropriate trust/disagreement;
- perceived cognitive load;
- usefulness;
- retained understanding after review;
- ability to explain decision rationale.

### 13.9 Operational metrics

- end-to-end latency;
- API/model cost;
- tool calls;
- runtime jobs;
- cache/reuse rate;
- failure recovery;
- reproducibility;
- security-policy violations;
- maintenance complexity.

---

## 14. Case taxonomy is essential

Aggregate performance hides architecture weakness.

UpgradePilot cases should eventually be tagged along dimensions such as:

### Update mechanism

- API/signature;
- behavioral/default;
- import/module movement;
- packaging/install;
- build-tool/plugin;
- transitive resolution;
- platform/Python/runtime support;
- persisted-state format;
- CI/action/tooling;
- package behavior/security;
- paradigm shift.

### Evidence shape

- changelog sufficient;
- upstream source/API diff required;
- static target usage sufficient;
- runtime evidence required;
- repository-purpose context required;
- multi-source conflict;
- unavailable evidence.

### Decision difficulty

- direct/deterministic;
- semantic but bounded;
- investigation required;
- fundamentally unresolved.

### Repository characteristics

- simple Python package;
- application/service;
- CLI/tool;
- plugin framework;
- monorepo;
- generated code/artifacts;
- complex CI;
- weak/no tests.

This makes failures diagnostically useful.

---

## 15. Development set vs protected evaluation set

A critical methodological rule:

```text
cases used for architecture design / prompt tuning / feature development
!=
cases used for final comparative evaluation
```

UpgradePilot should maintain:

### Development corpus

Visible and reusable for:

- learning;
- debugging;
- prompt/tool development;
- regression creation.

### Protected evaluation corpus

Used only for evaluation decisions.

Ideally:

- recent/fresh cases;
- hidden expected outcomes where practical;
- mechanism diversity;
- not repeatedly inspected during implementation;
- periodically refreshed.

### Challenge corpus

Cases deliberately selected to stress:

- uncertainty;
- missing evidence;
- contradictory evidence;
- unusual repository patterns;
- unsupported syntax/tools;
- adversarial/noisy release notes;
- inadequate CI;
- model hallucination pressure.

This prevents “the system learned our examples” from being mistaken for generalization.

---

## 16. Evaluation of deterministic components must be as strict as AI evaluation

One danger is to apply rigorous evaluation only to LLMs while treating handcrafted rules as inherently trustworthy.

That is wrong.

Deterministic code can fail because:

- assumptions are incomplete;
- parsers mis-handle syntax;
- environment models omit a precedence source;
- graph extraction misses dynamic behavior;
- identity/correlation logic selects the wrong entity;
- tests encode the same mistaken assumption as implementation.

Therefore the same principles apply:

```text
explicit proposition
+ independent oracle
+ representative cases
+ negative cases
+ mutation/counterexample testing
+ coverage limitations
```

The comparison should be:

```text
best deterministic method
vs
best AI/hybrid method
```

not:

```text
AI gets empirical evaluation
while deterministic method is trusted by construction
```

---

## 17. Human evaluation design for UpgradePilot

A future maintainer study should avoid asking only:

> “Did you like the report?”

A stronger design could compare:

### Condition A — normal dependency PR

Maintainer gets:

- PR;
- release notes;
- repository CI.

### Condition B — deterministic UpgradePilot report

Adds structured target/evidence analysis.

### Condition C — hybrid UpgradePilot report

Adds semantic discovery/investigation/synthesis components.

Measure:

- final decision;
- decision correctness against adjudicated case truth;
- time;
- external searches;
- confidence;
- rationale quality;
- errors caught/missed;
- trust calibration;
- report sections actually used.

### Adversarial trust cases

Include some cases where UpgradePilot deliberately contains:

- one plausible but wrong AI suggestion;
- incomplete evidence;
- unresolved conflict.

Measure whether maintainers detect the problem.

A trustworthy system should help the user challenge it, not maximize agreement.

---

## 18. Product success hierarchy

A useful candidate hierarchy is:

```text
LEVEL 0 — technically runs
LEVEL 1 — individual evidence facts correct
LEVEL 2 — relevant mechanisms discovered
LEVEL 3 — applicability/uncertainty correct
LEVEL 4 — investigation efficient and justified
LEVEL 5 — synthesis faithful to evidence
LEVEL 6 — maintainer decision improves
LEVEL 7 — improvement persists at acceptable cost/noise/security
```

A system failing Level 2 cannot compensate with excellent prose at Level 5.

A system succeeding at Level 5 but increasing maintainer confusion fails Level 6.

---

## 19. Learning / exposure opportunities

### SWE-bench evaluation harness — high-value lab

What it teaches:

- containerized real-repository evaluation;
- hidden test/oracle design;
- agent benchmarking;
- task-quality problems;
- reproducibility.

Recommended:
bounded hands-on evaluation lab, not product dependency.

### BUMP / DepBench methodology — very high project relevance

Rather than loading the full heavy BUMP corpus immediately, reproduce the methodology on a small curated Python dependency-update corpus:

```text
pre-update image/state
vs
post-update image/state
+ exact oracle
+ mechanism label
```

This could become real UpgradePilot evaluation infrastructure.

### Fresh benchmark / contamination management

SWE-rebench-style ideas teach:

- continuously refreshed cases;
- contamination control;
- automatic environment construction;
- data-quality validation.

This is valuable ML/agent-evaluation engineering experience.

### Calibration / selective prediction

Implement risk-coverage curves for one current/future semantic model.

Skills:

- calibration;
- uncertainty estimation;
- threshold selection;
- abstention policy;
- statistical evaluation.

High-value AI engineering exposure.

### Agent trajectory analytics

Build a small trajectory evaluator for EvidenceGapPlanner:

- action sequence;
- state transitions;
- costs;
- invalid actions;
- evidence gains;
- stopping result.

This provides real agent-evaluation experience rather than only agent construction.

### Human-factor evaluation

Designing even a small structured maintainer study would teach:

- experiment design;
- usability metrics;
- trust calibration;
- qualitative/quantitative analysis;
- decision-support UX.

This is valuable but should happen only when the product surface is stable enough.

---

## 20. What should NOT be copied blindly

1. Do not optimize UpgradePilot for SWE-bench-style patch success; that is not its primary product responsibility.
2. Do not trust a benchmark because it is popular.
3. Do not use repository tests as the only oracle.
4. Do not interpret human agreement with AI as correctness.
5. Do not optimize for user trust independent of calibration.
6. Do not hide unresolved evidence merely to increase decisive-output rate.
7. Do not report only aggregate accuracy.
8. Do not evaluate one stochastic agent run per case.
9. Do not compare agents with different tools/budgets and call it a model comparison.
10. Do not use development cases as protected evaluation.
11. Do not evaluate AI rigorously while assuming deterministic rules are correct by construction.
12. Do not make autonomous-action rate a product-success metric unless autonomous action itself becomes an explicit user goal.
13. Do not create so many metrics that none drive decisions; each evaluation should answer a concrete architecture/product question.

---

## 21. Track-C hypotheses

1. UpgradePilot should have a layered evaluation architecture, not one benchmark score.
2. Case/oracle quality must be treated as first-class data with human audit and freshness.
3. Protected and development corpora must be separate.
4. Evaluation should be mechanism-stratified and evidence-shape-stratified.
5. Deterministic and AI approaches should compete under the same independent oracle where possible.
6. Unresolved/abstain can be a correct outcome and should be scored accordingly.
7. Model confidence, evidence strength, and empirically calibrated risk must remain separate concepts.
8. Agent evaluation must include repeated runs, action efficiency, stopping behavior, and authority violations.
9. The final product should be evaluated on maintainer decision quality/time/appropriate trust, not report persuasiveness.
10. UpgradePilot's UX should support orientation → analysis → next-action → decision, matching real review cognition.
11. Explanations should enable disagreement and verification, not maximize acceptance.
12. A Python-first reproducible dependency-update evaluation corpus could become one of the project's most valuable engineering artifacts.

---

## 22. Sources checked

### Dependency-update benchmarks
- https://arxiv.org/abs/2401.09906
- https://github.com/chains-project/bump/
- https://arxiv.org/abs/2607.17957

### Software-engineering agent evaluation
- https://openai.com/index/introducing-swe-bench-verified/
- https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- https://www.swebench.com/
- https://www.swebench.com/SWE-bench/guides/datasets/
- https://arxiv.org/abs/2505.20411
- https://arxiv.org/abs/2602.23866
- https://arxiv.org/abs/2609.08149

### Agent trajectory / framework evaluation
- https://arxiv.org/abs/2511.00872
- https://arxiv.org/abs/2511.00197
- https://arxiv.org/abs/2604.02547

### Calibration / selective prediction
- https://arxiv.org/abs/2402.02047
- https://arxiv.org/abs/2502.11620
- https://arxiv.org/abs/2505.13553

### Maintainer / human decision support
- https://arxiv.org/abs/2206.07230
- https://link.springer.com/article/10.1007/s10664-025-10791-2
- https://arxiv.org/abs/2607.24601
- https://arxiv.org/abs/2505.22906

---

## 23. Tier-1 checkpoint

**Tier-1 Report 07: COMPLETE.**

All initially planned Tier-1 deep families are now complete:

1. closest dependency-update products/workflows;
2. risk/reachability/upgrade-impact platforms;
3. remediation/migration engines;
4. dependency/evidence graph foundations + provenance standards;
5. CI/runtime evidence + program analysis;
6. repository intelligence + agent architectures;
7. evaluation + maintainer UX / decision quality.

Before Track C, perform the planned **Step 2B-X independent candidate-architecture refresh** using the full Tier-1 evidence.

That refresh should explicitly identify:

- which original six candidate architectures survive;
- which need modification;
- which new architecture patterns emerged;
- what product scope has narrowed;
- which architecture competitions now have enough evidence to decide;
- which still require hands-on comparative experiments;
- which Tier-2 research should be promoted before Track C because Tier-1 exposed a material gap.
