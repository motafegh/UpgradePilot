# System limitations and correctness investigation

**Recorded:** 2026-09-08
**Session responsibility:** Separate supporting investigation; planning checkpoint.
**Plan:** [System limitations and correctness investigation](../plans/SYSTEM_LIMITATIONS_AND_CORRECTNESS_INVESTIGATION_PLAN.md).
**Authority:** Dated progression and handoff only; [MEMORY.md](../MEMORY.md) owns canonical project continuation.

## User request and boundary

Ali requested our own investigation process, plan and working memory, with progressive records of discoveries before deciding subsequent work. The immediate instruction was to write the plan first. This authorizes the two artifacts here, not product fixes or expansion. Product integration continues separately; do not replace its plan, live memory, working record or deferred proof obligations.

## Starting evidence and corrections

The preceding chat review traced acquisition, dependency/CI, upstream/model, Target/artifact and CLI boundaries against source and plans at `09d9eaa`, with remote documentation then advancing to `a2876bc`. It identified seed concerns about shell-comment recognition, PR revision correspondence, run-attempt binding, CI branch failure and hidden CLI diagnostics. These were source-traced, not executable reproductions or proven public incidents.

During this planning checkpoint the shared checkout advanced to `9fe57f721afe3ab8ea6fdc050124d8ce0c2610e1`, matching origin at inspection. Compared with the earlier review, product changes were in `src/upgradepilot/cli.py` and `tests/test_cli.py`; live memory selected cross-responsibility/end-to-end proof after the human-facing explanation cycle.

**Correction:** “artifact output missing” is no longer an accurate implementation finding at that snapshot. The CLI now has artifact, Target-environment and applicability rendering. Its new behavior still needs the main task's recorded executable proof. Other intermediate diagnostic omissions remain questions for fresh rendering inspection, not a blanket claim that the CLI lacks explanation.

The recorded user constraint still defers executable proof. No product tests, live acquisition, model invocation or hosted workflow was run in this planning checkpoint. Tool access alone does not close that debt.

## Seed register — revalidate before concluding

| Question | Starting evidence | Disposition at this checkpoint |
|---|---|---|
| Shell comments/quoted data become install evidence | `dependency/direct_install.py` scans segments for requirement flags; CI consumes observed declarations | Source-traced hypothesis; controlled positive/negative and composition checks pending |
| PR patch/revision mismatch | PR identity and mutable files endpoint are separate reads; source contexts use the initial head | Snapshot-consistency hypothesis; stable/changed-head sequence needed |
| Workflow attempt mismatch | Run stores attempt, jobs request `latest` | Attempt-binding hypothesis; stable/rerun sequence needed |
| CI errors stop independent branches | Actions calls precede package acquisition; exceptions reach CLI | Source-traced degradation behavior; classify prerequisite versus independent failure |
| Diagnostic detail lost in CLI | Returned index/tag/changelog outcomes are richer than earlier renderer | Refresh against changed CLI; artifact-output absence superseded |
| Deliberate coverage limits | Static/runtime separation, Target single-job/direct-requirements gate, strict source/semantic bounds | Assess value and real-case pressure; no expansion selected |
| Persistence and evaluation gaps | Existing focused storage proposal and development-only report evaluation | Classify dependencies; do not duplicate their design or claim measured quality |

Source links and discriminating checks are owned by the linked plan and will be made exact for each evaluated snapshot. Earlier source inspection is evidence to test, not authority to keep a finding.

## Planning decisions

Use one bounded investigation plan and one progressively maintained record. Prioritize potential false evidence and identity mixing before wider coverage. Keep source diagnosis separate from executable reproduction, and both separate from prevalence or product acceptance. Reuse real preserved cases with exposure/comparability disclosed; do not create an aggregate “accuracy” from heterogeneous unsupported cases.

The plan sets revision checks, permitted evidence work, coordination boundaries, completion criteria and a decision gate. It deliberately leaves repair designs open until the finding is established. Existing main-task proof should be reused only when it matches the exact proposition and revision.

## Planning validation and learning cycle

Local Markdown targets, fence balance, whitespace and governance doctor all passed. These checks validate the documentation, not the suspected defects or current product behavior. Publication is limited to the two new artifacts; unrelated checkout changes remain with their owners.

