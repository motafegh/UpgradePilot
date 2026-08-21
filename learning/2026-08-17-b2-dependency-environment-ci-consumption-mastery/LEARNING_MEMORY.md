# B2 Dependency Environment + CI Consumption — Learning Memory

**Created:** 2026-08-17  
**Role:** local working memory for this learning package  
**Controlling contract:** `00_LEARNING_SESSION_CONTRACT_AND_ROUTE.md`  
**Plan set:** `PLAN_01_...` through `PLAN_04_...` in this folder  
**Live project-state authority:** `../../MEMORY.md`  
**Current learning status:** ACTIVE — Plan 02 / Chunk 1

## 1. Purpose and authority boundary

This file preserves the continuity of our interactive learning journey so important progress, discoveries, corrections, open questions, subtle proof boundaries, engineering-audit findings, and potentially reusable learning material are not lost across conversations.

It is intentionally a **working memory**, not a finished learning note.

It may record:

- where we currently are in the approved learning plans;
- what Ali has actually understood, predicted, challenged, diagnosed, or critiqued;
- important explanations or mental-model corrections that emerged during conversation;
- important real-case/source/test discoveries made while learning;
- `[~]` non-blocking gaps worth revisiting later;
- RED/blocking misunderstandings that must be repaired before proceeding;
- useful questions, comparisons, examples, source traces, or design-audit findings that may deserve a later learning artifact;
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
- challenged whether a design choice is necessary and reasoned about its tradeoff;
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
- Engineering critique should be preserved, but a speculative redesign should not derail the active route unless correctness or the next authorized build decision depends on it.

## 4. Artifact-seed rule

This file is also a capture surface for future reusable learning artifacts.

When a conversation produces something worth preserving later, add a short seed rather than writing the artifact immediately. A seed may include:

```text
SEED:
- subject / misconception / code trace / design question;
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

Learning implementation anchor for the original plan set: `f7fcd5e2dad98e3ab3ac59a1950cfb6d79cb0099`.

Current live project authority in `../../MEMORY.md` records:

```text
Clusters 0–5: COMPLETE / GREEN
Cluster 6: NOT STARTED
Cluster 7: NOT STARTED
Cluster 8: NOT STARTED
Tranche 2 static↔runtime correlation: NOT SELECTED
```

Latest documented Cluster-5 validation point remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

The immediate product action is still the user-selected bounded source-clarity/refactoring pass before Cluster 6. That product continuation is separate from the active learning route. Re-read `../../MEMORY.md` before any return-to-building handoff.

## 7. Plan progress

### Plan 01 — S001 Real Case → First UpgradePilot Evidence Models

**Status:** `[~] CONTENT ROUTE COMPLETE — formal ownership/test gates deferred`  
**Opened:** 2026-08-17  
**Content route completed:** 2026-08-21

- [x] Chunk 1 — S001 orientation + Soup Sieve first contact — GREEN
- [x] Chunk 2 — `uv` + `uv.lock` using exact S001 evidence — GREEN
- [x] Chunk 3 — CI → GitHub Actions → Pydantic documentation CI — GREEN
- [~] Chunk 4 — content covered; independent reconstruction/test gates deferred
- [~] Chunk 5 — content covered; independent prediction/test-ownership gate deferred

Durable Plan-01 study artifacts now live under `notes/`:

```text
01_PLAN01_END_TO_END_LEARNING_NOTE.md
02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md
03_PLAN01_EVIDENCE_AND_PROOF_BOUNDARIES.md
04_PLAN01_MASTERY_AND_REVIEW_MAP.md
```

### Plan 02 — S001 Membership → CI Consumption → Coverage

**Status:** `[~] ACTIVE`  
**Opened:** 2026-08-21  
**Current chunk:** Chunk 1 — exact `pyproject.toml` + `uv.lock` evidence needed for one membership question

- [~] Chunk 1 — ACTIVE
- [ ] Chunk 2 — S001 graph reachability + membership witness
- [ ] Chunk 3 — membership → exact static CI consumption
- [ ] Chunk 4 — whole-workflow evidence + bounded CI coverage

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

## 11. Historical active-chunk record — Plan 01 / Chunk 4

**Status:** `[~] CONTENT COVERED; FORMAL OWNERSHIP/TEST GATES DEFERRED`  
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
→ RepositoryTextFile exact-revision provider boundary
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

- `src/upgradepilot/github/repository.py`
  - `RepositoryTextFile`;
  - `GitHubRepositoryClient.get_pull_request_base_file(...)` / `get_pull_request_head_file(...)`;
  - `_get_exact_repository_text_file(...)`;
- `src/upgradepilot/dependency/uv_lock.py`
  - `extract_uv_lock_changes(...)`;
  - `_build_source_evidence(...)`;
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

### Material covered so far

- first source responsibility: exact base/head repository files → file-level extracted dependency transition;
- `DependencyChangeSourceEvidence` carries exact source provenance with the transition;
- `extract_uv_lock_changes(...)` admits only bounded evidence shapes and returns an explicit problem instead of guessing on unsupported/ambiguous structures;
- initial explanation was intentionally concept-first, but Ali correctly identified that it did **not yet satisfy the source-walk requirement** because material Python syntax/control flow had not been read.

### Ali-owned evidence / questions

Ali currently reasons that revision/path are useful because they make evidence expressive and accurate, but challenged whether all recorded provenance fields are genuinely necessary rather than merely “more data = stronger.” This is a productive engineering-audit question, not a misconception.

### Engineering audit — exact repository-file provenance

Provider source inspected: `src/upgradepilot/github/repository.py` at the pinned implementation anchor.

Current facts:

```text
repository + path + revision
→ identify which repository file at which immutable commit was requested

