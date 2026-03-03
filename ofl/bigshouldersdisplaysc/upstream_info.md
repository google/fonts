# Investigation Report: Big Shoulders Display SC

- **Family name**: Big Shoulders Display SC
- **Slug**: bigshouldersdisplaysc
- **Family dir**: ofl/bigshouldersdisplaysc
- **Model**: Claude Opus 4.6
- **Date**: 2026-03-03

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "0b3d09a86862b19efae28eae0cd868f17c476b20"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders/fonts/variable/display/BigShouldersDisplaySC[wght].ttf"
    dest_file: "BigShouldersDisplaySC[wght].ttf"
  }
  branch: "master"
}
```

## Repository

- **URL**: https://github.com/xotypeco/big_shoulders
- **Cached at**: upstream_repos/fontc_crater_cache/xotypeco/big_shoulders
- **Remote verified**: Yes, remote URL matches expected repository

## Commit Verification

- **Referenced commit**: `0b3d09a86862b19efae28eae0cd868f17c476b20`
- **Commit date**: 2024-02-26
- **Commit message**: "regenerate font files"
- **Author**: XO Type Co <info@xotype.co>
- **Exists in repo**: Yes
- **Branch**: master (commit is an ancestor of master)

The commit was a large regeneration of font binaries across the entire Big Shoulders superfamily (Big Shoulders, Inline, and Stencil variants). It regenerated OTF, TTF, and variable font files for all sub-families.

### Commit Hash Cross-Verification

The commit hash `0b3d09a` was explicitly referenced in:
- The google/fonts commit message for `203560305` ("Taken from the upstream repo ... at commit ...0b3d09a...")
- The PR #7783 body (same text)

The PR was authored by Simon Cozens and merged on 2024-06-25 by Emma Marichal. The commit predated the PR merge by approximately 4 months, which was expected for an onboarding workflow.

**Note on master HEAD**: Master has moved beyond `0b3d09a` with 14 additional commits (as of the cache state). The latest upstream work (from early 2025) included interpolation fixes, Eturned glyph additions, line height adjustments, and VF renaming. These changes have NOT been incorporated into Google Fonts and would require a separate update process.

## Source Files

At commit `0b3d09a`, the relevant source file was:
- `Big-Shoulders/sources/BigShoulders.glyphs` -- the primary Glyphs source for the entire Big Shoulders superfamily

The upstream repo did NOT contain a `BigShouldersDisplaySC[wght].ttf` pre-built binary at this commit. The `Big-Shoulders/fonts/variable/display/` directory only contained:
- `BigShouldersDisplay[wght].ttf` (the non-SC variant)
- `BigShoulders[opsz,wght].ttf.stat.yaml`

The Display SC variant was produced at onboarding time using the override config.yaml, NOT copied from the upstream repo. Despite what the METADATA.pb `files` mapping suggests (`source_file: "Big-Shoulders/fonts/variable/display/BigShouldersDisplaySC[wght].ttf"`), this file did not exist in the upstream repo at the referenced commit. The file mapping in METADATA.pb appears to be a leftover from gftools-packager's template generation and does not reflect reality.

## Build Configuration

### Upstream config.yml (NOT config.yaml)

The upstream repo contained a `Big-Shoulders/sources/config.yml` (note: `.yml` extension, not `.yaml`) which was a gftools-builder v1 configuration. It only built the main `BigShoulders[opsz,wght].ttf` variable font and did NOT produce the Display SC variant. The config included STAT table definitions for opsz and wght axes but had no small caps or display-specific subsetting logic.

### Override config.yaml in google/fonts (EXISTS)

A local override `config.yaml` existed in the google/fonts family directory at `ofl/bigshouldersdisplaysc/config.yaml`. This override was part of the original onboarding commit (`203560305`), meaning it was created by Simon Cozens when adding the family.

The override config.yaml contained a gftools-builder recipe that:
1. Built from `Big-Shoulders/sources/BigShoulders.glyphs` (using `../` relative paths to the upstream repo root)
2. Created `BigShouldersDisplay[wght].ttf` by subsetting `opsz=72` from the full opsz+wght design space
3. Created `BigShouldersDisplaySC[wght].ttf` by additionally remapping the `smcp` feature to `ccmp` (making small caps the default)
4. Renamed both variants to their respective family names
5. Applied fix operations and STAT table postprocessing

This was a custom build pipeline created specifically for onboarding; the upstream repo had no equivalent build process for the Display SC variant.

### config_yaml Field in METADATA.pb

The `config_yaml` field was correctly omitted from the METADATA.pb `source {}` block. Since the override config.yaml existed locally in the google/fonts family directory, the google-fonts-sources tool would auto-detect it.

## Google Fonts Git History

The family was added and subsequently modified in four commits:

1. `203560305` (2024-05-30) -- "Big Shoulders Display SC: Version 2.002 added" by Simon Cozens
   - Initial addition with font binary, METADATA.pb, DESCRIPTION, OFL.txt, and config.yaml
2. `b74efaa4c` (2024-05-30) -- "Add SC reference to description" by Simon Cozens
   - Added SC-specific text to DESCRIPTION.en_us.html
3. `fb7593001` (2024-06-21) -- "Update DESCRIPTION.en_us.html - space" by Emma Marichal
   - Minor whitespace fix
4. `177fc4c54` (2024-06-21) -- "Update OFL.txt" by Emma Marichal
   - License text update

All were part of or related to PR #7783 (`google/gftools_packager_ofl_bigshouldersdisplaysc`).

## File Mapping Issue

The METADATA.pb `files` block contains a mapping for `BigShouldersDisplaySC[wght].ttf` claiming it comes from `Big-Shoulders/fonts/variable/display/BigShouldersDisplaySC[wght].ttf` in the upstream repo. However, this file never existed at the referenced commit (or in the upstream repo at all -- the repo only ever had a `BigShouldersDisplaySC` file at commit `b16b16d` which came much later in 2025). The binary was produced by the override config.yaml at build time. This is a minor metadata inconsistency but does not affect functionality since the override config.yaml handles the actual build.

## Assessment

- **Status**: complete
- **Repository URL**: Correct (https://github.com/xotypeco/big_shoulders)
- **Commit hash**: Correct (`0b3d09a86862b19efae28eae0cd868f17c476b20`)
- **Config**: Override config.yaml in google/fonts (correctly present, config_yaml omitted from METADATA.pb)
- **Confidence**: HIGH

The source block was well-configured at onboarding. The repository URL, commit hash, and override config.yaml were all correctly set up by Simon Cozens in PR #7783. The only minor issue was the phantom file mapping for the DisplaySC TTF in the `files` block, which referenced a path that did not exist in the upstream repo -- but this did not impact build correctness since the override config.yaml handled font generation.

No changes are needed to the METADATA.pb source block or the override config.yaml.
