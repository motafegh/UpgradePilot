# Real-world engineering practices × UpgradePilot — project-fit study

**Status:** active, non-controlling research/learning working memory  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Branch base:** `1781bb6aa70fb0824a2de2271cf7ce6b4052e44b` (`main`, 2026-10-24)  
**Purpose:** progressively examine real-world software-engineering terms, patterns, practices, operational mechanisms and governance concepts against UpgradePilot's actual architecture, code, evidence doctrine and product needs; retain both learning and engineering judgments; defer any product adoption until the end-of-study decision or a separately authorized product responsibility.

This record is intentionally **not** a master plan, specification, ADR, product authorization, or replacement for `MEMORY.md`. `MEMORY.md` remains the sole owner of live project position. The active `main` position at branch creation is Learning-Only; engineering progression is paused. This branch must not silently activate the proposed deterministic API call/signature design, Workspace migration, acquisition, inference, target execution, or any other product implementation.

## Cycle status

- **A0 — DONE:** reconciled current `main`, governing ownership, recent product/source-access work, current Learning-Only selection, and branch boundary; created this single cycle working-memory record.
- **A1 — DONE:** current system orientation established sufficiently for this study: typed evidence/domain owners, application orchestration, Workspace foundations and staged migration, report/source preservation, current action boundary, experimental semantic failures and unresolved maintainer-value question.
- **A2 — CURRENT:** establish and refine the term-by-term decision method and candidate inventory. Each term is oriented when selected rather than teaching the entire inventory upfront.
- **B — PENDING / ITERATIVE:** investigate selected terms one by one against current source, tests, plans/ADRs and real product needs; record evidence and disposition candidates.
- **Verification gate — PENDING / PER-TERM:** claims about existing implementation or fit must be checked against actual repository evidence; adoption claims require their own later proof.
- **D — PENDING / ITERATIVE:** consolidate what each term teaches about UpgradePilot and distinguish vocabulary recognition from actual architecture ownership.
- **E — PENDING:** final cross-term synthesis; decide what to recognize as already present, name more clearly, adopt, experiment with, defer, reject, or keep outside project scope. Any consequential adoption must return to its proper product owner/plan/ADR/build route.
- **C — CONTINUOUS:** preserve only meaningful term analyses, changed judgments, evidence, unresolved questions, and final dispositions here.

## Current project anchor for this study

At this branch base:

1. UpgradePilot remains a **production-oriented evidence-backed dependency-update decision system** for maintainers of public Python repositories. The Charter requires provenance, explicit uncertainty, bounded recommendations/abstention, reproducibility obligations and evidence-driven technology admission.
2. The executable system already has substantial separation of concerns: provider/acquisition modules, typed dependency/CI/upstream/target/impact owners, `investigation.py` application orchestration, report projection/rendering, maintainer-action synthesis, and a dedicated `workspace/` subsystem.
3. Workspace concepts are implemented, not merely planned: immutable checkpoint revisions, durable checkpoint storage, lifecycle host/boundaries/records, native capture/codecs/projection/reconstruction, consumer access and material-validity handling exist. The ordinary product path is still **staged**: legacy investigation fields coexist with the Workspace revision boundary, and normal user-facing migration/recovery/replay is incomplete.
4. PR-description preservation and explicit offline source inspection are implemented and verified. Source availability is deliberately kept distinct from semantic interpretation, upstream authority and target applicability.
5. The currently admitted maintainer action remains only **explained `abstain`**. Non-abstention permissions have not been proven through the normal producer path.
6. The strongest strategic debt is not simply missing infrastructure. Recent audit/review evidence says independent maintainer usefulness remains unproved, normal end-to-end impact/action reachability is narrow, and broader semantic experiments have demonstrated real interpretation failures.
7. The current proposed engineering handoff for a later explicit return is a bounded deterministic API call/signature evidence design reusing existing target-source/binding/call-keyword/adapter work. This study does not activate it.

These anchors are allowed to become stale as `main` progresses. Before a term analysis depends materially on current product state, refresh the relevant repository evidence and record the newer horizon here rather than assuming this branch-base snapshot remains authoritative.

## Decision method for every term or practice

