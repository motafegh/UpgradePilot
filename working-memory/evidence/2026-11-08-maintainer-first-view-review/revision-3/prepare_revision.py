"""Prepare the frozen revision 2 material with matched replacement HTTPX cards."""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent / "revision-2"


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path, help="original owner-only packet")
    parser.add_argument("output", type=Path, help="new owner-only revision 3 directory")
    args = parser.parse_args()

    previous_receipt = (PREVIOUS / "receipt.json").read_bytes()
    card = (HERE / "HTTPX_FOCUS.txt").read_bytes()
    allocation = json.loads((HERE.parent / "receipt.json").read_bytes())["allocation"]
    revision_2 = subprocess.check_output([
        sys.executable, str(PREVIOUS / "prepare_revision.py"),
        str(args.original), str(args.output),
    ])
    if json.loads(revision_2) != json.loads(previous_receipt):
        raise ValueError("Assembly did not reproduce the frozen revision 2 receipt")

    for slot, assignments in allocation.items():
        for index, (case, _) in enumerate(assignments, 1):
            if case == "httpx":
                (args.output / slot / f"{index:02d}-{case}" / "FOCUS.txt").write_bytes(card)

    print(json.dumps({
        "revision": 3,
        "status": "prepared_local_only",
        "revision_2_receipt_sha256": sha256(previous_receipt),
        "assembly_sha256": sha256(Path(__file__).read_bytes()),
        "operator_protocol_sha256": sha256((HERE / "OPERATOR_PROTOCOL.md").read_bytes()),
        "httpx_focus_sha256": sha256(card),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
