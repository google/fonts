# Investigation Report: Grand Hotel

## Summary

Grand Hotel is a condensed upright connecting script designed by Brian J. Bonislawsky and Jim Lyles for Astigmatic (AOETI), added to Google Fonts on 2012-11-30. The font was part of the initial bulk commit in the google/fonts repository. An upstream repository exists at `librefonts/grandhotel` on GitHub, but it only contains VFB (FontLab Studio) source files and TTX decompositions -- no gftools-builder-compatible sources (.glyphs, .ufo, .designspace). There is no config.yaml and no way to create one with the available sources. The METADATA.pb currently has no source block.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Grand Hotel                                        |
| Designer           | Astigmatic (Brian J. Bonislawsky, Jim Lyles)       |
| Date Added         | 2012-11-30                                         |
| Repository URL     | https://github.com/librefonts/grandhotel           |
| Onboarding Commit  | b0716771fb1056ca9db1d65d94e62ecf9dbedefa (single commit in repo) |
| Config YAML        | None (VFB-only sources, not gftools-builder compatible) |
| Source Files       | src/GrandHotel-Regular.vfb, src/GrandHotel-Regular-TTF.vfb, src/GrandHotel-Regular-OTF.vfb |
| Status             | **no_config_possible**                             |
| Confidence         | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no `source { }` block at all. The font is categorized as HANDWRITING and DISPLAY, with a single weight (Regular 400).

### Git History in google/fonts

The font file `GrandHotel-Regular.ttf` has only one commit in google/fonts:

- `90abd17b4` (2015-03-07) - "Initial commit" by Dave Crossland. This was the massive initial commit that imported the entire Google Fonts collection into the repository. The font itself was added to Google Fonts on 2012-11-30 according to `date_added`.

No subsequent updates have been made to the font file.

### Upstream Repository

The repository `https://github.com/librefonts/grandhotel` exists and is accessible (HTTP 200). It is cached locally at `fontc_crater_cache/librefonts/grandhotel/`. The repo is a shallow clone with a single commit:

- `b071677` (2014-10-17) - "update .travis.yml" by hash3g

This is part of the librefonts collection, which is an automated decomposition archive. The repo contains:
- **VFB source files** (FontLab Studio format): `src/GrandHotel-Regular.vfb`, `src/GrandHotel-Regular-TTF.vfb`, `src/GrandHotel-Regular-OTF.vfb`
- **TTX decompositions** of both the TrueType and CFF versions
- FONTLOG.txt, DESCRIPTION.en_us.html, METADATA.json, OFL.txt

There are **no** `.glyphs`, `.ufo`, or `.designspace` files. The VFB format is proprietary FontLab Studio format and is not compatible with gftools-builder. No `config.yaml` exists.

### Source File Assessment

The FONTLOG.txt documents three source files:
1. `GrandHotel-Regular.vfb` - Original with contour overlaps
2. `GrandHotel-Regular-TTF.vfb` - TrueType outlines with hinting adjustments
3. `GrandHotel-Regular-OTF.vfb` - Merged contours, optimized for OTF

All are VFB format. Without conversion to .glyphs or .ufo, a config.yaml cannot be created.

### Note on librefonts Repository

The `librefonts` organization on GitHub is not the original upstream source. It is an archival project that decomposed Google Fonts binaries into TTX format and stored VFB sources where available. The original designer's contact is astigma@astigmatic.com (Brian J. Bonislawsky). No separate Astigmatic GitHub repository for this font was found in the upstream cache.

## Conclusion

Grand Hotel has an identifiable upstream repository at librefonts/grandhotel, but it only contains VFB sources that are not compatible with gftools-builder. Creating a config.yaml is not possible with the available source files.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/grandhotel"
}
```

A minimal source block with only the repository_url is appropriate since:
- The commit hash is not meaningful (single auto-generated commit, not the original onboarding commit)
- No config.yaml is possible (VFB-only sources)
- The librefonts repo is a decomposition archive, not the original design source

### Status: no_config_possible

The VFB source format cannot be used with gftools-builder. The font would need to be re-sourced from the original designer or have its VFB files converted to a modern format before a config.yaml could be created.
