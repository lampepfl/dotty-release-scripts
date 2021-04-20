#!/usr/bin/env bash

UPSTREAM_coursierapps="coursier/apps"
UPSTREAM_BRANCH_coursierapps="master"

function update_coursierapps {
  replace "apps/resources/dotty-repl.json" \
    "org.scala-lang:scala3-compiler_$RC_PATTERN\:latest.release" \
    "org.scala-lang:scala3-compiler_$release_version:latest.release"

  replace "apps/resources/scala3-compiler.json" \
    "org.scala-lang:scala3-compiler_$RC_PATTERN" \
    "org.scala-lang:scala3-compiler_$release_version"

  replace "apps/resources/scala3-decompiler.json" \
    "org.scala-lang:scala3-compiler_$RC_PATTERN" \
    "org.scala-lang:scala3-compiler_$release_version"

  replace "apps/resources/scala3-doc.json" \
    "org.scala-lang:scala3-doc_$RC_PATTERN" \
    "org.scala-lang:scala3-doc_$release_version"

  replace "apps/resources/scala3-repl.json" \
    "org.scala-lang:scala3-compiler_$RC_PATTERN" \
    "org.scala-lang:scala3-compiler_$release_version"
}
