# Working Memory — B2 R1 Tagged-Changelog Exact-Source Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; EXECUTION VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent reasoning record:** `2026-08-23_B2-R1-tagged-changelog-responsibility-trace.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Step responsibility

Reconcile the proposed-tag changelog path with the R1 strong exact-file ownership model without changing upstream authority policy, deterministic Markdown release-window semantics, grounded-claim validation, or ADR-0006 local-model authority boundaries.

Normal product path remains:

```text
DependencyReleaseInterval
+ selected upstream repository
→ GitHub tag resolution
→ GitHubTagCommitEvidence(resolved_commit_sha)
→ changelog discovery at that exact commit
→ RepositoryTextFile(repository, path, resolved_commit_sha, content)
→ build_tagged_changelog_evidence(...)
→ TaggedChangelogEvidence
→ assemble_upstream_interval_authority(...)
→ crossed-release source window
→ bounded semantic extraction / deterministic grounding
```

## 2. Important trace correction

Before the trace, the likely assumption was that tagged-changelog composition would need to retain repository/revision checks because tag evidence and file evidence are conceptually separate objects.

The real call path showed otherwise:

```text
investigation.py
→ resolves one tag commit
→ discovers the changelog at that same commit
→ calls get_exact_commit_text_file(selected repository, resolved_commit_sha, discovered path)
→ immediately passes that file + same tag evidence to build_tagged_changelog_evidence(...)
```

Therefore the composer is a controlled packaging stage, not an independently supplied tag/file composition boundary.

This is another concrete example of:

```text
conceptually separate objects
!= independently composed production evidence branches
```

## 3. Final durable tagged-changelog contract

`TaggedChangelogEvidence` is now:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

Interpretation:

> exact non-empty changelog text at one immutable repository/commit/path, admitted as authority for the selected dependency release interval.

Removed durable fields:

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

- tag ref/object/peeling details are acquisition evidence owned by `GitHubTagCommitEvidence` and its provider;
- the interval already contains the proposed version;
- `(repository, immutable resolved commit, path)` is the durable exact-source locator needed downstream;
- returned path/blob/count/time are provider/acquisition facts, not additional upstream authority propositions.

## 4. Strong domain-type ownership

Static review caught a potential recreation of the original weak-type problem: after shrinking `TaggedChangelogEvidence`, direct construction could still represent a fake commit or malformed path/text.

The successful domain type now owns its intrinsic invariants in `__post_init__`:

```text
repository
→ validate_repository(...)

resolved_commit_sha
→ canonical 40/64-hex validate_commit_sha(...)

path
→ normalized repository-relative POSIX path

content
→ non-empty usable text

interval
→ must be DependencyReleaseInterval
```

Consequences:

```text
malformed intrinsic tagged-source record
→ rejected at construction

later authority assembler
→ does not revalidate those intrinsic fields
→ only joins independent repository/interval candidates
```

This mirrors the R1 principle already established for `RepositoryTextFile`:

```text
successful type owns intrinsic validity
composition boundary owns relationships
```

## 5. `build_tagged_changelog_evidence(...)`

The composer now keeps only:

```text
public input type admission
UnavailableRepositoryFile → source_unavailable
empty exact file text → source_unavailable
resolved commit from GitHubTagCommitEvidence
path/content from RepositoryTextFile
```

It no longer revalidates:

```text
proposed tag spelling
Git tag ref/object internals
file repository == tag repository
file revision == tag resolved commit
returned_path/blob/count/time
```

Those relations are already established by the admitted normal orchestration/provider route. Direct manual mismatch construction is not an independently supported product route.

## 6. Authority assembly keeps the real independent join

`assemble_upstream_interval_authority(...)` can receive independently supplied authority candidates, so it still owns:

```text
TaggedChangelogEvidence.repository == selected upstream repository
TaggedChangelogEvidence.interval == selected DependencyReleaseInterval
```

It also retains distinct-candidate ambiguity handling.

After strengthening `TaggedChangelogEvidence`, it no longer revalidates the candidate's commit/path/content field-by-field.

This boundary therefore demonstrates:

```text
intrinsic source validity
!= cross-candidate authority coherence
```

## 7. Crossed-release source window

`CrossedReleaseSourceWindow` no longer carries `blob_sha`.

Its durable source locator is:

```text
repository
interval
path
resolved_commit_sha
```

plus the deterministic selected sections, exact line IDs/offsets, text, and character-bound facts.

`build_crossed_release_source_window(...)` retains the independent:

```text
CrossedReleaseIndexEvidence.repository/interval
↔ TaggedChangelogEvidence.repository/interval
```

join.

Static review then removed a residual revalidation of changelog commit/path/content because those are now intrinsic `TaggedChangelogEvidence` invariants.

No changes were made to:

```text
ATX Markdown heading grammar
fenced-code exclusion
release-section completeness
release ordering
source-line IDs
character offsets
window character bounds
```

## 8. AI/LLM boundary preserved

The downstream support-drop model still receives only the deterministic crossed-release source window and remains an untrusted semantic selector.

Unchanged proof flow:

```text
exact tagged source
→ deterministic release window + line IDs
→ local model semantic candidate
→ deterministic exact-line recovery
→ validate_support_drop_candidates(...)
→ grounded claim or explicit problem
```

No source authority, repository identity, quote offsets, compatibility, safety, or action authority was transferred to the model.

The live Step-6C experiment fixture and semantic corpus fixtures were migrated to the new domain contract without changing their model prompts/oracles/trust-boundary logic.

## 9. Production files changed

```text
src/upgradepilot/upstream/interval_evidence.py
src/upgradepilot/upstream/interval.py
src/upgradepilot/upstream/changelog.py
```

Key production commits include:

```text
9a9b2e380ed68e22a18cb500b2f75f12ea7c2677
→ narrow tagged-changelog composer

402bc24a566436c8f4bc7d3efeaffb7473d930d0
→ minimize durable TaggedChangelogEvidence

0fd2dab5580af76fa99193cefed73e6114c07fe6
→ remove blob propagation from source window

6b95806d0a71bc19637622fda5cc09ee2348147c
→ strengthen minimal TaggedChangelogEvidence intrinsic invariants

27b5305a7dcafbc709bbf354852534a7e6e22a43
→ remove residual source-window revalidation of strong tagged evidence
```

## 10. Test and experiment migration

Standard test consumers migrated:

```text
tests/test_tagged_changelog_acquisition.py
tests/test_upstream_changelog.py
tests/test_upstream_interval.py
tests/test_upstream_interval_authority_edges.py
tests/test_upstream_interval_acquisition_integration.py
tests/test_upstream_claim.py
tests/test_upstream_claim_edges.py
tests/test_upstream_support_drop.py
tests/test_support_drop_extractor.py
```

Experiment consumers migrated:

```text
experiments/tests/test_step6_support_drop_semantic_corpus.py
experiments/step6_support_drop_smoke.py
```

Tests no longer fabricate tagged-source blob/byte/returned-path/retrieval metadata.

Obsolete composer mismatch tests were removed where normal orchestration owns the relation. Retained or added coverage protects:

```text
minimal matching tagged source
lightweight-tag resolved commit propagation
typed file unavailability
empty file not promoted to authority
wrong public input types
TaggedChangelogEvidence constructor invariants
repository/interval mismatch at independent authority/window boundaries
distinct tagged-source ambiguity
Markdown completeness/order/offset/bounds behavior
grounded claim and local-model trust boundaries
```

## 11. Static review result

Comparison from pre-step branch point `68050a52edbd22f7679d85618998c8fab35c21d4` showed the migration confined to the three upstream production modules, their tests/experiment fixtures, and this working-memory family.

Static review found and corrected two important issues before closure:

1. `TaggedChangelogEvidence` initially remained weakly constructible after field removal → strengthened with intrinsic `__post_init__` validation.
2. `build_crossed_release_source_window(...)` initially still revalidated strong tagged-source commit/path/content → removed after ownership review.

No runtime execution was performed.

## 12. Proof state

```text
responsibility trace        COMPLETE
production migration        COMPLETE
standard test migration     COMPLETE
experiment fixture migration COMPLETE
static review               COMPLETE
runtime execution           NOT PERFORMED
```

Latest historical accepted runtime proof remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

No claim from this migration supersedes that runtime evidence.

## 13. Next R1 pressure discovered

A final product-source scan found another remaining exact-file consumer:

```text
src/upgradepilot/target/python.py
```

Current pressure includes:

```text
TargetPythonDeclaration.blob_sha
TargetPythonDeclarationProblem.blob_sha
RepositoryTextFile.blob_sha propagation
```

This is a separate Target-domain proposition (`pyproject.toml [project].requires-python`) and must receive its own producer/consumer/retention trace before editing.

Therefore:

```text
R1 tagged-changelog step    COMPLETE / STATIC ONLY
R1 overall                  STILL IN PROGRESS
next bounded trace          target/python.py
R2                          NOT STARTED
```
