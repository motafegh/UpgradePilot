"""Prepare and execute the known-development two-case local feasibility pilot.

Preparation acquires pinned public text without extracting or executing archives;
bounded historical CI captures keep their explicit capture authority. Execution
requires an already-loaded model plus the optional isolated SDK. Raw corpus,
requests and responses remain under ignored .tmp; reviewed evidence is separate.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import zipfile
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests

from .broader_agency_local import LocalJSONActionProvider
from .broader_agency_trial import run_investigation_trial
from .broader_agency_workspace import (
    SourceDocument,
    SourceWorkspace,
    digest,
    strict_json,
)

ROOT = Path(__file__).resolve().parents[1]
CASE_SPECS = (
    {
        "case_id": "development-httpx-framework-ci",
        "repository": "Aidan-Wallace/kubernetes-dashboard-token-api",
        "base": "b065646e4b7b894964567950f9ad770b02c136c2",
        "head": "391508134b083b8f54461c0b576e8f7985c6ecb4",
        "dependency": "httpx",
        "old": "0.27.2",
        "proposed": "0.28.1",
        "scenario": "S002-kubernetes-dashboard-token-api-httpx-0.27.2-to-0.28.1",
        "upstream": [
            ("httpx-old", "encode/httpx", "0.27.2"),
            ("httpx-new", "encode/httpx", "0.28.1"),
            ("starlette-old", "Kludex/starlette", "0.36.3"),
            ("starlette-new", "Kludex/starlette", "0.37.2"),
            ("fastapi-reference", "fastapi/fastapi", "0.115.2"),
        ],
        "observations": [
            "E16-actions-run-and-job.json",
            "E19-docker-log-retrieval-error.json",
        ],
    },
    {
        "case_id": "development-glyphslib-pytest-stopping",
        "repository": "googlefonts/glyphsLib",
        "base": "044f19e4b1437bfc4343592486f4e3c6040306d9",
        "head": "f3cda8a94600e58d27f1bc17c99b7693718b6350",
        "dependency": "pytest",
        "old": "9.0.2",
        "proposed": "9.0.3",
        "scenario": "S004-glyphslib-pytest-9.0.2-to-9.0.3",
        "upstream": [
            ("pytest-old", "pytest-dev/pytest", "9.0.2"),
            ("pytest-new", "pytest-dev/pytest", "9.0.3"),
        ],
        "observations": ["ev-005-ci-results.json"],
    },
)
SOURCE_FILES = [
    "broader_agency_workspace.py",
    "broader_agency_trial.py",
    "broader_agency_local.py",
    "broader_agency_pilot.py",
]
TEXT_SUFFIXES = {
    ".py",
    ".md",
    ".rst",
    ".txt",
    ".toml",
    ".yaml",
    ".yml",
    ".json",
    ".ini",
    ".cfg",
    ".lock",
    ".sh",
    ".html",
    ".in",
    ".csv",
    ".xml",
}


def code_identities() -> dict:
    return {
        name: hashlib.sha256((ROOT / "experiments" / name).read_bytes()).hexdigest()
        for name in SOURCE_FILES
    }


def public_bytes(session, url, maximum):
    with session.get(url, timeout=30, stream=True) as response:
        response.raise_for_status()
        content = bytearray()
        for chunk in response.iter_content(65536):
            content.extend(chunk)
            if len(content) > maximum:
                raise ValueError("public response exceeds byte ceiling")
    return bytes(content)


def acquire_repository_text(
    session, source_id, repository, revision
) -> tuple[list[SourceDocument], dict]:
    """Resolve tags to commits, retain broad UTF-8 text, and expose capture limits.

    Archive members never reach the host filesystem. Nontext, oversized and
    unsafe paths are recorded omissions, rather than implied source absence.
    """
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        metadata = strict_json(
            public_bytes(
                session,
                f"https://api.github.com/repos/{repository}/commits/{revision}",
                1_048_576,
            ).decode()
        )
        revision = metadata["sha"]
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("repository revision is not a commit")
    url = f"https://codeload.github.com/{repository}/zip/{revision}"
    archive = public_bytes(session, url, 32 * 1024 * 1024)
    documents = []
    omissions = []
    retained = 0
    with zipfile.ZipFile(io.BytesIO(archive)) as tree:
        if len(tree.infolist()) > 20_000:
            raise ValueError("archive member ceiling exceeded")
        for member in tree.infolist():
            path = PurePosixPath(member.filename)
            relative = PurePosixPath(*path.parts[1:])
            if member.is_dir():
                continue
            reason = None
            if path.is_absolute() or ".." in path.parts or len(path.parts) < 2:
                reason = "unsafe archive path"
            elif relative.suffix.lower() not in TEXT_SUFFIXES and relative.name not in {
                "Dockerfile",
                "Makefile",
                "LICENSE",
                "CHANGELOG",
                "README",
            }:
                reason = "outside declared text-file inventory"
            elif (
                member.file_size > 2 * 1024 * 1024
                or retained + member.file_size > 32 * 1024 * 1024
            ):
                reason = "text capture byte ceiling"
            if reason:
                omissions.append(
                    {"path": str(relative), "reason": reason, "size": member.file_size}
                )
                continue
            try:
                # ZIP permits skipping irrelevant members without expanding
                # binary fixture payloads. Bound selected text before reading.
                with tree.open(member) as stream:
                    raw = stream.read(2 * 1024 * 1024 + 1)
                if len(raw) > 2 * 1024 * 1024:
                    raise ValueError("expanded text exceeds declared ceiling")
                text = raw.decode("utf-8")
                if "\x00" in text:
                    raise UnicodeError("binary NUL")
            except UnicodeError:
                omissions.append(
                    {
                        "path": str(relative),
                        "reason": "non UTF-8 text",
                        "size": member.file_size,
                    }
                )
                continue
            retained += len(raw)
            documents.append(
                SourceDocument(
                    source_id,
                    str(relative),
                    text,
                    {
                        "repository": repository,
                        "revision": revision,
                        "path": str(relative),
                        "basis": "fresh public exact-commit archive",
                    },
                )
            )
    source = {
        "source_id": source_id,
        "repository": repository,
        "revision": revision,
        "file_count": len(documents),
        "scope": "broad retained UTF-8 text; declared file types/byte limits; not installed runtime",
        "omitted_file_count": len(omissions),
    }
    receipt = {
        **source,
        "url": url,
        "archive_sha256": hashlib.sha256(archive).hexdigest(),
        "retained_bytes": retained,
        "omissions": omissions,
    }
    return documents, receipt


def acquire_repository_tree_text(
    session, source_id, repository, revision, blob_cache
) -> tuple[list[SourceDocument], dict]:
    """Capture the same text selection without expanding a binary-heavy archive.

    A complete exact-commit tree supplies paths/sizes/blob identities. Selected
    raw bytes must match their Git blob SHA1; repeated blobs reuse those checked
    bytes. Six independent public readers bound acquisition concurrency.
    """
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("tree capture requires an exact commit")
    url = f"https://api.github.com/repos/{repository}/git/trees/{revision}?recursive=1"
    raw_tree = public_bytes(session, url, 8 * 1024 * 1024)
    tree = strict_json(raw_tree.decode())
    if tree.get("truncated") is not False or len(tree["tree"]) > 50_000:
        raise ValueError("tree is incomplete or exceeds entry ceiling")
    selected, omissions = [], []
    retained = 0
    for row in tree["tree"]:
        if row["type"] == "tree":
            continue
        path = PurePosixPath(row["path"])
        reason = None
        if path.is_absolute() or ".." in path.parts or not path.parts:
            reason = "unsafe tree path"
        elif row["type"] != "blob" or row["mode"] not in {"100644", "100755"}:
            reason = "outside ordinary file inventory"
        elif path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {
            "Dockerfile",
            "Makefile",
            "LICENSE",
            "CHANGELOG",
            "README",
        }:
            reason = "outside declared text-file inventory"
        elif row["size"] > 2 * 1024 * 1024 or retained + row["size"] > 32 * 1024 * 1024:
            reason = "text capture byte ceiling"
        if reason:
            omissions.append(
                {"path": str(path), "reason": reason, "size": row.get("size", 0)}
            )
            continue
        retained += row["size"]
        selected.append(row)

    def fetch(row):
        raw = blob_cache.get(row["sha"])
        if raw is None:
            with requests.Session() as reader:
                reader.trust_env = False
                reader.headers["User-Agent"] = "UpgradePilot-public-research"
                raw = public_bytes(
                    reader,
                    f"https://raw.githubusercontent.com/{repository}/{revision}/{quote(row['path'], safe='/')}",
                    2 * 1024 * 1024,
                )
        git_blob = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        if git_blob != row["sha"] or len(raw) != row["size"]:
            raise ValueError("raw source does not match frozen Git blob")
        return row, raw

    documents = []
    with ThreadPoolExecutor(max_workers=6) as readers:
        for row, raw in readers.map(fetch, selected):
            blob_cache[row["sha"]] = raw
            try:
                text = raw.decode("utf-8")
                if "\x00" in text:
                    raise UnicodeError("binary NUL")
            except UnicodeError:
                omissions.append(
                    {"path": row["path"], "reason": "non UTF-8 text", "size": len(raw)}
                )
                continue
            documents.append(
                SourceDocument(
                    source_id,
                    row["path"],
                    text,
                    {
                        "repository": repository,
                        "revision": revision,
                        "path": row["path"],
                        "basis": "fresh complete public commit tree and Git-blob-verified raw text",
                        "git_blob_sha1": row["sha"],
                    },
                )
            )
    receipt = {
        "source_id": source_id,
        "repository": repository,
        "revision": revision,
        "file_count": len(documents),
        "scope": "broad retained UTF-8 text; declared file types/byte limits; not installed runtime",
        "omitted_file_count": len(omissions),
        "url": url,
        "tree_response_sha256": hashlib.sha256(raw_tree).hexdigest(),
        "git_tree_sha1": tree["sha"],
        "retained_bytes": sum(len(d.text.encode()) for d in documents),
        "omissions": omissions,
    }
    return documents, receipt


def prepare_pilot(
    directory: Path, *, tree_repositories=(), reuse_captures=None
) -> dict:
    directory.mkdir(parents=True, exist_ok=False)
    captures = directory / "source-captures"
    captures.mkdir()
    session = requests.Session()
    session.trust_env = False
    session.headers["User-Agent"] = "UpgradePilot-public-research"
    cases = []
    blob_cache = {}
    try:
        for spec in CASE_SPECS:
            documents = []
            receipts = []
            specs = [
                ("target-base", spec["repository"], spec["base"]),
                ("target-proposed", spec["repository"], spec["head"]),
                *spec["upstream"],
            ]
            for source_id, repository, revision in specs:
                previous = (
                    reuse_captures
                    / "source-captures"
                    / f"{spec['case_id']}-{source_id}.json"
                    if reuse_captures
                    else None
                )
                if previous and previous.is_file():
                    raw_capture = previous.read_bytes()
                    capture = strict_json(raw_capture.decode())
                    receipt = capture["receipt"]
                    acquired = [SourceDocument(**d) for d in capture["documents"]]
                    if (
                        receipt["source_id"] != source_id
                        or receipt["repository"] != repository
                        or (
                            re.fullmatch(r"[0-9a-f]{40}", revision)
                            and receipt["revision"] != revision
                        )
                        or len(acquired) != receipt["file_count"]
                        or any(
                            d.source_id != source_id
                            or d.identity["repository"] != repository
                            or d.identity["revision"] != receipt["revision"]
                            for d in acquired
                        )
                    ):
                        raise ValueError("reused capture identity differs")
                    receipt = {
                        **receipt,
                        "reused_capture_sha256": hashlib.sha256(
                            raw_capture
                        ).hexdigest(),
                        "reuse_basis": "completed same-session exact-commit capture; bytes not reacquired",
                    }
                elif repository in tree_repositories:
                    acquired, receipt = acquire_repository_tree_text(
                        session, source_id, repository, revision, blob_cache
                    )
                else:
                    acquired, receipt = acquire_repository_text(
                        session, source_id, repository, revision
                    )
                (captures / f"{spec['case_id']}-{source_id}.json").write_text(
                    json.dumps(
                        {
                            "documents": [asdict(doc) for doc in acquired],
                            "receipt": receipt,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
                documents.extend(acquired)
                receipts.append(receipt)
                print(
                    json.dumps(
                        {
                            "acquired": spec["case_id"],
                            "source": source_id,
                            "files": len(acquired),
                        }
                    ),
                    flush=True,
                )
            for name in spec["observations"]:
                path = (
                    ROOT
                    / "product-simulation/scenarios"
                    / spec["scenario"]
                    / "artifacts/raw"
                    / name
                )
                original = path.read_text()
                value = strict_json(original)
                # Historical raw captures sometimes include investigator advice.
                # Retain observations, not those conclusion/authority annotations.
                for key in (
                    "authority_note",
                    "capture_note",
                    "retention_limit",
                    "interpretation",
                    "conclusion_note",
                ):
                    value.pop(key, None)
                identity = {
                    "repository": spec["repository"],
                    "revision": spec["head"],
                    "path": name,
                    "basis": "historical bounded public CI capture; not freshly reacquired logs",
                    "original_capture_sha256": hashlib.sha256(
                        original.encode()
                    ).hexdigest(),
                }
                documents.append(
                    SourceDocument(
                        "ci-observations", name, json.dumps(value, indent=2), identity
                    )
                )
            sources = [
                {
                    key: value
                    for key, value in receipt.items()
                    if key
                    in {
                        "source_id",
                        "repository",
                        "revision",
                        "file_count",
                        "scope",
                        "omitted_file_count",
                    }
                }
                for receipt in receipts
            ]
            sources.append(
                {
                    "source_id": "ci-observations",
                    "repository": spec["repository"],
                    "revision": spec["head"],
                    "file_count": len(spec["observations"]),
                    "scope": "historical bounded public CI captures, not full logs or resolved environments",
                }
            )
            task = {
                key: spec[key]
                for key in (
                    "case_id",
                    "repository",
                    "base",
                    "head",
                    "dependency",
                    "old",
                    "proposed",
                )
            }
            task["scope"] = (
                "known-development technical feasibility; fresh frozen public source and bounded historical CI observations"
            )
            workspace = SourceWorkspace(documents, sources)
            cases.append(
                {
                    "task": task,
                    "documents": [asdict(doc) for doc in documents],
                    "sources": sources,
                    "acquisition": receipts,
                    "corpus_sha256": workspace.identity,
                }
            )
    finally:
        session.close()
    bundle = {"cases": cases}
    (directory / "corpus.json").write_text(
        json.dumps(bundle, ensure_ascii=False) + "\n"
    )
    freeze = {
        "code": code_identities(),
        "corpus_sha256": digest(bundle),
        "case_corpus_sha256": {
            item["task"]["case_id"]: item["corpus_sha256"] for item in cases
        },
        "methods": ["fixed", "agent"],
        "interface_candidates": ["compatible-tools-v2", "native-json-v2"],
        "oracle": "not supplied to model; development review only",
    }
    (directory / "pre-inference-freeze.json").write_text(
        json.dumps(freeze, indent=2) + "\n"
    )
    return freeze


def prepare_from_frozen(directory: Path, previous: Path) -> dict:
    """Reuse unchanged model-visible corpus; bind this executable configuration."""
    bundle = strict_json((previous / "corpus.json").read_text())
    old = strict_json((previous / "pre-inference-freeze.json").read_text())
    if old["corpus_sha256"] != digest(bundle):
        raise ValueError("prior frozen corpus changed")
    for item in bundle["cases"]:
        workspace = SourceWorkspace(
            [SourceDocument(**d) for d in item["documents"]], item["sources"]
        )
        if workspace.identity != item["corpus_sha256"]:
            raise ValueError("prior source map changed")
    directory.mkdir(parents=True, exist_ok=False)
    (directory / "corpus.json").write_text(
        json.dumps(bundle, ensure_ascii=False) + "\n"
    )
    freeze = {
        "code": code_identities(),
        "corpus_sha256": digest(bundle),
        "case_corpus_sha256": {
            i["task"]["case_id"]: i["corpus_sha256"] for i in bundle["cases"]
        },
        "methods": ["fixed", "agent"],
        "interface_candidates": ["compatible-tools-v2", "native-json-v2"],
        "reuse_basis": {
            "directory": str(previous),
            "prior_code": old["code"],
            "unchanged_corpus": True,
        },
        "oracle": "not supplied to model; development review only",
    }
    (directory / "pre-inference-freeze.json").write_text(
        json.dumps(freeze, indent=2) + "\n"
    )
    return freeze


def execute_pilot(
    directory: Path,
    model,
    chat_factory,
    model_identity: dict,
    *,
    interface="compatible-tools",
    reasoning="off",
    probe_call_budget=12,
) -> dict:
    freeze = json.loads((directory / "pre-inference-freeze.json").read_text())
    bundle = json.loads((directory / "corpus.json").read_text())
    if freeze["code"] != code_identities() or freeze["corpus_sha256"] != digest(bundle):
        raise ValueError("frozen code/corpus changed; prepare a new run")
    info = model.get_info().to_dict()
    if (
        model_identity.get("key") != info["modelKey"]
        or model_identity.get("size_bytes") != info["sizeBytes"]
        or model_identity.get("path") != info["path"]
        or not re.fullmatch(r"[a-f0-9]{64}", model_identity.get("gguf_sha256", ""))
    ):
        raise ValueError("precomputed model-file identity does not match deployment")
    output = directory / (
        "execution-"
        + re.sub(r"[^a-zA-Z0-9_-]", "_", model.identifier)
        + "-"
        + interface
    )
    output.mkdir(exist_ok=False)
    provider = LocalJSONActionProvider(
        model, chat_factory, interface=interface, reasoning=reasoning
    )
    configuration = provider.configuration()
    configuration["model_file_identity"] = model_identity
    configuration["model_file_hash_basis"] = (
        "caller-computed SHA256 before loading; model key/path/size checked here, not rehashed during inference"
    )
    (output / "deployment-freeze.json").write_text(
        json.dumps(configuration, indent=2) + "\n"
    )
    results = []
    try:
        probe = provider.harmless_probe(call_budget=probe_call_budget)
        (output / "probe.json").write_text(json.dumps(probe, indent=2) + "\n")
        if probe["outcome"] != "passed":
            result = {
                "configuration": configuration,
                "probe": probe,
                "trials": [],
                "assigned_case_trials": "not started: interface qualification failed",
            }
            (output / "result.json").write_text(json.dumps(result, indent=2) + "\n")
            return result
        for case_index, item in enumerate(bundle["cases"]):
            documents = [SourceDocument(**document) for document in item["documents"]]
            workspace = SourceWorkspace(documents, item["sources"])
            if workspace.identity != item["corpus_sha256"]:
                raise ValueError("case corpus identity changed")
            # Reverse ordering on the second case; this is formative, not a
            # randomized protected comparison or a best-of-multiple-run search.
            for method in ["fixed", "agent"] if case_index == 0 else ["agent", "fixed"]:
                result = run_investigation_trial(
                    item["task"], workspace, method, provider
                )
                results.append(result)
                (output / f"{case_index + 1}-{method}.json").write_text(
                    json.dumps(result, indent=2, ensure_ascii=False) + "\n"
                )
                print(
                    json.dumps(
                        {
                            "case": result["case_id"],
                            "method": method,
                            "outcome": result["outcome"],
                            "counters": result["counters"],
                            "elapsed_seconds": result["elapsed_seconds"],
                        }
                    ),
                    flush=True,
                )
        result = {"configuration": configuration, "probe": probe, "trials": results}
        (output / "result.json").write_text(
            json.dumps(result, indent=2, ensure_ascii=False) + "\n"
        )
        return result
    finally:
        provider.close()
        (output / "private-provider-receipts.json").write_text(
            json.dumps(provider.private_receipts, indent=2, ensure_ascii=False) + "\n"
        )
        if freeze["code"] != code_identities():
            raise ValueError("code changed during execution")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--prepare", action="store_true")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--model", default="gemma-4-e4b-it-ud")
    parser.add_argument("--model-identity", type=Path)
    parser.add_argument("--sdk-site", type=Path)
    parser.add_argument("--tree-repository", action="append", default=[])
    parser.add_argument("--reuse-captures", type=Path)
    parser.add_argument("--reuse-corpus", type=Path)
    parser.add_argument(
        "--interface",
        choices=["compatible-tools", "native-json"],
        default="compatible-tools",
    )
    parser.add_argument(
        "--reasoning", choices=["off", "on", "server-default-accounted"], default="off"
    )
    parser.add_argument("--probe-call-budget", type=int, default=12)
    args = parser.parse_args()
    if not re.fullmatch(r"[a-zA-Z0-9_-]{1,80}", args.name):
        parser.error("name must contain letters, digits, underscore or hyphen")
    if args.prepare == args.execute:
        parser.error("choose exactly one of --prepare or --execute")
    if args.execute and args.model_identity is None:
        parser.error("--execute requires --model-identity with precomputed GGUF hash")
    directory = ROOT / ".tmp/broader-agency-pilot" / args.name
    if args.prepare:
        try:
            freeze = (
                prepare_from_frozen(directory, args.reuse_corpus)
                if args.reuse_corpus
                else prepare_pilot(
                    directory,
                    tree_repositories=args.tree_repository,
                    reuse_captures=args.reuse_captures,
                )
            )
        except FileExistsError:
            # A rejected reuse must not write into another run's record.
            raise
        except Exception as error:
            if directory.is_dir():
                (directory / "preparation-problem.json").write_text(
                    json.dumps(
                        {
                            "problem": f"{type(error).__name__}: {error}",
                            "source_captures": "completed captures retained; no inference occurred",
                        },
                        indent=2,
                    )
                    + "\n"
                )
            raise
        print(
            json.dumps(
                {
                    "prepared": len(freeze["case_corpus_sha256"]),
                    "directory": str(directory),
                }
            )
        )
        return 0
    if args.sdk_site:
        sys.path.append(str(args.sdk_site.resolve()))
    for key in (
        "HTTP_PROXY",
        "HTTPS_PROXY",
        "ALL_PROXY",
        "http_proxy",
        "https_proxy",
        "all_proxy",
    ):
        os.environ.pop(key, None)
    os.environ["NO_PROXY"] = "127.0.0.1,localhost,::1"
    import lmstudio as lms

    lms.set_sync_api_timeout(30)
    with lms.Client("127.0.0.1:18080") as client:
        models = [m for m in client.llm.list_loaded() if m.identifier == args.model]
        if len(models) != 1:
            raise ValueError("exactly one requested instance must already be loaded")
        result = execute_pilot(
            directory,
            models[0],
            lms.Chat.from_history,
            strict_json(args.model_identity.read_text()),
            interface=args.interface,
            reasoning=args.reasoning,
            probe_call_budget=args.probe_call_budget,
        )
    return (
        0
        if result["probe"]["outcome"] == "passed"
        and all(t["outcome"].startswith("completed") for t in result["trials"])
        else 1
    )


if __name__ == "__main__":
    raise SystemExit(main())
