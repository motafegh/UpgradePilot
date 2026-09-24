# Runtime package-state decision-criticality — 2026-09-24

**Status:** ACTIVE — parent action-relative comparison / selection investigation  
**Operation:** Planning/Design + Learning-by-Doing; read-only product analysis until a next responsibility is explicitly selected  
**Controlling parent:** `plans/END_TO_END_PRODUCT_FLOW_LEARNING_AND_EVIDENCE_TO_ACTION_EXECUTION_PLAN.md`  
**Supporting runtime-state plan:** `plans/RUNTIME_DEPENDENCY_STATE_PROOF_COMPLETION_PLAN.md`  
**Prior closed work:** Runtime Dependency-State Proof Cycle 1 CLOSED; conditional Cycle 2 NOT selected  
**Purpose:** determine whether exact runtime package state is now a decision-critical missing premise for one accepted maintainer-action path.

## Exact question

Cycle 1 established:

```text
command semantics
+ exact runtime correlation
→ insufficient by themselves for trustworthy normal exact package-state proof
```

Target-owned runtime package-state evidence is technically feasible in some real cases.

The remaining selection question is:

> **Does resolving the exact runtime package-state proposition materially change reachability of one accepted maintainer action, strongly enough to justify selecting conditional Cycle 2?**

The proposition under test is bounded:

> **The exact proposed dependency version is present/satisfied in the exact selected dependency-consuming CI environment at the relevant observation boundary.**

This investigation does not assume that proposition is useful enough to build. It must prove decision value first.

## Decision rule

Select conditional Cycle 2 only if all three entry conditions are established:

```text
1. command semantics + exact runtime correlation are insufficient
   → ESTABLISHED by closed Cycle 1

2. exact runtime package state is decision-critical for one concrete action path
   → CURRENT QUESTION

3. proportionate target-owned evidence can discriminate that fact
   → FEASIBILITY SHOWN IN PART; exact adapter still unselected
```

If condition 2 fails, do not select Cycle 2 merely because state evidence is technically possible.

## Mini-plan — A → B → C → D → E

### A — Re-anchor action permissions and current producer reachability

Review only the current accepted action family and current normal producer truth:

```text
merge after normal review
run targeted checks
investigate or block
defer
abstain
```

For each action, preserve its positive permission and identify which premises are already normally reachable after F4/F5/F6/Cycle-1 findings.

**Output:** current action → reachable premises → unresolved premises map.

**Stop line:** do not redesign action semantics or build producers.

### B — Identify the smallest action-critical missing premise

Compare unresolved premises by:

```text
specific action permission
→ exact missing premise
→ closest defeater
→ product value if repaired
→ proof/implementation cost
```

Do not treat F5/F6/F7 as a backlog.

**Output:** one or a very small set of plausible next decision-critical premises.

### C — Test whether exact runtime package state is actually discriminating

For each plausible action path, ask:

```text
if exact proposed-version presence were established
→ what proposition changes?
→ does that materially change action reachability?
→ what still remains missing afterward?
```

Also test the opposite:

```text
if package state remains unresolved
→ which action is blocked specifically because of that fact?
```

**Pass for Cycle-2 selection:** package state is a necessary and materially discriminating missing premise for a concrete action path.

**Fail/defer:** package state is only helpful context, or another unresolved premise still dominates action reachability.

### D — Ownership check

Ali should be able to explain:

1. which action path is under evaluation;
2. why package state is or is not decision-critical for that path;
3. what establishing package state would change;
4. what it still would not prove.

### E — Selection

Choose exactly one continuation:

```text
A. SELECT Cycle 2
   → exact runtime package state is decision-critical
   → append/activate the smallest target-owned evidence cycle

B. DO NOT SELECT Cycle 2
   → package state is not the next decisive premise
   → select the actual action-critical responsibility

C. STOP / ABSTAIN FROM NEW BUILD
   → no currently justified producer repair materially changes an action path
```

No implementation begins merely because this investigation identifies a technically interesting evidence source.

## Current state

```text
A — DONE
B — IN PROGRESS
C — BLOCKED on B
D — BLOCKED on C
E — BLOCKED on D
```

