# AI-Native Engineering and Career Capability Research Findings — Initial Evidence Map

**Date:** 2026-10-20  
**Branch:** `research/ai-native-career-capability-strategy-2026-10-20`  
**Status:** Provisional branch research; not a `main` integration decision.  
**Base state:** research branch was created from `ecd11a4a424bd1b6cecc8a8c83e9e17370ab88db`; `main` has already advanced beyond that anchor with additional Fresh Current CI cases, so every final recommendation remains subject to later reconciliation.

## 1. Research question

The horizon proposal intentionally preserves many possible capabilities. This pass asks a narrower question:

> **Which capability gaps are actually worth strengthening through UpgradePilot, which are already substantial but under-proven, and which should stay outside the product or be deferred despite career relevance?**

The objective is not to maximize technology coverage. The objective is to identify a coherent set of responsibilities that improve one or more of:

- real maintainer/product value;
- engineering quality and operational trustworthiness;
- Ali-owned technical capability;
- credible external evidence;
- employability for realistic near-term roles;
- the longer-term trustworthy AI / AI-security specialization.

## 2. Evidence consulted so far

### Repository/current-project evidence

- [`PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) — product decision, evidence doctrine, technology admission and claim limits.
- [`README.md`](../README.md) — public product surface, current CLI flow, assistance disclosure and current product limits.
- [`MEMORY.md`](../MEMORY.md) — current/recent experiment, comparison and ownership boundaries at the branch anchor.
- [`SECURITY.md`](../SECURITY.md) — untrusted-evidence, credential, external-action and execution trust boundaries.
- [`plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md) — evidence-derived route and X1 advanced-method gates.
- [`docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md`](../docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md) — canonical Workspace, revisions, recovery and authority separation.
- [`src/upgradepilot/workspace/checkpoint_store.py`](../src/upgradepilot/workspace/checkpoint_store.py) — current SQLite transaction/immutability/storage/backup implementation evidence.
- [`pyproject.toml`](../pyproject.toml) — narrow runtime dependency set; LangGraph remains experiment-only.
- [`.github/workflows/product-verification.yml`](../.github/workflows/product-verification.yml) — clean hosted package/test verification with pinned Actions and read-only permissions.
- [`proposals/2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md`](2026-10-19_INVESTIGATOR_RESPONSIBILITY_DECOMPOSITION_AND_PRODUCT_DIRECTION_PROPOSAL.md) — recent negative semantic evidence and product-value gate.
- [`proposals/2026-10-20_UPGRADEPILOT_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_HORIZON_PROPOSAL.md`](2026-10-20_UPGRADEPILOT_AI_NATIVE_ENGINEERING_AND_CAREER_CAPABILITY_HORIZON_PROPOSAL.md) — broad opportunity horizon.
- `product-simulation/fresh-current-ci-diagnostic-2026-10-20/` — current development cohort pressure. At the latest observed `main`, FCI002 and FCI003 preserve non-empty current GitHub runtime steps while intentionally remaining unresolved where matrix/dynamic or missing static display-name relationships exceed the present correlation contract.

### Current external capability/hiring signals

These sources inform **career prioritization only**. They do not create UpgradePilot product requirements.

- Cisco AI Workforce Consortium, *AI Agents and the Impact on Cybersecurity* — current G7 demand data places Python automation, prompt/context engineering, AI/ML model security, agent orchestration and MLOps/LLMOps among frequent agent-tagged cyber skills: https://www.cisco.com/site/m/ai-workforce-consortium/agent-cybersecurity-impact.html
- OpenAI, *Security Engineer, Agent Security* — a frontier example emphasizing production software engineering, isolation, network/identity controls, telemetry and cloud security rather than prompt knowledge alone: https://openai.com/careers/security-engineer-agent-security-san-francisco/
- OWASP GenAI Security Project, *Top 10 for Agentic Applications 2026* — identifies agent goal hijack, tool misuse, identity/privilege abuse, agentic supply chain, unexpected code execution, memory/context poisoning and related risks: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- GermanAI Defense, *Junior AI Software Developer* — current entry-level example explicitly accepting demonstrable own projects and emphasizing Python/TypeScript, Git, LLM/API experience, tests/documentation and understanding why behavior occurs: https://germanaidefense.de/karriere/ai-dev-junior
- Current AI-evaluation/reliability postings reviewed during this pass repeatedly combine Python, evaluation datasets/regression, adversarial scenarios, tracing/observability, SQL and production behavior. These are useful pattern evidence, not a claim that one specific posting defines the market.

