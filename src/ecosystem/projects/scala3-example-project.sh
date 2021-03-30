#!/usr/bin/env bash

function update_scala3-example-project {
  local what="rcVersion\s*=\s*\".*\""
  local with_what="rcVersion = \"$release_version\""

  echo "MARKER $release_version"
  replace "README.md" "$what" "$with_what"
  replace "build.sbt" "$what" "$with_what"
}

function test_scala3-example-project {
  sbt run
}
