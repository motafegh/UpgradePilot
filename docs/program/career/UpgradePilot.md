# UpgradePilot — Governing Project Charter

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-19  
**Status:** Formally selected and final primary 90-day flagship project  
**Execution period:** 2026-07-20 to 2026-10-17  
**Authority:** Formal primary-project decision under `governance/EXECUTION_CONTRACT.md` Section 11  
**Current activation state:** Selection is final; planning is authorized; technical implementation is not yet authorized  
**Working identity:** **AI-augmented Python/data/ML engineer developing secure engineering capability.**

## 1. Decision and authority

UpgradePilot is the selected primary project for the 90-day execution period.

The broad project-comparison stage is closed. RunSleuth and other candidates are no longer competing primary projects. Reopening broad selection requires the formal change evidence defined in this charter and the Execution Contract.

This charter changes the primary-project allocation previously assigned to AegisLab:

- UpgradePilot receives the primary technical focus.
- Existing AegisLab execution plans, daily routes, weekly packages, milestone sequences, and implementation orders are **deferred and non-controlling**.
- `plans/90_DAY_MASTER_PLAN.md`, `plans/CURRENT_WEEK.md`, and any lower-level plan written for the AegisLab route must not govern UpgradePilot execution.
- AegisLab remains preserved as prior technical evidence and as a source of reusable controls or bounded components only when explicitly admitted by a later UpgradePilot plan.
- Sentinel remains a research archive and source of selectively reusable lessons or bounded work. It does not dictate the mission, architecture, modules, or roadmap.
- No AegisLab or Sentinel work becomes active merely because it already exists.

Until the next planning artifacts named in Section 24 are approved, no UpgradePilot implementation, repository creation, architecture build-out, data-collection campaign, model experiment, cloud deployment, or advanced-systems package may begin.

## 2. Governing specifications

This charter operationalizes:

1. `strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md`;
2. `strategy/PROJECT_SELECTION_AND_CAPABILITY_SPECIFICATION.md`;
3. `strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md`;
4. `governance/EXECUTION_CONTRACT.md`;
5. `strategy/STRATEGY_AND_SCOPE.md`.

When this charter conflicts with an older AegisLab-specific or candidate-comparison document, this charter controls the selected-project decision. It does not override higher-level safety, legal, privacy, workload, evidence, or ownership requirements.

## 3. Working definition

UpgradePilot is an evidence-backed dependency-update decision system for maintainers of public Python repositories.

> For an open-source Python maintainer reviewing an automated dependency-update pull request, UpgradePilot will produce a provenance-backed, uncertainty-aware recommendation to **merge after normal review, run targeted checks, investigate or block, defer, or abstain**. It will use the pull-request change, upstream release evidence, repository-specific dependency context, dependency relationships, and available CI evidence because existing signals are fragmented and a passing build, version number, compatibility score, or generated changelog alone does not establish that an update is appropriate for the repository.

UpgradePilot is not an automatic merge bot, a generic vulnerability scanner, a universal dependency platform, or a substitute for maintainer judgment.

## 4. Final selection basis

UpgradePilot has passed the formal selection gates because:

- the problem exists independently of the learning plan;
- the primary user and supported decision are specific;
- public, lawful, imperfect inputs are available;
- a weak end-to-end flow is feasible early;
- usefulness and quality can be evaluated beyond visual appearance;
- the project contains a nontrivial evidence and context thesis;
- the mission has sufficient curiosity and technical runway for 90 days;
- the product can remain bounded to one user, workflow, input family, and output family;
- the core can be implemented and progressively owned by Ali;
- the mission supports strong Python, data, SQL, testing, security, CI, ML, AI, and production-oriented capability;
- the same mission supports project-connected advanced-systems exposure without requiring permanent adoption;
- no known external dependency makes the complete project impossible to continue.

The project remains subject to evidence-based narrowing, reclassification, or termination. Final selection does not guarantee that every technical hypothesis will succeed.

## 5. Personal mission-validation result

The personal-fit requirement is passed.

The mission is motivating to Ali, and the investigation pattern is engaging rather than merely technically respectable. In particular, the project repeatedly asks questions that fit Ali's natural reasoning and learning style:

- How can a change propagate through a repository or dependency relationship?
- Which dependency relationships are direct, transitive, structural, or only apparent?
- Which evidence is trustworthy, incomplete, stale, unavailable, or conflicting?
- How deeply should a maintainer investigate this particular update?
- When is a broad investigation disproportionate to the likely risk?
- What does the simple baseline miss?
- Does structural, historical, learned, or AI-assisted context materially improve the decision?
- What should the maintainer do next, and why?

This mission preserves continuity across acquisition, software engineering, data work, evaluation, ML, security, operations, deployment, and advanced-systems experiments.

## 6. Primary user, problem, and decision

### 6.1 Primary user

A maintainer of a public Python open-source repository who receives an automated Dependabot dependency-update pull request.

### 6.2 Central problem

The maintainer must decide how to handle a dependency update using evidence distributed across the pull request, dependency declarations, repository code and configuration, upstream releases, package metadata, dependency relationships, CI runs, and prior repository history.

