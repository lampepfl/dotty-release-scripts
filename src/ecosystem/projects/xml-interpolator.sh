#!/usr/bin/env bash

UPSTREAM_xml-interpolator="lampepfl/xml-interpolator"
UPSTREAM_BRANCH_xml-interpolator="master"

function update_xml-interpolator {
  local what="val\s+dottyVersion\s*=\s*\".*\""
  local with_what="val dottyVersion = \"$release_version\""

  replace "build.sbt" "$what" "$with_what"
}

function test_xml-interpolator {
  sbt test
}
