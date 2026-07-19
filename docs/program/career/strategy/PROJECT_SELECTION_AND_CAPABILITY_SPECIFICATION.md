# Project Selection and Capability Specification

**Owner:** Ali Rajabi  
**Recorded:** 2026-07-18  
**Status:** Active specification for project discovery and selection; no project selected  
**Scope:** Desired problem, mission, product, capability, skill, novelty, evaluation, ownership, and scope characteristics  
**Authority:** Required input for a formal primary-project decision. This file does not select a project or silently replace the Execution Contract, fixed career identity, current allocation, or active plan.

## 1. Purpose

This document defines what the desired 90-day project must be capable of providing before any particular project or architecture is selected.

It answers:

- What kind of real-world problem should the project address?
- What properties must the mission and product have?
- What learning and career capabilities should the project develop?
- What can those capabilities enable inside a real system?
- What constitutes meaningful novelty rather than a generic tutorial?
- Which technologies are required, preferred, conditional, or deferred?
- How should candidate projects be rejected, compared, tested, and selected?
- How will the project remain ambitious without repeating Sentinel's loss of scope and ownership?

This specification must be used **before** architecture design. It prevents the selection process from starting with a preferred technology such as RAG, graphs, Docker, an LLM, or a model family and then inventing a problem around it.

## 2. Correct decision order

The project-selection process must follow this order:

```text
real-world problem
        ↓
affected user or stakeholder
        ↓
valuable decision, action, or outcome
        ↓
current alternatives and their limitations
        ↓
technical or product thesis
        ↓
measurable success and acceptable outcome
        ↓
smallest credible end-to-end product boundary
        ↓
required skills, data, methods, and technologies
        ↓
implementation and learning plan
```

Do not reverse this order into:

```text
skills or technologies we want to use
        ↓
features that demonstrate them
        ↓
a project description created afterward
```

Career alignment is a selection criterion, but it is not permission to create an artificial problem merely to include résumé keywords.

## 3. Outcome doctrine

The project must not intentionally target an imperfect result.

The correct operating rule is:

> Define the real problem, desired user outcome, acceptable quality level, evaluation method, and safety boundaries. Pursue that outcome seriously. Treat actual success, partial success, failure, and unexpected behavior as evidence rather than predetermining which result must occur.

Therefore:

- success is not assumed;
- failure is not manufactured merely to create a lesson;
- weak quality is not accepted without diagnosis;
- early results are not called successful merely because a pipeline executed;
- the project may evolve when evidence reveals that the original approach, data, framing, or success criterion was incomplete;
- changes must preserve the mission or explicitly record why the mission itself needs revision.

A failed acquisition, weak baseline, unusable output, or rejected hypothesis can be valuable, but only when it is an honest result of pursuing a meaningful target.

## 4. Central project definition

The desired project should satisfy this working definition:

> **A major, mission-driven, production-oriented end-to-end product that addresses a specific real-world problem for a defined user, operates on real and imperfect inputs, pursues explicit quality and usefulness targets, and evolves through evidence from actual successes, failures, and limitations. It must contain a meaningful technical or product thesis rather than reproduce a generic tutorial category. Skills, tools, models, and infrastructure are introduced only when they help solve the active problem or test a justified hypothesis.**

The governing scope principle is:

```text
large enough mission to create gravity and sustained curiosity
+
narrow enough product boundary to remain understandable and ownable
+
deep enough technical runway to support meaningful investigation and improvement
```

## 5. Non-negotiable problem characteristics

A candidate must satisfy every requirement in this section before scoring.

### 5.1 A real problem exists outside the learning plan

The problem must affect a real user, operator, analyst, developer, organization, community, or decision process.

The only problem cannot be:

> Ali needs to learn Python, Docker, machine learning, or another technology.

Learning is a project benefit. It is not the product's reason to exist.

Required evidence may include:

- direct examples of the problem;
- public discussions, issue reports, workflows, datasets, or failures;
- limitations of current tools;
- repeated manual work;
- observable quality, reliability, trust, cost, or decision problems;
- a credible stakeholder explanation.

The selection process does not require proof of a commercial market, but it does require evidence that the problem is not invented solely for the project.

### 5.2 A specific primary user is identifiable

The project must identify one primary user type for the 90-day boundary.

Examples of a user type include:

- a security analyst;
- an open-source maintainer;
- a data engineer;
- a software developer;
- a model evaluator;
- an incident responder;
- a technical researcher;
- an operations engineer.

"Everyone," "companies," or "developers" is too broad without a narrower workflow.

### 5.3 A meaningful decision or action is supported

