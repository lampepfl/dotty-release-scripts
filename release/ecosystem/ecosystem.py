import yaml, os
from release.util import choice_loop, load_data
from release.ecosystem.project import Project

def select_ecosystem(release_version):
  options = { file: file for file in os.listdir('data/projects') }
  choice_loop(options, 'Select ecosystem',
    lambda file: select_project(os.path.join('projects', file), release_version))

def select_project(file, release_version):
  projects = yaml.safe_load(load_data(file, release_version))
  options = { name: Project(name, release_version, spec) for name, spec in projects.items() }
  choice_loop(options, 'Select a project', project_menu)

def project_menu(project):
  with project as p:
    choice_loop(p.project_menu(), 'What should we do?', lambda task: task())
