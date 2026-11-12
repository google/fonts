# Investigation: IM Fell DW Pica

## Summary

| Field | Value |
|-------|-------|
| Family Name | IM Fell DW Pica |
| Slug | im-fell-dw-pica |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/imfelldwpica |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for IM Fell DW Pica (at `google/fonts/ofl/imfelldwpica/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland), predating the modern source tracking infrastructure.

The upstream repository was identified as `https://github.com/librefonts/imfelldwpica` (confirmed by examining the cached repo at `upstream_repos/fontc_crater_cache/librefonts/imfelldwpica/`).

The librefonts/imfelldwpica repository contains only TTX-decompiled font files as sources:
- `IMFePIrm28P.ttf.ttx` (and split per-table `.ttx` files)
- `IMFePIit28P.ttf.ttx` (and split per-table `.ttx` files)

There are no gftools-builder-compatible sources (no `.glyphs`, `.ufo`, or `.designspace` files). The `src/` directory contains only `METADATA_comments.txt` and `VERSIONS.txt` (which records version 3.00 for both files). The font was designed by Igino Marini (copyright 2007) as a revival of historical Fell Types.

The HEAD commit of the upstream repo is `0d86e14c53d15bed552ac4b2619a091ca36d4443` (message: "update .travis.yml").

Because the upstream repository only contains TTX decompiled sources and no gftools-builder-compatible source files, it is not possible to add a meaningful `config_yaml` for automated rebuilds.

## Conclusion

No source block can be completed for IM Fell DW Pica. The upstream repository (`librefonts/imfelldwpica`) only contains TTX-decompiled sources, which are not compatible with gftools-builder. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` is available.
