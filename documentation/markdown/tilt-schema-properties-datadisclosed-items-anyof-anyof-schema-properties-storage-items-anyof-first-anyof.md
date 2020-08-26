# First anyOf Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([First anyOf](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof.md))

## 0 Examples

```json
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
```

# First anyOf Properties

| Property                                        | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [temporal](#temporal)                           | `array`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal")                                        |
| [purposeConditional](#purposeConditional)       | `array`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-purposeconditional.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/purposeConditional#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/purposeConditional")          |
| [legalBasisConditional](#legalBasisConditional) | `array`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-legalbasisconditional.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/legalBasisConditional#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/legalBasisConditional") |
| [aggregationFunction](#aggregationFunction)     | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-aggregationfunction.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction")       |
| Additional Properties                           | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                            |

## temporal

This schema serves to specify a temporal description of how long the data is stored and for what exactly.


`temporal`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal")

### temporal Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal-items.md))

### temporal Examples

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

## purposeConditional

Specifies the purpose that requires data storage.


`purposeConditional`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-purposeconditional-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-purposeconditional.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/purposeConditional#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/purposeConditional")

### purposeConditional Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-purposeconditional-items.md))

### purposeConditional Examples

```json
[
  "Data is stored until the end of the ordering process."
]
```

## legalBasisConditional

If the storage is required by law, the respective one has to specified in here.


`legalBasisConditional`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-legalbasisconditional-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-legalbasisconditional.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/legalBasisConditional#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/legalBasisConditional")

### legalBasisConditional Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-legalbasisconditional-items.md))

### legalBasisConditional Examples

```json
[
  "SGB-100-42"
]
```

## aggregationFunction

The aggregation function describes the calculation basis when specifying several time intervals. For example, if there is storage for 2 weeks for technical reasons (e.g. backup), but there is a legally longer retention period, the maximum aggregation function (max) would be selected (standard case). Aggregation functions available: min, max, sum, avg


`aggregationFunction`

-   is required
-   Type: `string` ([AggregationFunction](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-aggregationfunction.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-aggregationfunction.md "\#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction")

### aggregationFunction Type

`string` ([AggregationFunction](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-aggregationfunction.md))

### aggregationFunction Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | ----------- |
| `"min"` |             |
| `"max"` |             |
| `"sum"` |             |
| `"avg"` |             |

### aggregationFunction Default Value

The default value is:

```json
"max"
```

### aggregationFunction Examples

```json
"max"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
