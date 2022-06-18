import yaml

with open('../yaml/calculo.yaml', 'r') as f:
  print(yaml.full_load(f))

  