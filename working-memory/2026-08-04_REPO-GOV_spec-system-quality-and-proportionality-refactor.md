# Specification-System Quality and Proportionality Refactor

**Date:** 2026-08-04  
**Record type:** Dated repository-governance working memory  
**Status:** Completed  
**Scope:** Active UpgradePilot control/specification/ADR/plan/public-orientation Markdown system  
**Explicit exclusion:** `product-simulation/` and all of its local controls/specifications/artifacts

## 1. Trigger and audit question

A dedicated audit reviewed UpgradePilot's mature Markdown control system without asking whether the documents reflected the latest product implementation state.

The question was instead:

> Are the project-local instruction, memory, environment, charter, route, specification, ADR, plan, audit, and public-orientation artifacts still the clearest, smallest, most maintainable control system for Ali and AI agents, or has accumulated governance begun to duplicate itself and impose unnecessary reading/synchronization cost?

The audit concluded that the foundational architecture was strong but the control surface had begun to inflate through repeated ownership tables, authority ladders, operating rules, historical contracts, proof matrices, environment evidence, and execution detail copied into several artifacts.

The refactor therefore optimized **ownership and subtraction**, not new governance.

## 2. Repository baselines and concurrent-state handling

The initial audit inspected repository state around:

```text
f738d31de4258b3b151ed76ab8e52dceb76cdee8
```

Before refactor writes began, `main` had already advanced through a separate governance/security alignment series ending at:

```text
76c42bbfd19ab0e5688cbb968ee61520a7ad277d
```

That newer state introduced/strengthened `SECURITY.md`, credential-use ownership, and ADR-0007 path interpretation.

A stale first write to `AGENTS.md` was rejected by GitHub because the file had changed. The refactor then refreshed the latest file and deliberately integrated the new `SECURITY.md` owner rather than overwriting or reverting concurrent work.

The specification-system refactor itself begins after `76c42b...` and was planned in:

- [`../plans/SPEC_SYSTEM_GOVERNANCE_REFACTOR_PLAN.md`](../plans/SPEC_SYSTEM_GOVERNANCE_REFACTOR_PLAN.md)

Plan commit:

```text
ae583e543df4953647d831df2d798b9e6bbfe194
```

Pre-working-memory refactor head:

```text
f0bf08d69a59e6b9ef0a22797da04cdd42d9e85d
```

## 3. Primary finding — the control model was strong but increasingly self-duplicating

The strongest existing rule was already:

```text
one fact or rule
→ one normal owner
→ link rather than duplicate
```

But the control system itself had drifted away from that principle.

Examples included:

- `AGENTS.md` repeating environment, operating, generality, architecture-admission, learning, validation, route, and document-routing rules owned elsewhere;
- `MEMORY.md` containing a large architecture tree, test output, incident narrative, experiment scores, and source-path maps in addition to live continuation;
- `ENVIRONMENT.md` mixing reusable machine/service facts with complete model inventory, historical measurements, experiment results, and point-in-time resource evidence;
- the active core specification embedding a large historical M2 contract;
- ADRs containing execution plans, implementation-path inventories, exhaustive proof matrices, and experiment-report detail;
- bounded plans re-specifying already accepted ADR/specification decisions;
- `README.md` reproducing substantial internal project-control detail;
- the audit template making a twelve-section formal record and stable finding IDs appear normal even for small reviews.

The goal was therefore not to remove evidence discipline or architectural clarity. It was to restore the repository's own responsibility-ownership model to the documentation system itself.

## 4. Authority-model correction

### Previous weakness

`AGENTS.md` and `OPERATING_GUIDE.md` expressed a long linear precedence such as:

```text
user
→ AGENTS
→ stable controls
→ route/plan
→ specification/ADR
→ records
```

That was conceptually inaccurate after the first few levels because a specification, ADR, plan, route, charter, and executable evidence own **different responsibilities** rather than one generally outranking another.

### New rule

Strict precedence is now intentionally short:

```text
safety / legal / platform constraints
→ Ali's explicit instruction
→ nearest applicable AGENTS.md
```

After that, questions are resolved by the artifact that owns the disputed responsibility.

Examples:

```text
required behavior     → specification
selected mechanism    → ADR
execution sequence    → bounded plan
live continuation     → MEMORY.md
implemented truth     → source/tests/outputs
environment baseline  → ENVIRONMENT.md
security rules        → SECURITY.md
```

