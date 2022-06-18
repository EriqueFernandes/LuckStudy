import yaml

with open('../yaml/ga.yaml', 'r') as f:
  print(yaml.full_load(f))

  