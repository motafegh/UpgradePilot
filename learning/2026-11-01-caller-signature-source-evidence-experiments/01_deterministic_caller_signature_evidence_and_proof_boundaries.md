# Deterministic caller/signature evidence and proof boundaries

**Educational snapshot:** 2026-11-01 learning package, explaining the experiment implementation and retained proof at repository horizon **`c53430c6e3fb4f24147a28aa642ab94834233243`**.

**Learning responsibility:** understand why UpgradePilot needed deterministic Python caller/signature evidence, how the experiment represents source bindings, calls and declared signatures, how it performs bounded local argument binding, how it preserves unresolved premises, and exactly what the resulting evidence proves and does **not** prove.

**Not this note's responsibility:** automatic ordinary-PR source discovery, cross-module source correspondence, protocol/factory traversal, fresh-provider blocker resolution, capacity/partial-analysis engineering, transfer qualification, native Workspace/product integration, installed-environment reconstruction, runtime dispatch, or whole dependency-update compatibility. Those are separate responsibilities in later notes.

The implementation discussed here is experimental. It is not native product authority.

---

## 1. Why this experiment existed

The key problem was not simply “we need more source code” and it was not simply “the model made a mistake.” The October investigation separated three materially different failure classes:

```text
needed evidence was never acquired
        ↓
acquisition / source-retention responsibility

relevant evidence exists, but its relationship or interpretation is wrong/unestablished
        ↓
source facts / correspondence / interpretation responsibility

we want a stronger claim about what actually ran or was installed
        ↓
runtime / environment / execution responsibility
```

That separation matters because the wrong repair can produce a confident-looking but unsupported system.

If source is missing, more reasoning does not create it. If source is already present but the call/signature relationship is misread, another acquisition does not repair the interpretation. If static source establishes only a conditional relationship, a stronger runtime conclusion cannot be manufactured by making the static analyzer more confident.

The retained HTTPX/Starlette/FastAPI material exposed exactly this distinction. Existing source facts already showed important details:

- the target used `TestClient(...)`;
- FastAPI re-exported Starlette's `TestClient`;
- an older captured Starlette `TestClient` initializer forwarded `app=...` to `super().__init__`;
- a newer captured Starlette initializer did not forward that `app` keyword;
- the older captured HTTPX `Client.__init__` declared an `app` parameter;
- the proposed captured HTTPX initializer did not declare `app` and did not have `**kwargs`;
- both inspected HTTPX signatures still contained `cert`.

But the existing producer did **not** yet emit a complete declared-signature representation or a reusable caller-to-signature binding result. The missing responsibility was therefore narrower than “build another Python analyzer” and broader than “subtract two keyword-name sets.”

The selected experiment became:

> Extract inspectable call and declared-signature facts from qualified Python source, compare supported argument binding under an explicit source-pair/receiver premise, and preserve the result for offline inspection without pretending that the selected pair proves runtime dispatch.

### Primary historical anchors

- `working-memory/2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md`
- `working-memory/2026-10-28_reusable-caller-signature-evidence_design-cycle.md`
- `working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md`
- `working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md`
- `working-memory/evidence/2026-10-28-caller-signature-build/REVIEW.md`

All should be read at the pinned horizon above.

---

## 2. The central mental model

The experiment becomes much easier to reason about if you keep six different layers separate:

```text
1. RETAINED SOURCE
   exact captured bytes + repository/revision/path/coverage
             ↓
2. SOURCE FACTS
   imports, bindings, calls, signatures, spans
             ↓
3. SOURCE RELATIONSHIP / PAIRING
   “compare this call with this declared signature”
   + source/version/receiver premises
             ↓
4. LOCAL ARGUMENT BINDING
   bound / rejected / undetermined
   + per-keyword reception + violations
             ↓
5. RUNTIME APPLICABILITY
   installed versions, effective dispatch, MRO, decorators, branch activation
   NOT established here
             ↓
6. PRODUCT DECISION / COMPATIBILITY
   safe update? maintainer action? actual behavior?
   NOT established here
```

Most mistakes happen when two adjacent layers are silently collapsed.

Examples:

- A call expression with lexical origin `fastapi.testclient.TestClient` is not proof that a specific Starlette revision was installed.
- A captured `super().__init__` call is not proof that runtime dispatch reached the selected HTTPX initializer.
- A local binding result `bound` means the supplied syntactic arguments fit the selected declared signature under the stated premises. It does **not** mean the call executed successfully.
- A keyword being present in a signature does not settle deprecation, meaning, behavior or compatibility.
- A selected caller/callee pair is evidence input for a curated calibration experiment. It is not automatic discovery proof.

