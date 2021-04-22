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
    for entry in self.update_spec:
      if 'bump_patch' in entry:
        full_path = os.path.join(self.project_dir, entry['file'])
        with open(full_path, 'r') as f:
          src = f.read()
          pattern = Template(entry['bump_patch'])
          patchVersion = int(re.search(pattern.substitute(
            patch_version='(\\d+)'), src).group(1))

          entry['pattern'] = pattern.substitute(patch_version=patchVersion)
          entry['replacement'] = pattern.substitute(patch_version=patchVersion+1)
          del entry['bump_patch']

    super().update()
