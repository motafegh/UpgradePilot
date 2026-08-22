# TEMPORARY — Learning Governance and Plan Refinement Implementation Plan

**Created:** 2026-08-22  
**Status:** ACTIVE TEMPORARY IMPLEMENTATION PLAN  
**Scope:** `learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/` only  
**Deletion rule:** delete this file after all required refinements below are implemented, validated, and the final learning continuation state is recorded.  
**Authority:** this file is a temporary execution checklist only. It does not replace the learning contract, plan files, mastery/depth maps, `LEARNING_MEMORY.md`, source/tests, or root `MEMORY.md`.

## 1. Purpose

Refine the current learning package so its rules are easier to apply consistently, less duplicated, more precise about evidence/design reasoning, and less likely to drift across long sessions.

The target is **not more governance**. The target is:

```text
fewer canonical rules
+ clearer rule ownership
+ plan-specific specialization
+ explicit learning-depth limits
+ concise live learning continuity
```

No product source behavior, architecture, tests, or implementation authorization is changed by this work.

## 2. Target artifact hierarchy

After refinement, the package should follow this responsibility split:

```text
00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
→ permanent/global learning invariants, roles, and trigger-based operating rules

PLAN_XX_....md
→ plan-specific route, real cases, special traps/rules, chunk sequence, and gates

PLAN_XX_MASTERY_AND_DEPTH_MAP.md
→ how deeply each responsibility/concept/source/test must be learned and what is deferred

00_PLAN_MASTERY_AND_DEPTH_INDEX.md
→ navigation + global depth vocabulary only

LEARNING_MEMORY.md
→ current learning position, demonstrated understanding, open gaps/audit questions, and exact continuation

CAREER_DAY30_OWNERSHIP_HANDOFF.md
→ Career-specific ownership/evidence overlay; reference it instead of duplicating its detailed rules elsewhere
```

### One-normal-owner / inherit-don't-repeat rule

A learning rule should have one normal owner. Other artifacts may reference or specialize it, but should not restate the full rule unless the local specialization materially changes how it applies.

Each active/future plan should make clear that it **inherits the contract**. Silence in a plan does not disable a contract rule.

## 3. Required contract refinements

**File:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`

### 3.1 Add a compact high-salience operating section

Near the beginning, add a concise **Core rules to actively enforce every session** section containing only the highest-value invariants, approximately 8–12 items.

It should cover at minimum:

- real case/evidence before abstraction when available;
- background-first for genuinely new material subjects;
- minimum-complete chunks and anti-jump behavior;
- Ali may interrupt/challenge/backtrack at any point;
- fair learner checkpoints only after enough prerequisite material exists;
- source/tests are implementation truth, not automatic design truth;
- material syntax/control flow is taught in context, not every line equally;
- evidence/proof/non-proof boundaries remain explicit;
- no forced mutations or manufactured failures;
- reduce assistance as ownership grows;
- challenge premises and artifact/check necessity rather than assuming the teacher/source is correct;
- global rules are inherited by plans rather than duplicated.

The longer detailed sections may remain as reference, but remove/merge obvious duplication where the same rule is repeated without adding meaning.

### 3.2 Add an explicit engineering-necessity classification

For material fields/checks/evidence requirements/design constraints, distinguish:

```text
PROPOSITION-ESSENTIAL
logically necessary for the claim being established

CURRENT-IMPLEMENTATION REQUIREMENT
required by current source/design, but a different valid design might not require the same mechanism/artifact

DEFENSIVE / BOUNDARY HARDENING
upstream should normally preserve the invariant, but this boundary revalidates it to fail closed

