- [ ] Look at the milestone of the version being released. Move all the open issues from it to the next milestone.
- [ ] Publish artifacts to Maven via CI
  - [ ] Create branch `release-{release_version}` from `master`
  - [ ] On that branch
    - [ ] In `Build.scala`: Set `baseVersion` to `{release_version}`
    - [ ] In `Build.scala`: Set `previousDottyVersion` according to the instructions in the comment to that variable.
    - [ ] In `tasty/src/dotty/tools/tasty/TastyFormat.scala`: Set `ExperimentalVersion` to `0` to indicate a stable release; make sure `MajorVersion` and `MinorVersion` are set correctly for the release.
    - [ ] Tag the branch as `{release_version}`
  - [ ] On `master`:
    - [ ] In `Build.scala`: Set `baseVersion` to the next version to be released
    - [ ] In `Build.scala`: Set `previousDottyVersion` to `{release_version}`
    - [ ] In `project/MiMaFilters.scala`: Remove all `exclude` filters
- [ ] [Release ecosystem](https://www.notion.so/Scala-3-Ecosystem-Status-2460b396a89b478e8d4fa47ac27abbbd)
- [ ] Announce the release
  - [ ] Publish releases for the RC and stable versions on GitHub Releases
  - [ ] Publish Blog Post on dotty.epfl.ch
  - [ ] Make an announcement thread on https://contributors.scala-lang.org
  - [ ] Tweet the announcement blog post on https://twitter.com/scala_lang

[Instructions on how to release](https://dotty.epfl.ch/docs/contributing/procedures/release.html)
