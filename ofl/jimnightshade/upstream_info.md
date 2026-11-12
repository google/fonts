# Investigation: Jim Nightshade

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jim Nightshade |
| Slug | jim-nightshade |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/jimnightshade |
| Commit Hash | a04375d8b6c564c11f00a67fa5df1d7bf446527f |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jimnightshade/` directory in google/fonts contains `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `JimNightshade-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has only basic metadata — no `source { }` block.

The git log shows the font has been in google/fonts since the initial commit (`90abd17b4`, 2015-03-07). No font file updates have been pushed since then.

The copyright reads: "Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name 'Jim Nightshade'." Designed by Brian J. Bonislawsky for Astigmatic in 2011.

The tracking JSON (`data/gfonts_library_sources.json`) records the upstream repository as `https://github.com/librefonts/jimnightshade` at commit `a04375d8b6c564c11f00a67fa5df1d7bf446527f` (subject: "update .travis.yml"). This is the librefonts GitHub organization's mirror repository.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/librefonts/jimnightshade`. The local clone has only one commit (shallow clone). The repository contains:
- `JimNightshade-Regular.ttf` (binary font)
- `src/JimNightshade-Regular.vfb` (FontLab Studio source)
- `src/JimNightshade-Regular.otf` (OTF binary)
- `src/JimNightshade-Regular-OTF.vfb` and `src/JimNightshade-Regular-TTF.vfb` (FontLab variants)
- TTX decompositions of the fonts
- `src/VERSIONS.txt`: "JimNightshade-Regular.ttf: Version 1.000"

The source format is `.vfb` (FontLab Studio binary format), which is NOT compatible with gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` files exist.

## Conclusion

The upstream repository is `https://github.com/librefonts/jimnightshade` at commit `a04375d8b6c564c11f00a67fa5df1d7bf446527f`. However, the only sources available are `.vfb` (FontLab Studio) files, which are not gftools-builder compatible. No config.yaml is possible with these sources. A source block needs to be added to METADATA.pb but the status will remain `missing_config` until buildable sources become available.
