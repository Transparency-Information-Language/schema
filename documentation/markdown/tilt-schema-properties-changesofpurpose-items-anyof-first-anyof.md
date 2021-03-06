# First anyOf Schema

```txt
#/properties/changesOfPurpose/items/anyOf/0#/properties/changesOfPurpose/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([First anyOf](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof.md))

## 0 Examples

```json
{
  "description": "Due to technical requirements...",
  "affectedDataCategories": [
    "Email adress",
    "Credit score"
  ],
  "plannedDateOfChange": "2020-08-20",
  "urlOfNewVersion": "https://greencomp.de/privacypolicy/2"
}
```

# First anyOf Properties

| Property                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------ | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [description](#description)                       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-description.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/description#/properties/changesOfPurpose/items/anyOf/0/properties/description")                                  |
| [affectedDataCategories](#affectedDataCategories) | `array`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-affecteddatacategories.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/affectedDataCategories#/properties/changesOfPurpose/items/anyOf/0/properties/affectedDataCategories") |
| [plannedDateOfChange](#plannedDateOfChange)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-planneddateofchange.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/plannedDateOfChange#/properties/changesOfPurpose/items/anyOf/0/properties/plannedDateOfChange")          |
| [urlOfNewVersion](#urlOfNewVersion)               | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-urlofnewversion.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/urlOfNewVersion#/properties/changesOfPurpose/items/anyOf/0/properties/urlOfNewVersion")                      |
| Additional Properties                             | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                          |

## description

Description of the change of purpose.


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-description.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/description#/properties/changesOfPurpose/items/anyOf/0/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-description.md))

### description Examples

```json
"Due to technical requirements..."
```

## affectedDataCategories

Data categories that are affected from the change of purpose.


`affectedDataCategories`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-affecteddatacategories-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-affecteddatacategories.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/affectedDataCategories#/properties/changesOfPurpose/items/anyOf/0/properties/affectedDataCategories")

### affectedDataCategories Type

an array of merged types ([Details](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-affecteddatacategories-items.md))

### affectedDataCategories Examples

```json
[
  "Email adress",
  "Credit score"
]
```

## plannedDateOfChange

Specify the planned date to the changes as ISO 8601 string.


`plannedDateOfChange`

-   is optional
-   Type: `string` ([PlannedDateOfChange](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-planneddateofchange.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-planneddateofchange.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/plannedDateOfChange#/properties/changesOfPurpose/items/anyOf/0/properties/plannedDateOfChange")

### plannedDateOfChange Type

`string` ([PlannedDateOfChange](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-planneddateofchange.md))

### plannedDateOfChange Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
```

[try pattern](https://regexr.com/?expression=%5E(%5B%5C%2B-%5D%3F%5Cd%7B4%7D(%3F!%5Cd%7B2%7D%5Cb))((-%3F)((0%5B1-9%5D%7C1%5B0-2%5D)(%5C3(%5B12%5D%5Cd%7C0%5B1-9%5D%7C3%5B01%5D))%3F%7CW(%5B0-4%5D%5Cd%7C5%5B0-2%5D)(-%3F%5B1-7%5D)%3F%7C(00%5B1-9%5D%7C0%5B1-9%5D%5Cd%7C%5B12%5D%5Cd%7B2%7D%7C3(%5B0-5%5D%5Cd%7C6%5B1-6%5D)))(%5BT%5Cs%5D(((%5B01%5D%5Cd%7C2%5B0-3%5D)((%3A%3F)%5B0-5%5D%5Cd)%3F%7C24%5C%3A%3F00)(%5B%5C.%2C%5D%5Cd%2B(%3F!%3A))%3F)%3F(%5C17%5B0-5%5D%5Cd(%5B%5C.%2C%5D%5Cd%2B)%3F)%3F(%5BzZ%5D%7C(%5B%5C%2B-%5D)(%5B01%5D%5Cd%7C2%5B0-3%5D)%3A%3F(%5B0-5%5D%5Cd)%3F)%3F)%3F)%3F%24 "try regular expression with regexr.com")

### plannedDateOfChange Examples

```json
"2020-08-20"
```

## urlOfNewVersion

URL points to a document of the same as this one. That creates a chain of information requirements for seamless recognition of transparency information even over a longer period of time.


`urlOfNewVersion`

-   is optional
-   Type: `string` ([UrlOfNewVersion](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-urlofnewversion.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-urlofnewversion.md "\#/properties/changesOfPurpose/items/anyOf/0/properties/urlOfNewVersion#/properties/changesOfPurpose/items/anyOf/0/properties/urlOfNewVersion")

### urlOfNewVersion Type

`string` ([UrlOfNewVersion](tilt-schema-properties-changesofpurpose-items-anyof-first-anyof-properties-urlofnewversion.md))

### urlOfNewVersion Examples

```json
"https://greencomp.de/tilt/2"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
