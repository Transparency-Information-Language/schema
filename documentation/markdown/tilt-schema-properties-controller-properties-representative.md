# Representative Schema

```txt
#/properties/controller/properties/representative#/properties/controller/properties/representative
```

The representative is a responsible real person that represents the controller.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## representative Type

`object` ([Representative](tilt-schema-properties-controller-properties-representative.md))

## representative Examples

```json
{
  "name": "Jane Super",
  "email": "contact@greencompany.de",
  "phone": "0049 151 1234 5678"
}
```

# Representative Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                    |
| :-------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-name.md "\#/properties/controller/properties/representative/properties/name#/properties/controller/properties/representative/properties/name")    |
| [email](#email)       | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-email.md "\#/properties/controller/properties/representative/properties/email#/properties/controller/properties/representative/properties/email") |
| [phone](#phone)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-phone.md "\#/properties/controller/properties/representative/properties/phone#/properties/controller/properties/representative/properties/phone") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                               |

## name

Name of the controller's representative.


`name`

-   is required
-   Type: `string` ([Name](tilt-schema-properties-controller-properties-representative-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-name.md "\#/properties/controller/properties/representative/properties/name#/properties/controller/properties/representative/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-controller-properties-representative-properties-name.md))

### name Examples

```json
"Jane Super"
```

## email

Email address of the controller's representative.


`email`

-   is required
-   Type: `string` ([Email](tilt-schema-properties-controller-properties-representative-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-email.md "\#/properties/controller/properties/representative/properties/email#/properties/controller/properties/representative/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-controller-properties-representative-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@greencompany.de"
```

## phone

Phone number of the controller's representative.


`phone`

-   is optional
-   Type: `string` ([Phone](tilt-schema-properties-controller-properties-representative-properties-phone.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller-properties-representative-properties-phone.md "\#/properties/controller/properties/representative/properties/phone#/properties/controller/properties/representative/properties/phone")

### phone Type

`string` ([Phone](tilt-schema-properties-controller-properties-representative-properties-phone.md))

### phone Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%2B%5D*%5B(%5D%7B0%2C1%7D%5B0-9%5D%7B1%2C4%7D%5B)%5D%7B0%2C1%7D%5B-%5Cs%5C.%2F0-9%5D*%24 "try regular expression with regexr.com")

### phone Examples

```json
"+49 151 1234 5678"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
