# Storage Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/storage#/properties/dataDisclosed/items/anyOf/0/properties/storage
```

In this section, the duration of storage or storage criteria are given.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## storage Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items.md))

## storage Examples

```json
[
  {
    "temporal": [
      {
        "description": "Creating backups.",
        "ttl": "2005-08-09T18:31:42P3Y6M4DT12H30M17S"
      },
      {
        "description": "Finishing ordering process.",
        "ttl": "2020-08-09T18:31:42P3Y6M4DT12H30M17S"
      }
    ],
    "purposeConditional": [
      "Data is stored until the end of the ordering process."
    ],
    "legalBasisConditional": [
      "SGB-100-42"
    ],
    "aggregationFunction": "max"
  }
]
```
