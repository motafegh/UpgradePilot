# Temporary Work Package 01 — Document Responsibilities and State Ownership

**Status:** Ready  
**Sequence:** 1 of 7  
**Primary repository:** Canonical `motafegh/Career`  
**Dependency:** None  
**Stop boundary:** Finish the canonical Career document-responsibility refactor before changing learning-session mechanics or refreshing the UpgradePilot Career snapshot.

> This package changes how rules and state are distributed across documents. It must not change the UpgradePilot mission, accepted technical decisions, current capability claims, product architecture, or milestone order.

## 1. Outcome

After this package:

- every major document has one clear responsibility;
- frequently changing facts have one canonical owner;
- stable documents no longer carry exact session-level state;
- plans define requirements and gates rather than repeatedly recording results;
- repeated learning and execution rules have one primary owner;
- a future small state change does not require edits across governance, strategy, roadmap, README, and agent-instruction files.

## 2. Files in scope

### Canonical Career entry points and charter

- `README.md`
- `AGENTS.md`
- `UpgradePilot.md`

### Governance

- `governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md`
- `governance/UPGRADEPILOT_LEARNING_PREFERENCES.md`
- `governance/90_DAY_EXECUTION_CONTRACT.md`
- `governance/SESSION_AND_BLOCKER_PROTOCOL.md`

### Strategy and capability

- `strategy/LEARNING_AND_PROJECT_DESIGN_PROFILE.md`
- `strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md`
- `strategy/STRATEGY_AND_SCOPE.md`
- `strategy/ADVANCED_SYSTEMS_EXPOSURE_AND_ADOPTION_POLICY.md`

### Plans and state

