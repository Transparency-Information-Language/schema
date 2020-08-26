# AggregationFunction Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction#/properties/dataDisclosed/items/anyOf/0/properties/storage/items/anyOf/0/properties/aggregationFunction
```

The aggregation function describes the calculation basis when specifying several time intervals. For example, if there is storage for 2 weeks for technical reasons (e.g. backup), but there is a legally longer retention period, the maximum aggregation function (max) would be selected (standard case). Aggregation functions available: min, max, sum, avg


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## aggregationFunction Type

`string` ([AggregationFunction](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-storage-items-anyof-first-anyof-properties-aggregationfunction.md))

## aggregationFunction Constraints

**enum**: the value of this property must be equal to one of the following values:

| Value   | Explanation |
| :------ | ----------- |
| `"min"` |             |
| `"max"` |             |
| `"sum"` |             |
| `"avg"` |             |

## aggregationFunction Default Value

The default value is:

```json
"max"
```

## aggregationFunction Examples

```json
"max"
```
