# Transparency Information Language and Toolkit

With this proposed schema for transparency information with regards to data privacy, an essential step towards a sophisticated ecosystem shall be made by introducing a transparency enhancing toolkit based on a formal language model describing transparency information in the context of multi-service environments and latest legal requirements (EU General Data Protection Regulation). The desired results of the work should be suitable as ready-to-use privacy engineering solutions for developers and serve as a starting point for further research in this area. Eventually, data subjects should (be able to) understand what happens to data relating to them by using the interfaces of the toolkit.


## Author
Elias Grünewald

## License
GNU General Public License, Version 3

---

## Useful Regular Expressions for Editing the Schema

The following examples show how to find, replace or delete elements within the schema. The regular expressions where tested with tooling like VS Code.

```
Find: (The)( )((?!anyOf).*)( )(schema)
# The meta schema

Replace: \u$3
# Meta
```
