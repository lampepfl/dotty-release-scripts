#!/usr/bin/env python3
from release import changelog, util
from release.ecosystem import ecosystem

release_version = input('What version are we releasing? > ')
util.choice_loop(
  {
    'Produce Checklist': lambda: print(util.load_data('checklist.md', release_version)),
    'Refine Changelog': lambda: changelog.refine(),
    'Release Ecosystem': lambda: ecosystem.select_project(release_version)
  },
  'What do you want to do?',
  lambda f: f()
)
