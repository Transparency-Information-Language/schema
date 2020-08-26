# RightToDataPortability Schema

```txt
#/properties/rightToDataPortability#/properties/rightToDataPortability
```

The right to data portability as stated in Art. 20 GDPR.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## rightToDataPortability Type

`object` ([RightToDataPortability](tilt-schema-properties-righttodataportability.md))

## rightToDataPortability Examples

```json
{
  "available": true,
  "description": "Data portability is only possible when...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy"
  ]
}
```

# RightToDataPortability Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-available.md "\#/properties/rightToDataPortability/properties/available#/properties/rightToDataPortability/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-description.md "\#/properties/rightToDataPortability/properties/description#/properties/rightToDataPortability/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-url.md "\#/properties/rightToDataPortability/properties/url#/properties/rightToDataPortability/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-email.md "\#/properties/rightToDataPortability/properties/email#/properties/rightToDataPortability/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-identificationevidences.md "\#/properties/rightToDataPortability/properties/identificationEvidences#/properties/rightToDataPortability/properties/identificationEvidences") |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                           |

## available




`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-righttodataportability-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-available.md "\#/properties/rightToDataPortability/properties/available#/properties/rightToDataPortability/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-righttodataportability-properties-available.md))

### available Default Value

The default value is:

```json
true
```

### available Examples

```json
false
```

```json
true
```

## description




`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-righttodataportability-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-description.md "\#/properties/rightToDataPortability/properties/description#/properties/rightToDataPortability/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-righttodataportability-properties-description.md))

### description Examples

```json
"Data portability is only possible when..."
```

## url




`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-righttodataportability-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-url.md "\#/properties/rightToDataPortability/properties/url#/properties/rightToDataPortability/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-righttodataportability-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://greencompany.org/rights"
```

## email




`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttodataportability-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-email.md "\#/properties/rightToDataPortability/properties/email#/properties/rightToDataPortability/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttodataportability-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## identificationEvidences




`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-righttodataportability-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability-properties-identificationevidences.md "\#/properties/rightToDataPortability/properties/identificationEvidences#/properties/rightToDataPortability/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-righttodataportability-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "ID card copy"
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
