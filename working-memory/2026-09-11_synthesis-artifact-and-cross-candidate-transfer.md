# Synthesis Artifact and Cross-Candidate Transfer — Working Memory

**Date:** 2026-09-11  
**Session status:** CONTINUED  
**Primary mode:** Planning/Design + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Previous:** [`2026-09-10_synthesis-real-case-transfer-and-handoff.md`](2026-09-10_synthesis-real-case-transfer-and-handoff.md)  
**Continued by:** [`2026-09-11_synthesis-stop-defer-abstain-transfer.md`](2026-09-11_synthesis-stop-defer-abstain-transfer.md)

## Session anchor

Continue the real-evidence-first synthesis design route established by the September 10 plan re-anchor. The previous record remains the detailed provenance for the route correction and the S007/Python investigation-handoff transfer. `MEMORY.md` selected this record as the live continuation at this point; the record is now continued by the linked September 11 stop/defer/abstain transfer record.

No source/test implementation, stable specification change, new simulation case, framework work, or LLM synthesis experiment is admitted in this session.

## Gap repair from the previous reasoning checkpoint

Ali answered that he did not yet know whether final proposition-local stopping should be represented by a new explicit stop field or derived from existing state.

The minimum mental model is:

```text
final proposition state
→ the owned technical question is already closed
→ do not add another stop fact merely to restate closure

unresolved proposition state
→ closure cannot be inferred
→ continuation/stopping meaning may require additional investigation-owner evidence
```

Current design preference therefore remains:

- derive proposition-local stopping from an already-final applicability state;
- do not add a generic `no_further_investigation` flag merely for final Python results;
- reserve richer handoff semantics for unresolved post-attempt states where current producers do not establish whether another justified UpgradePilot investigation exists, no justified investigation remains, or a useful outside responsibility is known.

This is still a design conclusion, not a new accepted specification rule.

## Evidence-transfer map 2 — S008 versus current artifact-serviceability path

### Evidence basis

- **S008:** preserved real CARLA/ScenarioRunner/OpenCV case. It establishes a bounded artifact transition: old compatible prebuilt wheel path exists, proposed compatible prebuilt wheel path disappears, proposed source distribution remains, and source-build success stays a distinct downstream proposition.
- **Current artifact-serviceability source:** exact old/proposed PyPI inventories can formulate a target-agnostic wheel-serviceability candidate. Exact target applicability requires `TargetWheelCompatibilityEvidence` containing target-supported wheel tags.
- **Current Target artifact-environment source/tests:** workflow runner, literal setup-python version, and direct install declaration are partial static facts only. `exact_wheel_compatibility_state` deliberately remains `unresolved`; matrices, containers, dynamic expressions and runtime formation are not upgraded into exact wheel-tag evidence.
- **Current application path:** after forming an artifact candidate, normal application evaluates it without exact target compatibility evidence and may compose partial Target artifact-environment results, but it does not convert those results into `TargetWheelCompatibilityEvidence`, does not reevaluate artifact applicability with exact tags, and has no artifact-specific selector that can obtain those tags.
- **Focused evaluator tests:** controlled tests can manually inject exact `TargetWheelCompatibilityEvidence` and prove both applicable and not-applicable outcomes. Those tests prove the evaluator contract, not normal producer reachability.

### Transfer and reachability map

| Needed distinction | Current product status | Evidence / interpretation |
|---|---|---|
| exact old/proposed published wheel inventories | **available** | PyPI release evidence is consumed by the artifact candidate builder |
| published wheel compatibility capability loss across releases | **available** | removed wheel tags form the target-agnostic candidate |
| proposed source distribution exists | **available** | candidate preserves `proposed_source_distribution_available` |
| exact target runner / literal Python / direct install declaration | **partially available** | Target artifact-environment evidence preserves these as static declaration-strength facts |
| exact target-supported wheel tags | **genuinely missing from the normal producer path** | the evidence contract exists, but current Target composition intentionally does not infer tags |
| target had an old compatible wheel | **derivable only after exact target tag evidence exists** | evaluator intersects old published tags with target-supported tags |
| target lacks a proposed compatible wheel | **derivable only after exact target tag evidence exists** | evaluator intersects proposed published tags with target-supported tags |
| target-specific artifact-serviceability applicability | **currently unresolved in the normal application path when a candidate exists** | normal application does not supply exact tag evidence to the evaluator |
| exact wheel-compatibility investigation selected/attempted | **not owned by the current artifact path** | no artifact-specific selector/investigation result analogous to the Python declaration acquisition exists |
| source fallback availability | **available at release-inventory strength** | proposed sdist presence is known |
| source fallback succeeds in exact target environment | **not established and intentionally separate** | S008 shows this is a different proposition; current artifact candidate also states source-build success remains separate |
| CI exercises the exact artifact-selection branch | **not established merely from package installation or partial Target facts** | S008 and current Target proof boundaries both reject broad installation/configuration as exact branch coverage |

### Main design consequence

The artifact gap is earlier than the Python unresolved-post-attempt gap.

```text
Python
→ one admitted investigation exists
→ normal application selects + attempts it
→ unresolved continuation may still lack an explicit stop/next-investigation conclusion

Artifact serviceability
→ exact discriminating evidence contract exists
→ normal application has no producer/selector that can satisfy it
→ target-specific applicability remains unresolved before any equivalent exact-compatibility investigation occurs
```

