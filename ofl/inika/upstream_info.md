# Investigation: Inika

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inika |
| Slug | inika |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/inika |
| Commit Hash | unknown |
| Config YAML | none |
| Status | no_config_possible |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Inika (at `google/fonts/ofl/inika/METADATA.pb`) contains no source block. The family was added in the initial commit to google/fonts (commit `90abd17b4`, dated 2015-03-07 by Dave Crossland), predating the modern source tracking infrastructure.

The git log for `ofl/inika/Inika-Regular.ttf` shows only the initial commit `90abd17b4`, confirming the font has not been updated since the original onboarding.

The upstream repository was identified as `https://github.com/librefonts/inika` (confirmed by the cached repo at `upstream_repos/fontc_crater_cache/librefonts/inika/` with remote URL `https://github.com/librefonts/inika`).

The librefonts/inika repository structure:
- Root level: `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `Inika-Bold.ttf`, `Inika-Regular.ttf`, `OFL.txt`, `METADATA.json`, `src/`
- `src/` directory contains FontForge `.sfd` files: `Inika-Regular-TTF.sfd`, `Inika-Bold-TTF.sfd`, along with `.vfb` and TTX decompiled files

The HEAD commit of the upstream repo is `bccbe87bf5a91ebb43d149cd786cdabde71c8e52` (message: "update .travis.yml").

The `.sfd` (Spline Font Database) files are FontForge format. While they contain the original font source data, they are NOT compatible with gftools-builder, which only supports `.glyphs`, `.ufo`, and `.designspace` formats. Therefore, no `config.yaml` can be created for automated gftools-builder rebuilds.

The font was designed by Constanza Artigas (copyright 2011).

## Conclusion

No source block can be completed for Inika. The upstream repository (`librefonts/inika`) only contains FontForge `.sfd` source files, which are not compatible with gftools-builder. Status: `no_config_possible`. A source block with `repository_url` only could be added to document the upstream location, but no `config_yaml` can be provided.