This layered model is the most important thing to own from this note.

---

## 3. Reuse the existing binding owner instead of building another import analyzer

The existing binding owner is `experiments/api_python_bindings.py`.

Its module-level contract is unusually important:

- it analyzes source without executing target code;
- it propagates possible imported origins through supported lexical constructs;
- it preserves uncertainty from branches, rebinding, delayed global reads, dynamic namespace operations and unsupported control flow;
- only an **established** origin populates `ReferenceFact.lexical_import`;
- binding traces are source observations, not execution histories;
- no installed distribution or compatibility conclusion follows.

### 3.1 `BindingAssessment`

The central record is conceptually:

```text
BindingAssessment
  state
  possible_imports
  unknown_possible
  unbound_possible
  scope
  reasons
  trace
```

The four states mean:

| State | Meaning in this experiment | What it does not mean |
| --- | --- | --- |
| `established` | exactly one imported origin remains and no unknown/unbound alternative is retained | that origin executed at runtime |
| `conditional` | several alternatives, or an imported origin competes with unknown/unbound possibilities | one branch was actually taken |
| `unknown` | the examined source cannot establish an imported origin | the name definitely does not refer to the library |
| `unbound` | the examined lexical path supports an unbound possibility without a competing unknown | that runtime execution necessarily reached this path |

The state is derived from the **set of possibilities**, not from a confidence score.

### 3.2 Why `lexical_import` is intentionally narrower

`ReferenceFact.lexical_import` is populated only when the binding is `established`.

That policy prevents a downstream consumer from treating a conditional possible origin as a positive fact.

For example:

```python
if backend:
    import httpx
httpx.Client()
```

The source can preserve `httpx.Client` as a possible import while also preserving that the name may be unbound. The result is conditional; it does not become an established lexical import just because `httpx.Client` appears in one branch.

This distinction later becomes important for source acquisition and correspondence. A source owner may inspect a conditional candidate explicitly without rewriting its binding state to established.

### 3.3 Why traces matter

A `BindingTraceStep` carries exact source identity and AST coordinates:

```text
source_id
scope
line / column / end_line / end_column
operation
name
origin
input_name
```

The trace is not a reconstructed execution timeline. It is an ordered record of source observations that contributed to the assessment.

That means two mutually exclusive branches may both appear in a trace. Their presence records alternatives; it does not claim both ran.

### 3.4 Examples worth understanding

The focused binding tests protect several important source semantics:

- import → alias → rebinding → restoration can return to an established origin;
- a function-local name follows Python's function-wide local rule and cannot borrow a module binding before its local assignment;
- delayed global reads remain uncertain because definition-time state is not invocation-time state;
- branch alternatives preserve multiple possible imported origins rather than selecting one;
- deletion is different from unknown rebinding;
- star imports, `exec`, dynamic namespace operations and unsupported writes invalidate stale positive claims;
- relative imports remain unresolved rather than being converted into invented absolute external origins;
- trace-budget exhaustion becomes an explicit limitation and cannot silently remain positive.

These controls are not incidental test trivia. They define the epistemic discipline of the whole caller/signature experiment.

### Source anchor

Pinned file:

`experiments/api_python_bindings.py`

Useful entry points:

- `BindingTraceStep`
- `BindingAssessment`
- `ReferenceFact`
- `binding_state`
- `_Analyzer.lookup`
- `_Analyzer.reference`
- `_Analyzer.block`
- `analyze_python_bindings`

Focused tests:

`experiments/tests/test_api_python_bindings.py`

---

## 4. Why exact spans are part of evidence identity

A line number and expression spelling are not enough to identify a call.

This is valid Python:

```python
send(a=1); send(a=2)
```

Both calls:

- are on the same line;
- have the same callee spelling;
- may share the same lexical import origin;
- still represent different source occurrences.

The experiment therefore uses full AST spans:

```text
line
column
end_line
end_column
```

Python AST columns are UTF-8 byte offsets, not Unicode character indices. The saved reader validates that a retained coordinate does not split a UTF-8 continuation byte.

The call/signature fact identity is then derived from:

```text
fact kind
+ source unit identity
+ full source span
```

This protects against a subtle but dangerous shortcut: “take the first call with the same line/expression.” That would manufacture precision not supported by the source.

The same-line-call test confirms that the two calls receive different spans and different fact identities.

### Engineering lesson

**Identity should be as precise as the proposition you later want to prove.**

If the downstream comparison is occurrence-specific, the upstream source identity must also be occurrence-specific.

---

## 5. What `api_call_signature.py` adds

The caller/signature owner deliberately does **not** replace the binding analyzer.

