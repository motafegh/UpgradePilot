# R2 learning checkpoint — state-witness scope and reuse (2026-09-24)

Status: supporting checkpoint for the ACTIVE `2026-09-24_effective-package-manager-semantics-system-design.md`; not a separate active plan or accepted architecture decision.

## Reasoning clarification

Ali challenged the redundant later-step example: if an earlier command already proves the exact proposed requirement is satisfied in the relevant environment at command completion, why examine subsequent installation commands or inventory reports?

**Answer:** We do not need later evidence for that same bounded claim. Reuse the nearest already sufficient, positively established witness. A dry-run command following the earlier installation does not erase the prior command-completion proof or establish installation itself. A later direct inventory is an independent state-at-observation-time witness and may be useful when earlier command semantics cannot close, when the desired claim concerns the later moment, or when independently observed state is needed. It is not an automatic extra gate for every valid Route A proof.

Keep the distinct propositions explicit:

- `requirement satisfied in environment E at command C completion`;
- `package/version present in environment E at observation time T`;
- `same package/version present in the environment used by later command X`;
- `later command X actually exercised that version`.

Do **not** promote the first or second proposition to the third or fourth without a positive environment/time/continuity and consumption relationship. Investigate intervening commands, mutation, environment changes, and later use only to the extent material to the **requested** later claim; do not scan all intervening steps indiscriminately or presume persistence forever. Missing material relationships stay unresolved.

This reinforces the already accepted proposition-first, demand-driven B4/B5 boundaries in the active record and `2026-09-24_runtime-state-reconciled-design-baseline.md`; it is a clarification, not a new proof contract, new action permission, or Build authorization.

Next R2 focus: review whether candidate Routes A and B can feed appropriately time/environment-scoped state facts without conflating their provenance, and determine the minimum explicit relationships required for a later exercise claim.

UP-SKILL:upgradepilot-working-memory