returned_path
→ GitHub response must point back to the exact requested repository-relative path

blob_sha
→ GitHub's Git-blob identity for the returned file content; retained as a content/provenance fingerprint

reported_byte_count
→ file size reported by GitHub

decoded_byte_count
→ actual byte length after base64 decoding

reported == decoded
→ transport/response consistency check

1,000,000-byte bound
→ bounded-analysis/resource-safety limit
```

Important nuance:

- `revision + path` are already sufficient to *locate* one immutable Git file in a repository; blob SHA is not needed merely to formulate that lookup.
- blob SHA adds a second exact-content identity/provenance handle, but the current provider validates that GitHub supplied a non-empty blob SHA; it does **not** recompute the Git blob hash from decoded content at this boundary. Therefore do not overstate it as independent cryptographic verification of bytes.
- reported/decoded byte counts detect malformed/truncated/inconsistent response representation and enforce the bounded text-file size contract. They are defensive acquisition metadata, not dependency semantics.
- `_build_source_evidence(...)` revalidates strong fields even though the runtime provider already validated them. This is partly explained by `RepositoryTextFile` intentionally admitting older manually constructed fixtures where strong provenance fields may be missing; downstream strict boundaries must therefore validate before trust.

Engineering judgment to carry forward:

```text
HIGH-VALUE / STRUCTURAL:
repository, path, immutable revision

HIGH-VALUE PROVENANCE / PARTLY REDUNDANT FOR LOOKUP:
blob SHA

DEFENSIVE TRANSPORT + RESOURCE-BOUND EVIDENCE:
reported/decoded byte counts

