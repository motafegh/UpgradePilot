# UpgradePilot Capability and Prerequisite Specification

**Owner:** Ali Rajabi

**Recorded:** 2026-07-19

**Status:** Approved and controlling capability-control artifact

**Authority:** Controls UpgradePilot capability and prerequisite decisions; subordinate to ../UpgradePilot.md and higher-level governance

**Activation effect:** Defines capability gates only. It does not authorize implementation, repository creation, architecture design, corpus acquisition, a roadmap, a session plan, or an experiment.

## 1. Purpose and controlling boundary

This document specifies the capabilities needed to build and own UpgradePilot, when each capability becomes necessary, how it should be learned, and what evidence may justify a capability claim.

UpgradePilot remains exactly the product defined in ../UpgradePilot.md: an evidence-backed dependency-update decision system for maintainers of public Python repositories reviewing Dependabot pull requests. This specification does not redefine its mission, user, supported decision, product boundary, thesis, outcome classes, or advanced-systems ambition.

This is not:

- a generic computer-science curriculum;
- a technology catalogue;
- a course list;
- a 90-day roadmap;
- a milestone or session schedule;
- an implementation architecture;
- permission to begin technical work.

The governing learning rule is:

> Learn the smallest safe prerequisite before it blocks real work; learn the rest around a live UpgradePilot responsibility; require preserved ownership evidence before increasing the recorded depth.

## 2. Evidence basis and assessment limits

### 2.1 Evidence inspected

The assessment used:

- the Career repository at revision 88f34b71b52258f3361ed9f291a92eafe49d722b, including all files required by the task;
- the Career progress ledger, which explicitly records early assisted Python structure, basic assisted testing and debugging, mixed acquisition and validation evidence, guided secure-engineering reasoning, unestablished SQL depth, prior Docker exposure, and unverified ML exposure;
- AegisLab at revision b5f0234840338e2af012c46cfb4ead1ebcec0cad, especially its learner profile, current learning state, and namespace SSH lifecycle worklog;
- learning_sentinel at revision 211c3a5cb4f5169f9b83603975e95fba1846d56a, especially its index and session log;
- small public Git and GitHub Actions practice repositories;
- the public PersianLLM-API and Sentinel repositories as evidence of prior project exposure, not proof that Ali independently designed or owns their code.

### 2.2 What that evidence establishes

The strongest preserved practical evidence is guided rather than independent:

- Ali has operated real Linux and networking experiments, interpreted multiple evidence sources, and localized a controlled SSH authentication failure with substantial guidance.
- Ali has demonstrated introductory HTTP request and response understanding, client/server roles, listener and process inspection, and basic evidence-boundary reasoning.
- Ali has repeatedly used repositories and commits. A public practice history includes a revert and a basic GitHub Actions workflow.
- Ali has encountered Python applications, package files, data pipelines, tests, Docker, ML, LLM, graph, and MLOps concepts in prior repositories.

### 2.3 What that evidence does not establish

The inspected evidence does not reliably establish:

- independent blank-page Python application construction;
- independent test design or changed-case debugging;
- Python packaging and dependency-resolution competence;
- pull-request, branch, review, or open-source maintainer workflow ownership;
- SQL and relational-model ownership;
- independent data-pipeline, static-analysis, ML, graph, LLM-evaluation, Docker, CI, cloud, queue, Kubernetes, microservice, multi-agent, or MLOps capability;
- UpgradePilot-specific technical capability, because implementation has not begun.

Repository size, sophisticated architecture, completed AI-authored documentation, successful command execution, or the existence of tests and workflows cannot close these gaps by itself.

## 3. Capability-depth model

| Depth | Controlled meaning |
|---|---|
| D0 — Unassessed | Reliable ability has not been established. Mentioning, reading, watching, discussing, or seeing AI-generated work does not establish capability. |
| D1 — Introduced | Ali recognizes the full term, practical purpose, and basic relationship to UpgradePilot. |
| D2 — Guided application | Ali can perform a bounded UpgradePilot-relevant task with explanation, examples, and substantial assistance. |
| D3 — Independent bounded application | Ali can perform a representative project task, inspect output, and diagnose common problems with limited assistance. |
| D4 — Technical ownership | Ali can explain trade-offs, design or challenge the responsibility, implement or materially modify it, test it, diagnose failures, and connect it to the complete UpgradePilot flow. |
| D5 — Advanced independent capability | Ali repeatedly performs with low assistance across varied situations, unfamiliar failures, and substantial design trade-offs. |

D5 is not required for the core during this 90-day project. D4 is reserved for central product responsibilities. D2 or D3 may be the correct Day-90 result for bounded experiments and advanced exposure.

### 3.1 Required assessment dimensions

Every level record must separately state:

1. **Prior exposure (PE):** what Ali has encountered.
2. **Prior demonstrated evidence (PD):** what preserved behavior Ali personally performed or explained.
3. **UpgradePilot-specific evidence (UP):** what Ali has demonstrated in this project.
4. **Confidence (Conf):** High, Medium, or Low, based on evidence quality, recency, assistance, and transfer.

A provisional level means the evidence supports a cautious working estimate but a small project-embedded diagnostic is still required. A mixed group may record different subtopic depths rather than hiding uncertainty in one optimistic average.

## 4. Technical vocabulary and intentional depth

These definitions establish the mental model needed for the capability gates. They are not instructions to study every deeper mechanism now.

### 4.1 Repository and maintainer workflow

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Open-source maintainer workflow | The review, testing, discussion, release, and repository-governance work used to decide whether a public project accepts a change. “Maintainer” identifies the person responsible for sustaining the project. | Defines the real user and the decision context. | D1 before the first case; real trade-offs and repeated review patterns develop through cases. |
| Git | A distributed version-control system: each clone can contain history and branches. | Preserves project changes, evidence versions, experiments, and ownership history. | Basic history, diff, commit, and branch reasoning first; object internals and advanced history repair later. |
| GitHub | A hosted collaboration platform built around Git repositories, issues, pull requests, reviews, and automation. | Supplies the initial public repository, pull request, and Continuous Integration evidence. | Public read-only workflow first; administration and private-repository features later or out of scope. |
| Commit, branch, pull request, diff, history | A commit is a recorded snapshot; a branch is a movable line of work; a pull request proposes merging changes; a diff shows line-level change; history records prior snapshots and decisions. | The update itself and its repository context are expressed through these objects. | D1–D2 around the first PR; independent branch and review use develops during project work. |
| Dependabot | GitHub automation that detects dependency updates and opens pull requests. “Dependency bot” describes its role. | It defines the initial update-bot and PR boundary. | PR anatomy and limits now; alert internals, private alerts, and automated merge behavior remain outside the core. |

