#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FORGEJO_LIB="$SCRIPT_DIR/lib/hg-forgejo.sh"
SOURCE_RESOLVER="$SCRIPT_DIR/lib/resolve-home-baseline-source.sh"
if [ -f "$FORGEJO_LIB" ]; then
  # shellcheck source=scripts/lib/hg-forgejo.sh
  source "$FORGEJO_LIB"
fi
if [ -f "$SOURCE_RESOLVER" ]; then
  # shellcheck source=scripts/lib/resolve-home-baseline-source.sh
  source "$SOURCE_RESOLVER"
fi

BOX_WIDTH=66

EXIT_CODE=0
DRY_RUN=0
FORCE=0
YES=0
BACKUP=0
KEEP_REMOTE=0
RECURSIVE=0
WORKSPACE_NAME=""
WORKSPACE_DIR=""
HOME_DIR=""
NORMALIZED_NAME=""
README_PATH=""
GITIGNORE_PATH=""
GITCONFIG_PATH=""
GITCONFIG_D=""
INC_FILE=""

declare -a LEVEL2_PROJECTS=()
declare -a RESULTS=()
declare -A APPROVED_REMOTE_IDENTITIES=()
declare -A APPROVED_GIT_MARKERS=()

usage() {
  cat <<'EOF'
Verwendung / Usage:
  teardown-workspace.sh <WorkspaceName> [OPTIONEN / OPTIONS]

WorkspaceName:
  Einfacher Name eines echten direkten Home-Unterverzeichnisses /
  Simple name of a real direct Home child directory

Optionen / Options:
  --backup        Erstellt vor der Löschung ein Backup-Archiv / Create backup archive before deletion
  --keep-remote   Überspringt das Remote-Repository / Skip remote repository deletion
  --recursive     Verarbeitet Level-2-Repositories vor dem Workspace / Process Level-2 repositories first
  --force         Überspringt Sicherheitsprüfungen / Skip safety checks
  --yes           Überspringt die Rückfrage / Skip confirmation prompt
  --dry-run       Zeigt alle Aktionen ohne Ausführung / Show all actions without executing
  --help          Zeigt diese Hilfe / Show this help
EOF
}

set_warning_exit() {
  if [ "$EXIT_CODE" -lt 1 ]; then
    EXIT_CODE=1
  fi
}

add_result() {
  RESULTS+=("$1|$2")
}

box_line() {
  printf '║ %-66.66s ║\n' "$1"
}

print_box() {
  local title="$1"
  shift

  echo "╔════════════════════════════════════════════════════════════════════╗"
  box_line "  $title"
  echo "╠════════════════════════════════════════════════════════════════════╣"

  while [ "$#" -gt 0 ]; do
    box_line "$1"
    shift
  done

  echo "╚════════════════════════════════════════════════════════════════════╝"
}

normalize_name() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/-\+/-/g' | sed 's/^-\|-$//g'
}

resolve_home_dir() {
  local candidate=""

  if [ -n "${HOME:-}" ]; then
    candidate="$HOME"
  elif [ -n "${USERPROFILE:-}" ]; then
    candidate="$USERPROFILE"
  else
    candidate="$(cd ~ && pwd)"
  fi

  (
    cd "$candidate" >/dev/null 2>&1 && pwd -P
  )
}

