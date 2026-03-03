# Investigation: Kranky

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kranky |
| Slug | kranky |
| License Dir | apache |
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

The METADATA.pb for Kranky has no `source` block. The METADATA.pb only contains basic metadata. The font was added with Apache 2.0 license.

The copyright notice reads: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow. All rights reserved."

The DESCRIPTION.en_us.html describes it as "a hand-crafted, fun-filled font."

The cached repository at `upstream_repos/fontc_crater_cache/librefonts/kranky` contains only TTX source files:
- `Kranky.ttf.*` (TTX dumps)
- `src/` directory

No upstream GitHub repository for Font Diner / Sideshow was found in the cache. Font Diner is a commercial type foundry, and their fonts on Google Fonts may not have public upstream source repositories.

## Conclusion

The font is an old display font from 2011 by Font Diner (DBA Sideshow) with no tracked upstream repository. The librefonts cache contains only TTX dumps. Given that Font Diner is a commercial foundry, the original source files may not be publicly available. This family needs further investigation to determine if any upstream repository exists.
