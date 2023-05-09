# Transparency Information Language and Toolkit
With this proposed schema for transparency information with regards to data privacy, an essential step towards a sophisticated ecosystem shall be made by introducing a transparency enhancing toolkit based on a formal language model describing transparency information in the context of multi-service environments and latest legal requirements (EU General Data Protection Regulation). The desired results of the work should be suitable as ready-to-use privacy engineering solutions for developers and serve as a starting point for further research in this area. Eventually, data subjects should (be able to) understand what happens to data relating to them by using the interfaces of the toolkit.

## Language definition
**[For the main language definition incl. an exemplary document, please see here. ⤴️](tilt-schema.json)**<br>
The [valid](tilt.json) exemplary document standalone.<br>
An [*in*valid](tilt-NOT-valid.json) exemplary document standalone.

## Documentation
**[For a full documentation, please see here. ⤴️](https://transparency-information-language.github.io/schema/index.html)**<br>
[A Markdown version is available here. ⤴️](documentation/markdown/tilt-schema.md)



![](media/main.png)
![](media/dataDisclosed.png)

### ▶️ GitHub Actions
| Name | Description |
| ----------- | ----------- |
| Linting JSONs | Validates and automatically prettifies the tilt-schema.json. |
| Generating human readable TILT-schema | Creates a new index.html file based on latest tilt-schema.json.| 
| pages-build-deployment | Creates [GitHub Page](https://transparency-information-language.github.io/schema/index.html) based on docs/index.html. |

## 📝 Release notes: TILT Version 2.0
### Data Origin
According to Art. 20 (1) a "data subject has the right to receive the personal data concerning him or her, which he or she has provided to a controller".
Because of that, upon a data subject's Right to Data Portability request it is necessary to distinguish between multiple possible data origins. TILT
Version 2.0 adds an `origin` field to `sources` with three possible options: `received`, `observed` or `inferred`.

### Industry Sector
To classify data controllers according to the kind of economic activities TILT Version 2.0 uses the industry classification according to UN ISIC Rev. 4. A `sector` field is added to `controller`.

### URL Array
TILT Version 2.0 changes the `url` field to an array to allow for multiple URLs. This change was made to accommodate cases where there may be multiple sub-
entities that point to the same main entity.

### dataDisclosed Category Array
TILT Version 2.0 changes the `category` field to an array to allow for multiple categories. This change enables greater flexibility and specificity in categorizing the data disclosed.

### Domain for Recipients
TILT Version 2.0 adds a new `domain` field to the `recipients` of `dataDisclosed`. This allows a more detailed identification of the third party.

## Author
[Elias Grünewald](mailto:gruenewald@tu-berlin.de)

## License
[MIT License](LICENSE)
