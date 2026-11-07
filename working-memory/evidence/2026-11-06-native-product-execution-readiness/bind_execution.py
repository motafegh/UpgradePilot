"""Bind the qualified installed method for review, without activating acquisition.

The manifest records actual files, not a claim of hermetic dependency isolation.
It references the frozen case/task plus explicit later corrections and evidence.
"""
import importlib.metadata
import json
from pathlib import Path
import subprocess
import sys
import sysconfig
import tomllib

from packaging.requirements import Requirement

from launch_product import digest, write_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
REVIEW = HERE.parent / "2026-11-06-native-normal-product-attempt-contract"
PRIVATE = Path("/home/motafeq/.local/share/upgradepilot/native-signature-kubernetes-dashboard-token-api-pr-20-httpx-2026-11-06")


def dependency_bindings():
    """Declared runtime dependency closure and present distribution files; no extras."""
    pending = list(tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]["dependencies"])
    seen, descriptions, files = set(), {}, {}
    while pending:
        requirement = Requirement(pending.pop())
        if requirement.marker and not requirement.marker.evaluate({"extra": ""}):
            continue
        dist = importlib.metadata.distribution(requirement.name)
        if dist.version not in requirement.specifier:
            raise ValueError("Installed dependency does not satisfy declared requirement: " + requirement.name)
        name = dist.metadata["Name"]
        if name in seen:
            continue
        seen.add(name)
        inventory = []
        for entry in dist.files or ():
            path = Path(dist.locate_file(entry)).absolute()
            if path.is_file() and path.suffix != ".pyc" and "__pycache__" not in path.parts:
                files[str(path)] = digest(path)
                inventory.append(str(path))
        if not inventory:
            raise ValueError("Dependency distribution lacks an inspectable file inventory: " + name)
        descriptions[name] = dict(version=dist.version, files=len(inventory), location=str(Path(dist.locate_file("")).absolute()))
        pending.extend(dist.requires or ())
    return descriptions, files


