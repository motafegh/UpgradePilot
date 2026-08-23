# Working Memory — B2 R1 Integration / Provider-Test / Live-Tool Fan-Out Implementation

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; POST-CHANGE RUNTIME VALIDATION PENDING  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent traces:**
- `2026-08-23_B2-R1-integration-live-tool-fanout-trace.md`
- `2026-08-23_B2-R1-pull-request-provider-test-reconciliation.md`

## 1. Slice goal

Take a larger R1 closure slice across three adjacent non-production surfaces that still depended on the retired exact-file representation:

```text
application integration tests
developer live-proof tools
PR-specific repository-provider tests
```

The slice intentionally did not change production source semantics.

## 2. Application integration fixtures migrated

Modified:

```text
tests/test_investigation.py
tests/test_step7f_end_to_end.py
```

All controlled `RepositoryTextFile` values now use only:

```text
repository
path
revision
content
```

Removed fixture-only:

```text
returned_path
blob_sha
reported_byte_count
decoded_byte_count
retrieved_at
byte-size calculations used only to populate those fields
```

Preserved unchanged:

```text
upstream acquisition/authority sequencing
conditional target investigation selection
target acquisition only after grounded upstream support-drop evidence
target inactive when no grounded claim exists
exact target revision propagation
bounded local-model candidate extraction
deterministic source reconstruction and claim admission
impact applicability outcomes
CI branch preservation while upstream/target branches stop
```

## 3. Live S001 tools migrated

Modified:

```text
tools/live_s001_upstream_interval_proof.py
tools/live_s001_support_drop_extractor_proof.py
```

### Upstream interval proof

Removed diagnostics for deleted durable fields:

```text
TaggedChangelogEvidence.blob_sha
reported_byte_count
decoded_byte_count
```

Replaced them with the durable tagged-source locator:

```text
repository@resolved_commit_sha:path
```

Tag-resolution diagnostics remain because the tool explicitly demonstrates `GitHubTagCommitEvidence` acquisition and those fields still belong to that provider evidence type.

### Support-drop extractor proof

Removed:

```text
CrossedReleaseSourceWindow.blob_sha
```

Replaced it with:

```text
repository@resolved_commit_sha:path
```

Preserved:

```text
trusted crossed releases
source-order release sections
character_count / max_characters bound
LM Studio preflight
model candidate reporting
deterministic trust admission
expected S001 bounded outcome
no target/compatibility/safety claim
```

## 4. PR provider suite reconciled by responsibility

Modified:

```text
tests/test_pull_request_repository_files.py
```

The old suite mixed two responsibilities:

1. PR base/head wrapper binding;
2. historical generic provider response metadata.

Generic provider admission is already protected by `tests/test_exact_commit_repository_files.py`, including path mismatch, malformed base64, bounded content without provider-size metadata, exact locator invariants, and typed unavailability.

The PR-specific suite now owns:

```text
PR base wrapper → base SHA
PR head wrapper → head SHA
minimum durable RepositoryTextFile contract
404 exact locator preservation
returned-path mismatch rejection
invalid UTF-8 rejection on the PR wrapper path
```

Removed obsolete tests/assertions for:

```text
returned_path evidence
blob_sha evidence
reported_byte_count
decoded_byte_count
provider-reported size type
reported oversize
reported-vs-decoded size equality
required size field
```

This does **not** weaken file-size protection. Current provider code bounds compact encoded base64 before decoding and bounds decoded bytes afterward. The generic exact-commit suite protects that behavior without trusting GitHub's separate reported-size field.

## 5. Static review

Full slice comparison from pre-slice commit:

```text
1e0c6c1fbeda52e2847ded1052f68a3dcb984cc5
→ current branch after implementation
```

showed:

```text
tests/test_investigation.py                    modified
tests/test_pull_request_repository_files.py    modified
tests/test_step7f_end_to_end.py                 modified
tools/live_s001_support_drop_extractor_proof.py modified
tools/live_s001_upstream_interval_proof.py      modified
+ two working-memory trace records
```

No production source file changed.

A subsequent branch-specific spot check confirmed already-migrated neighboring suites remain on the strong contracts:

```text
tests/test_dependency_change_contracts.py
tests/test_target_artifact_environment.py
tests/test_uv_lock_change.py
tests/test_upstream_interval_acquisition_integration.py
```

## 6. Learning to retain

### A. Diagnostics do not own product evidence shape

```text
a field is convenient to print
!= product must retain the field
```

Tooling follows the product evidence contract.

### B. Tests can become accidental architecture authority

A historical test may encode a representation that was once valid. After an evidence-model correction:

```text
old test fails
→ inspect its unique responsibility
→ preserve proposition
→ migrate/remove obsolete representation assertion
```

Do not restore old production baggage merely to satisfy the old fixture.

### C. Security/resource protection is about effective controls, not field retention

Old model:

```text
trust provider-reported size
+ compare with decoded size
```

Current model:

```text
bound encoded representation before decode
+ strict base64
+ bound actual decoded bytes
+ validate UTF-8
```

The latter protects the resource boundary without turning reported provider metadata into durable evidence.

### D. Integration tests should protect flow, not every lower-layer mechanism

The integration suites retain assertions about:

```text
when evidence is acquired
which branch activates
which identity is preserved
where trust is admitted
what final bounded state results
```

They no longer duplicate transport details already owned at the provider boundary.

## 7. Proof state

```text
trace / ownership review                 COMPLETE
integration fixture migration            COMPLETE
live-tool migration                      COMPLETE
PR provider test reconciliation          COMPLETE
static diff review                       COMPLETE
post-change local runtime validation      NOT PERFORMED
```

Previously recorded focused runtime gates remain valid for the commits on which they ran, but they do not automatically validate these new edits.

## 8. Residual R1 direction

The residual scan is increasingly converging rather than exposing new production design pressure. Branch-specific spot checks show several high-probability default-branch search hits are already migrated on the R1 branch.

Next bounded continuation should therefore be a larger **R1 residual-contract closure audit** across remaining untested/unreviewed standard-test and tool consumers, with these rules:

```text
branch-specific evidence only
no default-branch search hit treated as current fact
production change only if a real surviving consumer proposition demands it
otherwise migrate stale fixtures/tooling
```

After that static closure pass, the highest-value next proof is local execution:

```text
Target-Python family
+ CI/workflow fixture family
+ investigation / Step-7F integration
+ PR provider tests
→ full standard suite
```

If that is green, R1 can move to same-branch `main` reconciliation rather than another contract-migration slice.