The output must help the user decide or do something.

Examples:

- prioritize investigation;
- identify a likely failure source;
- compare two alternatives;
- validate whether data is trustworthy;
- detect a meaningful change;
- select remediation work;
- explain why a result changed;
- reproduce an analysis;
- reject unsupported evidence;
- allocate attention.

A dashboard, report, prediction, score, or AI response is not valuable by itself. The specification must state what user action it supports.

### 5.4 Real and imperfect inputs are available

The project must interact with lawful, authorized, public, or user-supplied inputs that contain authentic uncertainty.

Possible input forms include:

- public APIs;
- repositories;
- package metadata;
- advisories;
- logs;
- telemetry;
- documents;
- code;
- public datasets;
- time-series records;
- graphs or networks;
- user-provided files.

Synthetic fixtures remain required for tests, but they cannot be the only source of product behavior.

Before selection, confirm that at least one real input source can legally and technically be accessed.

### 5.5 An end-to-end attempt is feasible early

Before committing the full 90 days, the candidate must support one credible attempt through the central flow:

```text
real input
→ acquisition
→ processing
→ analysis or decision logic
→ user-visible output
```

The attempt does not need to meet the final quality target. It must reveal whether the mission, input, and output are real and whether the central loop is technically reachable.

The project must not require several weeks of infrastructure, data labeling, or architecture work before the first complete attempt can be made.

### 5.6 A measurable acceptable outcome can be defined

The project must define what "better" or "useful enough" means.

Depending on the problem, this may include:

- correctness;
- coverage;
- precision and recall;
- calibration;
- latency;
- reproducibility;
- data-quality rates;
- reduced manual effort;
- ranking quality;
- failure recovery;
- explanation faithfulness;
- source traceability;
- consistency across repeated runs;
- user task completion.

The metric may evolve, but the project cannot rely only on "the demo looks impressive."

### 5.7 The mission contains a technical or product thesis

The project must test or embody a nontrivial position about how the problem should be solved.

The thesis may concern:

- representation;
- problem framing;
- evidence quality;
- uncertainty;
- temporal or structural relationships;
- workflow;
- evaluation;
- human review;
- model selection;
- data integration;
- system reliability;
- explainability;
- provenance.

A technology label is not a thesis.

Weak:

> Build a RAG system.

Stronger:

> Determine whether provenance-constrained retrieval and explicit abstention reduce unsupported answers when source records conflict or become stale.

Weak:

> Build an ML price predictor.

Stronger:

> Test whether event and structural context improve decisions over a transparent temporal baseline under realistic data availability constraints.

### 5.8 The project has curiosity runway

The problem should naturally support increasingly difficult questions after the first baseline works.

A good candidate allows a progression such as:

```text
Can the input be acquired reliably?
→ Can it be normalized and trusted?
→ Can a transparent baseline support the user decision?
→ Where does the baseline fail?
→ What information, structure, history, or context is missing?
→ Does a more advanced method produce measurable value?
→ Can the result be explained, reproduced, and operated reliably?
```

The project should not become conceptually complete after connecting one API to one model.

### 5.9 The core can remain within one bounded product

For the 90-day boundary, the project should normally have:

- one primary user type;
- one central problem;
- one main input family;
- one main output family;
- one application repository;
- one primary implementation language;
- one main persistence system;
- one deployment model;
- one central analytical question;
- one continuous product flow.

A candidate that requires several unfamiliar ecosystems before producing value should be rejected or narrowed.

### 5.10 The work is safe, lawful, and ethically supportable

The project must have clear authorization, data-use, privacy, and safety boundaries.

Reject candidates that depend on:

- unauthorized access;
- unsafe malware execution without an approved maturity gate;
- private data without permission;
- evasion, abuse, or harmful automation;
- deceptive collection;
- unsupported high-stakes claims;
- regulated activities beyond available expertise and controls.

## 6. Meaningful novelty and innovation

The project must avoid novelty theatre and generic tutorial replication.

Novelty does not require inventing a new scientific field or publishing an original algorithm. It requires a defensible contribution in at least one axis.

### 6.1 Problem-framing novelty

The project addresses a sharper, under-served, or poorly measured version of a broader problem.

Example pattern:

```text
generic problem
→ identify a specific user, context, constraint, or failure class
→ define a more useful decision problem
```

### 6.2 Representation novelty

The project tests whether a richer representation captures information ignored by a flat baseline.

Possible forms:

- graphs;
- temporal sequences;
- dependency paths;
- code structure;
- hierarchical records;
- provenance networks;
- multimodal evidence;
- relational or event-centered models.

