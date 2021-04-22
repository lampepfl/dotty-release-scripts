import tempfile, shutil, subprocess, os, re, json, textwrap, importlib
from release import util

class Project:
  def __init__(self, name, release_version, d):
    self.name = name
    self.release_version = release_version
    self.__dict__.update(d)

    if not hasattr(self, 'commit_directly'):
      self.commit_directly = False
    if not hasattr(self, 'upstream_branch'):
      self.upstream_branch = 'master'
    if not hasattr(self, 'staging_branch'):
      self.staging_branch = self.template('scala3-release-{release_version}')

    if hasattr(self, 'project_class'):
      module = importlib.import_module(self.project_class['module'])
      self.__class__ = getattr(module, self.project_class['class'])

  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, self.name)

    subprocess.run(self.template('''
      git clone {upstream} {name}
      cd {name}
      git checkout {upstream_branch}
    '''), cwd=self.root_dir, shell=True)

    if not self.commit_directly:
      subprocess.run(self.template('''
        git remote add staging {staging}
      '''), cwd=self.project_dir, shell=True)

    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    shutil.rmtree(self.root_dir)

  def template(self, cmd):
    return textwrap.dedent(cmd.format(**self.__dict__))


  ### User-facing Menu Methods ###
  def open_sublime_at_root(self):
    subprocess.run(self.template('subl {root_dir}'), shell=True)

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

  def debug(self):
    print(json.dumps(self.__dict__, indent=2, sort_keys=True))

  def show_diff(self):
    subprocess.run('git diff', cwd=self.project_dir, shell=True)

  def publish(self):
    if self.commit_directly:
      command = self.command('''
        git commit -am {release_version}
        git push
      ''')
      subprocess.run(command, cwd=self.project_dir, shell=True)
    else:
      command = self.template('''
        git checkout -b {staging_branch}
        git commit -am "Upgrade Dotty to {release_version}"
        git push -u staging
        open "{upstream}/compare/{upstream_branch}...dotty-staging:{staging_branch}"
      ''')
      subprocess.run(command, cwd=self.project_dir, shell=True)

  def open_staging(self):
    subprocess.run(self.template('open {staging}'), shell=True)

  def open_upstream(self):
    subprocess.run(self.template('open {upstream}'), shell=True)

  def delete_staging_branch(self):
    subprocess.run(self.template('''
      git checkout {upstream_branch}
      git branch -D {staging_branch}
      git push {staging} --delete {staging_branch}
    '''), cwd=self.project_dir, shell=True)
