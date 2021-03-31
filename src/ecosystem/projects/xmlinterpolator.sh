#!/usr/bin/env bash

UPSTREAM_xmlinterpolator="lampepfl/xml-interpolator"
UPSTREAM_BRANCH_xmlinterpolator="master"

function update_xmlinterpolator {
  local what="val\s+dottyVersion\s*=\s*\".*\""
  local with_what="val dottyVersion = \"$release_version\""

  replace "build.sbt" "$what" "$with_what"
}

function test_xmlinterpolator {
  sbt test
}
