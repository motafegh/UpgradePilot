# Working Memory — B2 R1 Target Artifact-Environment Exact-File Migration

**Date:** 2026-08-23  
**Status:** IMPLEMENTED + STATICALLY REVIEWED; EXECUTION VALIDATION DEFERRED  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent reasoning record:** `2026-08-23_B2-R1-target-artifact-environment-responsibility-trace.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Step responsibility

Migrate the bounded Target artifact-environment consumer to the strong exact-file contract without changing Target semantics or entering exact wheel-compatibility work.

The admitted flow remains:

```text
RepositoryFileEvidence for one workflow source
+ normalized dependency_source_file
→ provider-owned GitHub Actions static IR
→ Target interpretation
→ partial provenance-carrying artifact-environment evidence/problem
```

This is a single-source semantic consumer, not a multi-identity composition boundary like uv membership.

## 2. Files changed

Production:

```text
src/upgradepilot/target/artifact_environment.py
```

Nearest tests:

```text
tests/test_target_artifact_environment.py
```

Implementation commits:

```text
0b3e635bbc8020553ad20bf24063330aa04e3425
→ remove obsolete Target exact-file provenance revalidation and workflow blob propagation

2d3becb8cacbb595e088d12f19a5ad97f63b5702
→ migrate Target fixtures and add retained-boundary tests
```

## 3. Final exact-file ownership

Successful workflow evidence remains:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Target no longer attempts to re-prove provider/intrinsic facts after this object exists.

Removed:

```text
_validate_exact_file_provenance(...)
TargetArtifactEnvironmentProblemState.insufficient_file_provenance
TargetArtifactEnvironmentEvidence.workflow_blob_sha
returned_path / byte-count / retrieved-at dependency through Target
```

Reason:

```text
GitHub acquisition
→ owns external response truth and resource checks

RepositoryTextFile
→ owns exact-file structural invariants

Target artifact-environment interpreter
→ owns only Target semantics and its independent semantic inputs
```

No current Target proposition requires independent Git blob identity or acquisition-time metadata.

## 4. Durable provenance that remains

`TargetArtifactEnvironmentEvidence` still preserves:

```text
repository
revision
workflow_path
```

This is intentional.

The Target result can travel independently after the original `RepositoryTextFile` has been consumed. Those three fields identify the exact repository source from which the Target facts were interpreted:

```text
repository + immutable revision + workflow path
→ exact source locator for the derived Target evidence
```

This is durable domain provenance, unlike blob/byte/retrieval metadata.

## 5. Independent semantic input that remains validated

`dependency_source_file` is not part of `RepositoryTextFile`. It is an independently supplied plain string used by the shared direct-install observer.

Therefore this remains:

```python
repository_relative_parts(dependency_source_file)
```

and malformed/non-repository-relative input still raises `ValueError`.

The distinction is:

```text
strong exact object
→ do not revalidate intrinsic/provider properties

independent semantic argument
→ validate the preconditions needed by this consumer
```

## 6. Workflow structure ownership remains delegated

Target still calls:

```python
parse_workflow_definition(evidence)
```

The provider-owned static workflow IR remains responsible for:

```text
.github/workflows path role
YAML structural parsing
jobs / steps / uses / run static structure
source spans
```

Target maps `WorkflowDefinitionProblem` into its bounded Target problem state rather than duplicating YAML/path parsing.

## 7. Target semantics intentionally unchanged

Static diff review confirms no intended changes to:

```text
single-job selection
reusable-workflow abstention
runner interpretation
setup-python literal version interpretation
matrix/container limitation recording
direct dependency-source installation observation
working-directory handling
observed / not_observed / unresolved installation declaration semantics
exact_wheel_compatibility_state = unresolved
```

Proof guards remain:

```text
runner + Python declaration != exact wheel compatibility
static install declaration != runtime execution/success
not_observed != established absence
partial Target evidence != final compatibility evidence
```

## 8. Test migration

The test fixture now constructs only the strong exact-file contract:

```python
RepositoryTextFile(
    repository=...,
    path=...,
    revision=...,
    content=...,
)
```

Removed fixture machinery:

```text
blob SHA
datetime/retrieved_at
reported byte count
decoded byte count
returned_path
```

Existing semantic tests were preserved.

Two retained boundaries now have explicit focused coverage:

```text
UnavailableRepositoryFile
→ TargetArtifactEnvironmentProblem(state="file_unavailable")

malformed dependency_source_file
→ ValueError before semantic interpretation
```

These tests protect actual current responsibilities rather than deleted provider metadata.

## 9. Static review result

Production diff inspection showed the material changes are limited to:

```text
remove unreachable insufficient_file_provenance state
remove workflow_blob_sha from derived Target evidence
remove _validate_exact_file_provenance(...)
clarify ownership docstrings/comments
```

No Target semantic algorithm changed.

Repository/file review of the migrated source found no remaining `workflow_blob_sha` or `insufficient_file_provenance` references in the Target artifact-environment module.

## 10. Proof state

```text
R1 Target artifact-environment trace       COMPLETE
R1 Target artifact-environment migration   IMPLEMENTED
R1 Target static review                    COMPLETE
R1 Target runtime execution                NOT PERFORMED
```

No green/runtime claim is attached to these commits.

Latest accepted full runtime baseline remains:

```text
bfdfd4257574f85cc3a2d094bf46a37ad6373dea
508 tests / OK
```

When local WSL execution is available, add at least:

```text
tests.test_target_artifact_environment
```

to the accumulated R1 focused validation ledger.

## 11. Learning checkpoint

The central lesson is:

```text
provenance != provider metadata
```

More precisely:

```text
provider/acquisition metadata
→ facts needed to admit external bytes safely

exact-file identity
→ repository + immutable revision + path

derived-domain provenance
→ the smallest source locator the result needs after the source object is gone
```

Removing blob/count/time propagation did not remove Target provenance. It moved Target provenance to the correct abstraction level.

## 12. Next bounded R1 continuation

R1 is still not complete. The next materially different pressure should be the **tagged upstream changelog composition path**:

```text
GitHubTagCommitEvidence
+ RepositoryFileEvidence at the resolved tag commit
→ TaggedChangelogEvidence / UpstreamAuthoritySourceProblem
```

That path is expected to differ from this Target step because it genuinely composes two independently acquired identity branches (resolved tag evidence + exact repository file), so repository/revision joins may remain while returned-path/blob/byte/retrieval propagation is pressured separately.

Perform the end-to-end ownership trace before editing it.