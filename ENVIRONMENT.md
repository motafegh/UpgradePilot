# UpgradePilot Local Environment Reference

**Purpose:** Durable project-local reference for Ali's development machine, WSL2 runtime, LM Studio service boundary, GPU/model environment, and recurring local-execution rules.

This file is **not** the live project-position owner. [`MEMORY.md`](MEMORY.md) owns what UpgradePilot is doing now. This file owns reusable environment facts so future AI assistants do not repeatedly ask Ali to restate or rediscover setup already established by repository evidence.

## Core operating rule — WSL is the control plane

UpgradePilot work is performed from the project's **WSL2 environment**.

Use this mental model:

```text
Windows laptop host
├── NVIDIA GPU
├── LM Studio application/server process
└── WSL2  ← UpgradePilot control plane
    ├── repository and Git
    ├── Python virtual environment
    ├── tests and tools
    ├── curl / HTTP model-server control
    ├── nvidia-smi / runtime observation
    └── product and experiment execution
```

The fact that LM Studio's process runs on Windows does **not** make Windows PowerShell the normal UpgradePilot execution environment.

Default rule:

```text
project action
→ run from WSL
→ communicate with LM Studio over localhost HTTP
```

Windows-side commands, PowerShell, GUI inspection, or host-specific tooling are exceptions. Use them only when a concrete responsibility cannot be performed from WSL or when diagnosing a host-side LM Studio problem that the HTTP boundary cannot expose.

Do not ask Ali to switch to PowerShell merely because historical July evidence happened to be captured that way.

---

## Assistant rule — read before asking Ali

When work touches local execution, Python, WSL2, LM Studio, GPU memory, local models, or model-server networking:

1. read this file first;
2. assume WSL as the execution shell unless a specific host-only need is demonstrated;
3. reuse established facts unless there is concrete evidence they changed;
4. do **not** ask Ali to rerun inventory commands merely because a new conversation started;
5. re-check a fact only when the task materially depends on its current instantaneous value or an observed failure/change makes the stored value stale;
6. when a re-check is genuinely required, request only the smallest WSL-side observation needed;
7. use Windows-side commands only as an explicit exception, never as the default environment workflow.

Facts that normally do **not** need repeated confirmation:

- UpgradePilot runs from WSL2;
- repository and virtual-environment paths;
- RTX 3070 Laptop GPU identity and nominal 8 GiB VRAM;
- LM Studio's established loopback server at port `12345`;
- WSL2 can reach LM Studio through `127.0.0.1:12345`;
- previously captured model keys, quantizations, and sizes;
- known observed Gemma E4B deployment behavior.

Freshness can matter for:

- free/used VRAM immediately before a memory-sensitive experiment;
- which model instance is loaded right now;
- model inventory after Ali intentionally downloads/removes models;
- server reachability after an actual LM Studio/WSL/network configuration change;
- driver or LM Studio identity after an upgrade;
- a proof obligation that explicitly requires a fresh environment snapshot.

A new session is not evidence that the environment changed.

---

## 1. UpgradePilot WSL runtime

Last directly recorded on **2026-07-28**:

```text
repository: motafegh/UpgradePilot
checkout: /home/motafeq/projects/UpgradePilot
Python: 3.12.3
virtual-environment interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
```

Current package requirement:

```text
Python >= 3.12
```

Current active runtime dependencies:

```text
requests>=2.32,<3
packaging>=26.2,<27
```

No OpenAI Python client, Pydantic, Instructor, LangChain, or LM Studio Python SDK is an active UpgradePilot runtime dependency merely because historical experiments evaluated them.

### Normal WSL commands

Repository synchronization:

```bash
git pull --ff-only
```

Full deterministic suite:

```bash
python -m unittest discover -s tests -v
```

Python identity when genuinely needed:

```bash
python --version
python -c 'import sys; print(sys.executable)'
```

Git, Python, product tools, experiments, validation, and ordinary environment inspection should all remain in this shell.

---

## 2. Hardware baseline

### GPU

Observed on **2026-07-28**:

```text
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
last recorded driver: 610.74
nominal VRAM: 8192 MiB
```

Representative pre-model snapshots were approximately:

```text
used: 1392–1435 MiB
free: 6584–6627 MiB
temperature: 46–51 C
```

GPU identity and nominal VRAM are reusable. Free/used memory is dynamic.

### WSL GPU observation