## 3. Main finding

UpgradePilot does **not** currently suffer from a lack of technical surfaces.

The stronger pattern is:

```text
several valuable capabilities already exist
        ↓
but Ali-owned proof / external proof / reviewer legibility lag them

some genuinely missing capability classes exist
        ↓
AI-security attack evidence + external usefulness + operational diagnosis

many fashionable technologies are absent
        ↓
but absence alone is not a gap
```

Therefore the highest-leverage strategy is not to implement the horizon proposal breadth-first. It is to:

1. qualify and expose the strongest existing engineering responsibilities;
2. add a few missing evidence classes that naturally fit the product;
3. practise important fundamentals outside product runtime where appropriate;
4. obtain independent/external evidence;
5. defer technology expansion until a real product/operational responsibility demands it.

## 4. Capability evidence matrix

The statuses below are provisional research classifications.

### 4.1 Evidence, provenance and trustworthy knowledge architecture

**Current evidence:** **strong implemented foundation.** Exact target/revision identity, native evidence owners, explicit unresolved/unsupported states, proposition/applicability distinctions, lifecycle records and canonical Workspace/revision/recovery semantics already exist. The project repeatedly refuses to promote missing evidence or model claims into truth.

**What is not yet established:** complete end-to-end product usefulness, independent reviewer usefulness, blanket semantic adequacy, and Ali's independent ownership of all central paths.

**Career value:** very high and distinctive. This is a stronger signature than generic RAG or chatbot work because it demonstrates data lineage, epistemic state, authority and auditability.

**Recommendation:** **strengthen proof/presentation; do not add another generic truth/provenance framework.** A later reviewer-facing `Why?`/source→claim→decision trace may be valuable if it uses existing owners rather than duplicating them.

**Natural surface:** current product/report/portfolio presentation + Ali ownership exercises.

**Priority:** **very high for qualification and presentation; low for architectural expansion.**

### 4.2 Evaluation engineering and empirical method

**Current evidence:** **strong experimental capability, incomplete qualification.** The project already uses transparent baselines, frozen inputs, explicit resource ceilings, exposed-fixture caveats, source-aware semantic review, negative results and measured model/token/time costs. Recent Investigator variants completed mechanically while remaining semantically inadequate, and the project rejected unsupported adoption rather than counting successful execution as product success.

**What is missing:** protected/unseen qualification after material tuning; stronger independence where appropriate; external/user usefulness; a concise employer-facing evaluation result; more Ali-owned reasoning around protocol design, failure interpretation and causal limits.

**Career signal:** **very strong.** Current evaluation/reliability roles emphasize regression testing, adversarial evaluation, structured experiments, observability and cost/quality trade-offs. This closely matches work UpgradePilot already performs.

**Recommendation:** **top-tier capability thread.** Do not build a generic eval platform. Instead, mature one or two exact product/evaluation questions into reproducible, inspectable evaluation packets and a concise public case study. Preserve negative methods as evidence of judgment.

**Natural surface:** `experiments/`, product-simulation/evidence packets, later protected evaluation, portfolio case study.

**Priority:** **highest.**

### 4.3 AI/agent security and adversarial robustness

**Current evidence:** **strong policy/trust boundaries; weak adversarial proof.** `SECURITY.md` already states that PR text, repository files, CI output, model output and tool output are evidence/data rather than authority, forbids accidental external mutation/unknown-code execution, and separates credentials/transport from evidence truth.

**What is missing:** an explicit AI/agent threat model tied to the actual UpgradePilot architecture; adversarial fixtures; prompt/instruction injection cases; tool/authority abuse tests; context/evidence poisoning cases; security event/trace proof; attack→containment→residual-risk demonstrations.

**Career signal:** **very high.** OWASP's 2026 Agentic Top 10 and current agent-security roles emphasize exactly these responsibility classes. Importantly, strong roles also demand normal software/network/isolation/cloud engineering, so an attack corpus alone is insufficient.

