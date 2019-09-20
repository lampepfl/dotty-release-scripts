#!/usr/bin/env bash

function update_dotty-staging.g8 {
  local what="val\s+dottyVersion\s*=\s*\".*\""
  local with_what="val dottyVersion = \"$rc_version\""

  replace "src/main/g8/build.sbt" "$what" "$with_what"
}

function test_dotty-staging.g8 {
  cd_projects
  sbt new file://./dotty-staging.g8 --name=foo --description=bar && cd foo && sbt run
}
