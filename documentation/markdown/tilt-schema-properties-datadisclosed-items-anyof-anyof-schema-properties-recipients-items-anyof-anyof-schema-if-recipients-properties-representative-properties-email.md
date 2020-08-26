# Email Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/representative/properties/email
```

The email address of the representative of the third party (recipient).


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## email Type

`string` ([Email](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-representative-properties-email.md))

## email Constraints

**email**: the string must be an email address, according to [RFC 5322, section 3.4.1](https://tools.ietf.org/html/rfc5322 "check the specification")

## email Examples

```json
"contact@yellowcompany.de"
```