The evidence is often incomplete, inconsistent, stale, inaccessible, or non-project-specific. Existing automation can propose the update and expose signals, but the maintainer still has to determine the appropriate investigation depth and next action.

### 6.3 Supported decision

UpgradePilot supports one central question:

> **What should the maintainer do next with this dependency-update pull request?**

The bounded recommendation classes are:

1. **Merge after normal review** — available evidence does not identify a reason for additional investigation beyond the repository's normal process.
2. **Run targeted checks** — specific missing or risk-bearing evidence justifies a named test, environment check, compatibility check, or review step.
3. **Investigate or block** — observed evidence identifies a material compatibility, support, behavior, security, or reliability concern.
4. **Defer** — the update should not proceed now because of policy, timing, supersession, unresolved evidence, or disproportionate investigation cost.
5. **Abstain** — available evidence is too incomplete, inaccessible, or conflicting to support a defensible recommendation.

These actions are decision support, not automated repository mutation.

## 7. Mission

Build a production-oriented system that turns a real dependency-update pull request into a reproducible, provenance-backed, uncertainty-aware decision report, then rigorously determine whether repository context, structural relationships, learned methods, and grounded AI assistance improve the maintainer decision over a transparent deterministic baseline.

## 8. Central technical and product thesis

### 8.1 Primary thesis

> Combining repository-specific usage context, dependency-path evidence, upstream behavioral changes, and available CI history will produce more useful and better-calibrated dependency-update decisions than a transparent baseline using only version-change category, current CI conclusion, directness, and release-note keywords.

### 8.2 Supporting theses

The project will investigate whether:

- explicit evidence provenance and source-quality states reduce unsupported conclusions;
- abstention and proportional investigation depth are more useful than forcing a recommendation for every case;
- structural or graph representations capture dependency and propagation context missed by flat features;
- a learned ranking or recommendation method improves decision utility over deterministic rules;
- grounded LLM synthesis can improve evidence comprehension without increasing unsupported claims;
- bounded multi-agent investigation improves coverage or review quality over deterministic and single-agent workflows;
- asynchronous work, service boundaries, orchestration, and MLOps controls solve observed operational needs or remain unjustified complexity.

### 8.3 Thesis discipline

A technology label is not a thesis. A successful experiment requires:

1. an observed product or evaluation limitation;
2. a simpler baseline;
3. a bounded hypothesis;
4. a measurable success condition;
5. a rejection condition;
6. documented cost and new failure modes;
7. an adopt, retain-as-pilot, reject, or defer decision.

## 9. Outcome classification

Uncertain success is not a reason to remove ambition. Outcomes are classified so the project can pursue difficult goals without manufacturing positive results.

### 9.1 Core required outcome

UpgradePilot counts as a successful and useful flagship product only when all of the following exist:

- one public Python Dependabot PR can travel through the complete product flow;
- source inputs are acquired lawfully and preserved with version or time context;
- raw, normalized, accepted, rejected, missing, inaccessible, stale, and conflicting evidence states are explicit;
- the central evidence contracts and transformations are tested;
- a deterministic baseline produces one of the bounded recommendation or abstention states;
- every material factual statement in the report is traceable to preserved evidence;
- observed evidence is separated from inferred conclusions;
- missing or conflicting evidence can trigger uncertainty, degraded output, or abstention;
- runs, inputs, transformations, recommendations, and versions are persisted for comparison;
- representative results can be reproduced from a clean setup;
- unit, integration, and failure-path tests exist;
- CI verifies the supported core;
- secure configuration, untrusted-input handling, dependency risk, and claim boundaries are documented;
- a CLI and/or API exposes the user-visible flow;
- the deterministic baseline is evaluated on a staged corpus;
- the label and truth limitations are explicitly audited;
- Ali can explain, modify, test, query, and diagnose the central path;
- the portfolio accurately distinguishes implemented, measured, degraded, experimental, rejected, and future behavior.

The core does not require a successful learned model, permanent graph architecture, permanent LLM component, permanent agent system, microservices, a queue, Kubernetes, or multi-cloud operation.

### 9.2 Target outcome

The following are serious 90-day targets. They must receive planned investigation when prerequisites and core progress permit:

- construct a defensible adjudication and label process;
- train and evaluate at least one learned ranking or recommendation method;
- operate an advanced MLOps lifecycle around the real project model or, if the label audit rejects that model path, around a bounded reproducible model experiment with an explicit negative decision;
- compare flat features with dependency-path, structural, temporal, or graph-derived representations;
- evaluate grounded LLM evidence synthesis against a deterministic report;
- evaluate a bounded multi-agent investigation workflow against deterministic and single-agent baselines;
- implement a project-integrated distributed-queue pilot for a representative long-running or rate-limited job;
- compare one bounded service extraction with the modular-monolith baseline;
- deploy representative project behavior through Kubernetes;
- perform bounded multi-cloud portability or deployment exposure;
- provide A1 hands-on exposure for all six advanced-systems areas required by policy;
- complete at least two A2 project-integrated pilots, provisionally distributed queues and advanced MLOps.

