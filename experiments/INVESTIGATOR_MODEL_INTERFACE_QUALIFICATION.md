# Investigator deployment and stateless model-interface qualification

This experiment qualifies the real local model/request boundary after the model-free
[mechanical bridge](INVESTIGATOR_WORKSPACE_MECHANICAL_QUALIFICATION.md). The
[integration plan](../plans/INVESTIGATOR_INTEGRATION_AND_COMPARATIVE_EVALUATION_PLAN.md)
owns budgets/fairness/gates; [MEMORY](../MEMORY.md) alone owns live progression.
A successful canary is interface evidence, never a semantic comparison or product acceptance.

## Budget observation revision

Complete requests now include `investigator-budget-observation/1`. The trial driver
supplies remaining invocations/operation units/observations/corrections and sampled
time; model packing joins actual model-call/token allowances. Counts include the
upcoming invocation but exclude its not-yet-measured token cost. Snapshots remain
stable during repacking, survive event omission and stay visible in report phase.
Frozen task definitions cannot override live counters. Unknown usage remains null
and blocks subsequent prediction through the existing guard.

Tool costs and finish/report/termination obligations are visible, while only the
existing termination unit is enforced as reserved. This does not add automatic
stopping, guarantee report completion or prove adequacy. Preflight measures the
full budget representation; the changed source/request contract needs its own
source-bound qualification for all selected deployments before semantic use.

The [semantic comparison runner](run_investigator_semantic_comparison.py) consumes
a separate complete comparison freeze. It refuses before loading a model unless
the exact newly bound canary matrix qualified for every selected profile. It checks
the 12-assignment coverage/order, common inputs, source/contract/reviewer identities
and model/runtime file correspondence. Every semantic assignment starts with fresh
Workspace and model-instance state. Original results and costs remain separate from
offline semantic review; failed/unknown usage never becomes a successful sample.

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
conversation history. `current-complete-stateless-request/2` allows only references in the
complete returned observations actually included in this request. Model-authored prior
requests grant no evidence authority, even when they contain a typed-looking reference.
Internal native record/delivery/catalog IDs are not delivered typed citation IDs.
The `/2` adapter carries trusted `(kind,id)` pairs from actual registration through
whole-event selection. Each candidate pack compiles a closed per-kind citation schema
for claims, recommendation and notes; repacking rebuilds it before measurement. No-pair
arrays have `maxItems: 0`. Exact reference IDs and strict host/admission checks remain
unchanged; source strings and model intent cannot populate this metadata. Returned-event
envelopes expose factual `typed_citation_available`, preserving original observation text.
A problem with no typed evidence stays uncitable and may be recorded in existing
uncertainty/missing-observation fields. Empty/scoped-negative results can still have
real references. This is eligibility control, not entailment or adequacy evaluation.
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

`complete-fixed-first-request-observation-pairs-with-budget/4` and
`investigator-request-local-reference-schema/1` identify this presentation/policy.
Actual requests retain exact typed pairs, derived-schema and packed/rendered hashes.
New qualification/semantic freezes use `/2`; older results remain historical and unchanged.
Semantic scheduling requires inverse per-case 1:2 / 2:1 treatment-first counts as well
as global 3/3 and per-deployment inversion. The semantic freeze names the exact case
orientation. An append-only `investigator-semantic-admission/1` receipt binds both
pre-run freezes and all qualification originals after the matrix finishes, without
rewriting either freeze. Admission rechecks those bytes, known usage and actual
configuration/prompt/instance correspondence before model loading or output creation.

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

## Declared native-mode qualification

Plan §4.9 admits one native-mode point each for E2B/E4B/MiMo after the complete
r6 cohort: three configuration deployments/12 sequences/72 calls,219 actual prior
attempts and327 aggregate ceiling. The later two-deployment/eight-case comparison
remains unactivated. Old failures remain unchanged.

Preparation additionally accepts `--reasoning on|off` (default off), `--temperature`
(default0.2) and a paired `--top-k`/`--top-p`. Explicit top-k/top-p also disables
extra min-p/repetition filters. Defaults preserve r6 behavior. Thinking-on permits
reasoning-labelled fragments only after requested/applied settings match; those
fragments still never enter SDK accumulation, visible artifacts or subsequent history.
The same strict off violation and all usage/render/reference/sequence guards remain.
Absent separate reasoning-token usage is unknown. Native output allowance8192 includes
internal generation, rather than promising8192 visible answer tokens.

New loads observed CUDA llama.cpp2.60.0/b11698/2a667032d rather than r6's2.59.0.
Freeze the new exact executable/configuration and explicitly observed unified-KV
flags. Native startup scalar logs confirm32768 context per slot with unified KV;
backend ctx-size32768/parallel4 must not be divided by four without checking this.
MiMo flash flag is on; Gemmas auto remains a kernel-selection unknown. Changed
runtime/sampler/mode/batching makes this an operating-point qualification, not a
causal comparison against r6. Requested/applied correspondence is checked per call.
Earlier statements about pinned native sampler defaults mean only exposed fields;
absent top-p/top-k values in r6 metadata were not resolved by pinning CPU/tools.