**Recommendation:** **high-value genuine gap and likely signature thread**, but only through actual UpgradePilot trust boundaries. A bounded first security programme should prefer several real attack families over installing a security framework. Multi-agent structure is unnecessary for this proof.

Potential later families, subject to design and authorization:

- indirect prompt/instruction injection from repository/release/CI content;
- model request for an unauthorized capability/tool/action;
- evidence/citation poisoning or duplicate evidence presented as independent support;
- malicious path/URL/input boundary where the relevant product feature exists;
- context/resource exhaustion;
- unexpected code-execution request when target content is untrusted.

**Natural surface:** threat model + `product-simulation`/security fixtures + focused product/experiment security tests + portfolio attack case.

**Priority:** **very high, after/alongside product-value stabilization rather than instead of it.**

### 4.4 Reliability, durability and recovery

**Current evidence:** **substantial implementation, not merely a horizon idea.** The Workspace checkpoint store uses SQLite transactions, immutable historical tables, explicit storage failure classification, owner-only path checks, bounded contention, versioned schemas and online backup validation. ADR-0012 separately defines recovery/continuation boundaries and distinguishes recovery from replay.

**What is missing:** the final claim depends on current main integration state: complete product-path cutover/recovery, interruption demonstrations and Ali-owned diagnosis need to be verified rather than inferred from the existence of the store.

**Career signal:** high. Reliability is also a prerequisite for credible agent systems.

**Recommendation:** **finish/qualify the existing responsibility; do not add distributed infrastructure.** A strong future demonstration is process interruption → retained checkpoint → restart/inspection → explicit safe/unsafe continuation boundary.

**Natural surface:** product Workspace/recovery + failure tests + operational case study.

**Priority:** **very high for completion/ownership, low for new technology.**

### 4.5 Observability and operational diagnosis

**Current evidence:** **partial.** Experiments retain detailed timing, token, provider-attempt and resource-accounting evidence; project records preserve failure attribution carefully. This is valuable measurement discipline, but it is not yet a coherent product observability layer.

**What is missing:** durable structured application traces/diagnostic events across acquisition, Workspace revisions, tools/models, evaluation and report stages; operator-facing correlation; trace-based diagnosis proof. No OpenTelemetry dependency or production observability stack is currently present.

**Career signal:** high for AI evaluation/reliability and backend/platform roles.

**Recommendation:** **credible medium/high next capability, but start below OpenTelemetry.** First determine the smallest structured event/trace identity the real investigation lifecycle requires. Adopt OpenTelemetry/exporters only if a real service/operability boundary benefits from them.

**Natural surface:** product diagnostics / developer tooling / later service operation.

**Priority:** **medium-high, sequenced after the core lifecycle is stable enough to observe.**

### 4.6 Agent architecture and orchestration

**Current evidence:** **meaningful experiment exposure with important negative results.** LangGraph is experiment-only. The Workspace already separates native evidence, proposal, request, evaluation and action authority. Recent single/fixed/agent experiments repeatedly exposed unsupported semantic conclusions despite sophisticated control and evidence delivery.

**What is missing:** evidence that another agent role improves a named current product responsibility.

**Career signal:** high in current AI roles, but framework count is weak evidence.

**Recommendation:** **do not add a multi-agent product architecture now.** Preserve the existing failed/negative agent results as a strong engineering case study. Admit the smallest agent role only when a real residual uncertainty and baseline make it testable. A deterministic validator plus one bounded agent may be stronger than multiple model roles.

**Natural surface:** experiments until evidence earns product adoption.

**Priority:** **conditional/hold.**

### 4.7 Backend API / service engineering

**Current evidence:** **CLI-first product; no production web service.** `pyproject.toml` does not include FastAPI/Starlette as product dependencies. The current public interface and saved-report flow are legitimate software-engineering surfaces but do not demonstrate service/API operation.

**Career signal:** high, especially for near-term Applied AI/Python roles. Current entry and mid-level AI postings commonly expect Python APIs/backend integration.

**Product need today:** not established. A service could eventually be justified by long-running background investigations, remote users, cancellation/status or integration needs, but building one now would risk architecture-for-career-signaling.

