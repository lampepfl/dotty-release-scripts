import requests, os, re
from release.ecosystem.project import Project
from string import Template

class Homebrew(Project):
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

class Ammonite(Project):
  def update(self):
    if hasattr(self, 'latest_comlihaoyi_version'):
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

        self.update_spec.append({
          'file': 'build.sc',
          'pattern': dep_template.substitute(version='[\\d\\.]+'),
          'replacement': dep_template.substitute(version=latest_version)
        })
    super().update()
