from jsonschema import validate, Validator
import json

with open('tilt-schema.json') as file:
    tilt_schema = json.load(file)


def validate_sub_schema_examples(schema):
  print(schema.get("$id"))
  schema = schema.copy()
  schema["$schema"] = tilt_schema["$schema"]
  schema["$id"] = tilt_schema["$id"]
  for example in schema["examples"]:
    validate(instance=example, schema=schema)


def walk_schema(schema):
   validate_sub_schema_examples(schema)
   if not schema.get('properties'):
      return
   for property in schema["properties"].values():
      walk_schema(property)


walk_schema(tilt_schema)