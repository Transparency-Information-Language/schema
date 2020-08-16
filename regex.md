## Useful Regular Expressions for Editing the Schema

The following examples show how to find, replace or delete elements within the schema. The regular expressions where tested with tooling like VS Code.

```
Find: (The)( )((?!anyOf).*)( )(schema)
# The meta schema

Replace: \u$3
# Meta
```

