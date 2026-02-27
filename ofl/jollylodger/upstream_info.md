# Investigation: Jolly Lodger

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jolly Lodger |
| Slug | jolly-lodger |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/jollylodger |
| Commit Hash | 06a3c7f44fc01a8d09ed73ea8c180a11018bdac8 |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

No source block

## Investigation

The `ofl/jollylodger/` directory in google/fonts contains `DESCRIPTION.en_us.html`, `JollyLodger-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has only basic metadata — no `source { }` block.

The git log shows the font has been in google/fonts since the initial commit (`90abd17b4`, 2015-03-07). No font file updates have been pushed since then.

The copyright reads: "Copyright (c) 2012 by Font Diner, Inc (diner@fontdiner.com) with Reserved Font Name 'Jolly Lodger'." Created by Font Diner (Stuart Sandler).

The tracking JSON (`data/gfonts_library_sources.json`) records the upstream repository as `https://github.com/librefonts/jollylodger` at commit `06a3c7f44fc01a8d09ed73ea8c180a11018bdac8` (subject: "update .travis.yml"). This is the librefonts GitHub organization's mirror repository.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/librefonts/jollylodger`. The local clone has only one commit (shallow clone). The repository contains:
- `JollyLodger-Regular.ttf` (binary font)
- `src/JollyLodger-Regular-TTF.vfb` (FontLab Studio source, TTF variant)
- `src/VERSIONS.txt`: "JollyLodger-Regular.ttf: Version 1.000"
- TTX decompositions of the fonts

The source format is `.vfb` (FontLab Studio), which is NOT compatible with gftools-builder. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist.

## Conclusion

The upstream repository is `https://github.com/librefonts/jollylodger` at commit `06a3c7f44fc01a8d09ed73ea8c180a11018bdac8`. However, the only sources available are `.vfb` (FontLab Studio) files, which are not gftools-builder compatible. No config.yaml is possible with these sources. A source block needs to be added to METADATA.pb but the status will remain `missing_config` until buildable sources become available.
