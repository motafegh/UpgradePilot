# Failure-driven blocker resolution and experimental engineering

**Educational snapshot:** 2026-11-01 learning package, explaining the frozen experiment program at repository horizon **`c53430c6e3fb4f24147a28aa642ab94834233243`**.

**Learning responsibility:** understand how UpgradePilot took a real ordinary dependency-update PR from repeated fresh-attempt failures to the first useful paired-source result without rewriting history, forcing an expected answer, or repairing the wrong layer. The central subject is not the HTTPX case itself; it is the engineering method used to diagnose acquisition, allocation, source-correspondence, transport and representation failures under fixed evidence/proof boundaries.

**Not this note's responsibility:** the later LifeLog-scale source-first/partial-analysis architecture, untouched transfer qualification, native productization, general Python compatibility, runtime dispatch or maintainer usefulness. Artifact 04 owns the later capacity/work-admission redesign; Artifact 05 owns transfer methodology.

The live-attempt labels such as `S002`–`S008` are retained here only as historical provenance. They are **successive immutable attempts against one underlying real PR**, not independent cases and not the active vocabulary for the engineering lessons.

---

## 1. The real case and the actual objective

The blocker-resolution campaign used one real public dependency-update PR:

```text
Repository: Aidan-Wallace/kubernetes-dashboard-token-api
PR:         #20
Dependency: HTTPX 0.27.2 → 0.28.1
Base:       b065646e4b7b894964567950f9ad770b02c136c2
Head:       391508134b083b8f54461c0b576e8f7985c6ecb4
```

The experiment already had a retained curated HTTPX example where an older captured Starlette call forwarded `app=` to an old/proposed HTTPX initializer and the proposed signature rejected that keyword. But the ordinary real-PR task was **not**:

> Reproduce the historical `app` rejection by any means necessary.

The real task was:

> Starting from the ordinary PR, acquire enough trustworthy source evidence under frozen budgets to produce useful old/proposed caller/signature evidence, while preserving provenance, uncertainty, omissions and the exact method that produced each result.

That difference is essential.

A result where both versions bind can still be a successful experiment if it honestly answers the source question under the admitted evidence. A forced rejection would be methodologically worse than an informative non-rejection.

---

## 2. The engineering loop to own

Every material repair in this campaign should be reasoned about using the same loop:

```text
OBSERVED SYMPTOM
        ↓
TEMPTING EXPLANATION
        ↓
MEASURE / INSPECT THE EARLIEST OWNER
        ↓
CLASSIFY THE ACTUAL FAILURE
        ↓
REPAIR ONLY THAT RESPONSIBILITY
        ↓
ADD A DISCRIMINATING CONTROL
        ↓
FREEZE THE SUCCESSOR METHOD / CONTRACT
        ↓
RUN A NEW ATTEMPT
        ↓
PRESERVE THE PREDECESSOR UNCHANGED
```

This sounds straightforward, but most engineering shortcuts violate one of these transitions.

Common mistakes would have been:

- increasing every budget because useful evidence was missing;
- changing the binder because a provider request timed out;
- treating unavailable source as an absent API;
- rerunning a failed attempt after a transient endpoint recovered and calling the old attempt passed;
- deleting awkward gaps from the result so serialization fits;
- tuning source order to the known HTTPX path;
- requiring the fresh result to reproduce the historical mismatch;
- counting multiple source witnesses as independent real-world cases.

The blocker-resolution sequence is valuable because those shortcuts were explicitly avoided.

---

## 3. Before the first live attempt: acquisition policy is part of correctness

A fresh ordinary PR run is not just “call providers until enough data arrives.”

Source acquisition has several finite resources:

```text
GitHub request allowance
provider request allowance
release identities
module questions
source bytes
target-file attempts
analysis budgets
time
```

A policy that spends them in a poor order can make the final evidence weak even though every individual request succeeds.

The staged acquisition work therefore treated **source allocation** as an explicit responsibility.

The key distinction is:

```text
provider/account quota
    ≠
selected experiment work budget
```

For example, a run may stop at the experiment's selected 50 GitHub requests even if GitHub would have allowed thousands more. That stop is a methodological/resource choice, not proof that the provider account was exhausted.

Likewise, reaching a 12-module source-question ceiling means:

> the experiment chose not to inspect more modules under that profile.

It does not mean:

> no other relevant module exists.

### Why staged acquisition mattered

The changed dependency's old/proposed source is decision-critical. Optional adapter/framework exploration is useful, but it must not consume all work before the exact changed-package pair is acquired.

The intended policy eventually became roughly:

```text
exact PR/dependency identity
→ target/source roots
→ decision-critical changed-package old/proposed closure
→ strongest target-rooted adapter continuations
→ lower-priority sampled/internal work
→ explicit omissions when budget ends
```

The later failures show why that ordering had to be earned experimentally rather than assumed.

---

## 4. First fresh attempt: a provider timeout is not a semantic failure

The first official fresh attempt reached a source-acquisition request for the exact FastAPI release and encountered a pre-response timeout.

That attempt was terminal under its frozen no-retry contract.

The important interpretation is:

```text
what failed?
  provider transport before usable response

what did not fail?
  call/signature binder
  source correspondence semantics
  API compatibility
  source absence proposition
```

A provider timeout tells us that the requested observation was not obtained in that attempt.

