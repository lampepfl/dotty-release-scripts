- [ ] Finalize release
  - [ ] Look at the milestone of the version being released. Move all the open issues from it to the next milestone.
  - [ ] Merge branch of the previous release into `master` to guarantee that all of the commits are propagated to `master`
- [ ] Publish artifacts to Maven via CI
  - [ ] Create branch `{release_version}` from `master`
  - [ ] On that branch, set `baseVersion` and tag it as `{release_version}`
  - [ ] On `master`, set `baseVersion` to the next version to be released
- [ ] [Release ecosystem](https://www.notion.so/Scala-3-Ecosystem-Status-2460b396a89b478e8d4fa47ac27abbbd)
- [ ] Announce the release
  - [ ] Publish releases for the RC and stable versions on GitHub Releases
  - [ ] Publish Blog Post on dotty.epfl.ch
  - [ ] Make an announcement thread on https://contributors.scala-lang.org
  - [ ] Tweet the announcement blog post on https://twitter.com/scala_lang

[Instructions on how to release](https://dotty.epfl.ch/docs/contributing/procedures/release.html)
