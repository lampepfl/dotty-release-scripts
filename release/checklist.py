def produce(release_version):
  result = '''
  - [ ] Finalize release
    - [ ] Look at the milestone of the version being released. Move all the open issues from it to the next milestone.
    - [ ] Merge branch of the previous release into `master` to guarantee that all of the commits are propagated to `master`
  - [ ] Publish artifacts to Maven via CI
    - [ ] Create branch `{release_version}` from `master`
    - [ ] On that branch, set `baseVersion` and tag it as `{release_version}`
    - [ ] On `master`, set `baseVersion` to the next version to be released
  - [ ] Update `scalaVersion` (and, if applicable, the `sbt-dotty` version) in the Dotty ecosystem projects
    - [ ] https://github.com/scala/scala3-example-project [![Build Status](https://travis-ci.org/scala/scala3-example-project.svg?branch=master)](https://travis-ci.org/scala/scala3-example-project)
    - [ ] https://github.com/scala/scala3-example-project/tree/mill
    - [ ] https://github.com/scala/scala3.g8 [![Build Status](https://travis-ci.org/scala/scala3.g8.svg?branch=master)](https://travis-ci.org/scala/scala3.g8/)
    - [ ] https://github.com/scala/scala3-cross.g8 [![Build Status](https://travis-ci.org/scala/scala3-cross.g8.svg?branch=master)](https://travis-ci.org/scala/scala3-cross.g8/)
    - [ ] https://github.com/lampepfl/scala3-staging.g8 [![Build Status](https://travis-ci.org/scala/scala3-staging.g8.svg?branch=master)](https://travis-ci.org/lampepfl/scala3-staging.g8)
    - [ ] https://github.com/scala/scala3-tasty-inspector.g8 [![Build Status](https://travis-ci.org/scala/scala3-tasty-inspector.g8.svg?branch=master)](https://travis-ci.org/scala/scala3-tasty-inspector.g8)
    - [ ] https://github.com/lampepfl/homebrew-brew [![Build Status](https://travis-ci.org/lampepfl/homebrew-brew.svg?branch=master)](https://travis-ci.org/lampepfl/homebrew-brew)
    - [ ] https://github.com/lampepfl/packtest [![Build Status](https://travis-ci.org/lampepfl/packtest.svg?branch=master)](https://travis-ci.org/lampepfl/packtest)
    - [ ] https://github.com/lampepfl/xml-interpolator [![Build Status](https://travis-ci.org/lampepfl/xml-interpolator.svg?branch=master)](https://travis-ci.org/lampepfl/xml-interpolator)
    - [ ] https://github.com/scalacenter/scastie
      - [ ] PR submitted
      - [ ] PR merged
      - [ ] https://scastie.scala-lang.org/ -> Build Settings -> Dotty mentions `{release_version}`
    - [ ] Dotty reference compiler [![Dotty CI](https://github.com/lampepfl/dotty/workflows/Dotty%20CI/badge.svg?branch=master)](https://github.com/lampepfl/dotty/actions?query=branch%3Amaster)
      - [ ] PR submitted
      - [ ] PR merged
    - [ ] Scalac [![Build Status](https://travis-ci.org/scala/scala.svg?branch=2.13.x)](https://travis-ci.org/scala/scala)
      - [ ] PR submitted
      - [ ] PR merged
    - [ ] Update the dotty-repl Coursier [app definition](https://github.com/coursier/apps/blob/master/apps/resources/dotty-repl.json)
  - [ ] Announce the release
    - [ ] Publish releases for the RC and stable versions on GitHub Releases
    - [ ] Publish Blog Post on dotty.epfl.ch
    - [ ] Make an announcement thread on https://contributors.scala-lang.org
    - [ ] Tweet the announcement blog post on https://twitter.com/scala_lang

  [Instructions on how to release](https://dotty.epfl.ch/docs/contributing/procedures/release.html)'''.format(
    release_version = release_version,
  )
  print(result)
