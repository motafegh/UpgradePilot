# AUDIT-001 — Exact PR File Acquisition Evidence Contract

**Audit date:** 2026-08-01  
**Audit type:** implementation/design proportionality audit  
**Trigger:** learning review of the `uv.lock` exact base/head acquisition path and whether its provenance/byte metadata is necessary or over-specified  
**Inspected implementation baseline:** `c36bafc7b72519f97b3ab04ae284d0730e6d173a`  
**Disposition at audit time:** no implementation change authorized; preserve findings for later reassessment  

## 1. Audit question

UpgradePilot currently acquires complete `uv.lock` content at the pull request's exact base and head commit SHAs through GitHub's repository Contents API and returns an `ExactRepositoryTextFile` containing:

```text
repository
requested path
returned path
exact revision
Git blob SHA
GitHub-reported byte count
actual decoded byte count
complete UTF-8 text
```

The audit question is:

> Which parts of this contract are materially required by UpgradePilot's evidence responsibility, which are validation/transport details that do not need to become long-lived domain evidence, and which apparently extra values have a plausible future use in the planned B3/B5 responsibilities?

This is not an audit of whether exact base/head acquisition itself is necessary. Complete exact-revision acquisition remains justified for structured lockfile comparison because a PR patch is not a sufficient structural representation of `uv.lock`.

## 2. Scope

Inspected responsibilities:

```text
recognized modified uv.lock
→ exact base file acquisition
→ exact head file acquisition
→ response/path/size/encoding validation
→ Base64 decoding
→ actual byte-bound validation
→ UTF-8 decoding
→ ExactRepositoryTextFile
→ uv.lock source-evidence reconciliation
→ DependencyFileEvidence
→ PR-wide DependencyVersionChange
```

This audit evaluates the **acquisition/evidence contract** and how its metadata propagates into dependency evidence.

### Explicitly outside scope

The following are not being reassessed here:

- `uv.lock` TOML schema semantics beyond how the parser consumes exact file evidence;
- duplicate package-record comparison rules;
- PEP 440 version ordering;
- upstream support-drop relevance;
- target Python evaluation;
- CI authority;
- recommendation or maintainer-action logic;
- the one-million-byte bound value itself, except for how size is measured and stored.

## 3. Controlling and related project records

### Durable architecture

- [`../docs/architecture/ADR-0004-dependency-version-change-evidence.md`](../docs/architecture/ADR-0004-dependency-version-change-evidence.md)
  - Section 5 explicitly selected exact PR base/head acquisition through the GitHub Contents endpoint.
  - It requires preservation of repository, path, revision, returned path, blob SHA, reported byte size, decoded byte size, and UTF-8 text.
  - It rejects a blob/raw fallback for the B2 proof because the selected S001 files fit the bounded Contents path.

### Route implications

- [`../plans/UPGRADEPILOT_90_DAY_PLAN.md`](../plans/UPGRADEPILOT_90_DAY_PLAN.md)
  - B3 includes acquisition/replay robustness, raw preservation or durable references where justified, changed-head handling, malformed/failed-source handling, and deterministic replay.
  - B5 includes justified persistence, diagnostics, useful queries, idempotent storage, supersession, and corpus identity.

These planned responsibilities are the main credible future reasons to retain or redesign richer acquisition identity.

## 4. Affected source code and symbols

### `src/upgradepilot/github_repository.py`

Primary acquisition boundary:

- `ExactRepositoryTextFile`
  - currently stores `repository`, `path`, `returned_path`, `revision`, `blob_sha`, `reported_byte_count`, `decoded_byte_count`, and `content`;
- `UnavailableRepositoryFile`
  - preserves repository/path/revision plus ambiguity for absent or inaccessible exact content;
- `GitHubRepositoryClient.get_pull_request_base_file(...)`
  - selects `identity.base_sha`;
- `GitHubRepositoryClient.get_pull_request_head_file(...)`
  - selects `identity.head_sha`;
- `GitHubRepositoryClient._get_exact_pull_request_text_file(...)`
  - validates the requested revision is exactly the PR base or head SHA;
  - validates repository-relative path;
  - requests GitHub Contents JSON with `ref=<exact SHA>`;
  - validates response type/path/blob/size/encoding/content;
  - applies the reported-size bound before Base64 decoding;
  - Base64-decodes content;
  - requires decoded byte count to equal reported byte count;
  - applies the actual-byte bound;
  - decodes UTF-8;
  - returns `ExactRepositoryTextFile`;
