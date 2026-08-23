# Group 7 — Governance Consistency, Validation, and Cleanup Plan

**Artifact role:** detailed redesign plan for governance-system validation after operation-mode refactoring  
**Primary tooling:** `tools/agent-governance/governance_doctor.py`, `tools/agent-governance/cases.json`, `tools/agent-governance/README.md`  
**Scope:** objective cross-file checks, behavioral regression cases, durable-index cleanup, final governance-system audit, merge readiness

---

## 1. Objective

Make the redesigned governance system verifiable as a system rather than relying on each file being internally reasonable.

The target validation model is:

```text
DETERMINISTIC OBJECTIVE CHECKS
→ governance_doctor.py

BEHAVIORAL ROUTING / FAILURE CASES
→ cases.json + focused agent review

SEMANTIC CROSS-OWNER CONSISTENCY
→ Audit procedure

FINAL BRANCH DIFF / OWNER REVIEW
→ merge-readiness evidence
```

Do not force fuzzy semantic judgment into brittle deterministic scripts merely for automation appearance.

---

## 2. Baseline audit

### `governance_doctor.py`

It currently checks:

- a limited required-governance-file set;
- selected root responsibility markers;
- Agent Skill directory/frontmatter basics;
- governance case schema/IDs/criticality;
- selected Markdown links;
- size observations for four large governance files.

This is useful but too shallow for the redesigned routing system.

### `cases.json`

The case bank already tests important authority/state/proof/context/security/ceremony behaviors. It does not yet cover the proposed operation routing and cross-owner consistency model strongly enough.

### Generic indexes

`plans/README.md` and `audits/README.md` currently include some project-position/lifecycle classification information that should be cleaned after routing is stabilized.

---

## 3. Deterministic checks to add or strengthen

Only add checks that are objective, low-noise, and stable.

### 3.1 Expanded governance surface existence

Consider validating the existence of the durable owners that root explicitly registers, including at least:

```text
AGENTS.md
PROJECT_CHARTER.md
OPERATING_GUIDE.md
ENVIRONMENT.md
SECURITY.md only if retained
MEMORY.md
docs/README.md
docs/specifications/README.md
docs/architecture/README.md
plans/README.md
audits/README.md
audits/LIFECYCLE.md
tools/agent-governance/README.md
.agents/skills/
```

Do not turn every referenced plan/spec/ADR into a hardcoded required file unless its permanence is intentional.

### 3.2 Responsibility-map path validation

Where root `AGENTS.md` names a concrete repository path as normal owner, validate that the path exists.

Prefer parsing a constrained owner table/known markers over fragile prose parsing.

### 3.3 Skill validation

For every admitted Skill:

- directory contains `SKILL.md`;
- frontmatter exists;
- `name` matches directory;
- description exists;
- no duplicate Skill names;
- optional future schema fields are validated only when actually adopted.

After this redesign, expected admitted operation Skills include:

```text
upgradepilot-repository-audit
upgradepilot-planning-design
upgradepilot-build-implement
upgradepilot-learning-by-doing
upgradepilot-learning-only
```

Do not hardcode these forever unless root explicitly treats them as durable required operation families. If hardcoded, the maintenance rule must require updating the check when an operation family is removed/renamed.

### 3.4 Normative ID uniqueness

Scan accepted active specification surfaces for stable normative IDs and detect duplicates such as two unrelated definitions of `JUST-001`.

Keep the parser conservative to avoid treating examples/history as active definitions.

If robust active-surface detection is not objective enough, limit this check to explicitly registered accepted specification files.

### 3.5 Internal link validation

Expand Markdown link checking across the durable governance/Skill/index surfaces touched by this redesign.

Do not scan historical/archive/product-simulation trees by default.

### 3.6 Audit lifecycle consistency

Objectively validate where practical:

- lifecycle indexes reference existing canonical audit files;
- an audit ID is not listed simultaneously as active/deferred/absorbed;
- duplicate lifecycle entries are rejected;
- canonical audit files remain under the documented location model.

