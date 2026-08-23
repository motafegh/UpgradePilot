# Governance Redesign — Group 6 Learning-Only Validation

**Date:** 2026-08-23  
**Branch:** `governance/spec-governance-enhancement-refinement`  
**Role:** dated non-controlling implementation/validation evidence for Group 6 of the governance operating-model redesign

## 1. Group objective

Group 6 adds one reusable Learning-Only procedure for sessions where product mutation is paused and understanding/mastery becomes the selected responsibility.

The procedure must integrate with existing package-local learning architecture rather than replacing it.

Primary compatibility target:

```text
learning/2026-08-17-b2-dependency-environment-ci-consumption-mastery/
```

## 2. Files changed in Group 6

Compared with the completed Group-5 validation commit `11b58d79d43eaec142b37199ed41846001c9c78a`, Group 6 changed only:

```text
.agents/skills/upgradepilot-learning-only/SKILL.md
tools/agent-governance/learning_only_cases.json
tools/agent-governance/README.md
```

No product source/test file, specification, ADR, plan owner, root memory, B2 learning-package file, or other package-local learning artifact was modified.

## 3. Learning-Only Skill responsibility

`.agents/skills/upgradepilot-learning-only/SKILL.md` is explicitly procedural and non-controlling.

It owns the reusable operation procedure for:

- recognizing Learning-Only intent;
- immediately pausing product mutation;
- identifying the exact learning responsibility;
- discovering an applicable package-local learning owner rather than inventing a route;
- using real source/tests/evidence proportionately;
- minimum-background and minimum-complete-chunk teaching;
- fair learner reasoning/checkpoints;
- executable-source + focused-test ownership;
- technical independence and rationale/necessity reasoning;
- overlapping-evidence explanation;
- end-to-end ownership reasoning when material;
- bounded prerequisite repair;
- real-failure learning without manufactured failures;
- plan/design/spec learning without implementation;
- package learning-memory discipline;
- transition back to another primary operation when explicitly authorized.

It does not become:

- a second global teaching contract;
- a B2-specific learning contract;
- product implementation authority;
- live project-state authority;
- implementation truth;
- or an automatic learning-artifact write authorization.

## 4. Important action-boundary refinement

The Group-6 implementation preserves root `AGENTS.md`'s stronger write boundary:

```text
Learning-Only
→ product/source/test/governance mutation paused
→ read/inspect/trace/explain/compare/diagnose allowed within scope
```

Learning artifacts may change only when the user's learning request actually includes/authorizes that artifact work and the package/global ownership rules justify it.

Therefore even a package `LEARNING_MEMORY.md` is not silently writable merely because Learning-Only is active.

This avoids turning a read-only learning request into repository mutation through continuity bookkeeping.

## 5. B2 compatibility audit

The existing B2 package was inspected as the real integration target.

### Package contract

`00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md` already states the correct responsibility split:

```text
../../MEMORY.md
→ live project position

../../OPERATING_GUIDE.md
→ project-wide learning/execution method

package contract
→ package global learning invariants

PLAN_XX*.md
→ local route/traps/source/test targets/gates

PLAN_XX_MASTERY_AND_DEPTH_MAP.md
→ intended depth + depth rationale

LEARNING_MEMORY.md
→ package learning continuation/gaps/demonstrated understanding

source/tests
→ implementation truth
```

The new Skill preserves this exact architecture.

### Mastery/depth index

`00_PLAN_MASTERY_AND_DEPTH_INDEX.md` establishes that the learning unit is a meaningful engineering responsibility/mechanism rather than raw file length, and separates:

```text
execution plan
mastery/depth map
global contract
learning memory
```

The Skill follows that same model and does not globalize the B2 depth assignments.

### Learning memory

`LEARNING_MEMORY.md` currently owns the B2 package learning position and exact pause, while explicitly refusing live project-state authority.

The Skill therefore uses package learning memory for learning continuation and root `MEMORY.md` only when current product continuation/return-to-building is actually material.

This is important because package learning memories may preserve dated/copied project context that must not override current root state.

### Active Plan-02 route

`PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md` demonstrates the expected specialization model:

- inherits global package contract;
- owns exact Plan-02 route/source/test/audit gates;
- uses the matching mastery/depth map;
- keeps whole-file mastery out of scope;
- teaches overlapping `pyproject.toml` / `uv.lock` evidence accurately;
- keeps static selection distinct from file-content evidence;
- applies local necessity/audit rules.

The generic Skill can enter this route without rewriting it.

## 6. Rule-traceability consumption

The rule-ownership matrix requires Group 6 to consume:

```text
RT-LBD-001..010
RT-ENG-001..007
RT-SRC-001..002
RT-SRC-005..007
RT-OPS-004
RT-LOC-001..007 as locality constraints
```

### `RT-LBD-001..010`

Covered by the Skill through:

- real UpgradePilot responsibility as learning unit;
- real evidence before synthetic examples;
- background-first for new material;
- one minimum-complete chunk;
- fair checkpoints;
- learner challenge/backtrack and local correction;
- technical independence;
- assistance fading;
- no fake ownership evidence;
- project-local depth rationale and package depth-map deference.

