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

pdm run lint          # Run lint and static checks
