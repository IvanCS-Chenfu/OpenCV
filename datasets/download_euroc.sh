#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${1:-$ROOT/data/EuRoC/MH_01_easy}"
mkdir -p "$DEST"
URL="https://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy.zip"
TMP="$(mktemp --suffix=.zip)"; trap 'rm -f "$TMP"' EXIT
curl -L --fail --retry 3 "$URL" -o "$TMP"
unzip -q "$TMP" -d "$DEST"
echo "EuRoC MH_01_easy disponible en: $DEST"
