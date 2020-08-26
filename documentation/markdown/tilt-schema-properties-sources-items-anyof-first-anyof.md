# First anyOf Schema

```txt
#/properties/sources/items/anyOf/0#/properties/sources/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([First anyOf](tilt-schema-properties-sources-items-anyof-first-anyof.md))

## 0 Examples

```json
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
```

# First anyOf Properties

| Property                      | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                      |
| :---------------------------- | -------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [\_id](#_id)                  | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-_id.md "\#/properties/sources/items/anyOf/0/properties/\_id#/properties/sources/items/anyOf/0/properties/\_id")                          |
| [dataCategory](#dataCategory) | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-datacategory.md "\#/properties/sources/items/anyOf/0/properties/dataCategory#/properties/sources/items/anyOf/0/properties/dataCategory") |
| [sources](#sources)           | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources.md "\#/properties/sources/items/anyOf/0/properties/sources#/properties/sources/items/anyOf/0/properties/sources")                |
| Additional Properties         | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                 |

## \_id

This refers to an locally unique ID in an arbitrary but deterministic format.


`_id`

-   is required
-   Type: `string` ([\_id](tilt-schema-properties-sources-items-anyof-first-anyof-properties-_id.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-_id.md "\#/properties/sources/items/anyOf/0/properties/\_id#/properties/sources/items/anyOf/0/properties/\_id")

### \_id Type

`string` ([\_id](tilt-schema-properties-sources-items-anyof-first-anyof-properties-_id.md))

### \_id Examples

```json
"f1423cc00509931"
```

## dataCategory

The category the data refer to.


`dataCategory`

-   is required
-   Type: `string` ([DataCategory](tilt-schema-properties-sources-items-anyof-first-anyof-properties-datacategory.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-datacategory.md "\#/properties/sources/items/anyOf/0/properties/dataCategory#/properties/sources/items/anyOf/0/properties/dataCategory")

### dataCategory Type

`string` ([DataCategory](tilt-schema-properties-sources-items-anyof-first-anyof-properties-datacategory.md))

### dataCategory Examples

```json
"Creditworthiness"
```

## sources

Specify the source(s) where the data come from.


`sources`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources.md "\#/properties/sources/items/anyOf/0/properties/sources#/properties/sources/items/anyOf/0/properties/sources")

### sources Type

an array of merged types ([Details](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items.md))

### sources Examples

```json
[
  {
    "description": "This information could be retrieved from...",
    "url": "https://blueCompany.org",
    "publiclyAvailable": false
  }
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
