# AUDIT-008 — Current System End-to-End Evidence-to-Action Audit

**Date:** 2026-09-19  
**Inspected product-source baseline:** `0201069d91f2d2bc776b84616870fe0926386f3f`  
**Inspected pre-audit main head:** `45499223e75b64752de7d7ea275794154fcc1d94`  
**Primary trigger:** Ali explicitly requested a full current-system audit using the repository audit procedure before selecting the next UpgradePilot engineering responsibility.  
**Disposition:** preserve the strong evidence/provenance foundations; fix current admitted correctness/coordination defects before expanding product breadth; then select one action-critical producer/composition gap through the parent synthesis plan.  
**Authority:** non-controlling audit evidence. This file does not authorize source/test/spec/ADR/plan changes and does not replace `MEMORY.md` as live-state owner.

## 1. Audit question and scope

This audit asks:

> Given UpgradePilot's current accepted product semantics, implemented source/tests, observed proof, and normal application composition, what does the system reliably establish today, where does evidence stop or get lost, which current behaviors are incorrect versus deliberately conservative, and which missing capabilities actually block useful maintainer-action reachability?

This is a **cross-responsibility current-system audit**, not a line-by-line source review.

Included:

- project mission and claim boundary;
- core identity/provenance/trust invariants;
- dependency transition analysis;
- GitHub repository and exact-head CI acquisition;
- static/runtime CI evidence;
- PyPI/upstream evidence and bounded local semantic extraction;
- target and impact/applicability reasoning;
- normal application orchestration;
- maintainer-action synthesis;
- CLI/presentation boundary;
- deterministic/hosted proof state;
- current audit/live-state coordination where it materially affects continuation.

Excluded unless needed to interpret the current system:

- archived/superseded implementation history;
- experimental agentic orchestration as a product-runtime surface;
- broad product-simulation corpus review except where existing case pressure explains an accepted action boundary;
- speculative future architecture;
- new source/test implementation;
- fresh execution of target repositories or third-party code.

The audit applies the repository-audit Skill, `OPERATING_GUIDE.md`, the accepted specifications, the selected parent synthesis plan, current source/tests, and directly inspected hosted proof.

## 2. Evidence and revision basis

### 2.1 Product source correspondence

The inspected main product source is the same source/test implementation that received the final Cycle-3 hosted proof.

GitHub compare evidence shows:

- hosted proof commit `c5e3f08da8822fe4b80342d415640413009ab439` → product-source main `0201069d91f2d2bc776b84616870fe0926386f3f`: only plan/memory/working-memory files changed;
- `0201069d91f2d2bc776b84616870fe0926386f3f` → pre-audit main `45499223e75b64752de7d7ea275794154fcc1d94`: only `MEMORY.md` and the current working-memory record changed.

Therefore the directly inspected hosted result remains evidence for the current **product source/tests**, although it is not proof for later documentation changes or future product changes.

### 2.2 Hosted executable proof

Directly inspected GitHub Actions run:

