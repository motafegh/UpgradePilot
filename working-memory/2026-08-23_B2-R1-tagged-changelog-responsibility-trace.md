# Working Memory — B2 R1 Tagged-Changelog Responsibility Trace

**Date:** 2026-08-23  
**Status:** RESPONSIBILITY TRACE COMPLETE; BOUNDED MIGRATION NEXT  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Step responsibility

Reconcile tagged-changelog exact-file ownership after the strong `RepositoryTextFile` migration without changing upstream authority policy, Markdown release-section semantics, or the bounded local-LLM support-drop role.

Normal production flow:

```text
DependencyReleaseInterval
+ selected upstream repository
→ resolve proposed-version Git tag
→ GitHubTagCommitEvidence(resolved_commit_sha)
→ discover changelog path at that exact commit
→ get_exact_commit_text_file(repository, resolved_commit_sha, discovered path)
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ build_crossed_release_source_window(...)
→ bounded semantic extraction
```

`investigation.py` therefore pre-binds repository, exact commit, and discovered path before the composer receives the file.

## 2. Ownership findings

### Git tag resolution

`GitHubTagCommitClient` owns external tag-reference identity and annotated-tag peeling. It establishes the requested tag, exact tag ref, supported object type, object SHA chain, and immutable resolved commit SHA.

The tagged-changelog composer must not revalidate tag-response internals merely because `GitHubTagCommitEvidence` can be manually fabricated in tests.

### Exact changelog acquisition

`GitHubRepositoryClient.get_exact_commit_text_file(...)` owns repository/path/revision validation and exact-file acquisition. Successful `RepositoryTextFile` already establishes structural repository/path/revision/content invariants and provider response truth.

Returned path, blob SHA, reported/decoded byte counts, and retrieval time are not separate tagged-changelog propositions.

### Normal orchestration binding

`investigation.py` acquires the changelog with:

```text
repository = selected upstream repository
revision = tag_commit.resolved_commit_sha
path = discovered changelog path at that same commit
```

then immediately composes it with the same tag evidence. Rechecking repository/revision equality in the composer would therefore re-prove normal orchestration rather than establish an independent production join.

## 3. Durable tagged-changelog proposition

The smallest durable source identity needed after composition is:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

Meaning:

> exact non-empty changelog text from one repository/path at the immutable commit resolved for the proposed-version tag, admitted as interval-authority source evidence.

### KEEP

```text
repository
interval
resolved_commit_sha
path
content
```

Reasons:
- repository + commit + path locate the immutable historical source;
- interval binds the authority to the dependency transition under review;
- content is the source used for deterministic windows and grounded semantic extraction.

### REMOVE from durable tagged-changelog evidence

```text
requested_tag
tag_ref
tag_object_type
tag_object_sha
returned_path
blob_sha
reported_byte_count
decoded_byte_count
retrieved_at
```

Reasons:
- tag ref/object/peeling details remain owned by `GitHubTagCommitEvidence` during acquisition/orchestration and are not consumed as independent downstream semantic facts;
- exact proposed version already exists in `interval.proposed_version`;
- returned path/blob/count/time are provider/acquisition metadata and do not establish additional immutable-source authority beyond `(repository, resolved_commit_sha, path)`.

## 4. Composer behavior

`build_tagged_changelog_evidence(...)` should remain a bounded packaging/availability boundary, not become another provider validator.

Keep:

```text
input type admission
UnavailableRepositoryFile → source_unavailable
empty/whitespace exact text → source_unavailable
```

Remove:

```text
requested_tag ↔ interval repeated admission
Git tag ref/object consistency revalidation
file repository ↔ tag repository revalidation
file revision ↔ resolved commit revalidation
returned_path/blob/byte/time checks
```

The removed relations are already established by the normal producer/orchestration path. Direct manual construction is not an independently admitted product route.

## 5. Downstream authority assembly

`assemble_upstream_interval_authority(...)` combines independently supplied interval-authority candidates. It **does** own cross-candidate coherence:

```text
TaggedChangelogEvidence.repository == selected repository
TaggedChangelogEvidence.interval == selected interval
```

Keep those joins.

Intrinsic/provider details inside an already-admitted `TaggedChangelogEvidence` should not be revalidated there. Its minimal source identity/text should be treated as the input contract.

## 6. Crossed-release source window

`build_crossed_release_source_window(...)` combines:

```text
CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
```

It must retain repository + interval equality because those are independent evidence branches.

Its own durable source locator needs:

```text
repository
interval
path
resolved_commit_sha
```

but not blob SHA. `CrossedReleaseSourceWindow.blob_sha` is therefore migration pressure, not a retained proposition.

Markdown heading selection, exact line/offset grounding, character bounds, release ordering, and model-safety boundaries remain unchanged.

## 7. Test migration

Nearest acquisition/composition tests should stop fabricating provider metadata. Replace timestamp/blob/count assertions with current responsibilities:

```text
matching normal evidence → minimal TaggedChangelogEvidence
UnavailableRepositoryFile → source_unavailable
empty exact text → source_unavailable
wrong public input types → TypeError
```

Repository/revision mismatch tests at the composer are obsolete because normal orchestration owns those joins. Independent repository/interval mismatch tests remain at downstream authority/window composition boundaries.

All fixtures constructing `TaggedChangelogEvidence` must migrate to the minimal durable contract; tests are consumers to update, not authority for retaining removed fields.

## 8. Scope exclusions

Do not change:

```text
upstream authority ordering
complete-release-series vs tagged-changelog policy
Markdown release heading rules
crossed-release interval semantics
support-drop candidate validation
grounded source-line recovery
ADR-0006 local-model authority boundary
```

## 9. Proof state

```text
responsibility trace     COMPLETE
code migration           NEXT
runtime execution        NOT PERFORMED
```

Latest historical accepted runtime proof remains `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` — `508 tests / OK`.
