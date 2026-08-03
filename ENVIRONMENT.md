# UpgradePilot Local Environment Reference

**Purpose:** Durable project-local reference for Ali's development machine, WSL2 runtime, LM Studio setup, local model inventory, and recurring environment commands.

This file is **not** the live project-position owner. [`MEMORY.md`](MEMORY.md) owns what UpgradePilot is doing now. This file owns reusable environment facts so future AI assistants do not repeatedly ask Ali to restate or rediscover setup that the repository already establishes.

## Assistant rule — read before asking Ali

When work touches local execution, Python, WSL2, Windows/LM Studio, GPU memory, local models, or model-server networking:

1. read this file first;
2. reuse established facts unless there is concrete evidence they changed;
3. do **not** ask Ali to rerun inventory commands merely because a new conversation started;
4. re-check a fact only when the task materially depends on its *current instantaneous value* or when an observed failure/change makes the stored value stale;
5. when a re-check is genuinely required, ask only for the smallest missing/fresh observation and explain why the recorded evidence is insufficient.

Examples of facts that normally **do not** need repeated confirmation:

- Windows host + WSL2 development topology;
- UpgradePilot checkout and virtual-environment paths;
- RTX 3070 Laptop GPU identity and nominal 8 GiB VRAM;
- LM Studio's established loopback server port/base URL;
- previously captured model keys, quantizations, and file sizes;
- known successful LM Studio load configuration for the Gemma E4B control;
- the fact that WSL2 successfully reached LM Studio through `127.0.0.1:12345`.

Examples where freshness can matter:

- free/used VRAM immediately before a new memory-sensitive load;
- which model instance is loaded *right now*;
- model inventory after Ali intentionally downloads/removes a model;
- server reachability after LM Studio, WSL, firewall, or networking changes;
- driver/LM Studio identity after an upgrade;
- a reproducibility run whose proof obligation explicitly requires a new environment snapshot.

Do not turn a freshness-sensitive value into a permanent machine claim. Preserve the observation date.

---

## 1. Host and development topology

Established project topology:

```text
Windows laptop host
├── LM Studio desktop / local inference server
├── NVIDIA GeForce RTX 3070 Laptop GPU
└── WSL2
    └── UpgradePilot development/runtime environment
```

The project is developed from WSL2, while LM Studio runs on the Windows host.

### UpgradePilot checkout and Python environment

Last directly recorded on **2026-07-28**:

```text
repository: motafegh/UpgradePilot
WSL2 checkout: /home/motafeq/projects/UpgradePilot
Python: 3.12.3
virtual-environment interpreter: /home/motafeq/projects/UpgradePilot/.venv/bin/python3
```

Current package requirements also require:

```text
Python >= 3.12
```

Current active runtime dependencies in `pyproject.toml` are:

```text
requests>=2.32,<3
packaging>=26.2,<27
```

No OpenAI Python client, Pydantic, Instructor, LangChain, or LM Studio Python SDK is currently an active UpgradePilot runtime dependency merely because historical experiments evaluated them.

### Project Git behavior

Repository operating rules establish:

```text
ordinary development branch: main
ordinary changes: direct on main
feature branches / PRs: only when Ali explicitly requests them
```

A normal synchronization command used throughout the project is:

```bash
git pull --ff-only
```

The ordinary deterministic suite is:

```bash
python -m unittest discover -s tests -v
```

Use [`AGENTS.md`](AGENTS.md), [`MEMORY.md`](MEMORY.md), and the selected bounded plan for current governance and validation scope rather than treating this environment file as a project-status document.

---

## 2. Hardware baseline

### GPU

Observed on **2026-07-28**:

```text
GPU: NVIDIA GeForce RTX 3070 Laptop GPU
GPU driver: 610.74
nominal VRAM: 8192 MiB
```

Representative pre-model snapshots from the same investigation were approximately:

```text
used: 1392–1435 MiB
free: 6584–6627 MiB
temperature: 46–51 C
GPU utilization: ~1% at one baseline snapshot
```

The nominal 8192 MiB GPU identity is a reusable hardware fact. Free/used VRAM is dynamic and must not be assumed identical on another day.

### System memory

During the observed Gemma E4B run, WSL-visible memory was approximately:

```text
total: ~50 GiB
used: ~1.9 GiB
available: ~49 GiB
```

Treat this specifically as the **WSL-visible memory observation**, not as a separately proven laptop physical-RAM specification.

### Hardware details not established because UpgradePilot has not needed them

The repository does not currently establish an exact laptop chassis/model, CPU model, or a durable Windows build number. Do not ask for these during ordinary UpgradePilot work unless a concrete hardware-specific responsibility actually requires them.

---

## 3. LM Studio server baseline

### Established server identity and transport

Observed across the **2026-07-28** LM Studio evidence captures:

```text
LM Studio CLI identity: commit 71bd99c
server running: true
server port: 12345
listener address: 127.0.0.1
just-in-time model loading: active
WSL2 localhost transport: successful
```

Exact listener evidence:

```text
127.0.0.1:12345
```

WSL2 successfully queried:

```text
http://127.0.0.1:12345/v1/models
```

Therefore the established baseline URL for OpenAI-compatible calls is:

```text
http://127.0.0.1:12345/v1
```

and the native LM Studio model-inventory endpoint used by UpgradePilot is:

```text
http://127.0.0.1:12345/api/v1/models
```

### Available endpoint families observed

LM Studio reported these OpenAI-compatible routes:

```text
GET  /v1/models
POST /v1/responses
POST /v1/chat/completions
POST /v1/completions
POST /v1/embeddings
```

Native LM Studio endpoints are also available; UpgradePilot has used `/api/v1/models` for richer local-model and loaded-instance metadata.

### Network boundary

Observed baseline:

- listener was loopback-only (`127.0.0.1`);
- an unauthenticated loopback `/v1/models` request was accepted;
- WSL2 localhost access worked directly;
- no WSL gateway fallback was required for this baseline;
- no CORS change was required;
- no non-loopback bind was required;
- no firewall or authentication setting was broadened.

This does **not** mean gateway networking, firewall, binding, authentication, or CORS are unimportant concepts. A separate learning plan exists for that boundary. It means ordinary local inference should begin from the already-proven loopback path instead of re-opening networking variables.

Do not enable CORS, bind LM Studio to `0.0.0.0`, or broaden network exposure merely because a new assistant wants to inspect the environment.

### LM Studio logs

The Windows LM Studio server log location recorded by the project is:

```text
C:\Users\lenovo\.cache\lm-studio\server-logs
```

Useful CLI log streams used during diagnostics include:

```powershell
lms log stream --source model --filter input,output --json
lms log stream --source model --filter output --stats
```

Do not commit unrelated/private prompts from these logs.

---

## 4. Known LM Studio commands

These commands have already been identified and used/reviewed during UpgradePilot's local-model investigations. Future assistants should not ask Ali to discover them again from scratch.

### Server and inventory

Windows PowerShell:

```powershell
lms --version
lms server status --json --quiet
lms ls --llm --json
lms ps --json
```

GPU inspection:

```powershell
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used,memory.free --format=csv
nvidia-smi
```

WSL2 model endpoints:

```bash
curl -fsS http://127.0.0.1:12345/v1/models | python3 -m json.tool
curl -fsS http://127.0.0.1:12345/api/v1/models | python3 -m json.tool
```

Historical fallback command when localhost is genuinely unavailable:

```bash
WINDOWS_HOST="$(ip route show default | awk '/default/ {print $3; exit}')"
curl -fsS "http://${WINDOWS_HOST}:12345/v1/models" | python3 -m json.tool
```

Do not try the gateway merely for ceremony when localhost remains functional.

### Model sizing

Known estimation form:

```powershell
lms load --estimate-only <MODEL_KEY> --context-length 4096 --gpu max
lms load --estimate-only <MODEL_KEY> --context-length 8192 --gpu max
```

The July 2026 estimator proved too weight-dominated to answer every deployment question reliably; real observed load evidence is stronger when a model must actually be selected.

### Model load/unload controls

Known commands:

```powershell
lms unload --all
lms load <MODEL_KEY> ...
lms unload <INSTANCE_IDENTIFIER>
```

The installed CLI exposed the positive simple-speculative option but **did not** recognize:

```text
--no-speculative-draft-simple
```

For the observed Gemma control, omitting the positive simple-speculative flag left simple speculative decoding disabled, which was verified through native metadata.

---

## 5. Model inventory snapshot

**Snapshot date:** 2026-07-28  
**Source:** LM Studio native `GET /api/v1/models` response preserved under `working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json`.

This is a **last-observed inventory**, not a claim that Ali can never add/remove models later.

