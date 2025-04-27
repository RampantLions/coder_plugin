#!/usr/bin/env bash

if sh "set -o pipefail" > /dev/null 2>&1; then
  set -euo pipefail
else
  set -eu
fi

#pdm lock -G dev
#pdm install -G dev

#pdm lock -G :all
#pdm install -G :all

# Run unit tests
pdm run test

# Run tests with coverage
pdm run test-cov
