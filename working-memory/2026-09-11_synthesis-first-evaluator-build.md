# First Maintainer-Action Synthesis Evaluator — Working Memory

**Date:** 2026-09-11  
**Session status:** CONTINUED  
**Primary mode:** Build/Implement + Learning-by-Doing  
**Selected plan:** [`../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md`](../plans/OVERALL_EVIDENCE_SUFFICIENCY_AND_MAINTAINER_ACTION_SYNTHESIS_PLAN.md)  
**Accepted semantics:** [`../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md`](../docs/specifications/UPGRADEPILOT_MAINTAINER_ACTION_SYNTHESIS_SPECIFICATION.md)  
**Previous:** [`2026-09-11_synthesis-stable-semantic-acceptance.md`](2026-09-11_synthesis-stable-semantic-acceptance.md)  
**Continued by:** [`2026-09-11_targeted-check-action-admission.md`](2026-09-11_targeted-check-action-admission.md)

## Entry reconciliation

Before Build, the externally authored commit `a25d7f9b5a10d696f8d763e1b4c6d46ad53009e7` was reviewed against the Core authority rules, Product Decision Model, current producer chain, and accepted synthesis contract.

The correction is retained. Most importantly, Python-support applicability alone no longer pressures a runtime `block` path. The accepted synthesis specification now requires the actual proposal-level declared-support conflict, including trusted proposal identity, upstream support-exclusion authority, target support obligation, dependency/environment relationship, and the resulting conflict. Grounding a model-derived upstream claim establishes source correspondence, not independent semantic corroboration.

The same correction narrows first-evaluator admission: no non-abstention action is yet producer-proven through the normal path. Missing generic producers are not themselves proof that a narrow action-specific derivation is impossible.

## Build responsibility

Implement the smallest deterministic synthesis core that is truthful at current admission:

```text
PublicPullRequestInvestigation
→ deterministic maintainer-action evaluator
→ explained abstention
```

This increment deliberately does not integrate with the CLI and does not implement merge, targeted-check, investigate, block, or defer branches.

## Implemented source

Added `src/upgradepilot/maintainer_action.py`.

### Result type

`MaintainerActionSynthesis` preserves:

- the exact `PublicPullRequestInvestigation` as the source/provenance boundary;
- the currently admitted action (`abstain` only);
- decisive reasons;
- projected material residual uncertainty for currently handled branches;
- evaluator/admission limitations;
- explicit claim limits.

Keeping the source investigation avoids copying mechanism-specific evidence into a second semantic authority surface.

### Evaluator

`synthesize_maintainer_action(...)` currently returns only explained abstention.

It does not infer a more active action from a technical applicability state. That is intentional: no non-abstention permission has yet passed its action-specific normal-producer proof gate.

The evaluator currently projects material non-final state from:

- dependency-analysis problems;
- non-supported CI coverage state;
- unresolved/conflicted Python-support applicability;
- unresolved/conflicted artifact-serviceability applicability.

The complete source investigation remains attached even where this first projection is intentionally not yet a complete human-facing report.

## Focused proof assets

Added `tests/test_maintainer_action.py` with two independent responsibilities:

1. a supported exact dependency transition does **not** default to favorable or another active action;
2. a typed dependency-analysis problem remains visible in both the abstention reason and residual uncertainty.

During static inspection, the initial `uv.lock` fixture incorrectly used an invented extraction method (`structured_lockfile`). The real dependency contract admits `exact_base_head_files`; the fixture was corrected before proof was recorded. This is a useful reminder that type annotations using `Literal` do not automatically validate dataclass values at runtime.

## Validation evidence

### Source-level validation

- re-read the committed source/test files from `main`;
- reconciled the test fixture against `DependencyChangeSourceEvidence`'s actual closed vocabulary;
- Python 3.13 `py_compile` succeeded for local copies of the exact new source syntax and focused-test syntax after the fixture correction;
- Git diff from the externally corrected baseline contains only the new synthesis module and focused test file for this Build slice.

### Local executable proof — established

Ali synchronized local `main` from `a25d7f9b` to `4152117`, activated the project `.venv`, and confirmed the durable environment baseline:

```text
Python 3.12.3
/home/motafeq/projects/UpgradePilot/.venv/bin/python
```

Focused synthesis execution:

```bash
python -m unittest discover -s tests -p 'test_maintainer_action.py' -v
```

Result:

```text
2 tests passed
OK
```

Broader repository regression execution:

```bash
python -m unittest discover -s tests -v
```

Result:

```text
Ran 530 tests in 0.143s
OK
```

Therefore the previous executable-proof debt for this slice is closed:

```text
source/static validation = established
focused unittest execution against the actual repository = established
broader unit regression suite = established (530 passing)
CLI/application integration = NOT YET IMPLEMENTED
```

This proves the first evaluator executes in the real project environment and does not regress the current unit suite. It does not prove any non-abstention action or CLI/application integration.

## Learning / ownership progression

The post-Build walkthrough exposed and repaired several important understanding gaps. These are preserved because later learning should be able to reconstruct the real reasoning path rather than only the final terminology.

### Actions versus technical findings

An early ambiguity was whether technical states such as Python-support applicability, artifact uncertainty, or CI coverage were themselves the maintainer outputs. The corrected model is:

```text
technical investigation modules
→ establish mechanism-specific facts and uncertainty
→ maintainer-action synthesis composes those facts
→ one maintainer-facing Charter action
```

A technical finding therefore does not acquire action authority merely because it exists.

### “Baseline” was initially used too loosely