| Model key | Type | Publisher | Params | Quantization | Approx size | Max context | Notes |
|---|---|---|---:|---|---:|---:|---|
| `gemma-4-12b-it-qat` | LLM | lmstudio-community | 12B | Q4_0 | 6.497 GiB | 262,144 | no vision; tool use; reasoning default on |
| `google/gemma-4-12b` | LLM | google | 12B | Q4_K_M | 7.038 GiB | 131,072 | vision; tool use; reasoning default on |
| `qwopus3.5-9b-coder-mtp` | LLM | lmstudio-community | 9B | Q4_K_S | 5.112 GiB | 262,144 | coder/community-specialized |
| `qwen3.6-35b-a3b-ud` | LLM | lmstudio-community | 35B-A3B | IQ2_M | 10.731 GiB | 262,144 | MoE; too large for clean 8 GiB-GPU first candidate |
| `qwen3.5-27b-claude-4.6-opus-reasoning-distilled.i1` | LLM | lmstudio-community | 27B | IQ3_S | 11.255 GiB | 262,144 | community distilled; large |
| `qwen3.5-9b-ud` | LLM | lmstudio-community | 9B | Q4_K_XL | 5.556 GiB | 262,144 | primary general-language candidate; reasoning default on |
| `gemma-4-e2b-it` | LLM | lmstudio-community | 4.6B | Q4_K_M | 3.192 GiB | 131,072 | historical rejected semantic control |
| `qwen3.5-4b-uncensored-hauhaucs-aggressive` | LLM | lmstudio-community | 4B | Q8_0 | 4.175 GiB | 262,144 | deliberately excluded from evidence extraction |
| `gemma-4-e4b-it-ud` | LLM | lmstudio-community | 7.5B | Q4_K_XL | 4.751 GiB | 131,072 | primary architecture-diverse candidate; observed load available |
| `qwen2.5-0.5b-instruct` | LLM | lmstudio-community | 0.5B | Q8_0 | 0.495 GiB | 32,768 | weak control |
| `qwen2.5-coder-0.5b-instruct` | LLM | lmstudio-community | 0.5B | Q8_0 | 0.495 GiB | 32,768 | coder; weak control |
| `qwen2.5-coder-7b-instruct` | LLM | tensorblock | 7B | Q3_K_M | 3.547 GiB | 32,768 | optional coder control |
| `ministral-3-3b-instruct-2512` | LLM | lmstudio-community | 3B | Q4_K_M | 2.782 GiB | 262,144 | vision reported true; tool use |
| `qwen3-8b-thinking-2507` | LLM | lmstudio-community | 8B | Q4_K_M | 4.682 GiB | 262,144 | secondary reasoning candidate |
| `qwen3-4b-instruct-2507` | LLM | lmstudio-community | 4B | Q6_K | 3.079 GiB | 262,144 | historical rejected semantic control |
| `qwen3-4b-thinking-2507` | LLM | lmstudio-community | 4B | Q6_K | 3.079 GiB | 262,144 | historical/secondary control |
| `text-embedding-nomic-embed-text-v1.5` | embedding | nomic-ai | — | Q4_K_M | 0.078 GiB | 2,048 | not an extraction LLM |
| `text-embedding-mxbai-embed-large-v1` | embedding | mixedbread-ai | 335M | F16 | 0.624 GiB | 512 | not an extraction LLM |

At the captured pre-load snapshot, native inventory showed **no loaded model instances**.

### Previously selected comparison ladder

The project narrowed the first serious candidate set to:

```text
1. gemma-4-e4b-it-ud
   best expected hardware fit / architecture-diverse control

2. qwen3.5-9b-ud
   stronger likely general semantic candidate

3. gemma-4-12b-it-qat
   stretch quality candidate with partial-offload risk
```

`qwen3-8b-thinking-2507` remained a secondary comparison, and `qwen2.5-coder-7b-instruct` an optional specialization control.

Do not download another model merely because a future assistant has a favorite model. Existing candidates must first be evaluated against the selected UpgradePilot responsibility unless the current plan explicitly authorizes a new download.

---

## 6. Observed Gemma E4B deployment control

A real load and strict JSON-Schema smoke were executed on **2026-07-28**. This is valuable reusable deployment evidence and should not be rediscovered from scratch.

### Load request

The successful control used:

```text
model: gemma-4-e4b-it-ud
instance identifier: upgradepilot-gemma-e4b-smoke
context length: 4096
GPU request: max
parallelism: 1
TTL: 900 seconds
MTP speculative decoding: disabled
simple speculative decoding: disabled
```

Successful PowerShell load form:

```powershell
lms unload --all

lms load gemma-4-e4b-it-ud `
  --context-length 4096 `
  --gpu max `
  --parallel 1 `
  --ttl 900 `
  --identifier upgradepilot-gemma-e4b-smoke `
  --no-speculative-draft-mtp `
  -y
