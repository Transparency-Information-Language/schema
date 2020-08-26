# DataDisclosed Schema

```txt
#/properties/dataDisclosed#/properties/dataDisclosed
```

A detailed explanation about which data is disclosed in the processing tasks.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## dataDisclosed Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items.md))

## dataDisclosed Examples

```json
[
  {
    "_id": "f1424f86-ca0f-4f0c-9438-43cc00509931",
    "category": "E-mail address",
    "purposes": [
      {
        "purpose": "Marketing",
        "description": "Newsletter will be sent out once a month."
      }
    ],
    "legalBases": [
      {
        "reference": "GDPR-99-1-a",
        "description": "The data are processed on the basis of Art. 99 GDPR which states..."
      },
      {
        "reference": "BDSG-42-5",
        "description": "BDSG-42-5 refers to the processing of personal data within..."
      }
    ],
    "legitimateInterests": [
      {
        "exists": true,
        "reasoning": "There is an legitimate interest based on ... and is not overwritten because ..."
      }
    ],
    "recipients": [
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
    ],
    "storage": [
      {
        "temporal": [
          {
            "description": "Creating backups.",
            "ttl": "2005-08-09T18:31:42P3Y6M4DT12H30M17S"
          },
          {
            "description": "Finishing ordering process.",
            "ttl": "2020-07-12T18:31:42P3Y6M4DT12H30M17S"
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
    ],
    "nonDisclosure": {
      "legalRequirement": false,
      "contractualRegulation": false,
      "obligationToProvide": false,
      "consequences": "If the data is not disclosed, the shipment cannot be delivered."
    }
  }
]
```
