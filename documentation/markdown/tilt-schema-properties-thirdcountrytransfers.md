# ThirdCountryTransfers Schema

```txt
#/properties/thirdCountryTransfers#/properties/thirdCountryTransfers
```

This schema refers to the adequacy decisions of any third country transfers.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## thirdCountryTransfers Type

an array of merged types ([Details](tilt-schema-properties-thirdcountrytransfers-items.md))

## thirdCountryTransfers Examples

```json
[
  {
    "country": "ES",
    "adequacyDecision": {
      "available": true,
      "description": "An adequacy decision was made on the 23rd April 2020 by..."
    },
    "appropriateGuarantees": {
      "available": true,
      "description": "Here the appropriate guarantee was formulated by..."
    },
    "presenceOfEnforceableRightsAndEffectiveRemedies": {
      "available": true,
      "description": "These rights are given because of..."
    },
    "standardDataProtectionClause": {
      "available": true,
      "description": "The standard data protection clause which applies here can be found here: ..."
    }
  }
]
```
