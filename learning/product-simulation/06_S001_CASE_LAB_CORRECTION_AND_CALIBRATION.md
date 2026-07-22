# 06 — S001 Case Lab: Correction and Calibration

**Depth target:** Implementation-adjacent understanding using a real case.  
**Case:** `pydantic/pydantic#13432` — Soup Sieve `2.6` → `2.8.4`.  
**Current outcome:** Merge after normal maintainer review.  
**Execution mode:** Complete retrospective artifact reconstruction.

## 1. Why S001 is educational

S001 looks simple from the pull-request surface:

```text
one lockfile record changed
+ CI green
→ probably merge
```

The justified result required joining:

- exact lockfile change;
- dependency path;
- target use;
- target and upstream Python support;
- official advisory affected and corrected ranges;
- target relevance of the advisory conditions;
- package artifact identity;
- exact-head CI responsibility;
- unresolved trigger and publication evidence;
- correction and supersession history.

## 2. Exact case boundary

The investigation freezes:

- repository: `pydantic/pydantic`;
- PR: `#13432`;
- base SHA: `652a61ce4f9d7d76eaada31535807a485ece0e21`;
- head SHA: `aa2dc024d33f61cdef50bf1973ab5adf0a974f5a`;
- dependency: `soupsieve`;
- transition: `2.6` → `2.8.4`;
- changed shape: lockfile-only;
- historical decision boundary: proposed head before merge.

Later evidence must be tied to an authoritative publication or revision boundary before it is used for the historical decision.

## 3. Dependency-path reasoning

Soup Sieve was not a declared Pydantic runtime dependency.

Observed resolved path:

```text
docs dependency group
→ mkdocs-llmstxt
→ beautifulsoup4
→ soupsieve
```

This changes the question from:

> Does Pydantic application runtime use Soup Sieve?

To:

> Does the documentation toolchain install and exercise the changed dependency path, and do upstream changes conflict with that path?

The lesson is that `direct` versus `transitive` is not enough. Role, selected group, function, and execution path matter.

## 4. Target-use reasoning

The target documentation hook used Beautiful Soup for HTML parsing and tree traversal.

No direct bounded call to the advisory-named selector interfaces was observed in the inspected path.

Correct conclusion:

> Direct use of the named interfaces was not observed in the bounded path.

Incorrect conclusion:

> The repository cannot reach the affected behavior.

Indirect library behavior, plugins, generated paths, and private inputs were not exhaustively established.

## 5. Compatibility reasoning

The update crossed a Python support change:

- Soup Sieve 2.6: Python `>=3.8`;
- Soup Sieve 2.8.4: Python `>=3.9`;
- Pydantic target: Python `>=3.10`.

The new upstream floor is inside the target's declared support boundary.

This resolves the specific interpreter-floor question. It does not prove every form of compatibility.

## 6. Advisory authority and target relevance

Official advisory evidence established:

- the older version belonged to the affected range;
- the proposed version belonged to the corrected range;
- the reported conditions involved untrusted selector processing.

The update therefore had a real remediation benefit.

These statements remain distinct:

```text
old version is in an affected range
≠ the target exposes the reported condition
≠ the new version proves complete target safety
```

The target-specific relevance question remained bounded and incomplete.

## 7. Package identity

Official registry metadata aligned with the proposed locked distribution identities and hashes.

This supports:

> The proposed lock artifacts correspond to the official Soup Sieve 2.8.4 release.

It does not establish the complete behavior of that package in the target.

Artifact identity is integrity and provenance evidence, not behavior proof.

## 8. CI-authority reasoning

The exact-head documentation job:

- used the target head;
- installed the docs dependency group;
- loaded the documentation plugins;
- ran the MkDocs build;
- completed successfully.

This job exercised the owning dependency path more directly than a generic green badge would reveal.

The secret-bearing post-merge publication path was not reproduced, and later retrieval did not expose its result. That limitation did not negate the relevant pre-merge docs-build evidence.

## 9. Factual correction

