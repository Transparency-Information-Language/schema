# Temporal Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal
```

This schema serves to specify a temporal description of how long the data is stored and for what exactly.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## temporal Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal-items.md))

## temporal Examples

```json
[
  {
    "description": "Creating backups.",
    "ttl": "2005-08-09T18:31:42P3Y6M4DT12H30M17S"
  },
  {
    "description": "Finishing ordering process.",
    "ttl": "2020-08-09T18:31:42P3Y6M4DT12H30M17S"
  }
]
```
