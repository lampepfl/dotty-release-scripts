import requests
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
