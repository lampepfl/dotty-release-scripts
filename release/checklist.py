from release.util import load_data
def produce(release_version):
  print(load_data('checklist.md', release_version))
