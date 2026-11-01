# Ordinary PR source acquisition, correspondence and protocol paths

**Educational snapshot:** 2026-11-01 learning package, explaining the experiment implementation and retained proof at repository horizon **`c53430c6e3fb4f24147a28aa642ab94834233243`**.

**Learning responsibility:** understand how UpgradePilot moved from curated caller/signature pairs to an ordinary repository/PR-driven source-evidence pipeline: how target/dependency/source observations are acquired, how exact old/proposed sources differ from constraint-selected samples, how source relationships are discovered without answer selectors, how direct/re-export/initializer/protocol paths are represented, how uncertainty and alternatives survive traversal, and how the result is retained for cold offline inspection.

**Not this note's responsibility:** the later fresh-provider blocker-resolution campaign, live staged request allocation, retry policy, source-first capacity repairs, whole-file partial-analysis admission, untouched transfer qualification, native Workspace/product adoption, installed-environment reconstruction, runtime dispatch, semantic compatibility or maintainer action authority. Those are later responsibilities.

This implementation is experimental. Its output is not native product authority.

---

## 1. Why the curated experiment was not enough

Artifact 01 established that the deterministic caller/signature checker could answer a bounded question when it was given a qualified caller, a qualified declared signature and an explicit receiver premise.

That was useful, but it left a major responsibility outside the system:

```text
human/reviewer chooses caller + callee
        ↓
local structural comparison works
```

A real dependency-update investigation cannot stop there. Starting from an ordinary PR, the system must discover the relevant evidence itself.

The next question became:

> Given only a repository, a pull request and ordinary provider observations, can the experiment acquire the relevant target/library source, preserve exact source roles and provenance, derive plausible caller-to-declaration relationships without being handed the expected answer, run the already-qualified checker, and retain both useful findings and unresolved gaps for offline review?

This is a different proof class from the curated experiment.

Curated proof asks:

```text
for this selected source pair,
does the checker produce the expected local result?
```

Ordinary proof asks:

```text
starting from ordinary PR evidence,
can the system discover and preserve a useful source path itself?
```

The second question contains substantially more engineering responsibility.

---

## 2. The central mental model

The ordinary path is easiest to understand as five owners with explicit boundaries:

```text
REPOSITORY + PR
      │
      ▼
1. NATIVE PR / DEPENDENCY OBSERVATION
   exact PR identity + base/head + changed package transition
      │
      ▼
2. SOURCE ACQUISITION
   target source
   exact old/proposed changed-package source
   labelled adapter/framework samples
   complete admitted text + provenance + omissions
      │
      ▼
3. SOURCE CORRESPONDENCE
   target-rooted syntax paths:
   imports / re-exports / declarations / initializers / bounded protocols
   + alternatives + explicit premises + gaps
      │
      ▼
4. LOCAL CALL/SIGNATURE CHECKER
   unchanged Artifact-01 binder:
   bound / rejected / undetermined
      │
      ▼
5. RETAINED ORDINARY RESULT
   immutable result + complete admitted source companion
   + paths + roles + gaps + omissions + work
   + cold offline opening
```

The strongest rule in this note is:

> **A later layer may consume an earlier layer's evidence, but it must not rewrite the earlier layer's uncertainty into stronger truth.**

Examples:

- acquiring a module does not prove that an earlier conditional import executed;
- finding a class declaration does not prove the module effectively exported it;
- following a `super().__init__` source path does not prove runtime MRO/dispatch;
- finding a `__call__` declaration does not prove the object at runtime had that type;
- a constraint-selected package sample does not become the target's installed version;
- a locally `bound` comparison does not become compatibility evidence.

---

## 3. Start from one PR/dependency observation horizon

One early design concern was duplicated acquisition.

The older ordinary experimental path had historically acquired PR identity/changes independently. The integration work moved toward reusing the same native PR/dependency prefix so that the downstream experiment did not silently reason over a second observation horizon.

The intended shape became:

```text
acquire dependency inputs once
        ↓
retain:
  PR observation
  description
  changed files
  exact dependency transition
  source contexts
        ↓
ordinary target/source experiment
```

Why does this matter?

Because a PR is mutable during observation. Two independently fetched views can disagree about:

- head SHA;
- changed files;
- description;
- dependency transition;
- source context.

If later evidence is composed from a different observation horizon, the system can produce internally neat but historically incoherent evidence.

### Engineering lesson

**Share observation identity before sharing conclusions.**

The ordinary experiment reuses the already-acquired identity/transition and treats later source evidence as belonging to that exact target.

---

## 4. Target acquisition: source facts before relationships

The target-side source owner is `experiments/api_target_context.py`.

Its responsibility is deliberately narrower than correspondence.

It:

1. validates the exact target commit and tree;
2. inventories eligible files;
3. acquires bounded complete text;
4. extracts dependency declarations;
5. delegates Python import/reference analysis to the existing binding owner;
6. records exclusions, omissions and gaps.

It does **not** establish:

- runtime import binding;
- installed versions;
- effective module exports;
- actual call dispatch;
- compatibility.

### 4.1 `TargetInventory`

The inventory binds source enumeration to an exact repository revision and tree SHA.

Conceptually:

```text
TargetInventory
  repository
  revision
  tree_sha
  entries
  truncated
```

A truncated tree immediately weakens absence claims. The experiment records an explicit gap instead of treating a provider-truncated inventory as complete.

### 4.2 Acquisition ordering is policy, not truth

Target files are prioritized roughly as:

```text
dependency declarations
→ changed paths
→ other eligible files
```

