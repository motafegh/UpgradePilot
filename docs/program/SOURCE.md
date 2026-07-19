# Career Authority Snapshot

This directory preserves the active UpgradePilot control package from the canonical [motafegh/Career](https://github.com/motafegh/Career) repository so the project checkout carries enough context to operate safely and coherently.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `e5284dc1b2e365d32cc8c9b9a44b83d8760c6daa`
- Source commit date: `2026-07-19`
- Snapshot prepared: `2026-07-19`
- Exact mirrored paths: [FILES.txt](FILES.txt)

The files under `career/` are copied without content changes and retain their original relative layout so internal links continue to work.

This refresh advances the local snapshot through M1 closure, the M2-entry architecture-status audit, and approval of M2-S01 as the controlling next technical session.

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
- active tracker and session/blocker protocol.

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

For the 2026-07-19 M2-S01 activation refresh, the paths changed from the prior snapshot were:

- `README.md`;
- `AGENTS.md`;
- `governance/EXECUTION_CONTRACT.md`;
- `strategy/STRATEGY_AND_SCOPE.md`;
- `plans/DAILY_OPERATING_PLAN.md`;
- `plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md` — newly mirrored;
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`.

All listed paths now correspond to canonical Career source commit `e5284dc1b2e365d32cc8c9b9a44b83d8760c6daa`.