# B2 Step 6C — Live S001 Support-Drop Smoke Validation

**Date:** 2026-08-03  
**Scope:** One-case WSL → LM Studio → structured semantic selection → deterministic candidate mapping → Step 2 trust-admission smoke.  
**Model:** `gemma-4-e4b-it-ud`  
**Control plane:** WSL2  
**LM Studio base URL:** `http://127.0.0.1:12345`  
**Result:** PASS

## Deterministic validation observed by Ali

Ali reported the complete suite result after the Step 6C grounding redesign:

```text
Ran 322 tests in 0.062s

OK
```

This validates the deterministic harness, localhost proxy-isolation runner, and the new source-line selection mapping before the live model run.

## Live command

Ali ran from the UpgradePilot WSL virtual environment:

```bash
python tools/run_step6c_support_drop_smoke.py
```

The runner removed inherited HTTP proxy variables only for the child process and set localhost `NO_PROXY`, preserving the user's normal shell/system proxy configuration.

## Exact observed UpgradePilot output

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
completion HTTP: PASS (7.472s)
structured model content:
{
  "state": "candidates_available",
  "candidates": [
    {
      "python_line": "3.8",
      "introduced_in_version": "2.8",
      "source_line_id": "L3"
    }
  ],
  "detail": ""
}
structured candidate mapping: PASS
semantic oracle: PASS
Step 2 trust admission: PASS
trust result:
{
  "kind": "grounded",
  "python_line": "3.8",
  "introduced_in_version": "2.8",
  "source_count": 1
}
finish reason: stop
usage:
{
  "prompt_tokens": 499,
  "completion_tokens": 559,
  "total_tokens": 1058,
  "completion_tokens_details": {
    "reasoning_tokens": 475
  }
}
evidence file: /tmp/upgradepilot-step6c-support-drop-smoke.json

STEP 6C SMOKE: PASS
```

## Layer-by-layer conclusion

| Layer | Observed result | What it establishes |
|---|---|---|
| WSL localhost transport | PASS | Proxy-isolated WSL `requests` reached the LM Studio service. |
| Model inventory | PASS | The selected `gemma-4-e4b-it-ud` identity was available to the OpenAI-compatible endpoint. |
| Completion HTTP | PASS | `/v1/chat/completions` returned successfully. |
| Structured generation | PASS | The model returned the narrow JSON shape required by the revised adapter. |
| Candidate mapping | PASS | `3.8`, release `2.8`, and `L3` mapped mechanically to current Step 2 dataclasses and exact source offsets. |
| Semantic oracle | PASS | The one S001 case matched the frozen Step 6A expected meaning. |
| Step 2 trust admission | PASS | Existing deterministic grounding admitted exactly Python `3.8` introduced in `2.8`. |
| Completion termination | PASS | `finish_reason` was `stop`, not `length`. |

## Why the redesign mattered

The immediately preceding live attempt reached Gemma but failed because the model was asked to reproduce exact quote formatting and returned:

- `python_line = "Python 3.8"` instead of canonical `"3.8"`;
- normalized quote whitespace instead of the exact authoritative line;
- `state = "unresolved"` while also returning a candidate;
- `finish_reason = "length"` at a 512-token output cap.

The corrected boundary moved non-semantic mechanics out of the model:

```text
model decides:
  state
  Python X.Y token
  introduced release
  deterministic source line ID

adapter determines:
  dependency identity
  category = support_boundary_change
  change_state = support_dropped
  source kind
  exact original source quote
  exact quote offsets
```

The model still had to distinguish the dropped Python `3.8` line from the adjacent added Python `3.14` line. Exact whitespace reproduction was no longer treated as a language-understanding responsibility.

## LM Studio log corroboration

Ali also supplied the corresponding LM Studio desktop log. It corroborated:

```text
model: gemma-4-e4b-it-ud
prompt tokens: 499
completion tokens: 559
reasoning tokens: 475
total tokens: 1058
finish_reason: stop
truncated: 0
```

LM Studio timing output reported approximately:

```text
prompt eval: 501.84 ms / 499 tokens
generation: 7678.22 ms / 559 tokens
total model time: 8180.06 ms
generation throughput: 72.80 tokens/s
```

The UpgradePilot client-side completion measurement was `7.472s`; the LM Studio internal total timing was about `8.180s`. These are different measurement boundaries and are preserved separately rather than forced to match.

## Reproducibility caveat observed in LM Studio

LM Studio emitted this warning during the successful run:

```text
detected an outdated gemma4 chat template, applying compatibility workarounds. Consider updating to the official template.
```

This did not prevent the current Step 6C smoke from passing. It is nevertheless a deployment/reproducibility caveat for later model evaluation: the observed behavior includes LM Studio's compatibility workaround for this model/template combination.

Do not silently treat this warning as either harmless forever or as a reason to change the environment before scoring. Preserve it with the Step 6D results and only change the template/model deployment if evidence shows it materially affects the evaluation or reproducibility obligation.

## What Step 6C establishes

Step 6C now establishes one bounded fact:

```text
for the frozen S001 excerpt,
the current WSL + LM Studio + gemma-4-e4b-it-ud deployment
can produce the correct bounded semantic selection,
which the deterministic adapter maps to exact source evidence
and current Step 2 admits as Python 3.8 support dropped in release 2.8.
```

## What Step 6C does not establish

This one passing case does **not** establish:

- reliable support-drop extraction across paraphrases;
- correct abstention on support-added, continued-support, negation, future-drop, ambiguity, or raised-minimum-only text;
- robustness against instruction-shaped source text;
- repeatability across decision-critical cases;
- model/product adoption;
- normal-runtime semantic adapter admission;
- target Python relevance activation;
- S001 end-to-end product result;
- compatibility, safety, merge, defer, or maintainer-action conclusions;
- user mastery.

Those are outside Step 6C. The next bounded responsibility is Step 6D scored semantic evaluation against the frozen corpus and repeated critical controls.