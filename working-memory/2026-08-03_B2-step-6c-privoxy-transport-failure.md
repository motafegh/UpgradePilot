# B2 Step 6C — First Live Smoke Transport Failure

**Date:** 2026-08-03  
**Operation:** Execute the first WSL-side Step 6C support-drop extraction smoke after deterministic harness validation  
**Result classification:** Environment/proxy transport failure before LM Studio; no model/schema/semantic conclusion

## Deterministic validation reported by Ali

Ali reported the requested deterministic test run completed successfully:

```text
Ran 318 tests in 0.060s

OK
```

This validates the Step 6C deterministic harness/test boundary that existed before the live smoke attempt. It does not validate the later proxy-isolation runner added after the observed failure.

## Live command

From the active UpgradePilot WSL virtual environment:

```bash
python experiments/step6_support_drop_smoke.py
```

Observed output:

```text
B2 Step 6C support-drop extraction smoke
control plane: WSL
LM Studio base URL: http://127.0.0.1:12345
model: gemma-4-e4b-it-ud
case: s001_exact_excerpt
evidence file: /tmp/upgradepilot-step6c-support-drop-smoke.json

STEP 6C SMOKE: FAIL
stage error: HTTPError: 500 Server Error: Internal Privoxy Error for url: http://127.0.0.1:12345/v1/models
```

## Classification

The failure occurred on the first model-list request:

```text
WSL Python requests
→ intended http://127.0.0.1:12345/v1/models
→ Privoxy path observed instead
→ HTTP 500 Internal Privoxy Error
```

Therefore this run did **not** establish a failure of:

- LM Studio itself;
- `gemma-4-e4b-it-ud` availability or loading;
- `/v1/chat/completions`;
- JSON-Schema constrained generation;
- candidate mapping;
- semantic correctness;
- Step 2 grounding/trust admission.

The exact proxy environment variable(s) responsible were not inspected and are not invented. The observed evidence is only that Python `requests` inherited proxy behavior that routed the loopback request through Privoxy.

## Bounded correction

Do not change Ali's global WSL proxy configuration merely for this local experiment.

Added:

```text
tools/run_step6c_support_drop_smoke.py
tests/test_step6c_local_http_runner.py
```

The runner creates a child environment only for this smoke process that:

- removes HTTP/HTTPS/ALL proxy variables and lowercase equivalents;
- sets `NO_PROXY` and `no_proxy` to `127.0.0.1,localhost,::1`;
- executes the existing Step 6C experiment with the active UpgradePilot Python interpreter.

This preserves WSL as the control plane and does not mutate:

- the user's parent shell environment;
- system proxy configuration;
- LM Studio configuration;
- UpgradePilot production source.

## Stop line

The first Step 6C live semantic smoke remains open.

Do not infer model success/failure from this Privoxy error. Validate the proxy-isolation runner deterministically, then rerun the same one-case smoke through it before Step 6D or any model-adoption discussion.