POSSIBLE FUTURE SIMPLIFICATION QUESTION:
Could a stronger validated repository-file type/factory eliminate repeated downstream validation and separate runtime-exact evidence from legacy/manual fixtures?
```

No product change is authorized or proposed from this learning note; this is an audit observation to revisit only if architecture/refactoring work makes it relevant.

### Contract improvement triggered by Chunk 4 questions

Updated controlling contract at commit:

```text
b6571a7ef70093ac9be6bc0eaf25f26b50e4ef61
```

New/clarified durable rules:

- source/tests are implementation truth, not automatic design truth;
- material fields/checks/abstractions should be justified by the failure mode they protect and audited for proportionality;
- distinguish current behavior, rationale, engineering judgment, and authorization boundary;
- source-code chunks must teach material Python syntax/control flow, not only concepts/function names;
- audit while learning without stalling the build for speculative redesign.

### Do-not-forget boundaries

- package/version transition != environment membership;
- source provenance is part of trusted evidence, but each provenance field should have a justified role rather than being valued merely because it increases metadata volume;
- `UvLockDependencyContext` means the trusted transition came from exact `uv.lock` evidence at an exact repository/revision/package identity;
- it deliberately does **not** invent `docs`, `docs-upload`, or any selected group/extra;
- those environment-selection/membership propositions require later independent evidence.

### Open `[~]` items

- [~] Formal independent source reconstruction remains deferred.
- [~] Representative focused test explanation remains deferred.

## 12. Cross-session discoveries / corrections

- Chunk 1: project/repository dependency path must not be blurred into normal library-runtime ownership.
- Chunk 2: package existence is observed in lock/project evidence, not “inside CI”; CI is a separate evidence surface.
- “Environment” is overloaded: runner/machine, Python project/dependency environment, virtual environment, and GitHub deployment environment are not interchangeable.
- Modern pip has locking capability; use scope/workflow/tool-specific semantics rather than the outdated statement “pip cannot lock.”
- Chunk 3: `uses:` is a packaged reusable Action invocation; `run:` is direct shell command execution. Material Actions deserve first-contact treatment when they affect workflow meaning.
- Existing governance should be applied correctly before adding duplicate rules for the same principle.
- Chunk 4: current source is authoritative for current implementation behavior, but learning includes engineering critique; existence in source is not sufficient rationale.
- Chunk 4: concept-first orientation is useful, but a source-code chunk is incomplete until the material syntax/control flow that implements the responsibility has been read.
- Chunk 5: GitHub/provider workflow structure and Dependency project-selection semantics have different owners; `RunStepDefinition` is the seam.
- Chunk 5: `observed`, `not_observed`, and `unresolved` must remain distinct; unresolved must not become a negative fact.

## 13. Yellow `[~]` backlog

- Chunk 2: lockfile purpose/package-record/dependency-edge independent restatement can be reinforced when Plan 02 parses/traverses them.
- Plan 01 / Chunk 4: formal independent source/test ownership check remains deferred.
- Plan 01 / Chunk 5: independent prediction/test-ownership check remains deferred.
- Possible future type-boundary simplification around validated exact repository files versus legacy/manual fixtures; preserve as an audit seed, not a current redesign task.
- Workflow parser audit: `yaml.compose(...)` occurs before UpgradePilot's post-compose graph-depth guard, so pathological nesting can raise composition-time `RecursionError`; treat as a bounded future robustness fix/test candidate, not a reason to rewrite the architecture.
- Workflow parser audit: alias occurrence/source-span precision, closed problem reason codes, and stronger canonical workflow-path admission are smaller non-blocking improvement candidates.

## 14. Blocking `[!]` backlog

None.

## 15. Future artifact seeds

- Project/repository dependency path versus normal library runtime dependency, grounded in S001.
- “Environment” terminology map for this B2 route.
- Modern pip versus broader Python project/dependency managers at bounded operational depth.
- GitHub Actions `run:` versus `uses:` / `with:` grounded in the exact S001 docs-build job.
- Exact repository-file provenance map: revision vs blob SHA vs reported/decoded byte counts, including which are semantic identity, content identity, transport checks, and defensive redundancy.
- Implementation truth versus design truth: how to audit a live codebase while learning without silently redesigning it.

## 16. Evidence-state vocabulary discovery — 2026-08-21

Chunk 4 exposed a recurring terminology problem: the word **“know”** was being used for materially different stages of an evidence pipeline. That wording can hide accidental claim-strength upgrades, especially when moving from provider input to validated evidence, semantic interpretation, cross-source reconciliation, environment context, runtime evidence, and final evaluation.

Use this learning vocabulary when the distinction matters:

```text
0. OBSERVED
Information has been seen/received from an external or upstream source, but the current responsibility has not yet established stronger trust or meaning.

1. ACQUIRED
The required artifact/evidence item has been successfully retrieved.

