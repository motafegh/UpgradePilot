"""Opt-in PR → source proposals → offline saved recovery experiment.

Run with `run REPOSITORY PR --save PATH`; inspect with `open PATH`.
The default local provider refuses inference without measured request capacity.
Live evaluation supplies that evidence through the Python provider seam. Opening
a packet never calls a provider, reacquires a source or re-explores adapters.
"""

from __future__ import annotations

import argparse
import json
import os
from dataclasses import asdict
from pathlib import Path

from upgradepilot.upstream.interval import DependencyReleaseInterval

from .api_adapter_context_replay import decode_adapter_seed
from .api_change_interpretation import (
    ROLE,
    LocalInterpretationProvider,
    decode_proposals,
    interpret_acquired_source,
    packet_hash,
    prepare_request,
    source_input_from_projection,
    strict_json,
)
from .api_change_source_acquisition import AcquisitionProblem, TrialPublicSession
from .api_target_context_smoke import acquire_public_pr_context, trial_manifest

MAX_SAVED_BYTES = 8 * 1024 * 1024
PACKET_KIND = "api-change-interpretation-trial"
SUCCESS_STATES = {"observations_returned", "no_observations_returned"}
FAILURE_STATES = {
    "input_problem",
    "provider_problem",
    "context_problem",
    "contract_problem",
    "grounding_problem",
}


def dependency_interval(dependency: dict) -> dict:
    return asdict(
        DependencyReleaseInterval(
            **{
                key: dependency[key]
                for key in (
                    "package",
                    "normalized_package",
                    "old_version",
                    "proposed_version",
                )
            }
        )
    )


def run_interpretation_trial(
    repository: str, number: int, *, provider=None, session=None, **acquirers
) -> dict:
    session = session if session is not None else TrialPublicSession()
    acquired = acquire_public_pr_context(
        repository, number, session=session, **acquirers
    )
    context = trial_manifest(acquired, session)
    interpretation = None
    if not isinstance(acquired, AcquisitionProblem):
        interpretation = interpret_acquired_source(
            acquired.upstream,
            dependency_interval(context["dependency"]),
            provider if provider is not None else LocalInterpretationProvider(),
        )
    packet = {
        "artifact_kind": PACKET_KIND,
        "packet_version": 1,
        "proof": "experiment proposals and controlled/source correspondence; no semantic, target-impact, product or maintainer acceptance",
        "context": context,
        "interpretation": interpretation,
    }
    return {**packet, "packet_sha256": packet_hash(packet)}