Use `nvidia-smi` from WSL as the normal inspection path:

```bash
nvidia-smi
```

For a compact memory snapshot:

```bash
nvidia-smi \
  --query-gpu=name,driver_version,memory.total,memory.used,memory.free,utilization.gpu,temperature.gpu \
  --format=csv
```

Only use a Windows-side GPU command if WSL GPU visibility itself is the problem being diagnosed.

### System memory

During the observed Gemma E4B run, WSL-visible memory was approximately:

```text
total: ~50 GiB
used: ~1.9 GiB
available: ~49 GiB
```

Treat that specifically as a WSL-visible runtime observation, not a separately established physical-RAM specification.

The repository does not currently need the laptop chassis/model, CPU model, or Windows build. Do not ask for them without a concrete technical reason.

---

## 3. LM Studio service boundary

LM Studio runs on the Windows host, but UpgradePilot interacts with it from WSL as a local network service.

Observed baseline on **2026-07-28**:

```text
LM Studio CLI identity captured historically: commit 71bd99c
server running: true
server port: 12345
listener: 127.0.0.1
just-in-time model loading: active
WSL2 localhost transport: successful
```

Established OpenAI-compatible base URL:

```text
http://127.0.0.1:12345/v1
```

Established native LM Studio API base:

```text
http://127.0.0.1:12345/api/v1
```

### Proven WSL endpoints

OpenAI-compatible model listing:

```bash
curl -fsS http://127.0.0.1:12345/v1/models \
  | python -m json.tool
```

Native model inventory / loaded-instance metadata:

```bash
curl -fsS http://127.0.0.1:12345/api/v1/models \
  | python -m json.tool
```

OpenAI-compatible inference:

```text
POST http://127.0.0.1:12345/v1/chat/completions
```

These are the normal UpgradePilot LM Studio interfaces.

### Native REST model management

LM Studio's native v1 REST API provides model-management endpoints in current LM Studio releases, including:

```text
POST /api/v1/models/load
POST /api/v1/models/unload
```

For UpgradePilot, prefer this WSL→HTTP control path over Windows PowerShell when explicit load/unload control is needed.

Important evidence distinction:

- this project has directly proven `GET /api/v1/models` on Ali's server;
- July's exact controlled Gemma load was historically performed through the host CLI;
- therefore, before relying on a native load/unload request as a reproducibility boundary, perform one narrow feature probe against Ali's running server rather than assuming every current documentation feature from the historical CLI identity.

Because JIT model loading is already established as active, a basic Step 6 transport/schema smoke does **not** require PowerShell or explicit preloading: an inference request can address a downloaded model key and allow LM Studio to load it on demand.

For later scored experiments, where context length/load configuration must be frozen, prefer native REST load control from WSL if the installed server accepts it.

### Network boundary

Observed baseline:

- listener was loopback-only (`127.0.0.1`);
- WSL localhost access worked;
- no gateway fallback was needed;
- no CORS change was needed;
- no non-loopback bind was needed;
- no firewall or authentication setting was broadened.

Do not enable CORS, bind LM Studio to `0.0.0.0`, or broaden host exposure simply to make local UpgradePilot work easier.

Historical gateway fallback, only if localhost genuinely stops working:

```bash
WINDOWS_HOST="$(ip route show default | awk '/default/ {print $3; exit}')"
curl -fsS "http://${WINDOWS_HOST}:12345/v1/models" \
  | python -m json.tool
```

Preserve a localhost failure before changing the networking boundary.

---

## 4. WSL-first LM Studio workflow

### A. Check server/model visibility

```bash
curl -fsS http://127.0.0.1:12345/v1/models \
  | python -m json.tool
```

For richer local metadata:

```bash
curl -fsS http://127.0.0.1:12345/api/v1/models \
  | python -m json.tool
```

### B. Inspect GPU state

```bash
nvidia-smi
```

### C. Run inference

Use the project venv and `requests`, or `curl` for a diagnostic request, from WSL.

```text
WSL Python / requests
→ 127.0.0.1:12345
→ LM Studio
→ selected downloaded model
```

### D. Explicit model load when a frozen deployment is required

Preferred control path:

```text
WSL
→ POST /api/v1/models/load
→ LM Studio native REST API
```

Representative request shape:

