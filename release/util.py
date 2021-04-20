import inquirer

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
