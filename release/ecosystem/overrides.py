import requests, os, re, textwrap, subprocess
from release.ecosystem.project import Project
from string import Template
import inquirer

class Homebrew(Project):
  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, self.name)

    subprocess.run(self.template('''
      git clone {upstream} {name}
      cd {name}
      git checkout {upstream_branch}
    '''), cwd=self.root_dir, shell=True)

    return self

  def update(self):
    link = self.template('https://github.com/lampepfl/dotty/releases/download/{release_version}/sha256sum.txt')
    with requests.get(link) as f:
      for line in f.text.split('\n'):
        if line.endswith('.tar.gz'):
          release_hash = line.split()[0]

    def inject_hash(entry):
      new_entry = entry.copy()
      new_entry['replacement'] = Template(entry['replacement']).substitute(
        release_hash=release_hash)
      return new_entry

    self.update_spec = [ inject_hash(entry) for entry in self.update_spec ]
    super().update()

  def publish(self):
    command = self.template('''
      git commit -am "Upgrade Dotty to {release_version}"
      git push
    ''')
    subprocess.run(command, cwd=self.project_dir, shell=True)

class Ammonite(Project):
  def update(self):
    if hasattr(self, 'latest_comlihaoyi_version'):
      all_buildfiles = [ os.path.relpath(os.path.join(root, 'build.sc'), self.project_dir)
        for root, _, files in os.walk(self.project_dir) if 'build.sc' in files ]

      for dep_entry in self.latest_comlihaoyi_version:
        if isinstance(dep_entry, dict):
          dep = dep_entry['artefact']
          dep_project = dep_entry['project']
        else:
          dep = dep_project = dep_entry

        dep_template = Template('com.lihaoyi::{dep}::$version'.format(dep=dep))
        latest_version = requests.get(
          'https://github.com/com-lihaoyi/{dep_project}/releases/latest'.format(dep_project=dep_project)
        ).url.split('/')[-1]

        for buildfile in all_buildfiles:
          self.update_spec.append({
            'file': buildfile,
            'pattern': dep_template.substitute(version='[\\d\\.]+'),
            'replacement': dep_template.substitute(version=latest_version)
          })
    super().update()

  def release_to_maven(self):
    latest_release = requests.get(
      'https://github.com/com-lihaoyi/{name}/releases/latest'.format(name=self.name)
    ).url.split('/')[-1]

    major, minor, patch = latest_release.split('.')
    this_release = '.'.join([major, minor, str(int(patch)+1)])

    user_specified_next_version = inquirer.prompt([
      inquirer.Text('version', message='Version to release? [{0}]'.format(this_release)),
    ])['version']
    if user_specified_next_version != '':
      this_release = user_specified_next_version

    subprocess.run(textwrap.dedent('''
      git tag {this_release}
      git push --tag origin {this_release}
    '''.format(this_release=this_release)), cwd=self.project_dir, shell=True)

  def project_menu(self):
    menu = super().project_menu()
    menu.update({'Release to Maven': lambda: self.release_to_maven()})
    return menu