```bash
curl -fsS http://127.0.0.1:12345/api/v1/models/load \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "gemma-4-e4b-it-ud",
    "context_length": 4096,
    "flash_attention": true,
    "offload_kv_cache_to_gpu": true,
    "echo_load_config": true
  }' \
  | python -m json.tool
```

Do not treat this exact load request as already validated against Ali's installed server until one real request succeeds. It is the preferred WSL-native control direction, replacing PowerShell as the default operational approach.

### E. Explicit unload

Prefer the corresponding native REST unload endpoint from WSL when supported by the installed server.

If a specific REST capability is unavailable on the installed LM Studio build, classify that as an interface limitation. Do not automatically move the whole workflow to Windows. For a one-off host-only control that genuinely cannot be achieved through HTTP/JIT, use the narrowest exception possible.

---

## 5. Historical Windows/CLI evidence — not the default workflow

Some July 2026 environment evidence was captured using LM Studio's Windows-side `lms` CLI. Those commands remain useful **historical provenance** because they produced exact observed configuration evidence.

They are not the normal instructions for future UpgradePilot work.

Historical observations include:

```text
CLI commit: 71bd99c
server port: 12345
Gemma E4B explicit load control
model load/unload observations
LM Studio log capture
```

If an old working-memory record says "Run from Windows PowerShell," interpret it as the historical procedure for that dated experiment, not as a standing project rule.

The current standing rule is WSL-first.

---

## 6. Model inventory snapshot

**Snapshot date:** 2026-07-28  
**Source:** native `GET /api/v1/models` evidence preserved in the repository.

This is a last-observed inventory, not a claim that models can never be added or removed.

| Model key | Type | Publisher | Params | Quantization | Approx size | Max context | Notes |
|---|---|---|---:|---|---:|---:|---|
| `gemma-4-12b-it-qat` | LLM | lmstudio-community | 12B | Q4_0 | 6.497 GiB | 262,144 | stretch candidate |
| `google/gemma-4-12b` | LLM | google | 12B | Q4_K_M | 7.038 GiB | 131,072 | vision; poor 8 GiB fit |
| `qwopus3.5-9b-coder-mtp` | LLM | lmstudio-community | 9B | Q4_K_S | 5.112 GiB | 262,144 | coder/community-specialized |
| `qwen3.6-35b-a3b-ud` | LLM | lmstudio-community | 35B-A3B | IQ2_M | 10.731 GiB | 262,144 | too large for clean first candidate |
| `qwen3.5-27b-claude-4.6-opus-reasoning-distilled.i1` | LLM | lmstudio-community | 27B | IQ3_S | 11.255 GiB | 262,144 | large/community distilled |
| `qwen3.5-9b-ud` | LLM | lmstudio-community | 9B | Q4_K_XL | 5.556 GiB | 262,144 | primary general semantic candidate |
| `gemma-4-e2b-it` | LLM | lmstudio-community | 4.6B | Q4_K_M | 3.192 GiB | 131,072 | historical rejected control |
| `qwen3.5-4b-uncensored-hauhaucs-aggressive` | LLM | lmstudio-community | 4B | Q8_0 | 4.175 GiB | 262,144 | excluded from evidence extraction |
| `gemma-4-e4b-it-ud` | LLM | lmstudio-community | 7.5B | Q4_K_XL | 4.751 GiB | 131,072 | observed operational control |
| `qwen2.5-0.5b-instruct` | LLM | lmstudio-community | 0.5B | Q8_0 | 0.495 GiB | 32,768 | weak control |
| `qwen2.5-coder-0.5b-instruct` | LLM | lmstudio-community | 0.5B | Q8_0 | 0.495 GiB | 32,768 | weak coder control |
| `qwen2.5-coder-7b-instruct` | LLM | tensorblock | 7B | Q3_K_M | 3.547 GiB | 32,768 | optional coder control |
| `ministral-3-3b-instruct-2512` | LLM | lmstudio-community | 3B | Q4_K_M | 2.782 GiB | 262,144 | secondary |
| `qwen3-8b-thinking-2507` | LLM | lmstudio-community | 8B | Q4_K_M | 4.682 GiB | 262,144 | secondary reasoning candidate |
| `qwen3-4b-instruct-2507` | LLM | lmstudio-community | 4B | Q6_K | 3.079 GiB | 262,144 | historical rejected control |
| `qwen3-4b-thinking-2507` | LLM | lmstudio-community | 4B | Q6_K | 3.079 GiB | 262,144 | historical/secondary control |
| `text-embedding-nomic-embed-text-v1.5` | embedding | nomic-ai | — | Q4_K_M | 0.078 GiB | 2,048 | not extraction LLM |
| `text-embedding-mxbai-embed-large-v1` | embedding | mixedbread-ai | 335M | F16 | 0.624 GiB | 512 | not extraction LLM |

