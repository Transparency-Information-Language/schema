# RightToRectificationOrDeletion Schema

```txt
#/properties/rightToRectificationOrDeletion#/properties/rightToRectificationOrDeletion
```

This schema refers to the right to rectification or deletion (Art. 16 GDPR).


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## rightToRectificationOrDeletion Type

`object` ([RightToRectificationOrDeletion](tilt-schema-properties-righttorectificationordeletion.md))

## rightToRectificationOrDeletion Examples

```json
{
  "available": true,
  "description": "For the right to rectification please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ]
}
```

# RightToRectificationOrDeletion Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                        |
| :-------------------------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-available.md "\#/properties/rightToRectificationOrDeletion/properties/available#/properties/rightToRectificationOrDeletion/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-description.md "\#/properties/rightToRectificationOrDeletion/properties/description#/properties/rightToRectificationOrDeletion/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-url.md "\#/properties/rightToRectificationOrDeletion/properties/url#/properties/rightToRectificationOrDeletion/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-email.md "\#/properties/rightToRectificationOrDeletion/properties/email#/properties/rightToRectificationOrDeletion/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-identificationevidences.md "\#/properties/rightToRectificationOrDeletion/properties/identificationEvidences#/properties/rightToRectificationOrDeletion/properties/identificationEvidences") |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                   |

## available

Possibility available?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-righttorectificationordeletion-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-available.md "\#/properties/rightToRectificationOrDeletion/properties/available#/properties/rightToRectificationOrDeletion/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-righttorectificationordeletion-properties-available.md))

### available Default Value

The default value is:

```json
true
```

### available Examples

```json
true
```

```json
false
```

## description




`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-righttorectificationordeletion-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-description.md "\#/properties/rightToRectificationOrDeletion/properties/description#/properties/rightToRectificationOrDeletion/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-righttorectificationordeletion-properties-description.md))

### description Examples

```json
"For the right to rectification please use this contact form and..."
```

## url




`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-righttorectificationordeletion-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-url.md "\#/properties/rightToRectificationOrDeletion/properties/url#/properties/rightToRectificationOrDeletion/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-righttorectificationordeletion-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://greencompany.org/rights"
```

## email




`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttorectificationordeletion-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-email.md "\#/properties/rightToRectificationOrDeletion/properties/email#/properties/rightToRectificationOrDeletion/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttorectificationordeletion-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## identificationEvidences




`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-righttorectificationordeletion-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion-properties-identificationevidences.md "\#/properties/rightToRectificationOrDeletion/properties/identificationEvidences#/properties/rightToRectificationOrDeletion/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-righttorectificationordeletion-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "ID card copy",
  "Email verification"
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
