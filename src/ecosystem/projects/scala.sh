#!/usr/bin/env bash

function deploy_scala {
  git clone https://github.com/scala/scala.git
  cd scala
  git remote add staging https://github.com/dotty-staging/scala
  git checkout -b "dotty-release-$rc_version"
}

function update_scala {
  replace "project/DottySupport.scala" \
    "val\s+dottyVersion\s*=\s*\".*\"" \
    "val dottyVersion = \"$rc_version\""
}

function publish_scala {
  git commit -am "Upgrade Dotty to $rc_version"
  push -u staging
}
