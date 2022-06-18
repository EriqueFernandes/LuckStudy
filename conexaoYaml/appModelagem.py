import yaml

with open('../yaml/modelagem.yaml', 'r') as f:
  print(yaml.full_load(f))

  