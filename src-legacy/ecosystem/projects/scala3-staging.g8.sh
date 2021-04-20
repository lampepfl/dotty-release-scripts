#!/usr/bin/env bash

function update_scala3-staging.g8 {
  local what="val\s+scala3Version\s*=\s*\".*\""
  local with_what="val scala3Version = \"$release_version\""

  replace "src/main/g8/build.sbt" "$what" "$with_what"
}

function test_scala3-staging.g8 {
  cd_projects
  sbt new file://./scala3-staging.g8 --name=foo --description=bar && cd foo && sbt ";run; test"
}
