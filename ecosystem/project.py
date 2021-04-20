import tempfile, shutil, subprocess, os

class Project:
  def __init__(self, upstream, test_spec):
    self.upstream = upstream
    self.test_spec = test_spec

  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, 'cloned_project')
    subprocess.run(
      ['git', 'clone', self.upstream, 'cloned_project'],
      cwd=self.root_dir)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    shutil.rmtree(self.root_dir)

  def test(self):
    if isinstance(self.test_spec, str):
      subprocess.run(self.test_spec.split(), check=True, cwd=self.project_dir)
    else:
      self.test_spec(self)
