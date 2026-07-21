# Temporary Work Package 05 — Technical Specification and Repository Entrypoints

**Status:** Blocked until Work Package 04 passes  
**Sequence:** 5 of 7  
**Primary repository:** `motafegh/UpgradePilot`  
**Dependency:** Canonical Career Work Packages 01–04  
**Stop boundary:** Finish UpgradePilot-local technical/document responsibility changes before refreshing the Career snapshot.

> This package improves technical traceability and simplifies UpgradePilot entrypoints without changing ADR-0002, current implementation authorization, capability claims, or product behavior.

## 1. Outcome

After this package:

- the core technical specification uses explicit requirement strength;
- important invariants have stable identifiers;
- proof obligations map to test/evidence categories;
- the technical specification owns behavior while ADR-0002 owns Pydantic-specific choices;
- raw preservation, parsing, normalization, validation and trusted-object creation have a clear order;
- README, `AGENTS.md`, `MEMORY.md` and working memory no longer duplicate live state or contract detail.

## 2. Files in scope

### Technical control

- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`
- `docs/architecture/README.md`
- `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md`
- other ADRs only when a direct boundary/status inconsistency exists

### Repository entrypoints and continuity

- `README.md`
- `AGENTS.md`
- `MEMORY.md`
- current working-memory file(s), only to clarify their role or remove false authority claims

Do not modify mirrored Career files or `docs/program/SOURCE.md` in this package.

## 3. Requirement language

Define and use consistently:

- **MUST** — required for acceptance;
- **MUST NOT** — prohibited;
- **SHOULD** — expected unless a documented reason exists;
- **MAY** — permitted.

Keep terms such as accepted, provisional and deferred for decision or maturity status, not requirement strength.

Do not mechanically rewrite every sentence. Apply normative keywords where requirement strength matters.

## 4. Stable requirement identifiers

Assign identifiers to important invariants and contract obligations, grouped by responsibility.

Illustrative scheme:

```text
PR-ID-001: Pull-request number must be a positive non-boolean integer.
SHA-001: Base and head revisions must contain 40 hexadecimal characters.
RAW-001: Normalization must not mutate supplied raw input.
PATH-001: Normalized changed-file paths must be unique.
ERR-001: Invalid input must produce structured failure evidence.
```

Rules:

- IDs must be stable after publication;
- one ID must identify one testable obligation;
- avoid identifiers for explanatory prose;
- group by responsibility rather than one global undifferentiated sequence;
- future tests and evidence may cite the IDs.

## 5. Contract-to-proof mapping

Add a concise traceability section such as:

| Requirement | Required proof category | Current implementation evidence |
|---|---|---|
| `RAW-001` | Non-mutation test | Pending or linked test |
| `SHA-001` | Representative valid and invalid cases | Pending or linked tests |
| `ERR-001` | Structured failure assertion | Pending or linked test |

The specification defines what proof is required. Actual source/tests/outputs and the tracker record whether proof exists.

Do not use the specification itself as evidence that behavior is implemented.

## 6. Specification and ADR boundary

### Technical specification owns

- externally observable contract behavior;
- strict validation requirements;
- undeclared-field handling requirements;
- trusted/raw separation;
- immutability requirements for trusted structures;
- adapter behavior;
- failure categories and structured evidence;
- proof obligations and milestone boundaries.

### ADR-0002 owns

- selection of Pydantic v2;
- `BaseModel` and configuration mechanisms;
- framework-specific validator strategy;
- major-version policy;
- framework trade-offs;
- reassessment triggers.

The specification may state that the accepted implementation decision is recorded in ADR-0002. It should not duplicate unnecessary Pydantic mechanics.

Review ADR-0002 conservatively. Preserve its accepted decision and rationale. Remove or narrow content only when it clearly duplicates specification-owned requirements without adding decision context.

## 7. Clarify the semantic processing order

Define the boundary and order among:

```text
raw preservation
→ source-format parsing
→ normalization
→ type validation
→ semantic validation
→ trusted-object creation
```

For every stage, identify:

- input responsibility;
- allowed transformations;
- output responsibility;
- failure category;
- whether raw evidence remains available;
- whether the output is trusted.

Clarify that normalization is not hidden type coercion unless explicitly authorized by the contract.

## 8. Clarify M2 raw-input scope

State precisely whether M2:

- preserves only the raw mapping supplied to the adapter; or
- constructs the later complete raw-source/provenance record.

Do not imply that the full later provenance contract exists when M2 only guarantees local non-mutation and preservation of the supplied input.

## 9. UpgradePilot README redesign

Retain:

- product purpose;
- primary user and supported decision;
- concise product flow;
- high-level maturity category;
- repository layout;
- run/use instructions when executable implementation exists;
- links to the technical specification, ADR index, limitations and program source.

Remove or avoid:

- exact next session action;
- detailed live gate sequence;
- full restatement of ADR-0002;
- duplicated milestone contract text;
- session-start instructions;
- detailed current capability claims.

The README may point to `MEMORY.md` or the canonical tracker for exact continuation, but must not become another tracker.

## 10. UpgradePilot `AGENTS.md` redesign

Retain:

- stable authority resolution;
- repository and file boundaries;
- safety, privacy, credentials and untrusted-code rules;
- how to locate current state;
- evidence and claim discipline;
- ADR/specification responsibilities;
- snapshot-handling rules at a high level.

Remove:

- exact current method/session/next action;
- temporary milestone details;
- active implementation instructions;
- live state that will change during routine execution.

## 11. `MEMORY.md` redesign

Use a compact continuation structure:

```text
Current responsibility:
Accepted decisions relevant now:
Implemented/verified state:
Unresolved item:
Canonical state/evidence links:
Immediate continuation pointer:
```

Keep only context needed by the next project-local session. Do not duplicate full ADR rationale, governance rules, roadmap, milestone definitions or tracker entries.

## 12. Working-memory role

Working-memory records may preserve:

- what happened;
- Ali’s challenge, prediction or reasoning;
- actual output;
- assistance used;
- local unresolved questions;
- evidence links.

They must state or clearly imply that accepted artifacts and the tracker control current state. Historical working-memory files should not be broadly rewritten solely for stylistic consistency.

## 13. Out of scope

Do not in this package:

- implement Pydantic models;
- write or change product tests;
- reverse or reopen ADR-0002;
- update capability depth without evidence;
- alter the Career canonical controls completed in prior packages except to correct a direct contradiction;
- refresh `docs/program/career/**`;
- update `docs/program/SOURCE.md`.

## 14. Validation scenarios

### New architecture ADR

Normally updates ADR, ADR index, specification only if a requirement/status statement changes, tracker gate result and possibly concise memory. It should not force README or `AGENTS.md` updates.

### One test passes

Updates source/test evidence; tracker only if a gate materially changes; memory only if continuation changes. No governance or README update.

### Framework replacement later

Primarily update the relevant ADR. The technical specification should remain stable when required external behavior does not change.

### New session begins

Read current continuation from memory/tracker. Do not rewrite README or `AGENTS.md`.

## 15. Pass conditions

- [ ] MUST/SHOULD/MAY terminology is defined and used where necessary.
- [ ] Important testable obligations have stable IDs.
- [ ] Proof obligations map to evidence categories.
- [ ] Specification requirements and Pydantic implementation choices are separated.
- [ ] Semantic processing order and failure ownership are explicit.
- [ ] M2 raw-input preservation scope is precise.
- [ ] README is orientation, not a duplicate tracker.
- [ ] `AGENTS.md` contains stable instructions only.
- [ ] `MEMORY.md` is a concise continuation pointer.
- [ ] Working memory remains evidence, not state authority.
- [ ] ADR-0002 remains accepted and accurately represented.

## 16. Recommended commit boundaries

Use two focused commits:

1. `Refine UpgradePilot technical contract traceability`
2. `Simplify UpgradePilot entrypoint and memory responsibilities`

After validation, stop and proceed to Work Package 06.