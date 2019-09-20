#!/usr/bin/env bash

function process {
  cd_projects
  rm -rf *
  with_target $1
    call_verbose deploy
    call_verbose update
    exit_on_failure call_verbose test
    call_verbose publish
  end_with_target
}

function deploy_default {
  git clone https://github.com/lampepfl/$TARGET.git
  cd_target
}

function test_default {
  echo "No test available for $TARGET"
}

function update_default {
  echo "Not implemented error: update"
  exit 1
}

function publish_default {
  git commit -am "Upgrade Dotty to $rc_version"
  push
}
