import yaml

with open('../yaml/fundamentos.yaml', 'r') as f:
  print(yaml.full_load(f))

  