### 4.2 Python engineering and packaging

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Module, import, package, application structure | A module is a Python file or importable unit; import connects names across units; a package groups modules; application structure assigns responsibilities. | Keeps acquisition, evidence, decision, and reporting behavior traceable and changeable. | D1 before automation and D3 through the early vertical slice; metaprogramming and advanced import machinery later. |
| Type hint | A declared expected type used by people and tools; it is a “hint” because normal Python execution does not enforce all hints automatically. | Makes evidence and decision contracts inspectable. | Basic central contracts during implementation; advanced generic typing only when useful. |
| Exception | A structured signal that normal execution cannot continue as expected. | Separates source failure, invalid evidence, configuration error, and programmer defect. | Common handling patterns during acquisition; interpreter internals later. |
| Configuration | Values that change operation without changing source code, such as tokens, timeouts, and source choices. | Supports safe, reproducible runs without embedded secrets. | Environment and file boundaries when first needed; generalized configuration frameworks later. |
| Command-Line Interface — CLI | A text interface invoked from a shell. | Provides a small, reviewable way to run one case and reproduce behavior. | Bounded commands during the automated slice; complex CLI frameworks only if justified. |
| Python Package Index — PyPI | The public index from which Python package releases and metadata are commonly obtained. | Provides package and release evidence. | Metadata and release lookup first; index infrastructure internals later. |
| pyproject.toml | The standardized project configuration file used by Python build, packaging, and development tools. TOML means Tom’s Obvious, Minimal Language. | It can declare project metadata, dependencies, build settings, and tool configuration. | Read relevant dependency fields early; build-backend details just in time. |
| Requirements file, lockfile, package metadata | A requirements file lists install requirements; a lockfile records a concrete resolved set; metadata describes a distribution and its compatibility requirements. | They reveal declared and resolved dependency context at a particular snapshot. | Recognize and interpret the format encountered; support for every tool remains deferred. |
| Direct and transitive dependency | A direct dependency is declared by the project; a transitive dependency is required through another dependency. “Transitive” describes the relationship passing through an intermediate package. | The risk and investigation path may differ depending on how the updated package reaches the project. | D2 for the first encountered case; resolver-wide completeness later. |
| Dependency resolution | Choosing a mutually compatible set of package versions from constraints and metadata. | Needed to interpret lockfiles, paths, conflicts, and reproducible dependency context. | Observable inputs and outputs first; advanced resolver algorithms and backtracking internals deferred. |
| Version constraint, environment marker, optional dependency, extra | A constraint limits acceptable versions; a marker makes a requirement conditional on environment; an optional dependency is not always installed; an extra is a named optional feature set. | Prevents false claims about whether an update applies to a runtime, platform, or feature. | Read representative syntax when encountered; exhaustive cross-tool semantics later. |
| Semantic Versioning — SemVer | A convention using major, minor, and patch numbers to communicate kinds of compatibility change. The name indicates that version numbers carry intended meaning. | Supplies one weak signal for the baseline, never proof of compatibility. | D1–D2 early; ecosystem-specific deviations and release-policy analysis later. |

### 4.3 External evidence acquisition

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Hypertext Transfer Protocol — HTTP | The application protocol used to request and return web resources. | GitHub, PyPI, and release sources are commonly accessed through HTTP. | Existing guided foundation is enough to start; detailed HTTP versions, caching semantics, and transport internals later. |
| Representational State Transfer — REST API | An Application Programming Interface organized around resource representations and standard HTTP operations. “Representational state transfer” describes transferring a resource’s current representation. | Enables repeatable acquisition of PR, repository, package, and CI records. | Read one endpoint and response first; API design theory later. |
| JavaScript Object Notation — JSON | A text format for objects, arrays, strings, numbers, booleans, and null. It originated in JavaScript notation but is language-independent in practice. | Most initial public APIs return structured JSON evidence. | Read and transform a small response early; streaming and large-scale parsing later. |
| Authentication token | A secret value presented to prove API authorization. | May raise rate limits or permit authorized public API access. | Safe environment-variable handling when needed; delegated identity and enterprise authentication are out of scope. |
| Pagination and rate limit | Pagination divides a large result into pages; a rate limit bounds requests over time. | Prevents silent truncation and uncontrolled API use. | D2 before multi-case acquisition; optimization later. |
| Retry, backoff, cache, idempotency | Retry attempts again; backoff increases delay between attempts; cache reuses prior results; idempotency means repeating an operation does not create unintended duplicate effects. | Supports lawful, reproducible acquisition under temporary failures and limits. | Simple bounded policies at the reliable-acquisition gate; distributed cache design later. |
| Source preservation, schema change, partial source failure | Preservation retains raw response and source context; schema change means returned structure evolved; partial failure means some sources succeed while others do not. | UpgradePilot must show what was actually available and degrade honestly. | Central D2–D4 capability; automated schema evolution frameworks later. |

### 4.4 Data engineering and persistence

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Raw versus normalized evidence | Raw evidence preserves source form; normalized evidence maps it into a stable project contract. “Normalized” means brought into a consistent representation. | Enables traceability without forcing downstream logic to understand every source format. | D2 during the first milestone; large-scale lake patterns later. |
| Schema, validation, typing, transformation | A schema declares shape; validation checks conformance and meaning; typing records expected kinds; transformation derives one representation from another. | Prevents malformed or ambiguous source data from silently becoming a recommendation. | Central contracts through implementation; generalized schema platforms deferred. |
| Provenance | A record of origin, time, version, and transformations. The word means where something came from. | Every material report claim must resolve to preserved evidence. | Required from the first milestone; cryptographic provenance systems later. |
| Timestamp and snapshot | A timestamp records time; a snapshot records state as observed at a point or revision. | External sources and repository state change, so conclusions need temporal boundaries. | Required from the first case; event-sourcing platforms later. |
| Evidence states | Accepted, rejected, missing, inaccessible, stale, conflicting, and invalid describe distinct data-quality outcomes. | They control degradation, uncertainty, and abstention. | D2 first case and D4 core ownership; probabilistic source-trust modeling later. |
| Relational model | Data represented as tables with rows, columns, keys, and declared relationships. | Fits runs, sources, evidence, transformations, decisions, and comparisons. | One bounded model when persistence begins; distributed databases later. |
| Structured Query Language — SQL | A language for defining, changing, and querying relational data. | Supports traceability, diagnostics, repeated-run comparison, and evaluation datasets. | D2 when persistence begins and D3–D4 for central queries; advanced tuning and administration later. |
| Migration or reproducible schema setup | A migration changes a stored schema predictably; reproducible setup creates the same schema from a clean state. | Makes persisted evidence reviewable across code revisions. | Simple repeatable setup first; zero-downtime migration systems later. |

### 4.5 Decision and evaluation systems

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Deterministic rule, heuristic, decision table | A deterministic rule gives the same output for the same inputs; a heuristic is a useful but fallible shortcut; a decision table makes conditions and actions explicit. | Creates the transparent baseline and exposes assumptions. | D2 manual rule report first and D4 by baseline ownership; formal rule engines later. |
| Confidence, uncertainty, abstention, evidence sufficiency | Confidence represents support for an output; uncertainty represents what is unresolved; abstention declines to recommend; sufficiency asks whether evidence is adequate. | Prevents forced certainty when sources are missing or conflicting. | Central from the first report; advanced Bayesian methods later unless needed. |
| Asymmetric decision cost | Different mistakes have different consequences; a false “merge normally” may cost more than an unnecessary check. | Raw accuracy alone cannot represent maintainer utility. | D1 early, D3–D4 for evaluation; economic decision theory later. |
| Baseline | The simplest credible method used as a comparison point. | Tests whether context, ML, graphs, or AI add value. | Manual weak baseline first; stronger measured baseline before experiments. |
| Adjudication, label, ground truth | Adjudication applies a rubric to a case; a label is the recorded target; ground truth is the best supported reference, not automatically objective truth. | UpgradePilot lacks guaranteed objective labels, so disagreement and unadjudicable cases must stay visible. | D2 before corpus labeling; expert-consensus methodology later. |
| Leakage | Information from evaluation or the future improperly influences training or tuning. | Can make rules or models appear better than they generalize. | D2 before corpus splitting; advanced leakage audits as needed. |
| Calibration and held-out case | Calibration asks whether confidence matches observed outcomes; a held-out case is reserved from tuning. | Supports honest confidence and final comparison. | D2–D3 before learned evaluation; advanced calibration research later. |
| Metric, error analysis, reproducibility | A metric quantifies behavior; error analysis studies failures by type; reproducibility means the result can be recreated from declared inputs and versions. | Turns “looks useful” into inspectable evidence. | D2 at baseline and D4 by closure; broad statistical theory later. |

