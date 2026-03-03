# Investigation: Kotta One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kotta One |
| Slug | kotta-one |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_url |
| Confidence | LOW |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Kotta One has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012 by Ania Kruk (hello@aniakruk.com), with Reserved Font Name 'Kotta'"

The DESCRIPTION.en_us.html describes Kotta One as "a new and unusual text typeface that mixes the characteristics of an italic with legibility of a roman."

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kottaone` contains only TTX/binary source files:
- `KottaOne-Regular.ttf.*` (TTX dumps)
- No Glyphs, UFO, or Designspace sources

No upstream GitHub repository for Ania Kruk or Kotta One was found in the cache.

## Conclusion

The font is an old serif text font from 2012 with no tracked upstream repository. The librefonts cache contains only TTX dumps of the binary font, not editable source files. No `config.yaml` is possible with the current sources. This family needs further investigation to find the original source files from Ania Kruk.
