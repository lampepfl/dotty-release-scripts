#!/usr/bin/env bash

function deploy_scala3-example-project-mill {
  git clone https://github.com/scala/scala3-example-project "$TARGET"
  cd_target
  git checkout mill
}

function update_scala3-example-project-mill {
  local what="def\s+scalaVersion\s*=\s*\".*\""
  local with_what="def scalaVersion = \"$release_version\""

  replace "build.sc" "$what" "$with_what"
  replace "README.md" "$what" "$with_what"
}

function test_scala3-example-project-mill {
  ./mill root.run
}
