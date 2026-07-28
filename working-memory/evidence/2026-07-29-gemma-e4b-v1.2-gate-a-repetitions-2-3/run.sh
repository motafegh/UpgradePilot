#!/usr/bin/env bash
# Execute Gemma E4B state-contract v1.2 Gate A repetitions 2 and 3.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "Run this command from inside the UpgradePilot repository." >&2
  exit 1
fi

EVIDENCE="$REPO_ROOT/working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gate-a-repetitions-2-3"
DIAGNOSTIC="$EVIDENCE/diagnostic.py"
RESULT="$REPO_ROOT/working-memory/2026-07-29_B2-gemma-e4b-v1.2-gate-a-repetitions-2-3-result.md"
LMS_EXE="${LMS_EXE:-/mnt/c/Users/lenovo/.cache/lm-studio/bin/lms.exe}"
export LMS_EXE
export PYTHONDONTWRITEBYTECODE=1

if [[ -x "$REPO_ROOT/.venv/bin/python3" ]]; then
  PYTHON="$REPO_ROOT/.venv/bin/python3"
elif [[ -n "${VIRTUAL_ENV:-}" && -x "$VIRTUAL_ENV/bin/python3" ]]; then
  PYTHON="$VIRTUAL_ENV/bin/python3"
else
  PYTHON="$(command -v python3)"
fi

if [[ -e "$EVIDENCE/run-summary.txt" || -d "$EVIDENCE/runs" || -e "$RESULT" ]]; then
  echo "Existing Gate A repetition evidence was found and will not be overwritten." >&2
  echo "Preserve and push the first result for independent review." >&2
  exit 1
fi

mkdir -p "$EVIDENCE/logs"
cd "$REPO_ROOT"
git status --short --branch > "$EVIDENCE/repository-status-before.txt"

loaded=0
current_rep=""
input_log_pid=""
stats_log_pid=""
restoration_rc=0
workflow_rc=0
gate_semantic_stop=0

stop_logs() {
  local pid
  for pid in "$input_log_pid" "$stats_log_pid"; do
    if [[ -n "$pid" ]] && kill -0 "$pid" 2>/dev/null; then
      kill "$pid" 2>/dev/null || true
      wait "$pid" 2>/dev/null || true
    fi
  done
  input_log_pid=""
  stats_log_pid=""
}

unload_current() {
  local rep="$1"
  local rc=0
  stop_logs
  if [[ "$loaded" -eq 1 ]]; then
    "$LMS_EXE" unload upgradepilot-gemma-e4b-smoke \
      > "$EVIDENCE/unload-output-r${rep}.stdout.txt" \
      2> "$EVIDENCE/unload-output-r${rep}.stderr.txt"
    rc=$?
    printf '%s\n' "$rc" > "$EVIDENCE/unload-output-r${rep}.exit-code.txt"
    loaded=0
    if [[ "$rc" -ne 0 ]]; then
      restoration_rc="$rc"
    fi
  else
    printf '%s\n' "0" > "$EVIDENCE/unload-output-r${rep}.exit-code.txt"
    printf '%s\n' "Model was not marked loaded by the runner." \
      > "$EVIDENCE/unload-output-r${rep}.stdout.txt"
    : > "$EVIDENCE/unload-output-r${rep}.stderr.txt"
  fi
}

emergency_cleanup() {
  stop_logs
  if [[ "$loaded" -eq 1 && -n "$current_rep" ]]; then
    unload_current "$current_rep"
    "$PYTHON" "$DIAGNOSTIC" snapshot "emergency-post-unload-r${current_rep}" \
      > "$EVIDENCE/emergency-post-unload-r${current_rep}.stdout.txt" \
      2> "$EVIDENCE/emergency-post-unload-r${current_rep}.stderr.txt" || true
  fi
}

trap emergency_cleanup EXIT

