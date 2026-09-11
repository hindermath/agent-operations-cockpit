#!/usr/bin/env bash
# prepare-secure-development-hardening.sh
# Prepare MSL-based Level-2 repositories for later secure-development hardening runs.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB_FILE="$SCRIPT_DIR/lib/secure-development-hardening.sh"

if [ ! -f "$LIB_FILE" ]; then
  echo "Fehler: Hilfsbibliothek nicht gefunden: $LIB_FILE" >&2
  echo "Error: helper library not found: $LIB_FILE" >&2
  exit 1
fi
# shellcheck source=/dev/null
. "$LIB_FILE"

HOME_DIR="${HOME}"
OPT_DRY_RUN=false
OPT_COMMIT=false
OPT_PUSH=false
OPT_ALLOW_DIRTY=false
OPT_PRIMARY_LANGUAGE=""
OPT_ORDER_ONLY=false
OPT_MANIFEST=""
OPT_REPOS=()
OPT_ORDER_OUTPUTS=()

usage() {
  cat <<'EOF'
prepare-secure-development-hardening.sh — Secure-Development-Hardening vorbereiten

Erzeugt bei einem eindeutigen kanonischen Series-Manifest eine fuenfspaltige
Lastenheft-Reihenfolge: Position, Status, vollstaendig verlinkter Intake-
Dateiname, direkte eingehende Abhaengigkeiten und Spec-Kit-Feature. Feature-
Links entstehen nur aus einer ausdruecklichen eindeutigen Bindung; sonst wird
der exakte zweisprachige Fallback ausgegeben. --dry-run prueft denselben
Vertrag und schreibt keine Ziel- oder temporaeren Dateien in getrackte Pfade.

With one unambiguous canonical series manifest, generates a five-column
requirements order: position, status, linked complete intake filename, direct
incoming dependencies, and Spec Kit feature. Feature links require one explicit
unique binding; otherwise the exact bilingual fallback is rendered. --dry-run
checks the same contract without writing targets or temporary files to tracked
paths. Write mode rechecks the complete consumed input set and rejects any
generated output that overlaps a canonical input.

--order-only isolates this projection from language detection and secure-
development preparation. It requires one explicit --repo and --manifest,
supports repeated --order-output paths, and forbids commit and push.

Usage:
  bash scripts/prepare-secure-development-hardening.sh [options]

Options:
  --home-dir PATH             Home directory to scan (default: $HOME)
  --repo PATH                 Prepare one explicit Level-2 repo; repeatable
  --primary-language LANG     Override language detection for all discovered repos
  --order-only               Nur Intake-Projektion; erfordert --repo und --manifest
  --manifest PATH            Kanonisches Manifest relativ zum expliziten Repo
  --order-output PATH        Owned Ausgabe relativ zum Repo; wiederholbar
  --commit                    Commit changes in each changed repo
  --push                      Push current branch after commit/check; implies --commit
  --allow-dirty               Continue even if a repo already has local changes
  --dry-run                   Vertrag pruefen, keine Writes / check contract, no writes
  -h, --help                  Diese Hilfe anzeigen / show this help
EOF
}

log() {
  printf '%s\n' "$*"
}

die() {
  printf 'Fehler: %s\n' "$*" >&2
  exit 1
}

while [ $# -gt 0 ]; do
  case "$1" in
    --home-dir)
      [ $# -ge 2 ] || die "--home-dir braucht einen Pfad"
      HOME_DIR="$2"
      shift 2
      ;;
    --primary-language)
      [ $# -ge 2 ] || die "--primary-language braucht einen Wert"
      OPT_PRIMARY_LANGUAGE="$2"
      shift 2
      ;;
    --repo)
      [ $# -ge 2 ] || die "--repo braucht einen Pfad"
      OPT_REPOS+=("$2")
      shift 2
      ;;
    --order-only)
      OPT_ORDER_ONLY=true
      shift
      ;;
    --manifest)
      [ $# -ge 2 ] || die "--manifest braucht einen repositoryrelativen Pfad"
      OPT_MANIFEST="$2"
      shift 2
      ;;
    --order-output)
      [ $# -ge 2 ] || die "--order-output braucht einen repositoryrelativen Pfad"
      OPT_ORDER_OUTPUTS+=("$2")
      shift 2
      ;;
    --commit)
      OPT_COMMIT=true
      shift
      ;;
    --push)
      OPT_PUSH=true
      OPT_COMMIT=true
      shift
      ;;
    --allow-dirty)
      OPT_ALLOW_DIRTY=true
      shift
      ;;
    --dry-run)
      OPT_DRY_RUN=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Unbekannte Option: $1"
      ;;
  esac
done

command -v git >/dev/null 2>&1 || die "git nicht gefunden"

