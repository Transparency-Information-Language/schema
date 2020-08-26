# Sources Schema

```txt
#/properties/sources/items/anyOf/0/properties/sources#/properties/sources/items/anyOf/0/properties/sources
```

Specify the source(s) where the data come from.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## sources Type

an array of merged types ([Details](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items.md))

## sources Examples

```json
[
  {
    "description": "This information could be retrieved from...",
    "url": "https://blueCompany.org",
    "publiclyAvailable": false
  }
]
```