**Recommendation:** **important career gap; product integration conditional.** Practise HTTP/API fundamentals separately or through a bounded later lab if necessary. Add an UpgradePilot service only after an actual user/operational boundary requires one.

**Natural surface:** initially separate learning/prototype; later product if justified.

**Priority:** **high career-learning priority; low immediate product priority.**

### 4.8 Database engineering

**Current evidence:** **already meaningful through SQLite.** Transactions, immutable records, foreign keys, versioned schema, WAL/storage modes, contention/error classes and backup are real database-engineering material.

**What is missing:** primarily Ali-owned depth and end-to-end operational proof, not a different database brand.

**Recommendation:** **learn deeply from the existing store before considering PostgreSQL.** Use current SQLite to understand transactions, locking, indexes/query plans, durability assumptions, schema evolution and backup. PostgreSQL should enter only if actual multi-process/concurrent service/query requirements outgrow SQLite.

**Natural surface:** learning/ownership on existing product code.

**Priority:** **high learning value; PostgreSQL deferred.**

### 4.9 Linux, operating systems and networking fundamentals

**Current evidence:** **exposure exists; ownership proof is weak.** The project has real WSL/local-model/proxy/process/resource and network-boundary history, but repository sophistication does not prove that Ali can independently diagnose sockets, processes, DNS/TCP/HTTP/TLS/proxy or resource failures.

**Career signal:** very high for backend, security, agent infrastructure and reliability work. Current junior security roles explicitly value networking/OS/system reasoning; advanced agent-security roles demand network/isolation depth.

**Recommendation:** **top-tier separate ownership programme, not a product feature.** Use UpgradePilot incidents and local services for diagnosis drills, plus separate focused practice where the product does not naturally expose a concept.

**Natural surface:** Learning-by-Doing / Learning-Only / incident drills outside runtime architecture.

**Priority:** **highest for Ali development.**

### 4.10 Testing and verification maturity

**Current evidence:** **strong breadth.** The active test tree contains extensive CI/runtime, investigation, CLI, package-manager, Workspace and other deterministic tests; experiments have their own regression boundary. The project also distinguishes what tests do and do not establish.

**What is missing:** Ali's ability to choose the correct test layer and diagnose failures; selected advanced techniques only where current invariants justify them.

**Recommendation:** **do not chase test-technique badges.** Property/state-machine testing is particularly plausible for Workspace invariants; fuzzing is plausible for parsers/structured external input. Adopt them when a concrete invariant/failure class needs stronger generative pressure.

**Natural surface:** product tests/experiments only when justified; ownership exercises now.

**Priority:** **high ownership, medium technique expansion.**

### 4.11 DevOps, packaging, release and containers

**Current evidence:** **partial but credible.** GitHub Actions performs a clean Python 3.12 package install and full deterministic regression on Ubuntu, with pinned Action SHAs, read-only repository permission and credential persistence disabled. The project remains version `0.0.0`; product verification is manual dispatch and there is no demonstrated release/container/deployment contract.

**Career signal:** strong. Docker, CI/CD and cloud fundamentals recur in current AI/backend positions.

**Recommendation:** **important portfolio/production-maturity thread, but staged.** A real versioned release, clean external installation and reproducible demo are higher value than Kubernetes. Docker is worthwhile when it supports a real reproducible service/runtime boundary; cloud comes after a supported deployable path. Kubernetes remains deferred unless operational need appears.

**Natural surface:** release/operations/portfolio rather than core semantic architecture.

**Priority:** **medium-high before strong job/portfolio push; Kubernetes low.**

### 4.12 Performance and cost engineering

**Current evidence:** **meaningful experiment measurement.** Model calls already record tokens, attempts, latency, operation units and resource ceilings. That is more useful than a generic benchmark claim.

**What is missing:** consistent product-level latency/cost profiles tied to user outcomes and possibly regression thresholds after the product path stabilizes.

**Recommendation:** fold this into evaluation/observability rather than create a separate subsystem.

**Priority:** **medium, compound with eval/operations.**

### 4.13 Human-AI UX and reviewer-first presentation

