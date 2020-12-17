#!/usr/bin/env bash

function deploy_dotty-example-project-mill {
  git clone https://github.com/lampepfl/dotty-example-project "$TARGET"
  cd_target
  git checkout mill
}

function update_dotty-example-project-mill {
  local what="def\s+scalaVersion\s*=\s*\".*\""
  local with_what="def scalaVersion = \"$release_version\""

  replace "build.sc" "$what" "$with_what"
  replace "README.md" "$what" "$with_what"
}

function test_dotty-example-project-mill {
  ./mill root.run
}
