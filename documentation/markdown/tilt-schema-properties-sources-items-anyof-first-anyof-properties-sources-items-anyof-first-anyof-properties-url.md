# Url Schema

```txt
#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url
```

URL (reference) where the data is taken from.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## url Type

`string` ([Url](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-url.md))

## url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

## url Examples

```json
"https://blueCompany.org"
```
