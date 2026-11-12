# AV-Tracer PR #11 saved investigations

[Download the reviewed archive](av-tracer-pr-11.zip) to inspect both UpgradePilot captures of AV-Tracer PR #11, which proposed updating HTTPX from `0.25.2` to `0.28.1`. Each capture includes the exact saved `report.json` and main SQLite database. The archive also includes upstream licenses and notices and a `SHA256SUMS` file. The original local captures remain in the owner’s evidence store.

| Capture | Confirmed Workspace revision | What to inspect |
| --- | --- | --- |
| `source-only` | `80a58d494a8c46009aab8dc72b94b447` | Conditional comparison of the `app` keyword. `source-29` shows Starlette forwarding it. |
| `source-and-ci` | `b2a491b4b7864342b920fe51a0694f4c` | The same source comparison and the selected historical job observation. `source-48` shows the retained TypeError. |

The [source-only receipt](../../working-memory/evidence/2026-11-11-av-tracer-exact-version-allocation/qualification.json) and [combined receipt](../../working-memory/evidence/2026-11-12-av-tracer-native-ci/qualification.json) bind the saved report digests to the original qualifications. The archive SHA-256 is `ffb9365e034833ce4ba3cd35be2080b099d331271b76214e241e6d3a8e115990`.

## Open offline

From a checkout with UpgradePilot’s Python environment set up, extract the archive into an owner-only directory outside Git. The Workspace reader requires that location and ownership for both live and read-only stores.

```bash
capture_dir=$(mktemp -d /tmp/upgradepilot-av-tracer.XXXXXXXX)
(umask 077 && .venv/bin/python -m zipfile -e examples/av-tracer/av-tracer-pr-11.zip "$capture_dir")
(cd "$capture_dir" && sha256sum -c SHA256SUMS)

PYTHONPATH=src .venv/bin/python -m upgradepilot \
  --open-report "$capture_dir/source-only/report.json"

PYTHONPATH=src .venv/bin/python -m upgradepilot \
  --open-workspace "$capture_dir/source-and-ci/workspace" \
  --revision b2a491b4b7864342b920fe51a0694f4c \
  --show-source source-48
```

Remove `--show-source source-48` to see the complete combined report. The same commands work with the other capture’s path and revision from the table. The SQLite files are self-contained copies of the checkpointed databases. SQLite can create its own sidecars in the extracted directories when opened.

The source comparison is conditional. The combined report preserves an exact-job text observation and the same-job installation token. Loaded-module identity, upgrade causality and whole-workflow causality remain open. The saved action is `abstain`. The archive retains the selected CI excerpt and the full-log digest. The original full job log was transient during acquisition. [Live verification record](../../working-memory/2026-11-12_ci_job_diagnostic_native_bridge_build-cycle.md#live-combined-verification-and-d-handoff)

## Upstream source and notices

The two reports embed the same 24 retained source files. Their contents were verified against the exact upstream revisions below. The archive’s `licenses/` directory preserves the corresponding license and notice texts. The captures also retain the already public PR identity and UpgradePilot’s recorded worker module path.

| Project | Captured version or revision | License and notice |
| --- | --- | --- |
| AV-Tracer | `25e7205f39103456e7efbc4e9f503f3debc7b5d8` | [Apache-2.0](https://github.com/ivaronkun-Ahey/AV-Tracer/blob/25e7205f39103456e7efbc4e9f503f3debc7b5d8/LICENSE), [NOTICE](https://github.com/ivaronkun-Ahey/AV-Tracer/blob/25e7205f39103456e7efbc4e9f503f3debc7b5d8/NOTICE), [third-party notices](https://github.com/ivaronkun-Ahey/AV-Tracer/blob/25e7205f39103456e7efbc4e9f503f3debc7b5d8/THIRD_PARTY_NOTICES.md) |
| FastAPI | `0.104.1` | [MIT](https://github.com/fastapi/fastapi/blob/7e5afe2cb9bf1fa30c04a4dd393ea397a46db29b/LICENSE) |
| Starlette | `0.27.0` | [BSD-3-Clause](https://github.com/Kludex/starlette/blob/0c4b68ac4e179a788e38bac28f299dcad0f36e99/LICENSE.md) |
| HTTPX | `0.25.2` and `0.28.1` | [BSD-3-Clause at 0.25.2](https://github.com/encode/httpx/blob/cc206cf2dad42600479962ac1daaa44675cfaf56/LICENSE.md), [identical text at 0.28.1](https://github.com/encode/httpx/blob/26d48e0634e6ee9cdc0533996db289ce4b430177/LICENSE.md) |
