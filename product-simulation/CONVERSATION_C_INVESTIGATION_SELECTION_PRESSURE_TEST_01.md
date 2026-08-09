# Conversation-C Investigation-Selection Pressure Test 01

**Date:** 2026-08-09  
**Status:** Completed bounded cross-case pressure test; non-controlling simulation/design evidence  
**Wider design context reviewed:** `main` Conversation-C exploration through `86ad8962bd7f75d8d9c84930d8cc6c96d6ba427c`  
**Primary cases:** S006, S007, Kedro/Pluggy, Buildtest/OpenSSL, pip-audit/CacheControl/urllib3  
**Secondary confirmation:** AWS SDK for pandas / urllib3, CARLA ScenarioRunner / OpenCV

## 1. Purpose

This pass asks whether the current Conversation-C investigation-selection direction survives materially different real/simulation evidence without becoming:

- `uncertain → collect more evidence`;
- `dynamic test = strongest evidence`;
- `cheapest check = best check`;
- one fixed source/test/CI checklist;
- an LLM-owned planner/verdict;
- an endless attempt to eliminate every uncertainty.

The pass does **not** define product runtime schemas, planner classes, numerical Value-of-Information scores, or final stopping/maintainer semantics.

## 2. Current main-branch direction being tested

The reviewed Conversation-C exploration already proposes a strong general shape:

```text
material unresolved proposition
→ identify observations that could change its justified state
→ generate candidate investigations/checks
→ compare discrimination, scope, authority, coverage, feasibility,
  cost, latency, invasiveness, risk, reproducibility, pruning,
  and complementarity
→ choose useful investigation / sequence
OR justify no further supported check
→ return observations to Conversation-B proposition evaluation
→ repeat only while material uncertainty and useful investigation remain
```

It also explicitly preserves:

```text
relevant evidence != discriminating evidence
dynamic != universally stronger
static != universally weaker
information gain != decision-relevant information gain
```

This pressure test largely **supports** that direction.

The main new contribution is to sharpen how investigation selection changes over time as evidence arrives and to distinguish different reasons for stopping.

---

## 3. Pressure case A — S006: execution is genuinely worth selecting

### Unresolved question

```text
Does ConfigLambda(handler=<non-string>) expose different exception behavior
under Pydantic 1.10.x versus 2.x because validator TypeError semantics changed?
```

### Evidence before selection

- authoritative upstream behavior change established;
- exact target branch established;
- affected dependency major is permitted by the proposal;
- visible nearby tests do not execute the exact TypeError branch;
- exact historical resolved version/execution evidence unavailable.

### Candidate investigations

```text
import-only check                         → does not execute affected branch
valid-handler check                       → does not execute affected branch
install-only resolution                   → answers version selection, not behavior
full suite under unconstrained install    → broad, drift-prone, weak attribution
bounded old/new differential reproduction → exact branch + exact input + exact semantic boundary
```

### Result

```text
SELECT CHECK
→ bounded old/new differential reproduction
```

### C lesson

A dynamic/interventional investigation is justified when the unresolved proposition is behavioral, static evidence cannot settle the changed-property-to-target-behavior relation, and the proposed execution activates exactly the implicated branch with interpretable outcomes.

S006 therefore rejects:

```text
dynamic testing is always overkill
```

as strongly as it rejects:

```text
run the whole suite whenever uncertain
```

---

## 4. Pressure case B — S007: a plausible execution becomes unnecessary

### Initial unresolved question

```text
Can BiomedParse PR #96's exact declared Torch/TorchVision/TorchAudio package set
form a coherent package family for the documented Python-3.10.14 / CUDA-12.4 context?
```

At admission, reasonable candidate observations included:

1. exact target-relevant TorchVision wheel metadata;
2. isolated resolver dry-run.

### New evidence acquired before execution

Further authoritative source inspection established:

```text
TorchVision v0.21.0 setup logic
PYTORCH_VERSION present
→ exact torch==PYTORCH_VERSION dependency

official release/2.6 Linux binary workflow
→ install Torch 2.6 release dependency
→ export that Torch release version into PYTORCH_VERSION
→ build TorchVision 0.21 wheel
→ verify produced wheel contains pinned Requires-Dist: torch (==...)
```