A plan may coordinate implementation of an ADR/specification but cannot silently rewrite it. An ADR may select a method but cannot redefine the product charter. Explicit supersession is required when a later artifact replaces an earlier rule inside the same responsibility.

This change is reflected in:

- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- `docs/specifications/README.md`;
- `docs/architecture/README.md`;
- `plans/README.md`.

## 5. `AGENTS.md` — bootstrap/router instead of duplicate project manual

`AGENTS.md` was reduced to the material that every agent benefits from seeing early:

- purpose;
- short strict instruction hierarchy;
- responsibility-owner routing;
- sole live-state rule;
- artifact placement;
- task-dependent required reading;
- concise environment/security routing;
- critical repository safeguards;
- product/source structural anchors;
- concise generality/validation/claim rules;
- document-owner routing.

Detailed environment workflow, operating loop, teaching policy, generality specification contents, architecture-admission procedure, route narrative, learning-depth procedure, and repeated validation text were removed or reduced to links to their canonical owners.

The newer `SECURITY.md` responsibility was preserved and explicitly incorporated.

## 6. `OPERATING_GUIDE.md` — preserved as the real operating-method owner

The operating guide remains intentionally substantial because learning/execution/proportionality/debugging are its actual responsibility.

Changes were focused rather than reductive:

- replace long post-AGENTS total precedence with responsibility-owner resolution;
- keep actual implementation proof classes distinct;
- retain the Ceremony Tax Rule, proportional session modes, decision/execution/exploration modes, teaching, debugging, prerequisite repair, assistance fading, evidence interpretation, and stopping;
- reduce duplicated repository-routing detail where root `AGENTS.md` already owns it.

The result strengthens the guide by making other files stop copying it.

## 7. `MEMORY.md` — continuation index, not project dossier

The live-memory concept was preserved but the file was compressed around its true responsibility:

- execution branch/route;
- parent and selected bounded plan;
- accepted architecture anchors relevant to continuation;
- latest material verification summary and evidence links;
- exact Step 7B continuation;
- blockers/caveats only when they affect continuation;
- concise learning depth.

Removed duplication included:

- full source tree;
- detailed reconciliation narrative;
- long test output reproductions;
- shared-primitive/version-method architecture summaries;
- full Step 6 score/configuration table;
- Step 7 path map already owned by plan/ADR;
- detailed credential incident narrative.

Those details remain available through source, ADRs, environment, and working/evaluation evidence.

The live product continuation itself did **not** change: the selected product increment remains Step 7B deterministic crossed-release Markdown source windows.

## 8. `ENVIRONMENT.md` — durable baseline separated from dated evidence

`ENVIRONMENT.md` now retains:

- WSL2 as normal control plane;
- stable project/venv paths and Python observation;
- GPU identity/capacity;
- LM Studio localhost topology/base endpoints;
- reusable local semantic deployment identity relevant to ADR-0006;
- re-check/freshness rules;
- recurring GitHub credential caveat;
- links to detailed historical evidence.

It no longer duplicates:

- the complete dated model inventory;
- point-in-time VRAM/temperature/system-memory tables;
- historical comparison ladders;
- full experiment/evaluation results;
- long load/unload evidence reproductions;
- runtime dependency lists already authoritative in `pyproject.toml`.

Detailed evidence remains in `working-memory/` snapshots.

## 9. `PROJECT_CHARTER.md` — removed Career-program architecture ownership

The charter previously contained A1/A2/A3 advanced-system exposure obligations originating from a broader Career strategy.

Those quotas/checklists were removed from product-charter authority.

The replacement boundary is:

- UpgradePilot remains a learning-by-building flagship;
- Career review may identify UpgradePilot as a place to practise something;
- that does **not** automatically authorize a model, graph, agent, queue, service, Kubernetes, cloud component, or other architecture;
- advanced methods still require project-local product/evaluation need and the charter's technology-admission evidence.

Learning value remains a legitimate tradeoff consideration but cannot substitute for product need, evidence, proportionality, or claim discipline.

## 10. Route plan — gates instead of historical/implementation dossier

`plans/UPGRADEPILOT_90_DAY_PLAN.md` now focuses on:

- stable product-flow horizon;
- route principles;
- D0 → D1 → B1 → B2 → B3 → B4 → B5 → X1 → C1;
- each stage's purpose and exit outcome;
- stable capacity/scope discipline;
- route-maintenance boundary.

Historical D1 case synthesis and lower-level B2 implementation mechanics are linked to their evidence/bounded-plan owners rather than reproduced.

