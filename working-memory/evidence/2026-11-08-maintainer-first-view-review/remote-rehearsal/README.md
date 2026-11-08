# GitHub checkout AI rehearsal

This handoff rebuilds four exact revision 3 participant views for OpenCV and Soup Sieve from saved JSON already tracked in UpgradePilot. It can also include two views of the published [HTTPX report summary](HTTPX_REPORT.md), with the same detailed text in both and the [opening](HTTPX_OPENING.md) added in one. The original case numbers and assignments are preserved. The generated views are local scratch files.

From the repository root, use a Python 3.12+ environment with UpgradePilot's project dependencies installed:

```sh
mkdir -p .tmp
PYTHONPATH=src python working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/prepare.py .tmp/maintainer-first-view-remote-r3
```

For all three cases, pass `--include-httpx-summary` and use a fresh output directory. The script checks the two exact cases against their saved-input, prompt and view hashes. It reads saved reports offline. A GitHub assistant without a checkout and shell can read the [HTTPX summary](HTTPX_REPORT.md) and use the [saved-report walkthrough](../../2026-11-08-maintainer-report-first-view/REVIEW_PACKET.md) for technical inspection.

The full HTTPX saved report is 3.4 MB and embeds complete third-party files. The target repository is public, but redistribution permission for its captured source was not verified. The [tracked receipt](../receipt.json) records the saved report and original view hashes. The published derivative gives the findings, evidence IDs and pinned source links without bundling the source files. Record this case as a summary-based rehearsal, separate from the byte-exact revision 3 case.

## Reviewer prompts

For slot 1, give a fresh chat only the generated `reviewer-1` folder:

> Read TASK.md and act as a maintainer reviewing Python dependency updates. Use only this folder. Start with 02-opencv. Read its FOCUS.txt and report.txt and submit your answers in your own words. Record any source files you open or places where you get stuck. Wait for “next case” before opening 03-soup-sieve.

For slot 2, give another fresh chat only the generated `reviewer-2` folder:

> Read TASK.md and act as a maintainer reviewing Python dependency updates. Use only this folder. Start with 01-soup-sieve. Read its FOCUS.txt and report.txt and submit your answers in your own words. Record any source files you open or places where you get stuck. Wait for “next case” before opening 02-opencv.

With the HTTPX summary option, add `01-httpx` first in slot 1 and `03-httpx` last in slot 2. For the offline task, reviewers can use the visible evidence IDs and findings. The source links identify provenance and do not require a fetch.

Use the same model for both slots. An assistant that keeps GitHub access can also see the grading material and opposite views. Record that setup as an exposed walkthrough. Either rehearsal leaves maintainer usefulness unmeasured.