At that captured pre-load snapshot, native inventory showed no loaded model instances.

Previously selected comparison ladder:

```text
1. gemma-4-e4b-it-ud
   best observed hardware fit / architecture-diverse control

2. qwen3.5-9b-ud
   stronger likely general semantic candidate

3. gemma-4-12b-it-qat
   stretch quality candidate
```

Do not download another model merely because a future assistant prefers one. Use evidence from the selected UpgradePilot responsibility first.

---

## 7. Observed Gemma E4B deployment evidence

A real deployment and strict JSON-Schema smoke were observed on **2026-07-28**.

The observed configuration was:

```text
model: gemma-4-e4b-it-ud
historical instance identifier: upgradepilot-gemma-e4b-smoke
context length: 4096
GPU request: max
parallelism: 1
Flash Attention: true
KV cache on GPU: true
MTP speculative decoding: false
simple speculative decoding: false
```

Native metadata reported:

```text
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL
file size: 5,101,713,792 bytes
context length: 4096
eval batch: 2048
physical batch: 512
parallel: 1
```

Observed resource behavior:

| Point | GPU used | GPU free | GPU temp |
|---|---:|---:|---:|
| before load | 1392 MiB | 6627 MiB | 51 C |
| after load | 4759 MiB | 3260 MiB | 53 C |
| after smoke | 4792 MiB | 3227 MiB | 54 C |
| after unload | 1175 MiB | 6844 MiB | 54 C |

The load succeeded without observed OOM, crash, restart, or UI instability.

Strict OpenAI-compatible JSON-Schema request mechanics were also proven operationally:

```text
transport: pass
outer JSON: pass
inner JSON: pass
schema shape: pass
finish_reason: stop
exact source grounding: pass
```

The historical broader semantic smoke failed a semantic-state consistency gate. That is model/contract evidence, not an environment failure, and does not imply model adoption.

Earlier small-model semantic deployments `gemma-4-e2b-it` and `qwen3-4b-instruct-2507` were rejected for normal semantic extraction because structured/grounded-looking output still produced material semantic errors.

---

## 8. GitHub credential caveat

Observed on **2026-08-03**:

- WSL had a `GITHUB_TOKEN` environment variable set;
- its value was never printed or recorded;
- UpgradePilot's public GitHub REST path received HTTP 401 when that token was sent;
- removing it from the current shell allowed the public live proof to pass anonymously;
- Git repository authentication was a separate mechanism because `git pull --ff-only` already worked.

Never ask Ali to reveal a token value.

Safe presence test in WSL:

```bash
if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    echo "GITHUB_TOKEN is set"
else
    echo "GITHUB_TOKEN is not set"
fi
```

One-command public execution without that variable:

```bash
env -u GITHUB_TOKEN <COMMAND>
```

---

## 9. Evidence provenance

Primary historical records:

- [`working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md`](working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md)
- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md`](working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md)
- [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/`](working-memory/evidence/2026-07-28-gemma-e4b/)

Exact native inventory:

- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json)

Exact listener evidence:

- [`working-memory/evidence/2026-07-28-gemma-e4b/server-listener.json`](working-memory/evidence/2026-07-28-gemma-e4b/server-listener.json)

Historical CLI identity evidence:

- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/lms-version.stdout.txt`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/lms-version.stdout.txt)

Historical records may contain PowerShell commands because that was how those observations were captured. They do not override this file's WSL-first operating rule.

---

## 10. Maintenance policy

Update this file when a reusable environment fact materially changes, for example:

- UpgradePilot moves to another machine/GPU;
- WSL/project path changes;
- normal Python/venv changes;
- LM Studio's normal port/base URL changes;
- a different model becomes the reusable local deployment control;
- model inventory is intentionally replaced;
- WSL↔LM Studio transport changes;
- a recurring credential/network caveat is resolved.

Do not update this file for every temporary process, free-memory value, or short-lived model instance.

For freshness-sensitive evidence, use a dated `working-memory/` record. Update this file only when that observation changes the reusable baseline.

`MEMORY.md` remains the sole owner of live project position and exact continuation.