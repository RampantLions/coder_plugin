#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

#The installer will install PDM into the user site and the location depends on the system:
#$HOME/.local/bin for Unix
#$HOME/Library/Python/<version>/bin for MacOS
#%APPDATA%\Python\Scripts on Windows

# ➡ Install uv if missing
if ! command -v uv &> /dev/null; then
    echo "📦  uv not found. Installing..."
    brew install uv
fi

# ➡ Install pdm if missing
if ! command -v pdm &> /dev/null; then
    echo "📦  pdm not found. Installing..."
    # curl -sSL https://pdm-project.org/install-pdm.py | python3 -
    # powershell -ExecutionPolicy ByPass -c "irm https://pdm-project.org/install-pdm.py | py -"
    uv tool install pdm
    # pdm self update
fi

echo "🚧️️  Setting up environment..."
export UV_LINK_MODE=copy
VENV_DIR=".venv"
# FRESH=1 ./setup.sh   # force rebuild of Virtual Environment
if [[ "${FRESH:-0}" == "1" && -d "${VENV_DIR}" ]]; then
  echo " ╰─▶ ♻️  Removing existing virtualenv ${VENV_DIR}..."
  rm -rf "${VENV_DIR}"
fi

# Create environment and install dependencies
echo " ╰─▶ 🛠️️  Virtual Environment ${VENV_DIR} using pdm + uv..."
#echo " ╰─▶ 🛠️️  Virtual Environment [PEP582] using pdm + uv..."
pdm config python.use_venv false
pdm install
pdm config
