#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

pdm lock -G docs
pdm install -G docs

#pdm lock -G :all
#pdm install -G :all

# pdm run sphinx-quickstart docs/source