It does **not** tell us:

```text
FastAPI source does not exist
FastAPI is incompatible
HTTPX relationship is absent
the checker is wrong
```

### The later endpoint diagnostic

A separate diagnostic, `D001`, later requested the exact endpoint and succeeded:

```text
state: available
provider requests: 1
elapsed: ~0.36s
```

That was useful evidence about the likely transient nature of the earlier failure.

But it did not rewrite history.

The correct interpretation is:

```text
first official attempt:
  timeout under its frozen execution

later D001:
  endpoint available at a later observation time
```

Not:

```text
D001 succeeded
→ therefore the original failed attempt actually passed
```

### Transferable lesson

**Later availability can explain a historical transport failure; it cannot retroactively change the historical attempt's result.**

This is the first major no-regrade lesson of the campaign.

---

## 5. Successor attempt: the candidate frontier was too narrow

Once the transient timeout was no longer the active blocker, the next fresh attempt completed enough acquisition to expose a different problem.

Both FastAPI shim modules were acquired, but the experiment's candidate frontier stopped before following the useful Starlette continuation.

The frozen evidence described the situation as approximately:

```text
2 candidate attempts selected
FastAPI shim evidence acquired
Starlette continuation not reached
request policy still had room
```

This was **not** a Python checker defect.

It was a work-selection problem.

### Tempting wrong repair

A simple response would have been:

> Increase the candidate cap or breadth-first search until Starlette happens to appear.

But that can worsen the problem. More broad candidates can consume release/module budgets on unrelated roots before the useful re-export continuation is followed.

### Actual design correction: observed-symbol frontier

The successor design kept the existing target admission and source caps, but changed the priority of **continuations already justified by acquired source evidence**.

If the target-rooted question follows a member such as:

```text
TestClient
```

and an acquired source module contains a matching re-export:

```python
from package.module import TestClient
```

that continuation becomes higher priority than unrelated pending roots.

The important property is generality:

```text
observed member from target evidence
→ matching re-export continuation
```

not:

```text
if FastAPI then inspect Starlette
```

The design explicitly prohibited FastAPI/Starlette/HTTPX names, fixed source paths and expected results from producer logic.

### Discriminating proof

A renamed multi-root fixture had to show:

- the old queue misses the useful native frontier;
- the new queue follows the generic observed-symbol continuation;
- unrelated work remains explicitly omitted rather than silently disappearing.

### Transferable lesson

**When useful evidence is starved, first ask whether the allocation policy spends bounded work on the wrong questions. Do not immediately increase the budget.**

---

## 6. Next successor: module budget was spent on the wrong source family

The next fresh attempt got farther.

It retained both native HTTPX roots and both FastAPI/Starlette shim chains, but then spent its remaining module questions on Starlette internals. The actual HTTPX defining module was never acquired.

The exact evidence behind the follow-up design states:

```text
source module limit: 12
remaining 6 module questions spent on Starlette internals
no HTTPX defining module acquired
GitHub selected 50-request ceiling reached
```

Again, the checker was not the problem.

The system had source relationships, but its finite module work was allocated poorly for the comparison objective.

### Tempting wrong repair

Increase the 12-module cap.

That would hide the scheduling weakness and would not guarantee paired old/proposed material under larger repositories.

### Actual correction: native paired closure first

The successor work-selection rule became:

```text
native old/proposed internal questions
        ↓
matching package/module questions examined as a pair
        ↓
optional sampled-adapter internals afterward
```

This preserves the comparison's decision-critical material.

If the old side's internal defining module is relevant, the corresponding proposed side should be protected from starvation by unrelated sampled internals.

### What this does not mean

Paired source acquisition does not prove:

- both versions are installed;
- runtime dispatch reaches either module;
- the target actually used the sampled adapter path.

It only protects the evidence needed for a meaningful old/proposed structural comparison.

### Transferable lesson

**When the output requires a comparison, resource admission should protect both sides of the comparison before optional enrichment.**

---

## 7. Conditional superclass evidence: do not “fix” legitimate uncertainty

At the same stage, a separate retained diagnostic showed that the current Starlette class base had a possible HTTPX origin plus unknown alternatives because its fallback imports occurred inside unsupported `try` control flow.

A dangerous repair would have been:

> Teach the binder that this import is definitely HTTPX.

That would be false precision.

The binder's uncertainty was legitimate.

### Correct owner: source correspondence hypothesis

Instead of changing the binding state, the correspondence layer gained a weaker source-hypothesis route for a carefully bounded static class base whose uncertainty came from the specific examined `try`-import shape.

The candidate had to retain premises such as:

```text
unresolved_try_import_base_source_hypothesis
exception_matching_import_success_and_base_binding_not_established
```

and preserve import alternatives.

### Refusal conditions

If the root name was later:

- reassigned;
- deleted;
- mutated;
- replaced dynamically;
- affected by other unsafe namespace behavior;

the route remained refused.

### Transferable lesson

**Do not repair an honest lower-layer unknown merely because a higher-layer hypothesis could still be useful. Preserve the unknown and add the hypothesis at the owner that can state its premises honestly.**

---

## 8. Same successor exposed a stale-priority defect

Native-first paired closure improved policy, but another defect appeared.

A pending module could first enter the queue through weak evidence such as a wildcard observation. Later, stronger direct import/call evidence for that same module arrived—but the existing queued work kept its old weak priority.

