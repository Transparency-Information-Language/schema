# First anyOf Schema

```txt
#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0
```




| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## 0 Type

`object` ([First anyOf](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof.md))

## 0 Examples

```json
{
  "description": "This information could be retrieved from...",
  "url": "https://blueCompany.org",
  "publiclyAvailable": false
}
```

# First anyOf Properties

| Property                                | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                                  |
| :-------------------------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [description](#description)             | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-description.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/description#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/description")                   |
| [url](#url)                             | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-url.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url")                                           |
| [publiclyAvailable](#publiclyAvailable) | `boolean` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-publiclyavailable.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/publiclyAvailable#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/publiclyAvailable") |
| Additional Properties                   | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                             |

## description

Description of the source the data is taken from.


`description`

-   is required
-   Type: `string` ([Description](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-description.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-description.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/description#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/description")

### description Type

`string` ([Description](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-description.md))

### description Examples

```json
"This information could be retrieved from..."
```

## url

URL (reference) where the data is taken from.


`url`

-   is required
-   Type: `string` ([Url](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-url.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://blueCompany.org"
```

## publiclyAvailable

Are these data publicly available?


`publiclyAvailable`

-   is required
-   Type: `boolean` ([PubliclyAvailable](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-publiclyavailable.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-publiclyavailable.md "\#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/publiclyAvailable#/properties/sources/items/anyOf/0/properties/sources/items/anyOf/0/properties/publiclyAvailable")

### publiclyAvailable Type

`boolean` ([PubliclyAvailable](tilt-schema-properties-sources-items-anyof-first-anyof-properties-sources-items-anyof-first-anyof-properties-publiclyavailable.md))

### publiclyAvailable Examples

```json
false
```

```json
true
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