UNCERTAIN / AUDIT NEEDED
necessity/rationale has not yet been sufficiently justified
```

The assistant must not teach “the system needs X” when the evidence only supports “the current implementation requires X.”

### 3.3 Add an overlapping-evidence rule

When multiple artifacts contribute to one proposition, explicitly identify:

```text
what each artifact directly observes/declares
where their information overlaps
which information is primary versus derived/duplicated
what the current implementation actually consumes from each
what none of them establishes alone
```

Do not create an artificially clean `A tells X / B tells Y` division when the real artifacts overlap.

### 3.4 Add example-state labels

Whenever an example materially affects the learner's system model, identify whether it is:

```text
NORMAL / EXPECTED PATH
FAILURE / INVALID INPUT
TEST FIXTURE
HYPOTHETICAL DESIGN CASE
```

Defensive guards must not be taught as though their failure states are normal expected pipeline states.

### 3.5 Strengthen fair learner-checkpoint rules

Classify consequential learner prompts where useful as:

```text
RECALL
REASONING / PREDICTION
SOURCE RECONSTRUCTION
OPEN ENGINEERING CRITIQUE
```

Do not ask a checkpoint whose correct answer depends on implementation details deliberately not taught yet.

Prediction remains desirable when Ali has sufficient facts but the exact source answer has not yet been revealed.

### 3.6 Add a learner-interruption/resume protocol

When Ali stops at a specific section/question:

```text
answer the local uncertainty
→ correct any earlier oversimplification explicitly
→ re-establish the corrected mental model
→ do not automatically advance to later material
→ resume from the paused position only when ready
```

A local question must not trigger a new lecture or silently skip the unfinished chunk section.

### 3.7 Strengthen premise-challenge as ownership evidence

Explicitly recognize that challenging:

- the teacher's premise;
- whether an artifact is actually required;
- whether a defensive invariant is redundant;
- whether an example represents normal operation;
- whether a question itself is well-posed;

can be positive ownership evidence when grounded in the current material.

Resolve the premise before forcing downstream reasoning that assumes it.

### 3.8 Consolidate Career-overlay duplication

Keep the contract-level statement of the Career overlay's authority and general interaction, but prefer references to `CAREER_DAY30_OWNERSHIP_HANDOFF.md` instead of repeating detailed pre-change/post-change/diagnosis rules multiple times.

Do not weaken any Career evidence requirement; reduce duplication only.

## 4. Mastery/depth index refinement

**File:** `00_PLAN_MASTERY_AND_DEPTH_INDEX.md`

Keep this file narrow: navigation, depth vocabulary, stopping rule, and relationship between execution plans and mastery maps.

Required addition to **OWN / MASTER**:

> At mastery depth, when material to the responsibility, Ali can distinguish current implementation fact from proposition-essential requirements, defensive hardening, uncertain rationale, and plausible alternative design.

Do not duplicate the full contract methodology here.

Reinforce:

```text
master a responsibility/mechanism
!= master an entire large file
```

## 5. Plan 02 execution-map corrections

**File:** `PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md`

This is the active plan and requires the most precise update.

### 5.1 Add/clarify contract inheritance

State succinctly that Plan 02 inherits the global contract and records only Plan-02-specific rules/specializations.

Avoid re-copying broad contract rules unless Plan 02 changes their local application.

### 5.2 Correct Chunk-1 evidence framing

Replace overly categorical separation of `pyproject.toml` and `uv.lock` with the more accurate model:

```text
static environment-selection declaration
→ establishes which project environment/group the inspected static command selected

exact pyproject.toml
→ primary project declaration/configuration evidence used by the current evaluator for relevant project identity/root/group semantics

