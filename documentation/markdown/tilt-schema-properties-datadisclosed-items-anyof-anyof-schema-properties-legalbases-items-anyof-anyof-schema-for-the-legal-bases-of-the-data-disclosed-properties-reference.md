# Reference Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference
```

This field refers to the reference in legal regulations (laws, orders, declaration etc.). The format is set to uppercase letters for the legal text followed by hyphened numbers and lowercase letters for the exact location.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## reference Type

`string` ([Reference](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-reference.md))

## reference Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z]*([-]?[0-9]*|[a-z]*)*$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D*(%5B-%5D%3F%5B0-9%5D*%7C%5Ba-z%5D*)*%24 "try regular expression with regexr.com")

## reference Examples

```json
"GDPR-99-1-a"
```
