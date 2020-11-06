#!/usr/bin/env bash

UPSTREAM_scastie="scalacenter/scastie"
UPSTREAM_BRANCH_scastie="master"

function update_scastie {
  replace "project/SbtShared.scala" \
    "val\s+latestDotty\s*=\s*\".*\"" \
    "val latestDotty = \"$release_version\""
}
