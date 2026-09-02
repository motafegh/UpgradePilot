# UpgradePilot Whole-Project Learning-Artifact Roadmap Plan

**Plan responsibility:** coordinate the smallest sufficient sequence for a fresh, high-quality learning-artifact set covering the meaningful UpgradePilot engineering journey from project foundations through the evidence horizon available when each group is authored.

**Initial roadmap-analysis evidence horizon:** `main@91158b0925037cdde4142efc52a8a86d2950e9a6` (2026-09-02).

This revision is the pinned evidence horizon used to design this roadmap. It is **not** a claim that this commit remains the live project position. `MEMORY.md` alone owns live continuation, current blockers, selected work, and current verification.

## 1. Scope and outcome

This plan coordinates reusable study/relearning artifacts under `learning/`. It must eventually make the meaningful project recoverable as engineering understanding, including:

- product mission, decision boundary, evidence doctrine, uncertainty, provenance, and claim limits;
- the product-simulation pressures that shaped the decision model;
- important implementation stages, architecture transitions, mistakes, fixes, rejected/superseded directions, and unresolved boundaries;
- current product responsibilities, data/state/control flows, important syntax/APIs/tools, and tests/proof limits;
- representative real UpgradePilot cases rather than detached toy tutorials;
- experiments and advanced-method evaluation without presenting experimental behavior as adopted product architecture;
- the AI-assisted engineering and governance system used to operate, evaluate, and learn from the project.

The roadmap is organized by coherent engineering responsibility and transition, not by date, file count, conversation count, or one artifact per historical step.

This plan does not authorize product/source/test repair. If learning-artifact work exposes a material correctness, ownership, rationale, or proof question, use a bounded Repository-Audit composition and stop before repair unless Build is separately authorized.

## 2. Authoring and evidence rules

For every group:

1. use `.agents/skills/upgradepilot-learning-artifact/SKILL.md` and `learning/README.md` as the artifact-authoring owners;
2. establish a group-specific current or historical evidence horizon before writing;
3. ground current truth in the smallest sufficient chain of canonical owners → current source/tests/evidence → directly relevant history → representative real case/flow;
4. use working-memory/history only when it materially explains implementation path, rationale, failures, fixes, alternatives, or deferrals;
5. keep **current implementation fact**, **evidenced rationale**, **engineering judgment**, and **alternative/improvement** distinct;
6. never invent rationale for an existing mechanism; compose bounded Audit when material evaluation is required;
7. prefer one focused note; use a small ordered package only when genuinely distinct learning responsibilities would make one file hard to study or revisit;
8. for code-bearing material, record the relevant source/test revision or otherwise explicit evidence horizon.

Complex groups must use Planning/Design proportionately before authoring when decomposition, evidence selection, package shape, trust/failure coverage, or ordering remains materially non-trivial. Use the existing P0-P3 planning model; do **not** create a durable sub-plan for every group. P1/P2 is justified only when the group itself needs durable coordination; P3 requires genuinely separate owners/gates/proof obligations.

## 3. Ordered learning groups

### Group 1 — Product thesis, evidence model, and authority model

**Learning responsibility/outcome:** understand what UpgradePilot supports, what it refuses to claim, how evidence/provenance/uncertainty/abstention work, and how Charter/specification/ADR/plan/source/test/history differ as evidence and authority.

**Main anchors:** `PROJECT_CHARTER.md`; Core Pipeline, Minimum Useful Generality, and Product Decision Model specifications; only the governance/operating material needed to understand ownership and claim interpretation.

**Depth/shape:** **must master / own** evidence and claim boundaries; governance routing only operationally. Prefer **one focused note**.

**Dependency:** first; supplies the vocabulary used by all later groups.

### Group 2 — Product simulation to the decision model

**Learning responsibility/outcome:** reconstruct how real dependency-update cases exposed the need for completeness, impact candidates, applicability, investigation value, uncertainty, and a transparent baseline richer than version number plus CI status.

**Main anchors:** representative S001-S012 evidence rather than every case; `product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md`; cross-case synthesis/coverage pressure; decision-model handoffs; Product Decision Model specification; directly relevant history.

**Depth/shape:** must master the decision-model concepts; individual cases operationally. Prefer a **small two-note package**: concept/pressure synthesis + representative case walkthroughs.

