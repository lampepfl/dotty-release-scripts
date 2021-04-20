#!/usr/bin/env python3
import inquirer, os

# import pkgutil, importlib
# names = [name for _, name, _ in pkgutil.iter_modules(['projects'])]
# answers = inquirer.prompt([inquirer.List(
#     'target',
#     message='What project should we work on?',
#     choices = names
#   )
# ])
# mod = importlib.import_module('projects.{target}'.format(**answers))

from project import Project

Scala3ExampleProject = Project(
  upstream = 'https://github.com/scala/scala3-example-project',
  test_spec = 'sbt run'
)

choices = ['Test', 'Show Root Directory', 'Leave']
with Scala3ExampleProject as dummy:
  while(True):
    option = inquirer.prompt([inquirer.List(
      'target',
      message='What do we do?',
      choices=choices
    )])['target']
    opt_id = choices.index(option)

    if opt_id is 0:
      dummy.test()
    elif opt_id is 1:
      print(dummy.root_dir)
    elif opt_id is 2:
      break
