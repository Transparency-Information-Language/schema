# AnyOf schema Schema

```txt
#/properties/dataDisclosed/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0
```

The description of data disclosed.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema.md))

## 0 Examples

```json
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
  ],
  "nonDisclosure": {
    "legalRequirement": false,
    "contractualRegulation": false,
    "obligationToProvide": false,
    "consequences": "If the data is not disclosed, the shipment cannot be delivered."
  }
}
```

# AnyOf schema Properties

| Property                                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                              |
| :------------------------------------------ | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [\_id](#_id)                                | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-_id.md "\#/properties/dataDisclosed/items/anyOf/0/properties/\_id#/properties/dataDisclosed/items/anyOf/0/properties/\_id")                                               |
| [category](#category)                       | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/category")                                  |
| [purposes](#purposes)                       | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes#/properties/dataDisclosed/items/anyOf/0/properties/purposes")                                  |
| [legalBases](#legalBases)                   | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases#/properties/dataDisclosed/items/anyOf/0/properties/legalBases")                            |
| [legitimateInterests](#legitimateInterests) | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests") |
| [recipients](#recipients)                   | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients#/properties/dataDisclosed/items/anyOf/0/properties/recipients")                            |
| [storage](#storage)                         | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage#/properties/dataDisclosed/items/anyOf/0/properties/storage")                                     |
| [nonDisclosure](#nonDisclosure)             | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure")                   |
| Additional Properties                       | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                         |

## \_id

The id of a data item that is disclosed. The id is necessary to distinguish several processing tasks of the same data item (locally unique ID that can be based on the database implementation).


`_id`

-   is required
-   Type: `string` ([\_id](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-_id.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-_id.md "\#/properties/dataDisclosed/items/anyOf/0/properties/\_id#/properties/dataDisclosed/items/anyOf/0/properties/\_id")

### \_id Type

`string` ([\_id](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-_id.md))

### \_id Examples

```json
"f1424f86-ca0f-4f0c-9438-43cc00509931"
```

## category

The data (category) the data disclosed is referred to.


`category`

-   is required
-   Type: `string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-category.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/category")

### category Type

`string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-category.md))

### category Examples

```json
"E-mail address"
```

## purposes

The purpose for which a data item is processed for.


`purposes`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes#/properties/dataDisclosed/items/anyOf/0/properties/purposes")

### purposes Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items.md))

### purposes Examples

```json
[
  {
    "purpose": "Marketing",
    "description": "Newsletter will be sent out once a month."
  }
]
```

## legalBases

An explanation about the legal bases for the processing of personal data disclosed.


`legalBases`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases#/properties/dataDisclosed/items/anyOf/0/properties/legalBases")

### legalBases Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items.md))

### legalBases Examples

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

## legitimateInterests

An explanation about the legitimate interests for the processing of data disclosed.


`legitimateInterests`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests")

### legitimateInterests Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items.md))

### legitimateInterests Examples

```json
[
  {
    "exists": true,
    "reasoning": "There is an legitimate interest based on ... and is not overwritten because ..."
  }
]
```

## recipients

An explanation about the recipients of the data disclosed.


`recipients`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients#/properties/dataDisclosed/items/anyOf/0/properties/recipients")

### recipients Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items.md))

### recipients Examples

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

## storage

In this section, the duration of storage or storage criteria are given.


`storage`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage#/properties/dataDisclosed/items/anyOf/0/properties/storage")

### storage Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items.md))

### storage Examples

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

## nonDisclosure

This schema refers to the necessity and consequences of non-disclosure of personal data. According to Art. 13 (2e), this refers to the information whether the provision of the personal data is required by law or contract or is required for the conclusion of a contract, whether the data subject is obliged to provide the personal data and the possible consequences of not providing it.


`nonDisclosure`

-   is required
-   Type: `object` ([NonDisclosure](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure")

### nonDisclosure Type

`object` ([NonDisclosure](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure.md))

### nonDisclosure Examples

```json
{
  "legalRequirement": false,
  "contractualRegulation": false,
  "obligationToProvide": false,
  "consequences": "If the data is not disclosed, the shipment cannot be delivered."
}
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
