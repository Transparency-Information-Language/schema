# Root schema of a Transparency Information Language Schema

```txt
https://github.com/Transparency-Information-Language/schema
```

This schema defines the Transparency Information Language


## Root schema of a Transparency Information Language Type

`object` ([Root schema of a Transparency Information Language](tilt-schema.md))

## Root schema of a Transparency Information Language Examples

```json
{
  "meta": {
    "_id": "f1424f86-ca0f-4f0c-9438-43cc00509931",
    "name": "Green Company",
    "created": "2020-04-03T15:53:05.929588",
    "modified": "2020-04-03T15: 53: 05.929588",
    "version": 2,
    "language": "de",
    "status": "active",
    "url": "https://green-bikes.de/privacy",
    "_hash": "d732a793562a3e5dc57645a8"
  },
  "controller": {
    "name": "Green Company AG",
    "division": "Product line e-mobility",
    "address": "Wolfsburger Ring 2, 38440 Berlin",
    "country": "DE",
    "representative": {
      "name": "Jane Super",
      "email": "contact@greencompany.de",
      "phone": "0049 151 1234 5678"
    }
  },
  "dataProtectionOfficer": {
    "name": "Jane Super",
    "address": "Wolfsburger Ring 2, 38440 Berlin",
    "country": "DE",
    "email": "contact@greencompany.de",
    "phone": "0049 151 1234 5678"
  },
  "dataDisclosed": [
    {
      "_id": "f1424f86-ca0f-4f0c-9438-43cc00509931",
      "category": "E-mail address",
      "purposes": [
        {
          "purpose": "Marketing",
          "description": "Newsletter will be sent out once a month."
        }
      ],
      "legalBases": [
        {
          "reference": "GDPR-99-1-a",
          "description": "The data are processed on the basis of Art. 99 GDPR which states..."
        },
        {
          "reference": "BDSG-42-5",
          "description": "BDSG-42-5 refers to the processing of personal data within..."
        }
      ],
      "legitimateInterests": [
        {
          "exists": true,
          "reasoning": "There is an legitimate interest based on ... and is not overwritten because ..."
        }
      ],
      "recipients": [
        {
          "name": "Yellow Company AG",
          "division": "Product line e-mobility",
          "address": "Triana 123, 9999 Seville",
          "country": "ES",
          "representative": {
            "name": "Jane Super",
            "email": "contact@yellowcompany.de",
            "phone": "0049 151 1234 9876"
          },
          "category": "Marketing content provider"
        },
        {
          "category": "Responsible Statistical Institutes"
        }
      ],
      "storage": [
        {
          "temporal": [
            {
              "description": "Creating backups.",
              "ttl": "2005-08-09T18:31:42P3Y6M4DT12H30M17S"
            },
            {
              "description": "Finishing ordering process.",
              "ttl": "2020-08-09T18:31:42P3Y6M4DT12H30M17S"
            }
          ],
          "purposeConditional": [
            "Data is stored until the end of the ordering process."
          ],
          "legalBasisConditional": [
            "SGB-100-42"
          ],
          "aggregationFunction": "max"
        }
      ],
      "nonDisclosure": {
        "legalRequirement": false,
        "contractualRegulation": false,
        "obligationToProvide": false,
        "consequences": "If the data is not disclosed, the shipment cannot be delivered."
      }
    }
  ],
  "thirdCountryTransfers": [
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
  ],
  "accessAndDataPortability": {
    "available": true,
    "description": "Data access is possible through...",
    "url": "https://green-bikes.de/access",
    "email": "access@greencompany.de",
    "identificationEvidences": [
      "ID card copy",
      "Email verification"
    ],
    "administrativeFee": {
      "amount": 0,
      "currency": "EUR"
    },
    "dataFormat": "json"
  },
  "sources": [
    {
      "_id": "f1423cc00509931",
      "dataCategory": "Creditworthiness",
      "sources": [
        {
          "description": "This information could be retrieved from...",
          "url": "https://blueCompany.org",
          "publiclyAvailable": false
        }
      ]
    }
  ],
  "rightToInformation": {
    "available": true,
    "description": "For the right to information please use this contact form and...",
    "url": "https://greencompany.org/rightToInformation",
    "email": "contact@greencompany.de",
    "identificationEvidences": [
      "ID card copy",
      "Email verification"
    ]
  },
  "rightToRectificationOrDeletion": {
    "available": true,
    "description": "For the right to rectification please use this contact form and...",
    "url": "https://greencompany.org/rights",
    "email": "contact@greencompany.de",
    "identificationEvidences": [
      "ID card copy",
      "Email verification"
    ]
  },
  "rightToDataPortability": {
    "available": false,
    "description": "Data portability is only possible when...",
    "url": "https://greencompany.org/rights",
    "email": "contact@greencompany.de",
    "identificationEvidences": [
      "ID card copy"
    ]
  },
  "rightToWithdrawConsent": {
    "available": true,
    "description": "For the right to withdraw consent please use this contact form and...",
    "url": "https://greencompany.org/rights",
    "email": "contact@greencompany.de",
    "identificationEvidences": [
      "Email verification"
    ]
  },
  "rightToComplain": {
    "available": true,
    "description": "For the right to complain please use this contact form and...",
    "url": "https://greencompany.org/rights",
    "email": "contact@greencompany.de",
    "identificationEvidences": [
      "ID card copy",
      "Email verification"
    ],
    "supervisoryAuthority": {
      "name": "Commissioner for Data Protection",
      "address": "Friedrichstrasse 219, 10969 Berlin",
      "country": "DE",
      "email": "mailbox@privacy-berlin.de",
      "phone": "0049 444 222 111"
    }
  },
  "automatedDecisionMaking": {
    "inUse": true,
    "logicInvolved": "The personal data are processed as follows...",
    "scopeAndIntendedEffects": "From processing follows..."
  },
  "changesOfPurpose": [
    {
      "description": "Due to techncial requirements...",
      "affectedDataCategories": [
        "Email adress",
        "Credit score"
      ],
      "plannedDateOfChange": "2020-08-20",
      "urlOfNewVersion": "https://greencomp.de/privacypolicy/2"
    }
  ]
}
```

