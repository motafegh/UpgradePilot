# AUDIT-013 — Experiment architecture, lifecycle and dependency boundaries

Recorded October 29, 2026. **Inspected revision:** `629ede16126d7ee17edf4ddb76b97986b09cc54b` (`main`), immediately after closure of the source-correspondence and retained ordinary-comparison increment. **Authority:** non-controlling audit evidence, explicitly selected by Ali as the next engineering input before substantial expansion of the experiment stack. `MEMORY.md`, accepted plans/ADRs/specifications, source and tests remain the controlling owners.

## Trigger and question

The current source/API work increasingly reuses code originally created for earlier experiments. Reuse is desirable when it avoids duplicate implementations, but the repository now makes it difficult to tell whether a file is:

- a completed historical/frozen experiment,
- an active trial,
- reusable experimental substrate,
- a retained proof/reader whose exact identity matters,
- or a candidate for later native product adoption.

At the same time, `experiments/` remains largely a flat namespace containing several generations and goals of work. The concern is therefore not "old code was reused". The concern is whether **experiment-specific artifacts have silently become shared infrastructure without an explicit lifecycle, dependency direction, navigation model or stable API boundary**.

This audit asks:

> Does the current `experiments/` subsystem accurately represent the roles and authority of the code it contains, and can we improve its organization/dependency boundaries without damaging frozen evidence, reproducibility or the product/experiment separation?

## Scope and exclusions

Inspect the complete current `experiments/` tree, its tests, imports among experiment modules, imports between `experiments/` and `src/upgradepilot/`, retained code-identity/hash contracts, relevant frozen evidence, and current working-memory/design references.

Do **not** assume the observations below are complete or correct merely because they are recorded in this audit. The first responsibility of the implementing assistant is an independent source-level reconstruction and contradiction check.

This audit does **not** authorize:

- a mass folder move or rename;
- rewriting historical/frozen evidence;
- promoting reusable experiment code into `src/upgradepilot/` merely because multiple experiments use it;
- changing product semantics, evidence strength, source-association meaning, checker outcomes or runtime/action permissions;
- continuing protocol/factory expansion before the experiment-architecture baseline is understood;
- creating a generic framework solely to make the directory look cleaner.

## Initial observations from the independent review

### O1 — The product/package boundary appears intact

`pyproject.toml` packages from `src`, and the installed product entry point is `upgradepilot.cli:main`. The reviewed product tree is responsibility-oriented under `src/upgradepilot/`. No product-to-experiment import was found in the bounded review.

The observed healthy direction is:

```text
experiments/* -> src/upgradepilot/*
```

Experiments may use real native acquisition/Workspace/source-retention primitives to test composition. The dangerous reverse direction would be:

```text
src/upgradepilot/* -> experiments/*
```

The implementing assistant must verify this repository-wide rather than treating the bounded search as proof of absence.

### O2 — `experiments/` is a mixed, mostly flat multi-era namespace

The current directory contains, side by side, Investigator qualification material, older B2/X1 probes, evidence-gap work, CI diagnostics, API interpretation/acquisition/binding/signature work, retained trial runners and the new source-correspondence/ordinary-comparison path.

There is no current `experiments/README.md` that explains goals, lifecycle state, authority, dependency direction, frozen status or navigation. A reader must reconstruct those facts from filenames, commits, working-memory and retained evidence.

### O3 — New experiments materially depend on earlier experiments

The current ordinary source/signature path reuses multiple older experiment modules rather than reimplementing them. This is often correct engineering, but it means `experiments/` is no longer just a bag of independent probes: it is becoming an **experimental subsystem with internal dependency structure**.

Examples observed during review include the ordinary caller/signature runner consuming older adapter/source acquisition, signature checking, retained comparison reading, target-context and correspondence modules. The source-correspondence layer itself reuses the earlier call/signature checker.

### O4 — Some filenames/lifecycle labels no longer match the responsibility they serve

Several files that originated as a specific `trial`, `smoke` or `exploration` now expose functionality reused by later experiments.

Examples requiring revalidation include:

- `api_call_signature_trial.py` now supplying retained-record decoding/rendering/support used by the ordinary v2 flow, including private `_...` helpers;
- `api_target_context_smoke.py` supplying reusable acquisition/orchestration types/functions;
- `api_adapter_exploration.py` supplying reusable source-request/acquisition structures;
- `api_call_signature.py` acting as the checker substrate beneath newer source-correspondence work.

The issue is not that those implementations must move. The issue is that their **architectural role has changed without an explicit reclassification or public experimental API boundary**.

### O5 — Cross-experiment reuse currently includes private implementation APIs

The newer ordinary runner imports private helpers from an older specific trial. That creates a dependency inversion smell: a newer end-to-end trial depends on implementation details of an older trial rather than both depending on an intentionally shared experimental support owner.

This does not prove the helpers should be extracted. The assistant must first determine whether the shared semantics are truly stable/identical, how many consumers exist, and whether extraction would simplify or instead create another abstraction layer.

