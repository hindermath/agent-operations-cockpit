#!/usr/bin/env bash
set -euo pipefail

repo='.'
json_flag=''

while (($# > 0)); do
  case "$1" in
    --repo)
      if (($# < 2)) || [[ -z "$2" ]]; then
        printf '%s\n' 'VERWENDUNG / USAGE: validate-authoring-contract.sh --repo <path> [--json]' >&2
        exit 64
      fi
      repo="$2"
      shift 2
      ;;
    --json)
      json_flag='--json'
      shift
      ;;
    -h|--help)
      printf '%s\n' 'VERWENDUNG / USAGE: validate-authoring-contract.sh --repo <path> [--json]'
      exit 0
      ;;
    *)
      printf 'Unbekannte Option / unknown option: %s\n' "$1" >&2
      exit 64
      ;;
  esac
done

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
arguments=("$script_dir/validate_authoring_contract.py" --repo "$repo")
if [[ -n "$json_flag" ]]; then
  arguments+=("$json_flag")
fi
exec python3 -B "${arguments[@]}"
