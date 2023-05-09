import fastjsonschema
import json

with open('tilt-schema.json') as file:
    schema = json.load(file)

print('Compile schema...')
validate = fastjsonschema.compile(schema)

print('---')

print('Validate instance tilt.json...')
with open('tilt.json') as file:
    instance = json.load(file)

validate(instance)

print('---')

print('Validate tilt-NOT-valid.json...')
with open('tilt-NOT-valid.json') as file:
    not_valid = json.load(file)

validate(not_valid)

