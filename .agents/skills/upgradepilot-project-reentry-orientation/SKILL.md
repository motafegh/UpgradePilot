---
name: upgradepilot-project-reentry-orientation
description: Re-orient Ali to the current UpgradePilot responsibility after a break, a new conversation, or meaningful parallel project progress. Recover the smallest accurate current context from canonical live owners, optionally reconstruct a verified delta only when the prior meaningful touchpoint is explicit or recoverable, and return a compact current-responsibility / flow / proof / non-proof / defer / ownership-question / resume-point packet. Use when Ali asks to continue, resume, get oriented, catch up, check the latest project state before deciding what to do, or understand what changed since the last meaningful touchpoint. Read-only by default; never create a second live-state owner or silently continue into implementation, planning, audit, or learning work beyond the user's authorization.
---

# UpgradePilot Project Re-entry Orientation

Use this Skill as the compact **support/composition procedure** for returning Ali to meaningful UpgradePilot work with the smallest accurate current context.

**Skill provenance marker:** `UP-SKILL:upgradepilot-project-reentry-orientation`

This is **not a primary operation mode**. It does not replace Audit/Review, Planning/Design, Build/Implement, Learning-by-Doing, Learning-Only, Working Memory, Learning Artifact, or Workstream Supervision. It prepares the current project model so the correct next operation can be selected or resumed without paying the full repository-orientation cost again.

`MEMORY.md` remains the sole owner of the live project position. `OPERATING_GUIDE.md` remains the owner of project-wide context discipline, proportionality, Learning-by-Doing, evidence interpretation, and handoff. This Skill applies those owners to the recurring re-entry problem; it does not create another state system.

## 1. Activation boundary

Use this Skill when Ali asks, explicitly or clearly, to do things such as:

- continue or resume UpgradePilot from the latest point;
- get properly oriented before deciding what to do;
- check the current project state / latest progress / recent work;
- catch up after a break or a new conversation;
- recover what matters after another session or agent advanced the project;
- explain what changed since Ali's last meaningful touchpoint;
- prepare a compact current-state packet before learning or substantive work.

Typical user language includes:

```text
continue from where we left off
get oriented first
check the latest state and recent work
what changed since last time?
catch me up, then we decide
re-enter the project before we continue
```

Do **not** load this Skill merely because every new chat technically begins with some context recovery. Use it when re-entry/orientation is a material responsibility rather than an invisible trivial read.

Do not use it as a substitute for:

- a formal repository Audit/Review;
- supervision/reconciliation of named parallel agent workstreams;
- a Learning-Only mastery session;
- a durable learning-artifact request;
- ordinary continuation inside a session whose current state is already clear;
- implementation/planning permission.

## 2. Default action boundary — read and orient, do not silently act

Re-entry is **read-only by default**.

The normal result is a current orientation packet and, when appropriate, a recommendation about which existing operation/procedure owns the next responsibility.

Do not, merely because re-entry identifies a next action:

- edit product source/tests;
- change a plan/specification/ADR;
- update `MEMORY.md` or working memory;
- open a new implementation responsibility;
- start a formal Audit or Planning operation;
- create a learning artifact;
- mutate an external/target repository.

If Ali's request also clearly authorizes a next operation (for example, "get oriented and then continue the already-authorized analysis"), complete re-entry first, then route that substantive responsibility normally. Re-entry does not grant authority that the user/project did not already provide.

## 3. Two re-entry modes

### 3.1 Current-state orientation — default and always available

Use current canonical project truth to answer:

```text
where are we now?
what responsibility is active?
what has actually been established?
what remains unresolved or unproven?
where should Ali resume attention?
```

This mode does **not** require reconstructing Ali's prior session.

### 3.2 Verified delta orientation — conditional

Add "what changed since Ali's last meaningful touchpoint" only when the baseline is explicit or reliably recoverable.

Acceptable baseline evidence may include:

- an exact commit/ref explicitly supplied by Ali or preserved in the current conversation;
- a clearly identified prior project position or handoff that is known to correspond to Ali's last meaningful touchpoint;
- a prior conversation/session record with a sufficiently exact project horizon;
- another explicit dated/commit-pinned reference whose relationship to Ali's prior touchpoint is established.

Do **not** infer the baseline merely from:

- the newest old working-memory file;
- file modification timestamps;
- a plausible nearby commit;
- whichever historical artifact looks most relevant;
- the fact that a conversation is new.

If the baseline is uncertain, fail closed:

> provide a **current-state-only** orientation and state that the historical delta horizon is not established.

Never invent a plausible "since last time" story.

## 4. Required and conditional context route

Follow root `AGENTS.md` and the `OPERATING_GUIDE.md` context-discipline principle: load the **smallest sufficient evidence chain**.

### REQUIRED FOR MATERIAL RE-ENTRY

Normally establish:

```text
nearest applicable AGENTS.md
→ this Skill
→ current MEMORY.md
```

`MEMORY.md` determines the live responsibility, selected plan, active working memory, current mode, blockers/deferrals, and current handoff.

