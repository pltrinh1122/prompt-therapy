#!/usr/bin/env bash
# d-work: #3
# class: reversible
# undo: rm -rf "${WORK:-$HOME/pt-eval}" (the worktree, the dyad-system clone and the log; API spend is not undone)
# change-log: workstation-corpus/CHANGELOG.md row "#3 H1"
# postcondition: "${WORK:-$HOME/pt-eval}/evaluation.log" holds one summary line for each of the three candidate models
# destructive: none
#
# Runs Prompt Therapy's adversarial set (P2, 42 members) against claude-haiku-5-5, claude-sonnet-5-5 and
# claude-opus-5-5 as the operator, at most US$10 in total (budgets 1 + 3 + 6). Authentication by dmc:provider-auth,
# outcome sign-in: run `ant auth login` once beforehand; the script takes a fresh token with
# `ant auth print-credentials --access-token` before each model's run and never writes it anywhere. (Without `ant`,
# an ANTHROPIC_API_KEY exported in your shell is used instead: the record's last outcome.) Run from a clone of
# pltrinh1122/prompt-therapy that has fetched branches p3/ops and p3/inference:
#   bash workstation-corpus/ops/3-h1-provider-evaluation.sh 2>&1 | tee 3-h1-provider-evaluation.log
# Paste the output back: it holds results, tokens and cost, never a token or a key.
# A re-run after a complete run prints "already satisfied" and spends nothing.
set -euo pipefail
git rev-parse --short HEAD; sha256sum "$0"

ADAPTER=7465145ae1228b40aca7673ebf737d71bc386184   # p3/inference: the stdlib adapter, its sign-in path, evaluate.py
PIN=87daca88e8d56fe41ee4d0c2a0257280ada176e6       # dyad-system: the adversarial set's pin
WORK="${WORK:-$HOME/pt-eval}"
LOG="$WORK/evaluation.log"
MODELS=(claude-haiku-5-5 claude-sonnet-5-5 claude-opus-5-5)
BUDGETS=(1 3 6)

postcondition() {
  [[ -f "$LOG" ]] || return 1
  local m
  for m in "${MODELS[@]}"; do grep -q "^$m: .* passed, .* failed;" "$LOG" || return 1; done
}
postcondition && { echo "already satisfied"; cat "$LOG"; exit 0; }

token() { ant auth print-credentials --access-token; }   # a fresh sign-in token (dmc:provider-auth)
if command -v ant >/dev/null 2>&1 && token >/dev/null 2>&1; then AUTH=sign-in; unset ANTHROPIC_API_KEY
elif [[ -n "${ANTHROPIC_API_KEY:-}" ]]; then AUTH=api-key
else echo "sign in first (ant auth login), or export ANTHROPIC_API_KEY"; exit 1; fi
echo "authentication: $AUTH"
python3 -c 'import sys; sys.exit(sys.version_info < (3, 12))' || { echo "Python 3.12+ required"; exit 1; }

set -x
mkdir -p "$WORK"
git cat-file -e "$ADAPTER^{commit}" 2>/dev/null || git fetch origin p3/inference
[[ -d "$WORK/pt" ]] || git worktree add --detach "$WORK/pt" "$ADAPTER"
[[ -d "$WORK/dyad-system" ]] || git clone --quiet https://github.com/pltrinh1122/dyad-system.git "$WORK/dyad-system"
git -C "$WORK/dyad-system" cat-file -e "$PIN^{commit}"
git -C "$WORK/pt" config prompt-therapy.canon "$WORK/dyad-system"
: > "$LOG"
set +x
for i in "${!MODELS[@]}"; do
  if [[ $AUTH == sign-in ]]; then ANTHROPIC_AUTH_TOKEN="$(token)"; export ANTHROPIC_AUTH_TOKEN; fi
  ( cd "$WORK/pt" && python3 crafts/prompt-therapy/scripts/evaluate.py anthropic "${MODELS[$i]}" --effort low --budget "${BUDGETS[$i]}" ) | tee -a "$LOG" || true
done

postcondition || { echo "postcondition failed"; exit 1; }
echo "done"
