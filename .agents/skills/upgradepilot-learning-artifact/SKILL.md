---
name: upgradepilot-learning-artifact
description: Author or materially revise reusable UpgradePilot study/relearning artifacts from real project code, tests, plans, designs, concepts, evidence, and directly relevant history. Use when Ali asks to write learning notes, study guides, relearning notes, code/design/plan explanations, concept companions, or a small learning package for later study. Ground current truth in active owners/source/tests, use relevant working-memory for history, prefer real UpgradePilot cases/flows, and audit questionable material instead of inventing rationale.
---

# UpgradePilot Learning Artifact Authoring

Use this Skill as the compact **support/artifact-authoring procedure** for reusable material under `learning/`.

**Skill provenance marker:** `UP-SKILL:upgradepilot-learning-artifact`

This is **not a primary operation mode**. It does not replace Learning-Only, Learning-by-Doing, Audit, Planning/Design, Build/Implement, or Working-Memory.

`learning/README.md` is the canonical owner for learning-artifact meaning, snapshot policy, placement, depth, proportionality, and maintenance. `OPERATING_GUIDE.md` owns project-wide teaching/ownership/depth/evidence principles. This Skill applies those owners without re-specifying them.

## Activation and write boundary

Use this Skill when Ali asks for a durable artifact to study or relearn later, for example:

```text
write learning notes for this source code
make me a study guide for this plan/design
create a learning artifact for this concept/API/tool
write a compact note so I can master this later
turn these related files into a useful learning package
```

The artifact itself is the deliverable. Do **not** require an interactive lesson, quiz, learner response, or mastery demonstration merely to author it.

An explicit request to create/update a learning artifact authorizes only that bounded learning-artifact work and directly necessary evidence inspection. It does **not** authorize product/source/test repair, plan/spec/ADR changes, external mutation, or unrelated cleanup.

When active interactive mastery is also requested, compose Learning-Only for that learning session. When the artifact is produced during real project work, the primary operation and Learning-by-Doing boundaries remain unchanged.

## 1. Identify the exact learning deliverable

Establish proportionately:

```text
what Ali wants to learn later
→ exact responsibility/mechanism/flow
→ current or historical snapshot horizon
→ intended depth/use
→ one focused note or small ordered package
```

Prefer a meaningful engineering responsibility over raw file boundaries. Several files may form one learning unit; one large file may contain several distinct learning responsibilities.

Do not create a package merely because several source files exist.

## 2. Establish current truth before explaining it

For a current code/design/plan responsibility, use the smallest evidence chain that can support the teaching claims:

```text
applicable canonical owner(s)
→ current source/tests/commands/evidence
→ directly relevant history when needed
→ representative real case/flow when available
```

Examples of authority/evidence roles:

- specification/Charter → accepted stable requirement/semantics;
- ADR → accepted consequential method/structure;
- plan → bounded sequence/proof/stop responsibility;
- source/tests/commands/output → implemented/observed truth;
- working-memory → dated history, rationale evidence, errors, decisions, fixes, rejected/deferred alternatives;
- product-simulation → real discovery cases and pressure evidence;
- learning snapshot → prior educational model, not current implementation authority.

Never use the artifact being authored as proof of its own claims.

## 3. Recover directly relevant history, not all history

When implementation path, rationale, errors, repairs, user questions, rejected alternatives, or deferrals matter to understanding, search/read the directly related working-memory records.

Useful retrieval clues include:

- exact source/type/function name;
- plan/step identifier;
- real case identifier;
- error text;
- concept/mechanism name;
- approximate date or implementation tranche.

Do **not** scan all working-memory reflexively.

Treat history as evidence about **how/why the path was reached**, not as authority over current truth. If historical reasoning conflicts with current source or accepted owners, teach the distinction explicitly.

Loading `.agents/skills/upgradepilot-working-memory/SKILL.md` is unnecessary merely to read historical records; use it only when this session is also maintaining working memory.

## 4. Pressure-test the material; never invent rationale

Keep these separate:

```text
CURRENT FACT
what the project actually does

EVIDENCED RATIONALE
why the mechanism exists, only when evidence supports that claim

ENGINEERING JUDGMENT
whether it is correct, necessary, proportionate, well placed, weak, broad, stale, or improvable

ALTERNATIVE / IMPROVEMENT
another credible approach and its trade-offs when useful
```

If something looks defective, contradictory, stale, unnecessary, misleading, or suspicious:

1. do not rationalize it because it exists;
2. inspect the nearest relevant source/tests/owner/history;
3. use `OPERATING_GUIDE.md` rationale/necessity reasoning proportionately;
4. when the question becomes materially evaluative, compose `.agents/skills/upgradepilot-repository-audit/SKILL.md` for that bounded review;
5. classify honestly: justified / known-fixed / defect or stale behavior / questionable trade-off / improvement opportunity / unresolved;
6. teach the finding, fix, alternative, and proof limits when useful.

Audit findings do **not** authorize Build. If repair would be useful, record/explain it and stop unless Ali separately authorizes implementation.

