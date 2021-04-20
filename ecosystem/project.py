import tempfile, shutil, subprocess, os, re

class Project:
  def __init__(self, upstream, test_spec, update_spec):
    self.upstream = upstream
    self.test_spec = test_spec
    self.update_spec = update_spec

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
    if isinstance(self.update_spec, list):
      for where, what, with_what in self.update_spec:
        full_path = os.path.join(self.project_dir, where)
        src = ''
        with open(full_path, 'r') as f:
          src = f.read()
        res = re.sub(what, with_what, src, flags=re.MULTILINE)
        with open(full_path, 'w') as f:
          f.write(res)
    else:
      self.update_spec(self)

  def test(self):
    if isinstance(self.test_spec, list):
      subprocess.run(self.test_spec, cwd=self.project_dir)
    elif isinstance(self.test_spec, str):
      subprocess.run(self.test_spec.split(), cwd=self.project_dir)
    else:
      self.test_spec(self)