run_repetition() {
  local rep="$1"
  local load_rc=0
  local diagnostic_rc=0

  current_rep="$rep"

  "$PYTHON" "$DIAGNOSTIC" preflight "$rep" \
    > "$EVIDENCE/preflight-r${rep}.stdout.txt" \
    2> "$EVIDENCE/preflight-r${rep}.stderr.txt" || return 10

  "$PYTHON" "$DIAGNOSTIC" snapshot "pre-load-r${rep}" \
    > "$EVIDENCE/pre-load-snapshot-r${rep}.stdout.txt" \
    2> "$EVIDENCE/pre-load-snapshot-r${rep}.stderr.txt" || return 11

  "$LMS_EXE" load gemma-4-e4b-it-ud \
    --context-length 4096 \
    --gpu max \
    --parallel 1 \
    --ttl 900 \
    --identifier upgradepilot-gemma-e4b-smoke \
    --no-speculative-draft-mtp \
    -y \
    > "$EVIDENCE/load-output-r${rep}.stdout.txt" \
    2> "$EVIDENCE/load-output-r${rep}.stderr.txt"
  load_rc=$?
  printf '%s\n' "$load_rc" > "$EVIDENCE/load-output-r${rep}.exit-code.txt"
  if [[ "$load_rc" -ne 0 ]]; then
    return 12
  fi
  loaded=1

  if ! "$PYTHON" "$DIAGNOSTIC" snapshot "post-load-r${rep}" \
    > "$EVIDENCE/post-load-snapshot-r${rep}.stdout.txt" \
    2> "$EVIDENCE/post-load-snapshot-r${rep}.stderr.txt"; then
    unload_current "$rep"
    return 13
  fi

  "$LMS_EXE" log stream --source model --filter input,output --json \
    > "$EVIDENCE/logs/model-input-output-r${rep}.jsonl" \
    2> "$EVIDENCE/logs/model-input-output-r${rep}.stderr.txt" &
  input_log_pid=$!

  "$LMS_EXE" log stream --source model --filter output --stats \
    > "$EVIDENCE/logs/model-stats-r${rep}.txt" \
    2> "$EVIDENCE/logs/model-stats-r${rep}.stderr.txt" &
  stats_log_pid=$!
  sleep 1

  "$PYTHON" "$DIAGNOSTIC" run "$rep"
  diagnostic_rc=$?
  printf '%s\n' "$diagnostic_rc" > "$EVIDENCE/diagnostic-r${rep}.exit-code.txt"

  stop_logs
  "$PYTHON" "$DIAGNOSTIC" snapshot "post-diagnostic-r${rep}" \
    > "$EVIDENCE/post-diagnostic-snapshot-r${rep}.stdout.txt" \
    2> "$EVIDENCE/post-diagnostic-snapshot-r${rep}.stderr.txt" || true

  unload_current "$rep"
  "$PYTHON" "$DIAGNOSTIC" snapshot "post-unload-r${rep}" \
    > "$EVIDENCE/post-unload-snapshot-r${rep}.stdout.txt" \
    2> "$EVIDENCE/post-unload-snapshot-r${rep}.stderr.txt" || true

  current_rep=""

  if [[ "$diagnostic_rc" -ne 0 ]]; then
    return 14
  fi

  if "$PYTHON" "$DIAGNOSTIC" result-passed "$rep"; then
    sleep 2
    return 0
  fi

  return 2
}

"$PYTHON" "$DIAGNOSTIC" freeze \
  > "$EVIDENCE/freeze.stdout.txt" \
  2> "$EVIDENCE/freeze.stderr.txt" || workflow_rc=20

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" self-test \
    > "$EVIDENCE/self-test.stdout.txt" \
    2> "$EVIDENCE/self-test.stderr.txt" || workflow_rc=21
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  for rep in 2 3; do
    run_repetition "$rep"
    rep_rc=$?
    printf '%s\n' "$rep_rc" > "$EVIDENCE/repetition-r${rep}.runner-exit-code.txt"

    if [[ "$rep_rc" -eq 2 ]]; then
      gate_semantic_stop=1
      break
    fi
    if [[ "$rep_rc" -ne 0 ]]; then
      workflow_rc="$rep_rc"
      break
    fi
  done
fi

printf '%s\n' "$workflow_rc" > "$EVIDENCE/workflow.exit-code.txt"
printf '%s\n' "$restoration_rc" > "$EVIDENCE/restoration.exit-code.txt"
printf '%s\n' "$gate_semantic_stop" > "$EVIDENCE/gate-semantic-stop.txt"

emergency_cleanup
trap - EXIT

"$PYTHON" -m unittest discover -s tests -v \
  > "$EVIDENCE/product-tests.stdout.txt" \
  2> "$EVIDENCE/product-tests.stderr.txt"
product_test_rc=$?
printf '%s\n' "$product_test_rc" > "$EVIDENCE/product-tests.exit-code.txt"

git status --short --branch > "$EVIDENCE/repository-status-after.txt"

cat > "$EVIDENCE/run-summary.txt" <<EOF
workflow_exit=$workflow_rc
restoration_exit=$restoration_rc
gate_semantic_stop=$gate_semantic_stop
product_tests_exit=$product_test_rc
python=$PYTHON
lms_exe=$LMS_EXE
completed_at=$(date --iso-8601=seconds)
EOF

"$PYTHON" "$DIAGNOSTIC" report
"$PYTHON" "$DIAGNOSTIC" manifest

echo
echo "Gate A repetition execution and evidence capture finished."
echo "Result record: $RESULT"
echo "Evidence directory: $EVIDENCE"
echo "MEMORY.md was not changed. Push the first result and evidence for independent review."

if [[ "$gate_semantic_stop" -eq 1 ]]; then
  echo "A Gate A model-output failure reached the mandatory stop line." >&2
  echo "Do not rerun or continue to Gate B before independent review." >&2
fi

if [[ "$workflow_rc" -ne 0 || "$restoration_rc" -ne 0 || "$product_test_rc" -ne 0 ]]; then
  echo "An infrastructure, resource-guard, restoration, or product-test check failed." >&2
  echo "Preserve the evidence and do not rerun automatically." >&2
  exit 1
fi

exit 0
