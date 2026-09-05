#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' 'Verwendung / Usage: validate-current-evidence-binding.sh [--repo PATH] [--] current-evidence'
  printf '%s\n' 'Read-only: prueft die begrenzte Feature-003-Evidence-Bindung. / Read-only: validates the bounded Feature-003 evidence binding.'
}

repo='.'
mode=''
while (($# > 0)); do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --repo)
      if (($# < 2)); then
        printf '%s\n' 'Fehler / Error: --repo requires a path.' >&2
        exit 2
      fi
      repo=$2
      shift 2
      ;;
    --)
      shift
      if (($# > 0)); then
        mode=$1
        shift
      fi
      break
      ;;
    current-evidence)
      mode=$1
      shift
      break
      ;;
    *)
      if [[ "$1" != -* ]]; then
        mode=$1
        shift
        break
      fi
      printf 'Fehler / Error: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ "$mode" != 'current-evidence' ]] || (($# > 0)); then
  printf '%s\n' 'Fehler / Error: exactly one mode, current-evidence, is required.' >&2
  usage >&2
  exit 2
fi

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
exec python3 -B -- "$script_dir/validate_current_evidence_binding.py" --repo "$repo" "$mode"
