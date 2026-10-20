# Capability Evidence and Integration Matrix

**Recorded:** 2026-10-20  
**Branch:** `research/ai-native-career-capability-strategy-2026-10-20`  
**Status:** Branch research matrix; non-controlling.  
**Purpose:** Condense the horizon, evidence audit, integration design and target-role strategy into one decision surface for later reconciliation with `main`.

## Interpretation

`Current evidence` describes what the repository currently supports at the branch-research horizon; it is not a mastery claim.

`Likely surface` indicates where a capability should live **if later admitted**. It is not implementation authorization.

`Disposition` is provisional until final reconciliation with then-current `main`.

| Capability | Current evidence | Main gap | Product fit now | Likely surface if retained | Next discriminating proof | Priority | Provisional disposition |
|---|---|---|---|---|---|---|---|
| Evidence/provenance architecture | Strong product foundation: exact target/revision, native owners, unresolved/unsupported states, Workspace/lifecycle | Ali ownership; concise reviewer trace; external usefulness | Strong | existing product/report + learning/portfolio projection | explain/trace one source→claim→decision path and limits on a fresh case | Highest | **Strengthen proof; no new generic framework** |
| Evaluation/empirical method | Strong experiment history: baselines, frozen evidence, negative results, cost accounting | protected/unseen qualification; concise public case; Ali protocol ownership | Strong | experiments/evidence + compact case study | reconstruct one failed method fairly, with denominator/exposure/causal limits | Highest | **Signature capability** |
| AI/agent security | Strong policy/trust rules; little attack/containment proof | threat model, adversarial fixtures, capability misuse/evidence poisoning proof | Strong natural fit | security owner + adversarial fixtures/tests/experiment | 3–5 real attack families with fixed invariants and observable containment | Highest | **Design/admit bounded security programme later** |
| Reliability/recovery | Substantial Workspace/SQLite checkpoint implementation + accepted recovery architecture | full current integration/interrupt-recovery demonstration; Ali diagnosis | Strong | existing Workspace/product tests + case study | kill/interruption→restore→safe/unsafe continuation proof on current path | Highest | **Finish/qualify existing responsibility** |
| Ali-owned capability | Explicitly incomplete; LbD tracks D/E gaps | durable compact proof across explanation/modification/diagnosis/transfer/defense | Cross-cutting, not runtime | likely `learning/` + portfolio references | capability matrix linked to exact exercises; no auto-promotion | Highest | **Add minimal learning evidence mechanism** |
| Linux/OS fundamentals | Real exposure through WSL, local models, processes/resources | independent diagnosis/command fluency | Not a product feature | learning/incidents + separate labs | diagnose process/resource/filesystem faults before AI diagnosis | Highest learning | **Practise separately using real incidents** |
| Networking/HTTP fundamentals | Real GitHub/provider/proxy evidence | independent DNS/TCP/TLS/HTTP/proxy/rate-limit diagnosis | Not a product feature except client correctness | learning/incidents; product tests where behavior matters | diagnose transport vs auth vs source absence on controlled cases | Highest learning | **Practise separately + apply to clients** |
| Python/software fundamentals | Large Python codebase but heavy AI implementation | independent code reading, debugging, design/change fluency | Foundational | learning + real bounded product changes | predict/change/debug central paths with AI used as leverage | Highest learning | **Continuous ownership track** |
| SQL/database depth | Meaningful SQLite schema/transactions/locking/backup implementation | Ali reasoning/query-plan/migration depth | Strong existing fit | current Workspace + learning | explain/modify transaction/schema/query behavior; failure drill | High | **Deepen SQLite; defer PostgreSQL** |
| Testing/verification | Broad deterministic and experiment tests | Ali test selection/diagnosis; advanced techniques only where needed | Strong | existing tests + learning | choose correct layer for unseen failure; property/fuzz pilot if justified | High | **Strengthen ownership, selectively expand technique** |
| External maintainer/user validation | Major missing evidence class | independent usefulness/usability and misleading-claim feedback | Essential product/career proof, not runtime | external trial + retained feedback | independent clean-use + maintainer report review | Highest when stable | **Plan after stable useful slice** |
| Reviewer-first presentation | README improved but internal repository remains deep | 1/3/10-minute product/career legibility | Strong portfolio/product communication fit | README/demo/case studies; thin explorer only if useful | unfamiliar reviewer comprehension test | Very high | **Build after claim stabilization** |
| Observability/operational diagnosis | Rich experiment accounting; Workspace lifecycle state; no coherent product trace surface | fast operator diagnosis across sources/model/tools/revisions | Conditional but natural | diagnostic projection reusing lifecycle/native owners | answer concrete operator questions from structured trace | Medium-high | **Baseline projection before OpenTelemetry** |
| DevOps/release maturity | Manual hosted verification; clean install; pinned Actions; version 0.0.0 | real release contract, independent install, deployment/runbook | Strong later maturity fit | packaging/CI/release/operations | tagged reproducible release and outsider install/use | Medium-high | **Strengthen before portfolio launch** |
| Docker/container skills | Not current product architecture | practical packaging/isolation/deploy experience | Conditional | deployment lab or product service when justified | package a real supported service/model boundary and operate it | Medium | **Learn when boundary exists; no container theater** |
| Backend HTTP/API | CLI-first; no product service | request/response/API/async-job/idempotency experience | Not yet established product need | separate lab first; later product if real remote/background need | build/operate bounded API exercise; identify product trigger | High career / low product now | **Separate practice, conditional adoption** |
| Application security | Secure defaults/boundaries present, not broad AppSec proof | web/input/URL/path/secret/threat-model practice | Natural where surfaces exist | product security tests + separate labs/CTFs | threat model + bounded tests on actual acquisition/storage/API surfaces | High career / medium product | **Grow selectively** |
| Agent orchestration | Meaningful LangGraph/agent experiments with negative semantic results | no evidence another agent improves current responsibility | Conditional | experiments only until earned | baseline vs smallest bounded agent/validator only after named gap | Hold | **Do not add multi-agent product architecture now** |
| Performance/cost | Measured LLM tokens/time/operations; bounded resource gates | user-level product profiles/regression after path stabilizes | Natural cross-cutting | eval + diagnostics | quality/cost/latency frontier tied to real outcome | Medium | **Fold into eval/observability** |
| RAG/retrieval/vector DB | Some context/navigation research; no measured vector-retrieval need | role-specific exposure, not product necessity | Weak now | separate learning; experiment only after retrieval bottleneck | compare lexical/structural baseline before embeddings | Low/conditional | **Defer in product** |
| Cloud | Little production cloud evidence | deployment/IAM/network/secrets/ops depth | Conditional later | one deployment lab/path | deploy supported artifact securely and operate it | Medium later | **One cloud later, not multi-cloud** |
| Kubernetes | No product need | résumé/infra exposure only | Weak | separate later lab if needed | real scheduling/resource/probe/network need | Low | **Defer** |
| Distributed workers/queues | No demonstrated scale/concurrency need | practical distributed-systems experience | Weak now | separate learning or later product if jobs require | local concurrency/background-job baseline fails a real need | Low/conditional | **Defer product adoption** |
| Frontend/full stack | No core requirement | visual product/reviewer interaction | Conditional | thin report explorer if evidence navigation needs it | user/reviewer benefit over CLI/static report | Low/conditional | **No large frontend; thin UI only if useful** |
| Property/formal-style verification | Strong invariants in Workspace/provenance | no targeted state-space proof yet | Good advanced fit when justified | product tests/experiment | identify invariant where example tests leave material risk; state-machine/property test | Medium later | **Promising focused technique** |
| Learned ML/ranking/calibration | insufficient dataset/product need | data volume/labels/baselines | Weak now | later experiment only | adequate dataset + transparent baseline + holdout | Low | **Defer** |
| Open-source collaboration | mostly solo/internal project | team/review/upstream interaction evidence | External/professional, not runtime | genuine OSS issue/PR/review | meaningful external contribution arising from real work | High career | **Act when natural opportunity appears** |

