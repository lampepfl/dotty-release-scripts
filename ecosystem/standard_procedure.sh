#!/usr/bin/env bash
load util
load workflow

function process {
  with_target $1
    call deploy
    call update
    exit_on_failure call test
    call publish
    call cleanup
  end_with_target
}

function deploy_default {
  git clone https://github.com/lampepfl/$TARGET.git
  cd $TARGET
}

function cleanup_default {
  cd ..
  rm -rf $TARGET
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
