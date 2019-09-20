#!/usr/bin/env bash

function deploy_scastie {
  git clone https://github.com/scalacenter/scastie.git
  cd scastie
  git remote add staging https://github.com/dotty-staging/scastie
  git checkout -b "dotty-release-$rc_version"
}

function update_scastie {
  replace "project/SbtShared.scala" \
    "val\s+latestDotty\s*=\s*\".*\"" \
    "val latestDotty = \"$rc_version\""
}

function publish_scastie {
  git commit -am "Upgrade Dotty to $rc_version"
  push -u staging
}