It adds two missing source-fact families:

1. complete syntactic call argument shape;
2. declared callable signature shape.

The design keeps these as source observations and then performs a separate local comparison.

### 5.1 Call facts

`CallArguments` preserves roughly:

```text
fact_id
unit_id
exact call span
callee expression text
positional item kinds: ordinary / starred
keyword names: explicit name / None for ** expansion
argument spans
coverage completeness
existing BindingAssessment, when an exact trace join exists
```

Important: the analyzer does not evaluate argument values.

For example:

```python
f(1, *items, timeout=2, **options)
```

is represented structurally as:

```text
positional = ordinary, starred
keywords   = timeout, <unknown expansion>
```

It does not try to determine how many values `*items` contributes or which keys `**options` contains.

Even literal unpacking is not silently executed in the initial method.

### 5.2 Signature facts

`CallableSignature` preserves roughly:

```text
fact_id
unit_id
definition span
header span
qualified lexical name
kind: function / async_function / initializer
ordered parameters
coverage completeness
decorators
class bases
limitations
```

Each parameter keeps:

```text
name
kind
default presence
```

The supported parameter kinds are:

- positional-only;
- positional-or-keyword;
- variadic positional (`*args`);
- keyword-only;
- variadic keyword (`**kwargs`).

The experiment retains **default presence**, not evaluated default values.

Decorators and class context are retained because they may affect effective runtime calling semantics, but the extractor does not execute them or claim their effect.

### 5.3 Why source coverage is explicit

A successfully parsed fragment is not automatically a complete signature.

The host supplies whether the retained unit is a complete file or limited source. If a signature is incomplete, the comparison cannot use missing text as evidence that a parameter is absent.

This is why `complete=False` turns a would-be absence conclusion into `undetermined`.

### Source anchor

Pinned file:

`experiments/api_call_signature.py`

Useful entry points:

- `SourceSpan`
- `CallArguments`
- `ParameterFact`
- `CallableSignature`
- `SourceFacts`
- `extract_python_source`
- `compare_arguments`

Focused tests:

`experiments/tests/test_api_call_signature.py`

---

## 6. Receiver binding must be explicit

A method-like declared signature usually includes a receiver parameter, but a source call may not spell that receiver.

The experiment refuses to infer receiver behavior from a parameter named `self` or `cls`.

It has three explicit modes:

| Receiver mode | Meaning |
| --- | --- |
| `as_written` | bind only the arguments syntactically present at the caller |
| `one_receiver_assumed` | conditionally insert one positional receiver before source arguments |
| `unresolved` | do not claim complete argument binding; receiver-specific applicability is unresolved |

Consider:

```python
class Client:
    def __init__(self, *, option=None): ...
```

and a selected source call:

```python
super().__init__(option=1)
```

The experiment may compare that call to `Client.__init__` using `one_receiver_assumed`, but the result must retain the premise:

```text
one_bound_positional_receiver_assumed
```

It also retains:

```text
call_reaches_selected_declared_signature
target_installed_versions_and_runtime_not_established
```

So the result means:

> If this call reaches this selected declared signature with one bound receiver, the following local argument-binding facts hold.

It does **not** mean:

> We proved Python runtime dispatch reaches this signature.

This explicit premise is one of the strongest design choices in the experiment.

---

## 7. Local comparison semantics

The output has three comparison-level outcomes:

### `rejected`

At least one definite binding violation exists under the selected source pair and receiver premise.

Examples:

- unsupported explicit keyword;
- positional-only parameter supplied by keyword without a `**kwargs` receiver;
- too many positional arguments without `*args`;
- duplicate assignment;
- required parameter missing when full binding is otherwise checkable.

A definite rejection may survive other unresolved checks.

That is useful. Suppose a caller contains `**options`, but it also explicitly passes `app=...`, and the complete selected signature has neither `app` nor `**kwargs`. Unknown keys inside `**options` cannot make the explicit unsupported `app` keyword accepted. The comparison can retain that scoped rejection while still saying complete binding is not checked.

### `bound`

All supported syntactic binding checks are complete and no violation exists.

This requires, among other things:

- complete caller source;
- complete signature source;
- usable signature without unsupported limitations;
- specified receiver mode;
- no unresolved caller `*args` expansion;
- no unresolved caller `**kwargs` expansion.

`bound` is deliberately narrow. It does not establish execution, behavior, compatibility, installed versions or update safety.

### `undetermined`

No definite rejection is known, but at least one required binding check or premise remains unresolved.

Common causes:

- unresolved receiver;
- incomplete caller/signature coverage;
- starred positional expansion;
- double-star keyword expansion;
- unsupported signature limitation.

