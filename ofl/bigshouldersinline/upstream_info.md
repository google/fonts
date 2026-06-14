# Investigation: Big Shoulders Inline

- **Family Name**: Big Shoulders Inline
- **Slug**: bigshouldersinline
- **Designer**: Patric King
- **Date Added**: 2025-02-06
- **Model**: Claude Opus 4.6

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders-Inline/sources/config.yml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Inline/fonts/variable/BigShouldersInline[opsz,wght].ttf"
    dest_file: "BigShouldersInline[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Repository Verification

- **Repository URL**: https://github.com/xotypeco/big_shoulders (multi-family repo)
- **Repository accessible**: Yes
- **Cached at**: upstream_repos/fontc_crater_cache/xotypeco/big_shoulders
- **Remote matches**: Yes (origin points to https://github.com/xotypeco/big_shoulders)
- **Default branch**: master

## Commit Verification

- **Referenced commit**: `8ba99c9e347396d828b263b8b818269cb99eb27c`
- **Commit exists**: Yes
- **Commit date**: 2025-02-06 10:26:42 -0600
- **Commit message**: "Update README.md"
- **Commit author**: XO Type Co (info@xotype.co)
- **Is tip of master**: Yes (no newer commits exist in the repo)

### Onboarding Provenance

The font was onboarded to google/fonts by Yanone (post@yanone.de) on 2025-02-07 in commit `99e4ad649`. The commit message explicitly stated: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c." It resolved issue #7830.

### Binary Verification

The font binary `Big-Shoulders-Inline/fonts/variable/BigShouldersInline[opsz,wght].ttf` at the referenced commit had a SHA-256 hash of `417c1d07898a6648faa9e3a95d7302aa44ee614e2236a2b336e16922569d1fa3`, which matched exactly the binary currently in google/fonts. This confirmed the commit hash was correct.

### Timeline Analysis

The referenced commit `8ba99c9` (2025-02-06) was a README update, but it was also the HEAD of master at the time of onboarding. Prior commits by Yanone on the same day (2025-02-06) included source fixes (interpolation issues, Eturned additions, new binaries). The last commit that modified the Inline font binary was `0b3d09a` (2024-02-26, "regenerate font files"), which predated the referenced commit. No commits existed after `8ba99c9` in the repo.

## Config Verification

- **config_yaml in METADATA.pb**: `Big-Shoulders-Inline/sources/config.yml`
- **Config exists at referenced commit**: Yes
- **Override config.yaml in google/fonts**: No

### Config Contents

The config.yml referenced the Glyphs source `BigShouldersInline.glyphs` with:
- `familyName: Big Shoulders Inline`
- `autohintOTF: false`
- Axis order: opsz, wght
- STAT table definitions for optical size (10pt, 72pt) and weight (Thin through Black, 100-900)

The source file `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs` was confirmed to exist at the referenced commit.

## Source Files

The upstream repo contained the following structure for Big Shoulders Inline at the referenced commit:
- `Big-Shoulders-Inline/sources/BigShouldersInline.glyphs` (primary source)
- `Big-Shoulders-Inline/sources/config.yml` (gftools-builder config)
- `Big-Shoulders-Inline/fonts/variable/BigShouldersInline[opsz,wght].ttf` (pre-built binary)

## google/fonts Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `34926685b` | 2026-02-16 | Added config_yaml to METADATA.pb (batch of 15 families) |
| `f4fbbeaf1` | 2025-02-07 | Updated METADATA.pb - date added |
| `9201361a5` | 2025-02-07 | Updated OFL.txt - url link |
| `25199ad5e` | 2025-02-07 | Updated METADATA.pb |
| `99e4ad649` | 2025-02-07 | Big Shoulders Inline: Version 2.002 added (initial onboarding) |

## Assessment

- **Status**: complete
- **Confidence**: HIGH
- **Repository URL**: Verified correct
- **Commit hash**: Verified correct (explicitly referenced in onboarding commit, binary hash matched)
- **Config**: Verified correct (exists at the specified path in the referenced commit)
- **Branch**: Verified correct (master is the default and only branch)

All metadata fields were present and verified. The source block was complete with repository URL, commit hash, config_yaml path, file mappings, and branch. No corrections were needed.
