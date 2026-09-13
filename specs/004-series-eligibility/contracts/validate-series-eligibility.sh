#!/usr/bin/env bash
# Strikte lesende Delegation / Strict read-only delegation.
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"

show_help() {
  cat <<'EOF'
Series Eligibility pruefen / Assess Series Eligibility

VERWENDUNG / USAGE
  validate-series-eligibility.sh --repo PATH --fixture PATH [--json]
  validate-series-eligibility.sh --help | -h

OPTIONEN / OPTIONS
  --repo PATH     Repository-Wurzel. / Repository root.
  --fixture PATH  Fixture relativ zum Repository. / Fixture relative to the repository.
  --json          Maschinenlesbare Ausgabe. / Machine-readable output.
  --help, -h      Diese Hilfe anzeigen. / Show this help.

Die Pruefung liest nur und erteilt keine Startfreigabe.
The assessment is read-only and grants no authority to start.

Handbuch / Manual: docs/man/validate-series-eligibility.1
EOF
}

if [[ $# -eq 1 && ( "$1" == "--help" || "$1" == "-h" ) ]]; then
  show_help
  exit 0
fi

exec python3 -B "$script_dir/validate_series_eligibility.py" "$@"
