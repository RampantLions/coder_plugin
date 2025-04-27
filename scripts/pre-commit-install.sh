#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

pdm run pre-commit-install  # Install Git pre-commit hooks
