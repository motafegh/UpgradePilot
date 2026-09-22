# uv resolution-marker order reality check — Thumbor #1895

**Date:** 2026-09-22
**Kind:** Non-controlling Product Simulation forward-pressure research.

## Question

Can a real uv Dependabot update be blocked by current UpgradePilot transition extraction because unrelated repeated-package `resolution-markers` lists are serialized in a different order?

## Real case

Repository: `thumbor/thumbor`

PR `#1895`: Dependabot `pylint 4.0.7 → 4.0.8`.

- base: `7f8637ee599322a0e1f99d91ba3ee71c457c6d7c`
- head: `806520c717e5edb6e4b0d187bb592994725a393e`
- changed file: `uv.lock` only

Direct base/head inspection shows the expected pylint transition plus order-only changes inside `resolution-markers` lists for repeated records of:

- `docutils`
- `numpy`
- `pywavelets`
- `scipy`

For each inspected changed record, the marker strings are the same members; their serialized list order differs.

Example shape:

base:

```text
A
B
C
D
```

head:

```text
A
C
B
D
```

## Current UpgradePilot projection

`src/upgradepilot/dependency/uv_lock.py` currently:

1. compares repeated package records as an order-independent multiset of canonical records;
2. but `_canonical_record` freezes nested lists with list order preserved;
3. therefore reordering `resolution-markers` inside one repeated record changes that record's canonical value;
4. a changed repeated group returns `ambiguous_uv_lock_package_records` before later package transitions are accepted.

Because package names are traversed in sorted order, the changed repeated `docutils` group is encountered before `pylint`.

Therefore, by direct source tracing, current extraction of this proposal is expected to stop with `ambiguous_uv_lock_package_records` rather than emit the otherwise visible pylint transition.

## Why this is not yet classified as a product bug

Do **not** assume `resolution-markers` list order is semantically irrelevant merely because the marker membership is unchanged.

uv's resolver documentation explains that saved `resolution-markers` preserve fork structure so later resolution remains stable. Current uv changelog also records behavior specifically concerning ordering forks created from existing lockfile `resolution-markers` and `fork-strategy`.

Therefore the safe current conclusion is:

`real order-only marker serialization change` + `current UpgradePilot rejects it`

not:

`UpgradePilot should sort/normalize those lists`.

That normalization requires stronger proof that list order can be discarded for UpgradePilot's transition identity without collapsing meaningful fork context.

## Reality-check value

This case is useful because it cuts both ways:

- it demonstrates a real source-acquisition limitation rather than a synthetic counterexample;
- but it also warns against 'fixing' the limitation by normalizing a field whose ordering may carry resolver meaning.

The appropriate next step, only if this limitation becomes decision-relevant, is a bounded semantic investigation of uv fork identity/order rather than immediate implementation.

## Relationship to S016

S016 uses Thumbor #1867 because that proposal cleanly validates current lock-transition plus selector/reachability architecture.

PR #1895 is intentionally kept separate because its question is upstream:

`can the exact transition be admitted at all when unrelated repeated resolution-marker records reorder?`

Mixing the two would obscure both conclusions.

## Status

**Observed-real acquisition limitation; semantic normalization unresolved.**

No scenario number is assigned yet and no source change is authorized.