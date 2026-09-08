# Run records, evidence preservation, replay and recovery

**Recorded:** 2026-09-08

**Status:** Exploratory proposal, version 0.1; no storage technology or implementation is admitted by this document.

**Authority:** Non-controlling. Product semantics, architecture decisions, execution plans and live project selection remain with their existing owners.

**Requested outcome:** Explain the implemented system's retention gaps and propose a practical route to durable, inspectable runs, appropriate database use, deterministic replay and recoverable execution.

## 1. Decision summary

UpgradePilot now has useful evidence and reasoning objects but no normal product run store. The CLI prints a subset of the application result; provider responses, intermediate composition inputs and model-call details are not comprehensively retained. Historical simulations, experiment traces and temporary JSON files provide useful precedents, not a product persistence contract.

**Recommendation:** Admit a bounded saved-run responsibility when its interface can be reconciled with the ongoing application/CLI integration. Start with versioned result export and inspectable evidence capture; select an explicit replay boundary next. Add SQLite when cross-run queries or transactional lifecycle management are part of the admitted outcome. Introduce execution recovery only after repeatable units, failure boundaries and fresh authority are designed. A database alone supplies none of those semantic guarantees.

File bundles are the preferred first baseline for inspecting and sharing individual runs. SQLite is a credible alternative from the start if the first requirement includes searching and updating a run history. Neither a server database nor a durable workflow framework is justified merely by the word persistence.

The four capabilities may be delivered independently:

| Capability | User question answered | Minimum promise | Does not imply |
|---|---|---|---|
| Report/result export | What did this investigation conclude or leave unresolved? | Reopen a versioned result and readable explanation tied to exact inputs | Original response capture, deterministic recomputation or resume |
| Evidence preservation | What did the system actually observe and use? | Retain selected source content, acquisition context, transformations and failures | Freshness now, source authenticity from a hash alone, or replay completeness |
| Deterministic replay | Can we recompute a named boundary from recorded inputs? | Offline reproduction of specified deterministic outputs with compatible methods/contracts | A repeated model call, fresh external truth, or resuming interrupted work |
| Execution recovery | Can interrupted work continue without corrupting state or silently repeating effects? | Restart from a valid durable boundary with explicit attempt and authority semantics | Exactly-once external effects, automatic recovery across every version, or framework adoption |

This proposal's completion means those responsibilities, dependencies, alternatives and proof gates are concrete. It does not mean any has been implemented or validated.

## 2. Source-grounded system assessment

**Inspection snapshot:** synchronized `410e106d6a649712ff733e7e083a791eb82a1a17`. This is a dated assessment; [MEMORY.md](../MEMORY.md) alone owns continuation. The review traced the main caller, provider and interpretation boundaries, returned result, presentation consumer, experiment replay and existing plans. It is not a claim of exhaustive review of every parser or passing runtime tests.

| Boundary / owner | What the inspected implementation supplies | Retention gap and consequence |
|---|---|---|
| [CLI](../src/upgradepilot/cli.py), [package entry](../src/upgradepilot/__main__.py) | Input parsing, selected error exits and printed evidence | No run ID, save option, external result schema or file lifecycle; exit 0 can contain unresolved/unsupported evidence |
| [Application](../src/upgradepilot/investigation.py) | `PublicPullRequestInvestigation`, independent CI/package/upstream branches, Python-support results, artifact candidate and target-environment associations | In-memory result only; it is rich but not a full acquisition/operation transcript |
| [GitHub transport](../src/upgradepilot/github/api.py), [PR](../src/upgradepilot/github/pull_request.py), [repository files](../src/upgradepilot/github/repository.py), [CI](../src/upgradepilot/github/actions.py) | Parsed identity, exact-revision text and typed source problems/run observations | HTTP bodies/attempt context are not durably captured; a valid `RepositoryTextFile` alone is not proof of an actual acquisition |
| [PyPI transport](../src/upgradepilot/pypi/api.py), [releases](../src/upgradepilot/pypi/release.py), [provenance](../src/upgradepilot/pypi/provenance.py) | Exact package/release identity, artifact metadata, some retrieval times and source problems | Normalized inventory is not the original response or package binary; do not infer uniform timestamps where producers supply none |
| [Dependency analysis](../src/upgradepilot/dependency/analysis.py), [CI reasoning](../src/upgradepilot/ci/dependency_exercise.py), [target environment](../src/upgradepilot/target/artifact_environment.py) | Source contexts, static consumption and target facts with explicit proof limits | Some acquired workflow definitions and environment sources remain local composition inputs, not complete fields in the final result |
| [Support-drop bridge](../src/upgradepilot/upstream/support_drop.py), [model boundary](../src/upgradepilot/upstream/support_drop_extractor.py), [grounding](../src/upgradepilot/upstream/claim.py) | Bounded source window, model request, candidate extraction and deterministic validation | Final grounded output does not preserve every request/response, rejected candidate, timing or method invocation detail |
| [Python-support](../src/upgradepilot/impact/python_support.py), [artifact serviceability](../src/upgradepilot/impact/artifact_serviceability.py) | Mechanism-specific candidates/applicability | Storage must preserve these meanings; serializing a static target environment must not promote it into exact wheel compatibility |
| [Experiment transition replay](../experiments/evidence_gap_investigation_transition.py) | Recomputes one transition from a typed trace without model/GitHub I/O | Experiment-only proof; no product save/load contract or process recovery follows |
| [Real LangGraph smoke](../experiments/real_pydantic_python_support_langgraph_evidence_gap_smoke.py) | Writes diagnostic JSON to a fixed temporary file using `default=str` | Useful human diagnosis, but replacement/temporary lifetime and lossy generic encoding are not a durable product store |
| [Development evaluation](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md), [simulation](../product-simulation/README.md), working memory | Curated preserved evidence, labels and engineering history | Not automatic product capture; historical/development exposure remains explicit |

