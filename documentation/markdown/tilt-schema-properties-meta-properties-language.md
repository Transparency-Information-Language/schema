# Language Schema

```txt
#/properties/meta/properties/language#/properties/meta/properties/language
```

All language abbreviation codes follow the established ISO 639-1 standard as identifiers for names of languages.


| Abstract            | Extensible | Status         | Identifiable            | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                           |
| :------------------ | ---------- | -------------- | ----------------------- | :---------------- | --------------------- | ------------------- | -------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | Unknown identifiability | Forbidden         | Allowed               | none                | [tilt-schema.json\*](../out/tilt-schema.json "open original schema") |

## language Type

`string` ([Language](tilt-schema-properties-meta-properties-language.md))

## language Constraints

**pattern**: the string must match the following regular expression: 

```regexp
^(aa|ab|ae|af|ak|am|an|ar|as|av|ay|az|az|ba|be|bg|bh|bi|bm|bn|bo|br|bs|ca|ce|ch|co|cr|cs|cu|cv|cy|da|de|dv|dz|ee|el|en|eo|es|et|eu|fa|ff|fi|fj|fo|fr|fy|ga|gd|gl|gn|gu|gv|ha|he|hi|ho|hr|ht|hu|hy|hz|ia|id|ie|ig|ii|ik|io|is|it|iu|ja|jv|ka|kg|ki|kj|kk|kl|km|kn|ko|kr|ks|ku|kv|kw|ky|la|lb|lg|li|ln|lo|lt|lu|lv|mg|mh|mi|mk|ml|mn|mr|ms|mt|my|na|nb|nd|ne|ng|nl|nn|no|nr|nv|ny|oc|oj|om|or|os|pa|pi|pl|ps|pt|qu|rm|rn|ro|ru|rw|sa|sc|sd|se|sg|si|sk|sl|sm|sn|so|sq|sr|ss|st|su|sv|sw|ta|te|tg|th|ti|tk|tl|tn|to|tr|ts|tt|tw|ty|ug|uk|ur|uz|ve|vi|vo|wa|wo|xh|yi|yo|za|zh|zu)$
```

[try pattern](https://regexr.com/?expression=%5E(aa%7Cab%7Cae%7Caf%7Cak%7Cam%7Can%7Car%7Cas%7Cav%7Cay%7Caz%7Caz%7Cba%7Cbe%7Cbg%7Cbh%7Cbi%7Cbm%7Cbn%7Cbo%7Cbr%7Cbs%7Cca%7Cce%7Cch%7Cco%7Ccr%7Ccs%7Ccu%7Ccv%7Ccy%7Cda%7Cde%7Cdv%7Cdz%7Cee%7Cel%7Cen%7Ceo%7Ces%7Cet%7Ceu%7Cfa%7Cff%7Cfi%7Cfj%7Cfo%7Cfr%7Cfy%7Cga%7Cgd%7Cgl%7Cgn%7Cgu%7Cgv%7Cha%7Che%7Chi%7Cho%7Chr%7Cht%7Chu%7Chy%7Chz%7Cia%7Cid%7Cie%7Cig%7Cii%7Cik%7Cio%7Cis%7Cit%7Ciu%7Cja%7Cjv%7Cka%7Ckg%7Cki%7Ckj%7Ckk%7Ckl%7Ckm%7Ckn%7Cko%7Ckr%7Cks%7Cku%7Ckv%7Ckw%7Cky%7Cla%7Clb%7Clg%7Cli%7Cln%7Clo%7Clt%7Clu%7Clv%7Cmg%7Cmh%7Cmi%7Cmk%7Cml%7Cmn%7Cmr%7Cms%7Cmt%7Cmy%7Cna%7Cnb%7Cnd%7Cne%7Cng%7Cnl%7Cnn%7Cno%7Cnr%7Cnv%7Cny%7Coc%7Coj%7Com%7Cor%7Cos%7Cpa%7Cpi%7Cpl%7Cps%7Cpt%7Cqu%7Crm%7Crn%7Cro%7Cru%7Crw%7Csa%7Csc%7Csd%7Cse%7Csg%7Csi%7Csk%7Csl%7Csm%7Csn%7Cso%7Csq%7Csr%7Css%7Cst%7Csu%7Csv%7Csw%7Cta%7Cte%7Ctg%7Cth%7Cti%7Ctk%7Ctl%7Ctn%7Cto%7Ctr%7Cts%7Ctt%7Ctw%7Cty%7Cug%7Cuk%7Cur%7Cuz%7Cve%7Cvi%7Cvo%7Cwa%7Cwo%7Cxh%7Cyi%7Cyo%7Cza%7Czh%7Czu)%24 "try regular expression with regexr.com")

## language Default Value

The default value is:

```json
"en"
```

## language Examples

```json
"de"
```
