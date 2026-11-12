# Alex Brush

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alexbrush/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alex-brush |
| Commit | `1a50bd10383f6c5416f5b4806a9368fd2009ea8c` |
| Config YAML | `sources/config.yml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/alex-brush` is already recorded in the METADATA.pb `source` block. It was originally added via the gftools-packager commit `3f9fd6d69` (PR #5686), which explicitly references the upstream repo in its commit message:

> "Alex Brush Version 1.111; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/googlefonts/alex-brush at commit https://github.com/googlefonts/alex-brush/commit/1a50bd10383f6c5416f5b4806a9368fd2009ea8c"

The cached clone at `upstream_repos/fontc_crater_cache/googlefonts/alex-brush` confirms the remote URL matches: `https://github.com/googlefonts/alex-brush`.

## How the Commit Hash Was Identified

The commit `1a50bd10383f6c5416f5b4806a9368fd2009ea8c` ("winDescent small fix" by Viviana Monsalve, 2022-12-08) is verified through multiple lines of evidence:

1. **gftools-packager commit message**: The google/fonts commit `3f9fd6d69` (PR #5686, 2022-12-09) explicitly states the font was taken from this exact commit hash.
2. **Temporal consistency**: The upstream commit is dated 2022-12-08 and the google/fonts onboarding is dated 2022-12-09 -- the very next day.
3. **Only commit in the repo**: The upstream repository contains a single squashed commit (`1a50bd1`), which is also HEAD of `main`. There are no other commits that could be confused with it.
4. **Binary file identity**: The TTF file at this commit (`fonts/ttf/AlexBrush-Regular.ttf`, 116,244 bytes) has an identical SHA-256 hash (`df702038d8e27797230c77959c139eeea38cac0caf53e19ea5b513d3b0d3362d`) to the file in `ofl/alexbrush/AlexBrush-Regular.ttf` in google/fonts.

## How Config YAML Was Resolved

The config file `sources/config.yml` exists at the referenced commit and contains:

```yaml
sources:
  - AlexBrush.glyphs
familyName: "Alex Brush"
buildVariable: false
# autohintTTF: false
```

This is a valid gftools-builder configuration pointing to the Glyphs source file `sources/AlexBrush.glyphs`, which also exists in the repository at the referenced commit. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

## Conclusion

**Confidence: HIGH**

All source metadata for Alex Brush is complete and verified. The repository URL, commit hash, config YAML path, and branch are all correctly recorded in METADATA.pb. The binary font file in google/fonts is an exact byte-for-byte match with the file from the referenced upstream commit. The upstream repo is a single-commit repository, making verification straightforward. No changes are needed.
