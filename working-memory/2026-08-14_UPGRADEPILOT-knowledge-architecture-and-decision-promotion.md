# UpgradePilot Knowledge Architecture and Decision-Promotion Correction

**Date:** 2026-08-14  
**Type:** Dated governance / knowledge-architecture implementation record  
**Live-state authority:** `../MEMORY.md` only  
**Product behavior:** No runtime product capability is added or proven by this record

## Why this correction was needed

During the S008/S011 target-environment transfer discussion, comparison of `src/upgradepilot/ci/workflow_commands.py` and `src/upgradepilot/target/artifact_environment.py` exposed both a source-architecture issue and a project-knowledge issue.

The source issue was that materially overlapping GitHub Actions workflow-reading mechanics had begun to appear in separate responsibilities even though their final domain questions differ.

The knowledge issue was more foundational: UpgradePilot already had strong accepted whole-product decision semantics from the progressive A→B→C reconciliation and AUDIT-003, but many of those durable decisions were discoverable primarily through long dated working-memory/audit records. The repository had no explicit promotion lifecycle telling future sessions when accepted historical reasoning must move to a canonical owner.

That created a predictable failure mode:

```text
important discussion
→ dated working-memory
→ accepted decision
→ more working-memory
→ future session must rediscover/reconstruct the accepted rule
```

The correction therefore addresses durable knowledge ownership **before** performing the next source-architecture reconciliation.

## Sources reviewed

The correction was grounded against the existing repository ownership model and accepted design evidence, especially:

- `AGENTS.md`;
- `docs/specifications/README.md`;
- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`;
- `docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`;
- `docs/architecture/ADR-0007-responsibility-based-python-subpackages.md`;
- `plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`;
- `working-memory/2026-08-06_UPGRADEPILOT-product-decision-model-reconciliation.md`;
- `audits/2026-08-10_AUDIT-003_post-conversation-c-product-decision-model.md`;
- `working-memory/2026-08-12_B2-responsibility-shaped-expansion-decision.md`;
- `working-memory/2026-08-13_B2-target-evidence-boundary-adoption.md`;
- `proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md`;
- active CI/target/impact/orchestration source needed to expose the architectural pressure.

## Accepted knowledge-architecture decision

### 1. Canonical Product Decision Model specification

Created:

`docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`

This is now the normal durable owner for accepted framework-independent semantics covering:

- technical impact-candidate formulation;
- preservation of component evidential status;
- candidate-specific applicability;
- proposition/path composition;
- evidence coverage, path-model coverage, and candidate-discovery coverage;
- open-world/negative-evidence discipline;
- evidence identity/scope/composition protections;
- static declaration/configuration evidence versus runtime execution/success evidence;
- deterministic versus semantic authority;
- discriminating-investigation selection;
- epistemic value versus UpgradePilot execution admissibility versus maintainer-facing recommendability;
- investigation validity;
- result feedback and candidate refinement/supersession lineage;
- investigation stopping;
- the boundary to later overall sufficiency/policy/maintainer-facing synthesis.

The specification promotes durable accepted A/B/C semantics without rewriting the dated records that explain how those decisions were reached.

### 2. Documentation / decision navigation map

Created:

`docs/README.md`

It provides one findable map from a question/responsibility to its canonical owner and defines the durable promotion lifecycle:

```text
discussion / investigation / pressure test
→ dated reasoning/evidence
→ conclusion becomes stable + accepted + reusable
→ classify by responsibility
→ update canonical owner
```

The promotion rule explicitly prefers updating an existing owner over creating a new summary/artifact.

### 3. Working-memory remains historical reasoning/evidence

`working-memory/` remains the owner for dated execution/validation evidence, chronology, alternatives, debugging incidents, handoffs, and detailed reasoning.

It is not the preferred long-term lookup location for a stable accepted rule expected to guide unrelated future sessions.

Promotion does not erase history:

```text
canonical owner
→ what the accepted decision is now

working-memory / audit / simulation
→ why/how it was reached and what pressure evidence supported it
```

Historical records are not mass-edited merely to add reverse links after promotion.

### 4. Mature System Horizon remains non-controlling

`proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md` retains its existing role:

- whole-system orientation;
- design-discussion compass;
- reconciliation surface;
- mixture of accepted, partially designed, open, and experimental responsibilities.

It does **not** become the authority for accepted semantics or implementation methods.

Accepted semantics belong to specifications/Charter as appropriate; consequential methods belong to ADRs; live continuation belongs only to `MEMORY.md`.

### 5. ADRs remain implementation/structural decisions

The correction does not create an ADR merely to make the A→C reasoning model findable.

`docs/architecture/README.md` now makes the split explicit:

```text
framework-independent product decision semantics
→ specification