A — DONE: explained independent investigation, evidence classifications and parallel-work boundaries.
B — DONE: wrote the position-neutral investigation plan and this record; no diagnostics or fixes implemented.
C — DONE: preserved user scope, seed hypotheses and the material CLI/state correction.
D — explanation supplied with handoff; learner response pending. Ownership question for the investigation: what evidence would distinguish a safe unsupported-command abstention from an incorrect positive CI finding?
E — pending response/continuation; first proposed investigation checkpoint is baseline reconciliation followed by the command-recognition contrast, subject to the applicable execution constraints.

## Time-scoped handoff

At this planning stop, no seed hypothesis has gained executable proof. Resume by reading the then-current main state and source diff, then follow the first investigation checkpoint. Continue this record with evidence, corrections and dispositions at meaningful points. Do not launch the main task's proof campaign, write fixes, or expand Target/CI merely because this plan now exists.

Provenance: `UP-SKILL:upgradepilot-planning-design`; `UP-SKILL:upgradepilot-working-memory`.


## Command-recognition investigation — 2026-09-08

**User continuation:** Ali selected the plan's next step. Planning-only scope progressed to bounded investigation and record maintenance; product fixes remain unselected.

### Baseline and proof-constraint correction

Inspected local `af534cc55e1b3daff121ba6f5209250e9bff389e` and fetched remote `eda20e411e6fb33108d94d8db599e573928f9ddc`. The remote difference was live memory and the main task's [integration proof record](2026-09-08_artifact-serviceability-integration-proof.md), not product source. That record establishes WSL execution and reports the deterministic integration suite green after two harness corrections. This supersedes the earlier executable-proof deferral for our entry decision. It does not prove our new command contrasts.

Used the existing WSL virtual environment (Python 3.12.3) for one offline diagnostic. No broad suite, live acquisition, model call or target command execution occurred. Requests session calls were patched to fail if attempted. Source files and the fixture helper file were SHA-256 checked before/after; all were unchanged during the diagnostic.

### Proposition and ownership trace

The question is whether the source declares installation from the changed requirements file, not whether a declared command actually ran. [ADR-0008](../docs/architecture/ADR-0008-bounded-static-github-actions-workflow-definition.md) preserves that distinction. The earlier [CI proof audit](../audits/2026-08-02_AUDIT-002_ci-dependency-exercise-proof-boundary.md) is indexed as absorbed; this finding does not reopen its old `proven` runtime wording. It concerns incorrect recognition of the static premise itself.

Trace: GitHub workflow parser preserves a YAML block scalar → `bounded_shell_segments` splits command text without shell quote/comment interpretation → `observe_direct_installation_declaration` searches for requirements flags and strips surrounding quotes → CI promotes the observation when checkout/source prerequisites hold → application `_compose_target_artifact_environments` accepts that supported relation → Target reuses the same declaration observer.

The command `pip install wheel # -r requirements-dev.txt` contains the relevant flag only in a Bash comment. The command `echo "note; pip install -r requirements-dev.txt"` contains install-looking text only inside echo's quoted argument. Neither declares the alleged requirements installation, even at static proof strength.

### Reproduced results

All five synthetic workflows declare one local Bash job, current-repository checkout, a matching exact-revision dependency context and synthetic successful run/job metadata. Only the command text changes. Fixture constructors come from `tests/test_ci_dependency_coverage.py`; that test suite is not executed by the diagnostic.

| Command | Direct-install state | CI state | Target associations / installation state |
|---|---|---|---|
| `pip install -r requirements-dev.txt` | observed | supported_not_correlated | 1 / observed |
| `pip install wheel` | not_observed | unresolved | 0 |
| `pip install wheel # -r requirements-dev.txt` | observed — false positive | supported_not_correlated | 1 / observed |
| `echo "pip install -r requirements-dev.txt"` | not_observed | unresolved | 0 |
| `echo "note; pip install -r requirements-dev.txt"` | observed — false positive | supported_not_correlated | 1 / observed |

**Disposition:** confirmed defect within the exercised static declaration → CI → Target composition boundary. High priority for a bounded correction decision because unsupported command text earns positive evidence. No public-case frequency or overall product severity score is inferred from these synthetic inputs.

The existing direct-install tests include ordinary echo rejection, positive separators, dynamic paths and working-directory controls, but those do not discriminate the two failing cases. Their existence or the reported green suite does not invalidate this counterexample.

**Limits:** invoked the real parser, observer, CI evaluator and application Target-composition helper using controlled inputs. This is not a complete normal CLI/provider investigation: the outer artifact-candidate gate was not exercised. A normal run with a real candidate can reach this helper, but the diagnostic does not show a maintainer recommendation or strengthened artifact applicability. Target association remains static evidence, and exact wheel compatibility remains unresolved. Heredocs and other shells were not tested.

