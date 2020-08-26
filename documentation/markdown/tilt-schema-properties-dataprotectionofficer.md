# DataProtectionOfficer Schema

```txt
#/properties/dataProtectionOfficer#/properties/dataProtectionOfficer
```

The Data Protection Officer (DPO) of the controller.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## dataProtectionOfficer Type

`object` ([DataProtectionOfficer](tilt-schema-properties-dataprotectionofficer.md))

## dataProtectionOfficer Examples

```json
{
  "name": "Jane Super",
  "address": "Wolfsburger Ring 2, 38440 Berlin",
  "country": "DE",
  "email": "contact@greencompany.de",
  "phone": "0049 151 1234 5678"
}
```

# DataProtectionOfficer Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                             |
| :-------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-name.md "\#/properties/dataProtectionOfficer/properties/name#/properties/dataProtectionOfficer/properties/name")          |
| [address](#address)   | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-address.md "\#/properties/dataProtectionOfficer/properties/address#/properties/dataProtectionOfficer/properties/address") |
| [country](#country)   | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-country.md "\#/properties/dataProtectionOfficer/properties/country#/properties/dataProtectionOfficer/properties/country") |
| [email](#email)       | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-email.md "\#/properties/dataProtectionOfficer/properties/email#/properties/dataProtectionOfficer/properties/email")       |
| [phone](#phone)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-phone.md "\#/properties/dataProtectionOfficer/properties/phone#/properties/dataProtectionOfficer/properties/phone")       |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                        |

## name

The full name of the Data Protection Officer.


`name`

-   is required
-   Type: `string` ([Name](tilt-schema-properties-dataprotectionofficer-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-name.md "\#/properties/dataProtectionOfficer/properties/name#/properties/dataProtectionOfficer/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-dataprotectionofficer-properties-name.md))

### name Examples

```json
"Jane Super"
```

## address

Address of the DPO.


`address`

-   is required
-   Type: `string` ([Address](tilt-schema-properties-dataprotectionofficer-properties-address.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-address.md "\#/properties/dataProtectionOfficer/properties/address#/properties/dataProtectionOfficer/properties/address")

### address Type

`string` ([Address](tilt-schema-properties-dataprotectionofficer-properties-address.md))

### address Examples

```json
"Wolfsburger Ring 2, 38440 Berlin"
```

## country

The country in which the Data Protection officer is located at.


`country`

-   is required
-   Type: `string` ([Country](tilt-schema-properties-dataprotectionofficer-properties-country.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-country.md "\#/properties/dataProtectionOfficer/properties/country#/properties/dataProtectionOfficer/properties/country")

### country Type

`string` ([Country](tilt-schema-properties-dataprotectionofficer-properties-country.md))

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
"DE"
```

## email

The contact email address of the Data Protection Officer.


`email`

-   is required
-   Type: `string` ([Email](tilt-schema-properties-dataprotectionofficer-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-email.md "\#/properties/dataProtectionOfficer/properties/email#/properties/dataProtectionOfficer/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-dataprotectionofficer-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## phone

The phone number of the Data Protection Officer (may include country prefix).


`phone`

-   is optional
-   Type: `string` ([Phone](tilt-schema-properties-dataprotectionofficer-properties-phone.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer-properties-phone.md "\#/properties/dataProtectionOfficer/properties/phone#/properties/dataProtectionOfficer/properties/phone")

### phone Type

`string` ([Phone](tilt-schema-properties-dataprotectionofficer-properties-phone.md))

### phone Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%2B%5D*%5B(%5D%7B0%2C1%7D%5B0-9%5D%7B1%2C4%7D%5B)%5D%7B0%2C1%7D%5B-%5Cs%5C.%2F0-9%5D*%24 "try regular expression with regexr.com")

### phone Examples

```json
"0049 151 1234 5678"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
