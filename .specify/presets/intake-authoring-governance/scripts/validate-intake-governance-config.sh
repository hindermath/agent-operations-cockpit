#!/usr/bin/env bash
# Prueft die sprachbewusste Requirements-Intake-Governance read-only.
# Validates language-aware requirements intake governance read-only.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
exec python3 -B "$script_dir/validate-intake-governance-config.py" "$@"