For each selected concept, answer in this order:

1. **WHAT** — precise professional meaning; distinguish it from nearby terms and common misuse.
2. **WHY** — concrete failure mode, scaling pressure, coordination problem, proof need or operational need it addresses.
3. **WHERE** — where that responsibility would map into UpgradePilot, if anywhere.
4. **CURRENT REALITY** — what UpgradePilot already does in source/tests/owners, not what old prose or analogy suggests.
5. **OVERLAP / DISTINCTION** — whether we already have the mechanism under another name, only resemble it structurally, or genuinely lack it.
6. **FIT** — benefit, complexity, maintenance cost, new failure modes, learning value, and interaction with the Charter's technology-admission rule.
7. **EVIDENCE / TRIGGER** — what observable need or proof would justify adoption, expansion or rejection.
8. **DISPOSITION CANDIDATE** — one of:
   - `RECOGNIZE_EXISTING` — already present enough that the useful action is understanding/naming, not new machinery.
   - `CLARIFY_TERMINOLOGY` — current behavior exists but naming/documentation could become more precise.
   - `KEEP_PARTIAL` — selected elements are justified; adopting the full named pattern would overstate or overbuild.
   - `EXPERIMENT_IF_TRIGGERED` — credible but requires a bounded hypothesis and product/evaluation trigger.
   - `ADOPT_LATER_IF_EARNED` — likely useful at a foreseeable milestone, but not authorized/currently necessary.
   - `DEFER` — no current need or evidence; reconsider only on a named trigger.
   - `REJECT_FOR_CURRENT_PRODUCT` — conflicts with current architecture/boundary or adds unjustified complexity.
   - `OUTSIDE_SCOPE` — valid real-world concept, but not a responsibility of UpgradePilot's present product boundary.

A familiar industry label is never evidence by itself. Do not retrofit architecture to a buzzword. Conversely, do not reject a concept merely because current implementation already solves part of it informally; the analysis should determine whether clearer ownership or a standard mechanism would materially improve correctness, maintainability, proof or delivery.

## Initial concept inventory — hypotheses, not decisions

The inventory is deliberately broader than the items likely to be adopted. It gives us a reusable queue and vocabulary. Each row's relation is only a starting hypothesis until we inspect the term properly.

### Architecture, modularity and boundaries

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Modular monolith | Strongly relevant; current repository looks much closer to this than to microservices. |
| Layered architecture | Substantial real separation exists, but exact layers should be described from code rather than forced into textbook names. |
| Domain model / domain layer | Strongly present through typed evidence/result/problem owners. |
| Application/service layer | `investigation.py` is a clear candidate application orchestration boundary. |
| Infrastructure/adapters | GitHub/PyPI/provider clients and persistence boundaries resemble this responsibility. |
| Dependency Injection (DI) | Already materially present through injected clients/evaluators/Workspace components. |
| Inversion of Control (IoC) | Related to DI but should be distinguished carefully; not every injected dependency implies an IoC container. |
| Ports and Adapters / Hexagonal architecture | Structural similarities exist; whole-system label is not yet earned automatically. |
| Clean Architecture | Some dependency-direction ideas may fit; full label may overstate the current design. |
| Domain-Driven Design (DDD) | Responsibility-rich domain modeling exists; strategic/tactical DDD adoption is unestablished. |
| Bounded Context | Potentially useful vocabulary for evidence/CI/upstream/workspace/report boundaries; needs proof that contexts, not just modules, exist. |
| Anti-Corruption Layer | Potentially relevant at external GitHub/PyPI/model/provider boundaries if translation protects domain semantics. |
| Repository Pattern | Must distinguish persistence repositories from Git/GitHub repositories; likely only partially relevant. |
| Facade | Potentially already present at selected orchestration/consumer boundaries. |
| Adapter Pattern | Clearly relevant around provider and experimental integration seams. |
| Strategy Pattern | May describe interchangeable evaluators/providers in some places; avoid pattern-labeling ordinary callables. |
| State Machine | Strong relevance to lifecycle and explicit states; determine whether formal state-machine semantics are actually owned. |
| CQRS | No current demonstrated need; read/write separation alone would not justify the label. |
| Event Sourcing | Do not equate immutable revisions/checkpoints with event sourcing; likely unjustified unless event history becomes the source of truth. |
| Strangler Fig migration | Potentially useful lens for staged legacy-result → Workspace consumer migration. |
| Plugin architecture | Could matter only if multiple provider/ecosystem extension points become product responsibilities. |
| Microservices | Likely a poor fit for the current bounded product/deployment model. |

