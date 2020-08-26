# SupervisoryAuthority Schema

```txt
#/properties/rightToComplain/properties/supervisoryAuthority#/properties/rightToComplain/properties/supervisoryAuthority
```

Defines the supervisory authority that has to be contacted in order to complain about the data controller's practices.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## supervisoryAuthority Type

`object` ([SupervisoryAuthority](tilt-schema-properties-righttocomplain-properties-supervisoryauthority.md))

## supervisoryAuthority Examples

```json
{
  "name": "Commissioner for Data Protection",
  "address": "Friedrichstrasse 219, 10969 Berlin",
  "country": "DE",
  "email": "mailbox@privacy-berlin.de",
  "phone": "0049 444 222 111"
}
```

# SupervisoryAuthority Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                           |
| :-------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-name.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/name#/properties/rightToComplain/properties/supervisoryAuthority/properties/name")          |
| [address](#address)   | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-address.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/address#/properties/rightToComplain/properties/supervisoryAuthority/properties/address") |
| [country](#country)   | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-country.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/country#/properties/rightToComplain/properties/supervisoryAuthority/properties/country") |
| [email](#email)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-email.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/email#/properties/rightToComplain/properties/supervisoryAuthority/properties/email")       |
| [phone](#phone)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-phone.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/phone#/properties/rightToComplain/properties/supervisoryAuthority/properties/phone")       |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                      |

## name

Name of the supervisory authority.


`name`

-   is required
-   Type: `string` ([Name](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-name.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/name#/properties/rightToComplain/properties/supervisoryAuthority/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-name.md))

### name Examples

```json
"Commissioner for Data Protection"
```

## address

Adress of the supervisory authority.


`address`

-   is optional
-   Type: `string` ([Address](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-address.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-address.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/address#/properties/rightToComplain/properties/supervisoryAuthority/properties/address")

### address Type

`string` ([Address](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-address.md))

### address Examples

```json
"Friedrichstrasse 219, 10969 Berlin"
```

## country

Country of the supervisory authority.


`country`

-   is optional
-   Type: `string` ([Country](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-country.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-country.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/country#/properties/rightToComplain/properties/supervisoryAuthority/properties/country")

### country Type

`string` ([Country](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-country.md))

### country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

### country Examples

```json
"DE"
```

## email

Email adress of the supervisory authority.


`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-email.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/email#/properties/rightToComplain/properties/supervisoryAuthority/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"mailbox@privacy-berlin.de"
```

## phone

Phone number of the supervisory authority.


`phone`

-   is optional
-   Type: `string` ([Phone](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-phone.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-phone.md "\#/properties/rightToComplain/properties/supervisoryAuthority/properties/phone#/properties/rightToComplain/properties/supervisoryAuthority/properties/phone")

### phone Type

`string` ([Phone](tilt-schema-properties-righttocomplain-properties-supervisoryauthority-properties-phone.md))

### phone Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%2B%5D*%5B(%5D%7B0%2C1%7D%5B0-9%5D%7B1%2C4%7D%5B)%5D%7B0%2C1%7D%5B-%5Cs%5C.%2F0-9%5D*%24 "try regular expression with regexr.com")

### phone Examples

```json
"0049 444 222 111"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
