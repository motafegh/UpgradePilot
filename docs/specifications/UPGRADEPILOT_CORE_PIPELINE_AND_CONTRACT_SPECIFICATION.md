# UpgradePilot Core Invariants

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Stable project-wide framework-independent product/evidence invariants plus implementation-retention and cross-layer ownership constraints for admitted UpgradePilot behavior  
**Implementation decisions:** ADRs under `../architecture/`  
**Actual behavior:** Source, tests, commands, outputs, and environment

## 1. Boundary and activation separation

This specification defines stable product/evidence behavior that admitted implementation must preserve and the framework-independent retention/ownership constraints that determine whether a material implementation mechanism is justified to remain or be repeated across layers.

It does not:

- define project operation or learning procedure;
- select a framework, database, service, cloud, provider, or deployment method;
- define live progress, selected plan, latest commit, or next action;
- activate a requirement merely because it appears here;
- preserve obsolete implementation contracts inside the active normative surface solely for historical traceability.

`../../MEMORY.md` is the sole owner of live project position. The selected plan determines which applicable responsibility is currently being implemented/proven. ADRs choose consequential mechanisms; source/tests and observed evidence establish implemented truth.

The detailed historical M2 trusted-case contract formerly retained in this specification now lives as a non-controlling archive reference:

- [`../../archive/2026-08-04_RETAINED_M2_TRUSTED_CASE_CONTRACT.md`](../../archive/2026-08-04_RETAINED_M2_TRUSTED_CASE_CONTRACT.md)

That archive supports traceability and comparison; it is not part of the active contract unless a later accepted artifact independently readmits a requirement.

## 2. Normative language

- **MUST** — required for acceptance when the requirement applies to the admitted responsibility.
- **MUST NOT** — prohibited within the admitted responsibility.
- **SHOULD** — expected unless evidence justifies an exception.
- **MAY** — permitted.

## 3. Stable project invariants

| ID | Requirement |
|---|---|
| `FLOW-001` | Implemented responsibilities MUST reconnect to one continuous dependency-update decision flow. |
| `RAW-001` | Source/raw form MUST remain separate from normalized/trusted form. |
| `RAW-002` | Normalization or interpretation MUST NOT overwrite or mutate supplied raw evidence. |
| `OBS-001` | Observation, interpretation, evidence quality, and decision MUST remain distinct. |
| `SNAP-001` | Material evidence and conclusions MUST identify the repository and PR revision to which they apply. |
| `PROV-001` | Material normalized evidence and factual report claims MUST resolve to origin, time/revision, and transformation identity when that responsibility is admitted. |
| `STATE-001` | Missing, inaccessible, stale, conflicting, invalid, rejected, unsupported, and not-applicable states MUST remain distinguishable where applicable. |
| `TRUST-001` | Trusted application contracts MUST NOT silently coerce material values. |
| `FAIL-001` | Invalid caller input, malformed source data, unavailable evidence, and internal defects MUST remain different failure categories. |
| `REP-001` | Application, persistence, and report representations MUST NOT be assumed identical. |
| `VERSION-001` | Persisted or externally serialized contracts MUST become version-aware before compatibility matters. |
| `ACT-001` | Only responsibilities admitted by controlling project scope and the selected plan MAY be represented as accepted product behavior. |
| `PROOF-001` | A plan, specification, or accepted ADR MUST NOT be treated as proof of implementation or learner ownership. |
| `JUST-001` | Existing implementation, current use, passing tests, comments, historical design, prior effort, or compatibility with code that is itself under review MUST NOT by itself justify retaining a field, check, type, helper, abstraction, metadata value, dependency, or other mechanism. A material retained mechanism MUST trace to a current admitted product responsibility, proof need, material risk, or real compatibility/external obligation. |
| `JUST-002` | Retention reasoning MUST NOT be circular. A downstream consumer's dependence on an upstream field or mechanism does not establish that the upstream mechanism is necessary when that downstream dependence is itself being reviewed. |
| `JUST-003` | When a simpler mechanism satisfies the same current admitted responsibility and proof boundary without losing required behavior, risk control, or real compatibility, the implementation SHOULD prefer the simpler mechanism and remove or narrow obsolete propagation, validation, abstraction, or ceremony. |
| `JUST-004` | Before retaining or adding a material downstream check, field, transformation, metadata propagation, compatibility surface, or other mechanism whose purpose depends on an upstream fact or relationship, the implementation MUST trace the normal producer → integration → consumer path and identify the earliest sufficient owner of that proposition. A proposition being real does not by itself justify re-establishing it at every downstream layer. Repetition requires an independent supported boundary, independently combinable inputs, a distinct domain/cross-object proposition, or a material risk not already controlled upstream. |
| `JUST-005` | The mere possibility of directly calling an internal function, manually fabricating test fixtures, or misusing objects outside the admitted normal flow MUST NOT by itself justify duplicate production validation or compatibility behavior. If an alternate invocation/composition pattern is intended to be supported, that boundary MUST be explicitly admitted as a responsibility/contract and tested as such. |
| `AUTH-001` | A model-derived claim MUST retain its authority level and transformation identity when crossing grounding, orchestration, and decision boundaries. |
| `AUTH-002` | Literal source grounding MUST NOT be represented as independent corroboration or semantic truth. |
| `AUTH-003` | An uncorroborated model-derived claim MUST NOT independently justify a less cautious recommendation. |
| `AUTH-004` | Absence of a model-derived claim MUST NOT be treated as evidence that no relevant risk exists. |
| `AUTH-005` | Model output MUST NOT assign its own authority level, evidence state, or permitted decision effect. |
| `CLAIM-001` | A statement extracted from external evidence MUST be represented as an attributed source claim, not independently confirmed truth. |
| `CLAIM-002` | Accepting an evidence item for processing establishes only its eligibility/recorded state; it MUST NOT establish that every statement inside it is correct. |
| `CLAIM-003` | Distinct contradictory source claims MUST remain visible for later conflict handling rather than being silently collapsed or guessed away. |
| `GROUND-001` | Grounding MUST establish correspondence between an extracted claim and cited source content; it MUST NOT be represented as corroboration. |
| `CORR-001` | Corroborated, contradicted, irrelevant-to-the-case, and not-yet-corroborated states MUST remain distinguishable when cross-source assessment is admitted. |
| `CONTENT-001` | External content MUST NOT redefine extraction policy, output authority, or permitted decision effects; instruction-like wording alone MUST NOT erase or invalidate preserved source evidence. |

