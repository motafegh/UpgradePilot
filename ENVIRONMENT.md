# UpgradePilot Local Environment Reference

**Purpose:** Durable project-local reference for Ali's development-machine/runtime topology, recurring execution rules, stable local-service facts, and environment re-check policy.

This file is not the live-position owner or an evidence archive. `MEMORY.md` owns current continuation. Point-in-time measurements, inventories, incident details, and experiment outputs belong under `working-memory/`.

## 1. WSL2 is the control plane

```text
Windows host
├── NVIDIA GPU
├── LM Studio application/server
└── WSL2  ← UpgradePilot control plane
    ├── repository and Git
    ├── Python virtual environment
    ├── tests / experiments / tools
    ├── curl / HTTP local-model control
    ├── nvidia-smi
    └── product execution
```

Normal local-model path:

```text
UpgradePilot in WSL
→ localhost HTTP
→ LM Studio on Windows host
```

Use Windows-side commands/GUI only for a concrete host-only responsibility or a host-side failure that WSL/HTTP cannot expose. Historical PowerShell evidence does not make Windows the normal control plane.

## 2. Read before re-checking

When local execution, Python, WSL2, GPU, LM Studio, local models, or local networking matter:

1. read this file first;
2. reuse durable facts by default;
3. re-check only the smallest freshness-sensitive fact;
4. preserve consequential one-run evidence in `working-memory/`;
5. update this file only when the reusable baseline changes.

Freshness normally matters for current VRAM, currently loaded models, post-change inventory/reachability, upgraded driver/LM Studio/Python/machine identity, or an explicit reproducibility snapshot.

A new conversation is not evidence that the environment changed.

## 3. Reusable WSL runtime baseline

```text
repository: motafegh/UpgradePilot
checkout: /home/motafeq/projects/UpgradePilot
Python observed: 3.12.3
virtual-environment interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
```

Normal commands:

```bash
git pull --ff-only
python -m unittest discover -s tests -v
python --version
python -c 'import sys; print(sys.executable)'
```

`pyproject.toml` is the package/dependency authority; do not duplicate its dependency list here.

## 4. Hardware baseline

```text
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
nominal VRAM: 8192 MiB
```

Use WSL for a current observation when freshness matters:

```bash
nvidia-smi
```

Compact snapshot:

```bash
nvidia-smi \
  --query-gpu=name,driver_version,memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu \
  --format=csv
```

Point-in-time usage/temperature values are evidence, not durable facts. Do not request chassis, CPU, or Windows-build details without a concrete technical reason.

## 5. LM Studio service boundary

Reusable topology:

```text
server host: Windows
project client: WSL2
listener: 127.0.0.1
port: 12345
WSL localhost transport: proven
just-in-time model loading: observed
```

Bases:

```text
OpenAI-compatible: http://127.0.0.1:12345/v1
LM Studio native:  http://127.0.0.1:12345/api/v1
```

Normal visibility checks:

```bash
curl --noproxy '*' -fsS http://127.0.0.1:12345/v1/models | python -m json.tool
curl --noproxy '*' -fsS http://127.0.0.1:12345/api/v1/models | python -m json.tool
```

Normal inference endpoint:

```text
POST http://127.0.0.1:12345/v1/chat/completions
```

Native model-management endpoints may be used when the installed server supports them:

```text
POST /api/v1/models/load
POST /api/v1/models/unload
```

`GET /api/v1/models` has been directly proven. Probe a specific native load/unload request shape before treating it as a reproducibility boundary.

Do not broaden server exposure, enable CORS, bind to `0.0.0.0`, or weaken firewall/authentication merely for convenience. Preserve an actual WSL-localhost failure before trying a host-gateway fallback.

### Ambient-proxy caveat

This WSL environment has demonstrated ambient proxy interception of traffic intended for `127.0.0.1:12345`, despite wildcard-like `NO_PROXY` configuration.

Consequences:

- follow `SECURITY.md`'s invariant that local-inference traffic must not unintentionally egress through an ambient proxy;
- use `curl --noproxy '*'` for normal LM Studio diagnostics unless an exact working loopback exclusion is independently established;
- identify the responding network boundary before classifying an HTTP error as an LM Studio/model failure;
- do not disable the user's VPN/proxy globally merely to run UpgradePilot.

Incident evidence: [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md).

Implementation/ADR/tests—not this file—own the mechanism that enforces the security invariant.

## 6. Adopted local semantic deployment

ADR-0006 owns the decision to use the bounded local support-drop semantic extractor. Reusable deployment facts:

```text
model key: gemma-4-e4b-it-ud
observed architecture: gemma4
observed parameters: 7.5B
observed quantization: Q4_K_XL
validated context length: 4096
parallelism: 1
Flash Attention: true
KV cache on GPU: true
```

Detailed GPU measurements, comparison results, latency, inventory, and semantic outputs remain dated evidence. A change to model/quantization/deployment identity, chat template, structured-output behavior, or material load configuration is an ADR-0006 reassessment event rather than a silent substitution.

Historical model inventory/evaluation entry points:

- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/`](working-memory/evidence/2026-07-28-gemma-e4b/)

Do not download/substitute another model merely because a future assistant prefers one.

## 7. GitHub credential and proxy caveat

This environment has demonstrated two independent ambient-state failures for public GitHub REST acquisition:

```text
ambient GITHUB_TOKEN
→ public GitHub request sent with Authorization: Bearer ...
→ stale/invalid token can produce HTTP 401

ambient HTTP(S)/ALL proxy variables
→ requests/urllib3 can route api.github.com through the configured proxy
→ proxy/TLS handshake can time out even though direct GitHub access is healthy
```

A direct public control using `curl --noproxy '*'` has returned HTTP 200 for the real S001 PR endpoint while the proxied Python acquisition timed out.

Consequences:

- follow `SECURITY.md` for deliberate credential use;
- public read-only validation should not silently inherit authentication unless the proof requires it;
- when a public GitHub proof returns 401 and `GITHUB_TOKEN` is ambient, retry the proof without that variable before diagnosing product/source failure;
- when GitHub acquisition times out inside proxy preparation/TLS while direct access works, run only the affected command without ambient proxy variables rather than disabling the user's VPN/proxy globally;
- distinguish authentication failure, proxy/transport failure, source/evidence failure, and product/experiment failure.

Safe token presence check:

```bash
if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    echo "GITHUB_TOKEN is set"
else
    echo "GITHUB_TOKEN is not set"
fi
```

Direct public reachability control:

```bash
curl --noproxy '*' -fsS \
  https://api.github.com/repos/pydantic/pydantic/pulls/13432 \
  >/dev/null
```

One-command public execution without ambient token/proxies when that proof does not require them:

```bash
env \
  -u GITHUB_TOKEN \
  -u HTTP_PROXY -u HTTPS_PROXY -u ALL_PROXY \
  -u http_proxy -u https_proxy -u all_proxy \
  <COMMAND>
```

This is process-local isolation. Do not globally unset proxy configuration solely for UpgradePilot, and never request or expose the token value.

## 8. Maintenance

Update only when a reusable fact materially changes: machine/GPU identity, normal WSL/repo/venv/Python baseline, LM Studio endpoint/transport, accepted local deployment identity, or a recurring environment caveat.

Do not update for temporary processes, point-in-time memory values, one-run model instances, inventory snapshots, or experiment results.

`MEMORY.md` remains the sole live project-position owner.
