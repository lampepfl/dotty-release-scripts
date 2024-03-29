import tempfile, shutil, subprocess, os, re, json, textwrap, importlib
from string import Template
import inquirer
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
      class_name_tokens = self.project_class.split('.')
      module_name = '.'.join(class_name_tokens[:-1])
      class_name = class_name_tokens[-1]
      self.__class__ = getattr(importlib.import_module(module_name), class_name)

  def __enter__(self):
    self.root_dir = tempfile.mkdtemp()
    self.project_dir = os.path.join(self.root_dir, self.name)

    subprocess.run(self.template('''
      git clone {upstream} {name}
      cd {name}
      git checkout {upstream_branch}
    '''), cwd=self.root_dir, shell=True)

    subprocess.run(self.template('''
      git remote add staging {staging}
      git fetch --all --prune
    '''), cwd=self.project_dir, shell=True)
    return self

  def __exit__(self, exc_type, exc_val, exc_tb):
    shutil.rmtree(self.root_dir)

  def template(self, cmd):
    return textwrap.dedent(cmd.format(**self.__dict__))

  def submit_pr(self, staging_branch, commit_message):
    command = textwrap.dedent('''
      git checkout -b {staging_branch}
      git commit -am "{commit_message}"
      git push -u staging
      open "{upstream}/compare/{upstream_branch}...dotty-staging:{staging_branch}"
    ''').format(
      staging_branch = staging_branch,
      commit_message = commit_message,
      upstream = self.upstream,
      upstream_branch = self.upstream_branch
    )
    subprocess.run(command, cwd=self.project_dir, shell=True)


  ### User-facing Menu Methods ###
  def project_menu(self):
    return {
      'Update': lambda: self.update(),
      'Test': lambda: self.test(),
      'Git Status': lambda: self.show_diff(),
      'Publish': lambda: self.publish(),
      'Submit custom PR': lambda: self.prepare_custom_pr(),
      'Open in Sublime': lambda: self.open_sublime_at_root(),
      'Go to Upstream': lambda: self.open_upstream(),
      'Go to Staging': lambda: self.open_staging(),
      'Delete Staging Branch': lambda: self.delete_staging_branch(),
      'Debug Project': lambda: self.debug(),
    }

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
    self.submit_pr(self.staging_branch, "Upgrade Dotty to " + self.release_version)

  def prepare_custom_pr(self):
    answers = inquirer.prompt([
      inquirer.Text('commit_message', message="Commit message"),
      inquirer.Text('branch_name', message="Staging branch name"),
    ])
    self.submit_pr(answers['branch_name'], answers['commit_message'])

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
