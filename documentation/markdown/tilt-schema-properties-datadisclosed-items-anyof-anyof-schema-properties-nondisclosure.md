# NonDisclosure Schema

```txt
#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure
```

This schema refers to the necessity and consequences of non-disclosure of personal data. According to Art. 13 (2e), this refers to the information whether the provision of the personal data is required by law or contract or is required for the conclusion of a contract, whether the data subject is obliged to provide the personal data and the possible consequences of not providing it.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## nonDisclosure Type

`object` ([NonDisclosure](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure.md))

## nonDisclosure Examples

```json
{
  "legalRequirement": false,
  "contractualRegulation": false,
  "obligationToProvide": false,
  "consequences": "If the data is not disclosed, the shipment cannot be delivered."
}
```

# NonDisclosure Properties

| Property                                        | Type      | Required | Nullable       | Defined by                                                                                                                                                                                                                                                                                                                                                                               |
| :---------------------------------------------- | --------- | -------- | -------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [legalRequirement](#legalRequirement)           | `boolean` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-legalrequirement.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/legalRequirement#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/legalRequirement")                |
| [contractualRegulation](#contractualRegulation) | `boolean` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-contractualregulation.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/contractualRegulation#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/contractualRegulation") |
| [obligationToProvide](#obligationToProvide)     | `boolean` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-obligationtoprovide.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/obligationToProvide#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/obligationToProvide")       |
| [consequences](#consequences)                   | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-consequences.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/consequences#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/consequences")                            |
| Additional Properties                           | Any       | Optional | can be null    |                                                                                                                                                                                                                                                                                                                                                                                          |

## legalRequirement

Is there a legal requirement to collect these data?


`legalRequirement`

-   is required
-   Type: `boolean` ([LegalRequirement](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-legalrequirement.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-legalrequirement.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/legalRequirement#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/legalRequirement")

### legalRequirement Type

`boolean` ([LegalRequirement](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-legalrequirement.md))

### legalRequirement Examples

```json
false
```

```json
true
```

## contractualRegulation

Is there a contractual regulation to collect these data?


`contractualRegulation`

-   is required
-   Type: `boolean` ([ContractualRegulation](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-contractualregulation.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-contractualregulation.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/contractualRegulation#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/contractualRegulation")

### contractualRegulation Type

`boolean` ([ContractualRegulation](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-contractualregulation.md))

### contractualRegulation Examples

```json
false
```

```json
true
```

## obligationToProvide

Is there an obligation for the data subject to provide these data?


`obligationToProvide`

-   is required
-   Type: `boolean` ([ObligationToProvide](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-obligationtoprovide.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-obligationtoprovide.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/obligationToProvide#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/obligationToProvide")

### obligationToProvide Type

`boolean` ([ObligationToProvide](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-obligationtoprovide.md))

### obligationToProvide Examples

```json
false
```

```json
true
```

## consequences

Description of the consequences in the case of non-disclosure.


`consequences`

-   is required
-   Type: `string` ([Consequences](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-consequences.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-consequences.md "\#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/consequences#/properties/dataDisclosed/items/anyOf/0/properties/nonDisclosure/properties/consequences")

### consequences Type

`string` ([Consequences](tilt-schema-properties-datadisclosed-items-anyof-anyof-schema-properties-nondisclosure-properties-consequences.md))

### consequences Examples

```json
"If the data is not disclosed, the shipment cannot be delivered."
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
