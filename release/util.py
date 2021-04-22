import inquirer, yaml, importlib, re

def choice_loop(choices, prompt, task):
  choices_refined = choices.copy()
  choices_refined['Exit'] = ''
  while(True):
    option = inquirer.prompt([inquirer.List(
      'target',
      message=prompt,
      choices=choices_refined.keys()
    )])['target']

    if option is 'Exit':
      break
    else:
      task(choices_refined[option])

def load_data(name, release_version):
  with open('data/_variables.yaml', 'r') as f:
    template_variables = yaml.safe_load(f)
  with open('data/{0}'.format(name), 'r') as f:
    contents = f.read()
  return contents.format(release_version=release_version, **template_variables)

def import_class(module, cls):
  mymodule = importlib.import_module(module)
  return getattr(mymodule, cls)
