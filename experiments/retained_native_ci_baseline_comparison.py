"""Disposable, offline comparison of retained CI facts with baseline v0.1.

Start with ``prepare``, review/commit the frozen source spans and rubric, then ``run``
once. Preparation only inspects retained bytes; it never evaluates either arm. Each
bounded child translates four baseline inputs and reconstructs one exact native revision
on a private copy. The product store/projection owns typed integrity and historical
semantics; this module neither re-derives CI facts nor fabricates a full investigation.
Public results contain summaries/hashes; complete native output stays outside Git.
The source-aware human review owns information-value judgments, not this runner.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

from packaging.version import InvalidVersion, Version

from upgradepilot.ci.dependency_state import RequirementSatisfiedAtCommandCompletion
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError
from upgradepilot.workspace.checkpoint_store import CheckpointStore
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget
from upgradepilot.workspace.native_projection import reconstruct_ci_projection
from upgradepilot.workspace.native_representation import NativeReconstructionError

REPOSITORY = Path(__file__).resolve().parents[1]
INVENTORY_PATH = REPOSITORY / "working-memory/evidence/2026-10-20-product-value-and-transparent-baseline-feasibility/input-inventory.json"
BASELINE_PATH = REPOSITORY / "product-simulation/TRANSPARENT_BASELINE_SPECIFICATION.md"
BASELINE_SHA256 = "a9093136b66d1131cb7c32b9a70728782641cb624332279e09126c22f622957a"
CAUTION = (
    'breaking',
    'removed',
    'removal',
    'dropped support',
    'deprecated',
    'deprecation',
    'incompatible',
    'requires python',
    'minimum python',
    'platform support',
    'operating system',
    'architecture',
    'compiler',
    'build system',
)
BENEFIT = ("security", "vulnerability", "cve", "advisory", "fixed", "bug fix", "bugfix")
MAX_EVIDENCE_BYTES = 5 * 1024 * 1024
RUBRIC = {
    "question": "Does retained native CI add material source-supported information beyond the restricted baseline?",
    "httpx": {
        "required": [
            'exact transition',
            'October query returned zero workflows; historical CI absence not inferred',
        ],
        "forbidden": [
            'API compatibility',
            'installed framework identity',
            'CI never existed',
            'positive action permission',
        ],
    },
    "glyphslib": {
        "required": [
            'exact transition',
            'supported static declarations',
            'uncorrelated runtime',
            'manager-environment unknowns retained',
        ],
        "forbidden": [
            'changed version installed from job success',
            'compatibility from job success',
            'positive action permission',
        ],
    },
    "credit": "Supported reasons, located uncertainty and specific justified evidence questions; baseline limitations receive full credit. Detail/citations alone earn no value.",
    "limits": "Two exposed source-aware cases; implementer and reviewer overlap; no full action comparison, independent maintainer usefulness, positive compatibility control or general reliability claim.",
    "decisions": [
        'useful component information: propose one bounded next investment',
        'no added material value: stop automatic expansion',
        'input/operational/semantic failure: exact gap and inconclusive disposition',
    ],
}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path):
    return json.loads(path.read_text())


def json_bytes(value) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, default=_json_value) + "\n").encode()


def _json_value(value):
    if dataclasses.is_dataclass(value):
        return {
            'native_type': type(value).__name__,
            'fields': {f.name: getattr(value, f.name) for f in dataclasses.fields(value)},
        }
    if isinstance(value, (datetime, Version)):
        return str(value)
    raise TypeError(type(value).__name__)


class InputUnavailable(ValueError):
    """Missing/ambiguous/substituted retained input; never silently repair it."""


class _ReleaseSection(HTMLParser):
    def __init__(self, body: str):
        super().__init__(convert_charrefs=True)
        self.body = body
        self.offsets = [0]
        for line in body.splitlines(keepends=True):
            self.offsets.append(self.offsets[-1] + len(line))
        self.active = None
        self.sections = []

    def character_offset(self):
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def handle_starttag(self, tag, attrs):
        if tag == "details":
            if self.active is not None:
                raise InputUnavailable("Nested details section is outside this translation contract")
            self.active = {
                'start': self.character_offset(),
                'summary': [],
                'text': [],
                'in_summary': False,
                'summary_done': False,
            }
        elif tag == "summary" and self.active is not None:
            if self.active["in_summary"] or self.active["summary_done"]:
                raise InputUnavailable("Ambiguous details summary")
            self.active["in_summary"] = True

    def handle_data(self, data):
        if self.active is not None:
            if self.active["in_summary"]:
                self.active["summary"].append(data)
            elif self.active["summary_done"]:
                self.active["text"].append(data)

    def handle_endtag(self, tag):
        if tag == "summary" and self.active is not None:
            if not self.active["in_summary"]:
                raise InputUnavailable("Unbalanced summary")
            self.active["in_summary"] = False
            self.active["summary_done"] = True
        elif tag == "details":
            if self.active is None:
                raise InputUnavailable("Unbalanced details section")
            if self.active["in_summary"]:
                raise InputUnavailable("Unclosed summary")
            if "".join(self.active["summary"]).strip().casefold() == "release notes":
                end = self.body.index(">", self.character_offset()) + 1
                self.sections.append((self.active["start"], end, "".join(self.active["text"])))
            self.active = None


def extract_release_notes(body: str) -> tuple[str, dict]:
    """Select one Release notes details block; decode entities, retain text whitespace.

    No inserted separators, word normalization, changelog fallback or Dependabot footer.
    Spans are character offsets into the exact PR body; hashes bind UTF-8 bytes.
    """
    parser = _ReleaseSection(body)
    parser.feed(body)
    parser.close()
    if parser.active is not None or len(parser.sections) != 1:
        raise InputUnavailable("Missing, unclosed or ambiguous Release notes section")
    start, end, text = parser.sections[0]
    return (
        text,
        {
            'body_sha256': digest(body.encode()),
            'section_character_span': [start, end],
            'raw_section_sha256': digest(body[start:end].encode()),
            'text_sha256': digest(text.encode()),
            'text_bytes': len(text.encode()),
            'translation': 'HTML text nodes after summary, entity-decoded, whitespace retained, no inserted separators',
        },
    )


@dataclasses.dataclass(frozen=True)
class BaselineInputs:
    version_category: str
    ci_conclusion: str
    dependency_directness: str
    release_note_text: str


def evaluate_baseline(inputs: BaselineInputs) -> dict:
    """Four-input-only, first matching rule from the unchanged baseline specification."""
    text = inputs.release_note_text.lower()
    caution = [word for word in CAUTION if word in text]
    benefit = [word for word in BENEFIT if word in text]
    if inputs.ci_conclusion in ("failing", "mixed"):
        rule, outcome, reason, limit = (
            'B01',
            'investigate_or_block',
            'Current CI is not clean',
            'Cause and relevance are unknown',
        )
    elif inputs.ci_conclusion in ("missing", "unknown"):
        rule, outcome, reason, limit = (
            'B02',
            'run_targeted_checks',
            'No passing current CI conclusion is available',
            'Cannot select the relevant check',
        )
    elif inputs.dependency_directness == "unknown":
        rule, outcome, reason, limit = (
            'B03',
            'run_targeted_checks',
            'Dependency relationship is unknown',
            'No dependency-path or usage analysis is permitted',
        )
    elif inputs.version_category in ("major", "pre_release", "replacement_or_unknown") or caution:
        rule, outcome, reason, limit = (
            'B04',
            'run_targeted_checks',
            'Coarse compatibility-change signal',
            'Cannot determine whether the signal is relevant',
        )
    elif (
        inputs.ci_conclusion == "passing"
        and inputs.dependency_directness in ("direct", "transitive")
        and inputs.version_category in ("patch", "minor")
    ):
        rule, outcome, reason, limit = (
            'B05',
            'merge_after_normal_review',
            'Ordinary-size update with passing CI and no coarse breaking signal',
            'Does not know whether CI exercised the dependency or release claims are relevant or true',
        )
    else:
        rule, outcome, reason, limit = (
            "B06", "abstain", "Restricted inputs match no stronger rule", "Residual uncertainty"
        )
    return {
        'baseline_version': 'simulation-transparent-baseline-v0.1',
        'restricted_inputs': {
            'version_category': inputs.version_category,
            'ci_conclusion': inputs.ci_conclusion,
            'dependency_directness': inputs.dependency_directness,
            'release_note_text_sha256': digest(inputs.release_note_text.encode()),
        },
        'keyword_matches': {'caution': caution, 'benefit': benefit},
        'matched_rule_id': rule,
        'outcome': outcome,
        'reasons': [reason],
        'limitations': [limit],
        'benefit_signal_changes_action': False,
        'full_investigation_outcome': {
            'status': 'unavailable',
            'reason': 'Retained CI component only; no full investigation/action synthesized',
        },
        'comparison_dimensions': {'status': 'source-aware review pending', 'action': 'unavailable: component scope'},
        'reviewer_status': 'pending source-aware review',
    }


def version_category(old: str, new: str) -> str:
    try:
        before, after = Version(old), Version(new)
    except InvalidVersion:
        return "unclassifiable"
    if before.is_prerelease or after.is_prerelease:
        return "pre_release"
    if before.epoch != after.epoch or before.local or after.local:
        return "unclassifiable"
    if before.major != after.major:
        return "major"
    if before.minor != after.minor:
        return "minor"
    return "patch" if before != after else "unclassifiable"


def require_hash(path: Path, expected: str, size: int | None = None):
    if path.resolve() != path.absolute() or not path.is_file():
        raise InputUnavailable("Missing or symlinked input: " + str(path))
    data = path.read_bytes()
    if digest(data) != expected or (size is not None and len(data) != size):
        raise InputUnavailable("Input hash/size differs: " + str(path))


def verify_inputs(root: Path) -> tuple[dict, dict]:
    """Revalidate the accepted inventory, all 17 members and exact product membership."""
    inventory = read_json(INVENTORY_PATH)
    common = inventory["qualified_common_inputs"]
    require_hash(root / "qualification.json", common["qualification_sha256"])
    require_hash(root / "manifest.json", common["manifest_sha256"])
    if root.resolve() != Path(common["root"]):
        raise InputUnavailable("Unexpected common freeze root")
    for member in common["declared_members"]:
        path = root / member["path"]
        for private_input in (path, path.parent, root):
            info = private_input.stat()
            if info.st_uid != os.geteuid() or info.st_mode & 0o077:
                raise InputUnavailable("Private input is not owner-only: " + str(private_input))
        require_hash(path, member["sha256"], member["bytes"])
    manifest = read_json(root / "manifest.json")
    actual = {str(p.relative_to(REPOSITORY)): digest(p.read_bytes()) for p in (REPOSITORY / "src/upgradepilot").rglob("*.py")}
    if actual != manifest["product_source_sha256"]:
        raise InputUnavailable("Product source membership/hashes differ from retained freeze")
    require_hash(BASELINE_PATH, BASELINE_SHA256)
    return inventory, manifest


def translate_case(root: Path, selection: dict) -> tuple[BaselineInputs, dict]:
    """Translate captured public responses, never scenario findings or native conclusions."""
    target = selection["target"]
    captured = read_json(root / selection["directory"] / "public-acquisition.json")
    prefix = f"https://api.github.com/repos/{target['repository']}"
    pr_url = f"{prefix}/pulls/{target['pull_number']}"

    def responses(url):
        records = [record for record in captured if record["url"] == url]
        if not records or any(record["status"] != 200 for record in records):
            raise InputUnavailable("Missing successful captured response: " + url)
        values = [json.loads(record["body"]) for record in records]
        if any(value != values[0] for value in values):
            raise InputUnavailable("Conflicting captured responses: " + url)
        return values[0]

    pr = responses(pr_url)
    observed_target = (
        pr["number"], pr["base"]["sha"], pr["head"]["sha"], pr["base"]["repo"]["full_name"]
    )
    expected_target = (
        target["pull_number"], target["base_sha"], target["head_sha"], target["repository"]
    )
    if observed_target != expected_target:
        raise InputUnavailable("Captured PR target differs")
    text, release_identity = extract_release_notes(pr["body"])
    files = responses(pr_url + "/files?per_page=100&page=1")
    if len(files) != 1:
        raise InputUnavailable("This two-case translation requires one changed requirements file")
    changed = files[0]
    patch = changed.get("patch", "")
    old = f"-{target['normalized_package']}=={target['old_version']}"
    new = f"+{target['normalized_package']}=={target['proposed_version']}"
    if (
        not re.fullmatch(r"requirements(?:-[\w-]+)?\.txt", changed["filename"])
        or old not in patch.splitlines()
        or new not in patch.splitlines()
    ):
        raise InputUnavailable("Exact direct requirement change is unavailable")
    query = f"{prefix}/actions/runs?event=pull_request&head_sha={target['head_sha']}&per_page=100&page=1"
    runs_response = responses(query)
    runs = runs_response["workflow_runs"]
    if any(run["head_sha"] != target["head_sha"] for run in runs):
        raise InputUnavailable("Captured query includes another head")
    if runs_response["total_count"] != len(runs):
        conclusion = "unknown"
    elif not runs:
        conclusion = "missing"
    else:
        conclusions = [run.get("conclusion") for run in runs]
        bad = any(value in ("failure", "cancelled", "timed_out", "action_required", "startup_failure", "stale") for value in conclusions)
        good = any(value == "success" for value in conclusions)
        if bad:
            conclusion = "mixed" if good else "failing"
        elif all(run.get("status") == "completed" and run.get("conclusion") == "success" for run in runs):
            conclusion = "passing"
        else:
            conclusion = "unknown"
    inputs = BaselineInputs(version_category(target["old_version"], target["proposed_version"]), conclusion, "direct", text)
    return (
        inputs,
        {
            'version_category': inputs.version_category,
            'version_derivation': 'Mechanical PEP 440 major/minor/release-component comparison for these Python versions; no behavioral SemVer inference',
            'ci_conclusion': conclusion,
            'dependency_directness': 'direct',
            'directness_basis': {
                'path': changed['filename'],
                'removed': old,
                'added': new,
                'patch_sha256': digest(patch.encode()),
            },
            'ci_source': {
                'query': query,
                'run_ids': [run['id'] for run in runs],
                'conclusions': [run.get('conclusion') for run in runs],
                'total_count': runs_response['total_count'],
                'limit': 'October acquisition-time query, not historical CI absence or compatibility',
            },
            'release_notes': release_identity,
        },
    )


def prepare(root: Path) -> dict:
    inventory, manifest = verify_inputs(root)
    selections = []
    for index, case in enumerate(manifest["cases"], 1):
        selection = {key: case[key] for key in ("case_id", "lineage_id", "revision_id", "checkpoint_digest", "target")}
        selection["directory"] = f"case-{index}"
        selection["baseline_translation"] = translate_case(root, selection)[1]
        selections.append(selection)
    if [s["revision_id"] for s in selections] != ["0797f32c78e443eaaad877e1ef27e145", "df54ee39679e488cb7ef3563619c6935"]:
        raise InputUnavailable("Unexpected case/revision selection")
    return {
        'format': 'retained-native-ci-baseline-freeze/1',
        'root': str(root),
        'inventory_sha256': digest(INVENTORY_PATH.read_bytes()),
        'manifest_sha256': inventory['qualified_common_inputs']['manifest_sha256'],
        'baseline_specification_sha256': BASELINE_SHA256,
        'experiment_sha256': digest(Path(__file__).read_bytes()),
        'rubric': RUBRIC,
        'cases': selections,
        'caps': {
            'case_seconds': 60,
            'aggregate_case_seconds': 180,
            'whole_seconds': 300,
            'evidence_bytes': MAX_EVIDENCE_BYTES,
            'model_calls': 0,
            'new_acquisition': 0,
            'target_commands': 0,
            'engineering_hours': 4,
        },
    }


def reconstruct_on_copy(source: Path, scratch: Path, selection: dict):
    """The only native read: exact revision on a verified owned copy, never latest head."""
    original = source / "workspace.sqlite3"
    before = digest(original.read_bytes())
    scratch.mkdir(mode=0o700)
    copied = scratch / original.name
    shutil.copyfile(original, copied)
    copied.chmod(0o600)
    try:
        if digest(copied.read_bytes()) != before:
            raise InputUnavailable("Checkpoint copy differs")
        target = ExactInvestigationTarget(**selection["target"])
        store = CheckpointStore.open(scratch, read_only=True)
        stored = store.read_revision(selection["lineage_id"], selection["revision_id"], expected_target=target)
        if stored.revision.digest() != selection["checkpoint_digest"]:
            raise InputUnavailable("Exact checkpoint digest differs")
        projection = reconstruct_ci_projection(stored.revision.boundary, expected_target=target)
        return (
            projection,
            {
                'original_sha256': before,
                'copy_sha256_after': digest(copied.read_bytes()),
                'head_revision_id': stored.head_revision_id,
                'excluded_successor_ids': stored.excluded_successor_ids,
                'selected_revision_id': stored.revision.revision_id,
                'native_records': [
                    {key: getattr(record, key) for key in (
                        "family", "owner", "codec_version", "producer_method",
                        "producer_version", "retention_gaps", "record_id", "payload_digest",
                    )}
                    for record in stored.revision.boundary.records
                ],
            },
        )
    finally:
        if digest(original.read_bytes()) != before:
            raise InputUnavailable("Original checkpoint changed during copy/read")


def summarize_projection(projection) -> dict:
    """Retain every coverage axis and every runtime result without promoting a state."""
    coverage = projection.ci_coverage_result
    runtime = projection.runtime_dependency_state_result
    workflow_fields = (
        "workflow_name", "workflow_path", "state", "reason", "detail",
        "consumption_state", "consumption_reason",
        "direct_exercise_state", "direct_exercise_reason",
        "runtime_consumption_state", "runtime_consumption_reason",
        "runtime_direct_exercise_state", "runtime_direct_exercise_reason",
        "consumption_command", "execution_command",
    )
    coverage_summary = None
    if coverage is not None:
        coverage_summary = {
            "state": coverage.state,
            "reason": coverage.reason,
            "detail": coverage.detail,
            "workflows": [
                {key: getattr(workflow, key) for key in workflow_fields}
                for workflow in coverage.workflows
            ],
        }
    runtime_summary = None
    if runtime is not None:
        assessments = []
        for assessment in runtime.assessments:
            result = assessment.result
            witness = isinstance(result, RequirementSatisfiedAtCommandCompletion)
            assessments.append({
                "workflow_path": assessment.consumption.workflow_path,
                "job_key": assessment.consumption.job_key,
                "command": assessment.consumption.command,
                "state": "requirement_satisfied_at_command_completion" if witness else result.state,
                "reason": None if witness else result.reason,
                "detail": None if witness else result.detail,
                "blocking_dimension": None if witness else result.blocking_dimension,
            })
        runtime_summary = {
            "evaluation_state": runtime.evaluation_state,
            "reason": runtime.reason,
            "detail": runtime.detail,
            "assessments": assessments,
        }
    return {
        'target': dataclasses.asdict(projection.inputs.pull_request),
        'dependency': {key: getattr(projection.inputs.dependency_result, key) for key in ('normalized_package', 'old_version', 'proposed_version')},
        'ci_coverage': coverage_summary,
        'runtime_dependency_state': runtime_summary,
        'maintainer_action': {'status': 'unavailable', 'reason': 'Retained CI component; synthesis not invoked'},
    }


def _offline_audit(event, args):
    if event.startswith("socket.") or event in ("subprocess.Popen", "os.system", "os.exec", "os.posix_spawn"):
        raise RuntimeError("Offline comparison forbids network/process entry: " + event)


def _worker(freeze: dict, index: int, private: Path) -> dict:
    sys.addaudithook(_offline_audit)
    start = time.monotonic()
    root = Path(freeze["root"])
    selection = freeze["cases"][index]
    inputs, translation = translate_case(root, selection)
    if translation != selection["baseline_translation"]:
        raise InputUnavailable("Baseline translation differs from pre-execution freeze")
    baseline = evaluate_baseline(inputs)
    baseline["input_translation"] = translation
    # Retain the completed arm even if native decoding later refuses or the child dies.
    partial = private / (selection["directory"] + "-partial.json")
    partial.write_bytes(json_bytes({"baseline": baseline, "native_ci": {"status": "not_completed"}}))
    partial.chmod(0o600)
    with tempfile.TemporaryDirectory(prefix="checkpoint-copy-", dir=private) as temporary:
        projection, retention = reconstruct_on_copy(root / selection["directory"] / "checkpoint", Path(temporary) / "store", selection)
        output = json_bytes(projection)
        if len(output) > MAX_EVIDENCE_BYTES:
            raise InputUnavailable("Native output exceeds evidence cap")
        payload = private / (selection["directory"] + "-native.json")
        payload.write_bytes(output)
        payload.chmod(0o600)
    return {
        'case_id': selection['case_id'],
        'status': 'completed',
        'baseline': baseline,
        'native_ci': summarize_projection(projection),
        'native_payload': {'path': str(payload), 'bytes': len(output), 'sha256': digest(output)},
        'retention': retention,
        'elapsed_seconds': time.monotonic() - start,
    }


def run(freeze_path: Path, output: Path, private: Path) -> dict:
    """One attempt per frozen row; timeouts/failures are retained without retries."""
    started = time.monotonic()
    freeze = read_json(freeze_path)
    if prepare(Path(freeze["root"])) != freeze:
        raise InputUnavailable("Input, executable, rubric or translation changed after freeze")
    if private.resolve() != private.absolute() or any((p / ".git").exists() for p in (private, *private.parents)):
        raise InputUnavailable("Private output must be outside Git and symlink paths")
    private.mkdir(mode=0o700, parents=True, exist_ok=False)
    output.mkdir(parents=True, exist_ok=False)
    result = {
        'started_utc': datetime.now(timezone.utc).isoformat(),
        'freeze_sha256': digest(freeze_path.read_bytes()),
        'python': sys.version,
        'mode': 'retained-native-CI-output; no fresh producer derivation',
        'rows': [],
        'accounting': {
            'model_calls': 0,
            'new_acquisition': 0,
            'target_commands': 0,
            'historical_cost': '14 public GET operations and six native owner invocations at original preparation; earlier corpus/model and human preparation costs not reconstructed, not zero',
        },
    }
    result_path = output / "results.json"
    result_path.write_bytes(json_bytes(result))
    elapsed_cases = 0.0
    for index, selection in enumerate(freeze["cases"]):
        remaining = min(60, 180 - elapsed_cases, 300 - (time.monotonic() - started) - 5)
        if remaining <= 0:
            result["rows"].append({"case_id": selection["case_id"], "status": "unattempted_budget"})
            continue
        case_start = time.monotonic()
        try:
            child = subprocess.run([
                sys.executable,
                '-m',
                'experiments.retained_native_ci_baseline_comparison',
                '_worker',
                str(freeze_path.resolve()),
                str(index),
                str(private.resolve()),
            ], cwd=REPOSITORY, capture_output=True, timeout=remaining, check=False)
            if child.returncode:
                row = {
                    'case_id': selection['case_id'],
                    'status': 'input_unavailable' if child.returncode == 2 else 'operationally_failed',
                    'stderr': child.stderr.decode(errors='replace')[-6000:],
                }
            else:
                row = json.loads(child.stdout)
        except subprocess.TimeoutExpired:
            row = {
                'case_id': selection['case_id'],
                'status': 'operationally_failed',
                'reason': 'case_timeout; child killed; no retry',
            }
        partial = private / (selection["directory"] + "-partial.json")
        if row["status"] != "completed" and partial.is_file():
            row.update(read_json(partial))
        row["whole_child_seconds"] = time.monotonic() - case_start
        elapsed_cases += row["whole_child_seconds"]
        result["rows"].append(row)
        result_path.write_bytes(json_bytes(result))
    verify_inputs(Path(freeze["root"]))
    result["original_inventory_reverified_after"] = True
    result["aggregate_case_seconds"] = elapsed_cases
    result["whole_seconds"] = time.monotonic() - started
    result["counts"] = {state: sum(row["status"] == state for row in result["rows"]) for state in ("completed", "input_unavailable", "operationally_failed", "unattempted_budget")}
    result["semantic_review"] = "pending; operational completion is not semantic adequacy or information value"
    result_path.write_bytes(json_bytes(result))
    size = sum(p.stat().st_size for folder in (output, private) for p in folder.rglob("*") if p.is_file()) + freeze_path.stat().st_size
    if size > MAX_EVIDENCE_BYTES or result["whole_seconds"] > 300 or elapsed_cases > 180:
        raise RuntimeError("Comparison cap exceeded; retain incomplete evidence, do not rerun")
    return result


def main():
    args = sys.argv[1:]
    if args and args[0] == "_worker":
        try:
            print(json.dumps(_worker(read_json(Path(args[1])), int(args[2]), Path(args[3])), default=_json_value))
        except (InputUnavailable, CheckpointStorageError, NativeReconstructionError) as error:
            print(str(error), file=sys.stderr)
            raise SystemExit(2)
        return
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prep = commands.add_parser("prepare")
    prep.add_argument("--root", type=Path, required=True)
    prep.add_argument("--freeze", type=Path, required=True)
    execute = commands.add_parser("run")
    execute.add_argument("--freeze", type=Path, required=True)
    execute.add_argument("--output", type=Path, required=True)
    execute.add_argument("--private", type=Path, required=True)
    options = parser.parse_args()
    if options.command == "prepare":
        prepared = prepare(options.root)
        options.freeze.parent.mkdir(parents=True, exist_ok=True)
        with options.freeze.open("xb") as handle:
            handle.write(json_bytes(prepared))
        print("Prepared source/rubric freeze; neither arm evaluated")
    else:
        result = run(options.freeze, options.output, options.private)
        print(json.dumps({"counts": result["counts"], "whole_seconds": result["whole_seconds"]}))


if __name__ == "__main__":
    main()
