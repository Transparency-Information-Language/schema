# Sources Schema

```txt
#/properties/sources#/properties/sources
```

This duty to provide information is limited to the collection of personal data that does not take place from the data subject (Art. 14).


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## sources Type

an array of merged types ([Details](tilt-schema-properties-sources-items.md))

## sources Examples

```json
[
  {
    "_id": "f1423cc00509931",
    "dataCategory": "Creditworthiness",
    "sources": [
      {
        "description": "This information could be retrieved from...",
        "url": "https://blueCompany.org",
        "publiclyAvailable": false
      }
    ]
  }
]
```
