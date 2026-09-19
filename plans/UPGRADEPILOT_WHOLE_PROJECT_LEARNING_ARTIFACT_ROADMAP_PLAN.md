# UpgradePilot Whole-Project Learning-Artifact Roadmap Plan

**Plan responsibility:** coordinate the smallest sufficient sequence for a fresh, high-quality learning-artifact set covering the meaningful UpgradePilot engineering journey from project foundations through the evidence horizon available when each group is authored.

**Initial roadmap-analysis evidence horizon:** `main@91158b0925037cdde4142efc52a8a86d2950e9a6` (2026-09-02).

**Later roadmap-extension evidence horizon:** `main@d9c637b6df4d9449683d7f67d8859a4e18fd132f` (2026-09-06) for the bounded evidence-gap planner / LangGraph / framework-deferral learning responsibility.

**Current roadmap-reassessment evidence horizon:** `main@dbdae3a5e76c480541a45a82987ab632783c1d47` (2026-09-19) for the parser-backed workflow-command architecture, static-consumer migration, occurrence-level runtime strengthening, artifact/Target integration state, current maintainer-action synthesis boundary, and source-verified end-to-end product-flow reconstruction.

The initial roadmap horizon remains pinned provenance for the original decomposition. Later group-specific extensions may use later evidence when project progress creates a genuinely new learning responsibility or completes evidence that the original roadmap deliberately deferred. The 2026-09-19 reassessment does not silently modernize older frozen artifacts; it identifies which roadmap responsibilities are already satisfied by historical snapshots and which now require a new current artifact. This plan is **not** a claim that any horizon remains the live project position. `MEMORY.md` alone owns live continuation, current blockers, selected work, and current verification.

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

**Learning responsibility/outcome:** explicitly learn the artifact-serviceability responsibility from current source: exact old/proposed release inventories can establish a target-agnostic loss-of-wheel-capability candidate; exact target-owned wheel-compatibility evidence is a separate stronger proposition required to establish or refute applicability; partial static Target environment facts must not be promoted into exact supported wheel tags.

**Main anchors:** `src/upgradepilot/impact/artifact_serviceability.py`; `tests/test_artifact_serviceability.py`; PyPI `PackageReleaseEvidence`; `src/upgradepilot/target/artifact_environment.py`; `src/upgradepilot/investigation.py`; target artifact-environment tests/integration tests; the current-system audit's artifact/Target findings; related target-evidence/serviceability history and representative product-simulation pressure.

**Concepts/tools:** wheel filenames and compatibility tags, `packaging.tags.Tag`, `parse_wheel_filename`, set/intersection reasoning, source-distribution fallback, target-agnostic candidate vs target applicability, repository/revision identity checks, evidence-problem states, exact target-witness provenance, and the distinction between an implemented compatibility-evidence contract and a normally reachable producer.

**Current reassessment boundary:** the normal application can build the artifact-serviceability candidate and partial static Target environment results, but it does not currently produce exact `TargetWheelCompatibilityEvidence` or pass such a witness into normal artifact applicability evaluation. The learning artifact must teach this as a current product boundary rather than a hypothetical future design.

**Depth/shape:** **must master / own** the evidence separation, applicability logic, normal producer/composition path, and proof/non-proof boundary; wheel-parser/API details operationally. Prefer **one focused current note** with one representative candidate path and one target-witness applicability path.

**Dependency:** Groups 4 and 6.

### Group 8 — CI and workflow evidence without treating CI as a verdict

**Learning responsibility/outcome:** understand the current CI evidence architecture after the September command-correctness work: provider-owned workflow/shell structure, parser-backed static command occurrences, dependency/project/invocation consumers, canonical occurrence identity and bounded static ordering, exact static↔runtime step correlation, occurrence-level runtime-strengthening eligibility/composition, and the exact proof/non-proof boundary of the resulting CI states.

**Main anchors:** `src/upgradepilot/github/workflow_definition.py`; `workflow_command_shell.py`; `workflow_command_analysis.py`; `workflow_command_location.py`; `src/upgradepilot/dependency/direct_install.py`; `environment_selection.py`; `src/upgradepilot/ci/consumption.py`; `workflow_commands.py`; `workflow_runtime_correlation.py`; `runtime_strengthening.py`; `dependency_exercise.py`; ADR-0009; the completed static-command/runtime-strengthening plan; focused tests; Cycle-1/2/3 working-memory/proof only where it materially explains the correction; representative S001/S002 positive pressure and S004 deferred short-circuit pressure.

