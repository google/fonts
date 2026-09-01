# Investigation: IM Fell Great Primer

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell Great Primer |
| Slug | im-fell-great-primer |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/imfellgreatprimer |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for IM Fell Great Primer (at `google/fonts/ofl/imfellgreatprimer/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland).

The upstream repository was identified as `https://github.com/librefonts/imfellgreatprimer` (confirmed by examining the cached repo at `upstream_repos/fontc_crater_cache/librefonts/imfellgreatprimer/`).

The librefonts/imfellgreatprimer repository contains only TTX-decompiled font files:
- `IMFeGPrm28P.ttf.ttx` (and split per-table `.ttx` files)
- `IMFeGPit28P.ttf.ttx` (and split per-table `.ttx` files)

There are no gftools-builder-compatible sources (no `.glyphs`, `.ufo`, or `.designspace` files). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`. The font was designed by Igino Marini (copyright 2007) as part of the IM FELL Types revival series, based on the Great Primer types collected by John Fell and cut by Peter De Walpergen at Oxford.

The HEAD commit of the upstream repo is `caed052ae660283eebd0c5a497e5582d130825f5` (message: "update .travis.yml").

Because the upstream repository only contains TTX decompiled sources and no gftools-builder-compatible source files, it is not possible to add a meaningful `config_yaml` for automated rebuilds.

## Conclusion

No source block can be completed for IM Fell Great Primer. The upstream repository (`librefonts/imfellgreatprimer`) only contains TTX-decompiled sources. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` is available.