def decode_saved_trial(text: str) -> dict:
    """Independently reconstruct citations from saved acquisition evidence.

    Hashes detect packet consistency, not authenticity. Recomputed outer hashes
    cannot justify changed input maps or model-supplied quotations. The existing
    pure target-seed decoder owns target/head/binding checks; no fresh exploration.
    """
    try:
        packet = strict_json(text, max_bytes=MAX_SAVED_BYTES)
        if set(packet) != {
            "artifact_kind",
            "packet_version",
            "proof",
            "context",
            "interpretation",
            "packet_sha256",
        }:
            raise ValueError("unexpected saved packet fields")
        if (
            packet["artifact_kind"] != PACKET_KIND
            or type(packet["packet_version"]) is not int
            or packet["packet_version"] != 1
        ):
            raise ValueError("unsupported saved packet version/kind")
        body = {key: value for key, value in packet.items() if key != "packet_sha256"}
        if packet_hash(body) != packet["packet_sha256"]:
            raise ValueError("saved packet digest mismatch")
        context, interpretation = packet["context"], packet["interpretation"]
        if context["state"] == "incomplete":
            if interpretation is not None:
                raise ValueError("interpretation without acquired context")
            return packet
        decode_adapter_seed(context)
        if (
            set(interpretation)
            != {
                "role_version",
                "state",
                "source_input",
                "method",
                "observations",
                "unassessed",
                "problem",
            }
            or interpretation["role_version"] != ROLE
        ):
            raise ValueError("unexpected interpretation envelope")
        try:
            expected_input = source_input_from_projection(
                context["upstream"], dependency_interval(context["dependency"])
            )
        except (ValueError, KeyError, TypeError, AttributeError):
            if (
                interpretation["source_input"] is not None
                or interpretation["state"] != "input_problem"
                or interpretation["problem"]["reason"] != "invalid_source_relationships"
            ):
                raise ValueError("invalid saved source relationships") from None
            expected_input = None
        if packet_hash(expected_input) != packet_hash(interpretation["source_input"]):
            raise ValueError("saved input map differs from acquired source")
        method = interpretation["method"]
        if expected_input is None and method is not None:
            raise ValueError("request identity without valid source input")
        if method is not None:
            # Historical settings remain recoverable after the evaluated default
            # changes. Re-rendering still checks their exact request digest.
            expected_request = prepare_request(
                expected_input, max_output_tokens=method["max_output_tokens"]
            )
            expected_method = expected_request.method
            if set(method) != {*expected_method, "provider"}:
                raise ValueError("unexpected method identity fields")
            # Code digests are historical execution identity, not current-code equality.
            for key in expected_method.keys() - {"interpreter_code_sha256"}:
                if method[key] != expected_method[key]:
                    raise ValueError("saved method/request identity mismatch")
            if not isinstance(method["provider"], dict) or not method["provider"].get(
                "kind"
            ):
                raise ValueError("missing provider proof identity")
        state = interpretation["state"]
        if state in SUCCESS_STATES:
            if (
                method is None
                or interpretation["problem"] is not None
                or not expected_input["sections"]
            ):
                raise ValueError("success without source/method identity")
            output = {
                key: [
                    {k: v for k, v in item.items() if k != "evidence"}
                    for item in interpretation[key]
                ]
                for key in ("observations", "unassessed")
            }
            recovered = decode_proposals(
                output,
                expected_input,
                schema=expected_request.payload["response_format"]["json_schema"][
                    "schema"
                ],
            )
            if any(recovered[key] != interpretation[key] for key in recovered):
                raise ValueError("saved evidence differs from reconstructed spans")
            if (state == "observations_returned") != bool(recovered["observations"]):
                raise ValueError("saved result state disagrees with observations")
        elif state in FAILURE_STATES:
            problem = interpretation["problem"]
            if (
                interpretation["observations"]
                or interpretation["unassessed"]
                or set(problem) != {"stage", "reason"}
                or problem["stage"] != state
                or not isinstance(problem["reason"], str)
                or not problem["reason"]
            ):
                raise ValueError("malformed failed interpretation")
            if (
                state in {"provider_problem", "context_problem", "grounding_problem"}
                and method is None
            ):
                raise ValueError("provider/grounding failure lacks request identity")
            if state == "input_problem":
                if method is not None:
                    raise ValueError("input failure after request preparation")
                if expected_input is not None and (
                    expected_input["sections"]
                    or problem["reason"] != "no_retained_source_text"
                ):
                    raise ValueError("input failure disagrees with retained source")
            elif (
                method is None and problem["reason"] != "frozen_producer_assets_invalid"
            ):
                raise ValueError("output failure before request preparation")
        else:
            raise ValueError("unknown interpretation state")
        return packet
    except (KeyError, TypeError, AttributeError, RecursionError) as exc:
        raise ValueError("malformed saved interpretation packet") from exc


def read_saved_trial(path: Path) -> dict:
    with path.open("rb") as stream:
        raw = stream.read(MAX_SAVED_BYTES + 1)
    if len(raw) > MAX_SAVED_BYTES:
        raise ValueError("saved packet byte limit exceeded")
    return decode_saved_trial(raw.decode("utf-8"))


def save_trial(packet: dict, path: Path) -> None:
    text = json.dumps(
        packet, ensure_ascii=False, allow_nan=False, separators=(",", ":")
    )
    decode_saved_trial(text)
    # A new result must not overwrite a prior run. Raw replies are never saved.
    with path.open("x", encoding="utf-8") as stream:
        stream.write(text + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser(
        "run", help="acquire ordinary PR context and opt in to interpretation"
    )
    run.add_argument("repository")
    run.add_argument("pull_number", type=int)
    run.add_argument("--save", type=Path)
    run.add_argument(
        "--github-auth", choices=("anonymous", "token-env"), default="anonymous"
    )
    reopen = commands.add_parser("open", help="recover source-linked proposals offline")
    reopen.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "open":
            packet = read_saved_trial(args.path)
        else:
            token = (
                os.environ.get("GITHUB_TOKEN")
                if args.github_auth == "token-env"
                else None
            )
            if args.github_auth == "token-env" and not token:
                parser.error("token-env requires GITHUB_TOKEN")
            packet = run_interpretation_trial(
                args.repository,
                args.pull_number,
                session=TrialPublicSession(token=token),
            )
            if args.save:
                save_trial(packet, args.save)
        print(json.dumps(packet, ensure_ascii=False, separators=(",", ":")))
    except (ValueError, OSError) as exc:
        print(json.dumps({"state": "saved_result_problem", "reason": str(exc)}))
        return 1
    interpretation = packet["interpretation"]
    return 0 if interpretation and interpretation["state"] in SUCCESS_STATES else 1


if __name__ == "__main__":
    raise SystemExit(main())