### 4.6 Repository context and machine learning

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Static source inspection and static analysis | Inspection reads code and configuration without executing the target program; static analysis systematically derives facts from that material. | Finds declarations, imports, references, tests, and workflows relevant to an update. | Text and syntax-level evidence first; whole-program sound analysis deferred. |
| Import, reference, runtime dependency, development dependency | An import loads or names code; a reference points to a symbol or package; runtime dependencies support product execution; development dependencies support testing, building, linting, or tooling. | Helps estimate where and when the changed dependency matters. | D2 on representative repositories; dynamic import completeness later. |
| Dependency path and reachability limitation | A path links the project to a package through relationships; reachability asks whether a node can be reached. Static reachability cannot prove runtime execution. | Supports contextual risk without making causal claims. | Basic paths and explicit limitations first; whole-program call-graph precision later. |
| Structural or graph representation | Entities are nodes and relationships are edges. “Graph” names that node-edge structure. | May represent dependency paths and propagation context better than flat fields. | Basic construction and comparison only after a flat baseline; advanced graph models deferred until evidence supports them. |
| Supervised learning | A model learns from examples paired with target labels. | May learn ranking or recommendation patterns if labels are defensible. | D1 only when label audit permits; no early prerequisite. |
| Classification and ranking | Classification selects a category; ranking orders cases by priority or score. | The action may be modeled as a class or investigation priority. | Compare formulations after baseline; advanced learning-to-rank later if justified. |
| Feature construction | Turning evidence into model inputs. | Connects repository, package, release, CI, and quality-state evidence to a learned method. | D2–D3 during an admitted experiment; automated feature platforms deferred. |
| Train, validation, test separation | Training fits parameters; validation selects choices; test estimates frozen performance. | Prevents tuning on the final evidence. | Required before any model claim; advanced resampling later. |
| Class imbalance, selective prediction, model comparison | Imbalance means some actions are rare; selective prediction allows abstention; comparison evaluates candidates on the same evidence and metric. | The action distribution and error costs are unlikely to be uniform. | D2–D3 for admitted ML; specialized research methods later. |

### 4.7 Secure, reliable, AI, and advanced systems

| Term | Practical meaning and why the name fits | UpgradePilot need | Depth now; intentionally later |
|---|---|---|---|
| Untrusted repository content, secret, least privilege | Public content may be malicious or misleading; a secret grants access; least privilege grants only necessary capability. | The system must inspect without executing arbitrary content and protect API credentials. | D2 from the first case and D4 core ownership; enterprise identity later. |
| Supply-chain risk | Risk introduced through dependencies, build inputs, release channels, and tooling. | It is both part of the maintainer problem and a responsibility of UpgradePilot’s own dependencies. | Basic controls during setup; formal supply-chain certification later. |
| Structured error and log, failure-path test | Errors and logs use stable fields; failure-path tests deliberately verify non-happy behavior. | Makes degraded evidence and diagnosis reproducible. | D2 during automation and D4 core ownership; observability platforms later. |
| Continuous Integration — CI and GitHub Actions | CI automatically runs checks on changes; GitHub Actions is GitHub’s workflow automation service. | Protects the supported core and demonstrates reproducible checks. | D2–D3 after the first automated slice; large deployment pipelines later. |
| Container and Docker | A container runs a process with isolated views and declared filesystem/configuration; Docker is a common container build and runtime tool. | Supports a reproducible representative runtime and later exposure packages. | D2–D3 when reproducibility requires it; storage/network internals later. |
| Grounded Large Language Model — LLM synthesis | A generative model produces text constrained by supplied evidence. “Grounded” means claims remain tied to sources. | May improve report comprehension if citations entail claims and unsupported assertions do not increase. | Evidence-dependent experiment only; model training and generalized assistants deferred. |
| Citation entailment and hallucination control | Entailment asks whether the cited source actually supports the claim; hallucination is unsupported generated content presented as fact. | A citation string alone does not make a report trustworthy. | D3 for an admitted LLM experiment; advanced natural-language inference research later. |
| Bounded multi-agent workflow | Several AI roles operate with explicit tools, shared state, authorization, termination, and review limits. | May improve evidence coverage, but must be compared with deterministic and single-agent flows. | A1 hands-on exposure later; autonomous external action remains outside scope. |
| Asynchronous job and distributed queue | Asynchronous work completes outside the immediate request; a distributed queue stores work for separate producers and consumers. | May help with rate-limited or long-running acquisition and analysis. | A1 then provisional A2 pilot after a synchronous limitation exists; distributed-systems internals later. |
| Modular monolith and microservice | A modular monolith keeps clear modules in one deployable application; a microservice gives one responsibility an independent process and deployment boundary. | The monolith is the comparison baseline; one service boundary may be piloted later. | Understand the boundary before A1; service fleets remain deferred. |
| Kubernetes | A system for orchestrating containerized workloads. The name comes from the Greek for helmsman or pilot. | Provides project-connected orchestration exposure for representative behavior. | A1 bounded deployment later; production cluster administration deferred. |
| Cloud and multi-cloud | Cloud uses provider-operated compute, storage, networking, and services; multi-cloud compares or operates across more than one provider. | Supports bounded deployment and portability comparison. | A1 comparison later; high-availability multi-cloud architecture deferred. |
| Machine Learning Operations — MLOps | Engineering practices for reproducible data, experiments, model artifacts, promotion, inference, monitoring, and replacement. | Controls the real model lifecycle or an honest negative model experiment. | A1 and provisional A2 after a defensible experiment exists; generalized platforms deferred. |
| Experiment tracking, artifact/model versioning, controlled inference and replacement | Tracking records runs; versioning identifies data/code/model outputs; controlled inference fixes what serves predictions; replacement uses evidence and approval to change it. | Prevents an untraceable model from entering reports. | D2–D3 during the admitted MLOps pilot; fleet-scale governance later. |

## 5. Provisional project-stage identifiers

These identifiers are capability gates, not a schedule:

- G1 — manual evidence-reality investigation;
- G2 — first automated end-to-end vertical slice;
- G3 — reliable acquisition, validation, and persistence;
- G4 — repository-specific dependency and usage context;
- G5 — deterministic baseline and corpus evaluation;
- G6 — learned and graph-based experiments;
- G7 — grounded LLM and bounded multi-agent experiments;
- G8 — distributed queue and service-boundary pilots;
- G9 — container, Kubernetes, and cloud exposure;
- G10 — final ownership and portfolio closure.

## 6. Capability matrix

### 6.1 Depth, evidence, timing, and learning mode