### CONDITIONAL — LOAD ONLY WHEN NEEDED TO MAKE THE PACK ACCURATE

From the current `MEMORY.md`, follow only the owners needed to understand the selected responsibility:

```text
selected bounded plan / current responsibility owner
→ active working-memory record when detailed recent reasoning/handoff matters
→ exact source/tests/evidence needed to substantiate current implementation/proof claims
→ applicable specification/ADR when accepted semantics or method are material
```

For verified delta mode, additionally inspect only the history/diff needed to compare the known baseline with current truth.

Use current source/tests when the orientation packet makes an implementation/proof statement that cannot safely be supported by `MEMORY.md` alone. Do not reread implementation merely to make the packet look thorough.

### DO NOT LOAD REFLEXIVELY

Do not automatically scan:

- all plans;
- all working-memory history;
- all specifications/ADRs;
- learning snapshots;
- proposals/archives;
- product-simulation cases;
- Career repository/state;
- `ENVIRONMENT.md` or `SECURITY.md` when their triggers are absent;
- unrelated source/tests.

History is loaded for a precise delta/provenance question, not because old context exists.

## 5. Freshness and mixed-horizon protection

A re-entry packet should represent one reasonably coherent current horizon.

When meaningful parallel project progress may be occurring:

1. identify the current repository/branch horizon when practical;
2. read current `MEMORY.md` and the selected owners from that horizon;
3. avoid mixing an older source/test observation with a newer live-state claim without saying so;
4. if the repository changes materially during a long orientation pass, refresh the affected live owner/evidence before finalizing the packet.

Do not turn this into transactional snapshot machinery for ordinary orientation. The goal is to avoid obvious mixed-time synthesis, not to claim cryptographic or transactional consistency.

## 6. Recover the current responsibility before details

Before reading deeply, answer from current owners:

```text
What exact engineering/learning responsibility is active now?
What mode/authorization boundary is active?
Which plan/working-memory owner currently matters?
What has already closed and should not be reopened without evidence?
What is the immediate handoff or decision boundary?
```

Prefer the **complete semantic responsibility** over internal stage codes or historical shorthand.

If `MEMORY.md` itself appears stale, contradictory, or unable to support a current orientation, do not silently reconstruct a replacement live state from history. Surface the inconsistency and route the issue to the appropriate Audit/Working-Memory/live-state correction responsibility.

## 7. Recover only the material engineering flow

A useful re-entry packet normally includes **one** compact mental model or flow for the active responsibility.

Examples:

```text
producer / source evidence
→ transformation / interpretation
→ consumer / decision
→ current proof boundary
```

or:

```text
input/state
→ current mechanism
→ important branch/failure/unresolved state
→ output/evidence
```

Choose the flow that helps Ali resume reasoning. Do not summarize the whole architecture or enumerate every module.

When source/test detail is central, select the smallest representative locations worth reopening rather than listing the entire package.

## 8. Separate proof, non-proof, and unresolved state

Re-entry must preserve UpgradePilot's evidence discipline.

Keep distinct:

```text
CURRENT FACT / IMPLEMENTED OR OBSERVED
→ what current owners/source/tests/evidence establish

PROOF LIMIT / NON-CLAIM
→ what that evidence does not establish

UNRESOLVED / DEFERRED
→ what remains open, blocked, intentionally deferred, or not yet authorized
```

Do not convert:

- green tests into stronger semantic claims they do not prove;
- AI-generated implementation into Ali ownership;
- a plan into implementation truth;
- a historical rationale into current authority;
- a listed limitation into an automatically authorized next build.

## 9. Verified delta reconstruction — when admitted

When a reliable prior baseline exists, summarize **semantic change**, not raw commit chronology.

Prefer:

```text
prior meaningful responsibility/state
→ material responsibilities that closed/changed
→ current responsibility/state
→ changed proof/non-proof boundary
```

Group commits/files by engineering meaning. Mention exact commits/files only when they materially anchor the delta.

Do not dump:

- every commit;
- every file changed;
- every working-memory entry;
- routine refactors with no re-entry value.

If some part of the delta cannot be established confidently, label that part uncertain rather than filling the gap with inference.

## 10. Standard re-entry packet

Adapt the length to the user's request, but the default useful packet is:

### 1. Current responsibility

One short statement of what UpgradePilot is currently trying to decide/build/prove/learn and the active authorization/mode boundary.

### 2. Material change since baseline — only when verified

A few semantic changes that matter to Ali's return. Omit this section or explicitly say the delta horizon is unknown when no trustworthy baseline exists.

### 3. Current engineering flow / mental model

One compact flow that reconnects the current responsibility to the real system.

### 4. Current proof / non-proof

What is established now and the most important stronger claims that remain unsupported.

### 5. Exact owners / evidence worth opening

Normally only a small set such as:

```text
MEMORY.md
selected plan
active working memory
1–3 source/test/evidence locations when material
```