The absence of storage is partly deliberate sequencing and partly unfinished product capability. The [delivery route](../plans/UPGRADEPILOT_90_DAY_PLAN.md) separately owns acquisition/replay robustness and justified storage/diagnosis. The [vertical-slice plan](../plans/B2_PUBLIC_PR_VERTICAL_SLICE_PLAN.md) requires controlled evidence but does not claim a persistence platform. The [charter](../PROJECT_CHARTER.md) allows one main persistence system when justified and expects persisted/replayable runs when that responsibility activates.

Those controls do not establish that basic export is technically difficult or that all capture must await a database. The new diagnosis/evaluation needs justify considering a bounded earlier admission through the normal owners.

## 3. Fit with parallel implementation

At the inspected snapshot, [artifact integration](../plans/ARTIFACT_SERVICEABILITY_PUBLIC_INVESTIGATION_INTEGRATION_PLAN.md) has source-level candidate and target-environment composition; its executable proof remains recorded as deferred, and human-facing output remains a later step. This proposal must not be used to close that proof debt.

The new association between dependency source and exact workflow-derived target result must survive storage. Static configuration is not execution; unknown exact compatibility remains unresolved. Storage must also distinguish inactive analysis, no candidate and provider/interpretation problems rather than treating every `None` or empty tuple as the same semantic state.

Parallel preparation can define formats, examples, failure cases and database questions now. Product edits should follow one coordinated result/CLI boundary review once the integration's actual contract is ready. Do not independently redesign `PublicPullRequestInvestigation`, add competing CLI flags, or import experiment graph/trace types into product runtime. No implementation plan or live-state change is made by this proposal.

## 4. Concrete user value and priority

| Outcome | Value to investigate | Priority / feasibility | Main dependency |
|---|---|---|---|
| Reopen a completed or gapped report | Avoid losing the result when the terminal closes; share a public-safe review artifact | First; bounded extension | Versioned projection and reliable file writing |
| Diagnose a failed or surprising run | Inspect exact observations rather than reacquiring changing evidence | First alongside bounded capture; integration work | Acquisition/method capture before data is discarded |
| Compare reports for the same PR | Explain evidence, revision or method differences | After stable identities; moderate integration | New attempt/result lineage and structured difference semantics |
| Re-evaluate deterministic reasoning offline | Isolate code changes from provider/model variation | High evaluation value; replay-boundary work | Complete inputs at the selected boundary and version-aware loader |
| Search history using SQL | Find unresolved cases, repeated failures and evidence reuse | Conditional; SQLite is credible | Actual query set, schema and measured corpus shape |
| Resume interrupted acquisition/investigation | Reduce lost work and repeat costs | Later; highest semantic/coordination risk | Durable steps, incomplete-attempt classification and reauthorization |
| Learned ranking/training from runs | Potential applied-ML value | Research-dependent | Independent labels, selection bias and outcome/cost completeness; traces alone are not training labels |

No measured user benefit, artifact volume, retention duration, performance target or calendar estimate is asserted here. Use structural effort classes until the first capture reveals actual costs.

## 5. Information contract and formats

