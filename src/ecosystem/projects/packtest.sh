#!/usr/bin/env bash

function update_packtest {
  replace "artifacts" \
    "zip=https:\/\/github.com\/lampepfl\/dotty\/releases\/download\/$RC_PATTERN\/dotty-$RC_PATTERN.zip" \
    "zip=https:\/\/github.com\/lampepfl\/dotty\/releases\/download\/$release_version\/dotty-$release_version.zip"

  replace "artifacts" \
    "tar=https:\/\/github.com\/lampepfl\/dotty\/releases\/download\/$RC_PATTERN\/dotty-$RC_PATTERN.tar.gz" \
    "tar=https:\/\/github.com\/lampepfl\/dotty\/releases\/download\/$release_version\/dotty-$release_version.tar.gz"
}
