#!/usr/bin/env bash
# Run the portable META-LH-02 portfolio validator from Bash.
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$script_dir/validate-portfolio.py" "$@"