- `plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md`
- `plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md`
- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`

Review other files only when they contain a direct contradiction or duplicate live state. Do not broaden the package into a general rewrite.

## 3. Required information architecture

| Document | Owns | Must not own |
|---|---|---|
| `UpgradePilot.md` | Mission, user, supported decision, product boundary, outcome and claim limits | Exact current session or next action |
| Capability specification | Capability taxonomy, prerequisites, D0–D5, evidence and claim rules | Current progress state |
| Learning and Execution Contract | Mandatory Ali–AI execution, ownership and evidence behavior | Current milestone/session state |
| Learning Profile | Evidence and hypotheses about Ali’s learning mode and project fit | Repeated operating procedures |
| Learning Preferences | Teaching presentation, terminology, pacing and correction style | Duplicate execution contract |
| 90-Day Execution Contract | Stable workload, capacity, review and route-change rules | Exact method/session state |
| Session Protocol | Session templates and blocker/prerequisite workflows | Project-state authority |
| Strategy and Scope | Stable identity, priorities, project allocation and scope policy | Exact implementation continuation |
| Advanced Systems Policy | Exposure/adoption definitions and admission controls | Live tracker state |
| Roadmap | Route capacity and ordered development | Daily/session state |
| Milestone plan/amendment | Required outcomes, gates and boundaries | Rewritten result log |
| Tracker | Canonical current state, gate results, evidence, assistance, limits and next controlled responsibility | Full session transcript |
| README | Orientation, navigation and coarse maturity | Exact next action |
| `AGENTS.md` | Stable agent behavior, safety, authority routing and state lookup | Current method/session details |

## 4. Canonical ownership of changing facts

| Fact | Canonical owner |
|---|---|
| Product mission and boundary | `UpgradePilot.md` |
| Current milestone and gate state | Career tracker |
| Exact next controlled responsibility | Career tracker |
| Exact next command/action | Current session or working context |
| Accepted architecture method | Accepted ADR and ADR index |
| Required technical behavior | Technical specification |
| Actual implemented behavior | Source, tests and outputs; tracker summarizes verified proof |
| Capability depth | Career tracker under capability-spec rules |
| Session reasoning and assistance | Working-memory/session evidence |
| Workload and capacity rules | 90-Day Execution Contract |

## 5. Execution steps

### Step 1 — Inventory sections

Using the latest canonical files, classify each substantial section as:

- stable authority;
- live state;
- navigation;
- historical evidence;
- session evidence;
- technical requirement;
- implementation decision;
- duplicated rule.

Identify all direct statements of current milestone, exact next action, active session, method status, implementation status and capability status.

The inventory may remain in working notes or the active conversation. Do not create another repository planning artifact.

### Step 2 — Add responsibility boundaries

Near the top of each controlling file, state concisely:

- what the file owns;
- what it does not own;
- where current state is maintained;
- which higher-authority document governs overlap.

Avoid repeating the full authority chain in every file when one short reference is sufficient.

### Step 3 — Remove transient state from stable files

Remove or replace with canonical links:

- exact session-level next actions;
- current method-selection details in `AGENTS.md`;
- active session instructions in durable governance files;
- exact commands or session-start blocks in README files;
- result-state sections inside plans that duplicate the tracker.

README files may retain a coarse maturity or milestone summary only when it is deliberately stable and links to the tracker for exact state.

Historical activation statements may remain only when clearly labeled historical and non-controlling.

### Step 4 — Separate normative requirements from results

Plans and amendments must define:

- what must happen;
- what is authorized;
- pass conditions;
- boundaries.

The tracker must record:

- whether the requirement passed;
- evidence;
- assistance and ownership limits;
- current continuation.

Do not rewrite a plan merely because its gate passed.

### Step 5 — Consolidate duplicated rules

Use these primary owners:

- Capability Specification: capability families, D0–D5, prerequisites, assessment evidence and claim limits.
- Learning and Execution Contract: mandatory execution loop, assistance, ownership transfer, evidence interpretation and stopping.
- Learning Preferences: teaching presentation, terminology, chunking, analogy, command-explanation style and correction style.
- Learning Profile: observed learning-fit evidence, risks and hypotheses.
- Session Protocol: reusable session and blocker templates.

Retain the strongest formulation in the correct owner. Replace lower-level duplicates with concise references. Preserve project-specific refinements only when they add distinct information.

## 6. Review questions for every edit

1. What responsibility does this section currently serve?
2. Is that responsibility appropriate for this file?
3. Is the content stable or transient?
4. Does another file already own it?
5. Would removal weaken safety, learning, evidence or continuity?
6. Can it be replaced by a link or shorter boundary statement?
7. What future event would force this section to change again?
8. Is that future change appropriate for this file?

Do not shorten content merely to reduce line count. Correct responsibility and reduce change amplification.

## 7. Out of scope

Do not in this package:

- redesign the session modes;
- change D0–D5 evidence requirements;
- rebalance advanced-system targets;
- alter ADR-0002 or the core technical contract;
- modify UpgradePilot-local mirrors;
- refresh the Career snapshot;
- write source code or product tests.

## 8. Validation scenarios

### Exact next action changes

Expected edits: tracker/current execution context, and possibly concise project memory later.  
Not expected: README, `AGENTS.md`, charter, capability specification, learning contract, roadmap or milestone definitions.

### One gate passes

Expected edit: tracker with evidence.  
Not expected: rewriting the plan that defined the gate.

### One session ends

Expected edit: session evidence; tracker only when state or capability materially changes.  
Not expected: durable governance edits.

## 9. Pass conditions

- [ ] Every in-scope file states or clearly implies one responsibility.
- [ ] The Career tracker is the single exact current-state owner.
- [ ] Exact next actions are absent from stable governance and strategy files.
- [ ] `AGENTS.md` contains no live method/session instructions.
- [ ] README files do not act as duplicate trackers.
- [ ] Plans define gates rather than routine result state.
- [ ] Important rules no longer require reconciliation across several independent formulations.
- [ ] No substantive safety, learning or evidence control was lost.
- [ ] No UpgradePilot snapshot refresh occurred.

## 10. Recommended commit boundary

Use one or two focused commits:

1. `Clarify Career document responsibilities and state ownership`
2. `Consolidate duplicated Career control rules`

After validation, stop and proceed to Work Package 02.