# M2-S03 Evidence-to-Report Vertical Slice Plan

**Status:** Current controlling implementation plan
**Owner:** Ali Rajabi
**Milestone:** M2 — first automated vertical slice
**Starting point:** M2-S01 trusted case/evidence contracts and the closed M2-S02 extraction experiment

## 1. Outcome

Given one bounded real PR input and its supplied/replayed evidence, UpgradePilot
must produce one reproducible machine-readable and human-readable evidence report
with a deterministic decision or explicit abstention.

```text
raw case input + supplied/replayed evidence
→ strict case and evidence contracts
→ preserved observations and attributed claims
→ deterministic decision policy
→ traceable machine report + human report
```

This is the complete remaining M2 responsibility. It is not an extraction-only
slice and does not require an adopted LLM.

## 2. Starting evidence and method disposition

M2-S01 established strict case identity and evidence contracts. M2-S02 proved
the local structured-output transport but rejected both tested local deployments
for normal semantic extraction:

- `gemma-4-e2b-it`: 9/14 correct grounded claims and 11/14 correct decision
  effects in the complete run;
- `qwen3-4b-instruct-2507`: 8/14 correct grounded claims and 10/14 correct
  decision effects in the complete run;
- focused repeated cases reproduced material false dropped-support claims;
- the mandatory second-model detector and phrase/category regexes were rejected
  as normal runtime controls;
- schemas, raw preservation, quotation, provenance, model-derived authority, and
  bounded deterministic decision effects remain accepted controls.

The experimental clients, evaluators, tests, and JSON artifacts remain negative
evidence. They do not make an LLM part of the M2 supported core.

## 3. Required behavior

The slice must:

1. consume the real bounded input form already represented by the case contract;
2. preserve raw observations and evidence identity without converting source
   claims into corroborated truth;
3. keep missing, rejected, invalid, unsupported, and not-applicable evidence
   distinguishable where activated;
4. assemble the current evidence and decision contracts through one application
   entry point;
5. produce versionable machine-readable output and a useful human-readable
   report from the same application result;
6. trace every material report statement to evidence, policy output, or an
   explicit limitation;
7. abstain when available evidence cannot support a stronger outcome;
8. reproduce the result without credentials, live network acquisition, or a
   locally loaded model;
9. demonstrate a changed or missing-evidence case whose report and decision
   change for an explainable reason.

If no accepted automated semantic extractor exists, the report must preserve the
release-note observation and its unresolved interpretation. A caller-supplied
semantic answer must not be disguised as automated extraction.

## 4. Deliverables

- an application-level input/result contract that composes case identity,
  evidence, decision, limitations, and report provenance;
- one bounded orchestration entry point for the vertical slice;
- deterministic serialization for the machine-readable report;
- a concise human renderer that does not overstate evidence;
- a runnable bounded interface or command if it materially improves clean-run
  reproduction;
- unit tests for contracts and rendering;
- integration tests from raw case/evidence input to both outputs;
- a changed/missing-evidence test and an invalid-input test;
- a recorded clean-run command and output for the selected real PR case;
- a working-memory update covering behavior, failures, limits, assistance, and
  the M2 pass assessment.

## 5. Design constraints

- Application, serialized, and human-report representations remain separate.
- Report fields must be derived from trusted contracts, not arbitrary model JSON.
- Evidence quotation/attribution is not corroboration.
- No report label such as `safe`, `compatible`, or `ready to merge` may be
  inferred from absent or favorable model-derived claims.
- The deterministic decision module remains the only current decision authority.
- Prefer an explicit small composition over a new framework or speculative
  package hierarchy.
- Educational comments should explain non-obvious trust or provenance
  boundaries, not narrate obvious syntax.

## 6. Proof matrix

| Proof | Expected evidence |
|---|---|
| Real selected PR case | Both report forms identify the same case revision and evidence |
| Missing repository-support evidence | Limitation remains visible and policy abstains or requests targeted checks according to current authority rules |
| Changed evidence case | Output changes deterministically and the reason is traceable |
| Invalid raw input | Fails as caller/contract invalidity, not as missing external evidence |
| Serialization | Stable schema/version marker and no hidden Python-only values |
| No-model clean run | Supported M2 path succeeds with LM Studio unavailable |
| Security boundary | Untrusted source text cannot add fields, authority, tools, or actions |
| Regression | Full repository test suite, compilation, imports, and diff checks pass |

## 7. Stop line

Do not add during M2-S03:

- live GitHub, PyPI, or web acquisition;
- cross-source corroboration that requires unavailable package/repository/CI data;
- a database, queue, service, cloud deployment, RAG, graph, agent, or workflow framework;
- another model-selection round;
- category-specific phrase lists or deterministic language interpreters;
- LLM-controlled recommendations or actions.

Those are later responsibilities only when their milestone admits them.

## 8. Pass condition and continuation

M2-S03 passes when a clean command reproduces both report forms for the real
case, central behavior is tested, degraded evidence remains explicit, a changed
case behaves correctly, and Ali can locate and explain the path and its limits.

After that evidence is reviewed, close M2 and continue to M3 reliable acquisition,
replay, persistence, diagnostics, and CI. Reconsider learned extraction only
under the comparative admission rules of M6 unless earlier project evidence
creates a newly authorized need.
