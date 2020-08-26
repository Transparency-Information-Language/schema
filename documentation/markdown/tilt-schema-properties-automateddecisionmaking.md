# AutomatedDecisionMaking Schema

```txt
#/properties/automatedDecisionMaking#/properties/automatedDecisionMaking
```

Automated decision making and potentially involved logic. Does include profiling.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## automatedDecisionMaking Type

`object` ([AutomatedDecisionMaking](tilt-schema-properties-automateddecisionmaking.md))

## automatedDecisionMaking Examples

```json
{
  "inUse": true,
  "logicInvolved": "The personal data are processed as follows...",
  "scopeAndIntendedEffects": "From processing follows..."
}
```

# AutomatedDecisionMaking Properties

| Property                                            | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                   |
| :-------------------------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [inUse](#inUse)                                     | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-inuse.md "\#/properties/automatedDecisionMaking/properties/inUse#/properties/automatedDecisionMaking/properties/inUse")                                                       |
| [logicInvolved](#logicInvolved)                     | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-logicinvolved.md "\#/properties/automatedDecisionMaking/properties/logicInvolved#/properties/automatedDecisionMaking/properties/logicInvolved")                               |
| [scopeAndIntendedEffects](#scopeAndIntendedEffects) | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-scopeandintendedeffects.md "\#/properties/automatedDecisionMaking/properties/scopeAndIntendedEffects#/properties/automatedDecisionMaking/properties/scopeAndIntendedEffects") |
| Additional Properties                               | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                              |

## inUse

Is automated decision making in use?


`inUse`

-   is optional
-   Type: `boolean` ([InUse](tilt-schema-properties-automateddecisionmaking-properties-inuse.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-inuse.md "\#/properties/automatedDecisionMaking/properties/inUse#/properties/automatedDecisionMaking/properties/inUse")

### inUse Type

`boolean` ([InUse](tilt-schema-properties-automateddecisionmaking-properties-inuse.md))

### inUse Default Value

The default value is:

```json
true
```

### inUse Examples

```json
true
```

```json
false
```

## logicInvolved

An explanation about the logic involved to automated decision making.


`logicInvolved`

-   is optional
-   Type: `string` ([LogicInvolved](tilt-schema-properties-automateddecisionmaking-properties-logicinvolved.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-logicinvolved.md "\#/properties/automatedDecisionMaking/properties/logicInvolved#/properties/automatedDecisionMaking/properties/logicInvolved")

### logicInvolved Type

`string` ([LogicInvolved](tilt-schema-properties-automateddecisionmaking-properties-logicinvolved.md))

### logicInvolved Examples

```json
"The personal data are processed as follows..."
```

## scopeAndIntendedEffects

Scope and intended effects of such processing for the data subject.


`scopeAndIntendedEffects`

-   is optional
-   Type: `string` ([ScopeAndIntendedEffects](tilt-schema-properties-automateddecisionmaking-properties-scopeandintendedeffects.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking-properties-scopeandintendedeffects.md "\#/properties/automatedDecisionMaking/properties/scopeAndIntendedEffects#/properties/automatedDecisionMaking/properties/scopeAndIntendedEffects")

### scopeAndIntendedEffects Type

`string` ([ScopeAndIntendedEffects](tilt-schema-properties-automateddecisionmaking-properties-scopeandintendedeffects.md))

### scopeAndIntendedEffects Examples

```json
"From processing follows..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
