# First fresh ordinary PR — final executable freeze for inspection

**Status: frozen for inspection; live activation withheld.** [Execution snapshot](execution-freeze.json), [verification](verification.json), [cycle](../../2026-10-31_first-fresh-ordinary-pr-execution-freeze_cycle.md), [unchanged definition](../2026-10-30-first-fresh-ordinary-pr-contract/CONTRACT.md), [unchanged selected contract](../2026-10-30-first-fresh-ordinary-pr-contract/contract.json).

## What is frozen

The existing snapshot helper produced `ordinary-pr-execution-freeze/1` from the actual qualified implementation. Its mode `live_activation` selects the proposed fresh acquisition method; it does not activate a request or supply user authorization. Configuration is bound through the exact original contract digest, rather than a second editable policy copy.

| Selection | Frozen value |
| --- | --- |
| Repository / PR | `Aidan-Wallace/kubernetes-dashboard-token-api` /20 |
| Base guard | `b065646e4b7b894964567950f9ad770b02c136c2` |
| Head guard | `391508134b083b8f54461c0b576e8f7985c6ecb4` |
| Auth | Explicit existing owner-only trial credential location; no ambient token or anonymous fallback |
| Providers | HTTPS GET only, `api.github.com` and `pypi.org`, no redirects |
| Shared request allowance |50 GitHub /100 all-provider attempts |
| HTTP decoded bytes |8MiB per response /32MiB aggregate |
| Acquisition time |180s cooperative checks/socket limits; separate from analysis |
| Target/source selection |16 file attempts,2 adapter candidate attempts,24 protected source requests; existing4-release/12-module/2MiB library bounds |
| Analysis | Existing32-file/4MiB source,256-comparison,60s/512MiB worker bounds |
| Attempt | One official attempt; no automatic retry, cap enlargement or revised identity substitution |

The snapshot binds106 source files, including the native source forest and experimental owners. Its supported runtime representation binds CPython3.12.3, the actual virtual-environment executable and binary digest, Linux platform, requests2.34.2 and packaging26.2. It is not a complete machine/environment archive. Future provider responses, credential validity, PR freshness, acquisition cost/fit and useful results remain unobserved.

## Inspection proof

Current source/runtime identity exactly matches the [qualified implementation receipt](../2026-10-31-fresh-ordinary-attempt-lifecycle/verification.json). All31 artifacts bound by that receipt match their recorded hashes. Its recorded242 API/7 architecture passing tests, six authored-HTTP controls and historical full636 red disposition remain evidence at that qualification horizon; they were not rerun or relabelled as fresh provider proof here. No implementation changed.

The actual snapshot passes the runner's current fixed execution admission. Calling the normal entry with activation omitted refuses with `Live activation withheld; no credential/provider work.` Credential access, provider construction/HTTP and directory creation were forbidden during that check. It created no official started/terminal record and is not a consumed real attempt. The original frozen definition and retained evidence are not edited.

## Local prerequisite and authorization boundary

The selected private destination remains the original contract's `ordinary-pr-acquisition/httpx-pr20-2026-10-30/attempt-01`; the historical date in this name is retained unchanged. Its parent does not exist. After live authorization, create only the required private parent hierarchy with owner-only directories before invoking the runner; the runner itself must create the unused final attempt directory and start record. Do not create `attempt-01` as setup or work around an existing destination.

Credential existence, permissions and validity have not been inspected. The runner checks/reads the explicitly bound file only after retaining its immutable start. Missing/unsafe credential, auth refusal, exact identity drift, provider/material bounds or unsupported acquisition remain retained outcomes. No separate quota/auth request is selected. Keep current-input/source limitations distinct from a demonstrated implementation defect.

The snapshot and its review package do not override Ali's earlier instruction: “After those are reviewed and recorded, stop before executing the real attempt so we can inspect the frozen contract.” The distinct live activation decision is next. No model/target/workflow execution, install, new host, external write or native product adoption is admitted by this freeze.

## Execution recipe — inspect only, not executed

After explicit activation, use the current checkout and virtual environment, unchanged contract/snapshot bytes and the existing ordinary owner. Process-local proxy/ambient-token isolation follows ENVIRONMENT.md; global configuration stays unchanged. Prepare the private parent directories first, without creating the final attempt directory.

```sh
env -u GITHUB_TOKEN -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
    -u http_proxy -u https_proxy -u all_proxy \
    PYTHONPATH=src:. .venv/bin/python - <<'PY'
from pathlib import Path
from experiments.api_ordinary_call_signature_trial import run_fresh_ordinary_pr_attempt

evidence = Path("working-memory/evidence")
contract = (evidence / "2026-10-30-first-fresh-ordinary-pr-contract/contract.json").read_bytes()
freeze = (evidence / "2026-10-31-first-fresh-ordinary-pr-execution-freeze/execution-freeze.json").read_bytes()
attempt = run_fresh_ordinary_pr_attempt(contract, freeze, activate_live=True)
print(attempt["state"], attempt["reason"], attempt["structural_disposition"])
PY
```

Inspect any real outcome offline with the existing `open-attempt --result DIRECTORY` command. Preserve partial/refused/interrupted evidence and stop; do not rerun or change the freeze to rescue an outcome. Code/runtime/contract drift requires reconciliation and an explicitly labelled successor rather than refreshing this snapshot silently. Useful local comparisons remain conditional source evidence, not installation, runtime exercise, semantic compatibility, maintainer authority or independent usefulness proof.