| ID | Capability and UpgradePilot responsibility | Current demonstrated or provisional depth | Minimum before first use | Expected Day-90 depth | Earliest gate and learning mode |
|---|---|---|---|---|---|
| C01 | Maintainer workflow, Dependabot, and update-decision reasoning: interpret one PR in the user’s real workflow. | **D1 provisional.** PE: charter and prior repository work. PD: assisted product/evidence reasoning; no preserved real update-review decision. UP: none. Conf: Medium for D1, Low above it. | D1 before G1; D2 before the first milestone passes. | D4 for the bounded supported decision. | G1; taught during first milestone and learned through repeated cases. |
| C02 | Git and GitHub collaboration: commits, branches, PRs, diffs, history, and review evidence. | **D1 provisional.** PE: several repositories and commit histories, one revert, basic Actions file. PD: repeated commits are visible, but command explanation, branches, PR review, and changed-history diagnosis are absent. UP: none. Conf: Medium for exposure, Low for application. | D1 for read-only G1; D2 before Ali owns an implementation change. | D3, with D4 for the project’s ordinary change/review workflow if repeatedly demonstrated. | G1 read-only; just-in-time and learned through implementation. |
| C03 | Python fundamentals, modules, imports, package/application structure: implement the central flow in understandable responsibilities. | **D1 provisional.** PE: assisted HTTP server and broad Python repositories. PD: can run and explain selected prepared behavior; Career ledger says early assisted structure. UP: none. Conf: Medium. | D1 before G2; D2 during G2. | D4. | G2; taught during first automated slice and learned through implementation. |
| C04 | Types, exceptions, configuration, CLI, testing, debugging, and dependency management: expose, protect, and change central behavior. | **D0–D1 mixed.** PE: tests, type declarations, CLI, and configs exist in prior projects. PD: basic assisted testing/debugging only; systematic design unproven. UP: none. Conf: High that D3 is not established. | D1 at first use; D2 before G2 closes. | D4 for central contracts, tests, CLI, and diagnosis; D3 for routine dependency management. | G2; taught and learned through implementation. |
| C05 | Python declarations and metadata: PyPI, pyproject.toml, requirements, lockfiles, package metadata. | **D0.** PE: files exist in prior repositories and learning material. PD: no preserved interpretation task. UP: none. Conf: High. | D1 before reading the first case; D2 before G1 closes. | D3 across the formats admitted by real cases. | G1; taught during first milestone, then just in time. |
| C06 | Dependency semantics: direct/transitive paths, resolution, constraints, markers, extras, SemVer, release and compatibility evidence. | **D0.** PE: dependency concepts appear in prior project material. PD: no reliable UpgradePilot-relevant task. UP: none. Conf: High. | D1 for first inspection; D2 before G1 closes. | D4 for bounded decision reasoning; resolver internals remain lower. | G1; taught during first milestone and through cases. |
| C07 | HTTP, REST API, JSON, authentication: acquire one source record lawfully and interpret its response. | **D1 provisional overall; HTTP subtopic D2 guided.** PE/PD: guided HTTP request/response and JSON-body observation; no API pagination/token ownership. UP: none. Conf: Medium. | Manual G1 needs only D1; automated G2 needs D2. | D4 for supported sources. | G1 manual and G2 automated; just-in-time learning. |
| C08 | Reliable acquisition: pagination, limits, retries, backoff, caching, idempotency, preservation, schema change, partial failure. | **D1 provisional; evidence-boundary reasoning D2 guided.** PE/PD: real source failures and cross-source reasoning in Sentinel/AegisLab; acquisition implementation ownership unverified. UP: none. Conf: Medium. | D1 concepts at G1; D2 before G3 work. | D4 for supported sources. | G1 preservation; G3 learned through implementation. |
| C09 | Raw/normalized evidence, schema, validation, typing, transformations, provenance, snapshots, and evidence states. | **D1 provisional.** PE: broad Sentinel data-pipeline exposure. PD: one logged data-learning session completed; no independent implementation. AegisLab shows guided evidence-source separation. UP: none. Conf: Medium for D1, Low above it. | D1 at G1; D2 before the first milestone passes. | D4. | G1; taught during first milestone and learned through implementation. |
| C10 | Relational persistence, one database, SQL, reproducible schema setup, queries, and diagnostics. | **D0.** PE: SQLite appears in prior repositories/plans. PD: Career ledger says required depth not established. UP: none. Conf: High. | D1 before G3; D2 while G3 is implemented. | D3–D4 for central schema and diagnostic queries. | G3; just-in-time and learned through implementation. |
| C11 | Deterministic rules, heuristics, decision tables, uncertainty, abstention, evidence sufficiency, and asymmetric cost. | **D1 provisional.** PE: assisted evaluation and evidence reasoning. PD: source limitations and failure layers were interpreted with guidance; no update baseline exists. UP: none. Conf: Medium. | D1 for a weak manual report; D2 before G1 closes. | D4. | G1 weak manual baseline; deepened through G5. |
| C12 | Adjudication, labels, ground-truth limits, leakage, calibration, held-out cases, metrics, error analysis, reproducibility. | **D0–D1 provisional.** PE: extensive AI-assisted Sentinel evaluation material. PD: Career ledger records assisted exposure; no independent label or evaluation design. UP: none. Conf: High that ownership is unestablished. | D1 for avoiding truth overclaims in G1; D2 before G5. | D4 for the accepted evaluation design. | G1 claim limits; G5 learned through implementation. |
| C13 | Static source inspection: imports, references, runtime/development roles, tests, workflows, and reachability limitations. | **D1 provisional.** PE: learning_sentinel includes guided source reading. PD: one completed ingestion session and several pending-question sessions; independent changed-repository analysis absent. UP: none. Conf: Medium. | D1 before G4; D2 during first contextual case. | D3, with D4 only for adopted core responsibilities. | G4; just-in-time and learned through implementation. |
| C14 | Dependency paths and structural/graph representations: build reproducible relationships without claiming runtime causality. | **D0.** PE: graph terminology and large graph/ML artifacts exist in Sentinel. PD: no reliable independent construction, comparison, or diagnosis. UP: none. Conf: High. | D1 before G4 path work; D2 before a G6 graph experiment. | D3 if the experiment is admitted; otherwise D1–D2 orientation is honest. | G4 basic paths; G6 evidence-dependent experiment. |
| C15 | Supervised learning, classification/ranking, features, splits, leakage prevention, imbalance, and model comparison. | **D0 provisional despite broad exposure.** PE: extensive ML documentation and project artifacts. PD: current Career ledger says unverified; learning records do not establish low-assistance execution. UP: none. Conf: High. | D1 before G6; D2 before fitting a candidate. | D3 if label audit admits ML; otherwise a bounded D2 negative experiment. | G6; evidence-dependent experiment. |
| C16 | Calibration, selective prediction, failure analysis, and rejection of unsupported model paths. | **D0.** PE: terms appear in Sentinel material. PD: no preserved independent application. UP: none. Conf: High. | D1–D2 before candidate evaluation. | D3 for an admitted learned method; D4 is not required. | G6; evidence-dependent experiment. |
| C17 | Secure and reliable engineering: untrusted content, secrets, least privilege, secure config, supply chain, errors/logs, failure-path tests. | **D2 guided provisional.** PE/PD: AegisLab contains real trust-boundary, key-handling, permission, safe cleanup, and failure-localization evidence with substantial guidance. UP: none. Conf: Medium; transfer is untested. | D1 at G1; D2 before automation handles untrusted content or tokens. | D4 for core trust and failure boundaries. | G1 claim/read-only boundary; learned through all core gates. |
| C18 | Reproducible environments, CI, GitHub Actions, containers, and Docker. | **D1 provisional.** PE: basic Actions repositories, Docker inventory, and containerized prior project. PD: Docker image/container/process model and CI diagnosis were not demonstrated. UP: none. Conf: Medium. | D1 before first use; D2 before G2/G3 CI or Docker closure. | D3–D4 for supported core reproducibility; A1-equivalent Docker/Kubernetes exposure separately recorded. | G2 CI when useful; G9 bounded container/orchestration exposure. |
| C19 | Grounded LLM synthesis, citation/entailment evaluation, hallucination controls, bounded output, cost and latency comparison. | **D0.** PE: RAG/LLM repositories exist. PD: no preserved grounded-claim evaluation or independent modification. UP: none. Conf: High. | D1 before G7; D2 before executing an experiment. | D3 if admitted; otherwise D1–D2 orientation. | G7; evidence-dependent experiment. |
| C20 | Bounded multi-agent work, asynchronous jobs, and distributed queues: explicit roles, state, retry, idempotency, termination, and recovery. | **D0.** PE: Sentinel contains agent architecture and evaluation artifacts. PD: no independent bounded workflow or queue operation established. UP: none. Conf: High. | D1 before A1; queue A2 additionally requires D3 core job and persistence ownership. | Multi-agent D2/A1; queue D3/A2 target if admitted. | G7 agents and G8 queue; bounded advanced exposure. |
| C21 | Modular monolith and microservice boundaries: compare one-process modules with one independently deployed responsibility. | **D0.** PE: architecture discussions and multi-component repositories. PD: no independent boundary implementation/comparison. UP: none. Conf: High. | D1 before A1; D3 modular-core understanding before A2. | D2/A1 minimum; D3 if an A2 pilot is authorized. | G8; bounded advanced exposure. |
| C22 | Kubernetes, cloud fundamentals, and multi-cloud comparison: deploy, configure, observe, fail, recover, compare, and clean up a representative workload. | **D0.** PE: Docker/cloud claims in older repository material. PD: no Kubernetes or two-provider execution evidence. UP: none. Conf: High. | D2 container/runtime foundation before A1. | D2/A1 for Kubernetes and multi-cloud; D3 only if an A2 pilot is justified. | G9; bounded advanced exposure. |
| C23 | MLOps, experiment tracking, artifact/model versioning, controlled inference, promotion, monitoring, and replacement. | **D0.** PE: MLflow and model-lifecycle artifacts appear in Sentinel. PD: no independent lifecycle operation or replacement decision. UP: none. Conf: High. | D2 ML/evaluation and reproducibility before A1. | D3/A2 target if an admitted model or bounded negative experiment exists. | G6 earliest foundation; G9/G10 operational evidence; bounded advanced exposure. |