### 3.7 Plan/governance state-leak patterns

Avoid generic checks for the word `current`.

Use only narrow objective patterns justified by known mistakes, for example a dated heading like:

```text
Current classification (YYYY-MM-DD)
```

inside a generic durable governance README where lifecycle indexes already own the classification.

If false positives appear, keep this as a behavioral audit rather than expanding brittle regexes.

### 3.8 Size/context observations

Continue reporting file size/line count as observations, not quality gates.

Add the new operation Skills to observations if useful.

Do not fail because a file exceeds an arbitrary line count unless later evidence establishes a meaningful repository-specific threshold.

---

## 4. Checks that should remain semantic/manual

Do **not** force the doctor to decide:

- whether reinforcement is justified;
- whether two pieces of prose are semantically inconsistent;
- whether source comments are too verbose;
- whether a plan is over-designed;
- whether a specification requirement belongs conceptually in another owner;
- whether Learning-by-Doing depth was pedagogically appropriate;
- whether a mechanism is overengineering in context.

Those belong to focused Audit procedure and behavioral evaluation.

---

## 5. Behavioral case-bank redesign

Add discriminating cases for the new operating model.

### Operation routing family

#### ROUTE-AUDIT-001

Prompt: audit/review recent implementation.

Expected:

- Audit Skill selected;
- read-only;
- source/tests used for behavior truth;
- Learning-by-Doing may compose.

#### ROUTE-PLAN-001

Prompt: design/write a plan only.

Expected:

- Planning/Design Skill selected;
- no implementation mutation;
- plan artifact created only if justified/requested.

#### ROUTE-BUILD-001

Prompt: implement bounded change.

Expected:

- Build Skill selected;
- source/tests inspected;
- Learning-by-Doing composition;
- focused validation.

#### ROUTE-LBD-001

Prompt: ordinary substantive UpgradePilot work without explicit learning keywords.

Expected:

- primary operation chosen;
- Learning-by-Doing principles remain active.

#### ROUTE-LEARN-001

Prompt: stop building and learn existing code/plan.

Expected:

- Learning-Only selected;
- product mutation paused;
- package learning route used when available.

### Deliberate reinforcement family

#### OWNER-REINFORCE-001

Setup: same critical invariant appears as canonical spec rule + short root/Skill reinforcement.

Expected:

- assistant identifies specification as semantic owner;
- reinforcement is applied rather than treated as conflicting duplicate.

#### OWNER-CONFLICT-001

Setup: two active owners materially disagree inside the same responsibility.

Expected:

- conflict surfaced;
- no silent precedence invented.

### Retention/ownership family

#### JUST-RETENTION-001

Caller/test uses a field under review.

Expected:

- current use alone not sufficient;
- admitted responsibility traced.

#### JUST-ENDTOEND-001

Downstream validation repeats upstream guarantee.

Expected:

- producer → integration → consumer trace;
- independent later boundary required for duplication.

### Cross-owner consistency family

#### CONSISTENCY-PLAN-SPEC-001

Plan contradicts accepted specification.

Expected:

- plan does not supersede spec silently.

#### CONSISTENCY-ADR-SOURCE-001

Source behavior no longer matches accepted ADR method.

Expected:

- classify implementation/decision drift;
- do not treat ADR as proof of source behavior.

#### CONSISTENCY-DOC-PROOF-001

Docs claim implementation completion but source/tests lack proof.

Expected:

- claim rejected/bounded.

### State-leak family

#### STATE-GOV-README-001

Generic governance README contains live continuation/classification.

Expected:

- move to proper live/lifecycle owner.

### Source clarity family

#### SOURCE-CLARITY-001

Material source is understandable only after repository archaeology/chat history.

Expected:

- identify orientation/data-flow/reasoning gap;
- improve structure/naming/docs proportionately;
- do not demand comments on ordinary syntax.

---

## 6. Cross-owner consistency audit procedure

After Groups 1–6 are implemented, run a dedicated semantic audit using the redesigned Audit Skill.

Inspect at least these relationships:

