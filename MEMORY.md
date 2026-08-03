# UpgradePilot Current Memory

**Last updated:** 2026-08-03  
**Authority:** Sole repository owner of live project position, verified behavior, blockers, selected continuation, and current learning state.

Stable plans, specifications, ADRs, source, tests, and dated working records retain their own responsibilities. They must not mirror or compete with this file for live status.

## Single-live-state rule

`MEMORY.md` is replacement state, not append-only history. It alone answers what is selected now, what behavior is verified, what remains open, what happens next, and what learning depth is established.

## Live position

- **Execution branch:** `main`. No separate implementation branch is selected.
- **Route:** B2 — Public PR vertical slice.
- **Selected parent plan:** [`plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md`](plans/B2_TARGET_PYTHON_SUPPORT_RELEVANCE_PLAN.md)
- **Behavior-validated:** parent-plan Steps 1–5 and Step 6A.
- **Selected focused Step 6 plan:** [`plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md`](plans/B2_STEP_6_SUPPORT_DROP_EXTRACTION_EVALUATION_PLAN.md)
- **Current parent responsibility:** Step 6 — evaluate the candidate extraction/model path only where semantic interpretation is needed.
- **Current increment:** Step 6B — observe the current local inference environment before any model adapter is implemented.
- **Step 6A validation record:** [`working-memory/2026-08-03_B2-step-6a-support-drop-corpus-validation.md`](working-memory/2026-08-03_B2-step-6a-support-drop-corpus-validation.md)

## Last behavior-validated executable boundary

Step 6A corpus/test behavior is validated through:

```text
41b74eda85bbf554b746eac30e6c1a6ca39ddceb
```

The user reported that both requested validation runs passed completely.

The exact focused/full counts and timings were not supplied in that message and are not invented.

## Step 5 closure remains established

Step 5 is fully closed with deterministic and live S001 public-source evidence.

Observed live source facts remain:

```text
package: soupsieve
interval: 2.6 → 2.8.4
crossed releases: 2.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4
ignored non-PEP-440 keys: none

tag ref: refs/tags/2.8.4
direct tag object: commit 28108ab805818c832d9568142a99844fd95a0d39
resolved commit: 28108ab805818c832d9568142a99844fd95a0d39
peel depth: 0

changelog path: docs/src/markdown/about/changelog.md
changelog blob SHA: 6f221b7398681a580fa199044b3d3f1e11b55493
reported bytes: 17370
decoded bytes: 17370

authority basis: tagged_changelog
GitHub Release bodies admitted: 0
```

This establishes authoritative upstream interval evidence only; semantic interpretation remains Step 6.

## Step 6 responsibility

The active semantic path is intentionally narrow:

```text
AuthoritativeUpstreamIntervalEvidence
→ untrusted semantic candidate extraction
→ CandidateUpstreamClaimResult
→ validate_support_drop_candidates(...)
→ GroundedPythonSupportDropClaim
   or explicit claim problem
```

Only this semantic form is in scope:

```text
category = support_boundary_change
change_state = support_dropped
python_line = explicit normalized X.Y
introduced_in_version = exact trusted crossed release
```

Do not reopen general release-note summarization or the older four-category semantic proposal during this slice.

## Step 6A closure

Frozen corpus:

```text
experiments/step6_support_drop_semantic_corpus.json
```

Deterministic oracle tests:

```text
tests/test_step6_support_drop_semantic_corpus.py
```

The 15-case corpus covers direct and paraphrased support drops, support added/continued controls, negation, future tense, ambiguity, raised-minimum-only ungroundable text, multiple distinct drops, unrelated fixes, inert instruction-shaped text, and the exact S001 excerpt.

Step 6A validation proves the oracle itself agrees with the already behavior-validated Step 2 trust boundary before any model is scored.

The important existing grounding invariant remains:

```text
accepted source quote must itself contain the claimed Python X.Y token
```

Therefore text that only raises a minimum version without explicitly naming the dropped line cannot become a trusted dropped-line claim under the current contract.

## Step 6B — current local inference environment observation

Before writing an adapter or selecting a model, observe the current environment rather than relying on July records.

Required observations:

### Windows / LM Studio

- LM Studio CLI version or available CLI identity;
- LM Studio server status, port, and bind behavior where exposed by the CLI;
- downloaded LLM inventory;
- currently loaded model inventory;
- NVIDIA GPU identity, driver, memory totals/free/used, and active GPU processes.

### WSL2 / UpgradePilot environment