A target experiment may end in adoption, retained pilot status, rejection, or a documented inability to evaluate. A rigorous negative result satisfies the experimental responsibility; it does not convert the target technology into a core success claim.

### 9.3 Stretch or evidence-dependent outcome

The following depend on evidence not guaranteed at selection time:

- a learned method that materially improves recommendation utility on held-out cases;
- well-calibrated recommendation confidence at useful coverage;
- graph or structural representations that outperform flat contextual features;
- an LLM synthesis component with lower review effort and no unacceptable increase in unsupported claims;
- a multi-agent workflow that measurably improves coverage, quality, or recovery enough to justify continued use;
- external maintainer validation of decision usefulness;
- an A3 adopted queue, service boundary, orchestration layer, MLOps responsibility, or AI component;
- a larger cross-repository corpus with trustworthy labels;
- temporal generalization to later dependency-update periods;
- support for additional Python package-management formats or update-bot variants;
- evidence strong enough to make claims beyond a bounded learning and portfolio environment.

Failure to achieve a stretch outcome does not weaken the core if the experiment and decision are rigorous.

## 10. Frozen 90-day product boundary

### 10.1 Included

- one primary user type: public Python open-source maintainer;
- one central workflow: review of an automated Dependabot dependency-update PR;
- one main input family: public repository, PR, package, release, dependency, and CI evidence associated with that update;
- one main output family: dependency-update decision reports;
- one primary implementation language: Python;
- one main persistence system;
- one application repository;
- one deployment model for the supported core;
- one central analytical question: whether contextual evidence improves the maintainer decision over a transparent baseline;
- one continuous product flow.

### 10.2 Initial ecosystem boundary

The first supported boundary is:

- GitHub-hosted public repositories;
- Dependabot pull requests;
- Python projects;
- PyPI package metadata and upstream public release evidence;
- public repository files and public CI metadata available through authorized interfaces.

Support for Poetry, uv, pip-tools, requirements files, or other Python declaration formats is admitted only as the initial corpus demonstrates need. Supporting every Python packaging format is not an initial requirement.

### 10.3 Explicitly outside the frozen core

- private repositories;
- private Dependabot alert details;
- automatic merging, commenting, approval, or repository mutation;
- universal language or package-manager support;
- arbitrary Git hosting providers;
- Renovate and other update bots;
- a generic vulnerability scanner;
- exploitability prediction;
- a general CI repair or failure-diagnosis platform;
- general code review;
- enterprise authentication or multi-tenancy;
- multiple databases;
- a vector database without measured need;
- autonomous external actions;
- a generalized agent platform;
- a generalized MLOps platform;
- high-availability or multi-region production operation;
- unsupported claims that an update is objectively safe.

## 11. Input family and feasibility realities

The product may use:

- dependency-update PR metadata, diff, base and head revisions, comments, and final disposition;
- repository dependency declarations, lockfiles, configuration, source files, tests, and workflow definitions;
- public package metadata;
- upstream release notes, changelogs, commits, advisories, and support-policy statements;
- direct and transitive dependency relationships that can be reproduced for the relevant snapshot;
- recent public CI run metadata, conclusions, jobs, steps, and logs where still available;
- prior public update PRs and repository history;
- user-supplied preserved evidence files when lawful and appropriately bounded.

The charter records these constraints as product requirements:

- historical CI logs may have expired;
- private repository-specific Dependabot alert details may be inaccessible;
- release notes and package metadata may be incomplete, inconsistent, delayed, or wrong;
- repository files may not reveal dynamic use, generated behavior, optional paths, or deployment-specific configuration;
- merged or closed PR status is supporting evidence, not authoritative ground truth;
- a large, trustworthy label set for the objectively correct maintainer action is not guaranteed;
- external maintainer review is desirable but cannot be mandatory for completion;
- sources can disappear, rate-limit, change schema, or conflict;
- missing, inaccessible, stale, or conflicting evidence must remain visible and may require abstention.

The product must not hide these limitations with synthetic certainty.

## 12. End-to-end flow

```text
public Dependabot PR
→ acquire source records
→ preserve raw evidence and source context
→ validate, classify, and normalize evidence
→ identify missing, inaccessible, stale, and conflicting evidence
→ construct repository and dependency context
→ run deterministic baseline
→ optionally run admitted contextual, structural, learned, or AI-assisted methods
→ compare evidence and method outputs
→ produce provenance-backed recommendation, targeted next checks, or abstention
→ persist run, versions, evidence state, decision, and evaluation result
→ compare repeated runs and changed evidence
```

Not every responsibility requires a separate service or module.

## 13. Main output contract

Each decision report must contain:

- repository and pull-request identity;
- dependency and old/new version identity;
- analysis time and input snapshot identifiers;
- recommended action or abstention;
- confidence or uncertainty representation appropriate to the method;
- observed evidence;
- inferred conclusions;
- missing, inaccessible, stale, and conflicting evidence;
- material risk or compatibility signals;
- suggested targeted checks, when justified;
- evidence provenance for every material factual claim;
- rules, model, prompt, and configuration versions used;
- known limitations and claim boundary;
- degraded-state indicator;
- reproducibility information.

