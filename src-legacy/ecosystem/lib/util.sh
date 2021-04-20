#!/usr/bin/env bash

# Function existence status
  function isDefined { type $1 &> /dev/null; }
  function notDefined { ! isDefined $1; }

# Repository operations
  function replace {
    local where="$1"
    local what="$2"
    local with_what="$3"
    gsed -i -E "s/$what/$with_what/g" "$where"
  }

  function push {
    git push $@
  }
