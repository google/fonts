# Investigation: Inder

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inder |
| Slug | inder |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/inder |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Inder (at `google/fonts/ofl/inder/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland), predating the modern source tracking infrastructure.

The git log for `ofl/inder/Inder-Regular.ttf` shows only the initial commit `90abd17b4`, confirming the font has not been updated since the original onboarding.

The upstream repository was identified as `https://github.com/librefonts/inder` (confirmed by the cached repo at `upstream_repos/fontc_crater_cache/librefonts/inder/` with remote URL `https://github.com/librefonts/inder`).

The librefonts/inder repository structure:
- Root level: `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `Inder-Regular.ttf`, `OFL.txt`, `METADATA.json`, `src/`
- `src/` directory contains: FontForge `.sfd` files (`Inder-Regular-TTF.sfd`, `Inder-Regular-OTF.vfb`, `Inder-Regular.vfb`) and TTX decompiled files

The HEAD commit of the upstream repo is `5620f4744158d400ba1286612d14d49c43597033` (message: "update .travis.yml").

The `.sfd` (Spline Font Database) files are FontForge format. While they contain the original font source data, they are NOT compatible with gftools-builder, which only supports `.glyphs`, `.ufo`, and `.designspace` formats. Therefore, no `config.yaml` can be created for automated gftools-builder rebuilds.

The font was designed by Sorkin Type (Eben Sorkin), as indicated in the copyright notice: "Copyright (c) 2010 by Sorkin Type Co (eben@eyebytes.com)".

## Conclusion

No source block can be completed for Inder. The upstream repository (`librefonts/inder`) only contains FontForge `.sfd` source files, which are not compatible with gftools-builder. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` can be provided.
