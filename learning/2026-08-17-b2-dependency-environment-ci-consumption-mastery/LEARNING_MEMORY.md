# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 01 / Chunk 2 in progress

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
**Current chunk:** Chunk 2 — `uv` + `uv.lock` using exact S001 evidence

- [x] Chunk 1 — S001 orientation + Soup Sieve first contact — GREEN
- [~] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence — IN PROGRESS
- [ ] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI
- [ ] Chunk 4 — exact dependency transition + dependency-owned source context
- [ ] Chunk 5 — static workflow IR + project-environment selection

### Plan 02 — S001 Membership → CI Consumption → Coverage

**Status:** `[ ] NOT STARTED`

### Plan 03 — Generalization Pressure: S011 + S005

**Status:** `[ ] NOT STARTED`

### Plan 04 — Application Boundary + Return to Building

**Status:** `[ ] NOT STARTED`

## 8. Completed chunk record — Plan 01 / Chunk 1

**Status:** `[x] GREEN`  
**Opened:** 2026-08-17  
**Completed sufficiently for route:** 2026-08-17

### Real question

> What is Soup Sieve, why can a Pydantic dependency-update PR contain it, and what is the exact real dependency relationship that makes it relevant to this repository?

### Material covered

- Soup Sieve as a CSS-selector library used with Beautiful Soup;
- Beautiful Soup as Python HTML/XML parsing/navigation tooling at the depth needed here;
- practical CSS-selector meaning;
- direct versus transitive dependency;
- exact S001 documentation-tooling path:

```text
docs
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

with a second `docs-upload → beautifulsoup4 → soupsieve` path.

### Ali-owned evidence

Ali explained in his own words that Soup Sieve is a CSS-selector library for Beautiful Soup, Beautiful Soup deals with documents such as HTML, and Pydantic reaches Soup Sieve indirectly through Beautiful Soup, making Soup Sieve transitive rather than a direct dependency.

- [x] Soup Sieve practical role explained.
- [x] Beautiful Soup relationship explained.
- [x] Transitive dependency relationship explained.

### Important correction / precision

Ali initially phrased the relation as “Pydantic uses Beautiful Soup.” The useful precision is:

> **Pydantic's documentation/tooling path uses Beautiful Soup; this does not imply Pydantic's normal core runtime directly depends on Beautiful Soup or Soup Sieve.**

This was a wording/ownership precision, not a blocking misconception.

### Do-not-forget boundaries

- repository dependency != core runtime dependency;
- transitive documentation dependency can still be relevant to a dependency-update investigation;
- this relationship alone does not establish which environment selected/installed it or whether CI executed it.

### Open items

- none blocking;
- deeper Beautiful Soup/Soup Sieve internals deliberately deferred.

### Artifact seed

SEED:
- preserve the distinction between “the project/repository has a dependency path” and “the library's normal runtime directly depends on it”;
- S001 makes this distinction concrete through `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`.

## 9. Active chunk record — Plan 01 / Chunk 2

**Status:** `[~] IN PROGRESS`  
**Opened:** 2026-08-17

### Real question

> What are `uv` and `uv.lock`, what information does the exact S001 lockfile preserve, and why does Soup Sieve appearing there still not prove that one particular environment selected or installed it?

### Material covered so far

- `uv` as a Python project/package/dependency-environment tool at operational depth;
- dependency requirements → resolution → lock → sync/install distinction;
- purpose of a lockfile;
- `uv.lock` as a universal/cross-platform resolution rather than one CI job's installed-package list;
- exact S001 `uv.lock` records for:
  - Pydantic's `docs` and `docs-upload` dependency groups;
  - `mkdocs-llmstxt → beautifulsoup4`;
  - `beautifulsoup4 → soupsieve`;
  - concrete `soupsieve 2.8.4` package record.

### Ali-owned evidence

Ali explained the central proof boundary in his own words: because the universal lock contains packages/relationships for different project dependency environments, seeing Soup Sieve in the lock is not enough; we must establish that the particular environment relevant to the CI path selects/reaches it.

- [~] explain why lockfiles exist — explanation received from assistant; independent restatement not yet checked directly.
- [~] identify package record / dependency edge — introduced from exact S001 evidence; independent restatement not yet checked directly.
- [x] explain why Soup Sieve's presence in universal `uv.lock` does not identify one selected CI dependency environment — core relation demonstrated, with wording correction below.

### Questions raised while studying

1. **Poetry versus uv versus pip**
   - Is Poetry the same kind of tool as uv?
   - Why do project/dependency-management tools exist instead of pip doing all project workflow responsibilities?
   - What other tools exist and what is the useful difference at our current depth?

2. **How CI identifies the dependency environment**
   - If `uv.lock` contains multiple possible dependency groups/environments, does a workflow/job/run specify which environment it uses?
   - How should we distinguish machine/runner environment, GitHub Actions deployment `environment`, and Python dependency/project environment?

These questions are on-route because they directly affect the lock-presence versus environment-selection proposition.

### Important corrections / terminology precision

- Ali's sentence “when we see the package exists in the CI” should be corrected to **“when we see the package exists in `uv.lock`.”** The lockfile is static project source; CI is a separate evidence surface.
- A GitHub Actions workflow/job can establish Python dependency-environment selection through concrete commands such as `uv sync --group docs` or `pip install -e ".[dev]"`; there is not necessarily one generic YAML field named “Python environment.”
- GitHub Actions also has a feature literally named `jobs.<job_id>.environment`, but that means a deployment/protection environment such as staging/production and must not be conflated with the Python dependency environment in this B2 route.
- Runner/OS selection (`runs-on`), Python interpreter setup, project dependency selection, and runtime execution are separate facts.

### Contract/process improvement discovered

Ali explicitly established a durable study behavior:

```text
question/issue arises
→ first correct any material misconception/imprecise premise
→ answer at current-route depth
→ avoid unrelated depth unless explicitly requested
→ return to active chunk
→ if the exchange reveals a reusable rule, update the contract
→ otherwise preserve important session-specific findings here
```

This was added to the controlling learning contract in Section 12.1 on 2026-08-17.

### Do-not-forget boundaries

- exact lock membership somewhere != selected-environment membership;
- lockfile structure is static source evidence, not proof of command execution or successful installation;
- CI workflow definition may expose a dependency selection statically, but static declaration != runtime execution;
- do not confuse GitHub deployment `environment` with Python dependency environment;
- do not jump ahead to BFS/reachability implementation yet.

### Open items

- [~] Finish the compact Poetry/uv/pip comparison at only the depth needed to place uv correctly.
- [~] Finish the CI environment-selection explanation and reconnect it to S001.
- [ ] Then perform one final Chunk-2 check before deciding GREEN versus remaining `[~]`.

### Artifact seeds

SEED:
- terminology collision around “environment”: runner/machine environment, Python dependency/project environment, virtual environment, and GitHub Actions deployment environment are not interchangeable.

SEED:
- pip versus project/workflow managers: distinguish package installation/resolution responsibilities from broader environment/project/lock/workflow responsibilities, noting that modern pip now also has an experimental `pip lock` rather than teaching the outdated claim that pip has no locking capability at all.

### Next exact continuation

Answer the two on-route questions compactly, correct the lock-versus-CI wording, show how a CI job can statically select a dependency group through its command, then return to the Chunk-2 gate without opening full GitHub Actions (Chunk 3) or selected-environment reachability (Plan 02).

## 10. Cross-session discoveries / corrections

- Chunk 1 precision: say **Pydantic documentation/tooling uses Beautiful Soup**, not broadly “Pydantic uses Beautiful Soup,” when discussing dependency ownership.
- Chunk 2 precision: package existence is observed in the lock/project evidence, not “inside CI”; CI separately contains declarations/runtime evidence that may select and consume some part of that dependency universe.
- Terminology collision: GitHub Actions deployment `environment` is a different concept from the Python dependency/project environment in B2.
- Current-tooling correction: modern pip has an experimental `pip lock` producing `pylock.toml`; therefore the useful distinction is scope/workflow and lock semantics, not the outdated blanket statement “pip cannot lock dependencies.”

## 11. Yellow `[~]` backlog

- Chunk 2: independently restate lockfile purpose/package-record/dependency-edge if needed at the final gate; do not drill them separately unless the next check exposes confusion.

## 12. Blocking `[!]` backlog

None.

## 13. Future artifact seeds

- Project/repository dependency path versus normal library runtime dependency, grounded in S001.
- “Environment” terminology map for this B2 route.
- Modern pip versus broader Python project/dependency managers, grounded only to the depth needed for interpreting target repositories.