- `_decode_base64_repository_content(...)`
  - converts the Contents API transport representation into bytes;
- `_decode_utf8_repository_content(...)`
  - converts accepted bytes into deterministic text;
- `_validate_repository_path(...)`
  - rejects ambiguous or unsafe repository-relative path forms.

### `src/upgradepilot/dependency_analysis.py`

Integration boundary:

- `analyze_dependency_change(...)`
  - recognizes modified `uv.lock` files;
  - calls `get_pull_request_base_file(...)` and `get_pull_request_head_file(...)`;
  - passes both exact files to `extract_uv_lock_changes(...)`;
- `is_uv_lock_file(...)`
  - performs path recognition independently from status admission.

### `src/upgradepilot/uv_lock_change.py`

Source-specific evidence interpretation:

- `extract_uv_lock_changes(...)`
  - rejects unavailable exact files and begins lockfile interpretation only after acquisition succeeds;
- `_build_source_evidence(...)`
  - requires base/head repository identity to agree;
  - requires requested and returned paths to match the changed-file identity;
  - requires revision and blob SHA to be present;
  - requires reported and decoded byte counts to be valid, equal, and non-negative;
  - converts acquisition evidence into `DependencyFileEvidence`;
- `_parse_uv_lock(...)`
  - receives already validated UTF-8 text and begins TOML/schema interpretation.

### `src/upgradepilot/dependency_change.py`

Longer-lived dependency evidence:

- `DependencyFileEvidence`
  - stores `path`, file format, extraction method, base/head revision, base/head blob SHA, and base/head byte count;
- `ExtractedDependencyVersionChange`
  - attaches one `DependencyFileEvidence` record to a source-specific transition;
- `DependencyVersionChange`
  - carries one or more `DependencyFileEvidence` records after PR-wide comparison;
- `compare_extracted_dependency_changes(...)`
  - combines equivalent evidence and preserves evidence records downstream.

## 5. Affected tests

### `tests/test_pull_request_repository_files.py`

Direct acquisition-contract coverage includes:

- `test_base_and_head_acquisition_preserve_exact_file_evidence`
- `test_ambiguous_404_preserves_repository_path_and_revision`
- `test_returned_path_must_match_requested_path`
- `test_reported_size_must_be_a_nonnegative_integer`
- `test_reported_oversize_is_rejected_before_base64_decoding`
- `test_malformed_base64_remains_distinct`
- `test_reported_and_decoded_sizes_must_agree`
- `test_invalid_utf8_remains_distinct`
- `test_missing_reported_size_is_malformed_response`

### `tests/test_uv_lock_change.py`

Relevant source-evidence coverage includes:

- `test_extracts_one_transition_and_preserves_exact_source_evidence`
- `test_unavailable_exact_file_blocks_extraction`
- `test_exact_file_identity_must_match_repository_and_changed_path`

The file also protects the downstream lockfile structural rules that must remain unaffected by any acquisition simplification.

### `tests/test_uv_lock_versionless_records.py`

Constructs `ExactRepositoryTextFile` fixtures and therefore depends on the current acquisition record shape even though its real responsibility is versionless workspace-record behavior.

### `tests/test_dependency_analysis.py`

Relevant integration coverage includes:

- `test_modified_uv_lock_acquires_exact_files_and_preserves_provenance`
- `test_exact_files_are_acquired_only_for_modified_uv_lock`
- `test_equivalent_requirements_and_uv_lock_evidence_are_combined`
- `test_unavailable_lockfile_blocks_valid_requirements_result`

The test helpers also currently construct `ExactRepositoryTextFile` with blob and dual byte-count fields.

## 6. Baseline conclusion

The acquisition responsibility is **not broadly overengineered**.

The following remain strongly justified for the supported `uv.lock` path:

```text
repository identity
complete relative path
exact immutable base/head commit SHA
complete file content
returned-path equality validation
regular-file response validation
bounded input size
valid UTF-8 text
explicit unavailable/inaccessible evidence
```

These controls directly support complete structural comparison, immutable PR evidence, deterministic parsing, and safe bounded processing.

The main proportionality concern is narrower:

> Some values useful while validating the GitHub response are promoted into `ExactRepositoryTextFile` and then into `DependencyFileEvidence` even though later dependency reasoning currently does not consume their unique meaning.

The likely simplification target is therefore the **evidence-record shape**, not necessarily the current Contents JSON transport.

## 7. Findings

### AUDIT-001-F1 — `returned_path` is validation evidence, not obviously long-lived domain state

**Classification:** simplification opportunity  
**Current severity:** low  
**Recommended disposition:** keep the equality check; reassess storing the duplicate field when the acquisition contract is next changed.

The current acquisition correctly checks:

```text
returned_path == requested path
```

This is useful because an HTTP success for another path must not become evidence for the requested dependency file.

After successful validation, however, every accepted record necessarily contains:

```text
requested path == returned path
```

The second value carries no additional successful-domain state. It is a strong example of information that may be needed **during validation** without needing to survive in the returned application record.

Potential future value is weak. If GitHub returns a contradictory path, acquisition already fails and the mismatch belongs in the error/diagnostic record rather than a successful evidence record.

### AUDIT-001-F2 — `decoded_byte_count` is derivable and has no unique downstream meaning

**Classification:** simplification opportunity  
**Current severity:** low  
**Recommended disposition:** keep actual-byte measurement for the bound; do not assume the value must remain stored permanently.

The actual decoded byte length is needed while acquiring content:

```text
decoded bytes
→ len(...)
→ reject if over configured bound
```

Once bytes are successfully decoded as UTF-8 and the complete text is preserved, the byte count can be reproduced from the text with UTF-8 encoding. It is therefore derived data rather than unique provenance.

Current downstream dependency reasoning does not use the numeric value to establish package identity, version identity, lockfile structure, relevance, or a decision.

Future B5 persistence may choose to index artifact sizes, but that requirement does not exist yet and could calculate/store size in a storage-specific artifact record if justified.

### AUDIT-001-F3 — GitHub-reported byte size is unique provider metadata but weak domain evidence

**Classification:** future-reassessment item / possible simplification  
**Current severity:** low  
**Recommended disposition:** preserve the existing check for now; reconsider whether the value belongs in `DependencyFileEvidence` when B3 acquisition diagnostics/replay is designed.

Unlike `decoded_byte_count`, GitHub's reported `size` is not derivable from local content because it is an external assertion made by the provider.

It enables one distinct check:

```text
GitHub reports X bytes
actual Base64-decoded body contains Y bytes
X != Y
→ malformed/contradictory response
```

This can be valuable for diagnosing an abnormal provider response.

However, its current downstream value is limited:

- it does not identify the repository or PR revision;
- it does not establish package/version meaning;
- it does not independently prove content integrity;
- after successful validation, the actual content remains the evidence used by the parser.

The pre-decode size check prevents an additional Base64-decoded allocation for a provider-reported oversized file, but the JSON response and encoded content have already been received and parsed by that point. This is a bounded defensive optimization, not a complete network/memory protection mechanism.

B3 may justify preserving raw acquisition metadata or durable response references. If so, reported size may fit better in an acquisition diagnostic/artifact record than in the long-lived dependency-domain record.

### AUDIT-001-F4 — Git blob SHA has plausible future value, but its purpose should be explicit

**Classification:** accepted provisional complexity / future design question  
**Current severity:** none as a defect  
**Recommended disposition:** do not remove casually; reassess against B3 replay/caching and B5 persistence/corpus identity before changing the field.

The Git blob SHA gives a file-content object identity that can remain the same across different commits. That can support future capabilities such as:

- detecting identical file content across revisions;
- cache keys for already-parsed repository files;
- deduplicating stored evidence;
- Git-level traceability during replay or diagnosis.

Those capabilities are more plausible in B3/B5 than the future value of the byte-count fields.

The blob SHA is nevertheless not currently required to extract or compare a dependency version change because repository + path + exact commit SHA already identifies the file location in the immutable repository snapshot.

Also, the current implementation **does not independently verify the returned bytes against the blob SHA**. It accepts the blob identity and content from the same GitHub response. Therefore the field should not be described as independent cryptographic integrity proof.

When durable evidence storage is designed, compare two alternatives explicitly:

```text
GitHub blob SHA
versus
provider-neutral content fingerprint computed by UpgradePilot
```

A provider-neutral content fingerprint may be more reusable if future replay/corpus evidence can originate outside a live GitHub Contents response.

