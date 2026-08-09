# UpgradePilot Local Environment Reference

**Purpose:** Durable project-local reference for Ali's development-machine/runtime topology, recurring execution rules, stable local-service facts, and environment re-check policy.

This file is **not** the live project-position owner and is **not** an evidence archive. `MEMORY.md` owns current continuation. Dated measurements, inventories, incident details, experiment outputs, and one-run environment observations belong under `working-memory/` and are linked here when useful.

## 1. Core operating rule — WSL2 is the control plane

UpgradePilot normally runs from the project's WSL2 environment:

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

Default local-model interaction:

```text
UpgradePilot in WSL
→ localhost HTTP
→ LM Studio on Windows host
```

Do not make Windows PowerShell the normal project control plane merely because historical evidence was captured there. Use Windows-side commands/GUI only for a concrete host-only responsibility or when diagnosing a host-side failure that WSL/HTTP cannot expose.

## 2. Read-before-recheck rule

When a task touches local execution, Python, WSL2, GPU memory, LM Studio, local models, or local-model networking:

1. read this file first;
2. reuse established durable facts by default;
3. do not request repeated inventory merely because a new chat/session started;
4. re-check only the smallest fact whose freshness materially matters;
5. preserve consequential one-run evidence in `working-memory/`;
6. update this file only when the reusable baseline itself changes.

Freshness normally matters for:

- current free/used VRAM before a memory-sensitive operation;
- which model instance is loaded right now;
- inventory after an intentional add/remove operation;
- server reachability after an actual networking/configuration change;
- driver, LM Studio, Python, or machine identity after an upgrade;
- an explicit reproducibility proof requiring a new snapshot.

A new conversation is not evidence that the environment changed.

## 3. Reusable WSL runtime baseline

Last directly established baseline:

```text
repository: motafegh/UpgradePilot
checkout: /home/motafeq/projects/UpgradePilot
Python observed: 3.12.3
virtual-environment interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
```

Normal repository/runtime commands:

```bash
git pull --ff-only
python -m unittest discover -s tests -v
python --version
python -c 'import sys; print(sys.executable)'
```

The authoritative package/dependency declaration is `pyproject.toml`; do not duplicate its dependency list here.

## 4. Hardware baseline

Reusable GPU identity:

```text
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
nominal VRAM: 8192 MiB
```

Use WSL for current GPU observation when freshness matters:

```bash
nvidia-smi
```

Compact snapshot:

```bash
nvidia-smi \
  --query-gpu=name,driver_version,memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu \
  --format=csv
```

Point-in-time VRAM use, temperature, system-memory values, and load/unload measurements are evidence snapshots, not durable facts.

The project does not require the laptop chassis/model, CPU model, or Windows build unless a concrete technical responsibility later depends on them.

## 5. LM Studio service boundary

Established reusable baseline:

```text
server host: Windows
project client: WSL2
listener: 127.0.0.1
port: 12345
WSL localhost transport: proven
just-in-time model loading: observed
```

OpenAI-compatible base:

```text
http://127.0.0.1:12345/v1
```

Native LM Studio base:

```text
http://127.0.0.1:12345/api/v1
```

Normal visibility checks use explicit proxy bypass because this environment has previously demonstrated ambient-proxy interference with loopback traffic:

```bash
curl --noproxy '*' -fsS http://127.0.0.1:12345/v1/models | python -m json.tool
curl --noproxy '*' -fsS http://127.0.0.1:12345/api/v1/models | python -m json.tool
```

Normal OpenAI-compatible inference endpoint:

```text
POST http://127.0.0.1:12345/v1/chat/completions
```

Native model-management endpoints may be used from WSL when the installed server supports them:

```text
POST /api/v1/models/load
POST /api/v1/models/unload
```

`GET /api/v1/models` has been directly proven in Ali's environment. Before treating a particular native load/unload request shape as a reproducibility boundary, perform one narrow feature probe against the running server.

Do not broaden LM Studio exposure, enable CORS, bind to `0.0.0.0`, or modify firewall/authentication settings merely to simplify local work. If WSL localhost genuinely stops working, preserve the failure before trying a Windows-host gateway fallback.

### Reusable ambient-proxy caveat

This WSL environment has demonstrated that ambient proxy variables can intercept a request intended for `127.0.0.1:12345`, even when wildcard-like `NO_PROXY` values appear to cover loopback.

Operational consequence:

- follow `SECURITY.md`'s invariant that traffic intended for local inference must not unintentionally egress through an ambient proxy;
- use explicit `curl --noproxy '*'` for normal LM Studio diagnostics unless an exact working loopback exclusion has been independently established;
- do not interpret an HTTP error from a local-model probe as an LM Studio/model failure until the responding network boundary is identified;
- do not disable the user's VPN/proxy globally merely to run UpgradePilot.

Detailed incident/diagnostic evidence:

- [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md)

The product implementation/ADR/tests—not this environment reference—own the current mechanism that satisfies the security invariant.

## 6. Adopted local semantic deployment environment

ADR-0006 owns the architectural decision to use one bounded local support-drop semantic extractor. This file records only its reusable deployment environment.

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

The deployment was observed to fit the local GPU and support the required structured-output transport. Detailed GPU measurements, model-evaluation scores, rejected models, inventory, latency, and semantic results remain dated evidence.

A change to model identity, quantization/deployment identity, chat template, LM Studio structured-output behavior, or material load configuration is a reassessment event for ADR-0006 rather than a silent environment substitution.

## 7. Model inventory policy

The complete model inventory is intentionally not duplicated here because it is a dated snapshot.

Canonical historical inventory evidence:

- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json)

Do not download/substitute another model merely because a future assistant prefers one. Model selection follows the owning product responsibility and accepted architecture/evidence process.

## 8. Reusable GitHub credential caveat

This WSL environment has previously demonstrated an ambient `GITHUB_TOKEN` that caused a public GitHub REST proof to fail while anonymous access passed.

Operational consequence:

- follow `SECURITY.md` for intentional credential use;
- public read-only validation should not silently inherit ambient authentication unless the selected proof requires it;
- distinguish authentication/environment failure from source/evidence/product failure.

Safe presence check (never prints the value):

```bash
if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    echo "GITHUB_TOKEN is set"
else
    echo "GITHUB_TOKEN is not set"
fi
```

One-command anonymous execution when appropriate:

```bash
env -u GITHUB_TOKEN <COMMAND>
```

The credential value was never recorded and must never be requested or exposed.

## 9. Evidence references

Detailed historical environment/model evidence is preserved in:

- [`working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md`](working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md)
- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md`](working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md)
- [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md`](working-memory/2026-08-05_B2-step-7c-lm-studio-proxy-contamination-diagnosis.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/`](working-memory/evidence/2026-07-28-gemma-e4b/)

Historical records may contain PowerShell procedures because that is how those observations were obtained. They do not override this file's WSL-first rule.

## 10. Maintenance policy

Update this file only when a reusable environment fact materially changes, for example:

- machine/GPU identity;
- normal WSL/project/venv path;
- normal Python baseline;
- LM Studio port/base URL or WSL transport;
- reusable local deployment identity after its owning architecture decision is updated;
- a recurring credential/network caveat is resolved or materially changes.

Do not update this file for temporary processes, point-in-time memory values, one-run model instances, inventory snapshots, or experiment results.

`MEMORY.md` remains the sole live project-position owner.
