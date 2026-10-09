# Canonical Investigation Workspace architecture and recovery contract

**Educational snapshot:** 2026-10-09, repository closure commit **`62739556f06fe21a80331953d386b44b5e0edaa2`**. This note teaches the architecture and recovery contract accepted at the end of the Investigation Workspace / Investigator-interface design cycle. It does **not** claim that the Workspace, persistence, native codecs, recovery, replay, or consumer cutover are implemented in production source at this horizon.

**Primary owners at this snapshot:** [ADR-0012](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/docs/architecture/ADR-0012-canonical-investigation-workspace-and-recovery-boundary.md), [Core §6.4](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md#64-canonical-investigation-recovery-and-explicit-continuation), [Charter §6](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/PROJECT_CHARTER.md#6-required-core-outcome), and the [closed design-cycle record](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/working-memory/2026-10-07_investigation-workspace-and-investigator-interface-design_lbd-cycle.md). The four-note [Workspace implementation research package](2026-10-09-workspace-implementation-architecture-research/README.md) is the deep experimental companion; it is evidence, not the architecture owner.

## 1. The central mental model

UpgradePilot already has native owners for bounded facts and assessments: dependency changes, CI/static/runtime evidence, package-manager semantics, upstream release facts, target declarations/relevance, impact applicability and maintainer-action synthesis. The accepted Workspace architecture does **not** replace those owners with one generic reasoning layer.

The missing product responsibility is different: an adaptive investigation needs one place that can preserve **how investigation knowledge evolves across time** without stealing the authority of the native owners that produced or evaluated that knowledge.

The accepted structure is:

```text
native evidence producers / domain evaluators
                ↓
      canonical Investigation Workspace
                ↓
 bounded Investigator / evaluator projections
                ↓
 proposals / requests / attempts / observations
                ↓
 independent admitted evaluation
                ↓
       successor Workspace revision
                ↓
      synthesis / report projections
```

The Workspace therefore owns **composition and lifecycle**, not generic truth.

A useful ownership rule is:

```text
native owner
→ establishes its bounded fact / assessment

Workspace host
→ preserves identity, relationships, lifecycle, history and admission/publication

Investigator
→ reads bounded context and proposes meaning or evidence-acquisition work

admitted evaluator
→ establishes the proposition it actually owns

maintainer synthesis
→ owns action permission

report
→ presents selected knowledge; it does not become canonical state
```

If one of these layers silently takes another layer's authority, the architecture has failed even if every object is well typed.

## 2. Why the existing frozen result is not enough

At this snapshot, production source still exposes [`PublicPullRequestInvestigation`](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/src/upgradepilot/investigation.py), a frozen dataclass described by the source itself as the **“typed result of the current read-only evidence and reasoning sequence.”** The normal orchestrator runs one current sequence and returns that result.

That shape is useful for the current fixed flow, but an evolving investigation must represent things the frozen result was never designed to own:

- which exact Workspace revision a view or request came from;
- what material premises an outstanding request depended on;
- proposal, admission, attempt, observation and evaluation history;
- unavailable/failed/empty/unsupported states without collapsing them;
- candidate/proposition refinement and counterevidence lineage;
- which evidence existed versus which evidence was actually delivered to a mechanism;
- stopping proposals versus actual adequacy authority;
- unfinished or completion-unknown work;
- enough retained state for canonical historical recovery.

Extending the frozen result until it carried all of those responsibilities would effectively turn it into a different kind of object while preserving the old name and consumer assumptions. ADR-0012 therefore accepts a **distinct composed/evolving Investigation Workspace** as the canonical logical investigation state.

The current synthesis source makes the migration boundary concrete. [`synthesize_maintainer_action`](https://github.com/motafegh/UpgradePilot/blob/62739556f06fe21a80331953d386b44b5e0edaa2/src/upgradepilot/maintainer_action.py) still explicitly requires `PublicPullRequestInvestigation`, and its admitted action remains only explained `abstain`. This is current implementation truth, not a reason to keep the legacy snapshot canonical forever.

## 3. What one Workspace revision means

A Workspace has a continuing **investigation lineage**, while each revision is bound to an exact target snapshot. For the accepted design, the important target identity includes the repository, pull request, exact base SHA, exact head SHA and relevant dependency transition.

A revision is not just “version 8 of a dictionary.” It means:

> this is the canonical investigation state after a declared update, for this exact target, with this retained history and these explicit gaps.

The research-backed implementation-entry direction is **immutable published successors with shared immutable payloads**. The conceptual point matters more than the Python mechanism:

```text
W7 remains historically W7

new evidence / lifecycle event
        ↓
construct successor state
        ↓
validate it
        ↓
publish W8
```

Earlier membership must not change because a later revision was published. The research negative control showed why a read-only wrapper over a shared mutable backing collection is insufficient: an old view can still “see” later records if the underlying index is mutated.

Immutable publication does **not** imply copying all evidence bytes every time. Shared immutable payloads can belong to several revision indexes while each revision preserves its own frozen membership and relationships.

## 4. The lifecycle: evidence is not proposal, proposal is not truth

The accepted architecture separates several records that are easy to blur together.

### Discovery before a candidate exists

A **Discovery Objective** can justify bounded pre-candidate exploration:

```text
exact target + bounded question/horizon/scope
→ capability request
→ admitted attempt
→ observation/problem
→ possible candidate proposal
```

It does not establish that discovery is complete, that no impact exists, or that action is safe.

### Investigation after a proposition exists

An **Investigation Need** is different. It is tied to an already material non-final proposition/candidate and identifies evidence that could discriminate it.

```text
non-final proposition
→ Investigation Need
→ bounded Capability Request
→ host admission
→ attempt
→ observation/problem
→ owning evaluator
→ successor assessment
```

The request does not authorize itself. A successful observation does not establish the proposition. The host cannot turn an admitted proposal into domain truth merely because its references exist.

### Proposal and evaluation

A semantic/candidate **Proposal** is attributed suggested meaning. Structural proposal admission can verify references, scope and revision binding, but semantic support belongs to an admitted evaluator.

If no evaluator owns the proposition, the truthful state is an **unsupported evaluation attempt**. The Workspace must not invent an “unresolved assessment” just to make the state machine look complete.

This distinction is central:

```text
unresolved evidence under an admitted evaluator
!=
no admitted evaluator exists
```

They imply different next responsibilities.

## 5. Evidence use is relational, not one status field

A major lesson from the broader LLM research was that “the evidence exists” is not the same as “the mechanism used it.” The Workspace therefore keeps these meanings separate:

```text
AVAILABLE
→ retained/recoverably referenced in Workspace

DELIVERED / CURRENTLY VISIBLE
→ included in a particular consumer view

EXAMINED / USED
→ observably used when that can actually be established;
  otherwise unknown

CITED
→ referenced by a proposal/report

EVALUATED SUPPORT
→ explicitly considered by the admitted evaluator

SUFFICIENT
→ established only by the proposition/action owner for its exact decision
```

Do not compress this into one generic `evidence_status` or confidence score.

A concrete example: the Workspace may retain exact changelog content while a bounded Investigator view delivers only a reference to it. The content is **available but not delivered**. The mechanism cannot honestly call it unavailable, and a proposal cannot cite the undisclosed bytes from that view. A later explicit read can deliver the content without rewriting the history of the earlier view.

## 6. One real UpgradePilot flow: support-drop relevance

The support-drop path is useful because its native responsibilities already exist, while the Workspace lifecycle around them is the new accepted composition method.

A representative path is:

```text
exact dependency release interval
→ grounded upstream Python-support-drop candidate
→ native impact assessment = unresolved
→ selected target-declaration investigation need
→ exact-head pyproject.toml read
→ target Python declaration / relevance evaluation
→ successor support-impact assessment
```

Two results can be legitimate depending on the exact target:

- if the dropped Python line overlaps the target's declared support, the bounded support-impact path may become applicable;
- if the target declares `requires-python >=3.10` and the candidate is only a Python-3.8 support drop, that path can become `established_not_applicable`.

Neither result means:

```text
all dependency impacts are known
all candidate discovery is complete
CI proves compatibility
maintainer action is authorized
```

The Workspace's contribution is not to reimplement target relevance. It preserves the objective/need, exact request basis, observation, native successor assessment and history so later consumers can understand **what changed and why**.

For the real public grounding and controlled migration evidence behind this model, use [research note 4](2026-10-09-workspace-implementation-architecture-research/04_native_integration_migration_and_engineering_proof.md).

## 7. Original basis and current basis solve different problems

A delayed result must preserve where it came from **and** prove that it is still applicable now.

Suppose request `R7` was created at `W7` against target `H1`. Before the result arrives, `W8` is published.

If W8 only adds unrelated evidence:

```text
R7 originated at W7
→ current target/material premises still match at W8
→ admit the result into successor W9
```

The history remains truthful:

```text
requested at W7
validated against W8
ingested at W9
```

Do not pretend R7 originated at W8, and do not reject it merely because `W7 != W8`.

If W8 changed a material premise, source association, method, request scope or candidate identity, the old result may remain historical but must not silently become current evidence for the changed basis.

This yields two independent controls:

```text
expected-revision publication
→ protects canonical storage from lost updates

material-basis validation
→ protects semantic applicability of delayed/prepared work
```

A publication conflict means the canonical state advanced. It does **not** by itself prove that the evidence is stale.

## 8. Stopping is also an authority boundary

Three things must remain separate:

```text
mechanism run ended
!=
Investigator proposed stopping
!=
canonical investigation is adequate to stop
```

A model/agent can call `finish()` or emit a stopping proposal while a feasible decision-critical check still exists. Canonical `continue`/`stop` requires an admitted adequacy owner/method evaluating the current material state.

If no such method exists, the truthful result is unsupported adequacy evaluation plus visible open obligations. The architecture deliberately does **not** choose “ask a second LLM” as the answer.

This preserves one of UpgradePilot's broader evidence principles: procedural completion must not be promoted into decision completeness.

## 9. Canonical recovery: what must survive a restart

Core §6.4 accepts durable canonical Workspace recovery as an intended responsibility.

A durable checkpoint must declare one coherent boundary and retain the **material dependency closure** needed to explain and continue it. Depending on the admitted path, this can include:

- exact target/lineage/revision identity;
- native owner/type/scope/provenance and retained content or explicit content gaps;
- proposals, admissions and evaluation inputs/results;
- candidate/proposition lineage;
- discovery objectives and coverage limits;
- investigation needs;
- request/admission/attempt/observation/problem relations;
- material consumer views and method identity at the admitted proof boundary;
- run termination, stopping proposals and adequacy state;
- unfinished, failed, unsupported, stale, conflicted and completion-unknown states.

The checkpoint does **not** need every transient debug byte or hidden model state. “Material closure” is consumer/proof driven, not universal raw capture.

### Serialization fidelity is not completeness

A checkpoint can serialize and deserialize perfectly while still omitting a material input that was never captured. The research demonstrated exactly that with result-only capture.

```text
perfect round trip
= preserved everything supplied to the encoder

perfect round trip
!= proved the encoder was given every material dependency
```

This is why capture must occur at the producer/composition boundary while material inputs still exist, not only after the final legacy result has been built.

## 10. Recovery, continuation and replay are three different operations

This is one of the most important distinctions in the accepted contract.

### Recovery

```text
durable checkpoint
→ validate representation / references / coherence
→ restore historical canonical state offline
```

Recovery must not issue requests, invoke models/evaluators, retry work, rebase the target or infer present source validity.

### Explicit continuation

```text
recovered historical state
→ validate current target / material premises / method / authority
→ admit new work
→ produce fresh attributed facts/state
```

Historical admission is not current execution permission.

### Deterministic replay

Charter §6 separately requires:

```text
retained inputs + admitted deterministic processing/method identity
→ re-execute the supported historical processing boundary
→ compare against explicit equivalence criteria
```

Replay is not “open the checkpoint.” It is also not “rerun live GitHub/PyPI/model interactions.” The activating owner must define exactly which retained inputs, method identities and equivalence oracle belong to the replay promise.

A system may therefore have:

```text
successful checkpoint recovery = yes
trusted historical inspection = yes
explicit continuation path = yes
deterministic replay = not implemented
```

without contradiction.

## 11. Interruption and ambiguous acknowledgement

Suppose `W5` commits successfully, but the process dies before the caller receives “publication successful.” After restart, storage inspection finds a valid W5.

The correct interpretation is:

```text
canonical storage state:
W5 exists and is valid

historical caller knowledge:
acknowledgement was not received

retry authority:
none merely from the lost acknowledgement
```

The host first reconciles current state. It must not automatically repeat an external operation that may already have happened.

Likewise, if a process dies before a Workspace transaction commits, partial W5 database writes must not become canonical. W4 remains the last published boundary. Losing uncommitted progress is preferable to fabricating a half-coherent canonical revision.

The research-backed provisional persistence baseline is SQLite **WAL/FULL**, but that is an implementation-entry direction, not an architecture guarantee. The accepted semantic responsibility is coherent publication/recovery; SQLite is currently the best-supported candidate mechanism under the research evidence.

## 12. Cold native reconstruction is a separate proof obligation

Recovering exact bytes is not the same as recovering a trusted domain object.

After a fresh process restart, the system may have an exact retained representation of a historical `RuntimeDependencyStateResult` or `PropositionAssessment`, but no live Python object from the original process.

The safe design cannot simply do:

```text
retained class name
→ dynamic import
→ trust reconstructed object
```

and it must not silently rerun the evaluator during recovery.

The accepted implementation-entry obligation is **owner-specific, version-aware native capture and cold trusted reconstruction** for admitted families.

A codec/reconstruction method must be able to reject, as applicable:

- unsupported schema/type versions;
- missing required material;
- wrong target or material basis;
- inconsistent references/identity;
- malformed values that violate native invariants.

If no admitted reconstruction method exists, `unsupported_native_codec` is a truthful limitation rather than an excuse to invent a trusted object.

The deep experimental evidence for this gap is in [research note 4](2026-10-09-workspace-implementation-architecture-research/04_native_integration_migration_and_engineering_proof.md).

## 13. Migration: replace the canonical boundary, do not run two truths

The accepted target is:

```text
native producers / evaluators
        ↓
canonical Workspace
        ↓
direct synthesis / report / Investigator / evaluator projections
```

not:

```text
old investigation pipeline
+
new independent Workspace pipeline
```

During migration, a temporary one-way projection may be justified:

```text
Workspace
→ temporary PublicPullRequestInvestigation-shaped projection
→ existing synthesis/report
```

but only for a named parity, compatibility or proof need, with an explicit loss boundary and removal/reassessment trigger.

The bridge is lossy with respect to new Workspace responsibilities: the old snapshot cannot represent revision/basis history, evidence-delivery state, request/attempt lifecycle, proposals/evaluations, material-retention closure or unfinished work. Therefore the projection cannot become the canonical state from which a Workspace is later reconstructed.

Migration completes only when normal acquisition/evaluation publishes into the Workspace, consumers read proper Workspace/native projections, recovery/lifecycle proof exists for the admitted scope, and no independent obligation earns the legacy snapshot another canonical path.

## 14. What is accepted now, and what remains open

The closure decision accepts these as **implementation-entry directions**:

| Direction | Status at this snapshot |
| --- | --- |
| Canonical composed/evolving Workspace | Accepted architecture via ADR-0012. |
| Durable coherent canonical recovery | Accepted semantic responsibility via Core §6.4. |
| Immutable published successors + shared immutable payloads | Accepted implementation-entry baseline from research. |
| All-in-SQLite WAL/FULL | Accepted **provisional** persistence baseline; not a power-loss claim. |
| Small typed storage-independent Investigator/Workspace seam | Accepted implementation-entry direction. |
| Expected-revision publication + material-basis validation | Accepted as distinct controls. |
| Direct producer capture + direct consumer cutover | Accepted migration direction. |
| Versioned native capture/cold reconstruction | First-class future Build proof obligation. |

Important choices remain deliberately open:

- exact production Python module/type/schema layout;
- checkpoint cadence and maximum accepted lost-progress window;
- retention duration, backup/disaster recovery, privacy/deletion and schema migration;
- physical-write/power-loss proof;
- exact deterministic replay boundary and equivalence criteria;
- complete supported native-family scope;
- concrete Investigator/discovery policy;
- semantic-conflict evaluator and canonical adequacy evaluator;
- model/framework/agent topology;
- whether measured scale later earns hybrid blob storage or an out-of-process transport boundary.

Open does not mean forgotten. It means the accepted architecture does not manufacture evidence for decisions whose owning pressure has not yet appeared.

## 15. Current fact versus accepted target

Keep this table available when reading source after this snapshot:

| Question | Current implementation fact at `62739556…` | Accepted target / responsibility |
| --- | --- | --- |
| Canonical application result | `PublicPullRequestInvestigation` frozen result still exists. | Distinct evolving Investigation Workspace becomes canonical after Build/cutover. |
| Synthesis input | `synthesize_maintainer_action` requires `PublicPullRequestInvestigation`. | Synthesis should consume an explicit Workspace/native projection. |
| Maintainer action | Only explained `abstain` is admitted. | Workspace does not broaden action permission; synthesis remains owner. |
| Persistence | No production Workspace store. | Provisional SQLite WAL/FULL baseline must still be implemented/proven. |
| Recovery | Saved report opening exists, but is not canonical Workspace recovery. | Core §6.4 defines future canonical checkpoint recovery/continuation semantics. |
| Cold native reconstruction | Not implemented. | Versioned owner-specific reconstruction must be proven for admitted families. |
| Replay | Separate retained product obligation, not implemented by accepting recovery. | Later activating owner must define inputs/method/equivalence and prove it. |

This prevents a common architecture-learning mistake: confusing an accepted design with current source behavior.

## 16. The engineering progression worth remembering

The value of the design cycle is not the chronology of every meeting. The transferable progression is:

```text
1. Existing native owners were already stronger than a proposed generic reasoning layer.

2. The actual missing responsibility was cross-domain evolving investigation state,
   not a universal evidence type.

3. Workspace ownership therefore became composition/lifecycle rather than truth.

4. Pressure testing exposed additional distinctions:
   pre-candidate discovery vs proposition-directed investigation,
   procedural finish vs adequacy,
   available vs delivered evidence,
   unsupported evaluator vs unresolved evidence,
   revision change vs material staleness.

5. Recovery analysis exposed that report reopening was insufficient,
   so durable canonical checkpoint recovery became an explicit product responsibility.

6. Charter review caught a separate mistake: recovery is not deterministic replay.

7. Implementation research then tested representation, persistence, seam and migration,
   and exposed the cold native-codec gap instead of hiding it.

8. D/E accepted the architecture and bounded implementation directions
   while preserving unimplemented responsibilities honestly.
```

The recurring lesson is: **separate ownership first, then preserve enough identity/history to explain how knowledge changes without promoting evidence beyond what its owner established.**

## 17. Proof and non-proof at this snapshot

What supports this learning artifact:

- accepted ADR-0012 and Core §6.4 at closure commit `62739556…`;
- current source showing the legacy frozen result and current synthesis type boundary;
- closed B1–B4/D/E design record;
- merged four-experiment research package and its failure/correction evidence;
- recorded research verification of 121 scoped experiment tests plus 115 focused product tests at its final horizon;
- earlier B4 design-anchor verification of 58 native/report tests.

These do **not** prove:

- a production Workspace exists;
- SQLite is production durable under power loss;
- all native material is captured;
- cold codecs are implemented;
- general semantic conflict or adequacy evaluation exists;
- an Investigator/model autonomously discovers correct concerns;
- deterministic product replay exists;
- the legacy result is already retired;
- a non-abstention maintainer action is permitted;
- Ali has blanket source mastery merely because this note exists.

## 18. Learning depth

**Must own**

- native/domain authority versus Workspace composition/lifecycle authority;
- evidence → proposal/request → admission → observation/problem → evaluation separation;
- original basis versus current material-basis validity;
- available/delivered/examined/cited/evaluated/sufficient distinctions;
- stopping proposal/procedural finish versus canonical adequacy;
- material dependency closure versus serialization fidelity;
- recovery versus continuation versus replay;
- one-way migration/projection and why the legacy snapshot cannot become canonical again by default.

**Understand operationally**

- immutable successor revisions and shared immutable payloads;
- expected-revision publication and acknowledgement ambiguity;
- why SQLite WAL/FULL is provisional evidence-backed machinery rather than semantic authority;
- why cold reconstruction needs version-aware native codecs;
- how consumer projections can select/reformat without strengthening evidence.

**Lookup-level**

- exact experimental dataclass fields, SQLite schema/PRAGMA details, JSON codec syntax and benchmark numbers;
- exact test/helper names unless diagnosing that experiment.

**Deferred deliberately**

- production codec/schema design;
- checkpoint cadence/retention/disaster-recovery policy;
- exact replay implementation;
- semantic-conflict/adequacy evaluator design;
- future agent/model/framework topology;
- hybrid storage or process-isolation architecture until evidence requires it.

## 19. Fast relearning route

When returning after several weeks:

1. Read ADR-0012 from **Decision** through **Replacement-oriented migration**.
2. Read Core §6.4 and state aloud why recovery cannot execute anything.
3. Open `PublicPullRequestInvestigation` and `synthesize_maintainer_action` at this snapshot to recall current-vs-target separation.
4. Trace the support-drop flow in section 6 and the delayed-result flow in section 7.
5. Open research note 4 only if you need to recover why cold native reconstruction remains a real gap.
6. Answer the transfer questions below before rereading their relevant sections.

## 20. Transfer / ownership questions

1. A changelog is retained in the Workspace but omitted from one Investigator view. What can you say about availability, delivery, examination and citation, and what can you **not** infer?
2. Request `R7` was created at `W7`; unrelated evidence creates `W8` before R7 returns. Which identities/bases must be preserved and checked before admitting its result into `W9`?
3. A recovered checkpoint is coherent and byte-perfect, but the current process has no admitted codec for one historical native assessment. What can recovery establish, and what must remain unsupported?
4. A process dies after W5 commits but before acknowledgement. Why does recovery inspect current canonical state before any retry, and why is this a different question from semantic staleness?
5. During migration, what concrete responsibility could justify keeping a temporary `PublicPullRequestInvestigation` projection, and what condition should cause its removal?

---

`UP-SKILL:upgradepilot-learning-artifact`  
`UP-SKILL:upgradepilot-planning-design`