### State, persistence, consistency and reproducibility

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Immutable snapshots / revisions | Strongly present in Workspace. |
| Checkpointing | Strongly present; distinguish checkpoint recovery from replay and event sourcing. |
| Durable execution | Only partially related; current checkpoints/lifecycle do not automatically establish a durable-execution engine. |
| Deterministic replay | Explicit Charter outcome with a separate proof boundary; not yet equivalent to saved-report reopening or reconstruction. |
| Schema evolution | Already a real responsibility across report/native/checkpoint formats. |
| Database migration | Relevant to durable Workspace storage as schemas change; inspect actual migration owner before naming it complete. |
| Backward compatibility | Explicitly handled in several saved/native boundaries. |
| ACID transactions | Relevant to SQLite publication boundaries; need exact implementation analysis. |
| Transaction boundary | Important around coherent checkpoint publication and consumer visibility. |
| Unit of Work | Potential analogy around Workspace publication; adoption is not implied. |
| Optimistic concurrency | Likely relevant to competing-writer/refusal behavior. |
| Compare-and-Swap / CAS | Potentially describes revision/expected-head publication semantics; inspect exact code first. |
| Idempotency | Relevant to acquisition/publication/retry safety; no blanket claim yet. |
| Content addressing / hashes | Strongly present for integrity/provenance in several evidence paths. |
| Data lineage | Strong conceptual fit with evidence provenance. |
| Provenance | Core project doctrine and one of the strongest existing characteristics. |
| Data contracts | Strong relevance to typed producer/consumer evidence boundaries. |
| Cache / caching | Potential future performance mechanism; high freshness/provenance risk means no default adoption. |
| Cache invalidation | Particularly material if caching ever enters evidence acquisition. |

### Reliability and operational engineering

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Timeout | Already relevant for external providers; inspect ownership and consistency. |
| Retry | Must preserve evidence/time/error semantics; automatic retry is not automatically safe. |
| Exponential backoff / jitter | Possible provider concern only if retry is justified. |
| Rate limiting | External API reality; distinguish client behavior from product-level policy. |
| Circuit breaker | Probably premature for current local/single-user operation. |
| Bulkhead isolation | Likely unnecessary at current scale unless concurrent external subsystems justify it. |
| Graceful degradation | Strong conceptual match with explicit partial/unsupported/unknown outcomes. |
| Fail-open vs fail-closed | Very relevant to evidence admission, action permission and security boundaries. |
| Health checks / readiness checks | Relevant only when supported services/deployment require them. |
| Observability | Underdeveloped relative to evidence retention; needs separate logs/metrics/traces analysis. |
| Structured logging | Potentially useful before full observability tooling. |
| Metrics | Useful only with concrete operational/product questions. |
| Distributed tracing | Probably unjustified while architecture remains a local modular monolith. |
| OpenTelemetry | Likely premature absent a real observability/deployment need. |
| SLI / SLO | Could matter after a supported operational service exists and reliability is measured. |
| SLA | Outside current internal/production-oriented stage unless a real external service commitment appears. |
| Error budget | Depends on meaningful SLOs and production operation; likely premature. |
| Feature flags | Useful only if staged user-facing behavior/experiments need safe runtime switching. |

