from jsonschema import validate
import json

with open('tilt-schema.json') as file:
    schema = json.load(file)


for example in schema["examples"]:
  validate(instance=example, schema=schema)