This helps preserve the declaration basis and decision-relevant material under finite budgets.

But the ordering does not imply:

- those files execute first;
- those files are more semantically important at runtime;
- other omitted files are irrelevant.

It is work allocation.

### 4.3 Dependency declarations

The target source owner retains supported requirement declarations such as:

- requirements-style files;
- selected `pyproject.toml` dependency arrays.

It preserves:

```text
package
specifier
extras
marker
group
source identity/location
```

Markers and constraints remain declarations. They are not automatically resolved into an installed environment.

### 4.4 Import/declaration candidate versus package mapping

`ImportDependencyCandidate` can connect an imported module spelling and a declared distribution using an explicit candidate basis such as same-name association.

That is intentionally called a **candidate**.

A Python namespace name and a distribution name can differ. A same-name match is useful evidence for exploration, not universal proof that the imported namespace came from that installed distribution.

### Source anchor

Pinned file:

`experiments/api_target_context.py`

Useful concepts:

- `TargetInventory`
- `DependencyDeclaration`
- `ImportDependencyCandidate`
- `ContextGap`
- `TargetContext`
- `extract_python_facts`
- `extract_dependency_declarations`
- `TargetContextAcquirer.acquire`

---

## 5. Exact old/proposed source is not the same thing as an adapter sample

One of the most important distinctions in the experiment is between different source roles.

The source layer can retain at least these roles:

```text
target
native_old_version
native_proposed_version
constraint_sample
```

They answer different questions.

### 5.1 Native old/proposed roles

For the dependency actually changed by the PR, the experiment can ask for source corresponding to the exact old/proposed version identities from the dependency transition.

Conceptually:

```text
PR says vendor 1.0 → 2.0
        ↓
ask source owner for:
  vendor 1.0 module X  [native_old_version]
  vendor 2.0 module X  [native_proposed_version]
```

This gives the experiment exact **source-version roles**.

It still does not prove that a runtime environment actually installed or executed those sources.

### 5.2 Constraint-selected samples

Adapter/framework exploration can instead encounter a declaration such as:

```text
bridge >=1,<2
```

The experiment may choose the latest stable registry release satisfying that visible constraint as a bounded sample.

That role is explicitly:

```text
constraint_sample
```

It means:

> This source was selected as a representative release satisfying the visible declaration under the experiment's sampling rule.

It does **not** mean:

> This is the version the target actually resolved or installed.

The focused test `test_latest_stable_constraint_is_sampling_not_resolved_version` protects this exact distinction.

### 5.3 Why role labels matter

Suppose a target call reaches a sampled framework source, which then appears to call the changed dependency.

If the sample is presented as the target's real installed framework version, the final comparison becomes misleading even if every line of source analysis is mechanically correct.

The correct chain is:

```text
target source observation
→ framework sample selected under visible constraint
→ source-level relationship in that sample
→ exact old/proposed changed-package source
→ local comparison
```

with the sample role still visible.

---

## 6. `PythonSourceAcquisitionRun`: share source work without turning it into resolution state

The reusable exact source owner is exposed through `PythonSourceAcquisitionRun` in `experiments/api_adapter_exploration.py`.

Its important responsibilities are:

- exact package/version/module questions;
- per-run release observation reuse;
- module result caching;
- explicit failure caching;
- bounded release/module/source work;
- retention of original question basis.

### 6.1 Typed source questions

A `PythonModuleSourceRequest` carries approximately:

```text
package
version
module
version_basis
origin evidence, when available
```

The `version_basis` records why that version is being inspected:

- `native_old_version`;
- `native_proposed_version`;
- `constraint_sample`;
- `explicit_version`.

The question may also preserve the original import/reference evidence that caused the source request.

Crucially:

> **Reason to inspect source is not proof that the inspected source is the runtime callee.**

### 6.2 Conditional origin can coexist with exact source acquisition

This is subtle and important.

Imagine source says:

```python
if enabled:
    from vendor import send
send(...)
```

The changed dependency transition may still justify acquiring `vendor` old/proposed source for an explicit candidate examination.

That does not allow the experiment to rewrite the target binding from `conditional` to `established`.

Both statements can simultaneously be true:

```text
exact vendor old/proposed source acquired
AND
target call's effective import origin remains conditional
```

The experiment intentionally preserves both dimensions.

### 6.3 Run-local cache semantics

Within one source run, repeated questions for the same release/module can reuse:

- release metadata;
- tag resolution;
- repository inventory;
- module text;
- failures.

This serves two purposes:

1. request/resource control;
2. observation consistency within one run.

It is not a persistent dependency resolver or package database.

### 6.4 Failure caching matters

A failed source question is also part of the run's evidence.

Silently retrying every consumer request could create different observations and hide the original failure boundary.

The run therefore caches success/failure at the source-owner layer, while later live orchestration work may separately define admitted retry rules.

### 6.5 Finite source budgets

At this horizon, the reusable run keeps explicit ceilings such as:

```text
4 release identities
12 module attempts
2 MiB admitted source text
```

These are local source-work bounds, not provider-account quotas and not whole-process memory bounds.

A module left unexamined because the run hit a limit is not evidence that the module does not contain the relationship.

### Source anchor

Pinned file:

`experiments/api_adapter_exploration.py`

Useful entry points:

- `AdapterModuleSample`
- `PythonModuleSourceRequest`
- `ExaminedPythonModule`
- `PythonSourceAcquisitionRun`
- `select_exploration_version`
- `_module_path`

Focused controls:

`experiments/tests/test_api_adapter_exploration.py`

Especially:

- latest stable sample is not resolved version;
- conditional possible origin does not trigger ordinary positive sampling;
- branch alternatives retain uncertainty;
- sample budgets retain omitted candidates;
- same-release module questions reuse release/tree work;
- provider/source failures remain explicit.

---

## 7. Ordinary input composition: retain text, roles and omissions

The ordinary driver is `experiments/api_ordinary_call_signature_trial.py`.

Its acquisition entry eventually has this shape:

```text
acquire_ordinary_comparison_inputs(repository, PR number, providers...)
```

Importantly, callers do **not** supply:

- target source file paths;
- callable pairs;
- expected outcomes;
- known old/fixed adapter versions.

The experiment must derive useful material from ordinary evidence.

### 7.1 Library material is admitted before broad target text

The ordinary preparation step gives changed-package/library source roles priority before the target inventory consumes the analysis material budget.

Why?

Because a giant target repository could otherwise consume the retained-material ceiling and silently discard one side of the actual old/proposed comparison.

That would produce a strange result:

```text
lots of target source retained
but one changed dependency side missing
```

The chosen policy protects the decision-critical comparison material first.

This is work allocation, not runtime truth.

### 7.2 Internal source closure

After a qualified module is acquired, the driver examines its imports and can schedule additional modules from the **same qualified repository/release**.

This is how a package facade can lead to an implementation module without accepting a caller-supplied source path.

Example:

```text
vendor/__init__.py
  from .implementation import Base
        ↓
qualified exact release inventory
        ↓
vendor/implementation.py
```

The closure is bounded and inventory-supported.

It does not follow arbitrary runtime imports or dynamic module construction.

### 7.3 Priority can be promoted by stronger later evidence

A subtle bug later showed that a module first seen weakly—such as through a broad wildcard path—could be stuck with low priority even after direct call/import evidence appeared.

The driver was corrected so still-pending work can be promoted by stronger evidence.

This is an important general lesson:

> **A scheduling score based on evidence must be monotonic with stronger evidence until the work is consumed.**

Completed work is not requeued; pending work can receive a better priority.

### 7.4 Source retention versus acquisition receipt

The ordinary envelope separates two things:

```text
acquisition receipt
  identities / requests / provenance / gaps / costs

retained source companion
  complete admitted text used by analysis
```

A hash-only acquisition manifest is not equivalent to the full source text needed for later source inspection or call/signature analysis.

This distinction later becomes crucial during source-first capacity work.

---

## 8. Source correspondence is a separate owner

The source-path owner is `experiments/api_source_correspondence.py`.

Its module contract is explicit:

> consume a qualified retained catalog and module roles; add bounded declaration/import/initializer/protocol paths; call the unchanged argument checker; do not solve effective exports, installed namespace, decorators, MRO, execution or runtime dispatch.

This separation is essential.

The correspondence owner answers:

> Which captured source declarations are plausible structural destinations for this target-rooted call, and what source steps/premises support each alternative?

It does not answer:

> Which destination did Python runtime actually call?

---

## 9. A source candidate is a path plus premises, not a guessed callee

A useful source candidate contains more than the destination signature.

Conceptually it preserves:

```text
root target call
callee source role/version/module
selected declared signature
source relationship steps
receiver mode
premises
local comparison
```

A `SourceRelationshipStep` binds each step to:

```text
unit_id
exact source span
operation
literal expression
```

That means a candidate can be inspected as an evidence path rather than a mysterious graph edge.

### Typical operations

Across the supported families, steps can include concepts such as:

```text
import_origin
reexport
declaration
class_declaration
declared_base
initializer
allocation
attribute_getter
factory_return
call_protocol
```

Not every operation existed in method1; protocol/factory support introduced a later correspondence method version with its own operation vocabulary.

---

## 10. Direct alias/declaration path

The simplest ordinary correspondence looks like:

```python
from vendor import send as deliver
deliver(app=1)
```

with old/proposed retained source declaring `send`.

The correspondence owner can:

1. start from the target call's binding alternatives;
2. follow the import origin;
3. find matching declarations in the qualified native old/proposed sources;
4. keep both roles separate;
5. invoke the unchanged checker.

A focused control demonstrates:

```text
native_old_version      → bound
native_proposed_version → rejected
```

without any caller-supplied callable selector.

Even here the candidates retain a premise equivalent to:

```text
installed namespace and runtime dispatch not established
```

### Engineering lesson

Automatic source discovery does not eliminate conditionality. It eliminates the **human answer selector**.

---

## 11. Re-exports and relative source paths

Real Python libraries often expose public names through facade modules.

For example:

```text
package/__init__.py
  from .impl import send
        ↓
package/impl.py
  def send(...)
```

The correspondence owner can follow bounded source syntax through qualified modules.

### 11.1 Relative import resolution is repository-local

`absolute_import(...)` resolves relative spelling only inside the captured repository namespace.

It does not claim that the resulting module is the effective installed namespace at runtime.

### 11.2 Star exports preserve uncertainty

A `from .impl import *` can expose possible declarations, but the source owner does not claim exact effective `__all__`/runtime export membership unless established.

Candidates retain premises such as:

```text
star_export_membership_not_established
```

### 11.3 Repeated definitions remain alternatives

If a retained module contains several matching declarations, the correspondence owner does not silently select the first one.

It records alternatives and may emit a gap such as:

```text
multiple_declared_definitions_retained
```

This is especially important later for overload-decorated callables.

---

## 12. Initializer and parent-initialization paths

The next important family handles class initialization and `super()`-style source relationships.

A representative controlled shape is:

```text
target
  from facade import Client
  Client(app=1)
        ↓
facade.Client.__init__
  super().__init__(app=app)
        ↓
qualified base declaration
        ↓
old/proposed Base.__init__
```

The correspondence owner can connect these source declarations conditionally.

### 12.1 Nested callbacks must not become parent execution steps

If the initializer body contains:

```python
def never_called():
    vendor.Base(app=1)

ignored = lambda: vendor.Base(app=1)

super().__init__(app=app)
```

only the selected initializer body's actual lexical call is eligible for the parent-initialization path.

Nested function/lambda bodies do not become execution steps of the outer initializer merely because their syntax is physically nested.

The correspondence helper therefore uses lexical-body traversal that excludes nested definitions/callbacks.

### 12.2 MRO remains a premise

Even when the class source declares a base, the experiment does not solve arbitrary effective MRO/descriptor behavior.

A candidate can retain a premise like:

```text
builtin_super_and_effective_mro_assumed
```

and use `one_receiver_assumed` for the local checker.

Again:

```text
source path established enough to compare
!=
runtime dispatch established
```

---

## 13. Conditional `try`-import superclass hypotheses

Real compatibility code often contains fallback imports:

```python
try:
    import newer as backend
except ModuleNotFoundError:
    import vendor as backend

class Client(backend.Parent):
    ...
```

The original binding owner may correctly leave the effective source conditional.

The correspondence layer can still retain a guarded source hypothesis for each supported alternative.

It must carry premises such as:

```text
unresolved_try_import_base_source_hypothesis
exception_matching_import_success_and_base_binding_not_established
```

### Important refusal rule

Known writes, deletion, dynamic namespace mutation or incompatible rebinding after the import block can make the hypothesis unsafe.

In those cases, the route is refused rather than pretending the earlier import still controls the base.

The focused test explicitly checks rebinding, deletion, non-import writes and dynamic namespace operations.

### Engineering lesson

**Uncertainty can justify a labelled hypothesis; it cannot justify a fabricated positive binding.**

---

## 14. Local namespace collisions preserve alternatives

Consider a repository containing both:

```text
target/vendor.py
```

and an external distribution/module also named `vendor`.

A naive source resolver might pick one namespace by convention and lose the other.

The experiment instead preserves local and external candidates when the captured evidence cannot disambiguate them.

Candidates carry a premise such as:

```text
local_and_external_namespace_candidates
```

The test verifies that target, native-old and native-proposed alternatives can coexist.

This is exactly the kind of ambiguity that should remain visible rather than being “cleaned up” into one convenient path.

---

## 15. Multiple bases and overloads are alternatives, not runtime selection

Two recurring Python features pressure the source-correspondence boundary:

### Multiple bases

```python
class Client(vendor.A, vendor.B):
    def __init__(self):
        super().__init__()
```

The experiment can retain both declared source alternatives.

It does not become a complete MRO solver.

### Overload declarations

A class may contain:

```python
@overload
def __call__(...): ...

@overload
def __call__(...): ...

def __call__(self, *args, **kwargs): ...
```

All declarations are source facts with distinct spans.

The correspondence owner preserves them as alternatives; the saved view exposes decorator strings as syntax.

It does not silently decide which overload is the runtime effective signature.

This distinction becomes central in the retained pytest protocol case.

---

## 16. Gaps are first-class output

The ordinary source-discovery result can legitimately contain **zero comparisons**.

That is not a failure of representation.

The result may instead preserve reasons such as:

```text
named_declaration_or_reexport_not_found
source_relationship_cycle
source_relationship_depth_limit
comparison_candidate_limit
original_import_step_unavailable
inherited_or_missing_protocol_method
factory_return_expression_unsupported
source_path_limit
```

The important rule is:

> **A bounded traversal limit or unresolved relationship becomes a gap, not a global absence claim.**

For example, a missing source side cannot be translated into:

```text
API removed
```

unless another owner has enough evidence to support that proposition.

---

## 17. Ordinary result format versus curated result format

The curated reader from Artifact 01 required:

```text
proof = retained_curated_source_comparison
at least one selected pair
```

The ordinary experiment needed a different envelope because:

- candidate paths are discovered, not selected by a reviewer;
- zero useful candidates can be an honest result;
- discovery gaps and source relationships must be retained;
- acquisition provenance/omissions matter.

So the ordinary path uses its own versioned formats while reusing shared fact/comparison decoding.

At this horizon, relevant proof labels include:

```text
controlled_ordinary_pr_composition
retained_component_discovery
fresh_ordinary_pr_acquisition   # later live orchestration responsibility
```

This note focuses on the first two.

### Proof classes must not be blurred

A locally authored controlled provider composition proves:

```text
the ordinary composition/code path works against controlled evidence
```

A retained real-source component discovery proves:

```text
the correspondence method finds useful relationships in previously captured real source
```

Neither is automatically a fresh live-provider ordinary PR proof.

---

## 18. Controlled ordinary real flow: target → facade → wrapper → native dependency

The October 29 controlled ordinary result is a compact end-to-end teaching substrate.

Its flow is conceptually:

```text
repository + PR
      ↓
exact dependency transition: vendor old → proposed
      ↓
target import/call
      ↓
bridge re-export
      ↓
mediator.Client initializer
      ↓
declared vendor.Base / super initialization
      ↓
relative vendor implementation
      ↓
old/proposed native declaration comparison
```

No callable selector or expected answer enters the ordinary producer.

### Result

The retained result contains three meaningful role-labelled comparisons:

| Role | Version role | Local result |
| --- | --- | --- |
| sampled wrapper | constraint sample | bound |
| native changed package | old | bound |
| native changed package | proposed | rejected |

The proposed side rejects the explicit `app` keyword under the retained source/receiver premises.

### What this proves

It proves that the normal experimental composition can:

- start from repository/PR input;
- acquire/retain qualified source roles;
- close internal module source;
- discover re-export/initializer paths;
- run the unchanged checker;
- retain useful discriminatory output;
- reopen the result offline.

### What it does not prove

It does not prove:

- real GitHub/PyPI provider behavior;
- target installation;
- runtime dispatch;
- general Python source correspondence;
- compatibility;
- product adoption.

### Evidence anchor

`working-memory/evidence/2026-10-29-source-correspondence-and-ordinary-retention/REVIEW.md`

---

## 19. The incomplete-side control teaches negative-evidence discipline

A particularly useful control retains:

```text
old declaration available
proposed side empty/missing declaration
```

The result keeps the old-side comparison and a missing-declaration gap.

It does **not** conclude:

```text
proposed API removed
```

Why?

Because:

```text
missing captured declaration
```

is weaker than:

```text
complete qualified evidence proves no declaration exists
```

This same discipline later governs partial-analysis and transfer work.

---

## 20. Protocol/factory correspondence: why the direct/initializer family was not enough

The retained pytest case contained a structurally different API use:

```python
pytest.mark.parametrize(...)
```

This is not simply:

```text
import function
→ call function
```

A useful source-level path looks more like:

```text
pytest.mark
→ re-exported MARK_GEN
→ MarkGenerator(...) allocation
→ MarkGenerator.__getattr__("parametrize")
→ returns MarkDecorator(...)
→ MarkDecorator.__call__(...)
```

A direct/re-export/initializer resolver cannot reach this relationship without some bounded object/protocol reasoning.

The project deliberately did **not** jump to a general value-flow/type engine.

Instead it added one explicitly bounded syntax family.

---

## 21. The bounded protocol/factory pattern

The supported pattern is approximately:

```text
module-level Name assignment
  = declared-class allocation
        ↓
that class's own __getattr__
        ↓
lexical return directly allocates another declared class
        ↓
that returned class's own __call__ declaration(s)
```

The source path is retained through literal steps:

```text
allocation
attribute_getter
factory_return
call_protocol
```

### What remains a premise

The candidate carries conditions such as:

```text
module allocation binding and constructor success not established
attribute lookup / __getattr__ activation not established
factory constructor arguments not checked
getter call arguments and binding not checked
execution reaches selected return/branch
factory returns selected declared class instance
effective protocol method and receiver binding not established
```

This is why the path can be useful without pretending to be runtime object-flow proof.

---

## 22. Real retained pytest flow

The retained glyphsLib/pytest source gives the best real example.

The target transition is:

```text
pytest 9.0.2 → 9.0.3
```

The retained target contains calls including:

```text
pytest.raises(...)
pytest.mark.parametrize(..., ids=...)
```

### 22.1 Direct `pytest.raises`

The curated second-case evidence showed the direct call locally bound against both old/proposed retained `raises` declarations.

This is a straightforward direct source relationship.

### 22.2 `pytest.mark.parametrize`

The protocol path is:

```text
target pytest.mark.parametrize
        ↓
pytest.mark re-export
        ↓
MARK_GEN re-export
        ↓
MarkGenerator allocation
        ↓
MarkGenerator.__getattr__
        ↓
return MarkDecorator(...)
        ↓
MarkDecorator.__call__ declarations
```

The later retained-component discovery ran over all 12 already-selected real files without being given a callable pair or expected answer.

It automatically connected **two target parametrize call sites** through the protocol chain to old/proposed `MarkDecorator.__call__` declaration alternatives.

### 22.3 Three declarations remain three alternatives

Each retained version had:

- two overload-decorated declarations;
- one undecorated implementation declaration.

For two call sites × two versions × three declarations, the protocol-specific direct set contains:

```text
12 conditional comparisons
```

These are **not 12 independent cases**.

They are multiple declaration alternatives for two call sites in one retained scenario.

### 22.4 The undecorated implementation

The four call-site/version comparisons against the undecorated implementation show `ids` received through `**kwargs` and locally bind under the one-receiver/source premises.

That means:

> the selected declared implementation can structurally receive the explicit `ids` keyword.

It does not mean:

- pytest marker semantics are proven;
- the overload set selected that implementation at runtime;
- the marker executed;
- the target test ran;
- the update is compatible.

### 22.5 Overload alternatives

Some overload-decorated alternatives locally bind and some reject.

The correct representation is to preserve the alternatives and show their decorator syntax.

The wrong representation would be:

```text
one overload rejected
→ pytest incompatibility
```

because the experiment has not established effective overload/runtime selection.

### Evidence anchors

- `working-memory/evidence/2026-10-28-caller-signature-second-real-case/comparison-view.txt`
- `working-memory/evidence/2026-10-30-protocol-factory-source-correspondence/REVIEW.md`

---

## 23. Unsupported protocol shapes remain gaps

The protocol family is intentionally narrow.

Examples that remain unsupported or explicitly refused include:

- arbitrary factory functions;
- return-through-local-variable propagation;
- inherited protocol lookup;
- multi-attribute dynamic chains;
- dynamically computed class expressions;
- general heap/object identity;
- async/generator getter as direct instance-return evidence;
- nested callback returns;
- mutation/deletion that invalidates the allocation/export story.

### Async/generator correction

Boundary review found an important subtlety:

A lexical `return` inside an async/generator-style getter does not justify treating the attribute lookup as returning that class instance under the simple synchronous pattern.

The correspondence method was tightened to refuse this direct-instance interpretation.

This was a new-layer correspondence correction; the binder/checker did not need modification.

### Engineering lesson

**When a source-pattern method grows, reject unsupported execution semantics explicitly instead of broadening a syntax observation into a runtime claim.**

---

## 24. Protocol method versioning and fixed decoding

Adding protocol operations changed the correspondence representation.

The experiment therefore versioned the method rather than pretending the saved shape was unchanged.

Conceptually:

```text
method1
  direct / re-export / initializer vocabulary

method2
  adds allocation / attribute_getter / factory_return / call_protocol
```

The fixed reader supports historical method1 bundles with their historical operation set and method2 bundles with the new set.

A method2 protocol bundle cannot simply be relabelled method1 and accepted.

The reader also validates that the required ordered protocol sequence and minimum premises remain present.

This is an important historical-integrity principle:

> **A reader can support multiple historical methods without pretending they are the same method.**

---

## 25. Cold opening: saved evidence, not rerun discovery

Both the direct/initializer ordinary path and the protocol path preserve fixed offline opening.

Opening a saved result must not perform:

```text
provider acquisition
AST parsing
source correspondence discovery
argument checking
model inference
```

The tests explicitly patch these operations to fail during open.

A successful cold open validates saved evidence closure and renders it.

It does not regenerate today's answer from old source.

### Why this matters

Suppose correspondence method2 is later replaced by a better method3.

Historical method2 evidence should remain inspectable as:

```text
what method2 actually produced under its recorded inputs/limits
```

not silently transformed into:

```text
what method3 would produce today
```

This makes failures, corrections and transfer claims auditable.

---

## 26. Reader integrity versus semantic truth

The saved ordinary reader validates things such as:

- supported format/method version;
- target transition coherence;
- module/source role membership;
- exact source companion closure;
- source spans inside retained text;
- relationship endpoints;
- ordered source steps;
- required premises;
- call/signature/comparison identity;
- gap/omission structure;
- result/source digests.

This proves internal saved-record integrity.

It does not independently establish:

- publisher authenticity beyond recorded provenance owners;
- runtime environment;
- semantic compatibility;
- target execution.

---

## 27. Important engineering corrections from this slice

The final design is easier to understand if you remember the mistakes it corrected.

### 27.1 Curated pair success was not ordinary discovery

Two real curated cases proved the checker, not the source-discovery responsibility.

The ordinary path had to earn caller/callee relationships from source evidence.

### 27.2 Source identity/hash was not retained source text

Existing manifests could prove which file had been acquired without carrying enough bytes to support later full call/signature inspection.

The ordinary envelope therefore retained complete admitted text separately.

### 27.3 A constraint sample was not a resolved installed version

The sampling owner explicitly labels latest satisfying releases as samples.

### 27.4 Conditional source acquisition did not promote binding

Successfully acquiring the candidate module does not tell us which conditional branch ran.

### 27.5 Own-repository namespace initially hid external alternatives

During source-correspondence Build, a namespace rule incorrectly hid declared external old/proposed alternatives.

The correction preserved both local/external candidates when evidence could not choose.

### 27.6 Multiline display initially flattened an already-rendered view

This was a presentation-boundary defect, not correspondence/checker failure.

The fix stayed at the presentation owner.

### 27.7 Nested callback syntax is not outer-body execution

The lexical body traversal was designed so nested function/lambda calls do not become steps of the selected initializer/factory path.

### 27.8 Overload presence is not effective-overload selection

Multiple declarations stay alternatives with syntax/decorator context.

### 27.9 Async/generator lexical return is not direct instance evidence

Protocol boundary review added an explicit refusal instead of overclaiming object flow.

### 27.10 Zero candidates can be an honest result

The ordinary format allows zero comparisons plus explicit gaps. It does not require manufacturing a “useful” answer.

---

## 28. What the focused tests actually protect

The most useful tests are the ones that discriminate boundaries.

### Source acquisition / sampling tests

From `experiments/tests/test_api_adapter_exploration.py`:

- `test_latest_stable_constraint_is_sampling_not_resolved_version`
  - protects sample-vs-resolution meaning.

- `test_conditional_possible_origin_does_not_trigger_positive_exploration`
  - prevents a conditional binding from being promoted into positive ordinary sampling.

- `test_budgets_keep_unexamined_candidates_and_do_not_claim_coverage`
  - protects omission semantics.

- `test_same_release_modules_share_registry_tag_tree_budget`
  - proves per-run reuse without creating persistent resolution state.

### Direct/re-export/initializer correspondence tests

From `experiments/tests/test_api_source_correspondence.py`:

- `test_direct_alias_change_is_discovered_for_both_roles_without_selectors`
  - ordinary candidate discovery finds old/proposed declarations without supplied pair selectors.

- `test_relative_star_reexports_and_repeated_definitions_preserve_alternatives`
  - re-exports and repeated definitions remain alternatives.

- `test_conditional_target_origin_is_not_promoted_by_source_success`
  - source success does not rewrite binding truth.

- `test_initializer_parent_path_is_target_rooted_and_skips_nested_callback`
  - protects lexical-body scope and parent-initialization path.

- `test_missing_side_cycle_and_bounded_paths_remain_gaps_not_absence_claim`
  - protects bounded traversal semantics.

- `test_local_namespace_collision_retains_external_old_and_proposed_alternatives`
  - protects namespace ambiguity.

