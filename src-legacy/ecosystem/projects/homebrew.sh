#!/usr/bin/env bash

UPSTREAM_homebrew="lampepfl/homebrew-brew"
UPSTREAM_BRANCH_homebrew="master"
COMMIT_DIRECTLY_homebrew="true"

function update_homebrew {
  local hash=$(curl -L -s https://github.com/lampepfl/dotty/releases/download/$release_version/sha256sum.txt | grep ".tar.gz" | awk '{ print $1 }')

  replace "dotty.rb" \
    "url\s+\"https:\/\/github\.com\/lampepfl\/dotty\/releases\/download\/$RC_PATTERN\/scala3-$RC_PATTERN\.tar\.gz\"" \
    "url \"https:\/\/github.com\/lampepfl\/dotty\/releases\/download\/$release_version\/scala3-$release_version.tar.gz\""

  replace "dotty.rb" \
    "sha256 \"[0-9a-z]+\"" \
    "sha256 \"$hash\""
}
