#!/usr/bin/env bash

UPSTREAM_scastie="scalacenter/scastie"
UPSTREAM_BRANCH_scastie="master"

function update_scastie {
  replace "project/SbtShared.scala" \
    "val\s+latest3\s*=\s*\".*\"" \
    "val latest3   = \"$release_version\""
}