**Current evidence:** **partially improved but still internally heavy.** The README now gives a public product flow and clear assistance/claim limits. The repository remains deep and governance-heavy, and current product value/maintainer usefulness is not independently established.

**What is missing:** a short employer/user path; one compelling current real example; compact architecture diagram; fast evidence inspection; usability feedback.

**Recommendation:** **high priority after the current product-value question settles.** Prefer a small excellent reviewer surface over a React application built for breadth. A static/CLI walkthrough or thin evidence explorer may be sufficient.

**Natural surface:** README/docs/demo/possibly thin UI only if useful.

**Priority:** **very high for career conversion.**

### 4.14 External user / open-source validation

**Current evidence:** **major gap.** Internal simulation, AI review and project evidence do not show that another maintainer finds the tool useful or that another engineer can install, understand and work with it independently.

**Career signal:** extremely high for a candidate without prior professional software-team history. Current junior roles explicitly accept shipped personal projects, and security roles value non-trivial software/open-source/security initiative.

**Recommendation:** **one of the highest-value future threads.** Seek genuine maintainer review, external clean installation, issue/bug feedback, and at least one real upstream/open-source interaction when the product is ready enough. Do not manufacture collaboration artifacts.

**Natural surface:** external activity + retained feedback + portfolio.

**Priority:** **highest once a stable/useful slice exists.**

### 4.15 Ali-owned technical capability

**Current evidence:** **explicitly incomplete.** The README transparently states that substantial implementation/tests are heavily AI-assisted and not presented as independently authored/owned. Recent `MEMORY.md` repeatedly preserves pending learner D/E ownership even after technically successful/negative experiment cycles.

**This is not a defect in the AI-assisted method.** It is a separate proof responsibility.

**Recommendation:** **highest-priority cross-cutting programme.** For central capabilities, qualify through explanation, prediction, modification, diagnosis, transfer and defense. Avoid both extremes: requiring Ali to manually type generated code, or treating approval of an AI explanation as ownership.

High-value exercise forms:

- predict affected contracts/tests before an AI change;
- diagnose one failing trace before receiving an AI diagnosis;
- explain why a green test does not establish a stronger product claim;
- modify one bounded central path under AI assistance while controlling the design/proof;
- reason about an unseen/materially changed case;
- defend one architecture trade-off and rejected alternative.

**Natural surface:** project Learning-by-Doing/learning owners + compact portfolio ownership evidence.

**Priority:** **highest.**

### 4.16 Manual programming / interview fundamentals

**Current evidence:** repository complexity cannot prove independent fluency because implementation is heavily AI-assisted.

**Career need:** real. Entry roles still expect Python/Git/API/SQL fundamentals and interviews may include live coding/code reading.

**Recommendation:** **separate deliberate practice; do not corrupt product architecture by banning AI or forcing manual implementation.** Use UpgradePilot types/data for some exercises, but maintain a small independent Python/SQL/debugging practice track.

**Natural surface:** career-learning programme outside product runtime.

**Priority:** **high.**

### 4.17 Software/application security beyond AI-specific threats

**Current evidence:** secure defaults and boundaries exist around credentials, external actions, filesystem storage and untrusted execution. This is not equivalent to broad AppSec/security-engineering proof.

**Recommendation:** strengthen where UpgradePilot naturally exposes real surfaces: URL/resource acquisition, structured input parsing, filesystem paths, GitHub Actions/supply chain, secrets, eventual API/auth if introduced. Complement with separate security exercises/CTFs rather than forcing every security topic into the product.

**Priority:** **high career direction, medium product integration.**

### 4.18 Retrieval/RAG/vector databases

**Current evidence:** not a central product requirement. UpgradePilot performs bounded evidence selection/navigation and semantic experimentation, but current failures do not establish that embeddings/vector retrieval are the missing cause.

**Career signal:** common in Applied AI postings.

**Recommendation:** **do not introduce vector infrastructure for résumé coverage.** If retrieval quality becomes a measured bottleneck, compare lexical/structural/source-aware baselines first. RAG/vector practice can be separate if job preparation needs exposure.

**Priority:** **defer in product; optional separate learning.**

### 4.19 Cloud, Kubernetes and distributed systems

**Current evidence:** no justified distributed product requirement. Local durable state and current scope are intentionally bounded.

