# AdequacyDecision Schema

```txt
#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## adequacyDecision Type

`object` ([AdequacyDecision](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision.md))

## adequacyDecision Examples

```json
{
  "available": true,
  "description": "An adequacy decision was made on the 23rd April 2020 by..."
}
```

# AdequacyDecision Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [available](#available)     | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/available")       |
| [description](#description) | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/description") |
| Additional Properties       | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                             |

## available

Adequacy decision by the European commission exists?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-available.md))

### available Examples

```json
true
```

```json
false
```

## description

Description of the adequacy decision by the European commission.


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision-properties-description.md))

### description Examples

```json
"An adequacy decision was made on the 23rd April 2020 by..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
