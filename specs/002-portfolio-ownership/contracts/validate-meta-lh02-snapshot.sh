#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' 'Verwendung / Usage: validate-meta-lh02-snapshot.sh [--repo PATH] [--] post-global-ready'
  printf '%s\n' 'Read-only. Siehe / See: docs/man/validate-meta-lh02-snapshot.1'
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
    post-global-ready)
      mode=$1
      shift
      break
      ;;
    *)
      printf 'Fehler / Error: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ "$mode" != 'post-global-ready' ]] || (($# > 0)); then
  printf '%s\n' 'Fehler / Error: exactly one mode, post-global-ready, is required.' >&2
  usage >&2
  exit 2
fi

script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)
core="$script_dir/validate_meta_lh02_snapshot.py"
exec python3 -B -- "$core" --repo "$repo" "$mode"
