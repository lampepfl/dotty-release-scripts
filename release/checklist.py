def produce(release_version):
  with open('data/checklist.md', 'r') as f:
    template = f.read()

  result = template.format(
    release_version = release_version,
  )
  print(result)
