# AccessAndDataPortability Schema

```txt
#/properties/accessAndDataPortability#/properties/accessAndDataPortability
```

Defining the right to access and data portability.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## accessAndDataPortability Type

`object` ([AccessAndDataPortability](tilt-schema-properties-accessanddataportability.md))

## accessAndDataPortability Examples

```json
{
  "available": true,
  "description": "Data access is possible through...",
  "url": "https://green-bikes.de/access",
  "email": "access@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ],
  "administrativeFee": {
    "amount": 0,
    "currency": "EUR"
  },
  "dataFormat": "json"
}
```

# AccessAndDataPortability Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                      |
| :-------------------------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-available.md "\#/properties/accessAndDataPortability/properties/available#/properties/accessAndDataPortability/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-description.md "\#/properties/accessAndDataPortability/properties/description#/properties/accessAndDataPortability/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-url.md "\#/properties/accessAndDataPortability/properties/url#/properties/accessAndDataPortability/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-email.md "\#/properties/accessAndDataPortability/properties/email#/properties/accessAndDataPortability/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-identificationevidences.md "\#/properties/accessAndDataPortability/properties/identificationEvidences#/properties/accessAndDataPortability/properties/identificationEvidences") |
| [administrativeFee](#administrativeFee)             | `object`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee.md "\#/properties/accessAndDataPortability/properties/administrativeFee#/properties/accessAndDataPortability/properties/administrativeFee")                   |
| [dataFormats](#dataFormats)                         | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-dataformat.md "\#/properties/accessAndDataPortability/properties/dataFormats#/properties/accessAndDataPortability/properties/dataFormats")                                      |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                 |

## available

The information is subject to the requirements of Art. 20 (right to data portability) GDPR.


`available`

-   is required
-   Type: `boolean` ([Available](tilt-schema-properties-accessanddataportability-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-available.md "\#/properties/accessAndDataPortability/properties/available#/properties/accessAndDataPortability/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-accessanddataportability-properties-available.md))

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

Description of the requirements according to Art. 20 GDPR.


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-accessanddataportability-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-description.md "\#/properties/accessAndDataPortability/properties/description#/properties/accessAndDataPortability/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-accessanddataportability-properties-description.md))

### description Examples

```json
"Data access is possible through..."
```

```json
"In the event that the requirements of Art. 20 Para. 1 GDPR are met, you have the right to store your data in a structured, common .."
```

## url

URL to relevant resources such as access portals.


`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-accessanddataportability-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-url.md "\#/properties/accessAndDataPortability/properties/url#/properties/accessAndDataPortability/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-accessanddataportability-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://green-bikes.de/access"
```

## email

Contact email address


`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-accessanddataportability-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-email.md "\#/properties/accessAndDataPortability/properties/email#/properties/accessAndDataPortability/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-accessanddataportability-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"access@greencompany.de"
```

## identificationEvidences

ID evidences


`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-accessanddataportability-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-identificationevidences.md "\#/properties/accessAndDataPortability/properties/identificationEvidences#/properties/accessAndDataPortability/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-accessanddataportability-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "ID card copy",
  "Email verification"
]
```

## administrativeFee

The fee that refers to several copies.


`administrativeFee`

-   is optional
-   Type: `object` ([AdministrativeFee](tilt-schema-properties-accessanddataportability-properties-administrativefee.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee.md "\#/properties/accessAndDataPortability/properties/administrativeFee#/properties/accessAndDataPortability/properties/administrativeFee")

### administrativeFee Type

`object` ([AdministrativeFee](tilt-schema-properties-accessanddataportability-properties-administrativefee.md))

### administrativeFee Examples

```json
{
  "amount": 0,
  "currency": "EUR"
}
```

## dataFormats

An explanation about the data format(s) the data is provided in.


`dataFormats`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-accessanddataportability-properties-dataformat-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-dataformat.md "\#/properties/accessAndDataPortability/properties/dataFormats#/properties/accessAndDataPortability/properties/dataFormats")

### dataFormats Type

an array of merged types ([Details](tilt-schema-properties-accessanddataportability-properties-dataformat-items.md))

### dataFormats Default Value

The default value is:

```json
[
  "json"
]
```

### dataFormats Examples

```json
"json"
```

```json
"xml"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
