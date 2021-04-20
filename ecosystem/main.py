#!/usr/bin/env python3
import inquirer, os
from project import Project

release_version = input('Which version are we releasing? > ')

Scala3ExampleProject = Project(
  upstream = 'https://github.com/scala/scala3-example-project',
  test_spec = 'sbt run',
  update_spec = [
    ['README.md', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
    ['build.sbt', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
  ]
)

with Scala3ExampleProject as dummy:
  while(True):
    choices = {
      'Update': lambda: dummy.update(),
      'Test': lambda: dummy.test(),
      'Show Root Directory': lambda: dummy.print_root_dir(),
      'Open in Sublime': lambda: dummy.open_sublime_at_root(),
      'Exit': ''
    }

    option = inquirer.prompt([inquirer.List(
      'target',
      message='What do we do?',
      choices=choices.keys()
    )])['target']
    if option is 'Exit':
      break
    else:
      choices[option]()