## 5. Teach through real UpgradePilot cases and flows

Real project material is the default teaching substrate:

```text
real user/repository scenario
→ real input/evidence
→ actual source/control/data flow
→ important decision/trust boundary
→ result/problem state
→ focused proof/non-proof
```

Prefer real product-simulation cases, real implementation incidents, and actual tests over detached toy examples.

A tiny toy example is allowed only when isolating syntax/API behavior makes the real code easier to understand. Reconnect it immediately to the actual UpgradePilot mechanism.

Never present a fabricated failure fixture as the normal production flow.

## 6. Calibrate depth instead of explaining everything

Use the existing project-wide learning doctrine:

- **must master / own** — central responsibility, mechanism, boundary, decision, or proof relation;
- **understand operationally** — enough to read/reason/modify/debug/review/use safely;
- **recognize / lookup-level** — understand what incidental syntax/library/API machinery does here and know how to recover details;
- **deferred deliberately** — deeper internals that do not unlock the selected responsibility now.

Explain unfamiliar technical terms accurately, including full form/practical meaning/role when useful, but do not turn incidental syntax or library internals into prerequisite courses.

Engineering ownership is not source memorization. The artifact should improve reasoning, review, modification, testing, debugging, and decision capability.

## 7. Choose the smallest complete artifact shape

Adapt to the subject rather than forcing one template.

### Source/code responsibility

Usually emphasize:

```text
responsibility / non-responsibility
→ inputs/state/types
→ normal flow
→ important failure/problem paths
→ trust/authority boundaries
→ material syntax/API mechanisms
→ rationale/judgment where evidenced
→ tests and non-proof
→ representative real case
```

### Plan

Usually emphasize:

```text
problem/outcome
→ scope/exclusions
→ sequence/responsibility decomposition
→ dependencies/gates
→ decisions/rationale
→ proof obligations
→ stop/deferred scope
```

### Architecture/design/ADR

Usually emphasize:

```text
problem pressure
→ accepted constraints
→ meaningful alternatives
→ chosen ownership/structure
→ trade-offs/failure modes
→ implementation consequences
```

### Concept / syntax / API / tool

Usually emphasize:

```text
practical meaning
→ why it exists
→ exact UpgradePilot role
→ nearby distinctions
→ current required depth
→ lookup/deferred internals
```

### End-to-end flow

Trace one real representative case from producer/input through transformations/trust boundaries to consumer/result/proof.

Prefer one focused note. Use a small ordered package only when genuinely distinct responsibilities would make one note hard to study or revisit.

## 8. Author for study and relearning

Use only sections that materially help. A strong artifact normally makes recoverable:

- purpose and snapshot/evidence horizon;
- big-picture mental model;
- responsibility boundaries;
- representative real flow/case;
- important failure paths/trust boundaries;
- material concepts/syntax/APIs at calibrated depth;
- current fact vs rationale vs engineering judgment;
- proof/tests and non-claims;
- known issues/fixes/alternatives when useful;
- source/plan/design/history anchors;
- a short **fast relearning route**;
- a few ownership/transfer questions when useful.

Summarize; do not copy whole plans/specifications/working-memory/logs/source into the note.

Target the **smallest complete study artifact**: enough mechanism/context to learn from, but short enough to revisit.

## 9. QA before finishing

Check proportionately:

```text
accurate against current/pinned evidence?
authority vs history separated?
any invented rationale?
real project flow used where available?
depth proportional?
important failure/proof limits present?
artifact size usable?
fast relearning path actually useful?
source/history anchors sufficient?
no accidental product/plan/spec mutation?
```

For code-bearing snapshots, identify the relevant source/test revision or explicit evidence horizon.

Do not claim learner mastery merely because a high-quality note exists.

## 10. Stop and hand off

Stop when the requested artifact/package is useful and evidence-bounded.

If authoring exposed a material problem:

```text
teach/report the finding
→ state evidence and uncertainty
→ identify the appropriate Audit/Planning/Build continuation if useful
→ do not perform that new operation unless separately authorized
```

Do not update `MEMORY.md` merely because a learning artifact was created. Do not create working-memory merely to record this Skill's use.

## Anti-patterns

Do not:

- paraphrase source line by line;
- explain every import/API equally;
- copy a plan/specification into prose and call it learning;
- invent rationale for questionable code;
- teach current implementation as inherently correct;
- scan all working-memory/history;
- prefer toy examples when a real UpgradePilot case adequately teaches the mechanism;
- turn lookup-level syntax into a detached course;
- create a package/index/contract/learning memory for every note;
- silently rewrite frozen historical snapshots to match new code;
- imply tests prove more than they exercise;
- repair product code without separate Build authorization;
- claim ownership/mastery from artifact existence.

## Provenance

When this full Skill was materially used and a normal completion/handoff surface exists, emit:

```text
UP-SKILL:upgradepilot-learning-artifact
```

Marker presence records claimed Skill activation only; the actual evidence route and artifact quality establish whether the procedure was followed.
