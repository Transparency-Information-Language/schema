# Country Schema

```txt
#/properties/controller/properties/country#/properties/controller/properties/country
```

All country codes follow the established ones ISO 3166 country abbreviation standard.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## country Type

`string` ([Country](tilt-schema-properties-controller-properties-country.md))

## country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z][A-Z]$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D%5BA-Z%5D%24 "try regular expression with regexr.com")

## country Default Value

The default value is:

```json
"DE"
```

## country Examples

```json
"DE"
```
