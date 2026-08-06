# UpgradePilot Local Environment Reference

**Purpose:** Durable project-local reference for Ali's development machine/runtime topology, recurring execution rules, stable local-service facts, and environment re-check policy.

This file is **not** the live project-position owner and is **not** an evidence archive. `MEMORY.md` owns current continuation. Dated measurements, inventories, experiment outputs, and one-run environment observations belong under `working-memory/` and are linked here when useful.

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

Default interaction:

```text
UpgradePilot in WSL
→ localhost HTTP
→ LM Studio on Windows host
```

Do not make Windows PowerShell the normal project control plane merely because historical evidence was captured there. Use Windows-side commands or GUI inspection only for a concrete host-only responsibility or when diagnosing a host-side failure that WSL/HTTP cannot expose.

## 2. Read-before-recheck rule

When a task touches local execution, Python, WSL2, GPU memory, LM Studio, local models, or local model networking:

1. read this file first;
2. reuse established durable facts by default;
3. do not request repeated inventory merely because a new chat/session started;
4. re-check only the smallest fact needed when freshness materially matters;
5. preserve new one-run evidence in `working-memory/` when it is consequential;
6. update this file only when the reusable baseline itself changes.

Freshness normally matters for:

- current free/used VRAM before a memory-sensitive operation;
- which model instance is loaded right now;
- inventory after Ali intentionally adds/removes models;
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

The authoritative package/dependency declaration is `pyproject.toml`; do not duplicate its full dependency list here as environment truth.

## 4. Hardware baseline

Reusable GPU identity:

```text
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
nominal VRAM: 8192 MiB
```

Use WSL for current GPU observation:

```bash
nvidia-smi
```

Compact snapshot when freshness is actually required:

```bash
nvidia-smi \
  --query-gpu=name,driver_version,memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu \
  --format=csv
```

Point-in-time VRAM usage, temperature, system-memory values, and load/unload measurements are evidence snapshots, not durable facts. Their historical records remain linked below.

The project does not currently require the laptop chassis/model, CPU model, or Windows build. Do not ask for them without a concrete technical reason.

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

Normal visibility checks:

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

`GET /api/v1/models` has been directly proven in Ali's environment. Historical controlled model loading used the host CLI. Before treating a particular native load/unload request shape as a reproducibility boundary, perform one narrow feature probe against the running server.

Do not broaden LM Studio exposure, enable CORS, bind to `0.0.0.0`, or modify firewall/authentication settings merely to simplify local project work.

If WSL localhost genuinely stops working, preserve the failure before trying a Windows-host gateway fallback.

### Ambient proxy caveat for loopback LM Studio traffic

A 2026-08-05 Step 7C live proof established that this WSL environment can contain ambient proxy variables pointing at a local Privoxy instance on `127.0.0.1:8080`. The observed `NO_PROXY`/`no_proxy` configuration used wildcard-like entries such as `127.*`, but `curl` still sent `http://127.0.0.1:12345/v1/models` through Privoxy and received `HTTP 500 Internal Privoxy Error`.

The same request with explicit proxy bypass:

```bash
curl --noproxy '*' http://127.0.0.1:12345/v1/models
```

connected directly to port `12345` and returned `HTTP 200 OK` from LM Studio.

Stable operational rule:

- local LM Studio product/client traffic must not inherit ambient `HTTP_PROXY`, `HTTPS_PROXY`, or `ALL_PROXY` configuration;
- product code uses a `requests.Session` with `trust_env = False` for the loopback provider boundary;
- manual LM Studio `curl` checks should use `--noproxy '*'` unless the shell is already known to have an exact working loopback exclusion;
- do not disable the user's VPN/proxy globally merely to run UpgradePilot;
- an HTTP 500 from a local-model probe is not automatically an LM Studio/model failure—inspect whether a proxy/interceptor actually answered.

This rule is both a reliability and privacy boundary: bounded release text/model prompts intended for local inference must not be silently routed through an unrelated proxy.

## 6. Adopted local semantic deployment environment

ADR-0006 owns the architectural decision to use one bounded local support-drop semantic extractor. This file records only the reusable deployment environment established for that decision.

Reusable deployment identity:

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

The deployment was observed to fit the local GPU and support the required structured-output transport. Detailed GPU measurements, model-evaluation scores, rejected comparison models, full inventory, latency samples, and semantic results remain evidence rather than environment baseline.

A change to model identity, quantization/deployment identity, chat template, LM Studio structured-output behavior, or material load configuration is a reassessment event for ADR-0006 rather than a silent environment substitution.

## 7. Model inventory policy

The complete model inventory captured on 2026-07-28 is intentionally **not** duplicated here. It is a dated snapshot and may become stale as models are added or removed.

Canonical historical inventory evidence:

- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json)

Do not download or substitute another model merely because a future assistant prefers one. Model selection follows the owning product responsibility and accepted architecture/evidence process.

## 8. GitHub credential caveat

A historical WSL observation established that an ambient `GITHUB_TOKEN` existed and produced HTTP 401 when inherited by a public GitHub REST proof; anonymous public access then passed. The token value was never recorded and must never be requested or exposed.

Stable operational rule:

- follow `SECURITY.md` for intentional credential use;
- public read-only validation should not silently inherit ambient authentication unless the selected proof requires it;
- distinguish authentication/environment failure from source/evidence/product failure.

Safe presence check:

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

- machine/GPU identity changes;
- normal WSL/project/venv path changes;
- normal Python baseline changes;
- LM Studio port/base URL or WSL transport changes;
- reusable local deployment identity changes after its owning architecture decision is updated;
- a recurring credential/network caveat is resolved or materially changes.

Do not update this file for every temporary process, free-memory value, one-run model instance, inventory snapshot, or experiment result.

`MEMORY.md` remains the sole live project-position owner.
