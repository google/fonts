# Investigation: IM Fell DW Pica SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell DW Pica SC |
| Slug | im-fell-dw-pica-sc |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/imfelldwpicasc |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for IM Fell DW Pica SC (at `google/fonts/ofl/imfelldwpicasc/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland).

The upstream repository was identified as `https://github.com/librefonts/imfelldwpicasc` (confirmed by examining the cached repo at `upstream_repos/fontc_crater_cache/librefonts/imfelldwpicasc/`).

The librefonts/imfelldwpicasc repository contains only TTX-decompiled font files:
- `IMFePIsc28P.ttf.ttx` (and split per-table `.ttx` files)

There are no gftools-builder-compatible sources (no `.glyphs`, `.ufo`, or `.designspace` files). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt`. The SC (Small Caps) variant is a companion to IM Fell DW Pica, designed by Igino Marini.

The HEAD commit of the upstream repo is `7504ed1a04211a3a32b920be754c7076ffcb5230` (message: "update .travis.yml").

Because the upstream repository only contains TTX decompiled sources and no gftools-builder-compatible source files, it is not possible to add a meaningful `config_yaml` for automated rebuilds.

## Conclusion

No source block can be completed for IM Fell DW Pica SC. The upstream repository (`librefonts/imfelldwpicasc`) only contains TTX-decompiled sources. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` is available.