The report must never imply that a recommendation guarantees compatibility, security, absence of regressions, or maintainer intent.

## 14. Transparent deterministic baseline

The first analytical baseline will use explicit, inspectable signals such as:

- version-change category;
- direct versus transitive dependency status when reproducible;
- current CI conclusion and evidence availability;
- release-note or changelog indicators for breaking changes, support changes, deprecations, security fixes, and behavioral changes;
- runtime, Python-version, platform, or toolchain support changes;
- repository declaration and lockfile context;
- basic repository-specific usage evidence;
- known missing or conflicting source states;
- explicit abstention rules.

The baseline must be measured before a learned, graph-heavy, LLM, or agentic method can be claimed as an improvement.

## 15. Evidence semantics: what evidence can and cannot prove

### 15.1 Pull-request metadata and diff

Can support:

- what change the PR declares;
- which repository revision and files were changed;
- which dependency versions appear in the change;
- what comments, checks, and disposition are publicly recorded.

Cannot prove:

- that the update is safe;
- that all relevant files or runtime paths were tested;
- why a maintainer merged or closed the PR unless explicitly stated;
- compatibility outside the observed repository snapshot and environments.

### 15.2 Dependency declarations and lockfiles

Can support:

- declared requirements and resolved versions for a reproducible snapshot;
- direct and some transitive relationships;
- configuration constraints recorded in the repository.

Cannot prove:

- actual runtime reachability;
- which optional dependency paths are exercised;
- deployment-specific resolution outside the captured environment;
- exploitability or behavioral compatibility.

### 15.3 Repository source, tests, and workflow files

Can support:

- observable static imports, references, configuration, tests, and workflow behavior;
- which explicit repository paths appear related to the dependency;
- which checks are configured.

Cannot prove:

- complete dynamic behavior;
- hidden downstream users;
- all generated, reflective, plugin-based, or environment-specific usage;
- that configured tests are sufficient or actually representative.

### 15.4 Package metadata

Can support:

- metadata published by the package index or maintainer;
- release identity, declared Python support, dependencies, and distribution artifacts at a point in time.

Cannot prove:

- metadata completeness or correctness;
- project-specific compatibility;
- absence of undocumented behavior changes.

### 15.5 Release notes, changelogs, commits, and upstream issues

Can support:

- what upstream maintainers publicly stated or changed;
- explicit breaking, support, deprecation, security, and behavioral claims;
- traceable upstream evidence.

Cannot prove:

- that every relevant change was documented;
- that the statements are complete or accurate;
- how the change affects the target repository without contextual analysis.

### 15.6 Dependency paths and graph structure

Can support:

- relationships represented by the captured dependency resolution;
- paths through which a changed package may relate to the project;
- structural features and candidate propagation routes.

Cannot prove:

- runtime execution;
- causal impact;
- exploitability;
- that graph complexity improves the user decision.

### 15.7 CI evidence

Can support:

- that identified jobs or workflows reached recorded conclusions for a particular commit, configuration, time, and environment;
- the content of available steps and logs;
- observed failures and successes within that scope.

Cannot prove:

- universal compatibility;
- absence of untested regressions;
- correctness in unavailable platforms or environments;
- root cause when logs are missing, expired, truncated, or ambiguous.

A passing CI result is evidence, not a safety certificate.

### 15.8 Historical PR outcome

Can support:

- the action maintainers took;
- recorded timing, comments, checks, supersession, grouping, or policy evidence;
- retrospective workflow patterns.

Cannot prove:

- the objectively correct action;
- that merge equals safe;
- that close equals unsafe;
- that the same action generalizes to another repository or time.

### 15.9 Adjudicated recommendation labels

Can support:

- a documented interpretation under a declared rubric;
- repeatable evaluation against that rubric;
- disagreement, uncertainty, and label-quality analysis.

Cannot prove:

- universal maintainer preference;
- objective safety;
- a unique correct action where reasonable experts may differ;
- validity beyond the adjudicated population and evidence boundary.

### 15.10 Model scores and metrics

Can support:

- comparative performance on a defined corpus, split, label process, and metric;
- error patterns, calibration behavior, and selective performance within that evaluation.

Cannot prove:

- production safety;
- generalization to unobserved ecosystems;
- causal correctness;
- superiority when the label process or split is weak.

### 15.11 LLM or multi-agent output

Can support:

- a candidate synthesis, classification, explanation, or investigation trace when grounded and evaluated;
- comparison of workflow quality, cost, latency, coverage, and failure behavior.

Cannot prove:

- factual correctness without source verification;
- that cited evidence entails the conclusion;
- reliability merely because several agents agree;
- autonomy safety outside the bounded tools and termination rules.

### 15.12 External maintainer review

Can support:

- perceived usefulness, clarity, relevance, and actionability for the reviewed cases;
- discovery of rubric or workflow defects.

Cannot prove:

- general correctness;
- representative market demand;
- universal maintainer agreement;
- completion of the project's core when reviewers are unavailable.

## 16. Staged evaluation corpus

The corpus exists to support honest evaluation, not to create a large dataset for appearance.

### 16.1 Corpus construction principles