Target PR head independently declares:

```text
torch==2.8.0
torchvision==0.21.0+cu124
```

Therefore:

```text
TorchVersion allowed by direct requirement = {2.8.0}
TorchVersion allowed by retained TorchVision 0.21 release contract = Torch 2.6 family exact pin
intersection = ∅
```

### Result

```text
owned package-family proposition resolved/refuted
→ resolver dry-run becomes corroborative
→ TorchAudio metadata becomes redundant
→ runtime/GPU/API investigation remains downstream and inactive
→ NO FURTHER CHECK FOR OWNED QUESTION
```

### C lesson

Investigation selection is **stateful and revisable**.

```text
check worth considering at T1
+
new authoritative evidence at T2 resolves the proposition
→ cancel/prune check at T2
```

A planner must not treat a previously generated investigation as an obligation to execute.

This is stronger than ordinary conditional activation: candidate investigations themselves can lose value as evidence changes.

---

## 5. Pressure case C — Buildtest/OpenSSL: unresolved can remain unresolved

### Material proposition

```text
Did the exact relevant historical Buildtest environment use an SSL/OpenSSL state
that activates urllib3's changed native-environment requirement?
```

Established:

- upstream environment constraint exists;
- target has relevant historical HPC/Perlmutter environment evidence;
- exact historical SSL implementation/version was not recovered.

Potentially tempting work:

- inspect today's Perlmutter environment;
- search target source more deeply;
- inspect generic Python/OpenSSL documentation;
- reconstruct an approximate modern environment.

None automatically answers the exact historical proposition.

### Result shape

If no authentic historical module manifest, environment capture, log, or defensible frozen reconstruction exists:

```text
proposition remains unresolved
+
no supported sufficiently scoped investigation remains worth doing
→ STOP WITH UNRESOLVED
```

### C lesson

This stop result is materially different from S007.

```text
S007:
STOP because proposition was resolved before further execution.

Buildtest:
STOP because proposition remains unresolved and no sufficiently authoritative,
discriminating, proportionate investigation is available.
```

Both may surface as `no further investigation`, but they have different proposition state, rationale, and downstream meaning.

**Do not collapse them.**

---

## 6. Pressure case D — Kedro/Pluggy: investigate the proposition, not nearby facts

### Semantic-heavy proposition

```text
Does exact participating implementation I rely on the specific
Pluggy wrapper/result/exception property changed by the transition?
```

Several facts can be relevant without being discriminating for that exact proposition:

```text
Kedro depends on Pluggy
plugin installed
entry point registered
hook reachable
wrapper=True found
```

These may establish prerequisite propositions such as presence/participation.

But:

```text
participates in wrapper mechanism
!=
relies on the specific changed result/exception property
```

A presence/registration inventory cannot be credited as resolving semantic reliance merely because it is easier to obtain.

### Candidate sequence

A defensible sequence may be:

```text
1. establish exact implementation + participation if still unresolved
   ↓
2. inspect exact implementation/tests/docs against exact upstream changed semantic
   ↓
3. bounded semantic interpretation with explicit grounding
   ↓
4. only if ambiguity remains and execution is supported/valuable:
   targeted old/new differential execution or trace
```

### C lesson

One investigation normally targets one proposition or a clearly stated set of propositions.

If a check only resolves an upstream prerequisite, its value can still be high through **pruning**, but it must not be relabeled as answering the deeper semantic proposition.

---

## 7. Pressure case E — pip-audit/CacheControl/urllib3: investigation depth is decision-relative

Real path:

```text
pip-audit
→ CacheControl
→ Requests / urllib3 machinery
→ CacheControl assumption on urllib3.HTTPResponse.strict
```

Once exact dependency/resolution evidence and the concrete incompatible contract establish the target-relevant multi-hop path, continuing graph traversal merely because more dependencies exist has diminishing decision value.

A graph investigation is useful while it can answer questions such as:

```text
Does the relevant path exist?
Which exact versions are on it?
Where is the incompatible contract?
Is the target connected to that contract under the evaluated context?
```

