import yaml
from release.util import choice_loop, load_data
from release.ecosystem.project import Project

def ecosystem_projects(release_version):
  projects = yaml.safe_load(load_data('projects.yaml', release_version))
  return { name: Project(name, release_version, spec) for name, spec in projects.items() }

def project_menu(project):
  with project as p:
    choice_loop({
      'Update': lambda: p.update(),
      'Test': lambda: p.test(),
      'Git Status': lambda: p.show_diff(),
      'Publish': lambda: p.publish(),
      'Show Root Directory': lambda: p.print_root_dir(),
      'Open in Sublime': lambda: p.open_sublime_at_root(),
      'Go to Upstream': lambda: p.open_upstream(),
      'Go to Staging': lambda: p.open_staging(),
      'Delete Staging Branch': lambda: p.delete_staging_branch(),
      'Debug Project': lambda: p.debug(),
    },
    'What should we do?',
    lambda task: task())

def select_project(release_version):
  choice_loop(ecosystem_projects(release_version), 'Select a project', project_menu)
