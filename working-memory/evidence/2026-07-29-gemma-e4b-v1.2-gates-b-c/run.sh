#!/usr/bin/env bash
# Execute Gemma E4B state-contract v1.2 Gates B and C.

set -uo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
if [[ -z "$REPO_ROOT" ]]; then
  echo "Run this command from inside the UpgradePilot repository." >&2
  exit 1
fi

EVIDENCE="$REPO_ROOT/working-memory/evidence/2026-07-29-gemma-e4b-v1.2-gates-b-c"
DIAGNOSTIC="$EVIDENCE/diagnostic.py"
RESULT="$REPO_ROOT/working-memory/2026-07-29_B2-gemma-e4b-v1.2-gates-b-c-result.md"
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
  echo "Existing Gates B/C evidence was found and will not be overwritten." >&2
  echo "Preserve and push the first result for independent review." >&2
  exit 1
fi

mkdir -p "$EVIDENCE/logs"
cd "$REPO_ROOT"
git status --short --branch > "$EVIDENCE/repository-status-before.txt"

loaded=0
input_log_pid=""
stats_log_pid=""
workflow_rc=0
restoration_rc=0
semantic_stop=0

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

cleanup_model() {
  stop_logs
  if [[ "$loaded" -eq 1 ]]; then
    "$LMS_EXE" unload upgradepilot-gemma-e4b-smoke \
      > "$EVIDENCE/unload-output.stdout.txt" \
      2> "$EVIDENCE/unload-output.stderr.txt"
    local rc=$?
    printf '%s\n' "$rc" > "$EVIDENCE/unload-output.exit-code.txt"
    loaded=0
    if [[ "$rc" -ne 0 ]]; then
      restoration_rc="$rc"
    fi
  else
    printf '%s\n' "0" > "$EVIDENCE/unload-output.exit-code.txt"
    printf '%s\n' "Model was not marked loaded by the runner." > "$EVIDENCE/unload-output.stdout.txt"
    : > "$EVIDENCE/unload-output.stderr.txt"
  fi
}

emergency_cleanup() {
  cleanup_model
  "$PYTHON" "$DIAGNOSTIC" snapshot emergency-post-unload \
    > "$EVIDENCE/emergency-post-unload.stdout.txt" \
    2> "$EVIDENCE/emergency-post-unload.stderr.txt" || true
}

trap emergency_cleanup EXIT

"$PYTHON" -m py_compile "$DIAGNOSTIC" || workflow_rc=20

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" freeze > "$EVIDENCE/freeze.stdout.txt" 2> "$EVIDENCE/freeze.stderr.txt" || workflow_rc=21
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" self-test > "$EVIDENCE/self-test.stdout.txt" 2> "$EVIDENCE/self-test.stderr.txt" || workflow_rc=22
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" preflight > "$EVIDENCE/preflight.stdout.txt" 2> "$EVIDENCE/preflight.stderr.txt" || workflow_rc=23
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" snapshot pre-load > "$EVIDENCE/pre-load-snapshot.stdout.txt" 2> "$EVIDENCE/pre-load-snapshot.stderr.txt" || workflow_rc=24
fi

if [[ "$workflow_rc" -eq 0 ]]; then
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
  load_rc=$?
  printf '%s\n' "$load_rc" > "$EVIDENCE/load-output.exit-code.txt"
  if [[ "$load_rc" -ne 0 ]]; then
    workflow_rc=25
  else
    loaded=1
  fi
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" snapshot post-load > "$EVIDENCE/post-load-snapshot.stdout.txt" 2> "$EVIDENCE/post-load-snapshot.stderr.txt" || workflow_rc=26
fi

if [[ "$workflow_rc" -eq 0 ]]; then
  "$LMS_EXE" log stream --source model --filter input,output --json \
    > "$EVIDENCE/logs/model-input-output.jsonl" \
    2> "$EVIDENCE/logs/model-input-output.stderr.txt" &
  input_log_pid=$!
  "$LMS_EXE" log stream --source model --filter output --stats \
    > "$EVIDENCE/logs/model-stats.txt" \
    2> "$EVIDENCE/logs/model-stats.stderr.txt" &
  stats_log_pid=$!
  sleep 1

  "$PYTHON" "$DIAGNOSTIC" gate-b
  gate_b_rc=$?
  printf '%s\n' "$gate_b_rc" > "$EVIDENCE/gate-b.exit-code.txt"
  if [[ "$gate_b_rc" -eq 2 ]]; then
    semantic_stop=1
  elif [[ "$gate_b_rc" -ne 0 ]]; then
    workflow_rc=27
  fi
fi

if [[ "$workflow_rc" -eq 0 && "$semantic_stop" -eq 0 ]]; then
  "$PYTHON" "$DIAGNOSTIC" gate-c
  gate_c_rc=$?
  printf '%s\n' "$gate_c_rc" > "$EVIDENCE/gate-c.exit-code.txt"
  if [[ "$gate_c_rc" -eq 2 ]]; then
    semantic_stop=1
  elif [[ "$gate_c_rc" -ne 0 ]]; then
    workflow_rc=28
  fi
else
  printf '%s\n' "not-run" > "$EVIDENCE/gate-c.exit-code.txt"
fi

stop_logs
"$PYTHON" "$DIAGNOSTIC" snapshot post-diagnostic > "$EVIDENCE/post-diagnostic-snapshot.stdout.txt" 2> "$EVIDENCE/post-diagnostic-snapshot.stderr.txt" || true

cleanup_model
"$PYTHON" "$DIAGNOSTIC" snapshot post-unload > "$EVIDENCE/post-unload-snapshot.stdout.txt" 2> "$EVIDENCE/post-unload-snapshot.stderr.txt" || true
trap - EXIT

printf '%s\n' "$workflow_rc" > "$EVIDENCE/workflow.exit-code.txt"
printf '%s\n' "$restoration_rc" > "$EVIDENCE/restoration.exit-code.txt"
printf '%s\n' "$semantic_stop" > "$EVIDENCE/semantic-stop.txt"

"$PYTHON" -m unittest discover -s tests -v > "$EVIDENCE/product-tests.stdout.txt" 2> "$EVIDENCE/product-tests.stderr.txt"
product_test_rc=$?
printf '%s\n' "$product_test_rc" > "$EVIDENCE/product-tests.exit-code.txt"

git status --short --branch > "$EVIDENCE/repository-status-after.txt"

cat > "$EVIDENCE/run-summary.txt" <<EOF
workflow_exit=$workflow_rc
restoration_exit=$restoration_rc
semantic_stop=$semantic_stop
product_tests_exit=$product_test_rc
python=$PYTHON
lms_exe=$LMS_EXE
completed_at=$(date --iso-8601=seconds)
EOF

"$PYTHON" "$DIAGNOSTIC" report
"$PYTHON" "$DIAGNOSTIC" manifest

echo
echo "Gates B/C execution and evidence capture finished."
echo "Result record: $RESULT"
echo "Evidence directory: $EVIDENCE"
echo "MEMORY.md was not changed. Push the first result and evidence for independent review."

if [[ "$semantic_stop" -eq 1 ]]; then
  echo "A model-output failure reached the mandatory stop line." >&2
  echo "Do not rerun or continue before independent review." >&2
fi

if [[ "$workflow_rc" -ne 0 || "$restoration_rc" -ne 0 || "$product_test_rc" -ne 0 ]]; then
  echo "An infrastructure, resource-guard, restoration, or product-test check failed." >&2
  echo "Preserve the evidence and do not rerun automatically." >&2
  exit 1
fi

exit 0
