#!/usr/bin/env bash

function update_xml-interpolator {
  local what="val\s+dottyVersion\s*=\s*\".*\""
  local with_what="val dottyVersion = \"$rc_version\""

  replace "build.sbt" "$what" "$with_what"
}

function test_xml-interpolator {
  sbt test
}