### 6.2 Prerequisites, ownership evidence, risk, and deferred depth

| ID | Prerequisite relationships | Assessment task or ownership evidence | Consequence if weak | Intentionally deferred depth |
|---|---|---|---|---|
| C01 | Charter boundary and C02/C05/C06 basics. | Explain one real PR’s proposed change, evidence gaps, possible actions, and why disposition is not ground truth. | Report becomes a generic summary or unsafe verdict. | Maintainer governance across ecosystems and organizations. |
| C02 | None for read-only use; safe credential handling for authenticated operations. | Predict a diff/history command, explain output, make a bounded branch change later, inspect its diff, and recover a common mistake. | Lost provenance, unreviewable AI drops, weak ownership history. | Rebase surgery, bisect automation, Git object internals, repository administration. |
| C03 | Basic shell/file use. | Modify a small evidence transformation, predict output, run it, locate responsibility, and explain downstream report change. | AI owns the core while Ali only operates it. | Descriptors, metaclasses, interpreter/compiler internals. |
| C04 | C03. | Add or repair a test, classify an exception, change configuration safely, and diagnose a failing CLI case. | Silent regression and inability to maintain the core. | Framework-heavy abstractions and exhaustive typing theory. |
| C05 | C01 and basic text/structured-file reading. | Identify the declaration file, updated requirement, old/new versions, relevant metadata, and unresolved ambiguity. | The system can misidentify what changed. | Support for every packaging tool and build backend. |
| C06 | C05. | Distinguish direct/transitive status, interpret one constraint/marker/extra, and state what SemVer cannot prove. | False compatibility and applicability claims. | Advanced resolver algorithm internals and universal environment solving. |
| C07 | Basic HTTP/JSON understanding and C17 secrets. | Read a small response, identify status/body/fields, preserve source identity, and handle one error without hiding it. | Incomplete or unauditable evidence. | API platform design and high-throughput clients. |
| C08 | C07, C09, C17. | Predict retry/skip behavior, rerun without duplication, expose a partial failure, and preserve raw evidence. | Rate-limit abuse, duplicated state, hidden missing evidence. | Distributed caches, global scheduling, high-volume crawling. |
| C09 | C03 basics and C07 source records. | Predict validation states for changed examples, trace normalized fields to raw evidence, and explain a transformation. | Invalid data silently contaminates decisions and labels. | Generalized data platform and streaming architecture. |
| C10 | C09 and one chosen database only. | Create schema reproducibly, write/repair central queries, inspect duplicate/replay behavior, and diagnose a persistence failure. | Runs cannot be compared or audited reliably. | Replication, sharding, high availability, advanced tuning. |
| C11 | C01, C06, C09. | Build/challenge a decision table, predict outcomes, explain uncertainty, and modify one rule with tests. | Opaque scoring and unjustified certainty. | Formal decision engines and advanced probabilistic decision theory. |
| C12 | C09–C11 and a staged corpus later. | Adjudicate cases with a rubric, preserve disagreement, freeze a held-out set, compute/interpret metrics, and perform error analysis. | Misleading success claims and leakage. | Large-scale causal evaluation and generalized benchmarking platforms. |
| C13 | C02, C03/C05 basics. | Locate imports/references/tests/workflows for one dependency, explain runtime/development uncertainty, and identify a missed dynamic path. | Repository context becomes shallow or falsely complete. | Sound whole-program analysis and dynamic tracing across all frameworks. |
| C14 | C06, C10/C13, and a flat baseline. | Construct and query a small dependency graph, test reproducibility, state reachability limits, and compare with flat features. | Graph complexity adds no proven decision value. | Advanced graph algorithms and graph neural networks without measured need. |
| C15 | C12 label/split gate and measured C11 baseline. | Define target/features/split, fit a simple model, compare held-out results, and explain failures with reduced prompting. | Artificial ML and invalid comparison. | Deep models, broad hyperparameter search, recommendation-system scale. |
| C16 | C15 and enough held-out evidence. | Inspect reliability/selective-risk behavior, identify high-cost errors, and adopt or reject the model. | Confidence becomes decoration and bad models persist. | Advanced calibration research unless observed need exists. |
| C17 | Product trust boundary and source policy. | Identify untrusted content/secrets, predict blast radius, repair a secure-config or failure-path test, and explain claim limits. | Credential leakage, unsafe execution, or misleading security claims. | Enterprise identity, formal certification, hardened multi-tenant operation. |
| C18 | C03/C04 and a runnable slice. | Reproduce checks from clean state, repair one CI/runtime failure, explain container/process/config boundaries, and clean up safely. | Works-only-on-one-machine behavior and weak portfolio evidence. | Production platform engineering and fleet operations. |
| C19 | C09/C11/C12 provenance and baseline. | Evaluate claim-to-citation entailment, unsupported claims, omissions, abstention, latency, cost, and a changed failure case. | Fluent hallucination contaminates evidence-backed reports. | Foundation-model training and generalized RAG platforms. |
| C20 | Agents require C19 and C12; queues require C08/C10/C17/C18. | Agents: trace roles/tools/state/termination and recover one failure. Queue: inspect delivery/retry/duplicate/dead-letter behavior and compare with synchronous flow. | Unbounded autonomy or unreliable duplicate work. | Autonomous external actions and distributed queue fleets. |
| C21 | C03/C18 plus a stable modular monolith. | Trace request/response/config/logs, induce one boundary failure, measure burden, and adopt/reject extraction. | Artificial network boundaries and operational overload. | Service meshes and multi-service fleets. |
| C22 | C17/C18 and a representative deployable workload. | Deploy, inspect, roll out or fail, recover, compare with Docker/Compose or a second provider, and clean up. | Exposure displaces core ownership or creates cost/security risk. | Production cluster administration, high availability, multi-region operation. |
| C23 | C12/C15/C16/C18 and a real model lifecycle question. | Reproduce a run, identify data/code/model artifacts, apply an evaluation gate, operate controlled inference, and make a replacement/rejection decision. | Untraceable model claims and irreproducible inference. | Generalized MLOps platform and organization-scale governance. |

