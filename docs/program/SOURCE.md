# Career Authority Snapshot

This directory preserves a reviewed point-in-time control package from the canonical `motafegh/Career` repository so an UpgradePilot checkout has sufficient local context for safe operation.

It is **not** a live mirror and must not be refreshed after every session, test, implementation sub-gate, or exact-next-action change.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `49244d5aa32769ffe25b90ba8927efc22b32f4c1`
- Source commit date: `2026-07-21`
- Snapshot prepared: `2026-07-21`
- Exact mirrored paths: [`FILES.txt`](FILES.txt)

Files under `career/` are copied without content changes and retain the canonical relative layout so internal links remain meaningful.

## Refresh purpose

This refresh records completion of the non-strategic specification/governance responsibility refactor:

- `governance/90_DAY_EXECUTION_CONTRACT.md` is the single canonical execution contract;
- `governance/EXECUTION_CONTRACT.md` is a compatibility route only;
- Career README and `AGENTS.md` route live state to the canonical tracker;
- the UpgradePilot charter owns stable mission, product boundary, outcomes, evidence doctrine, admission rules, termination rules, and claim limits;
- the master roadmap owns route order, dates, capacity, reviews, fallbacks, forbidden scope, and Day-90 requirements without live status;
- the milestone plan owns normative milestone requirements and advancement without results or exact next actions;
- M2-S01 plan and amendment own bounded requirements, proof, and stop lines while the tracker/working memory own current completion state;
- the Learning and Execution Contract owns reusable Ali–AI execution and control-transfer rules;
- Learning Preferences owns teaching presentation and interaction style;
- the Session and Blocker Protocol owns proportional sessions and blocker/prerequisite procedures;
- the Capability Specification owns D0–D5 evidence, ownership dimensions, prerequisites, and claim limits;
- the tracker owns current program/capability state without becoming a transcript;
- `operations/SESSION_PROTOCOL.md` remains only a compatibility route.

The accepted Day-90 advanced-systems strategy, capacities, A1/A2 targets, roadmap allocation, adoption rules, and completion requirements were intentionally not changed.

## Snapshot nature and canonical precedence

The remote Career repository remains canonical whenever available.

When canonical Career and this snapshot differ:

1. do not reconcile by guessing or hand-editing mirrored files;
2. inspect canonical Career and its tracker;
3. apply governance or state corrections in Career first;
4. determine whether a refresh trigger is met;
5. refresh from one reviewed canonical commit;
6. verify the complete listed file set.

Refresh only for:

- a milestone transition;
- a formal program review;
- a material governance change affecting UpgradePilot operation;
- a materially misleading local snapshot;
- an explicit manual refresh request.

Do not refresh merely because one test passes, one session ends, an exact next action changes, one implementation sub-gate passes, or one working-memory record changes.

## Responsibility boundary

Career remains responsible for program authorization, route, capacity, review commitments, milestone gates, capability/ownership rules, and canonical state.

UpgradePilot remains responsible for project-level specifications, accepted ADRs, project-local plans, source, tests, working memory, learning artifacts, and project evidence.

This file owns snapshot origin, refresh policy, and verification only. It is not a tracker or next-action record.

## Included and excluded

The snapshot includes only paths listed in `FILES.txt`.

It intentionally excludes AegisLab execution routes and unnecessary historical operations, full `tracking/evidence/` content, private/sensitive evaluator context, and unlisted Career files.

## Verification

Changed canonical/mirrored blob SHAs:

```text
README.md
af83fa0bc5f6314d1c1beafa866326163e0e2019

AGENTS.md
961c7d9ae5e61b6445f4d4cab0f2f077b517da61

UpgradePilot.md
201f797a68d3d20e6984acf04bde970287cd79a6

governance/EXECUTION_CONTRACT.md
a91bb63e7c0a16e904941556c12b80e223e2466e

governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md
ec517342dbfdb8630c473a651d47659c80914baf

plans/UPGRADEPILOT_90_DAY_MASTER_ROADMAP.md
92904c41892217ad432c9ec79398b95886b4668a

plans/UPGRADEPILOT_STAGED_MILESTONE_PLAN.md
a9d76e616d40c6dd7915d7f381a887f9232c5e17

plans/UPGRADEPILOT_M2_FIRST_SESSION_PLAN.md
0a8ba5b63dcd0f2ca37fd07d3aa60faf2eb68d3f

plans/UPGRADEPILOT_M2_S01_TECHNICAL_CONTRACT_AMENDMENT.md
2fae4be6089ce1d196eff626ce1b4af519f55d6d
```

Unchanged but previously verified canonical controls include:

```text
governance/90_DAY_EXECUTION_CONTRACT.md
61eef7685bb2bfa1e0749da975d684db0ac3a434

governance/SESSION_AND_BLOCKER_PROTOCOL.md
3860f33a8bcaa5fcd77c87c58dc1a39f4b3fa891

governance/UPGRADEPILOT_LEARNING_PREFERENCES.md
ecac7a8ae9ef6cf891a07bfac20327d628c83d0a

strategy/STRATEGY_AND_SCOPE.md
6bd70f86b723c2c7757c941c24208fc7c35d5157

strategy/UPGRADEPILOT_CAPABILITY_AND_PREREQUISITE_SPECIFICATION.md
83ef84fdfb45c072645f3d495e35dbd9b917c4b5

operations/SESSION_PROTOCOL.md
c731bfee21cf841c4db318c0c4ded4a2cef367bb

tracking/UPGRADEPILOT_EVIDENCE_AND_PROGRESS_TRACKER.md
d672b768fa6c0d1b856231e98aa42e15f82bd2d5
```

For a local byte-for-byte verification after checking out the recorded Career commit:

```bash
while IFS= read -r file; do
  cmp --silent "/path/to/Career/$file" "docs/program/career/$file" \
    || echo "DIFF: $file"
done < docs/program/FILES.txt
```

No output means every listed file is byte-for-byte identical.

## Future maintenance

A lightweight copy/verification script MAY be added only when it reduces manual work without creating a live synchronization requirement.

Do not place current milestone details, exact next actions, session evidence, or technical implementation status in this file.
