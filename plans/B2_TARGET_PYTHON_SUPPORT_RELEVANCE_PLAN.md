# B2 Target Python Support Relevance Plan

**Owner:** Ali Rajabi  
**Parent gate:** [`B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md`](B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md)  
**Parent decision plan:** [`B2_TRANSPARENT_DECISION_METHOD_PLAN.md`](B2_TRANSPARENT_DECISION_METHOD_PLAN.md)  
**Stable product authority:** [`../PROJECT_CHARTER.md`](../PROJECT_CHARTER.md)

## Purpose

Define the smallest product slice that connects one explicit upstream Python-version support-drop claim to one exact-revision target-repository declaration.

```text
upstream change evidence for old_version < release <= proposed_version
→ one grounded support_dropped claim for Python X.Y
+ target exact-head [project].requires-python
→ declared-range overlap, declared non-overlap, or honest unresolved result
```

This is a relevance result, not a compatibility, safety, or merge decision. This plan remains position-neutral; `../MEMORY.md` alone selects it and records continuation.

## Owning question

For one supported exact pinned Python dependency update:

> When authoritative upstream change evidence within the complete crossed-version interval states that support for Python `X.Y` was dropped, does the target repository's exact-head `[project].requires-python` declaration include any stable Python `X.Y` release?

## Why the source interval matters

A dependency update may cross several releases. Reading only the proposed version's final release body can omit a material change introduced earlier in the crossed interval.

The first proof case demonstrates this:

```text
Soup Sieve 2.6 → 2.8.4

2.8 changelog:
Drop support for Python 3.8.

2.8.4 release body:
contains only 2.8.4 fixes
```

Therefore the admitted upstream responsibility is not merely "summarize the proposed release body." It is:

```text
identify authoritative upstream changes introduced after the old version
and no later than the proposed version
```

The interval is:

```text
old_version exclusive
proposed_version inclusive
```

Version ordering must use an accepted standards-based version implementation. Unsupported or ambiguous release ordering must remain unresolved.

## First bounded scope

### Upstream claim form

Only one grounded claim form is admitted initially:

```text
category: support_boundary_change
change_state: support_dropped
python_line: normalized X.Y
source_quote: exact contiguous upstream span
source_identity: exact immutable release, tag, revision, path, and blob where applicable
upgrade_interval: exact old and proposed dependency versions
```

`support_added`, generic behavior changes, compatibility assurances, deprecations, removals, and non-Python platform changes remain outside this first relevance comparison.

### Admitted upstream source order

Use only bounded authoritative sources whose identity and relation to the crossed interval can be preserved:

1. exact GitHub Release bodies for relevant crossed releases when their release identities and ordering are established;
2. an exact tagged upstream changelog at the proposed tag, with the relevant version section and blob identity preserved;
3. exact package metadata as corroboration for resulting Python requirements where available.

Dependabot release-note text may locate or corroborate a claim, but it is copied evidence and must not silently replace the authoritative upstream source.

Do not permit arbitrary documentation search, model-selected authority, or unbounded browsing.

### Target source

Only this source is admitted initially:

```text
pyproject.toml at PullRequestIdentity.head_sha
→ [project].requires-python
```

This source is selected because:

- `GitHubRepositoryClient.get_exact_head_text_file` provides bounded UTF-8 acquisition at the immutable PR head;
- Python 3.12 provides `tomllib`, so TOML structure can be parsed without a new TOML dependency;
- `[project].requires-python` is an explicit project declaration rather than an inference from file names or prose;
- missing, malformed, or unsupported evidence can remain explicit.

## Authority and claim limits

`[project].requires-python` establishes the project's declared Python installation-version specifier at one exact revision. It does **not** establish:

- which Python versions CI actually executed;
- production runtime versions;
- every Python version the maintainers actively test;
- dependency usage on the affected path;
- update safety or a maintainer action.

Therefore the comparator may say only whether the dropped Python line overlaps the accepted meaning of that declaration.

