# Baloo 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Ek Type

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| Repository URL   | https://github.com/yanone/Baloo2-Variable                         |
| Commit           | `da523dfa21aa0e376253d61c21e39146dc55702a`                         |
| Config YAML      | `builder/Baloo2.yaml`                                              |
| Branch           | `master`                                                           |

## Investigation

### Repository URL

The METADATA.pb `source` block listed `https://github.com/yanone/Baloo2-Variable` as the repository URL. This is Yanone's fork of the original EkType repository. The original repository is at `https://github.com/EkType/Baloo2-Variable`, as reflected in the copyright string in the font file and in METADATA.pb. Both repositories contain the referenced commit `da523dfa`.

The repository URL was originally set to `https://github.com/EkType/Baloo2-Variable` but was corrected to `https://github.com/yanone/Baloo2-Variable` in commit `a56c2bf3b` (2025-09-24) by Felipe Sanches ("sources info for Baloo 2: Version 1.700 (#3981)"). The yanone fork is the correct URL because it was the repository explicitly referenced by gftools-packager in PR #3981.

### Commit Verification

The commit `da523dfa21aa0e376253d61c21e39146dc55702a` was dated 2021-10-28 17:08:59 +0200 and had the message "Update BalooTammudu2[wght].ttf". This commit did not directly modify `Baloo2[wght].ttf` -- the last commit to touch that file was `e3d7aa54` ("Update Baloo2[wght].ttf", 2021-10-28 16:10:44 +0200), about one hour earlier the same day.

This is expected behavior for gftools-packager: since the yanone/Baloo2-Variable repository is a multi-family repository containing Baloo2, BalooBhai2, BalooBhaijaan2, BalooBhaina2, BalooChettan2, BalooDa2, BalooPaaji2, BalooTamma2, BalooTammudu2, and BalooThambi2, the packager referenced the latest commit at the time of packaging (`da523dfa`), which was the most recent update across all families in the batch.

Binary verification confirmed an exact match. The `Baloo2[wght].ttf` file at commit `da523dfa` in the upstream repo has SHA-256 hash `d47a6852548059b1db49a1319d06d499d546c3fa2237cf9eee9c43c8abb025c2`, which is identical to the file in `ofl/baloo2/` in google/fonts. File size also matched: 683,200 bytes in both locations.

The commit predated the google/fonts PR #3981 merge date (2021-11-25), confirming it was a valid reference point. The PR was created on 2021-10-29 and merged on 2021-11-25 by Yanone.

### Config YAML

The config file `builder/Baloo2.yaml` existed at the referenced commit and contained valid gftools-builder configuration:

```yaml
sources:
  - ../sources/Baloo2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/Baloo2.glyphs` was verified to exist at the referenced commit. No local override `config.yaml` was present in the google/fonts family directory, which is correct since the upstream config is available and valid.

### Google Fonts History

- `ee334a51f` - "baloo2: v1.640 added" (earlier static version)
- `8e0cd0588` - "Baloo 2: Version 1.700 added (#3981)" (2021-11-25) - the variable font onboarding commit by Yanone, which replaced 5 static weights with the variable font `Baloo2[wght].ttf`
- `a56c2bf3b` - "sources info for Baloo 2: Version 1.700 (#3981)" (2025-09-24) - added commit hash, corrected repository URL from EkType to yanone, and added config_yaml path

## Conclusion

All source metadata for Baloo 2 was verified and found to be correct. The repository URL points to Yanone's fork which was the actual source used for onboarding. The commit hash matches the gftools-packager reference and the binary file is an exact match. The config file exists at the specified path in the upstream repo with valid gftools-builder configuration. No changes are needed.