2. VALIDATED
The evidence has passed the identity, integrity, structural, schema, or other checks required by the current responsibility.

3. INTERPRETED
Validated evidence has been transformed into bounded domain meaning.

4. RECONCILED
Multiple admitted interpretations/evidence sources have been compared and combined into one consistent conclusion, or an explicit conflict/problem has been preserved.

5. CONTEXTUALIZED
The established meaning has been connected to a larger project/environment/workflow/dependency context.

6. EXERCISED
Runtime evidence establishes that the relevant mechanism/path actually executed or was consumed at the exact strength claimed. Static configuration alone does not reach this state.

7. EVALUATED
The accumulated evidence has been assessed against a higher-level investigation/product question at the strength actually supported.
```

Important qualification: these are **learning/evidence-language states**, not a requirement that production code introduce classes or enums with these exact names. Real modules may skip a label, combine adjacent work, or have source-specific state objects. The vocabulary exists to make explanations and proof boundaries precise.

Do not silently promote evidence between states. Examples:

```text
observed workflow YAML
!= exercised workflow

acquired file
!= validated file

interpreted file-level dependency transition
!= reconciled PR-wide dependency transition

contextualized environment membership
!= runtime package exercise
```

When describing a material result, prefer precise verbs such as **observed, acquired, validated, interpreted, reconciled, contextualized, exercised,** or **evaluated** over the generic phrase “UpgradePilot knows ...”. Always pair the positive claim with the nearby non-proof boundary when omission could imply a stronger state.

Current Chunk-4 application:

```text
exact base/head uv.lock files acquired + provenance/schema checks
→ validated source evidence
→ uv_lock.py interprets that evidence into one file-level ExtractedDependencyVersionChange
→ change.py later reconciles admitted file-level results into a PR-wide DependencyVersionChange
→ later environment/CI responsibilities contextualize or exercise stronger propositions independently
```

This discovery is non-blocking and should sharpen the remaining learning route rather than create a new implementation project.

## 17. Plan-01 Chunk-4 source-walk completion record — 2026-08-21

A guided executable-source walk of the current `src/upgradepilot/dependency/uv_lock.py` was completed at the practical depth needed for this route:

```text
extract_uv_lock_changes(...)
→ repository-relative path/basename admission
→ modified-status admission
→ exact base/head availability
→ post-guard isinstance/assert narrowing
→ _build_source_evidence(...)
→ independent base/head TOML parsing
→ _validate_package_record(...)
→ normalized grouping
→ _compare_uv_lock_packages(...)
→ _compare_single_record(...)
→ exactly-one-transition requirement
→ ExtractedDependencyVersionChange
```

Material Python mechanisms covered included negative indexing (`parts[-1]`), union evidence states, guard clauses/early returns, `isinstance`, assertions as internal invariants after guards, `_MISSING` + identity checks, `defaultdict`, `enumerate`, `.append`, set union, tuple return/unpacking, `Counter`, and bounded canonicalization at operational depth.

Engineering audit of helper decomposition found no justified source modification. The selected helpers generally earned their navigation cost through transformation, invariant isolation, or semantic naming. Formal closed-source reconstruction/test ownership remains deferred.

## 18. Plan-01 Chunk-4 downstream reconciliation record — 2026-08-21

The guided current-source walk covered `src/upgradepilot/dependency/change.py`, then `dependency/analysis.py`, `_source_contexts(...)`, and `dependency/environment.py` at the practical depth needed for the route.

Core progression:

```text
DependencyChangeSourceEvidence
→ provenance for one admitted dependency source

ExtractedDependencyVersionChange
→ one source-specific INTERPRETED file-level transition

compare_extracted_dependency_changes(...)
→ collect unique provenance
→ stop on any admitted DependencyChangeProblem
→ require at least one extracted transition
→ require exactly one normalized package identity
→ require exactly one exact (old_version, proposed_version) transition
→ promote only then

DependencyVersionChange
→ RECONCILED PR-wide canonical dependency transition