Workflow matrices, tox environments, classifiers, documentation, deployment files, and tool-specific Python settings are not silently combined with this evidence. They require a later activated need and their own authority rules.

## Responsibility separation

```text
Package and upstream identity
→ establish exact dependency versions, upstream repository, releases/tags, and source interval

Upstream source acquisition
→ acquire bounded authoritative change evidence for old_version < release <= proposed_version

Candidate semantic extraction
→ produce an untrusted structured candidate from admitted upstream text

Deterministic claim validation
→ validate source identity, exact quotation, allowed category/state, normalized Python line,
   interval relevance, and prohibited fields

Trusted support-drop input
→ emit one GroundedPythonSupportDropClaim or explicit unresolved state

Conditional target activation
→ only a valid grounded Python support-drop claim activates exact-head pyproject.toml acquisition

Target interpretation
→ parse only [project].requires-python

Range evaluation
→ use the accepted standards-based specifier method to determine Python-line overlap

Relevance result
→ declared overlap, declared non-overlap, or unresolved

Decision
→ remains outside this plan
```

## Two-layer upstream contract

The model-facing result and comparator input must remain distinct.

### Candidate result

`CandidateUpstreamClaimResult` is untrusted model output. A structured-output adapter such as Instructor may help generate and parse it, but schema-valid output is not trusted meaning.

It may contain:

- result state;
- candidate claims;
- category and change state;
- candidate normalized Python line;
- exact source quote or span;
- limitations and unresolved reasons.

### Trusted comparator input

`GroundedPythonSupportDropClaim` is deterministic domain evidence admitted only after validation. It must preserve:

```text
category = support_boundary_change
change_state = support_dropped
python_line = normalized major/minor
exact source identity
exact contiguous source quote
old dependency version
proposed dependency version
```

Controlled tests must construct this trusted type directly without an LLM, Instructor, LM Studio, or network call.

Instructor, Pydantic, an OpenAI-compatible client, and a particular model remain adapter or deployment choices. They do not own the product contract and are not admitted into the active runtime merely because this contract exists.

## Target evidence states

The target parser preserves:

- `available` — a non-empty textual `[project].requires-python` value was established;
- `file_unavailable` — exact-head `pyproject.toml` was absent or inaccessible;
- `malformed_toml` — the file existed but was not valid TOML;
- `project_table_absent` — TOML parsed but had no `[project]` table;
- `requires_python_absent` — `[project]` existed but did not declare `requires-python`;
- `invalid_requires_python` — the field existed but was not non-empty text.

No unavailable or malformed state may be converted into an inferred range.

## Accepted range method

Use the maintained `packaging` implementation for PEP 440 version and specifier parsing rather than writing a general parser from scratch.

Expected primitives include:

```text
packaging.version.Version
packaging.specifiers.SpecifierSet
```

This is a durable runtime dependency decision and must be recorded through the appropriate dependency or architecture owner before product implementation. Exact package bounds must be selected and tested rather than copied casually.

`packaging` owns standards-correct parsing and candidate membership. UpgradePilot still owns the product meaning of a Python line.

### Python-line overlap meaning

For a grounded dropped line `X.Y`:

```text
declared_python_overlap
= at least one stable Python X.Y.Z release is admitted by the target declaration
```

Examples:

```text
requires-python = ">=3.9"
dropped line = 3.9
→ overlap

requires-python = ">=3.9.7"
dropped line = 3.9
→ overlap

requires-python = ">=3.10"
dropped line = 3.9
→ outside declared range

requires-python = "!=3.9.*"
dropped line = 3.9
→ outside declared range

requires-python = ">=3.8,<3.10"
dropped line = 3.9
→ overlap
```

Do not implement this existential line rule as arbitrary finite patch enumeration without a proof that the selected method is complete for the admitted specifier forms. Before coding, freeze the exact algorithm and its unsupported cases.

Pre-release-only, epoch, local-version, arbitrary-equality, or other cases that cannot be mapped responsibly to a stable Python major/minor support line must return `comparison_unsupported` rather than guess.

