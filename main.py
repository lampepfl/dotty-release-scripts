#!/usr/bin/env python3
import sys
sys.path.append('release/ecosystem')

from release import changelog, checklist, util
from release.ecosystem import ecosystem

release_version = input('What version are we releasing? > ')
util.choice_loop(
  {
    'Produce Checklist': lambda: checklist.produce(release_version),
    'Refine Changelog': lambda: changelog.refine(),
    'Release Ecosystem': lambda: ecosystem.select_project(release_version)
  },
  'What do you want to do?',
  lambda f: f()
)