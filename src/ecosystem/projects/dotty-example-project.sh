#!/usr/bin/env bash

function update_dotty-example-project {
  local what="scalaVersion\s*:=\s*\".*\""
  local with_what="scalaVersion := \"$release_version\""

  replace "README.md" "$what" "$with_what"
  replace "build.sbt" "$what" "$with_what"
}

function test_dotty-example-project {
  sbt run
}