So the system knew more, yet the scheduler did not update its decision.

### Correct rule

For work that is still pending:

```text
new evidence produces stronger priority
        ↓
replace/promote pending priority
```

For work already consumed:

```text
completed source question
        ↓
keep cached result
        ↓
do not silently rerun because later evidence is stronger
```

This is a general scheduling principle:

> **Evidence-driven pending priority should improve monotonically when stronger evidence arrives, without re-executing completed work.**

### Why this is not just optimization

Under finite budgets, stale priority changes which evidence exists at the end of the experiment. Therefore it affects proof coverage, not just performance.

---

## 9. The same attempt exposed a missing-module traversal defect

The expanded traversal also revealed a much more serious source-correspondence problem.

A literal relationship like:

```python
from .missing import *
```

could encounter the fact that the exact required module was not retained. Instead of stopping at that module boundary, the resolver could reinterpret the missing path through the captured parent package and continue recursively through additional wildcard relationships.

The retained diagnostic showed extreme state/gap growth:

```text
4,155 counted states
4,096 admitted plus refusal checks
7,174 omitted gap records
```

This was not useful ambiguity. It was artificial traversal created by crossing a source boundary that the evidence did not support.

### Correct repair

Preserve the exact module boundary implied by the observed import/re-export.

If that required module is not retained:

```text
record missing / unavailable / unsupported module
STOP that path
```

Do not reinterpret it through a parent package merely to keep searching.

### What must still remain

Real captured alternatives still survive:

- actual re-exports;
- actual cycles;
- namespace alternatives;
- explicit unavailable source gaps.

The repair is not “prune uncertainty.” It is “do not invent a relationship across a missing exact module boundary.”

### Transferable lesson

**Missing evidence should terminate the exact unsupported edge; it should not become permission to search through a different evidence object.**

---

## 10. Fresh successor: one-sided native evidence from another transport timeout

After those source-selection/correspondence repairs, the next attempt reached a different external failure.

One native side was available while a relevant proposed/source/provenance request timed out before receiving a usable response.

This produced asymmetric evidence.

The correct disposition was not:

```text
old source exists
proposed source missing
→ proposed API absent
```

It was:

```text
old-side evidence acquired
proposed-side observation failed at transport
→ comparison closure incomplete
```

### Why this matters

Asymmetric evidence is particularly dangerous because it looks like a semantic difference.

A system that drops the transport reason can accidentally transform:

```text
we failed to acquire proposed evidence
```

into:

```text
the proposed version lacks the evidence
```

Those are entirely different propositions.

### Transferable lesson

**Provenance/source acquisition failure must survive all the way to the consumer so one-sided evidence cannot masquerade as a one-sided API.**

---

## 11. Another fresh timeout justified a narrow retry policy

A following attempt encountered another real pre-response PyPI timeout, this time on another relevant source request.

At this point the project had several independent observations of the same transport class:

- first fresh FastAPI release timeout;
- proposed HTTPX provenance/source timeout;
- Starlette release timeout.

A later diagnostic had also shown the first endpoint could succeed.

Now there was enough evidence to justify a narrow retry mechanism.

Before this point, automatically adding retries would have been speculative complexity.

### Selected retry contract

The successor-only recovery profile allowed:

```text
at most 1 retry for one logical request
at most 2 retry decisions for the entire acquisition
```

Only for:

```text
PyPI HTTPS GET
requests.exceptions.Timeout
before response status/body exists
```

Never retry:

- HTTP status responses, including 401/403/404/429;
- malformed/invalid body or JSON;
- integrity failures;
- policy refusal or deadline;
- credential/auth failure;
- GitHub requests;
- new hosts/non-GET operations.

Every physical attempt still consumes the existing request/body/time budgets.

No counter is reset because a retry was selected.

### Retain the failure history

If the first physical attempt times out and the second succeeds, the saved evidence must retain:

```text
logical request
  ├─ physical attempt 1: timeout
  ├─ retry decision
  └─ physical attempt 2: success
```

The eventual success must not erase the transient failure.

### Why this policy is strong

It is narrow in three dimensions:

1. **provider:** PyPI only;
2. **operation/failure:** GET pre-response timeout only;
3. **count:** one retry per logical request, globally bounded.

That minimizes hidden observation drift while addressing the exact demonstrated failure class.

### Transferable lesson

**Retries should be evidence-driven recovery policy, not a generic instinct. Define exactly which failure semantics are safe to retry and preserve every physical attempt.**

---

## 12. Fresh successor finally acquired both native sides—and still failed

With acquisition, scheduling, source-boundary and timeout-recovery improvements in place, the next attempt reached an important milestone:

> both native old/proposed HTTPX source sides were acquired.

Yet the attempt still failed.

This is one of the most instructive moments in the whole experiment.

### The tempting first explanation

The result looked like a capacity failure, so a natural guess was:

> the acquisition/input is simply too large.

That diagnosis was plausible but incomplete.

The correct next action was not to raise limits. It was to measure the actual representation at each boundary.

---

## 13. Measure the failure dimension before redesigning

Two explicit diagnostics were preserved after the failed attempt.

### D004 — input structural measurement

The ordinary input/receipt side measured approximately:

```text
106,437 JSON structural tokens
```

under an unchanged guard of:

```text
262,144 structural tokens
```

