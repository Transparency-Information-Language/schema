# Phone Schema

```txt
#/properties/dataProtectionOfficer/properties/phone#/properties/dataProtectionOfficer/properties/phone
```

The phone number of the Data Protection Officer (may include country prefix).


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## phone Type

`string` ([Phone](tilt-schema-properties-dataprotectionofficer-properties-phone.md))

## phone Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$
```

[try pattern](https://regexr.com/?expression=%5E%5B%2B%5D*%5B(%5D%7B0%2C1%7D%5B0-9%5D%7B1%2C4%7D%5B)%5D%7B0%2C1%7D%5B-%5Cs%5C.%2F0-9%5D*%24 "try regular expression with regexr.com")

## phone Examples

```json
"0049 151 1234 5678"
```
