# UpgradePilot Engineering Guide — pre-template

**Status:** non-controlling research artifact / future durable-guide template  
**Branch:** `research/real-world-engineering-practices-2026-10-24`  
**Purpose:** provide a concrete shape for a future human-facing `docs/ENGINEERING_GUIDE.md` without prematurely promoting it to main or duplicating canonical owners.

This is a template, not the Engineering Guide itself. Before promotion, reconcile it against then-current `main`, `MEMORY.md`, source/tests, applicable specifications/ADRs, and current documentation ownership.

## Authoring rule

The future guide should be **current-system-first, authority-aware, and history-linked**:

- explain the current technical mental model in one coherent place;
- link to canonical owners for exact rules/contracts instead of copying them;
- link selectively into `working-memory/` when the engineering journey materially explains why the current design exists, what failed before, what was corrected, or what remains intentionally unresolved;
- do not turn the guide into a chronological transcript or a second live-state tracker.

A useful distinction is:

```text
Engineering Guide
"How does UpgradePilot work now, and how should I understand it?"

Canonical owners
"What exact accepted rule / invariant / method controls this responsibility?"

Working memory
"How did we get here? What evidence, failures, corrections, experiments and handoffs produced this state?"

Learning artifacts
"How can I study or relearn this responsibility efficiently?"

MEMORY.md
"Where is the project right now, and what is selected next?"
```

## Proposed guide structure

### 1. How to use this guide

Explain:

- intended reader: engineer joining, reviewing, modifying or returning to UpgradePilot;
- this guide is explanatory/navigation material, not a second authority owner;
- current implementation truth remains source/tests/evidence;
- exact stable contracts remain with Charter/specifications/ADRs and other named owners;
- live continuation remains `MEMORY.md`;
- historical engineering progression remains under `working-memory/`.

### 2. Product and decision problem

Cover concisely:

- primary maintainer/user problem;
- supported decision classes;
- evidence-first product thesis;
- explicit non-goals and claim limits;
- why abstention and preserved uncertainty are product behavior rather than missing polish.

Primary deeper owners: `PROJECT_CHARTER.md`, relevant product-decision/action specifications.

### 3. One-page system mental model

Give the shortest correct end-to-end flow, for example:

```text
public dependency-update PR
→ exact identity + dependency transition
→ provider acquisition
→ typed/scoped evidence owners
→ applicability / impact / runtime / CI investigation
→ explicit unknown/problem states
→ Workspace/native preservation boundary
→ report projection + retained source access
→ maintainer-action synthesis
→ human/machine output
```

Then explain what each stage establishes and explicitly does not establish.

### 4. Architecture and subsystem map

Describe the major source responsibilities and their relationships, including as current evidence supports:

- application orchestration;
- GitHub/PyPI/upstream provider boundaries;
- dependency evidence;
- CI static/runtime evidence;
- target/environment evidence;
- impact/applicability evaluation;
- Workspace/native capture, representation, checkpoint and consumer boundaries;
- report projection/rendering;
- maintainer-action synthesis;
- CLI/application entry points;
- experiments and developer tooling as non-product boundaries.

Prefer diagrams/tables that show producer → transformation → consumer relationships.

For consequential architecture rationale, link the relevant ADR and, when useful, the working-memory record that demonstrates the pressure/failure/correction that led there.

### 5. Core UpgradePilot concepts and vocabulary

Explain project-specific meaning of terms such as:

- evidence;
- observation;
- interpretation/proposal/evaluated proposition;
- provenance and authority;
- exact identity;
- missing vs unresolved vs unsupported vs unavailable;
- coverage;
- applicability;
- candidate/finding;
- abstention;
- source reference vs retained original text;
- Workspace revision/checkpoint/reconstruction/recovery/replay distinctions;
- proof vs non-proof.

Link exact semantics to the relevant specification rather than re-owning them.

### 6. Major real data/control flows

Use real current UpgradePilot paths rather than toy architecture diagrams. At minimum consider:

1. normal public-PR investigation;
2. CI workflow/static/runtime correlation path;
3. package/upstream/support-impact path;
4. target/applicability path;
5. native Workspace publication/reconstruction path;
6. report save/open/offline-source path;
7. maintainer-action synthesis path.

For each flow:

```text
entry input
→ important producers
→ typed boundary
→ transformation/evaluation
→ downstream consumer
→ failure/unresolved states
→ proof anchors
```

### 7. State, persistence and time

Clarify the distinctions among:

- transient application state;
- immutable native/Workspace representations;
- published revisions;
- checkpoint storage;
- saved reports;
- source retention;
- reconstruction;
- recovery;
- deterministic replay;
- historical frozen evidence.

This section should specifically prevent readers from equating checkpointing, reopening, reconstruction and replay.

### 8. Evidence, trust and uncertainty model

Explain:

- source/provenance boundaries;
- copied context versus publisher authority;
- evidence strength;
- explicit unknown states;
- why one green CI job or one model output is not sufficient proof;
- why relationships/correspondence require their own evidence;
- fail-closed/abstention behavior where relevant.