The `JUST-*` invariants create a retention burden, not a deletion bias. They require the project to ask what a mechanism currently earns before keeping it. Existing callers and tests are important migration and regression evidence, but they are not architectural authority. Removal still has to preserve every independently justified responsibility, proof boundary, risk control, and real compatibility obligation.

For cross-layer mechanisms, retention review must be **end-to-end rather than file-local**. Classifying a check as “relational,” “defensive,” or “currently useful” is not sufficient: trace where the proposition first becomes guaranteed in the admitted normal flow, determine whether the downstream layer is independently responsible for distrusting/recombining those inputs, and retain another check only when that second ownership has its own current justification.

## 4. Validation and transformation order

Where applicable, implementation must preserve this conceptual order:

1. retain supplied raw form or durable reference;
2. parse source format without inventing meaning;
3. validate required shape, fields, and accepted runtime types;
4. perform only declared meaning-preserving normalization;
5. enforce field and cross-field semantic invariants;
6. create the complete trusted object only after required checks pass;
7. represent external evidence quality/availability separately from caller-input or internal-code failures.

A framework MAY combine internal mechanics, but observable behavior and tests must preserve these distinctions.

## 5. Failure and stopping classes

Keep materially different outcomes distinct where the admitted responsibility can produce them:

1. reject caller/request input;
2. reject a proposed trusted record/transformation;
3. preserve a missing, inaccessible, malformed, conflicting, stale, unsupported, or otherwise degraded external-evidence state while continuing;
4. degrade the result because evidence quality is insufficient for a stronger conclusion;
5. abstain from a decision or semantic conclusion;
6. fail the run because trustworthy continuation is impossible;
7. surface an internal implementation defect separately from expected source/evidence failure.

The selected plan/specification for a responsibility may refine these categories with named states. It must not collapse them merely for implementation convenience.

## 6. Representation and authority discipline

When a responsibility crosses representation boundaries:

```text
source/raw evidence
→ parsed/normalized evidence
→ attributed claim or deterministic interpretation
→ grounded/corroborated/conflicted state where admitted
→ finding or decision input
→ bounded decision/output
```

Each boundary must preserve enough identity to explain what changed, which actor/method performed the transformation, and what authority the resulting record is allowed to carry.

Schema-valid output from a parser, framework, or model is not automatically trustworthy semantic evidence.

### 6.1 Evidence reports and saved-result boundaries

When an evidence-report responsibility is admitted, the following representation requirements apply. They elaborate the Charter's decision-report promise and `PROV-001`, `REP-001`, `VERSION-001`, and failure/authority invariants; they do not select a storage mechanism or prove implementation.