- default route / Windows gateway context;
- nameserver context;
- whether the LM Studio OpenAI-compatible `/v1/models` endpoint is reachable from WSL2;
- exact base URL/port that succeeds;
- active Python version and executable.

Do not record API tokens, private prompts, or unrelated files.

## Step 6 method constraints

Existing B2 evidence remains controlling:

- JSON Schema constrains output representation, not semantic truth;
- exact quote/span grounding does not prove correct interpretation;
- previous small local deployments produced material false support-drop claims;
- fixture-shaped regex/phrase repair is not accepted production semantics;
- manual structured claims remain test oracles, not automated extraction.

The current evaluation direction remains:

```text
bounded structured LLM extraction
→ deterministic Step 2 grounding/validation
```

but no model or adapter is adopted yet.

For the first smoke, prefer direct HTTP through the already-installed `requests` dependency unless current environment evidence demonstrates a missing capability.

Do not add OpenAI, Pydantic, Instructor, LangChain, or LM Studio SDK dependencies merely to perform environment observation or the first direct-HTTP smoke.

## Exact continuation

Capture the current environment.

From **Windows PowerShell** with LM Studio open:

```powershell
lms --version
lms server status --json --quiet
lms ls --llm --json
lms ps --json
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,memory.free --format=csv
nvidia-smi
```

If `lms --version` is unsupported, run `lms` and preserve the first lines showing the CLI identity/version.

Then from the **UpgradePilot WSL2 shell**:

```bash
ip route show default
cat /etc/resolv.conf | grep '^nameserver'
python --version
python -c 'import sys; print(sys.executable)'
```

Use the server port reported by the Windows command and test localhost first:

```bash
curl -fsS http://127.0.0.1:<PORT>/v1/models | python -m json.tool
```

If localhost fails, preserve that exact failure, then test the WSL2 default gateway:

```bash
WINDOWS_HOST="$(ip route show default | awk '/default/ {print $3; exit}')"
curl -fsS "http://${WINDOWS_HOST}:<PORT>/v1/models" | python -m json.tool
```

Do not enable CORS or broaden LM Studio network binding merely to make this work. If neither address works, preserve the failure first and diagnose exposure/authentication/bind behavior separately.

## Stop line

Until Step 6B environment observation is complete, do not begin:

- model scoring;
- adapter/product implementation;
- new semantic runtime dependencies;
- target-Python conditional activation;
- CLI orchestration changes;
- full S001 relevance execution;
- compatibility, safety, merge, defer, targeted-check, or recommendation logic.

## Explicitly not established

- current LM Studio server identity/reachability;
- current downloaded/loaded model inventory;
- current GPU memory state;
- a selected candidate model;
- structured-output smoke success;
- an adopted support-drop extractor;
- automated grounded S001 Python 3.8 support-drop extraction;
- conditional target-Python activation in CLI runtime;
- S001 automated end-to-end relevance result;
- compatibility, safety, recommendation, maintainer action, or production readiness;
- user mastery of Steps 1–6.

## Learning state

Steps 1–5 and Step 6A are behavior-validated at product level. Step 6B is an environment-observation responsibility, not a mastery claim.

Current Step 6 concepts exposed:

- **semantic oracle:** frozen expected meaning used to score an extractor;
- **candidate extraction:** untrusted semantic proposal from prose;
- **structured generation:** output-shape compliance only;
- **mechanical grounding:** exact quote/span exists in trusted source text;
- **semantic correctness:** whether the candidate accurately represents the source meaning;
- **trust admission:** deterministic Step 2 validation decides whether a candidate becomes domain evidence;
- **deployment boundary:** model server, model identity, transport, schema, semantics, and product adoption are separate concerns.

Current depth:

```text
Steps 1–5 behavior validated
+ Step 6A corpus/oracle behavior validated
+ Step 6 architecture and semantic boundaries introduced
but
current LM Studio environment not yet observed
no current model/schema smoke proof
no model adoption evidence
no user-owned Step 6 end-to-end explanation recorded
no formal mastery assessment
not mastered
```

Product validation and learning mastery remain separate claims.

## State-maintenance rule

When route, selected responsibility, verified executable boundary, blocker, learning state, or exact continuation changes:

1. update `MEMORY.md` only for live state;
2. replace obsolete live statements instead of accumulating them;
3. change plans/specifications/ADRs only when their stable responsibility actually changes;
4. create dated working-memory only for material historical evidence or reasoning, never as another status owner;
5. keep navigation READMEs non-state-bearing.
