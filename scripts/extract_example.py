import json
from pathlib import Path

base_path = Path( __file__ ).parent.parent
tilt_schema_path = base_path / Path("tilt_schema")
tilt_schema_path.mkdir(exist_ok=True)

indent = 2

root_schema = None
with open(tilt_schema_path / Path("root_schema.json"), "r") as f:
  root_schema = json.load(f)

with open(base_path / Path("tilt.json"), "w") as f:
  json.dump(root_schema["examples"][0], f, indent=indent)