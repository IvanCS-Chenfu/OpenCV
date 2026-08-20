#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${1:-$ROOT/data/TUM_RGBD}"
mkdir -p "$DEST"
cat <<'EOF'
TUM RGB-D exige elegir una secuencia y respetar sus condiciones de uso.
Descarga la secuencia desde:
https://cvg.cit.tum.de/data/datasets/rgbd-dataset/download

Colócala descomprimida dentro de:
EOF
echo "$DEST"
