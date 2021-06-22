import sys, re

pipeline = [
  # Clean-up
  ['Remove assignees', '^@[\\w-]+$', ''],
  ['Remove checklist status tracker (2 of 2)', '^\\d+ of \\d+$', ''],
  ['Remove status starting with •', '^•.*', ''],
  ['Remove comment counts & milestones', '^\\s+[0-9\\-\\.RC]+$', ''],
  ['Remove tags', '  .*$', ''],

  # Add links to PRs and issues
  ['Process PR numbers', '^#(\\d+) by .*', '[#\\1](https://github.com/lampepfl/dotty/pull/\\1)'],
  ['Process issue numbers', '[fF]ix #(\\d+)', 'Fix [#\\1](https://github.com/lampepfl/dotty/issues/\\1)'],
  ['Make each issue on one line', '\\s*\\n+^\\[#', ' [#'],

  # Finalization
  ['Remove multiple newlines', '\\n+', '\\n'],
  ['Make it a markdown list', '^(.)', '- \\1']
]

def refine():
  print('Copy-paste PRs from GitHub below. Type Enter 3 times to finish.')
  nl_count = 0
  raw_prs = ''
  while (nl_count < 3):
    line = sys.stdin.readline()
    if line == '\n':
      nl_count += 1
    else:
      nl_count = 0
    raw_prs += '\n' + line

  result = raw_prs
  for task_name, pattern, replacement in pipeline:
    print('Executing: {0}'.format(task_name))
    result = re.sub(pattern, replacement, result, flags=re.MULTILINE)

  print('\n\n=========== RESULT ===============\n\n{0}'.format(result))
