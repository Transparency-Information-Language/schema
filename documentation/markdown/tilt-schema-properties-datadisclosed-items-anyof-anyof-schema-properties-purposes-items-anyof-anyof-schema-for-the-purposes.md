# AnyOf schema for the purposes. Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema for the purposes.](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes.md))

## 0 Examples

```json
{
  "purpose": "Marketing",
  "description": "Newsletter will be sent out once a month."
}
```

# AnyOf schema for the purposes. Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                        |
| :-------------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [purpose](#purpose)         | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-purpose.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/purpose#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/purpose")             |
| [description](#description) | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-description.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/description#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/description") |
| Additional Properties       | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                   |

## purpose

In this schema the purpose is specified (i.e. a headline or purpose category).


`purpose`

-   is required
-   Type: `string` ([Purpose](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-purpose.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-purpose.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/purpose#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/purpose")

### purpose Type

`string` ([Purpose](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-purpose.md))

### purpose Examples

```json
"Marketing"
```

## description

This schema refers to an exact description of the purpose the data is processed for.


`description`

-   is required
-   Type: `string` ([Description](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-description.md "\#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/description#/properties/dataDisclosed/items/anyOf/0/properties/purposes/items/anyOf/0/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-purposes-items-anyof-anyof-schema-for-the-purposes-properties-description.md))

### description Examples

```json
"Newsletter will be sent out once a month."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