## 7. First-milestone readiness

Provisional first milestone:

> Construct a traceable evidence package for one real public Python Dependabot pull request and produce a weak manual or minimally automated decision report.

### 7.1 Required before the first working session

Only these capabilities are necessary to begin:

- D1 recognition of the read-only public-repository boundary and prohibition on automatic repository mutation;
- D1 recognition that the output supports a maintainer decision and does not determine objective safety;
- D1 ability to distinguish observed evidence, interpretation, missing evidence, and an unsupported claim;
- basic safe browser/repository navigation sufficient to open a public PR and its changed files.

The inspected AegisLab and Career evidence provisionally satisfies this entry threshold. The first session should confirm it briefly against UpgradePilot language, but no standalone prerequisite course is justified.

### 7.2 Teachable during the first session

- Dependabot PR anatomy;
- pull request, commit, diff, base revision, and head revision;
- the encountered Python dependency declaration or lockfile;
- direct versus transitive dependency at introductory depth;
- one version constraint and SemVer as a weak signal;
- source identity, URL, retrieval time, snapshot/revision, and raw versus normalized evidence;
- one small JSON response if the real case makes it useful;
- the five authorized recommendation classes and explicit uncertainty.

These concepts should be introduced around the real PR, not as detached lectures.

### 7.3 Required before the milestone can pass

Ali must demonstrate at least D2 guided application for the narrow case:

- explain what the diff changes and what it does not prove;
- identify package, old version, new version, declaration context, and direct/transitive uncertainty;
- preserve the PR, diff/revisions, relevant package/release evidence, source locations, and acquisition time;
- classify evidence as observed, inferred, missing, inaccessible, stale, conflicting, invalid, accepted, or rejected where applicable;
- produce one weak recommendation, targeted check, defer decision, or abstention with explicit reasoning and limitations;
- trace every material factual statement in the report to the evidence package;
- respond to one changed or missing-evidence case without inventing certainty;
- explain which work was AI-generated, AI-assisted, Ali-directed, Ali-verified, and Ali-owned.

If minimal automation is used, Ali must additionally reach D2 for the bounded Python/JSON transformation and its nearest test. A manual report can pass without Python automation.

### 7.4 Not required yet

The first milestone does not require:

- SQL or a database;
- automated multi-source acquisition;
- pagination, caching, retries, or backoff beyond what the one case actually needs;
- a corpus, adjudication program, held-out set, or calibration;
- repository-wide static analysis;
- complete dependency resolution or graphs;
- ML, LLMs, agents, queues, microservices, Kubernetes, cloud, multi-cloud, or MLOps;
- Docker or CI merely to inspect and structure the case;
- a permanent framework, service, or architecture decision.

## 8. Provisional stage capability gates

These are entry and closure conditions, not a dated sequence.

| Gate | Entry capability and required depth | Evidence needed to close | What may remain weak | What the gate is expected to teach |
|---|---|---|---|---|
| G1 — Manual evidence reality | C01/C02/C05/C06/C09/C11/C17 at D1 entry; narrow D2 before closure. | One traceable real-PR evidence package, weak report, changed/missing-evidence response, and ownership explanation. | Python, SQL, automation, static analysis, ML, and all advanced systems. | Real workflow, packaging semantics, provenance, evidence states, claim limits, and weak decision reasoning. |
| G2 — First automated vertical slice | G1 passed; C03/C04/C07/C09/C11 at D1–D2. | One real input reaches a reproducible CLI or equally bounded interface; central transformation and decision behavior have tests; Ali modifies and diagnoses a changed case. | Persistence may be temporary; acquisition may support only one source/case; no corpus or ML. | Python structure, contracts, exceptions, configuration, tests, debugging, and end-to-end causality. |
| G3 — Reliable acquisition, validation, persistence | Runnable G2; C07–C10/C17 at D2 entry. | Raw and normalized records, explicit quality states, partial failure, replay/idempotency behavior, one relational store, reproducible schema, central SQL queries, failure-path tests. | Repository-specific use context and sophisticated evaluation. | API reliability, source preservation, schemas, transformations, provenance, SQL, and diagnosis. |
| G4 — Repository-specific dependency and usage context | Reliable G3; C05/C06/C13 at D2; C14 at D1. | Reproducible declaration/path/use/test/workflow evidence for representative cases, plus explicit static and reachability limitations. | Whole-program precision, graph value, labels, ML. | Static inspection, dependency paths, runtime/development distinctions, structural limitations. |
| G5 — Deterministic baseline and corpus evaluation | Stable evidence contracts and persistence; C11/C12 at D2. | Versioned decision table, staged corpus, adjudication rubric, label limitation audit, contamination controls, held-out freeze, metrics, error analysis, reproducibility. | ML may be unjustified; calibration may remain limited by sample size. | Baseline discipline, asymmetric cost, abstention, labels, leakage, metrics, and rejection reasoning. |
| G6 — Learned and graph experiments | Measured G5 baseline; defensible labels/target; C14–C16 at D2. | Bounded hypotheses, simpler comparisons, reproducible features/splits, held-out results, failure analysis, and adopt/reject/defer decisions. A negative result can pass. | D4 ML mastery, deep learning, graph superiority, broad generalization. | Honest model/representation formulation and evidence-based rejection. |
| G7 — Grounded LLM and bounded multi-agent experiments | Provenance-backed deterministic report and evaluation; C19 at D2; C20 agent subtopic at D1. | LLM comparison for citations, entailment, unsupported claims, omissions, abstention, cost, latency; A1 bounded agent workflow with roles, tools, termination, traceability, and failure inspection. | Permanent AI adoption and autonomous action. | Grounding, claim evaluation, tool boundaries, coordination failure, comparison discipline. |
| G8 — Queue and service-boundary pilots | Stable modular core; observed synchronous/boundary question; C08/C10/C18 at D3 and C20/C21 at D1–D2. | A1 queue and service evidence; provisional A2 queue pilot if justified; retry/duplicate/idempotency/failure evidence; monolith comparison; explicit decision. | Fleet operation, high availability, many services, permanent queue adoption. | Asynchrony, delivery semantics, network contracts, operational burden, adoption discipline. |
| G9 — Container, Kubernetes, cloud exposure | Reproducible core; C17/C18 at D3; C22 at D1. | Representative container behavior; Kubernetes A1 deploy/inspect/fail/recover/cleanup; bounded two-environment multi-cloud A1 comparison subject to cost and credentials. | Production cluster/cloud administration and permanent multi-cloud. | Runtime boundaries, orchestration, configuration/secrets, rollout, portability, cost and failure trade-offs. |
| G10 — Final ownership and portfolio closure | Core gates completed or honestly reclassified; central capabilities mostly D3 with selected D4 ownership. | Clean reproduction, central modification/test/query/diagnosis, reduced-assistance explanation, experiment decisions, exact claim language, limitations, AI-assistance record. | D5, broad ecosystem support, and advanced-system mastery. | Integration of the whole flow and truthful career evidence. |

