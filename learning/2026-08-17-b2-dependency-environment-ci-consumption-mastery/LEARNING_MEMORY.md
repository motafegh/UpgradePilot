# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 01 / Chunk 4 opened

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
**Current chunk:** Chunk 4 — exact dependency transition + dependency-owned source context

- [x] Chunk 1 — S001 orientation + Soup Sieve first contact — GREEN
- [x] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence — GREEN
- [x] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI — GREEN
- [~] Chunk 4 — exact dependency transition + dependency-owned source context — OPENED
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
- exact S001 documentation-tooling path `docs → mkdocs-llmstxt → beautifulsoup4 → soupsieve`, plus `docs-upload → beautifulsoup4 → soupsieve`.

### Ali-owned evidence

Ali explained Soup Sieve's practical role, its Beautiful Soup relationship, and why the Pydantic repository reaches Soup Sieve transitively through documentation/tooling rather than as a normal direct Pydantic runtime dependency.

### Important correction / precision

Say **Pydantic's documentation/tooling path uses Beautiful Soup**, not broadly “Pydantic uses Beautiful Soup,” when discussing dependency ownership.

### Do-not-forget boundaries

- repository dependency != core runtime dependency;
- transitive documentation dependency can still be relevant to a dependency-update investigation;
- this relationship alone does not establish environment selection, installation, or execution.

## 9. Completed chunk record — Plan 01 / Chunk 2

**Status:** `[x] GREEN`  
**Opened:** 2026-08-17  
**Completed sufficiently for route:** 2026-08-17

### Real question

> What are `uv` and `uv.lock`, what information does the exact S001 lockfile preserve, and why does Soup Sieve appearing there still not prove that one particular environment selected or installed it?

### Material covered

- `uv`, dependency requirements → resolution → lock → sync/install;
- purpose of lockfiles;
- `uv.lock` as a universal/cross-platform resolution rather than one CI job's installed-package list;
- exact S001 records for `docs` / `docs-upload`, `mkdocs-llmstxt → beautifulsoup4`, `beautifulsoup4 → soupsieve`, and `soupsieve 2.8.4`;
- compact Poetry/uv/pip placement;
- runner/OS, Python setup, dependency selection, GitHub deployment `environment`, and runtime execution as separate facts.

### Ali-owned evidence

Ali explained the central boundary: Soup Sieve appearing in the universal lock does not establish that the particular dependency environment relevant to a CI path selected/reaches it.

### Residual `[~]`

Independent restatement of lockfile purpose/package-record/dependency-edge was not separately drilled; reinforce naturally when later membership code parses/traverses them.

## 10. Completed chunk record — Plan 01 / Chunk 3

**Status:** `[x] GREEN`  
**Opened:** 2026-08-17  
**Completed sufficiently for route:** 2026-08-17

### Real question

> What are CI and GitHub Actions at the practical depth needed here, what is the exact structure of Pydantic's historical `docs-build` job, and what can its static workflow definition tell us without confusing configuration with runtime execution?

### Material covered

- CI = Continuous Integration and its repository-checking purpose;
- GitHub Actions workflow → job → step;
- `run:` as a shell-command step;
- `uses:` as invocation of a packaged reusable GitHub Action, not the same thing as a shell command and not necessarily built into GitHub;
- `with:` as inputs supplied to an Action;
- exact S001 `docs-build` structure:

```text
docs-build
→ runs-on: ubuntu-latest
→ uses: actions/checkout@<pinned SHA>
→ uses: astral-sh/setup-uv@<pinned SHA>
   with Python 3.12 / cache configuration
→ run: uv sync --all-packages --group docs
→ run: uv run python -c 'import docs.plugins.main'
→ prepare docs-related module shortcuts
→ run: uv run mkdocs build
```

- `actions/checkout` puts the repository source onto the runner;
- `astral-sh/setup-uv` prepares uv/Python context for later commands;
- docs CI as the responsibility of Pydantic's custom `docs-build` job, not a special reusable Action;
- static workflow definition versus actual runtime workflow/job/step evidence.

### Ali-owned evidence

Ali explained that the YAML statically defines a docs-group sync and MkDocs build but does not itself report that they ran successfully. This demonstrated the central static-definition versus runtime-evidence boundary.

- [x] static definition versus runtime evidence;
- [x] relevant `docs-build` purpose and dependency-selection command;
- [x] workflow/job/step structure at the depth needed to proceed;
- [x] `uses:` / reusable Action model repaired after Ali correctly challenged the omission.

### Important corrections / discoveries