**Dependency:** Group 1.

### Group 3 — Early implementation, experiments, and the clean-slate B2 reset

**Learning responsibility/outcome:** understand the early Python/runtime-contract and M2 semantic-extraction direction, the superseded report-first orientation, and why B2 was rebuilt around clearer responsibilities.

**Main anchors:** M2 S01/S02/S03 plans/artifacts; ADR-0001, ADR-0002, ADR-0003; B1 source/test reconciliation and responsibility-freeze evidence; historical source/archive/tests only where needed.

**Depth/shape:** implementation-adjacent; own the architectural lesson rather than obsolete source details. Prefer **one transition note**.

**Dependency:** Groups 1-2.

### Group 4 — Dependency identity, version transition, and upstream evidence

**Learning responsibility/outcome:** trace how UpgradePilot establishes what package changed, the exact old/proposed versions, the relevant upstream interval, and structured/semantic upstream evidence.

**Main anchors:** `package_identity.py`; dependency `versioning.py`/`change.py`; PyPI release evidence; `upstream/interval.py`, `interval_evidence.py`, `repository.py`, `changelog.py`, `claim.py`, `support_drop.py`, `support_drop_extractor.py`; focused tests; ADR-0004/0005/0006; relevant B2 Step plans and live-proof tools.

**Concepts/tools:** package normalization, PEP 440/version objects, version intervals, source identity, provenance, deterministic extraction, bounded semantic extraction, API/provider boundaries.

**Depth/shape:** **must master / own** the evidence/data flow; incidental library/API details lookup-level. Prefer **two focused notes**: dependency/version/interval + upstream/semantic evidence.

**Dependency:** Groups 1-3.

### Group 5 — Dependency declarations, environments, and uv reachability

**Learning responsibility/outcome:** understand how repository declarations and lock structure establish whether and under what conditions the changed dependency belongs to an admitted target environment.

**Main anchors:** dependency `pyproject.py`, `requirements.py`, `direct_install.py`, `uv_lock_structure.py`, `uv_lock.py`, `uv_reachability.py`, `environment.py`, `environment_membership.py`, `environment_selection.py`, relevant analysis/tests; source-evidence/uv-reachability reconciliation plans and directly related history.

**Concepts/tools:** TOML, requirement syntax, dependency graphs, roots/edges/reachability, markers, direct/transitive membership, conditional evidence, unresolved states, source-vs-lock authority.

**Depth/shape:** **must master / own**, especially `uv_lock_structure → uv_lock → uv_reachability → environment membership/selection`. Use **2-3 notes only if needed**; do not split by source file.

**Dependency:** Group 4.

### Group 6 — Target Python and target-environment evidence resolution

**Learning responsibility/outcome:** understand how exact target-side Python/environment evidence is acquired/interpreted and then used to resolve applicability propositions without substituting UpgradePilot's own runtime environment.

**Main anchors:** `target/python.py`, `python_specifier.py`, `relevance.py`, `artifact_environment.py`; repository/provider evidence and tests; target-Python plans; target-environment product-simulation handoffs; `learning/2026-09-02-target-python-evidence-resolution/` as a reuse candidate.

**Concepts/tools:** Python version specifiers, `packaging.specifiers`, typed evidence problems, unavailable/inaccessible evidence, proposition resolution, target-vs-tool runtime separation.

**Depth/shape:** must master proposition/data flow; packaging syntax operationally. Prefer **one focused note**, but reuse the existing September snapshot if group-entry review shows it already satisfies the responsibility at the required horizon.

**Dependency:** Groups 4-5.

### Group 7 — Artifact serviceability and wheel-compatibility applicability

**Learning responsibility/outcome:** explicitly learn the artifact-serviceability responsibility: exact old/proposed release inventories can establish a target-agnostic loss-of-wheel-capability candidate, while target-owned wheel-compatibility evidence is separately required to establish or refute applicability.

**Main anchors:** `src/upgradepilot/impact/artifact_serviceability.py`; `tests/test_artifact_serviceability.py`; PyPI `PackageReleaseEvidence`; target artifact-environment evidence; impact applicability owners/tests; related August target-evidence/serviceability history and product-simulation handoffs.

