# UpgradePilot Core Invariants

**Status:** Accepted controlling technical specification  
**Owner:** Ali Rajabi  
**Responsibility:** Stable project-wide framework-independent invariants for admitted UpgradePilot product behavior  
**Implementation decisions:** ADRs under `../architecture/`  
**Actual behavior:** Source, tests, commands, outputs, and environment

## 1. Boundary and activation separation

This specification defines stable behavior that admitted implementation must preserve.

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

## 7. Specialized specification relationships

This core specification defines the stable trust/evidence/representation/failure invariants shared across admitted responsibilities.

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