After those are settled:

```text
more graph depth
!=
more decision-relevant evidence
```

### C lesson

Multi-hop stopping should be tied to the unresolved proposition and remaining viable alternatives, not a fixed graph depth or exhaustive dependency traversal.

---

## 8. Secondary confirmation — AWS urllib3 Python-support drop

Real PR:

```text
aws/aws-sdk-pandas#3332
urllib3 2.6.3 → 2.7.0
```

One upstream mechanism drops Python 3.9.

Exact target declares:

```text
requires-python >=3.10,<4.0
```

For that mechanism-specific candidate:

```text
exact authoritative target declaration
+ deterministic version-range evaluation
→ Python-3.9 applicability refuted
→ no Python-support investigation needed
```

This independently confirms the S001 pattern in a different repository and release interval.

### C lesson

A known reasoning pattern still benefits from real-world confirmation. Not every useful case needs to add a new domain concept.

---

## 9. Secondary pressure — CARLA/OpenCV direct use still fans out by mechanism

Real PR:

```text
carla-simulator/scenario_runner#1111
opencv-python 4.2.0.32 → 4.8.1.78
```

Exact target base has concrete `cv2` runtime use in its visualizer.

The crossed upstream interval nevertheless contains independent mechanisms involving:

- Python support;
- platform/distribution behavior;
- binding changes;
- GPU-memory bindings;
- security fixes;
- other OpenCV runtime changes.

Therefore:

```text
direct target use of dependency
!=
every crossed upstream mechanism is applicable
```

### C lesson

Even in the easiest exposure topology, investigation generation must remain mechanism-specific rather than becoming `dependency used → test dependency broadly`.

---

## 10. What “sufficiently discriminating” appears to require

Across these cases, a candidate investigation is worth doing only when the following are sufficiently true for the owned question.

### 10.1 State-changing potential

At least one plausible outcome can materially change:

- the proposition state;
- a required candidate path;
- downstream investigation activation;
- or another explicitly owned decision-relevant state.

If every plausible outcome leaves the owned state unchanged, the investigation is not sufficiently discriminating for that purpose.

### 10.2 Admissible evidence path

The observation must be capable of becoming evidence with adequate:

- identity/scope;
- authority/provenance;
- interpretation boundary;
- coverage/completeness where the claimed direction requires it.

Interesting output that cannot support/refute the proposition is not enough.

### 10.3 Outcome semantics declared before execution when practical

Prefer freezing:

```text
O1 → establishes/supports P
O2 → refutes P
O3 → leaves P unresolved
acquisition/execution failure → source/check problem, not automatic proposition refutation
```

before executing the check.

This reduces post-hoc storytelling.

### 10.4 Direction-specific adequacy

The threshold differs by proposition/evidence direction.

```text
existence / positive witness
→ one authoritative witness may be sufficient

absence / non-existence
→ requires adequate completeness for the claimed universe

semantic reliance
→ requires grounded changed-property ↔ target-behavior relation;
  presence alone is weaker

pruning
→ requires enough evidence to close a prerequisite/path such that deeper work
  cannot change the owned result for that path
```

### 10.5 Non-redundancy at the current evidence state

An investigation that was useful earlier may become redundant later.

Selection must therefore be evaluated against **current admitted evidence**, not only against the initial case state.

### 10.6 Proportionality after adequacy

Only after candidate investigations are capable of answering the question should UpgradePilot prefer lower cost/risk/latency/invasiveness.

```text
adequate discrimination first
then proportionality among adequate options
```

This avoids both cheapest-first and strongest-test dogma.

---

## 11. Three materially different stopping results

The current main exploration explicitly recognizes `useful next investigation` versus `no additional supported investigation justified` while preserving unresolved state.

Cross-case evidence suggests preserving at least these **semantic reasons**, without implying runtime enums:

### Stop A — proposition resolved; no further check needed

Canonical current example: **S007**.

```text
new admitted evidence resolves/refutes proposition
→ planned execution becomes redundant
→ stop
```

### Stop B — proposition unresolved; no worthwhile supported check remains

