#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo "FYI args are: $@"

function init-vars {
  foo="bar"
}

echo "DIR IS $DIR"