So the input representation fit.

### D005 — computed output measurement

The computed ordinary result measured approximately:

```text
266,809 JSON structural tokens
```

which exceeded the same:

```text
262,144 structural-token guard
```

The exact failure owner was therefore not “input too large.”

It was the **derived result representation**.

### Important terminology

These are internal JSON-structure accounting units used by UpgradePilot's bounded representation guard.

They are **not LLM context tokens**.

Calling them “model tokens” would teach the wrong architecture.

### Why the distinction matters

Different limits imply different repairs:

```text
provider requests too high
→ acquisition policy

source bytes too high
→ source admission/retention

facts too high
→ analysis work admission

result structural representation too high
→ representation/projection

memory/time too high
→ execution/resource design
```

If you diagnose the wrong dimension, you usually repair the wrong owner.

### Transferable lesson

**Never turn “capacity failure” into a design decision until you know which resource dimension crossed which guard.**

---

## 14. Why the project did not simply raise the structural guard

Once D005 showed a 266,809 result against a 262,144 guard, the simplest mechanical fix would have been:

```text
262,144 → something larger
```

That was rejected.

Why?

Because the experiment had evidence that the result contained broad acquisition binding representations **and** independently derived call/signature analysis. Some of that broad material was not consumed by the ordinary comparison reader.

Before expanding a shared guard, the project asked:

> Is the oversized representation actually necessary for this consumer's responsibility?

That is a better architectural question.

### Exact interning was measured, not assumed

One hypothesis was that many acquisition fact packets were literal duplicates and could simply be interned.

The diagnostic found:

```text
13 acquisition fact packets
12 unique
```

Exact packet interning saved only about:

```text
84 bytes
```

That was nowhere near enough.

The project did not keep an ineffective optimization just because it sounded elegant.

### Transferable lesson

**Test representation hypotheses quantitatively. “Looks duplicated” is not evidence that deduplication will solve the actual capacity problem.**

---

## 15. The actual representation repair: purpose-specific receipt summary

The selected design did not weaken source evidence or the local checker.

It changed the **ordinary acquisition receipt projection** at the composition boundary.

The broad generic acquisition manifests retained fields such as:

```text
binding_analysis_version
binding_trace_steps
imports
references
```

Those fields were useful to generic acquisition/replay responsibilities, but the ordinary call/signature comparison did not consume those broad root tables from the inner receipt. Its actual comparison facts were independently recomputed from the complete admitted source text.

### Selected summary

At `prepare_ordinary_inputs`, the ordinary integration owner created a versioned summary and omitted exactly those broad root fields from selected receipt packets while retaining:

- target/dependency identities;
- declarations;
- module requests;
- request origin and its binding context;
- source identities/hashes;
- provenance;
- metadata;
- omissions;
- gaps;
- costs;
- native transition;
- complete admitted source companion;
- independently computed call/signature/comparison facts.

### What was not changed

The repair did **not** change:

- generic acquisition manifests;
- source text capture;
- binder semantics;
- correspondence semantics;
- call/signature checker;
- provider/request caps;
- analysis caps;
- native Workspace parser/guard;
- old frozen attempts.

### Why this is not “throw data away until it fits”

The question is ownership.

The ordinary comparison consumer did not need a second broad parallel binding table in its inner receipt when:

- source text remained retained;
- request-origin binding evidence needed by the ordinary path remained;
- comparison facts were independently derived from source;
- the fresh outer acquisition capture still preserved its original broad observations.

The projection removes unconsumed representation from one consumer boundary. It does not erase the original acquisition evidence from its owner.

### Transferable lesson

**Representation should carry the evidence a consumer actually owns and needs, while preserving richer upstream evidence at its authoritative owner.**

---

## 16. D006: repair proof is not a fresh attempt

After the receipt-summary design, the project ran a separate retained-component analysis using the already retained S007 source.

This was `D006`.

Its purpose was:

> Does the repaired representation successfully preserve the same source/fact/path/premise/comparison responsibility under the unchanged structural guard?

D006 successfully saved and cold-opened the repaired result.

That was strong evidence for the representation repair.

But D006 was **not**:

- a new fresh provider acquisition;
- a re-execution of S007 under the original S007 method;
- permission to relabel S007 successful;
- proof that fresh acquisition plus the new representation would succeed.

The correct relationship is:

```text
S007
  fresh attempt
  failed at encoding
  immutable

D004/D005
  diagnostics
  locate capacity dimension

D006
  retained-component successor-method proof
  qualifies representation repair

S008
  new fresh attempt
  tests the repaired method end to end
```

### Transferable lesson

**A retained replay can qualify a repair cheaply and safely, but only a new fresh attempt can establish the fresh end-to-end property.**

---

## 17. Final fresh successor: useful paired evidence

The fresh S008 attempt used the repaired/frozen successor method and completed acquisition, bounded analysis, serialization and fixed admission.

Its recorded disposition was:

```text
useful_partial_structural_evidence
```

### Exact case/cost summary

The retained review records:

```text
repository: Aidan-Wallace/kubernetes-dashboard-token-api
PR: #20
HTTPX: 0.27.2 → 0.28.1

outer elapsed: 44.837153s
acquisition:    43.056772s

GitHub requests: 50
all physical provider requests: 75
failed requests: 0
retry decisions: 0

decoded provider bytes: 2,601,631
retained files: 24
retained source bytes: 202,442
AST nodes: 24,153
call/signature facts: 1,107
comparison records: 12
```

