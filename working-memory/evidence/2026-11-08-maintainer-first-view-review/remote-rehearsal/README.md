# GitHub AI rehearsal

The [reviewer-1 packet](connector-packets/reviewer-1/) and [reviewer-2 packet](connector-packets/reviewer-2/) are ready to read through a GitHub connector. Each contains `TASK.md` and three numbered cases with `FOCUS.txt` and `report.txt`. OpenCV and Soup Sieve match the frozen revision 3 views. HTTPX uses the published summary, with the same detailed text in both conditions and the opening added to one. Evidence IDs are visible in the reports. The published packets have zero original-text attachments.

## Reviewer prompts

Give a fresh chat only its assigned folder path at the packet commit.

> Act as a maintainer reviewing Python dependency updates. Using the GitHub connector, read TASK.md in your assigned folder. Open only FOCUS.txt and report.txt for the first numbered case. Answer in your own words using the visible report evidence. Record any access problems and where you got stuck. Wait for “next case” before opening the next numbered case. Keep the other slot, grading key and earlier reviews outside your review.

Slot 1 follows HTTPX → OpenCV → Soup Sieve. Slot 2 follows Soup Sieve → OpenCV → HTTPX. Use the same model if available. Record repository-wide access as an exposed walkthrough because the connector can access the key and the opposite views. The exercise leaves maintainer usefulness unmeasured.

## Reproduce the published packets

From the repository root, use a Python 3.12+ environment with UpgradePilot's project dependencies installed:

```sh
mkdir -p .tmp
PYTHONPATH=src python working-memory/evidence/2026-11-08-maintainer-first-view-review/remote-rehearsal/prepare.py --include-httpx-summary .tmp/maintainer-first-view-remote-r3
```

The script checks the two exact cases against their saved-input, prompt and view hashes. It reads saved reports offline. The generated folders also contain empty `sources/` directories, which Git omits.

The full HTTPX saved report is 3.4 MB and embeds complete third-party files. The target repository is public, but redistribution permission for its captured source was not verified. The [tracked receipt](../receipt.json) records the saved report and original view hashes. The [published summary](HTTPX_REPORT.md) and [opening](HTTPX_OPENING.md) supply findings, evidence IDs and pinned source links. Record this case as a summary-based rehearsal, separate from the byte-exact revision 3 case.