## Relevance states

The comparator must distinguish:

- `declared_python_overlap` — the target declaration includes at least one stable release in the dropped Python line;
- `outside_declared_python_range` — the target declaration excludes the entire dropped line under the accepted method;
- `target_declaration_unresolved` — target evidence is unavailable, malformed, missing, or unsupported;
- `upstream_claim_unresolved` — no valid grounded support-drop claim is available;
- `comparison_unsupported` — both inputs exist but the accepted range method cannot evaluate them responsibly.

These states must not contain `safe`, `compatible`, `merge`, or equivalent claims.

## Conditional activation and CLI order

The current CLI implementation reads `pyproject.toml` immediately after identifying a supported dependency update. That ordering was acceptable for isolating and validating target acquisition, but it is temporary.

Current temporary order:

```text
supported dependency update
→ target pyproject.toml acquisition
→ CI evidence
→ package evidence
→ upstream release evidence
```

Required final semantic activation order:

```text
supported dependency update
→ package and upstream identity
→ authoritative upstream interval evidence
→ candidate extraction and deterministic validation
→ valid Python support-drop claim?
    ├── no  → target Python investigation not activated
    └── yes → acquire exact-head pyproject.toml
              → parse requires-python
              → compare
```

The target acquisition code may remain reusable, but orchestration must eventually move behind the grounded-claim activation condition. The CLI must expose non-activation explicitly rather than implying that every dependency update requires target Python investigation.

Do not refactor the order before the upstream contract, source interval, and comparator inputs are frozen enough to preserve existing behavior and tests.

## First proof case

Reuse historical simulation case S001 as the first current-product proof case; do not create a new simulation merely to increase case count.

```text
target: pydantic/pydantic
PR: 13432
head: aa2dc024d33f61cdef50bf1973ab5adf0a974f5a
dependency: soupsieve
update: 2.6 → 2.8.4

target declaration:
requires-python = ">=3.10"

upstream tagged changelog:
Drop support for Python 3.8.

expected relevance:
outside_declared_python_range
```

S001 is an historical oracle, not current automated proof. The new implementation must reacquire exact identities and produce the result through the current runtime without rewriting the completed simulation records.

The result proves only that Python 3.8 is outside Pydantic's declared installation range at the exact PR head. It does not prove universal compatibility, safety, or that the pull request should be merged.

## Revised work sequence

### Step 1 — Target declaration acquisition

Completed responsibility:

```text
exact-head pyproject.toml
→ tomllib parsing of [project].requires-python
→ typed target evidence
→ CLI presentation
```

This plan does not use its stable sections to record completion revisions; `../MEMORY.md` owns live progress.

### Step 2 — Freeze upstream interval and source authority

Define and test:

- old-version-exclusive/proposed-version-inclusive interval identity;
- admitted release-body and tagged-changelog sources;
- source ordering, provenance, unavailable states, and conflict handling;
- explicit rejection of model-selected or arbitrary source authority.

### Step 3 — Freeze the two-layer support-drop contract

Define `CandidateUpstreamClaimResult` and `GroundedPythonSupportDropClaim` independently of any selected model adapter.

Controlled tests must directly construct trusted claims and reject malformed, ungrounded, wrong-direction, wrong-category, and out-of-interval candidates.

### Step 4 — Freeze the packaging-based line-overlap algorithm

Record:

- exact `packaging` dependency bounds and admission rationale;
- stable Python-line semantics;
- handling of compound specifiers, exclusions, wildcards, compatible-release operators, patch boundaries, and pre-releases;
- unsupported and abstention cases;
- proof that the implementation does not rely on arbitrary finite patch enumeration.

### Step 5 — Implement deterministic relevance with manual trusted inputs

Before any LLM integration:

```text
GroundedPythonSupportDropClaim
+ TargetPythonDeclaration
→ packaging-based relevance result
```

Use controlled S001 fixtures to prove the expected non-overlap result.

### Step 6 — Implement authoritative upstream interval acquisition