These are logical responsibilities, not frozen table names or a schema that mirrors dataclasses:

| Record | Minimum information when available | Important boundary |
|---|---|---|
| Run / attempt manifest | Unique attempt ID, requested locator, exact resolved revisions, code/config identity, start/end, completion/failure state and capture coverage | A request is not an attempt; repeat runs and changed heads must not overwrite history |
| Source observation | Provider, exact request/resource identity, time, relevant status, content reference/hash and capture policy | Retain successful, absent, inaccessible and malformed outcomes distinctly; avoid headers containing credentials |
| Evidence content | Bounded stored bytes/text and encoding/media type, length and hash | A hash proves byte correspondence, not acquisition, freshness or trust |
| Normalized evidence | Versioned producer result plus origin references and method identity | Preserve producer timestamps and source revisions separately from run times |
| Interpretation invocation | Input references, method/code/prompt/config identity; model identity and relevant request/response when used; outcome/rejection detail | Model output remains a proposal/interpretation, not action authority or validated truth |
| Findings / application result | Supported mechanism results, associations, problems, limits and evidence references | No fabricated overall recommendation or missing-state reason |
| Operation/attempt events, if needed | Stable operation/attempt identity, start/completion/failure, bounded timing and source/result references | An event log is diagnosis material; it does not automatically become a durable job scheduler |
| Human report | Rendering/version and references to its structured source | Derived presentation, not an independently edited authoritative finding |

**Formats:** JSON for versioned structured records; Markdown for human review; source text/JSON bytes in their meaningful captured form. JSONL is appropriate for a bounded append-only diagnostic event stream when required. CSV is useful for analytical exports, not nested evidence authority. SQLite can store structured metadata and/or content once its ownership is selected. Do not use Python pickle to load portable or untrusted run bundles.

Do not use `dataclasses.asdict` plus `default=str` as a production round-trip contract. Explicit encoders/decoders must preserve discriminated variants, versions, times, package/version values and meaningful missing-state distinctions. Unknown schema versions or invalid references must produce a clear load error, not silent coercion.

A proposed first file layout, outside tracked source unless deliberately curated:

```text
<selected local data directory>/<run-id>/
  manifest.json
  result.json
  report.md
  evidence/<content-id>.<format>
  events.jsonl                 # only if the admitted diagnostic scope needs it
```

The exact location/CLI option is an implementation decision. The repository already ignores local `artifacts/`; that does not make every generated run appropriate for Git. Export a reviewed public-safe case deliberately rather than committing all runtime data.

## 6. Capture ownership and sequence

1. At a new outer run boundary, allocate attempt identity and record capture intent before acquisition. Keep invalid input distinct from an investigation that started and failed.
2. At existing provider boundaries, capture the relevant response body/selected safe metadata or typed failure before parsing destroys needed detail. Record pages, retries and repeated observations separately; content deduplication must not erase acquisition occurrences.
3. At normalization/interpretation boundaries, link produced evidence to source content and method version. Reuse captured workflow/source content across CI and artifact branches; preserve each distinct use relationship.
4. At the semantic boundary, record enough of the admitted source window, request configuration, returned output and validation outcome for the chosen reproduction promise. Redaction or omitted model data must narrow that promise explicitly.
5. After application return, serialize a deliberate result projection and derive the human report. On failure, finalize an honest partial run if possible; do not fabricate an application result.

Mechanism modules should not each acquire their own file/database writer. A narrow run recorder composed at acquisition/application boundaries is a candidate, not an instruction to build a universal event bus or observer framework. The first export can be implemented without all capture, but must say which guarantee it supplies.

For opt-in saving, failure to create the destination should be detected before expensive work. A mid-run write failure should make saving visibly fail and prevent a durable-completion claim. If ordinary console output remains available, preserve it while returning an interface status that exposes the save failure; the exact exit contract belongs with CLI design. Never silently downgrade requested capture into a supposedly complete saved run.

## 7. Files versus databases