Graphs are not mandatory. They are valuable only when the real problem contains meaningful relationships and when a simpler baseline can demonstrate what the graph adds.

### 6.3 Evidence and trust novelty

The project improves how evidence is preserved, reconciled, qualified, or traced.

Possible contributions:

- provenance-backed outputs;
- conflict detection;
- uncertainty or abstention;
- source-quality modeling;
- reproducible decision histories;
- separation of observed evidence from inferred conclusions;
- data-quality-aware analysis.

### 6.4 Workflow novelty

The project helps a real user perform an important task more effectively.

Possible contributions:

- better prioritization;
- reduced investigation effort;
- clearer explanations;
- changed-result tracing;
- faster reproduction;
- more useful error handling;
- human review at the right decision point.

### 6.5 Evaluation novelty

The project uses a more honest or decision-relevant evaluation design.

Possible contributions:

- temporal evaluation;
- leakage-safe grouping;
- independently maintained truth;
- missing-data robustness;
- calibration;
- abstention evaluation;
- scenario-based error analysis;
- comparison with realistic operational baselines.

### 6.6 Integration novelty

The value may come from combining existing methods into a coherent, evidence-backed workflow that typical tutorials do not provide.

Integration counts only when the combined system solves the user problem more effectively and the contribution can be explained and evaluated.

### 6.7 Novelty rejection rule

Reject a candidate when its project statement is primarily one of these:

- build a RAG chatbot;
- build a recommendation system;
- build a generic anomaly detector;
- build a price-prediction model;
- build a dashboard;
- build an AI agent;
- build a vulnerability scanner;
- build an MLOps platform.

Such categories may appear inside a selected project, but they are not sufficient missions. The candidate must state the real problem, user, thesis, baseline, and measurable contribution.

## 7. Required product characteristics

The selected project should eventually demonstrate the following product qualities when the problem justifies them.

### 7.1 Continuous end-to-end flow

A user should be able to trace:

```text
input
→ acquisition
→ preservation
→ validation
→ transformation
→ analysis
→ output
→ user decision or action
```

Not every stage requires a separate service or module.

### 7.2 Raw-input preservation and provenance

When practical, preserve enough source context to answer:

- Where did this result come from?
- What version or time was used?
- What transformations occurred?
- Can the result be reproduced?
- Which claims are directly observed versus inferred?

### 7.3 Explicit data quality

The product should distinguish:

- accepted records;
- rejected records;
- incomplete records;
- unknown formats;
- conflicting evidence;
- unavailable sources;
- degraded results.

Invalid data must not silently become trusted output.

### 7.4 Transparent baseline before advanced methods

The project should establish a simple, defensible baseline before adopting a complex method.

Examples:

- rules before ML;
- lexical or metadata retrieval before embedding-heavy retrieval;
- tabular features before graph models;
- heuristic ranking before learned ranking;
- deterministic reconciliation before AI synthesis.

A complex method should answer an observed limitation, not replace the need to understand the problem.

### 7.5 Measurable evolution

Major changes should produce comparable evidence:

```text
baseline
→ hypothesis
→ implementation or experiment
→ evaluation
→ error analysis
→ adopt, revise, or reject
```

### 7.6 Failure-aware behavior

The product should make important failure states visible and actionable.

Expected behavior may include:

- timeouts;
- retries;
- partial results;
- explicit degraded status;
- quarantine;
- safe aborts;
- recovery instructions;
- idempotent reruns;
- structured errors.

### 7.7 Reproducible operation

A technical reviewer should be able to understand how to:

- configure the project safely;
- run the main flow;
- test it;
- reproduce a representative result;
- inspect logs and state;
- clean up;
- identify limitations.

### 7.8 Honest production orientation

The project should use realistic engineering practices without unsupported readiness claims.

Possible practices include:

- typed contracts;
- package structure;
- migrations;
- structured logging;
- secure configuration;
- Docker Compose;
- CI;
- tests;
- health or readiness checks when actually needed;
- operational documentation;
- failure and recovery tests;
- versioned evidence.

"Production-oriented" is the default description. "Production-ready" requires evidence beyond repository sophistication.

## 8. Capability and skill map

This section defines which capabilities the project should develop and what those capabilities enable. It does not require every technology to appear from the first day.

### 8.1 Problem discovery and product reasoning — required

**Skills and knowledge**

- problem decomposition;
- user and workflow analysis;
- requirement definition;
- baseline and alternative analysis;
- acceptance criteria;
- trade-off reasoning;
- scope control;
- evidence-based prioritization.

**What these enable**