Acquire the bounded source needed for S001 and preserve exact release/tag/path/blob identity. Do not broaden into arbitrary documentation retrieval.

### Step 7 — Evaluate the extraction adapter and model only where needed

Use the admitted source to determine whether deterministic extraction is sufficient. When semantic extraction is required, evaluate the bounded LLM path.

Instructor may be compared as an adapter for JSON-Schema generation, Pydantic parsing, grounding context, and diagnostics. Keep first-pass retries disabled during scored evaluation. Adapter selection remains separate from model adoption.

### Step 8 — Correct conditional CLI orchestration

After the upstream claim path and comparator are validated, move target Python acquisition behind the valid grounded support-drop activation condition. Preserve existing PR, CI, package, provenance, and upstream behavior.

### Step 9 — Run S001 end to end

Expected bounded output:

```text
Target Python declaration: available
Target requires-python: >=3.10
Upstream support-drop claim: available
Dropped Python line: 3.8
Target relevance: outside_declared_python_range
```

No compatibility, safety, or merge conclusion may follow from this slice.

## Proof obligations

Controlled and public evidence must prove:

1. upstream evidence is bounded to the exact old/proposed dependency interval;
2. authoritative source identity, tag/revision/path/blob, and exact quote are preserved;
3. a support drop introduced in an intermediate crossed release is not missed merely because the final release body omits it;
4. Dependabot-copied notes do not silently become upstream authority;
5. candidate model output cannot enter the comparator without deterministic validation;
6. wrong category, wrong direction, malformed Python line, ungrounded quote, and out-of-interval claim remain unresolved;
7. target acquisition occurs at the exact PR head SHA;
8. valid `requires-python` evidence preserves path, revision, and blob identity;
9. missing file, malformed TOML, missing table, missing field, and invalid field remain distinct;
10. no target range is inferred from workflows, classifiers, documentation, or tool configuration;
11. comparison cannot run without one trusted support-drop claim and one valid target declaration;
12. included, excluded, compound, wildcard, exclusion, compatible-release, patch-boundary, and unsupported specifier cases are tested;
13. an included dropped line produces only `declared_python_overlap`;
14. an excluded line produces only `outside_declared_python_range`;
15. unsupported semantics produce `comparison_unsupported`;
16. the final CLI does not acquire target Python evidence when no valid support-drop claim activates that responsibility;
17. S001 produces the expected bounded non-overlap result from reacquired evidence;
18. no package, repository, version, release wording, or expected result is hardcoded into production logic;
19. the ordinary product test suite remains green.

## Rejection and reframing conditions

Reframe or stop this slice if:

- authoritative crossed-version change evidence cannot be acquired without unbounded source search;
- release ordering or interval membership cannot be established responsibly;
- the upstream claim cannot expose a reliable normalized Python line without disproportionate semantic tuning;
- the line-overlap algorithm would require a home-grown general PEP 440 parser or arbitrary incomplete enumeration;
- `requires-python` cannot provide a useful distinction for realistic admitted cases;
- useful comparison requires broad target inference before the narrow declaration is tested;
- the result would not affect any later bounded decision state;
- the work begins implying compatibility or safety from declared-range non-overlap.

## Stop line

Stop this plan when UpgradePilot can expose, for S001 or another explicitly admitted case:

```text
one grounded Python support-drop claim from the complete crossed-version interval
+ exact-head target requires-python evidence
→ deterministic declared-range relevance or honest unresolved result
```

Do not continue here into:

- support-added interpretation;
- broad repository usage analysis;
- workflow/tox/configuration aggregation without an activated gap;
- safety scoring or automatic merge/block action;
- target mutation;
- broad semantic-corpus expansion unrelated to an observed blocker;
- model comparison unrelated to the admitted extraction responsibility.

## Maintenance

Change this plan only when its responsibility, source interval, admitted authorities, claim contracts, range method, activation order, result states, proof obligations, rejection conditions, or stop line changes. Do not record live progress, current status, latest commits, or immediate continuation here.