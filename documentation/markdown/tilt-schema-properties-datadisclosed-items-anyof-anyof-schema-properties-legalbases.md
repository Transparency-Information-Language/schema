# LegalBases Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/legalBases#/properties/dataDisclosed/items/anyOf/0/properties/legalBases
```

An explanation about the legal bases for the processing of personal data disclosed.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## legalBases Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items.md))

## legalBases Examples

```json
[
  {
    "reference": "GDPR-99-1-a",
    "description": "The data are processed on the basis of Art. 99 GDPR which states..."
  },
  {
    "reference": "BDSG-42-5",
    "description": "BDSG-42-5 refers to the processing of personal data within..."
  }
]
```