### AUDIT-001-F5 — Repository identity is validated at the source boundary but dropped from `DependencyFileEvidence`

**Classification:** provenance-model question  
**Current severity:** low while evidence remains PR-scoped  
**Recommended disposition:** reassess before standalone replay/persistence records are introduced.

`ExactRepositoryTextFile` stores the repository, and `_build_source_evidence(...)` requires base and head repository values to agree.

But `DependencyFileEvidence` currently preserves:

```text
path
base/head revision
base/head blob SHA
base/head byte count
```

and does **not** preserve repository identity.

This is notable because repository identity is arguably more semantically important provenance than byte counts.

It is not necessarily a present bug: today the dependency result is produced inside an already known `PullRequestIdentity` context, so the enclosing analysis can supply repository scope.

The question becomes material if B3/B5 introduces standalone captured evidence, replay artifacts, persisted dependency evidence, or cross-run corpus queries. At that point the design should make one of these explicit:

```text
A. every evidence record is self-identifying and includes repository
or
B. repository identity is owned by a mandatory enclosing analysis/artifact record
```

Do not add duplicate repository fields everywhere without deciding the ownership model.

### AUDIT-001-F6 — Switching to raw GitHub file transport is not currently justified solely to remove Base64 handling

**Classification:** accepted current complexity  
**Current severity:** none  
**Recommended disposition:** keep the current Contents JSON path unless a later acquisition requirement creates a stronger reason to change it.

GitHub supports other ways to obtain exact file content, including raw-content representations. A raw path could conceptually reduce:

```text
JSON content field
→ Base64 decoding
```

into direct response bytes.

That does not automatically make it the better UpgradePilot implementation.

The existing `GitHubApiClient` path already handles structured GitHub JSON responses. Introducing a separate raw-byte HTTP primitive merely to avoid one deterministic Base64 decode could increase shared transport complexity more than it reduces the file-acquisition contract.

The current concern is therefore not "Base64 exists". The concern is whether transport-specific validation metadata should become permanent application/domain evidence.

Reassess raw/blob/alternate acquisition only if a concrete requirement appears, such as:

- selected files exceed the admitted Contents behavior or size boundary;
- B3 raw-response preservation is materially easier through another representation;
- replay requires byte-exact artifacts unavailable through the present abstraction;
- provider API behavior changes;
- a measured performance/resource problem appears.

## 8. Field-by-field disposition matrix

| Value/control | Needed during acquisition now? | Unique information? | Needed as long-lived dependency evidence now? | Plausible future value | Audit disposition |
|---|---:|---:|---:|---|---|
| Repository | Yes | Yes | Contextually yes | High for replay/persistence | Preserve; decide ownership before B3/B5 persistence |
| Requested path | Yes | Yes | Yes | High | Preserve |
| Returned path | Yes, for equality validation | Only before validation | No clear need | Low | Validate, then candidate to discard |
| Exact commit SHA | Yes | Yes | Yes | Very high | Preserve |
| Complete UTF-8 text | Yes | Yes | Required by parser | Very high/replay | Preserve or durable-reference it later |
| Git blob SHA | No for semantic extraction | Yes as Git object identity | No current semantic need | Medium/high for cache/dedup/traceability | Retain provisionally; reassess deliberately |
| GitHub-reported byte size | Yes under current response contract | Yes as provider assertion | No clear need | Narrow diagnostic value | Candidate to keep local/diagnostic later |
| Actual decoded byte size | Yes for bound | No; derivable | No | Low | Candidate to stop persisting |
| UTF-8 validation | Yes | N/A control | Successful text implies it | High correctness value | Preserve the control |
| Maximum-byte bound | Yes | N/A control | Limit itself belongs to acquisition policy | High resource-safety value | Preserve unless evidence changes the bound |

## 9. Recommended future decision sequence

No immediate refactor is required by this audit.

When the acquisition/evidence responsibility is next deliberately changed, use this sequence:

### Gate A — B3 acquisition and replay robustness

Decide what the replay unit actually is:

```text
normalized exact text
raw response body
provider response + metadata
durable content reference
```

Then decide which acquisition-only fields belong with that unit rather than automatically propagating them into `DependencyFileEvidence`.

### Gate B — content identity requirement

If caching, deduplication, or corpus identity becomes real, compare:

```text
Git blob SHA
provider-neutral content fingerprint
both
```

Select the smallest mechanism that satisfies the observed requirement.

### Gate C — B5 persistence model

Define where repository identity lives:

```text
self-contained evidence record
or
enclosing analysis/run artifact
```

Only then decide whether `DependencyFileEvidence` itself needs `repository`.

### Gate D — simplification refactor

If the findings remain valid, consider narrowing a successful exact-text record toward a shape conceptually similar to:

```text
repository
path
revision
content
[content identity only if justified]
```

while keeping path equality, encoding validation, size bounding, unavailable evidence, and other transport checks inside the acquisition boundary.

This is a candidate direction, not an approved target schema.

## 10. Reassessment triggers

Reopen this audit when any of the following occurs:

1. B3 begins implementation of deterministic replay or raw evidence preservation.
2. A selected real dependency file exceeds or stresses the current bounded acquisition path.
3. GitHub changes the Contents response contract used by UpgradePilot.
4. A cache or repeated-analysis optimization is justified by measured work.
5. B5 begins designing persisted evidence, corpus identity, or cross-run queries.
6. A diagnostic need requires explaining provider response inconsistencies after the live request is gone.
7. Another repository provider or non-live replay source is admitted and GitHub-specific identity begins leaking into source-neutral contracts.
8. `ExactRepositoryTextFile` or `DependencyFileEvidence` is otherwise being changed, making simplification low-cost.

## 11. Proof required if a later change is authorized

Any refactor based on these findings must preserve at least the following observable behavior:

### Exact identity

- base acquisition must use exactly `PullRequestIdentity.base_sha`;
- head acquisition must use exactly `PullRequestIdentity.head_sha`;
- arbitrary historical revisions must not silently enter the PR-specific acquisition method;
- repository-relative path validation must remain explicit;
- a contradictory returned path must not become successful evidence.

### Complete usable content

- `uv.lock` comparison must still receive the complete base and head file contents, not a partial diff;
- unavailable/inaccessible files must remain distinct from empty files;
- malformed transport content must not become valid text;
- non-UTF-8 content must not silently use replacement characters or guessed encodings;
- the configured actual-input size bound must remain enforced.

### Dependency evidence semantics

- `extract_uv_lock_changes(...)` must continue to receive identity-bound base/head evidence;
- a clear one-package transition must preserve source path and exact base/head revisions;
- source/path/revision contradictions must not be silently joined;
- multiple, ambiguous, malformed, and structural-change behavior must remain unchanged unless separately authorized.

### Regression scope

At minimum, update/run the focused acquisition, lockfile, and integration suites affected by the record-shape change, followed by the broader deterministic suite required by the selected plan.

## 12. Candidate follow-up references

If a later change addresses this audit, the change record should reference one or more stable finding IDs:

```text
AUDIT-001-F1 — returned-path lifetime
AUDIT-001-F2 — decoded byte-count persistence
AUDIT-001-F3 — reported-size domain placement
AUDIT-001-F4 — blob/content identity
AUDIT-001-F5 — repository provenance ownership
AUDIT-001-F6 — transport representation
```

A later ADR, plan, implementation commit, or validation record should state which finding it resolves, rejects, or supersedes and why.

## 13. Audit conclusion

The exact base/head `uv.lock` acquisition mechanism contains **justified defensive work** and should not be simplified into "download some text and parse it." Exact immutable revisions, complete content, path reconciliation, bounded input, UTF-8 validation, and explicit unavailability are aligned with UpgradePilot's evidence-backed product boundary.

The stronger audit concern is that the successful acquisition record and downstream dependency evidence currently preserve more GitHub transport/validation metadata than downstream semantic reasoning needs.

The clearest candidates for later simplification are:

```text
returned_path after equality validation
decoded_byte_count as persisted evidence
reported_byte_count as dependency-domain evidence
```

The Git blob SHA is different: it is not needed for today's dependency semantics, but it can provide useful file-content identity for later replay, caching, deduplication, or corpus work. Its future role should be decided explicitly rather than either defended forever or removed casually.

Finally, the audit exposes a provenance question worth revisiting before persistence: repository identity is validated at acquisition but dropped from `DependencyFileEvidence`, while less semantically important byte/blob metadata survives. That may be correct while evidence is always PR-scoped, but the ownership should be made explicit before standalone replay or persisted evidence is introduced.
