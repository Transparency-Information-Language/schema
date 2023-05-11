import json
from pathlib import Path
import re

base_path = Path( __file__ ).parent.parent
tilt_schema_path = base_path / Path("tilt_schema")
tilt_schema_path.mkdir(exist_ok=True)

indent = 2

root_schema = None
with open(tilt_schema_path / Path("root_schema.json"), "r") as f:
  root_schema = json.load(f)

properties = root_schema["properties"]

pattern = re.compile("[0-9]{2}_(\w+).json") 
properties_path = tilt_schema_path / Path("properties")
for path in sorted(properties_path.glob("*.json")):
  match = pattern.match(path.name)
  key = match.group(1)
  print(path.name)
  if match:
    with open(path, 'r') as f:
      properties[key] = json.load(f)



with open(base_path / Path("tilt-schema.json"), "w") as f:
  json.dump(root_schema, f, indent=indent)
