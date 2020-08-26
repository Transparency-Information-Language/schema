# Representative Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative
```

The representative of the third party (recipient).


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## representative Type

`object` ([Representative](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative.md))

## representative Examples

```json
{
  "name": "Jane Super",
  "email": "contact@yellowcompany.de",
  "phone": "0049 151 1234 9876"
}
```

# Representative Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-name.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/name#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/name")    |
| [email](#email)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-email.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email") |
| [phone](#phone)       | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-phone.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/phone#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/phone") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## name

The name of the representative of the third party (recipient).


`name`

-   is optional
-   Type: `string` ([Name](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-name.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/name#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-name.md))

### name Examples

```json
"Jane Super"
```

## email

The email address of the representative of the third party (recipient).


`email`

-   is optional
-   Type: `string` ([Email](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-email.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-email.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email")

### email Type

`string` ([Email](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-email.md))

### email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

### email Examples

```json
"contact@yellowcompany.de"
```

## phone

The phone number of the representative of the third party (recipient).


`phone`

-   is optional
-   Type: `string` ([Phone](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-phone.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-phone.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/phone#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/phone")

### phone Type

`string` ([Phone](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-phone.md))

### phone Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%2B%5D*%5B(%5D%7B0%2C1%7D%5B0-9%5D%7B1%2C4%7D%5B)%5D%7B0%2C1%7D%5B-%5Cs%5C.%2F0-9%5D*%24 "try regular expression with regexr.com")

### phone Examples

```json
"0049 151 1234 9876"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