The selected 50-request GitHub ceiling was reached, but no higher allowance was used merely to improve the result.

---

## 18. What the final source path actually found

One target root at:

```text
tests/test_routes.py:7
```

was connected through:

```text
target TestClient(...) call
        ↓
FastAPI testclient re-export
        ↓
constraint-selected Starlette TestClient source
        ↓
Starlette initializer
        ↓
conditional superclass source path
        ↓
HTTPX Client.__init__ old/proposed definitions
```

The fresh sampled Starlette forwarding call supplied:

```text
base_url
headers
transport
follow_redirects
cookies
```

It did **not** supply:

```text
app
```

All four native old/proposed comparison records were locally:

```text
bound
```

### Why there are four records

There were two retained export witnesses per HTTPX version for:

```text
one target root
one forwarded call
```

Therefore:

```text
4 comparison records
≠
4 independent target calls
≠
4 independent real-world cases
```

They are multiple source witnesses/alternatives around the same structural relationship.

This distinction prevents evidence-count inflation.

---

## 19. The fresh result did not reproduce the historical `app` mismatch—and that is a success

This is the conceptual climax of the blocker-resolution campaign.

The curated historical source example had shown:

```text
older captured Starlette forwarding app=
→ proposed HTTPX does not receive app
→ local rejection
```

The fresh ordinary S008 evidence instead found a sampled Starlette source where the inspected forwarding call did not include `app`.

Therefore the fresh local old/proposed comparisons bound.

A badly designed experiment would interpret this as failure and start tuning until a rejection appears.

The actual acceptance criterion did not require a rejection.

It required useful paired evidence.

So the correct interpretation was:

> The ordinary pipeline reached the relevant old/proposed source family and produced informative conditional local comparisons. The specific historical `app` mismatch is not present in the sampled fresh source path that was actually acquired.

That is scientifically stronger than reproducing the expected story by selection pressure.

### Transferable lesson

**A good diagnostic method is allowed to contradict the example that motivated it. If the method can only “succeed” when it confirms the prior story, it is not a trustworthy diagnostic method.**

---

## 20. Why the final result is still partial

S008 did not become “complete source truth.”

The retained review records:

```text
8 adapter candidates unexamined
12-module source budget exhausted for further questions
147 retained gap records
68 discovery states examined
0 diagnostic records omitted
```

Examples of remaining uncertainty include:

- another HTTPX2 alternative;
- unresolved conditional imports;
- unexamined Starlette/HTTPX modules;
- effective exports;
- branch activation;
- allocation/MRO;
- installed namespaces;
- runtime dispatch.

FastAPI 0.162.0 and Starlette 1.10.0 were **constraint-selected samples**, not observed installed/resolved target versions.

The result is therefore useful but conditional.

### What partiality means here

```text
useful local pair exists
AND
coverage still has explicit omissions/gaps
```

not:

```text
result is unreliable because anything is unknown
```

and not:

```text
one useful pair proves full compatibility
```

---

## 21. Representation repair verification in S008

The fresh result also confirmed the receipt-summary repair under the original structural guard.

The retained review compares three proof layers:

| Evidence | Outcome | Representation |
| --- | --- | --- |
| S007 fresh | failed encoding | diagnostic output 266,809 structural tokens > 262,144 |
| D006 retained | saved/cold-opened retained-component proof | repaired summary representation |
| S008 fresh | completed useful partial result | 2,005,355 bytes / 170,413 structural tokens |

This is exactly the proof sequence we want:

```text
historical failure
→ measured cause
→ retained repair qualification
→ fresh successor confirmation
```

No native structural guard increase was required.

---

## 22. Fixed opening proves historical inspectability, not current recomputation

S008's final opening controls forbid:

- AST parsing;
- HTTP access;
- checker execution;
- source discovery;
- credential reads;
- current executable-identity recomputation.

The saved attempt still opens and reproduces the retained view/source.

That means the historical result is inspectable as historical evidence.

It does not mean today's method reran and reconfirmed every semantic step.

The same no-regrade discipline applies to S002–S007.

---

## 23. The attempt sequence as a failure atlas

The easiest way to remember the campaign is not by attempt number but by the **new failure class each fresh successor exposed**.

| Fresh stage | Observed blocker | Correct owner | Repair / disposition |
| --- | --- | --- | --- |
| first live | FastAPI pre-response timeout | transport/provider observation | preserve failure; later endpoint diagnostic; no regrade |
| frontier successor | useful Starlette continuation omitted | candidate work allocation | target-rooted observed-symbol frontier |
| native-closure successor | module budget spent on sampled internals | source work allocation | native old/proposed paired closure before optional internals |
| next successor | weak queued priority stays stale after stronger evidence | scheduler | monotonic pending-priority promotion |
| same stage | missing wildcard module recursively reinterpreted through parent | correspondence/module boundary | stop at exact missing required module; retain gap |
| next fresh | one native side unavailable after pre-response timeout | transport | preserve asymmetric provenance failure; no semantic absence |
| next fresh | repeated relevant PyPI pre-response timeout | transport policy | narrowly qualified PyPI timeout retry profile |
| next fresh | both native sources acquired but final result exceeds structural guard | representation | measure D004/D005; do not raise guard |
| retained qualification | repair must fit unchanged representation guard | ordinary receipt projection | D006 purpose-specific summary, no regrade |
| final fresh | paired result completed; both native sides bind | no defect | accept useful partial evidence; do not force expected rejection |