## 9. Diagnostic tasks embedded in project work

Diagnostics are not run during this documentation task. Future execution should preserve the prompt, Ali’s prediction, actions, outputs, assistance, correction, and final explanation.

| Diagnostic | Capability assessed | Earliest use | Preserved evidence | Blocking rule |
|---|---|---|---|---|
| Explain one real PR diff, including base/head and what changed evidence cannot prove. | C01/C02 | G1 | Written explanation linked to PR and revisions. | Does not block starting; must pass before G1 closure. |
| Locate the dependency declaration and distinguish direct, transitive, unresolved, and optional status. | C05/C06 | G1 | Annotated declaration/lock excerpt and reasoning. | Same as above. |
| Interpret one real version constraint and predict whether two example versions satisfy it. | C06 | G1 | Prediction, result, correction, limitation. | Same as above. |
| Read a small JSON API response and map selected fields without losing the raw record. | C07/C09 | G1 or G2 | Raw response, mapping, explanation, rejected/missing fields. | Required only when API use begins. |
| Modify a small Python evidence structure or transformation and predict report/test changes. | C03/C04/C09 | G2 | Commit/diff, prediction, tests, explanation. | Blocks G2 closure, not G1. |
| Predict accepted/rejected/missing/conflicting validation outcomes for changed examples. | C09/C11 | G1/G2 | Decision table and actual results later. | Narrow D2 required for G1. |
| Interpret and repair one relevant failing test without changing unrelated layers. | C04 | G2 | Failure output, hypothesis, repair diff, nearby success test. | Blocks G2 closure. |
| Write a basic SQL query that traces a report claim or compares two runs. | C10 | G3 | Query, result, explanation, changed case. | Only when persistence exists. |
| Locate imports, references, tests, and workflows for an updated dependency and identify one static limitation. | C13 | G4 | Search commands/output, source locations, limitation statement. | Blocks G4 closure only. |
| Detect leakage or contamination in a proposed split and correct it. | C12/C15 | G5/G6 | Split proposal, diagnosis, corrected grouping, impact. | Required before a learned claim. |
| Compare a simple model or graph feature with the frozen baseline and choose adopt/reject/defer. | C14–C16 | G6 | Reproducible results and decision record. | A negative decision passes. |
| Check whether cited evidence entails an LLM claim and classify one unsupported claim. | C19 | G7 | Claim/source pairs, judgments, disagreement, correction. | Required for LLM claim, not core. |
| Diagnose one queue, service, container, Kubernetes, or cloud failure from state and logs. | C20–C22 | G8/G9 | Prediction, evidence, repair/recovery, cleanup. | Required only for the corresponding exposure claim. |

Diagnostics should use the current UpgradePilot case, not unrelated quiz questions. A failed diagnostic triggers the smallest just-in-time repair and return to product work; it does not automatically create a course or stop unrelated progress.

## 10. Advanced-systems capability rules

The A0–A4 exposure scale in the Advanced Systems Exposure and Adoption Policy remains separate from D0–D5. Roughly, A1 normally requires at least D2 guided application of the bounded workload; A2 normally requires D3 independent bounded application of the pilot responsibility. Neither implies D4 ownership of the whole technology.

| Area | Prerequisites for A1 hands-on exposure | Additional prerequisites for A2 project-integrated pilot | Not required beforehand | Evidence for A1 | Evidence for A2 | Why it must not block the early core |
|---|---|---|---|---|---|---|
| Kubernetes | D2 container/image/process/config/log/port model; safe CLI use; representative workload; C17 secrets/cleanup. | D3 operation of the workload; multiple components or an observed rollout/Job/scaling question; Docker/Compose baseline; measurable comparison and recovery test. | Cluster internals, production administration, Helm, service mesh, high availability, multi-node design. | Deploy locally or bounded remotely; inspect Pods, Deployment/Job, Service/config; observe rollout or failure; recover and clean up; teach back. | Project branch/deployment, tests/measurements, baseline comparison, failure recovery, operational-cost and adopt/reject record. | The manual and automated report need neither orchestration nor multiple services. |
| Microservices | D2 HTTP/JSON, process/config/logging, module boundaries, and one representative responsibility. | D3 modular-monolith ownership; contract/integration tests; observed independent lifecycle/isolation question; latency, failure, consistency, and operations baseline. | Domain-driven-design mastery, many services, service mesh, distributed transactions. | Operate one bounded service boundary, trace request/response/log/config, inspect one failure, clean up. | Extract one responsibility, compare with monolith, measure costs/failures, decide retain/reject. | A single deployable modular application is the simpler credible core. |
| Distributed queues | D2 Python job function, retry/error concepts, idempotency, persistence, producer/consumer roles, safe local operation. | D3 reliable acquisition and database ownership; observed long-running/rate-limited synchronous limitation; duplicate/dead-letter/recovery tests; synchronous baseline. | Consensus algorithms, broker clustering, exactly-once guarantees, high throughput, fleet operations. | Run representative job; observe success and retry/failure; inspect state; demonstrate duplicate-safe behavior; clean up. | Integrate representative workload, test delivery semantics and recovery, compare latency/complexity/reliability, make decision. | One-case and early vertical-slice work can run synchronously. |
| Multi-cloud | D2 containerized/reproducible workload, configuration/secrets, one basic cloud deployment path, cost and cleanup boundary. | D3 deployment ownership; genuine portability/provider question; equivalent workload/config definition; explicit identity/network/storage/observability/cost comparison. | Multi-region resilience, provider certification, advanced networking, organization-scale FinOps. | Actual bounded configuration or execution in two environments/providers, comparison, teardown, cost record. | Mission-relevant integrated portability/resilience pilot with measurements and operating model. | Public evidence analysis works locally; multiple providers add no early decision value. |
| Autonomous multi-agent systems | D2 grounded LLM/tool use, source traceability, structured outputs, roles, authorization, shared state, termination, and deterministic/single-agent baseline. | D3 evaluation ownership; separable responsibilities; measurable quality/coverage question; conflict, failure, cost, latency, and recovery tests. | General agent platform, unrestricted tools, external mutation, indefinite autonomy, many agents. | Execute bounded representative investigation with explicit limits; inspect trace, conflict/failure, termination, and sources. | Compare with deterministic/single-agent/human-sequential baseline; measure and decide. | A deterministic evidence report is required first and is safer to learn and evaluate. |
| Advanced MLOps | D2 ML formulation, split/leakage, reproducible fitting, evaluation, artifact identity, controlled inference. | D3 model/evaluation ownership; repeated lifecycle need; data/model versioning; evaluation gate; promotion/replacement/rollback question; monitoring plan. | Generalized platform, feature store, high-scale serving, automated retraining, organization governance. | Reproduce a bounded training/fitting run, track experiment, identify artifact/version, evaluate, and run controlled inference. | Integrate several lifecycle controls around the real model or honest negative experiment, test replacement/rollback, and decide. | No model should exist before defensible data, labels, baseline, and evaluation; MLOps cannot manufacture that foundation. |

Exposure claims require executable project-connected evidence, output interpretation, one failure, cleanup, and teach-back. Project-integrated capability additionally requires comparison, tests or measurements, a representative UpgradePilot workload, and an explicit adoption decision.

