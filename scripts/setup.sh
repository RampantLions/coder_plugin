#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

# Install pdm if missing
if ! command -v pdm &> /dev/null; then
    echo "📦  pdm not found. Installing..."
    brew install pdm
fi

# Install uv if missing
if ! command -v uv &> /dev/null; then
    echo "📦  uv not found. Installing..."
    brew install uv
fi

export UV_LINK_MODE=copy
VENV_DIR=".venv"

echo "🚧️️  Setting up environment..."

# FRESH=1 ./setup.sh   # force rebuild of Virtual Environment
if [[ "${FRESH:-0}" == "1" && -d "${VENV_DIR}" ]]; then
  echo " ➡ ♻️  Removing existing virtualenv ${VENV_DIR}..."
  rm -rf "${VENV_DIR}"
fi

# Create environment and install dependencies
echo " ➡ 🛠️️  Virtual Environment ${VENV_DIR} using pdm + uv..."
pdm install