### Per-keyword reception

Each explicit keyword separately receives one of:

- `named_parameter`;
- `variadic_keyword`;
- `not_received`;
- `undetermined`.

This is important because a caller/signature comparison contains more information than one top-level outcome.

For example, overall binding can be `undetermined` while an explicit keyword is still definitely not received.

---

## 8. The positional-only + `**kwargs` corner that changed the design

This was one of the most valuable engineering corrections in the experiment.

The tempting implementation shortcut was:

> Construct an `inspect.Signature` from extracted source facts and delegate binding to `Signature.bind`.

Fourteen locally authored controls agreed with the helper.

That looked encouraging but was not sufficient qualification.

A fifteenth control exposed a disagreement on the local Python 3.12.3 runtime:

```python
def f(value=0, /, **options):
    return value, options

f(value=2)
```

Actual Python execution of this trusted local control succeeds as:

```text
value   = 0
options = {"value": 2}
```

The keyword named `value` does **not** fill the positional-only slot. The slot keeps its default. Because the function has `**options`, the keyword is received by that mapping.

But the tested `inspect.signature(f).bind(value=2)` helper rejected the call in that environment, reporting that `value` is positional-only but was passed as a keyword.

The disposition was not:

> Python's standard library is broken everywhere.

The supported conclusion was narrower:

> This helper cannot be treated as the sole implementation/oracle for the experiment's source-binding semantics.

So the experiment implemented a small explicit slot-binding algorithm and validated it against trusted, side-effect-free, locally authored Python functions.

### Why this lesson matters

A dependency or standard-library helper can be:

- well-designed;
- useful for most cases;
- pass many controls;
- still be insufficient as the authority for your exact proposition.

The correct engineering move is to qualify the helper against the semantic corners that matter to your responsibility.

### Evidence anchor

`working-memory/evidence/2026-10-28-reusable-caller-signature-design/validation.json`

It records:

- runtime Python 3.12.3;
- the first fourteen agreeing controls;
- the additional disagreeing control;
- the trusted actual call result;
- the helper's rejection;
- the explicit proof limits.

---

## 9. The binding algorithm at the level you should own

You do not need to memorize the source implementation. You should be able to reconstruct the reasoning.

### Step 1 — determine what is unresolved

Before full binding, collect blockers such as:

```text
caller coverage limited
signature coverage limited
receiver unresolved
positional expansion unresolved
keyword expansion unresolved
signature limitation
```

### Step 2 — classify parameters

Separate:

```text
positional-only
positional-or-keyword
keyword-only
*args
**kwargs
```

Do not put positional-only names into the ordinary keyword-addressable parameter map.

### Step 3 — classify explicit keyword reception

For each explicit keyword:

```text
ordinary named parameter exists
    → named_parameter
else **kwargs exists
    → variadic_keyword
else complete usable signature
    → not_received + violation
else
    → undetermined
```

### Step 4 — if complete binding is possible, assign positional slots

Count syntactically known positional items plus one assumed receiver when that mode is selected.

Do **not** treat a starred source item as one runtime value when its expansion is unresolved.

### Step 5 — apply explicit keywords

Detect:

- duplicate keyword spelling;
- positional+keyword duplicate assignment;
- named parameter assignment.

A positional-only name supplied by keyword does not mark that positional-only slot assigned. If `**kwargs` exists, that same spelling can legitimately enter the variadic keyword mapping.

### Step 6 — check required parameters

For every non-variadic parameter without a default, require that its slot is assigned.

### Step 7 — decide outcome

```text
any definite violation
    → rejected
else all supported checks complete
    → bound
else
    → undetermined
```

This is a declared-syntax binder, not a Python runtime.

---

## 10. Real worked case: Starlette forwarding versus HTTPX signatures

This is the primary real teaching case for this note.

The retained source set contained seven selected files, including:

- target `requirements.txt`;
- target `tests/test_routes.py`;
- FastAPI `testclient.py` re-export source;
- older Starlette `testclient.py`;
- newer Starlette `testclient.py`;
- old HTTPX `_client.py`;
- proposed HTTPX `_client.py`.

The official curated attempt selected five comparisons.

### 10.1 Older Starlette forwarding → old HTTPX initializer

Captured caller:

```text
Starlette old TestClient
super().__init__(...)
```

Explicit keywords:

```text
app
base_url
headers
transport
follow_redirects
cookies
```

Selected old HTTPX `Client.__init__` includes an `app` keyword-only parameter and the other relevant named parameters.

Receiver mode:

```text
one_receiver_assumed
```

Local result:

```text
bound
```

What is established:

> Under the selected pairing and one-receiver premise, the supplied arguments fit the old declared HTTPX initializer.

What is not established:

- the actual target installed that Starlette revision;
- runtime `super()` dispatch reached that HTTPX initializer;
- the call executed;
- the dependency update was compatible.

### 10.2 Older Starlette forwarding → proposed HTTPX initializer

Same captured caller, but proposed HTTPX `Client.__init__` no longer declares `app` and has no variadic keyword receiver.

Local result:

```text
rejected
```

Per-keyword result:

```text
app → not_received
```

Violation:

```text
unexpected_keyword app
```

This is the mechanical relation that the earlier semantic explanation had failed to preserve clearly enough.

But the correct statement is still conditional:

> If this older captured Starlette forwarding call reaches this proposed HTTPX initializer with one bound receiver, `app` has no receiving parameter.

That is stronger and more useful than “the source looks suspicious,” but weaker than “the actual target fails at runtime.”

### 10.3 Newer Starlette forwarding → proposed HTTPX initializer

The newer captured Starlette call forwards:

```text
base_url
headers
transport
follow_redirects
cookies
```

It does not explicitly forward `app`.

Against the proposed HTTPX initializer, the local comparison is:

```text
bound
```

The correct conclusion is **not**:

> The update is compatible.

It is:

> This specific captured forwarding call does not contain the earlier explicit `app` mismatch, and its supported supplied syntax fits the selected proposed initializer.

### 10.4 Target `TestClient(app)` → older/newer Starlette initializer

The target's outer call also compares as locally bound against both captured Starlette initializer signatures under the receiver premise.

This teaches another important distinction:

```text
outer call accepts app
        ≠
inner forwarding still sends app to HTTPX
```

The outer constructor may continue accepting `app` while its internal forwarding behavior changes.

### 10.5 `cert` remains present

Both retained HTTPX initializer facts include `cert`.

That source fact can refute a mistaken claim that the parameter is absent in one captured signature.

But signature presence does not tell you:

- whether `cert` is deprecated;
- whether its semantics changed;
- whether another internal path handles it differently;
- whether actual target behavior is compatible.

This is an example of why structural evidence and semantic meaning must remain separate.

### Retained result anchor

`working-memory/evidence/2026-10-28-caller-signature-build/comparison-view-current.txt`

The saved view names each pair, exact source revisions, lines, parameter facts, per-keyword findings, remaining premises and suggested next evidence.

---

## 11. Curated comparison is a proof class, not automatic discovery

The first runner is deliberately labelled:

```text
retained_curated_source_comparison
```

Its input selections contain:

- exact source files;
- exact call span;
- exact callee definition span;
- receiver mode.

They are allowed to locate evidence, but they are not allowed to provide:

- expected result;
- removed keyword list;
- compatibility verdict;
- positive installed-version claim.

The reader rejects extra interpretation such as an injected `expected_result` field.

This boundary matters because the first experiment answers:

> Can the deterministic source/binding method compute and preserve the right local relation for a qualified selected pair?

It does **not** yet answer:

> Can UpgradePilot start from an ordinary PR and discover the correct caller/callee path itself?

That later responsibility is the subject of the next learning artifact.

---

## 12. Resource limits are evidence semantics, not just performance settings

The shared support owner defines finite analysis limits, including:

```text
max files
max retained source bytes
max AST nodes per file
max aggregate AST nodes
max facts
max comparison pairs
timeout
memory
```

A limit refusal is not equivalent to an empty finding.

For example:

```text
source_fact_limit
```

means the method refused to claim complete analysis under the selected bound. It does not mean the source had no facts.

Likewise, invalid Python syntax returns an explicit problem rather than an empty success.

This principle becomes much more important later during the capacity/partial-analysis work, but it begins here.

---

## 13. Saved evidence is immutable and cold-opened

A learning mistake would be to think that “saved result” means “save some selectors and recompute later.”

The curated runner instead preserves:

```text
attempt metadata
result.json
sources.json
human view
input digests
method/source-code identity
limits
```

The output directory is immutable for an attempt. A retry requires a new directory.

### 13.1 Bounded worker

Parsing and analysis run inside a bounded subprocess with memory and time limits.

Partial worker output is not promoted to a completed result.

A timed-out or failed attempt remains an inspectable attempt state rather than masquerading as an empty completed comparison.

### 13.2 Cold opening

`open_comparison(...)` validates saved records and their closure. It does not rerun extraction or access the network.

A focused test explicitly patches source extraction and socket creation to fail if called during opening. The saved result still opens successfully.

This proves a useful architectural property:

> Historical inspection consumes retained evidence, not today's analyzer behavior.

