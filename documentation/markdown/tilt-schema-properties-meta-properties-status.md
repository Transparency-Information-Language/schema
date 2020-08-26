# Status Schema

```txt
#/properties/meta/properties/status#/properties/meta/properties/status
```

The status of an instance can be active or inactive depending on the policy's legal force.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## status Type

`string` ([Status](tilt-schema-properties-meta-properties-status.md))

## status Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(active|inactive)$
```

[try pattern](https://regexr.com/?expression=%5E(active%7Cinactive)%24 "try regular expression with regexr.com")

## status Default Value

The default value is:

```json
"active"
```

## status Examples

```json
"active"
```

```json
"inactive"
```
