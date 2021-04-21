import tempfile, shutil, subprocess, os, re

class Project:
  def __init__(self, d):
    self.__dict__.update(d)

  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, 'cloned_project')
    subprocess.run(
      ['git', 'clone', self.upstream, 'cloned_project'],
      cwd=self.root_dir)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    shutil.rmtree(self.root_dir)

  def print_root_dir(self):
    print(self.root_dir)

  def open_sublime_at_root(self):
    subprocess.run(['subl', self.root_dir])

  def update(self):
    for spec in self.update_spec:
      print(spec)

      full_path = os.path.join(self.project_dir, spec['file'])
      with open(full_path, 'r') as f:
        src = f.read()
      res = re.sub(spec['pattern'], spec['replacement'], src, flags=re.MULTILINE)
      with open(full_path, 'w') as f:
        f.write(res)

  def test(self):
    subprocess.run(self.test_spec.split(), cwd=self.project_dir)

  def show_diff(self):
    subprocess.run(['git', 'diff'], cwd=self.project_dir)

  def publish(self, release_version):
    if self.commit_directly:
      subprocess.run(['git', 'commit', '-am', 'Upgrade Dotty to {0}'.format(release_version)], cwd=self.project_dir)
      subprocess.run(['git', 'push'], cwd=self.project_dir)
