#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

#The installer will install PDM into the user site and the location depends on the system:
#
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

    # https://pdm-project.org/install-pdm.py.sha256
    # curl -sSLO https://pdm-project.org/install-pdm.py
    # curl -sSL https://pdm-project.org/install-pdm.py.sha256 | shasum -a 256 -c -
    ## Run the installer
    #python3 install-pdm.py [options]
    #brew install pdm
    uv tool install pdm
    # pdm self update
fi

export UV_LINK_MODE=copy
VENV_DIR=".venv"

echo "🚧️️  Setting up environment..."

# FRESH=1 ./setup.sh   # force rebuild of Virtual Environment
if [[ "${FRESH:-0}" == "1" && -d "${VENV_DIR}" ]]; then
  echo " ╰─▶ ♻️  Removing existing virtualenv ${VENV_DIR}..."
  rm -rf "${VENV_DIR}"
fi

# Create environment and install dependencies
echo " ╰─▶ 🛠️️  Virtual Environment ${VENV_DIR} using pdm + uv..."
pdm config python.use_venv false
pdm install



#pdm venv --path for-test
#pdm venv --python for-test
# eval $(pdm venv activate for-test)


## Run a script
#pdm run --venv test test
## Install packages
#pdm sync --venv test
## List the packages installed
#pdm list --venv test

## Switch to a virtualenv named test
#$ pdm use --venv test
## Switch to the in-project venv located at $PROJECT_ROOT/.venv
#$ pdm use --venv in-project


## Create a virtualenv based on 3.9 interpreter
#pdm venv create 3.9
## Assign a different name other than the version string
#pdm venv create --name for-test 3.9
## Use venv as the backend to create, support 3 backends: virtualenv(default), venv, conda
#pdm venv create --with venv 3.10

# pdm use -f /path/to/venv

