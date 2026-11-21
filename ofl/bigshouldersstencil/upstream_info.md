# Investigation Report: Big Shoulders Stencil

- **Family name**: Big Shoulders Stencil
- **Slug**: bigshouldersstencil
- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Confidence**: HIGH

## METADATA.pb source block (current)

```
source {
  repository_url: "https://github.com/xotypeco/big_shoulders"
  commit: "8ba99c9e347396d828b263b8b818269cb99eb27c"
  config_yaml: "Big-Shoulders-Stencil/sources/config.yml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf"
    dest_file: "BigShouldersStencil[opsz,wght].ttf"
  }
  branch: "master"
}
```

## Upstream Repository

- **URL**: https://github.com/xotypeco/big_shoulders
- **Cached at**: upstream_repos/fontc_crater_cache/xotypeco/big_shoulders
- **Default branch**: master
- **Repository type**: Multi-family repo (Big Shoulders, Big Shoulders Inline, Big Shoulders Stencil share this repo)

## Commit Verification

- **Commit**: `8ba99c9e347396d828b263b8b818269cb99eb27c`
- **Date**: 2025-02-06
- **Author**: XO Type Co <info@xotype.co>
- **Message**: "Update README.md"
- **Is master HEAD**: Yes, this commit is the current HEAD of the master branch with no subsequent commits.
- **Binary match**: The font file `Big-Shoulders-Stencil/fonts/variable/BigShouldersStencil[opsz,wght].ttf` at this commit has SHA256 `758ec880296a8bdaf736a31fc57e90fa16673d8c357efc3c36bdb6582d625f0a`, which matches exactly the file in google/fonts.
- **DESCRIPTION.en_us.html match**: SHA256 matches exactly between upstream `Documentation/DESCRIPTION.en_us.html` and google/fonts copy.
- **OFL.txt**: Differs slightly. The google/fonts version had a post-onboarding edit by Emma Marichal (commit `f8206935e`, 2025-02-07) changing the SIL license URL from `http://scripts.sil.org/OFL` to `https://openfontlicense.org`.

## Config Verification

- **Config path**: `Big-Shoulders-Stencil/sources/config.yml`
- **Exists at commit**: Yes, confirmed present at `8ba99c9`.
- **Config format**: Valid gftools-builder YAML configuration.
- **Source file**: `BigShouldersStencil.glyphs`
- **Axis order**: opsz, wght
- **Settings**: autohintOTF disabled, STAT table defined for opsz (10pt, 72pt) and wght (Thin through Black).
- **No local override needed**: The upstream config is present and correctly referenced in METADATA.pb.

## google/fonts History

The family was onboarded on 2025-02-07 by Yanone (commit `3b113037a`):
- Commit message: "Big Shoulders Stencil: Version 2.001 added"
- Body: "Taken from the upstream repo https://github.com/xotypeco/big_shoulders at commit https://github.com/xotypeco/big_shoulders/commit/8ba99c9e347396d828b263b8b818269cb99eb27c. Resolves #7830"

Subsequent commits touching this family:
1. `754593c0e` (2025-02-07) - "Update METADATA.pb" by Yanone (added date field)
2. `f8206935e` (2025-02-07) - "Update OFL.txt - url link" by Emma Marichal (URL update)
3. `34926685b` (2026-02-16) - "Add config_yaml to METADATA.pb for 15 font families" by Felipe Sanches / Claude (added config_yaml field)

## Conclusion

The source block in METADATA.pb is **complete and correct**. The repository URL, commit hash, config_yaml path, file mappings, and branch are all verified. The commit hash `8ba99c9` was explicitly referenced in the onboarding commit message by Yanone and the binary font file matches byte-for-byte. The upstream config.yml exists at the referenced commit and is properly configured for gftools-builder. No changes needed.