This table is the heart of the artifact.

---

## 24. Immutable attempts and successor methods

An experimental campaign becomes unreliable if each failed attempt is silently edited until it passes.

UpgradePilot instead treated attempts as immutable evidence objects.

Conceptually:

```text
attempt A under method/config A
→ terminal result
→ frozen

new evidence exposes generic defect
→ repair + tests
→ method/config B
→ new attempt B
```

The predecessor remains evidence for why the successor exists.

### Why this matters

Suppose S007 had been overwritten after the receipt-summary repair.

We would lose the ability to prove:

- that the original fresh attempt actually failed;
- that the failure occurred before the repair;
- which diagnostic motivated the repair;
- that D006 was a successor-method replay rather than the original result;
- that S008 was a genuinely fresh post-repair run.

Historical failures are engineering assets when preserved correctly.

---

## 25. Diagnostics, controls and fresh attempts have different proof roles

This campaign used several kinds of evidence. They must not be merged.

### Fresh real attempt

Answers:

> What happened end to end against providers under this frozen method/contract?

Examples: first live attempt, S002–S008.

### Targeted diagnostic

Answers:

> What specific condition or resource dimension explains a historical result?

Examples: D001, D004, D005.

A diagnostic can locate a cause without changing the predecessor attempt.

### Controlled regression

Answers:

> Does the generic repair discriminate the intended behavior from the old defect under a controlled renamed case?

Examples:

- observed-symbol frontier control;
- competing adapter/native closure control;
- missing wildcard module control;
- timeout→success / timeout→timeout controls.

### Retained-component successor proof

Answers:

> Does the successor method work on preserved material without paying for another provider acquisition?

Example: D006.

### Fresh successor proof

Answers:

> Does the qualified successor survive a new end-to-end provider run?

Example: S008.

### Transferable lesson

**Different proof classes are complementary. None should be relabelled into another just because they support the same design decision.**

---

## 26. “No repair” is sometimes the correct engineering decision

Several fresh outcomes did not justify code changes.

Examples:

### Provider timeout before enough recurrence

The first timeout alone did not justify a retry framework.

The attempt remained failed; the endpoint was diagnosed separately.

### Legitimate conditional binding

The Starlette fallback import made the base uncertain. The lower-level binder was correct. The repair belonged in correspondence as a conditional hypothesis, not in binding.

### S008 both sides bind

This was not a defect simply because the historical curated case had a rejection.

No “make it reject” repair was warranted.

### Transferable lesson

A mature debugging process asks:

```text
is this behavior actually wrong for the owner's contract?
```

before asking:

```text
how do we change the code?
```

---

## 27. The earliest-sufficient-owner diagnosis model

This experiment repeatedly succeeded because repairs were placed at the earliest owner that had enough evidence to solve the actual problem.

Use this model:

| Symptom | Earliest likely owner | Wrong shortcut |
| --- | --- | --- |
| required evidence never acquired | provider/source acquisition | patch binder/checker |
| candidate exists but useful continuation starved | work allocation/prioritization | raise every cap |
| exact module missing during traversal | correspondence/module-boundary owner | reinterpret through parent package |
| conditional source relationship remains unresolved | correspondence hypothesis with premises | make binder falsely established |
| pre-response provider timeout | transport/retry policy | call source absent |
| one-sided source because one request failed | provenance/acquisition | infer version/API asymmetry |
| source facts correct but saved result exceeds structure guard | representation/projection | raise integrity guard or delete semantic facts |
| local structural pair is bound/rejected but runtime proposition is requested | runtime/environment evidence owner | strengthen static claim |
| fresh outcome differs from expected historical story | possibly no defect | tune until expected answer appears |

This matrix generalizes beyond caller/signature analysis.

---

## 28. A practical diagnostic decision tree

When a future experiment produces “insufficient evidence,” ask in this order:

```text
1. Was the necessary external observation attempted?
   ├─ no → acquisition policy / budget / selection
   └─ yes
       ↓
2. Did the provider return usable data?
   ├─ no → transport/status/body/auth/provenance class
   └─ yes
       ↓
3. Was exact source retained/admitted?
   ├─ no → retention/source admission
   └─ yes
       ↓
4. Did source analysis extract the necessary fact?
   ├─ no → extraction/binding limit or unsupported syntax
   └─ yes
       ↓
5. Did correspondence build a justified source path?
   ├─ no → path/candidate/gap/relationship owner
   └─ yes
       ↓
6. Did local comparison produce useful evidence?
   ├─ no → checker/premise/coverage
   └─ yes
       ↓
7. Could the result be retained/serialized?
   ├─ no → representation/work-admission owner
   └─ yes
       ↓
8. Is the requested claim stronger than static evidence?
   ├─ yes → separate runtime/environment/semantic owner
   └─ no → admitted structural evidence
```

Do not skip directly from “bad final result” to whichever module is easiest to edit.

---

## 29. Why renamed controls matter

Several repairs were explicitly required to pass renamed/synthetic controls.

This is not because synthetic cases are inherently more trustworthy than real cases.

