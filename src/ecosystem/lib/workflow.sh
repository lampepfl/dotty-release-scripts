#!/usr/bin/env bash

# Target Framework
  # Some functions have form: purpose_target...
  function with_target {
    TARGET="$1"
  }

  function end_with_target {
    unset TARGET
  }

  function call {
    cd_target  # Always start from the target directory
    PURPOSE="$1"
    FUNCTION="${PURPOSE}_$TARGET"
    if $(notDefined $FUNCTION); then
      FUNCTION="${PURPOSE}_default"
    fi
    $FUNCTION ${@:2}
  }

  function call_verbose {
    echo "Calling $1 on $TARGET"
    call $@
  }

# Directory functions
  function cd_projects {
    cd $PROJECTS_DIR
  }

  function cd_target {
    cd "$PROJECTS_DIR/$TARGET"
  }

  function mk_projects {
    mkdir $PROJECTS_DIR
  }

  function rm_projects {
    rm -rf $PROJECTS_DIR
  }

function exit_on_failure {
  if ! $1 ${@:2}; then
    echo "Fatal failure: $@"
    exit 1
  fi
}
