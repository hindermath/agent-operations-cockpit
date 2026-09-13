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

# Kinddiagnosen bleiben privat; nur definierte Ergebnisse passieren die Grenze.
# Keep child diagnostics private; only defined results cross the boundary.
core_exit=0
core_output="$(python3 -B "$script_dir/validate_series_eligibility.py" "$@" 2>/dev/null)" || core_exit=$?
if [[ ( "$core_exit" -eq 0 || "$core_exit" -eq 2 ) &&
      ( "$core_output" == '{"schemaVersion": "1.0", "mode": '* ||
        "$core_output" == 'Modus / Mode: '* ) ]]; then
  printf '%s\n' "$core_output"
  exit "$core_exit"
fi
json_output=false
for argument in "$@"; do
  if [[ "$argument" == "--json" ]]; then json_output=true; fi
done
if "$json_output"; then
  cat <<'EOF'
{"schemaVersion":"1.0","mode":null,"criteria":{},"outcome":"Blocked","reasons":[{"code":"EL_PROVIDER","criterion":null,"de":"Die Laufzeitprüfung ist fehlgeschlagen.","en":"The runtime check failed."}],"failureClass":"ProviderFailure","authorityGranted":false,"nextAction":{"de":"Eingaben und Nachweise erneut prüfen; nichts starten.","en":"Reassess inputs and evidence; start nothing."}}
EOF
else
  cat <<'EOF'
Modus / Mode: NotAssessed
Ergebnis / Outcome: Blocked
Die Laufzeitprüfung ist fehlgeschlagen. / The runtime check failed.
Nächste Aktion / Next action: Eingaben und Nachweise erneut prüfen; nichts starten. / Reassess inputs and evidence; start nothing.
Keine Startfreigabe. / No start authority granted.
EOF
fi
exit 3
