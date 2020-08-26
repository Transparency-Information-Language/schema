# AnyOf schema Schema

```txt
#/properties/thirdCountryTransfers/items/anyOf/0#/properties/thirdCountryTransfers/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema.md))

## 0 Examples

```json
{
  "country": "ES",
  "adequacyDecision": {
    "available": true,
    "description": "An adequacy decision was made on the 23rd April 2020 by..."
  },
  "appropriateGuarantees": {
    "available": true,
    "description": "Here the appropriate guarantee was formulated by..."
  },
  "presenceOfEnforceableRightsAndEffectiveRemedies": {
    "available": true,
    "description": "These rights are given because of..."
  },
  "standardDataProtectionClause": {
    "available": true,
    "description": "The standard data protection clause which applies here can be found here: ..."
  }
}
```

# AnyOf schema Properties

| Property                                                                                            | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                          |
| :-------------------------------------------------------------------------------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [country](#country)                                                                                 | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-country.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/country#/properties/thirdCountryTransfers/items/anyOf/0/properties/country")                                                                                                                         |
| [adequacyDecision](#adequacyDecision)                                                               | `object` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision")                                                                                              |
| [appropriateGuarantees](#appropriateGuarantees)                                                     | `object` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees")                                                                               |
| [presenceOfEnforceableRightsAndEffectiveRemedies](#presenceOfEnforceableRightsAndEffectiveRemedies) | `object` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-presenceofenforceablerightsandeffectiveremedies.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/presenceOfEnforceableRightsAndEffectiveRemedies#/properties/thirdCountryTransfers/items/anyOf/0/properties/presenceOfEnforceableRightsAndEffectiveRemedies") |
| [standardDataProtectionClause](#standardDataProtectionClause)                                       | `object` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause")                                                          |
| Additional Properties                                                                               | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                     |

## country

The country code of the third country.


`country`

-   is optional
-   Type: `string` ([Country](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-country.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-country.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/country#/properties/thirdCountryTransfers/items/anyOf/0/properties/country")

### country Type

`string` ([Country](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-country.md))

### country Constraints

**maximum length**: the maximum number of characters for this string is: `2`

**minimum length**: the minimum number of characters for this string is: `2`

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z][A-Z]$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D%5BA-Z%5D%24 "try regular expression with regexr.com")

### country Examples

```json
"ES"
```

## adequacyDecision




`adequacyDecision`

-   is optional
-   Type: `object` ([AdequacyDecision](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision#/properties/thirdCountryTransfers/items/anyOf/0/properties/adequacyDecision")

### adequacyDecision Type

`object` ([AdequacyDecision](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-adequacydecision.md))

### adequacyDecision Examples

```json
{
  "available": true,
  "description": "An adequacy decision was made on the 23rd April 2020 by..."
}
```

## appropriateGuarantees

Suitable guarantees according to Art. 45


`appropriateGuarantees`

-   is optional
-   Type: `object` ([AppropriateGuarantees](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees#/properties/thirdCountryTransfers/items/anyOf/0/properties/appropriateGuarantees")

### appropriateGuarantees Type

`object` ([AppropriateGuarantees](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-appropriateguarantees.md))

### appropriateGuarantees Examples

```json
{
  "available": true,
  "description": "Here the appropriate guarantee was formulated by..."
}
```

## presenceOfEnforceableRightsAndEffectiveRemedies

Presence of enforceable rights and effective remedies


`presenceOfEnforceableRightsAndEffectiveRemedies`

-   is optional
-   Type: `object` ([PresenceOfEnforceableRightsAndEffectiveRemedies](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-presenceofenforceablerightsandeffectiveremedies.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-presenceofenforceablerightsandeffectiveremedies.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/presenceOfEnforceableRightsAndEffectiveRemedies#/properties/thirdCountryTransfers/items/anyOf/0/properties/presenceOfEnforceableRightsAndEffectiveRemedies")

### presenceOfEnforceableRightsAndEffectiveRemedies Type

`object` ([PresenceOfEnforceableRightsAndEffectiveRemedies](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-presenceofenforceablerightsandeffectiveremedies.md))

### presenceOfEnforceableRightsAndEffectiveRemedies Examples

```json
{
  "available": true,
  "description": "These rights are given because of..."
}
```

## standardDataProtectionClause

Schema on Standard Data Protection clauses.


`standardDataProtectionClause`

-   is optional
-   Type: `object` ([StandardDataProtectionClause](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause.md "\#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause#/properties/thirdCountryTransfers/items/anyOf/0/properties/standardDataProtectionClause")

### standardDataProtectionClause Type

`object` ([StandardDataProtectionClause](tilt-schema-properties-thirdcountrytransfers-items-anyof-anyof-schema-properties-standarddataprotectionclause.md))

### standardDataProtectionClause Examples

```json
{
  "available": true,
  "description": "The standard data protection clause which applies here can be found here: ..."
}
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