- A report MUST identify the exact investigated update and preserve material findings, supporting evidence references, their proof strength, and scope. Source revisions and executed revisions MUST remain distinct when they differ.
- Material unknowns MUST identify the unresolved proposition, available evidence, reason the evidence does not close it, and decision consequence where established. Unsupported analysis, unavailable evidence, an unperformed check and contradictory evidence MUST NOT collapse into one unexplained unknown.
- Presentation MUST NOT establish new evidence, discard material uncertainty to make a result look complete, or promote an archived/manual conclusion into normally acquired product evidence. If justified investigation remains necessary, explaining uncertainty does not discharge that investigation responsibility.
- Recommendations and action availability remain owned by the Maintainer Action Synthesis specification. A report MUST NOT bypass its permission conditions by renaming an action as advice or a next check. Failure to form an investigation result MUST NOT become semantic abstention.
- Human and saved projections MUST preserve the same material meanings and evidence links. A saved result MUST declare its identity/version, retained-content boundary and missing provenance; source references alone MUST NOT be described as preserved raw evidence.
- Reopening a saved result MUST preserve its recorded observation/revision context and explain that no fresh acquisition or validation occurred. It MUST NOT silently make live requests, execute content, infer current validity, or claim deterministic replay from an output record alone.
- Compatibility, malformed-content and integrity outcomes MUST remain explicit. A content digest can establish consistency with recorded bytes, not independent source authenticity or semantic truth. These checks do not elevate external content into instructions or authority.

### 6.2 Foreseeable evidence consumers and AI contributions

Representation design MUST consider specifically identified investigation consumers as well as the human report. This includes admitted model interpretation and credible forthcoming impact-discovery, evidence-gap investigation or explanation responsibilities; it does not admit those capabilities by itself.

- A report is a projection of investigation knowledge, not the maximum evidence/context a future investigator may inspect. Do not require models or agents to reconstruct structured findings, uncertainty, identity or provenance by parsing rendered prose when the owning structured evidence is available.
- Before fixing an external representation or discarding material evidence, identify the named consumer, its required facts/source context, what remains retained or recoverable, and the consequence of omissions. Preserve exact source identity and available relevant content; where recovery is impossible or contingent on future retrieval, declare that limitation. A reference or digest is not a substitute for missing content.
- Broader source access and trusted result admission are different responsibilities. A model may need exact passages or richer repository context; access to that context does not establish applicability, completeness, semantic truth or action permission. Existing domain/synthesis and security owners remain controlling.
- Keep acquired evidence, model/agent proposals, assessment results and report presentation distinguishable. Material AI contributions MUST retain available input/source and method/model identity at the admitted proof boundary, with explicit missing provenance rather than reconstructed metadata. Framework/provider names must not define domain evidence semantics.
- Follow-up investigation MUST distinguish newly acquired evidence and changed conclusions from the earlier recorded result. Explicit continuation may retrieve/reassess evidence when authorized; offline report reopening remains a different operation. Missing inputs or tool/observation history MUST NOT be represented as replayable or resumable state.

These requirements favor justified information boundaries and explicit retention choices, not speculative frameworks, universal raw capture, or generic agent infrastructure. Reassess retention when a concrete consumer or proof obligation exposes a material missing premise.

### 6.3 Source-association bases and permitted effects

When package-to-source exploration is admitted, the association basis MUST remain explicit across acquisition, interpretation and presentation. Publisher-declared repository links, registry-reported publisher provenance and pinned repository text establish different propositions; they MUST NOT be substituted for one another inside a stronger evidence contract.

- Source examination eligibility and eligibility for a trusted release/claim contract MUST remain separate. A declared link may support bounded inspection and attributed proposals under an admitted method without establishing attested origin or package-to-commit build correspondence.
- Consistent declarations under the same publisher's control MUST NOT be presented as independent corroboration. Sampling a distribution MUST retain that sample's identity and coverage limits; a digest establishes correspondence to recorded distribution bytes, not source authenticity or semantic truth.
- Missing provenance MUST remain distinguishable from conflicting, malformed, unsupported or inaccessible provenance. A weaker association MUST NOT erase an adverse result or silently convert it into a stronger success.
- Every derived proposal MUST preserve association basis, exact examined source scope and unresolved correspondence premises. Pinning a tag/commit/file MUST NOT establish that an installed or published distribution was built from it, nor establish target applicability or action permission.

These invariants do not admit a new source policy or semantic role by themselves. The selected method/plan owns permitted examination effects and implementation scope; existing stronger contracts retain their meanings.

### 6.4 Canonical investigation recovery and explicit continuation

When canonical investigation recovery is activated, a durable checkpoint MUST declare one coherent investigation boundary: lineage, exact repository/PR/base/head/dependency transition, canonical revision and supported representation/semantic-version identity. Recovery MUST identify the persistence boundary; it MUST NOT imply preservation of later uncheckpointed activity. Checkpoint cadence and retention duration require an explicit implementation contract before durability is claimed.

The checkpoint MUST preserve the material dependency closure needed to explain and continue that boundary: native identity/owner/scope/provenance and retained content or explicit recovery limitations; material proposal/admission and evaluation inputs/results; candidate/proposition lineage and reasons; discovery objectives/coverage; investigation needs; request/admission/attempt/observation/problem relationships; procedural termination, stopping proposals and adequacy assessments or unsupported/failed outcomes. Material views and available method/model/configuration identity MUST be retained at their admitted proof boundary, with missing provenance explicit. Reference-only content MUST NOT be labeled exact retained evidence. No universal raw capture, hidden model reasoning or secret retention is required or authorized.

