# Architecture Decisions

This directory contains UpgradePilot Architecture Decision Records (ADRs), including accepted and explicitly superseded consequential decisions.

## ADR responsibility

An ADR records one durable implementation or structural decision:

- context and owning responsibility;
- selected option;
- credible alternatives;
- rationale and material tradeoffs;
- consequences, risks, and reversal;
- bounded scope/undecided matters;
- reassessment triggers;
- links to requirements, plans, and evidence.

An ADR does not prove implementation, passing tests, installation, capability, live progress, or project continuation. Source/tests/commands/outputs and dated evidence prove implemented truth; `../../MEMORY.md` alone records live continuation.

## Proportionality rule

Use the **smallest ADR that preserves the durable decision**.

An ADR may include technical detail when that detail is itself part of the decision—for example an algorithmic boundary, dependency version range, trust rule, or structural constraint. It should not normally duplicate:

- the complete execution sequence from a bounded plan;
- exhaustive test matrices/proof catalogs;
- full experiment logs or score tables;
- current source-tree inventories;
- dated incidents/results already preserved as evidence;
- teaching/session instructions owned by `OPERATING_GUIDE.md`.

Preferred structure:

```text
why a durable decision is needed
→ selected method/boundary
→ important alternatives and rationale
→ consequences/reversal
→ reassessment triggers
→ links to detailed proof/evidence
```

Acceptance authorizes the decision within scope; detailed implementation proof remains with its actual evidence owners.

## Decision navigation

This section is navigation only. Each ADR's own `Status` field determines whether that decision is accepted or superseded. This list is not a live-stage register.

- [`ADR-0001-initial-python-source-layout.md`](ADR-0001-initial-python-source-layout.md)
  — **Accepted baseline.** Repository/distribution/import naming, `src/upgradepilot/`, active product test root, installed-package testing, and non-speculative package baseline.
- [`ADR-0002-pydantic-runtime-contract-models.md`](ADR-0002-pydantic-runtime-contract-models.md)
  — **Superseded.** Historical M2 Pydantic choice; not an inherited product method.
- [`ADR-0003-clean-slate-b2-source-reset.md`](ADR-0003-clean-slate-b2-source-reset.md)
  — **Accepted.** Historical M2 preservation plus clean active-source reset boundary.
- [`ADR-0004-dependency-version-change-evidence.md`](ADR-0004-dependency-version-change-evidence.md)
  — **Accepted.** Source-specific dependency extraction, representation-neutral trusted comparison, bounded structured-file acquisition, conservative ambiguity, and separate CI-consumption proof.
- [`ADR-0005-packaging-version-and-python-line-method.md`](ADR-0005-packaging-version-and-python-line-method.md)
  — **Accepted.** Bounded `packaging` dependency, PEP 440 release ordering, and exact stable Python-line witness method.
- [`ADR-0006-bounded-local-support-drop-semantic-extractor.md`](ADR-0006-bounded-local-support-drop-semantic-extractor.md)
  — **Accepted.** Bounded local LM Studio semantic candidate extractor with deterministic authority/grounding and explicit reassessment triggers.
- [`ADR-0007-responsibility-based-python-subpackages.md`](ADR-0007-responsibility-based-python-subpackages.md)
  — **Accepted.** Responsibility-based internal Python packages, import ownership, minimal package-root surface, and product/experiment/tool separation.

Do not add labels such as **current ADR**, **active ADR**, or **next ADR** here. Live project position belongs only in `../../MEMORY.md`.

## Specification, ADR, plan, and implementation

Resolve questions by responsibility rather than a generic total ranking:

- `docs/specifications/` → required framework-independent behavior/invariants;
- `docs/architecture/` → selected consequential methods/structures;
- `plans/` → bounded implementation/investigation sequence, proof, and stop line;
- source/tests/commands/outputs → actual implemented behavior;
- `../../MEMORY.md` → live selected continuation;
- `archive/`/working evidence → historical context without current authority.

A plan may coordinate an ADR but may not silently redefine it. An ADR may choose a method but may not redefine the product charter or technical requirement it is intended to satisfy. Explicit supersession is required to replace a prior rule within the same responsibility.

Create an ADR only for a durable dependency/framework choice, source/package boundary, representation policy, persistence mechanism, service boundary, cross-cutting security rule, trust method, or comparable structural commitment. Do not create ADRs for routine implementation choices, exact next actions, transient results, or unactivated technologies.

## Proof and ownership

ADR acceptance does not prove:

- dependency installation/import resolution;
- runtime behavior or passing tests;
- successful integration;
- production fitness;
- learner ownership/capability.

Former implementations/proposals preserved in Git history or `archive/` are evidence, not active architecture or code baselines.
