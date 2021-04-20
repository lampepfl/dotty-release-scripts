import sys, re

pipeline = [
  ['Remove assignees', '^@[\\w-]+$', ''],
  ['Remove comment counts', '^\\s\\d+', ''],
  ['Remove tags', '  .*$', ''],
  ['Process PR numbers', '^#(\\d+) by .*', '[#\\1](https://github.com/lampepfl/dotty/pull/\\1)'],
  ['Process issue numbers', '[fF]ix #(\\d+)', 'Fix [#\\1](https://github.com/lampepfl/dotty/issues/\\1)'],
  ['Make each issue on one line', '\\s*\\n+^\\[#', ' [#'],
  ['Remove multiple newlines', '\\n+', '\\n'],
  ['Make it a markdown list', '^(.)', '- \\1']
]

def refine():
  print('Copy-paste PRs from GitHub below. Type Enter 3 times to finish.')
  nl_count = 0
  raw_prs = ''
  while (nl_count < 3):
    line = sys.stdin.readline()
    if line is '\n':
      nl_count += 1
    else:
      nl_count = 0
    raw_prs += '\n' + line

  result = raw_prs
  for task_name, pattern, replacement in pipeline:
    print('Executing: {0}'.format(task_name))
    result = re.sub(pattern, replacement, result, flags=re.MULTILINE)

  print('\n\n=========== RESULT ===============\n\n{0}'.format(result))
