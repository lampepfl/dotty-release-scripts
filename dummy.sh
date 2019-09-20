#!/usr/bin/env bash

ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

function load {
  . $ROOT_DIR/"$1.sh"
}

load ecosystem/constants
load dummy-lib

dostuff