### Testing, verification and evaluation

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Unit testing | Strongly present. |
| Integration testing | Strongly present in several composed paths; exact classification should be evidence-based. |
| End-to-end (E2E) testing | Some real-path proofs exist, but full supported-user E2E and hosted proof remain distinct. |
| Acceptance testing | Relevant to Charter/product responsibility and independent usefulness, not synonymous with regression tests. |
| Contract testing | Strongly relevant to producer/consumer boundaries. |
| Consumer-Driven Contract (CDC) testing | Do not claim merely because consumers are tested; requires explicit consumer-defined contract workflow. |
| Property-based testing | Candidate for invariant-heavy parsers/state/codec logic where example tests may miss combinations. |
| Golden / approval tests | Potentially useful for stable rendered reports; risk of blessing incorrect semantics must be controlled. |
| Snapshot tests | Similar utility/risk to golden tests; not a substitute for semantic assertions. |
| Mutation testing | Potential quality diagnostic for important deterministic logic if cost is justified. |
| Fuzz testing | Potentially strong for parsers/serialization/untrusted inputs. |
| Fault injection | Relevant to persistence/provider failure semantics and recovery proofs. |
| Chaos engineering | Likely excessive for current deployment scale; bounded failure injection may achieve the real need. |
| Hermetic testing | Strong relevance to deterministic/offline evidence tests. |
| Reproducible test fixtures | Already central to frozen evidence/case methodology. |
| Test pyramid / testing trophy | Useful heuristics only; should not become a quota. |
| Differential testing | Potentially relevant when comparing legacy vs native/Workspace projections or alternative analyzers. |
| Metamorphic testing | Potentially useful for evidence transformations with invariants under controlled input changes. |

### Security, trust and software supply chain

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Threat modeling | Strong candidate because UpgradePilot ingests untrusted public content and crosses provider/model/storage boundaries. |
| Trust boundary | Already fundamental even when not always named explicitly. |
| Least privilege | Relevant to GitHub credentials, filesystem and future deployment. |
| Secure-by-default | Relevant to authentication modes, no mutation and explicit refusal behavior. |
| Input validation | Strongly present in typed/provider/report boundaries. |
| Sandboxing | Potentially relevant if target code/model/tool execution expands; not automatically needed for read-only text processing. |
| Secret management | Relevant to GitHub/model/service credentials; current scope is limited. |
| SBOM | Relevant to software supply-chain awareness, but not automatically needed in the product's own runtime yet. |
| SLSA / build provenance | Potential future release/supply-chain hardening; distinguish from UpgradePilot's evidence provenance. |
| Dependency pinning / lockfiles | Operational/build reproducibility concern worth inspecting separately. |
| Vulnerability scanning | Generic scanner behavior is explicitly outside the Charter; project-dependency scanning may still be a development-security practice. |
| Secure Software Development Lifecycle (SSDLC) | Some practices exist; formal adoption would require a broader process judgment. |

### Delivery, API and compatibility engineering

| Concept | Initial UpgradePilot relation |
| --- | --- |
| CI | Already substantial and also a product evidence domain. Keep internal CI separate from analyzing target-repository CI. |
| Continuous Delivery | Not yet established merely because CI exists. |
| Continuous Deployment | Likely not relevant until a deployable service exists. |
| Release engineering | Underdeveloped compared with product internals; potentially important before portfolio/public distribution claims. |
| Semantic Versioning (SemVer) | Relevant to public package/API contracts if UpgradePilot begins formal releases. |
| API versioning | Relevant to stable external interfaces; current CLI/report/native schemas have different versioning responsibilities. |
| Compatibility policy | Already relevant to saved schemas and Python/package support. |
| Deprecation policy | May become necessary once public consumers depend on interfaces. |
| Migration strategy | Already materially relevant to Workspace/legacy consumer cutover. |
| Canary release | Probably premature for current deployment model. |
| Blue-green deployment | Probably outside current deployment needs. |
| Rolling deployment | Probably outside current deployment needs. |
| Clean install / packaging verification | Already an explicit proof concern and should be kept distinct from source-tree tests. |

### Engineering governance and decision process

