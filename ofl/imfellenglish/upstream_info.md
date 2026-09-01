# Investigation: IM Fell English

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell English |
| Slug | im-fell-english |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/imfellenglish |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for IM Fell English (at `google/fonts/ofl/imfellenglish/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland).

The upstream repository was identified as `https://github.com/librefonts/imfellenglish` (confirmed by examining the cached repo at `upstream_repos/fontc_crater_cache/librefonts/imfellenglish/`).

The librefonts/imfellenglish repository contains only TTX-decompiled font files:
- `IMFeENrm28P.ttf.ttx` (and split per-table `.ttx` files)
- `IMFeENit28P.ttf.ttx` (and split per-table `.ttx` files)

There are no gftools-builder-compatible sources (no `.glyphs`, `.ufo`, or `.designspace` files). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`. The font was designed by Igino Marini (copyright 2007) as a revival of the historical Fell Types from Oxford University Press.

The HEAD commit of the upstream repo is `4cc247267036e091cd401802ec99a383a403454a` (message: "update .travis.yml").

Because the upstream repository only contains TTX decompiled sources and no gftools-builder-compatible source files, it is not possible to add a meaningful `config_yaml` for automated rebuilds.

## Conclusion

No source block can be completed for IM Fell English. The upstream repository (`librefonts/imfellenglish`) only contains TTX-decompiled sources. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` is available.
