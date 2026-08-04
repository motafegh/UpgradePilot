# B2 Step 7B — Crossed-Release Source Window Validation

**Date:** 2026-08-05  
**Responsibility:** Deterministic crossed-release Markdown source windows  
**Validated implementation head:** `ec80105cabca9515c74a89549119f40415df6c0d`

## Result

Step 7B deterministic validation passed in the normal WSL project environment.

Ali reported all requested checks green after pulling the implementation head. The executed validation set was:

```bash
python -m unittest discover -s tests -p 'test_upstream_changelog.py' -v
python -m unittest discover -s tests -p 'test_github_changelog.py' -v
python -m unittest discover -s tests -p 'test_source_topology.py' -v
python -m unittest discover -s tests -v
```

## Proven boundary

The accepted product implementation now provides:

```text
CrossedReleaseIndexEvidence
+ TaggedChangelogEvidence
+ explicit caller-owned character bound
→ exact matching Markdown release sections
→ original global line IDs and character offsets
→ complete CrossedReleaseSourceWindow
or explicit typed problem
```

The focused product tests cover complete reverse-chronological selection, exact source slices, `v`-prefixed headings, nested subsections, fenced-code false headings, strict release-heading grammar, missing and duplicate releases, source-order conflict, overlapping release sections, CRLF/global offsets, identity mismatch, and complete-window overflow without truncation.

Step 7B remains deterministic and semantic-neutral. It does not identify Python support meaning, invoke a model, compare target declarations, or make compatibility/safety/recommendation claims.

## Continuation

The Step 7B proof gate is closed. The next bounded product increment is Step 7C: implement the accepted ADR-0006 local semantic adapter under `src/upgradepilot/upstream/support_drop_extractor.py` without importing experiment code or changing the accepted provider/model/contract/retry policy.
