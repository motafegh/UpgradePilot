# UpgradePilot Documentation and Decision Map

This is the durable navigation entry point for accepted project knowledge under `docs/` and for the repository artifact types that feed it.

Its purpose is **findability and ownership**, not live-state tracking. `../MEMORY.md` remains the sole owner of the current project position and immediate continuation.

## 1. Where to look

Use the owner that matches the question.

| Question / responsibility | Canonical owner |
|---|---|
| What product are we building, for whom, inside what boundary, with what claim limits? | [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md) |
| What route/stage gates govern delivery? | [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md) |
| What is the live project position, latest material verification, blocker, and next action? | [`../MEMORY.md`](../MEMORY.md) |
| What stable trust/evidence/representation/failure invariants must admitted behavior preserve? | [`specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`](specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md) |
| What are the accepted technical impact/applicability/investigation/stopping semantics? | [`specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md`](specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md) |
| What prevents fixture-specific/manual interpretation from masquerading as product capability? | [`specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md`](specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md) |
| What naming/terminology standard applies? | [`specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md`](specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md) |
| What consequential implementation/structural method has been accepted? | [`architecture/`](architecture/) and the relevant ADR |
| What does a bounded implementation responsibility do next, prove, and stop at? | relevant file under [`../plans/`](../plans/) |
| What does the product actually do today? | `../src/upgradepilot/`, `../tests/`, reproducible commands/outputs, relevant environment evidence |
| What mature whole-system responsibilities are visible or still open? | [`../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md`](../proposals/UPGRADEPILOT_MATURE_SYSTEM_HORIZON.md) — non-controlling orientation only |
| Why/how was a dated conclusion reached? | relevant record under [`../working-memory/`](../working-memory/) and, where applicable, [`../audits/`](../audits/) / [`../product-simulation/`](../product-simulation/) |
| What reusable understanding/teaching snapshot exists? | [`../learning/`](../learning/) |

## 2. Accepted-knowledge versus history

UpgradePilot intentionally keeps **canonical accepted knowledge** separate from the **historical reasoning/evidence trail**.

```text
working-memory / audit / simulation
"How and why did we reach this conclusion?"
        ↓ promotion when sufficiently stable and accepted
canonical responsibility owner
"What is the accepted rule/semantic/method now?"
```

Historical records are not rewritten merely because a decision is promoted. They preserve the evidence, alternatives, pressure tests, chronology, and reasoning that produced the accepted result.

Future sessions should normally load the canonical owner first and consult dated history only when a provenance, comparison, challenge, or unresolved-design question requires it.

## 3. Durable decision-promotion lifecycle

A substantial discussion or investigation may begin in a dated working-memory record, audit, simulation, or proposal. Once a conclusion is accepted and expected to guide unrelated future sessions, classify it by responsibility and promote it to the durable owner.

```text
DISCUSSION / INVESTIGATION / PRESSURE TEST
        ↓
DATED EVIDENCE OR REASONING
        ↓
CONCLUSION BECOMES STABLE + ACCEPTED + REUSABLE
        ↓
CLASSIFY BY RESPONSIBILITY
        │
        ├─ product mission / supported boundary / claim limit
        │      → PROJECT_CHARTER.md
        │
        ├─ framework-independent required behavior / invariant /
        │  product decision semantics
        │      → docs/specifications/
        │
        ├─ consequential implementation / structural method
        │      → docs/architecture/ ADR
        │
        ├─ bounded implementation / investigation sequence,
        │  proof obligations, stop line
        │      → plans/
        │
        ├─ reusable runtime / machine facts and re-check rules
        │      → ENVIRONMENT.md
        │
        ├─ security / privacy / authorization rule
        │      → SECURITY.md
        │
        ├─ learning / execution / debugging operating rule
        │      → OPERATING_GUIDE.md
        │
        ├─ still-unadmitted substantial future idea
        │      → proposals/
        │
        └─ live project position / continuation only
               → MEMORY.md
```

The promotion rule is not a requirement to create new artifacts for every conclusion. Prefer an existing owner and update it precisely. Create a new canonical file only when a distinct durable responsibility genuinely lacks an owner.

## 4. What remains in working-memory

`../working-memory/` remains the normal home for dated execution/validation evidence and detailed reasoning, including:

- investigation chronology;
- alternatives considered;
- pressure-test results;
- debugging incidents;
- implementation handoffs;
- one-run validation evidence;
- reasoning that may later justify a specification/ADR/plan change.

It is **not** the preferred long-term lookup location for a stable accepted rule that future unrelated sessions are expected to follow.

When a durable decision is promoted, the canonical artifact should link to the important historical evidence. The historical file need not be edited just to add a reverse link.

## 5. Specification versus ADR versus horizon

Keep these three roles distinct.

### Specification

```text
What behavior/meaning/boundary must admitted implementation preserve?
```

A specification is framework-independent and controlling within its responsibility.

### ADR

```text
What consequential implementation or structural method did we choose to satisfy an admitted responsibility?
```

An ADR does not prove implementation and should not be used to store every product-domain semantic rule.

### Mature-system horizon

```text
What whole system might UpgradePilot grow toward,
how do today's slices fit, and what remains open?
```

The horizon is intentionally evolving and non-controlling. It may contain accepted, partially designed, open, and experimental responsibilities side by side. Accepted semantics should be linked back to their canonical owner rather than becoming authoritative merely because they appear in the horizon.

## 6. Current canonical specification surface

See [`specifications/README.md`](specifications/README.md) for the full specification index. The high-level split is:

```text
CORE PIPELINE + CONTRACT
→ trust / provenance / representation / failure invariants

PRODUCT DECISION MODEL
→ candidate / applicability / coverage / investigation / stopping semantics

MINIMUM USEFUL GENERALITY
→ acceptance standard for variable-input automated responsibilities

NAMING CLARITY
→ project-wide engineering terminology standard
```

## 7. Architecture navigation

See [`architecture/README.md`](architecture/README.md) for accepted ADRs and architecture-decision responsibilities.

The source architecture follows responsibility ownership rather than generic layered folders. A shared primitive is admitted only when its meaning is genuinely identical across callers; source/provider/domain-specific meaning remains with the responsible consumer.

## 8. Maintenance rule

When a future session discovers an important accepted decision only in old working-memory, do not copy it into a new summary file by default.

Instead:

1. identify whether a canonical owner already exists;
2. verify the conclusion is still accepted and compatible with controlling sources/current implementation;
3. update the existing canonical owner, preserving a provenance link;
4. create a new durable owner only if the responsibility is genuinely distinct;
5. update this navigation map only when artifact ownership/navigation changes;
6. update `../MEMORY.md` only if the live project position or continuation also changed.

This keeps UpgradePilot's standing context small, searchable, and authoritative without erasing the reasoning history that produced it.