- selecting a problem worth solving;
- translating a broad mission into an ownable product;
- deciding which failure matters next;
- rejecting unnecessary features;
- connecting technical work to user value;
- explaining why a design exists.

**Required evidence**

- clear problem statement;
- primary user and decision;
- documented constraints;
- explicit success criteria;
- reasoned adoption and rejection decisions.

### 8.2 Python software engineering — required core

**Skills and knowledge**

- application and package structure;
- functions, classes, modules, and interfaces;
- typing;
- configuration;
- error handling;
- CLI and/or API design;
- dependency management;
- maintainable code organization;
- refactoring.

**What these enable**

- implementing the central product flow;
- isolating responsibilities;
- changing behavior safely;
- integrating external data and analytical methods;
- exposing the product to a user;
- creating a portfolio artifact that can be reviewed and extended.

**Required evidence**

- runnable application;
- important behavior Ali can explain and modify;
- clear module responsibilities;
- code review and refactoring history;
- typed or otherwise explicit central contracts.

### 8.3 Data acquisition and integration — required

**Skills and knowledge**

- HTTP and API use;
- files and serialization;
- authentication and rate limits when applicable;
- retries and timeouts;
- pagination;
- schema inspection;
- source versioning;
- ethical and legal data access;
- caching and idempotency when justified.

**What these enable**

- working with real external inputs;
- handling missing or unstable sources;
- preserving raw evidence;
- comparing sources;
- explaining acquisition failures;
- building a repeatable input path.

**Required evidence**

- at least one real source;
- preserved source context;
- explicit failure handling;
- reproducible representative acquisition;
- no hidden dependence on manually prepared perfect data.

### 8.4 Data engineering and modeling — required core

**Skills and knowledge**

- raw versus normalized data;
- schema design;
- validation;
- transformation;
- identifiers;
- deduplication;
- provenance;
- data-quality checks;
- version and time semantics;
- batch or incremental processing as required.

**What these enable**

- turning imperfect input into trustworthy records;
- preventing invalid data from contaminating results;
- supporting reproducible analysis;
- connecting multiple stages of the product;
- creating reliable datasets for rules or ML.

**Required evidence**

- explicit data contracts;
- accepted/rejected behavior;
- data-quality reporting;
- traceability from output to source;
- tests for malformed and changed inputs.

### 8.5 SQL and persistence — strongly required unless the problem genuinely does not need history

**Skills and knowledge**

- relational modeling;
- SQLite or another justified database;
- migrations or initialization;
- inserts and updates;
- constraints;
- indexes when measured;
- joins;
- grouping and aggregation;
- transactions;
- duplicate and replay behavior.

**What these enable**

- preserving runs and results;
- comparing changes over time;
- answering real user questions;
- auditing decisions;
- creating training or evaluation datasets;
- recovering from repeated execution.

**Required evidence**

- queries tied to user decisions;
- explicit duplicate behavior;
- reproducible schema setup;
- persistence tests;
- Ali can write and explain central queries.

### 8.6 Testing, debugging, and observability — required core

**Skills and knowledge**

- unit and integration tests;
- test fixtures;
- failure reproduction;
- logs;
- debugging;
- assertions and invariants;
- deterministic behavior;
- monitoring concepts;
- performance measurement when relevant.

**What these enable**

- changing the system without silent regression;
- distinguishing product failure from environment failure;
- diagnosing real external-input problems;
- evaluating whether a new method improved the system;
- making credible engineering claims.

**Required evidence**

- meaningful tests, not only happy-path coverage;
- at least one diagnosed and repaired changed failure;
- logs that answer operational questions;
- repeatable commands;
- explicit known failures and limitations.

### 8.7 Linux, command line, and operating-system reasoning — required as used

**Skills and knowledge**

- files and permissions;
- processes;
- environment variables;
- networking basics;
- shell use;
- resource and lifecycle inspection;
- safe cleanup;
- service behavior.

**What these enable**

- operating the actual development and runtime environment;
- understanding failures below application code;
- using tools for real project needs;
- running and inspecting local services;
- managing data and artifacts safely.

**Required evidence**

- commands used for active product questions;
- explanation of important effects and risks;
- reduced reliance on copied command sequences;
- safe environment recovery.

### 8.8 Docker and reproducible runtime engineering — strongly desired and likely required

**Skills and knowledge**

- images, containers, and processes;
- Dockerfiles;
- build context;
- networks;
- mounts and volumes;
- Compose;
- logs and lifecycle;
- secrets and configuration boundaries;
- clean recreation.

**What these enable**

