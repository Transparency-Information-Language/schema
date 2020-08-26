# RightToComplain Schema

```txt
#/properties/rightToComplain#/properties/rightToComplain
```

This schema refers to the right to complain.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## rightToComplain Type

`object` ([RightToComplain](tilt-schema-properties-righttocomplain.md))

## rightToComplain Examples

```json
{
  "available": true,
  "description": "For the right to complain please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ],
  "supervisoryAuthority": {
    "name": "Commissioner for Data Protection",
    "address": "Friedrichstrasse 219, 10969 Berlin",
    "country": "DE",
    "email": "mailbox@privacy-berlin.de",
    "phone": "0049 444 222 111"
  }
}
```

# RightToComplain Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                           |
| :-------------------------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-available.md "\#/properties/rightToComplain/properties/available#/properties/rightToComplain/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-description.md "\#/properties/rightToComplain/properties/description#/properties/rightToComplain/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-url.md "\#/properties/rightToComplain/properties/url#/properties/rightToComplain/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-email.md "\#/properties/rightToComplain/properties/email#/properties/rightToComplain/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-identificationevidences.md "\#/properties/rightToComplain/properties/identificationEvidences#/properties/rightToComplain/properties/identificationEvidences") |
| [supervisoryAuthority](#supervisoryAuthority)       | `object`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority.md "\#/properties/rightToComplain/properties/supervisoryAuthority#/properties/rightToComplain/properties/supervisoryAuthority")          |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                      |

## available

Is this right available?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-righttocomplain-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-available.md "\#/properties/rightToComplain/properties/available#/properties/rightToComplain/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-righttocomplain-properties-available.md))

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
-   Type: `string` ([Description](tilt-schema-properties-righttocomplain-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-description.md "\#/properties/rightToComplain/properties/description#/properties/rightToComplain/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-righttocomplain-properties-description.md))

### description Examples

```json
"For the right to complain please use this contact form and..."
```

## url




`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-righttocomplain-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-url.md "\#/properties/rightToComplain/properties/url#/properties/rightToComplain/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-righttocomplain-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://greencompany.org/rights"
```

## email




`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttocomplain-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-email.md "\#/properties/rightToComplain/properties/email#/properties/rightToComplain/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttocomplain-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## identificationEvidences




`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-righttocomplain-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-identificationevidences.md "\#/properties/rightToComplain/properties/identificationEvidences#/properties/rightToComplain/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-righttocomplain-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "ID card copy",
  "Email verification"
]
```

## supervisoryAuthority

Defines the supervisory authority that has to be contacted in order to complain about the data controller's practices.


`supervisoryAuthority`

-   is optional
-   Type: `object` ([SupervisoryAuthority](tilt-schema-properties-righttocomplain-properties-supervisoryauthority.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority.md "\#/properties/rightToComplain/properties/supervisoryAuthority#/properties/rightToComplain/properties/supervisoryAuthority")

### supervisoryAuthority Type

`object` ([SupervisoryAuthority](tilt-schema-properties-righttocomplain-properties-supervisoryauthority.md))

### supervisoryAuthority Examples

```json
{
  "name": "Commissioner for Data Protection",
  "address": "Friedrichstrasse 219, 10969 Berlin",
  "country": "DE",
  "email": "mailbox@privacy-berlin.de",
  "phone": "0049 444 222 111"
}
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
