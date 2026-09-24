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
A — NOT STARTED
B — BLOCKED on A
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