- use lawful public cases;
- preserve the evidence snapshot and acquisition time;
- group or split by repository and dependency where needed to reduce leakage;
- prefer temporal separation when enough history exists;
- distinguish evidence-complete from evidence-degraded cases;
- record exclusion reasons;
- do not use final PR disposition as the sole label;
- do not tune against held-out cases;
- freeze the held-out set before final model or rule comparison;
- allow an explicit unadjudicable state.

### 16.2 Calibration cases

**Purpose:** develop and debug the evidence schema, adjudication rubric, deterministic baseline, error categories, and report contract.

**Planned size:** 20–30 cases across multiple public Python repositories and update types.

Calibration cases may be inspected repeatedly and used to revise rules, prompts, features, and labeling guidance. They are not used as the primary evidence for final recommendation-quality claims.

### 16.3 Held-out evaluation cases

**Purpose:** evaluate extraction, provenance, evidence handling, baseline behavior, contextual methods, learned methods, abstention, and recommendation quality after the relevant method is frozen.

**Acquisition target:** at least 50 cases, with a target of 75–100 when lawful acquisition and adjudication quality permit.

**Recommendation-quality target:** at least 30 defensibly adjudicable held-out cases. The preferred target is 50 or more.

Cases that cannot support a defensible recommendation label remain valuable for extraction, provenance, evidence-coverage, degraded-behavior, and abstention evaluation. They must not be assigned manufactured labels merely to reach a count.

If fewer than 30 held-out cases are defensibly adjudicable after the label audit:

- no strong learned-recommendation claim may be made;
- model work may continue as a bounded feasibility experiment;
- the project records the label limitation as a negative result;
- evaluation emphasis shifts to evidence quality, selective prediction, ranking of investigation need, or another formally approved measurable framing.

### 16.4 External-review subset

**Purpose:** obtain limited external feedback on usefulness, clarity, missing evidence, proportional investigation depth, and recommendation actionability.

**Target:** 5–15 cases reviewed by one or more maintainers or technically relevant external reviewers when access is available.

This subset is desirable but optional. Lack of external participation does not block project completion. Reviewer selection, conflicts, instructions, and disagreements must be recorded. External review supplements; it does not replace internal evidence and held-out evaluation.

### 16.5 Freeze and contamination control

Before final evaluation:

- corpus membership is versioned;
- calibration and held-out identifiers are recorded;
- repository and dependency overlap is analyzed;
- label rubric and adjudication version are frozen;
- baseline and candidate method versions are frozen;
- post-freeze changes require a new evaluation version;
- cases used for prompt, feature, or rule tuning cannot silently return to the held-out set.

## 17. Evaluation metrics

Metrics must be reported with corpus scope, denominators, uncertainty, exclusions, and known label limitations.

### 17.1 Extraction quality

Measure:

- field-level correctness for required fields;
- record-level complete extraction rate;
- schema-valid normalized-record rate;
- source-specific acquisition success rate;
- malformed or changed-input detection rate;
- false acceptance and silent-drop counts.

A field is not considered correct merely because it is non-empty.

### 17.2 Provenance quality

Measure:

- **material-claim provenance coverage:** material factual claims with resolvable source references divided by all material factual claims;
- source-reference resolvability at evaluation time;
- transformation-trace completeness from report claim to normalized record and preserved raw input;
- observed-versus-inferred classification accuracy;
- unsupported factual-claim rate.

The core target is complete traceability for material factual claims in supported reports. Any exceptions must be explicit degraded behavior.

### 17.3 Evidence coverage and quality-state handling

Measure:

- expected evidence-source coverage by case;
- available, missing, inaccessible, stale, conflicting, and invalid evidence rates;
- correctness of evidence-quality state assignment;
- proportion of reports that expose material evidence gaps;
- source failure recovery and partial-result behavior;
- coverage change across repeated runs.

High evidence coverage does not prove decision correctness. Low coverage must not be hidden.

### 17.4 Abstention and selective behavior

Measure:

- overall abstention rate;
- abstention rate by evidence-quality state;
- justified-abstention precision;
- missed-abstention or false-confidence rate;
- recommendation coverage versus error or cost;
- selective risk curves where probabilistic scores exist;
- high-confidence error count;
- unsupported definitive recommendation count.

Abstention is valuable when it prevents unsupported conclusions. Excessive abstention that avoids useful decisions is also a failure and must be measured.

### 17.5 Reproducibility

Measure:

- deterministic rerun equivalence from preserved inputs and frozen versions;
- clean-checkout setup and representative-flow success;
- environment, configuration, rule, prompt, feature, data, and model version trace completeness;
- repeated-run difference explanation;
- idempotent acquisition and persistence behavior;
- recovery after interrupted or partial execution.

Expected nondeterminism from external or generative systems must be isolated, versioned, and evaluated rather than described as deterministic.

### 17.6 Contextual improvement over the baseline

Compare the transparent baseline with admitted contextual methods on the same held-out cases.

Measure, as applicable:

- change in cost-weighted recommendation utility;
- change in high-cost false-safe recommendations;
- change in ranking quality for investigation priority or depth;
- change in coverage at a fixed error or risk level;
- change in calibration;
- change in abstention quality;
- change in evidence completeness or explanation usefulness;
- per-case wins, losses, and unchanged results;
- paired uncertainty estimates or bootstrap intervals when the corpus permits.

A contextual method is not better merely because it is more complex or produces longer reports.

### 17.7 Recommendation quality

Because the actions have asymmetric consequences, report more than raw accuracy.

Measure, as the adjudication supports:

- class-wise precision, recall, and F1;
- macro-F1;
- cost-weighted utility or loss;
- confusion matrix;
- high-cost false-safe rate;
- unnecessary-investigation rate;
- defer and abstain quality;
- ranking metrics when the output is investigation priority rather than a single class;
- calibration error, Brier score, or reliability plots for probabilistic outputs;
- performance by repository, dependency type, evidence quality, and update category;
- disagreement-aware results where labels are uncertain.

Final metrics apply only to the declared corpus and rubric. They do not establish objective update safety.

### 17.8 Grounded LLM synthesis

When admitted, measure:

- material claim citation coverage;
- citation correctness and entailment;
- unsupported-claim rate;
- contradiction with preserved evidence;
- omission of material risk or missing-evidence states;
- structured-output validity;
- abstention compliance;
- human review time or usefulness compared with the deterministic report;
- latency and cost.

### 17.9 Multi-agent workflow

When admitted, compare against deterministic and single-agent workflows using:

- task completion;
- evidence coverage;
- unsupported claims;
- recommendation quality;
- reproducibility;
- cost;
- latency;
- tool and authorization violations;
- termination failures;
- conflicting-output handling;
- recovery after one agent fails.

Agent count is not a quality metric.

## 18. Hard-gate record

| Hard gate | Result | Governing boundary |
|---|---|---|
| Credible real user and decision | Pass | Public Python maintainer deciding how to handle a Dependabot PR |
| Problem exists outside learning plan | Pass | Dependency-update review is an existing maintainer workflow |
| Lawful real input | Pass | Public repository, PR, package, release, dependency, and CI evidence |
| Early complete attempt | Pass | One PR can reach a weak evidence-backed deterministic report |
| Measurable outcome | Pass | Explicit extraction, provenance, evidence, abstention, reproducibility, contextual, and recommendation metrics |
| Non-generic thesis | Pass | Repository-contextual evidence is tested against a simpler baseline |
| Bounded ecosystem | Pass | GitHub, Dependabot, Python, and public package/release evidence |
| One user and workflow | Pass | One maintainer decision for one PR class |
| Feasible cost and access | Pass | Core uses public data and conventional local compute |
| Ownership feasibility | Pass with controls | Deterministic-first, bounded responsibilities, weekly Ali-owned central change |
| Repeated visible progress | Pass | Acquisition, evidence, baseline, report, evaluation, reliability, and method improvements |
| Safety, legal, and privacy | Pass | Read-only public inputs and no autonomous mutation |
| Honest ML/AI path | Pass | Labels, baseline, evaluation, abstention, and rejection gates are explicit |
| Novelty beyond complexity | Pass | Evidence reconciliation, context, proportional investigation, abstention, and evaluation |
| Technical reviewer clarity | Pass | One traceable input-to-decision product flow |

A future failure of a hard gate triggers immediate reframe or termination review. A high score cannot override it.

## 19. Production-oriented quality requirements

The supported core should eventually include, where justified:

- explicit Python package and application structure;
- typed or otherwise explicit central contracts;
- configuration boundaries;
- structured errors and logs;
- raw-input preservation;
- validation and quarantine or degraded-state behavior;
- one main persistence system and reproducible schema setup;
- idempotent or explicit replay behavior;
- CLI and/or API;
- unit, integration, failure, and recovery tests;
- secure secret and credential handling;
- untrusted repository-content handling;
- dependency and supply-chain risk controls for UpgradePilot itself;
- Docker or another justified reproducible runtime;
- CI;
- health or readiness behavior only when a runtime component needs it;
- operational and cleanup documentation;
- limitations and claim register;
- versioned evaluation evidence;
- AI-assistance disclosure.

The default claim is **production-oriented**. Production readiness, safety certification, or universal compatibility must not be claimed without evidence beyond this 90-day project.

## 20. Ownership model

For central responsibilities, Ali must increasingly perform the full ownership loop:

```text
understand the maintainer need
→ predict system behavior
→ make or challenge the design decision
→ implement or materially modify a bounded responsibility
→ test it
→ run it on real evidence
→ interpret the result or failure
→ explain its effect on the complete decision flow
```

Required ownership evidence includes:

- at least one substantial Ali-owned central change each week;
- ability to locate responsible code and data;
- ability to explain central schemas and queries;
- ability to add or repair tests;
- ability to diagnose changed acquisition, data, evaluation, runtime, and model failures;
- ability to reject an impressive but unjustified technology or model;
- progressively reduced prompting for representative core behavior;
- explicit distinction between AI-generated, AI-assisted, Ali-directed, Ali-verified, and Ali-owned work.

Repository size, service count, model complexity, cloud count, cluster size, agent count, or tool count do not establish ownership.