```

### Actual applied configuration

Native LM Studio metadata reported:

```text
model key: gemma-4-e4b-it-ud
architecture: gemma4
parameters: 7.5B
quantization: Q4_K_XL (4 bits/weight)
file size: 5,101,713,792 bytes
context length: 4096
eval batch: 2048
physical batch: 512
parallel: 1
Flash Attention: true
KV cache offloaded to GPU: true
MTP speculative decoding: false
simple speculative decoding: false
```

LM Studio reported the model loaded successfully in approximately:

```text
1m 1.09s
reported model load: 4.75 GiB
```

### Observed resource behavior

| Point | GPU used | GPU free | GPU temp |
|---|---:|---:|---:|
| before load | 1392 MiB | 6627 MiB | 51 C |
| after load | 4759 MiB | 3260 MiB | 53 C |
| after smoke | 4792 MiB | 3227 MiB | 54 C |
| after unload | 1175 MiB | 6844 MiB | 54 C |

The load succeeded without observed OOM, guardrail failure, CPU-fallback message, crash, restart, or UI instability. The inspected endpoints did not expose an actual offloaded-layer count, so do not invent one.

### Structured-output capability

The OpenAI-compatible route used was:

```text
POST http://127.0.0.1:12345/v1/chat/completions
```

with strict `response_format.type = json_schema`, temperature `0`, seed `0`, non-streaming mode, and bounded output tokens.

Observed smoke mechanics:

```text
transport: pass
outer JSON: pass
inner JSON: pass
schema shape: pass
finish_reason: stop
exact source grounding: pass
```

The broader historical smoke failed its semantic-state consistency gate (`state: unresolved` while returning a grounded fix and no unresolved reasons). That failure is model/contract evaluation evidence, not an environment failure.

The current Step 6 support-drop contract is narrower than that historical four-category smoke, so this deployment remains useful as an operational control without implying semantic adoption.

### Historical small-model results

Earlier local semantic experiments rejected normal adoption of:

```text
gemma-4-e2b-it (Q4_K_M)
qwen3-4b-instruct-2507 (Q6_K)
```

because schema-valid/grounded-looking outputs still produced material semantic errors, including false dropped-support claims. Do not treat JSON Schema success as semantic trust.

---

## 7. GitHub credential caveat observed during live Step 5

Observed on **2026-08-03**:

- the WSL2 shell had a `GITHUB_TOKEN` environment variable set;
- its value was not printed or recorded;
- UpgradePilot's read-only public GitHub REST client received HTTP `401` when it sent that token as a Bearer credential;
- `unset GITHUB_TOKEN` removed the stale/invalid token from the current shell;
- the same public S001 live proof then passed anonymously;
- `git pull --ff-only` had already succeeded, showing Git's repository authentication path was separate from this environment variable.

Future assistants must **never** ask Ali to reveal or paste the token value.

To test presence safely without printing the secret:

```bash
if [[ -n "${GITHUB_TOKEN:-}" ]]; then
    echo "GITHUB_TOKEN is set"
else
    echo "GITHUB_TOKEN is not set"
fi
```

For a read-only public GitHub API proof that does not require authenticated rate limits, a clean one-command invocation can be:

```bash
env -u GITHUB_TOKEN <COMMAND>
```

Do not globally remove or replace credentials unless the selected task actually requires that change.

---

## 8. Environment evidence provenance

Primary reusable evidence records:

- [`working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md`](working-memory/2026-07-28_B2-lm-studio-server-and-instructor-assessment.md)
- [`working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md`](working-memory/2026-07-28_B2-local-model-inventory-and-candidate-shortlist.md)
- [`working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md`](working-memory/2026-07-28_B2-model-metadata-and-networking-sequencing-correction.md)
- [`working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md`](working-memory/2026-07-28_B2-first-observed-gemma-e4b-load-and-smoke.md)
- [`working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md`](working-memory/2026-07-28_B2-gemma-e4b-observed-evaluation-result.md)
- [`working-memory/evidence/2026-07-28-gemma-e4b/`](working-memory/evidence/2026-07-28-gemma-e4b/)

Exact native pre-load model snapshot:

- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/native-models.json)

Exact listener evidence:

- [`working-memory/evidence/2026-07-28-gemma-e4b/server-listener.json`](working-memory/evidence/2026-07-28-gemma-e4b/server-listener.json)

LM Studio CLI identity evidence:

- [`working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/lms-version.stdout.txt`](working-memory/evidence/2026-07-28-gemma-e4b/snapshots/pre-load/lms-version.stdout.txt)

These dated files remain the raw/historical evidence. This `ENVIRONMENT.md` is the reusable consolidated reference.

---

## 9. Maintenance policy

Update this file when a durable or reusable environment fact materially changes, for example:

- UpgradePilot moves to a different machine/GPU;
- WSL2/project path changes;
- the normal Python/venv changes;
- LM Studio's normal port/base URL changes;
- a model becomes the accepted reusable local deployment control;
- the model inventory is intentionally replaced and future work would otherwise use stale keys;
- a recurring credential/network caveat is resolved or replaced.

Do **not** update this file for every temporary process, one-off free-memory value, or short-lived loaded instance unless that observation becomes reusable project knowledge.

When a task needs a fresh instantaneous observation, preserve it in a dated `working-memory/` record and update this file only if it changes the reusable baseline.

`MEMORY.md` remains the sole owner of the live project position and exact next action.