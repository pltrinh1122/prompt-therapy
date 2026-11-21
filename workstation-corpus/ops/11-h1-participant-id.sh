#!/usr/bin/env bash
# d-work: #11
# class: read-only
# undo: none (writes nothing)
# change-log: workstation-corpus/CHANGELOG.md row "#11 H1"
# postcondition: one participant id, p- and 16 hex characters of HMAC-SHA-256(key, lowercased address), was printed; nothing was written
# destructive: none
#
# Run it yourself, on your own machine:  bash workstation-corpus/ops/11-h1-participant-id.sh
# It asks for the participant's email address and a secret key you choose and keep in your own private storage.
# Neither is echoed, passed on a command line, written to a file, or printed. Paste back only the p-… line.
# The commands that handle the address and the key run without `set -x`, so the trace never shows them.
set -euo pipefail
git rev-parse --short HEAD 2>/dev/null || echo "(not in a git checkout)"; sha256sum "$0"

ID=""
postcondition() {
  [[ $ID =~ ^p-[0-9a-f]{16}$ ]]
}
postcondition && { echo "already satisfied"; exit 0; }

set -x
command -v python3
python3 -c 'import hashlib, hmac'
set +x

[[ -t 0 ]] || { echo "no tty: run it in a terminal"; exit 2; }
read -r -s -p "participant's email address (not shown): " ADDR; echo
read -r -s -p "your secret key (not shown; keep it yourself): " KEY; echo
[[ -n $ADDR && -n $KEY ]] || { echo "address and key are both needed"; exit 1; }

ID=$(printf '%s\n%s\n' "$KEY" "$ADDR" | python3 -c '
import hashlib, hmac, sys
key, addr = sys.stdin.read().split("\n")[:2]
print("p-" + hmac.new(key.encode(), addr.strip().lower().encode(), hashlib.sha256).hexdigest()[:16])
')
unset ADDR KEY

postcondition || { echo "postcondition failed"; exit 1; }
echo "$ID"
echo "done"