### O6 — Frozen evidence makes naive cleanup risky

Recent retained comparison receipts bind exact experiment source identities/hashes, and original HTTPX/pytest bundles are deliberately preserved and opened read-only. Historical records also contain repository-relative paths and exact code identities.

Therefore a normal "move files into nicer folders" refactor can increase reproduction/navigation cost or break current readers/tests even if historical Git commits remain available. Organization repair must treat frozen evidence and current compatibility as first-class constraints.

## Findings

### AUDIT-013-F1 — High: experiment lifecycle and authority are under-specified

**Finding:** The repository does not provide an authoritative experiment inventory that distinguishes historical/frozen experiments, active trials, reusable experimental substrate and product-adoption candidates.

**Risk:** Reuse can silently convert a one-off experiment into de facto infrastructure; future assistants may either duplicate qualified logic unnecessarily or mistake reusable experimental code for native product authority.

**Required direction:** establish an explicit lifecycle/role map for the experiment subsystem before significant new experiment families are added.

### AUDIT-013-F2 — High: internal dependency boundaries are implicit and partially inverted

**Finding:** Cross-experiment imports are now material, including newer orchestration depending on older trial/private helpers. The current filenames and module boundaries do not clearly identify shared experimental APIs versus trial-specific code.

**Risk:** fragile coupling, accidental modification of frozen/legacy responsibilities, unclear ownership, and future difficulty deciding what is safe to reuse, replace or promote.

**Required direction:** reconstruct the actual import/dependency graph; then establish the smallest explicit dependency rule and extract shared support only where the evidence justifies it.

### AUDIT-013-F3 — Medium: navigation and goal-oriented organization are inadequate for the current scale

**Finding:** A flat directory that was acceptable for isolated probes is increasingly costly now that the folder contains multiple research eras, active API/source work, retained proof readers and shared components.

**Risk:** engineers must infer purpose/status from chronology and chat history; stale work and active infrastructure look equally authoritative; onboarding and auditing become unnecessarily expensive.

**Required direction:** add a durable navigation/index layer and, only if justified after dependency/frozen-reference analysis, introduce goal-oriented physical grouping incrementally.

### AUDIT-013-F4 — Medium: cleanup can damage evidence/reproducibility if treated as cosmetic refactoring

**Finding:** exact source hashes, code identities, retained bundles, relative references and historical replay/opening obligations constrain moves/renames and shared-helper extraction.

**Risk:** a cosmetically cleaner tree that weakens reproducibility, silently changes method identity, or makes original retained bundles harder to open is a regression.

**Required direction:** every structural change must state what historical/current identity it affects and how compatibility is preserved or intentionally versioned.

### AUDIT-013-F5 — Guardrail: repeated reuse does not itself justify product promotion

**Finding:** multiple experiment consumers prove reuse pressure, not product readiness or native authority.

**Risk:** moving an experimental checker/acquirer/correspondence component into `src/upgradepilot/` merely to "clean up" dependencies would collapse the product/experiment qualification boundary.

**Required direction:** keep the intermediate category of **reusable experimental substrate** explicit. Product adoption requires its own selected capability, native owner/type/codec/material/report contract and qualification evidence.

## Mandatory independent analysis before fixes

The assistant taking this audit must **not start by implementing the folder structure suggested in prior discussion**. First perform and preserve a source-backed analysis at the then-current `main`:

1. Reconcile the current head and recent experiment changes after `629ede16`; do not assume this audit is still complete if newer commits exist.
2. Inventory the full `experiments/` tree recursively, including tests and non-Python experiment records.
3. Build the actual import/dependency graph among experiment modules. Distinguish public names from private `_...` helpers and identify cycles/central modules.
4. Verify product boundary direction repository-wide: find any `src/upgradepilot -> experiments` dependency, dynamic path/import trick, CLI/package inclusion or test-only exception. Record exact evidence; absence must be scoped to the performed search.
5. Classify relevant experiment artifacts, with evidence, into at least:
   - historical/frozen experiment or proof;
   - active trial/runner;
   - reusable experimental substrate;
   - retained compatibility/reader surface;
   - product-adoption candidate (only when separately justified);
   - obsolete/superseded/unclear, if any.
6. Map which files are bound by current retained code identities, exact hash checks, frozen bundles, working-memory references or reproducibility commands. Identify which files are unsafe to move/rename without a compatibility strategy.
7. Identify modules whose current name (`trial`, `smoke`, `exploration`, etc.) materially understates their reused responsibility.
8. Identify duplicated functionality and accidental shared infrastructure separately. Do not infer that every duplicate deserves a generic abstraction.
9. Assess current `experiments/tests/` organization and whether tests reveal hidden lifecycle/API contracts.
10. Compare findings with this audit. Explicitly mark each initial observation as confirmed, narrowed, contradicted or superseded before selecting fixes.

Preserve that analysis in a dated working-memory/evidence record so the final organization decision does not depend on chat context.

## Fix-selection principles after the independent analysis