analysis.py / _source_contexts(...)
→ orchestration + provenance translation
→ UvLockDependencyContext
```

For S001:

```text
soupsieve 2.6 → 2.8.4
→ reconciled canonical transition
→ dependency-source contextualized as exact uv.lock evidence
```

Important proof boundary:

```text
UvLockDependencyContext
!= selected docs membership
!= CI consumption
!= runtime execution/exercise
```

Formal independent reconstruction and representative-test explanation remain `[~]` deferred rather than falsely promoted to GREEN.

## 19. Plan-01 completion + Plan-02 formal opening — 2026-08-21

### Plan-01 content completion

The guided content route continued through Chunk 5 and reached the intended Plan-01 stop line:

```text
exact S001 dependency transition
→ exact source context
→ bounded GitHub Actions workflow IR
→ RunStepDefinition("uv sync --all-packages --group docs")
→ dependency-owned static selector interpretation
→ DependencyGroupSelector("docs", mode="include")
→ ProjectEnvironmentSelectionObservation(state="observed")
```

The workflow/provider boundary was also audited. Current judgment:

```text
architecture / ownership: strong
PyYAML representation-node strategy: strong
shared provider IR: justified by CI + Target consumers
static/runtime separation: strong
local JobProblem / StepProblem preservation: strong

non-blocking robustness gap:
yaml.compose(...) can encounter RecursionError before the post-compose graph-depth guard
```

That gap is preserved for a proportional future fix/test; it does not block the learning route and does not justify rewriting the parser.

### Finished Plan-01 study artifacts

```text
notes/01_PLAN01_END_TO_END_LEARNING_NOTE.md
notes/02_PLAN01_SOURCE_CODE_AND_DATA_FLOW_MAP.md
notes/03_PLAN01_EVIDENCE_AND_PROOF_BOUNDARIES.md
notes/04_PLAN01_MASTERY_AND_REVIEW_MAP.md
```

The separate `PLAN_01_MASTERY_AND_DEPTH_MAP.md` remains the authoritative depth companion for the execution plan; the note `04_PLAN01_MASTERY_AND_REVIEW_MAP.md` is a reusable study/review artifact, not a replacement for the plan-depth authority.

### Honest mastery state

```text
[x] Plan-01 conceptual/content route covered through Chunk 5
[x] guided current-source walkthroughs completed for the selected mechanisms
[x] major proof/design boundaries discussed and audited
[x] reusable Plan-01 study artifacts created

[~] independent source reconstruction still deferred
[~] representative-test ownership demonstrations still deferred
```

No RED misconception blocks progression.

### Plan 02 formally opened

Plan 02 is now ACTIVE at Chunk 1.

Use these together:

```text
PLAN_02_S001_MEMBERSHIP_TO_CI_CONSUMPTION_AND_COVERAGE.md
+
PLAN_02_MASTERY_AND_DEPTH_MAP.md
```

Current exact learning question:

> Given the previously established `DependencyGroupSelector("docs")` and `UvLockDependencyContext` for Soup Sieve, what exact `pyproject.toml` + `uv.lock` evidence and provenance must be validated before UpgradePilot may safely ask whether the selected docs environment reaches the changed package?

Current source ownership target:

```text
src/upgradepilot/dependency/uv_membership.py

OWN / MASTER now:
- evaluate_uv_selected_environment_membership(...)
- _validate_exact_source_identity(...)
- only the project/lock parsing stages that determine admitted structure, project identity, selected roots, or explicit problem state

REUSE / NAVIGATE:
- environment_selection.py selector types from Plan 01
- github/repository.py exact-source evidence contract from Plan 01

DEFER:
- every parser helper
- generic graph theory / full BFS until Chunk 2
- uv resolver internals / marker breadth not required by S001
```

Next exact continuation:

```text
real S001 inputs
DependencyGroupSelector("docs")
+ UvLockDependencyContext("soupsieve")
+ exact head pyproject.toml
+ exact head uv.lock
        ↓
evaluate_uv_selected_environment_membership(...)
        ↓
_validate_exact_source_identity(...)
        ↓
why both exact project metadata and exact lock evidence are required before graph semantics
```
