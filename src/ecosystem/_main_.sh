#!/usr/bin/env bash

# Import Mechanism
  # https://stackoverflow.com/a/246128
  ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/src/ecosystem"
  PROJECTS_DIR="$(pwd)/ecosystem_projects"
  PROJECT_SCRIPTS_DIR="$ROOT_DIR/projects"
  function load {
    . $ROOT_DIR/"$1.sh"
  }

# Imports
  load constants
  load standard_procedure
  load lib/util
  load lib/workflow

# Version-related variables
  stable=$1
  live=$3  # Push changes to github if it is defined

  stable_patch=0
  rc_patch=0
  next_patch=0

  rc="$(($stable+1))"
  next="$(($rc+1))"

  stable_version="0.$stable.$stable_patch"
  rc_version_preview="0.$rc.$rc_patch"
  rc_version="$rc_version_preview-RC1"
  next_version="0.$next.$next_patch"
  stable_branch="0.$stable.x"
  rc_branch="0.$rc.x"

  TARGET_PROJECT="$2.sh"

# Guards
  if [ -z "$(which gsed)" ]
  then
    echo "Please install gsed to use this script – see e.g. https://stackoverflow.com/q/30003570"
    exit 1
  fi

# Main logic
  function handle_project {
    project=$1
    project_file="$PROJECT_SCRIPTS_DIR/$1.sh"
    . $project_file
    process $project
  }

  function main {
    mk_projects
    for project_path in "$PROJECT_SCRIPTS_DIR/$TARGET_PROJECT"; do
      project_filename=$(basename $project_path)
      project=${project_filename%.sh}  # Remove extension
      handle_project $project
    done
    rm_projects
  }

main
