import tempfile, shutil, subprocess, os, re, json, textwrap

class Project:
  def __init__(self, name, d):
    self.name = name
    self.__dict__.update(d)

  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, self.name)
    subprocess.run(
      ['git', 'clone', self.upstream, self.name],
      cwd=self.root_dir)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    shutil.rmtree(self.root_dir)

  def print_root_dir(self):
    print(self.root_dir)

  def open_sublime_at_root(self):
    subprocess.run(['subl', self.root_dir])

  def debug(self):
    print(json.dumps(self.__dict__, indent=2, sort_keys=True))

  def update(self):
    for spec in self.update_spec:
      full_path = os.path.join(self.project_dir, spec['file'])
      with open(full_path, 'r') as f:
        src = f.read()
      res = re.sub(spec['pattern'], spec['replacement'], src, flags=re.MULTILINE)
      with open(full_path, 'w') as f:
        f.write(res)

  def test(self):
    if self.test_spec.get('run_from_root'):
      target_dir = self.root_dir
    else:
      target_dir = self.project_dir
    subprocess.run(self.test_spec['command'], cwd=target_dir, shell=True)

  def show_diff(self):
    subprocess.run(['git', 'diff'], cwd=self.project_dir)

  def publish(self, release_version):
    if self.commit_directly:
      command = textwrap.dedent('''
        git commit -am {release_version}
        git push
      '''.format(release_version = release_version))
      subprocess.run(command, cwd=self.project_dir, shell=True)