| Approach | Strength for this project | Cost / limit | Admission trigger |
|---|---|---|---|
| Independent JSON/Markdown bundles | Inspectable, portable, easy to compare one run and feed manual evaluation | Searching/updating many bundles, references and crash-safe publication need deliberate handling | First need is inspect/reopen/export individual runs |
| SQLite as authoritative local run store | Transactions, constraints and SQL across related runs/evidence without a separate database service | Schema/migrations, backup, write contention and content-retention design | Cross-run queries or transactional run lifecycle are part of the first required outcome |
| File bundles plus rebuildable SQLite index | Preserve portable evidence while accelerating queries | Two representations; indexing/orphan/rebuild policy required | File scanning is demonstrably inadequate; database is explicitly derived |
| SQLite metadata plus external content blobs | Query metadata without forcing all payloads into tables | Cross-filesystem/database commit and cleanup/recovery complexity | Representative content sizes justify the split |
| Server relational database | Centralized access and more concurrent writers across workers | Deployment, authentication, backup and operational burden | A real shared-service workload outgrows the local design |
| Graph/vector database | Specialized relationship/retrieval queries | Additional system and evidence-authority complexity | A demonstrated query/retrieval limitation; graph-shaped findings alone are insufficient |

SQLite's official guidance identifies local application storage as a good fit and recommends client/server storage for direct multi-machine access or many simultaneous writers. SQLite is not simply a toy stage before a server database. [Appropriate uses](https://www.sqlite.org/whentouse.html)

**Proposed choice:** file bundles for the first inspectable-run slice unless the admitted first task includes relational history queries. In that case compare a small SQLite design directly; do not require a throwaway filesystem implementation. Select one canonical owner per datum. A report/export is derived; a rebuildable index is not a second writable truth store. Avoid introducing an ORM, repository abstraction hierarchy or generic multi-backend support before a real storage requirement exists.

Candidate SQL questions to validate before database admission: list runs for one PR/revision; find unresolved artifact findings with their source failures; distinguish repeated attempts from changed-input analyses; retrieve evidence used by a finding; compare method-version outcomes on identical captured inputs. Do not design dozens of tables before these queries can be exercised on representative records.

## 8. Replay contracts must name their boundary

| Mode | Inputs required | What can be claimed |
|---|---|---|
| Re-render | Saved result plus compatible renderer | Reopened explanation of that result; formatting may differ by renderer version |
| Deterministic reasoning replay | Complete normalized/source inputs and recorded semantic outputs at an explicit boundary, compatible code/config | Recomputed domain outcomes without network/model calls; compare defined semantic fields |
| Raw-source parsing replay | Original retained response/source content and compatible parsing/acquisition context | Re-exercise parser/normalizer behavior; missing pages or redacted bodies can prevent equivalence |
| New model evaluation | Frozen source window with a newly invoked model/config | New experiment linked to original run, not deterministic replay |
| Fresh rerun | New external acquisition | New attempt with possibly different evidence; no promise of identical results |

The existing experiment replay proves a narrow state transition and can inform proof design, but its types and `default=str` diagnostic exports are not product serialization precedent. Product replay must refuse incomplete required evidence and unsupported versions, and must never silently fetch a missing source. Tests should make network/model access fail if invoked during replay.

## 9. Recovery, durability and edge cases

Recovery is materially more demanding than export. Before promising it, define the durable step boundary, a new attempt identity, allowed repeat reads and how stored observations re-enter validated domain contracts. A crash after a response arrives but before it is saved leaves an uncertain attempt; repeating a public read can return changed content and must be recorded as a new observation.

A persisted action proposal or old authorization is not fresh execution authority. Resuming any future adopted planner must recheck input revisions, budget, consumed actions and relevant authority before an effect. Do not claim exactly-once external behavior from a SQLite transaction or workflow checkpoint. Product target writes remain outside current scope.

| Failure / variation | Required proposed behavior |
|---|---|
| Interrupted manifest/result write | Never expose a partial result as complete; use a tested staging/finalization protocol |
| Storage full, permissions or inaccessible path | Separate persistence failure from evidence insufficiency; retain a clear attempt outcome where possible |
| Malformed source then process failure | Preserve bounded diagnostic evidence without promoting it to a trusted source result |
| Missing/deleted/corrupt content | Detect and identify missing references; narrow inspection/replay capability rather than reacquire silently |
| Changed PR head or package metadata | Preserve old observation, open a new attempt, distinguish immutable revision from mutable publication data |
| Same payload acquired twice | Content reuse may be possible; keep separate acquisition timestamps/attempt identities |
| Concurrent local writers | Unique run allocation and defined commit boundary; no overwrite of another run or shared latest pointer |
| Schema/code/model version change | Preserve origin version; migrate through explicit supported paths or refuse replay/resume |
| Blob plus database partial commit | Detect orphan/missing references and recover with an explicit protocol; do not assume cross-store atomicity |
| Cancellation or hard kill | If supported, mark cancellation when observable; otherwise recognize incomplete attempt on reopen |

