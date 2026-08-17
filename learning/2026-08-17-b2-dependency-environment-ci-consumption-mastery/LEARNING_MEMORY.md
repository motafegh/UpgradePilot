# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 01 / Chunk 3 opened

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
**Current chunk:** Chunk 3 — CI → GitHub Actions → Pydantic documentation CI

- [x] Chunk 1 — S001 orientation + Soup Sieve first contact — GREEN
- [x] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence — GREEN
- [~] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI — OPENED
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

## 9. Completed chunk record — Plan 01 / Chunk 2

**Status:** `[x] GREEN`  
**Opened:** 2026-08-17  
**Completed sufficiently for route:** 2026-08-17

### Real question

> What are `uv` and `uv.lock`, what information does the exact S001 lockfile preserve, and why does Soup Sieve appearing there still not prove that one particular environment selected or installed it?

### Material covered

- `uv` as a Python project/package/dependency-environment tool at operational depth;
- dependency requirements → resolution → lock → sync/install distinction;
- purpose of a lockfile;
- `uv.lock` as a universal/cross-platform resolution rather than one CI job's installed-package list;
- exact S001 `uv.lock` records for Pydantic `docs` / `docs-upload`, `mkdocs-llmstxt → beautifulsoup4`, `beautifulsoup4 → soupsieve`, and concrete `soupsieve 2.8.4`;
- compact Poetry/uv/pip placement without expanding into a package-manager survey;
- how a CI job can expose Python dependency selection through commands such as `uv sync --group docs`;
- distinction among runner/OS selection, Python setup, dependency selection, GitHub deployment `environment`, and runtime execution.

### Ali-owned evidence

Ali explained the central proof boundary in his own words: because the universal lock contains packages/relationships for different project dependency environments, seeing Soup Sieve in the lock is not enough; we must establish that the particular environment relevant to the CI path selects/reaches it.

- [x] central lock-presence versus selected-environment boundary demonstrated;
- [x] understood that the relevant flow must be tied to the environment/group being investigated;
- [~] independent restatement of lockfile purpose/package-record/dependency-edge was not separately drilled; this is non-blocking and may be reinforced later when real code consumes those structures.

### Questions / useful discoveries

- Poetry and uv overlap substantially as project/dependency-management tools but are not semantically interchangeable.
- Modern pip has more capabilities than the outdated “installer only” caricature; the useful distinction here is broader project/workflow scope and tool-specific lock semantics.
- CI does not necessarily contain one generic “Python dependency environment” field. Selection may be expressed through actual setup/install/sync commands.
- GitHub Actions deployment `environment` is a separate concept from the Python dependency/project environment in this B2 route.

### Important correction / precision

Ali's wording “when we see the package exists in the CI” was corrected to:

> **Soup Sieve is observed in `uv.lock`; CI is a separate evidence surface that may statically declare which dependency group/environment it intends to consume.**

### Do-not-forget boundaries

- exact lock membership somewhere != selected-environment membership;
- lockfile structure is static source evidence, not proof of command execution or successful installation;
- static CI dependency selection != runtime execution;
- runner/OS, interpreter, dependency selection, deployment environment, and runtime evidence are separate facts.

### Residual `[~]`

- lockfile purpose/package-record/dependency-edge can be reinforced naturally when later membership code parses/traverses them; no need to delay forward progress now.

### Artifact seeds

SEED:
- terminology collision around “environment”: runner/machine environment, Python dependency/project environment, virtual environment, and GitHub Actions deployment environment are not interchangeable.

SEED:
- modern pip versus broader Python project/dependency managers, grounded only to the depth needed for interpreting target repositories.

## 10. Active chunk record — Plan 01 / Chunk 3

**Status:** `[~] IN PROGRESS`  
**Opened:** 2026-08-17

### Real question

> What are CI and GitHub Actions at the practical depth needed here, what is the exact structure of Pydantic's historical `docs-build` job, and what can its static workflow definition tell us without confusing configuration with runtime execution?

### Exact S001 workflow anchor

Frozen head:

```text
aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
.github/workflows/ci.yml
```

Relevant job:

```text
docs-build
→ runs-on: ubuntu-latest
→ setup uv / Python 3.12
→ uv sync --all-packages --group docs
→ uv run python -c 'import docs.plugins.main'
→ prepare documentation-related module shortcuts
→ uv run mkdocs build
```

### First-contact items to establish now

- CI = Continuous Integration;
- why repositories automatically check changes;
- GitHub Actions as the workflow platform in this target repository;
- workflow → job → step → `run` command;
- static workflow definition versus a runtime workflow run/job result;
- documentation CI / docs CI as a job whose responsibility is to install/build/check the documentation toolchain.

### Do-not-forget boundaries

- a YAML workflow definition says what is configured/intended, not by itself what actually ran or succeeded;
- `runs-on: ubuntu-latest` identifies runner selection, not the Python dependency group;
- `uv sync --all-packages --group docs` is the relevant static dependency-selection declaration here;
- `uv run mkdocs build` shows the job is intended to build documentation, but static syntax alone is not success evidence;
- docs CI relevance to Soup Sieve does not imply unrelated Pydantic runtime behavior is covered.

### Ali-owned evidence to obtain

- [ ] explain CI's practical role in a repository;
- [ ] identify workflow/job/step/run in the exact Pydantic example;
- [ ] explain what `docs-build` is trying to validate;
- [ ] distinguish static workflow definition from runtime evidence;
- [ ] explain why this docs job can be relevant to a documentation dependency such as Soup Sieve without becoming general Pydantic runtime proof.

### Next exact continuation

Teach CI → GitHub Actions → workflow/job/step/run using the exact historical `docs-build` job, then stop for one meaningful explanation/prediction before entering UpgradePilot source in Chunk 4.

## 11. Cross-session discoveries / corrections

- Chunk 1 precision: say **Pydantic documentation/tooling uses Beautiful Soup**, not broadly “Pydantic uses Beautiful Soup,” when discussing dependency ownership.
- Chunk 2 precision: package existence is observed in lock/project evidence, not “inside CI”; CI separately contains declarations/runtime evidence that may select and consume some part of that dependency universe.
- Terminology collision: GitHub Actions deployment `environment` is a different concept from the Python dependency/project environment in B2.
- Current-tooling correction: modern pip has an experimental locking capability; therefore the useful distinction is scope/workflow and lock semantics, not the outdated blanket statement “pip cannot lock dependencies.”

## 12. Yellow `[~]` backlog

- Chunk 2: independent restatement of lockfile purpose/package-record/dependency-edge was not separately checked; revisit only when later code makes those structures causally relevant.

## 13. Blocking `[!]` backlog

None.

## 14. Future artifact seeds

- Project/repository dependency path versus normal library runtime dependency, grounded in S001.
- “Environment” terminology map for this B2 route.
- Modern pip versus broader Python project/dependency managers, grounded only to the depth needed for interpreting target repositories.
