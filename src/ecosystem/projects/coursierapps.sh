#!/usr/bin/env bash

UPSTREAM_coursierapps="coursier/apps"
UPSTREAM_BRANCH_coursierapps="master"

function update_coursierapps {
  replace "apps/resources/dotty-repl.json" \
    "ch.epfl.lamp:dotty-compiler_[0-9\.]+:latest.stable" \
    "org.scala-lang:scala3-compiler_$release_version:latest.stable"
  replace "apps/resources/dotty-repl.json" \
    "org.scala-lang:scala3-compiler_[0-9\.-M]+:latest.stable" \
    "org.scala-lang:scala3-compiler_$release_version:latest.stable"
}
