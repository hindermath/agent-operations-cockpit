#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd -- "${script_dir}/../../.." && pwd)"
python3 "${script_dir}/validate-series-eligibility.py" \
  --contract "${repo_dir}/requirements/baseline/series-eligibility-contract.json" \
  --fixture "$1"