**Smallest next disposition:** consider a correction at the command-recognition owner that rejects unsupported text or distinguishes arguments from comments/quoted data; add these contrasts and relevant composition protection when repair is selected. Do not start with a new framework or a general shell interpreter, and do not patch each downstream consumer independently. Repair design remains open. The next independent investigation question is PR patch/revision consistency after this checkpoint is discussed.

### Reproducible diagnostic

The following is the exact script used, preserved here so temporary-file lifetime cannot erase the reproducer. Restore it to a local temporary file and run from the pinned checkout with `PYTHONPATH=src .venv/bin/python -B <script-path>`. It only treats the embedded workflow commands as data. Output includes the inspected source hashes; compare the command-result rows above rather than interpreting them as PASS assertions.

```python
import hashlib, json, pathlib, runpy, subprocess, sys
from unittest.mock import patch
from upgradepilot.github.workflow_definition import parse_workflow_definition, RunStepDefinition
from upgradepilot.dependency.direct_install import observe_direct_installation_declaration
from upgradepilot.ci.dependency_exercise import evaluate_dependency_ci_coverage
from upgradepilot.investigation import _compose_target_artifact_environments

root = pathlib.Path.cwd()
paths = sorted((root / 'src/upgradepilot').rglob('*.py')) + [root / 'tests/test_ci_dependency_coverage.py']
def hashes():
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before = hashes()
helpers = runpy.run_path('tests/test_ci_dependency_coverage.py')
dependency, contexts = helpers['_requirement_dependency']()
cases = {
    'real_requirement': 'pip install -r requirements-dev.txt',
    'unrelated_install': 'pip install wheel',
    'comment_only_requirement': 'pip install wheel # -r requirements-dev.txt',
    'echoed_command': 'echo "pip install -r requirements-dev.txt"',
    'quoted_separator_data': 'echo "note; pip install -r requirements-dev.txt"',
}
results = []
with patch('requests.sessions.Session.request', side_effect=AssertionError('Network prohibited')):
    for name, command in cases.items():
        content = ('name: CI\non: pull_request\njobs:\n  tests:\n    runs-on: ubuntu-latest\n'
                   '    steps:\n      - uses: actions/checkout@v4\n      - shell: bash\n        run: |\n          '
                   + command + '\n')
        workflow_input = helpers['_input'](content)
        definition = parse_workflow_definition(workflow_input.definition)
        step = next(s for s in definition.jobs[0].steps if isinstance(s, RunStepDefinition))
        observed = observe_direct_installation_declaration(step, dependency_source_path='requirements-dev.txt')
        coverage = evaluate_dependency_ci_coverage(dependency, [workflow_input], source_contexts=contexts)
        targets = _compose_target_artifact_environments(coverage, [workflow_input], contexts)
        results.append({'case': name, 'command': command, 'observation': observed.state,
                        'coverage': coverage.state, 'consumptions': [c.state for c in coverage.workflows[0].consumptions],
                        'target_associations': len(targets),
                        'target_installation': [t.target_environment.dependency_installation_declaration for t in targets]})
assert before == hashes(), 'Source changed during diagnostic'
print(json.dumps({'revision': subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
                  'python': sys.version.split()[0], 'interpreter': sys.executable,
                  'source_hashes': before, 'cases': results}, indent=2))
```

Source/fixture hash-map digest (SHA-256 of sorted-key JSON): `9176909f9cf116c4c5bf071463893491b5579afe32a743eeacd6ab79920196b4`.

### Checkpoint learning and handoff

A — DONE: separated static declaration correctness from runtime correlation and refreshed execution eligibility.
B — DONE: one five-case offline diagnostic reproduced two false positives and preserved three controls through relevant composition.
C — DONE: recorded exact inputs, source snapshot, observed states, correction to proof deferral and limits here.
D — explanation supplied; learner response pending. Question: why does `supported_not_correlated` still overstate the evidence for the comment-only flag, even though it explicitly avoids a runtime-success claim?
E — pending response; repair remains unselected. Continue with the next independent question only after discussion or explicit redirection.

Only this investigation record changed. Documentation checks precede publication; they do not add product proof. The other seed questions remain unvalidated by execution in this task.


## PR patch/revision consistency investigation — 2026-09-08

