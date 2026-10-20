# FCI offline replay verification

Verification date: 2026-10-20. Latest verification supersedes the earlier same-day replay record where source copies were checked only against their own manifest/Git identities rather than against the frozen upstream source Git identities.

## Final result

`PASS` for the corrected retained three-case cohort with no target-repository API values required during replay.

A separate Python process re-read a materialized mirror of the corrected retained case bytes and verified:

- every manifest-declared retained artifact exists;
- byte size and SHA-256 match;
- retained Git blob identity matches where recorded;
- provider-exact source overlays match the **frozen upstream Git blob identity** recorded in the manifest;
- authoritative dependency-transition artifacts are provider-exact and are not known flawed first reconstructions;
- retained PR number/base/head match the frozen case identity;
- selected run ID, attempt, head SHA and workflow path match the manifest;
- retained jobs belong to the selected run;
- step-state distinctions survive replay without normalization;
- FCI002 retains `static_job_name_missing` as the first expected current-owner correlation refusal and the later matrix as a secondary unsupported shape.

Corrected fresh-process result:

```json
{
  "status": "pass",
  "network_required": false,
  "cases": [
    {
      "case_id": "FCI001",
      "artifact_count": 5,
      "job_count": 1,
      "step_states": ["non_empty_array"],
      "qualification": "qualified_for_current_ci_diagnostic"
    },
    {
      "case_id": "FCI002",
      "artifact_count": 9,
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

The committed `verify_bundle.py` is network-free and now checks any recorded `upstream_git_blob_sha1` in addition to retained-file size/SHA-256/Git identity. It also encodes FCI002's corrected first-refusal semantics.

## Durable provider/source identity cross-check

Provider-exact dependency-transition diffs:

- FCI001: blob `a346589e412bf2d3df29e4bc0b08ba40a4740b13`, 3159 bytes;
- FCI002: blob `24e463d1743e1090bee2d7625ed2b22fa49bbaeb`, 238 bytes;
- FCI003: blob `00e77bcd80bfddcf1df5f45c961e68c84b123d99`, 2499 bytes.

Provider-exact source overlays added by the later fidelity audit:

- FCI001 workflow: `fb2110166d4df410cea5f181d0e75a55b92824a4`, 1190 bytes — identical to the frozen upstream workflow Git blob;
- FCI002 workflow: `9643a4ea975e7182c548e4bc8e94accb93aa0056`, 4354 bytes — identical to the frozen upstream workflow Git blob;
- FCI002 base requirements: `994653111f7abfd53b8e4e0f932a1696dcf87189`, 79 bytes — identical to the frozen upstream base Git blob;
- FCI002 head requirements: `b6afd3da9c4d83bbf7c82b2c1e9c7d900c03b790`, 79 bytes — identical to the frozen upstream head Git blob.

FCI003's retained workflow/base/head source files were already byte-identical to their frozen upstream Git blobs and needed no source-byte overlay.

## Failures found and repaired during verification

Two separate retention defects were found in the **cohort construction procedure**, not in `src/upgradepilot/`:

1. The first persisted PR-diff reconstructions for FCI001 and FCI003 inserted ASCII spaces on otherwise blank diff-context lines. Those files were preserved and marked non-authoritative; additive `pr.provider-exact.diff` files are authoritative.
2. A later audit found that the first FCI001 workflow copy and first FCI002 workflow/base/head requirements copies had lost their final newline during connector-to-text persistence. They were internally self-consistent, so the first replay passed, but they were not byte-identical to the frozen upstream source. Those files remain immutable/non-authoritative; additive `*.provider-exact.*` source overlays now match the upstream Git objects exactly.

The second defect demonstrates why checking a retained file only against its own stored hash is insufficient for a byte-exact source claim. Upstream Git object identity is now part of the verifier where such an identity is recorded.

## Semantic correction found during audit

FCI002 contains both unnamed static jobs and a later matrix test job. The current correlation owner checks jobs in workflow order. The first `pre-commit` job has no explicit literal display name, so the expected first refusal is `static_job_name_missing`; the matrix is a secondary unsupported property, not the first current-owner result.

## Environment limitation

A literal fresh `git clone` inside the execution container was attempted earlier but failed because that container could not resolve `github.com`. Therefore fresh-process replay uses a materialized mirror of already retained bytes, while durable persistence/upstream source fidelity is checked separately using recorded Git object identities. No current values from the three target repositories are required during replay.

This demonstrates that the corrected retained inputs are self-contained for deterministic offline reread while keeping the unavailable literal network clone explicit.
