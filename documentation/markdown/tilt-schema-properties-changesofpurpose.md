# ChangesOfPurpose Schema

```txt
#/properties/changesOfPurpose#/properties/changesOfPurpose
```

Notification of change of purpose.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## changesOfPurpose Type

an array of merged types ([Details](tilt-schema-properties-changesofpurpose-items.md))

## changesOfPurpose Examples

```json
[
  {
    "description": "Due to technical requirements...",
    "affectedDataCategories": [
      "Email adress",
      "Credit score"
    ],
    "plannedDateOfChange": "2020-08-20",
    "urlOfNewVersion": "https://greencomp.de/privacypolicy/2"
  }
]
```