## Summary by action

### Strengthen what already exists

- evidence/provenance;
- evaluation;
- reliability/recovery;
- SQLite/database reasoning;
- testing;
- measurable performance/cost.

The main work here is **qualification, personal ownership and presentation**, not replacing implementations with more fashionable stacks.

### Add genuinely missing evidence classes

- AI/agent security threat/attack evidence;
- external maintainer/user validation;
- structured operational diagnosis where current evidence is too expensive to interpret;
- reviewer-first proof surface;
- compact Ali-owned capability evidence.

### Practise outside product architecture

- Python fluency;
- SQL depth beyond existing implementation;
- Linux/OS;
- networking/HTTP;
- backend/API fundamentals;
- security labs;
- Docker/cloud fundamentals as they become useful.

### Resist until a trigger exists

- multi-agent product topology;
- PostgreSQL migration;
- vector database/RAG product infrastructure;
- queues/distributed workers;
- Kubernetes/multi-cloud;
- large frontend;
- learned ranking/calibration.

## Integration rule

At final branch closure, every retained row must be reclassified against current `main` as:

```text
merge/adapt
reference-only
defer
superseded
discard
```

No capability enters `main` merely because it is high priority for employment. The correct test is whether the proposed artifact/change belongs to its real owner and has a justified proof path.
