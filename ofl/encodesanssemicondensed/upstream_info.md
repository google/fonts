# Investigation Report: Encode Sans Semi Condensed

## Family Details
- **Family name**: Encode Sans Semi Condensed
- **Designer**: Impallari Type, Andres Torresi, Jacques Le Bailly
- **License**: OFL
- **Category**: SANS_SERIF
- **Date added**: 2017-02-08
- **METADATA.pb path**: `ofl/encodesanssemicondensed/METADATA.pb`

## Source Repository
- **Repository URL**: https://github.com/impallari/Encode-Sans
- **Verified**: Yes (HTTP 200, matches METADATA.pb `repository_url`)
- **Upstream cache**: `impallari/Encode-Sans`

## Upstream Repository Details

The upstream repository (`impallari/Encode-Sans`) is the original Encode Sans project by Pablo Impallari. It contains a single `.glyphs` source file (`sources/Encode-Sans.glyphs`) that defines the entire Encode Sans superfamily: all 5 width variants (Condensed, Semi Condensed, Normal, Semi Expanded, Expanded) with 9 weight instances each, for a total of 45 static font files.

The `.glyphs` file has 4 masters arranged on 2 axes:
- **Weight axis**: Light (weightValue=34) and Bold (weightValue=193/232)
- **Width axis**: Condensed (widthValue=0) and Extended (widthValue=1000)

The Semi Condensed instances are interpolated from these 4 masters, with the `familyName` custom parameter set to "Encode Sans SemiCondensed".

### Source Files
- **Primary source**: `sources/Encode-Sans.glyphs` (GlyphsApp format)
- **No `.designspace`, `.ufo`, or `.sfd` files**
- **No `config.yaml` or `config.yml`** in the upstream repository
- **Pre-built binaries**: `fonts/EncodeSansSemiCondensed-*.ttf` (9 files)

### Commit Analysis
- **Last commit (HEAD)**: `370cdccdb22daf862c6fca0636aad64b6835decd` (2017-02-03) - "Merge pull request #3 from m4rc1e/master" (Changed thin weight from 100 to 250)
- **Branch**: `master`
- **Repo status**: Clean, up to date with origin

The upstream repo's full commit timeline relevant to onboarding:

| Commit | Date | Description |
|--------|------|-------------|
| `97a5aec` | 2017-01-03 | "sources \| fonts: updated font names and regenerated fonts" |
| `2fdfa4a` | 2017-01-27 | Merge pull request #2 from m4rc1e/master |
| `fc35928` | 2017-01-30 | "fonts \| sources: Cahnged thing weight to 250." |
| `370cdcc` | 2017-02-03 | Merge pull request #3 from m4rc1e/master (tip) |

## Onboarding History

### google/fonts commit history for `ofl/encodesanssemicondensed/`:
1. `3e6ebfc03` (2017-02-07) - "encodesanssemicondensed: v2.000 added (#628)" by Marc Foley -- Initial onboarding
2. `c19f2d37a` (2017-10-15) - "Fix mode of non-executable files" by Dave Crossland -- OFL.txt permissions fix
3. `633ebadbf` (2021-12-12) - "Add language support metadata to all METADATA.pb files (#4160)" -- Metadata update
4. `c8a4f8556` (2024-01-14) - "More upstreams (e,f)" by Simon Cozens -- Added `source { repository_url }` to METADATA.pb

