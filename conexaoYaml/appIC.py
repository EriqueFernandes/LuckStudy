import yaml

with open('../yaml/ic.yaml', 'r') as f:
  print(yaml.full_load(f))

  