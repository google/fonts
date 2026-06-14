# Investigation: Just Me Again Down Here

## Summary

| Field | Value |
|-------|-------|
| Family Name | Just Me Again Down Here |
| Slug | just-me-again-down-here |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/justmeagaindownhere |
| Commit Hash | 63543cec6964e5061ece828c63948d1910e0dbdd |
| Config YAML | none (OTF-only sources in librefonts mirror) |
| Status | no_config_possible |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
No source block
```

## Investigation

The METADATA.pb for Just Me Again Down Here has no source block. The font was designed by Kimberly Geswein (kimberlygeswein@gmail.com), a prolific handwriting font designer with many fonts in the Google Fonts catalog.

The git history in google/fonts shows:
- Initial commit `90abd17b4` (earliest record, pre-dating 2011)
- `883939708` — "Remove METADATA.json files"
- `480630de3` — "Tentative update to METADATA.pb textprotos"
- `27f377ab0` — "Update copyright field in METADATA.pb"
- Several language/metadata-only changes since then

The copyright reads: "Copyright (c) 2011 by Kimberly Geswein (kimberlygeswein@gmail.com). All rights reserved."

The DESCRIPTION.en_us.html describes the font as created shortly after the designer's family moved to China in 2010/2011, created using a Wacom Tablet and Adobe Illustrator. No GitHub repository URL is mentioned.

A `librefonts` mirror exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/justmeagaindownhere/`. This contains TTX-decompiled OTF files and a `src/` directory with more OTF TTX files. No Glyphs, UFO, or gftools-builder compatible sources are present. The commit `63543cec6964e5061ece828c63948d1910e0dbdd` is recorded in the tracking JSON.

The DESCRIPTION.en_us.html confirms the font was created using a Wacom Tablet and Adobe Illustrator, suggesting the original sources are in Illustrator's proprietary format (AI or EPS), which is not compatible with gftools-builder.

The font file structure in google/fonts contains only:
- `JustMeAgainDownHere.ttf`
- `METADATA.pb`
- `OFL.txt`
- `DESCRIPTION.en_us.html`

No override `config.yaml` exists in the google/fonts directory.

## Conclusion

Just Me Again Down Here has a librefonts mirror at `https://github.com/librefonts/justmeagaindownhere` with commit `63543cec6964e5061ece828c63948d1910e0dbdd`. The librefonts mirror contains only TTX-decompiled OTF files — no gftools-builder compatible sources. The font was originally created in Adobe Illustrator, so no `.glyphs` or `.ufo` sources are expected to exist. Status: no_config_possible.