consequential implementation/structural method
→ ADR
```

A future source-architecture reconciliation may justify a new ADR, but only after the structural decision itself is sufficiently resolved.

## Governance/index updates applied

Updated:

- `AGENTS.md` — adds the documentation map and Product Decision Model specification as explicit responsibility owners; requires promotion of stable accepted conclusions; tells future sessions to load canonical owners before reconstructing decisions from historical records.
- `docs/specifications/README.md` — indexes the new specification and records the promotion relationship.
- `docs/architecture/README.md` — distinguishes product decision semantics from architectural methods and links the promotion map.
- root `README.md` — exposes `docs/README.md` and the Product Decision Model specification in the normal project-control navigation.

## New durable promotion rule

The governing rule is now:

> When a dated working-memory/audit/simulation/proposal record reaches a stable, accepted, reusable conclusion that is expected to guide unrelated future sessions, update the canonical owner for that responsibility and retain the dated record as provenance. Do not create another summary merely because the original reasoning file is long.

This rule is deliberately classification-based rather than format-based.

Examples:

```text
stable product semantic/invariant
→ specification

consequential structural/method choice
→ ADR

bounded implementation sequence/proof/stop line
→ plan

live continuation
→ MEMORY.md

still-unadmitted future idea
→ proposal/horizon
```

## Architectural pressure preserved for the next reconciliation

The knowledge correction does not resolve the source architecture itself. It preserves the concrete next design problem:

```text
exact GitHub workflow evidence
→ shared normalized workflow-definition structure?
        ├─ CI interpretation
        └─ target-environment interpretation
```

Current source inspection exposed at least these pressures:

1. `ci/workflow_commands.py` and `target/artifact_environment.py` duplicate material static workflow-reading mechanics such as job discovery, run-command extraction, direct pip/requirements recognition, and path normalization.
2. Their **domain conclusions are not the same**: CI owns successful dependency exercise; target owns scoped environment facts/formation evidence.
3. Static workflow declaration/configuration evidence must remain distinct from actual runtime execution/success evidence.
4. A shared structural parser should not automatically become a universal GitHub Actions execution engine.
5. Multi-job preservation belongs more naturally to structural reading than to a parser-level rejection; domain consumers may still remain unresolved when they cannot safely select/compose jobs.
6. Direct dependency-installation recognition may be another shared semantic primitive, but its exact owner/contract requires reconciliation before refactoring.
7. The second mechanism also pressures `investigation.py` toward heterogeneous mechanism-result orchestration rather than indefinitely adding one field family per mechanism.
8. Existing `impact/applicability.py` is a positive precedent: it shares semantics that are genuinely identical while mechanism-specific candidate/evaluator logic remains separate.

These are **architecture-reconciliation inputs**, not accepted implementation structures yet. In particular, no `github/workflow_definition.py`, generic environment model, universal impact engine, workflow AST, planner, graph, or plugin framework is authorized by this record.

## Implementation commits in this knowledge correction

At the time this record was created, the knowledge-architecture changes had been applied directly to `main` through these commits:

- `e8806856dfcf19d93fa9eaa12c5dd53270357b9b` — add canonical Product Decision Model specification;
- `97b068aaedac050604401d7b391a31b82223678e` — add documentation/decision navigation map;
- `c1498d9b1b5e563c6356bea66e2f54320ad60f44` — index the canonical Product Decision Model specification;
- `b9202457448734e1bfe5cbc8ec7a70db94bab1dc` — route durable decision knowledge through canonical owners in `AGENTS.md`;
- `cd05af94c76c0334beb17e14848088c78790b07a` — expose the new navigation from the root README;
- `47f2a2c56dc69c99c49819dc8c5a333f8061f2a6` — link architecture-decision ownership to the canonical product decision semantics.

No product source or test behavior changed in those commits.

## Next project action implied by this correction

Before adding another target-artifact-environment capability, perform a **cross-responsibility source-architecture reconciliation** using the newly canonical knowledge surface plus current source/tests.

The immediate architecture checkpoint should answer:

1. What exact raw/normalized GitHub workflow structure is genuinely shared by CI and target-environment consumers?
2. What must remain CI-specific versus target-specific?
3. What is the correct static-definition versus runtime-execution evidence boundary?
4. Which duplicate helpers should be promoted to a neutral owner, and which duplication is semantically justified?
5. How should the second technical mechanism join application orchestration without producing mechanism-field sprawl or a speculative universal engine?
6. Does the resulting structural decision justify a new ADR or an amendment/supersession of an existing architecture decision?

Only after that reconciliation should source refactoring or the next target-environment feature increment resume.