It is because they can test whether the repair encodes a **general rule** rather than the known case identity.

For example, a source-frontier repair should succeed when:

```text
FastAPI → Starlette → HTTPX
```

is renamed to:

```text
bridge → mediator → vendor
```

with the same structural relationship.

If the repair fails after renaming, it may be case hardcoding rather than a reusable method.

The real case supplies pressure. The renamed control checks generality of the local rule.

---

## 30. Why not all green tests mean the experiment is globally green

At the final S008 horizon, focused qualification reported:

```text
254 focused API tests pass
7 architecture tests pass
```

But the full experiment suite still retained historical debt:

```text
1 failure
25 errors
11 skips
```

The final review explicitly says the full suite is **not green**.

This matters for engineering communication.

Correct statement:

> The focused caller/signature/blocker-resolution qualification passed its selected controls; unrelated/historical full-suite debt remained unchanged.

Incorrect statement:

> All tests pass, therefore the experiment is production-ready.

---

## 31. What S008 proves—and what it does not

### Established by the fresh experiment

Within the selected case and frozen experimental method:

- the ordinary PR/dependency transition was acquired;
- target, sampled framework and exact old/proposed HTTPX source material were retained under bounded work;
- a target-rooted mediated source path was discovered;
- paired native old/proposed source comparisons were produced;
- the local comparisons were informative;
- gaps/omissions remained visible;
- the result fit the unchanged structural guard after the qualified representation repair;
- the saved attempt could be cold-opened without reanalysis/provider work.

### Not established

S008 does not prove:

- actual installed FastAPI/Starlette versions;
- actual runtime import fallback branch;
- MRO/dispatch;
- target test execution;
- behavioral compatibility;
- whole-repository/API coverage;
- broad statistical generality;
- maintainer usefulness;
- native product integration;
- action permission.

### Why this boundary is useful

The experiment ended with a **specific, inspectable, conditional claim** rather than a vague compatibility verdict.

That is the correct foundation for later productization.

---

## 32. Source/evidence walkthrough: shortest useful route

This artifact is more about evidence chronology than one source file. Use these anchors in this order.

### Step 1 — staged source policy

Read:

`working-memory/2026-10-30_staged-source-acquisition-policy_build-cycle.md`

Question:

> Which work budgets are experiment-local versus provider/account limits, and why does ordering affect evidence completeness?

### Step 2 — first fresh attempt

Read:

`working-memory/2026-10-31_first-fresh-ordinary-pr-live-attempt_cycle.md`

Then:

`working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/D001.json`

Question:

> Why does later endpoint availability not alter the original attempt?

### Step 3 — frontier and native closure

Read:

- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/FRONTIER_DESIGN.md`;
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/NATIVE_CLOSURE_AND_BASE_DESIGN.md`.

Question:

> Which failures are solved by better work selection rather than larger budgets?

### Step 4 — timeout recovery

Read:

`working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/PYPI_TIMEOUT_RECOVERY_DESIGN.md`

Question:

> Exactly which timeout is retryable, and which request/failure classes remain terminal?

### Step 5 — representation failure

Read:

- `D004-json-measurement.json`;
- `D005-result-measurement.json`;
- `ORDINARY_RECEIPT_SUMMARY_DESIGN.md`;
- `D006-receipt-summary.json`.

Question:

> Why was the correct repair a consumer-specific representation projection rather than a larger structural guard?

### Step 6 — final fresh result

Read:

`working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/S008/REVIEW.md`

Question:

> Why is a bound/bound fresh comparison still a successful result even though the historical motivating case contained a rejection?

---

## 33. What you should be able to explain after this note

### Must own

You should be able to explain:

- why every fresh attempt remains immutable;
- why a later diagnostic cannot regrade a predecessor;
- provider failure versus method failure;
- experiment-local budgets versus provider quota;
- source starvation as an allocation problem;
- target-rooted observed-symbol frontier;
- native old/proposed paired closure;
- monotonic promotion of pending priority;
- exact missing-module boundary;
- why lower-layer legitimate uncertainty should not be “fixed” away;
- why asymmetric acquisition failure is not API asymmetry;
- when retry behavior is justified and how to constrain it;
- why every physical retry remains charged/retained;
- how to diagnose a capacity failure by dimension;
- why D004/D005 disproved the initial input-size explanation;
- why exact interning was measured and rejected as insufficient;
- why purpose-specific receipt projection is not arbitrary evidence deletion;
- why D006 is repair qualification rather than fresh proof;
- why S008 does not need to reproduce the historical `app` mismatch;
- why four comparison records are not four cases;
- why useful partial evidence can coexist with many explicit gaps;
- how to locate the earliest sufficient repair owner.

### Understand operationally

You should be able to read:

- transport event histories;
- retry decision records;
- request/body/time budgets;
- source module work receipts;
- state/gap counters;
- structural representation measurements;
- frozen attempt/method identities;
- retained-component versus fresh-result labels.

### Lookup-level

You do not need to memorize:

- every attempt UUID;
- every SHA;
- every request URL;
- every regression fixture name;
- exact byte counts that do not explain a design choice;
- every individual gap code.

### Deliberately deferred

Do not solve here:

- LifeLog-scale source-first retention;
- whole-file partial-analysis admission;
- general dynamic Python semantics;
- untouched transfer methodology;
- native productization;
- maintainer usefulness.

