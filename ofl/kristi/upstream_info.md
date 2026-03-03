# Investigation: Kristi

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kristi |
| Slug | kristi |
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

The METADATA.pb for Kristi has no `source` block. The font was added in the "Initial commit" (`90abd17b4`) and subsequently updated in `1ac6f76ab` ("hotfix-kristi: v1.004 added (#902)", May 8, 2017).

The copyright notice reads: "Copyright (c) 2010, Birgit Pulk (birgitpulk@gmail.com). All rights reserved. Licenced under SIL OFL v1.1"

The DESCRIPTION.en_us.html describes it as "a calligraphy font inspired by old chancery typefaces" designed by Birgit Pulk, a graphic designer from Estonia.

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kristi` contains only TTX dumps of the binary font:
- `Kristi.ttf.*` (TTX dumps)
- No Glyphs, UFO, or other editable source formats

No upstream GitHub repository for Birgit Pulk was found in the cache.

## Conclusion

The font is an old handwriting font from 2010 with no tracked upstream repository. The librefonts cache contains only TTX dumps of the binary font. No `config.yaml` is possible with the current sources. This family needs further investigation to find the original source files from Birgit Pulk.
