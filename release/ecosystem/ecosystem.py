from release.util import choice_loop
from ecosystem_projects import ecosystem_projects

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

def select_project(release_version):
  choice_loop(ecosystem_projects(release_version), 'Select a project', project_menu)