exact uv.lock
→ resolved lock evidence used by the current evaluator for package/dependency graph semantics and may also preserve overlapping project/group information
```

Make explicit that these artifacts may contain overlapping information.

### 5.3 Correct the `uv.lock alone` wording

Do not say categorically that `uv.lock` cannot contain information about a project group/environment.

Use the stronger accurate boundary:

> Presence of dependency/group information in `uv.lock` does not itself establish that the inspected static CI command selected that environment. The selection proposition comes from the explicit static selection declaration; project and lock evidence then contribute to the current membership mechanism according to their actual roles.

### 5.4 Clarify why current evaluator consumes both artifacts

Chunk 1 must teach and audit separately:

- what `pyproject.toml` contributes in current source;
- what `uv.lock` contributes in current source;
- where their information overlaps;
- which contributions appear proposition-essential;
- which are current-design choices or defensive checks;
- what neither proves alone;
- lock freshness/resolver currentness remains outside the current proof boundary unless current source/spec says otherwise.

Do not force the learner to memorize “both are required” as an unexplained invariant.

### 5.5 Correct provenance-mismatch framing

When teaching revision/repository/path/blob mismatches, distinguish:

```text
NORMAL EXPECTED PIPELINE:
context + project evidence + lock evidence should already refer to the frozen exact case/revision.

