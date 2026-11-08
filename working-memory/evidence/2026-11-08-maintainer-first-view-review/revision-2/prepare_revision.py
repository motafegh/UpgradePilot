"""Copy verified original reviewer views into a new owner-only revision."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat


HERE = Path(__file__).resolve().parent
FOCUS = {
    "httpx": b"Review topic: caller/signature fit\n",
    "opencv": b"Review topic: published artifacts and target applicability\n",
    "soup-sieve": b"Review topic: upstream Python support evidence\n",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def private_entries(path: Path) -> set[str]:
    status = path.lstat()
    if not stat.S_ISDIR(status.st_mode) or stat.S_IMODE(status.st_mode) != 0o700:
        raise ValueError(f"Expected a private directory at {path}")
    if status.st_uid != os.getuid():
        raise ValueError(f"Unexpected directory owner at {path}")
    return {entry.name for entry in path.iterdir()}


def checked_bytes(path: Path, expected: str) -> bytes:
    status = path.lstat()
    if not stat.S_ISREG(status.st_mode) or stat.S_IMODE(status.st_mode) != 0o600:
        raise ValueError(f"Expected a private regular file at {path}")
    if status.st_uid != os.getuid():
        raise ValueError(f"Unexpected file owner at {path}")
    content = path.read_bytes()
    if sha256(content) != expected:
        raise ValueError(f"Receipt hash mismatch at {path}")
    return content


def verify_entries(path: Path, expected: set[str]) -> None:
    if private_entries(path) != expected:
        raise ValueError(f"Unexpected packet entries at {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path, help="existing owner-only packet")
    parser.add_argument("output", type=Path, help="new owner-only packet directory")
    args = parser.parse_args()

    original_receipt = (HERE.parent / "receipt.json").read_bytes()
    receipt = json.loads(original_receipt)
    allocation = receipt["allocation"]
    verify_entries(args.original, set(allocation))
    task = (HERE / "REVIEWER_TASK.md").read_bytes()
    files = {}
    for slot, assignments in allocation.items():
        reviewer = args.original / slot
        case_dirs = {
            f"{index:02d}-{name}": (name, condition)
            for index, (name, condition) in enumerate(assignments, 1)
        }
        verify_entries(reviewer, {"TASK.md", *case_dirs})
        checked_bytes(reviewer / "TASK.md", receipt["reviewer_task_sha256"])
        files[Path(slot) / "TASK.md"] = task
        for directory, (name, condition) in case_dirs.items():
            case = reviewer / directory
            case_receipt = receipt["cases"][name]
            source_hashes = {
                f"{source_id}.txt": digest
                for source_id, digest in case_receipt["original_text_views"].items()
            }
            verify_entries(case, {"report.txt", "sources"})
            verify_entries(case / "sources", set(source_hashes))
            prefix = Path(slot) / directory
            files[prefix / "report.txt"] = checked_bytes(
                case / "report.txt", case_receipt["views"][condition],
            )
            files[prefix / "FOCUS.txt"] = FOCUS[name]
            files[prefix / "sources"] = None
            for filename, digest in source_hashes.items():
                files[prefix / "sources" / filename] = checked_bytes(
                    case / "sources" / filename, digest,
                )

    os.umask(0o077)
    args.output.mkdir(mode=0o700)
    for relative, content in files.items():
        destination = args.output / relative
        if content is None:
            destination.mkdir(parents=True)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)

    print(json.dumps({
        "status": "prepared_local_only",
        "revision": 2,
        "original_receipt_sha256": sha256(original_receipt),
        "assembly_sha256": sha256(Path(__file__).read_bytes()),
        "operator_protocol_sha256": sha256((HERE / "OPERATOR_PROTOCOL.md").read_bytes()),
        "reviewer_task_sha256": sha256(task),
        "focus_sha256": {name: sha256(content) for name, content in FOCUS.items()},
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
