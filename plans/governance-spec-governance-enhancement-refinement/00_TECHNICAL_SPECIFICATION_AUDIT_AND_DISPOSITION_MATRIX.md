# Technical Specification Audit and Disposition Matrix

**Artifact role:** Group-8 specification-by-specification audit trace  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Date:** 2026-08-23  
**Controlling plan:** `08_TECHNICAL_SPECIFICATION_SYSTEM_AUDIT_AND_REFINEMENT_PLAN.md`  
**Authority:** planning/audit evidence only; accepted specification/standard files remain the semantic owners

---

## 1. Audit result summary

The active specification system is fundamentally sound. The audit does **not** justify a new technical specification, a broad semantic rewrite, or product source/test changes.

The evidence-backed dispositions are:

| Surface | Disposition | Severity | Reason |
|---|---|---:|---|
| `docs/specifications/README.md` | **MODIFY — clarify admission/quality rules** | P2 | The index correctly separates spec/ADR/plan/source, but after the agent-governance redesign it should make future specification admission, historical-vocabulary, proof/non-proof, and engineering-standard boundaries explicit. |
| Core Pipeline + Contract | **MODIFY — CLARIFY OWNER** | P2 | `JUST-001..005` are intentionally canonical here, and §7/§9 already acknowledge implementation-retention discipline, but the header and opening boundary describe only product behavior. The declared responsibility should match the body instead of implying `JUST-*` is an accidental guest. |
| Product Decision Model | **MODIFY — TERMINOLOGY CLEANUP** | P3 | Durable active prose still contains `Conversation-C` / `Conversation-D` labels. Their semantic responsibilities already have concrete durable names. Preserve conversation labels only in provenance/history. |
| Minimum Useful Generality | **KEEP UNCHANGED** | — | Responsibility is clear, method neutrality is explicit, fixture-specific acceptance is bounded to the owning automated responsibility, proof classes are conditional/proportional, and live activation remains outside the file. |
| Naming Clarity | **MODIFY — NARROW + REFERENCE** | P2 | Naming/terminology engineering is valid, but `NAME-005`, `NAME-006`, the Explanation Rule, and the Ali-specific recall test still overlap the post-redesign `OPERATING_GUIDE.md` teaching responsibility. Keep artifact naming/terminology here; route learner-teaching depth/first-use explanation to the Operating Guide. |

No P0/P1 specification defect was found.

---

## 2. System-level findings

### SPEC-SYS-001 — Current owner chain is correct

**Observation**

The repository consistently distinguishes:

```text
Charter
→ mission / product boundary / claim limits

Specification
→ framework-independent required behavior / semantic acceptance

Engineering standard
→ cross-cutting engineering quality constraint

ADR
→ consequential method / structure

Plan
→ bounded sequence / proof / stop line

Source/tests/evidence
→ implemented truth

MEMORY.md
→ live continuation
```

**Disposition:** KEEP.

No generic precedence ladder or new owner is needed.

### SPEC-SYS-002 — Specification and execution artifacts must stay separate

External contemporary spec-driven-development practice corroborates the existing UpgradePilot split:

```text
specification / intent
→ implementation plan
→ tasks / bounded execution
→ implementation
```

UpgradePilot already has the stronger project-local form through specification → ADR → plan → source/tests. The audit uses external practice as corroboration only, not authority.

**Disposition:** reinforce concisely in `docs/specifications/README.md`; do not copy task/procedure mechanics into specifications.

### SPEC-SYS-003 — No new specification earns its ceremony cost

The apparent issues have existing owners:

- implementation-retention semantics → Core `JUST-*`;
- teaching/learner explanation → `OPERATING_GUIDE.md` + Learning Skills;
- historical conversation labels → provenance only;
- future spec admission/navigation → `docs/specifications/README.md`.

**Disposition:** NO NEW SPEC.

---

## 3. Core Pipeline and Contract Specification

### CORE-AUD-001 — Declared responsibility understates `JUST-*` ownership

**Observation**

Header:

```text
Stable project-wide framework-independent invariants for admitted UpgradePilot product behavior
```

Body:

- `JUST-001..005` explicitly govern whether implementation mechanisms are allowed to remain active;
- §7 says Core includes “why an implementation mechanism is allowed to remain active at all”;
- §9 change control explicitly includes “implementation-retention discipline”.

**Interpretation**

This is not evidence that `JUST-*` belongs elsewhere. The redesign traceability and all operation Skills already treat Core as the canonical normative owner. Moving it now would create more semantic churn and another owner problem.

The defect is narrower: **owner-description mismatch**.

**Disposition:** CLARIFY OWNER.

Expected edits:

- header Responsibility explicitly includes implementation-retention/ownership invariants;
- opening boundary states the file owns stable product/evidence invariants **and** framework-independent retention/ownership constraints on admitted implementation;
- `docs/specifications/README.md` navigation description matches.

Do not alter `JUST-001..005` semantics.

### CORE-AUD-002 — `JUST-*` deliberate reinforcement remains valid

`AGENTS.md`, `OPERATING_GUIDE.md`, Audit/Planning/Build Skills apply or reinforce the Core semantics without claiming independent normative ownership.

**Disposition:** KEEP.

### CORE-AUD-003 — Product/evidence invariants remain implementation-neutral

The core trust/raw/provenance/failure/authority requirements describe behavior and semantic boundaries rather than libraries/frameworks/current classes.

**Disposition:** KEEP.

---

## 4. Product Decision Model Specification

### PDM-AUD-001 — Active conversation labels are stale vocabulary

Two active-semantic references remain:

```text
define Conversation-D/final maintainer-facing synthesis...
```

and:

```text
...MUST NOT be silently decided by Conversation-C investigation logic alone.
```

The same file already has durable responsibility names:

```text
investigation selection
later synthesis / policy
maintainer-facing synthesis
```

**Interpretation**

Conversation labels are valid historical provenance in §16 and in filenames/dated records. They should not remain part of the active semantic vocabulary when a durable project term exists.

**Disposition:** RENAME / TERMINOLOGY CLEANUP.

Expected edits:

- `Conversation-D/final maintainer-facing synthesis` → `later maintainer-facing synthesis/policy` or equivalent durable wording;
- `Conversation-C investigation logic` → `this investigation-selection responsibility` or equivalent;
- preserve Conversations A/B/C only inside §16 provenance/history.

No candidate/applicability/investigation semantics change.

### PDM-AUD-002 — Investigation semantics versus planner method

The specification explicitly refuses generic planner/graph/rule-engine architecture and keeps investigation value, automated execution admissibility, and maintainer recommendability distinct.

**Disposition:** KEEP.

### PDM-AUD-003 — Static/configuration/runtime proof strength

The explicit distinction:

```text
workflow declaration
!= execution
!= success
```

remains a correct durable product-decision/evidence semantic and is exercised by accepted architecture/source/tests.

**Disposition:** KEEP.

---

## 5. Minimum Useful Generality Specification

### MUG-AUD-001 — Responsibility integrity

The file owns a distinct acceptance question:

> When input meaning varies, what prevents a known fixture/manual interpretation from being accepted as automated capability?

This is neither a plan nor a selected architecture.

**Disposition:** KEEP.

### MUG-AUD-002 — Method neutrality

The specification:

- rejects known-answer hardcoding and category-by-category interpreters only when they cannot perform the complete owning semantic responsibility;
- permits disposable baselines/oracles;
- does not require a universal model/framework;
- permits a bounded LLM conditionally rather than mandating one;
- bounds generality to credible variation in the admitted product domain.

**Disposition:** KEEP.

### MUG-AUD-003 — Proof proportionality

The eight proof classes are explicitly introduced with “When applicable” and the plan selects only discriminating classes.

**Disposition:** KEEP.

### MUG-AUD-004 — Live-state references

The file names `MEMORY.md` as live-position owner but does not itself record a current responsibility/stage/result.

**Disposition:** KEEP.

**Final file disposition:** **KEEP UNCHANGED.**

---

## 6. Naming Clarity Engineering Standard

### NAME-AUD-001 — Naming standard versus teaching procedure

The standard correctly owns names and terminology, but several rules extend into learner-teaching procedure:

- `NAME-005` requires the first material use of a standard technical term to include practical meaning and why needed;
- `NAME-006` explicitly governs “learning explanations”;
- §3 Explanation Rule requires full term, practical meaning, why name fits, exact responsibility, non-meaning, and depth now/deferred;
- `NAME-009` uses Ali personally as the engineering recall-test subject.

Post-redesign, `OPERATING_GUIDE.md` §7 and Learning Skills already own learner explanation, term introduction, required depth, and deferred depth.

**Interpretation**

This is competing semantic ownership, not helpful deliberate reinforcement, because the Naming standard and Operating Guide both define the same teaching contract at similar depth.

**Disposition:** NARROW + REFERENCE.

Expected edits:

- keep the requirement that names/terms be concrete and standard/project meanings not be overloaded ambiguously;
- require project-specific/non-obvious terminology to be defined at its narrowest durable owner where ambiguity would matter;
- remove `learning explanations` from the naming requirement and keep user-facing CLI/report labels;
- replace Ali-specific recall test with a competent-maintainer recall test;
- replace §3 teaching-depth checklist with an artifact-local terminology rule plus explicit reference to `../../OPERATING_GUIDE.md` for learner-facing teaching depth.

### NAME-AUD-002 — Example vocabulary table remains illustrative

The dependency-version table explicitly says source names may evolve and is not an immutable source-layout contract.

**Disposition:** KEEP.

### NAME-AUD-003 — Historical preservation remains correct

`NAME-012` and the active-file audit policy avoid mass rewriting historical records.

This supports preserving Conversation A/B/C labels in Product Decision Model provenance even while removing them from active semantic wording.

**Disposition:** KEEP.

---

## 7. Specifications README

### README-AUD-001 — Existing role split is correct

The current README already distinguishes technical specification, ADR, plan, source/tests, live state, and history well.

**Disposition:** KEEP core structure.

### README-AUD-002 — Future specification admission/quality rule is under-specified

After the governance redesign, the directory index should prevent future AI assistants from creating/specifying at the wrong layer.

Add a compact maintenance/admission section requiring:

```text
one distinct durable semantic responsibility
→ framework/implementation neutrality at the owned level
→ exact relation to Charter/other specs/ADRs/plans/source
→ proof/non-proof boundary
→ no live-state or session/conversation vocabulary in active semantics
→ stable IDs only when durable cross-reference value exists
→ new file only when an existing owner cannot absorb the responsibility cleanly
```

Also state that teaching procedure belongs to `OPERATING_GUIDE.md`/Skills, not an engineering standard unless the teaching rule itself is the engineering responsibility.

**Disposition:** MODIFY.

---

## 8. Planned modification set

Expected exact owner edits:

```text
docs/specifications/README.md
→ add compact specification admission/quality guidance
→ update Core and Naming navigation descriptions

docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
→ responsibility/boundary clarification only
→ no `JUST-*` semantic rewrite

docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
→ remove Conversation-C/D from active semantic wording only
→ preserve historical provenance labels

docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md
→ NO CHANGE

docs/specifications/UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md
→ narrow teaching overlap
→ competent-maintainer recall test
→ point learner explanation/depth to OPERATING_GUIDE.md
```

Potential directly-required reference edit:

```text
docs/README.md
→ only if its Core/Naming navigation becomes materially inaccurate after owner clarification
```

No ADR, product plan, product source/test, or live memory change is justified by this audit.

---

## 9. Validation obligations

After implementation:

- re-read all four active spec/standard files as one system;
- confirm MUG blob remains unchanged;
- confirm `JUST-001..005` text remains unchanged unless a separately documented semantic defect appears;
- confirm active PDM body no longer uses Conversation-C/D as semantic labels while provenance may retain them;
- confirm Naming no longer duplicates learner-depth teaching procedure;
- confirm specification README/`docs/README.md` navigation accurately reflects owners;
- run `python tools/agent-governance/governance_doctor.py` locally on the final branch tip;
- compare against `main` and confirm no `src/upgradepilot/` or `tests/` changes were introduced by Group 8;
- write one dated Group-8 validation record;
- stop before merge.