**Concepts/tools:** effective shell context; syntax family vs execution profile; Tree-sitter as parser substrate; parser-neutral command IR; source span/order vs execution semantics; `StaticCommandLocation`; structural context; whole-step relation; static ordering; exact workflow/job/step identity; `eligible | ineligible | unresolved`; runtime correlation; `supported_not_correlated` vs `supported_runtime_correlated`; static/runtime proof limits; no regex/textual positive fallback after parser uncertainty.

**Depth/shape:** **must master / own** the proposition boundaries and complete producer → consumer → runtime-strengthening flow; parser-library node/API details remain lookup-level. Prefer a **two-note current package** because two distinct responsibilities now exist:
1. **Parser-backed static workflow-command evidence and consumer composition** — shell context, parsed occurrences, canonical command identity, direct requirements/project-environment/package-invocation consumers, and bounded static ordering.
2. **Occurrence-level runtime strengthening and CI proof boundaries** — workflow step correlation, structural/profile eligibility, exact occurrence handoff, runtime composition/aggregation, S001/S002/S004, and explicit non-claims.

The frozen `learning/2026-09-12-ci-static-runtime-correlation-bridge.md` remains useful historical prerequisite material but does not satisfy this current group by itself.

**Dependency:** Groups 5-7.

### Group 9 — Impact, applicability, investigation, and maintainer-action synthesis

**Learning responsibility/outcome:** understand how assembled evidence becomes structured impact candidates, applicability judgments, bounded investigation choices, typed `PublicPullRequestInvestigation`, and action-relative maintainer-action permission or abstention without collapsing evidence into an opaque score.

**Main anchors:** `src/upgradepilot/impact/`; `src/upgradepilot/investigation.py`; `src/upgradepilot/maintainer_action.py`; Product Decision Model specification; Maintainer Action Synthesis specification; parent synthesis plan; current-system audit; focused investigation/synthesis tests; representative decision-model/product-simulation pressure.

**Concepts:** candidate generation, proposition/path logic, mechanism-specific applicability, evidence completeness, investigation value, normal-producer reachability, action-relative sufficiency, positive permission, defeaters, residual uncertainty, deterministic synthesis, recommendation vs evidence fact, and abstention as an explicit honest outcome rather than a generic fallback.

**2026-09-19 internal stability reassessment:** this group is intentionally split at its existing two-note boundary.

1. **Impact / applicability / mechanism-specific investigation** — stable enough to author now. The generic applicability contract, Python-support-drop candidate/evaluation/target-investigation flow, typed investigation composition, and the artifact-serviceability transfer example are source/test-owned and are not the part currently being redesigned by the active synthesis audit.
2. **Action-relative maintainer-action synthesis / permission / proof limits** — remains gated. Stable specification semantics exist, but the current evaluator is abstention-only and the active end-to-end audit is still validating uncertainty preservation, normal-producer reachability, and which non-abstention premises can actually be earned.

Do not let Note 1 speculate about Note 2. It should stop explicitly at the boundary `mechanism-specific impact/applicability/investigation → later overall sufficiency and maintainer-action synthesis`.

**Depth/shape:** **must master / own**. Use **two notes**:
1. current impact/applicability/investigation model and application composition;
2. later action-relative synthesis/permission/proof-limits note only after its stability gate clears.

**Dependency:** Groups 4-8.

### Group 10 — Real product composition: public PR to evidence-backed output

**Learning responsibility/outcome:** trace the verified current application control/data flow across providers and domain responsibilities, including one representative normal path and at least one degraded/branch-stopping path, while keeping current evidence-report presentation separate from standalone maintainer-action synthesis.

**Main anchors:** `src/upgradepilot/cli.py`; `__main__.py`; GitHub/PyPI providers; dependency/upstream/target/CI/impact/investigation composition; `src/upgradepilot/maintainer_action.py`; `json_contract.py`; repository/path utilities; integration tests; the end-to-end product-flow learning/evidence-to-action execution plan; current-system audit; source-verified product-flow working memory; a representative S001-shaped path plus a distinct degraded/proof-boundary path.

**Concepts/tools:** producer → transformation → consumer composition; typed success/problem states; exact identity/provenance handoff; normal-path reachability; branch-stopping uncertainty; serialization/JSON contracts; CLI presentation; and the distinction between:
```text
current CLI → investigation evidence report
standalone investigation → maintainer-action synthesis
```
until source proves those paths have been integrated.

**Authoring gate:** this artifact is intentionally authored only after the current product-flow reconstruction has source-verified the major seams and proof limits. The execution plan already requires this durable artifact after reconstruction; this roadmap references that responsibility rather than creating a competing end-to-end learning process.

