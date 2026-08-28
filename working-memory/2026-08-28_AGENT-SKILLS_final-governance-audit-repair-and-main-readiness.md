# Agent Skills Governance — Final Audit Repair and Main-Readiness Record

**Date:** 2026-08-28  
**Scope:** `agent/skills-governance-evolution-2026-08-27` only  
**Authority:** Dated non-controlling execution/evidence record; root governance, canonical responsibility owners, and current user authorization remain authoritative.  
**Live-state rule:** This record does not own UpgradePilot product continuation. Root `MEMORY.md` remains the sole live project-state owner.

## 1. Entry

The final whole-branch governance audit was planned at commit `bbc66710ed639119edbcb897b9a1f8bed344418d` and executed read-only against branch base:

`f0322a5c997b201da740a4333faaeae9db74669d`

The initial final-audit disposition was:

```text
REPAIR REQUIRED BEFORE MAIN RECONCILIATION
```

No fundamental five-Skill architecture failure or sixth-Skill need was found.

## 2. Material findings repaired

### Default Learning-by-Doing reachability

Observed risk:

```text
substantive primary operation selected
→ agent focuses on Audit / Planning / Build Skill
→ user did not explicitly say Learning-by-Doing
→ default learning loop could be skipped
```

Repair:

- root `AGENTS.md` now states that Learning-by-Doing is the default operating/teaching method for substantive work even when Ali does not name it;
- selecting another primary operation does not disable the method;
- `OPERATING_GUIDE.md` mirrors that canonical rule;
- full `.agents/skills/upgradepilot-learning-by-doing/SKILL.md` loading remains a separate proportional choice rather than proof that the method is active;
- `CONSISTENCY-016` protects a substantive Build path where the method applies without ceremonial full-Skill loading.

### Progressive material-state preservation

Observed risk:

The loop's numbered preservation step could be read as “record only after the work.”

Repair:

```text
material state may be preserved before / during / after a bounded slice
when losing it would harm reasoning, evidence, continuation, or handoff
→ closure reconciles the correct owners
→ no continuous logging after every command/edit
```

Ownership remains unchanged:

- dated material execution/reasoning/evidence → `working-memory/` when justified;
- live continuation → `MEMORY.md` only;
- reusable understanding → `learning/` when justified;
- other owners update only when their responsibility changes.

### Lifecycle closure

- Stage 1 is explicitly structurally complete; its repository-wide doctor PASS is a final post-merge obligation, not an open Stage-1 gate.
- The Agent Skills proposal is now `Partially admitted`, preserves original candidate text as historical provenance, and records its six pre-implementation questions as resolved.
- The final whole-branch audit plan now records execution, repair, targeted re-audit, and readiness rather than claiming audit execution has not started.

## 3. Deliberate no-change decisions

Retain:

- exactly five admitted operation Skills;
- no sixth Debug, Governance-Maintenance, or Research operation Skill now;
- Build/Audit conditional progressive-disclosure references;
- current Learning-by-Doing / Learning-Only separation;
- project-wide proportionality and anti-rabbit-hole rules;
- no new global LLM ceremony;
- no live client-specific Skill-evaluation runner yet;
- no client-specific invocation metadata yet.

The real B2/X1 proportionality calibration on current `main` supported the conclusion that the LLM over-ceremony issue was local plan sequencing, not a missing global governance principle.

## 4. Latest-main divergence evidence

Latest `main` checked during repair closure:

`be8682b4e48a1836a93fabb2f857fa8c28aa33ad`

Main is 27 commits ahead of the governance branch's shared base. The changed main-line surfaces are B2 product/evaluation work, `MEMORY.md`, B2 plans/working-memory, experiment source/tests, a developer smoke runner, and audit lifecycle state.

No latest-main changes were observed in:

- `AGENTS.md`;
- `OPERATING_GUIDE.md`;
- the five admitted Skills or their references;
- `tools/agent-governance/`;
- this governance-evolution proposal/plan family.

Classification:

```text
NO MATERIAL GOVERNANCE OVERLAP
```

## 5. Targeted re-audit result

At the repaired branch state:

```text
authorization / semantic-owner conflicts     → 0 observed
unexplained product source/test branch drift → 0 observed
default Learning-by-Doing reachability       → repaired / coherent
method vs full Skill distinction             → explicit
Learning-Only product-read-only boundary     → preserved
progressive state preservation               → explicit + proportional
conditional reference behavior               → preserved
proportionality / anti-rabbit-hole model      → preserved
sixth Skill                                   → deferred / no admission
proposal/Stage-1 lifecycle restart pressure  → repaired
latest-main governance overlap               → none observed
```

Final disposition:

```text
READY FOR MAIN RECONCILIATION
```

## 6. Proof limitation and remaining obligation

No repository-wide executable PASS is claimed for:

```bash
python tools/agent-governance/governance_doctor.py
```

That validation remains deliberately deferred until the governance branch is reconciled/finalized, merged with Ali's explicit authorization, and pulled locally.

The behavioral case banks are contracts/manual evaluation surfaces; no statistical live-agent pass rate or observable universal Skill-load trace is claimed.

## 7. Handoff

The governance/Skills evolution branch is internally ready for latest-main reconciliation.

Do not treat this record as merge authorization. Merge/rebase/cherry-pick to `main` remains a separate action requiring Ali's explicit instruction.

After an authorized merge and local pull, run the deferred governance doctor and fix only concrete failures if any rather than reopening the whole governance redesign.