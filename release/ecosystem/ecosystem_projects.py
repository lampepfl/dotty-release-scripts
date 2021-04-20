from project import Project

def ecosystem_projects(release_version):
  return {
    'scala3-example-project': Project(
      upstream = 'https://github.com/scala/scala3-example-project',
      test_spec = 'sbt run',
      update_spec = [
        ['README.md', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
        ['build.sbt', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
      ],
      commit_directly = True
    ),
  }