## Guardrails

- preserve accepted action semantics;
- no generic environment reconstruction;
- no generic log-ingestion subsystem by default;
- no target mutation;
- no action permission from package-state evidence alone;
- missing evidence != negative evidence;
- one real case != general normal producer coverage;
- select one next responsibility only.

## A result — action permissions vs current producer reachability

Fresh inspection of the accepted synthesis specification, current `PublicPullRequestInvestigation`, current `maintainer_action.py`, and focused synthesis tests establishes the following normal-path map.

### Current producer baseline

The current investigation can normally preserve/produce, when the relevant branch is reachable:

```text
exact PR / repository / head identity
exact admitted dependency transition
exact-head workflow run/job evidence
static changed-dependency CI consumption
bounded runtime-correlated successful consumption
old/proposed package-release evidence
upstream repository/release-interval/tag/changelog evidence
grounded Python-support-drop claim + target-Python relevance/applicability
artifact-serviceability candidate
partial target artifact environment
  (exact workflow/job + runner/Python/install declaration)
artifact-serviceability applicability with exact wheel compatibility unresolved
material branch-stopping problems / residual uncertainty
```

Current product does **not** normally produce:

```text
exact runtime package-state proof
exact target wheel-tag compatibility
positive bounded candidate/repository-context discovery coverage
a maintainer-targeted check contract
a broader adaptive maintainer inquiry contract
a specific outside/future re-entry responsibility
non-abstention action permission
```

The current deterministic synthesis implementation deliberately admits only `abstain`. This is an implementation reachability fact, not a change to the stable action semantics.

### Action map

| Action | Positive permission that matters here | Current reachable premises | Important unresolved / unproduced premises |
| --- | --- | --- | --- |
| **merge after normal review** | Positive bounded evidence/mechanism/context closure; material concerns resolved/non-defeating; no decision-critical residual uncertainty | exact identity; several mechanism-specific evidence/applicability branches; residual uncertainty preserved | bounded candidate/context discovery coverage; closure across material concerns; some mechanism-specific exact target evidence such as wheel/runtime state when actually required |
| **run targeted checks** | one/small stable exact decision-critical proposition + bounded maintainer-performable discriminating check + interpretation/stopping logic + no better product-owned investigation | technical unresolved propositions can be preserved; product already demonstrates targeted internal investigation selection in some Python-support cases | no normal maintainer-check contract/producer; no currently selected proposition proven to be the exact stable decision-critical check target |
| **investigate** | grounded material concern + concrete broader/adaptive inquiry + discriminating directions + stopping/pruning logic | grounded technical concerns/uncertainties and mechanism-specific investigation states can exist | no normal broader adaptive maintainer-inquiry responsibility/producer |
| **block** | exact proposal-level failure/constraint/incompatibility/hold at sufficient proof strength; mechanism-specific extra premises as required | exact identity; upstream support evidence; target Python evidence/relevance; technical applicability branches | current normal path has not proven an action-level hold contract; exact environment obligation/dependency relation or observed failure may remain missing depending on mechanism; package-state presence alone cannot create block |
| **defer** | decision-critical unresolved question + no current justified investigation + specific useful outside/future responsibility + re-entry trigger | unresolved questions/limitations are preserved | no normal producer for the specific outside/future responsibility and re-entry condition |
| **abstain** | no other action is positively justified at current proof strength | fully reachable now; current evaluator intentionally emits only this action and preserves reasons/uncertainty/claim limits | not a technical negative conclusion; remains fallback until another action's positive permission is normally proven |

### A conclusion

No action currently has a demonstrated normal non-abstention permission path.

The important Step-A result for the Cycle-2 question is:

> **Exact runtime package state is not a universal prerequisite of the action family.** It can matter only when a concrete action-specific proposition requires it.

Therefore Step B must not ask “how do we build package state?” It must ask:

```text
which action path is closest to a real positive permission
→ what exact premise is currently decisive there
→ is runtime package state that premise or not?
```

A is complete. No action semantics, source, tests, or product behavior were changed.