Do not provide a giant reading list.

### 6. What not to broaden into

Name the nearest tempting but currently unjustified directions when that prevents wasted attention or accidental scope expansion.

### 7. Ownership reactivation questions

Ask approximately **3–5** short open-ended questions when useful. They should reactivate understanding, not pretend to certify mastery.

Prefer questions such as:

- why does this distinction matter?
- what does this proof establish and not establish?
- what failure/ambiguity keeps the stronger state unresolved?
- what evidence would justify the next step?
- if one condition changed, what result should you expect?

### 8. Resume point

State the exact current handoff / next authorized decision or action **as owned by `MEMORY.md` / the selected plan**, without silently beginning it.

## 11. Compact and low-energy variants

When Ali asks for a brief orientation or is clearly using the packet as low-energy reconnection, compress rather than remove accuracy.

A compact variant may be:

```text
NOW
→ current responsibility

FLOW
→ one mental model

PROVEN / NOT PROVEN
→ strongest useful boundary

DO NOT BROADEN INTO
→ 1–3 nearest distractions

RESUME
→ exact handoff

RECALL
→ 1–3 questions
```

Do not force retrieval questions when Ali only needs a factual status check. Do not interpret low-energy review as mastery evidence.

## 12. Composition with other UpgradePilot Skills

### Working Memory

Reading the active working-memory record for re-entry does **not** require activating `upgradepilot-working-memory`.

Compose `.agents/skills/upgradepilot-working-memory/SKILL.md` only when the session is also creating, updating, continuing, or closing working memory.

### Learning-by-Doing

Re-entry prepares the broader current context. It does not replace the next substantive slice's A → B → C → D → E cycle.

If the re-entry packet already covers some of the next slice's A-stage orientation, reuse/compress that overlap proportionately; do not repeat it ceremonially, but do not skip a materially different pre-action learning boundary.

### Learning-Only

If Ali decides after re-entry to pause project action and master a topic, route to Learning-Only. Re-entry itself does not become a mastery session.

### Learning Artifact

Do not create a durable re-entry artifact by default. If Ali separately asks for reusable study/relearning material, compose `upgradepilot-learning-artifact` and follow `learning/README.md`.

### Workstream Supervision

Use re-entry when the goal is **Ali's own current project orientation**.

Use `upgradepilot-workstream-supervision` when the goal is to supervise/reconcile named parallel agent workstreams, check whether they followed the right routes, or decide whether intervention is required.

A project that advanced in another session does not automatically require Workstream Supervision; simple current-state re-entry may be enough.

### Audit / Planning / Build

Re-entry may identify that Audit, Planning/Design, or Build is the correct next operation. Route to that procedure only when the user's request/authorization and current responsibility actually require it.

## 13. No new live-state artifact by default

The re-entry packet is normally **ephemeral conversation output**.

Do not create:

- `REENTRY.md`;
- a Future-Ali state file;
- a second handoff tracker;
- a daily orientation log;
- a Career-side project mirror;
- a new working-memory record merely because orientation occurred.

If a material live-state problem is discovered, update the correct owner only under the proper operation/authorization. If a durable educational artifact is requested, route to the learning-artifact procedure instead.

## 14. Quality checks before handoff

Before returning the packet, verify proportionately:

```text
current MEMORY.md actually consulted?
current responsibility stated semantically and accurately?
selected owners followed rather than broad repository scan?
delta included only with a trustworthy baseline?
current fact vs history/inference separated?
one useful current flow, not whole-system summary?
proof and non-proof both visible?
next action quoted/recovered from current owner rather than invented?
unjustified scope expansion explicitly avoided when material?
packet small enough to reduce re-entry cost?
no product/governance/live-state mutation performed merely for orientation?
```

If the answer to the delta-baseline check is no, remove the delta and use current-state-only orientation.

## 15. Stop condition

Stop when Ali has enough accurate current context to:

- understand where UpgradePilot actually is;
- recover the active responsibility and proof boundary;
- know what context matters and what can be ignored;
- decide, learn, review, or resume the next authorized responsibility through the correct operation.

Do not keep expanding context because more repository information is available.

## Anti-patterns

Do not:

- reconstruct live state from historical working memory when `MEMORY.md` is available and coherent;
- fabricate a last-touchpoint delta;
- dump commit history as orientation;
- load the whole repository for completeness;
- produce a second live-state document;
- treat re-entry questions as capability scoring;
- turn orientation into an unsolicited audit;
- begin implementation because the packet found a ready Build step;
- duplicate the selected plan or `MEMORY.md` verbatim;
- re-teach the entire project when one current responsibility is enough;
- confuse "another session changed the repo" with a requirement to supervise that other session;
- update Career merely because project state changed.

## Provenance

When this full Skill is materially used and a normal completion/handoff surface exists, emit:

```text
UP-SKILL:upgradepilot-project-reentry-orientation
```

Marker presence records Skill activation only. Accuracy comes from the current owners/evidence and the quality of the orientation packet, not from the marker.
