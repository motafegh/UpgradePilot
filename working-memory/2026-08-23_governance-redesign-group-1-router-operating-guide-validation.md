# Governance Redesign Group 1 — Router / Operating Guide Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Group plan:** `plans/governance-spec-governance-enhancement-refinement/01_CORE_ROUTER_AND_OPERATING_GUIDE_PLAN.md`  
**Implementation commit:** `b6efac8ad41fbf8e233b2142bdd2569c3687f597`  
**Main baseline merged before implementation:** `10cbcf9d5b4d5134b602fab05fdd02005f010adf`  
**Artifact role:** dated non-controlling implementation/validation evidence; not live project-position authority

## 1. Bounded Group-1 change

The implementation commit modifies only:

```text
AGENTS.md
OPERATING_GUIDE.md
SECURITY.md
plans/README.md
audits/README.md
```

No product source/tests, accepted product specifications, ADR semantics, operation Skills, or `MEMORY.md` live state were changed by Group 1.

## 2. Main design results

### Root routing

`AGENTS.md` now explicitly distinguishes:

```text
Audit / Review
Planning / Design
Build / Implement
Learning by Doing
Learning Only
```

Learning-by-Doing is represented as the normal project philosophy/overlay rather than a mutually exclusive action mode. Manual mode requests are supported but cannot override authorization, responsibility, or proof boundaries.

### Deliberate reinforcement

The former broad `state durable guidance once` policy is replaced by:

```text
one canonical semantic owner
+ bounded deliberate reinforcement when repeated failure/risk/salience justifies it
```

The important `JUST-*` implementation-retention and producer → integration/orchestration → consumer ownership checks remain visible at root as deliberate reinforcement. The Core specification remains their normative owner; `OPERATING_GUIDE.md` §4.1–4.2 retains the working method.

### Operating Guide

`OPERATING_GUIDE.md` remains a substantial controlling owner of project-wide Learning-by-Doing rather than becoming only an index.

It retains:

- real-responsibility working loop;
- context engineering;
- Ceremony Tax;
- implementation-retention burden;
- end-to-end responsibility trace;
- proportional session method;
- teaching/ownership method;
- prerequisite repair;
- assistance fading;
- evidence/proof interpretation;
- debugging;
- command/tool explanation;
- completion/stopping/handoff.

Operation-specific procedures are now explicitly identified as Skill responsibilities as they are admitted in later redesign groups.

### Source Clarity

The previous 22-rule + 21-question always-on Source Clarity contract is replaced in the Operating Guide by seven outcome families:

1. responsibility/orientation;
2. upstream → transformation → downstream flow;
3. input/output/type ownership;
4. non-obvious reasoning;
5. semantic/proof transformations;
6. selective educational depth;
7. truthfulness/maintenance.

No external repository references to the former `SOURCE-CLARITY-0xx` identifiers were found before compression. Detailed Build/Audit application belongs to later operation-Skill groups.

### Security disposition

`SECURITY.md` was **retained but reduced**, rather than deleted.

Reasoning:

- it still owns a coherent small responsibility: secrets/private data, external-evidence trust, unknown-code execution, external mutation, deliberate credentials, and transport boundary;
- many current and historical artifacts already reference the stable `SECURITY.md` path;
- deleting it would either break those references or force historical-record rewrites without a proportional benefit.

The retained file is intentionally compact and delegates concrete local proxy/token topology to `ENVIRONMENT.md` and claim semantics to the normal product owners.

### Durable-index cleanup

`plans/README.md` no longer acts as a changing catalog of the B2 architecture-reconciliation family. It now defines generic plan-family/local-index rules.

`audits/README.md` no longer duplicates a dated `Current classification (...)` list. Lifecycle membership remains owned by `audits/active/`, `audits/scheduled/`, `audits/deferred/`, and `audits/absorbed/` indexes.

## 3. Focused validation

### Scope/diff

`09eb6b6a66f1c0b9491c1c20ed2721f875942f18..b6efac8ad41fbf8e233b2142bdd2569c3687f597` contains exactly five modified files:

```text
AGENTS.md
OPERATING_GUIDE.md
SECURITY.md
audits/README.md
plans/README.md
```

### Branch baseline

After Group-1 implementation, GitHub comparison reported the governance branch **0 commits behind `main`** at baseline `10cbcf9d5b4d5134b602fab05fdd02005f010adf`.

### Governance-size observations

GitHub contents metadata after the change:

```text
AGENTS.md          14,253 bytes
OPERATING_GUIDE.md 18,958 bytes
SECURITY.md         3,679 bytes
ENVIRONMENT.md      7,048 bytes (unchanged)
```

Size is an observation only; no file-size threshold is treated as a correctness target.

### `governance_doctor.py` predicate review

A direct shell clone/run could not be performed in the available execution runtime because DNS/network access to GitHub was unavailable. This is **not** recorded as an executed PASS.

The deterministic predicates in the unchanged doctor were checked against the branch surfaces instead:

- all required governance files still exist, including the retained `SECURITY.md`;
- `AGENTS.md` still contains the required `audits/`, `examples/`, and `.agents/skills/` responsibility markers;
- the Skill tree and `cases.json` were not modified in Group 1;
- changed core Markdown references resolve to existing owners (`../docs/README.md`, `audits/LIFECYCLE.md`);
- no new broken operation-Skill Markdown path was introduced: not-yet-admitted Skills are referenced conceptually as `when present` rather than by nonexistent paths;
- the doctor itself required no Group-1 modification because `SECURITY.md` remains a required file.

An actual executable doctor run remains required when a repository-capable shell/environment is available; do not convert this predicate review into a claim that the script itself executed.

## 4. Planned routing-scenario review

### A — simple explanation

Pass condition represented:

- `explain` stays read-only;
- no repository-wide audit or plan is automatically required;
- Learning-by-Doing applies proportionately;
- smallest sufficient owner/source context is selected.

### B — audit request

Pass condition represented:

- audit/review is read-only unless separate change intent exists;
- the existing repository-audit Skill is selected for materially evaluative review;
- implementation truth remains source/test/evidence based.

### C — implementation request

Pass condition represented:

- Build/Implement is the primary operation;
- Learning-by-Doing normally overlays it;
- active source/tests are inspected first;
- applicable plan/specification/ADR/evidence is loaded only as needed;
- later Build Skill can replace detailed operation procedure without redefining authority.

### D — learning-only request

Pass condition represented:

- product mutation is explicitly paused;
- package-local learning contract/plan/memory is used when applicable;
- a later Learning-Only Skill can supply the reusable traversal procedure.

### E — repeated retention safeguard

Pass condition represented:

- root explicitly rejects current use/tests/history as retention authority;
- root requires producer → integration/orchestration → consumer tracing;
- `JUST-*` remains the canonical normative owner;
- `OPERATING_GUIDE.md` §4.1–4.2 remains the detailed reasoning method.

## 5. Group-1 stop line

Group 1 establishes the permanent router/Operating-Guide boundary only.

It does not create or broadly rewrite the planned Learning-by-Doing, Planning/Design, Build/Implement, or Learning-Only Skills, and it does not perform the full governance-consistency tooling expansion reserved for later groups.

This record is dated execution evidence only. `MEMORY.md` remains the sole live project-continuation owner.