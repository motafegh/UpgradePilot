# Working Memory — B2 R1 Target Artifact-Environment Exact-File Trace

**Date:** 2026-08-23  
**Status:** RESPONSIBILITY TRACE COMPLETE; CODE MIGRATION NEXT  
**Execution branch:** `agent/r1-exact-file-contract-migration`  
**Parent R1 record:** `2026-08-23_B2-R1-step-2c-implementation.md`  
**Current plan:** `../plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`

## 1. Why this is the next bounded R1 consumer

After dependency exact-file extraction and uv-membership composition, the smallest materially different remaining exact-file consumer is:

```text
src/upgradepilot/target/artifact_environment.py
```

It is a Target semantic consumer of one exact workflow file plus one independently supplied dependency-source path.

Its admitted proposition remains the bounded Target slice established on 2026-08-14:

```text
exact workflow source at one immutable repository revision
+ one normalized dependency-source path
→ partial static Target environment facts
```

The result may preserve literal runner/Python/install-declaration facts and explicit limitations, but it does not establish exact wheel compatibility, runtime execution, installation success, or a complete environment.

## 2. Producer / consumer trace

### Exact workflow source

`interpret_target_artifact_environment(...)` accepts `RepositoryFileEvidence`.

For a successful `RepositoryTextFile`, Step 1 already guarantees:

```text
repository
path
revision
content
```

are structurally valid exact-file evidence. GitHub acquisition already owns returned-path, encoding, size/resource, and UTF-8 truth.

The Target interpreter does not combine the workflow file with another independently produced repository/revision identity object before parsing. Therefore rechecking provider metadata inside Target does not establish a new composition proposition.

### Dependency source path

`dependency_source_file` is a plain string supplied independently of the workflow file. It is later interpreted by `observe_direct_installation_declaration(...)` against static workflow commands and working-directory context.

Therefore:

```text
repository_relative_parts(dependency_source_file)
```

remains a legitimate semantic input validation. It is not redundant with `RepositoryTextFile` because it validates a different object.

### Workflow structure

`parse_workflow_definition(evidence)` is the provider-owned bounded GitHub Actions structural interpreter. It already checks the workflow path role (`.github/workflows/*.yml|yaml`) and parses only static admitted YAML structure.

Target should consume that typed IR rather than duplicating workflow-path/YAML structure rules.

## 3. Existing exact-file pressure map

### A. typed file unavailability

**Decision: KEEP.**

`RepositoryFileEvidence` deliberately includes `UnavailableRepositoryFile`. Target cannot interpret a missing workflow source, so `file_unavailable` remains a real Target problem state.

### B. `_validate_exact_file_provenance(...)`

Current checks include old fields such as:

```text
returned_path
reported_byte_count
decoded_byte_count
retrieved_at
```

**Decision: REMOVE ENTIRELY.**

Reason: successful `RepositoryTextFile` construction and GitHub acquisition already own the exact-file/provider invariants. Target has no independent proposition requiring these transport fields.

### C. `insufficient_file_provenance` problem state

**Decision: REMOVE.**

After the strong exact-file contract, there is no admitted successful `RepositoryTextFile` state that this Target layer can legitimately classify as “insufficient provenance.” Keeping an unreachable domain state would preserve the old weak contract conceptually.

### D. `workflow_blob_sha` on `TargetArtifactEnvironmentEvidence`

**Decision: REMOVE.**

Repository search found no independent downstream product proposition that consumes blob identity. Exact workflow provenance is already represented by:

```text
repository + immutable revision + workflow_path
```

The blob field was inherited from the old provider-heavy exact-file contract rather than required by Target semantics.

### E. `repository`, `revision`, `workflow_path` on Target evidence/problem

**Decision: KEEP.**

These values identify the exact repository source from which the Target facts were interpreted. The resulting Target evidence can travel independently of the original `RepositoryTextFile`, so preserving its source locator is real durable provenance rather than provider metadata.

### F. `dependency_source_file` normalized repository-path validation

**Decision: KEEP.**

It is an independent semantic input, not part of the exact workflow file type. Direct-installation interpretation needs a normalized repository-relative path to compare safely against workflow command/path context.

### G. workflow path/YAML role checks

**Decision: KEEP IN `parse_workflow_definition`, NOT DUPLICATE IN Target.**

Target already delegates to the provider-owned workflow IR. If the exact repository file is not an admitted workflow path or its YAML structure is unreadable, the provider IR returns `WorkflowDefinitionProblem`, which Target maps to its own bounded abstention.

## 4. Target contract after migration

Expected durable evidence shape:

```text
TargetArtifactEnvironmentEvidence
├── repository
├── revision
├── workflow_path
├── job
├── runner?
├── python_version?
├── dependency_installation_declaration
├── installation_declaration_source?
├── limitations
└── exact_wheel_compatibility_state = unresolved
```

No blob/byte/retrieval metadata should survive merely because the provider once exposed it.

## 5. Test migration

Nearest test file:

```text
tests/test_target_artifact_environment.py
```

Required changes:

- construct `RepositoryTextFile(repository, path, revision, content)` only;
- remove timestamp/blob/count fixture constants;
- do not add tests that fabricate impossible weak successful file states;
- preserve all existing Target semantic tests;
- add/retain typed unavailability coverage because that remains part of the public input contract.

## 6. What this step does not redesign

Do not change:

```text
runner interpretation
setup-python interpretation
job ambiguity/reusable-job handling
matrix/container limitation semantics
direct-installation observer semantics
exact wheel compatibility boundary
Target decision strength
```

This is only an exact-file ownership migration.

## 7. Learning checkpoint

The key contrast is:

```text
successful strong object
→ do not re-prove its intrinsic/provider facts downstream

independent plain/domain input
→ validate the semantic preconditions actually needed by this consumer

result that outlives its source object
→ preserve the smallest durable provenance needed to identify where the result came from
```

So “remove duplicate provenance checks” does **not** mean “remove provenance.” It means keep provenance at the right abstraction level.

## 8. Proof state

No runtime execution is claimed.

```text
R1 Target artifact-environment trace  COMPLETE
R1 Target code migration              NEXT
```

The latest accepted full runtime baseline remains `bfdfd4257574f85cc3a2d094bf46a37ad6373dea` (`508 tests / OK`).