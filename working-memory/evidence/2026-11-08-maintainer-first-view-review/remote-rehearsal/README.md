# GitHub checkout AI rehearsal

This handoff rebuilds four exact revision 3 participant views for OpenCV and Soup Sieve from saved JSON already tracked in UpgradePilot. The original case numbers and assignments are preserved. HTTPX requires a separately delivered owner-local packet. The generated views are local scratch files.

From the repository root, use a Python 3.12+ environment with UpgradePilot's project dependencies installed:

```sh
mkdir -p .tmp
PYTHONPATH=src python working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/prepare.py .tmp/maintainer-first-view-remote-r3
```

The script checks the saved inputs, prompts and rendered bytes against the original receipts before creating the output. It reads saved reports offline. A GitHub assistant without a checkout and shell can use the [saved-report walkthrough](../../2026-11-08-maintainer-report-first-view/REVIEW_PACKET.md) for technical inspection.

## Reviewer prompts

For slot 1, give a fresh chat only the generated `reviewer-1` folder:

> Read TASK.md and act as a maintainer reviewing Python dependency updates. Use only this folder. Start with 02-opencv. Read its FOCUS.txt and report.txt and submit your answers in your own words. Record any source files you open or places where you get stuck. Wait for “next case” before opening 03-soup-sieve.

For slot 2, give another fresh chat only the generated `reviewer-2` folder:

> Read TASK.md and act as a maintainer reviewing Python dependency updates. Use only this folder. Start with 01-soup-sieve. Read its FOCUS.txt and report.txt and submit your answers in your own words. Record any source files you open or places where you get stuck. Wait for “next case” before opening 02-opencv.

Use the same model for both slots. An assistant that keeps GitHub access can also see the grading material and opposite views. Record that setup as an exposed walkthrough. The two-case subset gives an AI rehearsal only and leaves maintainer usefulness unmeasured.
