# FCI offline replay verification

Verification date: 2026-10-20.

## Result

`PASS` for the retained three-case cohort with no target-repository API values required during replay.

A separate Python process re-read a materialized mirror of the retained case bytes and verified:

- every manifest-declared retained artifact exists;
- byte size and SHA-256 match;
- Git blob identity matches where recorded;
- authoritative dependency-transition artifacts are provider-exact and are not the known flawed first reconstructions;
- retained PR number/base/head match the frozen case identity;
- selected run ID, attempt, head SHA and workflow path match the manifest;
- retained jobs belong to the selected run;
- step-state distinctions survive replay without normalization.

Fresh-process result:

```json
{
  "status": "pass",
  "network_required": false,
  "cases": [
    {
      "case_id": "FCI001",
      "artifact_count": 4,
      "job_count": 1,
      "step_states": ["non_empty_array"],
      "qualification": "qualified_for_current_ci_diagnostic"
    },
    {
      "case_id": "FCI002",
      "artifact_count": 6,
      "job_count": 13,
      "step_states": ["field_absent_or_unavailable", "non_empty_array"],
      "qualification": "qualified_as_unresolved_control"
    },
    {
      "case_id": "FCI003",
      "artifact_count": 7,
      "job_count": 5,
      "step_states": ["non_empty_array"],
      "qualification": "qualified_as_unresolved_control"
    }
  ]
}
```

The committed `verify_bundle.py` performs the same class of offline checks and deliberately contains no network client.

## Durable repository-object cross-check

The raw files were independently re-read through the UpgradePilot repository at commit `008b879f24ed84908ee8e5e9574f372a276e3dd9`. Their Git blob IDs and byte sizes agree with the manifest identities used for replay. In particular:

- FCI001 exact provider diff: blob `a346589e412bf2d3df29e4bc0b08ba40a4740b13`, 3159 bytes;
- FCI002 exact provider diff: blob `24e463d1743e1090bee2d7625ed2b22fa49bbaeb`, 238 bytes;
- FCI003 exact provider diff: blob `00e77bcd80bfddcf1df5f45c961e68c84b123d99`, 2499 bytes.

The other retained provider/source blobs also matched their independently computed Git object identities.

## Failure found and repaired during verification

The first persisted PR-diff reconstructions for FCI001 and FCI003 were not byte-identical to the captured provider strings: manual reconstruction had inserted an ASCII space on three and two otherwise blank diff-context lines respectively. Verification caught this because the persisted byte sizes/Git object IDs disagreed with the precomputed capture identities.

The raw mistake was **not overwritten**. Each flawed `raw/pr.diff` remains immutable and is marked `capture_error_non_authoritative`. Exact additive files named `raw/pr.provider-exact.diff` were then published; their Git object IDs match the original captured provider bytes, and the manifests point to those exact files as authoritative producer input.

FCI002's original `raw/pr.diff` matched exactly and needed no repair.

## Environment limitation

A literal fresh `git clone` inside the execution container was attempted but failed because that container could not resolve `github.com`. Therefore the fresh-process replay used a materialized mirror of the already captured bytes, while durable persistence was checked separately against the UpgradePilot repository's Git object IDs. No current values from the three target repositories were consulted during replay.

This is sufficient to demonstrate that the retained bytes and identities are self-contained for deterministic offline reread, while keeping the inability to perform a literal network clone explicit rather than disguising it.
