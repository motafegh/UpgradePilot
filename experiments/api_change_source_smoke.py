"""Anonymous source-component smoke; no PR, target or model acceptance claim.

Run from repository root with the project interpreter:
python -m experiments.api_change_source_smoke PACKAGE OLD_VERSION NEW_VERSION
Output is a public-safe manifest; source remains recoverable by exact commit/path.
"""

import argparse
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

from upgradepilot.package_identity import normalize_package_name
from upgradepilot.upstream.interval import DependencyReleaseInterval

from .api_change_source_acquisition import (
    DeclaredReleaseWindow,
    DeclaredReleaseWindowAcquirer,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package")
    parser.add_argument("old")
    parser.add_argument("proposed")
    args = parser.parse_args()
    runner = DeclaredReleaseWindowAcquirer()
    result = runner.acquire(
        DependencyReleaseInterval(
            args.package, normalize_package_name(args.package), args.old, args.proposed
        )
    )
    manifest = {
        "source_component_sha256": hashlib.sha256(
            Path(__file__).with_name("api_change_source_acquisition.py").read_bytes()
        ).hexdigest(),
        "input": vars(args),
        "timestamp": datetime.now(UTC).isoformat(),
        "auth": "anonymous",
        "github_requests": runner.session.github_requests,
        "proof": "live source acquisition only; no PR/target/model/semantic evaluation",
        "limits": {
            "github_requests": 50,
            "crossed_releases": 10,
            "window_characters": 20000,
        },
    }
    if isinstance(result, DeclaredReleaseWindow):
        manifest.update(
            {
                "state": "available",
                "basis": result.association.basis,
                "repository": result.association.repository,
                "provenance_states": [
                    a.provenance_result.state for a in result.release_associations
                ],
                "release_metadata_urls": [
                    a.release.source_url for a in result.release_associations
                ],
                "release_index_url": result.release_index.source_url,
                "crossed_versions": result.ordered_versions,
                "ignored_index_versions": result.ignored_index_versions,
                "commit": result.file.revision,
                "path": result.file.path,
                "full_source_sha256": result.full_text_sha256,
                "window_sha256": result.window_sha256,
                "sections": [
                    {
                        "version": s.version,
                        "start_line": s.start_line,
                        "start_offset": s.start_offset,
                        "end_offset": s.end_offset,
                        "characters": len(s.text),
                    }
                    for s in result.sections
                ],
                "tag_problems": [
                    {"state": p.state, "tag": p.requested_tag, "detail": p.detail}
                    for p in result.tag_problems
                ],
                "coverage": result.coverage,
            }
        )
    else:
        manifest.update(
            {
                "state": "incomplete",
                "stage": result.stage,
                "reason": result.reason,
                "detail": result.detail,
            }
        )
    print(json.dumps(manifest, indent=2))
    return 0 if isinstance(result, DeclaredReleaseWindow) else 1


if __name__ == "__main__":
    raise SystemExit(main())
