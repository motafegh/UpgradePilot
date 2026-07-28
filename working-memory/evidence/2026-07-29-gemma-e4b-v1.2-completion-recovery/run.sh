#!/usr/bin/env bash
# Execute the authorized one-response Gemma E4B v1.2 completion recovery.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "Run this command from inside the UpgradePilot repository." >&2
  exit 1
fi

EVIDENCE="$REPO_ROOT/working-memory/evidence/2026-07-29-gemma-e4b-v1.2-completion-recovery"
DIAGNOSTIC="$EVIDENCE/diagnostic.py"
RESULT="$REPO_ROOT/working-memory/2026-07-29_B2-gemma-e4b-v1.2-completion-recovery-result.md"
LMS_EXE="${LMS_EXE:-/mnt/c/Users/lenovo/.cache/lm-studio/bin/lms.exe}"
export LMS_EXE

if [[ -x "$REPO_ROOT/.venv/bin/python3" ]]; then
  PYTHON="$REPO_ROOT/.venv/bin/python3"
elif [[ -n "${VIRTUAL_ENV:-}" && -x "$VIRTUAL_ENV/bin/python3" ]]; then
  PYTHON="$VIRTUAL_ENV/bin/python3"
else
  PYTHON="$(command -v python3)"
fi

if [[ -e "$EVIDENCE/run-summary.txt" || -d "$EVIDENCE/runs" || -e "$RESULT" ]]; then
  echo "Existing completion-recovery evidence was found and will not be overwritten." >&2
  echo "Preserve the first result and push it for review." >&2
  exit 1
fi

mkdir -p "$EVIDENCE/logs"
cd "$REPO_ROOT"
git status --short --branch > "$EVIDENCE/repository-status-before.txt"

loaded=0
input_log_pid=""
stats_log_pid=""
unload_rc=99
workflow_rc=0

stop_logs() {
  local pid
  for pid in "$input_log_pid" "$stats_log_pid"; do
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
      wait "$pid" 2>/dev/null || true
    fi
  done
}

cleanup_model() {
  stop_logs
  if [[ "$loaded" -eq 1 ]]; then
    "$LMS_EXE" unload upgradepilot-gemma-e4b-smoke \
      > "$EVIDENCE/unload-output.stdout.txt" \
      2> "$EVIDENCE/unload-output.stderr.txt"
    unload_rc=$?
    printf '%s\n' "$unload_rc" > "$EVIDENCE/unload-output.exit-code.txt"
    loaded=0
  else
    unload_rc=0
    printf '%s\n' "$unload_rc" > "$EVIDENCE/unload-output.exit-code.txt"
    printf '%s\n' "Model was not marked loaded by the runner." > "$EVIDENCE/unload-output.stdout.txt"
    : > "$EVIDENCE/unload-output.stderr.txt"
  fi
  "$PYTHON" "$DIAGNOSTIC" snapshot post-unload \
    > "$EVIDENCE/post-unload-snapshot.stdout.txt" \
    2> "$EVIDENCE/post-unload-snapshot.stderr.txt" || true
}

trap cleanup_model EXIT

run_workflow() {
  "$PYTHON" -m py_compile "$DIAGNOSTIC" || return 1
  "$PYTHON" "$DIAGNOSTIC" freeze || return 1
  "$PYTHON" "$DIAGNOSTIC" self-test || return 1
  "$PYTHON" "$DIAGNOSTIC" preflight || return 1

  ss -ltnp > "$EVIDENCE/server-listener.txt" 2>&1 || true
  "$PYTHON" "$DIAGNOSTIC" snapshot pre-load || return 1

  "$LMS_EXE" load gemma-4-e4b-it-ud \
    --context-length 4096 \
    --gpu max \
    --parallel 1 \
    --ttl 900 \
    --identifier upgradepilot-gemma-e4b-smoke \
    --no-speculative-draft-mtp \
    --no-speculative-draft-simple \
    -y \
    > "$EVIDENCE/load-output.stdout.txt" \
    2> "$EVIDENCE/load-output.stderr.txt"
  local load_rc=$?
  printf '%s\n' "$load_rc" > "$EVIDENCE/load-output.exit-code.txt"
  if [[ "$load_rc" -ne 0 ]]; then
    return 1
  fi
  loaded=1

  "$PYTHON" "$DIAGNOSTIC" snapshot post-load || return 1

  "$LMS_EXE" log stream --source model --filter input,output --json \
    > "$EVIDENCE/logs/model-input-output.jsonl" \
    2> "$EVIDENCE/logs/model-input-output.stderr.txt" &
  input_log_pid=$!
  "$LMS_EXE" log stream --source model --filter output --stats \
    > "$EVIDENCE/logs/model-stats.txt" \
    2> "$EVIDENCE/logs/model-stats.stderr.txt" &
  stats_log_pid=$!
  sleep 1

  "$PYTHON" "$DIAGNOSTIC" run
  local diagnostic_rc=$?
  printf '%s\n' "$diagnostic_rc" > "$EVIDENCE/diagnostic.exit-code.txt"
  "$PYTHON" "$DIAGNOSTIC" snapshot post-diagnostic || true
  return "$diagnostic_rc"
}

run_workflow
workflow_rc=$?
printf '%s\n' "$workflow_rc" > "$EVIDENCE/workflow.exit-code.txt"

cleanup_model
trap - EXIT

"$PYTHON" -m unittest discover -s tests -v \
  > "$EVIDENCE/product-tests.stdout.txt" \
  2> "$EVIDENCE/product-tests.stderr.txt"
product_test_rc=$?
printf '%s\n' "$product_test_rc" > "$EVIDENCE/product-tests.exit-code.txt"

git status --short --branch > "$EVIDENCE/repository-status-after.txt"

cat > "$EVIDENCE/run-summary.txt" <<EOF
workflow_exit=$workflow_rc
unload_exit=$unload_rc
product_tests_exit=$product_test_rc
python=$PYTHON
lms_exe=$LMS_EXE
completed_at=$(date --iso-8601=seconds)
EOF

"$PYTHON" "$DIAGNOSTIC" report
"$PYTHON" "$DIAGNOSTIC" manifest

echo
echo "Completion-recovery execution and evidence capture finished."
echo "Result record: $RESULT"
echo "Evidence directory: $EVIDENCE"
echo "MEMORY.md was not changed. Push the result and evidence for independent review."

if [[ "$workflow_rc" -ne 0 || "$unload_rc" -ne 0 || "$product_test_rc" -ne 0 ]]; then
  echo "An infrastructure, resource-guard, restoration, or product-test check failed." >&2
  echo "Preserve the evidence and do not rerun automatically." >&2
  exit 1
fi

exit 0
