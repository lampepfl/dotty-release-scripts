#!/usr/bin/env bash

# Variables

#package object impl:
  #class DottyExample extends Project:

  #class DottyExampleMill extends Project:

  #class DottyG8 extends Project:

  #class DottyG8Cross extends Project:

  #trait Homebrew extends Project:

  #class Packtest extends Project with Homebrew:  // RC_PATTERN comes from Homebrew

  #class Scastie extends Project:

  #class Scalac extends Project:
    function deploy_scalac {
      git clone https://github.com/scala/scala.git
      cd scala
      git remote add staging https://github.com/dotty-staging/scala
      git checkout -b "dotty-release-$rc_version"
    }

    function update_scalac {
      replace "project/DottySupport.scala" \
        "val\s+dottyVersion\s*=\s*\".*\"" \
        "val dottyVersion = \"$rc_version\""
    }

    function publish_scalac {
      git commit -am "Upgrade Dotty to $rc_version"
      push -u staging
    }

#object Main:
  PROJECTS='
  dotty-example-project
  dotty-example-project-mill
  dotty.g8
  dotty-cross.g8
  homebrew-brew
  packtest
  scastie
  scalac'

https://github.com/lampepfl/dotty-staging.g8
https://github.com/lampepfl/xml-interpolator
Dotty

  function main {
    export -f process
    for p_raw in $PROJECTS; do
      p=$(echo $p_raw | xargs)
      process $p
    done
  }

main
