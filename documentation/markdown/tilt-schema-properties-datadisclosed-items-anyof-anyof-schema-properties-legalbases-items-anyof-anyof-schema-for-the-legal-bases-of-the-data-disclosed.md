# AnyOf schema for the legal bases of the data disclosed. Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([AnyOf schema for the legal bases of the data disclosed.](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed.md))

## 0 Examples

```json
{
  "reference": "GDPR-99-1-a",
  "description": "The data are processed on the basis of Art. 99 GDPR which states..."
}
```

# AnyOf schema for the legal bases of the data disclosed. Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-------------------------- | -------- | -------- | -------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [reference](#reference)     | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-reference.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference")       |
| [description](#description) | `string` | Optional | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-description.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/description#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/description") |
| Additional Properties       | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## reference

This field refers to the reference in legal regulations (laws, orders, declaration etc.). The format is set to uppercase letters for the legal text followed by hyphened numbers and lowercase letters for the exact location.


`reference`

-   is required
-   Type: `string` ([Reference](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-reference.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-reference.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/reference")

### reference Type

`string` ([Reference](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-reference.md))

### reference Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^[A-Z]*([-]?[0-9]*|[a-z]*)*$
```

[try pattern](https://regexr.com/?expression=%5E%5BA-Z%5D*(%5B-%5D%3F%5B0-9%5D*%7C%5Ba-z%5D*)*%24 "try regular expression with regexr.com")

### reference Examples

```json
"GDPR-99-1-a"
```

## description

An explanation about the legal basis used.


`description`

-   is optional
-   Type: `string` ([Description](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-description.md "\#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/description#/properties/dataDisclosed/items/anyOf/0/properties/legalBases/items/anyOf/0/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-legalbases-items-anyof-anyof-schema-for-the-legal-bases-of-the-data-disclosed-properties-description.md))

### description Examples

```json
"The data are processed on the basis of Art. 99 GDPR which states..."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
