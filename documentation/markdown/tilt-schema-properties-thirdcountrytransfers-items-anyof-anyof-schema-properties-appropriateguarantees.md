# AppropriateGuarantees Schema

```txt
#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees
```

Suitable guarantees according to Art. 45


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## appropriateGuarantees Type

`object` ([AppropriateGuarantees](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees.md))

## appropriateGuarantees Examples

```json
{
  "available": true,
  "description": "Here the appropriate guarantee was formulated by..."
}
```

# AppropriateGuarantees Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                 |
| :-------------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [available](#available)     | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/available")       |
| [description](#description) | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/description") |
| Additional Properties       | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                            |

## available

Do suitable guarantees according to Art. 45 exist?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-available.md))

### available Examples

```json
true
```

```json
false
```

## description

Description of suitable guarantees according to Art. 45


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees-properties-description.md))

### description Examples

```json
"Here the appropriate guarantee was formulated by..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
