# Career Authority Snapshot

This directory preserves the active UpgradePilot control package from the canonical [motafegh/Career](https://github.com/motafegh/Career) repository so the implementation checkout carries enough context to operate safely and coherently.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `b226bd50ef94685166b1660da4320eabb12bbe13`
- Source commit date: `2026-07-19T03:07:21+03:30`
- Snapshot prepared: `2026-07-19`
- Exact mirrored paths: [FILES.txt](FILES.txt)

The files under `career/` are copied without content changes and retain their original relative layout so internal links continue to work.

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

- the governing charter and repository instructions;
- execution, learning, security, and scope controls;
- retained learning-fit, selection, capability, and advanced-systems specifications;
- the controlling 90-day roadmap and milestone plan;
- the active first-session and daily operating plans;
- the active tracker and session/blocker protocol.

## Intentionally excluded

The snapshot excludes AegisLab master, monthly, weekly, current-week, and daily execution routes; historical reporting templates; legacy trackers; and historical daily/weekly records. Career marks those materials as deferred, historical, or non-controlling for UpgradePilot.

## Verify a refreshed snapshot

From the UpgradePilot repository root, after checking out the recorded source commit into a temporary directory:

```bash
while IFS= read -r file; do
  cmp --silent "/path/to/Career/$file" "docs/program/career/$file" \
    || echo "DIFF: $file"
done < docs/program/FILES.txt
```

No output means every listed file is byte-for-byte identical. Also confirm that every file below `docs/program/career/` is listed in `FILES.txt`.