Ali directed continuation to the next independent question. Local and fetched origin were synchronized at `5e1dbec70893f8a6d219202d9559492137291054`; the checkout was clean at entry. Product source hashes were unchanged before/after the diagnostic. Python 3.12.3 in the existing WSL virtual environment was used, with real Requests session calls prohibited. No external requests or target code execution occurred.

### Question, rationale and ownership

Can a mutable PR-files response supply a requirements patch that is assigned to an earlier frozen head? The relevant invariants are SNAP-001 and PROV-001 in the [core contract](../docs/specifications/UPGRADEPILOT_CORE_PIPELINE_AND_CONTRACT_SPECIFICATION.md). Changed-head handling is explicitly staged under acquisition robustness in the [delivery route](../plans/UPGRADEPILOT_90_DAY_PLAN.md); deliberate sequencing does not prove present correspondence.

The earlier [exact-file audit](../audits/2026-08-01_AUDIT-001_exact-pr-file-acquisition-evidence-contract.md) is indexed as absorbed and concerned exact base/head file acquisition, including uv.lock. Its protections cannot be assumed to cover the separate requirements-patch path. This finding does not reject the exact-file acquisition design.

Trace:

1. `GitHubPullRequestClient.get_pull_request` freezes head A.
2. `get_changed_files` requests `/pulls/1/files` by PR number and checks count completeness. It neither re-reads PR identity nor compares response revision references. Parsed `ChangedFile` discards the supplied `contents_url` and blob `sha`.
3. `analyze_dependency_change` passes an admitted requirements patch directly to its extractor. The complete base/head repository-file methods are not called for this path.
4. `_source_contexts` assigns `identity.head_sha` to the accepted dependency source context.
5. The normal application uses those same three operations in sequence. Its later CI acquisition uses the initial PR identity, so the differing requirements evidence has no reconciliation at this join.

GitHub's documented PR-files endpoint has PR-number/pagination parameters rather than a revision selector: [official endpoint documentation](https://docs.github.com/en/rest/pulls/pulls#list-pull-requests-files). This supports the API boundary, not an assertion that a public race was observed.

### Diagnostic and observed results

A fake HTTP session supplies structurally valid PR JSON, then a complete requirements patch. In the changed cases the simulated provider moves from head A to B during the files request; the supplied `contents_url` explicitly names the simulated files head. `sha` is a file blob identity, not a PR head, and must not be compared as though it were a commit SHA. The diagnostic uses the actual GitHub client/parsers and dependency analyzer, not preconstructed trusted dependency results.

A is forty `a` characters; B is forty `b` characters. Both cases start with one expected changed file and old pytest version 9.0.2.

| Controlled case | Files head / proposed version | Observed result | Context revision |
|---|---|---|---|
| Stable head | A / 9.0.3 | accepted dependency analysis | A |
| Changed head, same file count | B / 9.0.4 | accepted dependency analysis — mismatch | A |
| Changed head, two files instead of one | B / 9.0.4 | `GitHubResponseError`: expected 1 records but acquired 2 | No context produced |

Every case issued exactly two simulated requests: PR identity, then files page 1 with `per_page=100`. No identity refresh or exact-file fallback occurred. The count-mismatch control demonstrates a functioning completeness check; it does not protect the same-count race.

**Disposition:** confirmed snapshot-consistency defect within the controlled acquisition → requirements extraction → source-context path. A requirements change from simulated head B is attributed to head A. Priority is high for a bounded correction decision because source identity underlies subsequent reasoning. This is stronger than a source-only hypothesis but narrower than an observed public incident or whole-product decision failure.

**Limits:** one-page requirements case only. No live race, multi-page churn, base movement, uv/pyproject reproduction, CI/Target execution, or final CLI recommendation was tested. The fake deliberately creates the race; it measures behavior, not likelihood. The response reference is ignored today, but this does not establish that trusting that URL alone would be a complete repair.

### Alternatives to evaluate if repair is selected

Compare revision-bound extraction from exact base/head content against a bounded acquisition consistency protocol that detects movement and rejects/restarts with a fresh identity. Account for request cost, pagination, base as well as head movement, possible change-and-revert sequences, and whether the evidence actually establishes correspondence rather than merely observing equal endpoints. A simple second read may detect common movement but must not be advertised as an atomic snapshot guarantee. Do not merely attach the original head label more widely or use a blob SHA as a commit SHA.

The owning correction would begin at acquisition/evidence binding, with downstream context generation consuming established correspondence. No implementation approach is selected here, and product/test files remain unchanged.