validate_workspace_name() {
  case "$WORKSPACE_NAME" in
    .|..|*/*|*\\*)
      echo "Fehler: Workspace-Name muss ein einzelnes direktes Unterverzeichnis von Home sein / Error: Workspace name must be one direct child directory of Home" >&2
      exit 2
      ;;
  esac
}

resolve_direct_child() {
  local expected_parent="$1"
  local expected_name="$2"
  local candidate="$3"
  local resolved=""

  if [ ! -d "$candidate" ]; then
    return 1
  fi
  resolved="$(cd "$candidate" >/dev/null 2>&1 && pwd -P)" || return 1
  if [ "$(dirname "$resolved")" != "$expected_parent" ] ||
     [ "$(basename "$resolved")" != "$expected_name" ]; then
    return 1
  fi
  if [ -L "$resolved/.git" ]; then
    return 1
  fi
  printf '%s\n' "$resolved"
}

parse_args() {
  while [ "$#" -gt 0 ]; do
    case "$1" in
      --backup)
        BACKUP=1
        ;;
      --keep-remote)
        KEEP_REMOTE=1
        ;;
      --recursive)
        RECURSIVE=1
        ;;
      --force)
        FORCE=1
        ;;
      --yes)
        YES=1
        ;;
      --dry-run)
        DRY_RUN=1
        ;;
      --help|-h)
        usage
        exit 0
        ;;
      --)
        shift
        if [ $# -gt 0 ] && [ -z "$WORKSPACE_NAME" ]; then WORKSPACE_NAME="$1"; shift; fi
        continue
        ;;
      --*)
        echo "Fehler: Unbekannte Option '$1' / Error: Unknown option '$1'" >&2
        exit 2
        ;;
      *)
        if [ -n "$WORKSPACE_NAME" ]; then
          echo "Fehler: Mehr als ein Workspace-Name angegeben / Error: More than one workspace name provided" >&2
          exit 2
        fi
        WORKSPACE_NAME="$1"
        ;;
    esac
    shift
  done

  if [ -z "$WORKSPACE_NAME" ]; then
    usage >&2
    exit 2
  fi
}

validate_context() {
  local candidate=""
  local resolved=""
  local resolved_parent=""
  local resolved_name=""
  local protected_source=""

  HOME_DIR="$(resolve_home_dir)"
  validate_workspace_name

  candidate="$HOME_DIR/$WORKSPACE_NAME"
  NORMALIZED_NAME="$(normalize_name "$WORKSPACE_NAME")"
  README_PATH="$HOME_DIR/README.md"
  GITIGNORE_PATH="$HOME_DIR/.gitignore"
  GITCONFIG_PATH="$HOME_DIR/.gitconfig"
  GITCONFIG_D="$HOME_DIR/.gitconfig.d"
  INC_FILE="$GITCONFIG_D/$NORMALIZED_NAME.inc"

  case "$(printf '%s' "$WORKSPACE_NAME" | tr '[:upper:]' '[:lower:]')" in
    home-baseline|home-baseline-source)
      echo "Fehler: Level-0-Quelle ist geschützt / Error: Level 0 source is protected" >&2
      exit 2
      ;;
  esac

  if [ ! -d "$candidate" ]; then
    echo "Fehler: Workspace '$candidate' nicht gefunden / Error: Workspace '$candidate' not found" >&2
    exit 2
  fi

  resolved="$(resolve_direct_child "$HOME_DIR" "$WORKSPACE_NAME" "$candidate" || true)"
  if [ -z "$resolved" ]; then
    echo "Fehler: Workspace muss ein echtes direktes Unterverzeichnis von Home sein; Links und Pfadumgehungen sind unzulässig / Error: Workspace must be a real direct child of Home; links and path escapes are not allowed" >&2
    exit 2
  fi
  resolved_parent="$(dirname "$resolved")"
  resolved_name="$(basename "$resolved")"
  if [ "$resolved_parent" != "$HOME_DIR" ] || [ "$resolved_name" != "$WORKSPACE_NAME" ]; then
    echo "Fehler: Workspace muss ein echtes direktes Unterverzeichnis von Home sein; Links und Pfadumgehungen sind unzulässig / Error: Workspace must be a real direct child of Home; links and path escapes are not allowed" >&2
    exit 2
  fi

  if ! declare -F resolve_hb_source_repository >/dev/null 2>&1; then
    echo "Fehler: Level-0-Quelle nicht pruefbar / Error: Level 0 source unavailable" >&2
    exit 2
  fi
  protected_source="$(resolve_hb_source_repository "$HOME_DIR/README.md" 1 2>/dev/null)" || {
    echo "Fehler: Level-0-Quelle nicht pruefbar / Error: Level 0 source unavailable" >&2
    exit 2
  }
  if [ -n "$protected_source" ] && [ "$resolved" = "$protected_source" ]; then
    echo "Fehler: Konfigurierte Level-0-Quelle ist geschützt / Error: Configured Level 0 source is protected" >&2
    exit 2
  fi

  WORKSPACE_DIR="$resolved"
}

discover_level2_projects() {
  local gitdir="" discovered=""

  LEVEL2_PROJECTS=()
  discovered="$(find "$WORKSPACE_DIR" -mindepth 2 -maxdepth 2 -name ".git" \( -type d -o -type f -o -type l \) 2>/dev/null | sort)" || {
    echo "Fehler: Level-2-Projekte nicht pruefbar / Error: Level 2 projects unavailable" >&2
    return 1
  }
  while IFS= read -r gitdir; do
    if [ -n "$gitdir" ]; then
      LEVEL2_PROJECTS+=("$(dirname "$gitdir")")
    fi
  done <<< "$discovered"
}

has_git_marker() {
  [ -e "$1/.git" ] || [ -L "$1/.git" ]
}

check_git_metadata() {
  local inside=""
  inside="$(git -C "$1" rev-parse --is-inside-work-tree 2>/dev/null)" || return 1
  [ "$inside" = "true" ] || return 1
  git -C "$1" config --local --list >/dev/null 2>&1
}

origin_for_dir() {
  local dir="$1" remotes=""
  remotes="$(git -C "$dir" remote 2>/dev/null)" || return 1
  if grep -Fxq 'origin' <<< "$remotes"; then
    git -C "$dir" remote get-url origin 2>/dev/null
  else
    printf ''
  fi
}

remote_platform_for_dir() {
  local dir="$1"
  local remote_url=""
  local configured_platform=""
  local parsed=""

  remote_url="$(git -C "$dir" remote get-url origin 2>/dev/null || true)"
  configured_platform="$(git -C "$dir" config --local --get home-baseline.remote-platform 2>/dev/null || true)"
  if [ -z "$remote_url" ]; then
    echo "kein Remote / no remote"
  elif [ "$configured_platform" = "forgejo" ] || [ "$configured_platform" = "codeberg" ]; then
    if [ "$KEEP_REMOTE" -eq 1 ]; then
      echo "$configured_platform"
    else
      echo "${APPROVED_REMOTE_IDENTITIES[$dir]:-unsicheres Ziel / unsafe target}" | tr '|' ' '
    fi
  elif [ "$KEEP_REMOTE" -eq 0 ]; then
    echo "${APPROVED_REMOTE_IDENTITIES[$dir]:-none}" | tr '|' ' '
  else
    parsed="$(python3 "$SCRIPT_DIR/lib/parse_teardown_remote.py" "$remote_url" 2>/dev/null || true)"
    case "${parsed%%$'\t'*}" in
      github) echo "GitHub ${parsed#*$'\t'}" ;;
      gitlab) echo "GitLab ${parsed#*$'\t'}" ;;
      *) echo "anderes Remote / other remote" ;;
    esac
  fi
}

forgejo_target_for_dir() {
  local dir="$1"
  local origin="" platform="" base_url="" owner="" repository=""
  origin="$(git -C "$dir" remote get-url origin 2>/dev/null || true)"
  platform="$(git -C "$dir" config --local --get home-baseline.remote-platform 2>/dev/null || true)"
  base_url="$(git -C "$dir" config --local --get home-baseline.remote-base-url 2>/dev/null || true)"
  owner="$(git -C "$dir" config --local --get home-baseline.remote-owner 2>/dev/null || true)"
  repository="$(git -C "$dir" config --local --get home-baseline.remote-repository 2>/dev/null || true)"
  python3 "$SCRIPT_DIR/lib/validate_forgejo_teardown_remote.py" \
    "$origin" "$base_url" "$platform" "$owner" "$repository"
}

prepare_remote_targets() {
  local dir="" platform="" identity="" origin="" parsed=""
  for dir in "${LEVEL2_PROJECTS[@]}" "$WORKSPACE_DIR"; do
    APPROVED_GIT_MARKERS["$dir"]="none"
    APPROVED_REMOTE_IDENTITIES["$dir"]="none"
    if ! has_git_marker "$dir"; then continue; fi
    APPROVED_GIT_MARKERS["$dir"]="git"
    [ "$KEEP_REMOTE" -eq 0 ] || continue
    check_git_metadata "$dir" || {
      echo "Fehler: Git-Metadaten nicht pruefbar / Error: Git metadata unavailable: $dir" >&2
      return 1
    }
    origin="$(origin_for_dir "$dir")" || {
      echo "Fehler: Git-Remote nicht pruefbar / Error: Git remote unavailable: $dir" >&2
      return 1
    }
    [ -n "$origin" ] || continue
    platform="$(git -C "$dir" config --local --get home-baseline.remote-platform 2>/dev/null || true)"
    case "$platform" in
      forgejo|codeberg)
        identity="$(forgejo_target_for_dir "$dir")" || {
          echo "Fehler: Forgejo/Codeberg-Ziel stimmt nicht mit origin ueberein / Error: target does not match origin: $dir" >&2
          return 1
        }
        APPROVED_REMOTE_IDENTITIES["$dir"]="$platform|$identity"
        ;;
      *)
        parsed="$(python3 "$SCRIPT_DIR/lib/parse_teardown_remote.py" "$origin" 2>/dev/null)" || {
          echo "Fehler: Remote-Ziel ist ungueltig / Error: remote target is invalid: $dir" >&2
          return 1
        }
        APPROVED_REMOTE_IDENTITIES["$dir"]="${parsed%%$'\t'*}|${parsed#*$'\t'}"
        ;;
    esac
  done
}

build_preamble() {
  local title="teardown-workspace - Workspace-Entfernung / Workspace Removal"
  local line=""
  local project=""
  local project_name=""
  local remote_desc=""

  if [ "$DRY_RUN" -eq 1 ]; then
    title="[DRY-RUN] $title"
  fi

  box_line_buffer=()
  box_line_buffer+=("  Workspace:   $WORKSPACE_NAME")
  box_line_buffer+=("  Pfad / Path: $WORKSPACE_DIR")
  box_line_buffer+=("")
  box_line_buffer+=("  Geplante Aktionen / Planned actions:")

  if [ "${#LEVEL2_PROJECTS[@]}" -gt 0 ]; then
    for project in "${LEVEL2_PROJECTS[@]}"; do
      project_name="$(basename "$project")"
      remote_desc="$(remote_platform_for_dir "$project")"
      line="    L2 $project_name: Sicherheitsprüfung / Safety"
      if [ "$FORCE" -eq 1 ]; then
        line="    L2 $project_name: --force überspringt Safety / --force skips safety"
      fi
      box_line_buffer+=("$line")
      if [ "$BACKUP" -eq 1 ]; then
        box_line_buffer+=("      Backup / backup: $(basename "$(planned_backup_path "$project_name")")")
      fi
      box_line_buffer+=("      Remote / remote: $remote_desc")
      box_line_buffer+=("      Lokal löschen / delete local directory")
    done
  fi

  if [ "$BACKUP" -eq 1 ]; then
    box_line_buffer+=("    1. Backup / backup: $(basename "$(planned_backup_path "$WORKSPACE_NAME")")")
  fi

  if [ "$FORCE" -eq 1 ]; then
    box_line_buffer+=("    2. --force: Sicherheitsprüfungen übersprungen / safety checks skipped")
  else
    box_line_buffer+=("    2. Sicherheitsprüfung / safety check")
  fi

  box_line_buffer+=("    3. Remote / remote: $(remote_platform_for_dir "$WORKSPACE_DIR")")
  box_line_buffer+=("    4. Verzeichnis löschen / delete directory")
  box_line_buffer+=("    5. Artefakte bereinigen / clean up artifacts")
  box_line_buffer+=("       - ~/README.md")
  box_line_buffer+=("       - ~/.gitignore")
  box_line_buffer+=("       - ~/.gitconfig")
  box_line_buffer+=("       - ~/.gitconfig.d/$NORMALIZED_NAME.inc")

  print_box "$title" "${box_line_buffer[@]}"
  local target_dir=""
  for target_dir in "${LEVEL2_PROJECTS[@]}" "$WORKSPACE_DIR"; do
    if [ -n "${APPROVED_REMOTE_IDENTITIES[$target_dir]:-}" ] &&
       [ "${APPROVED_REMOTE_IDENTITIES[$target_dir]}" != "none" ]; then
      printf 'Remote-Loeschziel / Remote deletion target (%s): %s\n' \
        "$target_dir" "${APPROVED_REMOTE_IDENTITIES[$target_dir]}"
    fi
  done
}

planned_backup_path() {
  local target_name="$1"
  printf '%s/%s-backup-%s.tar.gz' "$HOME_DIR" "$target_name" "$(date +%Y-%m-%d)"
}

confirm_or_abort() {
  local answer=""

  if [ "$DRY_RUN" -eq 1 ] || [ "$YES" -eq 1 ]; then
    return 0
  fi

  printf 'Fortfahren? / Proceed? [y/N]: '
  read -r answer
  case "$answer" in
    y|Y)
      ;;
    *)
      echo "Abgebrochen / Aborted."
      exit 1
      ;;
  esac
}

check_safety() {
  local label="$1"
  local dir="$2"
  local preflight="${3:-0}"
  local status="" stash="" branches="" branch="" branch_name="" upstream="" remote="" ahead=""

  if [ "$FORCE" -eq 1 ]; then
    if [ "$preflight" -eq 0 ]; then
      add_result "skip" "Sicherheitsprüfung übersprungen / Safety check skipped: $label"
    fi
    return 0
  fi

  if [ "${APPROVED_GIT_MARKERS[$dir]:-}" = "git" ] && ! has_git_marker "$dir"; then
    add_result "fail" "Git-Metadaten seit Vorschau entfernt / Git metadata removed after preview: $label"
    set_warning_exit
    return 1
  fi
  if [ "${APPROVED_GIT_MARKERS[$dir]:-}" = "none" ] && has_git_marker "$dir"; then
    add_result "fail" "Git-Metadaten seit Vorschau hinzugefuegt / Git metadata added after preview: $label"
    set_warning_exit
    return 1
  fi

  if ! has_git_marker "$dir"; then
    if [ "$preflight" -eq 0 ]; then
      add_result "skip" "Kein Git-Repository für Sicherheitsprüfung / No git repository for safety check: $label"
    fi
    return 0
  fi

  if ! check_git_metadata "$dir"; then
    add_result "fail" "Git-Metadaten nicht pruefbar / Git metadata unavailable: $label"
    set_warning_exit
    return 1
  fi
  status="$(git -C "$dir" status --porcelain --ignored=matching --untracked-files=all 2>/dev/null)" || {
    add_result "fail" "Git-Status nicht pruefbar / Git status unavailable: $label"
    set_warning_exit
    return 1
  }
  if [ -n "$status" ]; then
    add_result "fail" "Lokale oder ignorierte Dateien erkannt / Local or ignored files detected: $label"
    set_warning_exit
    return 1
  fi

  stash="$(git -C "$dir" for-each-ref --format='%(refname)' refs/stash 2>/dev/null)" || {
    add_result "fail" "Git-Stash nicht pruefbar / Git stash unavailable: $label"
    set_warning_exit
    return 1
  }
  if [ -n "$stash" ]; then
    add_result "fail" "Git-Stash enthaelt lokale Arbeit / Git stash contains local work: $label"
    set_warning_exit
    return 1
  fi

  if ! git -C "$dir" symbolic-ref --quiet HEAD >/dev/null 2>&1; then
    add_result "fail" "Git-HEAD ohne pruefbaren Branch / Git HEAD has no verifiable branch: $label"
    set_warning_exit
    return 1
  fi
  branches="$(git -C "$dir" for-each-ref --format='%(refname)%09%(upstream)' refs/heads 2>/dev/null)" || {
    add_result "fail" "Git-Branches nicht pruefbar / Git branches unavailable: $label"
    set_warning_exit
    return 1
  }
  while IFS=$'\t' read -r branch upstream; do
    [ -n "$branch" ] || continue
    branch_name="${branch#refs/heads/}"
    remote="$(git -C "$dir" config --local --get "branch.$branch_name.remote" 2>/dev/null)" || {
      add_result "fail" "Git-Branch ohne pruefbaren Remote-Upstream / Git branch has no verifiable remote upstream: $label"
      set_warning_exit
      return 1
    }
    if [ -z "$remote" ] || [ "$remote" = "." ] ||
       [[ "$upstream" != "refs/remotes/$remote/"* ]] ||
       ! git -C "$dir" remote get-url "$remote" >/dev/null 2>&1; then
      add_result "fail" "Git-Branch ohne pruefbaren Remote-Upstream / Git branch has no verifiable remote upstream: $label"
      set_warning_exit
      return 1
    fi
    ahead="$(git -C "$dir" rev-list --count "$upstream..$branch" 2>/dev/null)" || {
      add_result "fail" "Git-Historie nicht pruefbar / Git history unavailable: $label"
      set_warning_exit
      return 1
    }
    if [[ ! "$ahead" =~ ^[0-9]+$ ]] || [ "$ahead" -ne 0 ]; then
      add_result "fail" "Ungepushte Commits erkannt / Unpushed commits detected: $label"
      set_warning_exit
      return 1
    fi
  done <<< "$branches"

  if [ "$preflight" -eq 0 ]; then
    add_result "done" "Sicherheitsprüfung bestanden / Safety check passed: $label"
  fi
}

preflight_all_safety() {
  local project="" project_name=""
  for project in "${LEVEL2_PROJECTS[@]}"; do
    project_name="$(basename "$project")"
    check_safety "Level-2 $project_name" "$project" 1 || return 1
  done
  check_safety "Workspace $WORKSPACE_NAME" "$WORKSPACE_DIR" 1
}

unique_backup_path() {
  local target_name="$1"
  local base=""
  local archive=""
  local index=1

  base="$HOME_DIR/$target_name-backup-$(date +%Y-%m-%d)"
  archive="${base}.tar.gz"
  while [ -e "$archive" ] || [ -L "$archive" ]; do
    archive="${base}-${index}.tar.gz"
    index=$((index + 1))
  done

  printf '%s\n' "$archive"
}

create_backup() {
  local label="$1"
  local dir="$2"
  local target_name="$3"
  local archive=""

  if [ "$BACKUP" -ne 1 ]; then
    return 0
  fi

  if ! command -v tar >/dev/null 2>&1; then
    add_result "fail" "Backup nicht erstellt, tar fehlt / Backup not created, tar missing: $label"
    set_warning_exit
    return 1
  fi

  archive="$(unique_backup_path "$target_name")"
  if tar czf "$archive" -C "$(dirname "$dir")" "./$(basename "$dir")" >/dev/null 2>&1 && [ -s "$archive" ]; then
    add_result "done" "Backup erstellt / Backup created: $(basename "$archive")"
  else
    add_result "fail" "Backup fehlgeschlagen / Backup failed: $label"
    set_warning_exit
    return 1
  fi
}

delete_remote_repo() {
  local label="$1"
  local dir="$2"
  local remote_url=""
  local owner_repo=""
  local configured_platform=""
  local forgejo_base_url=""
  local forgejo_owner=""
  local forgejo_repository=""
  local parsed=""
  local approved="${APPROVED_REMOTE_IDENTITIES[$dir]:-}"

  if [ "$KEEP_REMOTE" -eq 1 ]; then
    add_result "skip" "Remote bewusst behalten / Remote intentionally kept: $label"
    return 0
  fi

  if [ -z "$approved" ]; then
    add_result "fail" "Remote-Vorschau fehlt / Remote preview is missing: $label"
    set_warning_exit
    return 1
  fi

  if [ "${APPROVED_GIT_MARKERS[$dir]:-}" = "git" ] && ! has_git_marker "$dir"; then
    add_result "fail" "Git-Metadaten seit Vorschau entfernt / Git metadata removed after preview: $label"
    set_warning_exit
    return 1
  fi
  if [ "${APPROVED_GIT_MARKERS[$dir]:-}" = "none" ] && has_git_marker "$dir"; then
    add_result "fail" "Git-Metadaten seit Vorschau hinzugefuegt / Git metadata added after preview: $label"
    set_warning_exit
    return 1
  fi

  if ! has_git_marker "$dir"; then
    if [ "$approved" != "none" ]; then
      add_result "fail" "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $label"
      set_warning_exit
      return 1
    fi
    add_result "skip" "Kein Git-Repository, Remote-Schritt übersprungen / No git repository, remote step skipped: $label"
    return 0
  fi

  if ! check_git_metadata "$dir"; then
    add_result "fail" "Git-Metadaten nicht pruefbar / Git metadata unavailable: $label"
    set_warning_exit
    return 1
  fi
  remote_url="$(origin_for_dir "$dir")" || {
    add_result "fail" "Git-Remote nicht pruefbar / Git remote unavailable: $label"
    set_warning_exit
    return 1
  }
  if [ "$approved" != "none" ] && [ -z "$remote_url" ]; then
    add_result "fail" "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $label"
    set_warning_exit
    return 1
  fi
  if [ -z "$remote_url" ]; then
    add_result "skip" "Kein Remote konfiguriert / No remote configured: $label"
    return 0
  fi
  if [ "$approved" = "none" ]; then
    add_result "fail" "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $label"
    set_warning_exit
    return 1
  fi

  configured_platform="$(git -C "$dir" config --local --get home-baseline.remote-platform 2>/dev/null || true)"
  if [ "$configured_platform" = "forgejo" ] || [ "$configured_platform" = "codeberg" ]; then
    if [ ! -f "$FORGEJO_LIB" ]; then
      add_result "fail" "Forgejo-Bibliothek fehlt, Remote-Löschung abgebrochen / Forgejo library missing, remote deletion aborted: $label"
      set_warning_exit
      return 1
    fi
    forgejo_base_url="$(git -C "$dir" config --local --get home-baseline.remote-base-url 2>/dev/null || true)"
    forgejo_owner="$(git -C "$dir" config --local --get home-baseline.remote-owner 2>/dev/null || true)"
    forgejo_repository="$(git -C "$dir" config --local --get home-baseline.remote-repository 2>/dev/null || true)"
    if [ -z "$forgejo_base_url" ] || [ -z "$forgejo_owner" ] || [ -z "$forgejo_repository" ]; then
      add_result "fail" "Forgejo-Metadaten fehlen, bitte --keep-remote verwenden / Forgejo metadata missing, use --keep-remote: $label"
      set_warning_exit
      return 1
    fi
    local verified_identity=""
    verified_identity="$(python3 "$SCRIPT_DIR/lib/validate_forgejo_teardown_remote.py" \
      "$remote_url" "$forgejo_base_url" "$configured_platform" "$forgejo_owner" "$forgejo_repository")" || {
      add_result "fail" "Forgejo/Codeberg-Ziel stimmt nicht mit origin ueberein / target does not match origin: $label"
      set_warning_exit
      return 1
    }
    if [ "$configured_platform|$verified_identity" != "$approved" ]; then
      add_result "fail" "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $label"
      set_warning_exit
      return 1
    fi
    if hb_forgejo_delete_repository "$forgejo_base_url" "$forgejo_owner" "$forgejo_repository"; then
      add_result "done" "$configured_platform-Remote gelöscht / remote deleted: $forgejo_owner/$forgejo_repository"
      return 0
    fi
    add_result "fail" "$configured_platform-Remote konnte nicht gelöscht werden / remote could not be deleted: $forgejo_owner/$forgejo_repository"
    set_warning_exit
    return 1
  fi

  parsed="$(python3 "$SCRIPT_DIR/lib/parse_teardown_remote.py" "$remote_url" 2>/dev/null)" || {
    add_result "fail" "Unbekanntes oder unsicheres Remote, bitte --keep-remote verwenden / Unknown or unsafe remote, use --keep-remote: $label"
    set_warning_exit
    return 1
  }
  owner_repo="${parsed#*$'\t'}"
  if [ "${parsed%%$'\t'*}|$owner_repo" != "$approved" ]; then
    add_result "fail" "Remote-Ziel hat sich nach der Vorschau geaendert / Remote target changed after preview: $label"
    set_warning_exit
    return 1
  fi
  if [ "${parsed%%$'\t'*}" = "github" ]; then
    if ! command -v gh >/dev/null 2>&1; then
      add_result "fail" "gh fehlt, Remote-Löschung abgebrochen / gh missing, remote deletion aborted: $label"
      set_warning_exit
      return 1
    fi
    if gh repo delete "$owner_repo" --yes >/dev/null 2>&1; then
      add_result "done" "Remote-Repo gelöscht / Remote repo deleted: $owner_repo"
      return 0
    fi
    add_result "fail" "GitHub-Remote konnte nicht gelöscht werden / GitHub remote could not be deleted: $owner_repo"
    set_warning_exit
    return 1
  fi

  if [ "${parsed%%$'\t'*}" = "gitlab" ]; then
    if ! command -v glab >/dev/null 2>&1; then
      add_result "fail" "glab fehlt, Remote-Löschung abgebrochen / glab missing, remote deletion aborted: $owner_repo"
      set_warning_exit
      return 1
    fi
    if glab repo delete "$owner_repo" --yes >/dev/null 2>&1; then
      add_result "done" "GitLab-Remote gelöscht / GitLab remote deleted: $owner_repo"
      return 0
    fi
    add_result "fail" "GitLab-Remote konnte nicht gelöscht werden / GitLab remote could not be deleted: $owner_repo"
    set_warning_exit
    return 1
  fi

  add_result "fail" "Nicht unterstütztes Remote, bitte --keep-remote verwenden / Unsupported remote, use --keep-remote: $label"
  set_warning_exit
  return 1
}

delete_local_directory() {
  local label="$1"
  local dir="$2"

  if ! rm -rf "$dir" || [ -e "$dir" ] || [ -L "$dir" ]; then
    add_result "fail" "Verzeichnis konnte nicht geloescht werden / Directory could not be deleted: $label"
    set_warning_exit
    return 1
  fi
  add_result "done" "Verzeichnis gelöscht / Directory deleted: $label"
}

finish_cleanup_file() {
  local source="$1"
  local tmp_file="$2"
  local changed_message="$3"
  local missing_message="$4"
  local compare_status=0

  cmp -s "$source" "$tmp_file" || compare_status=$?
  if [ "$compare_status" -gt 1 ]; then
    rm -f "$tmp_file"
    add_result "fail" "Artefaktvergleich fehlgeschlagen / Artifact comparison failed: $source"
    set_warning_exit
    return 1
  fi
  if [ "$compare_status" -eq 0 ]; then
    rm -f "$tmp_file"
    add_result "skip" "$missing_message"
    return 0
  fi

  if ! mv "$tmp_file" "$source"; then
    rm -f "$tmp_file"
    add_result "fail" "Artefakt konnte nicht bereinigt werden / Artifact cleanup failed: $source"
    set_warning_exit
    return 1
  fi
  add_result "done" "$changed_message"
}

cleanup_readme() {
  local tmp_file="$README_PATH.tmp.$$"

  if [ ! -f "$README_PATH" ]; then
    add_result "skip" "README.md fehlt / README.md missing"
    return 0
  fi

  if ! awk -v workspace="$WORKSPACE_NAME" 'index($0, "~/" workspace "/") == 0 { print }' "$README_PATH" > "$tmp_file"; then
    rm -f "$tmp_file"
    add_result "fail" "README.md konnte nicht gelesen werden / README.md could not be read"
    set_warning_exit
    return 1
  fi
  finish_cleanup_file "$README_PATH" "$tmp_file" "README.md bereinigt / README.md cleaned up" "README.md-Eintrag nicht vorhanden / README.md entry not present"
}

cleanup_gitignore() {
  local tmp_file="$GITIGNORE_PATH.tmp.$$"

  if [ ! -f "$GITIGNORE_PATH" ]; then
    add_result "skip" ".gitignore fehlt / .gitignore missing"
    return 0
  fi

  if ! awk -v entry="$WORKSPACE_NAME/" '$0 != entry { print }' "$GITIGNORE_PATH" > "$tmp_file"; then
    rm -f "$tmp_file"
    add_result "fail" ".gitignore konnte nicht gelesen werden / .gitignore could not be read"
    set_warning_exit
    return 1
  fi
  finish_cleanup_file "$GITIGNORE_PATH" "$tmp_file" ".gitignore bereinigt / .gitignore cleaned up" ".gitignore-Eintrag nicht vorhanden / .gitignore entry not present"
}

cleanup_gitconfig() {
  local tmp_file="$GITCONFIG_PATH.tmp.$$"
  local tilde_header="[includeIf \"gitdir:~/$WORKSPACE_NAME/\"]"
  local expanded_header="[includeIf \"gitdir:$WORKSPACE_DIR/\"]"

  if [ ! -f "$GITCONFIG_PATH" ]; then
    add_result "skip" ".gitconfig fehlt / .gitconfig missing"
    return 0
  fi

  if ! awk -v header1="$tilde_header" -v header2="$expanded_header" '
    $0 == header1 || $0 == header2 { skip = 1; removed = 1; next }
    skip && /^[[:space:]]/ { next }
    { skip = 0; print }
  ' "$GITCONFIG_PATH" > "$tmp_file"; then
    rm -f "$tmp_file"
    add_result "fail" ".gitconfig konnte nicht gelesen werden / .gitconfig could not be read"
    set_warning_exit
    return 1
  fi
  finish_cleanup_file "$GITCONFIG_PATH" "$tmp_file" ".gitconfig bereinigt / .gitconfig cleaned up" ".gitconfig includeIf-Block nicht vorhanden / .gitconfig includeIf block not present"
}

cleanup_inc_file() {
  if [ ! -d "$GITCONFIG_D" ]; then
    add_result "skip" "~/.gitconfig.d fehlt / ~/.gitconfig.d missing"
    return 0
  fi

  if [ ! -f "$INC_FILE" ]; then
    add_result "skip" ".inc-Datei nicht vorhanden / .inc file not present: $NORMALIZED_NAME.inc"
    return 0
  fi

  if ! rm -f "$INC_FILE" || [ -e "$INC_FILE" ] || [ -L "$INC_FILE" ]; then
    add_result "fail" ".inc-Datei konnte nicht geloescht werden / .inc file could not be deleted: $NORMALIZED_NAME.inc"
    set_warning_exit
    return 1
  fi
  add_result "done" ".inc-Datei gelöscht / .inc file deleted: $NORMALIZED_NAME.inc"
}

commit_artifacts() {
  local staged=0
  local subject="chore: teardown $WORKSPACE_NAME - Artefakte bereinigt / artifacts cleaned up"
  local -a artifact_paths=()

  if ! git -C "$HOME_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    add_result "skip" "Artefakt-Commit übersprungen, ~/ ist kein Git-Repo / Artifact commit skipped, ~/ is not a git repo"
    set_warning_exit
    return 0
  fi

  if [ -f "$README_PATH" ]; then
    artifact_paths+=(README.md)
    git -C "$HOME_DIR" add --update -- README.md >/dev/null 2>&1 || {
      add_result "fail" "README-Commit-Vorbereitung fehlgeschlagen / README commit preparation failed"
      set_warning_exit
      return 1
    }
  fi
  if [ -f "$GITIGNORE_PATH" ]; then
    artifact_paths+=(.gitignore)
    git -C "$HOME_DIR" add --update -- .gitignore >/dev/null 2>&1 || {
      add_result "fail" "Gitignore-Commit-Vorbereitung fehlgeschlagen / gitignore commit preparation failed"
      set_warning_exit
      return 1
    }
  fi

  local diff_status=0
  git -C "$HOME_DIR" diff --cached --quiet -- README.md .gitignore >/dev/null 2>&1 || diff_status=$?
  if [ "$diff_status" -gt 1 ]; then
    add_result "fail" "Artefakt-Diff nicht pruefbar / Artifact diff unavailable"
    set_warning_exit
    return 1
  fi
  if [ "$diff_status" -eq 1 ]; then
    staged=1
  fi

  if [ "$staged" -eq 0 ]; then
    add_result "skip" "Kein Artefakt-Commit nötig / No artifact commit needed"
    return 0
  fi

  if git -C "$HOME_DIR" commit --only -m "$subject" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>" -- "${artifact_paths[@]}" >/dev/null 2>&1; then
    add_result "done" "Artefakte committed / Artifacts committed"
  else
    add_result "fail" "Artefakt-Commit fehlgeschlagen / Artifact commit failed"
    set_warning_exit
    return 1
  fi
}

check_home_artifacts_clean() {
  local status=""
  if ! git -C "$HOME_DIR" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    if has_git_marker "$HOME_DIR"; then
      add_result "fail" "Home-Git-Metadaten nicht pruefbar / Home Git metadata unavailable"
      set_warning_exit
      return 1
    fi
    return 0
  fi
  status="$(git -C "$HOME_DIR" status --porcelain -- README.md .gitignore)" || {
    add_result "fail" "Home-Artefaktstatus nicht pruefbar / Home artifact status unavailable"
    set_warning_exit
    return 1
  }
  if [ -n "$status" ]; then
    add_result "fail" "Vorhandene Home-Artefaktaenderungen blockieren Teardown / Existing Home artifact changes block teardown"
    set_warning_exit
    return 1
  fi
}

cleanup_workspace_artifacts() {
  cleanup_readme || return 1
  cleanup_gitignore || return 1
  cleanup_gitconfig || return 1
  cleanup_inc_file || return 1
  commit_artifacts
}

teardown_target() {
  local label="$1"
  local dir="$2"
  local backup_name="$3"
  local include_artifacts="$4"
  local expected_parent="$WORKSPACE_DIR"
  local validated_dir=""

  if [ "$include_artifacts" -eq 1 ]; then
    expected_parent="$HOME_DIR"
  fi

  validated_dir="$(resolve_direct_child "$expected_parent" "$backup_name" "$dir" || true)"
  if [ -z "$validated_dir" ]; then
    add_result "fail" "Unsicheres Teardown-Ziel abgelehnt / Unsafe teardown target rejected: $label"
    set_warning_exit
    return 1
  fi
  dir="$validated_dir"

  if ! create_backup "$label" "$dir" "$backup_name"; then
    return 1
  fi

  if ! check_safety "$label" "$dir"; then
    return 1
  fi

  validated_dir="$(resolve_direct_child "$expected_parent" "$backup_name" "$dir" || true)"
  if [ -z "$validated_dir" ]; then
    add_result "fail" "Unsicheres Teardown-Ziel abgelehnt / Unsafe teardown target rejected: $label"
    set_warning_exit
    return 1
  fi
  dir="$validated_dir"

  if ! delete_remote_repo "$label" "$dir"; then
    return 1
  fi

  validated_dir="$(resolve_direct_child "$expected_parent" "$backup_name" "$dir" || true)"
  if [ -z "$validated_dir" ]; then
    add_result "fail" "Unsicheres Teardown-Ziel abgelehnt / Unsafe teardown target rejected: $label"
    set_warning_exit
    return 1
  fi
  dir="$validated_dir"

  delete_local_directory "$label" "$dir" || return 1

  if [ "$include_artifacts" -eq 1 ]; then
    cleanup_workspace_artifacts
  fi
}

print_level2_abort() {
  local lines=()
  local project=""

  lines+=("Level-2-Repositories erkannt / Level-2 repositories detected:")
  for project in "${LEVEL2_PROJECTS[@]}"; do
    lines+=("  - $(basename "$project")")
  done
  lines+=("")
  lines+=("--recursive erforderlich / --recursive required")

  print_box "Teardown abgebrochen / Teardown aborted" "${lines[@]}"
}

print_completion_report() {
  local lines=()
  local entry=""
  local status=""
  local message=""
  local symbol=""

  for entry in "${RESULTS[@]}"; do
    status="${entry%%|*}"
    message="${entry#*|}"
    case "$status" in
      done)
        symbol="✓"
        ;;
      skip)
        symbol="→"
        ;;
      fail)
        symbol="✗"
        ;;
      *)
        symbol="•"
        ;;
    esac
    lines+=("  $symbol $message")
  done

  print_box "Teardown abgeschlossen / Teardown complete" "${lines[@]}"
}

main() {
  parse_args "$@"
  validate_context
  discover_level2_projects || exit 2

  if [ "${#LEVEL2_PROJECTS[@]}" -gt 0 ] && [ "$RECURSIVE" -ne 1 ]; then
    print_level2_abort
    exit 1
  fi

  prepare_remote_targets || exit 2

  build_preamble

  if [ "$DRY_RUN" -eq 1 ]; then
    exit 0
  fi

  confirm_or_abort

  if ! check_home_artifacts_clean; then
    print_completion_report
    exit "$EXIT_CODE"
  fi

  if ! preflight_all_safety; then
    print_completion_report
    exit "$EXIT_CODE"
  fi

  if [ "${#LEVEL2_PROJECTS[@]}" -gt 0 ]; then
    local project=""
    local project_name=""
    for project in "${LEVEL2_PROJECTS[@]}"; do
      project_name="$(basename "$project")"
      if ! teardown_target "Level-2 $project_name" "$project" "$project_name" 0; then
        print_completion_report
        exit "$EXIT_CODE"
      fi
    done
  fi

  if ! teardown_target "Workspace $WORKSPACE_NAME" "$WORKSPACE_DIR" "$WORKSPACE_NAME" 1; then
    print_completion_report
    exit "$EXIT_CODE"
  fi

  print_completion_report
  exit "$EXIT_CODE"
}

main "$@"
