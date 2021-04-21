import yaml
from release.util import choice_loop
from release.ecosystem.project import Project

def ecosystem_projects(release_version):
  with open('data/projects.yaml', 'r') as f:
    raw_yaml = f.read().format(release_version = release_version)
    projects = yaml.safe_load(raw_yaml)

  return { name: Project(name, spec) for name, spec in projects.items() }

def project_menu(project):
  with project as p:
    choice_loop({
      'Update': lambda: p.update(),
      'Test': lambda: p.test(),
      'Git Status': lambda: p.show_diff(),
      'Publish': lambda: p.publish(release_version),
      'Show Root Directory': lambda: p.print_root_dir(),
      'Open in Sublime': lambda: p.open_sublime_at_root(),
      'Debug Project': lambda: p.debug(),
    },
    'What should we do?',
    lambda task: task())

def select_project(release_version):
  choice_loop(ecosystem_projects(release_version), 'Select a project', project_menu)
