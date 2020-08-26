# Recipients Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients#/properties/dataDisclosed/items/anyOf/0/properties/recipients
```

An explanation about the recipients of the data disclosed.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## recipients Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items.md))

## recipients Examples

```json
[
  {
    "name": "Yellow Company AG",
    "division": "Product line e-mobility",
    "address": "Triana 123, 9999 Seville",
    "country": "ES",
    "representative": {
      "name": "Jane Super",
      "email": "contact@yellowcompany.de",
      "phone": "0049 151 1234 9876"
    },
    "category": "Marketing content provider"
  },
  {
    "category": "Responsible Statistical Institutes"
  }
]
```
