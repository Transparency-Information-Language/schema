# RightToWithdrawConsent Schema

```txt
#/properties/rightToWithdrawConsent#/properties/rightToWithdrawConsent
```

This schema refers to the right to withdraw consent.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## rightToWithdrawConsent Type

`object` ([RightToWithdrawConsent](tilt-schema-properties-righttowithdrawconsent.md))

## rightToWithdrawConsent Examples

```json
{
  "available": true,
  "description": "For the right to withdraw consent please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "Email verification"
  ]
}
```

# RightToWithdrawConsent Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                |
| :-------------------------------------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)                             | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-available.md "\#/properties/rightToWithdrawConsent/properties/available#/properties/rightToWithdrawConsent/properties/available")                                           |
| [description](#description)                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-description.md "\#/properties/rightToWithdrawConsent/properties/description#/properties/rightToWithdrawConsent/properties/description")                                     |
| [url](#url)                                         | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-url.md "\#/properties/rightToWithdrawConsent/properties/url#/properties/rightToWithdrawConsent/properties/url")                                                             |
| [email](#email)                                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-email.md "\#/properties/rightToWithdrawConsent/properties/email#/properties/rightToWithdrawConsent/properties/email")                                                       |
| [identificationEvidences](#identificationEvidences) | `array`   | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-identificationevidences.md "\#/properties/rightToWithdrawConsent/properties/identificationEvidences#/properties/rightToWithdrawConsent/properties/identificationEvidences") |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                           |

## available




`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-righttowithdrawconsent-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-available.md "\#/properties/rightToWithdrawConsent/properties/available#/properties/rightToWithdrawConsent/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-righttowithdrawconsent-properties-available.md))

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
-   Type: `string` ([Description](tilt-schema-properties-righttowithdrawconsent-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-description.md "\#/properties/rightToWithdrawConsent/properties/description#/properties/rightToWithdrawConsent/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-righttowithdrawconsent-properties-description.md))

### description Examples

```json
"For the right to withdraw consent please use this contact form and..."
```

## url




`url`

-   is optional
-   Type: `string` ([Url](tilt-schema-properties-righttowithdrawconsent-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-url.md "\#/properties/rightToWithdrawConsent/properties/url#/properties/rightToWithdrawConsent/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-righttowithdrawconsent-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://greencompany.org/rights"
```

## email




`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttowithdrawconsent-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-email.md "\#/properties/rightToWithdrawConsent/properties/email#/properties/rightToWithdrawConsent/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttowithdrawconsent-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## identificationEvidences




`identificationEvidences`

-   is optional
-   Type: an array of merged types ([Details](tilt-schema-properties-righttowithdrawconsent-properties-identificationevidences-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent-properties-identificationevidences.md "\#/properties/rightToWithdrawConsent/properties/identificationEvidences#/properties/rightToWithdrawConsent/properties/identificationEvidences")

### identificationEvidences Type

an array of merged types ([Details](tilt-schema-properties-righttowithdrawconsent-properties-identificationevidences-items.md))

### identificationEvidences Examples

```json
[
  "Email verification"
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
