#!/usr/bin/env bash

function deploy_dotty-cross.g8 {
  git clone https://github.com/lampepfl/dotty-cross.g8.git
}

function update_dotty-cross.g8 {
  local what="val\s+dottyVersion\s*=\s*\".*\""
  local with_what="val dottyVersion = \"$rc_version\""

  replace "dotty-cross.g8/src/main/g8/build.sbt" "$what" "$with_what"
}

function test_dotty-cross.g8 {
  sbt new file://./dotty-cross.g8 --name=foo --description=bar && cd foo && sbt run
}

function publish_dotty-cross.g8 {
  cd_target
  publish_default
}