Recovery MUST preserve authority, assessment basis, open work and failed/unsupported/stale/conflicted distinctions. It MUST NOT convert proposals into assessments, omitted evidence into absence, ambiguous attempts into successes/negative observations, or procedural completion into adequate investigation. Completed observations absent from the declared boundary MUST NOT be invented.

Supported representation, internal identities/references and integrity/coherence MUST be validated before recovered state is presented as canonical. Torn/invalid boundaries MUST NOT be silently merged or repaired into authoritative truth. A separately validated earlier boundary MAY be restored with explicit lost-progress limits. Incompatible versions, broken material references, missing required content and integrity problems MUST have explicit outcomes. Readable historical material MAY remain inspectable with declared limits; it MUST NOT be advertised as fully resumable where gaps block the next obligation.

Recovery MUST be offline historical restoration. It MUST NOT issue requests, invoke models/evaluators, execute content, retry work, rebase targets or infer present source validity. Offline report opening remains a separate projection operation and MUST NOT reconstruct absent canonical state.

Explicit continuation MUST distinguish fresh facts and state changes from the checkpoint. Before using recovered records/requests/assessments as current, validate the exact target and material identity/premise/scope/method/authority bindings; logical revision inequality alone is not staleness. Changed targets cannot be silently rebound. Missing methods/capabilities and material retention gaps MUST remain explicit and block affected operations without discarding unaffected evidence or manufacturing assessments.

Pending, interrupted and completion-unknown attempts MUST remain distinguishable from unperformed requests and completed observations. Reconciliation/retry requires explicit continuation and current host admission under the capability's effects/authorization contract. Historical admission MUST NOT independently grant present execution authority or imply exactly-once execution. Duplicate results MUST be identified against request/attempt/observation identity and checked for contradictory content before ingestion.

Recovered adequacy/synthesis conclusions MUST retain their historical basis. Material new evidence, discovery obligations, target/premise changes or newly feasible decision-critical checks require validity review and affected successor evaluation by the admitted owner before current use. Recovery cannot self-authorize stop/action; absent current adequacy/evaluation methods preserve unsupported evaluation rather than justified stop.

Recovery promises MUST be evidenced through interruption, coherent restoration, missing/corrupted/incompatible dependencies, ambiguous attempts, target change and explicit continuation tests. Recovery does not discharge the separate replay responsibility: replay requires its own admitted re-execution boundary, retained inputs/method identities, equivalence criteria and executable proof independently of live source availability. Recovery does not establish deterministic replay, semantic correctness, current compatibility, discovery completeness or action permission.

## 7. Specialized specification relationships

This core specification defines the stable trust/evidence/representation/failure invariants shared across admitted responsibilities and the project-wide implementation-retention/ownership constraints that apply when a material mechanism is added, repeated, or kept.

Two accepted specifications further constrain particular cross-product concerns:

- [`UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) — technical impact-candidate, applicability, coverage/negative-inference, discriminating-investigation, result-feedback/lineage, stopping, and later-synthesis-boundary semantics;
- [`UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) — acceptance rules for variable-input automated responsibilities so known fixtures, caller-supplied interpretations, or per-case rules do not masquerade as automated capability.

The relationship is complementary:

```text
CORE INVARIANTS
→ how evidence/trust/representation/failure boundaries must behave
→ why an implementation mechanism is allowed to remain active at all

PRODUCT DECISION MODEL
→ how technical concerns/applicability/investigation knowledge must be represented and advanced

MINIMUM USEFUL GENERALITY
→ what variation/generalization evidence is required before an automated method is accepted
```

None of these specifications by itself proves implementation or activates a responsibility outside the selected plan.

## 8. Historical relationship

Historical M2 contracts, tests, and implementation remain useful evidence for provenance, comparison, and learning. They do not become active requirements merely because they once existed or passed tests.

Consult the archived M2 contract only for a named historical comparison or when a later responsibility explicitly considers readmitting one of its ideas.

## 9. Change control

Change this specification only when stable project-wide invariants, validation/authority boundaries, representation discipline, failure semantics, or implementation-retention discipline change.

Do not update it for:

- one test pass/failure;
- implementation progress;
- session completion;
- stage or plan selection;
- latest commit or exact continuation;
- file reorganization that preserves the contract;
- historical traceability that can be represented through a non-controlling archive/evidence link.

Reassess an invariant when real evidence shows it is wrong, impossible to preserve without material loss, or in direct conflict with a newly admitted responsibility that cannot be represented safely under the existing rule.
