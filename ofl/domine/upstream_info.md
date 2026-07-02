# Domine

## Summary

Domine is a variable serif font by Impallari Type. It has complete source documentation in METADATA.pb with repository URL, commit hash, and config.yaml path.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Domine |
| **Designer** | Impallari Type |
| **License** | OFL |
| **Date Added** | 2012-11-30 |
| **Repository URL** | https://github.com/googlefonts/Domine |
| **Commit Hash** | `2974ac627aad3a34190288c07fd0a0040d38550f` |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |

## Investigation Details

### Onboarding History

Domine was originally added to Google Fonts in the initial commit (`90abd17b4`) as a static font. It was updated to v2.000 (variable font) in PR #2492 (commit `2194d6669`) by Marc Foley on 2020-06-10. The PR commit message states: "Taken from the upstream repo https://github.com/TypeNetwork/Domine at commit https://github.com/TypeNetwork/Domine/commit/a1676d0478fa24f63f45474091258008698bdf5f".

The source block was later populated in the batch port from fontc_crater targets list (commit `19cdcec59`).

### Upstream Repository

The upstream repo at https://github.com/googlefonts/Domine contains:
- `sources/Domine.designspace` - the designspace source
- `sources/Domine-Regular.ufo` and `sources/Domine-Bold.ufo` - UFO sources
- `sources/config.yaml` - gftools-builder configuration
- `fonts/` - compiled font files

The repo appears to be a fork/mirror maintained by googlefonts. The original v2 sources were at TypeNetwork/Domine.

### Commit Verification

The commit `2974ac6` in METADATA.pb is the HEAD (and only commit visible in the shallow clone) of the googlefonts/Domine repo. It adds the `sources/config.yaml` file. This is the commit used in fontc_crater targets.

### Config YAML

The `sources/config.yaml` contains:
```yaml
sources:
  - Domine.designspace
```

No override config.yaml exists in the google/fonts family directory.

## Conclusion

Domine is fully documented with all required metadata. The source block is complete with repository URL, commit hash, and config.yaml path pointing to a valid gftools-builder configuration in the upstream repo.
