"""Offline CI presentation consumer; original interpretation remains a separate proposal.

Start at compose_ci_presentation for already reconstructed native values. It calls the
product's shared report mapping, never a domain evaluator/model/synthesis owner. The CLI
prepare/run sequence is the disposable two-case proof, not a product replay interface.
Preparation validates retained identities without producing case views. Run once after
publishing the freeze; each exact checkpoint is decoded on a private copy with watchdogs.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

from experiments.retained_native_ci_baseline_comparison import (
    INVENTORY_PATH, InputUnavailable, json_bytes as native_projection_bytes, reconstruct_on_copy,
)
from upgradepilot.report import CIReport, render_ci_report
from upgradepilot.report_projection import project_ci_report
from upgradepilot.workspace.native_boundary import ExactInvestigationTarget, exact_investigation_target
from upgradepilot.workspace.native_projection import CINativeProjection
from upgradepilot.workspace.native_representation import NativeReconstructionError
from upgradepilot.workspace.checkpoint_revision import CheckpointStorageError

ROOT = Path(__file__).resolve().parents[1]
OLD_FREEZE = ROOT / "working-memory/evidence/2026-10-20-retained-native-ci-baseline-comparison/freeze.json"
MODEL_INDEX = ROOT / "working-memory/evidence/2026-10-19-investigator-evidence-first-build/run-retention.json"
PLAN = ROOT / "plans/INVESTIGATOR_NATIVE_CI_PRESENTATION_PLAN.md"
FORMAT = "investigator-native-ci-presentation/1"
CAP_BYTES = 5 * 1024 * 1024
REPORT_FILES = {"src/upgradepilot/report.py", "src/upgradepilot/report_projection.py"}
FAMILIES = {"investigation_inputs", "ci_inputs", "ci_coverage", "runtime_dependency_state"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path):
    return json.loads(path.read_text())


def write(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


@dataclass(frozen=True)
class InterpretationReference:
    """Original proposal metadata bound through trusted retained input/publication records.

    This record contains no model-authored assertion. Evaluation is copied verbatim, not
    assigned by the model or upgraded by the presentation. The CLI verifies byte identities
    from the original retention index before constructing it.
    """

    target: ExactInvestigationTarget
    role: str
    proposal_id: str
    evaluation: str
    response_path: str
    response_sha256: str
    packed_input_sha256: str
    publication_result_sha256: str


def bind_interpretation_reference(
    *, target: ExactInvestigationTarget, packed: bytes, publication: bytes,
    response: bytes, response_path: str,
) -> InterpretationReference:
    """Bind the new cross-artifact relationship; never inspect the proposal for truth."""
    task = json.loads(packed)["task"]
    result = json.loads(publication)
    if task["target"] != asdict(target) or task["case_label"] != result["role"]:
        raise ValueError("Interpretation input/publication has another target or role")
    published = result["report_publication"]
    if not published or not published.get("proposal_id") or not published.get("evaluation"):
        raise ValueError("Original interpretation has no retained publication/evaluation")
    return InterpretationReference(
        target, result["role"], published["proposal_id"], published["evaluation"],
        response_path, digest(response), digest(packed), digest(publication),
    )


@dataclass(frozen=True)
class CIPresentation:
    """Native view and proposal attribution have separate fields and display paths."""

    target: ExactInvestigationTarget
    ci: CIReport
    native_basis: dict
    interpretation: InterpretationReference | None

    def artifact(self) -> dict:
        return {"format": FORMAT, "target": asdict(self.target), "ci_view": asdict(self.ci),
                "native_basis": self.native_basis,
                "interpretation": {"status": "retained_attributed_proposal", **asdict(self.interpretation)}
                if self.interpretation else {"status": "unavailable", "reason": "No bound original interpretation supplied"},
                "authority_limit": "CI view copies native owner meaning; interpretation is not semantically accepted; no maintainer action is synthesized."}

    def render(self) -> str:
        # Split the rendered body into display lines before the final metadata sanitizer.
        # Treating the whole body as one line stripped its meaningful newline separators.
        lines = [*render_ci_report(self.ci).splitlines(), "", "Capture basis",
                 json.dumps(self.native_basis, sort_keys=True), "", "Separate laboratory interpretation"]
        if self.interpretation is None:
            lines.append("Unavailable: no bound original interpretation supplied.")
        else:
            reference = self.interpretation
            lines.extend((f"Proposal: {reference.proposal_id}", f"Recorded evaluation: {reference.evaluation}",
                          f"Original response SHA-256: {reference.response_sha256}",
                          f"Original artifact: {reference.response_path}"))
        lines.append("Proposal prose is not included in the owned CI conclusion; semantic adequacy and usefulness remain unestablished.")
        # The CI renderer also applies this boundary. Metadata/proposal paths are display
        # data too; sanitizing display does not alter either retained record.
        return "\n".join("".join(c for c in line if c == "\t" or c.isprintable()) for line in lines)


def compose_ci_presentation(
    projection: CINativeProjection, *, native_basis: dict,
    interpretation: InterpretationReference | None = None,
) -> CIPresentation:
    """Consume a validated native projection; copy facts without evaluating a proposal.

    Native reconstruction owns validity of the four families. This consumer owns only
    the distinct optional interpretation-to-target join and presentation. Native basis
    metadata comes from the same trusted checkpoint read, never from model prose.
    """
    target = exact_investigation_target(projection.inputs.pull_request, projection.inputs.dependency_result)
    if interpretation is not None and interpretation.target != target:
        raise ValueError("Cannot join interpretation from another exact investigation target")
    ci = project_ci_report(
        pull_request=projection.inputs.pull_request,
        dependency_result=projection.inputs.dependency_result,
        workflow_evidence=tuple((w.run, w.jobs) for w in projection.workflow_inputs),
        ci_coverage_result=projection.ci_coverage_result,
        runtime_dependency_state_result=projection.runtime_dependency_state_result,
    )
    return CIPresentation(target, ci, native_basis, interpretation)


def original_inputs() -> tuple[dict, dict]:
    """Preserve old input truth while explicitly admitting only report-source changes.

    The original comparison guard stays unchanged. This new proof binds its own code
    identity and exact report-only delta; it does not claim the old executable still fits.
    """
    old = load(OLD_FREEZE)
    common = load(INVENTORY_PATH)["qualified_common_inputs"]
    root = Path(old["root"])
    if root != Path(common["root"]):
        raise ValueError("Original common root differs")
    for relative, expected in [("manifest.json", common["manifest_sha256"]),
                               ("qualification.json", common["qualification_sha256"])]:
        if digest((root / relative).read_bytes()) != expected:
            raise ValueError("Original common metadata changed")
    for member in common["declared_members"]:
        path = root / member["path"]
        for scope in (root, path.parent, path):
            if scope.stat().st_mode & 0o077 or scope.stat().st_uid != os.geteuid():
                raise ValueError("Original input is not owner-only")
        if path.stat().st_size != member["bytes"] or digest(path.read_bytes()) != member["sha256"]:
            raise ValueError("Original input changed: " + member["path"])
    historical = load(root / "manifest.json")["product_source_sha256"]
    current = {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in (ROOT / "src/upgradepilot").rglob("*.py")}
    delta = report_source_delta(historical, current)
    return old, {"original_member_count": len(common["declared_members"]),
                 "historical_source_count": len(historical), "source_delta": delta,
                 "unchanged_native_owners": True}


def report_source_delta(historical: dict, current: dict) -> dict:
    """Admit the named presentation extraction, never altered native semantics/codecs."""
    if historical.keys() != current.keys():
        raise ValueError("Product source membership changed")
    delta = {path: {"historical": historical[path], "current": current[path]}
             for path in historical if historical[path] != current[path]}
    if not set(delta) <= REPORT_FILES:
        raise ValueError("Source delta escaped report-only scope: " + str(sorted(delta)))
    return delta


def experiment_sources() -> dict:
    paths = [Path(__file__), ROOT / "experiments/tests/test_investigator_ci_presentation.py",
             ROOT / "experiments/retained_native_ci_baseline_comparison.py", ROOT / "tests/test_report.py", PLAN,
             OLD_FREEZE, INVENTORY_PATH, MODEL_INDEX]
    paths.extend(ROOT / "tests" / name for name in (
        "test_report_file.py", "test_cli.py", "test_investigation.py",
        "test_ci_dependency_state.py", "test_workspace_native_reconstruction.py",
        "test_workspace_checkpoint_reconstruction.py"))
    paths.extend((ROOT / "src/upgradepilot").rglob("*.py"))
    return {str(p.relative_to(ROOT)): digest(p.read_bytes()) for p in sorted(paths)}


def prepare() -> dict:
    old, preservation = original_inputs()
    index = load(MODEL_INDEX)
    root = Path(index["run_root"])
    entries = {entry["path"]: entry for entry in index["entries"]}
    selections = []
    # These are original trusted role bindings, not an answer selected from model prose.
    for selection, role in zip(old["cases"], ("packet-a", "packet-c"), strict=True):
        files = {}
        for key, relative in (("packed", f"{role}/call-01.packed-input.json"),
                              ("publication", f"{role}.result.json"),
                              ("response", f"{role}/call-01.visible-response.txt")):
            path = root / relative
            entry = entries[relative]
            if (path.stat().st_mode & 0o077 or path.stat().st_uid != os.geteuid()
                    or path.stat().st_size != entry["bytes"] or digest(path.read_bytes()) != entry["sha256"]):
                raise ValueError("Original interpretation identity/permission differs")
            files[key] = {"path": str(path), "sha256": entry["sha256"]}
        reference = bind_interpretation_reference(
            target=ExactInvestigationTarget(**selection["target"]),
            packed=Path(files["packed"]["path"]).read_bytes(),
            publication=Path(files["publication"]["path"]).read_bytes(),
            response=Path(files["response"]["path"]).read_bytes(), response_path=files["response"]["path"],
        )
        selections.append({"selection": selection, "interpretation_files": files,
                           "interpretation_reference": asdict(reference)})
    return {"format": FORMAT + "/freeze", "source_files": experiment_sources(),
            "common_root": old["root"], "preservation": preservation, "cases": selections,
            "caps": {"case_seconds": 30, "aggregate_seconds": 60, "whole_seconds": 120, "evidence_bytes": CAP_BYTES},
            "review": "Same source-aware implementer/reviewer; exposed retained development cases. No semantic regrade or independent usefulness claim."}


def verify_freeze(path: Path) -> dict:
    frozen = load(path)
    if frozen != prepare():
        raise ValueError("Frozen inputs/executable/policy changed; no case dispatched")
    return frozen


def offline_guard(event, args):
    if event.startswith("socket.") or event in ("subprocess.Popen", "os.system", "os.exec", "os.posix_spawn"):
        raise RuntimeError("Offline case forbids network/process entry")


def case_worker(frozen: dict, index: int, output: Path, private: Path) -> None:
    sys.addaudithook(offline_guard)
    started = time.monotonic()
    row = {"case_id": frozen["cases"][index]["selection"]["case_id"], "state": "started"}
    write(output / "result.json", row)
    try:
        selection = frozen["cases"][index]["selection"]
        private.mkdir(mode=0o700)
        with tempfile.TemporaryDirectory(prefix="copy-", dir=private) as temporary:
            projection, basis = reconstruct_on_copy(
                Path(frozen["common_root"]) / selection["directory"] / "checkpoint", Path(temporary) / "store", selection)
            basis = {**basis, "selected_lineage_id": selection["lineage_id"],
                     "selected_checkpoint_digest": selection["checkpoint_digest"],
                     "native_records": [r for r in basis["native_records"] if r["family"] in FAMILIES]}
            item = frozen["cases"][index]
            files = item["interpretation_files"]
            ref = bind_interpretation_reference(
                target=ExactInvestigationTarget(**selection["target"]),
                packed=Path(files["packed"]["path"]).read_bytes(), publication=Path(files["publication"]["path"]).read_bytes(),
                response=Path(files["response"]["path"]).read_bytes(), response_path=files["response"]["path"],
            )
            view = compose_ci_presentation(projection, native_basis=basis, interpretation=ref)
            payload = native_projection_bytes(projection)
            if len(payload) > CAP_BYTES:
                raise ValueError("Native output exceeds evidence ceiling; not retained")
            path = private / "native-projection.json"
            path.write_bytes(payload)
            path.chmod(0o600)
            write(output / "ci-presentation.json", view.artifact())
            (output / "ci-presentation.txt").write_text(view.render() + "\n")
            row.update(state="completed", native_payload_sha256=digest(payload),
                       native_payload_bytes=len(payload), interpretation_evaluation=ref.evaluation,
                       original_checkpoint_unchanged=True)
    except (InputUnavailable, NativeReconstructionError, CheckpointStorageError) as error:
        row.update(state="input_unavailable", error_class=type(error).__name__, detail=str(error))
    except Exception as error:
        row.update(state="failed", error_class=type(error).__name__, detail=str(error))
    row.update(elapsed_seconds=time.monotonic() - started)
    write(output / "result.json", row)


def dispatch(command: list[str], path: Path, seconds: float) -> None:
    """One subprocess watchdog; preserve cancellation/partial output and never retry."""
    try:
        result = subprocess.run(command, cwd=ROOT, timeout=seconds, capture_output=True, text=True)
        if result.returncode:
            row = load(path) if path.exists() else {}
            write(path, {**row, "state": "process_failure", "returncode": result.returncode, "stderr": result.stderr[:2000]})
    except subprocess.TimeoutExpired:
        row = load(path) if path.exists() else {}
        write(path, {**row, "state": "watchdog_cancelled", "seconds": seconds,
                     "cancellation": "subprocess.run killed/waited for worker; no retry"})


def run(freeze: Path, output: Path, private: Path) -> None:
    started = time.monotonic()
    frozen = verify_freeze(freeze)
    if output.exists() or private.exists() or private.resolve().is_relative_to(ROOT):
        raise ValueError("Exclusive outputs required; private retention must be outside Git")
    output.mkdir(parents=True)
    private.mkdir(parents=True, mode=0o700)
    rows, aggregate = [], 0.0
    for index in range(len(frozen["cases"])):
        destination = output / f"case-{index+1}"
        seconds = min(30, 60 - aggregate, 117 - (time.monotonic() - started))
        if seconds <= 0:
            write(destination / "result.json", {"state": "unattempted", "reason": "deadline"})
        else:
            before = time.monotonic()
            dispatch([sys.executable, str(Path(__file__)), "_case", str(freeze), str(destination),
                      str(private / f"case-{index+1}"), "--index", str(index)], destination / "result.json", seconds)
            aggregate += time.monotonic() - before
        row = load(destination / "result.json")
        rows.append({"case_id": frozen["cases"][index]["selection"]["case_id"],
                     "state": row["state"], "result_sha256": digest((destination / "result.json").read_bytes())})
        write(output / "progress.json", {"rows": rows, "elapsed_seconds": time.monotonic() - started})
    verify_freeze(freeze)
    size = sum(p.stat().st_size for root in (freeze.parent, private) for p in root.rglob("*") if p.is_file())
    write(output / "summary.json", {"requested": 2, "rows": rows,
                                   "aggregate_case_wall_seconds": aggregate, "elapsed_seconds": time.monotonic() - started,
                                   "evidence_bytes_before_summary": size, "retention_cap_satisfied": size < CAP_BYTES,
                                   "frozen_inputs_and_original_results_unchanged": True})
    if size >= CAP_BYTES:
        raise ValueError("Evidence ceiling exceeded; preserve incomplete result and stop")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("prepare", "run", "_case"))
    parser.add_argument("freeze", type=Path)
    parser.add_argument("output", type=Path, nargs="?")
    parser.add_argument("private", type=Path, nargs="?")
    parser.add_argument("--index", type=int)
    args = parser.parse_args()
    if args.command == "prepare":
        if args.freeze.exists():
            raise ValueError("Cannot overwrite freeze")
        write(args.freeze, prepare())
    elif args.command == "_case":
        frozen = verify_freeze(args.freeze)
        case_worker(frozen, args.index, args.output, args.private)
    else:
        run(args.freeze, args.output, args.private)


if __name__ == "__main__":
    main()