| Concept | Initial UpgradePilot relation |
| --- | --- |
| ADR (Architecture Decision Record) | Already used and appropriately scoped to consequential structural decisions. |
| RFC | Could be useful for collaborative proposals, but may duplicate current plans/proposals in a single-owner project. |
| Design document | Already effectively represented by plans/design reviews; naming/formality should follow responsibility need. |
| Technical specification | Strongly present and explicitly owned under `docs/specifications/`. |
| Runbook | Potentially useful for repeatable operations/diagnostics once operational procedures stabilize. |
| Playbook | Similar to runbook but broader response guidance; may overlap existing operating/diagnostic guides. |
| Postmortem | Potentially useful after material incidents/failures; do not create incident ceremony for ordinary debugging. |
| Technical debt | Already tracked in multiple forms; classification could be sharpened. |
| Architecture debt | Useful subset when staged architecture/migration obligations remain. |
| Decision log | Current ADRs/working memory already provide parts of this responsibility. |
| Ownership / CODEOWNERS | Conceptually relevant; formal GitHub CODEOWNERS may be unnecessary in a one-owner repository until collaboration changes. |

### AI/agent-specific engineering and evaluation

| Concept | Initial UpgradePilot relation |
| --- | --- |
| Human-in-the-loop | Core fit: final maintainer judgment is intentionally retained. |
| Offline evaluation / evals | Strongly present in controlled experiments/comparisons. |
| Online evaluation | Not yet a natural fit without deployed operational usage. |
| Grounded generation / retrieval grounding | Highly relevant to semantic experiments; existing evidence shows grounding alone does not guarantee entailment. |
| Model/prompt/version tracing | Relevant to reproducibility and semantic-method identity; current retention is incomplete in normal user output. |
| LLM-as-judge | Must not be confused with independent adjudication; potentially useful only under a validated bounded role. |
| Multi-agent architecture | Previously explored conceptually; no automatic advantage or adoption from adding roles. |
| Guardrails | Relevant, but deterministic semantic/evidence owners should remain distinguishable from model prompt constraints. |
| Hallucination detection | Better framed as supported-claim/entailment validation for this product than a generic detector. |
| Red teaming | Potentially useful for model/evidence/adversarial-input boundaries if a concrete risk model is defined. |
| Model governance | Relevant only to admitted model-backed product roles; experimental local-model use alone does not require enterprise ceremony. |

## Cross-term questions to keep alive

These questions should influence multiple term analyses:

- Which current mechanisms are **real implementations of common engineering concepts**, and which only look similar superficially?
- Where would adopting a standard name improve communication, onboarding, career transfer and architecture reasoning without forcing a rewrite?
- Where are we carrying bespoke machinery because the evidence/provenance domain genuinely needs stronger semantics than a generic pattern provides?
- Which missing practices would materially improve **product usefulness**, not merely internal neatness?
- Which practices are valuable for **production-oriented proof** before any claim of production readiness?
- Which concepts become justified only when the deployment model changes from local/single-user CLI toward a persistent service?
- Which mechanisms would threaten the Charter by turning UpgradePilot into a generic CI/code-review/agent/MLOps platform?
- Which staged migration debts should be understood through established concepts (for example Strangler migration, schema evolution, optimistic concurrency) rather than inventing new project-specific vocabulary?
- Which concepts are especially valuable for Ali's transferable engineering understanding even when we decide **not** to adopt them?

## Per-term record template

Append a compact section when we actually study a term:

```text
### <Term>

Status: ORIENTED / ANALYZED / VERIFIED / DECISION-CANDIDATE / CLOSED
Repository horizon: <commit/ref checked>

WHAT:
WHY:
PROJECT MAPPING:
CURRENT EVIDENCE:
DISTINCTION FROM NEARBY TERMS:
BENEFIT / COST / FAILURE MODES:
TRIGGER OR REJECTION CONDITION:
DISPOSITION CANDIDATE:
UNRESOLVED QUESTIONS:
LEARNING TAKEAWAY:
```

Do not turn the record into a transcript. Preserve changed understanding and evidence, not every conversational step.

## Final synthesis obligation

At the end of this branch study, produce a cross-term decision matrix with at least:

- concept;
- whether it already exists in UpgradePilot;
- whether current naming is accurate;
- actual product problem it solves;
- disposition;
- evidence/trigger;
- required owner if promoted;
- likely implementation or migration cost;
- proof required before claiming adoption.

Possible outcomes include **no code change**. A useful result may simply be a more accurate mental model and terminology map. Any recommended product change must be reconciled against then-current `main`, the Charter, live `MEMORY.md`, applicable plans/specifications/ADRs, and the active Learning-Only/engineering mode before mutation.