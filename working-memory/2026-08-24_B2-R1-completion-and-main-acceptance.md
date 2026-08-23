# B2 R1 Completion and Main Acceptance

**Date:** 2026-08-24  
**Plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Accepted executable commit:** `9fb19dd483f568a459a0680527a8b00683334359`  
**Status:** R1 COMPLETE — R2 NOT STARTED

## 1. Closure statement

R1 — **Strengthen exact repository-file evidence ownership** — is complete.

The accepted implementation establishes a strong exact repository-text contract, removes retired provider/acquisition metadata from durable downstream evidence where no independent proposition requires it, preserves external GitHub admission checks at the provider boundary, preserves genuine semantic/composition joins, migrates affected consumers/tests/tools, and passes the required runtime acceptance gates.

No known R2–R5 uv reachability/structural concerns were pulled into R1 merely to make closure broader.

## 2. Accepted exact-file contract

Successful exact repository text:

```text
RepositoryTextFile
├── repository
├── path
├── revision
└── content
```

Typed unavailability:

```text
UnavailableRepositoryFile
├── repository
├── path
├── revision
├── reason
└── detail
```

Not retained as durable exact-file evidence:

```text
returned_path
reported_byte_count
decoded_byte_count
blob_sha
retrieved_at
```

Provider-local validation of returned path, regular-file type, supported base64 encoding, strict base64, actual encoded/decoded bounds, UTF-8, and immutable repository/path/revision identity remains intact.

## 3. Accepted ownership model

```text
GitHubRepositoryClient
→ external acquisition truth + provider admission

RepositoryTextFile / UnavailableRepositoryFile
→ intrinsic exact locator/content state

dependency/analysis.py
→ PR source admission + exact base/head orchestration + source-context rebinding

uv_lock.py / pyproject.py
→ source-format semantics

uv_membership.py
→ independently justified dependency/workflow/project/lock composition joins

target/artifact_environment.py
→ bounded Target workflow semantics + minimal source provenance

target/python.py
→ exact pyproject.toml requires-python semantics

upstream tagged-changelog chain
→ exact immutable source + bounded semantic source window

investigation.py
→ cross-object application sequencing and exact PR/target identity binding

CLI / tests / tools
→ consume product contracts; they do not enlarge evidence contracts for convenience
```

Final reduced dependency source provenance:

```text
DependencyChangeSourceEvidence
├── path
├── file_format
└── extraction_method
```

Final Target Python evidence:

```text
TargetPythonDeclaration
├── path
├── revision
└── requires_python
```

Final tagged changelog evidence:

```text
TaggedChangelogEvidence
├── repository
├── interval
├── resolved_commit_sha
├── path
└── content
```

## 4. Gate A — migration branch acceptance

Tested commit before main reconciliation:

```text
bd30c001b8d20459f6bd3f854b72582b477f7e1b
```

Local environment:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Observed results:

```text
structural contract assertions               PASS
focused R1 regression suite                  272 tests / OK
experiment suite                              27 tests / OK
compileall src/tests/tools/experiments       PASS
complete standard suite                      502 tests / OK
```

This superseded the earlier pre-fix `507 tests / 5 failures / 51 errors` inventory.

## 5. Main reconciliation

Current `main` at reconciliation:

```text
6095aa124cd5b6f02f74cc555e7d273a7acc58cc
```

R1 tested parent:

```text
bd30c001b8d20459f6bd3f854b72582b477f7e1b
```

Two-parent reconciliation merge:

```text
01bc1c2f7b41d60037f0bff6572a0827a51657c0
```

Tree-level comparison established that the net main-side governance/plan content was already represented in the R1 tree. The merge therefore joined histories without replacing the accepted R1 product content.

No force update, rebase, reset, or second migration branch was used.

## 6. Gate B — reconciled branch acceptance

After reconciliation and state-only documentation updates, the exact tested reconciled branch commit was:

```text
9fb19dd483f568a459a0680527a8b00683334359
```

User local runtime results:

```text
complete standard suite    502 tests / OK
experiment suite            27 tests / OK
```

## 7. Promotion to main

`main` was fast-forwarded non-destructively to the exact Gate-B-tested commit:

```text
9fb19dd483f568a459a0680527a8b00683334359
```

Immediately after promotion GitHub comparison reported:

```text
main == agent/r1-exact-file-contract-migration
status: identical
ahead_by: 0
behind_by: 0
```

No additional executable change occurred between Gate-B validation and promotion.

Therefore a second 502+27 run solely under the `main` ref name is not a distinct runtime proposition: Git ref names do not alter the commit/tree. The exact executable tree validated on the reconciled branch is the exact tree promoted to `main`.

## 8. Completion evidence boundary

The accepted executable/runtime authority for R1 is:

```text
9fb19dd483f568a459a0680527a8b00683334359
standard suite: 502 tests / OK
experiment suite: 27 tests / OK
```

Any commits after that SHA which only record R1 completion/live state are documentation-only closure commits. They do not supersede the executable acceptance SHA and do not require re-running the executable suite unless they also change executable/test/tool/experiment content.

## 9. R1 completion criteria disposition

```text
static ownership audit valid                         PASS
migration branch focused/full runtime                PASS
current main absorbed into same R1 branch            PASS
reconciled branch runtime                            PASS
exact validated tree promoted to main                PASS
main and R1 ref identity at promotion                PASS
R1 completion evidence recorded                      PASS
```

R1 is therefore **COMPLETE**.

## 10. Explicitly not solved by R1

The following remain later reconciliation responsibilities:

```text
duplicate uv.lock structural parsers
versionless-record drift between transition/reachability models
--all-packages workspace scope loss
membership naming/proposition breadth
bounded selected-root reachability redesign
later CI rebinding to reconciled reachability evidence
```

These belong to R2–R5 and must not be retroactively attributed to R1.

## 11. Next plan position

```text
R0 COMPLETE
R1 COMPLETE
R2 NOT STARTED
```

Next bounded step is R2: introduce one bounded uv-specific structural lock model, beginning with the demonstrated duplicate-parser/versionless-record drift and preserving the separation between structural parsing and semantic consumers.

The dedicated B2 learning package remains paused while the reconciliation plan continues. AUDIT-005 / the B2 agentic checkpoint remains SCHEDULED for the post-R7 trigger; it is not activated by R1 completion alone.
