#!/usr/bin/env bash
# d-work: #3
# class: reversible
# undo: docker rmi pt-eval:3-h1; rm -rf "${WORK:-$HOME/pt-eval}" (the image and the log; API spend is not undone)
# change-log: workstation-corpus/CHANGELOG.md row "#3 H1"
# postcondition: "${WORK:-$HOME/pt-eval}/evaluation.log" holds one summary line for each of the three candidate models
# destructive: none
#
# The evaluation container of plan #3 revision 5: Prompt Therapy's adversarial set (P2, 42 members) against
# claude-haiku-5-5, claude-sonnet-5-5 and claude-opus-5-5, at most US$10 in total (budgets 1 + 3 + 6), each model in
# its own `docker run --rm` of the image pt-eval:3-h1 (python:3.12-slim + git). Inside, the container fetches
# prompt-therapy at the adapter commit and dyad-system at the pin; it mounts nothing from your machine, and nothing
# of your git clones is touched. Authentication by dmc:provider-auth, outcome sign-in: run `ant auth login` once on
# your machine; before each model's run the script takes a fresh token with `ant auth print-credentials
# --access-token` and passes it into that one container (an exported ANTHROPIC_API_KEY is the fallback). Get and run:
#   git fetch origin p3/ops && git show origin/p3/ops:workstation-corpus/ops/3-h1-provider-evaluation.sh > /tmp/3-h1.sh
#   bash /tmp/3-h1.sh 2>&1 | tee 3-h1-provider-evaluation.log
# Paste the output back: it holds results, tokens and cost, never a token or a key. A re-run after a complete run
# prints "already satisfied" and spends nothing.
# Limits: the API workspace's rate limits and spend are shared with any other work that uses the same workspace (a
# dedicated profile and workspace is the remedy: `ant auth login --profile pt-eval`, then ANTHROPIC_PROFILE=pt-eval);
# the token is visible to `docker inspect` while its container runs.
set -euo pipefail
git rev-parse --short HEAD 2>/dev/null || echo "(not run from a git clone)"; sha256sum "$0"

ADAPTER=7465145ae1228b40aca7673ebf737d71bc386184   # prompt-therapy p3/inference: the stdlib adapter, its sign-in path, evaluate.py
PIN=87daca88e8d56fe41ee4d0c2a0257280ada176e6       # dyad-system: the adversarial set's pin
IMAGE=pt-eval:3-h1
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

command -v docker >/dev/null 2>&1 || { echo "docker is not installed or not on PATH"; exit 1; }
docker info >/dev/null 2>&1 || { echo "the docker daemon is not reachable (start Docker)"; exit 1; }
token() { ant auth print-credentials --access-token; }   # a fresh sign-in token (dmc:provider-auth)
if command -v ant >/dev/null 2>&1 && token >/dev/null 2>&1; then AUTH=sign-in
elif [[ -n "${ANTHROPIC_API_KEY:-}" ]]; then AUTH=api-key
else echo "sign in first (ant auth login), or export ANTHROPIC_API_KEY"; exit 1; fi
echo "authentication: $AUTH"

# Inside the container: fetch the two commits shallowly, point the adversarial set at the pin, run one model.
INNER='set -euo pipefail
model=$1; budget=$2
git init -q /pt && git -C /pt fetch -q --depth 1 https://github.com/pltrinh1122/prompt-therapy.git '"$ADAPTER"' && git -C /pt checkout -q FETCH_HEAD
git init -q /ds && git -C /ds fetch -q --depth 1 https://github.com/pltrinh1122/dyad-system.git '"$PIN"' && git -C /ds update-ref refs/pin FETCH_HEAD
git -C /pt config prompt-therapy.canon /ds
cd /pt && python3 crafts/prompt-therapy/scripts/evaluate.py anthropic "$model" --effort low --budget "$budget"'

set -x
mkdir -p "$WORK"
docker image inspect "$IMAGE" >/dev/null 2>&1 || printf '%s\n' \
  'FROM python:3.12-slim' \
  'RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*' \
  | docker build -q -t "$IMAGE" -
: > "$LOG"
set +x
for i in "${!MODELS[@]}"; do
  if [[ $AUTH == sign-in ]]; then
    ANTHROPIC_AUTH_TOKEN="$(token)" docker run --rm -e ANTHROPIC_AUTH_TOKEN "$IMAGE" bash -c "$INNER" _ "${MODELS[$i]}" "${BUDGETS[$i]}" | tee -a "$LOG" || true
  else
    docker run --rm -e ANTHROPIC_API_KEY "$IMAGE" bash -c "$INNER" _ "${MODELS[$i]}" "${BUDGETS[$i]}" | tee -a "$LOG" || true
  fi
done

postcondition || { echo "postcondition failed"; exit 1; }
echo "done"
