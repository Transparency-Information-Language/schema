# Modified Schema

```txt
#/properties/meta/properties/modified#/properties/meta/properties/modified
```

Last modified date of the document as an ISO-8601 time code.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## modified Type

`string` ([Modified](tilt-schema-properties-meta-properties-modified.md))

## modified Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
```

[try pattern](https://regexr.com/?expression=%5E(%5B%5C%2B-%5D%3F%5Cd%7B4%7D(%3F!%5Cd%7B2%7D%5Cb))((-%3F)((0%5B1-9%5D%7C1%5B0-2%5D)(%5C3(%5B12%5D%5Cd%7C0%5B1-9%5D%7C3%5B01%5D))%3F%7CW(%5B0-4%5D%5Cd%7C5%5B0-2%5D)(-%3F%5B1-7%5D)%3F%7C(00%5B1-9%5D%7C0%5B1-9%5D%5Cd%7C%5B12%5D%5Cd%7B2%7D%7C3(%5B0-5%5D%5Cd%7C6%5B1-6%5D)))(%5BT%5Cs%5D(((%5B01%5D%5Cd%7C2%5B0-3%5D)((%3A%3F)%5B0-5%5D%5Cd)%3F%7C24%5C%3A%3F00)(%5B%5C.%2C%5D%5Cd%2B(%3F!%3A))%3F)%3F(%5C17%5B0-5%5D%5Cd(%5B%5C.%2C%5D%5Cd%2B)%3F)%3F(%5BzZ%5D%7C(%5B%5C%2B-%5D)(%5B01%5D%5Cd%7C2%5B0-3%5D)%3A%3F(%5B0-5%5D%5Cd)%3F)%3F)%3F)%3F%24 "try regular expression with regexr.com")

## modified Examples

```json
"2020-04-03T15: 53: 05.929588"
```
