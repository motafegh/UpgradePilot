# Career Authority Snapshot

This directory preserves a reviewed point-in-time control package from the canonical `motafegh/Career` repository so an UpgradePilot checkout has sufficient local context for safe operation.

It is **not** a live mirror and must not be refreshed after every session, test, implementation sub-gate, or exact-next-action change.

## Snapshot identity

- Source repository: `https://github.com/motafegh/Career.git`
- Source branch: `main`
- Source commit: `152f4c31bf5bb2fb6af08806a4f16c7408787c49`
- Source commit date: `2026-07-21`
- Snapshot prepared: `2026-07-21`
- Exact mirrored paths: [`FILES.txt`](FILES.txt)

Files under `career/` are copied without content changes and retain the canonical relative layout so internal links remain meaningful.

## Refresh purpose

This refresh records the approved specification/governance responsibility refactor:

- Career README and `AGENTS.md` route live state to the canonical tracker rather than duplicating session details;
- Strategy and Scope owns stable identity, allocation, priorities, evidence expectations, and the unchanged advanced-systems strategy;
- the Learning and Execution Contract owns reusable Ali–AI execution and control-transfer rules;
- Learning Preferences owns teaching presentation and interaction style;
- the Session and Blocker Protocol owns lightweight, standard, and formal sessions plus decision/exploration/execution/tangent and blocker procedures;
- the 90-Day Execution Contract owns stable workload, capacity, reviews, and anti-diversion commitments;
- the Capability Specification owns atomic D0–D5 evidence, ownership dimensions, prerequisites, and claim limits;
- the tracker owns current program/capability state without becoming a full transcript;
- `operations/SESSION_PROTOCOL.md` remains only a compatibility route to the canonical governance protocol.

The accepted Day-90 advanced-systems strategy, capacity, exposure targets, adoption rules, roadmap allocation, and completion requirements were intentionally not changed.

## Snapshot nature and canonical precedence

The remote Career repository remains canonical whenever available.

When canonical Career and this snapshot differ:

1. do not reconcile by guessing or hand-editing mirrored files;
2. inspect canonical Career and its tracker;
3. apply any governance/state correction in Career first;
4. decide whether a refresh trigger is met;
5. refresh from one reviewed canonical commit;
6. verify the complete listed file set.

The snapshot must state its source commit and age clearly. Newer local timestamps do not override canonical authority.

## Refresh triggers

Refresh only when one of these occurs:

- a milestone transition;
- a formal program review;
- a material governance change that affects UpgradePilot operation;
- the local snapshot would otherwise be materially misleading for continued work;
- an explicit manual refresh request.

Do not refresh merely because:

- one test changes or passes;
- one session ends;
- the exact next action changes;
- one implementation sub-gate passes;
- one working-memory entry changes;
- one non-governing document is edited.

During a multi-commit Career refactor, refresh once from the final reviewed canonical commit rather than after each intermediate commit.

## Responsibility boundary

Career remains responsible for:

- program authorization and route;
- workload/capacity and review commitments;
- milestone gates;
- capability/ownership rules and canonical state.

UpgradePilot remains responsible for:

- project-level technical specifications;
- accepted ADRs;
- project-local plans after authorization;
- source, tests, working memory, learning artifacts, and project evidence.

This source record owns only snapshot origin, refresh policy, and verification. It is not a tracker or exact-next-action record.

## Included and excluded

The snapshot includes only paths listed in `FILES.txt`.

It intentionally excludes:

- AegisLab execution routes and historical operational records not needed by UpgradePilot;
- full `tracking/evidence/` content;
- private or sensitive evaluator context;
- unlisted Career files.

The canonical M1 evidence report remains in Career and is referenced through the canonical tracker.

## Verification

Changed or newly included canonical/mirrored content blob SHAs:

```text
README.md
1b4b5a8856e10cf5a3f4653688d92efd8adc8b51

AGENTS.md
c7da4a5f70f6f7f0f01dd25649bb6be46a189998

governance/90_DAY_EXECUTION_CONTRACT.md
61eef7685bb2bfa1e0749da975d684db0ac3a434

governance/SESSION_AND_BLOCKER_PROTOCOL.md
3860f33a8bcaa5fcd77c87c58dc1a39f4b3fa891

governance/UPGRADEPILOT_LEARNING_AND_EXECUTION_CONTRACT.md
fc6797e6b6076ce2db2e44fde9915c03b14f03d8

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

All other paths listed in `FILES.txt` were selected from the same canonical source commit and were not substantively changed by this refactor.

For a local byte-for-byte verification after checking out the recorded Career commit:

```bash
while IFS= read -r file; do
  cmp --silent "/path/to/Career/$file" "docs/program/career/$file" \
    || echo "DIFF: $file"
done < docs/program/FILES.txt
```

No output means every listed file is byte-for-byte identical. Also confirm that every file under `docs/program/career/` is listed in `FILES.txt`.

## Future maintenance

A lightweight copy/verification script MAY be added only if it reduces manual work without turning the snapshot into a live synchronization requirement.

Do not place current milestone details, exact next actions, session evidence, or technical implementation status in this file.