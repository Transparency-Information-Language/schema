import json
from pathlib import Path

base_path = Path( __file__ ).parent.parent
tilt_schema_path = base_path / Path("tilt_schema")
tilt_schema_path.mkdir(exist_ok=True)

indent = 2

with open(base_path / Path("tilt-schema.json"),'r') as f:
  tilt_schema = json.load(f)

with open(tilt_schema_path / Path("root_schema.json"), "w") as f:
  copy_tilt_schema = tilt_schema.copy()
  copy_tilt_schema["properties"] = {}
  json.dump(copy_tilt_schema, f, indent=indent)


for i, (key, value) in enumerate(tilt_schema["properties"].items()):
  path = tilt_schema_path / Path(f"properties/{i:02d}_{key}.json")
  path.parent.mkdir(exist_ok=True, parents=True)
  with open(path, 'w') as f:
    json.dump(value, f, indent=indent)
