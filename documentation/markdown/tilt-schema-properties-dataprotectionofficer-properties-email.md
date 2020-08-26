# Email Schema

```txt
#/properties/dataProtectionOfficer/properties/email#/properties/dataProtectionOfficer/properties/email
```

The contact email address of the Data Protection Officer.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## email Type

`string` ([Email](tilt-schema-properties-dataprotectionofficer-properties-email.md))

## email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## email Examples

```json
"contact@greencompany.de"
```
