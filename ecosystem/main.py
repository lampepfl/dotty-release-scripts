#!/usr/bin/env python3
import inquirer, os
from project import Project

release_version = input('Which version are we releasing? > ')

def choice_loop(choices, prompt, task):
  choices_refined = choices.copy()
  choices_refined['Exit'] = ''
  while(True):
    option = inquirer.prompt([inquirer.List(
      'target',
      message=prompt,
      choices=choices_refined.keys()
    )])['target']

    if option is 'Exit':
      break
    else:
      task(choices_refined[option])

def select_project_menu():
  choice_loop({
    'scala3-example-project': Project(
      upstream = 'https://github.com/scala/scala3-example-project',
      test_spec = 'sbt run',
      update_spec = [
        ['README.md', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
        ['build.sbt', 'scalaVersion\\s*:=\\s*".*"', 'scalaVersion := "{release_version}"'.format(release_version = release_version)],
      ],
      commit_directly = True
    ),
  },
  'Please select a project to work on:',
  project_menu)

def project_menu(project):
  with project as p:
    choice_loop({
      'Update': lambda: p.update(),
      'Test': lambda: p.test(),
      'Git Status': lambda: p.show_diff(),
      'Publish': lambda: p.publish(release_version),
      'Show Root Directory': lambda: p.print_root_dir(),
      'Open in Sublime': lambda: p.open_sublime_at_root(),
    },
    'What should we do?',
    lambda task: task())

select_project_menu()