### 13.3 Reader validation

The shared reader checks details such as:

- method/format version;
- target identity;
- companion digest;
- source spans inside retained bytes;
- fact identity;
- coverage consistency;
- binding state consistency;
- comparison call/signature identity;
- keyword reception/violation consistency;
- remaining premises;
- result/source closure.

This is integrity and representation validation. It is not cryptographic authenticity of the external world and not semantic re-proof.

### Source anchors

- `experiments/api_signature_evidence.py`
- `experiments/api_call_signature_trial.py`

Focused tests:

- `experiments/tests/test_api_call_signature_trial.py`

---

## 14. Important failure and correction lessons from this slice

The finished mechanism is easier to remember if you also remember what was rejected or corrected.

### 14.1 Wrong lesson: “the model failed, so add another model pass”

The retained source already contained mechanical facts that could be compared deterministically. The appropriate first remedy was a structural baseline, not another semantic trial.

### 14.2 Wrong lesson: “we need another import/keyword analyzer”

The existing binding producer already retained the useful imported-origin and explicit keyword facts. The extension reused it and added only the missing call/signature structure.

### 14.3 Wrong lesson: “line + expression is precise enough”

Same-line same-spelling calls proved this unsafe. Full spans became occurrence identity.

### 14.4 Wrong lesson: “`self` tells us receiver binding”

Receiver mode became an explicit comparison premise instead.

### 14.5 Wrong lesson: “a standard helper that passes many controls is automatically the oracle”

The positional-only/default/`**kwargs` corner disproved that assumption. The helper remained useful as a comparator, but not sole semantic authority.

### 14.6 Wrong lesson: “a rejected local comparison proves target failure”

The result still depends on selected source versions, pairing and dispatch premises.

### 14.7 Wrong lesson: “a bound local comparison proves compatibility”

It proves only that supported syntactic argument binding succeeds for the selected declared signature under the stated premises.

### 14.8 Implementation correction after the official retained run

The official retained comparison itself succeeded. Later review found a CLI display boundary where multiline attempt JSON lost display line breaks through a line-oriented sanitizer. The structured result and original saved view were intact.

The fix was made at the display boundary and covered by a regression test. The original attempt was not rerun or rewritten.

The review also tightened integrity/deadline checks in the reader/runner without changing the original binder result.

This is another evidence-discipline lesson:

> A later consumer fix does not mean the historical producer executed the later code.

---

## 15. What the focused tests actually prove

Test counts are useful only after the responsibility is understood.

The final build review recorded 165 API experiment tests passing at that horizon, including 29 new tests for this slice. More important than the number are the discriminating behaviors.

### Binding/source tests worth reading

From `experiments/tests/test_api_call_signature.py`:

1. `test_supported_binding_agrees_with_trusted_python_calls`
   - checks the explicit binder against locally authored Python functions;
   - does not execute retained project/library source.

2. `test_optional_positional_only_name_can_enter_variadic_keywords`
   - protects the exact semantic corner that invalidated blind helper delegation.

3. `test_keyword_reception_survives_unknown_expansions_without_full_success`
   - proves a definite explicit keyword rejection can coexist with unresolved overall binding.

4. `test_receiver_is_explicit_and_never_inferred_from_self_spelling`
   - protects the receiver-premise boundary.

5. `test_incomplete_signature_cannot_prove_an_absent_parameter`
   - protects negative-evidence discipline.

6. `test_shared_binding_trace_disambiguates_same_line_calls`
   - protects occurrence identity.

7. `test_rebinding_and_dynamic_super_preserve_uncertainty`
   - protects the distinction between source syntax and established origin/dispatch.

8. `test_invalid_source_and_work_limits_never_return_an_empty_success`
   - protects explicit refusal/unknown semantics.

### Binding-owner tests worth reading

From `experiments/tests/test_api_python_bindings.py`:

- alias restoration after rebinding;
- function-wide local behavior;
- delayed global reads;
- differing branch alternatives;
- conditional imports not promoted;
- star import/dynamic namespace invalidation;
- relative import uncertainty;
- binding trace exhaustion becoming explicit.

### Saved-consumer tests worth reading

From `experiments/tests/test_api_call_signature_trial.py`:

1. `test_selection_cannot_supply_expected_answer_or_upgrade_wrong_target`
   - prevents answer injection.

2. `test_limited_signature_does_not_make_an_absence_claim`
   - prevents incomplete evidence from becoming a false negative.

3. `test_saved_identity_version_span_and_reference_corruption_are_refused`
   - checks representation closure and corruption refusal.

4. `test_bounded_worker_completion_and_cold_open_do_not_reanalyze_or_use_network`
   - proves saved opening is actually offline/fixed.

