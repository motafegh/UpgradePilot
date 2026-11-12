#!/usr/bin/env bash
# Explicit, single-attempt local qualification of the opt-in source + CI profile.
# Writes only to a private directory outside Git; never prints token or signed URLs.
set -euo pipefail

ROOT="$(git -C "$(dirname "${BASH_SOURCE[0]}")" rev-parse --show-toplevel)"
TOKEN_FILE="$HOME/.config/upgradepilot/github-token"
if [[ ! -s "$TOKEN_FILE" ]]; then
  echo "Credential unavailable: owner-only UpgradePilot token file missing or empty."
  exit 2
fi
mode="$(stat -c '%a' "$TOKEN_FILE")"
if (( (8#$mode & 0077) != 0 )); then
  echo "Credential file permissions are not owner-only; refusing to run."
  exit 2
fi
PRIVATE_ROOT="$HOME/.local/share/upgradepilot"
mkdir -p "$PRIVATE_ROOT"
RESULT="$(mktemp -d "$PRIVATE_ROOT/av-tracer-native-ci-2026-11-12.XXXXXXXX")"

# Reuse the existing PyPI proxy, with direct GitHub/Actions storage routing.
# The explicit token applies only to the scoped child process, never to Git output.
if (
  cd "$ROOT"
  GITHUB_TOKEN="$(cat "$TOKEN_FILE")" \
  NO_PROXY="api.github.com,.blob.core.windows.net" \
  no_proxy="api.github.com,.blob.core.windows.net" \
  PYTHONPATH=src .venv/bin/upgradepilot \
    ivaronkun-Ahey/AV-Tracer 11 \
    --evidence-profile caller-signature-ci \
    --github-auth token-env \
    --expected-base 527a004918c0f825e97c3583404242605fd58ec2 \
    --expected-head 25e7205f39103456e7efbc4e9f503f3debc7b5d8 \
    --source-github-requests 56 \
    --ci-run-id 41416124208 \
    --ci-run-attempt 1 \
    --ci-job-id 125180284415 \
    --workspace-store "$RESULT/store" \
    --save-report "$RESULT/report.json"
) > "$RESULT/first-view.txt" 2>&1; then
  status=0
else
  status=$?
fi

printf 'Exit code: %d\nPrivate results: %s\n' "$status" "$RESULT"
if [[ -f "$RESULT/report.json" ]]; then
  (
    cd "$ROOT"
    PYTHONPATH=src .venv/bin/python - "$RESULT/report.json" <<'PY'
import sys
from upgradepilot.report_file import read_report
report = read_report(sys.argv[1])
ci = next((a for a in report.assessments if a.assessment_id == "ci-job-log"), None)
print("CI log result:", ci.state if ci else "not retained")
print("Source witnesses:", sum(
    a.assessment_id.startswith("caller-signature-comparison-")
    for a in report.assessments
))
print("Action:", report.action.state)
print("Full job-log body retained:", False)
PY
  )
else
  echo "No confirmed combined saved report; check the private first-view text."
fi
exit "$status"
