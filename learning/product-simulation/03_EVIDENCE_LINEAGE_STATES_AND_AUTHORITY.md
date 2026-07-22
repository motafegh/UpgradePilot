# 03 — Evidence Lineage, States, and Authority

**Depth target:** Implementation-adjacent understanding.  
**Primary question:** How does UpgradePilot move from source material to a decision without disguising interpretation as fact?

## 1. The central distinction

The simulation uses this chain:

```text
raw or referenced source
→ evidence item
→ attributed claim or interpretation
→ finding
→ decision reason
→ report statement
```

Every arrow changes the responsibility and the authority of the record.

A source being acquired does not mean its contents are true. A statement being accurately extracted does not mean it is corroborated. A corroborated upstream fact does not mean it matters to the target repository. A relevant finding does not automatically permit a stronger decision.

## 2. Raw source material

Raw material is the bounded thing actually acquired or generated:

- PR metadata;
- patch;
- manifest or lockfile excerpt;
- tagged source;
- changelog;
- advisory record;
- workflow definition;
- CI run/job summary;
- log or error response;
- test output;
- registry metadata.

Preservation can be:

- complete raw capture;
- bounded material capture;
- durable immutable reference;
- explicit non-preservation.

The correct strategy is the smallest one that retains audit, replay, disappearance-risk, and decision value.

## 3. Evidence item

An evidence item records:

- what was acquired or failed;
- exact source and revision identity;
- producing operation;
- raw/reference location;
- direct observation;
- evidence state;
- authority and allowed use;
- what it cannot establish;
- freshness and retention state;
- downstream references.

Example:

> The GitHub job-log endpoint returned HTTP 410 for the historical S002 Docker job.

This is evidence of log inaccessibility through the attempted path. It is not evidence that the job failed, passed incorrectly, or used a particular dependency resolution.

## 4. Claim and interpretation

A claim or interpretation assigns meaning to one or more evidence items.

Important record types include:

- attributed source claim;
- deterministic comparison;
- parser-derived claim;
- dependency-path interpretation;
- CI-authority interpretation;
- constraint interpretation;
- relevance assessment;
- contradiction assessment;
- human or model interpretation.

The transformation must identify its actor and method.

Example from S002:

```text
workflow definition
+ changed path
+ exact-head run/job
+ Dockerfile
→ CI-authority interpretation:
  installation and image build were exercised,
  but Ruff and pytest did not run
```

This is not a direct statement from one source. It is a joined interpretation grounded in several sources.

## 5. Finding

A finding is a case-level conclusion that may affect the decision.

It should preserve:

- statement;
- state;
- supporting evidence and transformations;
- contradicting records;
- repository/revision scope;
- uncertainty and limitations;
- permitted decision effect;
- prior state and supersession reason.

Example:

> S002's successful Docker CI proves dependency installation and image construction only; it does not establish TestClient compatibility.

This finding is stronger than one evidence item because it joins trigger, command, path, runner, and target-use evidence.

## 6. Decision reason

A decision reason is not a new fact. It is the explicit use of findings and limitations to justify a bounded action.

S002 decision reasoning includes:

- the removed HTTPX API intersects a real TestClient path;
- a fixed framework branch existed, so an indefinite block is disproportionate;
- the exact target environment is missing;
- relevant tests did not run;
- therefore exact-head resolver capture, Ruff, and pytest are proportionate.

## 7. Report statement

A report statement is an external projection for a maintainer or another system.

It should trace to:

- case identity;
- evidence/finding references;
- the current decision;
- explicit limitations.

A human report may simplify wording. It must not increase authority.

## 8. Evidence states are not one generic “bad” state

Useful states include:

- accepted;
- missing;
- inaccessible;
- expired;
- stale;
- malformed;
- invalid;
- conflicting;
- ambiguous;
- unsupported;
- rejected;
- superseded;
- partially preserved;
- not applicable;
- not independently corroborated.

These states have different consequences.

### Missing

The expected item was not available or not found.

### Inaccessible

The item may exist, but the used method or authorization could not retrieve it.

### Expired

The item existed but retention removed it.

### Invalid or malformed

The item was retrieved but does not satisfy required structure or integrity.

