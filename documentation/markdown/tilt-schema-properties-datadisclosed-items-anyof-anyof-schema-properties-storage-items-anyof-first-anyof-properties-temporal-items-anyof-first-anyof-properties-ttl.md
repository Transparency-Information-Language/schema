# Ttl Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal/items/anyOf/0/properties/ttl#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/temporal/items/anyOf/0/properties/ttl
```

The TTL (Time-to-Live) specifies the lifetime of this data (category). It follows the ISO 8601 for time spans.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## ttl Type

`string` ([Ttl](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-temporal-items-anyof-first-anyof-properties-ttl.md))

## ttl Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(\d{4}(-\d{2}(-\d{2})?(?!:))?(T\d{2}(:\d{2}(:\d{2})?(\.\d+)?)?)?(Z|([+,-]\d{2}(:\d{2})?))?)?P(([0-9]+([.,][0-9]*)?Y)?([0-9]+([.,][0-9]*)?M)?([0-9]+([.,][0-9]*)?D)?T?([0-9]+([.,][0-9]*)?H)?([0-9]+([.,][0-9]*)?M)?([0-9]+([.,][0-9]*)?S)?)|\d{4}-?(0[1-9]|11|12)-?(?:[0-2]\d|30|31)T((?:[0-1][0-9]|[2][0-3]):?(?:[0-5][0-9]):?(?:[0-5][0-9]|60)|2400|24:00)$
```

[try pattern](https://regexr.com/?expression=%5E(%5Cd%7B4%7D(-%5Cd%7B2%7D(-%5Cd%7B2%7D)%3F(%3F!%3A))%3F(T%5Cd%7B2%7D(%3A%5Cd%7B2%7D(%3A%5Cd%7B2%7D)%3F(%5C.%5Cd%2B)%3F)%3F)%3F(Z%7C(%5B%2B%2C-%5D%5Cd%7B2%7D(%3A%5Cd%7B2%7D)%3F))%3F)%3FP((%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FY)%3F(%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FM)%3F(%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FD)%3FT%3F(%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FH)%3F(%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FM)%3F(%5B0-9%5D%2B(%5B.%2C%5D%5B0-9%5D*)%3FS)%3F)%7C%5Cd%7B4%7D-%3F(0%5B1-9%5D%7C11%7C12)-%3F(%3F%3A%5B0-2%5D%5Cd%7C30%7C31)T((%3F%3A%5B0-1%5D%5B0-9%5D%7C%5B2%5D%5B0-3%5D)%3A%3F(%3F%3A%5B0-5%5D%5B0-9%5D)%3A%3F(%3F%3A%5B0-5%5D%5B0-9%5D%7C60)%7C2400%7C24%3A00)%24 "try regular expression with regexr.com")

## ttl Examples

```json
"2005-08-09T18:31:42P3Y6M4DT12H30M17S"
```
