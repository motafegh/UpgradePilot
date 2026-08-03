# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans/specifications/ADRs/source/tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated `working-memory/` records retain their own responsibilities.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with explicit disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted architecture:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
- **Selected Step 7 plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)
- **Current increment:** Step 7A — exact-commit changelog-path discovery.
- **Step 7A implementation:** product client, controlled tests, package exports, and live S001 proof tool committed; user validation pending.
- **Normal-runtime model extraction and CLI conditional activation are not implemented yet.**

## Last exact user-reported deterministic validation

Ali reported after the final Step 6 adoption-assessment tests:

```text
Ran 339 tests in 0.062s

OK
```

This validates the deterministic Step 6 assessment boundary. It does **not** validate the newer Step 7A source/test files.

## Step 6 final disposition

Final deterministic adoption assessment:

```text
model: gemma-4-e4b-it-ud
contract version: 2
strict oracle: 24 / 25
adoption safety: 25 / 25
all material critical repeats consistent: true
all 10 adoption-gate checks: true
proposed disposition: adopt_bounded_extractor
```

Observed 25-call latency:

```text
mean:   8.852445 s
median: 8.414366 s
min:    5.355407 s
max:   12.549101 s
```

Ali explicitly approved the bounded adoption and the recommended architecture.

The accepted boundary is:

```text
LM Studio local HTTP
+ gemma-4-e4b-it-ud
+ contract v2
+ direct requests baseline
+ temperature 0
+ seed 0
+ automatic retries disabled
+ deterministic exact-source reconstruction
+ mandatory validate_support_drop_candidates(...)
```

This is not general model trust. The model is not authorized to select source authority, infer dependency identity, compare target Python, make compatibility/safety claims, recommend merge/defer actions, or mutate target repositories.

Durable evidence:

```text
working-memory/evidence/2026-08-03-step6d/support-drop-evaluation.json
working-memory/evidence/2026-08-03-step6d/contract-v2-replay.json
working-memory/evidence/2026-08-03-step6d/contract-v2-live-evaluation.json
working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json
```

Complete Step 6 engineering history and failure/fix record:

[`working-memory/2026-08-03_B2-step-6-semantic-extraction-complete-engineering-retrospective.md`](working-memory/2026-08-03_B2-step-6-semantic-extraction-complete-engineering-retrospective.md)

Reusable lessons:

[`learning/bounded-llm-semantic-extraction.md`](learning/bounded-llm-semantic-extraction.md)

## Important Step 6 caveats retained

### Strict diagnostic miss

The live contract-v2 run classified one ambiguous case as:

```text
no_relevant_claim
```

where the frozen strict oracle expected:

```text
unresolved
```

The result contained zero candidates and stopped downstream activation, so the adoption-safety gate still passed. The strict miss remains recorded and is not rewritten.

### LM Studio template warning

LM Studio reported that the loaded Gemma 4 deployment used an outdated chat template and applied compatibility workarounds. Changing the template is a deployment change and requires re-evaluation rather than silent substitution.

### Localhost proxy boundary

Earlier WSL inference failed when inherited proxy variables sent `127.0.0.1` traffic through Privoxy. Experiment runners proved a local no-proxy process boundary. Product runtime integration must own equivalent loopback isolation without changing global proxy configuration.

## Closed Step 5 authority boundary

S001 upstream authority remains behavior-validated:

```text
soupsieve 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
upstream repository: facelessuser/soupsieve
resolved proposed-tag commit: 28108ab805818c832d9568142a99844fd95a0d39
historical S001 changelog path: docs/src/markdown/about/changelog.md
changelog blob: 6f221b7398681a580fa199044b3d3f1e11b55493
reported/decoded bytes: 17370 / 17370
authority basis: tagged_changelog
```

Step 5 proved acquisition when one explicit changelog path is supplied. It intentionally did not automate changelog-path discovery.

## Why Step 7 has deterministic prerequisites before model integration

Two separate proof gaps exist between Step 5/6 experiments and normal runtime:

1. S001 Step 5 supplied the changelog path manually; product runtime may not hardcode it.
2. Step 6 evaluated bounded release text; the real exact tagged changelog is 17,370 bytes, so whole-file prompting is not automatically equivalent to the evaluated model contract.

The selected Step 7 plan therefore requires:

```text
7A exact-commit changelog-path discovery
→ 7B deterministic crossed-release Markdown source windows
→ 7C product local semantic adapter
→ 7D semantic extraction + Step 2 evaluation service
→ 7E conditional CLI orchestration
→ 7F controlled + live S001 end-to-end proof
```

Do not skip 7A/7B and feed an arbitrary full changelog directly to the model.

## Step 7A implementation candidate

Implementation record:

[`working-memory/2026-08-03_B2-step-7a-changelog-discovery-implementation.md`](working-memory/2026-08-03_B2-step-7a-changelog-discovery-implementation.md)

New product module:

```text
src/upgradepilot/upstream_changelog.py
```

It performs:

```text
trusted repository + exact commit SHA
→ exact Git commit object
→ exact root tree SHA
→ complete recursive tree
→ admitted Markdown changelog basename filter
→ exactly one path or explicit problem
```

Initial admitted basenames:

```text
changelog.md
changes.md
history.md
release-notes.md
```

Directory location is not hardcoded. Multiple candidates are not ranked; they return an explicit ambiguity problem. A truncated recursive tree cannot establish complete discovery.

Controlled tests:

```text
tests/test_upstream_changelog.py
```

Package-interface regression was extended in:

```text
tests/test_package_interface.py
```

Live S001 proof tool:

```text
tools/live_s001_changelog_discovery_proof.py
```

The scenario-specific tool uses the historical S001 path only as a validation oracle. Product source contains no S001 path constant.

### Implementation wiring defect already corrected

The first package-export edit accidentally added two CI exercise type names to the `dependency_change` import block. Static review caught the mistake before validation, and the import block was corrected. The package-interface test now protects the intended changelog-discovery exports.

Executable Step 7A candidate boundary before documentation/live-state commits:

```text
d3738cc4408f7eb65df2a6ff7f5d56b94ee42446
```

## Exact continuation

From the WSL checkout, first synchronize. Because the final Step 6 assessment JSON was generated locally before the same file was preserved through the GitHub connector, remove only that duplicate untracked local copy **if Git reports it would block the pull**; do not remove any committed evidence.

Normal validation commands:

```bash
git pull --ff-only

python -m unittest \
  tests.test_upstream_changelog \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v

python tools/live_s001_changelog_discovery_proof.py
```

The live proof performs anonymous public GitHub reads and makes no LM Studio call.

Return the focused-test result, full-suite count/time, and complete live Step 7A proof output.

## Step 7A validation gate

Do not begin Step 7B until all three are observed:

```text
focused changelog-discovery/package-interface tests pass
+ complete deterministic suite passes
+ live S001 exact-commit discovery reaches docs/src/markdown/about/changelog.md
```

If live discovery returns several admitted candidates, no candidate, truncated tree, or acquisition/identity failure, preserve that evidence and reframe the source-discovery rule rather than hardcoding S001.

## Stop line

Until Step 7A passes, do not begin:

- deterministic crossed-release source-window implementation;
- normal-runtime LM Studio model client;
- automatic retries or Instructor/Pydantic integration;
- target-Python conditional CLI changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, or recommendation logic.

## Learning state

Current exposure includes:

- source authority vs source discovery;
- exact Git commit/tree identity;
- complete recursive-tree evidence and truncation semantics;
- deterministic source-location heuristics with ambiguity abstention;
- semantic extraction vs exact grounding;
- contract normalization;
- counterfactual replay;
- strict semantic vs adoption-safety metrics;
- material repeatability;
- local HTTP/proxy boundaries;
- architecture-decision evidence gates.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6 semantic model evaluation completed
+ Step 6 bounded extractor adopted by evidence and explicit approval
+ ADR-0006 accepted
+ Step 7 integration design established
+ Step 7A implementation exposure
but
Step 7A not yet behavior-validated
no normal-runtime model integration
no conditional target-Python orchestration
no full S001 end-to-end product proof
no formal mastery assessment
not mastered
```