The term `baseline` caused recursion confusion: if merge depends on positive evidence / bounded scope / coverage, do those each need more “baselines”? The correction is:

- **deterministic baseline** means the whole first transparent synthesis implementation used as the trusted comparison/admission reference;
- individual actions have **permission conditions**;
- those conditions are supported by lower-level propositions and typed evidence rather than separate arbitrary baselines.

The reasoning bottoms out in concrete evidence with identity/provenance/authority, not endlessly nested booleans.

### Merge terminology was unpacked

For `merge after normal review`, the walkthrough clarified:

- **positive evidence** = evidence affirmatively supports the proposition needed for the decision, not merely absence of a known problem;
- **bounded scope/horizon** = exactly what UpgradePilot claims to have examined for this decision;
- **coverage** = whether the material parts of that owned horizon were actually examined at sufficient proof strength;
- **material** = decision-relevant; changing the fact could change the recommendation;
- **action** = maintainer-facing next-step recommendation, not a technical finding.

Ali explicitly preferred to leave merge until later because this favorable action depends on a more mature bounded-discovery/context/coverage story.

### Permission conditions are derived from evidence, not magic booleans

The useful hierarchy became:

```text
final action
→ action-specific permission conditions
→ lower-level propositions/evidence requirements
→ concrete typed investigation producers/evidence
```

Some implementation facts may later be represented as booleans/enums/structured objects, but the semantics are not defined by inventing a few booleans first.

### Targeted checks do not excuse incomplete investigation

A key question was why UpgradePilot would ask a maintainer to run a check rather than discovering the answer itself. The clarified boundary is:

```text
UpgradePilot has a justified admitted way to obtain the evidence itself
→ investigation should do that first

exact decision-critical question remains
+ concrete bounded discriminating check is known
+ UpgradePilot should not/cannot perform the same justified work first
→ maintainer targeted-check action may become eligible
```

This is an evidence-acquisition responsibility boundary, distinct from merge's bounded decision horizon.

### Scenario-specific rule explosion is not the intended design

Ali correctly challenged the idea of hand-writing a separate rule for every repository/package/environment scenario. The resulting model is:

```text
raw heterogeneous technical scenario
→ mechanism-specific investigation handles its complexity
→ normalized typed findings
→ small generic action-permission semantics
```

Different Python, artifact, or CI scenarios can therefore converge on the same synthesis shape, for example an exact unresolved decision-critical proposition plus one concrete discriminating check. This is the main reason deterministic synthesis does not automatically imply a giant case-by-case rule tree.

### Investigation and synthesis responsibilities became explicit

Ali restated the key insight that many technically different scenarios can end in the same normalized state because the complex scenario work happens earlier. The wording was refined to preserve the layer boundary:

```text
technical complexity → investigation
maintainer-facing decision composition → synthesis
```

The complex work is not an earlier stage *of synthesis*; it is primarily the investigation system before synthesis.

### Abstain is a safe admission boundary, not the bottom of a ladder

The initial impression that implementation was proceeding “from the loosest/bottom option upward” was corrected. Actions are not severity levels. `abstain` is simply the least-committal truthful initial permission when no non-abstention action has yet earned its own proof. Each later action must be admitted independently from its own evidence structure.

### The first implementation slice is intentionally small

Ali now has direct runtime evidence that the first slice is a synthesis boundary/container rather than a finished decision engine:

```text
PublicPullRequestInvestigation
→ synthesize_maintainer_action(...)
→ action = abstain
+ reasons
+ residual uncertainty
+ limitations
+ claim limits
+ exact source investigation retained
```

The focused and full tests plus manual runtime inspection established that this behavior is deliberate and executable, not merely an unfinished branch accidentally falling through.

### LLM remains a possible later bounded mechanism, not the current answer to heterogeneity

The repeated LLM question was narrowed. Many raw scenarios do not by themselves require an LLM because investigation can normalize technical complexity before synthesis. If later evidence shows that deterministic cross-evidence composition becomes brittle or requires excessive semantic branching, that would be concrete evidence for comparing a bounded LLM-assisted method. Any such model output still cannot silently create evidence authority or action permission; the earlier experiment pattern remains bounded model projection/output plus deterministic admission/validation.

## Scope limits

This increment does not prove:

- any non-abstention action path;
- complete residual-uncertainty/report projection;
- CLI rendering;
- application integration;
- persistence/serialization;
- objective safety;
- candidate-discovery completeness;
- repository-context completeness.

It also does not repair the separate patch/revision, command-recognition, or workflow-attempt correctness findings.

## Learning-by-Doing state

```text
Slice: first deterministic synthesis evaluator

A — DONE:
    oriented the new post-investigation synthesis layer, corrected action admission, and selected explained abstention as the only currently admitted runtime action.

B — DONE:
    added the core result/evaluator and focused proof file on main; corrected one invalid test fixture discovered during contract inspection.

C — DONE:
    preserved implementation, proof evolution, and meaningful learning/ownership corrections in this record.

D — DONE:
    walked through the real code/data-flow boundary and repaired the main ownership gaps around action-vs-technical findings, permission conditions, investigation-vs-synthesis responsibility, deliberate abstention, and the possible bounded future LLM role.

E — DONE:
    executable proof was established locally (2 focused tests + 530 full-suite tests), the next bounded slice was selected by evidence/readiness rather than action ordering, and continuation moved to targeted-check action admission.
```

`UP-SKILL:upgradepilot-build-implement`  
`UP-SKILL:upgradepilot-learning-by-doing`  
`UP-SKILL:upgradepilot-working-memory`
