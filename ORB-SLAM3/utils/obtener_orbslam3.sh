#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/third_party/ORB_SLAM3"
if [[ -d "$DEST/.git" ]]; then
  echo "Ya existe $DEST; no se sobrescribe."
  exit 0
fi
git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git "$DEST"
git -C "$DEST" checkout 4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4
echo "ORB-SLAM3 fijado en 4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4"