## 21. Advanced-systems exposure and adoption plan

Advanced systems use the working UpgradePilot mission and representative workload. They do not precede the first working core flow.

Approximately 20–30% of focused technical capacity should be reserved in the later master plan for these packages, with only one major exposure package normally active at a time.

| Area | Minimum required path | Planned target | Likely A3 posture |
|---|---|---|---|
| Kubernetes | A1 deployment of a representative project workload; inspect resources, rollout or failure, recovery, and cleanup | A1; A2 only if multiple runtime components or operational needs justify comparison with Compose | Unlikely without demonstrated ongoing deployment need |
| Microservices | A1 bounded service boundary using a real UpgradePilot responsibility and one failure path | A1; possible A2 comparison of one extracted acquisition or analysis responsibility against the modular monolith | Likely reject or retain only as pilot unless lifecycle or isolation value is measured |
| Distributed queues | A1 producer-consumer workflow with success, retry or failure, state inspection, and idempotency | **A2 target** for rate-limited acquisition, analysis, or report jobs when synchronous execution shows a real limitation | Possible only if asynchronous reliability and workload isolation outweigh operations |
| Multi-cloud | A1 executable comparison of the same bounded workload in two environments, subject to cost and credentials | A1; A2 only if portability, provider differences, or resilience become relevant | Permanent multi-cloud operation is unlikely |
| Autonomous multi-agent architectures | A1 bounded roles, tools, shared state, termination, traceability, and failure inspection on a real investigation case | A1; A2 only if it measurably improves over deterministic and single-agent workflows | Unlikely unless quality and safety gains are clear |
| Advanced MLOps | A1 reproducible model lifecycle with experiment tracking, artifact identity, evaluation, and controlled inference | **A2 target** around the real learned method, including data/model versions, evaluation gates, deployment packaging, monitoring or replacement decision | Possible if repeated model development and operation justify it |

The provisional A2 pilots are:

1. distributed queues;
2. advanced MLOps.

If trustworthy recommendation labels are insufficient for a defensible learned method, the MLOps work still performs a bounded real lifecycle experiment and records the negative adoption decision. The second A2 pilot may shift to the microservice or multi-agent comparison only through a formal planning decision. This fallback must not manufacture an MLOps success claim.

Every package must record:

- product context and representative workload;
- simpler baseline;
- target exposure level;
- scope and time ceiling;
- safety, cost, privacy, credential, and cleanup boundaries;
- implementation and observed behavior;
- failure path;
- comparison;
- operational and maintenance burden;
- Ali ownership evidence;
- adopt, retain-as-pilot, reject, or defer decision;
- exact claim permitted afterward.

## 22. Technology and scope admission rules

A new technology, source, model family, representation, service, or major module enters only when:

1. a user-visible or evaluation limitation has been observed;
2. current simpler behavior is inadequate;
3. the proposed addition has a measurable success and rejection condition;
4. the smallest viable experiment is defined;
5. maintenance and delayed work are recorded;
6. Ali can explain and modify the responsibility;
7. the core remains runnable;
8. permanent adoption follows comparison with the baseline.

### 22.1 Learned method admission

A learned method requires:

- a real decision or ranking target;
- a completed label audit;
- defensible training and evaluation cases;
- a measured deterministic baseline;
- leakage-aware split design;
- explicit utility and failure metrics;
- a rejection rule.

A weak model is not accepted merely because training completed.

### 22.2 Graph or structural representation admission

Graph or structural work requires:

- meaningful entities and relationships in the actual problem;
- a reproducible construction method;
- a flat or simpler structural baseline;
- a hypothesis about what information is otherwise lost;
- leakage and temporal-risk analysis;
- a measurable user-decision benefit.

Graph complexity is not novelty by itself.

### 22.3 LLM admission

Grounded LLM synthesis requires:

- a specific user task not adequately served by the deterministic report;
- source-constrained context;
- structured or bounded output;
- explicit abstention and review behavior;
- evaluation of citations, unsupported claims, omissions, cost, and latency;
- comparison with a non-LLM baseline.

### 22.4 Multi-agent admission

A bounded multi-agent investigation requires:

- genuinely separable roles or tool responsibilities;
- tool and authorization limits;
- shared-state rules;
- termination conditions;
- conflict handling;
- deterministic or single-agent comparison;
- safety and recovery tests.

### 22.5 Additional source admission

An additional source requires evidence that current coverage or decision quality is insufficient and that the source is lawful, technically accessible, maintainable, and measurable.

## 23. Reframe and termination conditions

A formal review must reframe, narrow, or terminate UpgradePilot when evidence shows any of the following:

- public evidence cannot support output more useful than a simple PR summary;
- repository-specific context cannot be acquired or interpreted within the frozen boundary;
- a defensible evaluation or adjudication process cannot be constructed;
- the recommendation depends mainly on undocumented maintainer intuition;
- the useful product requires private data, unavailable logs, or inaccessible infrastructure;
- the mission requires multi-language, multi-hosting, or multi-bot support before value appears;
- the project becomes a generic scanner, CI platform, agent platform, MLOps platform, or code-review system;
- missing evidence is hidden rather than represented;
- model, LLM, graph, or agent work proceeds without a measured baseline and rejection gate;
- advanced exposure prevents completion or ownership of the core;
- Ali cannot increasingly modify, test, query, and diagnose the central flow;
- external cost, credential, legal, privacy, or safety constraints become material;
- repeated evidence shows the mission no longer produces sustained product pursuit;
- the deterministic baseline already solves the decision sufficiently and additional methods add no measurable value.

