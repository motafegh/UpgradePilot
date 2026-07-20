# Career Authority Snapshot

This directory preserves the active UpgradePilot control package from the canonical `motafegh/Career` repository so the project checkout carries enough context to operate safely and coherently.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `57ae78fece2e05d97bd0f52e76bf1fdb5b54d6e4`
- Source commit date: `2026-07-21`
- Snapshot prepared: `2026-07-21`
- Exact mirrored paths: [FILES.txt](FILES.txt)

The files under `career/` are copied without content changes and retain their original relative layout so internal links continue to work.

This refresh records the M2 technical-contract correction:

- the original M2-S01 plan remains controlling;
- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` supersedes conflicting M2 wording;
- UpgradePilot's core pipeline and contract specification now controls the conceptual pipeline, information boundaries, invariants, evidence states, M2 activation, and method-selection criteria;
- the original eight-field “case identity” is corrected into PR snapshot identity, dependency change, changed-file evidence, and an aggregate initial case record;
- no representation framework, runtime dependency, source implementation, tests, or executable behavior is accepted yet;
- the exact next action is representation-method comparison and decision before test-first implementation resumes.

Career remains responsible for program authorization, sequence, capacity, gates, and capability tracking. UpgradePilot remains responsible for project-level technical specifications, accepted architecture decisions, project-local plans after authorization, working memory, learning artifacts, implementation, tests, and project evidence.

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
- controlling active M2-S01 session plan;
- controlling M2-S01 technical-contract amendment;
- daily operating plan;
- canonical tracker and Session Protocol.

## Intentionally excluded

The snapshot excludes AegisLab master, monthly, weekly, current-week, and daily execution routes; historical reporting templates; legacy trackers; and historical daily/weekly records. Career marks those materials as deferred, historical, or non-controlling for UpgradePilot.

The canonical evidence report at `Career/tracking/evidence/UP-S01_pydantic-13432_manual-evidence-report.md` is also excluded because `tracking/evidence/` is not part of the fixed mirrored file list.

## Verification

Canonical and mirrored content blob SHAs for changed files are:

```text
README.md
971ba09b5ce671b4c1cb87bc5dc65ddd7580e62b

AGENTS.md
990684264f4d38b7064213b46c51608ae2fc5553

tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md
0bb38ea5ae43fe289b89ab764be3cd3b256cba57
```

The amendment was created in both repositories from identical content and is included in `FILES.txt`.

For a local byte-for-byte verification, after checking out the recorded Career source commit into a temporary directory, run from the UpgradePilot repository root:

```bash
while IFS= read -r file; do
  cmp --silent "/path/to/Career/$file" "docs/program/career/$file" \
    || echo "DIFF: $file"
done < docs/program/FILES.txt
```

No output means every listed file is byte-for-byte identical. Also confirm that every file below `docs/program/career/` is listed in `FILES.txt`.

## Changed paths in this refresh

- `README.md`;
- `AGENTS.md`;
- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md`;
- `tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md`.

All listed paths correspond to canonical Career source commit `57ae78fece2e05d97bd0f52e76bf1fdb5b54d6e4`.