- reproducible local execution;
- isolated dependencies;
- realistic service integration;
- clean demos and testing;
- controlled failure and recovery;
- portable reviewer experience.

**Admission rule**

Docker should solve an actual runtime, dependency, reproducibility, or deployment need. It should not become an isolated curriculum detached from the product.

**Required evidence when used**

- fresh build/run path;
- no unnecessary exposure;
- safe secret handling;
- clear state persistence;
- clean shutdown and cleanup;
- Ali can explain the main runtime boundaries.

### 8.9 Security and privacy engineering — required quality layer

**Skills and knowledge**

- threat and trust boundaries;
- secrets;
- input validation;
- least privilege;
- authorization;
- safe defaults;
- dependency risk;
- privacy;
- evidence and claim limits;
- secure failure behavior.

**What these enable**

- preventing the learning product from creating avoidable risk;
- handling untrusted input;
- distinguishing evidence from inference;
- making defensible security claims;
- documenting what the product does not guarantee.

**Required evidence**

- explicit trust boundaries;
- safe input and credential handling;
- limitations register;
- at least one security-oriented design or failure test;
- no secret or private-data leakage.

### 8.10 Machine learning and statistical reasoning — desired, conditional on a real question

**Skills and knowledge**

- problem formulation;
- labels and truth;
- feature or representation design;
- baselines;
- train/evaluation separation;
- leakage;
- metrics;
- calibration;
- error analysis;
- model comparison;
- reproducibility.

**What these enable**

- testing whether learned patterns add value beyond explicit rules;
- prioritizing or classifying difficult cases;
- understanding model failure;
- comparing representations;
- making an honest adopt-or-reject decision.

**Admission rule**

ML enters only after:

- a real analytical question exists;
- data or controlled experimental runs exist;
- truth or labels can be defended;
- a transparent baseline is measured;
- success and rejection criteria are explicit.

**Required evidence when used**

- leakage-aware evaluation;
- baseline comparison;
- error analysis;
- reproducible training and inference;
- Ali can explain what the model uses and where it fails.

### 8.11 Graph, temporal, or structured representations — high-value opportunity, not mandatory

**Skills and knowledge**

- entities and relationships;
- graph construction;
- structural features;
- traversal or message passing;
- temporal ordering;
- comparison with flat representations;
- graph-specific leakage and evaluation risks.

**What these enable**

- capturing dependencies, paths, interactions, or context that flat records may lose;
- asking structural questions;
- explaining relational effects;
- testing a technically interesting representation thesis.

**Admission rule**

Use only when the problem contains meaningful structure and when an explicit baseline can test whether the representation improves the user outcome.

### 8.12 AI and LLM integration — desired only when grounded and useful

**Skills and knowledge**

- prompt and output contracts;
- retrieval and context selection;
- grounding;
- structured outputs;
- tool use;
- evaluation;
- hallucination and uncertainty;
- cost and latency;
- privacy and security;
- human review.

**What these enable**

- explaining complex evidence;
- assisting a user workflow;
- summarizing or transforming validated information;
- operating tools under explicit boundaries;
- comparing deterministic and generative approaches.

**Admission rule**

An LLM, RAG component, or agent enters only when it improves a specific user task over a simpler approach and can be evaluated against source evidence.

**Required evidence when used**

- grounded source traceability;
- failure and unsupported-answer tests;
- structured or bounded output where appropriate;
- explicit abstention or review behavior;
- comparison with a non-LLM baseline.

### 8.13 Git, CI, and collaborative engineering — required

**Skills and knowledge**

- meaningful commits;
- branches and pull-request habits where appropriate;
- code review;
- CI;
- reproducible checks;
- versioned decisions;
- issue-driven work.

**What these enable**

- preserving engineering history;
- demonstrating reviewable progress;
- preventing regressions;
- supporting collaboration;
- creating credible portfolio evidence.

**Required evidence**

- coherent commit history;
- automated checks;
- issues or work packages tied to product behavior;
- review and correction evidence;
- no large unexplained AI-generated drops.

### 8.14 Technical communication and portfolio explanation — required

**Skills and knowledge**

- problem statements;
- architecture explanation;
- evidence-backed claims;
- limitations;
- runbooks;
- decision records;
- concise reporting;
- demonstration.

**What these enable**

- showing employers what was solved and why;
- defending technical choices;
- helping another person run the system;
- separating implemented, verified, degraded, and future behavior;
- explaining Ali's actual ownership.

**Required evidence**

- honest README;
- system flow;
- setup and operation instructions;
- limitations;
- AI-assistance disclosure;
- Ali can present and modify the central path.

## 9. Capability priority classes

