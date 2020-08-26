# Controller Schema

```txt
#/properties/controller#/properties/controller
```

The responsible controller is defined in here.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## controller Type

`object` ([Controller](tilt-schema-properties-controller.md))

## controller Examples

```json
{
  "name": "Green Company AG",
  "division": "Product line e-mobility",
  "address": "Wolfsburger Ring 2, 38440 Berlin",
  "country": "DE",
  "representative": {
    "name": "Jane Super",
    "email": "contact@greencompany.de",
    "phone": "0049 151 1234 5678"
  }
}
```

# Controller Properties

| Property                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                 |
| :-------------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                     | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-name.md "\#/properties/controller/properties/name#/properties/controller/properties/name")                               |
| [division](#division)             | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-division.md "\#/properties/controller/properties/division#/properties/controller/properties/division")                   |
| [address](#address)               | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-address.md "\#/properties/controller/properties/address#/properties/controller/properties/address")                      |
| [country](#country)               | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-country.md "\#/properties/controller/properties/country#/properties/controller/properties/country")                      |
| [representative](#representative) | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative.md "\#/properties/controller/properties/representative#/properties/controller/properties/representative") |
| Additional Properties             | Any      | Optional | can be null    |                                                                                                                                                                                                                            |

## name

Name of the controller.


`name`

-   is required
-   Type: `string` ([Name](tilt-schema-properties-controller-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-name.md "\#/properties/controller/properties/name#/properties/controller/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-controller-properties-name.md))

### name Examples

```json
"Green Company AG"
```

## division

Serves to differentiate between different areas of a company; particularly relevant for large companies.


`division`

-   is optional
-   Type: `string` ([Division](tilt-schema-properties-controller-properties-division.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-division.md "\#/properties/controller/properties/division#/properties/controller/properties/division")

### division Type

`string` ([Division](tilt-schema-properties-controller-properties-division.md))

### division Examples

```json
"Product line e-mobility"
```

## address

Address of the controller.


`address`

-   is required
-   Type: `string` ([Address](tilt-schema-properties-controller-properties-address.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-address.md "\#/properties/controller/properties/address#/properties/controller/properties/address")

### address Type

`string` ([Address](tilt-schema-properties-controller-properties-address.md))

### address Examples

```json
"Wolfsburger Ring 2, 38440 Berlin"
```

## country

All country codes follow the established ones ISO 3166 country abbreviation standard.


`country`

-   is required
-   Type: `string` ([Country](tilt-schema-properties-controller-properties-country.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-country.md "\#/properties/controller/properties/country#/properties/controller/properties/country")

### country Type

`string` ([Country](tilt-schema-properties-controller-properties-country.md))

### country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z][A-Z]$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D%5BA-Z%5D%24 "try regular expression with regexr.com")

### country Default Value

The default value is:

```json
"DE"
```

### country Examples

```json
"DE"
```

## representative

The representative is a responsible real person that represents the controller.


`representative`

-   is required
-   Type: `object` ([Representative](tilt-schema-properties-controller-properties-representative.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative.md "\#/properties/controller/properties/representative#/properties/controller/properties/representative")

### representative Type

`object` ([Representative](tilt-schema-properties-controller-properties-representative.md))

### representative Examples

```json
{
  "name": "Jane Super",
  "email": "contact@greencompany.de",
  "phone": "0049 151 1234 5678"
}
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