### Conflicting

Material sources disagree.

### Superseded

A later record replaces the authority of an earlier record while preserving history.

### Not applicable

The responsibility does not apply to this case. This is not missing evidence.

## 9. Source authority is question-specific

A source can be authoritative for one question and weak for another.

| Source | Strong for | Not sufficient for |
|---|---|---|
| GitHub PR metadata | repository, refs, lifecycle, changed files | compatibility or safety |
| Target manifest | declared constraints and groups at a revision | actual runtime environment |
| Lockfile | resolved dependency records for that lock | deployed behavior outside that lock |
| Upstream changelog | attributed upstream change claims | target impact |
| Tagged source | exact implementation at that tag | target selection of that version |
| PyPI metadata | distribution identity, hashes, Python floor | benign behavior |
| Advisory | affected/patched range and attack conditions | target exploitability |
| CI status | result of an exact configured execution | all repository behavior |
| Maintainer merge | historical user action | correctness proof |
| Model output | attributed interpretation candidate | authority assignment or truth |

## 10. Negative evidence and absence claims

An unsuccessful code search can support:

> No direct call was observed in the bounded searched path.

It cannot support:

> The repository never reaches this behavior.

Absence claims require scope:

- searched revision;
- searched paths;
- query or method;
- dynamic versus static boundary;
- hidden/generated/plugin paths;
- confidence and alternatives.

S001 correctly distinguishes no observed direct selector call from proof of complete non-exposure.

## 11. Supersession and correction

S001 originally recorded the advisory date as July 9 and inferred a strong security trigger. Fresh official-source verification established June 1 and weakened the trigger inference.

The correct behavior was:

```text
preserve original statement as superseded
→ add corrected evidence
→ update interpretation and finding
→ test whether decision changes
→ retain correction history
```

The decision did not change because its main support did not require proving the exact Dependabot trigger.

## 12. Backward trace exercise

Trace this S002 report idea:

> Public CI was green, but it did not run the decision-relevant Python tests.

Expected trace:

```text
human or machine report statement
→ decision reason dr-003
→ finding F6
→ CI-authority interpretation C07
→ evidence E14–E18
→ workflow/Docker/run raw captures
→ operation op-006
→ frozen head 391508...
```

The exact IDs may differ by representation, but every logical link must be resolvable.

## 13. Failure modes

### Source claim becomes truth

“Upstream says fixed” is treated as proof of target safety.

Correction: preserve it as an attributed claim, then evaluate target path and authority.

### Evidence state disappears

An empty API response is represented as “no workflow.”

Correction: preserve method and inaccessible/empty-result semantics without over-interpreting.

### Interpretation hides its actor

A human or model inference is written as a raw fact.

Correction: identify transformation actor, method, alternatives, and limitations.

### Finding exceeds scope

A bounded static search becomes a global absence claim.

Correction: keep repository revision, path, and dynamic limits explicit.

### Report upgrades certainty

A human renderer uses “safe” or “compatible” when the structured decision says only targeted checks.

Correction: reports must not exceed decision authority.

## 14. Read and inspect

- `RUNTIME_ARTIFACT_SPECIFICATION.md` sections on evidence, claims, findings, and reports;
- S002 `EVIDENCE_ITEMS.jsonl`;
- S002 `CLAIMS_AND_INTERPRETATIONS.jsonl`;
- S002 `FINDINGS.json` and `DECISION.json`;
- S001 correction and advisory captures.

## 15. Ownership checkpoint

Explain and demonstrate:

1. Why is an accepted evidence item not truth?
2. What is the difference between an attributed claim and an interpretation?
3. Give one source that has strong mechanical authority but weak semantic authority.
4. Distinguish missing, inaccessible, expired, and not applicable.
5. Trace one S001 or S002 decision reason backward to raw evidence.
6. Rewrite one overconfident absence claim into a bounded statement.
7. Explain why a maintainer merge cannot close an evidence gap.

## 16. Current demonstrated depth

S001 and S002 demonstrate the practical need for lineage and explicit evidence states. Reliability of automated transformation, conflict adjudication, large-scale provenance, and Ali-independent tracing remain unproven.
