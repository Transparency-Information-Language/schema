# Country Schema

```txt
#/properties/thirdCountryTransfers/items/anyOf/0/properties/country#/properties/thirdCountryTransfers/items/anyOf/0/properties/country
```

The country code of the third country.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## country Type

`string` ([Country](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-country.md))

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
