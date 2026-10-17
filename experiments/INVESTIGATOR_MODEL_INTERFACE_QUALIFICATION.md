# Investigator deployment and stateless model-interface qualification

This experiment qualifies the real local model/request boundary after the model-free
[mechanical bridge](INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md). The
[integration plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md)
owns budgets/fairness/gates; [MEMORY](../MEMORY.md) alone owns live progression.
A successful canary is interface evidence, never a semantic comparison or product acceptance.

Read [the model binding](investigator_model_interface.py), then
[the qualifier](qualify_investigator_model_interface.py), alongside
[the focused tests](tests/test_investigator_model_interface.py).

## Actual request and reference boundary

Every prediction supplies one complete explicit system/user history. Canonical packed
bytes own admission/accounting and are retained separately. The actual user message
presents fixed task/protocol/report facts first, then current phase/menu/omissions,
then chronological original request/returned-observation pairs. It includes each original
UTF8 request and exact observation JSON text directly, without another escape layer.
No expected next action is supplied. A missing-file result may omit its path; retaining
the actual prior arguments is necessary for complete stateless action history.
No response ID, prior server conversation, model-authored hidden notebook or implicit chat
history is used. Backend reuse of identical prefix computations does not grant extra
conversation history. `current-complete-stateless-request/1` allows only references in the
complete returned observations actually included in this request. Model-authored prior
requests grant no evidence authority, even when they contain a typed-looking reference.
Internal native record/delivery/catalog IDs are not delivered typed citation IDs.
Omitted request/result pairs stay omitted together and record each component's bytes/hash.
Omitted evidence must be re-read;
read-back pages retain their `trial_event` strength, not the original source strength.

The same actual loaded template and prediction configuration stack render and predict.
Every presented input component and eligible reference must survive rendering. Exact
canonical packed-input bytes/hash are retained beside each actual request/rendering. Automatic
backend BOS insertion is represented explicitly from verified GGUF special-token identity;
the SDK-rendered body alone may omit that token. Per-request runtime JSON grammar derives
from the offered closed tool schemas, or the final report schema, without output repair. The loaded
model tokenizes that exact rendering. Capacity admission reserves generated tokens and
an explicit margin; token overflow removes whole events rather than shortening source
text. A fixed prompt that cannot fit refuses. This is conservative packing, not an
optimal-packing algorithm or proof of semantic comprehension.

Original visible response bytes and raw scalar usage/applied configuration are retained
before strict adapter admission. There is no output coercion, JSON salvage or hidden
retry. Actual prompt usage must exactly match the rendered token count. A mismatched
instance/configuration, unknown/invalid usage, exhaustion, timeout, reasoning despite
reasoning-off, empty output or failed publication stops the assignment. Unreported
reasoning counts remain unknown, even when no reasoning fragments were observed.

## Installed SDK compatibility boundary

The existing optional `lmstudio==1.5.0` is selected explicitly with `--sdk-site`; no project
dependency is added. Its public configuration reader discards newer server fields and its
public prediction options cannot express `reasoning.enableThinking`. `SDKBinding` uses
that installed SDK's typed RPC and prediction channel to preserve the full applied load
record, exact template, explicit reasoning-off and raw success metadata. This small binding
is pinned to 1.5.0 and fails on unsupported shapes; no SDK patch or transport fallback occurs.
Reasoning fragments are discarded before accumulation or artifact writes.

The load template may omit `stopStrings` although prediction requires it. The prediction
configuration explicitly freezes an empty extra-stop list while retaining the original
load response unchanged. The installed backend's generated template file is copied into
durable retention before unloading. Process inspection emits only allowlisted fields;
an entire backend command line must never be emitted because it contains credentials.

## Preparation, freeze and canary execution

`python -m experiments.qualify_investigator_model_interface --help` describes the CLI.
For the revised cohort, `--prediction-base` points to this exact candidate's retained
native applied prediction configuration, with source identity/hash. Pin exposed defaults
including CPU threads, top-p/top-k and reasoning parser configuration. Current explicit
template/reasoning/output overrides win; the old per-call runtime grammar is discarded
and rebuilt from the current offered schema. Do not copy another model's defaults.

Preparation requires `--sdk-site`, `--model`, a new owned `--identifier`, an explicit
`--load-config` JSON file, verified `--tokenizer-policy` JSON and a new durable `--output` directory. It refuses interference
with pre-existing loaded models, loads only its own instance, records requested/applied
settings and actual backend/template observations, measures twelve complete short/near-
envelope/late/report shapes, snapshots the exact code, then unloads. It produces no model
output. Failures are retained in the same named preparation directory.

