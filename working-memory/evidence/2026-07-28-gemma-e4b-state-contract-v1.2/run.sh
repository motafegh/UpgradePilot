#!/usr/bin/env bash
# Execute the authorized Gemma E4B state-contract v1.2 diagnostic and preserve evidence.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "Run this command from inside the UpgradePilot repository." >&2
  exit 1
fi

EVIDENCE="$REPO_ROOT/working-memory/evidence/2026-07-28-gemma-e4b-state-contract-v1.2"
DIAGNOSTIC="$EVIDENCE/diagnostic.py"
RESULT="$REPO_ROOT/working-memory/2026-07-28_B2-gemma-e4b-state-contract-v1.2-diagnostic-result.md"
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
  echo "Existing v1.2 generated evidence was found. It will not be overwritten." >&2
  echo "Preserve and push the existing run, or obtain authorization for a new dated rerun." >&2
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
    set +e
    "$LMS_EXE" unload upgradepilot-gemma-e4b-smoke \
      > "$EVIDENCE/unload-output.stdout.txt" \
      2> "$EVIDENCE/unload-output.stderr.txt"
    unload_rc=$?
    set -e
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

  set +e
  "$LMS_EXE" load gemma-4-e4b-it-ud \
    --context-length 4096 \
    --gpu max \
    --parallel 1 \
    --ttl 900 \
    --identifier upgradepilot-gemma-e4b-smoke \
    --no-speculative-draft-mtp \
    -y \
    > "$EVIDENCE/load-output.stdout.txt" \
    2> "$EVIDENCE/load-output.stderr.txt"
  local load_rc=$?
  set -e
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

  set +e
  "$PYTHON" "$DIAGNOSTIC" gate-a
  local gate_a_rc=$?
  set -e
  printf '%s\n' "$gate_a_rc" > "$EVIDENCE/gate-a.exit-code.txt"
  if [[ "$gate_a_rc" -ne 0 ]]; then
    "$PYTHON" "$DIAGNOSTIC" snapshot post-diagnostic || true
    return 0
  fi

  set +e
  "$PYTHON" "$DIAGNOSTIC" gate-b
  local gate_b_rc=$?
  set -e
  printf '%s\n' "$gate_b_rc" > "$EVIDENCE/gate-b.exit-code.txt"
  if [[ "$gate_b_rc" -ne 0 ]]; then
    "$PYTHON" "$DIAGNOSTIC" snapshot post-diagnostic || true
    return 0
  fi

  set +e
  "$PYTHON" "$DIAGNOSTIC" gate-c
  local gate_c_rc=$?
  set -e
  printf '%s\n' "$gate_c_rc" > "$EVIDENCE/gate-c.exit-code.txt"
  "$PYTHON" "$DIAGNOSTIC" snapshot post-diagnostic || true
  return 0
}

set +e
run_workflow
workflow_rc=$?
set -e
printf '%s\n' "$workflow_rc" > "$EVIDENCE/workflow.exit-code.txt"

cleanup_model
trap - EXIT

set +e
"$PYTHON" -m unittest discover -s tests -v \
  > "$EVIDENCE/product-tests.stdout.txt" \
  2> "$EVIDENCE/product-tests.stderr.txt"
product_test_rc=$?
set -e
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
echo "Diagnostic execution and evidence capture finished."
echo "Result record: $RESULT"
echo "Evidence directory: $EVIDENCE"
echo "MEMORY.md was not changed. Push the result and evidence for independent review."

if [[ "$workflow_rc" -ne 0 || "$unload_rc" -ne 0 || "$product_test_rc" -ne 0 ]]; then
  echo "One infrastructure, restoration, or product-test check failed. Push the evidence unchanged for review." >&2
  exit 1
fi
exit 0
