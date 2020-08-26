# AnyOf schema for legitimate interests. Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema for legitimate interests.](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests.md))

## 0 Examples

```json
{
  "exists": true,
  "reasoning": "There is an legitimate interest based on ... and is not overwritten because ..."
}
```

# AnyOf schema for legitimate interests. Properties

| Property                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [exists](#exists)       | `boolean` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-exists.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/exists#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/exists")          |
| [reasoning](#reasoning) | `string`  | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-reasoning.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/reasoning#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/reasoning") |
| Additional Properties   | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## exists

The legitimate interest only has to be stated if the processing is carried out in accordance with Art. 13 (1d). This field refers to the existence of such an interest.


`exists`

-   is optional
-   Type: `boolean` ([Exists](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-exists.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-exists.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/exists#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/exists")

### exists Type

`boolean` ([Exists](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-exists.md))

### exists Examples

```json
true
```

```json
false
```

## reasoning

If the legitimate interest has to be stated because the processing is carried out in accordance with Art. 13 (1d), it is described in here.


`reasoning`

-   is optional
-   Type: `string` ([Reasoning](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-reasoning.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-reasoning.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/reasoning#/properties/dataDisclosed/items/anyOf/0/properties/legitimateInterests/items/anyOf/0/properties/reasoning")

### reasoning Type

`string` ([Reasoning](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legitimateinterests-items-anyof-anyof-schema-for-legitimate-interests-properties-reasoning.md))

### reasoning Examples

```json
"There is an legitimate interest based on ... and is not overwritten because ..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
