#!/usr/bin/env bash

if sh -c "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

# Settings
VENV_DIR="${1:-$HOME/common-venv}"  # Default to ~/common-venv if not specified
shift || true                      # Remove $1 from positional arguments

# List of project directories to install (absolute or relative paths)
PROJECTS=(
  "path/to/project1"
  "path/to/project2"
  "path/to/project3"
)

# Step 1,	Action: Creates the shared venv at given path if missing
if [[ ! -d "$VENV_DIR" ]]; then
  echo "🚧 Creating shared virtual environment at: $VENV_DIR"
  python3 -m venv "$VENV_DIR"
fi

# Step 2,	Action: Activate the virtual environment
echo "🔗 Activating virtual environment..."
# shellcheck source=/dev/null
source "${VENV_DIR}/bin/activate"

# Step 3,	Action: Upgrades pip inside the venv (optional if using uv later)
echo "⬆️  Upgrading pip in shared environment..."
pip install --upgrade pip

# Install uv if available
if command -v uv &> /dev/null; then
  INSTALL_CMD="uv pip install -e"
else
  INSTALL_CMD="pip install -e"
fi

# Step 4,	Action: For each project path listed, pip install -e . or uv pip install -e . if uv is available
for project in "${PROJECTS[@]}"; do
  if [[ -d "$project" ]]; then
    echo "📦 Installing project: $project"
    pushd "$project" > /dev/null
    #Step 5,	Action: Installs all projects into the same common environment
    $INSTALL_CMD .
    popd > /dev/null
  else
    echo "⚠️  Warning: Project path not found: $project"
  fi
done

echo "✅ All projects installed into shared environment at: $VENV_DIR"

#chmod +x setup_shared_env.sh
#
## Run with default shared venv path (~common-venv):
#./setup_shared_env.sh
#
## OR specify a different venv location:
#./setup_shared_env.sh /path/to/my-venv
