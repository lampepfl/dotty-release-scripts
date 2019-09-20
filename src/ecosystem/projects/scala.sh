#!/usr/bin/env bash

UPSTREAM_scala="scala/scala"
UPSTREAM_BRANCH_scala="2.13.x"

function update_scala {
  replace "project/DottySupport.scala" \
    "val\s+dottyVersion\s*=\s*\".*\"" \
    "val dottyVersion = \"$rc_version\""
}