**Concepts/tools:** wheel filenames and compatibility tags, `packaging.tags.Tag`, `parse_wheel_filename`, set/intersection reasoning, source-distribution fallback, target-agnostic candidate vs target applicability, repository/revision identity checks, evidence-problem states, proposition/path evaluation and explicit non-claims.

**Depth/shape:** **must master / own** the evidence separation and applicability logic; wheel-parser/API details operationally. Prefer **one focused note**; split only if historical evolution and current mechanism cannot remain studyable together.

**Dependency:** Groups 4 and 6.

### Group 8 — CI and workflow evidence without treating CI as a verdict

**Learning responsibility/outcome:** understand static GitHub Actions workflow modelling, dependency exercise/environment evidence, and the exact proof/non-proof boundary of available CI.

**Main anchors:** `src/upgradepilot/ci/`; GitHub provider layer; dependency/workflow integration; ADR-0008; CI/dependency-consumption plans; representative S003 failing-CI and S011 optional-extra evidence; focused tests.

**Concepts/tools:** GitHub Actions YAML, jobs/steps/matrices, static workflow analysis, exercised behavior vs safety, missing/partial coverage, optional extras and proof gaps.

**Depth/shape:** must master the proof boundary; parser/models implementation-adjacent. Prefer **one substantial focused note**.

**Dependency:** Groups 5-7.

### Group 9 — Impact, applicability, investigation, and deterministic decision formation

**Learning responsibility/outcome:** understand how assembled evidence becomes structured impact candidates, applicability judgments, investigation choices, bounded recommendation/abstention, and explicit uncertainty rather than an opaque score.

**Main anchors:** `src/upgradepilot/impact/`; `investigation.py`; Product Decision Model specification; impact/applicability/investigation foundation and transparent-decision plans; focused tests; representative decision-model pressure tests/history.

**Concepts:** candidate generation, proposition/path logic, evidence completeness, investigation value, deterministic reasoning, uncertainty propagation, recommendation vs evidence fact, abstention.

**Depth/shape:** **must master / own**. Prefer **two notes**: impact/applicability/investigation + deterministic decision/proof limits.

**Dependency:** Groups 4-8.

### Group 10 — Real product composition: public PR to evidence-backed output

**Learning responsibility/outcome:** trace the current application control/data flow across providers and domain responsibilities, including a normal path and at least one degraded/unresolved path.

**Main anchors:** `cli.py`, `__main__.py`, GitHub/PyPI providers, dependency/upstream/target/CI/impact/investigation composition, `json_contract.py`, repository/path utilities, integration tests, current S001 plus a distinct degraded/proof-boundary case.

**Concepts/tools:** composition boundaries, producer → transformer → consumer flow, typed errors/problems, serialization/JSON contracts, CLI boundary, deterministic output and degradation.

**Depth/shape:** must master the end-to-end path; CLI/incidental syntax lookup-level. Prefer **one end-to-end walkthrough**.

**Dependency:** Groups 4-9.

### Group 11 — Architecture evolution, proof strategy, and engineering corrections

**Learning responsibility/outcome:** understand why major responsibility boundaries and proof structures changed, including the B2 reset, responsibility-based subpackages, source/test reconciliation, naming/clarity refinements, cross-responsibility composition, and selected regressions/fixes.

**Main anchors:** ADR-0003 and ADR-0007; source-code-structure and cross-responsibility reconciliation plans; Naming Clarity specification; B1 reconciliation; representative working memories/regressions/tests; archived implementation only when it explains a material transition.

**Concepts:** cohesion/coupling, ownership, refactoring/migration, test responsibility, unit vs boundary/integration proof, source clarity, deterministic enforcement, over-/under-engineering.

**Depth/shape:** implementation-adjacent / engineering-ownership depth. Prefer **one retrospective/design note**.

**Dependency:** after current product mechanics and composition are understood.

### Group 12 — B2/X1 bounded agentic evidence-gap planning and orchestration

**Learning responsibility/outcome:** understand the admitted agentic experiment through the actual evidence horizon available at authoring: model-visible planning context, structured decision, model-hidden authority, deterministic rebinding/admission, local-model boundary, bounded execution, evolving state, budget/consumption semantics, operational failure, trace/replay, and no-action outcomes.