### 9. Proof and evaluation model

Map the main proof classes and their limits:

- focused unit tests;
- integration/composition tests;
- deterministic product regression;
- historical/frozen product-simulation cases;
- live acquisition diagnostics;
- installed-package/clean-install proof;
- hosted verification;
- experiment/evaluation evidence;
- independent usefulness/maintainer evaluation.

Make clear that passing one proof class does not silently upgrade another.

### 10. How the system evolved — selective engineering journey

This is where `working-memory/` becomes first-class, but **selectively**.

Do not summarize every cycle. Instead identify major architecture/product transitions where knowing the journey improves technical understanding, for example:

```text
initial assumption / design
→ observed limitation or failure
→ investigation / experiment
→ correction / accepted decision
→ resulting current mechanism
→ remaining debt / non-proof
→ links to exact working-memory/evidence records
```

Possible journey themes to include only when still relevant:

- clean-slate/responsibility-based architecture corrections;
- CI static/runtime correlation evolution;
- applicability/impact model evolution;
- semantic/LLM experiments and demonstrated interpretation failures;
- Workspace research → accepted architecture → staged migration;
- report/source preservation and source-access evolution;
- product-value/usefulness investigations and unresolved acceptance questions.

This section makes the project explainable as an engineering journey without making old history authoritative over current source/specifications.

### 11. How to change UpgradePilot safely

Give human-facing modification guidance by responsibility:

- new provider/acquisition evidence;
- new typed domain evidence;
- new impact/applicability semantics;
- new Workspace/native representation;
- persistence/schema change;
- report projection/source-retention change;
- maintainer-action permission change;
- experiment versus product capability;
- new dependency/framework/tool admission.

Each item should say where to start reading and which owner must change if semantics/architecture change.

This section should not duplicate `.agents/skills/`; it should teach the **project responsibility map** a human engineer needs before selecting an implementation route.

### 12. Failure and diagnosis map

Provide a compact map of common failure classes, not step-by-step runbooks:

- input/identity rejection;
- acquisition/provider failure;
- evidence unavailable/unsupported;
- correlation failure;
- semantic extraction/evaluation limitation;
- material-basis/integrity failure;
- checkpoint/storage/reconstruction failure;
- report projection/decoding failure;
- environment/local-model issue;
- product defect versus evidence insufficiency.

Link to playbooks/runbooks only when such artifacts have actually been earned and adopted.

### 13. Repository/documentation map

Explain the role of:

- `README.md`;
- `PROJECT_CHARTER.md`;
- `MEMORY.md`;
- `docs/README.md`;
- `docs/specifications/`;
- `docs/architecture/`;
- `plans/`;
- `src/upgradepilot/` and `tests/`;
- `product-simulation/`;
- `experiments/`;
- `tools/`;
- `working-memory/`;
- `learning/`;
- `audits/`;
- `proposals/`;
- `.agents/skills/`.

Explicitly distinguish current authority, historical evidence, education, experimentation and AI-operation procedure.

### 14. Fast engineer onboarding route

End with a compact route such as:

```text
1. Read the one-page system mental model.
2. Trace one current real investigation flow.
3. Read the core evidence/decision semantics.
4. Inspect one representative Workspace/report flow.
5. Inspect the relevant current tests/proof.
6. Follow selected working-memory links for major design corrections.
7. Read MEMORY.md only for current continuation/status.
```

The exact route should be updated as the project architecture evolves.

## Working-memory integration policy

The future guide should use `working-memory/` in three specific ways:

1. **Rationale provenance** — link when a dated record contains the real evidence/pressure that explains a current architectural or semantic decision.
2. **Failure/correction history** — link when understanding an earlier incorrect approach, failed experiment or regression materially prevents future repetition.
3. **Engineering evolution** — selectively summarize major transitions so a reader can understand not only the final shape but the technical reasoning journey.

It should **not**:

- load or summarize all working-memory files;
- treat old working-memory conclusions as current truth without reconciliation;
- duplicate chronology for its own sake;
- replace promoted canonical owners;
- use historical records to override current implementation/proof.

## Maintenance model if adopted

The guide should be updated only when the **durable current mental model** materially changes, such as:

- a major subsystem/responsibility is introduced or removed;
- a normal end-to-end flow changes;
- a major persistence/state boundary changes;
- a core concept/term changes;
- a new proof class or operational boundary becomes part of the supported system;
- a staged migration reaches a new durable state.

Routine commits, dated investigations and live next-step changes should not churn the guide.

## Promotion checklist

Before creating a canonical `docs/ENGINEERING_GUIDE.md` on main:

- reconcile against current `main` and `MEMORY.md`;
- inspect current source/test architecture rather than copying this research snapshot;
- verify all major links/owners;
- remove sections that are no longer materially useful;
- ensure no canonical contract has been copied in a way that creates dual authority;
- include selective working-memory journey links where they materially improve understanding;
- make the guide understandable to a human engineer without requiring AI-agent procedure knowledge;
- record its documentation responsibility in `docs/README.md` if adopted.
