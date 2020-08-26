# Meta Schema

```txt
#/properties/meta#/properties/meta
```

Meta information for the identification and verification of the document.


| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ------------ | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## meta Type

`object` ([Meta](tilt-schema-properties-meta.md))

## meta Examples

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

# Meta Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                                             |
| :-------------------- | --------- | -------- | -------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [\_id](#_id)          | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-_id.md "\#/properties/meta/properties/\_id#/properties/meta/properties/\_id")              |
| [name](#name)         | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-name.md "\#/properties/meta/properties/name#/properties/meta/properties/name")             |
| [created](#created)   | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-created.md "\#/properties/meta/properties/created#/properties/meta/properties/created")    |
| [modified](#modified) | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-modified.md "\#/properties/meta/properties/modified#/properties/meta/properties/modified") |
| [version](#version)   | `integer` | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-version.md "\#/properties/meta/properties/version#/properties/meta/properties/version")    |
| [language](#language) | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-language.md "\#/properties/meta/properties/language#/properties/meta/properties/language") |
| [status](#status)     | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-status.md "\#/properties/meta/properties/status#/properties/meta/properties/status")       |
| [url](#url)           | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-url.md "\#/properties/meta/properties/url#/properties/meta/properties/url")                |
| [\_hash](#_hash)      | `string`  | Required | cannot be null | [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-_hash.md "\#/properties/meta/properties/\_hash#/properties/meta/properties/\_hash")        |
| Additional Properties | Any       | Optional | can be null    |                                                                                                                                                                                        |

## \_id

The ID follows the database-specific implementation and does not have to be set in advance; but should offer as much entropy as possible for globally unique identifiers.


`_id`

-   is required
-   Type: `string` ([\_id](tilt-schema-properties-meta-properties-_id.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-_id.md "\#/properties/meta/properties/\_id#/properties/meta/properties/\_id")

### \_id Type

`string` ([\_id](tilt-schema-properties-meta-properties-_id.md))

### \_id Examples

```json
"f1424f86-ca0f-4f0c-9438-43cc00509931"
```

## name

Name of the data controller.


`name`

-   is required
-   Type: `string` ([Name](tilt-schema-properties-meta-properties-name.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-name.md "\#/properties/meta/properties/name#/properties/meta/properties/name")

### name Type

`string` ([Name](tilt-schema-properties-meta-properties-name.md))

### name Examples

```json
"Green Company"
```

## created

Creation date of the document as an ISO-8601 time code.


`created`

-   is required
-   Type: `string` ([Created](tilt-schema-properties-meta-properties-created.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-created.md "\#/properties/meta/properties/created#/properties/meta/properties/created")

### created Type

`string` ([Created](tilt-schema-properties-meta-properties-created.md))

### created Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
```

[try pattern](https://regexr.com/?expression=%5E(%5B%5C%2B-%5D%3F%5Cd%7B4%7D(%3F!%5Cd%7B2%7D%5Cb))((-%3F)((0%5B1-9%5D%7C1%5B0-2%5D)(%5C3(%5B12%5D%5Cd%7C0%5B1-9%5D%7C3%5B01%5D))%3F%7CW(%5B0-4%5D%5Cd%7C5%5B0-2%5D)(-%3F%5B1-7%5D)%3F%7C(00%5B1-9%5D%7C0%5B1-9%5D%5Cd%7C%5B12%5D%5Cd%7B2%7D%7C3(%5B0-5%5D%5Cd%7C6%5B1-6%5D)))(%5BT%5Cs%5D(((%5B01%5D%5Cd%7C2%5B0-3%5D)((%3A%3F)%5B0-5%5D%5Cd)%3F%7C24%5C%3A%3F00)(%5B%5C.%2C%5D%5Cd%2B(%3F!%3A))%3F)%3F(%5C17%5B0-5%5D%5Cd(%5B%5C.%2C%5D%5Cd%2B)%3F)%3F(%5BzZ%5D%7C(%5B%5C%2B-%5D)(%5B01%5D%5Cd%7C2%5B0-3%5D)%3A%3F(%5B0-5%5D%5Cd)%3F)%3F)%3F)%3F%24 "try regular expression with regexr.com")

### created Examples

```json
"2020-04-03T15:53:05.929588"
```

## modified

Last modified date of the document as an ISO-8601 time code.


`modified`

-   is required
-   Type: `string` ([Modified](tilt-schema-properties-meta-properties-modified.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-modified.md "\#/properties/meta/properties/modified#/properties/meta/properties/modified")

### modified Type

`string` ([Modified](tilt-schema-properties-meta-properties-modified.md))

### modified Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^([\+-]?\d{4}(?!\d{2}\b))((-?)((0[1-9]|1[0-2])(\3([12]\d|0[1-9]|3[01]))?|W([0-4]\d|5[0-2])(-?[1-7])?|(00[1-9]|0[1-9]\d|[12]\d{2}|3([0-5]\d|6[1-6])))([T\s]((([01]\d|2[0-3])((:?)[0-5]\d)?|24\:?00)([\.,]\d+(?!:))?)?(\17[0-5]\d([\.,]\d+)?)?([zZ]|([\+-])([01]\d|2[0-3]):?([0-5]\d)?)?)?)?$
```

[try pattern](https://regexr.com/?expression=%5E(%5B%5C%2B-%5D%3F%5Cd%7B4%7D(%3F!%5Cd%7B2%7D%5Cb))((-%3F)((0%5B1-9%5D%7C1%5B0-2%5D)(%5C3(%5B12%5D%5Cd%7C0%5B1-9%5D%7C3%5B01%5D))%3F%7CW(%5B0-4%5D%5Cd%7C5%5B0-2%5D)(-%3F%5B1-7%5D)%3F%7C(00%5B1-9%5D%7C0%5B1-9%5D%5Cd%7C%5B12%5D%5Cd%7B2%7D%7C3(%5B0-5%5D%5Cd%7C6%5B1-6%5D)))(%5BT%5Cs%5D(((%5B01%5D%5Cd%7C2%5B0-3%5D)((%3A%3F)%5B0-5%5D%5Cd)%3F%7C24%5C%3A%3F00)(%5B%5C.%2C%5D%5Cd%2B(%3F!%3A))%3F)%3F(%5C17%5B0-5%5D%5Cd(%5B%5C.%2C%5D%5Cd%2B)%3F)%3F(%5BzZ%5D%7C(%5B%5C%2B-%5D)(%5B01%5D%5Cd%7C2%5B0-3%5D)%3A%3F(%5B0-5%5D%5Cd)%3F)%3F)%3F)%3F%24 "try regular expression with regexr.com")

### modified Examples

```json
"2020-04-03T15: 53: 05.929588"
```

## version

This number serves to version documents of a controller.


`version`

-   is required
-   Type: `integer` ([Version](tilt-schema-properties-meta-properties-version.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-version.md "\#/properties/meta/properties/version#/properties/meta/properties/version")

### version Type

`integer` ([Version](tilt-schema-properties-meta-properties-version.md))

### version Constraints

**minimum**: the value of this number must greater than or equal to: `1`

### version Default Value

The default value is:

```json
1
```

### version Examples

```json
2
```

## language

All language abbreviation codes follow the established ISO 639-1 standard as identifiers for names of languages.


`language`

-   is required
-   Type: `string` ([Language](tilt-schema-properties-meta-properties-language.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-language.md "\#/properties/meta/properties/language#/properties/meta/properties/language")

### language Type

`string` ([Language](tilt-schema-properties-meta-properties-language.md))

### language Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(aa|ab|ae|af|ak|am|an|ar|as|av|ay|az|az|ba|be|bg|bh|bi|bm|bn|bo|br|bs|ca|ce|ch|co|cr|cs|cu|cv|cy|da|de|dv|dz|ee|el|en|eo|es|et|eu|fa|ff|fi|fj|fo|fr|fy|ga|gd|gl|gn|gu|gv|ha|he|hi|ho|hr|ht|hu|hy|hz|ia|id|ie|ig|ii|ik|io|is|it|iu|ja|jv|ka|kg|ki|kj|kk|kl|km|kn|ko|kr|ks|ku|kv|kw|ky|la|lb|lg|li|ln|lo|lt|lu|lv|mg|mh|mi|mk|ml|mn|mr|ms|mt|my|na|nb|nd|ne|ng|nl|nn|no|nr|nv|ny|oc|oj|om|or|os|pa|pi|pl|ps|pt|qu|rm|rn|ro|ru|rw|sa|sc|sd|se|sg|si|sk|sl|sm|sn|so|sq|sr|ss|st|su|sv|sw|ta|te|tg|th|ti|tk|tl|tn|to|tr|ts|tt|tw|ty|ug|uk|ur|uz|ve|vi|vo|wa|wo|xh|yi|yo|za|zh|zu)$
```

[try pattern](https://regexr.com/?expression=%5E(aa%7Cab%7Cae%7Caf%7Cak%7Cam%7Can%7Car%7Cas%7Cav%7Cay%7Caz%7Caz%7Cba%7Cbe%7Cbg%7Cbh%7Cbi%7Cbm%7Cbn%7Cbo%7Cbr%7Cbs%7Cca%7Cce%7Cch%7Cco%7Ccr%7Ccs%7Ccu%7Ccv%7Ccy%7Cda%7Cde%7Cdv%7Cdz%7Cee%7Cel%7Cen%7Ceo%7Ces%7Cet%7Ceu%7Cfa%7Cff%7Cfi%7Cfj%7Cfo%7Cfr%7Cfy%7Cga%7Cgd%7Cgl%7Cgn%7Cgu%7Cgv%7Cha%7Che%7Chi%7Cho%7Chr%7Cht%7Chu%7Chy%7Chz%7Cia%7Cid%7Cie%7Cig%7Cii%7Cik%7Cio%7Cis%7Cit%7Ciu%7Cja%7Cjv%7Cka%7Ckg%7Cki%7Ckj%7Ckk%7Ckl%7Ckm%7Ckn%7Cko%7Ckr%7Cks%7Cku%7Ckv%7Ckw%7Cky%7Cla%7Clb%7Clg%7Cli%7Cln%7Clo%7Clt%7Clu%7Clv%7Cmg%7Cmh%7Cmi%7Cmk%7Cml%7Cmn%7Cmr%7Cms%7Cmt%7Cmy%7Cna%7Cnb%7Cnd%7Cne%7Cng%7Cnl%7Cnn%7Cno%7Cnr%7Cnv%7Cny%7Coc%7Coj%7Com%7Cor%7Cos%7Cpa%7Cpi%7Cpl%7Cps%7Cpt%7Cqu%7Crm%7Crn%7Cro%7Cru%7Crw%7Csa%7Csc%7Csd%7Cse%7Csg%7Csi%7Csk%7Csl%7Csm%7Csn%7Cso%7Csq%7Csr%7Css%7Cst%7Csu%7Csv%7Csw%7Cta%7Cte%7Ctg%7Cth%7Cti%7Ctk%7Ctl%7Ctn%7Cto%7Ctr%7Cts%7Ctt%7Ctw%7Cty%7Cug%7Cuk%7Cur%7Cuz%7Cve%7Cvi%7Cvo%7Cwa%7Cwo%7Cxh%7Cyi%7Cyo%7Cza%7Czh%7Czu)%24 "try regular expression with regexr.com")

### language Default Value

The default value is:

```json
"en"
```

### language Examples

```json
"de"
```

## status

The status of an instance can be active or inactive depending on the policy's legal force.


`status`

-   is required
-   Type: `string` ([Status](tilt-schema-properties-meta-properties-status.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-status.md "\#/properties/meta/properties/status#/properties/meta/properties/status")

### status Type

`string` ([Status](tilt-schema-properties-meta-properties-status.md))

### status Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(active|inactive)$
```

[try pattern](https://regexr.com/?expression=%5E(active%7Cinactive)%24 "try regular expression with regexr.com")

### status Default Value

The default value is:

```json
"active"
```

### status Examples

```json
"active"
```

```json
"inactive"
```

## url

URL to this schema.


`url`

-   is required
-   Type: `string` ([Url](tilt-schema-properties-meta-properties-url.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-url.md "\#/properties/meta/properties/url#/properties/meta/properties/url")

### url Type

`string` ([Url](tilt-schema-properties-meta-properties-url.md))

### url Constraints

**URI reference**: the string must be a URI reference, according to [RFC 3986](https://tools.ietf.org/html/rfc4291 "check the specification")

### url Examples

```json
"https://green-bikes.de/privacy"
```

## \_hash

The hash is based on one SHA256 calculation of the document.


`_hash`

-   is required
-   Type: `string` ([\_hash](tilt-schema-properties-meta-properties-_hash.md))
-   cannot be null
-   defined in: [Root schema of a Transparency Information Language](tilt-schema-properties-meta-properties-_hash.md "\#/properties/meta/properties/\_hash#/properties/meta/properties/\_hash")

### \_hash Type

`string` ([\_hash](tilt-schema-properties-meta-properties-_hash.md))

### \_hash Constraints

**maximum length**: the maximum number of characters for this string is: `64`

**minimum length**: the minimum number of characters for this string is: `64`

### \_hash Examples

```json
"be81d309088dde861ab5fc4d62d4bbfe0aeef3e3baf2f5362c1086f451f0a1e7"
```

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