Prefer the smallest sequence that makes lifecycle and dependency ownership explicit without breaking evidence.

A likely first layer, subject to the assistant's independent findings, is:

- create an authoritative `experiments/README.md` or equivalent index that explains purpose, lifecycle categories, current major experiment families, frozen/retained status and dependency rules;
- publish a role inventory for the active/reusable experiment modules;
- state and verify the invariant that native product code must not depend on experiment modules;
- distinguish trial runners from reusable experimental substrate;
- remove avoidable imports of another trial's private helpers when a smaller explicit shared owner is genuinely justified;
- preserve curated/frozen v1 readers and exact historical evidence without regrading/reanalysis;
- leave physical moves/renames until their benefit exceeds their compatibility/reproduction cost.

If physical restructuring is justified, prefer incremental moves with explicit compatibility/versioning rather than one mass reorganization. If retaining a historically named module is cheaper/safer than moving it, document its current role rather than forcing cosmetic purity.

## Verification requirements for any repair cycle

The eventual repair must demonstrate, as applicable:

- the experiment role/dependency map matches actual imports;
- no new `src/upgradepilot -> experiments` dependency is introduced;
- relevant experiment suites remain green;
- current controlled source-correspondence/ordinary-comparison behavior remains semantically unchanged unless a separately justified defect is found;
- original HTTPX/pytest retained bundles remain read-only openable under their supported compatibility path and frozen member hashes are not rewritten;
- retained/current code-identity checks are deliberately preserved or explicitly versioned when shared support changes;
- no historical evidence/result is silently regenerated, regraded or relabeled;
- product tests are run if any native source boundary changes; otherwise do not claim fresh product proof merely from experiment-only tests;
- current documentation/commands do not point to removed paths without an intentional migration/compatibility story.

## Disposition and sequencing

**Lifecycle selection: ACTIVE.** Ali selected this audit as the next engineering input after the source-correspondence increment closed.

The intended sequence is:

```text
independent current-state experiment audit
    -> corrected inventory/dependency/lifecycle model
    -> bounded repair plan/selection
    -> implementation of justified organization/API-boundary fixes
    -> verification against retained/frozen evidence
    -> only then resume substantial protocol/factory expansion or broader experiment growth
```

This does not require solving every historical naming issue before any future experiment. The gate is that the project must first make the current experiment subsystem understandable and stop accidental infrastructure growth from remaining implicit.

A successful outcome is not "more folders". It is:

> a repository where an engineer can tell what an experiment artifact is for, whether it is historical or active, whether it is safe to depend on, what authority it has, and what evidence would be affected by changing it.

## References / initial evidence horizon

- `pyproject.toml` — package boundary under `src`.
- `src/upgradepilot/` — native product source tree.
- `experiments/` and `experiments/tests/` — audited subsystem.
- `experiments/api_call_signature.py`
- `experiments/api_call_signature_trial.py`
- `experiments/api_target_context_smoke.py`
- `experiments/api_adapter_exploration.py`
- `experiments/api_source_correspondence.py`
- `experiments/api_ordinary_call_signature_trial.py`
- `working-memory/2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md`
- `working-memory/evidence/2026-10-29-source-correspondence-and-ordinary-retention/REVIEW.md`
- `working-memory/evidence/2026-10-29-source-correspondence-and-ordinary-retention/final-verification.json`
- `working-memory/evidence/2026-10-28-pr-driven-caller-signature-design/DESIGN.md`
- `audits/README.md` and `audits/LIFECYCLE.md`

The observations in this audit are a bounded independent review horizon, not a substitute for the mandatory current-state analysis above.

UP-SKILL:upgradepilot-repository-audit

## Subsequent independent adjudication and repair — October29

The original observations/selection above remain the recorded629ede16 review horizon.
[Independent reconstruction](../working-memory/evidence/2026-10-29-experiment-lifecycle-and-dependency-repair/INDEPENDENT_ANALYSIS.md)
was preserved/published ata1d994cb against97983da3 BEFORE repair selection; it explicitly
adjudicates O1–O6/F1–F5. It confirms the product boundary and reuse, narrows lifecycle
absence and dependency-inversion claims (the actual graph is acyclic), identifies
earlier family-local shared/private APIs and records material baseline test debt.

The [bounded plan](../plans/EXPERIMENT_ORGANIZATION_AND_DEPENDENCY_BOUNDARY_REPAIR_PLAN.md)
and [resolution/evidence](../working-memory/evidence/2026-10-29-experiment-lifecycle-and-dependency-repair/RESOLUTION.md)
carry the implemented role inventory/navigation, explicit public signature-evidence
support, exact legacy exceptions, static graph/package boundary check, current/historical
source identity handling, unchanged frozen results and failure-baseline comparison.
No proposed physical folder arrangement was assumed or implemented; no native/product
promotion or semantic expansion followed. Lifecycle is now carried by the absorbed
index under LIFECYCLE.md. Historical fixture debt remains explicitly owned/deferred;
this resolution does not rewrite the original audit or experimental outcomes.