5. `test_attempt_is_immutable_and_corrupt_companions_or_outputs_cannot_reopen`
   - protects immutable attempt history.

6. `test_deadline_failure_and_unattempted_work_are_preserved_without_completion`
   - prevents a timeout/refusal from masquerading as an empty result.

### What these tests do not prove

They do not prove:

- arbitrary Python semantics;
- actual target installation;
- runtime dispatch;
- target test execution;
- behavioral compatibility;
- a safe dependency update;
- maintainer usefulness;
- automatic PR discovery;
- product integration.

---

## 16. Source walkthrough: shortest useful path

If you are reading the code later, do not start from every helper.

### Step 1 — binding semantics

Open:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_python_bindings.py
```

Read, in order:

1. `BindingAssessment`;
2. `binding_state`;
3. `_Analyzer.lookup`;
4. `_Analyzer.reference`;
5. branch handling inside `_Analyzer.block`;
6. `analyze_python_bindings`.

Question to keep in mind:

> Under what exact conditions is `lexical_import` allowed to become positive?

### Step 2 — call/signature facts and binder

Open:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_call_signature.py
```

Read:

1. `CallArguments`;
2. `CallableSignature` / `ParameterFact`;
3. `extract_python_source`;
4. `ArgumentComparison`;
5. `compare_arguments`.

Question:

> Which unresolved conditions block only full binding, and which explicit facts can still survive?

### Step 3 — retained evidence support

Open:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_signature_evidence.py
```

Focus on:

- `AnalysisLimits`;
- source-span/fact decoding;
- binding/comparison consistency checks;
- fixed result/source reconstruction.

Question:

> Which validations are integrity/closure checks, and which would require re-running semantics?

### Step 4 — curated runner

Open:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_call_signature_trial.py
```

Read:

- `prepare_comparison`;
- `read_comparison`;
- `open_comparison`;
- `run_comparison`.

Question:

> Where is the boundary between curated evidence location and computed comparison result?

### Step 5 — real retained result

Open:

`working-memory/evidence/2026-10-28-caller-signature-build/comparison-view-current.txt`

Trace the five pairs and explicitly list which premises remain for each.

---

## 17. What you should be able to explain after this note

### Must own

You should be able to explain without reading the source line-by-line:

- why acquisition, source facts, correspondence, local binding and runtime applicability are separate layers;
- what `established`, `conditional`, `unknown` and `unbound` mean;
- why only an established origin becomes `lexical_import`;
- why exact AST spans are needed;
- what information call facts and signature facts preserve;
- why receiver mode is explicit;
- why `bound`, `rejected` and `undetermined` are local structural outcomes;
- why keyword reception and whole-call binding are separate;
- why caller unpacking is preserved as unresolved instead of evaluated;
- why the positional-only + `**kwargs` case invalidated blind `inspect.Signature.bind` delegation;
- why the HTTPX `app` comparison is conditional evidence, not runtime compatibility proof;
- why `cert` presence is a source fact, not a semantic verdict;
- why saved opening cannot recompute historical results.

### Understand operationally

You should be comfortable reading:

- AST span coordinates;
- parameter kinds/default presence;
- trace reasons;
- analysis limits;
- immutable attempt metadata;
- saved source/result integrity checks.

### Lookup-level

You do not need to memorize:

- every dataclass field;
- every JSON key;
- exact SHA values;
- every binding reason string;
- the CLI argument parser;
- every test helper.

### Deliberately deferred

Do not try to solve here:

- arbitrary import execution;
- general object/value flow;
- descriptors/MRO/metaclasses;
- actual installed package resolution;
- runtime dispatch/execution;
- automatic source correspondence;
- product report integration.

---

## 18. Fast relearning route

If you return months later, use this route instead of rereading everything.

### Five-minute mental refresh

Recall this chain:

```text
source bytes
→ binding/call/signature facts
→ explicit caller/callee + receiver premise
→ local argument binding
→ preserved runtime/version unknowns
```

Then remember two rules:

```text
bound != compatible
rejected != observed runtime failure
```

### Fifteen-minute source refresh

Read:

1. `BindingAssessment` + `binding_state` in `api_python_bindings.py`;
2. `extract_python_source` + `compare_arguments` in `api_call_signature.py`;
3. one binding test and one cold-open test.

### Thirty-minute real-case refresh

Read:

1. `comparison-view-current.txt`;
2. the older-Starlette → proposed-HTTPX rejected pair;
3. the newer-Starlette → proposed-HTTPX bound pair;
4. the design validation's positional-only/`**kwargs` discrepancy.

