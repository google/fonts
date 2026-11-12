# Big Shoulders

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Family slug**: bigshoulders
- **Family directory**: ofl/bigshoulders
- **Designer**: Patric King
- **Status**: complete
- **Confidence**: HIGH

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders/sources/config.yml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders/fonts/variable/BigShoulders[opsz,wght].ttf"
    dest_file: "BigShoulders[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Repository

- **URL**: https://github.com/xotypeco/big_shoulders
- **Cached at**: upstream_repos/fontc_crater_cache/xotypeco/big_shoulders
- **Cache status**: Clean (HEAD detached at 0b3d09a), no local modifications
- **Remote verified**: origin points to https://github.com/xotypeco/big_shoulders

## Commit Verification

- **Referenced commit**: `8ba99c9e347396d828b263b8b818269cb99eb27c`
- **Commit message**: "Update README.md"
- **Commit author**: XO Type Co <info@xotype.co>
- **Commit date**: 2025-02-06
- **Exists in repo**: Yes
- **Is HEAD of master**: Yes -- no newer commits exist after this one

The commit was verified as the correct onboarding commit. The google/fonts commit `7f99323` by Yanone (2025-02-07) explicitly stated: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c." This was merged via PR #9027 on 2025-02-12.

### Binary File Verification

The font binary `BigShoulders[opsz,wght].ttf` in google/fonts was confirmed to be identical to the file at the referenced commit in the upstream repository. Both files produced the same SHA-256 hash: `4b4b24aa6f799aa73cdcd5b6fa840cbcbbb38b81fa9fa82c25126a4530c1ba44`.

## Config Verification

- **config_yaml field**: `Big-Shoulders/sources/config.yml`
- **File exists at referenced commit**: Yes
- **Override config.yaml in google/fonts**: No (not needed; upstream has one)

The `config.yml` file at `Big-Shoulders/sources/config.yml` was present at the referenced commit and contained valid gftools-builder configuration. It referenced `BigShoulders.glyphs` as the source, with `opsz` and `wght` axis order, and a full STAT table definition.

The source directory at the referenced commit also contained:
- `BigShoulders.glyphs` -- the Glyphs source file
- `BigS-vf-Display.yml` and `BigS-vf-Text.yml` -- additional config variants
- `build-B.sh` -- a build script

## File Mappings

All three file mappings in the source block were verified to exist at the referenced commit:
- `OFL.txt` -> `OFL.txt`
- `Documentation/DESCRIPTION.en_us.html` -> `DESCRIPTION.en_us.html`
- `Big-Shoulders/fonts/variable/BigShoulders[opsz,wght].ttf` -> `BigShoulders[opsz,wght].ttf`

## Google Fonts History

The Big Shoulders family was added to google/fonts on 2025-02-07 (date_added: 2025-02-06 in METADATA.pb) in commit `7f99323` by Yanone, resolving issue #7830. It was merged via PR #9027 on 2025-02-12.

The `config_yaml` field was added later in commit `3492668` (2026-02-16) as part of a batch update for 15 font families.

### Related Families

The upstream repository `xotypeco/big_shoulders` contains sources for multiple Big Shoulders variants:
- Big Shoulders (this family) -- `Big-Shoulders/`
- Big Shoulders Inline -- `Big-Shoulders-Inline/`
- Big Shoulders Stencil -- `Big-Shoulders-Stencil/`

All three were onboarded to google/fonts on the same day by Yanone.

## Conclusion

The source block in METADATA.pb was complete and correct. The repository URL, commit hash, config_yaml path, file mappings, and branch were all verified. The binary font file matched exactly between google/fonts and the upstream repository at the referenced commit. No changes were needed.
