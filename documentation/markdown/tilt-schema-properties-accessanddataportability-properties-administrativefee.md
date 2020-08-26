# AdministrativeFee Schema

```txt
#/properties/accessAndDataPortability/properties/administrativeFee#/properties/accessAndDataPortability/properties/administrativeFee
```

The fee that refers to several copies.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## administrativeFee Type

`object` ([AdministrativeFee](tilt-schema-properties-accessanddataportability-properties-administrativefee.md))

## administrativeFee Examples

```json
{
  "amount": 0,
  "currency": "EUR"
}
```

# AdministrativeFee Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                |
| :-------------------- | -------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [amount](#amount)     | `number` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-amount.md "\#/properties/accessAndDataPortability/properties/administrativeFee/properties/amount#/properties/accessAndDataPortability/properties/administrativeFee/properties/amount")       |
| [currency](#currency) | `string` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-currency.md "\#/properties/accessAndDataPortability/properties/administrativeFee/properties/currency#/properties/accessAndDataPortability/properties/administrativeFee/properties/currency") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                           |

## amount

The amount of money to be paid for a copy.


`amount`

-   is required
-   Type: `number` ([Amount](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-amount.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-amount.md "\#/properties/accessAndDataPortability/properties/administrativeFee/properties/amount#/properties/accessAndDataPortability/properties/administrativeFee/properties/amount")

### amount Type

`number` ([Amount](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-amount.md))

### amount Examples

```json
0
```

## currency

The currency in which the amount of money for one copy has to be provided acc. to ISO 4217.


`currency`

-   is required
-   Type: `string` ([Currency](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-currency.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-currency.md "\#/properties/accessAndDataPortability/properties/administrativeFee/properties/currency#/properties/accessAndDataPortability/properties/administrativeFee/properties/currency")

### currency Type

`string` ([Currency](tilt-schema-properties-accessanddataportability-properties-administrativefee-properties-currency.md))

### currency Constraints

**maximum length**: the maximum number of characters for this string is: `3`

**minimum length**: the minimum number of characters for this string is: `3`

### currency Default Value

The default value is:

```json
"EUR"
```

### currency Examples

```json
"EUR"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