Before inference inspect the rendering, reference eligibility and resource admission for
both treatments. Freeze the selected deployment count, candidates not selected, ordered
assignment IDs, per-sequence and total budgets, actual profile/asset/runtime/code identities,
request/history/reasoning settings and protocol revision. Execute only with
`--execute-freeze` plus `--expected-freeze-sha256` and a new owner-only output directory.
A code/profile/asset mismatch refuses before prediction. All four qualification assignments
per deployment are explicit; each permits the frozen call allocation (at most six). Spent attempts from previous revisions
remain inside the explicitly revised aggregate cycle ceiling. Later semantic assignments
are outside this command and remain separately gated.

The two independent sequences use synthetic retained source/native inputs. The short
sequence exercises a positive read, scoped-zero search, empty file, procedural finish and cited report. The near-envelope sequence additionally pressures
late/final input with neutral calibration text, a missing-source problem; structured access also exercises a native unfinished result.
Separate real-model note/event-readback probes remain explicitly deferred since r4; their
mechanical contracts are covered. The five required steps plus at most one extra response retain every selected plan gate. Both treatments
share the same calibration padding within each deployment. A valid early stop or empty
report cannot qualify skipped operations. No actual development case answers or protected
oracle material enter these canaries. This is neither an agent-reasoning benchmark nor
proof that the workload is a global resource optimum.

Private code/configuration, requests/renderings, original visible responses, usage,
failures and reports stay in durable owner-only storage outside Git. Public-safe evidence
contains hashes/counts/limits and reproduction pointers. Local retention is not an
off-machine backup. The completed mechanical cycle's historical proof remains distinct
from current real-model qualification and later comparative/semantic/usefulness evidence.

## Interrupted-stream retention

The post-r4 repair persists visible fragments before SDK accumulation so client termination
does not discard the received prefix. Reasoning fragments are filtered before that write.
Handled exits fsync the fragment artifact and record its bytes/hash and whether a complete
response was received. Partial text is never salvaged into an accepted response; missing
usage stays unknown and blocks further calls in the assignment. This changed retention code
requires a new source-bound freeze before inference; its new failure path has controlled
test proof, not a silently inherited live qualification. Historical r4 prefix loss remains
explicit rather than relabeled as retained.

## Six-candidate diagnostic revision

The October17 re-entry uses the same actual transport/authority checks for all six
candidates,24 independent sequences and at most six responses each. The sixth response
provides correction headroom; refusals remain charged and retained, and cannot replace
a required successful operation. The shared task explicitly distinguishes zero search
from a separate empty-file read. It is scaffolded interface qualification, not autonomous
planning evidence. No grammar constrains the model to the expected next action.

Preparation accepts `--output-tokens` (default8192); r5 freezes2048 for concise synthetic
reports, unchanged32768 context and the original8192 case reserve. Exact prediction and
ModelLimits generation ceilings must agree. The batch freeze can explicitly set
`continue_independent_sequences_after_failure` so remaining independent sequences run
after a behavioral failure; all four must still qualify before that deployment's later
comparison. Load/profile failures are saved per deployment and do not substitute another
model. Freeze new cohort/order and144 new/19 prior/163 aggregate call ceilings before
inference. The later semantic design remains two deployments/eight case assignments.

## Complete request/result history revision

The r6 source adds model-authored request intent at the experiment AdapterEvent/driver
boundary and packs it with its returned observation. The current reference whitelist
still derives only from delivered observations; a proposed/forged ID cannot authorize
itself. Unavailable/non-UTF8 historical intent stays explicitly unavailable, never
repaired. The strict sequence assessor and output parser remain unchanged.

The driver also retains actual report-refusal details with attempt numbers, including
a final-turn refusal that cannot appear in a subsequent request. This prevents a
generic turn-exhaustion outcome from hiding the underlying citation/schema rejection.
Original rejected reports remain separate and unmodified.

Freeze six deployments/24 new ordered sequences/144 new calls after actual preparation.
All19 earlier calls and every actual r5 attempt remain charged; the explicit aggregate
ceiling is267 (19 + at most104 r5 +144 r6), with no automatic further sweep. Two-deployment/
eight-case semantic comparison stays unactivated. Same2048 synthetic generation limit,
32768 context and actual per-model weight/KV settings remain;8192 is still the later
case reserve, not newly established8192-token generation performance. Resource and
semantic claims must retain those limits.