**Main anchors:** current B2/X1 plans and depth map; `experiments/` and `experiments/tests/`; directly relevant R2-R4 working memories; B2/X1 product-simulation transfer/pressure evidence; `learning/2026-09-01-b2-x1-r4-evidence-gap-planner/` and later learning snapshots as reuse candidates.

**Concepts/tools:** Pydantic structured outputs, LLM trust boundaries, prompt/context projection, action descriptor vs execution authority, stale-action/precondition checks, immutable state replacement, state machines, budgets, semantic consumption vs operational failure, LM Studio/OpenAI-compatible API, trace/replay and framework-comparison discipline.

**Depth/shape:** must master the trust/authority and state/control-flow architecture; local-model API details operationally. Prefer a **small package**. Reuse current A1-A3 material where sufficient and add only genuinely missing current slices such as A4/state-transition learning.

**Dependency:** after the deterministic product responsibilities the experiment orchestrates.

**Future boundary:** do not pre-author LangGraph/LangChain/adoption conclusions. Add or revise comparison learning only after the project produces evidence that earns it.

### Group 13 — AI-assisted engineering and UpgradePilot governance system

**Learning responsibility/outcome:** learn the engineering system used to build UpgradePilot with AI assistance: responsibility/authority routing, Learning-by-Doing, operation Skills, progressive disclosure/context control, Planning/Audit/Build separation, working-memory/live-memory boundaries, provenance markers, artifact ownership, behavioral governance evaluation, deterministic checks, and how this system evolved to reduce drift without creating ceremony.

**Main anchors:** root/local `AGENTS.md`; `OPERATING_GUIDE.md`; `docs/README.md`; `plans/README.md`; `learning/README.md`; admitted `.agents/skills/`; representative governance-refinement plans/audits/history; `tools/agent-governance/README.md`, `governance_doctor.py`, operation/consistency/learning-artifact case sets and their validation evidence.

**Concepts/tools:** AI-assisted engineering ownership vs blind/vibe coding, instruction hierarchy, canonical ownership, operation routing, context economics/progressive disclosure, deterministic vs behavioral enforcement, eval cases, provenance markers, auditability, Ceremony Tax, assistance fading and learning transfer.

**Depth/shape:** must master the governance architecture and engineering rationale; understand the evaluation harness operationally. Prefer a **two-note package**: AI-assisted engineering/learning workflow + governance-system architecture/evaluation.

**Dependency:** final group, so it can use concrete examples from the product and experiment journey rather than becoming an abstract governance tutorial.

**Anti-duplication with Group 1:** Group 1 teaches only the minimum authority/evidence model needed to interpret UpgradePilot engineering. Group 13 teaches the governance system itself as an engineered AI-assistance mechanism.

## 4. Existing-artifact disposition

### Reuse/reference first

Treat these as high-value frozen evidence or possible direct coverage; inspect them at the relevant group boundary before creating overlapping material:

- `learning/2026-08-10-seven-concept-foundation-pre-a-c-implementation.md`;
- `learning/2026-08-10-product-decision-model-a-b-c-mastery-note.md`;
- `learning/2026-08-15-tranche1-real-case-code-flows/`;
- `learning/2026-08-17-Cluster1-5-B2 Dependency Environment and CI Consumption Evidence.md`;
- `learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/`;
- `learning/2026-09-01-b2-x1-r4-evidence-gap-planner/`;
- `learning/2026-09-02-target-python-evidence-resolution/`;
- `learning/2026-07-24-b2-public-pr-through-ci-authority/`;
- `learning/b2-pr-acquisition-and-pinned-extraction/`;
- `learning/bounded-llm-semantic-extraction.md`;
- `learning/m2-s02/`;
- directly relevant `learning/product-simulation/` and `learning/concepts/` material.

Reuse may mean direct study, a cited historical snapshot, or satisfying part/all of a group when the existing artifact already has the required responsibility, evidence horizon, depth, and QA. Do not create a new artifact merely to give the fresh roadmap uniform filenames.

### Frozen/superseded snapshots

- `learning/m2-s03/` is a superseded report-first orientation and should remain historical learning evidence, not current architecture.
- Earlier concept/code-flow snapshots whose mechanics have materially changed remain frozen at their recorded horizons.
- Do not silently modernize historical snapshots. Correct them only under the Learning-Artifact snapshot policy for factual error, unsafe instruction, or broken reference.

