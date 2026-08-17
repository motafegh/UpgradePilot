# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 01 / Chunk 1 opened

## 1. Purpose and authority boundary

This file preserves the continuity of our interactive learning journey so important progress, discoveries, corrections, open questions, subtle proof boundaries, and potentially reusable learning material are not lost across conversations.

It is intentionally a **working memory**, not a finished learning note.

It may record:

- where we currently are in the approved learning plans;
- what Ali has actually understood, predicted, challenged, or diagnosed;
- important explanations or mental-model corrections that emerged during conversation;
- important real-case/source/test discoveries made while learning;
- `[~]` non-blocking gaps worth revisiting later;
- RED/blocking misunderstandings that must be repaired before proceeding;
- useful questions, comparisons, examples, or source traces that may deserve a later learning artifact;
- deviations from a plan and why they were justified;
- source/implementation movement that makes a remaining learning route stale;
- concise continuation instructions for the next conversation.

This file does **not** own:

- live UpgradePilot implementation/project status;
- authorization for implementation changes;
- architecture or product decisions;
- source/test truth;
- completion of a learning gate merely because a subject was discussed;
- polished reusable teaching content.

If this file conflicts with the learning contract, the contract wins. If it conflicts with current source/tests, source/tests win for implementation truth. If it conflicts with `../../MEMORY.md` about live project position, `../../MEMORY.md` wins.

## 2. Recording style

Keep entries concise but information-rich. Preserve what would be expensive or easy to forget, not a transcript of every message.

Use these status markers:

```text
[ ]  not started / not demonstrated
[~]  partial, useful but non-blocking gap remains
[x]  sufficiently demonstrated for the current route
[!]  blocking misconception/question; repair before continuing
```

For each active chunk, prefer this shape:

```text
Chunk status
Real question
Material covered
Ali-owned evidence
Important discoveries/corrections
Do-not-forget boundaries
Open [~] / [!] items
Artifact seeds
Next exact continuation
```

### What counts as Ali-owned evidence

Record an item as demonstrated only when Ali has done something that exposes understanding, for example:

- explained the mechanism in his own words;
- predicted an output/state before being shown it;
- correctly compared two cases;
- traced an important input → function → output path;
- identified an overclaim or proof boundary;
- diagnosed why an interpretation is wrong;
- later modified/tested a focused behavior when appropriate.

Immediate recognition after reading an explanation is not enough by itself.

## 3. Pace and momentum rule

This memory must help us move forward, not become extra paperwork.

- Update it at meaningful boundaries, discoveries, corrections, or session stops—not after every small exchange.
- A non-blocking gap is recorded as `[~]` and carried forward rather than forcing a perfection loop.
- Only `[!]` items that would make the next reasoning/code step materially unreliable should stop progress.
- When a later implementation step makes an older `[~]` item causally relevant, bring it back then.
- Do not delay building merely to convert all `[~]` items into `[x]`.
- If live project implementation advances, re-anchor the remaining learning route instead of mechanically completing stale study.

## 4. Artifact-seed rule

This file is also a capture surface for future reusable learning artifacts.

When a conversation produces something worth preserving later, add a short seed rather than writing the artifact immediately. A seed may include:

```text
SEED:
- subject / misconception / code trace;
- why it was useful;
- exact case/source/test anchors;
- what should be preserved if Ali later asks for a learning note.
```

Only create a polished learning note/artifact when Ali explicitly asks or when another controlling rule clearly requires one.

## 5. Learning route overview

```text
Plan 01 — S001 real case → first UpgradePilot evidence models
Plan 02 — S001 membership → CI consumption → coverage
Plan 03 — S011 + S005 generalization pressure
Plan 04 — application boundary → return to building
```

Overall momentum target:

```text
minimum accurate background
→ real evidence
→ real source/functions/tests
→ one meaningful user-owned check
→ proceed
→ return to building when sufficiently ready
```

## 6. Current implementation snapshot relevant to learning