### Exact reproducer

Restore the following to a temporary file and run from the pinned checkout with `PYTHONPATH=src .venv/bin/python -B <script-path>`. Synthetic HTTP responses never contact the illustrated URLs. The script records source hashes, request coordinates and result states; it does not launch the product regression suite.

```python
import hashlib, json, pathlib, subprocess, sys
from unittest.mock import Mock, patch
from upgradepilot.github.pull_request import GitHubPullRequestClient
from upgradepilot.github.api import GitHubResponseError
from upgradepilot.dependency.analysis import analyze_dependency_change, DependencyChangeAnalysis

ROOT = pathlib.Path.cwd()
def hashes():
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted((ROOT/'src/upgradepilot').rglob('*.py'))}
before = hashes()
A, B, BASE = 'a'*40, 'b'*40, 'c'*40
rows = []
for case in ('stable_head', 'changed_head_same_count', 'changed_head_count_mismatch'):
    current = {'head': A}
    requests = []
    supplied_files = []
    def get(url, **kwargs):
        requests.append({'url': url, 'params': kwargs.get('params')})
        if url.endswith('/files'):
            current['head'] = A if case == 'stable_head' else B
            version = '9.0.3' if case == 'stable_head' else '9.0.4'
            data = [{'filename': 'requirements.txt', 'status': 'modified',
                     'additions': 1, 'deletions': 1, 'changes': 2,
                     'patch': '@@ -1 +1 @@\n-pytest==9.0.2\n+pytest==' + version,
                     'sha': 'd'*40,
                     'contents_url': 'https://api.github.com/repos/example/project/contents/requirements.txt?ref='+current['head']}]
            if case == 'changed_head_count_mismatch':
                data.append({'filename': 'README.md', 'status': 'modified',
                             'additions': 1, 'deletions': 1, 'changes': 2,
                             'patch': '@@ -1 +1 @@\n-old\n+new'})
            supplied_files.extend(data)
        else:
            assert url.endswith('/pulls/1'), url
            data = {'number': 1, 'title': 'Dependency update', 'state': 'open',
                    'merged': False, 'user': {'login': 'dependabot[bot]'},
                    'base': {'ref': 'main', 'sha': BASE},
                    'head': {'ref': 'dependency-update', 'sha': current['head']},
                    'changed_files': 1}
        response = Mock(status_code=200)
        response.json.return_value = data
        return response
    session = Mock()
    session.get.side_effect = get
    client = GitHubPullRequestClient(session=session)
    with patch('requests.sessions.Session.request', side_effect=AssertionError('Network prohibited')):
        identity = client.get_pull_request('example/project', 1)
        try:
            files = client.get_changed_files(identity)
            # Any repository-file fallback would fail, making that behavior visible.
            result = analyze_dependency_change(identity, files, object())
            assert isinstance(result, DependencyChangeAnalysis), result
            row = {'case': case, 'outcome': 'accepted',
                   'proposed_version': result.dependency.proposed_version,
                   'context_revision': result.source_contexts[0].revision}
        except GitHubResponseError as exc:
            row = {'case': case, 'outcome': 'rejected', 'error': str(exc)}
    row.update({'identity_head': identity.head_sha, 'simulated_files_head': current['head'],
                'supplied_contents_url': supplied_files[0]['contents_url'],
                'requests': requests})
    rows.append(row)
assert before == hashes(), 'Source changed during diagnostic'
print(json.dumps({'revision': subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip(),
                  'python': sys.version.split()[0], 'source_hashes': before, 'cases': rows}, indent=2))
```

Source hash-map digest (SHA-256 of sorted-key JSON): `3585de66c6563c6fcbcbe1b1d10e1f002c5553eb28e7d910b361a1eb62123230`.

### Checkpoint learning and handoff

A — DONE: distinguished complete file count from correspondence to one PR revision.
B — DONE: reproduced the same-count mismatch through real parsers/analyzer with stable-head and count-mismatch controls.
C — DONE: preserved exact inputs, outputs, ownership, alternatives and proof limits here.
D — explanation supplied; learner response pending. Ownership question: why does a complete changed-file list still fail to prove that its patch belongs to the initially captured head?
E — pending response or continuation. The next independent question is workflow run-attempt/job consistency; fixes remain unselected.

At this checkpoint two questions have executable evidence: command recognition and PR revision correspondence. Other seed concerns remain pending. Documentation validation applies only to this record; no claim of a product fix or overall investigation completion follows.