if $OPT_ORDER_ONLY; then
  [ "${#OPT_REPOS[@]}" -eq 1 ] || die "--order-only erfordert genau ein explizites --repo"
  [ -n "$OPT_MANIFEST" ] || die "--order-only erfordert --manifest"
  ! $OPT_COMMIT && ! $OPT_PUSH || die "--order-only erlaubt weder --commit noch --push"
  [ -z "$OPT_PRIMARY_LANGUAGE" ] || die "--order-only verwendet keine --primary-language"
  [ "${#OPT_ORDER_OUTPUTS[@]}" -gt 0 ] || OPT_ORDER_OUTPUTS=('Lastenheft_Abarbeitungsreihenfolge.md')
  order_repo="${OPT_REPOS[0]}"
  [ -d "$order_repo/.git" ] || die "--repo ist kein Git-Repository"
  if ! $OPT_DRY_RUN && ! $OPT_ALLOW_DIRTY; then
    order_status="$(git -C "$order_repo" status --short)"
    [ -z "$order_status" ] || die "Repo hat lokale Aenderungen; fuer einen begrenzten Write explizit --allow-dirty verwenden: $order_repo"
  fi
  order_mode='write'
  $OPT_DRY_RUN && order_mode='check'
  if sdh_render_linked_intake_views "$order_repo" "$OPT_MANIFEST" "$order_mode" "${OPT_ORDER_OUTPUTS[@]}"; then
    :
  else
    order_exit=$?
    exit "$order_exit"
  fi
  log "Intake-Projektion / intake projection: $SDH_RENDER_RESULT, writes=$SDH_RENDER_WRITE_COUNT"
  exit 0
fi

if [ -n "$OPT_MANIFEST" ] || [ "${#OPT_ORDER_OUTPUTS[@]}" -gt 0 ]; then
  die "--manifest und --order-output sind nur mit --order-only erlaubt"
fi

REPOS=()

contains_repo() {
  local needle="$1"
  local item
  for item in "${REPOS[@]+"${REPOS[@]}"}"; do
    [ "$item" = "$needle" ] && return 0
  done
  return 1
}

is_level2_repo() {
  local repo="$1"
  [ -d "$repo/.git" ] || return 1
  [ -d "$repo/.specify" ] || [ -f "$repo/AGENTS.md" ] || [ -f "$repo/CLAUDE.md" ] || return 1
}

add_repo() {
  local repo="$1"
  [ -d "$repo" ] || return 0
  is_level2_repo "$repo" || return 0
  contains_repo "$repo" && return 0
  REPOS+=("$repo")
}

discover_repos() {
  local workspace project
  REPOS=()

  if [ "${#OPT_REPOS[@]}" -gt 0 ]; then
    for project in "${OPT_REPOS[@]}"; do
      add_repo "$project"
    done
    return 0
  fi

  for workspace in "$HOME_DIR"/*; do
    [ -d "$workspace" ] || continue
    [ -d "$workspace/.git" ] || continue
    for project in "$workspace"/*; do
      [ -d "$project" ] || continue
      add_repo "$project"
    done
  done
}

commit_and_push() {
  local repo="$1"
  local branch

  if ! $OPT_COMMIT && ! $OPT_PUSH; then
    return 0
  fi

  if $OPT_DRY_RUN; then
    $OPT_COMMIT && log "  [dry-run] git add docs/secure-development Lastenheft_Secure-Development-Hardening.md Lastenheft_Abarbeitungsreihenfolge.md && git commit"
    $OPT_PUSH && log "  [dry-run] git push origin <branch>"
    return 0
  fi

  git -C "$repo" add docs/secure-development Lastenheft_Secure-Development-Hardening.md Lastenheft_Abarbeitungsreihenfolge.md
  git -C "$repo" diff --cached --check

  if ! git -C "$repo" diff --cached --quiet; then
    git -C "$repo" commit -m "docs: prepare secure development hardening"
  fi

  if $OPT_PUSH; then
    branch="$(git -C "$repo" branch --show-current)"
    [ -n "$branch" ] || die "Kein aktueller Branch in $repo"
    git -C "$repo" push origin "$branch"
  fi
}

prepare_repo() {
  local repo="$1"
  local status project_name dry force

  project_name="$(basename "$repo")"
  log "## $repo"

  if ! $OPT_DRY_RUN && ! $OPT_ALLOW_DIRTY; then
    status="$(git -C "$repo" status --short)"
    [ -z "$status" ] || die "Repo hat lokale Aenderungen: $repo"
  fi

  dry=0
  force=0
  $OPT_DRY_RUN && dry=1

  if ! sdh_prepare_repo "$repo" "$project_name" "$OPT_PRIMARY_LANGUAGE" "$dry" "$force" "$SCRIPT_DIR"; then
    die "$SDH_PREPARE_REASON"
  fi

  case "$SDH_PREPARE_RESULT" in
    prepared)
      log "  vorbereitet: $SDH_PREPARE_REASON"
      commit_and_push "$repo"
      ;;
    skipped)
      log "  uebersprungen: $SDH_PREPARE_REASON"
      ;;
    *)
      log "  Status: $SDH_PREPARE_RESULT $SDH_PREPARE_REASON"
      ;;
  esac
}

discover_repos

log "Secure-Development-Hardening Vorbereitung"
log "  Home             : $HOME_DIR"
if [ "${#OPT_REPOS[@]}" -gt 0 ]; then
  log "  Repos            : ${#OPT_REPOS[@]} explizit"
fi
log "  Primaersprache   : ${OPT_PRIMARY_LANGUAGE:-auto}"
log "  Commit           : $OPT_COMMIT"
log "  Push             : $OPT_PUSH"
log "  Dry-run          : $OPT_DRY_RUN"
log ""

if [ "${#REPOS[@]}" -eq 0 ]; then
  die "Keine Level-2-Repos gefunden"
fi

for repo in "${REPOS[@]}"; do
  prepare_repo "$repo"
done

log ""
log "Secure-Development-Hardening Vorbereitung abgeschlossen."