Learning implementation anchor: `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`.

At the time this memory was opened, repository `MEMORY.md` records:

```text
Clusters 0–4: COMPLETE / GREEN
Cluster 5: IMPLEMENTED / VALIDATION PENDING
Cluster 6: NOT STARTED / HOLD
Tranche 2 static↔runtime correlation: NOT SELECTED
```

Do not silently promote Cluster 5 to validated or Cluster 6 to active from this learning memory. Re-read `../../MEMORY.md` before any return-to-building handoff.

## 7. Plan progress

### Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Status:** `[~] ACTIVE`  
**Opened:** 2026-08-17  
**Current chunk:** Chunk 1 — S001 orientation + Soup Sieve first contact

- [~] Chunk 1 — S001 orientation + Soup Sieve first contact — OPENED
- [ ] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence
- [ ] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI
- [ ] Chunk 4 — exact dependency transition + dependency-owned source context
- [ ] Chunk 5 — static workflow IR + project-environment selection

### Plan 02 — S001 Membership → CI Consumption → Coverage

**Status:** `[ ] NOT STARTED`

### Plan 03 — Generalization Pressure: S011 + S005

**Status:** `[ ] NOT STARTED`

### Plan 04 — Application Boundary + Return to Building

**Status:** `[ ] NOT STARTED`

## 8. Active chunk record — Plan 01 / Chunk 1

**Status:** `[~] IN PROGRESS`  
**Opened:** 2026-08-17

### Real question

Before touching lockfiles, CI, graph reachability, or UpgradePilot abstractions:

> What is Soup Sieve, why can a Pydantic dependency-update PR contain it, and what is the exact real dependency relationship that makes it relevant to this repository?

### Frozen real-case anchor

```text
repository: pydantic/pydantic
PR: #13432
changed dependency: soupsieve
transition: 2.6 → 2.8.4
base: 652a61ce4f9d7d76eaada31535807a485ece0e21
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
changed file: uv.lock
```

Historical S001 investigation established the documentation/tooling relationship:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

and also a second documentation-upload path:

```text
docs-upload
→ beautifulsoup4
→ soupsieve
```

At this chunk we use that relationship only to understand why Soup Sieve is present. We do **not** yet use `uv.lock` structure, environment selection, CI execution, or graph traversal as learned premises.

### First-contact items to establish now

- Soup Sieve;
- CSS selector at practical depth;
- Beautiful Soup at practical depth;
- direct versus transitive dependency only enough to explain the S001 path;
- why Pydantic can have a dependency used by documentation/tooling rather than its normal runtime library path.

### Do-not-forget boundaries

- dependency presence in the repository does not imply Pydantic's core runtime directly depends on or calls it;
- documentation/tooling dependency relevance can still matter to a dependency-update decision;
- do not jump from this relationship to claims that a particular CI environment selected/installed/executed Soup Sieve;
- do not jump to `uv.lock` internals until Chunk 2;
- S001 is historical manual case evidence, not proof that current ordinary UpgradePilot application already reconstructs this entire relationship.

### Ali-owned evidence

- [ ] Ali explains what Soup Sieve does in his own words.
- [ ] Ali explains the Beautiful Soup relationship.
- [ ] Ali explains why Soup Sieve can be transitive documentation tooling inside Pydantic rather than a direct core-runtime dependency.

### Open items

- none yet; chunk has just begun.

### Artifact seeds

- none yet; capture only if the live discussion reveals a particularly useful mental model, correction, or source trace.

### Next exact continuation

Teach the first-contact Soup Sieve / CSS selector / Beautiful Soup relationship using authoritative package documentation plus the frozen S001 dependency path. Stop for Ali's explanation/prediction before opening Plan 01 / Chunk 2.

## 9. Cross-session discoveries / corrections

None yet after formal Plan-01 start.

## 10. Yellow `[~]` backlog

None yet.

## 11. Blocking `[!]` backlog

None.

## 12. Future artifact seeds

None yet.