The smallest necessary change must be preferred. A negative technical result does not by itself terminate the mission. It terminates or revises the failed hypothesis, component, representation, or adoption claim.

## 24. Required next planning artifacts

No implementation begins until these artifacts are produced, reviewed, reconciled, and activated in this order.

### 24.1 Capability and prerequisite specification

Defines:

- the capabilities UpgradePilot requires;
- Ali's current depth for each capability;
- minimum prerequisite depth before each milestone;
- what will be learned just in time;
- ownership and assessment gates;
- what is intentionally deferred.

This file must avoid implying mastery from topic exposure.

### 24.2 Learning and execution contract

Defines:

- session behavior;
- AI and Ali responsibilities;
- implementation ownership;
- teaching depth;
- prediction, execution, testing, diagnosis, and explanation loops;
- assistance disclosure;
- stop and escalation rules;
- evidence requirements.

It must inherit the governing Execution Contract rather than replace it.

### 24.3 Revised 90-day master roadmap

Replaces the AegisLab-specific master route and allocates:

- core product progression;
- evaluation and model work;
- advanced-systems exposure capacity;
- review points;
- fallback paths;
- explicit milestone gates;
- forbidden scope;
- Day 90 closure.

### 24.4 Staged milestone plan

Defines the product capabilities and evidence gates from the first weak flow through corpus evaluation, contextual methods, production-oriented operation, advanced pilots, and portfolio closure.

Milestones must describe user-visible capability, not technology-study topics.

### 24.5 First-session plan

Defines one exact first session with:

- current state;
- user-visible output;
- real input;
- files or repository state;
- concepts required;
- implementation boundary;
- tests and evidence;
- ownership check;
- exact completion demonstration;
- stop line.

### 24.6 Evidence and progress tracker

Tracks:

- current product behavior;
- milestone state;
- evidence links;
- evaluation versions and results;
- assistance and ownership depth;
- introduced versus practiced versus independently demonstrated capability;
- advanced exposure levels A0–A4;
- adopted, retained, rejected, and deferred decisions;
- blockers, limitations, and next action.

The tracker must never mark a broad subject complete when only a narrow introduction or guided use occurred.

## 25. AegisLab and Sentinel preservation

### 25.1 AegisLab

Preserve and selectively reuse:

- safety boundaries;
- assistance records;
- explicit learning-depth distinctions;
- structured errors and failure diagnosis;
- validation and quarantine concepts;
- reproducible evidence;
- bounded scenarios;
- operational cleanup;
- resistance to unsupported production claims.

Do not reuse automatically:

- the environment-first route;
- namespace, SSH, DFIR, or threat-hunting work as required UpgradePilot prerequisites;
- AegisLab-specific module structure;
- AegisLab-specific roadmap sequencing;
- any architecture merely because it already exists.

AegisLab remains deferred historical and technical evidence unless a later UpgradePilot plan explicitly imports a bounded artifact or lesson.

### 25.2 Sentinel

Preserve and selectively reuse:

- real external acquisition;
- raw and normalized data separation;
- provenance;
- source failure handling;
- visible end-to-end flow;
- evaluation discipline;
- representation experiments;
- graph-learning lessons;
- scope and ownership failure lessons.

Do not reuse automatically:

- Sentinel's mission;
- its repositories or ecosystems as dependencies;
- its architecture or module count;
- blockchain-specific scope;
- AI-generated complexity not independently owned.

Sentinel remains a research archive.

## 26. Claim standard

Permitted claims must match evidence:

- **selected primary project** — this charter;
- **implemented** — behavior exists and is verified;
- **evaluated** — method was measured on a declared corpus and metric;
- **production-oriented** — realistic engineering practices exist with explicit limitations;
- **hands-on exposure** — A1 evidence;
- **project-integrated pilot** — A2 comparison evidence;
- **adopted product responsibility** — A3 evidence;
- **independent capability** — repeated low-assistance design, operation, diagnosis, and modification evidence.

Do not claim:

- that UpgradePilot determines objective update safety;
- that a merged PR proves a correct recommendation;
- that a model is successful because it trained;
- that an LLM is grounded because it emitted citations;
- that several agents are reliable because they agree;
- that Kubernetes, multi-cloud, queues, microservices, or MLOps exposure establishes professional mastery;
- that the project is production-ready without evidence beyond the 90-day environment.

## 27. Selection closure

The primary-project selection decision is closed.

UpgradePilot is the single primary flagship mission. Future work must move from this charter into the required planning artifacts and then into controlled implementation. Broad candidate comparison, AegisLab continuation, and architecture-first redesign are not authorized next actions.

The next authorized artifact is:

> **UpgradePilot Learning and Execution Contract.**
