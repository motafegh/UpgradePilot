# Career Authority Snapshot

This directory preserves the active UpgradePilot control package from the canonical [motafegh/Career](https://github.com/motafegh/Career) repository so the project checkout carries enough context to operate safely and coherently.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `d1cafdfd61c1b03b291e6cd196e06480be950087`
- Source commit date: `2026-07-20`
- Snapshot prepared: `2026-07-20`
- Exact mirrored paths: [FILES.txt](FILES.txt)

The files under `career/` are copied without content changes and retain their original relative layout so internal links continue to work.

This refresh preserves the approved M2-S01 state and clarifies that Career's UpgradePilot evidence and progress tracker is the single general product-progress and capability tracker. UpgradePilot may create only distinct technical inventories that do not duplicate it.

The canonical M1 evidence report is intentionally not duplicated because `tracking/evidence/` remains outside the mirrored path list. The tracker and Career README link to the canonical report.

## Authority rule

The remote Career repository remains canonical. This snapshot is read-only convenience context.

When the two differ:

1. do not reconcile by guessing;
2. inspect the canonical Career commit and current tracker;
3. apply governance or tracker updates in Career first;
4. refresh this snapshot from one reviewed source commit;
5. update this file and verify the complete mirrored file set.

Do not hand-edit a mirrored file to create a local policy fork.

## Included

The snapshot includes:

- governing charter and repository instructions;
- execution, learning, security, and scope controls;
- retained learning-fit, selection, capability, and advanced-systems specifications;
- controlling roadmap and milestone plan;
- completed M1 session plan;
- controlling M2-S01 session plan;
- daily operating plan;
- canonical tracker and session/blocker protocol.

## Intentionally excluded

The snapshot excludes AegisLab master, monthly, weekly, current-week, and daily execution routes; historical reporting templates; legacy trackers; and historical daily/weekly records. Career marks those materials as deferred, historical, or non-controlling for UpgradePilot.

The canonical evidence report at `Career/tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md` is also excluded because `tracking/evidence/` is not part of the fixed mirrored file list.

## Verify a refreshed snapshot

From the UpgradePilot repository root, after checking out the recorded source commit into a temporary directory:

```bash
while IFS= read -r file; do
  cmp --silent "/path/to/Career/$file" "docs/program/career/$file" \
    || echo "DIFF: $file"
done < docs/program/FILES.txt
```

No output means every listed file is byte-for-byte identical. Also confirm that every file below `docs/program/career/` is listed in `FILES.txt`.

For the 2026-07-20 tracker-ownership refresh, the path changed from the prior snapshot was:

- `README.md`.

All listed paths now correspond to canonical Career source commit `d1cafdfd61c1b03b291e6cd196e06480be950087`.
