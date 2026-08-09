---
name: upgradepilot-repository-audit
description: Audit or orient within the UpgradePilot repository while separating governance/context from implementation truth, honoring explicit exclusions, and reporting evidence-backed findings without unnecessary repository-wide scanning.
---

# UpgradePilot Repository Audit

Use this skill for repository-wide or bounded UpgradePilot audit/orientation requests where the procedure itself is useful but should not live in always-on root instructions.

This skill is **procedural and non-controlling**. Root `AGENTS.md` and the applicable responsibility owners remain authoritative. Do not copy or reinterpret their standing authorization/security rules here.

## Procedure

1. **Establish exact scope**
   - identify repository/ref when material;
   - preserve the user's explicit inclusions and exclusions;
   - distinguish audit/review-only intent from a separate explicit change request.

2. **Load only the needed owners**
   - start with the nearest applicable `AGENTS.md`;
   - load `MEMORY.md` only when current continuation/state matters;
   - load Security/Environment/Charter/plan/specification/ADR only when their responsibility is material;
   - do not speculatively scan archives, old working records, proposals, or unrelated controls.

3. **Separate the layers being audited**
   - governance/control documents define instructions, stable requirements, decisions, or context;
   - active source/tests/commands/outputs and relevant environment evidence establish implemented behavior;
   - experiments and developer tools keep their own proof classes.

4. **Establish implementation truth independently**
   - when behavior is part of the question, inspect active source/tests before accepting implementation claims from docs, plans, ADRs, memory, or historical records;
   - distinguish requirement/decision drift from implementation defects rather than collapsing them.

5. **Inspect the smallest sufficient evidence**
   - prefer exact files/symbols/tests/revisions over broad scans;
   - use history only for a precise provenance/comparison question;
   - do not execute untrusted upstream code merely to inspect it.

6. **Classify findings explicitly**
   Keep separate when material:
   - observation;
   - evidence/source context;
   - interpretation;
   - remaining uncertainty;
   - finding/severity;
   - recommended disposition or next discriminating check.

7. **Check responsibility and proportionality**
   Look for:
   - duplicate or conflicting ownership;
   - stale/current-state leakage into non-live owners;
   - implementation mechanisms owned by the wrong stable control;
   - proof-class collapse;
   - unnecessary persistent context, files, abstractions, plans, audits, or agent machinery;
   - missing deterministic enforcement where an objective repeated failure justifies it.

8. **Report with exact evidence**
   - prioritize material findings over exhaustive commentary;
   - state what was not inspected or could not be proven;
   - do not convert one case/tool/test into broader claims than it supports.

## Change boundary

For an audit/review/orientation request, remain read-only and report findings.

If the user separately and explicitly requests changes, follow root `AGENTS.md`'s request-to-action boundary and the applicable bounded plan/owner. An audit finding does not authorize implementation by itself.

## Output shape

Prefer a concise structure such as:

```text
scope and inspected revision
→ material observations
→ findings with severity/evidence
→ ownership/architecture implications
→ recommended smallest changes or next checks
→ explicit exclusions/limitations
```

Use a durable `audits/` record only when the finding itself has future review/reassessment value under `audits/README.md`; do not create one merely because an audit occurred.