DEFENSIVE FAILURE PATH:
_validate_exact_source_identity(...) rejects inconsistent/misbound evidence if an upstream/caller/cache/provider/test path violates those invariants.
```

Do not imply that HEAD-A/HEAD-B evidence mixing is expected normal operation.

### 5.6 Rewrite Chunk-1 gate

Replace the categorical gate “explain why both exact project metadata and exact lock evidence are required” with a gate requiring Ali to explain:

- static selection declaration role;
- exact `pyproject.toml` role;
- exact `uv.lock` role;
- evidence overlap;
- why the **current evaluator** consumes both;
- proposition-essential vs implementation-specific vs defensive requirements where material;
- provenance validation before semantic interpretation;
- one representative identity/provenance test and its non-proof boundary.

## 6. Plan 02 mastery/depth-map alignment

**File:** `PLAN_02_MASTERY_AND_DEPTH_MAP.md`

Align Chunk 1 and completion criteria with the corrected Plan-02 wording.

Required changes:

- replace blanket “why exact project + lock evidence are both required” language with the current-evaluator/evidence-role distinction;
- add evidence-overlap understanding to Chunk-1 mastery;
- add proposition-essential/current-implementation/defensive/uncertain classification to material design-audit mastery;
- preserve existing source-depth limits;
- keep TOML/uv internals operational/deferred except where causally necessary;
- keep graph/BFS learning in Chunk 2, not Chunk 1.

Do not expand Plan 02 into full `pyproject.toml`, TOML, uv resolver, or lock-format mastery.

## 7. Future-plan audit and specialization cleanup

Audit but modify **only where necessary**:

- `PLAN_03_GENERALIZATION_PRESSURE_S011_AND_S005.md`
- `PLAN_03_MASTERY_AND_DEPTH_MAP.md`
- `PLAN_04_APPLICATION_BOUNDARY_AND_RETURN_TO_BUILDING.md`
- `PLAN_04_MASTERY_AND_DEPTH_MAP.md`

Goals:

- state/infer contract inheritance clearly;
- retain only plan-specific special rules and depth targets;
- remove obvious duplicated global teaching/Career rules when a reference is sufficient;
- preserve real-case-specific traps, transfer rules, seam rules, and gates;
- ensure no frozen/dated snapshot is presented as current live continuation;
- keep `../../MEMORY.md` as the only live project continuation authority.

### Plan-04 live-handoff check

Specifically audit Plan 04 because root `MEMORY.md` now selects a post-learning bounded agentic investigation/orchestration evaluation checkpoint, while source-clarity/ordinary Cluster-6 continuation is deferred.

Do not silently rewrite legitimate historical snapshot statements. Correct only wording that could be read as current/future authority or that conflicts with the rule that live `MEMORY.md` selects the actual post-learning action.

## 8. Completed/historical Plan-01 artifacts

Audit only if a global-reference correction is genuinely necessary.

Do **not** rewrite completed Plan-01 learning notes or historical learning records merely to retrofit today's cleaner wording.

Preserve dated/history-specific findings. If a historical statement is useful but later refined, prefer a current correction in `LEARNING_MEMORY.md` or active plan rather than silently changing history.

## 9. Learning-memory update

**File:** `LEARNING_MEMORY.md`

After governance/plan refinements are complete, update the working memory concisely.

Required content:

### 9.1 Correct live continuation drift

Remove/correct the stale current statement that the immediate product action is the source-clarity/refactoring pass before Cluster 6.

Reflect only the current root `MEMORY.md` authority:

- active learning route remains first;
- post-learning checkpoint is the bounded agentic investigation/orchestration evaluation under the current live gate;
- source-clarity/ordinary Cluster 6 remain deferred unless live authority changes.

Do not duplicate full root-memory detail.

### 9.2 Record exact learning pause

Record that Plan 02 / Chunk 1 is paused during the first `pyproject.toml` + `uv.lock` evidence/background section before source-code validation walkthrough.

### 9.3 Record material corrections/discoveries

Preserve concisely:

- `pyproject.toml` and `uv.lock` have partially overlapping evidence;
- static selection declaration is separate from either artifact's mere contents;
- current evaluator consumes both exact project and lock evidence, but the learning task is to distinguish logical necessity from current design/defensive hardening;
- mixed-revision evidence is a defensive invalid-input scenario, not expected normal flow;
- Ali's challenges to those premises are positive engineering-audit/ownership evidence;
- Chunk 1 must resume from the corrected mental model rather than restarting or jumping to BFS.

Do not turn `LEARNING_MEMORY.md` into another rulebook.

## 10. Validation pass after edits

Before deleting this temporary plan, perform a bounded audit of the modified learning files.

Validate all of the following:

- [ ] Contract contains the permanent/global rules once, with a short high-salience core section.
- [ ] Contract is not made longer through simple additive duplication; repeated material is consolidated where safe.
- [ ] Plan files inherit the contract and specialize it rather than cloning it.
- [ ] Mastery/depth files remain focused on learning depth and stopping criteria.
- [ ] `LEARNING_MEMORY.md` remains a continuity/state file, not governance.
- [ ] `pyproject.toml` / `uv.lock` overlap is represented accurately.
- [ ] Static environment selection is not confused with group information merely existing in a project/lock artifact.
- [ ] “Current implementation requires” is not silently rewritten as “the proposition inherently requires.”
- [ ] Defensive invalid-input examples are labeled as such rather than taught as normal pipeline behavior.
- [ ] Learner checkpoints cannot depend on untaught implementation details.
- [ ] Learner interruption/resume behavior is explicit.
- [ ] Premise/design challenges are preserved as legitimate ownership evidence.
- [ ] Plan 02 remains bounded; BFS/graph internals remain Chunk 2.
- [ ] Future plans do not claim authority over the post-learning action; root `MEMORY.md` remains controlling.
- [ ] Historical Plan-01 artifacts are not silently rewritten.
- [ ] No product source/test behavior was changed by this refinement work.

## 11. Implementation sequence

Use this order so one canonical owner is established before dependent files are aligned:

```text
1. Refine 00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md
2. Refine 00_PLAN_MASTERY_AND_DEPTH_INDEX.md
3. Correct active PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md
4. Align PLAN_02_MASTERY_AND_DEPTH_MAP.md
5. Audit/trim future Plan 03/04 execution + mastery files only where needed
6. Update LEARNING_MEMORY.md with corrected live continuation + exact pause/discoveries
7. Re-read modified files as a set and run the validation checklist above
8. Delete this temporary plan
```

## 12. Stop/deletion condition

This temporary plan is complete only when:

```text
all required edits are implemented
+ conditional Plan-03/04 audits are resolved
+ cross-file rule ownership is consistent
+ active Plan-02 wording reflects the corrected evidence model
+ learning memory records the exact continuation point
+ final validation finds no material drift/duplication/conflict
```

Then delete:

`TEMP_LEARNING_GOVERNANCE_AND_PLAN_REFINEMENT_IMPLEMENTATION_PLAN.md`

The commit history may preserve that it existed; it should not remain as a permanent competing governance artifact.