def main():
    manifest_path = HERE / "execution-manifest.json"
    if manifest_path.exists():
        raise FileExistsError("Bind a successor rather than overwrite an existing execution manifest.")
    review = json.loads((REVIEW / "contract.json").read_bytes())
    qualification = PRIVATE / "method-qualification-02"
    result = json.loads((qualification / "results.json").read_bytes())
    assert result["outcome"] == "passed" and result["real_provider_calls"] == 0
    cold_proof = PRIVATE / "method-cold-successor-01"
    cold = json.loads((cold_proof / "results.json").read_bytes())
    assert cold["outcome"] == "passed" and cold["cold_method_sha256"] == digest(HERE / "cold_review.py")
    installed = PRIVATE / "runtime/installed"
    earlier = HERE.parent / "2026-11-06-caller-signature-cli-revision-guards"
    source = json.loads((earlier / "verification.json").read_bytes())["product_source_sha256"]
    assert all(digest(ROOT / p) == h and digest(installed / p.removeprefix("src/")) == h for p, h in source.items())
    bindings = {str(ROOT / p): h for p, h in source.items()}
    dependencies, files = dependency_bindings()
    bindings.update(files)
    bindings[str(Path(sys.executable).resolve())] = digest(Path(sys.executable).resolve())
    bindings[str(ROOT / ".venv/pyvenv.cfg")] = digest(ROOT / ".venv/pyvenv.cfg")
    for p in Path(sysconfig.get_paths()["purelib"]).glob("*.pth"):
        bindings[str(p)] = digest(p)
    clock = HERE.parent / "2026-11-06-independent-host-timing"
    timing_proof = json.loads((clock / "verification.json").read_bytes())
    assert all(digest(clock / p) == h for p, h in timing_proof["method_sha256"].items())
    powershell = Path("/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe")
    assert digest(powershell) == timing_proof["powershell_binary_sha256"]
    bindings[str(powershell)] = digest(powershell)
    evidence = [REVIEW / "CONTRACT.md", REVIEW / "contract.json", earlier / "README.md",
        earlier / "verification.json", earlier / "results-summary.json",
        clock / "run_preflight.py", clock / "host_clock.ps1", clock / "RESULTS.md",
        clock / "verification.json", clock / "preflight-results.json", clock / "results-summary.json",
        qualification / "results.json", qualification / "contract.json",
        qualification / "authored-fixture.json",
        cold_proof / "results.json", cold_proof / "contract.json", cold_proof / "cold_review.py",
        *sorted((qualification / "methods").glob("*.py")), *sorted(HERE.glob("*.py")),
        ROOT / "pyproject.toml", HERE / "README.md"]
    for directory in ("timing-preflight-01", "timing-traversal-01"):
        for name in ("contract.json", "results.json"):
            p = PRIVATE / directory / name
            assert digest(p) == timing_proof["private_artifact_sha256"][directory][name]
            evidence.append(p)
    wheel = next((PRIVATE / "runtime/wheels").glob("*.whl"))
    evidence.append(wheel)
    for p in evidence:
        bindings[str(p)] = digest(p)
    installed_files = {str(p): digest(p) for p in sorted(installed.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}
    assert len(list(installed.rglob("*.py"))) == len(source) == 112
    manifest = dict(format="upgradepilot-native-product-execution-manifest/1", date="2026-11-06",
        state="prepared_for_review_not_executed", separate_live_activation_required=True,
        proof_class="prospective_native_normal_product_live_source_capture",
        repository_source_commit=subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        repository_tree=subprocess.check_output(["git", "rev-parse", "HEAD^{tree}"], cwd=ROOT, text=True).strip(),
        product_source_commit="dcee66e4", installed=str(installed), wheel_sha256=digest(wheel),
        interpreter=dict(invocation=sys.executable, resolved=str(Path(sys.executable).resolve()), version=sys.version),
        dependencies=dependencies, dependency_isolation=False,
        installed_files_sha256=installed_files, bound_files_sha256=bindings,
        argv=[sys.executable, *review["normal_product"]["proposed_post_repair_argv"]],
        credential_source=review["authentication"]["credential_source"], credential_value_read_during_preparation=False,
        environment=dict(product_path="bound installed directory only; existing venv dependencies reused",
            removed=["GITHUB_TOKEN (replaced only on activated launch)", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
                "http_proxy", "https_proxy", "all_proxy", "PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP", "PYTHONINSPECT"],
            python_no_user_site=True, python_dont_write_bytecode=True),
        destinations={k: review["retention"][k] for k in ("product_attempt", "task_review")},
        outer_host_limit_seconds=900, clock_directory=str(clock),
        contract_corrections=["40/64-hex existing validator supersedes original40-only proposal",
            "Guard forwarding is implemented and qualified; old missing-parser descriptions remain historical",
            "Independent host timing qualification completed; measured raw access is expensive and optional for the task"],
        acquisition_policy=review["acquisition_policy"], source_limits=review["source_limits"],
        analysis_limits=review["analysis_limits"], correspondence_limits=review["correspondence_limits"],
        representation_limits=review["representation_limits"], retry=review["retry"], maintainer_task=review["maintainer_task"],
        task_execution_order=["direct bounded original-source baseline", "saved report plus original-source navigation"],
        reviewer_exposure="Implementing assistant already exposed to case and expected outcomes; assisted engineering review only, not independent human benefit/mastery.",
        method_qualification=dict(results=str(qualification / "results.json"), controlled_github=45, controlled_provider=55,
            controlled_exact_native_and_report_source_recovery=True, live_auth_validity="unverified", live_account_quota="unverified"),
        access_cost_disposition="Existing report/source task first; necessary paging/cost counts. Repair inaccessible evidence/hidden premises; general optimization deferred.",
        failure_rules="No automatic retry/cap enlargement/case switch. Preserve nonzero/timeout/interrupt and exact publication uncertainty; inspect earned revision only.",
        transport=review["transport"], reserved_qualification_attempt_id=review["reserved_qualification_attempt_id"])
    write_json(manifest_path, manifest)
    print(json.dumps(dict(outcome="manifest_bound_for_review", product_files=len(source), installed_files=len(installed_files),
        dependencies=len(dependencies), bound_files=len(bindings), provider_calls=0, credential_value_read=False)))


if __name__ == "__main__":
    main()