# Root schema of a Transparency Information Language Properties

| Property                                                          | Type     | Required | Nullable       | Defined by                                                                                                                                                                                               |
| :---------------------------------------------------------------- | -------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [meta](#meta)                                                     | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta.md "\#/properties/meta#/properties/meta")                                                                               |
| [controller](#controller)                                         | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-controller.md "\#/properties/controller#/properties/controller")                                                             |
| [dataProtectionOfficer](#dataProtectionOfficer)                   | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer.md "\#/properties/dataProtectionOfficer#/properties/dataProtectionOfficer")                            |
| [dataDisclosed](#dataDisclosed)                                   | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed.md "\#/properties/dataDisclosed#/properties/dataDisclosed")                                                    |
| [thirdCountryTransfers](#thirdCountryTransfers)                   | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers.md "\#/properties/thirdCountryTransfers#/properties/thirdCountryTransfers")                            |
| [accessAndDataPortability](#accessAndDataPortability)             | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability.md "\#/properties/accessAndDataPortability#/properties/accessAndDataPortability")                   |
| [sources](#sources)                                               | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-sources.md "\#/properties/sources#/properties/sources")                                                                      |
| [rightToInformation](#rightToInformation)                         | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation.md "\#/properties/rightToInformation#/properties/rightToInformation")                                     |
| [rightToRectificationOrDeletion](#rightToRectificationOrDeletion) | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion.md "\#/properties/rightToRectificationOrDeletion#/properties/rightToRectificationOrDeletion") |
| [rightToDataPortability](#rightToDataPortability)                 | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability.md "\#/properties/rightToDataPortability#/properties/rightToDataPortability")                         |
| [rightToWithdrawConsent](#rightToWithdrawConsent)                 | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent.md "\#/properties/rightToWithdrawConsent#/properties/rightToWithdrawConsent")                         |
| [rightToComplain](#rightToComplain)                               | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain.md "\#/properties/rightToComplain#/properties/rightToComplain")                                              |
| [automatedDecisionMaking](#automatedDecisionMaking)               | `object` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking.md "\#/properties/automatedDecisionMaking#/properties/automatedDecisionMaking")                      |
| [changesOfPurpose](#changesOfPurpose)                             | `array`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose.md "\#/properties/changesOfPurpose#/properties/changesOfPurpose")                                           |
| Additional Properties                                             | Any      | Optional | can be null    |                                                                                                                                                                                                          |

## meta

Meta information for the identification and verification of the document.


`meta`

-   is required
-   Type: `object` ([Meta](tilt-schema-properties-meta.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta.md "\#/properties/meta#/properties/meta")

### meta Type

`object` ([Meta](tilt-schema-properties-meta.md))

### meta Examples

```json
{
  "_id": "f1424f86-ca0f-4f0c-9438-43cc00509931",
  "name": "Green Company",
  "created": "2020-04-03T15:53:05.929588",
  "modified": "2020-04-03T15: 53: 05.929588",
  "version": 2,
  "language": "de",
  "status": "active",
  "url": "https://green-bikes.de/privacy",
  "_hash": "d732a793562a3e5dc57645a8"
}
```

## controller

The responsible controller is defined in here.


`controller`

-   is required
-   Type: `object` ([Controller](tilt-schema-properties-controller.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-controller.md "\#/properties/controller#/properties/controller")

### controller Type

`object` ([Controller](tilt-schema-properties-controller.md))

### controller Examples

```json
{
  "name": "Green Company AG",
  "division": "Product line e-mobility",
  "address": "Wolfsburger Ring 2, 38440 Berlin",
  "country": "DE",
  "representative": {
    "name": "Jane Super",
    "email": "contact@greencompany.de",
    "phone": "0049 151 1234 5678"
  }
}
```

## dataProtectionOfficer

The Data Protection Officer (DPO) of the controller.


`dataProtectionOfficer`

-   is required
-   Type: `object` ([DataProtectionOfficer](tilt-schema-properties-dataprotectionofficer.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-dataprotectionofficer.md "\#/properties/dataProtectionOfficer#/properties/dataProtectionOfficer")

### dataProtectionOfficer Type

`object` ([DataProtectionOfficer](tilt-schema-properties-dataprotectionofficer.md))

### dataProtectionOfficer Examples

```json
{
  "name": "Jane Super",
  "address": "Wolfsburger Ring 2, 38440 Berlin",
  "country": "DE",
  "email": "contact@greencompany.de",
  "phone": "0049 151 1234 5678"
}
```

## dataDisclosed

A detailed explanation about which data is disclosed in the processing tasks.


`dataDisclosed`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-datadisclosed-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-datadisclosed.md "\#/properties/dataDisclosed#/properties/dataDisclosed")

### dataDisclosed Type

an array of merged types ([Details](tilt-schema-properties-datadisclosed-items.md))

### dataDisclosed Examples

```json
[
  {
    "_id": "f1424f86-ca0f-4f0c-9438-43cc00509931",
    "category": "E-mail address",
    "purposes": [
      {
        "purpose": "Marketing",
        "description": "Newsletter will be sent out once a month."
      }
    ],
    "legalBases": [
      {
        "reference": "GDPR-99-1-a",
        "description": "The data are processed on the basis of Art. 99 GDPR which states..."
      },
      {
        "reference": "BDSG-42-5",
        "description": "BDSG-42-5 refers to the processing of personal data within..."
      }
    ],
    "legitimateInterests": [
      {
        "exists": true,
        "reasoning": "There is an legitimate interest based on ... and is not overwritten because ..."
      }
    ],
    "recipients": [
      {
        "name": "Yellow Company AG",
        "division": "Product line e-mobility",
        "address": "Triana 123, 9999 Seville",
        "country": "ES",
        "representative": {
          "name": "Jane Super",
          "email": "contact@yellowcompany.de",
          "phone": "0049 151 1234 9876"
        },
        "category": "Marketing content provider"
      },
      {
        "category": "Responsible Statistical Institutes"
      }
    ],
    "storage": [
      {
        "temporal": [
          {
            "description": "Creating backups.",
            "ttl": "2005-08-09T18:31:42P3Y6M4DT12H30M17S"
          },
          {
            "description": "Finishing ordering process.",
            "ttl": "2020-07-12T18:31:42P3Y6M4DT12H30M17S"
          }
        ],
        "purposeConditional": [
          "Data is stored until the end of the ordering process."
        ],
        "legalBasisConditional": [
          "SGB-100-42"
        ],
        "aggregationFunction": "max"
      }
    ],
    "nonDisclosure": {
      "legalRequirement": false,
      "contractualRegulation": false,
      "obligationToProvide": false,
      "consequences": "If the data is not disclosed, the shipment cannot be delivered."
    }
  }
]
```

## thirdCountryTransfers

This schema refers to the adequacy decisions of any third country transfers.


`thirdCountryTransfers`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-thirdcountrytransfers-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-thirdcountrytransfers.md "\#/properties/thirdCountryTransfers#/properties/thirdCountryTransfers")

### thirdCountryTransfers Type

an array of merged types ([Details](tilt-schema-properties-thirdcountrytransfers-items.md))

### thirdCountryTransfers Examples

```json
[
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
]
```

## accessAndDataPortability

Defining the right to access and data portability.


`accessAndDataPortability`

-   is required
-   Type: `object` ([AccessAndDataPortability](tilt-schema-properties-accessanddataportability.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-accessanddataportability.md "\#/properties/accessAndDataPortability#/properties/accessAndDataPortability")

### accessAndDataPortability Type

`object` ([AccessAndDataPortability](tilt-schema-properties-accessanddataportability.md))

### accessAndDataPortability Examples

```json
{
  "available": true,
  "description": "Data access is possible through...",
  "url": "https://green-bikes.de/access",
  "email": "access@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ],
  "administrativeFee": {
    "amount": 0,
    "currency": "EUR"
  },
  "dataFormat": "json"
}
```

## sources

This duty to provide information is limited to the collection of personal data that does not take place from the data subject (Art. 14).


`sources`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-sources-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-sources.md "\#/properties/sources#/properties/sources")

### sources Type

an array of merged types ([Details](tilt-schema-properties-sources-items.md))

### sources Examples

```json
[
  {
    "_id": "f1423cc00509931",
    "dataCategory": "Creditworthiness",
    "sources": [
      {
        "description": "This information could be retrieved from...",
        "url": "https://blueCompany.org",
        "publiclyAvailable": false
      }
    ]
  }
]
```

## rightToInformation

Refers to the right of information.


`rightToInformation`

-   is required
-   Type: `object` ([RightToInformation](tilt-schema-properties-righttoinformation.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttoinformation.md "\#/properties/rightToInformation#/properties/rightToInformation")

### rightToInformation Type

`object` ([RightToInformation](tilt-schema-properties-righttoinformation.md))

### rightToInformation Examples

```json
{
  "available": true,
  "description": "For the right to information please use this contact form and...",
  "url": "https://greencompany.org/rightToInformation",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ]
}
```

## rightToRectificationOrDeletion

This schema refers to the right to rectification or deletion (Art. 16 GDPR).


`rightToRectificationOrDeletion`

-   is required
-   Type: `object` ([RightToRectificationOrDeletion](tilt-schema-properties-righttorectificationordeletion.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttorectificationordeletion.md "\#/properties/rightToRectificationOrDeletion#/properties/rightToRectificationOrDeletion")

### rightToRectificationOrDeletion Type

`object` ([RightToRectificationOrDeletion](tilt-schema-properties-righttorectificationordeletion.md))

### rightToRectificationOrDeletion Examples

```json
{
  "available": true,
  "description": "For the right to rectification please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ]
}
```

## rightToDataPortability

The right to data portability as stated in Art. 20 GDPR.


`rightToDataPortability`

-   is required
-   Type: `object` ([RightToDataPortability](tilt-schema-properties-righttodataportability.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttodataportability.md "\#/properties/rightToDataPortability#/properties/rightToDataPortability")

### rightToDataPortability Type

`object` ([RightToDataPortability](tilt-schema-properties-righttodataportability.md))

### rightToDataPortability Examples

```json
{
  "available": true,
  "description": "Data portability is only possible when...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy"
  ]
}
```

## rightToWithdrawConsent

This schema refers to the right to withdraw consent.


`rightToWithdrawConsent`

-   is required
-   Type: `object` ([RightToWithdrawConsent](tilt-schema-properties-righttowithdrawconsent.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttowithdrawconsent.md "\#/properties/rightToWithdrawConsent#/properties/rightToWithdrawConsent")

### rightToWithdrawConsent Type

`object` ([RightToWithdrawConsent](tilt-schema-properties-righttowithdrawconsent.md))

### rightToWithdrawConsent Examples

```json
{
  "available": true,
  "description": "For the right to withdraw consent please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "Email verification"
  ]
}
```

## rightToComplain

This schema refers to the right to complain.


`rightToComplain`

-   is required
-   Type: `object` ([RightToComplain](tilt-schema-properties-righttocomplain.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-righttocomplain.md "\#/properties/rightToComplain#/properties/rightToComplain")

### rightToComplain Type

`object` ([RightToComplain](tilt-schema-properties-righttocomplain.md))

### rightToComplain Examples

```json
{
  "available": true,
  "description": "For the right to complain please use this contact form and...",
  "url": "https://greencompany.org/rights",
  "email": "contact@greencompany.de",
  "identificationEvidences": [
    "ID card copy",
    "Email verification"
  ],
  "supervisoryAuthority": {
    "name": "Commissioner for Data Protection",
    "address": "Friedrichstrasse 219, 10969 Berlin",
    "country": "DE",
    "email": "mailbox@privacy-berlin.de",
    "phone": "0049 444 222 111"
  }
}
```

## automatedDecisionMaking

Automated decision making and potentially involved logic. Does include profiling.


`automatedDecisionMaking`

-   is required
-   Type: `object` ([AutomatedDecisionMaking](tilt-schema-properties-automateddecisionmaking.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-automateddecisionmaking.md "\#/properties/automatedDecisionMaking#/properties/automatedDecisionMaking")

### automatedDecisionMaking Type

`object` ([AutomatedDecisionMaking](tilt-schema-properties-automateddecisionmaking.md))

### automatedDecisionMaking Examples

```json
{
  "inUse": true,
  "logicInvolved": "The personal data are processed as follows...",
  "scopeAndIntendedEffects": "From processing follows..."
}
```

## changesOfPurpose

Notification of change of purpose.


`changesOfPurpose`

-   is required
-   Type: an array of merged types ([Details](tilt-schema-properties-changesofpurpose-items.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-changesofpurpose.md "\#/properties/changesOfPurpose#/properties/changesOfPurpose")

### changesOfPurpose Type

an array of merged types ([Details](tilt-schema-properties-changesofpurpose-items.md))

### changesOfPurpose Examples

```json
[
  {
    "description": "Due to technical requirements...",
    "affectedDataCategories": [
      "Email adress",
      "Credit score"
    ],
    "plannedDateOfChange": "2020-08-20",
    "urlOfNewVersion": "https://greencomp.de/privacypolicy/2"
  }
]
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