- `test_multiple_declared_bases_stay_alternatives_without_mro_selection`
  - prevents source traversal from becoming an MRO solver.

- unresolved try-import base controls
  - allow guarded hypotheses but refuse unsafe rebinding/dynamic writes.

### Protocol/factory tests

The protocol controls protect:

- allocation → getter → return → call-protocol sequence;
- renamed/imported/annotated allocations;
- overload and competing allocation alternatives;
- unsupported factory return expressions;
- missing protocol methods;
- nested-return refusal;
- path/pair limits;
- source mutation/export gaps;
- method-version/premise/text corruption;
- cold opening without AST/network/discovery.

### What these tests do not prove

They do not prove:

- arbitrary Python import semantics;
- dynamic value flow;
- runtime object type;
- effective MRO/descriptor dispatch;
- installed versions;
- real provider acquisition;
- target execution;
- whole-update compatibility;
- product reliability.

---

## 29. Source walkthrough: shortest useful path

If you return to the code later, use this order.

### Step 1 — target facts

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_target_context.py
```

Read:

1. `TargetContext`;
2. `extract_python_facts`;
3. `extract_dependency_declarations`;
4. `TargetContextAcquirer.acquire`.

Ask:

> Which facts are observations from exact captured source, and which relationships remain candidates?

### Step 2 — source acquisition roles

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_adapter_exploration.py
```

Read:

1. `PythonModuleSourceRequest`;
2. `ExaminedPythonModule`;
3. `PythonSourceAcquisitionRun`;
4. `select_exploration_version`;
5. `_module_path`.

Ask:

> Which field records why a version was inspected, and why does that not establish installed state?

### Step 3 — ordinary composition

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_ordinary_call_signature_trial.py
```

Focus on:

- `prepare_ordinary_inputs`;
- `encode_ordinary_inputs`;
- `acquire_ordinary_comparison_inputs`;
- ordinary comparison/read/open functions.

Ask:

> Where are complete source text, source roles, acquisition receipts and omissions kept distinct?

### Step 4 — correspondence

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_source_correspondence.py
```

Focus on:

- `PythonSourceModule`;
- `SourceRelationshipStep`;
- `absolute_import`;
- declaration/re-export resolution;
- initializer/base handling;
- guarded try-import base hypothesis;
- protocol/factory path functions;
- `discover_source_candidates`.

Ask:

> Which parts are source syntax observations, and which premises explicitly admit that runtime behavior is not established?

### Step 5 — real retained results

Read:

- `working-memory/evidence/2026-10-29-source-correspondence-and-ordinary-retention/REVIEW.md`;
- `working-memory/evidence/2026-10-30-protocol-factory-source-correspondence/REVIEW.md`;
- `working-memory/evidence/2026-10-28-caller-signature-second-real-case/comparison-view.txt`.

Trace one initializer path and one pytest protocol path end to end.

---

## 30. What you should be able to explain after this note

### Must own

You should be able to explain:

- why curated source-pair proof is different from ordinary discovery;
- why one PR/dependency observation horizon matters;
- target source acquisition versus source correspondence;
- exact old/proposed source roles versus constraint-selected samples;
- why a source request's version basis is not installed-version truth;
- why acquiring a conditional source does not promote the original binding;
- why full source text and a hash/fact manifest are different retained responsibilities;
- how direct, re-export and initializer source paths work;
- why nested callbacks are excluded from an outer lexical body path;
- why source correspondence does not establish runtime dispatch;
- why local/external namespace collisions preserve alternatives;
- why repeated definitions, multiple bases and overloads remain alternatives;
- why source traversal limits produce gaps rather than absence;
- the bounded protocol/factory pattern;
- why `pytest.mark.parametrize` requires more than direct callable lookup;
- why `ids` reception through `**kwargs` is only local structural evidence;
- why async/generator getter handling required an explicit refusal;
- why cold opening must not rerun discovery/checking.

### Understand operationally

You should be comfortable reading:

- source role records;
- repository inventories;
- dependency declarations and markers;
- module requests and source-run work counters;
- source relationship steps;
- path premises;
- gap records;
- ordinary result/proof labels;
- retained source companion identities;
- fixed reader validation.

### Lookup-level

You do not need to memorize:

- every acquisition dataclass field;
- every provider method;
- exact request-count constants;
- every source-step operation string;
- every JSON field;
- every test helper.

### Deliberately deferred

Do not try to solve here:

- live provider reservation/retry orchestration;
- general Python value-flow/type inference;
- actual installed namespace resolution;
- runtime MRO/descriptor execution;
- semantic behavior;
- capacity/partial-analysis architecture;
- transfer qualification;
- native product integration.

---

## 31. Fast relearning route

### Five-minute mental refresh

Recall:

```text
ordinary PR
→ one exact dependency transition
→ qualified target/library source roles
→ source relationship candidates
→ unchanged local checker
→ retained paths + gaps + source
```

Then remember:

```text
exact source role != installed runtime
source path != dispatch
sample != resolved version
unexamined != absent
```

### Fifteen-minute source refresh

Read:

1. `PythonModuleSourceRequest` + `PythonSourceAcquisitionRun`;
2. `SourceRelationshipStep` + the correspondence module contract;
3. one direct/initializer test;
4. one protocol/factory test.

### Thirty-minute real-case refresh

Trace:

1. the controlled ordinary target→bridge→mediator→vendor initializer flow;
2. the retained pytest `mark.parametrize` chain;
3. one overload alternative;
4. one explicit gap/refusal;
5. cold-open proof.

