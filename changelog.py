#!/usr/bin/env python3

import sys, re

raw_prs = ''.join(sys.stdin.readlines())
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

result = raw_prs
for task_name, pattern, replacement in pipeline:
  print('Executing: {0}'.format(task_name))
  result = re.sub(pattern, replacement, result, flags=re.MULTILINE)

print('\n\n=========== RESULT ===============\n\n{0}'.format(result))