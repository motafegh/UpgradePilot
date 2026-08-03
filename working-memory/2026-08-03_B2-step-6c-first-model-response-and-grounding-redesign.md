# B2 Step 6C — First Model Response and Grounding Redesign

**Date:** 2026-08-03  
**Scope:** Preserve the first real Step 6C model response after localhost proxy isolation and record the bounded harness correction it justified.  
**Position authority:** `MEMORY.md` remains the sole live-state owner.

## Deterministic validation observed before the live run

Ali reported the complete suite result:

```text
Ran 320 tests in 0.057s

OK
```

This validates the deterministic repository state that included the Step 6C localhost proxy-isolation runner before the later semantic-selection harness redesign recorded below.

It does **not** validate the later redesign until Ali reruns tests from its new boundary.

## Live Step 6C attempt

Command:

```bash
python tools/run_step6c_support_drop_smoke.py
```

Observed transport progression:

```text
Step 6C localhost HTTP runner
control plane: WSL
environment proxies for child process: disabled
NO_PROXY: 127.0.0.1,localhost,::1
python: /home/motafeq/projects/UpgradePilot/.venv/bin/python

B2 Step 6C support-drop extraction smoke
control plane: WSL
LM Studio base URL: http://127.0.0.1:12345
model: gemma-4-e4b-it-ud
case: s001_exact_excerpt
transport/model inventory: PASS
completion HTTP: PASS (17.139s)
```

The previous Privoxy transport blocker was therefore resolved for this run.

## Observed model response

LM Studio returned structured content equivalent to:

```json
{
  "state": "unresolved",
  "package": "soupsieve",
  "normalized_package": "soupsieve",
  "old_version": "2.6",
  "proposed_version": "2.8.4",
  "candidates": [
    {
      "category": "support_boundary_change",
      "change_state": "support_dropped",
      "python_line": "Python 3.8",
      "introduced_in_version": "2.8",
      "source_kind": "tagged_changelog",
      "source_quote": "- **NEW**: Drop support for Python 3.8."
    }
  ],
  "detail": ""
}
```

The original frozen source line is:

```text
-   **NEW**: Drop support for Python 3.8.
```

The model normalized the three spaces after `-` to one space. The adapter correctly refused to derive a quote span from text that did not occur exactly in the source:

```text
STEP 6C SMOKE: FAIL
stage error: ValueError: Candidate 0 source_quote occurred 0 times; a unique exact span is required before offsets can be derived.
```

No exact-grounding rule was weakened.

## LM Studio generation evidence supplied by Ali

Observed LM Studio timing/log facts:

```text
prompt tokens: 441
completion tokens: 512
total tokens: 953
reasoning tokens: 333
finish_reason: length
prompt eval: 435.41 ms / 441 tokens
eval: 7756.61 ms / 512 tokens
total model timing: 8192.02 ms / 953 tokens
reported generation rate: 66.01 tokens/s
truncated: 0
```

The HTTP call measured by the UpgradePilot harness was `17.139s`; LM Studio's internal model timing was about `8.192s`. These are different measurement boundaries and are preserved separately rather than treated as contradictory.

## What this attempt establishes

Established:

```text
WSL localhost path after proxy isolation: works
LM Studio /v1/models: works
LM Studio /v1/chat/completions: works
gemma-4-e4b-it-ud generated JSON-shaped structured content
the model recognized the relevant semantic event and introduced release in its reasoning/content
```

Not established:

```text
contract-valid CandidateUpstreamClaimResult
canonical python_line value
exact quote/span grounding
coherent candidate state
semantic-oracle pass
Step 2 trust admission
Step 6C pass
model adoption
```

## Three distinct model-output defects

### 1. Exact-source reproduction defect

Model output:

```text
- **NEW**: Drop support for Python 3.8.
```

Exact source:

```text
-   **NEW**: Drop support for Python 3.8.
```

The semantic meaning was preserved, but the exact source bytes/characters were not. Exact quotation is a deterministic grounding responsibility and should not depend on the model preserving Markdown whitespace.

### 2. Canonical Python-line defect

Model output:

```text
Python 3.8
```

Trusted Step 2 representation requires:

```text
3.8
```

The model-facing schema had only constrained this field to `string`, so the schema was weaker than the existing domain contract.

### 3. State/candidate coherence defect

The model returned:

```text
state = unresolved
candidates = non-empty
```

The existing Step 2 contract does not permit non-available states to contain candidates. The model-facing shape had not encoded or mechanically checked that coherence before exact quote mapping.

## Finish-reason issue

The request used:

```text
max_tokens = 512
```

The model consumed all 512 completion tokens and returned:

```text
finish_reason = length
```

with 333 reasoning tokens. A later smoke must provide enough output budget that truncation does not confound semantic/contract evaluation. Increasing the bounded output budget is not an automatic retry and does not change the source case.

## Design correction

The failed quote reproduction exposed a responsibility mistake in the first harness:

```text
semantic extraction
!=
exact whitespace reproduction
```

The corrected model-facing contract now asks the model only for semantic selections:

```text
state
candidates[]:
  python_line
  introduced_in_version
  source_line_id
detail
```

Deterministic adapter code supplies or derives:

```text
package / normalized package / old / proposed identity
category = support_boundary_change
change_state = support_dropped
source_kind = tagged_changelog
exact source_quote from source_line_id
quote_start
quote_end
```

The source is rendered to the model with deterministic line IDs such as:

```text
L3 | -   **NEW**: Drop support for Python 3.8.
```

The model selects `L3`; it no longer has to reproduce the Markdown line exactly.

This preserves strict grounding because the adapter recovers the exact original source line and offsets. It does not fuzzy-match or normalize the model's quote.

## Additional mechanical bounding

The corrected harness also deterministically extracts explicit `Python X.Y` tokens from the source without interpreting direction. For the S001 excerpt the available values are:

```text
3.8
3.14
```

The JSON Schema therefore allows the model to select only an explicit source token rather than returning forms such as `Python 3.8`.

This is token bounding, not semantic extraction: deciding which token is a current dropped-support line remains the model's job.

The adapter now also rejects state/candidate incoherence before Step 2 admission.

## Output budget correction

The next bounded smoke uses:

```text
max_tokens = 1024
```

This is intended only to remove the demonstrated `finish_reason=length` confound. Automatic retries remain disabled.

## New implementation boundaries

Semantic-selection / deterministic-line-grounding harness redesign:

```text
6a69ffcb3f8fe05445ff0ab8acff9a2a71839875
```

Updated deterministic harness tests:

```text
d6af31ef01cc30040127f4fca384161e5a8cc8be
```

These boundaries are **not behavior-validated yet**. Ali must rerun the focused and complete deterministic tests before the next live smoke.

## Stop line

Remain in Step 6C.

Do not start the 15-case Step 6D evaluation or adopt a model until the redesigned one-case smoke is deterministically validated and then observed live.