If you can explain why all of those can coexist without establishing runtime dispatch, you have recovered the core mechanism.

---

## 32. Transfer questions

### 1. Exact source plus conditional import

A PR changes `vendor` 1.0→2.0. The target contains:

```python
if enabled:
    from vendor import send
send(app=1)
```

The experiment successfully acquires exact `vendor` 1.0 and 2.0 `send` declarations.

Should the target call's binding become established? What can the correspondence owner legitimately do?

### 2. Constraint sample

The target declares `bridge>=1,<2`. The experiment samples `bridge 1.9` because it is the latest stable release satisfying the visible constraint.

What exactly may the result call this source? What stronger claim is forbidden?

### 3. Missing proposed declaration

Old source contains `def send(...)`; the proposed captured module is empty because the selected source closure did not find a declaration.

Can the experiment claim the API was removed? What should the result contain instead?

### 4. Multiple overloads

A retained class contains two `@overload` declarations and one undecorated implementation. A target call is discovered automatically.

Should the source-correspondence layer choose the declaration that produces the cleanest answer? Why or why not?

### 5. Factory protocol

A module variable is assigned `Generator()`. Its `__getattr__` returns `Decorator()`, whose class declares `__call__`.

Which parts of that chain are source observations, and name at least four runtime premises that remain unresolved.

---

## 33. Answers/checkpoints for self-review

1. No. Exact source acquisition does not establish branch activation. The binding remains conditional. The correspondence owner may retain old/proposed candidate paths labelled with the conditional-origin premise and compare them locally without rewriting the binding.
2. It is a `constraint_sample`: a bounded source sample selected by the experiment's visible-constraint rule. It must not be called the target's resolved or installed version.
3. No. Preserve the available old-side evidence plus an explicit missing-declaration/source gap. Absence requires stronger qualified coverage than “the selected closure did not find it.”
4. No. Retain all supported declaration alternatives with exact spans/decorator syntax and let later evidence determine effective selection. Outcome-driven declaration selection would contaminate the evidence path.
5. Source observations include the module allocation syntax, the class's own `__getattr__` declaration, the direct lexical returned-class allocation and the returned class's own `__call__` declarations. Unresolved premises include allocation/constructor success, attribute lookup actually invoking that getter, branch/return execution, returned object identity, effective protocol method/receiver binding, installed version and runtime dispatch.

---

## 34. Final proof boundary

By the end of this experiment slice, UpgradePilot had moved materially beyond curated pair checking.

The demonstrated architecture was:

```text
ordinary repository/PR input
→ one shared identity/dependency horizon
→ bounded target + exact/sample source acquisition
→ complete admitted source retention
→ target-rooted direct/re-export/initializer/protocol source candidates
→ unchanged deterministic call/signature checker
→ explicit alternatives, premises, gaps and omissions
→ immutable versioned ordinary result
→ cold offline source/result inspection
```

The controlled ordinary flow demonstrated automatic discriminatory discovery for the direct/re-export/initializer family.

The retained real pytest source demonstrated that the bounded protocol/factory family can automatically connect `pytest.mark.parametrize` through re-export → allocation → `__getattr__` → returned class → `__call__` alternatives, while preserving overload and runtime uncertainty.

That is meaningful progress toward ordinary evidence acquisition.

It still does **not** establish:

- that fresh real providers will fit the same budgets;
- that source allocation priorities will retain the necessary closure under real pressure;
- installed versions;
- runtime dispatch/execution;
- behavioral compatibility;
- broad generality;
- native product integration.

The next engineering problem is therefore operational:

> Can the same ordinary pipeline acquire useful evidence from a fresh real PR under frozen provider/work budgets, and when it fails, can we diagnose and repair the correct owner without tuning the system to force an expected answer?

That is the subject of Artifact 03.

---

## Pinned source and evidence anchors

Implementation:

- `experiments/api_target_context.py`
- `experiments/api_adapter_exploration.py`
- `experiments/api_change_source_acquisition.py`
- `experiments/api_target_context_smoke.py`
- `experiments/api_source_correspondence.py`
- `experiments/api_ordinary_call_signature_trial.py`
- `experiments/api_python_bindings.py`
- `experiments/api_call_signature.py`

Focused tests:

- `experiments/tests/test_api_adapter_exploration.py`
- `experiments/tests/test_api_public_pr_context.py`
- `experiments/tests/test_api_source_correspondence.py`
- `experiments/tests/test_api_ordinary_call_signature_trial.py`

Historical progression/evidence:

- `working-memory/2026-10-28_second-real-caller-signature-case_qualification-and-evaluation-cycle.md`
- `working-memory/2026-10-28_pr-driven-caller-signature-integration_design-cycle.md`
- `working-memory/2026-10-29_pr-source-acquisition-integration_build-cycle.md`
- `working-memory/2026-10-29_source-correspondence-and-ordinary-retention_build-cycle.md`
- `working-memory/2026-10-30_protocol-factory-source-correspondence_build-cycle.md`
- `working-memory/evidence/2026-10-28-caller-signature-second-real-case/comparison-view.txt`
- `working-memory/evidence/2026-10-29-source-correspondence-and-ordinary-retention/REVIEW.md`
- `working-memory/evidence/2026-10-30-protocol-factory-source-correspondence/REVIEW.md`

For local source inspection, keep the snapshot pinned, for example:

```sh
git show c53430c6e3fb4f24147a28aa642ab94834233243:experiments/api_source_correspondence.py
```

Do not substitute mutable `main` and still call the explanation this frozen experiment snapshot.

`UP-SKILL:upgradepilot-learning-artifact`
