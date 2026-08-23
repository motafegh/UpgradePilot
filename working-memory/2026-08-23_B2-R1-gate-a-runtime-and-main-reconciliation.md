# B2 R1 Gate A Runtime Acceptance and Main Reconciliation

**Date:** 2026-08-23  
**Branch:** `agent/r1-exact-file-contract-migration`  
**Plan:** `plans/B2_SOURCE_EVIDENCE_AND_UV_REACHABILITY_RECONCILIATION_PLAN.md`  
**Status:** GATE A GREEN; CURRENT MAIN RECONCILED; GATE B RUNTIME VALIDATION PENDING

## 1. Gate A — migration branch runtime acceptance

The migration branch was updated locally to exact remote commit:

```text
bd30c001b8d20459f6bd3f854b72582b477f7e1b
```

Environment:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Observed results:

```text
R1 structural contract assertions
→ PASS

accumulated focused R1 regression suite
→ 272 tests / OK

experiment regression suite
→ 27 tests / OK

compileall src + tests + tools + experiments
→ PASS

complete standard suite
→ 502 tests / OK
```

This supersedes the earlier pre-fix `507 tests / 5 failures / 51 errors` inventory as the current migration-branch runtime evidence.

Gate A therefore establishes that the completed R1 contract migration is internally runtime-green before `main` reconciliation.

## 2. Current main reconciliation

At reconciliation time:

```text
main
→ 6095aa124cd5b6f02f74cc555e7d273a7acc58cc

R1 migration
→ bd30c001b8d20459f6bd3f854b72582b477f7e1b
```

The original divergence was historical rather than a surviving product-tree conflict. Tree-level inspection established:

- `AGENTS.md`, `MEMORY.md`, and `OPERATING_GUIDE.md` were identical;
- the complete `audits/` subtree was identical;
- the complete `docs/` subtree was identical;
- the complete `plans/` subtree was identical;
- the main-side R1 static-closure working-memory record existed on the R1 branch with the same blob;
- main had no surviving product-source/test/tool changes beyond the original R1 merge base that were absent from the migration tree.

Therefore the correct merge content was the already-tested R1 tree. A two-parent, non-force merge commit was created:

```text
01bc1c2f7b41d60037f0bff6572a0827a51657c0

parent 1: bd30c001b8d20459f6bd3f854b72582b477f7e1b
parent 2: 6095aa124cd5b6f02f74cc555e7d273a7acc58cc
```

The branch ref was advanced normally (no force, no rebase, no second migration branch).

Post-merge GitHub comparison:

```text
base: main
head: agent/r1-exact-file-contract-migration
status: ahead
behind_by: 0
```

So current `main` is now an ancestor of the R1 branch.

## 3. What Gate B must prove

Because the merge commit preserves the already-tested R1 product tree, Gate B is not another architectural migration. It is integration/runtime confirmation that the exact reconciled branch remains executable after joining histories and after the state-only documentation updates that follow this record.

Required local proof:

```text
pull exact current R1 branch
→ complete standard test suite
→ experiment test suite
```

If both are green, the reconciled branch becomes the R1 acceptance candidate for promotion to `main`.

## 4. Learning checkpoint

Important distinction:

```text
Git histories diverged
!= current file contents conflict
```

Git commit ancestry and repository tree content are separate dimensions.

Here, governance changes had been promoted independently to both histories, so the correct reconciliation was a content-preserving merge commit whose purpose is to join ancestry rather than invent a new combined implementation.

Likewise:

```text
merge commit exists
!= integrated tree is accepted
```

Runtime validation after reconciliation is still required before promoting the branch to `main` and declaring R1 complete.