## 11. Core technical specification — historical M2 contract extracted

The active file:

- `docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md`

now owns current stable project-wide:

- raw/trusted separation;
- observation/interpretation/decision separation;
- snapshot/provenance/evidence-state invariants;
- trust/authority/grounding/corroboration boundaries;
- validation/transformation order;
- failure/stopping classes;
- representation/authority discipline.

The large detailed historical M2 caller/trusted-case contract was removed from the active normative surface and preserved at:

- [`../archive/2026-08-04_RETAINED_M2_TRUSTED_CASE_CONTRACT.md`](../archive/2026-08-04_RETAINED_M2_TRUSTED_CASE_CONTRACT.md)

That archive is explicitly historical and non-controlling. It preserves field-level rules, normalization behavior, proof obligations, and failure distinctions for traceability without giving obsolete M2 design disproportionate authority during normal reading.

## 12. Naming rules — engineering standard, not product-behavior specification

`UPGRADEPILOT_NAMING_CLARITY_SPECIFICATION.md` remains at its existing path to avoid low-value path churn and broken references, but its title/status now explicitly classify it as an **accepted project-wide engineering standard**.

This is an intentional compromise:

- semantic authority classification is corrected;
- useful naming/teaching rules remain unchanged in substance;
- no new governance directory/category is created solely for taxonomic purity;
- historical references do not require repository-wide migration.

`docs/specifications/README.md` explains the distinction.

## 13. ADR proportionality

The ADR meta-control now says to preserve the **smallest durable decision** and link detailed proof/evidence.

ADR-0004, ADR-0005, and ADR-0006 were substantially reduced while preserving their accepted decisions.

### ADR-0004 retained

- source-specific dependency extraction;
- representation-neutral trusted comparison;
- exactly-one-transition semantics;
- admitted requirements/constraints and bounded `uv.lock` boundary;
- exact base/head acquisition and 1,000,000-byte bound;
- conservative duplicate-record handling;
- separation of dependency identity from CI consumption;
- alternatives/consequences/reassessment.

Removed/reduced:

- current source-file/function inventory;
- large problem-code catalog;
- known-case byte measurements;
- exhaustive proof/test checklist;
- learning-session instructions.

### ADR-0005 retained

- `packaging>=26.2,<27`;
- raw/parsed version separation;
- crossed-release ordering;
- exact stable `X.Y.Z` question;
- boundary-complete witness derivation;
- admitted/unsupported specifier forms;
- alternatives/consequences/reassessment.

Detailed test catalog and teaching list were delegated to plan/tests.

### ADR-0006 retained

- bounded LM Studio/local model method;
- model-facing contract v2;
- no-auto-retry baseline;
- deterministic authority/source reconstruction/grounding;
- strict bounded semantic scope;
- adoption evidence summary;
- source-window runtime obligation;
- transport/security boundary;
- alternatives/consequences/reassessment.

Detailed per-case evaluation history, latency table, counterfactual replay narrative, and experiment-report detail remain with Step 6 evidence rather than architecture.

## 14. Plans — execution owners rather than second specifications

`plans/README.md` now explicitly states:

```text
reference accepted requirement/method owner
→ state execution consequence
→ sequence
→ proof
→ stop line
```

The selected target-Python parent plan and Step 7 integration plan were refocused accordingly.

They retain:

- product question;
- scope;
- execution sequence;
- activation order;
- modification boundary;
- proof obligations;
- stop/reframe conditions.

They no longer reproduce full ADR-0004/5/6/7 decisions.

Step 7 still owns its not-yet-separately-architected deterministic bridges—exact-commit changelog discovery, Markdown section/window rules, runtime composition, conditional application sequencing, and controlled/live integration proof—because those are execution responsibilities required to make the accepted extractor usable.

## 15. Audit proportionality

`audits/README.md` now makes compact audit records the default for one bounded concern.

Formal twelve-part-style records, stable `AUDIT-NNN` names, and finding IDs are reserved for cases where:

- several findings need separate tracking;
- later artifacts must cross-reference findings;
- consequential architecture/security/evidence questions justify durable structure.

The audit process explicitly applies the `OPERATING_GUIDE.md` Ceremony Tax Rule to itself.

## 16. Root README — public orientation only

The root README now provides:

- product purpose and supported boundary;
- short product flow;
- executable repository boundaries;
- concise route pointer;
- control-owner navigation table;
- learning/claim orientation.