- [Cycle 3 Phase B final proof — run 35448172928](https://github.com/motafegh/UpgradePilot/actions/runs/35448172928)
- checked revision: `c5e3f08da8822fe4b80342d415640413009ab439`;
- fresh Python: 3.12.14;
- package installation: PASS;
- `pip check`: PASS;
- installed CLI entry points: PASS;
- focused investigation suite: 15/15 PASS;
- Cycle-3 focused regression: 76/76 PASS;
- full deterministic product suite: 604/604 PASS;
- S001 sole-command boundary: eligible;
- S002 first-sequential Bash boundary: eligible;
- S004 `&&` short-circuit boundary: unresolved/deferred.

This proof establishes the tested installed-package and deterministic source behavior at that source revision. It does **not** establish live public acquisition reliability, live LM Studio semantic quality, exact installed dependency version in target CI, target wheel compatibility, candidate-discovery completeness, upgrade safety, or a maintainer-action permission.

## 3. Current owner map

The current responsibility chain is coherent at the artifact/authority level:

```text
PROJECT_CHARTER.md
→ product mission, supported maintainer outcome family, claim limits

docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md
→ identity, provenance, state/failure/trust invariants

docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md
→ technical impact candidate, applicability, investigation, stopping semantics

docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md
→ action-relative sufficiency and maintainer-action permission

plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md
→ current bounded execution/proof coordination

source + tests + observed runs
→ implemented truth

MEMORY.md
→ sole live-position owner
```

The principal normal runtime composition is:

```text
public GitHub dependency-update PR
→ frozen PR/base/head identity
→ exact dependency transition + dependency source contexts
→ exact-head GitHub Actions run/job/workflow evidence
→ static dependency consumption/direct exercise
→ bounded runtime strengthening
→ PyPI old/proposed release evidence
→ upstream repository / crossed releases / exact tagged changelog
→ bounded Python-support semantic extraction and deterministic admission
→ target Python relevance / Python-support impact
→ artifact-serviceability candidate
→ partial static Target artifact environment
→ typed PublicPullRequestInvestigation
```

The current CLI then renders the investigation evidence directly.

Separately:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ abstention-only MaintainerActionSynthesis
```

The CLI does **not** currently call that synthesis evaluator.

## 4. Findings

### AUDIT-008-F1 — Exact identity/provenance foundations are coherent and should be retained

**Classification:** accepted implementation strength / KEEP.

The current system has a strong exact-identity spine:

- PR identity freezes repository, PR, base SHA and head SHA;
- exact repository-file acquisition binds files to explicit immutable revisions;
- dependency analysis preserves exact source evidence/contexts;
- GitHub Actions acquisition filters exact PR head SHA and binds jobs to the captured workflow-run attempt;
- CI static evidence retains workflow path/revision/job/step/command occurrence;
- PyPI release evidence retains requested/published package/version, source URL, retrieval metadata and distribution records;
- upstream interval composition preserves repository, release interval, exact tag/changelog identity and source problems;
- impact candidates retain exact target repository/revision and exact dependency transition.

The Core Specification's `SNAP-001`, `PROV-001`, `STATE-001`, `FAIL-001` and related trust boundaries are visible in both source structure and focused tests.

**Consequence:** this is a real product asset. The next work should compose or extend these facts, not weaken exact identity merely to reach a stronger action.

**Disposition:** KEEP. Do not reopen closed exact-revision/run-attempt/command-identity work without concrete regression evidence.

**Primary evidence:**

- [core pipeline specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [GitHub PR acquisition](../src/upgradepilot/github/pull_request.py)
- [exact repository evidence](../src/upgradepilot/github/repository.py)
- [GitHub Actions acquisition](../src/upgradepilot/github/actions.py)
- [dependency analysis](../src/upgradepilot/dependency/analysis.py)
- [CI consumption](../src/upgradepilot/ci/consumption.py)
- [PyPI release evidence](../src/upgradepilot/pypi/release.py)
- [upstream interval](../src/upgradepilot/upstream/interval.py)
- [hosted proof](https://github.com/motafegh/UpgradePilot/actions/runs/35448172928)

---

### AUDIT-008-F2 — The implemented product is still an evidence-report system, not yet a complete maintainer-action product

**Classification:** intentional implementation incompleteness / NO DEFECT in itself.

Current source truth is:

```text
CLI
→ investigate_public_pull_request(...)
→ _print_investigation(...)
```

while the maintainer-action evaluator is separately callable and currently declares:

```python
type MaintainerAction = Literal["abstain"]
```

The evaluator deliberately withholds merge, targeted-check, investigate, block and defer until each positive permission has normal-producer proof.

This matches the README's current limitation and the parent plan. The system should not be criticized for failing to emit action classes that have not yet earned their prerequisites.

**Consequence:** CLI wiring is not the next product problem merely because the final product wants a recommendation. Wiring an abstention-only or under-grounded evaluator into presentation would not solve evidence sufficiency.

**Disposition:** KEEP the current separation while action reachability is audited. Integrate maintainer-action rendering only after the evaluator contract and at least the selected action path are sufficiently trustworthy, or after a separate explicit decision that abstention-only output is itself useful.

**Primary evidence:**

- [maintainer action evaluator](../src/upgradepilot/maintainer_action.py)
- [CLI](../src/upgradepilot/cli.py)
- [maintainer-action tests](../tests/test_maintainer_action.py)
- [CLI tests](../tests/test_cli.py)
- [parent synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)

---

### AUDIT-008-F3 — The current abstention evaluator can omit material residual uncertainty

**Classification:** implementation correctness / synthesis-contract gap.  
**Disposition:** FIX before relying on synthesis as the product's honest final interpretation layer.

This audit found a more fundamental issue than the earlier CI→Target candidate.

The accepted synthesis specification requires:

```text
abstention
→ preserve why stronger-looking alternatives were unavailable
→ preserve material residual uncertainty/conflicts
→ preserve trust/coverage limitations
```

Current `_material_residual_uncertainty(...)` in `maintainer_action.py` examines only a subset of the typed investigation:

- dependency change problem;
- CI coverage states other than the two supported states;
- unresolved/conflicted Python-support impact;
- unresolved/conflicted artifact-serviceability impact.

The typed `PublicPullRequestInvestigation` contains materially more possible failure/problem state, including:

- package release problems;
- upstream-repository problems;
- release-index/crossed-release problems;
- tag/changelog problems;
- upstream interval/source problems;
- support-drop claim problems;
- target-artifact-environment problems;
- conditional investigation state.

Some of these problems can stop a technical branch **before** a final impact assessment exists. In that shape, the current evaluator may return an empty or materially incomplete `residual_uncertainty` while only saying that non-abstention actions are not yet admitted.

A concrete current source/test shape already exists in `tests/test_investigation.py`: an upstream source problem can stop semantic/target/impact work while CI remains available. The current maintainer-action tests do not exercise that investigation shape.

This is not a demand that synthesis duplicate every lower-level field. The issue is narrower:

> material branch-stopping uncertainty that explains why stronger action permission cannot be evaluated must survive into the synthesis explanation.

**Consequence:** even the currently admitted `abstain` baseline can under-explain the evidence state. That conflicts with the accepted synthesis responsibility and should be corrected before new action permissions build on the evaluator.

**Smallest justified disposition:**

```text
trace branch-stopping investigation/problem states
→ identify which are materially action-relevant
→ preserve them in abstention reasons/residual uncertainty without duplicating domain semantics
→ prove with normal-shaped investigation fixtures and defeater cases
```

Do not redesign the entire investigation object or invent generic evidence graphs merely to fix this.

**Primary evidence:**

- [maintainer-action synthesis specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)
- [maintainer action evaluator](../src/upgradepilot/maintainer_action.py)
- [typed investigation](../src/upgradepilot/investigation.py)
- [investigation tests](../tests/test_investigation.py)
- [maintainer-action tests](../tests/test_maintainer_action.py)

---

### AUDIT-008-F4 — CI already owns an exact consuming-job relation that Target currently does not receive

**Classification:** available-but-not-composed evidence + deliberate conservative Target coverage.

`StaticDependencyConsumptionEvidence` already preserves:

- workflow path;
- workflow revision;
- exact `job_key`;
- step source index;
- dependency source path;
- package identity;
- command occurrence/context.

For artifact target composition, `_compose_target_artifact_environments(...)` uses supported direct-requirements consumption, validates workflow/source correspondence, then calls:

```text
interpret_target_artifact_environment(
    definition,
    dependency_source_file=...
)
```

It does **not** pass `consumption.job_key`.

Its relationship deduplication key also omits job:

```text
(workflow_revision, workflow_path, dependency_source_path)
```

Target then independently selects a job and intentionally accepts only one-job workflows; multiple jobs return `ambiguous_target_job_selection`.

The application test `test_multi_job_target_ambiguity_is_preserved_despite_ci_job_relevance` proves the exact current behavior.

**Consequence:** current Target can lose useful specificity already established by CI. This is not false-positive evidence—the system safely returns ambiguity—but it prevents static environment interpretation for common multi-job workflows.

**Disposition:** REASSESS as a bounded composition repair when Target/artifact reasoning is selected. A sound change must preserve exact workflow/revision/source/job binding and must not convert arbitrary job keys into Target authority.

This finding does **not** by itself justify making Target job-aware now, because the stronger artifact-applicability bottleneck in F5 still remains.

**Primary evidence:**

- [CI consumption evidence](../src/upgradepilot/ci/consumption.py)
- [application composition](../src/upgradepilot/investigation.py)
- [Target artifact environment](../src/upgradepilot/target/artifact_environment.py)
- [Target tests](../tests/test_target_artifact_environment.py)
- [application tests](../tests/test_investigation.py)

---

### AUDIT-008-F5 — Exact target wheel-compatibility evidence has a contract but no normal production producer

**Classification:** missing evidence producer / current architecture bottleneck.

Artifact-serviceability candidate generation correctly compares exact old/proposed published wheel inventories and preserves candidate applicability as unresolved without exact target compatibility.

The impact module already defines the stronger required input:

```python
TargetWheelCompatibilityEvidence(
    repository=...,
    revision=...,
    source=...,
    supported_tags=frozenset(...)
)
```

and validates repository/revision coherence.

However, current normal Target interpretation produces only partial static declarations such as:

- runner;
- configured Python version;
- static dependency-installation declaration;
- limitations.

It hard-codes:

```text
exact_wheel_compatibility_state = unresolved
```

and does not produce exact supported wheel tags.

Current application also evaluates `evaluate_artifact_serviceability_impact(candidate)` without target compatibility evidence. Static target-environment results are derived afterward and are not a substitute for the missing exact tag witness.

Focused artifact tests prove that manually constructed controlled `TargetWheelCompatibilityEvidence` can establish/refute applicability. Those fixtures prove the impact contract, **not** normal producer reachability.

**Consequence:** artifact-serviceability can detect a real published-wheel capability loss candidate but cannot currently prove whether that candidate applies to the exact target environment.

**Disposition:** candidate next producer responsibility **only if** artifact-serviceability is chosen as the decision-critical path. The design question must be exact:

> What trustworthy target observation can establish the target-supported wheel-tag set at the exact target revision/environment?

Do not infer exact tags from `runs-on` + `python-version`, do not use UpgradePilot's own `sys_tags()`, and do not build generic job-log/artifact ingestion until a selected proposition requires it.

**Primary evidence:**

- [artifact serviceability](../src/upgradepilot/impact/artifact_serviceability.py)
- [Target artifact environment](../src/upgradepilot/target/artifact_environment.py)
- [application](../src/upgradepilot/investigation.py)
- [artifact tests](../tests/test_artifact_serviceability.py)
- [S008 artifact pressure](../product-simulation/S008_POST_CASE_SYNTHESIS.md)

---

### AUDIT-008-F6 — Runtime-correlated CI support deliberately does not establish exact installed dependency/artifact identity

**Classification:** deliberate proof boundary + missing stronger producer.

The current CI bridge is soundly conservative:

```text
exact supported static occurrence
+ eligible structural/profile facts
+ exact correlated completed-successful runtime step
→ supported_runtime_correlated
```

It explicitly does **not** prove:

- exact resolved/installed dependency version;
- wheel versus sdist selection;
- artifact filename/tags;
- exact target-supported tags;
- behavioral compatibility.

This is correct under ADR-0009 and the completed Cycle-3 design.

**Consequence:** any future action permission that requires exact runtime installation/artifact identity needs a new evidence source. Existing green/runtime-correlated CI must not be reinterpreted upward.

**Disposition:** KEEP the current claim boundary. Add a runtime version/artifact witness only when a selected action/proposition demonstrates why that exact fact changes the decision. Generic log ingestion is not justified merely because logs exist.

**Primary evidence:**

- [CI dependency coverage](../src/upgradepilot/ci/dependency_exercise.py)
- [runtime strengthening](../src/upgradepilot/ci/runtime_strengthening.py)
- [ADR-0009](../docs/architecture/ADR-0009-parser-backed-static-workflow-command-analysis.md)
- [parent synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)
- [Cycle-3 hosted proof](https://github.com/motafegh/UpgradePilot/actions/runs/35448172928)

---

### AUDIT-008-F7 — Candidate/context discovery coverage remains intentionally bounded and is not enough for favorable merge permission

**Classification:** deliberate product coverage limitation / missing favorable-permission premise.

Current normal investigation has implemented technical reasoning for a bounded set of mechanisms, notably:

- Python support drop;
- published artifact-serviceability loss.

The Product Decision Model correctly permits zero or more mechanism-specific candidates without pretending candidate generation is globally complete.

The Maintainer Action Synthesis Specification is stricter for favorable output:

```text
merge after normal review
→ requires positive closure over an explicitly bounded evidence/context/coverage horizon
→ absence of a known concern is not sufficient
```

The parent plan explicitly records that generic discovery/context coverage is not generally producer-grounded today.

**Consequence:** the system cannot honestly turn:

```text
current implemented mechanisms found nothing defeating
```

into:

```text
merge after normal review
```

unless the relied-upon bounded horizon itself is positively established.

This is not a correctness bug in the current product. It is an important action-reachability limit.

**Disposition:** preserve abstention/favorable claim limits. Before implementing merge permission, define the exact bounded horizon being claimed and prove its discovery/context coverage with normal producers and defeaters. Do not require universal dependency-risk discovery.

**Primary evidence:**

- [Product Decision Model](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)
- [Maintainer Action Synthesis Specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)
- [parent synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)
- [S010 discovery pressure](../product-simulation/S010_POST_CASE_SYNTHESIS.md)

---

### AUDIT-008-F8 — Local-model semantic extraction has a good trust boundary, but current hosted proof does not prove the live semantic deployment

**Classification:** proof/reproducibility boundary / KEEP with explicit limitation.

The Python-support semantic path is carefully separated:

```text
authoritative bounded source window
→ local LM Studio structured candidate extraction
→ deterministic source-line recovery
→ deterministic candidate validation/admission
→ grounded support-drop result
```

Important strengths include:

- release text explicitly treated as untrusted data;
- strict structured-output schema;
- line IDs and deterministic quote recovery rather than trusting model-rewritten quotes;
- trusted crossed-release/version constraints;
- malformed/provider failures become unresolved;
- local LM Studio session disables ambient proxy inheritance;
- model output cannot assign action authority.

This is strong alignment with the Core, Minimum Useful Generality and Security boundaries.

However, the directly inspected hosted 604-test proof does not invoke the live LM Studio model. Extractor tests use controlled HTTP responses, and the product verification workflow also documents that local-model behavior is outside its hosted scope.

**Consequence:** deterministic adapter correctness and source-grounding behavior are well protected; current live model/deployment semantic quality remains a separate evidence class.

**Disposition:** KEEP the architecture and claim limit. Refresh live local-model evaluation only when current semantic extraction quality becomes a release/action-admission prerequisite. Do not confuse unit/hosted regression with model-quality proof.

**Primary evidence:**

- [support-drop runtime](../src/upgradepilot/upstream/support_drop.py)
- [local extractor](../src/upgradepilot/upstream/support_drop_extractor.py)
- [extractor tests](../tests/test_support_drop_extractor.py)
- [runtime tests](../tests/test_upstream_support_drop.py)
- [ADR-0006](../docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
- [SECURITY.md](../SECURITY.md)
- [ENVIRONMENT.md](../ENVIRONMENT.md)

---

### AUDIT-008-F9 — Public GitHub acquisition can be silently changed by an ambient GITHUB_TOKEN

**Classification:** trust/transport policy mismatch and real robustness risk.  
**Disposition:** FIX at the public acquisition/CLI configuration boundary before treating public live runs as deterministic evidence.

`SECURITY.md` requires deliberate credential use and states that ambient credentials must not silently change a public/read-only proof when authentication is unnecessary.

Current CLI unconditionally passes:

```python
token=os.getenv("GITHUB_TOKEN")
```

to the GitHub clients. `GitHubApiClient` then adds:

```text
Authorization: Bearer <token>
```

whenever that environment variable is non-empty.

`ENVIRONMENT.md` records an observed failure mode:

```text
ambient stale/invalid GITHUB_TOKEN
→ public GitHub request becomes authenticated
→ HTTP 401
```

and currently recommends running public proofs with `env -u GITHUB_TOKEN ...` when authentication is not needed.

An environment variable may be a deliberate configuration mechanism, but the **current CLI has no explicit anonymous/authenticated selection boundary**. A token inherited from an unrelated shell/session can change public acquisition behavior without being part of the command's visible input.

**Consequence:** a public read-only investigation can fail for ambient-credential reasons even though anonymous source access is healthy, weakening reproducibility and violating the project's intended deliberate-authentication boundary.

**Smallest justified disposition:** make authentication choice explicit enough that normal public proof does not silently inherit unrelated ambient credentials. Exact CLI/API design belongs to a later Build/Design step; possibilities include an explicit auth mode or another bounded configuration contract. Do not print/token-test secret values.

This finding is separate from proxy behavior. GitHub proxy routing is a known environment/transport condition; this audit does not claim that all ambient proxy use is a source defect.

**Primary evidence:**

- [SECURITY.md](../SECURITY.md)
- [ENVIRONMENT.md](../ENVIRONMENT.md)
- [CLI](../src/upgradepilot/cli.py)
- [GitHub API client](../src/upgradepilot/github/api.py)

---

### AUDIT-008-F10 — Operational acquisition failure containment remains a source-traced risk, not yet a confirmed current defect

**Classification:** REASSESS / unproven resilience gap.

Several GitHub acquisition/response exceptions escape the investigation constructor and are converted by the CLI into operational exit codes. The synthesis specification explicitly distinguishes this from semantic abstention:

```text
operational failure preventing formation of synthesis input
!= semantic abstention
```

The parent plan previously identified a resilience question: one provider failure may prevent later independent evidence from being acquired or returned.

This audit did not fresh-reproduce a case where the current admitted product **must** continue after such a failure and incorrectly stops. The Core Specification also permits failing the run when trustworthy continuation is impossible.

**Consequence:** this remains a real design/reliability question, but calling it a confirmed product defect would exceed the evidence.

**Disposition:** REASSESS when an action path or user-facing partial-result requirement demonstrates that independent evidence must survive a specific provider failure. Use the smallest discriminating failure test then. Do not create a general resilience framework preemptively.

**Primary evidence:**

- [core pipeline specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [investigation](../src/upgradepilot/investigation.py)
- [CLI](../src/upgradepilot/cli.py)
- [parent synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)

---

### AUDIT-008-F11 — Audit lifecycle metadata conflicts with the canonical live project position

**Classification:** governance/state-coordination drift.  
**Disposition:** RECONCILE separately; do not let the stale lifecycle entry steer product work.

`MEMORY.md` currently and correctly owns the selected main responsibility:

```text
post-Cycle-3 parent evidence-path / maintainer-action synthesis re-audit
```

However, `audits/active/README.md` still lists only:

```text
ACTIVE — AUDIT-005 — Product AI / Agentic Orchestration and Sequencing Reassessment
```

and describes the B2/X1 model-ready checkpoint as the current engineering route.

The audit lifecycle rules say `active` is for validated findings selected as inputs to the **current** engineering responsibility, and `MEMORY.md` remains the sole live-state authority.

The current index therefore contains stale lifecycle state relative to the canonical owner.

**Consequence:** a future agent loading the lifecycle index can be incorrectly pulled toward the paused B2/X1 agentic path even though current live continuation is the parent synthesis audit.

**Disposition:** after this audit is accepted as the current engineering input, reconcile AUDIT-005's lifecycle classification through the audit lifecycle process. Do not reinterpret AUDIT-005 as invalid; only its current `active` classification is inconsistent with the present live route.

**Primary evidence:**

- [MEMORY.md](../MEMORY.md)
- [audit lifecycle](LIFECYCLE.md)
- [active audit index](active/README.md)
- [AUDIT-005](2026-08-21_AUDIT-005_product-ai-agentic-orchestration-sequencing.md)

## 5. Cross-finding system assessment

### 5.1 What the current system is strong at

UpgradePilot already has a credible technical foundation for:

- exact proposal/revision/dependency identity;
- strong source/provenance preservation;
- explicit unsupported/unresolved/failure states;
- exact-head and exact-attempt GitHub Actions evidence;
- bounded parser-backed static command semantics;
- conservative static↔runtime strengthening;
- exact old/proposed PyPI artifact inventories;
- bounded upstream interval authority;
- deterministic grounding around a local semantic extractor;
- candidate-specific applicability semantics;
- keeping action authority separate from mechanism-specific findings;
- large deterministic regression coverage with successful fresh hosted installation proof.

These foundations are not merely design documents; substantial portions are source/test/runtime-proven.

### 5.2 What the current system is not yet

It is not yet:

- a final maintainer recommendation CLI;
- a multi-action synthesis engine;
- a complete candidate/context discovery system;
- a runtime installed-version/artifact observer;
- an exact target wheel-compatibility producer;
- a complete multi-job Target interpreter;
- a live-model-hosted end-to-end proof;
- a proof that dependency updates are safe.

### 5.3 The central architectural bottleneck

The remaining problem is not one missing algorithm. It is **action-relative reachability across heterogeneous evidence**.

The system has several strong local facts, but useful maintainer actions require specific combinations:

```text
technical fact
+ target applicability
+ coverage/context
+ provenance/trust
+ stopping/next-responsibility state
→ positive permission for one action
```

The correct next work therefore depends on the exact action/proposition being targeted.

## 6. Priority and disposition map

This is an audit prioritization, **not an implementation plan**.

| Finding | Type | Current disposition | Why it matters now |
|---|---|---|---|
| F3 | current synthesis correctness | **FIX FIRST / correctness gate** | the already-admitted abstention evaluator can under-report material uncertainty |
| F9 | trust/transport robustness | **FIX before relying on public live proof** | ambient token can silently alter/fail public acquisition |
| F11 | governance coordination | **RECONCILE** | stale active-audit route can misdirect future work |
| F4 | evidence composition | **candidate** | preserves exact consuming job into Target; improves common multi-job static interpretation |
| F5 | missing producer | **candidate** | necessary for exact artifact-serviceability applicability |
| F6 | missing producer | **candidate** | necessary only for actions/propositions requiring runtime installed/artifact identity |
| F7 | bounded coverage | **preserve limit / future favorable-action prerequisite** | prevents unjustified merge recommendation |
| F8 | proof boundary | **keep; refresh when required** | hosted deterministic proof is not live model-quality proof |
| F10 | resilience risk | **reassess on trigger** | source-traced, but not yet proven to violate an admitted continuation responsibility |
| F1/F2 | sound foundation / intentional incompleteness | **keep** | prevents unnecessary redesign and action overreach |

## 7. Recommended post-audit continuation

The audit supports this decision order:

```text
1. repair / prove the current admitted synthesis baseline
   → F3: honest material uncertainty preservation

2. reconcile product-run trust and coordination defects that can invalidate/re-route proof
   → F9 credential-selection boundary
   → F11 audit lifecycle state

3. re-evaluate non-abstention action reachability from the corrected baseline
   → do not choose an action by vocabulary completion

4. only then select the smallest producer/composition responsibility required by the chosen permission
   → F4 consuming-job → Target composition
   → F5 exact target wheel-tag producer
   → F6 exact runtime version/artifact witness
   → F7 explicit bounded discovery/context horizon
   → or another source-backed missing premise discovered during action proof

5. integrate human/machine maintainer-action presentation only after the selected permission is proven
```

Why F3 comes first:

- it concerns **already admitted behavior**, not optional feature breadth;
- the synthesis specification already requires truthful material residual uncertainty;
- stronger action logic should not be layered on a baseline that can hide why evidence stopped;
- the repair can be bounded without inventing new evidence producers.

This ordering does not imply that F4/F5/F6 are unimportant. It prevents feature expansion from outrunning the correctness of the layer that will consume those results.

## 8. What this audit does not authorize

This audit does not authorize:

- modifying `maintainer_action.py`;
- changing CLI authentication behavior;
- reclassifying AUDIT-005;
- implementing Target job selection;
- adding job-log/artifact ingestion;
- adding exact wheel-tag collection;
- implementing any non-abstention action;
- changing specifications/ADRs;
- expanding product-simulation cases;
- starting agentic orchestration.

Each mutation requires the normal Planning/Design or Build route and its own bounded A→B→C→D→E cycle.

## 9. Reassessment triggers

Reassess this audit when any of the following materially changes:

- the synthesis evaluator begins admitting a non-abstention action;
- the CLI begins rendering synthesis results;
- exact target wheel-compatibility evidence gets a normal producer;
- runtime installed-version/artifact evidence gets a normal producer;
- candidate/context coverage responsibility is explicitly broadened;
- public acquisition authentication/configuration is changed;
- the local semantic model/deployment or grounding contract changes;
- a later audit/plan supersedes a finding with stronger evidence.

## 10. References

### Controlling / live

- [Project Charter](../PROJECT_CHARTER.md)
- [Core Pipeline and Contract Specification](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md)
- [Product Decision Model Specification](../docs/specifications/UPGRADEPILOT_PRODUCT_DECISION_MODEL_SPECIFICATION.md)
- [Maintainer Action Synthesis Specification](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)
- [Minimum Useful Generality Specification](../docs/specifications/UPGRADEPILOT_MINIMUM_USEFUL_GENERALITY_SPECIFICATION.md)
- [parent synthesis plan](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)
- [MEMORY.md](../MEMORY.md)

### Main implementation/evidence

- [investigation](../src/upgradepilot/investigation.py)
- [maintainer action](../src/upgradepilot/maintainer_action.py)
- [CLI](../src/upgradepilot/cli.py)
- [dependency analysis](../src/upgradepilot/dependency/analysis.py)
- [GitHub Actions acquisition](../src/upgradepilot/github/actions.py)
- [GitHub API client](../src/upgradepilot/github/api.py)
- [CI dependency coverage](../src/upgradepilot/ci/dependency_exercise.py)
- [CI consumption](../src/upgradepilot/ci/consumption.py)
- [Target artifact environment](../src/upgradepilot/target/artifact_environment.py)
- [artifact serviceability](../src/upgradepilot/impact/artifact_serviceability.py)
- [Python support impact](../src/upgradepilot/impact/python_support.py)
- [support-drop runtime](../src/upgradepilot/upstream/support_drop.py)
- [local support-drop extractor](../src/upgradepilot/upstream/support_drop_extractor.py)
- [SECURITY.md](../SECURITY.md)
- [ENVIRONMENT.md](../ENVIRONMENT.md)

### Tests / proof

- [investigation tests](../tests/test_investigation.py)
- [maintainer-action tests](../tests/test_maintainer_action.py)
- [Target tests](../tests/test_target_artifact_environment.py)
- [artifact-serviceability tests](../tests/test_artifact_serviceability.py)
- [local extractor tests](../tests/test_support_drop_extractor.py)
- [test-suite boundary](../tests/README.md)
- [hosted Cycle-3 proof](https://github.com/motafegh/UpgradePilot/actions/runs/35448172928)

### Product pressure evidence

- [Investigate vs Block existing-evidence report](../product-simulation/INVESTIGATE_VS_BLOCK_EXISTING_EVIDENCE_REPORT_2026-09-11.md)
- [S003 block-like pressure](../product-simulation/S003_POST_CASE_SYNTHESIS.md)
- [S006 targeted-check pressure](../product-simulation/S006_POST_CASE_SYNTHESIS.md)

---

`UP-SKILL:upgradepilot-repository-audit`
