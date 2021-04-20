#!/usr/bin/env bash

function process {
  cd_projects
  rm -rf *
  with_target $1
    call_verbose init_vars
    call_verbose deploy
    call_verbose update
    exit_on_failure call_verbose test
    call_verbose publish
  end_with_target
}

function init_vars_default {
  UPSTREAM_NAME="UPSTREAM_$TARGET"
  UPSTREAM_BRANCH_NAME="UPSTREAM_BRANCH_$TARGET"
  COMMIT_DIRECTLY_NAME="COMMIT_DIRECTLY_$TARGET"
  # https://stackoverflow.com/a/1921337
  UPSTREAM=${!UPSTREAM_NAME}
  UPSTREAM_BRANCH=${!UPSTREAM_BRANCH_NAME}
  COMMIT_DIRECTLY=${!COMMIT_DIRECTLY_NAME}
}

function deploy_default {
  if [ ! -z $UPSTREAM ]; then
    TARGET_URL="https://github.com/$UPSTREAM.git"
  else
    TARGET_URL="https://github.com/scala/$TARGET.git"
  fi
  git clone "$TARGET_URL" "$TARGET"
}

function test_default {
  echo "No test available for $TARGET"
}

function update_default {
  echo "Not implemented error: update"
  exit 1
}

function publish_default {
  if [ ! -z $UPSTREAM ] && [ ! -z $UPSTREAM_BRANCH ] && [ -z $COMMIT_DIRECTLY ]; then
    ORIGIN_BRANCH="dotty-release-$release_version"
    git remote add staging https://github.com/dotty-staging/$TARGET.git
    git checkout -b $ORIGIN_BRANCH
    git commit -am "Upgrade Dotty to $release_version"
    push -u staging
    open "https://github.com/$UPSTREAM/compare/$UPSTREAM_BRANCH...dotty-staging:$ORIGIN_BRANCH"
  else
    git commit -am "Upgrade Dotty to $release_version"
    push
  fi
}