### Genuinely new work

Author new material only for roadmap responsibilities not already satisfied at the needed horizon. Expected new coverage includes the fresh whole-project spine, current responsibility syntheses where old snapshots are stale, explicit artifact-serviceability learning, the current end-to-end product flow, architecture/proof retrospective, missing B2/X1 transition slices, and the final AI-assisted engineering/governance-system group.

At group entry, an existing artifact may eliminate or narrow a planned new note.

## 5. One-group-at-a-time execution and QA

Do not batch-author the roadmap.

For one selected group:

```text
re-anchor group-specific owners/evidence
→ reassess reuse vs new artifact
→ use proportional Planning/Design if the group remains non-trivial
→ retrieve only directly relevant history/cases
→ compose bounded Audit if rationale/correctness is materially uncertain
→ author the smallest complete note/package
→ QA against the Learning-Artifact procedure
→ preserve/commit the bounded group change
→ stop before the next group unless Ali explicitly continues
```

QA must check proportionately:

- accurate against the pinned/current group evidence horizon;
- authority/current truth/history separated;
- no invented rationale;
- representative real UpgradePilot flow/case used where available;
- important responsibility/non-responsibility, logic, states, failure paths, trust boundaries and trade-offs covered;
- material syntax/APIs/tools taught at the planned depth, not equally/exhaustively;
- relevant tests/proof and explicit non-proof/claim limits included;
- known mistakes/fixes/alternatives/unresolved questions preserved where educationally material;
- artifact size remains studyable;
- source/history anchors are sufficient;
- a useful fast-relearning route exists;
- no accidental product/plan/spec/ADR mutation;
- no mastery claim from artifact existence.

## 6. Reassessment when the project advances

The initial roadmap-analysis horizon remains frozen as provenance. Each later code-bearing group gets its own evidence horizon at authoring.

Before authoring a later group:

- if relevant source/tests/specifications/ADRs or accepted experimental evidence changed materially, re-run proportional Planning/Design for that group's coverage/shape before writing;
- if the change only affects details inside the same responsibility, update the new group's current explanation without rewriting older snapshots;
- if a responsibility was replaced, teach the transition and current owner rather than presenting obsolete mechanics as current;
- if an existing newer learning artifact now fully covers the group, reuse it and avoid duplication;
- if project evolution creates a genuinely new whole-project learning responsibility, add/narrow/reorder roadmap coverage only when needed to preserve complete meaningful coverage, not merely because a new file or feature exists;
- if a change materially invalidates the roadmap's decomposition/order, update this plan through Planning/Design rather than letting individual learning notes silently redefine the roadmap.

Experiment/framework outcomes are evidence-bounded: never teach a planned comparison, adoption, rejection, or future architecture as established before the corresponding evidence exists.

## 7. Completion, stop lines, and prohibited ceremony

The whole responsibility is complete when every meaningful group is either:

1. satisfied by a QA'd new artifact/package; or
2. explicitly satisfied by a still-adequate existing artifact/reference at the required learning responsibility and horizon.

Coverage completeness is about meaningful engineering responsibilities, transitions, proof/failure boundaries, and representative real flows—not file-by-file exhaustiveness.

Stop/prohibited boundaries:

- do not use this plan as live project-state authority or duplicate `MEMORY.md`;
- do not author more than one roadmap group in one bounded authoring operation unless Ali explicitly requests continuation;
- do not create an artifact per file, date, case, plan, ADR, or working-memory record;
- do not create package indexes, contracts, depth maps, glossaries, quizzes, learning memories, trackers, or sub-plans merely for symmetry;
- do not create a plan family for this roadmap while one plan remains sufficient;
- do not scan or summarize all working-memory/history; retrieve only evidence material to the selected responsibility;
- do not copy source/specifications/plans/history wholesale into learning notes;
- do not rewrite frozen snapshots to make the set look uniform;
- do not duplicate an existing artifact that already satisfies the selected responsibility;
- do not repair product/experiment/governance source during learning-artifact authoring without separate authorization;
- do not speculate beyond the evidence horizon;
- do not let governance learning dominate or replace the product-engineering journey.

**Immediate plan stop:** creation/verification of this roadmap plan does not authorize Group 1 authoring. Group 1 begins only as a separately selected learning-artifact responsibility.
