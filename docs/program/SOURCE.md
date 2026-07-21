# Career Authority Snapshot

This directory preserves the active UpgradePilot control package from the canonical `motafegh/Career` repository so the project checkout carries enough context to operate safely and coherently.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `d3a1fc2ed63190ccd3f7a2bb43cf71c47bc93e24`
- Source commit date: `2026-07-21`
- Snapshot prepared: `2026-07-21`
- Exact mirrored paths: [FILES.txt](FILES.txt)

The files under `career/` are copied without content changes and retain their original relative layout so internal links continue to work.

## Refresh purpose

This refresh records completion of the M2 representation-method decision:

- the original M2-S01 plan remains controlling;
- `plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md` remains the controlling amendment and now activates the selected method;
- UpgradePilot's core pipeline and contract specification records the conceptual pipeline, boundaries, invariants, evidence states, and activated Pydantic policy;
- UpgradePilot `docs/architecture/ADR-0002-pydantic-runtime-contract-models.md` adopts Pydantic v2 for strict runtime boundary and trusted application contracts;
- raw source data remains separate from validated Pydantic models;
- explicit adapters map flat/source-specific input into nested trusted records;
- application contracts remain separate from persistence records and permanent public report schemas;
- no package metadata, installed runtime dependency, source implementation, tests, import proof, or executable behavior exists yet;
- the exact next action is minimum Pydantic onboarding followed by reviewed package/dependency setup, editable installation/import verification, and the valid nested-contract test first.

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
e77edb6063fea153433a26fe4cf53b31109181b4

AGENTS.md
64c820a149594c3d3289a0faecd2e7dc09428980

plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md
b0633dbb0be2b19b2b924190443db8658be3d9e7

tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md
db4314158be7c167e09e96d59d3534616f407c9a
```

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

All listed paths now correspond to canonical Career source commit `d3a1fc2ed63190ccd3f7a2bb43cf71c47bc93e24`.