### `RT-ENG-001..007`

Covered through:

- current fact vs rationale vs engineering judgment vs authority;
- no invented rationale;
- proposition → necessity → owner/layer → evidence → alternative reasoning;
- necessity vocabulary as reasoning aids;
- proportionate engineering audit without turning every lesson into formal Audit;
- explicit overlapping-evidence analysis;
- normal/failure/test-fixture/hypothetical/synthetic example-state labeling.

### `RT-SRC-001..002`, `RT-SRC-005..007`

Covered through:

- executable-source responsibility rather than comments/docstrings alone;
- source ↔ focused-test coupling and non-proof explanation;
- real-failure diagnosis with no manufactured failures;
- current source/tests/callers not serving as automatic architectural retention authority;
- producer → integration/composition → consumer / earliest-sufficient-owner reasoning when ownership is material.

### `RT-OPS-004`

Covered through selective package discovery and smallest-sufficient source/test/evidence loading. Learning-Only does not scan all learning packages/history reflexively.

### `RT-LOC-001..007`

Preserved as locality constraints. The Skill explicitly refuses to globalize:

- S001 → S011 → S005 route;
- B2 uv/CI/tox/BFS depth assignments;
- A–N chunk mechanics and GREEN/YELLOW/RED package notation;
- B2 0–7 evidence-strength vocabulary;
- exact B2 plan/depth pairs and continuation;
- Career Day-30 evidence/reassessment requirements;
- Career two-session executable-contact drift rule.

## 7. Behavioral regression bank

`tools/agent-governance/learning_only_cases.json` contains 11 focused cases:

```text
LEARN-001  explicit Learning-Only stops product mutation
LEARN-002  resume existing B2 package through its real owners
LEARN-003  learn plan/design without executing it
LEARN-004  technical independence / no invented rationale
LEARN-005  bounded prerequisite repair and return
LEARN-006  explicit exit to Build/Planning
LEARN-007  executable source + focused test, not docstring-only learning
LEARN-008  overlapping-evidence explanation
LEARN-009  fixture/failure/synthetic truthfulness
LEARN-010  package learning memory vs root project memory
LEARN-011  no unnecessary learning-package ceremony
```

The evaluation README registers the bank and marks package-learning-memory-as-live-project-authority as a zero-tolerance regression.

## 8. Deterministic-validation boundary

Current `governance_doctor.py` discovers Skill directories generically, so the new Skill's frontmatter/name can be checked by the existing Skill logic once the doctor is executed in a repository-capable environment.

The new scoped `learning_only_cases.json` bank is not yet loaded by the current doctor, exactly like the existing Audit/Planning/Build scoped banks.

Therefore:

```text
Skill structural compatibility
→ statically inspected

Learning-Only behavioral cases
→ behavioral/manual regression surface

scoped-bank deterministic doctor validation
→ NOT YET IMPLEMENTED
```

Do not report an executed doctor PASS from this Group-6 work.

Group 7 owns extending/consolidating scoped-bank validation.

## 9. Root / Operating Guide routing decision

No root `AGENTS.md` or `OPERATING_GUIDE.md` edit was made in Group 6.

The existing Group-1 routing already states that explicit Learning-Only:

- pauses product mutation;
- uses the admitted Learning-Only procedure when present;
- composes with package-local contract/plan/memory;
- retains `OPERATING_GUIDE.md` as the project-wide teaching/evidence owner.

The Skill is now present, so the routing is semantically functional.

A final cross-operation consistency cleanup remains for Group 7: replace remaining generic `when present` / `when available` operation references with exact admitted Skill paths for Audit, Planning, Build, Learning-by-Doing, and Learning-Only together. Doing that once avoids piecemeal root/Guide churn and keeps all operation references symmetric.

## 10. Acceptance assessment

Group 6 acceptance criteria are satisfied at the designed scope:

- [x] explicit reusable Learning-Only Skill exists;
- [x] product mutation is reliably paused;
- [x] B2 package architecture works without wholesale rewriting;
- [x] package contract/plan/depth/memory responsibilities remain intact;
- [x] Learning-by-Doing and Learning-Only share global principles without collapsing action boundaries;
- [x] code/tests/plans/design/specifications/concepts/evidence/governance can all be learning subjects;
- [x] technical audit is proportionate and can escalate to the Audit procedure without authorizing mutation;
- [x] package learning continuity is separate from root project continuation;
- [x] no fake learner-ownership mutation/failure is required;
- [x] behavioral cases cover the high-risk routing/ownership failures;
- [x] no product semantics or B2 package rules changed.

## 11. Stop line and next redesign group

Group 6 does not implement Group 7.

The next redesign step is:

```text
Group 7 — Governance Consistency / Validation / Cleanup
```

That group must now validate the complete operation family as one system, reconcile exact Skill routing references, extend/consolidate deterministic case-bank checks, verify the full rule-promotion matrix, check cross-owner consistency, and prepare merge readiness without changing product implementation.