### 9.1 Required in the selected project

- real problem and product reasoning;
- Python software engineering;
- real-input acquisition;
- data modeling and validation;
- testing and debugging;
- security and privacy reasoning;
- Git and CI;
- technical explanation;
- reproducible end-to-end operation.

### 9.2 Strongly desired unless the problem gives a reason to exclude them

- SQL and persistence;
- Docker and runtime reproducibility;
- historical or repeated-run comparison;
- explicit evaluation and error analysis.

### 9.3 Desired conditional depth

- machine learning;
- graph or temporal representations;
- AI or LLM integration;
- API and user interface;
- advanced observability;
- additional data sources.

These enter when they solve a demonstrated problem or test a justified thesis.

### 9.4 Deferred by default

- Kubernetes;
- microservices;
- distributed queues;
- service mesh;
- multi-cloud deployment;
- multiple databases;
- enterprise authentication;
- autonomous multi-agent systems;
- advanced MLOps platforms;
- deep-learning scale without data and evaluation support;
- blockchain or proof systems unless central to the selected problem;
- broad multi-language or multi-domain support.

## 10. Mission and motivation fit

Technical value alone is insufficient. The selected project must have enough mission gravity to sustain Ali's effort.

### 10.1 Required attraction characteristics

The project should create genuine questions such as:

- Why did the real input fail?
- Why is the result worse than expected?
- What information does the baseline miss?
- Does structure or history matter?
- Can another source improve evidence?
- How does one change affect the complete flow?
- Can the result be trusted and reproduced?
- What should the user do next?

### 10.2 Attraction is evidence, not architecture authority

A compelling technology or idea earns a bounded hypothesis test. It does not automatically become part of the product.

For every significant addition, define:

- observed limitation;
- hypothesis;
- simplest baseline;
- experiment boundary;
- success criterion;
- rejection criterion;
- implementation and maintenance cost;
- ownership requirement.

### 10.3 Mission-continuity test

A candidate is a better fit when the same mission remains visible while the work moves through acquisition, software, data, operations, analysis, evaluation, and deployment.

A candidate is weaker when each skill appears as a separate course or laboratory disconnected from the user outcome.

## 11. Ownership constraints

The selected project must be ambitious enough to motivate without permitting AI-assisted complexity to hide weak personal ownership.

### 11.1 Required ownership progression

Ali should progressively be able to:

- explain the problem and central flow;
- locate responsible code;
- predict effects before changes;
- make bounded design decisions;
- implement or materially modify central behavior;
- add and repair tests;
- diagnose failures;
- interpret data and model results;
- reject unsupported AI suggestions;
- reproduce core behavior with reduced prompting.

### 11.2 Weekly ownership evidence

Every week should contain at least one central change involving substantial Ali-owned reasoning or implementation.

Examples:

- designing and implementing a parser rule;
- diagnosing a real acquisition failure;
- writing a database query that answers a user question;
- defining and evaluating a baseline;
- changing a representation and interpreting the effect;
- repairing a runtime failure;
- rejecting an advanced method after evidence shows no value.

### 11.3 AI contribution limits

AI may accelerate scaffolding, explanation, review, and debugging. It must not:

- silently produce the entire architecture;
- add permanent modules because they are impressive;
- hide uncertainty behind confident prose;
- replace Ali's decision and interpretation work;
- make repository size look like learning progress;
- generate large unreviewed implementations that Ali cannot trace.

## 12. Hard rejection gates

Reject or materially narrow a candidate when any of these is true:

1. No credible real user or decision exists.
2. The problem is created mainly to demonstrate a technology.
3. Real lawful input is unavailable.
4. The first complete attempt requires weeks of prerequisites.
5. Success cannot be evaluated beyond subjective appearance.
6. The project statement is a generic category without a thesis.
7. Several unfamiliar ecosystems are mandatory before value appears.
8. The 90-day boundary requires multiple primary users or unrelated workflows.
9. The project depends on unavailable private data, expensive infrastructure, or inaccessible compute.
10. The main technical work would be performed by AI while Ali only operates the result.
11. The candidate cannot produce repeated visible product progress.
12. The project creates legal, ethical, safety, or privacy risk that cannot be bounded.
13. ML or AI is mandatory without data, truth, a baseline, or an evaluation path.
14. The candidate has novelty only through added complexity.
15. The project cannot be explained credibly to a technical reviewer.

A high score cannot override a hard rejection gate.

## 13. Candidate scoring model

After passing all hard gates, score each candidate from 0 to 5 for every criterion and multiply by the weight.

Scoring meaning:

- `0` — absent or contradicted;
- `1` — very weak;
- `2` — weak or highly uncertain;
- `3` — credible;
- `4` — strong;
- `5` — exceptional and evidence-backed.

| Criterion | Weight | What is being judged |
|---|---:|---|
| Real problem and user value | 20 | Problem evidence, user specificity, and meaningful supported action |
| Mission gravity and personal fit | 15 | Likelihood of sustained pursuit, curiosity, and daily mission continuity |
| Technical/product thesis and novelty | 15 | Non-generic contribution, hypothesis, and defensible reason to exist |
| Career capability compounding | 15 | Depth across Python, data, testing, SQL, operations, security, ML/AI when justified |
| Real-input and end-to-end feasibility | 10 | Accessible real data and an early complete product attempt |
| Curiosity and research runway | 10 | Ability to generate deeper evidence-based questions for 90 days |
| Ownership and scope feasibility | 10 | Ability to remain narrow enough for Ali to explain, modify, test, and diagnose |
| Production-oriented portfolio value | 5 | Reproducibility, engineering quality, and reviewer clarity |

Calculate:

```text
criterion score / 5 × weight
```

Maximum total: `100`.

Interpretation:

- below `65`: reject;
- `65–74`: promising but requires material reframing;
- `75–84`: strong candidate;
- `85–100`: exceptional candidate, still subject to feasibility testing.

A candidate should normally score at least:

- `4/5` for real problem and user value;
- `4/5` for mission gravity and personal fit;
- `3/5` for thesis and novelty;
- `3/5` for ownership and scope feasibility.

These minimums prevent a technically convenient but psychologically weak project from winning by total score.

## 14. Project-selection process

### Stage 1 — Identify problem territories

Generate problem territories, not technology projects.

Examples of territory categories:

- software supply-chain decisions;
- evidence quality and provenance;
- security telemetry and investigation;
- AI-system evaluation and trust;
- open-source maintenance intelligence;
- reliability and failure diagnosis;
- data-quality decision support;
- code or dependency structure;
- technical knowledge change and staleness.

Do not select a project during this stage.

### Stage 2 — Investigate problem reality

For each territory:

- identify users;
- inspect real workflows and failures;
- review existing tools and their limitations;
- locate accessible real inputs;
- record legal and operational constraints;
- identify plausible decisions the product could support.

### Stage 3 — Form candidate missions

Each candidate mission must state:

```text
For [primary user],
who needs to [decision or action],
this project will [valuable outcome]
using [real input family],
because current approaches fail or underperform when [specific limitation].
The central thesis is [nontrivial hypothesis or contribution].
```

### Stage 4 — Define the acceptable outcome

For each candidate, define:

- minimum useful outcome;
- desired 90-day outcome;
- quality or performance criteria;
- evidence and evaluation strategy;
- honest failure outcome;
- conditions that would invalidate the project thesis.

### Stage 5 — Run bounded feasibility investigations

Before final selection, verify:

- one real input can be acquired;
- one complete flow can be attempted;
- the user-visible output can be represented;
- the central technical unknown is real;
- the project does not require hidden infrastructure or unavailable data;
- the problem remains interesting after contact with its actual data and constraints.

These are feasibility investigations, not miniature full projects.

### Stage 6 — Apply hard gates and score candidates

Use Sections 12 and 13.

Record evidence for each score. Do not score from enthusiasm alone.

### Stage 7 — Select and freeze the core boundary

The final decision must define:

- mission;
- primary user;
- problem;
- supported decision;
- input and output families;
- technical thesis;
- minimum and desired outcomes;
- evaluation strategy;
- first end-to-end attempt;
- 90-day scope;
- forbidden scope;
- admission rules for graphs, ML, AI, extra sources, and infrastructure;
- ownership plan;
- preservation or reuse of AegisLab and Sentinel work;
- evidence that would justify changing or terminating the project.

## 15. Candidate specification worksheet

Use this template for every serious candidate.