If you can explain why all four results can be simultaneously true without proving target compatibility, you have recovered the core model.

---

## 19. Transfer questions

These are reasoning questions, not recall trivia.

### 1. Unknown expansion plus definite keyword rejection

A captured call is:

```python
client(*args, removed=1, **options)
```

The selected complete signature has no `removed` parameter and no `**kwargs`.

What can the experiment conclude? What remains unresolved?

### 2. Positional-only name plus `**kwargs`

Given:

```python
def f(value=0, /, **options): ...
f(value=2)
```

Which slot receives the keyword? Is the positional-only `value` slot assigned by that keyword? Why was this case important to the design?

### 3. Conditional origin

Source says:

```python
if enabled:
    from vendor import send
send(option=1)
```

The exact vendor source is later acquired and its signature accepts `option`.

Should the call's binding state be promoted from conditional to established because source acquisition succeeded? Why or why not?

### 4. Bound source comparison

A target call is locally `bound` against both old and proposed dependency signatures.

Name at least four distinct propositions that remain unproved before you can claim compatibility.

### 5. Saved historical result after code changes

Suppose the current binder implementation changes six months later. You open an old saved comparison bundle.

Should the reader rerun the new binder and replace the historical outcome? What should it validate instead?

---

## 20. Answers/checkpoints for self-review

Do not use this as a quiz answer sheet before attempting the questions.

1. The explicit unsupported keyword can produce a definite local rejection even though complete binding remains unresolved because of `*args`/`**options`. Unknown expansions do not create a receiving slot for an explicit keyword when the complete selected signature has none.
2. The keyword `value=2` goes into `**options`; it does not fill the positional-only slot. That slot keeps its default `0`. This case showed that the tested `inspect.Signature.bind` behavior could not serve as the sole oracle for the experiment.
3. No. Source acquisition establishes availability of a candidate source, not which branch executed or which binding became effective. Conditional source origin must remain conditional unless another owner supplies evidence that discharges that premise.
4. Examples: actual installed old/proposed versions, effective imported namespace, caller→callee correspondence, runtime dispatch/MRO/descriptor behavior, branch activation, execution, behavioral semantics, test exercise, whole-update compatibility.
5. No historical regrade. Validate format/method identity, target/source/result closure, digests, spans, fact/comparison consistency and supported historical representation. Recompute only in a separately labelled new analysis responsibility.

---

## 21. Final proof boundary

At this snapshot, this slice established a reusable experimental capability with real retained source evidence:

```text
qualified source files
→ conservative scoped binding facts
→ exact call/signature facts
→ explicit curated source pair + receiver premise
→ bounded local argument comparison
→ immutable saved result + retained source companion
→ cold offline inspection
```

The retained HTTPX case produced five expected conditional comparisons, including the important older-Starlette → proposed-HTTPX `app` rejection and newer-Starlette → proposed-HTTPX bound contrast.

That is meaningful deterministic structural evidence.

It is **not yet** ordinary automatic PR discovery, installed-version evidence, runtime dispatch, target execution, behavioral compatibility, product adoption or maintainer usefulness.

The next engineering question is therefore not “can the binder compare a selected pair?” It is:

> Can ordinary repository/PR evidence discover and retain the relevant source relationships without being handed the expected caller/callee answer?

That transition is the subject of Artifact 02.

---

## Pinned source and evidence anchors

Implementation:

- `experiments/api_python_bindings.py`
- `experiments/api_call_signature.py`
- `experiments/api_signature_evidence.py`
- `experiments/api_call_signature_trial.py`

Focused tests:

- `experiments/tests/test_api_python_bindings.py`
- `experiments/tests/test_api_call_signature.py`
- `experiments/tests/test_api_call_signature_trial.py`

Historical design/result evidence:

- `working-memory/2026-10-26_capability-limits-for-explanation-milestone_discussion-cycle.md`
- `working-memory/2026-10-28_reusable-caller-signature-evidence_design-cycle.md`
- `working-memory/2026-10-28_reusable-caller-signature-evidence_build-cycle.md`
- `working-memory/evidence/2026-10-28-reusable-caller-signature-design/DESIGN.md`
- `working-memory/evidence/2026-10-28-reusable-caller-signature-design/validation.json`
- `working-memory/evidence/2026-10-28-caller-signature-build/REVIEW.md`
- `working-memory/evidence/2026-10-28-caller-signature-build/comparison-view-current.txt`

For any local source inspection, pin the horizon explicitly, for example:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_call_signature.py
```

Do not substitute mutable `main` and still call the result this frozen educational snapshot.

`UP-SKILL:upgradepilot-learning-artifact`
