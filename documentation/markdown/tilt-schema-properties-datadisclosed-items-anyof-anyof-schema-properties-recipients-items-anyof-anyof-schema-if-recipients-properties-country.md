# Country Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/0/properties/country
```

The country in which the recipient is located at. Attention: This explictly specifies third country transfers!


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## country Type

`string` ([Country](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-anyof-schema-if-recipients-properties-country.md))

## country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z][A-Z]$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D%5BA-Z%5D%24 "try regular expression with regexr.com")

## country Examples

```json
"ES"
```