```markdown
# Candidate: <working name>

## Problem
- Real-world problem:
- Evidence the problem exists:
- Primary user:
- Decision or action supported:
- Current alternatives:
- Specific limitation or gap:

## Mission
- Mission statement:
- Why this matters:
- Why Ali is likely to pursue it for 90 days:

## Inputs and outputs
- Real input family:
- Access and legal status:
- Expected data imperfections:
- Main output:
- User-visible action or decision:

## Technical/product thesis
- Thesis:
- Transparent baseline:
- Proposed novelty axis:
- What result would support the thesis:
- What result would reject or weaken it:

## End-to-end flow
- Acquisition:
- Preservation:
- Validation/transformation:
- Analysis:
- Output:
- Feedback or repeated-run loop:

## Outcome definition
- Minimum useful outcome:
- Desired 90-day outcome:
- Quality and usefulness criteria:
- Failure and degradation behavior:

## Capability value
- Python/software engineering:
- Data engineering:
- SQL/persistence:
- Testing/debugging:
- Linux/Docker/operations:
- Security/privacy:
- ML/statistics opportunity:
- Graph/structured representation opportunity:
- AI/LLM opportunity:
- Communication/portfolio value:

## Scope and ownership
- Fixed 90-day boundary:
- Explicit exclusions:
- Major unknowns:
- Required external dependencies:
- Ali-owned central responsibilities:
- Main risk of Sentinel-style expansion:
- Expansion controls:

## Feasibility evidence
- Real input acquired:
- Complete flow attempted:
- Major blocker:
- Estimated complexity:
- Compute/cost constraints:

## Hard-gate result
- Pass/fail by gate:

## Weighted score
- Real problem and user value:
- Mission gravity and personal fit:
- Thesis and novelty:
- Career capability compounding:
- Real-input and end-to-end feasibility:
- Curiosity runway:
- Ownership and scope feasibility:
- Production-oriented portfolio value:
- Total:

## Decision
- Reject / reframe / shortlist:
- Reason:
```

## 16. Project features versus implementation choices

Keep these distinctions explicit.

### Feature or product responsibility

Describes what the system must do for the user.

Examples:

- preserve source evidence;
- compare two runs;
- prioritize findings;
- expose uncertainty;
- explain changed results;
- recover from source failure.

### Capability

Describes what Ali and the system must be able to perform.

Examples:

- normalize inconsistent records;
- query historical state;
- evaluate a ranking baseline;
- reproduce a run;
- diagnose a container failure.

### Implementation choice

Describes one possible technology or architecture.

Examples:

- PostgreSQL;
- SQLite;
- NetworkX;
- PyTorch Geometric;
- FastAPI;
- Docker Compose;
- an LLM;
- a vector database.

Never present an implementation choice as though it were the user requirement.

Use:

```text
user problem
→ product responsibility
→ required capability
→ simplest suitable implementation
```

## 17. Change and evolution rules after selection

The project may evolve when real evidence reveals new constraints or opportunities.

Evolution is allowed when:

- the core mission remains stable;
- a real limitation has been observed;
- the change improves the supported user decision;
- the success criterion is explicit;
- the smallest sufficient change is chosen;
- delayed work and maintenance cost are recorded;
- Ali can understand and own the added responsibility.

A change requires formal scope review when it adds:

- a new primary user;
- a new unrelated workflow;
- a new ecosystem;
- a new deployment model;
- a second database;
- a second major input family;
- a major model family;
- a separate service boundary;
- a new project thesis.

The project must not become large through a sequence of individually attractive additions that were never evaluated together.

## 18. Relationship to current Career identity

The fixed identity remains:

> **AI-augmented Python/data/ML engineer developing secure engineering capability.**

The selected project should compound this identity through real product work.

The identity does not require artificial inclusion of every technology. It requires that the chosen problem provides substantial opportunity to demonstrate:

- reliable Python systems;
- real data acquisition and transformation;
- testing and evidence-based debugging;
- persistence and queryable state;
- production-oriented operation;
- secure engineering;
- analytical reasoning;
- machine learning or AI only where measurable value can be tested.

## 19. Decision standard

The final project should not be selected because it is:

- fashionable;
- technically impressive;
- easy to describe;
- likely to produce a polished demo;
- convenient for a predefined curriculum;
- similar to a popular tutorial;
- guaranteed to use every desired technology.

It should be selected because evidence supports all of these claims:

1. The problem is real.
2. The user and decision are specific.
3. The mission is compelling enough to sustain pursuit.
4. Real inputs create authentic uncertainty.
5. A credible end-to-end product is reachable.
6. The outcome can be evaluated.
7. The thesis is nontrivial and defensible.
8. The problem has deep curiosity runway.
9. The project develops the target career capabilities.
10. The product boundary is narrow enough for Ali to own.
11. Production-oriented engineering can be demonstrated honestly.
12. Scope growth can be controlled without destroying the mission.

## 20. Maintenance rule

Update this specification only when:

- Ali provides new durable project-fit requirements;
- candidate evaluation exposes a missing criterion;
- execution evidence contradicts an assumption;
- the formal project decision requires a deliberate refinement;
- ownership or scope controls prove insufficient.

Do not weaken a requirement merely to make a favored candidate pass.