Canonical current example: **Buildtest/OpenSSL** if authentic historical evidence cannot be recovered/reconstructed sufficiently.

```text
material proposition unresolved
+
available candidate checks fail scope/authority/discrimination/proportionality
→ preserve unresolved
→ stop
```

### Stop C — proposition/path closed early; deeper branch pruned

Examples:

- S001/AWS Python-support concern outside target range;
- Kedro if complete exact environment inventory refutes affected plugin participation.

```text
necessary prerequisite/path refuted
→ downstream semantic investigation cannot change candidate result for that path
→ prune
```

These reasons may share an operational outcome such as `no next check`, but they should remain explainably distinct because they carry different knowledge states and downstream consequences.

---

## 12. Revised pressure-tested reasoning shape

The current Conversation-C direction survives, with one refinement emphasized by S007:

```text
MATERIAL QUESTION / UNRESOLVED PROPOSITION
        ↓
re-evaluate whether already-admitted/newly-acquired evidence can settle it
        ├── yes → return to B evaluation
        │          ↓
        │        resolved/path closed?
        │          ├── yes → stop/prune further checks
        │          └── no  → continue
        └── no
             ↓
identify observations that could change its state
             ↓
generate candidate investigations
             ↓
reject candidates that are:
    non-discriminating
    wrong-scope
    non-authoritative for the claim
    insufficiently complete for negative inference
    unsupported/unsafe
    redundant at current evidence state
             ↓
map plausible outcomes to proposition/downstream state changes
             ↓
consider sequencing, complementarity, and pruning
             ↓
among sufficiently adequate candidates,
prefer proportionate lower-cost/lower-risk path
             ↓
SELECT CHECK / SEQUENCE
OR
STOP WITH UNRESOLVED because no justified useful check remains
             ↓
new observation returns to Conversation-B evaluation
             ↓
recompute whether any previously planned investigation still has value
```

This is a reasoning model only, not a runtime pipeline/schema.

---

## 13. Findings relative to main Conversation C

### Strongly confirmed

- relevant evidence is not automatically discriminating;
- investigation outcomes should be considered before execution;
- static evidence can dominate dynamic checks for some propositions;
- dynamic/differential execution is highly valuable for other propositions;
- sequencing and pruning matter;
- complementarity can matter but should be earned;
- cost/risk should not override basic adequacy;
- LLM-generated investigation ideas need independent scope/safety/authority validation;
- no-further-check is a legitimate result;
- graph depth should be decision-relative.

### Bounded refinement from S007

Main should make explicit enough that:

> **Investigation selection is continuously conditional on the current evidence state. A check that was sufficiently useful when generated may become unnecessary before execution if newly admitted evidence resolves the targeted proposition or closes its path.**

And:

> **`No further check` should preserve why: resolved, path-pruned, or still-unresolved-with-no-justified-investigation are materially different explanations even if they eventually share one presentation/action surface.**

No new runtime state/enum is requested by this refinement.

---

## 14. What this pressure test does not establish

It does not establish:

- a universal investigation taxonomy;
- a numeric ranking formula;
- exact planner data structures;
- universal structural-first ordering;
- that every static contradiction should skip resolver corroboration in every product mode;
- final cost thresholds;
- autonomous package/build/test execution;
- complete security sandbox requirements;
- maintainer-facing action semantics;
- final Conversation-D stopping model.

---

## 15. Simulation disposition

This pressure test is complete enough for its current purpose.

### Main-branch handoff threshold

A handoff is **potentially justified** because S007 adds a real-world static-closure/cancel-planned-check contrast not present in the earlier S006/Challenge Pass 02 handoffs.

Before creating a separate handoff, compare against the latest main Conversation-C record:

- if main has already made evidence-state re-evaluation/check-cancellation and the distinct stop reasons explicit, no handoff is needed;
- if not, one short bounded handoff should carry only those refinements plus S007 as supporting evidence.

### Independent discovery

Continue broad real-world screening independently of main when useful. CARLA/OpenCV is the strongest retained direct-runtime candidate from Screening 03, but it should not become S008 automatically.

Confirmation cases remain legitimate external-validity evidence; novelty is not a mandatory admission criterion.