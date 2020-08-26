# Second anyOf Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 1 Type

`object` ([Second anyOf](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-second-anyof.md))

## 1 Examples

```json
{
  "category": "Responsible Statistical Institutes"
}
```

# Second anyOf Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                    |
| :-------------------- | -------- | -------- | -------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [category](#category) | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-second-anyof-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1/properties/category") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                               |

## category

This category has to be given, even if the controller is not mentioned explicitly.


`category`

-   is required
-   Type: `string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-second-anyof-properties-category.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-second-anyof-properties-category.md "\#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1/properties/category#/properties/dataDisclosed/items/anyOf/0/properties/recipients/items/anyOf/1/properties/category")

### category Type

`string` ([Category](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-recipients-items-anyof-second-anyof-properties-category.md))

### category Examples

```json
"Responsible Statistical Institutes"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