**Career signal:** useful, especially for senior platform/security roles, but not the current differentiator.

**Recommendation:** cloud fundamentals eventually matter; Kubernetes/distributed workers do not belong in the product until service/scale/security responsibilities require them. Prefer one later deployable path and understand it deeply.

**Priority:** **cloud fundamentals medium later; Kubernetes low/deferred.**

### 4.20 Frontend/full-stack breadth

**Current evidence:** not required for the current core user flow.

**Recommendation:** a thin report/evidence explorer may eventually improve product/reviewer usability, but frontend framework depth should not displace Python/evaluation/security/reliability fundamentals.

**Priority:** **low/conditional.**

### 4.21 Formal/property-oriented verification

**Current evidence:** the Workspace contains strong state/identity/immutability invariants that are plausible candidates for state-machine/property testing.

**Recommendation:** this is a potentially high-quality advanced technique because it fits real complexity. Do not add formalism generically. First identify an invariant family where example-based tests plausibly leave schedule/state-space risk.

**Priority:** **medium later; stronger fit than many résumé-oriented technologies.**

## 5. Provisional priority groups

### Group A — strengthen now through proof/ownership/research, not technology expansion

1. **Ali-owned capability qualification**
2. **Evaluation engineering and empirical method**
3. **Evidence/provenance architecture as a signature capability**
4. **Reliability/recovery completion and diagnosis**
5. **Linux/networking/Python/SQL/backend fundamentals**

These mostly build on responsibilities already present. The immediate opportunity is to convert internal sophistication into demonstrable skill and concise evidence.

### Group B — genuine missing evidence worth designing as likely signature additions

1. **AI/agent security threat model + adversarial tests**
2. **External maintainer/user/open-source validation**
3. **Operational observability/trace-based diagnosis**
4. **Reviewer-first portfolio/demo surface**

These fill actual evidence classes that current implementation depth does not already provide.

### Group C — useful career capabilities, but product adoption must be earned

- backend HTTP/API service;
- Docker/release/deployment;
- cloud fundamentals;
- stronger property/fuzz testing;
- application-security expansion;
- richer data analysis/SQL around evaluation results.

These can be practised separately until a product need makes integration natural.

### Group D — explicitly resist for now

- multi-agent architecture merely for agent breadth;
- PostgreSQL merely to replace existing substantial SQLite work;
- vector database/RAG because jobs mention it;
- microservices;
- distributed queues/workers without concurrency/operation need;
- Kubernetes;
- multi-cloud;
- large frontend build;
- learned ranking/ML before enough data and baseline evidence exist.

Absence from UpgradePilot is not a deficiency when the responsibility is absent.

## 6. Provisional career-position consequence

The research so far supports a **two-level identity** rather than one narrow title.

### Near-term market identity

A defensible broad positioning is approximately:

> **Python / AI systems engineer focused on trustworthy automation, evaluation, reliability and security.**

This keeps realistic entry paths open across:

- junior/associate AI software engineering;
- Python/backend roles with AI integration;
- AI-native software engineering;
- developer tooling/automation;
- junior security engineering / security automation;
- evaluation-oriented AI work when experience requirements fit.

The current GermanAI Defense entry-level posting is particularly relevant as evidence that demonstrable own projects, Python/TypeScript, Git, LLM/API experience and tests can form a legitimate entry signal.

### Longer-term specialization

Continue compounding toward:

> **AI Security Automation / Agent Security / trustworthy agent systems.**

The OpenAI agent-security profile demonstrates why the destination requires more than prompt-injection knowledge: production software engineering, network/identity controls, isolation, secure telemetry and cloud security are core. UpgradePilot can contribute part of that path, but separate systems/security depth is necessary.

## 7. Candidate signature demonstration set

This is provisional, not yet an implementation plan.

A small coherent set appears stronger than broad feature accumulation:

### Signature 1 — evaluation/judgment

A bounded AI/agent method produces a plausible but materially unsupported conclusion; predeclared semantic review rejects it; the project preserves cost, evidence, uncertainty and the rejection decision.

Much of the raw material already exists. The main missing work is concise qualification, Ali ownership and employer-facing presentation.

