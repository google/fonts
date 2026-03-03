# Investigation Report: Homemade Apple

## Summary

Homemade Apple is a handwriting/display font designed by Font Diner, licensed under Apache 2.0. It was initially added to google/fonts in the 2015 "Initial commit" and received a hotfix update in 2017 (PR #776). The upstream repository at `https://github.com/librefonts/homemadeapple` contains only TTX-decomposed font tables and no buildable source files (.glyphs, .ufo, .designspace, .sfd, or .vfb). The font has no source block in METADATA.pb and no config.yaml. Since the upstream repo contains no compilable sources, a config.yaml cannot be created.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Homemade Apple                                     |
| Designer           | Font Diner                                         |
| License            | Apache 2.0                                         |
| Directory          | apache/homemadeapple                               |
| Repository URL     | https://github.com/librefonts/homemadeapple        |
| Onboarding Commit  | N/A (no buildable sources in upstream)             |
| Config YAML        | None (no compilable sources)                       |
| Status             | **no_config_possible**                             |
| Confidence         | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file at `apache/homemadeapple/METADATA.pb` has no `source { }` block. The font was added on 2011-01-06 and is categorized as HANDWRITING and DISPLAY.

### Git History in google/fonts

The font file `HomemadeApple-Regular.ttf` has only one modifying commit:

1. **8e94f9c12** (2017-08-07) by Marc Foley: "hotfix-homemadeapple: v1.001 added (#776)"
   - Renamed `HomemadeApple.ttf` to `HomemadeApple-Regular.ttf`
   - Updated METADATA.pb fields (filename, post_script_name, full_name, copyright)
   - Updated DESCRIPTION.en_us.html

The original addition was in the "Initial commit" (90abd17b4, 2015-03-07) by Dave Crossland.

### Upstream Repository Analysis

The cached repository at `librefonts/homemadeapple` (remote: `https://github.com/librefonts/homemadeapple`) contains:

- **1 commit total**: `5159ae2` (2014-10-17) "update .travis.yml"
- **Files**: TTX-decomposed font tables (HomemadeApple.ttf.*.ttx), LICENSE.txt, COPYRIGHT.txt, DESCRIPTION.en_us.html, METADATA.json
- **src/ directory**: Contains only `VERSIONS.txt` (records "HomemadeApple.ttf: Version 1.000") and an empty `METADATA_comments.txt`
- **No buildable sources**: No .glyphs, .ufo, .designspace, .sfd, or .vfb files found anywhere in the repository

The repository is a legacy `librefonts` mirror containing TTX decompositions rather than actual design sources. This is consistent with early Google Fonts onboarding practices where some fonts were contributed as pre-compiled binaries without editable sources.

### Font Diner Context

Font Diner is a commercial foundry. The font was contributed under the Apache 2.0 license. The original design sources (likely proprietary format) were never made publicly available.

## Conclusion

**Status: no_config_possible**

Homemade Apple has an upstream repository at `https://github.com/librefonts/homemadeapple`, but it contains only TTX decompositions of the compiled font, not editable design sources. No config.yaml can be created because there are no compilable source files (.glyphs, .ufo, .designspace) from which to build the font. The font is licensed under Apache 2.0 (not OFL) and resides in `apache/homemadeapple` rather than `ofl/`. This family is not currently tracked in `data/gfonts_library_sources.json` as the tracking system currently covers only OFL-licensed fonts.

A source block could theoretically be added to METADATA.pb pointing to the librefonts repo, but without buildable sources, the `config_yaml` field cannot be populated. The repository URL could still be documented for reference purposes.
