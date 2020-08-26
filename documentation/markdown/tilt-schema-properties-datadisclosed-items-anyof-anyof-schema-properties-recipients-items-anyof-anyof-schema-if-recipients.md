# AnyOf schema if recipients Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema if recipients](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients.md))

## 0 Examples

```json
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
}
```

# AnyOf schema if recipients Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                     | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-name.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/name#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/name")                               |
| [division](#division)             | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-division.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/division#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/division")                   |
| [address](#address)               | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-address.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/address#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/address")                      |
| [country](#country)               | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-country.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country")                      |
| [representative](#representative) | `object` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative") |
| [category](#category)             | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/category")                   |
| Additional Properties             | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                               |

## name

The name of the third party (recipient).


`name`

-   is optional
-   Type: `string` ([Name](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-name.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/name#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-name.md))

### name Examples

```json
"Yellow Company AG"
```

## division

The division of the third party (recipient) for structuring controllers into smaller entities.


`division`

-   is optional
-   Type: `string` ([Division](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-division.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-division.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/division#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/division")

### division Type

`string` ([Division](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-division.md))

### division Examples

```json
"Product line e-mobility"
```

## address

The address of the third party (recipient).


`address`

-   is optional
-   Type: `string` ([Address](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-address.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-address.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/address#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/address")

### address Type

`string` ([Address](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-address.md))

### address Examples

```json
"Triana 123, 9999 Seville"
```

## country

The country in which the recipient is located at. Attention: This explictly specifies third country transfers!


`country`

-   is optional
-   Type: `string` ([Country](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-country.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-country.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country")

### country Type

`string` ([Country](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-country.md))

### country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z][A-Z]$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D%5BA-Z%5D%24 "try regular expression with regexr.com")

### country Examples

```json
"ES"
```

## representative

The representative of the third party (recipient).


`representative`

-   is optional
-   Type: `object` ([Representative](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative")

### representative Type

`object` ([Representative](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative.md))

### representative Examples

```json
{
  "name": "Jane Super",
  "email": "contact@yellowcompany.de",
  "phone": "0049 151 1234 9876"
}
```

## category

The category of the the recipient.


`category`

-   is required
-   Type: `string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-category.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/category")

### category Type

`string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-category.md))

### category Examples

```json
"Marketing content provider"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