Therefore this is **not primarily a synthesis-input projection problem**. A synthesis layer cannot repair it by inventing target tags, interpreting `runner + Python` as exact compatibility, or treating absence of a producer as proof that the evidence is unobtainable.

The next design question belongs first to the investigation/capability boundary:

```text
Is obtaining exact target wheel-compatibility evidence a justified UpgradePilot-executable investigation for the admitted product scope?
```

Only after that is answered can later synthesis distinguish:

```text
product should investigate first
vs
useful check exists but lies outside UpgradePilot execution boundary
vs
no sufficiently justified investigation exists
```

No artifact investigation implementation is authorized by this finding.

### S008 stopping lesson retained

S008 also prevents a second overreach:

```text
wheel-path transition established
+ sdist exists
+ source-build success unresolved
!= source-build investigation automatically required
```

The real case stopped because its owned question was the installation-path transition. Source-build success is a separate downstream consequence proposition and becomes active only if a later owned decision actually needs it.

This distinction must remain visible when synthesis later pressures `run targeted checks`, `investigate or block`, or abstention. Synthesis should not demand deeper execution merely because a related uncertainty exists.

## Evidence-transfer map 3 — S009/S010 and heterogeneous synthesis

### Repository context

S009 establishes with a real public pandas update that repository purpose/provenance can be decision-relevant without being technical applicability. The repository's publication-reproduction contract was inconsistent with the updated dependency pin even though technical breakage and changed numerical output were not established.

Current consequence:

- repository context may legitimately matter to overall synthesis;
- it must not be coerced into a mechanism-specific applicability candidate;
- current `PublicPullRequestInvestigation` does not yet expose a generic S009-style repository-purpose/context finding owner;
- therefore V1 must not invent policy/context downstream merely because simulation demonstrates that such context can matter.

A future favorable or blocking action that requires such context needs a real admitted producer or must remain unavailable/restricted.

### Multiple candidates and different handling

S010 establishes with a real NumPy requirement-broadening proposal that:

```text
same dependency transition
+ same target runtime area
!= same mechanism
!= same target handling
```

One candidate was exposed by removal of a version guard; another had a local compatibility shim. Candidate B's mitigation did not erase Candidate A, and neither the two candidates nor their handling established complete NumPy-2 discovery coverage.

Current consequence for synthesis:

- consume current mechanism results independently rather than converting them into mechanism votes or one scalar;
- preserve material evidence identity and lineage for each mechanism;
- do not treat one non-applicable/mitigated/closed candidate as erasing another concern;
- do not treat the currently implemented Python-support + artifact-serviceability families as proof that candidate discovery is complete;
- do not add a generic mitigation enum merely because S010 contains one mitigated mechanism; current admitted mechanisms must first demonstrate a real need for such shared representation.

### Favorable-action pressure exposed

S009/S010 make the favorable-action problem sharper:

```text
all currently implemented mechanism results look non-concerning
!= adequate bounded discovery/context coverage established
```

The current product has mechanism-specific results but no general owner proving that the evaluated mechanism/context coverage is sufficient for a broader favorable recommendation.

This does not prove that `merge after normal review` must remain permanently unavailable. It means the positive permission boundary cannot be based merely on:

- Python-support non-applicability;
- no artifact candidate;
- green/bounded CI;
- absence of another currently implemented mechanism result.

A smaller enforceable bounded-coverage contract may still be possible, but it must be designed and accepted explicitly rather than inferred from current code breadth.

## Current design position after three transfer maps

The real-case transfer is now separating three different missing-responsibility shapes:

```text
1. Python unresolved post-attempt continuation
   → investigation happened; broader justified continuation/stopping may be missing

2. Artifact exact-compatibility applicability
   → exact evidence contract exists; normal investigation producer/selector is missing

3. Repository-context / discovery-coverage support for broader synthesis
   → real cases prove these dimensions can matter; current normal product may not own the necessary producers/coverage claim
```

These should not be solved by one universal handoff enum or generic planner.

## Learning-by-Doing progression

```text
Slice: repair S007 reasoning gap and transfer S008/S009/S010 into current synthesis design

A — DONE:
    repaired the final-vs-unresolved stopping distinction before using it as a premise.

B — DONE:
    traced S008 against current artifact evaluator, Target artifact-environment producer, normal application reachability and focused tests; then transferred S009/S010 repository-context and heterogeneous-candidate pressure.

C — DONE:
    preserved the artifact producer gap, downstream-consequence stop boundary, repository-context limitation and cross-candidate/discovery-coverage consequences here.

D — compressed for this slice:
    the previous learner gap was repaired directly rather than turning it into another quiz. The new artifact/cross-candidate findings were explained from real cases and current source truth.

E — ACTIVE:
    next pressure S011/S012 and the no-tool transfer evidence to distinguish question-settled stopping, known useful outside responsibility, and honest unresolved/abstention without importing old experiment disposition labels directly into synthesis.
```

## Current route

Next bounded slice:

```text
S011 + S012 + B2/X1 no-tool transfer
→ question-relative stopping / outside capability / unresolved distinction
→ reconcile those semantics with current product producer reachability
→ identify whether `defer` or abstention needs any genuine new producer facts
```

After that, return to the remaining candidate gaps:

- maintainer-facing targeted-check handoff after product investigation boundaries are respected;
- `investigate` versus `block` inside the Charter family;
- positive favorable-action prerequisites.

Do not request new product-simulation work until those questions have been checked against the existing corpus.

`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-planning-design`  
`UP-SKILL:upgradepilot-working-memory`