---

## 34. Fast relearning route

### Five-minute mental refresh

Remember the failure chain:

```text
timeout
→ frontier starvation
→ native-source starvation
→ stale priority + bad missing-module traversal
→ one-sided timeout
→ narrowly justified retry
→ both native sides but representation overflow
→ measure
→ receipt-summary repair
→ fresh useful paired evidence
```

Then remember:

```text
repair the earliest sufficient owner
never regrade the predecessor
never force the expected answer
```

### Fifteen-minute refresh

Read:

1. `FRONTIER_DESIGN.md`;
2. `NATIVE_CLOSURE_AND_BASE_DESIGN.md`;
3. `PYPI_TIMEOUT_RECOVERY_DESIGN.md`;
4. `ORDINARY_RECEIPT_SUMMARY_DESIGN.md`.

### Thirty-minute real-case refresh

Compare:

1. one failed pre-response timeout attempt;
2. S007 structural failure;
3. D004/D005 measurements;
4. D006 repair qualification;
5. S008 final review.

If you can explain why none of those artifacts replaces another, you have recovered the campaign's proof discipline.

---

## 35. Transfer questions

### 1. Later endpoint recovery

A frozen fresh attempt times out on `GET /package/1.2/json`. Ten minutes later a diagnostic gets HTTP 200 from the same endpoint.

What does the later diagnostic establish? What must remain unchanged?

### 2. Missing useful source under a module cap

A run spends 12 module questions on sampled framework internals and never reaches the changed dependency's proposed defining module.

Would you first raise the module cap? What should you inspect instead?

### 3. Retry semantics

A PyPI GET receives HTTP 429. The experiment's retry profile permits one retry for a pre-response timeout.

Should 429 be retried under that profile? Why is this distinction important?

### 4. Capacity diagnosis

The saved input measures 110k structural units under a 262k limit. The computed result measures 270k.

Which owner should be investigated first? Why would raising provider/source budgets be irrelevant?

### 5. Unexpected fresh outcome

A motivating curated example had old=bound, new=rejected. A fresh ordinary case under a frozen method finds old=bound, new=bound with a different sampled wrapper source.

Should the experiment be considered failed because no rejection appeared? What determines success instead?

---

## 36. Answers/checkpoints for self-review

1. The later diagnostic establishes that the endpoint was available at the later observation time and supports a transient-failure hypothesis. The original attempt's timeout, contract, state and evidence remain unchanged.
2. Inspect work allocation first: which questions consumed the 12 slots and whether decision-critical old/proposed closure was starved. Prefer a generic prioritization repair if the budget is being spent poorly; do not increase it automatically.
3. No. A received HTTP 429 is a status response, not a pre-response timeout. Retrying it would broaden the policy into a different failure class and could hide rate/policy semantics.
4. The representation/projection owner. Input fits; derived output does not. Provider/source budgets are upstream and do not explain the failing structural boundary.
5. No. Success is defined by the frozen acceptance criterion: useful paired structural evidence under preserved provenance/premises, not confirmation of a preselected rejection. The fresh wrapper may legitimately not contain the historical mismatch.

---

## 37. Final engineering model

The blocker-resolution campaign demonstrates a reusable way to mature an evidence pipeline:

```text
real fresh pressure
→ preserve exact failure
→ identify failure class
→ measure the responsible boundary
→ choose smallest generic repair
→ prove repair on discriminating controls
→ freeze successor
→ run fresh again
→ accept whatever honest evidence appears
```

The final success was not “HTTPX finally failed the way we expected.”

The final success was:

> A demanding real PR could progress through ordinary acquisition, target-rooted source discovery, exact old/proposed source comparison, bounded representation and cold saved inspection, producing useful paired structural evidence without case-specific selectors, hidden retries, cap inflation, historical regrading or a forced semantic outcome.

That is the engineering result worth retaining.

The next major pressure came from a different kind of case: a much larger direct-use repository where complete source retention succeeded but broad derived representation/analysis no longer fit the existing work model. That later source-retention/capacity redesign is Artifact 04.

---

## Pinned evidence anchors

Primary historical records:

- `working-memory/2026-10-30_staged-source-acquisition-policy_build-cycle.md`
- `working-memory/2026-10-31_first-fresh-ordinary-pr-live-attempt_cycle.md`
- blocker-resolution working-memory record at the pinned horizon

Blocker-resolution design/diagnostic evidence:

- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/D001.json`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/FRONTIER_DESIGN.md`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/NATIVE_CLOSURE_AND_BASE_DESIGN.md`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/PYPI_TIMEOUT_RECOVERY_DESIGN.md`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/D004-json-measurement.json`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/D005-result-measurement.json`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/ORDINARY_RECEIPT_SUMMARY_DESIGN.md`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/D006-receipt-summary.json`
- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/S008/REVIEW.md`

Immutable live-attempt directories:

- `working-memory/evidence/2026-10-31-ordinary-source-blocker-resolution/S002/`
- `.../S003/`
- `.../S004/`
- `.../S005/`
- `.../S006/`
- `.../S007/`
- `.../S008/`

Implementation/tests remain pinned to:

`c53430c6e3fb4f24147a28aa642ab94834233243`

Do not substitute current productization source and still call this the frozen experiment-learning artifact.

`UP-SKILL:upgradepilot-learning-artifact`
