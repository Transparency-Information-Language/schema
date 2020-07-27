from jsonschema import validate
import json

with open('tilt-schema.json') as file:
    schema = json.load(file)

with open('tilt.json') as file:
    instance = json.load(file)

validate(instance=instance, schema=schema)


with open('tilt-NOT-valid.json') as file:
    not_valid = json.load(file)

validate(instance=not_valid, schema=schema)