### Signature 2 — AI-security containment

Attacker-controlled repository/CI/release content attempts to manipulate an AI-assisted investigation or capability request. The system treats it as untrusted data, contains unauthorized effect, preserves trace/evidence and reports residual uncertainty.

This is a genuine missing evidence class and aligns naturally with UpgradePilot's domain.

### Signature 3 — reliability/recovery

An investigation is interrupted during evolving work; durable state is restored; completed/unresolved/unsafe-to-continue work remains distinguishable; continuation is validated rather than guessed.

The architecture and storage foundations already exist; the exact remaining product proof must follow current `main` rather than this branch's assumptions.

### Signature 4 — external usefulness

Another developer/maintainer can run or inspect the supported path and provide concrete feedback about usefulness, misleading statements, uncertainty and actionability.

This is not replaceable by another internal model or test suite.

Four is an upper bound for a coherent public set, not a quota. The final strategy may use fewer.

## 8. Main-state delta observed during this research pass

After branch creation, `main` advanced from `ecd11a4a` to observed `862731e0` through two additional FCI case commits. The delta is limited to the fresh diagnostic cohort rather than product architecture/source changes.

Material new evidence:

- **FCI002 (`mdformat-footnote`, tox):** current GitHub provider data exposes non-empty runtime steps, but the matrix and missing explicit static display names require the current correlator to refuse rather than guess. Green pytest jobs do not establish updated tox install/exercise.
- **FCI003 (`pasarguard`, FastAPI):** current provider data again exposes non-empty runtime steps. No matrix exists, but jobs lack explicit literal `name:` and current correlation intentionally refuses YAML-key→runtime-name inference. Green `make setup-test`/`make test` jobs do not themselves establish exact FastAPI installation/exercise.

This strengthens an important research conclusion: **the project currently benefits from precise unsupported/refusal semantics and real current evidence; the career branch should not prescribe broader CI correlation merely to produce more positive results.** Current FCI work may instead become good evidence of trustworthy refusal/diagnosis if the cohort later supports that conclusion.

No branch rebase/merge is justified by these two evidence-only additions. Final strategy will re-read the completed FCI disposition from `main` before integration decisions.

## 9. Next research decisions

Before designing exact additions, the remaining research should answer:

1. **Ownership control:** What is the smallest durable capability-evidence/ownership mechanism that helps Ali without creating a second project-management bureaucracy?
2. **AI-security scope:** Which 3–5 attack families naturally exercise current/near-term UpgradePilot surfaces and can be evaluated deterministically enough to be credible?
3. **Observability:** What operator questions exist now that current working-memory/evidence artifacts cannot answer efficiently, and what is the simplest trace/event baseline?
4. **External validation:** At what product maturity point should a maintainer trial begin, and what feedback protocol avoids marketing-style confirmation bias?
5. **Portfolio surface:** What can an unfamiliar reviewer learn in 1, 3 and 10 minutes without reading the internal governance history?
6. **Separate fundamentals track:** Which capabilities should be deliberately learned outside product architecture (Python fluency, SQL, HTTP/networking, Linux, cloud/Docker) and how can UpgradePilot supply realistic exercises without pretending they are product features?
7. **Final sequencing:** How should these capability threads coexist with the actual then-current main product responsibility rather than interrupt it?

These questions should be resolved before converting this matrix into implementation tasks.

## 10. Provisional conclusion

The broad horizon proposal survives the first audit, but the correct strategic use is **selective mining**, not breadth-first execution.

The strongest emerging strategy is:

```text
finish and understand the serious engineering already present
+ qualify evaluation as a real capability
+ add adversarial AI-security proof where naturally justified
+ improve operational diagnosis
+ obtain external usefulness/collaboration evidence
+ build concise reviewer-facing proof
+ practise missing fundamentals separately
```

while deliberately resisting:

```text
more agents
+ more frameworks
+ more infrastructure
+ more databases
+ more services
```

unless the product itself earns them.

This is an initial evidence map, not the final branch disposition. The next research step is to design the **ownership/capability-evidence mechanism and the candidate AI-security/external-validation threads** at enough precision to decide whether they belong in later `main`, stay branch-only, or remain outside UpgradePilot entirely.
