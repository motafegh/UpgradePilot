# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans/specifications/ADRs/source/tests, [`ENVIRONMENT.md`](ENVIRONMENT.md), and dated `working-memory/` records retain their own responsibilities.

## Live position

- **Execution branch:** `main`.
- **Route:** B2 — Public PR vertical slice.
- **Parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Step 6:** closed with explicit disposition `adopt_bounded_extractor` for the narrow support-drop semantic role.
- **Accepted semantic architecture:** [`docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md`](docs/architecture/ADR-0006-bounded-local-support-drop-semantic-extractor.md)
- **Step 7 runtime-integration plan:** [`plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md`](plans/B2_TARGET_PYTHON_STEP_7_BOUNDED_EXTRACTOR_RUNTIME_INTEGRATION_PLAN.md)
- **Selected bounded continuation before further Step 7 work:** [`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md)
- **Step 7A implementation:** product client, controlled tests, package exports, and live S001 proof tool are committed remotely but remain user-validation pending.
- **Source-structure reconciliation:** planned and approved in direction, but no source migration has started.
- **Immediate action:** make the WSL checkout follow `origin/main`, preserve/remove the one blocking untracked duplicate safely, then establish the pre-refactor validation baseline.
- **Normal-runtime model extraction and conditional target-Python orchestration are not implemented.**

## Local synchronization blocker

Ali attempted:

```bash
git pull origin main
```

Git fetched remote changes but correctly aborted the merge because this untracked local file would be overwritten by the tracked remote version:

```text
working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json
```

The local file was created by the deterministic adoption-assessment command before the same evidence path was later preserved on remote `main`. Remote is the selected source of repository truth. Do not use `git reset --hard`, `git clean`, or other broad destructive commands to solve this one-file conflict.

## Last exact user-reported deterministic validation

Ali reported after the final Step 6 adoption-assessment tests:

```text
Ran 339 tests in 0.062s

OK
```

This validates the deterministic Step 6 assessment boundary. It does **not** validate the newer Step 7A source/test files or the future source-structure reconciliation.

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

## Step 7A implementation candidate

The committed Step 7A candidate performs:

```text
trusted repository + exact commit SHA
→ exact Git commit object
→ exact root tree SHA
→ complete recursive tree
→ admitted Markdown changelog basename filter
→ exactly one path or explicit problem
```

The current pre-reconciliation paths are:

```text
src/upgradepilot/upstream_changelog.py
tests/test_upstream_changelog.py
tools/live_s001_changelog_discovery_proof.py
```

The source-structure reconciliation plan intends to move the GitHub-specific product module under the GitHub provider boundary before further Step 7 implementation. The existing Step 7A behavior must be regression-proved after that move.

## Why source reconciliation precedes further Step 7 work

The flat product package grew incrementally while B2 established real boundaries. It now contains stable GitHub, PyPI, dependency, CI, upstream, target, and application responsibilities plus transition-era contracts and duplicated primitives.

ADR-0001 explicitly allows subpackages only after implemented responsibilities demonstrate a stable boundary. That reassessment trigger has now been reached.

The selected reconciliation plan covers:

```text
responsibility-based product subpackages
minimal package-root API
legacy dependency-path removal
shared package/repository/GitHub identity primitives
GitHub/PyPI provider grouping
Step 7A changelog discovery rehoming
dependency vs target version-method split
exact repository-file evidence convergence
old upstream unresolved_claim reconciliation
CLI vs investigation orchestration split
product-test vs experiment-test separation
active source comment/docstring correction
```

No Step 7 semantic runtime capability is authorized as part of this cleanup.

## Exact continuation

### 1. Synchronize local WSL checkout safely

Preserve the blocking untracked JSON outside the repository before letting remote win:

```bash
cd /home/motafeq/projects/UpgradePilot

mkdir -p /tmp/upgradepilot-sync-backup
cp \
  working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json \
  /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.local-untracked.json

git fetch origin main

git show \
  origin/main:working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json \
  > /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.remote.json

sha256sum \
  /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.local-untracked.json \
  /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.remote.json

cmp -s \
  /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.local-untracked.json \
  /tmp/upgradepilot-sync-backup/contract-v2-adoption-assessment.remote.json \
  && echo "assessment files are identical" \
  || echo "assessment files differ; local backup preserved in /tmp"

rm \
  working-memory/evidence/2026-08-03-step6d/contract-v2-adoption-assessment.json

git pull --ff-only origin main

git status
git log -1 --oneline
```

The `rm` is intentionally limited to the one untracked duplicate after it has been copied to `/tmp`. Remote `main` then restores the tracked authoritative file at the same path.

### 2. Establish the pre-refactor baseline

With a clean synchronized checkout:

```bash
python -m unittest \
  tests.test_upstream_changelog \
  tests.test_package_interface \
  -v

python -m unittest discover -s tests -v

python tools/live_s001_changelog_discovery_proof.py
```

Return:

- focused Step 7A test result;
- complete deterministic suite count/time;
- complete live Step 7A proof output;
- final `git status` and `git log -1 --oneline`.

Do not begin the first source-migration cluster until this baseline is known.

## Source-reconciliation first gate

After synchronization and baseline validation:

```text
record the ADR evolving ADR-0001
→ shared package/repository/GitHub identity primitives
→ migrate provider/domain clusters one at a time
→ validate after every cluster
```

The controlling details and final acceptance gate are in:

[`plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md`](plans/B2_SOURCE_CODE_STRUCTURE_RECONCILIATION_PLAN.md)

## Stop line

Until the source-reconciliation acceptance gate passes, do not begin:

- Step 7B deterministic crossed-release source windows;
- normal-runtime LM Studio model client;
- automatic retries or Instructor/Pydantic integration;
- target-Python conditional activation;
- full S001 relevance execution;
- compatibility, safety, merge, defer, or recommendation logic.

Source reconciliation itself must not silently implement any of those capabilities.

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
- architecture-decision evidence gates;
- recognizing when a flat package has accumulated real subpackage boundaries;
- separating provider acquisition, domain evidence, method semantics, orchestration, and interface responsibilities.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6 semantic model evaluation completed
+ Step 6 bounded extractor adopted by evidence and explicit approval
+ ADR-0006 accepted
+ Step 7 integration design established
+ Step 7A implementation exposure
+ source-structure inconsistencies identified and reconciliation plan selected
but
Step 7A not yet behavior-validated in Ali's synchronized checkout
source reconciliation not yet implemented
no normal-runtime model integration
no conditional target-Python orchestration
no full S001 end-to-end product proof
no formal mastery assessment
not mastered
```