## 11. Ownership assessment and AI-assistance control

### 11.1 Evidence combinations

No single act establishes ownership. Central capability evidence should combine:

- predicting behavior before running a command;
- explaining the command, important output, and what it does not prove;
- locating responsible code, configuration, schema, evidence, or data;
- implementing or materially modifying a bounded responsibility;
- writing, changing, or repairing tests;
- querying persisted evidence;
- diagnosing a failure from evidence before changing multiple layers;
- explaining downstream effects on the complete UpgradePilot flow;
- comparing a proposal with a simpler baseline;
- deciding to adopt, reject, defer, or retain an experiment;
- reproducing behavior with decreasing AI assistance.

### 11.2 Assistance labels

Every substantial ownership record should use:

- **AI-generated:** AI produced the artifact or code; Ali ownership not established.
- **AI-assisted:** Ali contributed but required substantial generation, explanation, or repair.
- **Ali-directed:** Ali specified the responsibility, constraints, or approach and evaluated the result.
- **Ali-verified:** Ali ran relevant checks and interpreted what they prove and do not prove.
- **Ali-owned:** Ali can explain, modify, test, diagnose, and reconnect the responsibility with limited assistance.

Working AI-generated code is not Ali-owned merely because it runs. D4 requires representative changed-case evidence and connection to the complete flow.

## 12. Critical prerequisite risks

Only risks capable of stopping or materially distorting UpgradePilot are listed.

| Risk | Affected capability and earliest gate | Why it matters | Diagnostic evidence | Remediation | Blocks next milestone? |
|---|---|---|---|---|---|
| Python implementation ownership is below the level needed for a central automated system. | C03/C04, G2. | A sophisticated AI-generated pipeline could hide weak ability to modify, test, or diagnose it. | Small transformation modification, predicted output, repaired test failure, reduced-prompt explanation. | Keep G2 narrow; teach around one responsibility; require Ali-directed changes and assistance labels. | **No** for starting or passing a manual G1; **yes** for G2 closure. |
| Python packaging and dependency semantics are unassessed. | C05/C06, G1. | Misreading a constraint, optional extra, lockfile, or direct/transitive path can distort the first report. | Locate declaration; interpret constraint; classify direct/transitive/unknown; state SemVer limits. | Teach only the format in the real PR; preserve uncertainty; use a second changed example. | **No** for starting G1; **yes** for G1 closure at narrow D2. |
| GitHub PR/diff workflow is exposure-level rather than demonstrated review capability. | C01/C02, G1. | The system starts from a PR; base/head, diff, checks, and history must not be conflated. | Explain a real diff and revisions; identify checks and missing historical evidence. | Guided inspection of the first PR, then reduced-prompt changed case. | **No** for starting; **yes** for G1 closure. |
| Evidence and claim discipline has not transferred to dependency updates. | C09/C11/C17, G1. | Guided AegisLab evidence reasoning is promising, but dependency evidence has different limitations. | Classify observed/inferred/missing/conflicting claims and choose abstention when evidence changes. | Reuse the evidence-boundary method, not AegisLab architecture; require traceability for every material claim. | **No** for starting; **yes** for G1 closure. |
| Label quality may not support the intended learned recommendation path. | C12/C15/C16, G5–G6. | Disposition is not ground truth; weak labels can invalidate ML, calibration, and MLOps claims. | Label audit, disagreement/unadjudicable cases, split/leakage inspection, baseline error analysis. | Reframe to investigation ranking, selective prediction, or bounded feasibility; record negative result. | **No** for the first milestone; blocks unsupported learned claims later. |
| Prior project breadth may encourage AI-assisted scope growth faster than ownership. | Cross-cutting, first material risk at G2. | Sentinel shows that impressive components can outpace independent understanding. | Weekly central modification/diagnosis evidence and ability to reject an unjustified addition. | One responsibility at a time, simpler baseline, admission gates, reduced prompting, explicit stop lines in later artifacts. | **No** for G1; blocks advancement when central ownership evidence is absent. |

No evidence supports declaring SQL, ML, graphs, agents, queues, Kubernetes, or cloud a prerequisite blocker for the first milestone.

## 13. Explicit deferrals

The following must not be front-loaded:

- advanced package-resolver algorithms, backtracking internals, and exhaustive cross-environment resolution;
- support for every Python package manager, declaration format, lockfile, build backend, and platform;
- whole-program static analysis, sound call-graph construction, dynamic-import completeness, and runtime-causality proof;
- graph neural networks and advanced graph-learning methods before a reproducible graph and flat baseline demonstrate a limitation;
- deep-learning recommendation models, large hyperparameter searches, and model scale without data and evaluation support;
- generalized retrieval-augmented generation or LLM platforms;
- autonomous agent platforms, unrestricted tools, or autonomous repository mutation;
- distributed service fleets, service meshes, distributed transactions, and generalized event platforms;
- production Kubernetes administration, multi-node resilience, autoscaling engineering, and cluster security specialization;
- high-availability, multi-region, or permanent multi-cloud architecture;
- generalized MLOps platforms, feature stores, automated retraining systems, and organization-scale model governance;
- database replication, sharding, high availability, and advanced query tuning;
- D5 depth for most topics.

A deferred topic becomes eligible only when an observed UpgradePilot limitation, a simpler baseline, an approved bounded hypothesis, success and rejection conditions, and ownership prerequisites justify it.

## 14. Current readiness judgment

### 14.1 Judgment

**Ready now.**

Ali is ready to begin the provisional first milestone because it can start manually, uses one real public case, and can teach the unassessed dependency-specific concepts in context. The inspected evidence establishes enough guided evidence-boundary, HTTP, repository, Linux, and failure-reasoning foundation to begin safely. It does not establish that the milestone has already passed or that automation should begin without ownership checks.

### 14.2 First prerequisite block

No standalone prerequisite block is required before the first working session.

The maximum entry confirmation is a brief UpgradePilot-specific check that Ali can:

- restate the read-only product boundary;
- distinguish observation from inference;
- state that a passing check, version number, or merged PR does not prove safety;
- explain why abstention is allowed.

This is confirmation of already introduced reasoning, not a separate course. The first real PR supplies the teaching context for the remaining D1–D2 concepts.

### 14.3 Important unassessed capabilities

The following remain D0 or materially provisional:

- real Dependabot PR review and maintainer workflow;
- branch, PR, diff, and code-review ownership beyond basic Git exposure;
- independent Python application structure, types, exceptions, tests, debugging, CLI, and dependency management;
- Python packaging formats, dependency resolution, constraints, markers, extras, and compatibility reasoning;
- API authentication, pagination, rate limits, retries, caching, and idempotency;
- normalized evidence contracts and UpgradePilot-specific provenance;
- relational modeling and SQL;
- deterministic baseline ownership, adjudication, metrics, calibration, and held-out evaluation;
- repository-specific static analysis and reproducible dependency paths;
- ML, graph, and model-selection capability;
- grounded LLM and entailment evaluation;
- CI/Docker failure diagnosis;
- multi-agent, queue, microservice, Kubernetes, cloud, multi-cloud, and MLOps capability.

They will be assessed at their earliest gates through the project-embedded diagnostics in Section 9. They must not be preemptively marked complete.

## 15. Next authorized artifact

After this specification is reviewed and approved, the next planning artifact is:

> **UpgradePilot Learning and Execution Contract**

That contract is not created in this task. This specification does not authorize implementation or any later planning artifact.