**Depth/shape:** must master the end-to-end path and important evidence-strength transitions; CLI/incidental syntax lookup-level. Prefer **one end-to-end walkthrough**.

**Dependency:** Groups 4-9.

### Group 11 — Architecture evolution, proof strategy, and engineering corrections

**Learning responsibility/outcome:** understand why major responsibility boundaries and proof structures changed, including the B2 reset, responsibility-based subpackages, source/test reconciliation, naming/clarity refinements, cross-responsibility composition, selected regressions/fixes, and the later correction from duplicated textual shell splitting to parser-backed shared command structure plus bounded occurrence-level runtime strengthening.

**Main anchors:** ADR-0003, ADR-0007, and ADR-0009; source-code-structure and cross-responsibility reconciliation plans; Naming Clarity specification; B1 reconciliation; the completed static workflow command analysis/runtime-strengthening plan; representative Cycle-1/2/3 working memories and hosted proof; current-system audit; archived implementation only when it explains a material transition.

**Concepts:** cohesion/coupling, earliest sufficient owner, shared producer vs consumer semantics, refactoring/migration, parser substrate vs product-owned IR, identity vs ordering vs execution proof, static vs runtime authority, test responsibility, unit vs boundary/integration/hosted proof, source clarity, deterministic enforcement, and evidence-driven decisions to prefer a larger foundational correction over repeated local patches.

**Depth/shape:** implementation-adjacent / engineering-ownership depth. Prefer **one retrospective/design note** after current product mechanics and composition are understood.

**Dependency:** after current product mechanics and composition are understood.

### Group 12 — Bounded evidence-gap planning, deterministic execution authority, orchestration, and framework evaluation

**Learning responsibility/outcome:** understand the bounded agentic evidence-gap responsibility through the evidence actually earned by 2026-09-06: model-visible planning context, structured decision, model-hidden exact authority, post-model deterministic rebinding/admission, local-model boundary, bounded execution, immutable state consequence, budget/consumption semantics, no-action outcomes, semantic-result versus operational-failure behavior, explicit trace/replay in the ordinary-Python control, independent LangGraph orchestration design, fair cross-implementation semantic comparison, real pydantic execution proof, framework value/cost findings, and the product-driven reason richer framework work was deferred.

**Main anchors:**

- `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_AND_EVALUATION_PLAN.md`;
- `plans/LANGGRAPH_BOUNDED_EVIDENCE_GAP_PLANNER_INDEPENDENT_DESIGN_IMPLEMENTATION_AND_COMPARISON_PLAN.md`;
- `plans/BOUNDED_EVIDENCE_GAP_PLANNER_IMPLEMENTATION_COMPARISON_LEARNING_DEPTH_AND_REENTRY_MAP.md`;
- current semantic experiment owners under `experiments/` and `experiments/langgraph/`, plus focused tests under `experiments/tests/`;
- the ordinary-Python execution/replay closure, LangGraph representation-coupling correction, controlled semantic-comparison proof, real pydantic LangGraph executable proof, LangGraph value/cost findings, and framework-deferral working memories;
- `learning/2026-09-01-b2-x1-r4-evidence-gap-planner/` and `learning/2026-09-02-target-python-evidence-resolution/` as frozen prerequisite/reuse snapshots rather than material to rewrite.

**Concepts/tools:**

```text
bounded model observation / context projection
structured output != authority
proposal != deterministic execution authorization
post-model current-state rebinding / time-of-check-to-time-of-use pressure
immutable state transition
budget spent != action consumed
semantic/domain problem != operational/provider failure
trace != replay != re-execution
framework-independent requirement vs implementation representation
Graph API vs Functional API reasoning
Graph State vs Runtime Context vs product/domain truth
explicit plan → authorize → investigate → conclude topology
control behavior reuse behind adapters vs architecture coupling
semantic equivalence != implementation equality
framework-neutral semantic projection
real smoke test vs controlled/unit proof
runtime node-path observability
currently exercised framework value vs credible future value vs speculative value
framework adoption/dependency cost
product-driven framework re-entry triggers
```

**Depth/shape:** **must master / own** the trust/authority, execution/state, failure, and semantic-comparison principles; understand the tested LangGraph Graph API architecture and runtime boundaries operationally/architecturally; keep exact LangGraph/LangChain API syntax lookup-assisted. Prefer a **two-note current package/slice**, while reusing the September 1 and target-Python snapshots rather than duplicating them:

1. **Bounded evidence-gap execution, state consequence, trace/replay, and framework-neutral semantic proof** — complete the ordinary-Python execution/state responsibility that the September 1 notes intentionally stopped before, then teach the cross-implementation comparison contract.
2. **Independent LangGraph orchestration, real pydantic proof, framework value/cost, and deferral** — teach the independent design, representation-coupling mistake/correction, tested Graph API mechanics, real runtime proof, what LangGraph did/did not earn, and why executable LangChain/richer LangGraph work is deferred.

The notes should preserve the engineering story where it materially improves learning, especially:

```text
ordinary-Python responsibility completed
→ independent framework design attempted
→ over-reuse of control representations detected
→ control behavior isolated behind adapters
→ bounded LangGraph implementation proven
→ semantic comparison normalized rather than coupling internals
→ real pydantic path proven
→ framework value/cost evaluated
→ higher-level LangChain experiment deferred because one planner-selectable action does not create enough real agent-loop/tool-choice pressure
```

**Dependency:** after the deterministic product responsibilities the experiment orchestrates. Existing September 1 planner and September 2 target-Python learning snapshots are direct prerequisites/reuse material for this group.

**Current evidence-bounded disposition to teach, not overstate:**

```text
ordinary Python
→ proven bounded control/reference asset

LangGraph
→ proven viable bounded orchestration experiment
→ explicit topology/observability value
→ real state/type/dependency ceremony
→ no product adoption decision
→ further expansion deferred

LangChain
→ higher-level agent/tool/middleware concepts are relevant to the credible future system
→ no executable integration has been earned yet
→ no three-way framework verdict exists
```

**Framework re-entry boundary:** richer LangGraph expansion, executable LangChain experimentation, and broader framework comparison should re-enter learning only when the product has multiple independently useful planner-selectable investigation capabilities and real states where choice/order/history/failure/budget pressure makes fixed deterministic orchestration materially brittle, duplicated, combinatorial, or semantically contextual. Do not manufacture a second action or generic tool loop for framework exposure.

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

- `learning/2026-09-12-ci-static-runtime-correlation-bridge.md` — retain as the frozen first static↔runtime bridge snapshot; current Group 8 requires additional post-ADR-0009/Cycle-1–3 material rather than rewriting this file;
- `learning/2026-09-07-target-artifact-environment-evidence/` — retain as the frozen static Target-evidence snapshot; its core proof boundary remains valuable while its pre-composition application horizon is historical;
- `learning/2026-09-07-dependency-environment-and-uv-reachability/` — retain as the frozen source-context/selection/uv-reachability package; current parser-backed command semantics should be taught in new Group 8 material rather than silently inserted here;
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

Author new material only for roadmap responsibilities not already satisfied at the needed horizon.

The 2026-09-19 roadmap reassessment establishes this coverage disposition:

```text
Groups 1–4
→ usable existing September 2 / earlier roadmap artifacts

Group 5
→ usable September 7 dependency-environment / uv-reachability package
→ parser-backed command changes belong to Group 8, not a rewrite of Group 5

Group 6
→ usable target-Python + static Target artifact-environment snapshots
→ application composition has advanced, but the old files remain frozen history

Group 7
→ SATISFIED at the 2026-09-19 reassessment horizon by
  learning/2026-09-19-artifact-serviceability-and-exact-target-wheel-applicability.md

Group 8
→ SATISFIED at the 2026-09-19 reassessment horizon by
  learning/2026-09-19-parser-backed-ci-command-evidence-and-runtime-strengthening/
→ the September 12 bridge remains a historical prerequisite snapshot, not current coverage by itself

Groups 9–10
→ NEXT UNSATISFIED ROADMAP RESPONSIBILITIES
→ materially evolving under the current synthesis/product-flow reconstruction
→ author only after the selected source/test horizon stabilizes

Group 11
→ later retrospective should include ADR-0009 and the three-cycle correction

Group 12
→ usable September 6 bounded-evidence-gap / LangGraph package already exists

Group 13
→ remains future governance/AI-assisted-engineering learning coverage
```

Accordingly, Groups 7–8 are satisfied at this evidence horizon. Groups 9–10 are the next unsatisfied roadmap responsibilities, but their explicit stability gate remains: do not freeze those artifacts while the active product-flow/synthesis responsibility is still changing.

At any group entry, newer evidence may eliminate, narrow, split, or defer a planned note; use the reassessment rules rather than creating artifacts for roadmap symmetry.

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

**Roadmap authoring boundary after the 2026-09-19 reassessment:** updating this plan does not itself authorize product/source/test repair. When learning-artifact authoring is separately selected, execute one unsatisfied group at a time through the Learning-Artifact procedure. Groups 7–8 are now satisfied by the current artifacts named above; Groups 9–10 are next but retain their explicit stability gates above.

`UP-SKILL:upgradepilot-planning-design`