- Prefer **“configured to synchronize the docs group and invoke an MkDocs build”** over “exercising” when talking about static YAML; `exercise` has stronger later semantics in UpgradePilot.
- A successful overall job/run is stronger runtime evidence, but it must not be collapsed directly into “Soup Sieve was installed/exercised” without the separate selected-environment membership relation and the exact runtime proposition being inspected.
- The contract's existing first-contact rule already covered material reusable Actions; the issue was failure to apply it, not absence of a rule. Do not create duplicate governance for an application mistake.

### Do-not-forget boundaries

```text
workflow definition
!= runtime execution
!= selected-environment membership
!= exact package installation witness
!= direct package exercise
```

### Artifact seed

SEED:
- GitHub Actions step taxonomy for this route: `run:` direct shell command versus `uses:` packaged Action plus `with:` inputs; show exact S001 `checkout` and `setup-uv` examples.

## 11. Active chunk record — Plan 01 / Chunk 4

**Status:** `[~] IN PROGRESS`  
**Opened:** 2026-08-17

### Real question

> Starting from the real S001 PR evidence, how does UpgradePilot establish one trusted canonical dependency transition and preserve the exact source context needed by later environment reasoning—without prematurely claiming that any environment selected or contains the dependency?

### Pinned source anchor

```text
f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099
```

### Primary source path

```text
ChangedFile / exact base+head uv.lock evidence
→ extract_uv_lock_changes(...)
→ ExtractedDependencyVersionChange
→ compare_extracted_dependency_changes(...)
→ DependencyVersionChange
→ analyze_dependency_change(...)
→ DependencyChangeAnalysis
   ├── dependency
   └── source_contexts
        └── UvLockDependencyContext for S001
```

### Central files / types / functions

- `src/upgradepilot/dependency/uv_lock.py`
  - `extract_uv_lock_changes(...)`;
- `src/upgradepilot/dependency/change.py`
  - `DependencyChangeSourceEvidence`;
  - `ExtractedDependencyVersionChange`;
  - `DependencyVersionChange`;
  - `compare_extracted_dependency_changes(...)`;
- `src/upgradepilot/dependency/analysis.py`
  - `DependencyChangeAnalysis`;
  - `analyze_dependency_change(...)`;
  - `_source_contexts(...)`;
- `src/upgradepilot/dependency/environment.py`
  - `UvLockDependencyContext`.

### S001 representative values

```text
repository: pydantic/pydantic
changed source: uv.lock
base: 652a61ce4f9d7d76eaada31535807a485ece0e21
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
package: soupsieve
old: 2.6
proposed: 2.8.4
file format: uv_lock
extraction method: exact_base_head_files
```

### Do-not-forget boundaries

- package/version transition != environment membership;
- source provenance is part of trusted evidence, not decorative metadata;
- `UvLockDependencyContext` means the trusted transition came from exact `uv.lock` evidence at an exact repository/revision/package identity;
- it deliberately does **not** invent `docs`, `docs-upload`, or any selected group/extra;
- those environment-selection/membership propositions require later independent evidence.

### Ali-owned evidence to obtain

- [ ] explain why source evidence travels with the version transition;
- [ ] trace S001 through extraction → PR-wide comparison → `DependencyChangeAnalysis`;
- [ ] state what `UvLockDependencyContext` adds and what it deliberately does not claim;
- [ ] identify the main input/output/proof boundary of `analyze_dependency_change(...)`.

### Next exact continuation

Start with the real S001 `uv.lock` base/head transition and the first source responsibility: `extract_uv_lock_changes(...)` turns exact source files into one file-level extracted change plus provenance. Then move to PR-wide comparison and only afterward to `_source_contexts(...)`.

## 12. Cross-session discoveries / corrections

- Chunk 1: project/repository dependency path must not be blurred into normal library-runtime ownership.
- Chunk 2: package existence is observed in lock/project evidence, not “inside CI”; CI is a separate evidence surface.
- “Environment” is overloaded: runner/machine, Python project/dependency environment, virtual environment, and GitHub deployment environment are not interchangeable.
- Modern pip has locking capability; use scope/workflow/tool-specific semantics rather than the outdated statement “pip cannot lock.”
- Chunk 3: `uses:` is a packaged reusable Action invocation; `run:` is direct shell command execution. Material Actions deserve first-contact treatment when they affect workflow meaning.
- Existing governance should be applied correctly before adding duplicate rules for the same principle.

## 13. Yellow `[~]` backlog

- Chunk 2: lockfile purpose/package-record/dependency-edge independent restatement can be reinforced when later code makes those structures causally relevant.

## 14. Blocking `[!]` backlog

None.

## 15. Future artifact seeds

- Project/repository dependency path versus normal library runtime dependency, grounded in S001.
- “Environment” terminology map for this B2 route.
- Modern pip versus broader Python project/dependency managers at bounded operational depth.
- GitHub Actions `run:` versus `uses:` / `with:` grounded in the exact S001 docs-build job.
