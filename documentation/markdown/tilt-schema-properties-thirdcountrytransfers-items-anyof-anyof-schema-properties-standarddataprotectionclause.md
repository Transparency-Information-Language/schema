# StandardDataProtectionClause Schema

```txt
#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause
```

Schema on Standard Data Protection clauses.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## standardDataProtectionClause Type

`object` ([StandardDataProtectionClause](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause.md))

## standardDataProtectionClause Examples

```json
{
  "available": true,
  "description": "The standard data protection clause which applies here can be found here: ..."
}
```

# StandardDataProtectionClause Properties

| Property                    | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [available](#available)     | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/available")       |
| [description](#description) | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/description") |
| Additional Properties       | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                                 |

## available

Does a standard data protection clause exist?


`available`

-   is optional
-   Type: `boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-available.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-available.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/available#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/available")

### available Type

`boolean` ([Available](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-available.md))

### available Examples

```json
true
```

```json
false
```

## description

An explanation about the standard data protection clause (may include link).


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-description.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/description#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause-properties-description.md))

### description Examples

```json
"The standard data protection clause which applies here can be found here: ..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