It no longer duplicates full internal route, source-layout, learning loop, historical clean-source rationale, and project-ownership detail already owned elsewhere.

## 17. Intentionally unchanged areas

The audit considered several directory-level controls already strong and did not rewrite them merely for uniformity:

- `working-memory/README.md`;
- `learning/README.md`;
- `proposals/README.md`;
- `chronicle/README.md`.

Their existing boundaries remain useful and proportional.

### Explicit user-directed exclusion

No file under `product-simulation/` was changed, including:

- local `AGENTS.md`;
- `SIMULATION_GOVERNANCE_AND_PLAN.md`;
- `RUNTIME_ARTIFACT_SPECIFICATION.md`;
- `TRANSPARENT_BASELINE_SPECIFICATION.md`;
- scenarios or discovery evidence.

The simulation subsystem remains historical and may be separately reconsidered only if future work explicitly reactivates it.

## 18. Validation performed

A commit comparison isolated this refactor from the latest pre-refactor governance/security baseline:

```text
base: 76c42bbfd19ab0e5688cbb968ee61520a7ad277d
head before this record: f0bf08d69a59e6b9ef0a22797da04cdd42d9e85d
commits: 20
```

Isolated changed paths were only the intended control/documentation surfaces plus the new refactor plan and historical M2 archive.

Confirmed absent from the isolated diff:

```text
product-simulation/
src/
tests/
experiments/
tools/
pyproject.toml
SECURITY.md
ADR-0007
```

`SECURITY.md` and ADR-0007 had changed in the newer pre-refactor baseline and were preserved/consumed rather than overwritten.

Line-level diff summary for the isolated refactor before this record:

```text
additions: 1,657
deletions: 3,360
net:      -1,703 lines
```

That net reduction includes adding both:

- the 164-line bounded refactor plan;
- the 180-line historical M2 archive.

Therefore the reduction is not achieved by deleting historical traceability; it primarily removes duplicated active normative/operational text.

No new branch or pull request was created. All changes were made directly on `main` as explicitly requested.

No product source/test execution was required because the refactor changed Markdown control artifacts only. Product behavior, runtime dependencies, and the live Step 7B continuation were not changed.

## 19. Tradeoffs and accepted risks

### Less convenient local duplication

A reader may now need to follow a link to an ADR/specification/environment record instead of finding the same rule copied into the current file.

This is intentional. The reduced immediate convenience is accepted in exchange for lower synchronization drift and smaller mandatory context.

### Naming file path remains historically named `...SPECIFICATION.md`

Its authority class is corrected in the document/index, but the existing path was retained to avoid cosmetic churn and widespread historical-reference migration.

Revisit only if the filename itself materially causes misunderstanding despite the explicit classification.

### Old unselected/historical plans may still contain duplicated or outdated wording

The refactor deliberately did not mass-rewrite every historical/unselected plan. When one is selected again, reconcile it with accepted owners first, as `plans/README.md` now requires.

### Compression can become harmful if it hides required context

The goal is not shortest possible documents. If repeated real work shows that a removed summary is necessary at the point of use for safety or execution accuracy, restore the **smallest useful summary** while retaining one canonical owner.

## 20. Reassessment triggers

Reopen this governance design if evidence shows any of the following:

- agents repeatedly cannot determine which artifact owns a material question;
- responsibility-based conflict resolution still produces ambiguous authority;
- required work repeatedly needs large speculative document scans;
- `MEMORY.md` again grows into an architecture/evidence archive;
- `ENVIRONMENT.md` again accumulates point-in-time experiment evidence;
- ADRs again absorb plan/test/report responsibilities;
- plans repeatedly re-specify accepted ADR/specification content and drift;
- useful context was removed so aggressively that safe/accurate execution suffers;
- the naming-standard classification continues to cause real confusion;
- a new top-level artifact responsibility becomes genuinely necessary.

Do not create a new master governance layer merely because future documents become long. First apply the same responsibility-owner and Ceremony Tax tests used here.

## 21. Result

The repository retains the same core governance architecture:

```text
one live-state owner
+ stable charter
+ route/gates
+ operating guide
+ environment/security owners
+ technical specifications
+ ADRs
+ bounded plans
+ source/tests/evidence
```

The material change is that these owners now rely more strongly on **links and responsibility boundaries instead of duplicated control text**.

The desired operating property after this refactor is:

```text
smaller mandatory context
+ clearer ownership
+ preserved evidence
+ lower synchronization cost
+ less accidental historical authority
+ no loss of safety or product-control boundaries
```
