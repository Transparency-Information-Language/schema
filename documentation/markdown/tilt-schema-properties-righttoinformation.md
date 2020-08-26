# RightToInformation Schema

```txt
#/properties/rightToInformation#/properties/rightToInformation
```

Refers to the right of information.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## rightToInformation Type

`object` ([RightToInformation](tilt-schema-properties-righttoinformation.md))

## rightToInformation Examples

```json
{
  "available": true,
  "description": "For the right to information please use this contact form and...",
  "url": "https://greencompany.org/rightToInformation",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ]
}
```

# RightToInformation Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :-------------------------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-available.md "\#/properties/rightToInformation/properties/available#/properties/rightToInformation/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-description.md "\#/properties/rightToInformation/properties/description#/properties/rightToInformation/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-url.md "\#/properties/rightToInformation/properties/url#/properties/rightToInformation/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-email.md "\#/properties/rightToInformation/properties/email#/properties/rightToInformation/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-identificationevidences.md "\#/properties/rightToInformation/properties/identificationEvidences#/properties/rightToInformation/properties/identificationEvidences") |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                               |

## available

Possibility available?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-righttoinformation-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-available.md "\#/properties/rightToInformation/properties/available#/properties/rightToInformation/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-righttoinformation-properties-available.md))

### available Default Value

The default value is:

```json
true
```

### available Examples

```json
true
```

## description

Description of the right.


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-righttoinformation-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-description.md "\#/properties/rightToInformation/properties/description#/properties/rightToInformation/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-righttoinformation-properties-description.md))

### description Examples

```json
"For the right to information please use this contact form and..."
```

## url

URL to an online portal.


`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-righttoinformation-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-url.md "\#/properties/rightToInformation/properties/url#/properties/rightToInformation/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-righttoinformation-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://greencompany.org/rightToInformation"
```

## email




`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttoinformation-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-email.md "\#/properties/rightToInformation/properties/email#/properties/rightToInformation/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttoinformation-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## identificationEvidences




`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-righttoinformation-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation-properties-identificationevidences.md "\#/properties/rightToInformation/properties/identificationEvidences#/properties/rightToInformation/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-righttoinformation-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "ID card copy",
  "Email verification"
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
