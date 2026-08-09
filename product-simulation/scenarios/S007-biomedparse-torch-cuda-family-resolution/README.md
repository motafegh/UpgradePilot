# S007 — BiomedParse Torch/CUDA Family Resolution

**Form:** untouched real public Dependabot PR with optional bounded package-resolution observation  
**Admission:** [`../../S007_CANDIDATE_SCREENING.md`](../../S007_CANDIDATE_SCREENING.md)  
**Target:** `microsoft/BiomedParse#96`  
**Claim boundary:** package-family/artifact/environment applicability and investigation ordering only

## Owned question

> Does the proposed BiomedParse dependency set form a coherent version/platform package family for the target's documented CUDA-12.4 environment, what exact evidence can establish or refute that proposition, and is any resolver observation still worth doing before deeper runtime semantics?

This scenario does **not** own global PyTorch-2.8 compatibility, GPU correctness, model-output correctness, performance, safety, or maintainer action.

## Frozen identity

```text
repository       microsoft/BiomedParse
pull request     96
base branch      v2
base SHA         ac054c43b0f6cb579e00fe7d28bfbf29716c62b3
head SHA         b8e53d5232ebb3e8068fed4fe79450f720665603
changed file     assets/requirements/requirements.txt
```

Proposal:

```text
torch==2.6.0+cu124
→
torch==2.8.0
```

Unchanged neighboring requirements:

```text
--extra-index-url https://download.pytorch.org/whl/cu124
torchvision==0.21.0+cu124
torchaudio==2.6.0+cu124
```

## Target context

At the exact base revision, the target README instructs:

```text
Python 3.10.14
pip install -r assets/requirements/requirements.txt
requirements assume CUDA 12.4
```

and demonstrates real PyTorch inference with CUDA-device selection and model execution.

Therefore the package family and CUDA environment are target-relevant, not merely unused metadata.

## Current evidence boundary

### Established directly

- exact PR/base/head/change identity;
- exact base and head requirements;
- target-documented Python 3.10.14 + CUDA-12.4 installation intent;
- direct target PyTorch runtime use;
- official PyTorch guidance pairs Torch 2.6.0 / TorchVision 0.21.0 / TorchAudio 2.6.0 and offers CUDA 12.4 for that family;
- official PyTorch guidance pairs Torch 2.8.0 / TorchVision 0.23.0 / TorchAudio 2.8.0 and lists CUDA 12.6 / 12.8 / 12.9 rather than CUDA 12.4;
- official CUDA-12.4 TorchVision index contains `torchvision-0.21.0+cu124` artifacts including Python-3.10 Linux x86_64;
- no public PR-head combined status or pull-request workflow run was obtained through the checked GitHub interfaces.

### Strong supporting evidence, not silently broadened

PyTorch issue `pytorch/pytorch#157476` preserves extracted metadata from an official Windows `torchvision-0.21.0+cu124` wheel showing:

```text
Requires-Dist: torch (==2.6.0+cu124)
```

This strongly supports coordinated-package exactness but is **not** being silently treated as direct metadata for every platform artifact.

### Still to establish or refute

- exact dependency metadata/resolver behavior for the target-relevant Python-3.10/Linux/CUDA-12.4 context;
- whether one bounded resolver observation adds material information beyond the static package-family evidence;
- exact final proposition state after that evidence is admitted;
- whether deeper runtime/API investigation remains inactive.

## Investigation discipline

No BiomedParse source, model weights, CUDA kernels, or target runtime are executed merely to investigate the first package-family proposition.

Before any resolver observation, freeze:

```text
remaining unresolved proposition
→ possible resolver observations
→ state change implied by each observation
→ why existing static evidence is insufficient
→ exact stop condition
```

If exact static evidence already resolves the owned proposition sufficiently, a resolver execution may be retained as optional corroboration or skipped entirely.

## Durable artifacts

Read in order:

1. [`artifacts/CASE_IDENTITY_AND_TARGET_CONTEXT.json`](artifacts/CASE_IDENTITY_AND_TARGET_CONTEXT.json)
2. [`artifacts/PACKAGE_FAMILY_EVIDENCE.json`](artifacts/PACKAGE_FAMILY_EVIDENCE.json)
3. [`artifacts/PROPOSITION_MAP.json`](artifacts/PROPOSITION_MAP.json)

Later artifacts are created only if a distinct responsibility is activated.

## Sources

Target:

- https://github.com/microsoft/BiomedParse/pull/96
- https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/assets/requirements/requirements.txt
- https://github.com/microsoft/BiomedParse/blob/b8e53d5232ebb3e8068fed4fe79450f720665603/assets/requirements/requirements.txt
- https://github.com/microsoft/BiomedParse/blob/ac054c43b0f6cb579e00fe7d28bfbf29716c62b3/README.md

Upstream:

- https://pytorch.org/get-started/previous-versions/
- https://download.pytorch.org/whl/cu124/torchvision/
- https://github.com/pytorch/vision
- https://github.com/pytorch/pytorch/issues/157476

## Stop line

Stop this scenario when the package-family/environment proposition, investigation choice, and remaining uncertainty are bounded well enough to compare with S003/S006 and Conversation C.

Do not continue into a general PyTorch migration review simply because more release-note mechanisms or runtime checks exist.