Atomic visibility of a renamed file is not a blanket power-loss durability guarantee. Test the chosen publication protocol on the supported filesystem. If SQLite WAL is selected, backup/restore must respect the database and its associated state; blindly copying only a live database file is not a safe backup design. Use a supported SQLite backup method and exercise restoration. [SQLite WAL](https://www.sqlite.org/wal.html), [backup API](https://www.sqlite.org/backup.html)

## 10. Privacy, retention and evaluation use

Public-source support does not justify saving arbitrary response headers, environment variables, tokens or unrelated local data. Use an allowlist of capture fields; default to bounded material needed by the admitted question. Store untrusted source content as data and safely escape it in any later HTML renderer. Validate imported bundle paths, sizes, hashes and schemas; do not follow path traversal or execute supplied code.

Record whether content was redacted/truncated and which replay promises remain possible. Hash the stored representation unambiguously; do not label redacted bytes an exact raw response. Hashes are not signatures or authentication. Limits on item size, total run size and retention require explicit measured choices before release, not unlimited capture by default.

Retention applies to reports and model prompts/responses as well as source blobs: deleting one copy does not delete duplicated quoted content. Keep references to unavailable evidence honest after deletion, and reconcile deduplication with deletion/refcounts. Operational records stay outside Git by default; curate reviewed evaluation fixtures through their own owner.

Saved runs can help diagnosis and evaluation immediately. They do not automatically supply correct labels, independent cases or useful ranking outcomes. Preserve acquisition/model/code identity, related-case grouping, prior exposure and assistance. Prefer the existing [development evaluation](../experiments/EVIDENCE_REPORT_DEVELOPMENT_EVALUATION.md) for first report checks; an independent benchmark or training corpus requires separate design.

## 11. Proposed implementation admission sequence

| Bounded slice | Entry / scope | Acceptance evidence and stop |
|---|---|---|
| Saved-result export | Reconcile actual application/CLI contract; choose versioned projection and destination semantics | Save/reopen supported and degraded results; identity/types/limits preserved; save failure visible; no claim of full capture/replay |
| Evidence and failure capture | Select the minimum source/method boundaries needed for one diagnostic/replay task | Existing inputs linked to stored content; partial/provider/model failures retained distinctly; limits/redaction tested |
| Deterministic replay | Name one complete input/output boundary and version compatibility | Offline round-trip semantic equivalence plus incomplete/corrupt/version-mismatch contrasts; prohibit fallback network/model calls |
| Queryable history, if justified | Exercise concrete history queries and choose file/SQLite ownership | Correct joins/constraints and repeated-attempt semantics; migration and backup/restore tested; measure query/write cost |
| Recovery, if justified | Durable steps and repeat/authority semantics explicit | Interrupt at chosen boundaries, resume without hidden duplicate/corrupt completion; reject stale authority; no exactly-once claim |

These are dependency-aware candidates, not a replacement live route. A combined file/SQLite first slice can be appropriate when required by the actual user task; do not expand the slice to include every capability. New invariants go to the accepted specification, a consequential storage method to an architecture decision, and admitted execution/proof coordination to one bounded plan. Update live memory only when Ali selects that work.

## 12. Release gates and unresolved decisions

Before advertising a capability, test its exact promise: typed result round trip; provenance and missing-state fidelity; write/read failure classification; partial-run recognition; imported data limits; schema incompatibility; offline replay equivalence; and recovery behavior only if offered. Exercise normal application-to-storage-to-reader composition, not just fabricated serialization fixtures. Measure content volume, storage overhead, selected query latency and save/replay cost on a small disclosed sample without inventing throughput targets.

The first design checkpoint must resolve:

1. Is the first user task individual-run inspection or searchable run history? This chooses the file/SQLite baseline.
2. Which source and semantic inputs must be preserved for the first promised replay boundary? Final-result serialization cannot answer this alone.
3. What is the save-failure/partial-result contract and default capture/retention policy?
4. How does the projection represent the settled artifact integration's inactive/problem/candidate/association states without inferring absent semantics?
5. Which schema versions and code configurations may load, re-render, replay or resume a record?

**Learning value:** this work provides concrete practice in serialization contracts, SQL and data modeling, transactions, migrations, provenance, reproducibility, idempotency and failure recovery. The evidence of learning is explaining/modifying those boundaries and diagnosing a changed case, not adding a database name to the stack.

**Stop:** proposal and source assessment only. No runtime recorder, export flag, database, replay loader, recovery machinery, dependency or simulation change is introduced. Further expansion should follow the first admitted storage task and actual captured evidence.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-repository-audit`.
