# Anton SC

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete (with caveats)
- **Designer**: Vernon Adams
- **Google Fonts date_added**: 2024-05-27

## Source Data

| Field | Value |
|---|---|
| `repository_url` | `https://github.com/googlefonts/AntonFont` |
| `commit` | `beb92fcad87808357123bb66881b4032dc96efe7` |
| `branch` | `main` |
| `config_yaml` | `sources/config.yaml` (see caveats below) |

## How URL Found

The repository URL `https://github.com/googlefonts/AntonFont` was set by the original onboarder, Simon Cozens, in the initial commit that added Anton SC to google/fonts (commit `7023dbc93`, 2024-05-27). The commit message explicitly states: "Taken from the upstream repo https://github.com/googlefonts/AntonFont at commit ...". The URL is confirmed valid. This is the same upstream repo used by the regular "Anton" family.

## How Commit Identified

The commit `beb92fcad87808357123bb66881b4032dc96efe7` ("Fix weight axis", by Simon Cozens, 2024-04-04) was set by the onboarder in the original commit to google/fonts. The commit message in google/fonts explicitly references it. This is the **only commit** in the upstream repository -- the repo appears to have been force-pushed/reset at some point, so there is no older history.

The same commit is referenced by both the regular "Anton" family and "Anton SC" in google/fonts. The regular Anton was previously onboarded from a different commit (`80d01123`), which no longer exists in the repo history due to the force-push.

The PR #7770, merged by Viviana Monsalve on 2024-05-30, contains the original onboarding.

## How Config Resolved

The upstream repo has `sources/config.yaml` at the referenced commit, containing:

```yaml
sources:
  - Anton.glyphs
```

**Critical caveat**: This config only builds `Anton-Regular.ttf` (the regular Anton family). It does NOT produce `AntonSC-Regular.ttf`. The `AntonSC-Regular.ttf` binary was generated through a separate build process, likely by Simon Cozens during onboarding.

The `Anton.glyphs` source file does contain extensive small caps glyphs (1170+ `.sc` glyph references) and includes `c2sc` and `smcp` OpenType features. However, the existing `config.yaml` does not configure a separate SC output. To build `AntonSC-Regular.ttf` from `Anton.glyphs`, a separate config or build step would be needed that extracts the small caps into a standalone font.

The `config_yaml: "sources/config.yaml"` field was NOT set by the original onboarder -- it was added later by the batch 1/4 commit (`19cdcec5`, "[Batch 1/4] port info from fontc_crater targets list"). This is technically incorrect for Anton SC specifically, since that config only produces the regular Anton binary.

### File Mapping Issue

The METADATA.pb `source { files { } }` block references `fonts/ttf/AntonSC-Regular.ttf` as the `source_file`. This path **does not exist** in the upstream repo at any commit. The only font binary in the upstream repo at the referenced commit is `fonts/Anton-Regular.ttf`. The SC binary was generated externally and placed directly in google/fonts.

## Relationship to Regular Anton

Anton SC shares the same upstream repository (`googlefonts/AntonFont`) and the same commit hash as the regular "Anton" family in google/fonts. The difference is:

- **Anton** (`ofl/anton/`): Uses `fonts/Anton-Regular.ttf` from the upstream repo (file actually exists)
- **Anton SC** (`ofl/antonsc/`): Uses `AntonSC-Regular.ttf` which was built from the same `Anton.glyphs` source but does not exist in the upstream repo

## Conclusion

The repository URL and commit hash are correct -- this is where the source comes from. However, the `config_yaml` field pointing to `sources/config.yaml` is misleading for Anton SC, as that config only produces the regular Anton font, not the SC variant. The `source_file` path `fonts/ttf/AntonSC-Regular.ttf` in the files mapping is also incorrect (the file doesn't exist at that path in the repo).

For fontc_crater / gftools-builder purposes, building Anton SC from this config would require either:
1. A modified config.yaml that instructs the builder to produce the SC variant
2. Or recognition that this is a special case where the binary was generated through a custom build process

**Confidence**: HIGH for repository_url and commit. LOW for config_yaml accuracy (the config does not actually build AntonSC).
