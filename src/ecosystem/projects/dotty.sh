#!/usr/bin/env bash

UPSTREAM_dotty="lampepfl/dotty"
UPSTREAM_BRANCH_dotty="master"

function update_dotty {
  local what="val\s+referenceVersion\s*=\s*\".*\""
  local with_what="val referenceVersion = \"$rc_version\""

  replace "project/Build.scala" "$what" "$with_what"
}