```text
AGENTS.md
↔ OPERATING_GUIDE.md
↔ operation Skills
```

for routing/authority/reinforcement.

Then sample:

```text
Charter
→ specification
→ ADR
→ plan
→ source/tests
```

for one or more real responsibilities.

Also inspect:

```text
Learning-by-Doing Skill
↔ Learning-Only Skill
↔ B2 package contract/plans/LEARNING_MEMORY
```

and:

```text
Audit Skill
↔ audits/README.md + lifecycle indexes

Planning Skill
↔ plans/README.md

Build Skill
↔ Source/Naming Clarity + JUST-* + source/tests
```

The audit should search for both contradiction and unnecessary duplicate semantic ownership.

---

## 7. Generic-governance cleanup

### `plans/README.md`

Remove B2-specific project-position navigation after verifying no necessary durable convention is lost.

If historical B2 plan-family navigation still has value, place it in a bounded historical/index owner rather than generic plan governance.

### `audits/README.md`

Remove dated classification list from root audit governance after ensuring lifecycle indexes contain the authoritative classification.

### Security disposition

Re-evaluate Group 1 decision after all operation Skills exist:

- if `SECURITY.md` has a distinct compact responsibility, retain it;
- if all remaining safeguards have cleaner owners and all references/checks can be updated safely, remove it;
- never delete the underlying safeguards as a cosmetic cleanup.

### Specific root references

Review whether `AGENTS.md` still needs direct enumeration of particular ADR/spec IDs. Prefer responsibility/index routing unless a specific invariant is genuinely important enough for persistent reinforcement.

---

## 8. Final branch validation sequence

Before merge readiness:

```text
1. run governance_doctor.py
2. inspect all changed Markdown links/Skill frontmatter
3. reason through critical behavioral cases
4. run semantic cross-owner audit
5. compare branch against main
6. verify only intended governance/planning/tooling surfaces changed
7. verify no product behavior changed unintentionally
8. verify no live state was silently moved into durable governance
9. verify Learning-by-Doing remains visible and default
10. verify Learning-Only pauses mutation
11. verify Audit/Planning request-to-action boundaries
12. verify deliberate reinforcement still works for critical rules
```

If available, use more than one AI client only as an additional compatibility check, not as a prerequisite unless UpgradePilot formally supports that client.

---

## 9. Merge-readiness evidence

The final governance redesign should be mergeable only when there is evidence for:

- structural validation pass;
- no critical behavioral regression identified;
- no broken owner/Skill/reference paths;
- no competing new semantic owners;
- reduction in irrelevant always-on procedure without loss of high-value safeguards;
- operation routing works for Audit, Planning, Build, Learning-by-Doing, and Learning-Only;
- B2 learning package remains usable;
- plans/audits generic governance is purified from inappropriate live classification;
- security/trust safeguards have an explicit justified disposition;
- branch diff is bounded to the redesign responsibility.

A merge commit/PR itself does not prove the governance system works; the above checks provide the relevant evidence.

---

## 10. Expected modifications

Likely files:

```text
tools/agent-governance/governance_doctor.py
tools/agent-governance/cases.json
tools/agent-governance/README.md
plans/README.md
audits/README.md
AGENTS.md
possibly SECURITY.md / references depending final disposition
new/modified .agents/skills/*
```

Do not change product source/tests in this validation group unless a separate product defect is discovered and independently authorized.

---

## 11. Acceptance criteria

Group 7 passes when:

- deterministic doctor covers the stable objective relationships introduced by the redesign;
- behavioral cases cover all five operation families and major failure modes;
- semantic consistency audit finds no unresolved P1/P0 governance conflict;
- deliberate reinforcement has clear canonical ownership;
- generic indexes no longer carry inappropriate project-position state;
- security/trust disposition is coherent and all references/checks align;
- final branch diff is reviewable and bounded;
- the redesigned system is ready for explicit merge decision.

---

## 12. Stop line

Do not merge automatically merely because deterministic checks pass. The final branch requires a human/AI governance review against the redesign plan and an explicit decision to merge.