The original case recorded:

- advisory date: July 9, 2026;
- timing: one day before the PR;
- inference: strongly security-triggered Dependabot update.

Fresh official verification corrected this to:

- advisory date: June 1, 2026;
- timing: more than one month before the PR;
- trigger: security motivation plausible but unresolved.

The correct update process was:

```text
preserve old statement as superseded
→ preserve new official evidence
→ update interpretation and finding
→ test downstream decision effect
```

## 10. Why the decision did not change

The recommendation did not require proving the exact Dependabot trigger.

Stable decision support remained:

- bounded lockfile-only scope;
- transitive docs-tooling role;
- compatible Python floor;
- advisory remediation;
- official artifact alignment;
- relevant exact-head docs build;
- no material contradictory target evidence;
- explicit target-relevance and publication limitations.

The correction changed factual accuracy and certainty calibration, not the bounded action.

## 11. Decision sufficiency

### Why not a stronger conclusion

- complete target relevance and production publication were not established;
- automatic merge is outside UpgradePilot's boundary.

### Why not run another targeted docs check

- the exact-head job already installed and exercised the relevant path;
- a duplicate equivalent check would add little decision value.

### Why not block

- the update removed a version in the affected range;
- no target support conflict was found;
- relevant CI passed.

## 12. Baseline comparison

The baseline saw:

- minor version category;
- passing CI;
- transitive relationship;
- no exact literal caution-keyword match.

It also selected `merge_after_normal_review`.

The full investigation added:

- actual docs dependency path;
- Python-floor relevance;
- advisory remediation and conditions;
- bounded target-use analysis;
- official artifact identity;
- exact CI authority;
- corrected trigger uncertainty;
- report and follow-up limitations.

Same action did not mean equivalent decision support.

## 13. Retrospective honesty boundary

The artifact bundle was reconstructed after the original investigation.

It does not claim recovery of:

- complete original search ordering;
- exact candidate rejection notes;
- every raw connector response;
- original per-operation timestamps;
- local target execution;
- original prospective artifact checkpoints.

## 14. Source walk

Read in this order:

1. S001 `README.md`;
2. S001 `CASE.md` sections on correction, dependency path, target use, advisories, CI, and decision;
3. `RUN_MANIFEST.json`;
4. `EVIDENCE_ITEMS.jsonl` and `CLAIMS_AND_INTERPRETATIONS.jsonl`;
5. `FINDINGS.json`;
6. `BASELINE_RESULT.json`;
7. `DECISION.json`;
8. `HUMAN_REPORT.md`;
9. `FOLLOW_UP_STATE.json`;
10. `REVIEW_AND_OWNERSHIP.json`.

## 15. Lab tasks

### Task A — reconstruct the dependency path

Using only target manifest and lock evidence, write the exact path and explain the role of each node.

### Task B — bound the absence claim

Write two sentences:

- the strongest claim supported by the static target-use inspection;
- one stronger claim that is not supported.

### Task C — decision trace

Trace the CI decision reason backward through finding, interpretation, evidence, operation, and raw workflow capture.

### Task D — correction impact

List every artifact class that should change after the advisory-date correction and every class that may remain unchanged.

### Task E — alternative evidence

State what new evidence would justify changing the decision to:

- run targeted checks;
- investigate or block;
- defer or abstain.

## 16. Ownership checkpoint

Explain without reading the human report:

1. Why was Soup Sieve in the target repository?
2. Why did the Python support change not block the update?
3. What did the advisory establish, and what did it not establish?
4. What did the target-use inspection establish?
5. Why was the docs CI relevant?
6. Why did the factual correction not change the action?
7. Why was another targeted docs check disproportionate?
8. Which parts of this case remain unconfirmed?

## 17. Current demonstrated depth

S001 demonstrates correction, bounded advisory reasoning, dependency-path analysis, and relevant passing-CI interpretation. It does not demonstrate complete target-condition analysis, prospective execution, independent dynamic confirmation, or Ali-owned technical execution.