### PR #628 (onboarding)
- **Author**: Marc Foley (m4rc1e)
- **Created**: 2017-02-03
- **Merged**: 2017-02-07
- **Title**: "encodesanssemicondensed: v2.000 added"
- **Body**: "This complies with our Font Bakery Discussion, https://github.com/googlefonts/fontbakery/issues/1211 -- Family name is Encode Sans Semi Condensed."
- **Context**: Part of a batch of 5 PRs (#625-#629) that added all Encode Sans v2 width variants simultaneously (Condensed, Expanded, Semi Condensed, Semi Expanded, and the Normal width update)

The FontBakery issue #1211 was about how to properly name superfamily width variants (e.g., "Encode Sans Semi Condensed" as a separate family name).

### Binary Verification

Font file sizes do **not** match exactly between google/fonts and any upstream commit:

| File | google/fonts | Upstream tip (370cdcc) | Upstream pre-PR3 (2fdfa4a) |
|------|-------------|----------------------|---------------------------|
| Black.ttf | 167,572 | 167,564 | 167,568 |
| Bold.ttf | 168,628 | 168,620 | 168,620 |
| ExtraBold.ttf | 170,384 | 170,380 | 170,376 |
| ExtraLight.ttf | 166,556 | 166,544 | 166,564 |
| Light.ttf | 168,296 | 168,288 | 168,304 |
| Medium.ttf | 168,888 | 168,840 | 168,840 |
| Regular.ttf | 170,864 | 170,856 | 170,856 |
| SemiBold.ttf | 171,072 | 171,064 | 171,072 |
| Thin.ttf | 162,164 | 162,156 | 162,180 |

The sizes are very close but not identical, differing by 4-48 bytes. This strongly suggests Marc Foley re-compiled the fonts from the `.glyphs` source (possibly with slightly different fontmake/toolchain settings) rather than copying the pre-built binaries from the upstream repo. This was common practice in early onboarding work.

Since the PR was created on 2017-02-03 (the same day as the tip commit `370cdcc`), and the fonts were re-compiled rather than copied, the most likely scenario is that Marc Foley compiled from the state of the source at or near the tip commit.

## How Commit Hash Was Identified

The commit `370cdccdb22daf862c6fca0636aad64b6835decd` is the HEAD of the `master` branch and the last commit in the repo. It was authored on 2017-02-03, the same day PR #628 was created in google/fonts. There are no commits after this date.

Since binary files don't match exactly (the onboarder likely re-compiled from source), the timeline alignment is the primary evidence:
- The upstream tip commit `370cdcc` was merged on 2017-02-03
- PR #628 was created on 2017-02-03 and merged on 2017-02-07
- Marc Foley authored both the upstream PR #3 (the tip commit) and the google/fonts PR #628

This strongly indicates `370cdcc` is the correct onboarding commit.

## Config.yaml Status

### Upstream repo
- **No `config.yaml` found** in the upstream repository
- Fonts were built using fontmake from the `.glyphs` source, but no build configuration file exists

### google/fonts family directory
- **No `config.yaml`** in `ofl/encodesanssemicondensed/`

### Config.yaml Feasibility

The upstream `.glyphs` source (`sources/Encode-Sans.glyphs`) is a multi-axis source that produces 5 separate font families (one per width). A gftools-builder `config.yaml` could be created to build all families from this source. The Semi Condensed family's instances are defined within the `.glyphs` file with the `familyName` custom parameter set to "Encode Sans SemiCondensed".

A minimal override config.yaml could be:

```yaml
sources:
  - sources/Encode-Sans.glyphs
```

However, note that this single source generates all 5 width families (45 fonts total). The gftools-builder would need to handle the instance filtering/separation, or a more specific configuration might be needed.

**Important note**: The main "Encode Sans" family (`ofl/encodesans/`) was later upgraded to a variable font in 2020 using Stephen Nixon's fork (`thundernixon/Encode-Sans`). The Semi Condensed variant remains as static fonts from the original `impallari/Encode-Sans` repo and has not been updated to a variable font.

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/impallari/Encode-Sans"
}
```

## Recommended METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/impallari/Encode-Sans"
  commit: "370cdccdb22daf862c6fca0636aad64b6835decd"
}
```

Note: `config_yaml` is omitted. An override `config.yaml` could potentially be created in the google/fonts family directory, but the single `.glyphs` source generates all 5 width families, so the config would need careful consideration.

## Related Families

This font is part of the Encode Sans superfamily. The width variants in google/fonts are:

| Family | METADATA.pb path | Repository | Status |
|--------|-----------------|------------|--------|
| Encode Sans | `ofl/encodesans/` | `thundernixon/Encode-Sans` | Variable font (v3, 2020) |
| Encode Sans Condensed | `ofl/encodesanscondensed/` | `impallari/Encode-Sans` | Static (v2, 2017) |
| Encode Sans Expanded | `ofl/encodesansexpanded/` | `impallari/Encode-Sans` | Static (v2, 2017) |
| Encode Sans SC | `ofl/encodesanssc/` | `thundernixon/Encode-Sans` | Variable font (v3, 2020) |
| Encode Sans Semi Condensed | `ofl/encodesanssemicondensed/` | `impallari/Encode-Sans` | Static (v2, 2017) |
| Encode Sans Semi Expanded | `ofl/encodesanssemiexpanded/` | `impallari/Encode-Sans` | Static (v2, 2017) |

The static width variants (Condensed, Semi Condensed, Semi Expanded, Expanded) all come from the original `impallari/Encode-Sans` repo and were onboarded in PRs #625-#629. The main "Encode Sans" and "Encode Sans SC" were later upgraded to variable fonts from Stephen Nixon's fork.

## Summary
- **Status**: missing_config
- **Repository URL**: Correct, verified (https://github.com/impallari/Encode-Sans)
- **Commit hash**: `370cdcc` (HIGH confidence -- repo tip, authored same day as google/fonts PR by the same person)
- **Config.yaml**: Not available in upstream or google/fonts; override could be created
- **Action needed**: Add `commit` field to source block in METADATA.pb. Consider creating an override config.yaml.

## Confidence

**HIGH** -- The repository URL is correct and already present in METADATA.pb. The commit hash `370cdcc` is the HEAD of the upstream repo's master branch, authored by Marc Foley on the same day he created the google/fonts onboarding PR #628. Although binary files don't match exactly (common with re-compilation), the timeline alignment and authorship evidence are strong. There are no commits in the upstream repo after this date.
